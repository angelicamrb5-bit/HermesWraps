# Hermes Wraps — Website Solutions, Section by Section

_v2 · October 2026_

**Inputs**
- Client audit report: 6 opportunities, 10 recommendations.
- `website-audit.md`: 79 findings.
- Competitor website research: 7 sites, 12 patterns.
- A reference screenshot from the client: a reviews section.
- **The `hermes-wraps` design skill, which is the source of truth:** `SKILL.md`, `references/` (tokens, brand foundations, visual system, components, page blueprints, voice and copy), and the Brand Color Guide v1.0 PDF.

> **How to read this.** The homepage follows the skill's Home blueprint and its persuasion order: promise → proof → process → capability → story → risk removal → close. Each section lists:
> - **Problem:** what the report found.
> - **Leaders:** what the competitors do.
> - **Solution:** the Hermes Wraps version, with layout, draft copy, components and tokens.
> - **Placeholders** and a **Done when** checklist.
>
> Other pages and site-wide fixes come after the homepage.
>
> **Fixed rules (skill):**
> - The primary action is always **"Book a free consultation"**. The compact form is "Book free consultation".
> - The reassurance line **"Free · No obligation · We review your specs before quoting."** goes under the main CTA.
> - The signature line **"We focus on your quality exigencies."** is used verbatim, and only in its four fixed places.
> - Pages are mostly Ivory and Stone, with one burgundy band in the body and gold at about 10%.
> - Colors come only from `--hw-*` role tokens.
> - Nothing is invented. Unknowns are marked `[CLIENT TO SUPPLY: …]`.

---

## Decisions needed (recommended defaults are already applied below)

| # | Decision | Research says | Skill / color guide says | Recommended default |
|---|---|---|---|---|
| **D1** | **Who the homepage speaks to first** | Car owners and small businesses | Design-system and brand teams at medium-to-large companies; the color guide also says US corporate clients (fleet managers, marketing teams, procurement) | **Lead with business, brand and fleet clients, as the skill says.** Most of today's portfolio is personal cars, so those stay visible as proof of craft. Add a labeled *Personal vehicles* route inside Vehicle & fleet wraps. |
| **D2** | **Prices** | "From $" on every service and a cost guide | No invented pricing; competitiveness comes from clarity and lower risk, not price claims | No prices by default. A price line appears **only if the client supplies figures and approves publishing them**. Otherwise: "Priced to your spec after the consultation." |
| **D3** | **Texting/WhatsApp in the sticky mobile bar** | Sticky **Call · Text · Quote** bar | Sticky bar = Midnight, one on-dark button only; phone and email are a secondary path | **Follow the component spec:** the bar holds only the button. Call and WhatsApp sit in the utility row, the mobile menu, the consultation page and the footer. _Alternative:_ add two 44px icon links to the bar. This is a deliberate deviation the client would need to approve. |
| **D4** | **Offers, financing, visualizer** | Launch offers, financing, a wrap visualizer | No discounts or price claims; don't copy competitors' signature widgets | **Not adopted.** |
| **D5** | **Real form submission + uploads** | Photo upload, stated response time | Upload brand guidelines; response time `[CLIENT TO SUPPLY]` | The server sends the request, with files, to the business inbox. This replaces "Nothing is stored on this website", so the site needs a short privacy policy. |
| **D6** | **Spanish** | Bilingual site or "Hablamos español" badge | Signature line never translated | "Hablamos español" now, an EN / ES switch once `/es/` exists. The signature line stays in English everywhere. The Spanish CTA wording is `[CLIENT TO CONFIRM]`. |
| **D7** | **Home H1: brand line vs. search keywords** | City and service in the H1 | Headline leads with "your" (blueprint example: "Your brand standards, applied exactly.") | **Brand line on Home**, with "Vehicle wraps · Tampa Bay" in the eyebrow, lead text and page title. Keyword-led H1s go on the service pages. |

---

## 0. Foundations (before any section)

### 0.1 Domain and email — _Report Opp. 1 · Rec 1 · audit F-001, F-002, F-027_
- **Problem:** The site runs on a temporary workers.dev address. Its search and sharing tags point to hermeswraps.com, which doesn't load. Contact goes to a Gmail address. **The printed business card also lists hermeswraps.com**, so anyone typing it from the card currently reaches a dead address. That makes this the most urgent fix.
- **Solution:**
  - Connect `hermeswraps.com` to the Cloudflare Worker and redirect the workers.dev address to it.
  - Use a domain email (for example `hello@hermeswraps.com`, forwarding to the current inbox). The brand foundations file notes a branded email suits enterprise buyers.
  - Add a sitemap and a branded "page not found" screen with the logo on a dark plate, a short message, the primary CTA and a link to Work.
- **Done when:** the domain loads over HTTPS, the old address redirects, shared links show a preview image, and the 404 page is branded.

