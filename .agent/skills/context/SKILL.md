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

## Session Handoff Role

This skill is responsible for maintaining `workspace/context.md` as the **single resumption file** for cross-session continuity.

**Rules:**
- After ANY stage completes (not just Stage 2), update `context.md` with current state.
- Keep it compact (~200 lines max). Summarize, don't duplicate.
- If `context.md` already exists, UPDATE it (merge new info). Don't append or recreate from scratch.
- Include artifact index: which workspace files exist and their status (Draft/Done).
- A new session reading ONLY `context.md` should know: what stage to resume, what decisions were made, what's blocking.

## Feedback Output

Use [references/change-log.md](../../references/change-log.md).

If feedback expands scope → hand off to `scope` before revising WBS/proposal.
