# Agent System

```
User Input → Orchestrator → Agent (persona) → Skill (procedure) → Output Artifact
                 ↑                                                      |
                 └─────────── Handoff / Loop Back ──────────────────────┘
```

## Architecture Overview

Three-layer model: **Orchestrator → Agents → Skills**.

- **Orchestrator** (`skills/orchestrator/SKILL.md`): Routing layer — reads `status.md`, maps stage → agent, loads AGENT.md + SKILL.md, checks handoff conditions.
- **Agents** (`agents/<name>/AGENT.md`): Expert personas with stage ownership, Stop/Assume rules, and handoff conditions. Agents do NOT produce artifacts directly — they invoke skills.
- **Skills** (`skills/<name>/SKILL.md`): Procedures that produce artifacts. Each skill has clear inputs, outputs, and gates.

**Shared components:**
- **Comm Hub** (`agents/comm-hub/AGENT.md`): Communication specialist — formats questions for clients when Stop Rule triggers.
- **Assumption Ledger** (`skills/assumption-ledger/SKILL.md`): Tracks all assumptions created during pipeline. Callable by any agent.

---

## Agents

### Senior BA

**File:** `agents/senior-ba/AGENT.md`

**Persona:** Senior Business Analyst with 10+ years of presale experience. Focuses on understanding client needs before solution design begins.

**Stages owned:**

| Stage | Skill |
|-------|-------|
| 1. Discovery | `discovery` |
| 2. Context | `context` |

**Handoff → Solution Architect** when: `discovery.md` + `deal-context.md` exist, no Stop Rule questions pending.

---

### Solution Architect

**File:** `agents/solution-architect/AGENT.md`

**Persona:** System design expert. Converts business requirements into deliverable solution scope.

**Stages owned:**

| Stage | Skill |
|-------|-------|
| 3. Scope | `scope` |
| 3.5. Technical | `technical` |

**Sub-skills:** `architecture`, `wireframe`

**Handoff → Senior PM** when: `pain-scope.md` exists, scope register has ≥1 approved item, `technical.md` exists or skip condition met.

**Loop back → Senior BA** when: scope item doesn't map to any requirement in deal-context.

---

### Senior PM

**File:** `agents/senior-pm/AGENT.md`

**Persona:** Senior Project Manager — delivery planning and proposal writing.

**Stages owned:**

| Stage | Skill |
|-------|-------|
| 4. WBS | `wbs` |
| 5. Proposal | `proposal` |
| 6. Review & Finalize | `review-finalize` |

**Sub-skills:** `wireframe`, `slides`

**Handoff → Done** when: Review gate PASS, no High impact assumptions unconfirmed.

**Loop back → Solution Architect** when: WBS task doesn't map to scope item, or scope conflict detected.

---

### Comm Hub

**File:** `agents/comm-hub/AGENT.md`

**Persona:** Communication specialist — called when any agent triggers Stop Rule.

**Functions:**
- Tone Switcher (CTO → technical, CEO → business, PM → delivery)
- Batching (max 5 questions per block)
- Format (3 options + 1 recommendation per question)
- Language matching (Vietnamese in → Vietnamese out)

---

## Skills

### 1. Discovery

**File:** `skills/discovery/SKILL.md`

**Purpose:** Normalize raw customer input and generate clarification questions.

**Behavior:**
- Summarizes raw input without adding unsupported facts
- Extracts confirmed facts (explicitly stated by client)
- Identifies missing info affecting scope/WBS/proposal/timeline/cost/risk
- Generates clarification questions: 3 options, 1 recommendation each

**Output:** `workspace/discovery.md`, `workspace/backlog-questions.md`

---

### 2. Context

**File:** `skills/context/SKILL.md`

**Purpose:** Update and compress deal context from customer answers, notes, Q&A, and feedback.

**Behavior:**
- Classifies new input: fact, clarification, correction, decision, assumption, constraint, risk, scope change, preference
- Updates deal context before any artifact edits
- Merges duplicates, removes obsolete notes
- Preserves traceability via decisions + change log
- Compresses long history into rolling summary
- Hands off to Scope if feedback expands scope

