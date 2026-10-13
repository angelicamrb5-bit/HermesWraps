#!/usr/bin/env python3
"""Static drift scanner for Hermes Wraps web design work.

Flags code that drifts from the hermes-wraps skill: off-palette colors, raw hex
instead of role tokens, gold/copper misuse, extra fonts, non-standard CTA labels,
signature-line variants, hype or invented-looking claims, stock imagery, missing
alt text, removed focus outlines and motion issues.

The palette is read from hermes-wraps/references/tokens.css, so this script never
drifts from the design skill itself.

Usage:
  drift_scan.py PATH [PATH ...] [--tokens tokens.css] [--json]
  drift_scan.py --git [--tokens tokens.css] [--json]

Suppress a finding with a comment containing `hw-qa-ignore: <reason>` on the same
line or the line above. Exit code: 1 if any error-level finding, else 0.
"""

import argparse
import json
import os
import re
import subprocess
import sys

SCAN_EXTS = {".html", ".htm", ".css", ".scss", ".sass", ".less", ".js", ".jsx",
             ".ts", ".tsx", ".vue", ".svelte", ".astro", ".liquid", ".njk",
             ".hbs", ".php", ".mdx"}
SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next", ".nuxt", "out",
             "coverage", "vendor", ".cache", ".svelte-kit"}

FALLBACK_PALETTE = {
    "460714": "burgundy", "C9A477": "gold", "1A0307": "midnight",
    "0A0A0A": "carbon", "F7F4EC": "ivory", "EDCA9D": "gold-highlight",
    "A27B55": "gold-shadow", "F4D394": "ring-gold", "5B1B26": "burgundy-lift",
    "C7755E": "copper", "7D5C38": "gold-text", "ECE6DC": "stone",
    "6B5F57": "warm-gray",
    "ECE6E8": "burgundy-50", "D1C1C4": "burgundy-100", "A2838A": "burgundy-300",
    "74454F": "burgundy-400", "31050E": "burgundy-700", "1C0308": "burgundy-900",
    "FAF6F1": "gold-50", "F2E8DD": "gold-100", "E4D2BB": "gold-200",
    "D6BB99": "gold-300", "8D7353": "gold-700", "504230": "gold-900",
}

ALLOWED_FONTS = {
    "barlow", "barlow semi condensed", "ibm plex mono",
    # fallbacks declared in tokens.css / generic families
    "arial narrow", "arial", "helvetica neue", "helvetica", "sans-serif",
    "ui-monospace", "sfmono-regular", "menlo", "monospace", "system-ui",
    "-apple-system", "inherit", "initial", "unset", "revert",
}

PRIMARY_CTA = "Book a free consultation"
SIGNATURE = "We focus on your quality exigencies"

CTA_VARIANTS = re.compile(
    r"\b(get an? (free )?(quote|estimate)|request an? (free )?(quote|estimate)|"
    r"free (quote|estimate)|contact us|get started|book now|book an? call|"
    r"schedule an? (call|consultation|meeting)|book an? consultation|"
    r"book (your|a) (free )?consult\b|let'?s talk|get in touch|start your project|"
    r"free consultation\b(?! ?[A-Za-z]))", re.I)

HYPE = re.compile(
    r"\b(world[- ]class|best in (the )?(industry|business|town)|industry[- ]leading|"
    r"#\s?1\b|number one|unleash|elevate your brand|cutting[- ]edge|one[- ]stop[- ]shop|"
    r"game[- ]chang\w*|revolutionary|unmatched|unbeatable|second to none|"
    r"synerg\w*|state[- ]of[- ]the[- ]art|premier\b)", re.I)

CLAIMS = re.compile(
    r"(\b\d[\d,]*\+?\s*(happy |satisfied )?(clients|customers|projects|vehicles|"
    r"wraps|installs|reviews|fleets)\b|★{3,}|\b5[- ]star\b|\b100\s?% (satisfaction|"
    r"guarantee)|\bguarantee[ds]?\b|\bcertified\b|\baward[- ]winning\b|"
    r"\b(same|next)[- ]day\b|\blowest price)", re.I)

STOCK = re.compile(
    r"(unsplash\.com|pexels\.com|shutterstock|istockphoto|gettyimages|pixabay|"
    r"picsum\.photos|placehold\.co|placeholder\.com|via\.placeholder|dummyimage|"
    r"loremflickr|placekitten)", re.I)

