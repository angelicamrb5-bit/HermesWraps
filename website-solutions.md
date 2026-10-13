# Hermes Wraps — Website Solutions, Section by Section

_October 2026 · Inputs: client audit report (6 opportunities, 10 recommendations), `website-audit.md` (79 findings), competitor website research (7 sites, 12 patterns), and the `hermes-wraps` design skill (source of truth)._

> **How to read this.** Each section of the new site lists: the **problem** from the report, **what the leaders do** (competitor research), and the **solution for Hermes Wraps**: structure, draft copy, components and tokens, mobile behavior. It ends with **placeholders** and a **done when** checklist.
>
> **Rules applied throughout (from the `hermes-wraps` skill):**
> - Primary action is always **"Book a free consultation"**, followed by **"Free · No obligation · We review your specs before quoting."**
> - The signature line **"We focus on your quality exigencies."** appears verbatim, only in its four fixed places.
> - The site is mostly ivory and stone, with one burgundy band, gold at about 10%, pill buttons, and the Barlow family.
> - Nothing is invented. Anything we don't know is marked `[CLIENT TO SUPPLY: …]`.

---

## Decisions needed before we build

These are places where the competitor research and the brand skill pull in different directions, or where only the client can decide. I've written the solutions below with the **recommended default** applied, so nothing blocks the work.

| # | Decision | Research says | Skill says | Recommended default |
|---|---|---|---|---|
| D1 | **Who the homepage speaks to first** | Car owners and small businesses ("Get a Free Quote", "Text Us") | Brand and design teams at medium-to-large companies; fleets and commercial work | **Lead with business and fleet work, as the skill says**, and keep a clearly labeled *Personal vehicles* path. Today's portfolio is mostly personal cars, so dropping them would hide most of the proof. |
| D2 | **Show prices?** | "From $" on every service and a cost guide | "Don't invent pricing" | Build a **price slot** into each service card and the FAQ, filled **only with numbers the client supplies**. If the client says no, the slot becomes "Priced per spec after your consultation". |
| D3 | **Texting/WhatsApp** | Text is the main contact channel | Phone and email are a secondary path, never competing with the primary button | Keep **WhatsApp/Text as a secondary icon link** (header utility row, sticky bar, form fallback). The primary button stays "Book a free consultation". |
| D4 | **Offers, financing, visualizer** | Launch offers, financing, a wrap visualizer | No discounts or price claims; don't copy competitors' signature widgets | **Not adopted.** A visualizer copies CWD/Wrapmate's signature feature, and offers or financing would need client terms. We can revisit financing if the client offers it. |
| D5 | **Real form submission + photo upload** | Upload photos and promise a response time | Form with optional file upload; response time `[CLIENT TO SUPPLY]` | Send the form to the business by email from the server (photos included). This **replaces** the current "Nothing is stored on this website" note, so we'll need a short privacy policy. |
| D6 | **Spanish** | Bilingual site or "Hablamos español" badge | Signature line verbatim, never translated | "Hablamos español" in the header and footer now, and a `/es/` page later. The signature line stays in English on the Spanish page. |
| D7 | **Missing brand files** | — | The skill refers to `tokens.css`, `components.md`, `page-blueprints.md`, `voice-and-copy.md`, `visual-system.md`, the color guide PDF and `inspiration/` | Those files **did not sync**; only `SKILL.md` arrived. The colors and contrast rules below come from the `quality-insurance` skill's built-in palette. Exact type sizes, component dimensions and blueprints should be checked once the files are re-uploaded. |

---

## 0. Foundations (do these first; every section depends on them)

### 0.1 Move to hermeswraps.com — _Report: Opportunity 1 · Rec 1_
- **Problem:** The site runs on a temporary workers.dev address. Google and social previews point to hermeswraps.com, which doesn't load yet. Contact goes to a Gmail address.
- **Leaders:** Every competitor has its own domain and a matching email address. It's a baseline trust signal, not a differentiator.
- **Solution:**
  1. Connect `hermeswraps.com` to the Cloudflare Worker as a custom domain, and redirect the workers.dev address to it.
  2. Create `hello@hermeswraps.com` (or similar) and forward it to the current inbox. Use it everywhere on the site.
  3. Add a site map for Google, a branded "page not found" screen (logo, short message, "Book a free consultation", link to Work), and set up Google Search Console.
