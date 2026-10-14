"""Vehicle cutouts: lift the vehicle off its photo background and re-stage it on a
plain Stone studio backdrop with a ground shadow, framed the same way every time.

    python scripts/cutouts.py tucson-pink-front work/cargo-van-construction-side ...

Source: the full-resolution original from the client's Drive folder when
scripts/cutout_sources.json maps the photo to one (5712 px HEIC, far finer edges),
otherwise public/assets/<name>.jpg. Output: public/assets/cutout/<basename>{,-800}.{jpg,webp}
at 4:3 (the card frame), rendered at 2x and downsampled.

Pipeline: BiRefNet mask -> keep the vehicle only -> edge tightened to a crisp line and
grass trimmed at the tyres -> background colour removed from the edge pixels -> light colour grade
-> studio backdrop, under-body shadow and tyre contact shadows -> sharpen.
Masks are cached in .cutout-cache/ (git-ignored); delete one to recompute it.
Runs fully offline (rembg, pymatting, OpenCV).
"""
import json
import os
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
from scipy import ndimage

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "public" / "assets"
OUT = ASSETS / "cutout"
CACHE = ROOT / ".cutout-cache"
DRIVE = Path(os.environ.get("HW_DRIVE", "G:/My Drive/Hermes Wraps"))
SOURCES = json.loads((Path(__file__).parent / "cutout_sources.json").read_text())

W, H = 1600, 1200          # 4:3, matches the card .media frame
SS = 2                     # render at 2x, then downsample
WORK = 2400                # long side the photo is processed at
STONE = (236, 230, 220)    # --hw-stone
IVORY = (247, 244, 236)    # --hw-ivory
GROUND = 0.84              # tyres sit at 84% of the frame height
MAX_W, MAX_H = 0.84, 0.68  # largest share of the frame the vehicle may fill
MODEL = "birefnet-general"
# Photos where a neighbouring vehicle touches the subject need a harder split.
SPLIT = {"corvette-front": 40}
# A red car parked behind sits on the roofline: drop strong reds in the top quarter.
DROP_RED_TOP = {"corvette-front"}
# Tyres whose foot is hidden in tall grass: the tyre's outline as an ellipse
# ((cx, cy), (w, h), angle) in WORK-size source pixels. Inside the rubber ring the
# silhouette is completed and grass blades are repainted in the tyre's own tone.
TYRES = {"tucson-pink-front": [((996, 1529), (310, 462), 4)]}
# Dark glossy bodies mirror the sky along their outline and fade into a light backdrop:
# burn the inner rim back down: (strength 0..1, rim width as a share of the photo).
EDGE_BURN = {"cargo-van-construction-side": (0.7, 0.03)}
# Hand-traced lower edge (x, y) in WORK-size source pixels where grass blades cross a
# bumper lip: nothing below the line is kept.
BOTTOM_CLIP = {"tucson-pink-front": [(40, 1452), (100, 1490), (200, 1558), (300, 1620), (350, 1648),
                                     (425, 1670), (500, 1680), (600, 1686), (700, 1686), (780, 1674), (800, 1666)]}


def load_source(name: str) -> Image.Image:
    orig = SOURCES.get(name)
    if orig and (DRIVE / orig).exists():
        if orig.lower().endswith(".heic"):
            import pillow_heif
            pillow_heif.register_heif_opener()
        im = ImageOps.exif_transpose(Image.open(DRIVE / orig)).convert("RGB")
    else:
        im = Image.open(ASSETS / f"{name}.jpg").convert("RGB")
    s = WORK / max(im.size)
    if s < 1:
        im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    return im


def mask_for(name: str, src: Image.Image) -> np.ndarray:
    cached = CACHE / f"{name.replace('/', '__')}.{MODEL}.png"
    if cached.exists():
        m = Image.open(cached).convert("L")
        if m.size == src.size:
            return np.asarray(m, dtype=np.float32) / 255
    from rembg import new_session, remove
    m = remove(src, session=new_session(MODEL), only_mask=True)
    CACHE.mkdir(exist_ok=True)
    m.save(cached)
    return np.asarray(m, dtype=np.float32) / 255