NAMED_COLOR = re.compile(
    r"(?<![-\w])(color|background|background-color|border|border-color|fill|stroke|"
    r"outline|outline-color)\s*:\s*[^;{}]*?(?<![-\w])(white|black|red|blue|green|gray|grey|"
    r"silver|navy|teal|orange|yellow|purple|pink|gold|brown|maroon|beige|tan)\b(?![-\w])",
    re.I)

TAILWIND_COLOR = re.compile(
    r"(?<![-\w\[])(bg|text|border|from|via|to|fill|stroke|ring|outline|decoration|"
    r"divide|placeholder|accent|caret|shadow)-(white|black|slate|gray|zinc|neutral|"
    r"stone|red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|"
    r"violet|purple|fuchsia|pink|rose)(-\d{2,3})?(?![-\w])")

HEX = re.compile(r"(?<![\w&])#([0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})(?![\w-])")
RGB = re.compile(r"rgba?\(\s*(\d{1,3})[\s,]+(\d{1,3})[\s,]+(\d{1,3})", re.I)
HSL = re.compile(r"hsla?\(", re.I)
FONT_DECL = re.compile(r"(?:font-family|fontFamily)\s*:\s*([^;{}\n]+)", re.I)
GFONTS = re.compile(r"fonts\.googleapis\.com/css2?\?([^\"'\s>]+)", re.I)
GRADIENT = re.compile(r"(linear|radial|conic)-gradient\(", re.I)
OUTLINE_NONE = re.compile(r"outline\s*:\s*(none|0)\b|outline-(width|style)\s*:\s*(0|none)\b", re.I)
DURATION = re.compile(r"(?<![\w.-])(\d*\.?\d+)(ms|s)\b")
MOTION_LINE = re.compile(r"(transition|animation|duration|delay)", re.I)
MOTION_BAD = re.compile(r"\b(bounce\w*|elastic\w*|wobble\w*|shake\w*|jello|rubber\w*|"
                        r"swing|tada|spin\w*|tilt\w*|parallax\w*|pulse\w*|heartbeat)\b", re.I)
BEZIER = re.compile(r"cubic-bezier\(\s*([-\d.]+)\s*,\s*([-\d.]+)\s*,\s*([-\d.]+)\s*,\s*([-\d.]+)\s*\)")
SPACING_LINE = re.compile(r"(?<![-\w])(margin|padding|gap|row-gap|column-gap|inset|top|"
                          r"bottom|left|right)(-[a-z]+)?\s*:\s*([^;{}]+)", re.I)
PX = re.compile(r"(?<![\w.-])(\d+(?:\.\d+)?)px")
SPACING_SCALE = {0, 1, 2, 4, 8, 12, 16, 24, 32, 48, 64, 96, 128}
HEADING_BANG = re.compile(r"<h[1-3][^>]*>[^<]*!", re.I)
IMG_TAG = re.compile(r"<(img|Image)\b[^>]*?>", re.S)
COPPER_FILL = re.compile(r"(?<![-\w])(color|background|background-color)\s*:[^;{}]*"
                         r"(--hw-copper\b|#c7755e)", re.I)
GOLD_TEXT = re.compile(r"(?<![-\w])color\s*:[^;{}]*(--hw-gold\)|--hw-accent\)|#c9a477\b)", re.I)
TW_ARBITRARY = re.compile(r"(?<![-\w])(text|bg)-\[(#[0-9a-fA-F]{3,8})\]")
SIGNATURE_NEAR = re.compile(r"exigen|focus on your quality", re.I)


def default_tokens_path():
    here = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(here, "..", "..", "hermes-wraps", "references", "tokens.css"),
        os.path.join(os.getcwd(), ".claude", "skills", "hermes-wraps", "references", "tokens.css"),
        os.path.expanduser("~/.claude/skills/hermes-wraps/references/tokens.css"),
    ]
    for c in candidates:
        if os.path.isfile(c):
            return os.path.abspath(c)
    return None


def norm_hex(h):
    h = h.upper()
    if len(h) in (3, 4):
        h = "".join(c * 2 for c in h[:3])
    return h[:6]


def load_palette(tokens_path):
    if not tokens_path:
        return dict(FALLBACK_PALETTE), "built-in fallback (tokens.css not found)"
    palette = {}
    with open(tokens_path, encoding="utf-8") as f:
        for m in re.finditer(r"--hw-([\w-]+)\s*:\s*#([0-9a-fA-F]{6})", f.read()):
            palette.setdefault(m.group(2).upper(), m.group(1))
    return palette, tokens_path


def rgb_hex(r, g, b):
    return "%02X%02X%02X" % (int(r), int(g), int(b))


