---
name: website-audit
description: Deep, read-only, intentionally messy first-pass audit of a website (live URL), a local web codebase, or both. Produces a single very detailed `website-audit.md` covering UX, UI, layout, hierarchy, navigation, IA, user journeys, content, messaging, CTAs, trust, conversion, accessibility, mobile, forms, interactions, states (empty/loading/error/success), SEO, performance, technical issues, code quality, design-system consistency, repeated components, missing pages and opportunities. Use when the user asks to audit, review, critique, tear down or assess a website, landing page, web app or front-end codebase, or invokes /website-audit. Never modifies the site or code.
---

# Website audit (messy first pass)

Goal: capture **as much useful, evidenced information as possible** about a website and/or its codebase in one Markdown file, `website-audit.md`. This is a raw working document, not a client deliverable. Breadth and detail beat polish. The user will refine and restructure it later.

## Hard rules

1. **Read-only.** Do not edit, fix, refactor, format, commit or deploy anything in the audited site or codebase. Do not submit real forms, create accounts, place orders, send messages or trigger emails on a live site. The only file you create in the project is `website-audit.md` (plus optional screenshots/evidence under `website-audit-evidence/`, only if the user agrees or it's clearly useful; mention it).
2. **No invented facts.** No made-up analytics, traffic, conversion rates, revenue, user research, competitor data or business goals. If something matters but can't be checked, write it as a question or an assumption.
3. **Label every claim's certainty.** Use these tags inline:
   - `[VERIFIED]` — directly observed (page content, code, network response, tool output). Cite where.
   - `[LIKELY]` — strong inference from evidence; say what evidence.
   - `[ASSUMPTION]` — reasonable guess, not checked. Say why it's assumed.
   - `[UNVERIFIED]` — couldn't check (tool unavailable, auth wall, blocked, out of scope). Say what would verify it.
   - `[QUESTION]` — needs input from the owner/team.
4. **Messy is fine, wrong is not.** Duplicates, overlaps, half-thoughts, rough ideas and TODOs are welcome. Don't delete detail to make it tidy. Do not soften or omit real problems.
5. Write the report in the language the user is using with you, unless they ask otherwise.

## Step 0 — Figure out the scope

From the request, work out which of these applies, and ask only if it is genuinely unclear:

- **Live site only** — a URL was given.
- **Codebase only** — the current repo / a path is a web project (look for `package.json`, `index.html`, framework configs, `src/`, `app/`, `pages/`, templates, CMS themes, `.webflow`, etc.).
- **Both** — URL + code. Cross-reference: what's in code but not live, live but not in code, env differences.

If the current directory has no web code and no URL was given, ask for a URL or path (one short question). Record the scope, date, tools used and limits at the top of the report.

Also note anything you can infer about the business/purpose (what is sold, to whom, primary conversion), labeled with certainty. If the primary goal is unclear, list candidate goals as `[ASSUMPTION]` and audit against them.

## Step 1 — Gather evidence (use whatever tools exist; degrade gracefully)

Prefer real evidence over opinion. Use the best available option for each, and log which tools you used and which weren't available in the report's "Method & limits" section.

### Live site
- **Fetch pages**: WebFetch, Firecrawl (`firecrawl_scrape` with `markdown`, `links`, `html`, `screenshot`, `branding` formats), or `curl -sL`. Start with home, then follow primary nav, footer, and every key journey page (product/service, pricing, about, contact, blog/article, legal, checkout/booking/signup entry, 404).
- **Site discovery**: `/robots.txt`, `/sitemap.xml` (and sitemap index), `/favicon.ico`, `/manifest.json`/`site.webmanifest`, `/.well-known/security.txt`, a deliberately bad URL to see the 404, `http://` → `https://` and `www`/non-`www` redirects.
- **Headers**: `curl -sIL <url>` for status codes, redirects chains, caching, compression, HSTS, CSP, X-Frame-Options, Referrer-Policy, Permissions-Policy, server/tech fingerprints.
- **Rendered capture**: if Node + Playwright are available, run the bundled script (see below) for screenshots at mobile/tablet/desktop, console errors, failed requests, headings, meta, links, images, forms and basic a11y signals. Look at the screenshots (Read the PNGs) — visual findings must come from looking, not guessing.
- **Optional extras if available** (don't install heavy things without asking): `npx lighthouse` / PageSpeed Insights API, axe-core via Playwright, `npx pa11y`. If not available, mark perf/a11y scores `[UNVERIFIED]` and do the manual checks.

#### Bundled capture script
`scripts/capture.mjs` (in this skill's directory) — read-only Playwright crawl.

```bash
# find the skill dir, then:
node <skill-dir>/scripts/capture.mjs <url-or-file> [more urls...] --out website-audit-evidence [--max 15] [--crawl]
```

- Writes `summary.json` and screenshots (`<slug>-mobile.png`, `-tablet.png`, `-desktop.png`, full-page) to `--out`.
- `--crawl` follows same-origin links from the first URL up to `--max` pages.
- It needs the `playwright` package resolvable from Node (global install or local `node_modules`). If it fails because Playwright/Chromium is missing, note it and fall back to fetch-based evidence; don't spend long installing. If a system Chromium exists, set `CHROMIUM_PATH=/path/to/chromium`.
- It never clicks submit buttons or fills forms.
- Ask before writing the evidence folder into a repo the user cares about; otherwise put it in a scratch/temp dir and reference paths in the report.

### Codebase
- Inventory: framework, build tool, package manager, routing, styling approach (CSS/SCSS/Tailwind/CSS-in-JS), component library, CMS, analytics/tag scripts, i18n, test setup, lint/format config, CI, deploy config, env files (don't print secrets — just note if secrets look committed).
- Map **routes/pages** and **components**; list which components repeat and where near-duplicates exist (e.g. three slightly different Button/Card/Hero implementations).
- Grep for signals, e.g.: `TODO|FIXME|HACK|XXX`, `console.log`, `lorem|ipsum|placeholder|coming soon`, `alt=""`/missing `alt`, `onClick` on `div`/`span`, `outline: none`, `tabindex="[1-9]`, hard-coded colors/px font sizes/z-index values, `!important`, inline styles, `dangerouslySetInnerHTML`/`innerHTML`/`v-html`, `target="_blank"` without `rel`, `http://` assets, huge images in `public/`/`static/`, unused deps, very large files/components.
- States: for each data-driven view/form, check whether loading, empty, error, success, disabled, offline, permission/auth and 404/500 states exist in code.
- Design tokens: is there a single source of truth (theme file, CSS variables, Tailwind config)? Count distinct colors, font sizes, spacing values, radii, shadows, breakpoints actually used.
- SEO in code: per-route titles/descriptions, canonical, OG/Twitter tags, structured data, sitemap/robots generation, `lang` attribute, SSR/SSG vs client-only rendering.
- Perf in code: image formats/sizes, lazy loading, font loading (`font-display`, preload), bundle-heavy deps, third-party scripts, render-blocking CSS/JS, caching config.
- You may run the project's existing read-only checks if cheap and safe (`npm run lint`, `tsc --noEmit`, `npm run build` into a temp dir). Don't install new deps or change lockfiles without asking. Record outputs.

### Both
Compare live vs code: pages missing in one, content drift, features behind flags, env-specific scripts, broken deploy assumptions.

## Step 2 — Audit every area

Go through **every** area in `references/audit-checklist.md` (read it). The checklist is prompts, not a form — skip what truly doesn't apply but say "N/A because …". Look for the same issue from multiple angles; overlapping findings are fine (cross-reference IDs).

Also walk **user journeys** end to end, as specific personas with specific goals (e.g. "first-time mobile visitor wants a price", "returning customer wants to contact support", "keyboard-only user wants to book"). For each journey: steps, friction, dead ends, missing info, number of clicks/scrolls, where they might drop off and why (`[ASSUMPTION]` unless evidenced).

## Step 3 — Write findings

Every finding uses this shape (fill as much as you can; write "?" or "unknown" rather than dropping a field):

```markdown
#### F-023 · Primary CTA below the fold on mobile  `[VERIFIED]`
- **Area(s):** Conversion, Mobile, Visual hierarchy
- **What I noticed:** …
- **Where:** URL(s) / route / file:line / component / viewport / screenshot path
- **Evidence:** quote, selector, code snippet, tool output, measurement
- **Why it may be a problem:** …
- **User impact:** …
- **Business impact:** … (no invented numbers)
- **Severity:** Critical | High | Medium | Low | Note — plus one line why
- **Effort guess:** S | M | L  `[ASSUMPTION]`
- **Possible solution(s):** option A / option B, trade-offs
- **Implementation notes:** files/components to touch, gotchas, dependencies, tokens to use
- **Related:** F-007, F-031
- **Investigate further / open questions:** …
```

Severity guide:
- **Critical** — blocks a core task or conversion, legal/accessibility blocker (e.g. form can't be submitted, checkout broken, keyboard trap, site down on mobile), security exposure.
- **High** — major friction or trust/SEO damage on key pages; WCAG A/AA failures on key flows.
- **Medium** — noticeable friction, inconsistency, or missed opportunity on important pages.
- **Low** — polish, minor inconsistency, edge cases.
- **Note** — observation, idea, or question; not necessarily a problem.

Number findings sequentially (`F-001` …) across the whole report so they can be referenced and later re-sorted.

## Step 4 — Assemble `website-audit.md`

Use the skeleton in `references/report-template.md`. Save to the project root (or the path the user specified). If a `website-audit.md` already exists, don't overwrite silently — ask, or write `website-audit-<YYYY-MM-DD>.md`.

The report should be **long**. Include tables (page inventory, component inventory, token counts, meta tag table, heading outlines, link/status table, finding index), raw notes, quotes of copy, screenshots references, and a "parking lot" of rough ideas and unanswered questions. Overlap is OK.

## Step 5 — Finish

- Re-read the report once for fabricated facts or missing certainty tags; fix those (this is the only cleanup pass).
- Confirm nothing in the audited project was changed except the new report (and evidence folder if agreed): `git status` when in a repo.
- Reply to the user briefly: where the file is, scope covered, counts by severity, top ~5 issues in one line each, and what couldn't be verified. Don't paste the whole report into chat.
