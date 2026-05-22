# Refactor: Agent Model for Presale Pipeline

## Overview

Convert the presale system from an "orchestrator + flat skills" model to an "orchestrator + agents + skills" model — where each agent is an expert persona owning a group of stages, possessing branching logic (Stop/Assume Rules), and communicating with clients via a standardized Comm Hub.

**Keep unchanged:** The 7-stage pipeline, all skill procedures, references, and output formats.
**Newly added:** The agent layer on top of skills, the Comm Hub, and the Assumption Ledger.

---

## Overall Architecture (ASCII)

```
                              [ USER INPUT ]
                                    |
                                    v
      +================================================================+
      |                        ORCHESTRATOR                             |
      |                                                                 |
      |  1. Read status.md → determine current stage                    |
      |  2. Map stage → agent owner                                     |
      |  3. Load agents/<agent>/AGENT.md                                |
      |  4. Agent selects skill (stage) to run                          |
      |  5. Receive result → handoff or loop                            |
      +================================================================+
                  |                    |                    |
                  v                    v                    v
      +====================+  +====================+  +====================+
      |    SENIOR BA       |  | SOLUTION ARCHITECT |  |    SENIOR PM       |
      |    (Agent)         |  |    (Agent)         |  |    (Agent)         |
      |                    |  |                    |  |                    |
      | Owns:              |  | Owns:              |  | Owns:              |
      |  Stage 1: Discovery|  |  Stage 3: Scope    |  |  Stage 4: WBS      |
      |  Stage 2: Context  |  |  Stage 3.5: Tech   |  |  Stage 5: Proposal |
      |                    |  |                    |  |  Stage 6: Review   |
      +=========+=========++  +=========+=========++  +=========+==========+
                |          |            |          |            |          |
                v          v            v          v            v          v
      +====================================================================+
      |                         SKILLS LAYER                                |
      |                                                                     |
      |  discovery | context | scope | technical | wbs | proposal | review  |
      |  architecture | wireframe | slides | transale                       |
      +====================================================================+
                          |                          |
            +-------------+                          +-------------+
            v                                                      v
      +------------------+                              +--------------------+
      |    COMM HUB      |                              | ASSUMPTION LEDGER  |
      |  (Shared Agent)  |                              |  (Shared Skill)    |
      |                  |                              |                    |
      | - Tone Switcher  |                              | - Record assumption|
      | - Batch questions|                              | - Classify impact  |
      | - Standard format|                              | - Track status     |
      |                  |                              | - Review gate check|
      +--------+---------+                              +--------------------+
               |                                                   |
               v                                                   |
      +----------------+                                           |
      |     CLIENT     | --(responds)--> Orchestrator loop         |
      +----------------+                                           |
                                                                   v
      +====================================================================+
      |                    WORKSPACE (Shared State)                          |
      |                                                                     |
      |  discovery.md | deal-context.md | backlog-questions.md              |
      |  pain-scope.md | technical.md | wbs.md | proposal/                  |
      |  assumption-ledger.md | status.md | change-log.md | context.md      |
      +====================================================================+
                                       |
                                       v
      +====================================================================+
      |                    REFERENCES (Templates)                            |
      +====================================================================+
```

---

## Detailed Processing Flow

```
                           [ USER INPUT ]
                                 |
                                 v
                        +------------------+
                        |   ORCHESTRATOR   |
                        +--------+---------+
                                 |
                 +---------------+---------------+
                 |  Routing logic:               |
                 |  1. Read status.md            |
                 |  2. Map stage → agent         |
                 |  3. Load AGENT.md             |
                 +---------------+---------------+
                                 |
                                 v
                 +===============================+
                 |        ACTIVE AGENT           |
                 +===============================+
                                 |
                                 v
                 +-------------------------------+
                 |   Run Skill (stage procedure) |
                 +---------------+---------------+
                                 |
                                 v
                        /==================\
                       /   VERIFY INFO      \
                       \  (Stop/Assume)     /
                        \==================/
                          |       |       |
              +-----------+       |       +-----------+
              |                   |                   |
        (Missing Core)       (Sufficient)      (Missing Details)
         STOP RULE                             ASSUME RULE
              |                   |                   |
              v                   |                   v
       +-------------+            |         +-------------------+
       |    HOLD     |            |         | ASSUMPTION LEDGER |
       +------+------+            |         +--------+----------+
              |                   |                  |
              v                   |                  |
       +-------------+            |                  |
       |  COMM HUB   |            |                  |
       +------+------+            |                  |
              |                   |                  |
              v                   |                  |
       [Ask Client]               |                  |
              |                   |                  |
              v                   |                  |
       [Client Responds]          |                  |
              |                   |                  |
              v                   v                  v
              +------------------+------------------+
                                 |
                                 v
                 +-------------------------------+
                 |    AGENT COMPLETES STAGE      |
                 |    → Write workspace artifact |
                 |    → Update status.md         |
                 +---------------+---------------+
                                 |
                                 v
                        +------------------+
                        |   ORCHESTRATOR   |
                        |   Handoff Logic  |
                        +--------+---------+
                                 |
                 +---------------+---------------+
                 |                               |
                 v                               v
       +-------------------+          +--------------------+
       | NEXT STAGE        |          | HANDOFF TO         |
       | (same Agent)      |          | NEXT AGENT         |
       +-------------------+          +--------------------+
```

