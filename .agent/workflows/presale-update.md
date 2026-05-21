---
description: Update any component of existing proposal/WBS from feedback, scope changes, or revisions
---

# /presale-update

## Trigger

1. Load `.agent/rules.md` (skip if already loaded).
2. Identify active project (ask if multiple in `projects/`).
3. Read `status.md` of that project.
4. Proceed with steps below.

## Change Classification

| Type | Example | Cascade |
| --- | --- | --- |
| Question answered | Client trả lời câu hỏi từ backlog | Backlog-questions → Discovery → Context → Scope (if needed) |
| Scope change | Add/remove module, platform | Scope → WBS → Proposal |
| Requirement update | Change user count, SLA, stack | Context → Scope → WBS → Proposal |
| Timeline change | Shorten/extend deadline | WBS → Proposal |
| Cost/resource change | Budget, team size | WBS → Proposal |
| Content revision | Wording, format, detail | Only affected artifact |
| Correction | Fix wrong info | Context → cascade if needed |

## Steps

### Step 1: Classify

- Classify changes per table above.
- Identify affected artifacts (cascade path).
- Present impact summary. Wait for user confirm.

Output format:

```
## Change Request
| # | Change | Type | Affected artifacts |
| 1 | {{desc}} | {{type}} | {{list}} |

## Impact
- Scope: none / expand / reduce / modify
- WBS: none / add / remove / re-estimate
- Proposal: none / revise sections [list]
```

### Step 2: Update Context

Delegate to [orchestrator](../skills/orchestrator/SKILL.md) → routes to correct agent + skill.

- Record change in deal context.
- Add change log entry.
- Classify: fact / decision / scope change / correction.

### Step 2b: Handle Question Answered (only for type "Question answered")

1. In `backlog-questions.md`: move question from "Open" to "Answered", fill Answer/Notes fields.
2. In `discovery.md`: update relevant sections (Confirmed Facts, Assumptions, Missing Info) based on the answer.
3. If answer changes scope/requirements → continue cascade (Step 3).
4. If answer only confirms existing assumption → mark assumption as confirmed, no further cascade needed.

### Step 3: Cascade

Order: `Context → Scope → WBS → Proposal (section-level)`

Delegate each step to [orchestrator](../skills/orchestrator/SKILL.md) — it routes to the correct agent owner per stage. Agent's Stop/Assume rules apply at each step.

Rules:
- Revise only affected sections, never regenerate full artifact.
- Scope change → require user approve before updating WBS/Proposal.
- Content revision → update directly, no approve needed.

Proposal (multi-section):
1. Read `workspace/proposal/_index.md`.
2. Map change type → affected sections:
   - Scope change → 05, 06, 09, 01
   - Timeline → 08, 09
   - Requirement → corresponding sections
   - Content revision → specified section only
3. Read + edit only those sections.
4. Update `_index.md` (version, date, history).

### Step 4: Consistency check (conditional)

Run ONLY for scope/requirement/timeline changes. Skip for content revision or correction.

Delegate to orchestrator → routes to `review-finalize` skill (review mode, no finalize).

- Check proposal ↔ WBS.
- Check WBS ↔ scope.
- Flag inconsistencies.

### Step 5: Save

- Write updated artifacts to `projects/YYYY-MM-DD-<client>/workspace/`.
- Update `status.md` if state changed.
- Write change log entry.

## Gate

- All changes classified.
- Scope changes approved before cascade.
- No inconsistency in updated artifacts.
- Change log recorded.
- No section revised outside impact scope.