def keep_vehicle(a: np.ndarray, src: Image.Image, base: str) -> np.ndarray:
    """Largest blob only (a car parked behind is dropped), glass holes closed."""
    if base in DROP_RED_TOP:
        rgb = np.asarray(src).astype(int)
        rows = np.where((a > 0.5).any(axis=1))[0]
        top = rows[0] + (rows[-1] - rows[0]) // 3
        r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
        red = ndimage.binary_dilation((r > 80) & (r > g * 1.35) & (r > b * 1.35), iterations=10)
        red[top:] = False
        a = np.where(red, 0, a)
    split = SPLIT.get(base, 12)
    solid = a > 0.5
    core = ndimage.binary_erosion(solid, iterations=split)
    labels, n = ndimage.label(core)
    if n > 1:
        sizes = ndimage.sum(core, labels, range(1, n + 1))
        core = labels == (int(np.argmax(sizes)) + 1)
    keep = ndimage.binary_dilation(core, iterations=split + 2) & solid
    keep = ndimage.binary_fill_holes(keep)
    band = ndimage.binary_dilation(keep, iterations=8)
    return np.where(keep, 1.0, np.where(band, a, 0.0)).astype(np.float32)


def smooth_bottom(alpha: np.ndarray, top: int, bot: int, base: str = "") -> np.ndarray:
    """Clean the lower silhouette: grass blades along bumper lips and the tyres' feet
    make that edge spiky. Take each column's lowest solid row, median-filter that
    profile and cut everything below it with a 1 px anti-aliased edge."""
    solid = alpha > 0.5
    has = solid.any(axis=0)
    hgt = solid.shape[0]
    bottom = (hgt - 1 - np.argmax(solid[::-1, :], axis=0)).astype(np.float32)
    cols = np.where(has)[0]
    k = max(9, int((cols[-1] - cols[0]) * 0.014) | 1)
    prof = bottom.copy()
    prof[cols] = ndimage.median_filter(bottom[cols], size=k, mode="nearest")
    prof[cols] = ndimage.gaussian_filter1d(prof[cols], k / 6)
    clip = BOTTOM_CLIP.get(base)
    if clip:
        xs = np.arange(clip[0][0], clip[-1][0] + 1)
        prof[xs] = np.minimum(prof[xs], np.interp(xs, *zip(*clip)))
    low = prof > top + (bot - top) * 0.55  # only the underside, not the roof or mirrors
    rows = np.arange(hgt, dtype=np.float32)[:, None]
    cut = np.clip(prof[None, :] - 1.5 - rows + 0.5, 0, 1)
    return np.where((has & low)[None, :], alpha * cut, alpha)


def mend_tyres(img: np.ndarray, a: np.ndarray, base: str) -> tuple[np.ndarray, np.ndarray]:
    for (cx, cy), (w, h), ang in TYRES.get(base, []):
        outer = np.zeros(a.shape, np.uint8)
        cv2.ellipse(outer, ((cx, cy), (w, h), ang), 1, -1)
        inner = np.zeros_like(outer)
        cv2.ellipse(inner, ((cx, cy), (w * 0.74, h * 0.74), ang), 1, -1)
        lower = np.arange(a.shape[0])[:, None] > cy
        ring = (outer > 0) & (inner == 0) & lower
        r, g, b = img[..., 0], img[..., 1], img[..., 2]
        grass = ring & (((g > r + 0.02) & (g > b + 0.02)) | (g > b + 0.04) | (a < 0.5))
        rubber = np.median(img[ring & ~grass & (a > 0.5)], axis=0)
        # Pale, sunlit blades on the grass side of the tyre (the lettering is on the other side).
        right = np.arange(a.shape[1])[None, :] > cx + w * 0.1
        grass |= ring & right & (img.mean(axis=2) > rubber.mean() * 1.6)
        grass = ndimage.binary_dilation(grass, iterations=1) & ring
        # Keep a little of the original light variation so the patch is not flat.
        lum = img.mean(axis=2, keepdims=True)
        tone = rubber * (0.85 + 0.3 * np.clip(lum / max(lum[ring].mean(), 1e-3), 0, 1.5) / 1.5)
        # Rubber grain, and a feathered blend so the patch has no hard rim.
        rng = np.random.default_rng(7)
        grain = cv2.GaussianBlur(rng.normal(0, 0.035, a.shape).astype(np.float32), (0, 0), 1.2)[..., None]
        tone = np.clip(tone * (1 + grain * 3), 0, 1)
        k = cv2.GaussianBlur(grass.astype(np.float32), (0, 0), 2.5)
        k = np.clip(np.maximum(k * 1.6, grass), 0, 1)[..., None] * ring[..., None]
        img = img * (1 - k) + tone * k
        a = np.where(outer > 0, np.maximum(a, (outer > 0) & lower), a).astype(np.float32)
    return img, a


