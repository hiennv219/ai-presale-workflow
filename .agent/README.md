# Agent System

```
User Input → Orchestrator → Skill Agent → Output Artifact
                ↑                              |
                └──────── Next Stage ──────────┘
```

## Orchestrator

**File:** `skills/orchestrator/SKILL.md`

Routing layer — does not produce artifacts. Determines which skill to invoke based on:

- User intent (what they typed or asked for)
- Available artifacts (what has already been produced)
- Pipeline position (which stage comes next)

---

# Skill Agents

Reference for all skill agents in this workspace. The orchestrator routes to these agents based on user intent and pipeline position.

---

## 1. Discovery Agent

**File:** `skills/discovery/SKILL.md`

**Purpose:** Normalize raw customer input and generate clarification questions.

**Behavior:**
- Summarizes raw input without adding unsupported facts
- Extracts confirmed facts (explicitly stated by client)
- Identifies missing info affecting scope/WBS/proposal/timeline/cost/risk
- Generates clarification questions: 3 options, 1 recommendation each

**Assumptions Rule:** Ask first, assume later. Every item affecting scope/effort/timeline must be a question before it can become an assumption. Minor technical details (caching, tooling, library choices) may be assumed directly.

**Output:** `workspace/discovery.md`, `workspace/backlog-questions.md`

---

## 2. Context Agent

**File:** `skills/context/SKILL.md`

**Purpose:** Update and compress deal context from customer answers, notes, Q&A, and feedback.

**Behavior:**
- Classifies new input: fact, clarification, correction, decision, assumption, constraint, risk, scope change, preference
- Updates deal context before any artifact edits
- Merges duplicates, removes obsolete notes
- Preserves traceability via decisions + change log
- Compresses long history into rolling summary
- Hands off to Scope Agent if feedback expands scope

**Output:** `workspace/deal-context.md`, `workspace/change-log.md`

---

## 3. Scope Agent

**File:** `skills/scope/SKILL.md`

**Purpose:** Analyze pain points and define solution scope with scope-creep control.

**Behavior:**
- Converts confirmed requirements into pain points + business impact
- Marks root causes as hypotheses unless confirmed
- Defines solution direction
- Builds scope register: in-scope, out-of-scope, future phase, pending decisions
- Runs impact check for any new/expanded request
- Provides 3 options per scope change candidate (include / future phase / exclude)

**Scope Change Triggers:** New user groups, platforms, integrations, reports, AI/automation, migration, compliance, uptime/scale, support, timeline changes.

**Output:** `workspace/pain-scope.md`

---

## 4. WBS Agent

**File:** `skills/wbs/SKILL.md`

**Purpose:** Create or revise Work Breakdown Structure from approved scope.

**Behavior:**
- Uses approved in-scope items only
- Groups work into delivery phases
- Breaks each phase into tasks with: deliverable, owner role, dependency, assumption, estimate range, acceptance criteria, scope reference
- Flags any task not mapped to approved scope
- Estimates as range if detail is incomplete
- Marks customer dependencies explicitly

**Output:** `workspace/wbs.md`

---

## 5. Proposal Agent

**File:** `skills/proposal/SKILL.md`

**Purpose:** Create or revise the presale proposal from context, scope, WBS, and risks.

**Behavior:**
- Reflects customer context and pain points before presenting solution
- Uses approved scope register
- Uses WBS summary for implementation plan
- Includes assumptions, risks, out-of-scope, next steps
- Never adds deliverables missing from WBS
- Uses multi-section file structure in `workspace/proposal/`

**Revision Rule:** Revise affected sections only. Never regenerate full proposal unless scope/positioning changed significantly.

**Output:** `workspace/proposal/` (multi-file)

---

## 6. Review & Finalize Agent

**File:** `skills/review-finalize/SKILL.md`

**Purpose:** Review artifacts for consistency and scope creep. Approve or block finalization.

**Behavior:**
- Checks proposal against WBS
- Checks WBS against approved scope
- Checks scope against requirements/decisions/assumptions
- Flags unapproved scope changes
- Flags assumptions written as facts
- Flags missing dependencies, risks, acceptance criteria, open questions

**Finalization Gate (all must pass):**
- No critical open questions
- No unapproved scope changes
- Proposal and WBS use same scope
- Assumptions accepted or explicitly listed
- Out-of-scope explicit
- Final version and date present

**Output:** Review findings table (if not ready) or finalization approval (if ready)

---

## 7. Transale Agent

**File:** `skills/transale/SKILL.md`

**Purpose:** Translate Markdown documents between English, Japanese, and Vietnamese while preserving structure and technical accuracy.

**Behavior:**
- Preserves all Markdown formatting: headings, tables, lists, code blocks, links, images
- Does NOT translate technical terms, acronyms, product names, file paths, or code
- Adapts tone per language: professional English, です/ます Japanese, natural Vietnamese business writing
- Validates structure match between source and output (heading count, table count, list items)
- Supports single file, directory, and incremental translation

**Standalone:** This agent runs independently via `/presale-transale` — it is not part of the main pipeline stages.

### Usage

```
/presale-transale proposal ja        → Incremental: chỉ dịch section thay đổi, concat kết quả
/presale-transale proposal ja force  → Dịch lại toàn bộ sections
/presale-transale wbs ja             → Dịch single file
/presale-transale workspace/scope/ vi → Dịch cả thư mục
```

**Output:**
- Single/directory: `{{name}}_{{lang}}.md` cùng thư mục source
- Incremental: `workspace/proposal_{{lang}}/` + `workspace/proposal-full_{{lang}}.md`

---

## 8. Technical Agent

**File:** `skills/technical/SKILL.md`

**Purpose:** Propose technical decisions when SA has not provided them.

**Behavior:**
- Runs only when deal-context has no confirmed technical decisions
- Proposes: architecture pattern, tech stack, infrastructure approach, key trade-offs
- Draws system architecture using `architecture` skill
- Writes component communication narrative grouped by delivery phases
- Identifies 3rd-party services and pass-through cost models
- All outputs marked as "proposed" until SA/user confirms

**Output:** `workspace/technical.md`

---

## 9. Architecture Agent (Sub-skill)

**File:** `skills/architecture/SKILL.md`

**Purpose:** Draw ASCII architecture diagrams and Mermaid data-flow sequences.

**Behavior:**
- Static view: ASCII layered box art (Client → API → Service → Data)
- Dynamic view: Mermaid sequence diagram for data flow
- Annotates phase-specific components with `(Phase N)`
- Keeps width under 80 characters
- Labels every box with technology + responsibilities

**Delegated by:** `technical`, `proposal` (section 5)

---

## 10. Wireframe Agent (Sub-skill)

**File:** `skills/wireframe/SKILL.md`

**Purpose:** Draw ASCII wireframes for UI screens in proposals.

**Behavior:**
- Draws spatial layout using box-drawing characters
- Shows field placement, buttons, data areas with sample data
- One wireframe per screen, default/loaded state
- Never describes a screen with text-only bullet points

**Delegated by:** `proposal` (section 3.2)

---

## Agent Communication

Agents do not call each other directly. The orchestrator mediates all transitions:

1. Agent completes its stage and produces output
2. Orchestrator evaluates next stage based on output + user intent
3. Orchestrator loads the next agent with only the context it needs

This keeps each agent focused and prevents token bloat from loading unnecessary context.

## Token Discipline

All agents follow these rules:
- Load `rules.md` once per session
- Load only the current stage's SKILL.md
- Do not re-read prior artifacts unless the current stage needs them as input
- Use compact deal context, not full chat history
- For revisions, read only the affected section
