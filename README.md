# AI Presale Workflow

> **A specialized AI assistant that transforms raw customer requirements into structured Proposals and WBS (Work Breakdown Structure) through a controlled, multi-stage pipeline.**

This project is a **Markdown Skill Workspace**. It is not a software application that needs to be built or deployed. It is a workspace designed for AI Assistants (Claude Code, Cursor, Copilot Chat, etc.) to read repository content, execute workflows, and produce output artifacts.

---

## Usage (Slash Commands)

The system operates via slash commands. Type a command and provide information in the AI chat to begin.

### 1. Initialize a Project
Create the standard folder structure for a new project before processing data.
```text
/presale-init project: Acme App
```

### 2. Run the Analysis Pipeline
Feed raw customer requirements into the system. The AI will automatically analyze (Discovery), clarify (Context & Scope), and structure (WBS & Proposal).
```text
/presale-run

Client: Acme Corp
Requirements:
- Build an order management system
- Integrate online payments
- Mobile app for end-users
```
**How it works:** The AI reads the input, works within `workspace/`, and guides you through each stage until the draft Proposal + WBS are complete.

### 3. Update from Feedback
When client feedback or requirement changes arrive, use this command. The system automatically identifies which components are affected and updates only those sections.
```text
/presale-update

Client responded:
- Budget: $200K
- Timeline: 6 months
- Prioritize mobile first
```

### 4. Finalize for Internal Review
When edits and reviews are complete, export Final Proposal and Final WBS documents.
```text
/presale-finalize
```
*Note: The system enforces a Review Gate. If open questions or unconfirmed scope remain, the AI will require resolution before allowing final export.*

### 5. Export Deliverables for Client
Export styled HTML/PDF based on the final Markdown files for client delivery.
```text
/presale-export
```
Deliverables are saved to the `_delivery/` folder.

---

## Directory Structure

The system separates AI behavior configuration from project data.

```text
.agent/                     # AI CONFIGURATION (Workflows, Rules, Templates)
├── rules.md                # Non-negotiable workflow rules
├── workflows/              # Scripts for each slash command
├── skills/                 # Specialized AI skill modules (Discovery, Scope, WBS...)
└── references/             # Output templates and format references

projects/                   # PROJECT WORKSPACE
└── YYYY-MM-DD-<client>/
    ├── _source/            # Raw input (briefs, meeting notes, emails)
    ├── workspace/          # Working files (Context, Scope, Draft WBS, Draft Proposal)
    ├── _delivery/          # Final deliverables for client (HTML, PDF, Final Docs)
    └── status.md           # Progress tracker and current project state
```

---

## Pipeline Stages

The system operates through 6 sequential stages. Each stage has a **Gate** — the AI will not advance if the previous stage's exit criteria are not met.

| # | Stage | Skill | Output |
|:---:|---|---|---|
| **1** | **Discovery** | `discovery` | Intake summary, confirmed facts, clarification questions |
| **2** | **Context** | `context` | Deal context, decisions, assumptions, change history |
| **3** | **Scope** | `scope` | Pain points, in/out scope, risks, scope register |
| **4** | **WBS** | `wbs` | Work breakdown, milestones, resource estimates |
| **5** | **Proposal** | `proposal` | Multi-section proposal draft |
| **6** | **Review & Finalize** | `review-finalize` | Consistency check, finalization approval |

---

## Artifact Flow

Each workflow phase produces specific artifacts. Later phases depend on earlier ones.

```text
/presale-init
│
│  projects/YYYY-MM-DD-<client>/
│  ├── _source/client-input.md        ← template (user fills manually)
│  ├── workspace/                     ← empty
│  ├── _delivery/                     ← empty
│  └── status.md                      ← progress tracker
│
▼
/presale-run (Stage 1 → 6)
│
│  Stage 1 - Discovery
│  └── workspace/discovery.md         ← intake summary, facts, open questions
│
│  Stage 2 - Context (optional if input is complete)
│  └── workspace/context.md           ← decisions, assumptions, risks, change log
│
│  Stage 3 - Scope
│  └── workspace/scope.md             ← pain points, in/out scope, scope register
│
│  Stage 3.5 - Technical (optional if SA provided tech context)
│  └── workspace/technical.md         ← architecture, tech stack, tech decisions
│
│  Stage 4 - WBS
│  └── workspace/wbs.md               ← milestones, tasks, estimates
│
│  Stage 5 - Proposal
│  ├── workspace/proposal/_index.md   ← multi-section draft
│  └── workspace/proposal-full.md     ← assembled full proposal
│
│  Stage 6 - Review & Finalize
│  └── (no new file — validates consistency across artifacts)
│
▼
/presale-finalize
│
│  workspace/final-proposal.md        ← locked proposal after review gate passes
│  workspace/final-wbs.md             ← locked WBS after review gate passes
│
▼
/presale-export
│
│  _delivery/proposal.html            ← styled HTML for client
│  _delivery/wbs.html                 ← styled HTML for client
```

---

## Non-Negotiables

- **No fabrication**: The AI never invents customer facts. If unclear, it asks.
- **No silent scope creep**: Any additional features must be flagged and approved.
- **Proposal-WBS sync**: Both documents must match exactly in scope and timeline. The Review Gate enforces this.
- **Section-level updates**: Only revise affected sections, never regenerate entire files for small changes.
- **Review before export**: Final Proposal and Final WBS cannot be produced until the review gate passes.
