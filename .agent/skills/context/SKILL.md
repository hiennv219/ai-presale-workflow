---
name: context
description: Update and compress deal context from customer answers, notes, Q&A, and feedback.
---

# Presale Context

## Procedure

1. Classify new input: fact, clarification, correction, decision, assumption, constraint, risk, scope change, preference.
2. **Customer Feedback Priority**: Any explicit concern, direct feedback, or strong preference mentioned by the customer must be marked with **Critical** in the `Priority` column of the `Confirmed Requirements` table in the Deal Context.
3. Update deal context before artifact edits.
4. Merge duplicates, remove obsolete notes.
5. Preserve traceability via decisions + change log.
6. Compress long history into rolling summary.

## Deal Context

Use [references/deal-context.md](../../references/deal-context.md).

Keep active: deal summary, confirmed/unconfirmed requirements, scope register, assumptions, risks, decisions, open questions, artifact summaries, pending scope changes.

## Feedback Output

Use [references/change-log.md](../../references/change-log.md).

If feedback expands scope → hand off to `scope` before revising WBS/proposal.
