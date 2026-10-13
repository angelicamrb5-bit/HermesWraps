# HermesWraps

Design resources for **Hermes Wraps** (vinyl specialists).

## Claude skills

| Skill | Use |
|---|---|
| `hermes-wraps` | Design direction - Claude follows it whenever it designs for Hermes Wraps. |
| `quality-insurance` | Drift check - run it after each completed web design section to confirm the work still follows `hermes-wraps`. |

## `hermes-wraps`

`.claude/skills/hermes-wraps/` is the internal design instruction set Claude follows whenever it designs pages, websites, landing pages or product experiences for Hermes Wraps.

```
.claude/skills/hermes-wraps/
├── SKILL.md                    # approach, messaging, CTA rules, visual direction, do/don't, checklist
├── references/
│   ├── brand-foundations.md    # palette, contrast pairs, logo rules, confirmed brand facts
│   ├── tokens.css              # --hw-* design tokens (color, type, spacing, radius, motion)
│   ├── visual-system.md        # type scale, grid, spacing, imagery, icons, motifs, motion
│   ├── components.md           # component data: anatomy, sizes, tokens, states
│   ├── page-blueprints.md      # page hierarchy for key marketing pages
│   └── voice-and-copy.md       # tone, headline patterns, CTA + microcopy library
├── inspiration/                # client reference screenshots + log (translate, don't copy)
└── assets/brand/               # color guide PDF, logo reference, business card reference
```

**Using it**
- Claude Code: the skill loads automatically in this repo.
- Claude.ai / Claude apps: zip the `hermes-wraps` folder and upload it under Settings → Capabilities → Skills.

**Adding reference designs:** drop screenshots into `inspiration/` and add an entry to `inspiration/README.md` describing what to take and what not to take.

## `quality-insurance`

Run it in Claude Code after finishing a section: `/quality-insurance` (optionally with a section name, files, or `fix`).

It reloads `hermes-wraps` as the source of truth, scopes the changed files, runs `scripts/drift_scan.py` (palette read from `hermes-wraps/references/tokens.css`), reviews the rendered section at 375px and 1280px when possible, goes through `references/checklist.md`, and returns a **PASS / PASS WITH NOTES / DRIFT** verdict with `file:line` fixes. Each run is appended to `qa/hermes-drift-log.md` so recurring drift gets a root-cause fix.

```
.claude/skills/quality-insurance/
├── SKILL.md
├── references/
│   ├── checklist.md         # rubric mapped to hermes-wraps rules (blocking / should fix / note)
│   └── report-template.md   # report + drift log format
└── scripts/
    ├── drift_scan.py        # static drift scanner (Python 3, stdlib only)
    └── contrast.py          # WCAG contrast check with the brand's approved pairs
```

Both skills must be installed together; `quality-insurance` depends on `hermes-wraps`.
