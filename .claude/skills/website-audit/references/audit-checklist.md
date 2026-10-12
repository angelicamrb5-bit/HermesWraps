# Audit checklist (prompts, not a form)

Use these as prompts to look harder. For each area, write findings in the F-### format, plus loose notes. If an area truly doesn't apply, write "N/A because …". Tag certainty on everything (`[VERIFIED]`, `[LIKELY]`, `[ASSUMPTION]`, `[UNVERIFIED]`, `[QUESTION]`).

---

## 1. First impression / 5-second test
- Within 5 seconds above the fold (mobile AND desktop): what is this, who is it for, why should I care, what do I do next?
- Is the value proposition specific or generic ("We deliver quality solutions")?
- Does the hero image/video support the message or just decorate?
- Anything that looks broken, unfinished, stock-y, dated, or off-brand?

## 2. UX (general)
- Cognitive load: too many choices, competing CTAs, walls of text, jargon.
- Consistency of patterns (same action looks/behaves the same everywhere).
- Feedback for every action (hover, focus, pressed, loading, done).
- Error prevention and recovery; undo; confirmations for destructive actions.
- Dead ends: pages with no next step.
- Surprises: auto-playing media, unexpected new tabs, popups on load, scroll-jacking, layout shift.

## 3. UI design
- Typography: number of families/weights/sizes, line length (45–75ch), line height, contrast, hierarchy of H1–H6, orphan/widow issues, all-caps overuse.
- Color: palette size, purpose consistency (is "primary" always the same?), brand fit, contrast.
- Spacing rhythm: consistent scale or random px values? Cramped/loose areas.
- Imagery & icons: quality, resolution, consistent style, cropping, stretched/pixelated assets, icon set mixing.
- Buttons/links: clear affordance, consistent shapes, sizes, states (hover/focus/active/disabled/loading).
- Polish: misalignment, uneven gutters, inconsistent radii/shadows/borders, z-index overlaps.

## 4. Layout
- Grid use, max width, alignment, gutters; what happens at very wide (1920+, 2560) and very narrow (320) widths.
- Content order makes sense? Section lengths balanced?
- Sticky elements eating viewport (headers, banners, cookie bars, chat widgets).
- Horizontal scroll, overflowing text, clipped content, overlapping elements.

## 5. Visual hierarchy
- What's the most visually dominant thing on each key page — is it the most important?
- One clear primary action per view?
- Headings that look like body text or body text that looks like headings.
- Scannability: subheads, bullets, bold, chunking.

## 6. Navigation
- Primary nav: number of items, labels clear and user-language (not internal jargon), active state, order by priority.
- Mobile nav: hamburger usability, focus trapping, close button, scroll lock, tap targets, nested menus.
- Footer: useful links, contact, legal, social, duplication with header.
- Breadcrumbs, back paths, search (exists? works? empty/no-results state?).
- Logo links home? Current page indicated? Broken/orphan links.

## 7. Information architecture
- Page inventory and hierarchy (draw it as a tree). Depth: key content within 3 clicks?
- Duplicate/overlapping pages, thin pages, orphan pages (in sitemap/code but not linked).
- Naming consistency between nav, page titles, H1s, URLs.
- URL structure: readable, consistent, trailing slashes, case, parameters.
- Missing pages users expect for this type of site (pricing, FAQ, about, contact, shipping/returns, privacy, terms, cookie policy, accessibility statement, careers, case studies/portfolio, blog, help/docs, status, 404/500).

## 8. User journeys
- Define 3–6 realistic personas × goals. Walk each step by step on mobile and desktop.
- Count steps/clicks/scrolls; note where info is missing at the moment of decision.
- Drop-off risk points (`[ASSUMPTION]` unless analytics provided).
- Returning-user journeys (login, reorder, support, account).
- Cross-device/cross-channel handoffs (email links, WhatsApp, phone, maps, social).

## 9. Content
- Accuracy, freshness (dates, © year, "new" items that are old), consistency of facts (prices, hours, addresses, phone numbers across pages).
- Placeholder text, lorem ipsum, TODOs, test data, broken embeds, typos, grammar, mixed languages.
- Reading level, jargon, wall-of-text, passive voice, vague claims.
- Content gaps: questions users will have that aren't answered (pricing, process, timelines, materials, guarantees, location/service area, FAQ).
- Media: captions, transcripts, alt text quality (not just presence).

## 10. Messaging
- Is the core promise consistent across hero, meta description, social preview, about page?
- Benefits vs features; customer's language vs company's language.
- Differentiation: why this over alternatives? Is it stated?
- Tone consistency; brand voice.
- Objection handling (price, risk, time, quality, trust).

