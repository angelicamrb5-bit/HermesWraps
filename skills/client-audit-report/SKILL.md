---
name: client-audit-report
description: Turns a raw website audit written in Markdown (.md) into a polished, client-ready Word document (.docx) with a title page, executive summary, what's working, key opportunities, prioritized recommendations and next steps. It picks out the findings that matter most, rewrites them in plain, client-friendly language and ranks them by business impact. Use this skill whenever someone has a website, SEO, UX, accessibility, performance, conversion or content audit (in Markdown, pasted text or notes) and wants a client deliverable, report, summary, proposal or Word document from it. Phrases like "make this audit client-ready", "turn my site audit into a report", "clean this up for the client" or "write up the audit findings" should trigger it even if Word or .docx isn't mentioned.
---

# Client Audit Report

Turn a technical website audit (usually a `.md` file) into a strategic, client-ready Word report.

The audit was written by a specialist for a specialist. The report is for a business owner or marketing lead who has 10 minutes, cares about leads, sales, reputation and cost, and has to decide what to approve. Everything in this skill comes from that difference. Your job is to **edit and translate**, not transcribe: pick the few things that matter, explain them in business terms, and make the order of work obvious.

## Workflow

1. **Read the whole audit** before you write anything. Note the client name, site URL, audit date, the auditor or agency, and any scores or metrics.
2. **Inventory the findings.** List every issue and every strength in a scratch note. Group duplicates: audits often report the same root cause several times, for example "missing alt text" on 40 pages is one finding, not 40.
3. **Score and select** each finding by business impact, effort and urgency. See *Prioritizing* below. Expect to drop or merge a lot. An audit with 60 line items usually becomes 4–6 opportunities and 6–10 recommendations.
4. **Rewrite in client language.** Read `references/writing-guide.md` before drafting. It has the jargon translation table and before/after examples.
5. **Write the content JSON** following the schema below and save it next to the output, for example `report_content.json`.
6. **Build the document:**
   ```bash
   python3 <skill-dir>/scripts/build_report.py report_content.json "<Client> Website Audit Report.docx"
   ```
   The script needs `python-docx` (`pip install python-docx` if the import fails). It prints jargon and length warnings. Fix the JSON and rebuild until it reports no warnings, or until the remaining ones are deliberate.
7. **Check the visual result** when LibreOffice is available:
   ```bash
   soffice --headless --convert-to pdf --outdir <out-dir> "<file>.docx"
   pdftoppm -png -r 60 <out-dir>/<file>.pdf <out-dir>/page
   ```
   Look at the page images. Check the title page, that tables don't overflow, and that no section is a wall of text.
8. **Deliver** the `.docx`. In your reply, give the 2–3 headline points and say what you left out or merged, so the consultant knows what was edited.

For a worked example, compare `examples/sample-audit.md`, a raw technical audit, with `examples/sample-report-content.json`, the edited client content built from it. They show how much gets cut, merged and reframed. Read them if you're unsure how far to take the rewrite.

## Document structure

The report always has these six parts, in this order. The script builds the layout. You supply the words.

1. **Title**: the cover page with report title, client, site, date and who prepared it.
2. **Executive summary**: a short overview paragraph (3–5 sentences: where the site stands, the single biggest issue, the size of the opportunity), an optional "at a glance" row of 2–4 headline numbers, and 3 key takeaways.
3. **What's working**: 3–5 genuine strengths, each tied to why it helps the business. This builds trust and shows the audit was balanced. Don't invent praise. If the audit has little positive, use fewer items.
4. **Key opportunities**: 3–6 themes, ordered by impact. Each one says what we found, in plain terms, and why it matters, in terms of business consequence, with an impact level.
5. **Prioritized recommendations**: concrete actions in a ranked table (impact, effort, timing), followed by a short explanation of each. Group them by timing, *Quick wins (0–30 days)*, *Next (1–3 months)* and *Later (3+ months)*, so the client sees a plan, not a list.
6. **Recommended next steps**: 3–5 numbered, concrete actions for the next couple of weeks (approve X, give access to Y, schedule Z), plus a short closing line that invites a conversation.

