# Visual system

Token names refer to `tokens.css`.

## Typography

| Style | Font | Size (mobile → desktop) | Weight | Line height | Notes |
|---|---|---|---|---|---|
| Display | Barlow Semi Condensed | 40 → 72 | 700, italic | 1.05 | Home hero only. Burgundy on light, Ivory on dark. |
| H1 | Barlow Semi Condensed | 36 → 56 | 700, italic | 1.1 | One per page. |
| H2 | Barlow Semi Condensed | 28 → 40 | 700 (italic optional) | 1.15 | Section titles. Keep italic consistent within a page. |
| H3 | Barlow Semi Condensed | 20 → 24 | 600, upright | 1.2 | Card and sub-section titles. |
| H4 | Barlow | 18 | 600 | 1.3 | Labels inside components. |
| Lead | Barlow | 18 → 21 | 400 | 1.55 | Hero/section intros, max 2-3 lines. |
| Body | Barlow | 17 | 400 | 1.6 | Max 68ch. |
| Small | Barlow | 14 | 400/500 | 1.5 | Captions (Warm Gray), legal, reassurance lines. |
| Eyebrow | Barlow | 13 | 600 uppercase, +0.08em | 1.2 | Gold Text on light, Gold Highlight on dark. Number them: "01  OUR PROCESS". |
| Stat | Barlow Semi Condensed | 48 → 80 | 700 | 1 | Key figures ("8+"). Gold on dark, Burgundy on light. Tabular numbers. |
| Spec | IBM Plex Mono | 13-14 | 400/500 | 1.5 | Spec labels, step numbers, measurements. Never body copy. |

Rules
- Headlines are short (≤ 10 words) and sentence case. No all-caps headlines; uppercase is for eyebrows and the tagline bar only.
- Italic is a brand gesture for display/H1/H2, not for emphasis in body text (use 600 weight instead).
- Use `font-variant-numeric: tabular-nums` for numbers in stats, specs and tables.
- Avoid widows in headlines (`text-wrap: balance`).

## Grid and layout

- Container 1200px (wide galleries 1280px), centered, side gutter 16px mobile / 24px desktop.
- 12 columns desktop, 8 tablet, 4 mobile. Gutter 24px desktop, 16px mobile.
- Common splits: 6/6 (hero text + image), 5/7 (copy + project image), 4/4/4 (services, steps), 3×4 (stats).
- Text blocks align left to a shared edge. Center only short hero/closing statements.
- Breakpoints: 640, 960, 1200.
- Asymmetry is allowed when it signals forward motion (image bleeding right, text left), not as decoration.

## Spacing

- 8px base: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128.
- Section vertical padding: 96 desktop, 64 mobile (`--hw-section-y`).
- Heading → body: 16-24. Eyebrow → heading: 12. Body → CTA: 32.
- Card padding: 24 mobile, 32 desktop. Grid gap between cards: 24.
- When in doubt, add space. Crowding reads as cheap; space reads as established.

## Section rhythm

Default page rhythm: Burgundy/Midnight hero (or ivory hero with burgundy header) → Ivory → Stone → Ivory → (one burgundy band if hero was ivory) → Stone → Midnight closing CTA band → Midnight/Burgundy footer.

Rule: one strong burgundy band per page in the body, plus header/footer. The closing CTA band may use Midnight Wine.

## Imagery

**Types and priority**
1. **Detail macros** - edges, seams, corners, wrapped mirrors/handles, panel alignment, lettering crispness. The best proof of precision for a design-system audience.
2. **Finished work** - full vehicle, fleet line-up, storefront, sign, interior graphics. Clean, well-lit, straight-on or 3/4.
3. **Process** - hands applying film, squeegee, trimming, measuring, proof on screen next to the vehicle.

**Treatment**
- Natural color; no heavy filters. Slight warmth is fine (palette is warm).
- Aspect ratios: 16:9 heroes, 4:3 project cards, 1:1 detail macros, 3:2 case study galleries.
- Media radius 8px. Optional 1px Ring Gold hairline frame on featured images.
- Text on photos only with the Midnight overlay (`--hw-overlay`), gradient from the text side.
- Before/after: same angle, same crop, labeled "Before" / "After" in the spec style.
- Alt text describes the work: "Box truck wrapped in a burgundy fleet livery, driver side, panels aligned across the roll-up door."

**Placeholders**: when photos are missing, use a Stone block with a centered Spec label `[PROJECT PHOTO: fleet van, side view]`. Never fill with stock that could be mistaken for client work.

## Iconography

- Line icons, 1.5px stroke, square-ish caps, 24px grid (e.g. Lucide/Phosphor "regular" style).
- Burgundy on light, Gold on dark. Icons support labels; never stand alone as meaning.
- Use sparingly: services, process steps, contact rows. No illustrated mascots; the helmet emblem belongs to the logo only.

## Brand motifs

- **Tagline bar**: Carbon (or Burgundy on light / Carbon on dark) rectangle, `transform: skewX(-12deg)`, label counter-skewed back upright, uppercase eyebrow style in Ivory or Gold Highlight. Use for: hero eyebrow, "Featured project" badge, section index. Max two per page.
- **Ring**: thin Ring Gold circle or arc echoing the logo ring - for framing a stat or the emblem. Decorative, low frequency.
- **Copper linework**: thin copper curves from the business card. Only as subtle decoration on dark backgrounds (e.g., a corner of the closing band), never near text it could be confused with.
- **Hairline rules**: 1px `--hw-border` dividers to structure content like a spec sheet.

## Motion

| Use | Duration | Easing | Behavior |
|---|---|---|---|
| Hover/press (buttons, links, cards) | 150ms | `--hw-ease` | Color change; cards lift 2px and border darkens. |
| Menus, accordions, tabs | 240ms | `--hw-ease` | Height/opacity; chevron rotates 180°. |
| Section reveal on scroll | 520ms | `--hw-ease` | Opacity 0→1 + rise 16px, once, staggered 60ms between items max 4. |
| Application reveal (signature) | 700ms | `--hw-ease-in-out` | Project image clip-path wipe left→right. Once per page. |
| Stat count-up | ≤ 900ms | `--hw-ease` | Only for real numbers; static final value is in the DOM. |

- Direction of movement is forward (left→right, upward). No bounce, elastic, spin, 3D tilt, cursor followers, or scroll-jacking.
- Never animate the CTA to attract attention (no pulsing/shaking).
- `prefers-reduced-motion`: no transforms or wipes; content simply appears.
