---
name: presale-scope
description: Analyze pain points and define solution scope with scope-creep control.
---

# Presale Scope

## Procedure

1. Convert confirmed requirements → pain points + business impact. Evaluate and rank pain points by severity.
2. Mark root causes as hypotheses unless confirmed.
3. Define solution direction: write a **Proposed Solution Overview** at business/functional level — describe what will be built, how it solves the problems, and the core differentiator. Do not go into technical details.
4. Build scope register: in-scope, out-of-scope, future phase, pending decisions, scope change candidates.
5. **Prioritize Features**: Apply the MoSCoW method (Must-have, Should-have, Could-have, Won't-have) to all items in the in-scope register.
6. Run impact check for any new/expanded request.
7. Generate User Flow (Mermaid) and High-level Wireframe text descriptions for the core features.
8. Ask user if there are relevant case studies / showcase projects to include in the proposal (optional).

## Scope Change Triggers

Flag when feedback adds/expands: user group, platform, integration, report/analytics, AI/automation, migration, security/compliance, uptime/scale, support obligation, timeline/delivery model.

## Scope Change Options

For each candidate:
- A. Include in current scope.
- B. Move to future phase.
- C. Exclude.

Mark one recommendation + reason.

## Visualizing Solution (User Flow & Mockups)

- **User Flow**: Generate a `mermaid` flowchart diagram for the primary user journey (Core Feature). Ensure it includes start points, decision nodes, and end states.
- **High-Level Wireframe**: Provide a text-based, structural layout description for 1-2 critical screens (e.g., Dashboard, Main Input Form). Describe what is on the header, sidebar, main content area, and call-to-action buttons.

## Output

Use [references/pain-scope.md](../../references/pain-scope.md).