### 0.2 Re-skin to the color guide — _Skill §5 · audit F-054, F-055, F-074, F-075_
The current site is off-brand. Every section below assumes this base:

| Element | Current site | Brand system (token / spec) |
|---|---|---|
| Colors | 82 hard-coded values, wine `#691C2A`, gold `#BB8B38` | Only role tokens from `tokens.css` (`--hw-bg`, `--hw-text`, `--hw-heading`, `--hw-btn-*`, `--hw-eyebrow`…) |
| Page balance | Mostly dark (5 dark bands) | 60% Ivory/Stone · 30% Burgundy/Midnight · 10% Gold |
| Gold text on light | `#BB8B38` on light (2.5–3.1:1, **fails**) | `--hw-accent-text` `#7D5C38` (5.5:1 on Ivory, 4.89:1 on Stone) |
| Fonts | Barlow Condensed + Manrope | Barlow Semi Condensed (display 600/700, italic H1/H2) · Barlow 400/500/600 · IBM Plex Mono 400/500, loaded with the exact Google Fonts link in `tokens.css` |
| Type scale | 46 sizes, all-caps headlines | Token scale: display 40→72, H1 36→56, H2 28→40, H3 20→24, body 17/1.6, eyebrow 13 uppercase +0.08em; **sentence-case headlines** |
| Buttons | Square, uppercase | Pill, Barlow 600 16px, no uppercase; L 56 / M 48 / S 40 |
| Cards | Square, heavy photo gradients | 12px radius, 1px `--hw-border`, `--hw-shadow-card` |
| Spacing | 30 padding values | 8px scale (4…128), section padding `--hw-section-y` (64→96) |
| Focus | Browser default | Global rule in `tokens.css`: 2px `--hw-focus`, 2px offset |
| Motion | Autoplaying carousels and hero loop | 150/240/520ms with `--hw-ease`; reduced-motion zeroes durations (already in tokens) |

### 0.3 Measurement — _Rec 5 · audit F-009_
- Use cookie-free analytics (Cloudflare Web Analytics).
- Track these events: CTA clicks by location (header, hero, after proof, story, closing, sticky), consultation submissions, tap-to-call, WhatsApp and email taps.
- Add UTM tags to the bio links on Instagram, Facebook and TikTok.

---

## HOME PAGE

Background rhythm (following the visual system):

