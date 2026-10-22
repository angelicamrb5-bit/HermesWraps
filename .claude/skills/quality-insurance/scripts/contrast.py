#!/usr/bin/env python3
"""WCAG contrast check for Hermes Wraps color pairs.

Usage:
  contrast.py FG BG          # hex (#7D5C38) or palette name (gold-text, ivory, burgundy...)
  contrast.py --approved     # list the brand guide's approved / forbidden pairs

Thresholds: 4.5:1 normal text, 3:1 large text (24px+, or 18.66px+ bold) and UI parts.
Names resolve from hermes-wraps/references/tokens.css when found, else a built-in palette.
"""

import os
import re
import sys

BUILTIN = {
    "burgundy": "#460714", "gold": "#C9A477", "midnight": "#1A0307",
    "carbon": "#0A0A0A", "ivory": "#F7F4EC", "gold-highlight": "#EDCA9D",
    "gold-shadow": "#A27B55", "ring-gold": "#F4D394", "burgundy-lift": "#5B1B26",
    "copper": "#C7755E", "gold-text": "#7D5C38", "stone": "#ECE6DC",
    "warm-gray": "#6B5F57",
}

# From Brand Color Guide v1.0, "Approved text / background pairs"
APPROVED = [
    ("carbon", "ivory", "Body text", True),
    ("burgundy", "ivory", "Headings, links", True),
    ("gold-text", "ivory", "Gold text on light", True),
    ("warm-gray", "ivory", "Captions", True),
    ("ivory", "burgundy", "Text on burgundy", True),
    ("gold-highlight", "burgundy", "Gold text on burgundy", True),
    ("gold", "midnight", "Gold on dark", True),
    ("carbon", "gold", "Gold button label", True),
    ("gold", "ivory", "NOT ALLOWED", False),
    ("copper", "burgundy", "NOT FOR TEXT", False),
]


def load_palette():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "..", "..", "hermes-wraps", "references", "tokens.css")
    pal = dict(BUILTIN)
    if os.path.isfile(path):
        with open(path, encoding="utf-8") as f:
            for m in re.finditer(r"--hw-([\w-]+)\s*:\s*(#[0-9a-fA-F]{6})", f.read()):
                pal[m.group(1)] = m.group(2)
    return pal


def resolve(value, pal):
    v = value.strip().lower().replace("--hw-", "").replace("var(", "").rstrip(")")
    if v in pal:
        return pal[v].upper(), v
    h = v.lstrip("#")
    if re.fullmatch(r"[0-9a-f]{3}", h):
        h = "".join(c * 2 for c in h)
    if re.fullmatch(r"[0-9a-f]{6}", h):
        name = next((k for k, x in pal.items() if x.lower() == "#" + h), None)
        return "#" + h.upper(), name
    sys.exit("Unknown color: %s" % value)


def luminance(hex_color):
    def chan(c):
        c = c / 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (int(hex_color[i:i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * chan(r) + 0.7152 * chan(g) + 0.0722 * chan(b)


def ratio(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def main():
    pal = load_palette()
    if len(sys.argv) == 2 and sys.argv[1] == "--approved":
        for fg, bg, label, ok in APPROVED:
            r = ratio(pal[fg], pal[bg])
            print("%-15s on %-10s %5.1f:1  %-22s %s" % (fg, bg, r, label, "APPROVED" if ok else "FORBIDDEN"))
        return
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    fg, fg_name = resolve(sys.argv[1], pal)
    bg, bg_name = resolve(sys.argv[2], pal)
    r = ratio(fg, bg)
    print("%s (%s) on %s (%s): %.2f:1" % (fg, fg_name or "off-palette", bg, bg_name or "off-palette", r))
    print("  Normal text (4.5:1): %s" % ("PASS" if r >= 4.5 else "FAIL"))
    print("  Large text / UI (3:1): %s" % ("PASS" if r >= 3 else "FAIL"))
    for a, b, label, ok in APPROVED:
        if (a, b) == (fg_name, bg_name):
            print("  Brand guide: %s (%s)" % ("APPROVED" if ok else "FORBIDDEN", label))
            break
    else:
        print("  Brand guide: not on the approved list - allowed only if it passes for its text size.")
    if fg_name is None or bg_name is None:
        print("  Note: off-palette color - this alone is drift.")
    sys.exit(0 if r >= 4.5 else 1)


if __name__ == "__main__":
    main()
