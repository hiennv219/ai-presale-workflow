---
name: slides
description: Transform proposal into slide-deck Markdown structured for external AI handoff.
---

# Slide Deck Generator

## Purpose

Summarize the proposal into a structured Markdown format for slides, ready to be imported into GPT/Gemini to create a visual deck.

## Slide Structure (17 fixed slides + expandable slides)

| # | Slide | Source | Content | Limits / Constraints |
|---|-------|--------|---------|---------------------|
| 1 | Title | Metadata | Project name, client, date, prepared by | 4-5 lines |
| 2 | Agenda | — | Main sections to be presented | 5-7 bullets |
| 3 | Project Overview | §1 (1.1 + 1.2) | Pain points + objectives + business value | 4-5 bullets |
| 4 | Solution Overview | §2.1 | High-level solution description | 2-3 sentences + 2 bullets |
| 5 | Key Features | §2.2 | Key features, business value | 3-5 bullets (expandable) |
| 6 | User Flow | §2.3 | Primary flow, suggested diagram | 3-4 steps |
| 7 | Scope: In-Scope | §3.1 | Deliverables grouped by module | 3-5 bullets (expandable) |
| 8 | Scope: Out-of-Scope | §3.2 | Excluded in this phase | 2-4 bullets |
| 9 | Architecture | §5.1 | High-level architecture, suggested diagram | 3-5 bullets |
| 10 | Tech Stack | §5.2 | Primary stack + concise justification | 4-6 bullets |
| 11 | Risks | §4.2 | Top risks + mitigations | 3 items |
| 12 | Assumptions | §4.1 | Strategic assumptions | 3-4 bullets |
| 13 | Roadmap & Timeline | §6.1 | Phases + durations | 3-5 phases |
| 14 | Milestones | §6.2 | Milestones + key deliverables | 3-5 items |
| 15 | Team & Resources | §7.1 | Roles, team composition | 3-5 bullets |
| 16 | Cost Summary | §7 + §8 | Total dev cost + operational + 3rd party | 3-5 lines, clear numbers |
| 17 | Next Steps | — | Action items + follow-up timeline | 3-4 bullets |

## Expansion Rules

- **Key Features** (slide 5): if >5 features or split by module → split into multiple slides, one slide per module
- **Scope In-Scope** (slide 7): if >4 modules → split slide by module group
- Other slides: keep fixed at 1 slide/topic
- When splitting slides, use sub-numbering: 5a, 5b or 7a, 7b

## Output Format

```markdown
# {{Project Name}} — Slide Deck

## Slide 1: Title

- **Project**: {{name}}
- **Client**: {{client}}
- **Date**: {{date}}
- **Prepared by**: {{author}}

---

## Slide 2: Agenda

- Project Overview
- Solution & Key Features
- ...

---

## Slide 3: Project Overview
...
```

## Writing Principles

1. Max 5 bullets per slide (unless expanded), max 2 lines per bullet.
2. Write for the listener, not the reader — short, clear, and impactful.
3. Prioritize metrics and outcomes over process descriptions.
4. Do not repeat the proposal verbatim — extract key highlights only.
5. Use business-first language, avoid technical jargon (except slides 9 and 10).
6. If a proposal section has no content → skip that slide and leave a note.

## Perspective by Slide Group

| Group | Perspective |
|-------|-------------|
| 3-4 | Client-centric: "What your problem is, we understand" |
| 5-6 | Product-centric: "What you will receive" |
| 7-8 | Commitment-centric: "Clear boundaries and deliverables" |
| 9-10 | Tech-centric: "A reliable and credible foundation" |
| 11-12 | Transparency-centric: "Identified risks and assumptions" |
| 13-16 | Execution-centric: "How we will deliver" |
| 17 | Action-oriented: "Next concrete steps" |

## Handling Missing Data

- If a section is missing from the proposal → skip the corresponding slide and write `[Skipped — no data in proposal]`.
- If a section exists but is brief → still create the slide with the available information.
- DO NOT invent or fabricate information.