def git_files():
    out = set()
    for cmd in (["git", "diff", "--name-only", "HEAD"],
                ["git", "ls-files", "--others", "--exclude-standard"]):
        try:
            res = subprocess.run(cmd, capture_output=True, text=True, check=True)
            out.update(l.strip() for l in res.stdout.splitlines() if l.strip())
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass
    return sorted(p for p in out if os.path.isfile(p))


def collect(paths):
    files = []
    for p in paths:
        if os.path.isdir(p):
            for root, dirs, names in os.walk(p):
                dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
                files.extend(os.path.join(root, n) for n in names)
        elif os.path.isfile(p):
            files.append(p)
    keep = []
    for f in files:
        if os.path.splitext(f)[1].lower() not in SCAN_EXTS:
            continue
        if ".min." in os.path.basename(f) or any(part in SKIP_DIRS for part in f.split(os.sep)):
            continue
        keep.append(f)
    return sorted(set(keep))


class Scanner:
    def __init__(self, palette, tokens_path):
        self.palette = palette
        self.tokens_path = os.path.abspath(tokens_path) if tokens_path else None
        self.findings = []

    def add(self, sev, rule, path, line_no, msg, snippet=""):
        self.findings.append({"severity": sev, "rule": rule, "file": path,
                              "line": line_no, "message": msg,
                              "snippet": snippet.strip()[:140]})

    def scan_file(self, path):
        if self.tokens_path and os.path.abspath(path) == self.tokens_path:
            return
        try:
            with open(path, encoding="utf-8", errors="replace") as f:
                text = f.read()
        except OSError as e:
            self.add("error", "IO", path, 0, "Could not read file: %s" % e)
            return
        lines = text.splitlines()
        ignored = set()
        for i, l in enumerate(lines, 1):
            if "hw-qa-ignore" in l:
                ignored.update({i, i + 1})
        ext = os.path.splitext(path)[1].lower()
        is_style = ext in {".css", ".scss", ".sass", ".less"}
        has_reduced = "prefers-reduced-motion" in text
        has_focus_visible = "focus-visible" in text
        uses_motion_literal = False

        for i, line in enumerate(lines, 1):
            if i in ignored:
                continue
            self.check_colors(path, i, line, is_style)
            self.check_fonts(path, i, line)
            self.check_copy(path, i, line)
            if OUTLINE_NONE.search(line):
                if has_focus_visible:
                    self.add("warn", "A11Y-FOCUS", path, i,
                             "Outline removed - confirm a 2px Ring Gold :focus-visible ring replaces it.", line)
                else:
                    self.add("error", "A11Y-FOCUS", path, i,
                             "Outline removed with no :focus-visible style in this file. Focus must stay visible (2px --hw-focus, 2px offset).", line)
            if self.check_motion(path, i, line):
                uses_motion_literal = True
            if is_style:
                self.check_spacing(path, i, line)

        if (uses_motion_literal or "@keyframes" in text) and not has_reduced:
            self.add("warn", "MOTION-REDUCED", path, 0,
                     "Animation/transition with literal timings but no prefers-reduced-motion handling in this file. Use --hw-dur-* tokens or add a reduced-motion rule.")

        for m in IMG_TAG.finditer(text):
            line_no = text.count("\n", 0, m.start()) + 1
            if line_no in ignored:
                continue
            if not re.search(r"\balt\s*=", m.group(0)):
                self.add("error", "A11Y-ALT", path, line_no,
                         "Image without alt. Describe the work, or alt=\"\" if decorative.", m.group(0))

        n_cta = len(re.findall(re.escape(PRIMARY_CTA), text, re.I))
        n_ph = len(re.findall(r"\[(CLIENT TO SUPPLY|PROJECT PHOTO)", text))
        if n_cta:
            self.add("info", "CTA-COUNT", path, 0,
                     "%d x \"%s\" - confirm only one primary button per viewport." % (n_cta, PRIMARY_CTA))
        if n_ph:
            self.add("info", "CONTENT-PLACEHOLDER", path, 0,
                     "%d open placeholder(s) ([CLIENT TO SUPPLY] / [PROJECT PHOTO]) - keep visible and list for the client." % n_ph)

    def check_colors(self, path, i, line, is_style):
        for m in HEX.finditer(line):
            before = line[max(0, m.start() - 6):m.start()].lower()
            if not is_style and ("href=" in before or "#" in before.strip("\"'")):
                continue
            if not is_style and re.search(r"(href|to|id|url)\s*=\s*[\"'{]?\s*$", line[:m.start()], re.I):
                continue
            h = norm_hex(m.group(1))
            if h in self.palette:
                self.add("warn", "COLOR-RAW-HEX", path, i,
                         "Raw palette hex #%s - use a role token (palette: --hw-%s)." % (h, self.palette[h]), line)
            else:
                self.add("error", "COLOR-OFF-PALETTE", path, i,
                         "#%s is not in the Hermes palette. Use --hw-* tokens only; no new hues." % h, line)
        for m in RGB.finditer(line):
            h = rgb_hex(*m.groups()) if all(0 <= int(v) <= 255 for v in m.groups()) else None
            if h and h in self.palette:
                self.add("warn", "COLOR-RAW-HEX", path, i,
                         "Raw rgb() of --hw-%s - use a token (alpha variants belong in tokens.css)." % self.palette[h], line)
            else:
                self.add("error", "COLOR-OFF-PALETTE", path, i,
                         "rgb(%s) is not a Hermes palette color." % ", ".join(m.groups()), line)
        if HSL.search(line):
            self.add("warn", "COLOR-OFF-PALETTE", path, i, "hsl() color - verify it maps to the palette, then use a token.", line)
        m = NAMED_COLOR.search(line)
        if m:
            self.add("error", "COLOR-OFF-PALETTE", path, i,
                     "Named color '%s' - use --hw-* tokens (ivory/carbon, not white/black)." % m.group(2), line)
        for m in TAILWIND_COLOR.finditer(line):
            self.add("error", "COLOR-OFF-PALETTE", path, i,
                     "Framework color class '%s' - map the brand tokens into the framework theme instead." % m.group(0), line)
        if COPPER_FILL.search(line):
            self.add("error", "COLOR-COPPER", path, i,
                     "Copper used as text or fill. Copper Line is for decorative lines only - never text or buttons.", line)
        if GOLD_TEXT.search(line):
            self.add("warn", "COLOR-GOLD-TEXT", path, i,
                     "Wraps Gold used as text. OK only on Midnight/Burgundy; on light use --hw-accent-text (#7D5C38).", line)
        for m in TW_ARBITRARY.finditer(line):
            h = norm_hex(m.group(2)[1:])
            if h == "C7755E":
                self.add("error", "COLOR-COPPER", path, i, "Copper used as text/fill via utility class.", line)
            elif h == "C9A477" and m.group(1) == "text":
                self.add("warn", "COLOR-GOLD-TEXT", path, i, "Wraps Gold text - confirm dark background.", line)
        if GRADIENT.search(line):
            self.add("warn", "COLOR-GRADIENT", path, i,
                     "Gradient - only the gold metallic treatment (sparingly) or the Midnight photo overlay are allowed.", line)

    def check_fonts(self, path, i, line):
        for m in FONT_DECL.finditer(line):
            decl = m.group(1).strip().rstrip(",;}").strip()
            if "var(--hw-font" in decl or decl.startswith(("{", "$", "theme(")):
                continue
            first = decl.split(",")[0].strip().strip("'\"` ").lower()
            if first and first not in ALLOWED_FONTS:
                self.add("error", "TYPE-FONT", path, i,
                         "Font '%s' is outside the system (Barlow Semi Condensed / Barlow / IBM Plex Mono). Use var(--hw-font-*)." % first, line)
        for m in GFONTS.finditer(line):
            for fam in re.findall(r"family=([^&:]+)", m.group(1)):
                name = fam.replace("+", " ").lower()
                if name not in ALLOWED_FONTS:
                    self.add("error", "TYPE-FONT", path, i, "Loads font '%s' - not in the type system." % name, line)

    def check_copy(self, path, i, line):
        if SIGNATURE_NEAR.search(line) and SIGNATURE not in line:
            self.add("error", "MSG-SIGNATURE", path, i,
                     "Signature line variant. Use verbatim: \"%s.\"" % SIGNATURE, line)
        m = CTA_VARIANTS.search(line)
        if m and PRIMARY_CTA.lower() not in line.lower():
            self.add("warn", "CTA-LABEL", path, i,
                     "'%s' - the primary action is always \"%s\". OK only as a clearly secondary/footer link." % (m.group(0), PRIMARY_CTA), line)
        m = HYPE.search(line)
        if m:
            self.add("warn", "COPY-HYPE", path, i, "Hype/superlative '%s' - show proof instead." % m.group(0), line)
        m = CLAIMS.search(line)
        if m and "CLIENT TO SUPPLY" not in line:
            self.add("warn", "CONTENT-CLAIM", path, i,
                     "Claim '%s' - confirm it is client-supplied fact; otherwise use [CLIENT TO SUPPLY: ...]." % m.group(0), line)
        if re.search(r"lorem ipsum|dolor sit amet", line, re.I):
            self.add("error", "CONTENT-LOREM", path, i, "Lorem ipsum - use real copy or a [CLIENT TO SUPPLY] placeholder.", line)
        if HEADING_BANG.search(line):
            self.add("warn", "COPY-HEADING-BANG", path, i, "Exclamation mark in a heading - keep headlines calm.", line)
        m = STOCK.search(line)
        if m:
            self.add("warn", "IMG-STOCK", path, i,
                     "Stock/placeholder image service '%s' - use real project photos or a labeled [PROJECT PHOTO: ...] block." % m.group(0), line)

    def check_motion(self, path, i, line):
        literal = False
        if MOTION_LINE.search(line):
            for m in DURATION.finditer(line):
                val = float(m.group(1)) * (1000 if m.group(2) == "s" else 1)
                literal = literal or val > 0
                if val > 700:
                    self.add("warn", "MOTION-DURATION", path, i,
                             "%sms - UI states 150-300ms, reveals <= 600ms (application reveal <= 700ms)." % int(val), line)
        m = MOTION_BAD.search(line)
        if m and re.search(r"(animation|keyframes|class|transition|ease|motion|variants|@)", line, re.I):
            self.add("warn", "MOTION-STYLE", path, i,
                     "'%s' motion - no bounce/spin/tilt/parallax/pulsing; movement is short and forward." % m.group(0), line)
        for m in BEZIER.finditer(line):
            y1, y2 = float(m.group(2)), float(m.group(4))
            if y1 < 0 or y1 > 1 or y2 < 0 or y2 > 1:
                self.add("warn", "MOTION-STYLE", path, i,
                         "Overshooting cubic-bezier (bounce feel) - use --hw-ease.", line)
        return literal

    def check_spacing(self, path, i, line):
        m = SPACING_LINE.search(line)
        if not m:
            return
        off = sorted({float(v) for v in PX.findall(m.group(3))} - SPACING_SCALE)
        if off:
            self.add("info", "SPACE-SCALE", path, i,
                     "Off-scale spacing %s - scale is 4/8/12/16/24/32/48/64/96/128 (or --hw-space-*)."
                     % ", ".join("%gpx" % v for v in off), line)


