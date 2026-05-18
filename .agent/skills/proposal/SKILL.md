---
name: proposal
description: Create or revise presale proposal from context, scope, WBS, and risks. Uses 7-section file structure.
---

# Presale Proposal

## Procedure

1. Use 8-section structure. Embed "Company Showcase" as appendix if needed.
2. **Customer Feedback Priority**: Pull requirements marked **Critical** from `Confirmed Requirements` table in Deal Context. These MUST be prioritized — weave them naturally at the top or highlight them in Pain Points (1.1), Key Features (2.2), and Risks (4.2). Clients appreciate seeing their core concerns addressed front and center.
3. Section 2.2 Key Features = **natural prose**, business language (non-tech stakeholders must understand). **REQUIRED**: Reference Value Mapping from `pain-scope.md` as content source, but write as **coherent paragraphs** — DO NOT copy the table verbatim. Each feature must naturally weave: pain → solution → business value. Prioritize sharp reasoning and real-world impact over numbers. If using numbers → must have evidence basis (client data, benchmark, comparable project). **NEVER fabricate numbers** — unsubstantiated figures backfire immediately.
4. Section 2.3/2.4: Mermaid user flow & Wireframe. Delegate wireframes to `wireframe` skill.
5. Section 3: In-Scope and Out-of-Scope only.
6. Section 4: Assumptions → Risks.
7. Section 5: Architecture → Tech Stack → Capacity → Security. Use Bullet Points exclusively, NO TABLES in this section.
8. Section 6: Execution & Delivery Plan (combines Roadmap, Milestones+AC).
9. Section 7: Budget & Commercials. **Consistency rules**: Section 7.1 Resource Allocation table MUST include every role from the WBS Role Registry — no phantom roles (in budget but not in WBS), no missing roles (in WBS but not in budget).
10. Section 8: Development Cost & Payment Schedule. **Total Development Cost MUST exactly equal Section 7.1 Total** — no rounding differences. Payment schedule milestones must match Section 6.2 milestones exactly (same names, same sequence).

## Format & Tone (Table vs Prose & Humanization Rules)

- **No horizontal rules `---`**: Do not insert `---` or `***` before or after headings (H1, H2, H3). Let natural whitespace and Markdown heading hierarchy structure the document.
- **No decorative emoji in formal text**: Do not use emoji (`💡`, `🔴`, `🟡`, `⚠️`, `⭐`) in headings, subheadings, or blockquotes. Use plain text (e.g., "Key Objective", "Risk Level: High") instead.
- **Avoid monotonous bullet patterns**: Do not overuse `- **Name** — Description` structure for all lists. Write flexibly using flowing prose, short analytical paragraphs, or colons `:` instead of em-dashes `—` for a natural human-written feel.
- **Remove placeholder instructions**: Eliminate all parenthetical instructions like `*(Features structured by...)*` or `*(Illustrative wireframe...)*`. Real authors present content directly without explaining formatting methodology.
- **Tables**: Only for Roadmap (6.1), Milestones (6.2), Resource Allocation & Cost (7.1), and Operational Cost (7.2). Every table MUST have a brief prose paragraph above it to guide the reader.
- **Prose/Bullets**: Use for all other sections. Ensure fluent, professional language. Avoid AI cliché words ("robust", "seamless", "frictionless").
- **Voice & Tone**: Write in a friendly, approachable tone that still conveys sharp expertise and confidence. Use plain, everyday business language — the kind a senior consultant would use in a face-to-face meeting. No flowery, ornate, or overly literary phrasing. No grandiose promises. Say what you mean directly. If a simpler word works, use it.

