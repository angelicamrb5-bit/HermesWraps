"""Light retouch of original catalog photos (no background removal).

The client asked for the real photos back, with simple edits that make the wrap
graphics stand out: a brighter centre on the vehicle, deeper shadows around the
edges, a little more contrast and crisp lettering. Nothing is added or removed.

Source: full-resolution originals on Drive (map in cutout_sources.json).
Output: public/assets/edit/<name>.jpg (1600 wide) and <name>-800.jpg, 4:3.
pages.py thumb() uses these for the catalog cards when they exist.

Run:  python scripts/enhance.py [name ...]
"""
import json, os, sys
import numpy as np
from PIL import Image, ImageFilter, ImageOps
import pillow_heif

pillow_heif.register_heif_opener()
HERE = os.path.dirname(os.path.abspath(__file__))
DRIVE = 'G:/My Drive/Hermes Wraps/'
OUT = os.path.join(HERE, '..', 'public', 'assets', 'edit')
SOURCES = json.load(open(os.path.join(HERE, 'cutout_sources.json')))

# name: crop top as a fraction of the free vertical room (4:3 crop from the full frame),
#       spotlight centre (x, y) and radii (rx, ry) as fractions of the cropped frame.
EDITS = {
  'work/cargo-van-construction-side': dict(top=0.5, centre=(0.52, 0.52), radii=(0.48, 0.42)),
  'tucson-pink-front':                dict(top=0.50, centre=(0.50, 0.55), radii=(0.55, 0.42)),
  'silverado-hood-angle':             dict(top=0.50, centre=(0.52, 0.55), radii=(0.50, 0.45)),
  'work/wrecker-towing-front':        dict(top=0.5, centre=(0.52, 0.55), radii=(0.55, 0.45)),
  'work/box-truck-tire-shop-side':    dict(top=0.5, centre=(0.48, 0.50), radii=(0.50, 0.45)),
  'work/dump-truck-front':            dict(top=0.5, centre=(0.48, 0.55), radii=(0.58, 0.45)),
  'corvette-front':                   dict(top=0.5, centre=(0.45, 0.50), radii=(0.55, 0.45)),
  'work/wrecker-junk-cars-front':     dict(top=0.5, centre=(0.52, 0.48), radii=(0.55, 0.42)),
  'work/express-van-electrical-side': dict(top=0.5, centre=(0.55, 0.42), radii=(0.55, 0.42)),
  'work/vacuum-truck-side':           dict(top=0.5, centre=(0.50, 0.55), radii=(0.58, 0.42)),
  'work/isuzu-truck-landscape-side':  dict(top=0.5, centre=(0.52, 0.50), radii=(0.55, 0.42)),
  'work/express-van-full-wrap':       dict(top=0.5, centre=(0.55, 0.58), radii=(0.55, 0.42)),
}

LIFT = 0.12      # centre brightening (midtones)
SHADE = 0.38     # edge darkening at the corners
CONTRAST = 0.10  # S-curve strength


def crop43(im, top):
    w, h = im.size
    if w / h > 4 / 3:
        cw = round(h * 4 / 3); x = (w - cw) // 2
        return im.crop((x, 0, x + cw, h))
    ch = round(w * 3 / 4); y = round((h - ch) * top)
    return im.crop((0, y, w, y + ch))


def retouch(im, centre, radii):
    a = np.asarray(im, dtype=np.float32) / 255
    h, w = a.shape[:2]
    # Auto levels per channel (0.2% clip) so the whites of the vinyl are clean
    lo = np.percentile(a, 0.2, axis=(0, 1)); hi = np.percentile(a, 99.8, axis=(0, 1))
    a = np.clip((a - lo) / np.maximum(hi - lo, 1e-3), 0, 1)
    # Gentle S-curve for contrast
    a = (1 - CONTRAST) * a + CONTRAST * (0.5 - 0.5 * np.cos(np.pi * a))
    # Spotlight mask: 1 on the vehicle, falling smoothly to 0 at the corners
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    d = np.sqrt(((xx / w - centre[0]) / radii[0]) ** 2 + ((yy / h - centre[1]) / radii[1]) ** 2)
    m = np.clip(1.6 - d, 0, 1)
    m = m * m * (3 - 2 * m)  # smoothstep
    m = m[..., None]
    # Brighten midtones in the centre (protect highlights), darken outside
    lifted = a + LIFT * a * (1 - a) * 2
    shaded = a * (1 - SHADE)
    a = lifted * m + shaded * (1 - m)
    return Image.fromarray((np.clip(a, 0, 1) * 255 + 0.5).astype(np.uint8))


def run(name):
    cfg = EDITS[name]
    im = ImageOps.exif_transpose(Image.open(DRIVE + SOURCES[name])).convert('RGB')
    im = crop43(im, cfg['top'])
    im = im.resize((2400, 1800), Image.LANCZOS)
    im = retouch(im, cfg['centre'], cfg['radii'])
    # Local contrast so lettering, logos and phone numbers read crisply
    im = im.filter(ImageFilter.UnsharpMask(radius=24, percent=10, threshold=0))
    base = os.path.join(OUT, name.split('/')[-1])
    os.makedirs(OUT, exist_ok=True)
    # 1200w serves 3x phones (a full-width card is ~1030px there) at about half the 1600w weight
    for size, suffix in ((1600, ''), (1200, '-1200'), (800, '-800')):
        out = im.resize((size, size * 3 // 4), Image.LANCZOS)
        out = out.filter(ImageFilter.UnsharpMask(radius=1.0, percent=35 if size == 800 else 25, threshold=3))
        out.save(base + suffix + '.jpg', quality=85, optimize=True, progressive=True)
    print('edited', name)


if __name__ == '__main__':
    for n in sys.argv[1:] or EDITS:
        run(n)
