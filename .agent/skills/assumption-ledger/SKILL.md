---
name: assumption-ledger
description: Track all assumptions created during pipeline execution. Shared skill callable by any agent.
---

# Assumption Ledger

## Purpose

Centrally track all assumptions created throughout the pipeline. Provide visibility for the Review gate and the client.

## Trigger

Any agent that triggers the Assume Rule → calls this skill to record the assumption.

## Procedure

### Record a New Assumption

1. Read `workspace/assumption-ledger.md` (create from template if it doesn't exist yet)
2. Generate a new ID: `A-{n}` (sequential, never reuse)
3. Record the entry with: ID, Description, Created By (agent), Stage, Impact, Status=Active, Date, Notes
4. Update the Overview table (totals)
5. Save the file

### Impact Classification

| Impact | Definition | Examples |
|--------|------------|----------|
| Low | Incorrect → only changes implementation details, does not affect scope/cost | Caching engine, logging tool |
| Medium | Incorrect → changes effort estimate or timeline | Number of user roles, API complexity |
| High | Incorrect → changes scope, cost, or architecture | Migration required, compliance, platform choice |

### Status Lifecycle

```
Active → Confirmed (confirmed by client)
Active → Rejected (rejected by client → triggers re-scope)
Active → Replaced (replaced by another assumption)
Pending confirm → Confirmed / Rejected
```

### Escalation

- Assumption Active > 7 days + impact Medium → escalate to Stop Rule in the next stage
- Assumption Rejected by client → trigger re-scope (loop back)

## Integration with Review Gate

Review agent (Stage 6) MUST check the Assumption Ledger:
- impact=High + status≠Confirmed → **BLOCK finalization**
- impact=Medium + status=Active > 7 days → **WARNING**
- List all Active assumptions in the proposal (Section: Assumptions & Risks)

## Output

File: `workspace/assumption-ledger.md`
Template: `references/assumption-ledger.md`