def main():
    ap = argparse.ArgumentParser(description="Hermes Wraps drift scanner")
    ap.add_argument("paths", nargs="*", help="files or folders to scan")
    ap.add_argument("--git", action="store_true", help="scan changed + untracked files in git")
    ap.add_argument("--tokens", help="path to hermes-wraps references/tokens.css")
    ap.add_argument("--json", action="store_true", help="JSON output")
    ap.add_argument("--min", choices=["info", "warn", "error"], default="info",
                    help="minimum severity to print")
    args = ap.parse_args()

    tokens_path = args.tokens or default_tokens_path()
    if args.tokens and not os.path.isfile(args.tokens):
        sys.exit("tokens file not found: %s" % args.tokens)
    palette, source = load_palette(tokens_path)

    targets = list(args.paths)
    if args.git:
        targets += git_files()
    if not targets:
        ap.error("give paths to scan or use --git")
    files = collect(targets)

    sc = Scanner(palette, tokens_path)
    for f in files:
        sc.scan_file(f)

    order = {"error": 0, "warn": 1, "info": 2}
    shown = [f for f in sc.findings if order[f["severity"]] <= order[args.min]]
    shown.sort(key=lambda f: (order[f["severity"]], f["file"], f["line"]))
    counts = {s: sum(1 for f in sc.findings if f["severity"] == s) for s in order}

    if args.json:
        print(json.dumps({"palette_source": source, "files": files, "counts": counts,
                          "findings": shown}, indent=2))
    else:
        print("Hermes Wraps drift scan")
        print("Palette: %s (%d colors)" % (source, len(palette)))
        print("Files scanned: %d" % len(files))
        print("Errors: %(error)d  Warnings: %(warn)d  Info: %(info)d" % counts)
        current = None
        for f in shown:
            if f["severity"] != current:
                current = f["severity"]
                print("\n== %s ==" % current.upper())
            loc = "%s:%d" % (f["file"], f["line"]) if f["line"] else f["file"]
            print("[%s] %s - %s" % (f["rule"], loc, f["message"]))
            if f["snippet"]:
                print("    > %s" % f["snippet"])
        if not shown:
            print("\nNo findings.")
    sys.exit(1 if counts["error"] else 0)


if __name__ == "__main__":
    main()
