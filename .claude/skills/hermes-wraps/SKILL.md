---
name: hermes-wraps
description: Internal design instruction set for the client Hermes Wraps (vinyl specialists - vehicle wraps, fleet graphics, signs, commercial graphics). Use this skill whenever designing, wireframing, writing UI copy for, building, or reviewing anything visual for Hermes Wraps - websites, marketing pages, landing pages, consultation/booking flows, product or portal experiences, components, design tokens, emails, or social/ad layouts. Also use when the user mentions Hermes Wraps, Hermes Burgundy/Wraps Gold, the --hw- tokens, or asks to "make it on-brand" for this client.
---

# Hermes Wraps - Design Skill

This is how Claude designs for Hermes Wraps. It turns the client's audience, message, conversion goal and brand color guide into decisions. Read this file in full before any design work. Open the files under `references/` when the task needs that level of detail (they are listed at the end).

## 0. The brief in one breath

- **Who we design for:** design system designers, design leaders and their teams at medium-to-large enterprises in the wraps and signage business. They own brand standards and hand work to production partners. They judge a partner by how faithfully it executes *their* system.
- **What we must say:** Hermes Wraps has 8+ years of hands-on experience - first alongside talented mentors, now as its own company. It is defined by commitment to the client and the skill to reach the highest quality standards. It is ready for new challenges and wants to prove it performs as expected for any company that hires it.
- **Signature message:** *"We focus on your quality exigencies."* The client's standards come first; Hermes Wraps meets them.
- **What the page must do:** get a qualified visitor to **book a free consultation**, and make Hermes Wraps look like the most competitive, lowest-risk choice in the room.
- **Creative source of truth:** `assets/brand/hermes-wraps-color-guide-v1.0.pdf` (summarized in `references/brand-foundations.md`, implemented in `references/tokens.css`).

## 1. Design approach and feeling

**Target feeling: "a precise partner you can hand your brand to."** Calm, exact, premium, quietly confident. The energy comes from the forward-leaning wordmark and winged helmet, never from loud color or busy effects.

Hold these three ideas together on every screen:

| Idea | How it shows up |
|---|---|
| **Established** (burgundy) | Ivory/stone pages anchored by one strong burgundy band. Generous whitespace. Orderly grid. Nothing looks improvised. |
| **Precise** (midnight + carbon) | Hairline rules, aligned edges, spec-sheet labels, tabular numbers, measured spacing. The page itself is proof of attention to detail. |
| **Premium craft with young energy** (gold + the angled wordmark) | Gold kept to about 10% of any screen. A forward slant (the "tagline bar" motif) and short forward-moving motion. |

The test for any design decision: *would a design system lead look at this and think "these people will respect my specs"?* If a choice is decorative and doesn't support that thought, cut it.

## 2. Communicating expertise to design system teams

This audience writes brand guidelines for a living. They notice sloppiness instantly and distrust hype. Show expertise; don't claim it.

**Do**
- **Speak in their vocabulary**, correctly: brand standards, specs, tolerances, color matching, proofs/approvals, panel layout, seam placement, consistency across locations and fleets, rollout, file handoff, sign-off.
- **Show the system behind the work.** Make the process visible: intake of their standards → proof → approval → production → installation → final QA and photo record. Number the steps. Use the spec-sheet pattern (`references/components.md` §Spec block) to show what Hermes Wraps checks.
- **Let the page demonstrate the discipline**: consistent tokens, strict alignment, WCAG AA contrast, real focus states, no orphan styles. A design-system person will inspect it.
- **Prefer evidence formats**: before/after, detail macro shots (edges, corners, seams, wrapped door handles and mirrors), project facts (vehicle count, surface, material, timeline) - only with real data from the client.
- **Be concrete about the experience**: "8+ years", the mentor-to-independent story, the commitment to the client. These are the facts we have; use them precisely.

**Avoid**
- Superlatives without proof ("best in the industry", "#1", "world-class").
- Invented numbers, certifications, client logos, testimonials, awards or material brands. If proof is needed and not supplied, insert a clearly marked placeholder: `[CLIENT TO SUPPLY: project count]`.
- Generic agency jargon ("synergy", "solutions", "unleash"). Write like a careful craftsperson.
- Talking down: never explain basic design concepts to designers.

