# HermesWraps

## Skills

### `client-audit-report`

A Claude skill that turns a raw website audit written in Markdown into a polished, client-ready Word report.

It picks out the findings that matter, rewrites them in plain business language, ranks them by impact and effort, and builds a styled `.docx` with this structure:

1. Title page
2. Executive summary, with "at a glance" metrics and key takeaways
3. What's working
4. Key opportunities, each with what we found, why it matters and an impact rating
5. Prioritized recommendations: a ranked table, then details grouped into Quick wins, Next and Later
6. Recommended next steps

**Install:** upload `dist/client-audit-report.skill` in Claude (Settings → Capabilities → Skills). For Claude Code, copy `skills/client-audit-report/` into `~/.claude/skills/`.

**Use:** give Claude your audit `.md` and ask something like *"Turn this audit into a client-ready report for Acme"*. You can mention a brand colour, who it's prepared by, or what the client cares about most.

**Layout:**

```
skills/client-audit-report/
├── SKILL.md                     # workflow, structure, prioritization, quality bar
├── references/writing-guide.md  # jargon translation table + before/after examples
├── scripts/build_report.py      # content JSON → styled .docx (+ jargon/length checks)
├── examples/                    # sample audit → content JSON → finished report
└── evals/evals.json             # test prompts for iterating on the skill
```

Requirements: Python 3 with `python-docx` (`pip install python-docx`). LibreOffice is optional, for previewing the rendered pages.
