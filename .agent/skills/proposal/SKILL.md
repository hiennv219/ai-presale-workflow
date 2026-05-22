---
name: proposal
description: Create or revise presale proposal from context, scope, WBS, and risks. Uses dynamic template structure.
---

# Presale Proposal

## Procedure

1. **Read the project template**: Load `workspace/proposal-template.md` from the active project directory. If the file does not exist (legacy projects), fall back to `.agent/references/proposal-template-default.md`. The template defines which sections to generate, their filenames, format, and data sources.
2. **Generate one file per section** in `workspace/proposal/` using the `file` field from the template as filename. Follow the `structure` field for subsection layout and the `format` field for output style.
3. **Customer Feedback Priority**: Pull requirements marked **Critical** from `Confirmed Requirements` table in Deal Context. These MUST be prioritized — weave them naturally at the top or highlight them in Pain Points, Key Features, and Risks. Clients appreciate seeing their core concerns addressed front and center.
4. Key Features section = **natural prose**, business language (non-tech stakeholders must understand). **REQUIRED**: Reference Value Mapping from `pain-scope.md` as content source, but write as **coherent paragraphs** — DO NOT copy the table verbatim. Each feature must naturally weave: pain → solution → business value. Prioritize sharp reasoning and real-world impact over numbers. If using numbers → must have evidence basis (client data, benchmark, comparable project). **NEVER fabricate numbers** — unsubstantiated figures backfire immediately.
5. Wireframes: Delegate to `html-wireframe` skill.
6. Scope section: In-Scope and Out-of-Scope only.
7. Risks section: Assumptions → Risks.
8. Technical Architecture: Use Bullet Points exclusively, NO TABLES in this section.
9. Execution & Delivery Plan: combines Roadmap, Milestones+AC.
10. Budget section: **Consistency rules**: Resource Allocation table MUST include every role from the WBS Role Registry — no phantom roles (in budget but not in WBS), no missing roles (in WBS but not in budget).
11. Payment section: **Total Development Cost MUST exactly equal Budget Total** — no rounding differences. Payment schedule milestones must match Execution milestones exactly (same names, same sequence).

## Conciseness & Information Density

Every sentence must earn its place. Proposals that feel "too wordy" lose credibility — busy stakeholders skim, not read.

### Sentence-Level Rules
1. **One idea per sentence.** If a sentence has two clauses joined by "thereby", "and", "ensuring", or "to optimize" — split or cut the weaker half.
2. **Delete echo phrases.** Do NOT repeat the subject or context the reader already knows. Bad: *"To address the risk of leaking sensitive project meeting information, DailyTools provides authentication..."* → Good: *"Individual user authentication secures project meeting data."*
3. **Cut filler openers.** Remove lead-in phrases that add no information: "In order to address the challenge of...", "To meet client needs...", "In order to optimize...". Start with the **what**, not the **why-prelude**.
4. **Avoid synonym stacking.** Do not chain near-synonyms for emphasis: "robust and powerful", "fast and efficient", "complete and absolute". Pick the stronger word and drop the other.
5. **Numbers over adjectives.** Replace vague intensifiers ("significantly", "greatly", "maximum") with concrete numbers when available. If no number exists, drop the intensifier.

### Section-Level Rules
6. **Section 1 (Overview):** Problem statement ≤ 3 sentences + ≤ 4 bullet pain points. Goals ≤ 2 sentences + ≤ 4 bullet benefits. Total section ≤ 350 words.
7. **Section 2 (Solution):** Solution overview ≤ 3 sentences. Each Key Feature description ≤ 2 sentences (feature name in bold, then direct description). No "in order to solve problem X" preamble per feature.
8. **Section 3 (Scope):** Each In-Scope bullet: bold name + 1 sentence. Each Out-of-Scope bullet: bold name + 1 reason sentence.
9. **Section 4 (Risks):** Each assumption ≤ 1 sentence. Each risk: 1 sentence description + 1 sentence mitigation.
10. **Section 5 (Technical):** Each tech stack item: bold name + 1 "why" sentence. Capacity/Security bullets ≤ 1 sentence each.