## 11. CTAs
- Inventory every CTA per page: label, style, destination, position, repetition.
- Verb-first, specific labels ("Get a free quote" vs "Submit"/"Learn more"/"Click here").
- Competing primary CTAs; CTA that goes nowhere or to the wrong place.
- CTA visible above the fold on mobile? Sticky CTA appropriate?
- Secondary/low-commitment options for not-ready users (newsletter, guide, pricing view).

## 12. Trust
- Social proof: reviews, testimonials (real names/photos/sources?), ratings, client logos, case studies, before/after, counts — verifiable or vague?
- Credentials: certifications, guarantees, warranties, awards, years in business, team photos, real address, phone, business registration.
- Security cues: HTTPS everywhere, payment badges (only where honest), privacy policy, clear data use near forms.
- Red flags: broken links, stock photos of "team", outdated content, missing contact info, typos, aggressive popups, fake urgency.
- Third-party presence: Google Business profile, social links (do they work and are they active? `[UNVERIFIED]` unless checked).

## 13. Conversion
- What are the conversion events? (call, form, booking, purchase, signup, WhatsApp, email). `[ASSUMPTION]` if not stated.
- Friction per conversion path: fields, steps, required account, surprise costs, unclear next step.
- Pricing transparency; quote process clarity; "what happens next" after submission.
- Tracking: analytics/pixels present in code/network? Events on key actions? (Don't invent data; just note presence/absence.)
- Opportunities: lead magnets, exit paths, retargeting hooks, urgency only if honest, cross-sell, reassurance near CTA.

## 14. Accessibility (WCAG 2.2 AA as reference)
- Semantics: landmarks (`header`, `nav`, `main`, `footer`), one H1, logical heading order, lists as lists, buttons vs links used correctly.
- Keyboard: everything reachable and operable, visible focus, logical order, no traps, skip link, menus/modals/accordions/carousels operable, Escape closes overlays.
- Images: meaningful `alt`, decorative `alt=""`, text in images, SVG titles/aria-hidden.
- Color contrast (text 4.5:1 / large 3:1 / UI components 3:1), info not by color alone.
- Forms: labels (not placeholder-only), required indicated, errors announced and linked (`aria-describedby`), autocomplete attributes, input types.
- ARIA misuse (roles on wrong elements, `aria-hidden` on focusable, redundant ARIA).
- Motion: `prefers-reduced-motion`, auto-play, carousels with pause.
- Zoom 200%/400% reflow, text spacing, `lang` attribute, page titles, link text out of context, target size (24×24 min).
- Media: captions, transcripts, no flashing.

## 15. Mobile responsiveness
- Test widths: 320, 375/390, 414, 768, 1024, 1280, 1440, 1920. Landscape mobile.
- Viewport meta, no horizontal scroll, tap targets ≥ 44px ideally, font ≥ 16px in inputs (iOS zoom), sticky elements, image cropping, hidden content on mobile, mobile-only bugs.
- Click-to-call, click-to-map, click-to-WhatsApp/email on mobile.
- Performance on mobile (heavy hero video/images).

## 16. Forms
- Inventory each form: purpose, fields, required/optional, input types, autocomplete, validation (client + server?), error messages, success state, spam protection, where data goes (`action`, endpoint, third party) — **do not submit**.
- Field count vs necessity; asking for data too early; unclear labels; long dropdowns.
- Privacy/consent text, GDPR/marketing opt-in clarity.
- What happens on failure/network error? Double-submit protection? Disabled-state clarity?

## 17. Interactions & motion
- Hover/focus/active states, transitions, animations (purposeful or distracting?), scroll effects, parallax, carousels/sliders (usable? auto-advance?), modals/popups (timing, dismissible, focus handling), accordions, tabs, tooltips, lightboxes, maps, embeds, chat widgets.
- JS-dependence: does the page work without JS? What breaks?
- Layout shift caused by late-loading elements.

## 18. States: empty, loading, error, success (and more)
For every dynamic area (forms, search, filters, lists, cart, account, embeds, maps):
- Loading: skeletons/spinners? Layout stable? Timeouts?
- Empty: helpful message + next action, or blank?
- Error: human message, recovery path, retains input? Network/offline errors?
- Success: confirmation, what happens next, email confirmation mentioned?
- Also: partial data, disabled, permission denied, expired session, 404, 500, maintenance, slow 3G, ad-blocker breaking things.
- Code-only: are these states implemented, or only the happy path?

## 19. SEO
- Per page: `<title>` (unique, ~50–60 chars), meta description (unique, ~150–160), one H1, heading outline, canonical, `robots` meta, `hreflang` if multilingual, `lang`.
- Open Graph / Twitter cards (title, description, image size), favicon set, manifest.
- Structured data (Organization, LocalBusiness, Product, BreadcrumbList, FAQ, Article, Review) — present, valid-looking, truthful?
- robots.txt, sitemap.xml (exists, matches real pages, no 404s/redirects in it), redirects (http→https, www), duplicate content, parameter URLs, pagination.
- Internal linking, anchor text, orphan pages, broken links, image alt/filenames, URL slugs.
- Rendering: content in HTML or only after client-side JS? Indexability of key content.
- Local SEO (if local business): NAP consistency, map embed, service-area pages, Google Business profile link.
- Content depth vs intent for target queries (`[ASSUMPTION]` about keywords unless provided).

## 20. Performance
- Lighthouse/PSI or WebPageTest numbers if available; otherwise `[UNVERIFIED]` and estimate from evidence.
- Page weight, request count, largest assets, image formats (WebP/AVIF?), responsive `srcset`/`sizes`, lazy loading, hero image priority.
- Fonts: count, weights, `font-display`, preload, self-hosted vs Google.
- JS/CSS: bundle size, unused code, render-blocking resources, third-party scripts (tags, chat, embeds, pixels), hydration cost.
- Caching headers, compression (gzip/br), CDN, HTTP/2/3.
- Core Web Vitals risks: LCP element, CLS sources, INP-heavy handlers.

## 21. Technical issues
- Console errors/warnings, failed network requests (4xx/5xx), mixed content, CORS errors, broken images/links, redirect chains.
- Security headers (HSTS, CSP, X-Content-Type-Options, frame-ancestors, Referrer-Policy, Permissions-Policy), exposed `.git`/`.env`/source maps/directory listings (check only with harmless GET on obvious paths; don't probe aggressively).
- Cookies & consent: banner present? Scripts load before consent? `[LIKELY]`/`[UNVERIFIED]` legal implications — not legal advice.
- Browser compatibility hints (CSS features without fallbacks).
- Outdated libraries/CMS versions visible in source.

## 22. Code quality (if codebase in scope)
- Structure, naming, file sizes, separation of concerns, dead code, duplicated logic, magic numbers, hard-coded strings/content (i18n readiness), config/env handling, secrets committed.
- Types/lint/test coverage present? CI? Build reproducible?
- Dependency health: outdated, unused, heavy, vulnerable (`npm audit` only if safe/offline-friendly; mark `[UNVERIFIED]` otherwise).
- Accessibility and SEO patterns at code level (reusable components that bake in good/bad patterns).
- Error handling, logging, analytics wiring.
- README/docs/onboarding quality.

## 23. Design-system consistency
- Tokens: count distinct colors, font sizes, font weights, line heights, spacing values, radii, shadows, breakpoints, z-indexes. Table them. Flag near-duplicates (#333 vs #343434).
- Components: variants of the same thing (buttons, cards, headings, section wrappers, inputs) — list them, where they appear, and how they differ.
- Documented system (Storybook, Figma, style guide)? Drift between it and production?

## 24. Repeated components
- Inventory repeated UI blocks (hero, feature grid, testimonial, CTA band, FAQ, pricing card, footer CTA, contact block, gallery).
- Where each appears, which copies diverge, which should be one shared component, which are copy-pasted in code.
- Repetition from a user POV: same CTA band 4× on a page? Same testimonial everywhere?

## 25. Missing pages or states
- Expected-but-missing pages (see IA list), states (see §18), features (search, filtering, language switch, dark mode only if relevant, account recovery), metadata (OG images, favicon sizes), legal pages, accessibility statement, custom 404/500.

## 26. Confusing decisions
- Things that made you stop and think "why?". Odd labels, odd ordering, inconsistent behaviour, features that seem to fight the main goal, design choices that look accidental. Write them as questions where intent is unknown.

## 27. Potential opportunities
- Quick wins (S effort, visible impact), bigger bets, content ideas, SEO content gaps, conversion experiments (frame as hypotheses, no invented uplift), automation, personalization, partnerships, reviews collection, local SEO, email capture, retargeting, accessibility as differentiator.

## 28. Legal / compliance hints (not legal advice)
- Privacy policy, terms, cookie consent, accessibility statement, required business info for the region, consent on forms, age gates if relevant. Mark everything `[UNVERIFIED]` legally.

## 29. Analytics & measurement
- What tracking exists (GA4, GTM, Meta Pixel, Hotjar, etc. — from code/network)? Key events instrumented? Consent integration?
- What should be measured to validate the findings in this report? (Turn assumptions into measurable questions.)

## 30. Anything else
- Internationalization, localization, currency/units, time zones.
- Print styles, email templates, PWA/offline, social share previews, embed behaviour.
- Content governance: who updates what, how (CMS?), likelihood of rot.
