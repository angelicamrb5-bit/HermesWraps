# Component data

Specs for the core components. All values reference `tokens.css`. Every interactive component has default, hover, active, focus-visible and disabled states; focus is always the 2px Ring Gold outline with 2px offset.

## Button

| Variant | Background | Label | Border | Hover | Use |
|---|---|---|---|---|---|
| Primary | `--hw-btn-primary-bg` | `--hw-btn-primary-text` | none | bg `--hw-btn-primary-bg-hover` | Main CTA on light surfaces. |
| On dark | `--hw-btn-dark-bg` | `--hw-btn-dark-text` | none | bg `--hw-btn-dark-bg-hover` | Main CTA on burgundy/midnight/photo overlay. |
| Secondary | transparent | `--hw-burgundy` | 2px `--hw-burgundy` | bg `--hw-burgundy-50` | Second action on light. |
| Secondary on dark | transparent | `--hw-ivory` | 2px `--hw-gold` | bg rgba(201, 164, 119, 0.12) | Second action on dark. |
| Text link button | none | `--hw-link` + arrow → | none | underline, arrow moves 4px right | Tertiary ("See the project →"). |

- Shape: pill (`--hw-radius-pill`). Heights: L 56px (hero), M 48px (default), S 40px (dense UI). Min touch target 44px.
- Padding: L 0 32px, M 0 24px, S 0 16px. Label: Barlow 600, 16px (L 17px), no uppercase.
- Optional trailing arrow icon, 16px, 8px gap.
- Disabled: 40% opacity, no hover, `aria-disabled`.
- One primary (or on-dark) button per viewport. Under the main CTA, a Small reassurance line in `--hw-text-muted` (or Ivory 80% on dark).

## Header / navigation

- Height 72px desktop, 64px mobile. Background Ivory with 1px bottom `--hw-border`, or Burgundy when the hero is dark (then logo on burgundy, links Ivory, CTA On dark).
- Left: logo (on dark plate if header is light; max height 48px). Center/right: 4-5 links max - Services, Work, How we work, About, (FAQ). Right: primary CTA "Book a free consultation" (M).
- Optional utility row (32px, Midnight, Small text) with phone and email.
- Sticky on scroll, shrinks to 64px, adds `--hw-shadow-card`.
- Mobile: hamburger → full-height Ivory sheet, links as H3, CTA full-width at bottom, phone/email below.
- Active link: Burgundy, 2px Gold underline offset 6px.

## Hero

- Variants: **Dark** (Burgundy or Midnight background or project photo with `--hw-overlay`) and **Light** (Ivory with project image right).
- Content stack: tagline-bar eyebrow → Display/H1 (≤10 words, client-standards framed) → Lead (1-2 sentences) → primary CTA + secondary/text button → reassurance line → optional proof strip.
- Image: real project, 6/12 or full-bleed. Optional application-reveal.
- Min height: content-driven; don't force 100vh. Desktop ~ 560-680px.

## Proof strip

- Row directly under or inside the bottom of the hero.
- Items: "8+ years of hands-on experience", services count or real figures `[CLIENT TO SUPPLY]`, service area. Stat number in Stat style (Gold on dark, Burgundy on light) + Small label.
- 3-4 items, separated by 1px vertical hairlines. On mobile: 2×2 grid.
- Only verified facts. No logos wall unless real client permission exists.

## Spec block (signature component)

A spec-sheet style table that shows the standards Hermes Wraps checks - speaks directly to design-system teams.

- Container: Ivory or Stone card, 12px radius, 1px `--hw-border`, padding 32.
- Header: Spec label (IBM Plex Mono 13px, Gold Text) e.g. `SPEC / FLEET LIVERY` + H3 title.
- Rows: label (Mono 13px, Warm Gray, 30% width) | value (Body, Carbon). 1px hairline between rows, 12px vertical padding.
- Example rows: Brand standard source · Color match method · Proof & approval · Panel/seam plan · Install QA · Handover record. Values must be real or `[CLIENT TO SUPPLY]`.
- Use on services, case studies and the "How we work" page.

## Service card

- Ivory card on Stone section (or vice versa), radius 12, 1px border, padding 32, gap 16.
- Anatomy: icon (24px, Burgundy) → H3 → 2-line description → 3 bullet "what's included" (Small) → text link "Explore {service} →".
- Hover: border `--hw-burgundy-300`, lift 2px, `--hw-shadow-raised`. Whole card clickable, single link target.
- Grid: 3 columns desktop, 2 tablet, 1 mobile.