---

## Directory Structure

```
.agent/
├── README.md                            ← Update: describe new model
├── rules.md                             ← Update: add Stop/Assume Rules
├── improvement-backlog.md
│
├── agents/                              ← NEW
│   ├── senior-ba/
│   │   └── AGENT.md
│   ├── solution-architect/
│   │   └── AGENT.md
│   ├── senior-pm/
│   │   └── AGENT.md
│   └── comm-hub/
│       └── AGENT.md
│
├── skills/                              ← Unchanged + 1 new
│   ├── orchestrator/SKILL.md            ← Update: 2-level routing
│   ├── discovery/SKILL.md
│   ├── context/SKILL.md
│   ├── scope/SKILL.md
│   ├── technical/SKILL.md
│   ├── wbs/SKILL.md
│   ├── proposal/SKILL.md
│   ├── review-finalize/SKILL.md
│   ├── assumption-ledger/SKILL.md       ← NEW
│   ├── architecture/SKILL.md
│   ├── wireframe/SKILL.md
│   ├── transale/SKILL.md
│   └── slides/SKILL.md
│
├── workflows/                           ← Content updates
│   ├── presale-run.md                   ← Update: flow via agents
│   ├── presale-update.md                ← Minor update
│   ├── presale-init.md
│   ├── presale-finalize.md
│   ├── presale-preview.md
│   ├── presale-slides.md
│   └── presale-export.md
│
├── references/                          ← Unchanged + 1 new
│   ├── assumption-ledger.md             ← NEW: template
│   ├── backlog-questions.md
│   ├── change-log.md
│   ├── checklist.md
│   ├── deal-context.md
│   ├── pain-scope.md
│   ├── proposal-index.md
│   ├── proposal-template-default.md
│   ├── status.md
│   ├── wbs.md
│   └── designs/
│       ├── documents.md
│       ├── export-template.html
│       └── slides.md
│
└── scripts/
    └── presale_cli.py
```

---

## Agent Details

### Agent: Senior BA

**File:** `agents/senior-ba/AGENT.md`

**Persona:** Senior Business Analyst with 10+ years of presale experience. Focuses on correctly understanding customer needs before anyone starts designing the solution.

**Stages owned:**
- Stage 1: Discovery (skill: `discovery`)
- Stage 2: Context (skill: `context`)

**Responsibilities:**
- Normalize raw client inputs
- Classify information: fact / assumption / decision / open question
- Identify missing information
- Maintain deal-context.md as the single source of truth

**Stop Rule (core info — MUST ask the client):**
- Business goal / objectives
- Target users / personas
- Budget range
- Strict timelines / deadlines
- Platform choice (web / mobile / both)
- Number of primary user roles
- Mandatory external integrations

**Assume Rule (minor details — can assume):**
- Caching strategy (Redis vs Memcached)
- CI/CD tooling
- Library/framework choices (if scope is unaffected)
- Internal naming conventions
- Monitoring/logging stack
- Development methodology (Agile/Scrum — default: Scrum)

**Handoff to Solution Architect when:**
- `workspace/discovery.md` exists
- `workspace/deal-context.md` exists
- No remaining unanswered Stop Rule questions
- Or: questions asked > 2 times with no response → promote to assumption + record in Ledger

---

### Agent: Solution Architect

**File:** `agents/solution-architect/AGENT.md`