- **Done when:** the domain loads over HTTPS, the old address redirects, a shared link shows a preview image, and the error page is branded.

### 0.2 Re-skin to the brand color guide — _Skill §5 · fixes audit F-054, F-074, F-075_
The current site is **off-brand** compared with the color guide. These changes are the base for every section:

| Element | Current site | Brand guide (skill) |
|---|---|---|
| Main red | Wine `#691C2A` / `#3A0D16` | Hermes Burgundy `#460714` / Midnight Wine `#1A0307` |
| Gold | `#BB8B38` (also used as text on light backgrounds; **fails contrast**) | Wraps Gold `#C9A477` on dark only; **Gold Text `#7D5C38`** for gold text on light |
| Backgrounds | Mostly dark (5 dark bands: videos, gallery, Spanish strip, footer, hero) | **Mostly Ivory `#F7F4EC` / Stone `#ECE6DC`**, one burgundy band plus header and footer |
| Display font | Barlow Condensed, all caps, very large | **Barlow Semi Condensed 600–700**, sentence case; H1/H2 may be italic |
| Body font | Manrope | **Barlow 400/500/600**, 16–18px, line height ~1.6 |
| Spec labels | — | **IBM Plex Mono** (step numbers, project specs) |
| Buttons | Square, uppercase | **Pill**, Barlow 600, not uppercase |
| Cards | Square, photo with heavy gradient | **12px radius, 1px hairline border** (Burgundy tint `#D1C1C4` or Stone) |
| Focus state | Browser default | **2px Ring Gold `#F4D394`, 2px offset**, on every interactive element |
| Colors in code | 82 hard-coded values | Only `--hw-*` role tokens |