| # | Section | Background |
|---|---|---|
| 0 | Utility row | Midnight |
| 1 | Header | Ivory |
| 2 | Hero (light variant) | Ivory |
| 3 | Proof strip | Ivory, bottom of hero |
| 4 | Selected work | Ivory → Stone edge |
| 5 | How we protect your standards | Stone |
| 6 | Services | Ivory |
| 7 | Story | **Burgundy band (the page's one band)** |
| 8 | Consultation explainer + reviews + FAQ | Stone |
| 9 | Closing CTA band | Midnight |
| 10 | Footer | Burgundy |

The light hero keeps the page mostly light and leaves the Story section as the single burgundy band, as the visual system's rhythm rule requires.

---

### 1. Utility row + header — _Opp. 2 · Rec 2 · audit F-012, F-013, F-066_
- **Problem:** The header scrolls away, "Request a quote" is hidden in the mobile menu, "Terms" is in the main navigation, and the navigation labels are written in capitals in the code.
- **Leaders:** CWD keeps the quote button and phone number visible at all times. Ziebart shows hours and directions. Your reference screenshot puts an EN / ES switch in the header.
- **Solution:**
  - **Utility row** (32px, Midnight, Small text, Ivory/Gold Highlight links):
    - Left: `Tampa Bay & surrounding communities`.
    - Right: `(813) 475-1311` · `WhatsApp` · `hermeswraps@gmail.com → domain email` · `Hablamos español` (it becomes an **EN | ES** switch once `/es/` exists; principle taken from the reference, see Appendix A).
  - **Header** (72px desktop / 64px mobile, Ivory, 1px bottom `--hw-border`):
    - Logo on a dark plate, max 48px. Use a clean vector; the supplied JPG has an AI sparkle in the corner and is reference-only.
    - Links in sentence case: **Services · Work · How we work · About · FAQ**.
    - Primary button M **Book a free consultation**.
    - Active link: Burgundy with a 2px gold underline.
  - **Sticky:** shrinks to 64px and adds `--hw-shadow-card`.
  - **Mobile:** a hamburger opens a full-height Ivory sheet:
    - Links shown at H3 size.
    - Full-width CTA at the bottom.
    - Phone, WhatsApp and email below the CTA.
    - Closes with Escape and keeps focus inside the sheet.
  - "Terms" moves to the footer and a `/terms` page.
- **Done when:** the CTA is visible at every scroll position on desktop and reachable in one tap on mobile (sheet or sticky bar), and the logo is never on bare ivory.

### 2. Hero — Promise — _Opp. 2, 5 · audit F-011, F-033, F-045, F-046_
- **Problem:**
  - The headline doesn't say what or where.
  - The gold button leads to videos instead of booking.
  - The looping video shows a blurry arm.
  - The logo appears twice.
- **Leaders:** Real work only, the city named, one primary ask plus one secondary.
- **Solution (light hero, components §Hero):**
  - **Layout:** 6/6 split. Text on the left; a real finished-work photo (16:9 or 4:3, 8px radius) on the right.
  - **Signature motion:** the optional *application reveal* (700ms left-to-right wipe, once per page) runs on that photo. There is no autoplaying video; the process videos move to section 5. There is no logo in the hero.
  - **Eyebrow, as a tagline bar** (Carbon, skewed -12°, label upright): `VINYL SPECIALISTS · TAMPA BAY`
  - **Display/H1** (Burgundy, 700 italic): **Your brand standards, applied exactly.**
  - **Supporting line** (Lead, Carbon, verbatim): **We focus on your quality exigencies.**
  - **Lead** (≤2 lines): "Vehicle and fleet wraps, signs and commercial graphics in Tampa Bay, installed by a specialist with 8+ years of hands-on experience."
  - **Actions:** primary L **Book a free consultation** + text link **See our work →**
  - **Reassurance** (Small, Warm Gray): *Free · No obligation · We review your specs before quoting.*
  - **Mobile:** text first, photo below, button full-width.
  - **Page title (for search):** "Vehicle Wraps, Fleet Graphics & Signs in Tampa Bay | Hermes Wraps" (D7).
- **Placeholders:** `[PROJECT PHOTO: best finished job, daylight, 3/4 view — clean, sharp]`
- **Done when:** a visitor can say what, where and what to do within 5 seconds; there is one primary button; the signature line appears once in this viewport.

### 3. Proof strip — _Opp. 4 · Rec 4, 7 · audit F-024, F-029_
- **Problem:** There are no numbers, film details, warranty or reviews anywhere near the top.
- **Leaders:** A trust row right under the hero (rating, film brand, warranty, location). In Tampa, competitors **don't show ratings near the top**.
- **Solution (components §Proof strip):** 4 items separated by 1px vertical hairlines; a 2×2 grid on mobile. Stat numbers in Burgundy with tabular numerals; labels in Small.

| Stat | Label |
|---|---|
| **8+** | years of hands-on experience |
| **4** | services: vehicle & fleet wraps · signs · commercial graphics · all things vinyl |
| **Tampa Bay** | and surrounding communities |
| `[CLIENT TO SUPPLY: projects completed, or the Google rating "★ x.x · n reviews" once there are real reviews]` | |

- Film brand and warranty appear **only when confirmed**. Today's site says "premium 3M vinyl", which is the client's own claim. Say "certified" only if it's true. The proof strip spec allows "only verified facts"; no logo wall.
- **Done when:** every item is a confirmed fact, and nothing in the strip moves on its own.

### 4. Selected work — Proof — _Opp. 4 · Rec 8 · audit F-028, F-032, F-041, F-043, F-044_
- **Problem:**
  - The gallery is a 3D carousel that advances every 4.5 seconds.
  - Its tabs don't filter.
  - Captions are thin.
  - Fleet and sign claims have no examples.
  - Two descriptions contradict each other.
- **Leaders:** A portfolio treated as the product: cards titled **"Vehicle | Film + color"**, each with its own page, before/after views, and filters by service. Tampa competitors use generic captions; that's an opening.
- **Solution (blueprint Home §3 + components §Project card):**
  - **Eyebrow** `02  SELECTED WORK` · **H2** (italic): **Work measured against our clients' standards.**
  - **3 project cards** (blueprint count). Each card has:
    - A 4:3 image, detail macro first.
    - A tagline-bar badge.
    - The vehicle and finish as the title (the research's "Vehicle | Film" pattern).
    - A Mono meta line: `TYPE · UNITS · AREA`.
    - One "standard met" line.

| Badge | H3 | Mono meta | Standard met (only real facts) |
|---|---|---|---|
| Commercial | Business SUV \| printed side & hood graphics | `COMMERCIAL GRAPHICS · 1 VEHICLE · [CLIENT TO SUPPLY: area]` | Logo and web address matched across side and hood. `[CLIENT TO SUPPLY: permission to name the client]` |
| Vehicle | Chevrolet Corvette C8 \| gloss black roof & mirrors | `PARTIAL WRAP · 1 VEHICLE · FILM [CLIENT TO SUPPLY]` | Gloss black roof and mirrors. |
| Vehicle | Hyundai Tucson \| `[CLIENT TO SUPPLY: exact film name]` | `FULL COLOR CHANGE · 1 VEHICLE` | Full color change, front to rear. |

  - Text link **See all work →**, then the **after-proof CTA** (the blueprint places one here): primary M **Book a free consultation** + reassurance.
  - **Each card links to a case-study page:** Requirement → Approach → Execution → Result (detail macros, before/after on the same angle, labeled in spec style).
  - **No carousel, no autoplay.** Filters live on the Work page.
- **Fix before publishing:** the Tucson color name (the site and Facebook give different names) and the Silverado hood story.
- **Done when:** every card names the vehicle, finish and service, and links to a page; nothing moves on its own.

### 5. How we protect your standards — Process — _Opp. 6 · Rec 6 · audit F-035, F-050, F-057, F-061, F-062_
- **Problem:**
  - The process lives in an autoplaying 3D video carousel with 9px dots and no captions.
  - The "Terms of service" section does the explaining, in contract language.
- **Leaders:** A short numbered process with time frames.
- **Solution (blueprint Home §4 + components §Process steps, §Spec block):**
  - **Eyebrow** `03  HOW WE WORK` · **H2:** **We start with your standards.**
  - **5 steps.** Desktop shows them in a row; mobile shows a vertical timeline. Each number is in Mono inside a 40px Burgundy-outline circle, joined by a 1px `--hw-border` line. The descriptions reuse what the client already publishes in its terms:
    1. **Share your brand standards.** Guidelines, files, color references, quantities, deadlines.
    2. **Review and vehicle assessment.** Every surface is cleaned and inspected; existing damage is noted and photographed at drop-off.
    3. **Proof and approval.** One approved layout per vehicle type. Nothing is scheduled until the written quote is approved.
    4. **Production and installation.** Film placed, stretched, trimmed and finished to the approved layout.
    5. **QA and photo handover.** Final review with you, care instructions, and the process filmed and photographed.
  - **Time frames:** `[CLIENT TO SUPPLY: typical days per step]`. Shown only when confirmed (research pattern 9).
  - **Spec block** (Ivory card on Stone), header `SPEC / WHAT WE CHECK`:

| Row | Value |
|---|---|
| Brand standard source | Your guidelines and files |
| Color match method | `[CLIENT TO SUPPLY]` |
| Proof & approval | Written quote; layout approved per vehicle type before scheduling |
| Panel / seam plan | `[CLIENT TO SUPPLY]` |
| Install QA | Surfaces cleaned and inspected; damage noted at drop-off |
| Handover record | Process filmed and photographed; care instructions provided |

  - **Videos** (they move here): one featured video next to step 4, **paused until pressed**, with native controls, 44px controls, captions if there's speech, and a one-line description. The other two go on the How we work page.
- **Done when:** nothing plays on its own, every control is keyboard-reachable, and step 1 is about the client's standards.

### 6. Services — Capability — _Opp. 4, 5 · Rec 7, 10 · audit F-014, F-041, F-048_
- **Problem:**
  - Five of six cards don't link anywhere.
  - There's no scope or price guidance.
  - Signs have no photo.
- **Leaders:** Every service card links to a page; "from $" prices; packages for entry-level partial wraps.
- **Solution (blueprint Home §5 + components §Service card):**
  - The **4 services from the business card**.
  - Ivory cards with a 12px radius, 1px border and 32px padding.
  - The whole card is clickable.
  - Each card has: a 24px Burgundy line icon → H3 → a 2-line description → 3 "included" bullets → **Explore {service} →**

| H3 | Description | Included (only confirmed scope) |
|---|---|---|
| **Vehicle & fleet wraps** | Single vehicles to fleet programs, one approved layout per vehicle type. | Partial wraps (roof, hood, mirrors, chrome delete) · Full color change · Wrap removal |
| **Signs** | Business signs for storefronts and spaces. | `[CLIENT TO SUPPLY: sign types]` |
| **Commercial graphics** | Printed vehicle and business graphics with your logo, services and contact details. | Logo and layout matched across panels · `[CLIENT TO SUPPLY]` |
| **All things vinyl** | Window and wall graphics, decals and custom vinyl. | Window graphics · Wall graphics · Decals |

  - **Price line (D2):** absent unless the client supplies and approves it.
  - **Packages** (research): *roof, hood, chrome delete, mirror caps, blackout*. These can live on the Vehicle & fleet wraps page as a scope list, **without prices** unless supplied.
  - **Signs image:** `[PROJECT PHOTO: finished sign or window graphic]`. Use a Stone placeholder in design files. On the live site, use the icon-only card until a real photo exists.
- **Done when:** 4 cards each link to a page, and nothing claims scope or price that isn't confirmed.

### 7. Story — the one Burgundy band — _Opp. 4 · Rec 7 · audit F-025_
- **Problem:** The site promises "quality with a name behind it" but shows no name, face or story.
- **Leaders:** Years in business, *Meet the team*, owner-run messaging, shop photos.
- **Solution (blueprint Home §6):**
  - **Eyebrow** (Gold Highlight): `04  WHY HERMES WRAPS` · **H2** (Ivory, italic): **8+ years of craft. Now ready for your next challenge.**
  - **Stat:** **8+** in Wraps Gold (Stat style) with a thin Ring Gold arc. This is the page's only stat row besides the proof strip.
  - **Body** (Ivory, confirmed facts only): "Hermes Wraps was built on 8+ years of hands-on work, first alongside talented mentors and now as its own company. That means one person accountable for your project, from the first spec review to the final walk-around. We're ready for new challenges, and we want to prove it on yours."
  - **Owner portrait** (photo at work) `[CLIENT TO SUPPLY: name, role, photo]`, framed with a 1px Ring Gold hairline.
  - **Secondary on dark:** **About us** (2px gold outline). This isn't a second primary button.
  - **Location and hours:** `[CLIENT TO SUPPLY: shop, mobile or both · general area · hours]` on the About page and in the footer.
- **Done when:** the visitor can name the person behind the work, and "new company" reads as focus and drive, never inexperience.

### 8. Risk removal — consultation explainer, reviews, FAQ (Stone) — _Opp. 3, 4 · Rec 3, 4, 7 · audit F-035, F-039_
- **Problem:** The FAQ avoids price, time, lifespan and warranty. The terms read like a contract. There are no reviews.
- **Leaders:** FAQs on cost, Florida sun, lifespan, leasing, paint safety and aftercare; reviews tagged with vehicle and service, source and date, and owner replies.

**8a. What happens in your consultation** (components §Consultation explainer; three steps, Mono numbers):
1. **Share your requirements.** Vehicle or fleet, brand files, photos, timeline.
2. **We review your standards and scope.** We point out anything, like paint condition, that could affect the result.
3. **You get a clear plan and quote.** In writing. `[CLIENT TO SUPPLY: response time]`

Then the primary M button **Book a free consultation** + reassurance line.

**8b. Reviews** — _new module, from the client's reference screenshot (see Appendix A)_. **Built now, switched on only once there are real reviews.**
- **Header row:** eyebrow `05  CLIENT REVIEWS`, H2 **Standards met, in our clients' words.** On the right, aligned to the H2 baseline, a **verifiable rating summary**:
  - The rating number in Stat style (Burgundy): `[CLIENT TO SUPPLY]`.
  - A Mono line: `GOOGLE · [n] REVIEWS`.
  - A text link: **Read every review on Google →**
  - Stars are line icons in `--hw-accent-text`. Wraps Gold on Stone fails contrast for meaningful graphics.
- **Cards:** 3 per row, 1 on mobile. Each is an Ivory card with a 12px radius, a 1px border and 32px padding:
  - A quote in Body, max 68ch.
  - A Mono tag: `VEHICLE · SERVICE`, for example `TOYOTA COROLLA · PARTIAL WRAP` (the research gap no Tampa competitor fills).
  - Name, source and date in Small Warm Gray.
  - The owner's reply, collapsed, if one exists.
- **Rules:** real reviews only, quoted verbatim, linked to the source. Hidden until there are at least `[CLIENT TO SUPPLY: minimum, e.g. 3]`. No "verified" or "unfiltered" claims unless the reviews are pulled automatically from the source.
- **Start collecting now (Rec 4):** set up or claim the Google Business Profile and send every finished customer a direct review link.

**8c. FAQ** (3–5 questions on Home, grouped per blueprint; `<details>` accordion, H4 Burgundy questions, hairline separators):
- *What does the free consultation include?* (the 3 steps above)
- *Do you work from our brand guidelines and files?* Yes. Your guidelines are the brief.
- *How do proofs and approvals work?* One approved layout per vehicle type; nothing is scheduled until the written quote is approved.
- *What areas do you serve?* Tampa Bay and surrounding communities. `[CLIENT TO SUPPLY: list]`
- *How long does a project take?* `[CLIENT TO SUPPLY]`
- The FAQ page covers more: cost (D2), lifespan in the Florida sun `[CLIENT TO SUPPLY: film data]`, warranty `[CLIENT TO SUPPLY]`, leased vehicles, paint condition, aftercare, Spanish.
- **Terms:** the 8 terms move to `/terms`, linked from the FAQ, the form and the footer.

- **Done when:** the four deciding questions (cost, time, lifespan, warranty) have either a real answer or an honest "confirmed in your written quote".

### 9. Closing CTA band (Midnight) — _audit F-023_
- **Problem:** Five different button labels all lead to the same form.
- **Solution (components §Closing CTA band):**
  - Midnight background; optional copper linework in one corner, decorative only.
  - **H2** (Ivory, italic, verbatim): **We focus on your quality exigencies.**
  - Line (Gold Highlight): "Have a standard we should meet?"
  - **On-dark button L:** **Book a free consultation** + reassurance (Ivory 80%) + phone and email as text links.
- **Watch:** the footer also carries the signature line. To avoid both appearing in one viewport, put the footer's signature in the footer's bottom row and **verify at 1280×800 and 375px** during QA. If both still show together, the client chooses which one stays on Home.
- **Done when:** every CTA on the page uses the same wording.

### 10. Footer (Burgundy) — _audit F-026, F-076, F-078_
- **Problem:** No hours or legal pages, a domain that doesn't load, and a YouTube link that goes nowhere.
- **Solution (components §Footer):**
  - **Columns:**
    - Logo + signature line (verbatim, see note in §9).
    - **Services:** the 4 service pages.
    - **Company:** Work, How we work, About, FAQ.
    - **Contact:** phone, WhatsApp, email, socials (Instagram, Facebook, TikTok; YouTube only when it exists), service area, `[CLIENT TO SUPPLY: hours]`.
  - **Bottom row:** © Hermes Wraps · Terms · Privacy · Hablamos español, with a 1px `--hw-border-on-dark` divider.
- **Done when:** every link works, and the service area matches the Google Business Profile.

### 11. Sticky mobile CTA bar — _Opp. 2 · Rec 2 · audit F-012, F-022_
- **Problem:** About 20 screens of scrolling with no way to act.
- **Leaders:** Wrap Bullys' sticky Call · Text · Quote bar.
- **Solution (components §Sticky mobile CTA bar):**
  - 64px Midnight bar with safe-area padding.
  - An on-dark button full-width: **Book free consultation**.
  - Appears after the hero; hides near the closing band and on the consultation page.
  - **D3:** if the client approves the deviation, add Call and WhatsApp as 44px icon links with labels for screen readers.
- **Done when:** one tap reaches booking from any point on the page, and the bar never covers form fields.

---

## OTHER PAGES

### 12. Book a free consultation — the conversion point — _Opp. 3 · Rec 3 · audit F-015 to F-022_
- **Problem:** No photo upload; the email button fails silently; answers come pre-filled; "Copy details" is a dead end.
- **Leaders:** A short form that asks for the vehicle first, with photo upload and a stated response time.
- **Solution (blueprint §Book + components §Consultation form):**
  - **Compact header:** logo + phone. No sticky bar and no competing links.
  - **Left column:**
    - H1 **Book a free consultation**.
    - The **signature line** (fixed place #4).
    - The 3-step explainer.
    - The reassurance list.
    - Other ways to reach us: phone, WhatsApp (prefilled message, English or Spanish), email.
  - **Right column, the form** (Stone page, Ivory card, 12px radius, 40px padding, max 640px):
    - **Required:** Name · Company · Work email · Project type (*Vehicle/fleet wraps · Signs · Commercial graphics · Other vinyl*) · Requirements.
      - Requirements hint: *"Brand guidelines, color references, quantities, locations, deadlines - whatever applies."*
    - **Optional, under "Helpful details":** Phone · Quantity/fleet size · Timeline · Upload.
      - Upload accepts **PDF, AI, SVG, EPS** (spec) **plus JPG, PNG, HEIC vehicle photos** (research and audit).
      - Size limit: `[CLIENT TO SUPPLY]` MB.
    - **D1 adjustment:** if the project type is a personal vehicle, show Company as optional and "Work email" as "Email". This needs client approval, because the spec makes Company required.
    - **No pre-selected answers.** Labels sit above the fields. Errors use Burgundy text, an icon and a message (never color alone), linked to the field with `aria-describedby`.
    - **Submit:** primary L, full-width on mobile, **Book a free consultation** + reassurance.
  - **Real submission (D5):** the Worker emails the request and its files to the business inbox. No email app is needed on the visitor's side.
  - **Success state:** H2 **"Thank you - we'll review your requirements."** + "What happens next" (3 steps) + "We'll contact you within `[CLIENT TO SUPPLY]`." + contact details.
  - **Error state:** a plain message, the entered data kept, and the other ways to reach us listed.
  - **Privacy:** "We use your details only to answer this request." + a link to the policy.
  - **Below the form:** a short FAQ with 3 questions.
- **Done when:** a request with photos arrives in the inbox; nothing is pre-selected; a failure never looks like a success.

### 13. Services overview + 4 service detail pages — _Opp. 5 · Rec 10 · audit F-005, F-006_
- **Overview:**
  - H1 **Vinyl work built to your spec.** (blueprint).
  - The 4 cards.
  - A "What every project gets" Spec block.
  - Selected work.
  - Closing band.
- **Detail pages** (template):
  - Hero H1 framed on the outcome **and the search term**. For example, Vehicle & fleet wraps: **Vehicle and fleet wraps built to your spec, Tampa Bay**.
  - Scope (only confirmed items).
  - A service-specific Spec block. For fleets: consistency across vehicles, panel/seam plan, color match, rollout `[CLIENT TO SUPPLY]`.
  - A condensed 4-step process.
  - 2–3 related projects.
  - 3–4 FAQs.
  - Closing band.
- **Personal vehicles route (D1)**, inside Vehicle & fleet wraps: partial wraps, color change, chrome delete and wrap removal, with the current personal-car projects as proof.
- **Later (research pattern 6):** area pages `[CLIENT TO SUPPLY: areas actually served]` and a cost guide (only with real price ranges).

### 14. Work + case studies — _Rec 8_
- H1 **Work measured against our clients' standards.**
- Filter tags (pill, selected = Burgundy): Fleet · Vehicle · Signs · Commercial · Other vinyl.
- A 3-column grid, detail macro first.
- An inline prompt after the 6th card: *"Have a standard we should meet? Book a free consultation."*
- Empty filter message: *"No projects in this category yet. See all work."*
- **Case study:** Requirement → Approach → Execution → Result. The spec strip uses real data only. A pull quote appears only if the client approves it.
- **First commercial case study:** `[CLIENT TO SUPPLY: job with permission]`.

### 15. How we work — the key page for brand teams
- H1 **We start with your standards.**
- A 6-step timeline: share standards → review & assessment → proof & approval → production → installation → QA & photo handover.
- A "What we need from you" checklist.
- A "What you get from us" Spec block.
- A detail-macro gallery with captions on what to look for (edges, seams, alignment).
- All three process videos, on demand only.
- A process FAQ.
- Closing band.

### 16. About
- H1 **Committed to the standards you set.**
- The owner portrait `[CLIENT TO SUPPLY]`.
- The 8+ years story.
- A stat row: 8+ · `[CLIENT TO SUPPLY]`.
- 3 principles: *Your standards first · Precision you can inspect · Commitment to every client*.
- 3 projects.
- Closing band.

### 17. Landing page template (ads, e.g. a fleet campaign)
- No main navigation: logo + phone + CTA.
- Hero matched to the ad.
- Proof strip.
- 3 relevant projects.
- 3-step process.
- **Inline consultation form** (this is where the research's "form on the page" pattern fits).
- FAQ.
- Closing band.
- Minimal footer.

### 18. Spanish — _Opp. 5 · Rec 10 · audit F-038_
- **Now:** "Hablamos español" in the utility row and footer; a Spanish prefilled WhatsApp message; the form hint "Puedes escribir en español."
- **Later:** `/es/` versions of Home, Services and the consultation page, with an **EN | ES switch** in the utility row (principle from the reference screenshot). The signature line stays in English. The Spanish CTA is `[CLIENT TO CONFIRM]`. No Tampa competitor offers Spanish, so this is a real advantage.

---

## SITE-WIDE

### 19. Accessibility and speed — _Opp. 6 · Rec 6, 9_

| Audit issue | Fix |
|---|---|
| Gold labels fail contrast (F-054) | `--hw-eyebrow` = Gold Text (5.5:1 Ivory / 4.89:1 Stone); Gold Highlight on dark |
| Motion without pause (F-043, F-057) | No autoplay anywhere; reveals once, ≤520ms; application reveal ≤700ms once per page |
| No focus style (F-055) | Global Ring Gold rule from `tokens.css` |
| Small targets (F-061) | Everything ≥44px |
| Video captions (F-062) | Captions or a text description |
| Lightbox focus (F-060) | Native `<dialog>` for image zoom |
| Heavy video and images (F-068, F-069) | No hero video; AVIF/WebP in several sizes with `srcset`; measure with PageSpeed after launch |
| Fonts (F-070) | The exact weights listed in `tokens.css` only |

### 20. QA after each section
Run **quality-insurance** (drift scan + 375px and 1280px renders + checklist) after each built section before moving to the next.

---

## Research patterns: adopted, adapted, not adopted

| Pattern | Status | Where |
|---|---|---|
| 1. Real work + city + one clear ask | **Adapted** (city in the eyebrow and lead, brand line as H1 — D7) | §2 |
| 2. Contact from any scroll position | **Adapted** (sticky header + sticky bar per spec; call/WhatsApp in the utility row and menu — D3) | §1, §11 |
| 3. Short form, vehicle first, photos, response time | **Adopted** within the spec's fields | §12 |
| 4. Rating near the top, reviews with vehicle + service | **Adopted, real data only** | §3, §8b |
| 5. Portfolio as product, project pages | **Adopted** | §4, §14 |
| 6. Service / make / area pages | **Phased** (services now, areas later) | §13 |
| 7. Film brand + warranty | **Adopted once confirmed** | §3, §8c |
| 8. Price anchors | **Pending D2** | §6 |
| 9. Steps with time frames | **Adapted** (skill's 5–6 steps; times once confirmed) | §5, §15 |
| 10. Years, team, hours, languages | **Adopted** | §3, §7, §10, §18 |
| 11. Offers and urgency | **Not adopted** (D4) | — |
| 12. Visualizer | **Not adopted** (a competitor's signature feature) | — |
| Mega-menu by make, award badges, "I want the same →" | **Not adopted** (no proof yet; copies distinctive copy; breaks the CTA rule) | — |

## Report recommendations → where they're solved

| Report rec | Sections | Timing |
|---|---|---|
| 1. Connect hermeswraps.com | 0.1 | Quick win |
| 2. One-tap booking/calling on phones | 1, 2, 11 | Quick win |
| 3. Make the form reliable | 12 | Quick win |
| 4. Start collecting reviews | 8b | Quick win |
| 5. Measure calls, messages, requests | 0.3 | Quick win |
| 6. Easier to read and use | 0.2, 5, 19 | Quick win |
| 7. Answer the big questions | 3, 6, 7, 8 | Next |
| 8. Show more work | 4, 14 | Next |
| 9. Lighter on mobile | 2, 19 | Next |
| 10. Service pages + Spanish | 13, 18 | Later |

## What the client needs to supply

1. Domain registrar access; the domain email to use.
2. A **clean vector logo** (SVG/PDF) and transparent PNGs. The supplied JPG has an AI sparkle and is reference-only.
3. Owner name, role, a photo at work, and a 2–3 sentence story.
4. Shop, mobile or both; area; hours; the list of areas served (confirm Brandon).
5. Film brand and series; whether "certified" applies; the warranty period; color match method; panel/seam approach.
6. Prices or a no-prices decision (D2); typical timeline per step; consultation response time; upload size limit.
7. Permission to name business clients; a commercial job for a case study; sign types offered.
8. Photos: the hero image, detail macros (edges, seams, mirrors), signs/window work, before/after pairs.
9. Corrections: the Tucson film name; the Silverado hood story.
10. Do the process videos have voice (for captions)?
11. Google Business Profile access; the minimum number of reviews before showing them.
12. The Spanish CTA wording; who answers in Spanish.
13. Decisions D1–D7.

## Build order
1. **Week 1:** 0.1–0.3 foundations · §1 header · §2 hero · §3 proof strip · §11 sticky bar · §12 consultation page.
2. **Week 2:** §4 work · §5 process · §6 services · §7 story · §8 explainer + FAQ · §9 closing band · §10 footer.
3. **Weeks 3–4, as content arrives:** §8b reviews (when real), §13–16 pages, §18 Spanish.

Each section is checked with **quality-insurance** before the next one starts.

---

## Appendix A — Reference screenshot: reviews section (translated, not copied)

_Per skill §8. Paste this entry into `hermes-wraps/inspiration/README.md` and save the screenshot there as `01-reviews-section.webp` so future work uses it too._

```
### 01 - reviews section
File: 01-reviews-section.webp
Source: Sign Up Creative, Reviews section
Section(s) shown: header + reviews
What the client likes: (client to fill in)
Take: numbered section index as the eyebrow; a large, confident headline with lots of
      whitespace on a warm light background; the rating summary as hard data (score ·
      count · source) set apart on the right with a "read all on the source" link;
      reviews in a flat, hairline-bordered 3-up grid with no shadows; a language
      switch (EN | ES) in the header.
Don't take: the ultra-condensed all-caps headline (our headlines are sentence case,
      Barlow Semi Condensed italic); the headline copy "What clients actually say." and
      "pulled, not curated"; the oversized orange star row and orange/navy colors; the
      big orange "Start a project" header block; the bracketed "[ 05 ]" styling (we use
      our own Mono "05  CLIENT REVIEWS" eyebrow).
Applies to: Home §8b reviews, header utility row (EN | ES), FAQ/consultation pages.
```

**How it was translated:**

| Principle taken | Hermes Wraps version |
|---|---|
| Numbered section index | Gold Text Mono eyebrow `05  CLIENT REVIEWS`, consistent with every section |
| Big headline, lots of space | H2 in Barlow Semi Condensed italic, sentence case, on Stone with 96px padding |
| Rating as verifiable data | Stat number + Mono `GOOGLE · n REVIEWS` + "Read every review on Google →", shown only with real data |
| Flat bordered grid | Ivory cards, 12px radius, 1px `--hw-border`, plus a **vehicle · service** tag the reference doesn't have |
| EN \| ES switch | In our Midnight utility row, not in the main bar |

What makes it ours, not theirs:
- The burgundy/gold palette.
- Rounded cards in place of a shared-border table.
- The vehicle · service tags.
- Stars as small line icons, not a giant orange row.
- Our own headline: *Standards met, in our clients' words.*