## 3. "We focus on your quality exigencies" - the message system

This line is the spine of the experience. It means: **your standard is the brief; our job is to meet it.** It should be felt on every page, not just printed once.

**Where the literal line appears (verbatim, do not reword it):**
1. Home hero - as the supporting line under the headline, or as the headline itself.
2. The closing CTA band before the footer on key pages.
3. The footer, next to the logo, as the signature.
4. The consultation page intro.

Use it once per screen-region at most; never stack it twice in the same viewport.

**Where the idea appears (in plain language, every page):**
- **Headlines lead with "your"**: the client's brand, specs, fleet, standards. Hermes Wraps is the subject second.
- **Proof modules** frame results as "standard met": the requirement → what we did → the result.
- **Process** begins with *their* standards ("We start with your brand guidelines"), not with Hermes Wraps' capabilities.
- **Form copy** asks about their requirements first ("What standards does this project need to meet?").
- **Microcopy** keeps the promise small and specific: "We'll review your specs before we quote."

Supporting phrasings Claude may use in body copy (adapt; don't overuse any one): *"Your standards set the brief." / "Built to your spec." / "Your brand, applied exactly." / "Measured against your guidelines, not ours."*

## 4. Messaging hierarchy and CTA guidance

**Order of persuasion on every marketing page** (top to bottom):
1. **Promise** - what they get, framed around their standards. (Hero)
2. **Proof** - work that shows precision; experience (8+ years). (Immediately after the hero; never below the fold of the second screen.)
3. **Process** - how their standards are protected, step by step.
4. **Capability** - services (vehicle wraps, fleet graphics, signs, commercial graphics, all things vinyl).
5. **Story** - 8+ years, trained alongside talented mentors, now independent and ready for new challenges. Frame the "new company" angle as focus and hunger, never as inexperience.
6. **Risk removal** - free consultation, what happens in it, no obligation. FAQ.
7. **Close** - the signature line + the CTA.

**CTA rules**
- **One primary action everywhere: "Book a free consultation."** Keep the wording identical across the site. Short form where space is tight: "Book free consultation".
- One primary CTA per screen (color guide rule: gold or burgundy CTA once per viewport). Secondary actions ("See our work", "How we work") are secondary or text buttons.
- Primary CTA appears: in the header (right side, always visible), in the hero, after the proof section, and in the closing band. On mobile, a slim sticky bottom bar after the visitor scrolls past the hero.
- **Reduce friction:** under every primary CTA, add a one-line reassurance: *"Free · No obligation · We review your specs before quoting."* (Adjust only if the client confirms different terms.)
- **Explain the consultation**: a short "What happens in your consultation" block (3 steps: share your requirements → we review standards and scope → you get a clear plan and quote). Use this wherever the CTA is the main focus.
- Phone/email are always visible as a secondary path (header utility row or footer), never competing with the primary button.
- Consultation form: as few fields as possible. Required: name, company, work email, project type, short description of requirements. Optional: phone, fleet size/quantity, timeline, file upload for brand guidelines. Confirmation screen restates next steps and expected response time `[CLIENT TO SUPPLY]`.

**Competitiveness** comes from clarity and lowered risk, not from price claims: fast-to-scan pages, visible process, explicit standards, quick booking. Don't invent pricing, discounts or turnaround promises.

## 5. Visual direction (summary - full specs in references)

### Color (from the brand color guide - non-negotiable)
- **60 / 30 / 10**: 60% Ivory `#F7F4EC` + Stone `#ECE6DC` backgrounds; 30% Hermes Burgundy `#460714` + Midnight Wine `#1A0307` (header, hero/one strong band, footer, primary buttons); 10% Wraps Gold `#C9A477` (buttons on dark, icons, dividers, key figures like "8+").
- Body text Carbon Black `#0A0A0A`; headings and links Burgundy; captions Warm Gray `#6B5F57`.
- **Gold text on light backgrounds = Gold Text `#7D5C38` only.** Never Wraps Gold as text on ivory/stone (2.1:1, fails).
- Copper `#C7755E` is decorative linework only - never text, never buttons.
- No new hues (no blues, greens, neons). No gradients except a gold metallic treatment, used sparingly.
- Mostly light site. A fully dark burgundy site reads as nightlife/luxury retail - avoid.
- Always use `--hw-*` role tokens from `references/tokens.css`; never hard-code hex in components.

### Typography
- **Display/headings:** Barlow Semi Condensed, 600-700. H1/H2 may be *italic* to echo the forward-leaning wordmark (the color guide itself uses bold italic headings). H3 and below upright.
- **Body/UI:** Barlow, 400/500/600. 16-18px body, line-height 1.55-1.65, measure 60-75 characters.
- **Spec/data labels:** IBM Plex Mono 400/500, small, used for specs, step numbers, token-like labels. Use sparingly - it signals precision.
- **Eyebrows:** uppercase, 13px, letter-spacing 0.08em, Gold Text on light / Gold Highlight on dark, often numbered ("01  HOW WE WORK") - mirrors the color guide.
- Full scale in `references/visual-system.md`. If a project mandates other fonts, keep the roles (condensed display / neutral sans body / mono specs).

### Layout and spacing
- 12-column grid, 1200px content max (1280px for full-bleed galleries), 24px gutters desktop, 16px side gutter mobile.
- 8px spacing base. Section padding 96px desktop / 64px mobile. Generous whitespace = established.
- Strong left alignment; centered text only for short hero or closing statements.
- One burgundy (or midnight) band per page, plus header and footer. Alternate ivory and stone for other sections.

### Imagery
- Real Hermes Wraps project photos carry the color - let them. Three types: hero/finished vehicles or signs; **detail macros** that prove precision (edges, seams, wrapped curves, alignment across panels); process (install, squeegee, trimming, proofing).
- Text over photos only on a Midnight Wine overlay (≥70% opacity where text sits).
- Logo only on Midnight, Burgundy or a dark plate; never on busy photos.
- No stock handshakes or generic office people. Never present AI-generated vehicles or mock-ups as completed work; label mock-ups as "Concept" if used.
- When real photos aren't available, use neutral placeholders labeled `[PROJECT PHOTO: description]` - don't fill gaps with stock that looks like real jobs.

### UI styling
- Buttons: pill shape (fully rounded), per the color guide. Primary = Burgundy/Ivory text; on dark = Gold/Carbon text; secondary = Burgundy 2px outline.
- Cards: 12px radius, 1px hairline border (Burgundy tint `#D1C1C4` or Stone), no heavy shadows. Flat and exact > glossy.
- Signature motif: the **tagline bar** - a Carbon (or Burgundy) bar skewed ~-12° holding a short uppercase label, taken from the "VINYL SPECIALISTS" bar. Use for eyebrows on dark, badges, or section markers; max one or two per page.
- Thin Ring Gold `#F4D394` rules and circle frames as detail, echoing the logo ring.
- Focus ring: 2px Ring Gold with 2px offset on every interactive element.
- Full component specs: `references/components.md`.

### Motion
- Purpose: show care and forward momentum, not spectacle. 150-300ms for UI states, 400-600ms max for reveals. Ease-out (`cubic-bezier(0.2, 0.7, 0.2, 1)`).
- Direction: elements enter with a short rise or slight left-to-right movement (forward, like the wordmark). Never bounce, spin or parallax-heavy scenes.
- Signature (optional, once per page): **"application reveal"** - a project image revealed by a left-to-right wipe, like vinyl being squeegeed on.
- Respect `prefers-reduced-motion`: replace movement with fades or nothing.

## 6. Pages

Recommended site structure and section order for each key page are in `references/page-blueprints.md`: Home, Services overview + service detail, Work (projects) + case study, How we work (process), About, Book a consultation, landing page template, and FAQ. Start every page from its blueprint, then adapt.

## 7. Design rules

**Lean into**
- Mostly ivory/stone pages, one confident burgundy band, gold as the finishing touch.
- Precision you can see: alignment, hairlines, spec labels, numbered steps, consistent spacing.
- Real work and detail shots as the main proof.
- "Your standards" language and the signature line in its four fixed places.
- One clear primary CTA per screen, always "Book a free consultation".
- Forward-leaning accents (italic display, skewed tagline bar, forward motion), used sparingly.
- Accessibility as part of quality: AA contrast pairs from the guide, visible focus, real labels, alt text that describes the work.

**Avoid**
- Wraps Gold text on light backgrounds; copper for text or buttons; new hues; non-gold gradients.
- Fully dark pages, nightclub/luxury aesthetics, chrome/flame/"car show" clichés, neon, heavy glows, glassmorphism.
- Hype, invented proof, unsupported numbers or claims; placeholder copy that looks final.
- Multiple competing CTAs; CTA wording that changes page to page.
- Copying reference sites' signature widgets, layouts or copy (see §8).
- Decoration that doesn't serve "they'll respect my specs".

## 8. Using the client's reference designs (translate, don't copy)

The client keeps screenshots of sites they like in `inspiration/`. They show **the level and feel** the web should reach - not things to replicate. Before designing a page:

1. List `inspiration/` and read `inspiration/README.md` (the reference log). View every screenshot relevant to the task.
2. For each, extract **principles only**: layout rhythm, density, whitespace, type scale contrast, image treatment, how proof and CTAs are sequenced, interaction tone.
3. **Translate** each principle into Hermes Wraps terms: our tokens, our type, our tagline-bar motif, our message order, our real content.
4. **Differentiate:** if the result would be recognized as the reference site (same signature widget, same unique interaction, same hero composition, same copy structure, same illustration style), change it until it isn't. Shared conventions (a nav bar, a card grid, an FAQ accordion) are fine; distinctive "gadgets" are not.
5. When you present the design, briefly name which reference principles you used and how they were translated.

If `inspiration/` is empty, proceed with this skill alone. Never fetch or reproduce competitor assets.

## 9. Workflow for any design task

1. Identify the deliverable (page, section, component, flow) and its job in the conversion path.
2. Load `references/tokens.css` (and `visual-system.md` / `components.md` as needed). Pick the page blueprint if it's a page.
3. Review `inspiration/` per §8.
4. Write the message first: headline framed around the client's standards, proof, CTA. Then lay out.
5. Build with role tokens only. Mark every missing fact as `[CLIENT TO SUPPLY: ...]`.
6. Run the checklist below before presenting.

## 10. Pre-ship checklist

- [ ] Every color comes from `--hw-*` tokens; no new hex values.
- [ ] Page is mostly ivory/stone; one burgundy/midnight band; gold ≈10%.
- [ ] Every text/background pair is on the approved list (`references/brand-foundations.md`); Gold Text `#7D5C38` used for any gold text on light.
- [ ] Logo sits on Midnight, Burgundy or a dark plate.
- [ ] Hero frames the client's standards; signature line appears in its fixed places, verbatim, not repeated in one viewport.
- [ ] Proof appears right after the hero; no invented numbers, logos or testimonials.
- [ ] One primary CTA per screen, worded "Book a free consultation", with the reassurance line.
- [ ] Focus states visible (Ring Gold); reduced-motion respected; images have descriptive alt text.
- [ ] Layout works at 375px with 16px gutters and no horizontal scroll.
- [ ] Nothing would be recognized as copied from a reference site.

## Reference files

- `references/brand-foundations.md` - full palette, approved contrast pairs, color roles, logo rules, brand facts.
- `references/tokens.css` - drop-in CSS variables: color, role, type, spacing, radius, motion.
- `references/visual-system.md` - type scale, grid, spacing, imagery, iconography, motion specs.
- `references/components.md` - component data: anatomy, sizes, tokens and states for each core component.
- `references/page-blueprints.md` - page hierarchy and section-by-section content guidance for key marketing pages.
- `references/voice-and-copy.md` - tone, word choices, headline patterns, CTA and microcopy library.
- `inspiration/README.md` - how reference screenshots are stored, logged and translated.
- `assets/brand/` - the color guide PDF, logo reference and business card reference.