**Persona:** Solution Architect with expertise in system design and technical trade-offs. Converts business requirements into a deliverable solution scope.

**Stages owned:**
- Stage 3: Scope (skill: `scope`)
- Stage 3.5: Technical (skill: `technical`)

**Sub-skills callable:**
- `architecture` — draw ASCII diagrams
- `wireframe` — draw wireframes for UI screens

**Responsibilities:**
- Convert requirements into pain points + business impact
- Build the scope register (in-scope / out-of-scope / future phase)
- Propose technical decisions (if the human SA has not provided them)
- Control scope creep

**Stop Rule (core info — MUST ask the client):**
- Greenfield vs Brownfield project
- Compliance/regulatory requirements (PCI, HIPAA, SOC2, etc.)
- Performance requirements (concurrent users, response time)
- Data migration requirements
- 3rd-party system constraints (API versions, rate limits)

**Assume Rule (minor details — can assume):**
- Database engine (default: PostgreSQL)
- Cloud provider (default: AWS)
- API style (default: REST, gRPC for internal services)
- Authentication method (default: JWT + OAuth2)
- Container orchestration (default: Kubernetes for Enterprise)

**Handoff to Senior PM when:**
- `workspace/pain-scope.md` exists
- Scope register has at least 1 approved in-scope item
- `workspace/technical.md` exists OR stage 3.5 is skipped (tech already in context)

**Loop back to Senior BA when:**
- A scope item cannot be mapped to any requirement in deal-context
- The client provides feedback that expands scope → requires a Context update first

---

### Agent: Senior PM

**File:** `agents/senior-pm/AGENT.md`

**Persona:** Senior Project Manager specializing in delivery planning and proposal writing. Converts scope into concrete deliverables and a persuasive proposal.

**Stages owned:**
- Stage 4: WBS (skill: `wbs`)
- Stage 5: Proposal (skill: `proposal`)
- Stage 6: Review & Finalize (skill: `review-finalize`)

**Sub-skills callable:**
- `wireframe` — draw wireframes for the proposal
- `slides` — generate slide decks

**Responsibilities:**
- Create the WBS based on approved scope
- Write the multi-section proposal
- Review consistency across all artifacts
- Gate finalization

**Stop Rule (core info — MUST ask the client):**
- Payment terms
- Preferred delivery model (fixed price / T&M / hybrid)
- Team composition preferences (onshore / offshore / mixed)
- Warranty/support period requirements
- Specific milestone deadlines (if any)

**Assume Rule (minor details — can assume):**
- Sprint duration (default: 2 weeks)
- Buffer percentage (default: 15-20%)
- Communication cadence (default: weekly status report)
- Documentation deliverables (standard set)
- QA approach (default: manual + automated)

**Handoff (end of pipeline) when:**
- Review gate PASS
- Assumption Ledger: no High-impact items are unconfirmed
- All finalization conditions met

**Loop back to Solution Architect when:**
- A WBS task cannot be mapped to any scope item
- Scope conflict or gap is detected
- A technical assumption requires SA confirmation

---

### Agent: Comm Hub

**File:** `agents/comm-hub/AGENT.md`

**Persona:** Communication specialist — does not own any stage, called only when other agents need to ask the client a question (Stop Rule triggered).

**Trigger:** Any agent encounters a Stop Rule → call Comm Hub before outputting questions.

**Functions:**

1. **Tone Switcher:**
   - Client is CTO/Tech Lead → use technical language with specific examples
   - Client is CEO/Business → use business value, ROI-focused language
   - Client is PM/PO → use delivery, timeline, and risk-focused language
   - Default: business tone (if stakeholder type is unknown)

2. **Batching:**
   - If > 1 pending question → batch into a single block
   - Max 5 questions per call (to avoid overwhelming the client)
   - Prioritize blocking questions first

3. **Standard Format:**
   - 3 options + 1 recommendation per question
   - Clearly state the impact (affects scope / timeline / cost / risk)
   - Number questions for easy client responses

4. **Language matching:**
   - Vietnamese input → Vietnamese questions
   - English input → English questions
   - Do not mix languages

---

## Shared Skill Details: Assumption Ledger

**File:** `skills/assumption-ledger/SKILL.md`

**Purpose:** Centrally track all assumptions created during the pipeline. Provide visibility for the Review gate and the client.

