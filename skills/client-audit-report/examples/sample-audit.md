# Site Audit – brightsmiledental.com
Auditor: M. Ortiz (Northlight Digital) · Crawl date: 2026-09-28 · Tools: Screaming Frog 21, PSI, Lighthouse 12, GSC (last 90d), GA4, WAVE

## 1. Crawl overview
- 214 URLs crawled (HTML 96, images 88, JS/CSS 30)
- 200: 171 | 301: 22 | 302: 6 | 404: 15
- Indexable HTML: 81 / 96
- 9 pages `noindex` incl. /services/invisalign/ and /services/emergency-dentist/ (!!) — looks like leftover from staging
- XML sitemap present at /sitemap_index.xml (Yoast), 12 URLs in sitemap return 301/404
- robots.txt OK, no blocking of critical resources

## 2. Performance (PSI, mobile, homepage)
- Perf score 38 (mobile), 81 (desktop)
- LCP 5.1s (hero slider, 3 images, 2.8MB total, JPG/PNG, no width/height)
- CLS 0.24 (cookie banner + web font swap)
- TBT 890ms — 7 render-blocking scripts in <head> (jQuery 1.12, slider plugin, 3x tracking, chat widget, font awesome)
- TTFB 1.4s – shared hosting (Bluehost basic), no page caching plugin, no CDN
- Booking page /book-online/ LCP 6.3s due to embedded 3rd-party iframe (Dentrix widget)

## 3. On-page SEO
- 23 pages missing meta description
- 14 duplicate title tags ("Home - Bright Smile Dental" pattern on service pages)
- 6 pages missing H1; 11 pages with multiple H1s (theme puts logo in H1)
- Service pages thin: avg 210 words; /services/implants/ = 94 words
- No location pages despite 2 clinics (Austin – Main St, Round Rock)
- Blog: 38 posts, last post 2023-11; 12 posts < 300 words; 4 pairs cannibalizing ("teeth whitening cost" x2, "do implants hurt" x2)
- Images: 61/88 missing alt attributes
- Internal linking: service pages get 0–2 internal links from blog

## 4. Local SEO
- GBP Austin: verified, 4.9★ (318 reviews), categories ok
- GBP Round Rock: verified, 4.7★ (96 reviews), primary category = "Dentist" ok; hours on GBP don't match site footer (Sat)
- NAP: Round Rock phone differs on site footer vs GBP vs Yelp (old number on Yelp + 3 directories)
- No LocalBusiness / Dentist schema; no Review schema
- Reviews not displayed anywhere on site

## 5. UX / Conversion
- Primary CTA "Book Online" in header, but on mobile hidden in hamburger menu
- Phone number not click-to-call on mobile (plain text in header)
- Homepage hero slider rotates every 3s, 3 slides, generic stock photo of model smiling; no headline mentions location or services
- New patient form (/new-patients/) = 18 fields incl. SSN and insurance ID; no autosave; GA4 shows 71% abandonment on form start → submit
- No pricing/insurance info page — "Do you take my insurance?" is top query in chat widget logs (per client)
- Trust: no team photos (stock only), dentist bios exist but buried under /about/team/
- Contact page: map embed OK, form works, confirmation message OK
- Emergency dentist page noindexed (see §1) — this is a high-intent query ("emergency dentist austin" 1.9k/mo)

## 6. Accessibility (WAVE + manual)
- 61 images w/o alt (see above)
- Contrast errors: 34 (light grey #A9A9A9 body text on white, teal buttons w/ white text 2.9:1)
- Form fields on /new-patients/ missing labels (placeholder only)
- Slider not pausable; auto-rotates
- Skip link missing; focus states removed in CSS (outline:none)
- Heading order skips levels on most pages

## 7. Security / Tech
- HTTPS valid, HSTS not set
- Mixed content on 4 blog posts (http images)
- WordPress 6.6 core up to date; 4 plugins outdated (incl. slider plugin w/ known XSS CVE-2026-1182)
- No uptime monitoring
- Backups: unknown — client to confirm with host

## 8. Analytics
- GA4 installed via GTM; no conversion events configured (form submits, calls, booking clicks not tracked)
- GSC verified; 90d: 41.2k impressions, 1,180 clicks, CTR 2.9%, avg pos 18.4
- Top queries mostly branded; non-branded "dentist round rock" pos 14, "dental implants austin" pos 27
- Call tracking: none

## 9. Positives
- Strong reviews (4.9 / 318) – big differentiator vs competitors avg ~4.5
- Clean, modern visual design; brand colours consistent
- Site is HTTPS and on current WP core
- Contact page and map work well
- Domain age 2009, decent referring domains (112 RDs, several local news + Chamber of Commerce)
- Dentist bios are well-written (just hard to find)

## 10. Misc / low priority
- Favicon low-res
- Footer copyright says 2023
- 404 page is default theme page, no search/links
- Some PDFs (forms) not optimized, 3-5MB each
- Author archives indexable (thin)
- Tag pages indexable (38 tag pages, thin)
- Font Awesome full library loaded for 6 icons
- jQuery migrate loaded
