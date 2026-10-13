# Hermes Wraps site

Static site in `public/` (Cloudflare Pages, no build step). See `README.md`.

## Design work

- Brand rules come from the `hermes-wraps` skill. They win over any generic design advice, including Impeccable's.
- Impeccable is installed for this project in `.claude/skills/impeccable` (`/impeccable …`). When using it, keep:
  - colors from the `--hw-*` tokens in `public/assets/site.css` (no new hues);
  - the signature line "We focus on your quality exigencies." verbatim;
  - one primary CTA, worded "Book a free consultation";
  - real project photos only; no invented reviews, numbers or logos.
- After CSS/JS changes, bump the `?v=` number on `/assets/site.css`, `site.js`, `work.js` and `book.js` in every HTML page (assets are cached for 7 days).
