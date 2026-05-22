# Proposal Template (Default)

This file defines the default proposal structure. Copy it to `workspace/proposal-template.md` in each project. Users can add, remove, reorder, or rename sections freely.

## How to use
- Each H2 heading = one section in the final proposal
- `file`: output filename (prefix number controls concat order)
- `format`: output style (prose, table, bullets, mermaid)
- `source`: workspace artifacts to use as input data
- `structure`: subsections and their format within this section
- `content`: brief description of what to cover

---

## 01 - Project Overview & Business Value
- file: 01-project-overview.md
- format: prose
- source: context.md, scope.md
- structure: |
    ### 1.1 Context & Problem Statement
    Prose narrative (2-3 sentences current state) + bullet list of Core Pain Points (bold name: root cause. impact).
    ### 1.2 Goals & Business Impact
    Goal (1 sentence), Project Type, then bullet list of Business Benefits.
- content: Project background, client pain points, goals, and business impact.

## 02 - Proposed Solution & UX
- file: 02-proposed-solution.md
- format: prose, mermaid
- source: context.md, pain-scope.md
- structure: |
    ### 2.1 Solution Overview
    Prose (3-5 sentences) describing the overall solution.
    ### 2.2 Key Features
    Prose using business language, grouped by module. Reference Value Mapping from pain-scope.md but write as coherent paragraphs (do not copy the table verbatim). Each feature must naturally weave: pain → solution → business value.
    ### 2.3 User Flow
    Prose (2-3 sentences) + Mermaid diagram.
    ### 2.4 High-Level Wireframe
    Delegate to wireframe skill if needed.
- content: Proposed solution, key features, user flows, and wireframes.

## 03 - Project Scope
- file: 03-project-scope.md
- format: bullets
- source: pain-scope.md
- structure: |
    ### 3.1 In-Scope
    Bullet list: bold phase/module name + description.
    ### 3.2 Out-of-Scope
    Bullet list: bold item + reason for deferral.
- content: Project scope (in-scope and out-of-scope boundaries).

## 04 - Risks & Strategic Assumptions
- file: 04-risks-assumptions.md
- format: prose, bullets
- source: context.md, scope.md
- structure: |
    ### 4.1 Strategic Assumptions
    Bullet list: bold category + assumption statement.
    ### 4.2 Risk & Mitigation
    Each risk: bold name (severity level), description paragraph, then Mitigation line.
- content: Strategic assumptions and project risks with mitigation steps.

## 05 - Technical Architecture
- file: 05-technical-architecture.md
- format: bullets, diagram
- source: context.md, technical.md
- structure: |
    ### 5.1 Target Architecture
    ASCII box diagram or Mermaid.
    ### 5.2 Tech Stack
    Bullets only (no tables): Frontend, Backend, Database, Infrastructure — each item: bold tech + why.
    ### 5.3 Data Flow
    Mermaid sequenceDiagram.
    ### 5.4 Capacity & Sizing
    Bullets: Target Users, Concurrent Connections, Storage Strategy.
    ### 5.5 Security & Privacy
    Bullets: Transport, Storage, Auth.
- content: Technical architecture, tech stack, data flows, capacity, and security. Bullets only — NO TABLES.

## 06 - Execution & Delivery Plan
- file: 06-execution-plan.md
- format: table, prose
- source: wbs.md, scope.md
- structure: |
    ### 6.1 Product Roadmap
    Prose (2-3 sentences) about timeline strategy, then table: Phase | Feature | Duration | Timeline | Month columns.
    ### 6.2 Milestones & Acceptance Criteria
    Prose (2-3 sentences) about acceptance method, then table: # | Milestone | Target Date | Key Deliverables | Acceptance Criteria.
- content: Roadmap, milestones, and acceptance criteria.

## 07 - Budget & Commercials
- file: 07-budget.md
- format: table, prose
- source: wbs.md
- structure: |
    ### 7.1 Resource Allocation & Development Cost
    Prose explaining pricing model, then table: Position | Seniority | Unit Price | Month columns | Total Effort | Total Cost.
    RULE: Table MUST include every role from WBS Role Registry — no phantom roles, no missing roles.
    ### 7.2 Operational Cost (Infra)
    Prose on cost optimization, then table: Phase | Users | Infra Cost/month | Main Components.
    ### 7.3 3rd-Party Vendor Costs
    Bullet list: bold vendor + cost + note.
- content: Resource budget, operational costs, and third-party vendor costs.

## 08 - Development Cost & Payment Schedule
- file: 08-payment-schedule.md
- format: prose, bullets
- source: wbs.md
- structure: |
    Total Development Cost statement (MUST equal Section 7.1 Total exactly).
    Payment Schedule bullets: each milestone payment with conditions.
    RULE: Payment milestones must match Section 6.2 milestones (same names, same sequence).
- content: Total development cost statement and milestone-based payment schedule.

---

## Format Guidelines (Table vs Prose)

1. **USE TABLES ONLY for the following 4 contents** (a brief prose paragraph above the table is mandatory):
   - 6.1 Roadmap, 6.2 Milestones & AC, 7.1 Resource Allocation & Cost, 7.2 Operational Cost.
2. **USE PROSE / BULLET POINTS for all other sections**:
   - Section 1 & 2: Business language, storytelling.
   - Section 4: Bullet list with bold titles.
   - Section 5: Bullets only, explaining the "why".
   - Section 7.3: Bullet list.

## Humanization Checklist

1. Do not use `---` or horizontal rules between headings.
2. Do not use decorative emoji (`💡`, `🔴`, `⭐`, `⚠️`) in headings or blockquotes.
3. Vary bullet list patterns — avoid repeating `- **Title** — Description`. Mix prose, colon separators, and direct text.
4. Remove parenthetical formatting instructions like `*(Illustrative...)*`.
5. Avoid AI clichés: "robust", "seamless", "frictionless", "revolutionary", "cutting-edge". Use practical business terms.

## Conciseness Targets

Word counts below are **maximum** targets (Vietnamese word count / English word count). Going under budget is fine — going over means the section needs editing.

| Section | Max Words (VI) | Max Words (EN) | Key Constraint |
| --- | --- | --- | --- |
| 01 - Project Overview | 400 | 350 | Problem ≤ 3 sentences; Benefits ≤ 4 bullets |
| 02 - Proposed Solution | 600 | 500 | Solution overview ≤ 3 sentences; each feature ≤ 2 sentences |
| 03 - Project Scope | 400 | 350 | Each bullet = bold name + 1 sentence |
| 04 - Risks & Assumptions | 400 | 350 | Each assumption ≤ 1 sentence; each risk = 1 desc + 1 mitigation |
| 05 - Technical Architecture | 500 | 450 | Each tech stack item: bold name + 1 "why" sentence |
| 06 - Execution Plan | 300 + tables | 250 + tables | Lead-in prose ≤ 2 sentences per table |
| 07 - Budget | 200 + tables | 180 + tables | Lead-in prose ≤ 2 sentences per table |
| 08 - Payment Schedule | 250 | 200 | Total cost statement = 1 sentence |

### Anti-Patterns to Avoid
- **Echo preamble per bullet:** "To solve X problem, the system provides Y" — Just state Y directly.
- **Synonym stacking:** "robust and powerful", "fast and efficient" — Pick one.
- **Filler openers:** "In order to address the challenge of..." — Start directly with the action.
- **Restating the obvious:** If Section 1 already explained the pain point, do not re-explain it in Section 2.