def refine(a: np.ndarray, src: Image.Image, base: str = "") -> tuple[np.ndarray, np.ndarray]:
    img = np.asarray(src, dtype=np.float32) / 255
    img, a = mend_tyres(img, a, base)
    # Tighten the model's soft edge to a crisp 1-2 px anti-aliased line: a soft,
    # wide edge is what reads as a "hairy" halo once the background is gone.
    t = np.clip((a - 0.3) / 0.4, 0, 1)
    alpha = t * t * (3 - 2 * t)
    # Grass at the foot of the tyres: drop green pixels, but only on the outer rim of
    # the silhouette in the bottom band. Black bumpers and tyres reflect the grass, so a
    # deeper trim punches ragged holes into them.
    solid = alpha > 0.5
    hgt = solid.shape[0]
    rows = np.arange(hgt)[:, None]
    top_rows = np.where(solid.any(axis=1))[0]
    band = rows > top_rows[-1] - (top_rows[-1] - top_rows[0]) * 0.08
    rim = ndimage.distance_transform_edt(solid) < 6
    r, g, b = img[..., 0], img[..., 1], img[..., 2]
    green = (g > r + 0.03) & (g > b + 0.03)
    mended = np.zeros(solid.shape, np.uint8)
    for e in TYRES.get(base, []):
        cv2.ellipse(mended, e, 1, -1)
    alpha = np.where(band & rim & green & (mended == 0), 0.0, alpha)
    alpha = smooth_bottom(alpha, top_rows[0], top_rows[-1], base)
    alpha = cv2.GaussianBlur(alpha.astype(np.float32), (0, 0), 0.7)
    alpha = np.where(alpha < 0.04, 0.0, alpha)
    # Remove the background colour (grass, sky) that bleeds into the edge pixels.
    from pymatting import estimate_foreground_ml
    fg = estimate_foreground_ml(img.astype(np.float64), alpha.astype(np.float64))
    return np.clip(fg, 0, 1).astype(np.float32), alpha.astype(np.float32)


def burn_edge(fg: np.ndarray, alpha: np.ndarray, base: str) -> np.ndarray:
    if base not in EDGE_BURN:
        return fg
    s, w = EDGE_BURN[base]
    d = ndimage.distance_transform_edt(alpha > 0.5)
    width = max(alpha.shape) * w
    ramp = np.clip(1 - d / width, 0, 1) ** 1.5
    # Burn the bright reflections only; dark paint is already the right edge.
    lum = fg.mean(axis=2)
    k = s * ramp * np.clip((lum - 0.12) / 0.5, 0, 1)
    return fg * (1 - k[..., None] * 0.8)


def grade(fg: np.ndarray, alpha: np.ndarray) -> np.ndarray:
    """Gentle, consistent grade from the vehicle's own pixels: levels, vibrance."""
    sel = alpha > 0.9
    lo, hi = np.percentile(fg[sel], 0.4), np.percentile(fg[sel], 99.6)
    fg = np.clip((fg - lo) / max(hi - lo, 1e-3), 0, 1)
    im = Image.fromarray((fg * 255).astype(np.uint8))
    im = ImageEnhance.Color(im).enhance(1.06)
    im = ImageEnhance.Contrast(im).enhance(1.04)
    return np.asarray(im, dtype=np.float32) / 255


def backdrop(w: int, h: int, horizon: int) -> np.ndarray:
    """Studio cove: lit centre, wall fading into a slightly deeper floor."""
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    bg = np.empty((h, w, 3), np.float32)
    stone, ivory = np.array(STONE) / 255, np.array(IVORY) / 255
    t = np.clip((yy - horizon * 0.55) / (horizon * 0.9), 0, 1)[..., None]
    bg[:] = ivory * (1 - t) + stone * t
    floor = np.clip((yy - horizon) / (h - horizon), 0, 1)[..., None]
    bg *= 1 - 0.05 * floor
    r = np.hypot((xx - w / 2) / (w * 0.62), (yy - h * 0.48) / (h * 0.75))
    bg *= (1 - 0.06 * np.clip(r - 0.55, 0, 1))[..., None]
    return bg


