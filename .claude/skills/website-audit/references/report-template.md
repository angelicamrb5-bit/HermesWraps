# Report skeleton for `website-audit.md`

Copy this structure. Add, split, or repeat sections freely; it's a working doc. Keep every section even if thin (write "nothing found", "N/A because …" or "not checked — why").

```markdown
# Website audit — <site / project name> (messy first pass)

> Raw, intentionally unpolished working audit. Detailed > tidy. Duplicates and overlaps are intentional.
> Certainty tags: [VERIFIED] observed · [LIKELY] inferred from evidence · [ASSUMPTION] guess · [UNVERIFIED] couldn't check · [QUESTION] needs owner input

## 0. Meta
- Date:
- Auditor: Claude Code (website-audit skill)
- Scope: live URL(s) … / codebase path … / both
- Pages/routes reviewed: (count + list or link to inventory table)
- Viewports checked:
- Tools used: (WebFetch / Firecrawl / curl / Playwright capture / Lighthouse / axe / grep / build / lint …)
- Tools NOT available / not run, and what that means for confidence:
- Not in scope / couldn't access (auth walls, checkout, admin, geo-blocked, forms not submitted):
- Evidence folder: (path or "none")

## 1. What I think this site is for  [ASSUMPTION unless stated by owner]
- Business / offer:
- Audience(s):
- Primary conversion(s):
- Secondary goals:
- Open questions for owner:

## 2. Quick scan — raw first impressions (unfiltered)
- bullet dump, gut reactions, anything weird on first load (mobile + desktop)

## 3. Severity snapshot
| Severity | Count | Finding IDs |
|---|---|---|
| Critical | | |
| High | | |
| Medium | | |
| Low | | |
| Note | | |

Top issues (rough, not final priority):
1.
2.
3.

## 4. Inventories
### 4.1 Page / route inventory
| URL / route | Source file (if code) | Status | Title | H1 | Meta desc? | Canonical | Indexable | Notes |
|---|---|---|---|---|---|---|---|---|

### 4.2 Sitemap tree (as navigated) vs sitemap.xml vs code routes
(tree + diff notes)

### 4.3 Navigation inventory (header / mobile / footer)
| Location | Label | Destination | Works? | Notes |
|---|---|---|---|---|

### 4.4 CTA inventory
| Page | CTA label | Style (primary/secondary/link) | Position | Destination | Notes |
|---|---|---|---|---|---|

### 4.5 Forms inventory (NOT submitted)
| Page | Form purpose | Fields | Required | Labels ok? | Validation | Endpoint/handler | Success/error states | Notes |
|---|---|---|---|---|---|---|---|---|

### 4.6 Component inventory / repeated components
| Component / block | Where used | Variants found | Divergences | Should be shared? | Notes |
|---|---|---|---|---|---|

### 4.7 Design tokens actually used
| Token type | Distinct values (count) | Values | Near-duplicates | Source of truth? |
|---|---|---|---|---|
| Colors | | | | |
| Font families | | | | |
| Font sizes | | | | |
| Font weights | | | | |
| Spacing | | | | |
| Radii | | | | |
| Shadows | | | | |
| Breakpoints | | | | |
| z-index | | | | |

### 4.8 Tech stack & third parties
| Thing | Evidence | Notes |
|---|---|---|

### 4.9 Technical checks
| Check | Result | Evidence | Tag |
|---|---|---|---|
| HTTPS / redirects | | | |
| robots.txt | | | |
| sitemap.xml | | | |
| 404 page | | | |
| Security headers | | | |
| Console errors | | | |
| Failed requests | | | |
| Lighthouse / PSI | | | |

## 5. Findings by area
(Each finding uses the F-### template. Areas below — keep all, add more.)

### 5.1 First impression / 5-second test
### 5.2 UX
### 5.3 UI design
### 5.4 Layout
### 5.5 Visual hierarchy
### 5.6 Navigation
### 5.7 Information architecture
### 5.8 User journeys
(per journey: persona, goal, device, steps table, friction, drop-off risks, findings)
### 5.9 Content
### 5.10 Messaging
### 5.11 CTAs
### 5.12 Trust
### 5.13 Conversion
### 5.14 Accessibility
### 5.15 Mobile responsiveness
### 5.16 Forms
### 5.17 Interactions & motion
### 5.18 Empty / loading / error / success states
| Area | Loading | Empty | Error | Success | Other states | Notes |
|---|---|---|---|---|---|---|
### 5.19 SEO
### 5.20 Performance
### 5.21 Technical issues
### 5.22 Code quality
### 5.23 Design-system consistency
### 5.24 Repeated components
### 5.25 Missing pages / states / features
### 5.26 Confusing decisions
### 5.27 Opportunities (quick wins / bigger bets / experiments as hypotheses)
### 5.28 Legal / compliance hints (not legal advice)
### 5.29 Analytics & measurement

## 6. Page-by-page raw notes
### <URL or route>
- desktop:
- mobile:
- copy quotes:
- weirdness:
- related findings:

## 7. Live vs code differences (if both in scope)

## 8. Parking lot
- Rough ideas
- Unfinished thoughts
- Things to look at again with more access/tools
- Hypotheses to test

## 9. Questions for the owner / team
- [QUESTION] …

## 10. Assumptions log
| # | Assumption | Why assumed | How to verify |
|---|---|---|---|

## 11. Could not verify
| Item | Why not | What would verify it |
|---|---|---|

## 12. Finding index
| ID | Title | Area(s) | Severity | Effort | Tag | Where |
|---|---|---|---|---|---|---|
```
