---
description: Generate slide-deck Markdown from proposal — structured for handoff to external AI (GPT/Gemini) for visual slide creation
---

# /presale-slides

## Trigger

User runs `/presale-slides` to generate a slide-structured Markdown file from the current proposal.

## Prerequisites

1. Locate active project folder (most recent `projects/YYYY-MM-DD-*`).
2. One of these must exist:
   - `workspace/proposal-full.md` (preferred — run `/presale-preview` first)
   - `workspace/proposal/` directory with section files
3. If neither exists → report "No proposal found", stop.

## Behavior

1. Read proposal content (full file or concat sections in order).
2. Read project context from `workspace/context.md` if available (for client name, project name).
3. Load skill: `.agent/skills/slides/SKILL.md`.
4. Generate `workspace/slides.md` following the skill's structure and rules.

## Output

```
Slides generated:
  - workspace/slides.md ({{slide_count}} slides)

Ready to copy into GPT / Gemini for visual slide generation.
```

## Rules

- No rendering or HTML export. Output is plain Markdown only.
- Each slide separated by `---` on its own line.
- Keep content concise — bullet points, not paragraphs.
- Do NOT invent facts not present in the proposal or context.
- Overwrites previous slides.md if it exists.