### When it is called

Any agent triggers an Assume Rule → calls Assumption Ledger to record it.

### Data Structure

```markdown
## Assumption Ledger

| ID   | Assumption                    | Created By | Stage     | Impact | Status           | Note                    |
|------|-------------------------------|------------|-----------|--------|------------------|-------------------------|
| A-1  | Redis for session caching     | SA         | Technical | Low    | Active           | Swap-able, no scope hit |
| A-2  | 3 user roles (Admin/User/PM)  | BA         | Discovery | Medium | Pending confirm  | Asked 2025-05-20        |
| A-3  | No legacy data migration      | SA         | Scope     | High   | Confirmed        | Client confirmed email  |
| A-4  | PostgreSQL as primary DB      | SA         | Technical | Low    | Active           | Standard choice         |
```

### Impact Classification

| Impact | Definition | Examples |
|--------|------------|----------|
| Low | Incorrect → only changes implementation details, no scope/cost impact | Caching engine, logging tool |
| Medium | Incorrect → changes effort estimate or timeline | Number of user roles, API complexity |
| High | Incorrect → changes scope, cost, or architecture | Migration required, compliance, platform choice |

### Status Lifecycle

```
Active → Confirmed (client confirmed)
Active → Rejected (client rejected → trigger re-scope)
Active → Replaced (replaced by another assumption)
Pending confirm → Confirmed / Rejected
```

### Integration with Review Gate

The Review agent (Stage 6) MUST check the Assumption Ledger:
- Any assumption with impact=High and status≠Confirmed → **BLOCK finalization**
- Any assumption with impact=Medium and status=Active > 7 days → **WARNING**
- List all Active assumptions in the proposal (Section: Assumptions & Risks)

### Output

File: `workspace/assumption-ledger.md`
Template: `references/assumption-ledger.md`

---

## Interaction Rules Between Components

### Rule 1: Agents DO NOT call each other directly

```
❌ Senior BA calls Solution Architect
✅ Senior BA → returns result → Orchestrator → loads Solution Architect
```

The Orchestrator is the sole coordination center.

### Rule 2: Agents only call skills they own

```
Senior BA active:
  → skills/discovery/SKILL.md    ✅ (owned skill)
  → skills/scope/SKILL.md        ❌ (owned by SA)
```

### Rule 3: Shared skills/agents can be called from anywhere

- Comm Hub: called by any agent that needs to ask the client
- Assumption Ledger: called by any agent that creates an assumption

### Rule 4: Communicate via workspace artifacts

Agents do not message each other. Communication is done by reading the artifacts of previous agents:

| Artifact | Written by | Read by |
|----------|------------|---------|
| discovery.md | Senior BA | SA, PM |
| deal-context.md | Senior BA | All |
| backlog-questions.md | Senior BA | Updated by Comm Hub |
| pain-scope.md | Solution Architect | PM |
| technical.md | Solution Architect | PM |
| wbs.md | Senior PM | Review |
| proposal/ | Senior PM | Review |
| assumption-ledger.md | All (write) | Review (verify) |
| status.md | Orchestrator | All (read) |
| context.md | Senior BA (Context skill) | All (resume) |

### Rule 5: Conditional Handoffs

| From → To | Condition |
|-----------|-----------|
| BA → SA | discovery.md + deal-context.md EXIST, no active Stop Rules |
| SA → PM | pain-scope.md EXISTS, scope register has ≥1 approved item |
| PM → Done | Review gate PASS, Ledger has no High unconfirmed items |
| SA → BA (loop back) | Scope item does not map to any requirement |
| PM → SA (loop back) | WBS conflicts with scope |
| Any → Comm Hub | Stop Rule triggered |
| Any → Assumption Ledger | Assume Rule triggered |

---

## Changes to rules.md

### New: Stop Rule / Assume Rule (replacing rules #1 and #2)

```markdown
## 1. Stop Rule — Core Information

When an agent detects missing information that belongs to its Stop Rule list:
1. Halt the current stage
2. Mark status = HOLD
3. Call Comm Hub to format the questions
4. Wait for client response before continuing

Boundary: "If this information is INCORRECT, it will change the scope, effort, or cost → Stop Rule."

## 2. Assume Rule — Minor Details

When an agent detects missing information that belongs to its Assume Rule list:
1. Select a reasonable default value
2. Call the Assumption Ledger to record it (ID, description, impact, status=Active)
3. Continue the stage — do not stop, do not ask the client

Boundary: "If this information is INCORRECT, it only changes implementation details → Assume Rule."

## Escalation

- Assumption Active > 7 days + impact Medium → escalate to Stop Rule in the next stage
- Assumption Rejected by client → trigger re-scope (loop back)
```