## Project card

- Image 4:3, radius 8, optional tagline-bar badge top-left ("Fleet", "Signage").
- Below: H3 project name, Small meta line in Mono (`TYPE · VEHICLES/UNITS · LOCATION`), one-line outcome framed as "standard met".
- Hover: image scale 1.02 inside crop (240ms), title underline.

## Case study layout

- Hero: project image full-bleed, title, meta spec strip (Client type, Scope, Surface/Material, Timeline - real data only).
- Sections: The requirement (their standards) → Our approach (plan, proofs) → Execution (process photos) → Result (detail macros, before/after) → CTA band.
- Pull quote only if a real, approved client quote exists.

## Process steps

- 4-6 numbered steps horizontally (desktop) / vertical timeline (mobile).
- Number in Mono ("01") inside a 40px Ring Gold circle outline (on dark) or Burgundy outline (on light); H3 step title; 1-2 line description.
- 1px connecting line between steps (Gold on dark, `--hw-border` on light).
- Step 1 is always about the client's standards ("Share your brand standards").

## Stat

- Number in Stat style, label in Small. Gold on Midnight/Burgundy, Burgundy on Ivory.
- Optional thin Ring Gold arc behind the number (motif). Max one stat row per page.

## Consultation form

- Card on Stone or on a burgundy band (then Ivory card). Radius 12, padding 32-40, max width 640.
- Fields: label above input (Barlow 500 15px, Carbon), input height 48, radius 8, 1px `--hw-burgundy-100` border, Ivory/White background, 16px text. Hover border `--hw-burgundy-300`; focus border Burgundy + Ring Gold focus ring.
- Required: Name, Company, Work email, Project type (select: Vehicle/fleet wraps · Signs · Commercial graphics · Other vinyl), Requirements (textarea, hint: "Tell us the standards this project must meet").
- Optional (visually grouped under "Helpful details"): Phone, Quantity/fleet size, Timeline, Upload brand guidelines (PDF, AI, SVG).
- Hints Small Warm Gray; errors: Burgundy text + icon + message below field, `aria-describedby`; never color alone.
- Submit: Primary L full-width on mobile, "Book a free consultation". Reassurance line beneath.
- Success state: H2 "Thank you - we'll review your requirements.", 3-step "What happens next", contact details.

## Consultation explainer

- Three columns/steps: "Share your requirements" → "We review your standards and scope" → "You get a clear plan and quote". Mono numbers, short copy, CTA below.

## FAQ accordion

- Items separated by 1px hairlines. Question H4 (Barlow 600 18px, Burgundy), chevron right. Answer Body, max 68ch.
- `<details>/<summary>` or button with `aria-expanded`. Motion 240ms.
- Questions are about risk: process, standards, proofs, timelines, areas served, what the free consultation includes. Answers only with confirmed info.

## Closing CTA band

- Midnight Wine background (optional subtle copper linework in one corner).
- Signature line "We focus on your quality exigencies." as H2 (Ivory, italic) or as Gold Highlight eyebrow above a headline.
- On-dark CTA (L) + reassurance line + phone/email as text links.

## Sticky mobile CTA bar

- Appears after scrolling past the hero, hides near the footer CTA band and on the consultation page.
- 64px, Midnight background, On-dark button full-width (minus 16px gutters), safe-area padding.

## Footer

- Midnight or Burgundy background, Ivory text, links Gold Highlight on hover.
- Columns: logo + signature line; Services; Company (Work, How we work, About, FAQ); Contact (phone, email, socials, service area).
- Bottom row: © Hermes Wraps, Small, 1px `--hw-border-on-dark` divider.

## Badge / tag

- Tagline-bar badge: skewed -12°, Carbon background, Ivory 12px uppercase 600 label, padding 4px 10px.
- Neutral tag (filters, categories): pill, 1px `--hw-border`, Small label Carbon; selected = Burgundy bg, Ivory text.

## Tables (product/portal experiences)

- Header row Stone background, Mono 13px uppercase labels Warm Gray. Rows 48px, 1px hairlines, tabular numbers.
- Status uses text + icon + neutral tones (no new hues): e.g., "Approved" Carbon with check, "Needs proof" Burgundy with dot, "In production" Gold Text.