**Output:** `workspace/deal-context.md`, `workspace/change-log.md`

---

### 3. Scope

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

### 4. WBS

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

### 5. Proposal

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

### 6. Review & Finalize

**File:** `skills/review-finalize/SKILL.md`

**Purpose:** Review artifacts for consistency and scope creep. Approve or block finalization.

**Behavior:**
- Checks proposal against WBS
- Checks WBS against approved scope
- Checks scope against requirements/decisions/assumptions
- Flags unapproved scope changes
- Flags assumptions written as facts
- Flags missing dependencies, risks, acceptance criteria, open questions
- **Checks Assumption Ledger:** High + unconfirmed → BLOCK; Medium + Active > 7 days → WARNING

**Finalization Gate (all must pass):**
- No critical open questions
- No unapproved scope changes
- Proposal and WBS use same scope
- Assumptions accepted or explicitly listed
- Out-of-scope explicit
- Final version and date present
- Assumption Ledger: no High impact unconfirmed

**Output:** Review findings table (if not ready) or finalization approval (if ready)

---

### 7. Assumption Ledger (Shared)

**File:** `skills/assumption-ledger/SKILL.md`

**Purpose:** Track all assumptions created during pipeline. Callable by any agent when Assume Rule triggers.

**Behavior:**
- Assigns sequential ID (A-{n})
- Classifies impact: Low / Medium / High
- Tracks status lifecycle: Active → Confirmed / Rejected / Replaced
- Escalation: Medium + Active > 7 days → promote to Stop Rule

**Output:** `workspace/assumption-ledger.md`

---

### 8. Technical

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

### 9. Architecture (Sub-skill)

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

### 10. Wireframe (Sub-skill)

**File:** `skills/wireframe/SKILL.md`

**Purpose:** Draw ASCII wireframes for UI screens in proposals.

**Behavior:**
- Draws spatial layout using box-drawing characters
- Shows field placement, buttons, data areas with sample data
- One wireframe per screen, default/loaded state
- Never describes a screen with text-only bullet points

**Delegated by:** `proposal` (section 3.2)

---

### 11. Transale (Standalone)

**File:** `skills/transale/SKILL.md`

**Purpose:** Translate Markdown documents between English, Japanese, and Vietnamese while preserving structure and technical accuracy.

**Behavior:**
- Preserves all Markdown formatting: headings, tables, lists, code blocks, links, images
- Does NOT translate technical terms, acronyms, product names, file paths, or code
- Adapts tone per language: professional English, です/ます Japanese, natural Vietnamese business writing
- Validates structure match between source and output (heading count, table count, list items)
- Supports single file and multi-file (directory) translation

**Standalone:** This skill runs independently via `/presale-transale` — it is not part of the main pipeline stages.

**Output:** `{{original_name}}_{{lang_code}}.md` in same directory as source

---

### 12. Slides (Standalone)

**File:** `skills/slides/SKILL.md`

**Purpose:** Transform proposal into slide-deck Markdown structured for external AI handoff.

**Standalone:** Runs via `/presale-slides` — not part of the main pipeline stages.

---

## Agent Communication Rules

1. **Agents do NOT call each other directly.** Orchestrator is the sole mediator for all transitions.
2. **Agents only invoke skills they own.** Sub-skills (architecture, wireframe) are exceptions — delegated by the owning agent.
3. **Shared components** (Comm Hub, Assumption Ledger) are callable from any agent.
4. **Communication via workspace artifacts.** Agents read artifacts produced by prior agents — no direct messaging.
5. **Handoff requires conditions met.** Each agent defines handoff conditions in its AGENT.md.

## Token Discipline

All agents follow these rules:
- Load `rules.md` once per session
- Load only the current agent's `AGENT.md` + current stage's `SKILL.md`
- Do not re-read prior artifacts unless the current stage needs them as input
- Use compact deal context, not full chat history
- For revisions, read only the affected section