### Unchanged (renumbered)

- Rule #3: Every scope item needs a source
- Rule #4: Proposal ↔ WBS must match
- Rule #5: Never expand scope silently
- Rule #6: Greenfield vs Brownfield
- Rule #7: Think before generating
- Rule #8: Stages run in order (UPDATE: add handoff conditions)
- Rule #9: Artifact must exist before marking Done
- Rule #10: Match the client's language
- Rule #11: Conserve tokens

---

## Changes to Orchestrator

### New Orchestrator: 2-Level Routing

```markdown
## Stage → Agent Mapping

| Stage | Agent | Skill |
|-------|-------|-------|
| 1. Discovery | Senior BA | discovery |
| 2. Context | Senior BA | context |
| 3. Scope | Solution Architect | scope |
| 3.5. Technical | Solution Architect | technical |
| 4. WBS | Senior PM | wbs |
| 5. Proposal | Senior PM | proposal |
| 6. Review | Senior PM | review-finalize |

## Routing Procedure

1. Read `workspace/status.md` → determine current stage
2. Map stage → agent (using the table above)
3. Load `agents/<agent>/AGENT.md` (persona + rules)
4. Load `skills/<skill>/SKILL.md` (procedure)
5. Agent executes the skill with Stop/Assume logic
6. Result handling:
   - Stage completed → verify handoff conditions → next stage/agent
   - Stop Rule triggered → load Comm Hub → HOLD
   - Assume Rule triggered → call Assumption Ledger → continue
   - Loop back needed → revert to previous agent

## Handoff Conditions

BA → SA:
  - workspace/discovery.md EXISTS
  - workspace/deal-context.md EXISTS
  - No active unanswered Stop Rule questions

SA → PM:
  - workspace/pain-scope.md EXISTS
  - Scope register has ≥1 approved in-scope item
  - workspace/technical.md EXISTS or skip condition met

PM → Done:
  - Review gate PASS
  - assumption-ledger.md: no items with impact=High and status≠Confirmed

## Loop Back Triggers

SA → BA: scope item does not map to a requirement in deal-context
PM → SA: WBS task does not map to a scope item, or scope conflict detected
Any → same agent (retry): client responds after HOLD → resume stage
```

---

## Changes to presale-run.md

### Updated Flow

```markdown
## Trigger

1. Load `.agent/rules.md` (once per session)
2. Load orchestrator routing table
3. Locate active project folder
4. Check client-input.md has content
5. Orchestrator determines current stage + agent
6. Load AGENT.md → load SKILL.md → run stage
7. After each stage: state output, check handoff, recommend next stage

## Stages (same table, added Agent column)

| # | Agent | Skill | In | Out | Gate |
|---|-------|-------|----|----|------|
| 1 | Senior BA | discovery | Raw input | Intake, facts, questions | Unknowns visible |
| 2 | Senior BA | context | Answers, feedback | Deal context, change log | Info classified |
| 3 | Sol. Architect | scope | Context, requirements | Pain points, scope register | Items mapped |
| 3.5 | Sol. Architect | technical | Scope, NFRs | Architecture, tech decisions | Optional |
| 4 | Senior PM | wbs | Scope, solution | WBS draft, milestones | WBS maps to scope |
| 5 | Senior PM | proposal | All artifacts | Proposal (multi-section) | Proposal = WBS scope |
| 6 | Senior PM | review-finalize | All artifacts | Review findings or approval | Gates pass |
```

---

## Template: references/assumption-ledger.md

```markdown
# Assumption Ledger

## Overview

| Total | Active | Confirmed | Rejected | High Impact Unconfirmed |
|-------|--------|-----------|----------|------------------------|
| 0     | 0      | 0         | 0        | 0                      |

## Ledger

| ID | Assumption | Created By | Stage | Impact | Status | Date | Note |
|----|-----------|------------|-------|--------|--------|------|------|
|    |           |            |       |        |        |      |      |

## Rules

- ID format: A-{n} (sequential, never reuse)
- Impact: Low / Medium / High
- Status: Active / Pending confirm / Confirmed / Rejected / Replaced
- High + unconfirmed → blocks finalization
- Medium + Active > 7 days → escalate to Stop Rule
```

