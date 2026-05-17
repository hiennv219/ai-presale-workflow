---
name: review-finalize
description: Review artifacts for consistency and scope creep. Approve finalization or list required fixes.
---

# Presale Review & Finalize

## Procedure

1. Check proposal ↔ WBS.
2. Check WBS ↔ approved scope.
3. Check scope ↔ requirements/decisions/assumptions.
4. Flag unapproved scope changes.
5. Flag assumptions written as facts.
6. Flag missing dependencies, risks, acceptance criteria, open questions.
7. Approve finalization only if all gates pass.

## Finalization Gate

- No critical open questions.
- No unapproved scope changes.
- Proposal and WBS use same scope.
- Assumptions accepted or explicitly listed.
- Out-of-scope explicit.
- Final version and date present.

## Output

Not ready:

```
## Review Findings
| Severity | Finding | Impact | Required Fix |
```

Ready:

```
## Finalization Approved
- Final Proposal: ready
- Final WBS: ready
- Conditions: {{conditions_or_none}}
```

## On Finalization Pass

Do NOT auto-export. Inform user: "Finalization approved. Run `/presale-finalize` to generate final files."
