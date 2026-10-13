---
name: quality-insurance
description: Drift check for Hermes Wraps web design work. Use right after a web design section, component or page for Hermes Wraps is completed in Claude Code (or when the user says "quality insurance", "QA this section", "check for drift", "did we drift?", "is this on-brand?") to verify the work still follows the hermes-wraps skill - message, CTA, color, typography, layout, imagery, components, motion, accessibility and reference-copying rules. Runs an automated scan plus a rendered and judgment review, returns a PASS / PASS WITH NOTES / DRIFT verdict with file:line fixes, and logs results. Pass "fix" to apply the blocking fixes after the review.
---

# Quality insurance - Hermes Wraps drift check

This skill checks finished work against the design direction. It does not set direction. **The hermes-wraps skill is the only source of truth.** Every finding must point to the hermes-wraps rule it breaks. If something looks wrong but no rule covers it, report it as a question, not as drift.

Invoke after each completed web design section. Arguments (optional): a section name or file paths to check, and `fix` to apply blocking fixes after the review.

## 1. Load the source of truth (every time, never from memory)

1. Find the hermes-wraps skill: the sibling folder `../hermes-wraps/` next to this skill, or the installed `hermes-wraps` skill (invoke it if it isn't loaded). List its directory: its `references/` files are part of the skill. If it can't be found, stop and tell the user; don't review from memory. Never report the reference files as missing without having listed the folder. If there's no file access in this environment, say so and review against hermes-wraps SKILL.md alone, marking the scanner and reference checks "not verified".
2. Read `hermes-wraps/SKILL.md` in full, plus:
   - `references/tokens.css` (always)
   - `references/components.md` for each component in the section
   - `references/page-blueprints.md` for the page the section belongs to
   - `references/visual-system.md` and `references/voice-and-copy.md` when type, imagery, motion or copy are involved
   - `inspiration/README.md` and the screenshots it logs, if any exist (needed for the copying check)
3. Read the project's drift log (`qa/hermes-drift-log.md` at the project root) if it exists, to know what has drifted before.

## 2. Define the scope

- **What was built:** the section/component name, the page it belongs to, and its position in that page's blueprint.
- **Which files:** files named by the user; otherwise the changed files from `git status --porcelain` and `git diff --name-only HEAD` (plus untracked files). Include shared CSS/token files the section touches.
- **Neighbors:** the sections directly above and below on the page. Some rules are page-level (one burgundy band, one primary CTA per viewport, background alternation, signature line not repeated in a viewport) and need that context.

State the scope in one line before reviewing.

## 3. Automated scan

Run the static scanner on the scoped files:

```bash
python3 <this-skill>/scripts/drift_scan.py <files or folders> \
  --tokens <hermes-wraps>/references/tokens.css
# or scan everything changed in git:
python3 <this-skill>/scripts/drift_scan.py --git --tokens <hermes-wraps>/references/tokens.css
```

It flags off-palette and hard-coded colors, copper used for text or buttons, Wraps Gold used as text, extra fonts, CTA wording that doesn't match, signature-line variants, hype words, placeholder text, stock-photo URLs, missing alt text, removed focus outlines, long or bouncy motion, missing reduced-motion handling and similar issues. Exit code 1 means it found errors.

The scanner gives evidence; it doesn't give the verdict. Check every hit in context: a `warn` may be fine (for example, Wraps Gold text on a Midnight background is allowed). A line can be excluded with an `hw-qa-ignore: <reason>` comment. Accept that only when the reason is valid under hermes-wraps.

Check any new text/background pair with:

```bash
python3 <this-skill>/scripts/contrast.py <fg> <bg>   # hex or token name, e.g. gold-text ivory
```

## 4. Rendered review

If the section can be rendered (static HTML, or a running dev server), look at it. Don't review layout from code alone when you can see it.

- Screenshot at **375px** and **1280px** width (Playwright/Chromium if available; otherwise the project's own preview tooling).
- Check: no horizontal scroll at 375px with 16px gutters; hierarchy reads correctly; one primary CTA per viewport; gold ≈10% of the screen; image crops and overlays; focus ring visible (tab through once); reduced-motion behavior if there's animation.
- If rendering isn't possible, say so in the report and mark the visual checks "not verified".

## 5. Judgment review

Go through `references/checklist.md` area by area for the scoped section: Message & signature line · CTA & conversion · Content integrity · Color · Typography · Layout & spacing · Imagery · Components · Motion · Accessibility · Reference translation. Skip items that don't apply to this section and say so; don't pad the report.

Severity:
- **Blocking (drift):** breaks a hermes-wraps rule stated as must/never/only, breaks an approved contrast pair or AA, invents facts, changes the signature line or primary CTA wording, or copies a reference's distinctive element.
- **Should fix:** goes against a "lean into / avoid" preference or a component spec, without breaking a hard rule.
- **Note:** polish, or a question where hermes-wraps doesn't say.

## 6. Verdict and report

Verdict:
- **PASS** - no blocking or should-fix findings.
- **PASS WITH NOTES** - no blocking findings; should-fix or notes listed.
- **DRIFT** - one or more blocking findings. The section is not done until they're fixed and re-checked.

Write the report with `references/report-template.md`. Keep it short: verdict first, then findings (most severe first), each with `file:line`, what drifted, the hermes-wraps rule it breaks (file + section), and the exact fix. End with what was verified and what wasn't.

## 7. Fixing

- **Default:** report only, then offer to apply the fixes.
- **With `fix`** (or when the user asks): apply blocking and should-fix items that are mechanical and unambiguous (token swaps, CTA label, signature-line wording, alt text, focus styles, motion durations, removing invented facts → `[CLIENT TO SUPPLY: …]`). Re-run the scanner and the affected checks, then update the verdict.
- Anything that needs a design decision (restructuring a section, changing imagery, choosing between two valid directions) goes to the user as a question with a recommended option.
- Fix the root cause: if the same drift comes from a shared component or token, fix it there, not just in this section.
- QA never changes the hermes-wraps skill. If a rule seems wrong or missing, recommend a skill update to the user; until they change it, the current rule stands.

## 8. Drift log

Append one entry per run to `qa/hermes-drift-log.md` at the project root (create it if missing, using the header in `references/report-template.md`): date, section, files, verdict, blocking items (rule IDs), fixed or open. If an item has already appeared in the log for an earlier section, mark it **recurring** and recommend a root-cause fix (shared component, token, lint rule, or a hermes-wraps clarification).

## Reference files

- `references/checklist.md` - the review rubric, each item mapped to the hermes-wraps rule it enforces.
- `references/report-template.md` - report format and drift-log format.
- `scripts/drift_scan.py` - static drift scanner (Python 3, standard library only). `--help` for options; `--json` for machine output.
- `scripts/contrast.py` - WCAG contrast checker that knows the Hermes palette and approved pairs.
