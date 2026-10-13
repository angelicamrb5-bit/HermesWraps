"""Build the Hermes Wraps color guide (PDF) and web tokens (CSS) from one palette.

Usage:  python3 brand/tools/build_brand_guide.py
Output: brand/hermes-wraps-color-guide.pdf, brand/tokens.css

Every color below was measured from brand/source/logo.jpg (the digital master)
or brand/source/business-card-photo.jpg (a phone photo, so lighting shifts it).
Change a value here, re-run, and both outputs stay in sync.
"""
import datetime
from pathlib import Path

from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "source"
PDF_OUT = ROOT / "hermes-wraps-color-guide.pdf"
CSS_OUT = ROOT / "tokens.css"

# ---------------------------------------------------------------- palette
# (token, name, hex, role, source, usage)
CORE = [
    ("burgundy", "Hermes Burgundy", "#460714", "Primary",
     "Logo disc - 38% of all logo pixels",
     "Hero bands, header, footer, primary buttons, section anchors."),
    ("gold", "Wraps Gold", "#C9A477", "Accent",
     "Emblem + wordmark gold, midtone",
     "Buttons and icons on dark, dividers, key figures. Never as text on light backgrounds."),
    ("midnight", "Midnight Wine", "#1A0307", "Dark base",
     "Logo outer background",
     "Dark sections, overlays on project photos, footer base."),
    ("carbon", "Carbon Black", "#0A0A0A", "Structure",
     "Emblem outlines, 'Vinyl Specialists' bar",
     "Body text on light backgrounds, outlines, the tagline bar motif."),
    ("ivory", "Ivory", "#F7F4EC", "Light base",
     "Wordmark highlights, card text",
     "Main page background, text on burgundy / midnight."),
]
SUPPORT = [
    ("gold-highlight", "Gold Highlight", "#EDCA9D",
     "Metallic gold highlights", "Gold hover state, gold text on burgundy."),
    ("gold-shadow", "Gold Shadow", "#A27B55",
     "Shaded side of the gold", "Borders, gradients. Large text only on ivory."),
    ("ring-gold", "Ring Gold", "#F4D394",
     "Logo outer ring", "Thin rules, badges, the circle frame."),
    ("burgundy-lift", "Burgundy Lift", "#5B1B26",
     "Lightest disc tone", "Hover / pressed state for burgundy surfaces."),
    ("copper", "Copper Line", "#C7755E",
     "Card linework (photo - approximate)", "Decorative lines only. Never text, never buttons."),
]
# Not in the logo or card: added so a corporate-grade website stays legible.
WEB = [
    ("gold-text", "Gold Text", "#7D5C38",
     "Darkened Wraps Gold", "The only gold allowed for text on ivory / stone (5.5:1)."),
    ("stone", "Stone", "#ECE6DC",
     "Warm off-white", "Alternate section background next to ivory."),
    ("warm-gray", "Warm Gray", "#6B5F57",
     "Neutral from the burgundy family", "Secondary text, captions, form hints (5.6:1)."),
]
ALL = {t: h for t, _, h, *_ in CORE} | {t: h for t, _, h, *_ in SUPPORT} | {t: h for t, _, h, *_ in WEB}

# ---------------------------------------------------------------- color math
def rgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))


def cmyk(h):
    r, g, b = (v / 255 for v in rgb(h))
    k = 1 - max(r, g, b)
    if k >= 1:
        return 0, 0, 0, 100
    return tuple(round(v * 100) for v in ((1 - r - k) / (1 - k), (1 - g - k) / (1 - k), (1 - b - k) / (1 - k), k))


