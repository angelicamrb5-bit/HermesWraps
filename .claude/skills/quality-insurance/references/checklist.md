# Drift checklist

Each item names the hermes-wraps rule it enforces (`SKILL.md §n` = hermes-wraps SKILL.md; other files are in hermes-wraps `references/`). Severity: **B** blocking, **S** should fix, **N** note. `[auto]` = the scanner checks it too; still confirm it in context.

## 1. Message & signature line

- [ ] B - Headline frames the client's standards/brand/fleet first; Hermes Wraps is the subject second. (SKILL.md §3)
- [ ] B - Signature line, where used, is exactly "We focus on your quality exigencies." - no paraphrase, translation or shortening. [auto] (SKILL.md §3, voice-and-copy.md)
- [ ] S - Signature line appears only in its fixed places (home hero, closing CTA band, footer, consultation intro) and isn't repeated within one viewport. (SKILL.md §3)
- [ ] S - Section sits in the right place in the persuasion order: promise → proof → process → capability → story → risk removal → close. Proof comes right after the hero. (SKILL.md §4, page-blueprints.md)
- [ ] S - Story copy presents being a young company as focus and drive, never as inexperience; uses only confirmed story facts. (SKILL.md §4, voice-and-copy.md)
- [ ] S - Speaks to design-system teams in their vocabulary (specs, proofs, seams, consistency, rollout) without explaining basics. (SKILL.md §2)

## 2. CTA & conversion

- [ ] B - Primary CTA label is "Book a free consultation" (compact: "Book free consultation"). No "Get a quote", "Contact us", "Get started" as the primary action. [auto] (SKILL.md §4, voice-and-copy.md)
- [ ] B - At most one primary (or on-dark) button per viewport; secondary actions use the secondary or text-link style. (SKILL.md §4, brand-foundations.md)
- [ ] S - Reassurance line under the main CTA: "Free · No obligation · We review your specs before quoting." (SKILL.md §4)
- [ ] S - Where the CTA is the section's focus, the consultation is explained (3 steps). (SKILL.md §4)
- [ ] S - Phone/email visible as a secondary path, never competing with the primary button. (SKILL.md §4)
- [ ] S - Forms: only the specified required fields; optional ones grouped; labels above inputs; errors in text + icon, not color alone. (components.md §Consultation form)
- [ ] B - No invented pricing, discounts, turnaround or guarantee claims. (SKILL.md §4)

## 3. Content integrity

- [ ] B - No invented numbers, client names/logos, testimonials, certifications, awards, material brands or team facts. Unknowns are visible `[CLIENT TO SUPPLY: …]` placeholders. [auto: hype words, lorem ipsum] (SKILL.md §2, brand-foundations.md §Brand facts)
- [ ] S - No hype/superlatives ("world-class", "best in the industry", "#1", "unleash", "elevate your brand"). [auto] (SKILL.md §2, voice-and-copy.md)
- [ ] S - No exclamation marks in headlines; headlines ≤ 10 words, sentence case. [auto: "!" in headings] (voice-and-copy.md, visual-system.md)
- [ ] N - Placeholder count noted in the report so the client list stays current. [auto]

## 4. Color

- [ ] B - Every color comes from `--hw-*` tokens; no off-palette hex/rgb, no new hues. [auto] (SKILL.md §5, brand-foundations.md)
- [ ] S - Components use **role** tokens (`--hw-bg`, `--hw-text`, `--hw-btn-*`…), not raw palette tokens or palette hex. [auto] (brand-foundations.md, tokens.css)
- [ ] B - No Wraps Gold `#C9A477` text on ivory/stone/light; gold text on light uses Gold Text `#7D5C38`. [auto: flags gold text, confirm background] (SKILL.md §5)
- [ ] B - Copper never used for text, buttons or fills; decorative lines only. [auto] (SKILL.md §5)
- [ ] B - Every text/background pair is on the approved list or verified with `contrast.py` (4.5:1, or 3:1 for 24px+ / 18.66px+ bold). (brand-foundations.md §Approved pairs)
- [ ] B - No gradients except gold metallic (sparingly) or the Midnight photo overlay. [auto] (SKILL.md §5)
- [ ] S - Page balance holds with this section in place: mostly ivory/stone, one burgundy band in the body, gold ≈10% of any screen. (SKILL.md §5, visual-system.md §Section rhythm)
- [ ] B - Logo sits only on Midnight, Burgundy or a dark plate; never on a busy photo or bare ivory. (brand-foundations.md §Logo)

