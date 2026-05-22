---
name: review-finalize
description: Review artifacts for consistency and scope creep. Approve finalization or list required fixes.
---

# Presale Review & Finalize

## Procedure

### Update Checklist (Second Pass)

Before running checks, open `workspace/checklist.md` (created at Stage 4) and complete the remaining items:
- Update **Role Registry**: verify WBS roles = Proposal Section 7.1 roles.
- Update **Cross-Artifact Consistency**: fill all rows (scope match, roles match, milestones, risks).
- Update **Overview** table with final Pass/Fail status for each check.

All findings below are also reflected in the checklist.

### Pre-check: Run Local Linter

Before running LLM-based checks, execute the offline linter:

```
python3 shared/scripts/presale_cli.py --project <project_path> --lint
```

- If exit code 0 → systemic checks (items 1-5 below) already verified. Skip them, proceed to General Checks (items 6-11).
- If exit code 1 → report lint findings as review failures. Do NOT proceed to finalization until fixed.

### Systemic Consistency Checks (Rule #10)

1. **Scope → WBS**: Every In-Scope item (`S-{n}`) has ≥1 WBS task referencing it. Flag orphan scope items with no WBS coverage.
2. **WBS → Scope**: Every WBS task references a valid `S-{n}`. Flag tasks with invalid or missing scope refs.
3. **WBS Roles → Budget**: Every unique Owner Role in WBS appears in Proposal Section 7.1 Resource table. Flag phantom roles (in budget but not in WBS) and missing roles (in WBS but not in budget).
4. **Financial Math**: Section 7.1 Total = Σ(individual role costs). Section 8 Total Dev Cost = Section 7.1 Total. Flag any mismatch — exact-to-decimal, no rounding tolerance.
5. **Milestone Alignment**: Section 6.2 milestones = Section 8 payment milestones (same names, same count). Each milestone's deliverables map to real WBS task IDs.

### General Checks

6. Check scope ↔ requirements/decisions/assumptions.
7. Flag unapproved scope changes.
8. Flag assumptions written as facts.
9. Flag missing dependencies, risks, acceptance criteria, open questions.
10. **Value Articulation Check**: Verify every feature in Proposal Section 2.2 (Key Features) includes clear business value woven naturally as prose — not dry tables. Accept two forms: **(a)** numbers with stated evidence (client data, benchmark, comparable project — must cite basis), or **(b)** sharp qualitative impact descriptions (e.g., "eliminates 3-step manual process entirely"). Flag: tech-only descriptions, vague value without reasoning ("improve", "enhance", "optimize"), or **fabricated numbers without evidence basis** (most critical violation).
11. Approve finalization only if all gates pass.

## Finalization Gate

- No critical open questions.
- No unapproved scope changes.
- Proposal and WBS use same scope.
- Assumptions accepted or explicitly listed.
- Out-of-scope explicit.
- Final version and date present.
- **Every feature in Section 2.2 has business value articulation** — evidence-based numbers OR sharp qualitative impact. Fabricated numbers without basis = critical violation, block finalization.
- **Scope ↔ WBS**: No orphan scope items. No WBS tasks without valid scope refs.
- **Roles ↔ Budget**: WBS Role Registry = Section 7.1 roles. No phantom or missing roles.
- **Financial Math**: Section 7.1 Total = Σ(role costs). Section 8 Total = Section 7.1 Total. Exact match.
- **Milestones**: Section 6.2 = Section 8 payment milestones. All deliverables map to WBS IDs.

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
