# Report template

Use this format for the response after every quality-insurance run. Leave out empty sections.

```markdown
## Quality insurance - <Section name> (<Page>)

**Verdict: PASS | PASS WITH NOTES | DRIFT**
Scope: <files> · Blueprint position: <e.g. Home §4 "How we protect your standards"> · Rendered: <375 + 1280 checked | not rendered - reason>

### Blocking (must fix)
1. **<What drifted>** - `path/file.css:42`
   Rule: hermes-wraps <file §section> - "<short quote of the rule>"
   Fix: <exact change, e.g. `color: var(--hw-accent-text)`>

### Should fix
1. ...

### Notes / questions
- ...

### Verified
- Scanner: <n errors, n warnings, n info> (all reviewed in context)
- Checklist areas checked: <list> · Not applicable: <list>
- Not verified: <anything that couldn't be checked and why>
- Open placeholders: <count> `[CLIENT TO SUPPLY]`
```

After fixes (with `fix`), add a short **After fixes** line: what changed, the re-run scanner result, and the updated verdict.

# Drift log format

File: `qa/hermes-drift-log.md` at the project root. Create it with this header if it doesn't exist, then append one row per run (newest last).

```markdown
# Hermes Wraps - drift log

Written by the quality-insurance skill. Source of truth: hermes-wraps skill.

| Date | Section (page) | Files | Verdict | Blocking items | Status | Recurring |
|---|---|---|---|---|---|---|
```

Row example:

```markdown
| 2026-10-13 | Hero (Home) | src/sections/Hero.tsx, hero.css | DRIFT → PASS | COLOR-GOLD-TEXT, CTA-LABEL | fixed | CTA-LABEL (2nd time) |
```

Use the scanner rule IDs where they exist; otherwise a short label like `MSG-HEADLINE-FRAMING`.