## 5. Typography

- [ ] B - Only Barlow Semi Condensed (display), Barlow (body/UI) and IBM Plex Mono (spec labels). [auto] (SKILL.md §5)
- [ ] S - Scale matches the visual system (display/H1/H2/H3 sizes and weights, body 17px at 1.6, measure ≤ 68ch). (visual-system.md §Typography)
- [ ] S - Italic only on Display/H1/H2 and consistent within the page; no italic for emphasis in body. (visual-system.md)
- [ ] S - Uppercase only for eyebrows and the tagline bar; eyebrows 13px, +0.08em, Gold Text on light / Gold Highlight on dark. (visual-system.md)
- [ ] S - Mono used only for specs, step numbers and meta lines, never body copy. (visual-system.md)
- [ ] N - Tabular numbers on stats/specs; balanced headline wrapping.

## 6. Layout & spacing

- [ ] S - Uses the 12-column grid, 1200px container (1280 wide galleries), 24px/16px gutters. (SKILL.md §5, visual-system.md §Grid)
- [ ] S - Spacing values are on the 8px scale (4, 8, 12, 16, 24, 32, 48, 64, 96, 128); section padding 96/64. [auto: off-scale px values as notes] (visual-system.md §Spacing)
- [ ] S - Left-aligned text to a shared edge; centered only for short hero/closing statements. (SKILL.md §5)
- [ ] B - Works at 375px: no horizontal scroll, 16px side gutters, touch targets ≥ 44px. (SKILL.md §10)
- [ ] S - Background alternates correctly with the neighbor sections. (visual-system.md §Section rhythm)

## 7. Imagery

- [ ] B - No stock photos that could pass as client work; no AI-generated vehicles presented as real projects (mock-ups labeled "Concept"). [auto: stock URLs] (SKILL.md §5)
- [ ] S - Missing photos use labeled placeholders `[PROJECT PHOTO: …]`. (visual-system.md §Imagery)
- [ ] S - Text over photos only on the Midnight overlay. (SKILL.md §5)
- [ ] S - Aspect ratios and 8px media radius follow the visual system; detail macros favored as proof. (visual-system.md §Imagery)
- [ ] B - Meaningful images have alt text describing the work; decorative images use `alt=""`. [auto] (SKILL.md §10)

## 8. Components

- [ ] S - Each component matches its spec in components.md: anatomy, sizes, tokens, states (default, hover, active, focus-visible, disabled).
- [ ] S - Buttons are pills; heights 56/48/40; label Barlow 600, not uppercase. (components.md §Button)
- [ ] S - Cards: 12px radius, 1px hairline border, light shadows only. (SKILL.md §5)
- [ ] S - Tagline-bar motif skewed -12° with the label counter-skewed; max two per page. (visual-system.md §Brand motifs)
- [ ] N - Reused existing components instead of creating near-duplicates.

## 9. Motion

- [ ] S - UI states 150-300ms, reveals ≤ 600ms (application reveal ≤ 700ms, once per page); `--hw-ease`. [auto] (SKILL.md §5, visual-system.md §Motion)
- [ ] B - No bounce/elastic/spin/3D tilt/scroll-jacking/cursor followers; CTA never pulses or shakes. [auto: keywords] (visual-system.md §Motion)
- [ ] B - `prefers-reduced-motion` handled for every animation. [auto] (SKILL.md §5)
- [ ] S - Movement direction is forward (left→right, upward). (SKILL.md §5)

## 10. Accessibility

- [ ] B - Visible focus on every interactive element: 2px Ring Gold, 2px offset; no `outline: none` without a replacement. [auto] (brand-foundations.md)
- [ ] B - Semantic structure: one H1 per page, no skipped heading levels, buttons are `<button>`/links are `<a>`, form inputs have labels. (SKILL.md §7)
- [ ] B - Status/error never conveyed by color alone. (components.md)
- [ ] S - Keyboard path through the section works in visual order.

## 11. Reference translation

- [ ] B - Nothing would be recognized as a reference site from `inspiration/`: no copied signature widget, unique interaction, hero composition, illustration style, copy structure, colors or assets. (SKILL.md §8)
- [ ] S - If references informed the section, the principles used are named in the hand-off. (SKILL.md §8)