---

## End-to-End Flow Example

```
1. User pastes client email (Vietnamese)

2. Orchestrator:
   - status.md: no stage yet → Stage 1
   - Map: Stage 1 → Senior BA → discovery skill
   - Load: agents/senior-ba/AGENT.md + skills/discovery/SKILL.md

3. Senior BA executes Discovery:
   - Normalize input → extract facts
   - Check Stop Rule list:
     ✗ Business goal: yes (in email)
     ✗ Target users: yes
     ✗ Budget: MISSING → Stop Rule triggered
     ✗ Timeline: MISSING → Stop Rule triggered
   - Check Assume Rule list:
     ✗ CI/CD: missing → assume GitHub Actions → call Assumption Ledger (A-1, Low)
   - 2 Stop Rule questions → call Comm Hub

4. Comm Hub:
   - Detect: stakeholder unknown → use business tone (default)
   - Batch: 2 questions → 1 block
   - Format: 3 options + 1 recommendation for each
   - Output questions for the user
   - Status = HOLD

5. User pastes client answers

6. Orchestrator:
   - Status = HOLD → resume Senior BA
   - Load: agents/senior-ba/AGENT.md + skills/context/SKILL.md (Stage 2)

7. Senior BA executes Context:
   - Classify input: budget = fact, timeline = decision
   - Update deal-context.md
   - Verify: no remaining missing Stop Rule items
   - Stage 2 done

8. Orchestrator:
   - Handoff check: discovery.md ✓, deal-context.md ✓, no Stop Rule active ✓
   - Handoff → Solution Architect
   - Load: agents/solution-architect/AGENT.md + skills/scope/SKILL.md

9. Solution Architect executes Scope:
   - Read deal-context.md
   - Build pain points + scope register
   - Check Stop Rule: Greenfield? → in context ✓
   - Check Assume Rule: DB engine missing → assume PostgreSQL → Ledger (A-2, Low)
   - Stage 3 done

10. ... continue to Stage 6 Review
```

---

## Refactoring Checklist

### Phase 1: Create agents/ (without breaking existing setups)

- [x] Create `agents/senior-ba/AGENT.md`
- [x] Create `agents/solution-architect/AGENT.md`
- [x] Create `agents/senior-pm/AGENT.md`
- [x] Create `agents/comm-hub/AGENT.md`

### Phase 2: Create Assumption Ledger

- [x] Create `skills/assumption-ledger/SKILL.md`
- [x] Create `references/assumption-ledger.md` (template)

### Phase 3: Update rules.md

- [x] Replace rules #1 and #2 with Stop Rule / Assume Rule
- [x] Keep rules #3-#11 (renumber if necessary)

### Phase 4: Update Orchestrator

- [x] Add Stage → Agent mapping table
- [x] Add 2-level routing logic
- [x] Add handoff conditions
- [x] Add loop back triggers

### Phase 5: Update workflows

- [x] Update `presale-run.md`: add Agent column, flow via agents
- [x] Update `presale-update.md`: revisions go through the correct agent owner

### Phase 6: Update documentation

- [x] Update `README.md`: describe new model
- [x] Update `CLAUDE.md`: new routing table

### Phase 7: Test

- [ ] Run test `/presale-run` with a new project
- [ ] Verify BA → SA handoff works
- [ ] Verify SA → PM handoff works
- [ ] Verify Stop Rule → Comm Hub → HOLD → resume works
- [ ] Verify Assume Rule → Ledger records correctly
- [ ] Verify Review gate checks the Ledger

---

## Risks & Mitigation

| Risk | Level | Mitigation |
|------|-------|------------|
| Agent personas too long, wasting tokens | Medium | Keep AGENT.md < 80 lines, only containing personas + rules, no procedures |
| Orchestrator more complex, routing errors | Medium | Clear handoff conditions based on file existence (easy to verify) |
| Comm Hub adds a step → slower | Low | Comm Hub only formats, does not generate new content |
| Assumption Ledger forgotten | Low | Embed reminders in each AGENT.md: "When assuming → call Ledger" |
| Backward compatibility with old projects | Low | Skills retain procedures, only adding agent layer on top |
