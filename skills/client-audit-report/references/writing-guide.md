# Writing guide: from audit-speak to client language

Read this before drafting the content JSON.

## The core move

Each technical finding goes through the same chain:

**what's technically wrong → what the visitor or Google experiences → what it costs the business → what we'll do about it**

The audit usually only states the first link. The report leads with the last three.

## Jargon translation table

| Audit says | Say instead |
|---|---|
| LCP 4.6s / poor Core Web Vitals | "The main content takes almost 5 seconds to appear on a phone. Most visitors expect under 2.5, and Google uses this speed as a ranking signal." |
| CLS / layout shift | "Parts of the page jump around while it loads, so visitors sometimes tap the wrong thing." |
| Render-blocking JS/CSS, unminified assets | "Behind-the-scenes code is slowing down how fast pages appear." |
| Uncompressed images / no WebP | "Images are much larger than they need to be, which slows the site down, especially on mobile data." |
| Missing / duplicate title tags & meta descriptions | "Several pages show the same or missing headline and summary in Google results, so they're less likely to be clicked." |
| Missing H1 / poor heading hierarchy | "Some pages don't clearly state their main topic, which makes them harder for both visitors and search engines to understand." |
| Canonical issues / duplicate content | "Google sees several near-identical versions of some pages and has to guess which one to show." |
| 404s / broken internal links | "Some links lead to pages that no longer exist, which is a dead end for visitors." |
| Redirect chains / 302s | "Some old links take a few detours before reaching the right page, which slows things down and weakens their search value." |
| No schema / structured data | "We can give Google extra details (reviews, opening hours, prices) so your listing stands out in search results." |
| robots.txt / noindex errors | "Some important pages are accidentally hidden from Google." |
| XML sitemap missing | "Google doesn't have a complete map of the site, so new pages may be found slowly." |
| Missing alt text | "Images lack text descriptions, so people using screen readers miss them and Google can't 'see' them." |
| Low colour contrast / WCAG failures | "Some text is hard to read, especially for people with visual impairments, and that also creates accessibility compliance risk." |
| No HTTPS / mixed content | "Some pages trigger browser 'not secure' warnings, which make visitors hesitate to share details." |
| Low CTR / high bounce rate | "Many visitors leave without taking the next step." |
| No clear CTA above the fold | "Visitors have to scroll or hunt to find how to contact you or buy." |
| Form has 11 fields | "The enquiry form asks for more than most people are willing to fill in." |
| Thin content | "Some key pages say too little to persuade a visitor or rank well in search." |
| Keyword cannibalization | "Several pages are competing with each other for the same searches." |
| No GA4 conversion tracking | "We can't currently see which pages or campaigns produce enquiries, so marketing decisions are partly guesswork." |
| Backlink profile weak / low DA | "Few other reputable websites link to yours, which limits how much Google trusts it." |

If a term isn't in the table, ask whether the client would say it in a meeting. If not, describe the effect instead.

## Before / after examples

**Opportunity**

> *Audit:* "LCP on mobile is 4.6s (poor). Hero image is a 2.3MB PNG. 4 render-blocking scripts in `<head>`. TTFB 1.2s on shared hosting."

> *Report:*
> - **title:** "Mobile visitors are waiting too long"
> - **finding:** "On a typical phone, the homepage takes almost five seconds to show its main content. The biggest causes are an oversized header image and some slow-loading code."
> - **why_it_matters:** "Most mobile visitors start leaving after about three seconds, and Google favours faster sites in its rankings. Speeding this up protects both enquiries and search visibility."

**Recommendation**

> *Audit:* "Convert hero to WebP, add width/height attrs, lazy-load below-fold images, defer non-critical JS."

> *Report:*
> - **action:** "Speed up the homepage"
> - **detail:** "Resize and compress the main images and delay non-essential code so the page appears in under three seconds on mobile. This is mostly a one-off technical task with no visible design change."
> - impact High · effort Low · Quick win

**What's working**

> *Audit:* "SSL valid. GBP verified, 4.8★ (212 reviews). NAP consistent."

> *Report:*
> - **title:** "A strong local reputation"
> - **detail:** "With a 4.8-star rating from over 200 Google reviews and consistent contact details across the web, you already have the trust signals many competitors lack. The site should showcase this more."

## Executive summary formula

1. **Where things stand**, one sentence and balanced: "The site has a strong foundation: a trusted brand, good reviews and clear services."
2. **The biggest issue** in business terms: "However, slow mobile performance and a hard-to-find contact path are likely costing enquiries."
3. **The size and shape of the opportunity**: "Most of the improvements are quick, low-cost fixes that can be done within a month, with two larger projects to follow."

Key takeaways are three short sentences a client could repeat to their boss.

## Tone checklist

- Write "we found" / "we recommend", and address the client as "you" / "your site".
- Use active verbs and short sentences. Remove filler like "it is important to note that".
- Use confident but honest words like "likely", "typically", "we expect". Avoid guarantees.
- Use numbers only when they come from the audit, and round them so they read cleanly ("almost 5 seconds", "around 40 pages").
- No exclamation marks, no emojis.