def luminance(h):
    c = [v / 255 for v in rgb(h)]
    c = [v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4 for v in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def contrast(a, b):
    hi, lo = sorted((luminance(a), luminance(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def mix(h, other, t):
    a, b = rgb(h), rgb(other)
    return "#%02X%02X%02X" % tuple(round(x + (y - x) * t) for x, y in zip(a, b))


def on(h):
    """Readable text color for a given background."""
    return ALL["ivory"] if contrast(h, ALL["ivory"]) >= contrast(h, ALL["carbon"]) else ALL["carbon"]


# ---------------------------------------------------------------- pdf helpers
pdfmetrics.registerFont(TTFont("Sans", "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Sans-Bold", "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Sans-BoldItalic", "/usr/share/fonts/truetype/liberation/LiberationSans-BoldItalic.ttf"))
pdfmetrics.registerFont(TTFont("Mono", "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf"))

W, H = letter
M = 48
BODY = ParagraphStyle("body", fontName="Sans", fontSize=10, leading=14.5, textColor=ALL["carbon"])
SMALL = ParagraphStyle("small", parent=BODY, fontSize=8.5, leading=11.5, textColor=ALL["warm-gray"])


def para(c, text, x, top, width, style=BODY):
    p = Paragraph(text, style)
    _, h = p.wrap(width, 1000)
    p.drawOn(c, x, top - h)
    return h


def fill(c, h):
    c.setFillColor(h)


def page_header(c, n, title, kicker):
    fill(c, ALL["ivory"]); c.rect(0, 0, W, H, stroke=0, fill=1)
    fill(c, ALL["burgundy"]); c.rect(0, H - 8, W, 8, stroke=0, fill=1)
    fill(c, ALL["gold"]); c.rect(0, H - 11, W, 3, stroke=0, fill=1)
    fill(c, ALL["gold-text"]); c.setFont("Sans-Bold", 8.5)
    c.drawString(M, H - 44, kicker.upper())
    fill(c, ALL["burgundy"]); c.setFont("Sans-BoldItalic", 24)
    c.drawString(M, H - 72, title)
    fill(c, ALL["warm-gray"]); c.setFont("Sans", 8)
    c.drawString(M, 28, "Hermes Wraps  |  Color Guide v1.0")
    c.drawRightString(W - M, 28, str(n))


def swatch(c, x, y, w, h, color, label=None, border=False):
    fill(c, color)
    if border:
        c.setStrokeColor(ALL["stone"]); c.setLineWidth(0.8)
    c.roundRect(x, y, w, h, 6, stroke=1 if border else 0, fill=1)
    if label:
        fill(c, on(color)); c.setFont("Sans-Bold", 8)
        c.drawString(x + 8, y + 8, label)


def specs(h):
    r, g, b = rgb(h)
    C, Mg, Y, K = cmyk(h)
    return f"HEX {h}   RGB {r} {g} {b}   CMYK {C} {Mg} {Y} {K}"


# ---------------------------------------------------------------- pages
def clean_logo():
    """Logo with the generator sparkle (bottom-right of the source file) painted out."""
    logo = Image.open(SRC / "logo.jpg").convert("RGB")
    patch = logo.crop((950, 850, 1020, 950))
    logo.paste(patch, (860, 850))
    return logo.crop((60, 60, 964, 964))


def p_cover(c):
    fill(c, ALL["midnight"]); c.rect(0, 0, W, H, stroke=0, fill=1)
    logo = clean_logo()
    c.drawImage(ImageReader(logo), (W - 300) / 2, H - 390, 300, 300)
    fill(c, ALL["gold"]); c.rect(W / 2 - 30, H - 430, 60, 2, stroke=0, fill=1)
    fill(c, ALL["ivory"]); c.setFont("Sans-BoldItalic", 34)
    c.drawCentredString(W / 2, H - 480, "Brand Color Guide")
    fill(c, ALL["gold-highlight"]); c.setFont("Sans", 12)
    c.drawCentredString(W / 2, H - 504, "Palette, rules and web tokens for every Hermes Wraps touchpoint")
    y = 150
    for i, (_, name, h, *_r) in enumerate(CORE):
        x = W / 2 - 5 * 64 / 2 + i * 64
        fill(c, h); c.setStrokeColor(ALL["gold-shadow"]); c.setLineWidth(0.6)
        c.circle(x + 32, y, 22, stroke=1, fill=1)
    fill(c, ALL["warm-gray"]); c.setFont("Sans", 8.5)
    fill(c, ALL["gold-shadow"])
    c.drawCentredString(W / 2, 70, f"Version 1.0  |  {datetime.date.today():%B %Y}  |  Source of truth: brand/tools/build_brand_guide.py")


def p_sources(c):
    page_header(c, 2, "Where the colors come from", "01  Source & method")
    para(c, "Colors were measured pixel by pixel, not picked by eye. Each image was split into regions "
         "(disc, background, emblem, wordmark, card face, linework) and clustered to find its dominant tones. "
         "<b>The logo file is the master reference</b> because it is digital. The card is a phone photo, so "
         "lighting and the paper finish shift its values a little. The card confirms the same burgundy + gold "
         "family and adds one extra tone: the copper linework.", M, H - 92, W - 2 * M)
    top = H - 190
    logo = clean_logo()
    c.drawImage(ImageReader(logo), M, top - 230, 230, 230)
    card = Image.open(SRC / "business-card-photo.jpg").crop((0, 520, 720, 950))
    cw = W - 2 * M - 250
    c.drawImage(ImageReader(card), M + 250, top - 230 + (230 - cw * 430 / 720) / 2, cw, cw * 430 / 720)
    fill(c, ALL["carbon"]); c.setFont("Sans-Bold", 10)
    c.drawString(M, top - 250, "Logo (digital master)")
    c.drawString(M + 250, top - 250, "Business card (photo)")

    def sampled(x, y, rows):
        for i, (h, label) in enumerate(rows):
            yy = y - i * 24
            swatch(c, x, yy, 30, 18, h, border=luminance(h) > 0.8)
            fill(c, ALL["carbon"]); c.setFont("Mono", 8.5); c.drawString(x + 38, yy + 5, h)
            fill(c, ALL["warm-gray"]); c.setFont("Sans", 8.5); c.drawString(x + 90, yy + 5, label)

    sampled(M, top - 280, [("#460714", "Disc (38% of pixels)"), ("#1A0307", "Outer background"),
                           ("#C9A477", "Gold midtone"), ("#EDCA9D", "Gold highlight"),
                           ("#A27B55", "Gold shadow"), ("#F4D394", "Outer ring"),
                           ("#070302", "Emblem outlines"), ("#F7F4EC", "Brightest highlight")])
    sampled(M + 250, top - 280, [("#50151D", "Card face (lit, reads lighter)"), ("#D7B895", "Title gold"),
                                 ("#ECC18B", "'US' gold"), ("#C7755E", "Copper linework"),
                                 ("#F7F5F6", "White text")])
    para(c, "<b>Reading the numbers:</b> the card face measures #50151D against the logo's #460714. That is the "
         "same burgundy under room light. The website uses the logo values. Printed items should be "
         "proofed against a physical sample before a large run.", M + 250, top - 410, W - 2 * M - 250, SMALL)


def p_core(c):
    page_header(c, 3, "Core palette", "02  The five colors that define the brand")
    y = H - 100
    for token, name, h, role, source, usage in CORE:
        bh = 104
        y -= bh
        swatch(c, M, y, 170, bh - 12, h, border=(token == "ivory"))
        fill(c, on(h)); c.setFont("Sans-Bold", 9); c.drawString(M + 12, y + 12, role.upper())
        x = M + 186
        fill(c, ALL["burgundy"]); c.setFont("Sans-Bold", 15); c.drawString(x, y + bh - 30, name)
        fill(c, ALL["warm-gray"]); c.setFont("Mono", 8); c.drawString(x + 180, y + bh - 29, f"--hw-{token}")
        fill(c, ALL["carbon"]); c.setFont("Mono", 8.5); c.drawString(x, y + bh - 47, specs(h))
        para(c, f"<b>Use:</b> {usage}", x, y + bh - 54, W - M - x)
        para(c, f"Measured from: {source}", x, y + 18, W - M - x, SMALL)


def p_support(c):
    page_header(c, 4, "Supporting tones & web additions", "03  Extended palette")
    para(c, "Supporting tones come from the logo and card too. Use them for detail, depth and interaction "
         "states, never as the main color of a section.", M, H - 92, W - 2 * M)
    y = H - 130
    cw = (W - 2 * M - 4 * 12) / 5
    for i, (token, name, h, source, usage) in enumerate(SUPPORT):
        x = M + i * (cw + 12)
        swatch(c, x, y - 70, cw, 70, h)
        fill(c, ALL["burgundy"]); c.setFont("Sans-Bold", 10); c.drawString(x, y - 86, name)
        fill(c, ALL["carbon"]); c.setFont("Mono", 8); c.drawString(x, y - 99, h)
        para(c, usage, x, y - 104, cw, SMALL)

    y -= 200
    fill(c, ALL["burgundy"]); c.setFont("Sans-Bold", 13); c.drawString(M, y, "Web-only additions")
    para(c, "These are <b>not</b> in the logo. A corporate website needs a legible gold for text, a second "
         "light background and a secondary text gray. Each is derived from the brand family and passes WCAG AA.",
         M, y - 8, W - 2 * M)
    y -= 50
    cw3 = (W - 2 * M - 2 * 12) / 3
    for i, (token, name, h, source, usage) in enumerate(WEB):
        x = M + i * (cw3 + 12)
        swatch(c, x, y - 50, cw3, 50, h, border=True)
        fill(c, ALL["burgundy"]); c.setFont("Sans-Bold", 10); c.drawString(x, y - 66, name)
        fill(c, ALL["carbon"]); c.setFont("Mono", 8); c.drawString(x, y - 79, h)
        para(c, usage, x, y - 84, cw3, SMALL)

    y -= 150
    fill(c, ALL["burgundy"]); c.setFont("Sans-Bold", 13); c.drawString(M, y, "Tints & shades")
    para(c, "For backgrounds, borders and states only. Mixed from the core colors.", M, y - 8, W - 2 * M, SMALL)
    for row, (base, label) in enumerate([("burgundy", "Burgundy"), ("gold", "Gold")]):
        yy = y - 60 - row * 54
        steps = [mix(ALL[base], "#FFFFFF", t) for t in (0.9, 0.75, 0.5, 0.25)] + [ALL[base]] + \
                [mix(ALL[base], "#000000", t) for t in (0.3, 0.6)]
        sw = (W - 2 * M - 70) / len(steps)
        fill(c, ALL["carbon"]); c.setFont("Sans-Bold", 9); c.drawString(M, yy + 16, label)
        for i, h in enumerate(steps):
            x = M + 70 + i * sw
            fill(c, h); c.rect(x, yy, sw, 40, stroke=0, fill=1)
            fill(c, on(h)); c.setFont("Mono", 7); c.drawCentredString(x + sw / 2, yy + 6, h)


def p_meaning(c):
    page_header(c, 5, "What the palette says", "04  Positioning for US corporate clients")
    para(c, "Hermes Wraps is a young company led by someone with <b>8+ years of hands-on experience</b>. "
         "The goal is to become a trusted contractor for <b>medium to large US companies</b>. Those buyers are "
         "fleet managers, marketing teams and procurement departments. The palette already speaks their language. "
         "The job of the website is to use it with discipline.", M, H - 92, W - 2 * M)
    blocks = [
        ("burgundy", "Burgundy = established, trustworthy",
         "Deep reds are the color of institutions: universities, law firms, heritage brands. To a corporate "
         "buyer it signals stability and seriousness, the opposite of a fly-by-night shop."),
        ("gold", "Gold = premium craftsmanship",
         "Gold says the work is finished to a high standard. Used sparingly, it makes the brand feel premium. "
         "Used everywhere, it feels flashy. Keep it to roughly 10% of any screen."),
        ("midnight", "Midnight + Carbon = precision",
         "The near-black tones carry the sharp lines of the emblem and the 'Vinyl Specialists' bar. "
         "They read as technical and exact, which matters to a client handing over a fleet."),
        ("copper", "Copper + the angled wordmark = young energy",
         "The youth shows in the movement, not in louder colors: the forward-leaning italic, the winged "
         "helmet, the card's copper linework. Use these as accents of motion, not as the base."),
    ]
    y = H - 175
    for token, title, body in blocks:
        swatch(c, M, y - 68, 56, 68, ALL[token])
        fill(c, ALL["burgundy"]); c.setFont("Sans-Bold", 12); c.drawString(M + 72, y - 14, title)
        para(c, body, M + 72, y - 22, W - 2 * M - 72)
        y -= 96
    fill(c, ALL["burgundy"]); c.roundRect(M, y - 92, W - 2 * M, 92, 8, stroke=0, fill=1)
    fill(c, ALL["gold"]); c.setFont("Sans-Bold", 9); c.drawString(M + 18, y - 22, "THE BALANCE TO KEEP")
    para(c, "<font color='%s'>Corporate buyers skim. They want clarity, proof and an easy way to request a quote. "
         "So the site should be <b>mostly light (ivory/stone)</b> with burgundy as the confident anchor and gold "
         "as the finishing touch. A fully dark burgundy site reads as nightlife or luxury retail, not as a "
         "contractor you can trust with 200 vehicles.</font>" % ALL["ivory"],
         M + 18, y - 30, W - 2 * M - 36)


def p_rules(c):
    page_header(c, 6, "Website color rules", "05  Guardrails")
    fill(c, ALL["burgundy"]); c.setFont("Sans-Bold", 13); c.drawString(M, H - 100, "60 / 30 / 10 split")
    bw = W - 2 * M
    parts = [("ivory", 0.6, "60%  Ivory + Stone"),
             ("burgundy", 0.3, "30%  Burgundy + Midnight"),
             ("gold", 0.1, "10%  Gold")]
    x = M
    for token, f, label in parts:
        fill(c, ALL[token]); c.setStrokeColor(ALL["stone"])
        c.rect(x, H - 150, bw * f, 36, stroke=1 if token == "ivory" else 0, fill=1)
        fill(c, on(ALL[token])); c.setFont("Sans-Bold", 8)
        c.drawString(x + 8, H - 136, label if token != "gold" else "10%")
        x += bw * f
    para(c, "60%: page backgrounds and breathing room.  30%: header, hero, footer, primary buttons.  "
         "10%: buttons on dark, icons, dividers, key numbers like '8+ years'.", M, H - 158, bw, SMALL)

    fill(c, ALL["burgundy"]); c.setFont("Sans-Bold", 13); c.drawString(M, H - 200, "Approved text / background pairs")
    pairs = [("carbon", "ivory", "Body text"), ("burgundy", "ivory", "Headings, links"),
             ("gold-text", "ivory", "Gold text on light"), ("warm-gray", "ivory", "Captions"),
             ("ivory", "burgundy", "Text on burgundy"), ("gold-highlight", "burgundy", "Gold text on burgundy"),
             ("gold", "midnight", "Gold on dark"), ("carbon", "gold", "Gold button label"),
             ("gold", "ivory", "NOT ALLOWED"), ("copper", "burgundy", "NOT FOR TEXT")]
    y = H - 216
    colw = (W - 2 * M - 12) / 2
    for i, (fg, bg, label) in enumerate(pairs):
        x = M + (i % 2) * (colw + 12)
        yy = y - (i // 2) * 40 - 34
        ratio = contrast(ALL[fg], ALL[bg])
        ok = ratio >= 4.5 and not label.startswith("NOT")
        fill(c, ALL[bg]); c.setStrokeColor(ALL["stone"]); c.setLineWidth(0.8)
        c.roundRect(x, yy, 150, 32, 4, stroke=1, fill=1)
        fill(c, ALL[fg]); c.setFont("Sans-Bold", 11); c.drawString(x + 10, yy + 11, "Aa  Sample")
        fill(c, ALL["carbon"]); c.setFont("Sans-Bold", 9); c.drawString(x + 160, yy + 18, label)
        fill(c, "#1E6B34" if ok else "#9B1C1C"); c.setFont("Sans-Bold", 8.5)
        verdict = "PASS AA" if ok else ("FAIL" if ratio < 4.5 else "AVOID")
        c.drawString(x + 160, yy + 5, f"{ratio:.1f}:1  {verdict}")

    y = H - 470
    fill(c, ALL["burgundy"]); c.setFont("Sans-Bold", 13); c.drawString(M, y, "Buttons & links")
    btns = [("Primary", "burgundy", "ivory", None), ("Primary hover", "burgundy-lift", "ivory", None),
            ("On dark", "gold", "carbon", None), ("On dark hover", "gold-highlight", "carbon", None),
            ("Secondary", "ivory", "burgundy", "burgundy")]
    bw2 = (W - 2 * M - 4 * 10) / 5
    for i, (label, bg, fg, outline) in enumerate(btns):
        x = M + i * (bw2 + 10)
        plate = "midnight" if label.startswith("On dark") else "ivory"
        fill(c, ALL[plate]); c.setStrokeColor(ALL["stone"]); c.roundRect(x, y - 70, bw2, 56, 4, stroke=1, fill=1)
        fill(c, ALL[bg])
        if outline:
            c.setStrokeColor(ALL[outline]); c.setLineWidth(1.5)
        c.roundRect(x + 10, y - 56, bw2 - 20, 26, 13, stroke=1 if outline else 0, fill=1)
        fill(c, ALL[fg]); c.setFont("Sans-Bold", 9); c.drawCentredString(x + bw2 / 2, y - 47, "Get a quote")
        fill(c, ALL["warm-gray"]); c.setFont("Sans", 8); c.drawString(x, y - 82, label)
    para(c, "Links: Burgundy, underlined on hover. On dark: Gold Highlight. Focus ring: 2px Ring Gold "
         "with 2px offset, visible on every interactive element.", M, y - 94, W - 2 * M, SMALL)

    y -= 140
    col = (W - 2 * M - 16) / 2
    for i, (head, color, items) in enumerate([
        ("DO", "#1E6B34", ["Keep backgrounds mostly ivory / stone", "Use burgundy for one strong band per page",
                           "Let project photos carry the color", "Use gold for one CTA per screen",
                           "Check contrast before adding any new pair"]),
        ("DON'T", "#9B1C1C", ["Put Wraps Gold text on light backgrounds", "Use copper for text or buttons",
                              "Add new hues (blues, greens, neons)", "Use gradients other than gold metallic",
                              "Place the logo on busy photos without a dark plate"])]):
        x = M + i * (col + 16)
        fill(c, color); c.setFont("Sans-Bold", 11); c.drawString(x, y, head)
        for j, it in enumerate(items):
            fill(c, ALL["carbon"]); c.setFont("Sans", 9.5); c.drawString(x + 12, y - 18 - j * 15, it)
            fill(c, color); c.circle(x + 4, y - 15 - j * 15, 2, stroke=0, fill=1)


def css_text():
    lines = ["/* Hermes Wraps brand tokens - generated by brand/tools/build_brand_guide.py. Do not edit by hand. */",
             ":root {", "  /* Core */"]
    lines += [f"  --hw-{t}: {h};" for t, _, h, *_ in CORE]
    lines += ["", "  /* Supporting (from logo / card) */"]
    lines += [f"  --hw-{t}: {h};" for t, _, h, *_ in SUPPORT]
    lines += ["", "  /* Web-only additions (derived, AA-checked) */"]
    lines += [f"  --hw-{t}: {h};" for t, _, h, *_ in WEB]
    lines += ["",
              "  /* Roles - use these in components, not the raw colors above */",
              "  --hw-bg: var(--hw-ivory);",
              "  --hw-bg-alt: var(--hw-stone);",
              "  --hw-bg-dark: var(--hw-midnight);",
              "  --hw-surface-brand: var(--hw-burgundy);",
              "  --hw-text: var(--hw-carbon);",
              "  --hw-text-muted: var(--hw-warm-gray);",
              "  --hw-text-on-dark: var(--hw-ivory);",
              "  --hw-heading: var(--hw-burgundy);",
              "  --hw-link: var(--hw-burgundy);",
              "  --hw-link-on-dark: var(--hw-gold-highlight);",
              "  --hw-accent: var(--hw-gold);",
              "  --hw-accent-text: var(--hw-gold-text);",
              "  --hw-btn-primary-bg: var(--hw-burgundy);",
              "  --hw-btn-primary-bg-hover: var(--hw-burgundy-lift);",
              "  --hw-btn-primary-text: var(--hw-ivory);",
              "  --hw-btn-dark-bg: var(--hw-gold);",
              "  --hw-btn-dark-bg-hover: var(--hw-gold-highlight);",
              "  --hw-btn-dark-text: var(--hw-carbon);",
              "  --hw-focus: var(--hw-ring-gold);",
              "  --hw-gold-metallic: linear-gradient(135deg, var(--hw-gold-shadow) 0%, var(--hw-gold-highlight) 45%, var(--hw-gold) 70%, var(--hw-gold-shadow) 100%);",
              "}", ""]
    return "\n".join(lines)


def p_tokens(c):
    page_header(c, 7, "Web tokens & checklist", "06  For the website build")
    para(c, "The website must use these variables from <font name='Mono'>brand/tokens.css</font> and never "
         "hard-coded colors. Components should reference the <b>role</b> tokens so the palette can be adjusted "
         "in one place.", M, H - 92, W - 2 * M)
    roles = [ln.strip() for ln in css_text().splitlines() if ln.strip().startswith("--hw-") and "var(" in ln
             and "gradient" not in ln]
    box_top = H - 140
    box_h = 14 + len(roles) * 11.5
    fill(c, ALL["midnight"]); c.roundRect(M, box_top - box_h, W - 2 * M, box_h, 6, stroke=0, fill=1)
    c.setFont("Mono", 8.2)
    for i, ln in enumerate(roles):
        name, val = ln.split(":", 1)
        fill(c, ALL["gold-highlight"]); c.drawString(M + 14, box_top - 16 - i * 11.5, name + ":")
        fill(c, ALL["ivory"]); c.drawString(M + 220, box_top - 16 - i * 11.5, val.strip())
    y = box_top - box_h - 30
    fill(c, ALL["burgundy"]); c.setFont("Sans-Bold", 13); c.drawString(M, y, "Before shipping any page")
    checks = ["Every color comes from tokens.css. No new hex values in the code",
              "The page is mostly ivory / stone, with one burgundy band and gold limited to about 10%",
              "Every text pair is on the approved list (4.5:1 minimum, 3:1 for text 24px+)",
              "Gold text on light backgrounds uses Gold Text (#7D5C38), never Wraps Gold",
              "The logo sits on Midnight Wine, Burgundy or a dark plate, never on busy photos",
              "Focus states are visible (Ring Gold outline) for keyboard users",
              "Page tone fits a corporate buyer: clear, calm, with proof (projects, fleet clients, years)"]
    for j, it in enumerate(checks):
        yy = y - 22 - j * 18
        c.setStrokeColor(ALL["gold-shadow"]); c.setLineWidth(1); c.rect(M, yy - 2, 10, 10, stroke=1, fill=0)
        fill(c, ALL["carbon"]); c.setFont("Sans", 9.5); c.drawString(M + 18, yy, it)
    yy = y - 22 - len(checks) * 18 - 14
    para(c, "<b>Asset notes:</b> the logo provided is a 1024px JPG with an AI-generator sparkle in the bottom-right "
         "corner. Before launch, get a clean vector logo (SVG / PDF), plus transparent PNGs in full-color and "
         "one-color gold versions. CMYK values in this guide are computed starting points. For print, match "
         "them to a Pantone / vinyl swatch and proof physically.", M, yy, W - 2 * M, SMALL)


def main():
    c = canvas.Canvas(str(PDF_OUT), pagesize=letter)
    c.setTitle("Hermes Wraps - Brand Color Guide")
    c.setAuthor("Hermes Wraps")
    for page in (p_cover, p_sources, p_core, p_support, p_meaning, p_rules, p_tokens):
        page(c)
        c.showPage()
    c.save()
    CSS_OUT.write_text(css_text())
    print(f"wrote {PDF_OUT.relative_to(ROOT.parent)} and {CSS_OUT.relative_to(ROOT.parent)}")


if __name__ == "__main__":
    main()