**Contrast check of the pairs this plan uses** (calculated with the QA skill's `contrast.py`):

| Text on background | Ratio | Use |
|---|---|---|
| Carbon `#0A0A0A` on Ivory | 18.0:1 ✔ approved | Body text |
| Burgundy on Ivory | 14.7:1 ✔ approved | Headings, links |
| Gold Text `#7D5C38` on Ivory | 5.5:1 ✔ approved | Eyebrows on light |
| Gold Text on Stone | 4.89:1 ✔ passes | Eyebrows on stone sections |
| Warm Gray `#6B5F57` on Ivory / Stone | 5.6:1 / 4.98:1 ✔ | Captions, helper text |
| Ivory on Burgundy | 14.7:1 ✔ approved | Text in the burgundy band |
| Gold Highlight `#EDCA9D` on Burgundy | 10.4:1 ✔ approved | Gold text in the band |
| Wraps Gold on Midnight | 8.5:1 ✔ approved | Footer accents |
| Carbon on Wraps Gold | 8.5:1 ✔ approved | Gold button label |
| ~~Wraps Gold on Ivory~~ | 2.1:1 ✘ forbidden | Never |
| ~~Ring Gold on Ivory~~ | 1.31:1 ✘ | Use the focus ring with an offset on light, plus a dark inner edge, so it stays visible. Confirm against `tokens.css` |

- **Done when:** no hard-coded colors remain, the page reads light, and every text pair is on the list above.

### 0.3 Measurement — _Rec 5 · audit F-009_
- **Solution:** Use privacy-friendly analytics (Cloudflare Web Analytics, no cookies). Count events for: "Book a free consultation" clicks, form submissions, tap-to-call, WhatsApp/Text taps, and email taps. Add UTM tags to the Instagram, Facebook and TikTok bio links.
- **Done when:** the owner can see weekly consultations by source.

---

## 1. Header and navigation

- **Problem** _(Opportunity 2 · Rec 2 · audit F-012, F-013)_: The header scrolls away, "Request a quote" is hidden in the mobile menu, and "Terms" sits in the main navigation while "FAQ" doesn't.
- **Leaders:** CWD keeps *Get Quote* and the phone number in the header at all times. Ziebart shows hours and directions. Wrap Bullys and CWD use service menus.
- **Solution:**
  - **Utility row** (thin, Midnight Wine, 32px): `Tampa Bay, FL` · `[phone]` · `WhatsApp` · `Hablamos español`. This is the secondary path; it never competes with the button.
  - **Main bar** (Burgundy, logo on dark per the logo rule): logo · **Work** · **Services ▾** (Fleet & commercial · Partial wraps · Color change · Wrap removal · Signs & vinyl) · **How we work** · **About** · **FAQ** · `[Book a free consultation]` (gold pill on dark).
  - **Sticky:** the header compacts to the main bar only (64px) after scrolling, and stays visible.
  - **Mobile:** logo · menu button. The CTA moves to the sticky bottom bar (section 11), so it's never hidden. The menu opens as a full-height ivory sheet that closes with Escape, keeps focus inside, and has its own Call and WhatsApp links at the bottom.
  - "Terms" moves to the footer and to a `/terms` page (section 8).
- **Done when:** the CTA is visible at every scroll position on desktop and mobile, the menu works with the keyboard, and the logo only sits on a dark background.

---

## 2. Hero — the Promise

- **Problem** _(Opportunity 2 & 5 · audit F-011, F-033, F-045)_: The headline "One standard. Across every vehicle." doesn't say what or where. The main gold button leads to the videos, not to booking. The background video frame shows a blurry arm, and the logo is repeated.
- **Leaders:** Every top site shows **its own work**, names the **city** in the headline, and has **one primary ask plus one secondary** (call or text).
- **Solution (Hermes version):**
  - **Layout:** split hero on Ivory. Text on the left (5 columns); on the right (7 columns), one strong **finished-work photo** with an optional *application reveal* (a left-to-right wipe, ≤700ms, once). We're not copying the competitors' full-screen video heroes, and the page stays light. No logo in the hero, since it's already in the header.
  - **Eyebrow** (Gold Text, Plex Mono numbering): `01  VEHICLE WRAPS · FLEET GRAPHICS · SIGNS — TAMPA BAY`
  - **H1** (Barlow Semi Condensed 700 italic, ≤10 words). Pick one:
    - **A (recommended, strongest for search):** *Vehicle wraps built to your standards in Tampa Bay*
    - B: *Your brand, applied exactly. On every vehicle.*
  - **Signature line** (directly under the H1, verbatim): **We focus on your quality exigencies.**
  - **Body (≤40 words):** "Fleet graphics, partial and full wraps, and signs, installed by a specialist with 8+ years of hands-on experience. You bring the standard; we review your specs before we quote."
  - **Buttons:** `[Book a free consultation]` (burgundy pill) + secondary text link `See the work →`.
  - **Reassurance line:** *Free · No obligation · We review your specs before quoting.*
  - **Mobile:** text first, photo below (4:3), button full-width.
- **Video:** the hero no longer autoplays a looping video. That removes the motion-without-pause issue and the mobile data cost. The process videos move to section 4, where they act as proof.
- **Placeholders:** `[PROJECT PHOTO: best finished job, sharp, daylight, 4:3 — e.g. the Corvette C8 roof and mirrors]`
- **Done when:** a first-time visitor can say what, where and what to do within 5 seconds; one primary button; the H1 contains "vehicle wraps" and "Tampa Bay".

---

## 3. Proof strip + selected work — the Proof

- **Problem** _(Opportunity 4 · Rec 4, 7, 8 · audit F-024, F-028, F-041, F-043, F-044)_: There are no reviews, no film or warranty details, and fleet claims have no fleet example. The gallery moves every 4.5 seconds without a pause button; its tabs don't actually filter; signs have no photos.
- **Leaders:** A **trust strip right under the hero** (rating, film brand, warranty, location). Portfolio cards titled **"Vehicle | Film + color"**, filterable, each with its own page. Before/after for partial wraps and removals. In Tampa, competitors use generic captions ("Corvette") and show no ratings near the top. **That's our opening.**

### 3.1 Proof strip (Stone, directly under the hero)
A spec-sheet row of four cells, with hairline dividers and Plex Mono labels:

| Label | Value |
|---|---|
| EXPERIENCE | **8+** years hands-on (the "8+" in Wraps Gold on a dark plate, or Gold Text on light) |
| MATERIAL | `[CLIENT TO SUPPLY: film brand and series, e.g. "3M 2080" — confirm; say "certified" only if true]` |
| WARRANTY | `[CLIENT TO SUPPLY: installation warranty period]` |
| PROCESS | Filmed and photographed, from prep to final trim |

- When real reviews exist, the fifth cell becomes `★ [CLIENT TO SUPPLY: Google rating] from [n] reviews` with a link to Google. **Until then, no rating appears.** We never use a placeholder rating on the live site.

### 3.2 Selected work (Ivory)
- **Eyebrow:** `02  SELECTED WORK` · **H2:** *Your standard, met on real vehicles*
- **Grid, not carousel:** six cards (3×2 desktop, 1 column mobile), with filter chips that **really filter**: All · Fleet & commercial · Partial · Color change · Removal · Signs.
- **Card anatomy (spec style):** photo (4:3, 8px radius) → title **"Vehicle | Finish — Service"** → mono spec line.
  - *Chevrolet Corvette C8 | Gloss black roof & mirrors — Partial wrap* · `FILM: [CLIENT TO SUPPLY]`
  - *Toyota Corolla | Gloss black roof — Partial wrap*
  - *Hyundai Tucson | `[CLIENT TO SUPPLY: exact color name — site says "Gloss laser flip pink", Facebook says "Space Candy Pink"]` — Full color change*
  - *BMW X1 | Gloss black hood & roof — Partial wrap*
  - *Business SUV | Printed side & hood graphics — Commercial* `[CLIENT TO SUPPLY: client permission to name the business]`
  - *Chevrolet Silverado | `[CLIENT TO SUPPLY: confirm — black hood, or hood returned to white?]` — Hood wrap*
- **"Standard met" detail (on each project page):** *Requirement → What we did → Result*, plus the detail macro shots (edges, corners, mirror caps). This is the skill's proof format, and it matches the research pattern of one page per project (good for searches like "gloss black roof wrap Tampa").
- **Before/after:** a simple side-by-side pair for wrap removal and chrome delete. A drag slider is optional later. No autoplay anywhere.
- **Fleet proof:** one short case study as soon as one is available `[CLIENT TO SUPPLY: commercial job with permission — vehicles, layout approval, timeline]`. If there isn't one yet, the fleet wording elsewhere stays modest ("Ready for fleets: one approved layout per vehicle type").
- **CTA after proof** (the skill places one here): `[Book a free consultation]` + reassurance line.
- **Done when:** no element moves on its own; filters change the visible cards; every card names vehicle, finish and service; nothing unverified appears on the live site.

---

## 4. How we work — the Process (videos live here)

- **Problem** _(Opportunity 6 · Rec 6 · audit F-035, F-050, F-057, F-061, F-062)_: The process is shown as an autoplaying 3D video carousel with tiny 9px dots, hidden controls and no captions. The "Terms of service" block does the job of a process explanation but reads like a contract.
- **Leaders:** A short numbered process with **time frames** (Wrapmate: Day 1 / Day 5 / Week 2; Tinterz: consultation → installation → follow-up).
- **Solution:**
  - **Eyebrow:** `03  HOW WE WORK` · **H2:** *We start with your brand guidelines*
  - **Six numbered steps** (the skill's sequence), mono numbers and a hairline timeline:
    1. **Your standards in:** brand guide, vehicle photos, specs, deadlines.
    2. **Proof:** layout or mock-up for your review, labeled "Concept".
    3. **Approval:** written quote and scope; nothing is scheduled until you sign off.
    4. **Production:** film ordered and, for graphics, printed to the approved file.
    5. **Installation:** surface prep and inspection, placement, trim. _(the process video sits here)_
    6. **Final QA and photo record:** walk-through with you, care guide, photos for your files.
  - **Time frames:** `[CLIENT TO SUPPLY: typical days per step]`. Show them only once confirmed (the research shows they help).
  - **Videos:** one video at a time, **paused until pressed**, with visible play/pause, native controls, captions if there's speech `[CLIENT TO SUPPLY: do the videos have voice?]`, and a one-line description. Arrows at 44px; no tiny dots.
  - **Mobile:** steps stack; the video sits under step 5 at full width (9:16, max 70vh).
- **Done when:** the steps read in under 30 seconds, the videos never autoplay with sound or loop without a pause, and every control is reachable by keyboard.

---

## 5. Services — the Capability

- **Problem** _(Opportunity 4 & 5 · Rec 7, 10 · audit F-014, F-041, F-048)_: Five of six service cards don't link anywhere, there's no price guidance, and signs have no photo.
- **Leaders:** Service cards with **"from $" prices**, each linking to its own page. Tampa competitors don't offer **packages for entry-level partial wraps**, so there's an opening there.
- **Solution:**
  - **Eyebrow:** `04  SERVICES` · **H2:** *Built to your spec, from one vehicle to a fleet*
  - **Five cards** (12px radius, hairline border, photo on top, not text over photo). Each card is fully clickable and goes to its service page:

| Card | One line | "What we check" (mono) | Price slot (D2) |
|---|---|---|---|
| Fleet & commercial graphics | One approved layout per vehicle type, applied the same way on every unit. | `LAYOUT · COLOR MATCH · PANEL SEAMS` | `[CLIENT TO SUPPLY: from $ per vehicle, or "per spec"]` |
| Partial wraps | Roof, hood, mirrors, pillars and chrome delete. | `EDGES · RELIEF CUTS · TRIM` | `[CLIENT TO SUPPLY: from $]` |
| Full color change | A complete new color, with the film named in your quote. | `PREP · COVERAGE · DOOR JAMBS (quoted separately)` | `[CLIENT TO SUPPLY: from $]` |
| Wrap removal | Old wraps and fleet graphics removed before a return or rebrand. | `ADHESIVE · PAINT CONDITION` | `[CLIENT TO SUPPLY: from $]` |
| Signs & vinyl graphics | Window, wall and business signage. | `SIZE · SURFACE · PLACEMENT` | `[CLIENT TO SUPPLY: from $]` |

  - **Partial-wrap packages** (from the research; only if the client wants them): *Roof · Hood · Chrome delete · Mirror caps · Blackout*. Shown as a compact row of pills on the Partial wraps page, each with a client-supplied price.
  - **Personal vehicles path (D1):** a one-line link under the grid: *Wrapping your own car? See partial wraps and color changes →*
  - **Signs card photo:** `[PROJECT PHOTO: a finished sign or window graphic]`. Until one exists, the card uses a neutral labeled placeholder in design files and is **left out** of the live site.
- **Done when:** every card links to a page; no price appears unless supplied; signs have a real photo or aren't shown.

---

## 6. About — the Story

- **Problem** _(Opportunity 4 · Rec 7 · audit F-025)_: The site promises "quality with a name behind it", but there's no name, face or story.
- **Leaders:** Years in business stated plainly, a *Meet the team* section, shop photos, family-owned or owner-run messaging.
- **Solution:**
  - **Eyebrow:** `05  ABOUT` · **H2:** *8+ years at the panel, now on our own*
  - **Body (from the skill's brand facts only):** "Hermes Wraps is built on 8+ years of hands-on work, first alongside talented mentors and now as its own company. That means one person is accountable for your project, from the first spec review to the final walk-around. We're ready for new challenges, and we want to prove it on yours."
  - **Owner card:** photo at work, name, role. `[CLIENT TO SUPPLY: owner name, photo, 2–3 sentence story]`
  - **Location and hours:** `[CLIENT TO SUPPLY: shop, mobile service or both · general area · hours]`. This answers the "drop-off" question raised in the current terms.
  - The "new company" angle is framed as **focus and drive, never inexperience** (skill §4).
- **Done when:** a visitor can name the person behind the work and knows where the work happens.

---

## 7. Risk removal — consultation explainer, FAQ, terms, reviews

- **Problem** _(Opportunity 4 · Rec 7 · audit F-035, F-039, F-029)_: The FAQ dodges the questions buyers care about most (price, time, lifespan, warranty). The terms sit in the main page and navigation and read like a contract.
- **Leaders:** FAQs answering **cost, Florida sun and UV, lifespan, leased cars, paint safety, aftercare** (research Must-have #10), the warranty length stated plainly, and reviews tagged with vehicle and service.

### 7.1 "What happens in your consultation" (the skill requires this wherever the CTA is the focus)
Three steps in a row (mono numbers):
1. **Share your requirements:** vehicle or fleet, brand files, photos, timeline.
2. **We review your standards and scope**, and point out anything (like paint condition) that could affect the result.
3. **You get a clear plan and a written quote.** `[CLIENT TO SUPPLY: response time, e.g. "within 1 business day"]`

### 7.2 FAQ (Ivory, accordion with clear plus/minus icons hidden from screen readers)
Keep the six current questions, rewrite the vague answers, and add:
- *How much does a wrap cost?* `[CLIENT TO SUPPLY: ranges or "priced per spec"]`
- *How long does installation take?* `[CLIENT TO SUPPLY]`
- *How long will the film last in the Florida sun?* `[CLIENT TO SUPPLY: per film data]`
- *Will a wrap damage my paint?* (honest answer about paint condition, already in the terms)
- *What warranty do I get?* `[CLIENT TO SUPPLY]`
- *Do you work in Spanish?* Sí. Escríbenos en español.

### 7.3 Terms
Move the eight terms to a `/terms` page, linked from the footer and the form. On the homepage they are summarized by step 3 of the process ("Nothing is scheduled until you sign off").

### 7.4 Reviews (built now, switched on when real reviews exist)
- **Process first:** set up or claim the Google Business Profile and send every finished customer a direct review link (Rec 4).
- **Component:** quote, name, **vehicle + service tag** (the research's best practice; Tampa competitors don't do this), source and date, and an owner reply if there is one. Hidden on the live site until there are at least `[CLIENT TO SUPPLY: minimum, e.g. 3]` real reviews. **No invented testimonials.**

- **Done when:** the four big questions (cost, time, lifespan, warranty) have real answers or an honest "per spec" note.

---

## 8. Consultation form — the conversion point

- **Problem** _(Opportunity 3 · Rec 3 · audit F-015 to F-022)_: Photos can't be attached. "Send by email" fails silently on computers without an email app. Two answers come pre-filled with "Business / fleet" and "Commercial / fleet graphics". "Copy details" is a dead end, and WhatsApp is only reachable through the form.
- **Leaders:** A **short form that asks for the vehicle first**, with **photo upload** and a **stated response time** (Purple Flare, Tinterz). Wrapmate saves progress across steps.
- **Solution:**
  - **Section:** Stone background. **Eyebrow** `06  BOOK A FREE CONSULTATION` · **H2:** *Tell us the standard your project needs to meet*
  - **Fields** (skill's list, adjusted for D1; labels above inputs; none pre-filled):
    - **Project type** (required, segmented buttons, not a dropdown): Business / fleet · Personal vehicle · Signs
    - **Name** (required)
    - **Company** (required for Business / fleet; hidden for Personal)
    - **Email** (required; "Work email" for business)
    - **What standards does this project need to meet?** (required, short text: vehicle(s), finish, brand requirements)
    - _Optional, grouped under "Helpful details":_ phone · number of vehicles · timeline · **photos and brand files** (up to `[n]` files, drag-and-drop or camera on mobile)
    - If the customer gives a phone number and wants text replies: a short consent checkbox `[CLIENT TO CONFIRM wording]`
  - **Submit:** `[Book a free consultation]` + reassurance line.
  - **Real submission (D5):** the form sends to the Cloudflare Worker, which emails the request **with the photos attached** to the business inbox and returns a confirmation. No email app is needed.
  - **States:**
    - **Success:** "Thanks, [name]. We'll review your specs and reply within `[CLIENT TO SUPPLY]`. Next: we'll confirm scope and send a written quote." (Restates the next steps, as the skill asks.)
    - **Error:** a plain message, the entered data is kept, and the alternative paths are listed: call, WhatsApp, email.
    - **Validation:** inline, in text and with an icon, not color alone.
  - **Secondary path beside the form:** "Prefer to text? Message us on WhatsApp" (opens a pre-filled message in English or Spanish) · phone · email.
  - **Privacy:** replace "Nothing is stored on this website" with "We use your details only to answer this request. `[Privacy policy]`".
- **Done when:** the request arrives with photos; nothing is pre-selected; a failure never looks like a success; the form takes under 2 minutes on a phone.

---

## 9. Closing band — the Close

- **Problem** _(skill structure · audit F-023)_: Five different button labels ("Request a quote", "Start the conversation", "Ask about a sign", "Escribir mensaje"…) all point to the same form.
- **Leaders:** Repeat **one** ask before the footer.
- **Solution:** the page's **one Burgundy band**.
  - Signature line (verbatim, display size, Ivory): **We focus on your quality exigencies.**
  - Line (Gold Highlight): "Send us your standard. We'll show you how we'll meet it."
  - `[Book a free consultation]` (gold pill, carbon label) + reassurance line.
- **Done when:** this is the only dark band in the body of the page, and the signature line isn't visible in the same viewport as the footer signature (add spacing, or use the footer's short version as the skill allows).

---

## 10. Footer

- **Problem** _(audit F-026, F-027, F-076, F-078)_: There's no address area, hours or legal pages; the footer mentions a domain that doesn't load; and a YouTube link points nowhere.
- **Leaders:** Address, hours and map; services; areas served; socials (research Must-have #7).
- **Solution** (Midnight Wine):
  - Logo + signature line (verbatim, small): **We focus on your quality exigencies.**
  - **Services** (links to the five service pages) · **Company** (Work, How we work, About, FAQ) · **Contact** (phone, WhatsApp, `hello@hermeswraps.com`, `[CLIENT TO SUPPLY: area/address and hours]`) · **Areas served** `[CLIENT TO SUPPLY: confirm — e.g. Tampa, Brandon, …]` · socials (Instagram, Facebook, TikTok; YouTube only when the channel exists).
  - `Hablamos español` · `Terms` · `Privacy` · © year.
- **Done when:** every link works and the area served is consistent with Google Business Profile.

---

## 11. Sticky mobile bar

- **Problem** _(Opportunity 2 · Rec 2 · audit F-012, F-022)_: On a phone the page is about 20 screens long, and there's no way to call or message from wherever the visitor is.
- **Leaders:** Wrap Bullys' sticky **Call · Text · Quote** bar; CWD's text bubble.
- **Solution (translated, not copied):** a **slim bar that appears once the visitor scrolls past the hero** (the skill's rule):
  - `[Book free consultation]` (the skill's short form; Burgundy pill, fills the remaining width) + two **44px icon buttons**: **Call** and **WhatsApp**, each with a text label for screen readers.
  - Hides when the form is on screen and when the menu or a video is open; respects the iPhone safe area.
- **Done when:** one tap reaches the form, a call or WhatsApp from any point on the page, and the bar never covers form fields.

---

## 12. Spanish — _Opportunity 5 · Rec 10 · audit F-038_

- **Now:** "Hablamos español" in the header utility row and footer; a Spanish pre-filled WhatsApp message; form helper text "Puedes escribir en español."
- **Later:** a `/es/` homepage with the same sections and translated copy. **The signature line and the button label follow the client's decision** (skill: signature verbatim; the CTA wording rule is written for English). `[CLIENT TO CONFIRM: Spanish CTA wording, e.g. "Agenda una consulta gratis"]`
- The research confirms **no Tampa competitor offers Spanish**, so this is a real advantage.

---

## 13. Beyond the homepage — site structure

- **Problem** _(Opportunity 5 · Rec 10 · audit F-005)_: Everything lives on one page, so the site can't appear for specific service searches.
- **Leaders:** Pages organized **by service, by vehicle make and by area**, plus cost guides.
- **Solution (in order):**
  1. **Service pages (Rec 10):** Fleet & commercial · Partial wraps (with packages) · Full color change · Wrap removal · Signs & vinyl. Each follows the same order as the homepage (promise → proof → process → FAQ → consultation).
  2. **Project pages** for each portfolio item: "Requirement → What we did → Result" + detail shots.
  3. **Book a consultation page** (signature line in its intro, as the skill requires) and **How we work**, **About**, **FAQ**, **Terms**, **Privacy**.
  4. **Later:** a "Car wrap cost in Tampa" guide (only with real price ranges), area pages `[CLIENT TO SUPPLY: areas actually served]`, and make pages once there are enough projects per make.

---

## 14. Cross-cutting: accessibility and speed — _Opportunity 6 · Rec 6, 9_

| Issue (audit) | Fix in the new build |
|---|---|
| Gold labels fail contrast (F-054) | Gold Text `#7D5C38` on light (5.5:1 / 4.89:1) |
| Moving content without pause (F-057, F-043) | No autoplay; grid instead of carousel; videos play on demand |
| No custom focus style (F-055) | Ring Gold 2px, 2px offset, on everything |
| Tiny controls (F-061) | Every control ≥ 44px |
| No captions (F-062) | Captions or a text description for each video |
| Lightbox focus escapes (F-060) | Native modal dialog for image zoom |
| Heavy hero video, full-size images (F-068, F-069) | No hero video; images served in modern formats and several sizes; measure with PageSpeed after launch |
| Reduced motion | Reveals become fades or nothing under `prefers-reduced-motion` |

---

## 15. Research patterns: adopted, adapted, not adopted

| Research pattern | Status | How |
|---|---|---|
| 1. Real work + city in the hero, one clear ask | **Adopted** | Section 2 (H1 with "Tampa Bay", own photo, one primary) |
| 2. Contact from any scroll position | **Adapted** | Sticky header + mobile bar; text/WhatsApp as secondary (D3) |
| 3. Short form, vehicle first, photos, response time | **Adopted** | Section 8; response time `[CLIENT TO SUPPLY]` |
| 4. Rating near the top, reviews with vehicle + service | **Adapted** | Proof strip slot + review component, **only with real reviews** |
| 5. Portfolio as product, "Vehicle \| Film" cards, project pages | **Adopted** | Section 3 + project pages |
| 6. Service / make / area structure | **Phased** | Services now, areas and makes later |
| 7. Film brand + warranty | **Adopted, client data needed** | Proof strip and FAQ |
| 8. Price anchors | **Pending D2** | Price slots, client numbers only |
| 9. 3-step process with timeline | **Adapted** | Skill's 6-step process + 3-step consultation explainer |
| 10. Human, local signals (years, team, hours, languages) | **Adopted** | 8+ years, owner card, hours, Spanish |
| 11. Offers and urgency | **Not adopted** | Skill: no discounts or price claims (D4) |
| 12. Visualizer / concept tool | **Not adopted** | Copies a competitor's signature feature; low return for now (D4) |
| Mega-menu, "I want the same →" CTA, award badges | **Not adopted** | Copying distinctive elements, a different CTA wording, or proof we don't have |

---

## 16. Report recommendations → where they're solved

| Report rec | Section(s) | Timing |
|---|---|---|
| 1. Connect hermeswraps.com | 0.1 | Quick win |
| 2. One-tap Call, WhatsApp and booking on phones | 1, 2, 11 | Quick win |
| 3. Make the form reliable | 8 | Quick win |
| 4. Start collecting reviews | 7.4, 3.1 | Quick win |
| 5. Measure calls, messages, requests | 0.3 | Quick win |
| 6. Easier for everyone to read and use | 0.2, 4, 14 | Quick win |
| 7. Answer the big questions | 3.1, 5, 6, 7 | Next |
| 8. Show more work, starting with business clients | 3.2 | Next |
| 9. Lighten the site for mobile | 2, 14 | Next |
| 10. Service pages + Spanish | 12, 13 | Later |

---

## 17. Everything the client needs to supply

1. Domain registrar access for hermeswraps.com, and the business email to use.
2. Owner name, photo at work, and a 2–3 sentence story.
3. Shop, mobile or both; general area; hours; areas served (confirm Brandon).
4. Film brand and series; whether "certified" applies; the standard warranty period.
5. Price ranges or "from" prices per service, or a decision not to publish them (D2).
6. Typical timeline per step; response time for consultations.
7. Permission to name business clients (e.g. the Business SUV client); any fleet job for a case study.
8. Photos: best finished job for the hero; sign or window work; before/after for removal and chrome delete; detail close-ups.
9. Corrections: the Tucson color name; the Silverado hood story.
10. Do the process videos have voice (for captions)?
11. Google Business Profile access; minimum number of reviews before showing them.
12. Spanish CTA wording; who answers messages in Spanish.
13. Decisions D1–D6 above, and the missing brand files (D7).

---

### Suggested build order
1. **Week 1:** Foundations (0.1–0.3) + header (1) + hero (2) + sticky bar (11) + form (8).
2. **Week 2:** Proof (3) + process (4) + services (5) + closing band (9) + footer (10).
3. **Weeks 3–4, as client content arrives:** About (6), FAQ and reviews (7), service and project pages (13), then Spanish (12).

After each section is built, run the **quality-insurance** check (drift scan, 375px and 1280px renders, checklist) before moving on.
