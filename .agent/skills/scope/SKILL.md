---
name: scope
description: Analyze pain points and define solution scope with scope-creep control.
---

# Presale Scope

## Procedure

1. Convert confirmed requirements → pain points + business impact. Evaluate and rank pain points by severity.
2. Mark root causes as hypotheses unless confirmed.
3. Define solution direction: write a **Proposed Solution Overview** at business/functional level — describe what will be built, how it solves the problems, and the core differentiator. Do not go into technical details.
4. **Value Mapping (Required)**: After defining solution direction, build a business value map for EVERY major feature/capability. This is an internal working document — use a table to organize thinking before writing the proposal.

   | Feature / Capability | Pain Point Solved | Business Value | Evidence Basis | Who Benefits |
   |:---------------------|:------------------|:---------------|:---------------|:-------------|
   | {{feature_1}}        | {{pain_ref}}      | {{impact}}     | {{basis}}      | {{stakeholder}} |

   **Business Value Rules — DO NOT FABRICATE NUMBERS:**
   - Every number MUST have clear evidence from one of 4 sources: **(a)** client-provided data, **(b)** industry benchmark with source, **(c)** results from comparable delivered project, **(d)** logical derivation from confirmed data (show the math).
   - State the basis in "Evidence Basis" column (e.g., "Client reported 4h/day manual work", "AWS benchmark", "Project X achieved similar results").
   - **If no reliable basis exists → use qualitative impact description instead of fabricating numbers.** Example: "Eliminates 3-step manual process entirely, freeing operations staff for strategic work" is far better than "Saves 70% time" without evidence.
   - Fabricated numbers will be challenged immediately by C-level clients and destroy the entire proposal's credibility.

   This table is **internal input** for Proposal Section 2.2 (Key Features). When writing the proposal, convert to **prose** — do not copy the table verbatim into the client-facing document.

5. Build scope register: in-scope, out-of-scope, future phase, pending decisions, scope change candidates. **Every in-scope item MUST have a stable ID using format `S-{n}`** (e.g., S-1, S-2, S-3). These IDs are the single reference key used by WBS (`Scope Ref` column) and Proposal (Section 3.1). Do not renumber existing IDs when adding new items.
6. **Prioritize Features**: Apply the MoSCoW method (Must-have, Should-have, Could-have, Won't-have) to all items in the in-scope register.
7. Run impact check for any new/expanded request.
8. Generate User Flow (Mermaid) and High-level Wireframe text descriptions for the core features.
9. Ask user if there are relevant case studies / showcase projects to include in the proposal (optional).

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