def shadows(alpha: np.ndarray, x: int, y: int, w: int, h: int) -> np.ndarray:
    """Shadow strength map (0..1) on the canvas.

    The ground line is the lower convex hull of the vehicle's silhouette: it touches
    the tyres. Between the tyres the body sits above it, and that gap is the dark
    space under the car. Tyre contact points get a tight, darker shadow.
    """
    sh = np.zeros((h, w), np.float32)
    solid = alpha > 0.5
    cols = np.where(solid.any(axis=0))[0]
    bottom = solid.shape[0] - 1 - np.argmax(solid[::-1, :], axis=0)
    pts = [(int(c), int(bottom[c])) for c in cols[:: max(1, len(cols) // 400)]]
    hull = []  # lower hull in image coordinates (largest y)
    for p in pts:
        while len(hull) >= 2:
            (x1, y1), (x2, y2) = hull[-2], hull[-1]
            if (x2 - x1) * (p[1] - y1) - (y2 - y1) * (p[0] - x1) >= 0:
                hull.pop()
            else:
                break
        hull.append(p)
    hx = np.array([p[0] for p in hull], np.float32)
    hy = np.array([p[1] for p in hull], np.float32)
    ground = np.interp(cols, hx, hy)
    span = cols[-1] - cols[0]
    under = np.zeros_like(sh)
    contact = np.zeros_like(sh)
    for c, g in zip(cols, ground):
        b = bottom[c]
        gx, gy0, gy = x + c, y + int(b), y + int(g)
        if gy > gy0:  # gap between body and ground: shade it, darker toward the ground
            under[gy0:gy, gx] = np.linspace(0.45, 0.85, gy - gy0)
        if g - b < span * 0.012:  # tyre (or bumper) touching the ground line
            contact[gy - 6: gy + 2, gx] = 1.0
        under[gy - 2: gy + int(h * 0.006), gx] = 0.45
    under = cv2.GaussianBlur(under, (0, 0), h * 0.006)
    contact = cv2.GaussianBlur(contact, (0, 0), h * 0.003)
    # A broad, faint pool that grounds the whole vehicle.
    pool = np.zeros_like(sh)
    cx0, cx1 = x + cols[0], x + cols[-1]
    gy_mid = int(y + ground.max())
    cv2.ellipse(pool, ((cx0 + cx1) // 2, gy_mid - int(h * 0.016)), ((cx1 - cx0) // 2, int(h * 0.028)), 0, 0, 360, 0.22, -1)
    pool = cv2.GaussianBlur(pool, (0, 0), h * 0.022)
    return np.clip(np.maximum.reduce([under * 0.85, contact * 0.95, pool]), 0, 0.92)


def stage(name: str) -> None:
    base = name.split("/")[-1]
    src = load_source(name)
    a = keep_vehicle(mask_for(name, src), src, base)
    fg, alpha = refine(a, src, base)
    fg = grade(burn_edge(fg, alpha, base), alpha)

    ys, xs = np.where(alpha > 0.02)
    y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    fg, alpha = fg[y0:y1, x0:x1], alpha[y0:y1, x0:x1]

    cw, ch = W * SS, H * SS
    s = min(cw * MAX_W / fg.shape[1], ch * MAX_H / fg.shape[0])
    size = (round(fg.shape[1] * s), round(fg.shape[0] * s))
    fg = cv2.resize(fg, size, interpolation=cv2.INTER_AREA if s < 1 else cv2.INTER_CUBIC)
    alpha = np.clip(cv2.resize(alpha, size, interpolation=cv2.INTER_AREA if s < 1 else cv2.INTER_CUBIC), 0, 1)
    x, y = (cw - size[0]) // 2, round(ch * GROUND) - size[1]

    canvas = backdrop(cw, ch, round(ch * GROUND) - round(ch * 0.10))
    shade = shadows(alpha, x, y, cw, ch)
    # Multiply the shadow in, a touch warmer than neutral so it sits on Stone.
    canvas *= 1 - (shade * 0.62)[..., None] * np.array([1.0, 1.03, 1.07], np.float32)
    region = canvas[y:y + size[1], x:x + size[0]]
    region[:] = fg * alpha[..., None] + region * (1 - alpha[..., None])

    out = Image.fromarray((np.clip(canvas, 0, 1) * 255).astype(np.uint8)).resize((W, H), Image.LANCZOS)
    out = out.filter(ImageFilter.UnsharpMask(radius=1.1, percent=55, threshold=2))
    OUT.mkdir(exist_ok=True)
    small = out.resize((800, 600), Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=0.8, percent=40, threshold=2))
    for suffix, im in (("", out), ("-800", small)):
        im.save(OUT / f"{base}{suffix}.jpg", quality=88, optimize=True, progressive=True)
        im.save(OUT / f"{base}{suffix}.webp", quality=84, method=6)
    print("staged", base, flush=True)


if __name__ == "__main__":
    for n in sys.argv[1:]:
        stage(n)
