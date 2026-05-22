---
description: Presale pipeline — raw input to Final Proposal + Final WBS
---

# /presale-run

## Trigger

1. Load `.agent/rules.md` (once per session).
2. Locate active project folder (most recent `projects/YYYY-MM-DD-*`).
3. Check `_source/client-input.md` has real content (not just template placeholders).
   - If empty/template-only AND user provided content inline (in the same message as `/presale-run`) → write that content to `_source/client-input.md`, then continue.
   - If empty/template-only AND no inline content → ask user to paste content now (accept in chat). Write response to `_source/client-input.md`, then continue.
   - Do NOT stop and tell user to open the file manually.
4. Resume at next logical stage if prior artifacts exist.
5. Delegate routing to [orchestrator](../skills/orchestrator/SKILL.md): determines current stage → loads agent → loads skill → runs pipeline with Stop/Assume logic.
6. End each stage: state next stage + next agent, wait for user confirm.
7. Save output → `projects/YYYY-MM-DD-<client>/workspace/<stage>.md`.

## Session Handoff (Auto-maintained)

After completing each stage, update `workspace/context.md` with a rolling summary so any new session can resume without re-reading all artifacts.

**When to write/update:**
- After Stage 1 (Discovery): create `context.md` with initial deal context.
- After Stage 2+: update existing `context.md` — merge new info, don't append chat history.

**What to include** (compact, max ~200 lines):
- Deal summary (1-2 sentences)
- Current stage + what's done vs pending
- Confirmed requirements (table)
- Key decisions made
- Active assumptions
- Open questions (blocking vs non-blocking)
- Scope register summary (in/out/future — IDs only if scope.md exists)
- Risks
- Artifact index (which files exist, their version/status)

**What NOT to include:**
- Full chat history or conversation quotes
- Duplicate content already in stage artifacts
- Detailed WBS or proposal content (just reference the file)

**Resume behavior:** When starting a new session, if `workspace/context.md` exists → read it first as primary context. Only read other artifacts if needed for the current stage's work.