### Self-Check Before Saving
- Read each paragraph aloud. If you run out of breath, the sentence is too long.
- Count connector words (thereby, ensuring, while, as well as). Target: ≤ 1 per paragraph.
- If removing a sentence changes nothing about what the reader understands, delete it.

## Voice, Tone & Language

### Language Policy
- Each proposal is written in **one language only** — either Vietnamese or English, never mixed.
- Language is determined by the project's `context.md` field `Language` or the language of the client input. If unclear, default to Vietnamese for domestic clients, English for international clients.
- All instructions and rules are documented in English for the AI. Write the final proposal files in the targeted language using these guidelines.

### Tone Philosophy: Business-First, Tech-Credible

The proposal's primary reader is a **business decision-maker** (CEO, CTO, VP, Head of Product) — someone who approves budgets, not someone who writes code. Write like a senior consultant presenting to a client in a meeting room: confident, direct, no fluff.

**Core principles:**
- Lead with **business impact**, follow with **how**. The reader cares about "what changes for my business" before "what technology makes it happen."
- Technical terms are welcome when they add precision — but always explain the *business reason* for a technical choice, not just the choice itself.
- No grandiose promises. No "revolutionary", "game-changing", "cutting-edge". Say what you mean, plainly.
- Use the simplest word that carries the meaning. If "reduce" works, don't write "fully optimize the reduction of."

### Per-Section Tone Calibration

| Section | Tone Lean | Guideline |
| --- | --- | --- |
| 01 - Project Overview | **100% Business** | Pain points in business language. No tech jargon. Reader = CEO/VP. |
| 02 - Proposed Solution | **80% Business / 20% Tech** | Features described by business value. Tech names (API, WebSocket) appear only as supporting detail. |
| 03 - Project Scope | **70% Business / 30% Tech** | Scope items named by business function. Brief tech detail only when it clarifies boundaries. |
| 04 - Risks & Assumptions | **90% Business** | Risks framed as business consequences (cost, delay, compliance). Mitigations can mention tech approach briefly. |
| 05 - Technical Architecture | **30% Business / 70% Tech** | This is where tech depth lives. But each tech choice must still answer "why this benefits the project" — not just "what it is." |
| 06 - Execution Plan | **100% Business** | Timeline, milestones, acceptance criteria — pure project management language. |
| 07 - Budget | **100% Business** | Costs, resource allocation, ROI framing. No tech explanations. |
| 08 - Payment Schedule | **100% Business** | Contract-level language. Clear, unambiguous. |

### Format Rules

- **No horizontal rules `---`** before or after headings. Let Markdown heading hierarchy structure the document.
- **No decorative emoji** (`💡`, `🔴`, `⭐`, `⚠️`) in headings or blockquotes. Use plain text labels.
- **Vary bullet structure** — don't repeat `- **Name** — Description` for every item. Mix prose paragraphs, colon separators, and direct statements.
- **No placeholder instructions** like `*(Features structured by...)*`. Present content directly.
- **Tables**: Only for Roadmap (6.1), Milestones (6.2), Resource Allocation (7.1), and Operational Cost (7.2). Each table must have 1–2 sentences of lead-in prose above it.
- **Prose/Bullets**: All other sections. Fluent, professional language.

### Anti-Pattern Reference

| Anti-Pattern | Bad Example | Fix |
| --- | --- | --- |
| Filler opener | "In order to address the challenge of fragmented meeting records, the system provides a centralized Dashboard." | "The Dashboard centralizes all processed meetings in one view." |
| Echo preamble | "To eliminate the significant overhead of manual scriptwriting that content creators currently face, the tool integrates a web scraper API alongside OpenAI GPT-4o." | "The tool scrapes URL content and structures it into narration scripts via GPT-4o." |
| Synonym stack | "robust and powerful", "fast and efficient" | "robust" or "fast" — pick one. |
| Ornate language | "cutting-edge architecture", "state-of-the-art solution", "seamlessly integrated" | "architecture", "solution", "integrated" |
| Over-explaining tech to CEO | "The system uses exponential backoff with jittered retry intervals and heartbeat ping frames at 30-second cadence to maintain WebSocket persistence through Cloudflare's idle timeout." | "Connections auto-recover within seconds if interrupted, keeping data displays accurate." |

