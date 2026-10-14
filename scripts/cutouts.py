"""Vehicle cutouts: remove the photo background and re-stage the vehicle on a
plain Stone backdrop with a soft ground shadow, framed the same way every time.

    python scripts/cutouts.py tucson-pink-front silverado-hood-angle work/cargo-van-construction-side

Reads public/assets/<name>.jpg and writes public/assets/cutout/<basename>{,-800}.{jpg,webp}
at 4:3 (the .type-card frame). Masks are cached in .cutout-cache/ (git-ignored) so
re-staging is fast; delete a mask to recompute it. Runs fully offline (rembg).
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy import ndimage

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "public" / "assets"
OUT = ASSETS / "cutout"
CACHE = ROOT / ".cutout-cache"

W, H = 1600, 1200          # 4:3, matches .type-card .media
STONE = (236, 230, 220)    # --hw-stone
GROUND = 0.86              # tyres sit at 86% of the frame height
MAX_W, MAX_H = 0.86, 0.72  # largest share of the frame the vehicle may fill
MODEL = "isnet-general-use"
# Photos where a neighbouring vehicle touches the subject need a harder split.
SPLIT = {"corvette-front": 40}
# Photos where a red car parked behind sits on the roofline: drop strong reds in the top quarter.
DROP_RED_TOP = {"corvette-front"}


def mask_for(name: str, src: Image.Image) -> Image.Image:
    cached = CACHE / f"{name.replace('/', '__')}.png"
    if cached.exists():
        return Image.open(cached).convert("L")
    from rembg import new_session, remove
    m = remove(src, session=new_session(MODEL), only_mask=True, post_process_mask=True)
    CACHE.mkdir(exist_ok=True)
    m.save(cached)
    return m


def clean(mask: Image.Image, split: int = 12) -> Image.Image:
    # Keep only the vehicle (largest blob) and close see-through holes in the glass.
    a = np.asarray(mask, dtype=np.uint8)
    solid = a > 128
    # Erode first so a neighbouring car that merely touches the vehicle separates.
    core = ndimage.binary_erosion(solid, iterations=split)
    labels, n = ndimage.label(core)
    if n > 1:
        sizes = ndimage.sum(core, labels, range(1, n + 1))
        core = labels == (int(np.argmax(sizes)) + 1)
    keep = ndimage.binary_dilation(core, iterations=split + 2) & solid
    keep = ndimage.binary_fill_holes(keep)
    near = ndimage.binary_dilation(keep, iterations=6)
    a = np.where(keep, 255, np.where(near, a, 0)).astype(np.uint8)
    return Image.fromarray(a, "L")


def ground_shadow(cmask: Image.Image, x: int, y: int) -> Image.Image:
    # Follow the vehicle's real underside: a tight contact line under every tyre
    # and bumper, plus a soft pool spreading just below it.
    a = np.asarray(cmask) > 128
    cols = np.where(a.any(axis=0))[0]
    bottom = a.shape[0] - 1 - np.argmax(a[::-1, :], axis=0)
    contact = Image.new("L", (W, H), 0)
    pool = Image.new("L", (W, H), 0)
    dc, dp = ImageDraw.Draw(contact), ImageDraw.Draw(pool)
    for c in cols:
        by = y + int(bottom[c])
        dc.line((x + c, by - 10, x + c, by + 4), fill=230)
        dp.line((x + c, by - 30, x + c, by + H * 0.045), fill=165)
    contact = contact.filter(ImageFilter.GaussianBlur(H * 0.006))
    pool = pool.filter(ImageFilter.GaussianBlur(H * 0.022))
    return Image.fromarray(np.maximum(np.asarray(contact), np.asarray(pool)), "L")


def backdrop() -> Image.Image:
    # Plain Stone, a touch lighter in the centre so the vehicle reads as lit.
    bg = Image.new("RGB", (W, H), STONE)
    glow = Image.new("L", (W, H), 0)
    ImageDraw.Draw(glow).ellipse((W * 0.1, H * 0.05, W * 0.9, H * 0.95), fill=70)
    glow = glow.filter(ImageFilter.GaussianBlur(H * 0.18))
    return Image.composite(Image.new("RGB", (W, H), (246, 242, 234)), bg, glow)


def stage(name: str) -> None:
    src = Image.open(ASSETS / f"{name}.jpg").convert("RGB")
    base = name.split("/")[-1]
    raw = mask_for(name, src)
    if base in DROP_RED_TOP:
        a, rgb = np.asarray(raw).copy(), np.asarray(src).astype(int)
        rows = np.where((a > 128).any(axis=1))[0]
        top = rows[0] + (rows[-1] - rows[0]) // 4
        r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
        red = (r > 90) & (r > g * 1.5) & (r > b * 1.5)
        red = ndimage.binary_dilation(red, iterations=4)
        red[top:] = False
        a[red] = 0
        raw = Image.fromarray(a, "L")
    mask = clean(raw, SPLIT.get(base, 12))
    box = mask.getbbox()
    car, cmask = src.crop(box), mask.crop(box)

    scale = min(W * MAX_W / car.width, H * MAX_H / car.height)
    size = (round(car.width * scale), round(car.height * scale))
    car, cmask = car.resize(size, Image.LANCZOS), cmask.resize(size, Image.LANCZOS)
    x, y = (W - size[0]) // 2, round(H * GROUND) - size[1]

    canvas = backdrop()
    shade = ground_shadow(cmask, x, y)
    canvas = Image.composite(Image.new("RGB", (W, H), (70, 58, 50)), canvas, shade)

    canvas.paste(car, (x, y), cmask)

    OUT.mkdir(exist_ok=True)
    for suffix, im in (("", canvas), ("-800", canvas.resize((800, 600), Image.LANCZOS))):
        im.save(OUT / f"{base}{suffix}.jpg", quality=84, optimize=True, progressive=True)
        im.save(OUT / f"{base}{suffix}.webp", quality=80, method=6)
    print("staged", base)


if __name__ == "__main__":
    for n in sys.argv[1:]:
        stage(n)