## Prioritizing

For every candidate finding, ask:

- **Business impact.** Does it affect revenue, leads, conversions, trust, legal exposure or the ability to be found by customers? Issues on high-traffic or money pages (home, product, pricing, contact, checkout) outrank issues on a 2019 blog post.
- **Reach.** Is it sitewide or on a single page?
- **Effort.** Is it a settings change, a template fix, or a rebuild?
- **Risk or urgency.** Is it a security warning, a broken form, an accessibility exposure, or something actively costing money now?

Then rank. **High impact + low effort = quick wins, and they go first.** High impact + high effort becomes a planned project. Low impact + low effort can be bundled into one "housekeeping" recommendation. Low impact + high effort usually gets **cut**. Mention it in your chat reply, not in the report.

Impact and effort use exactly `High`, `Medium` or `Low`. Timing uses `Quick win`, `Next` or `Later`, which map to the three groups above.

## Content JSON schema

```json
{
  "client_name": "Acme Plumbing",
  "site_url": "acmeplumbing.com",
  "report_title": "Website Audit: Findings & Recommendations",
  "subtitle": "A clear plan to turn more visitors into booked jobs",
  "prepared_by": "Jane Doe, Northlight Digital",
  "date": "October 2026",
  "brand_color": "1F4E79",

  "executive_summary": {
    "overview": "One paragraph, or a list of 1-2 short paragraphs.",
    "at_a_glance": [
      {"value": "4.8s", "label": "Mobile load time (target: under 2.5s)"},
      {"value": "3 of 5", "label": "Key pages missing a clear call to action"}
    ],
    "key_takeaways": ["Takeaway 1", "Takeaway 2", "Takeaway 3"]
  },

  "whats_working": [
    {"title": "Strong, trustworthy brand", "detail": "Why it helps the business."}
  ],

  "opportunities": [
    {
      "title": "Mobile visitors are waiting too long",
      "impact": "High",
      "finding": "What we found, in plain language.",
      "why_it_matters": "The business consequence."
    }
  ],

  "recommendations": [
    {
      "action": "Compress and resize homepage images",
      "detail": "1–3 sentences: what to do and what result to expect.",
      "impact": "High",
      "effort": "Low",
      "timing": "Quick win"
    }
  ],

  "next_steps": {
    "intro": "Optional one-liner.",
    "steps": [
      {"title": "Approve the quick-win package", "detail": "…", "timing": "This week"}
    ],
    "closing": "Short, warm closing line."
  }
}
```

Notes:
- `subtitle`, `prepared_by`, `brand_color` (hex without `#`), `at_a_glance`, `next_steps.intro` and `step.timing` are optional. Leave out anything you don't actually know. Don't make up a preparer name or a metric.
- `date` defaults to the current month and year if it's left out.
- Order `opportunities` by impact and `recommendations` by priority. The script numbers recommendations in the order you give, within each timing group, so put the most important first.
- If the user gives brand colours, a logo name, or a client name that's different from the audit's, use theirs.

## Quality bar

Before you build, re-read your JSON as the client would:

- **No copy-paste from the audit.** Every sentence should be rewritten for this reader. If a sentence still reads like a crawler report, rewrite it.
- **No unexplained jargon.** Terms like LCP, CLS, canonical, schema, hreflang, 301, robots.txt, render-blocking, alt attributes, H1 and TTFB either get translated or get dropped. Specific URLs, code, file names and tool names (Lighthouse, Screaming Frog) belong in the technical audit, not here. The only exception is a page name the client will recognize, like "the Contact page".
- **Every problem links to a consequence** the client cares about, such as fewer enquiries, lost search visibility, lower trust or legal risk. Every recommendation links to an outcome.
- **Be honest and calm.** Don't use scare language or overpromise ("this will double your traffic"). Use numbers from the audit when they help. Don't invent statistics.
- **Keep it scannable.** Short paragraphs of 2–4 sentences. A finished report usually runs 4–7 pages.
- **Keep the tone respectful.** Someone built the current site, maybe the client. Frame issues as opportunities, not failures.
