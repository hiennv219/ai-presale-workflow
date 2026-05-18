# WBS: DailyTools MVP

## Metadata

- Artifact ID: WBS-DT-001
- Version: Final
- Status: Approved
- Context Version: 1.1
- Date: 2026-05-17

## WBS

| WBS ID | Phase | Task | Deliverable | Owner Role | Dependency | Assumption | Estimate Range |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.0 | P1: Foundation | Project Kickoff & Env Setup | Dev Environment | Solutions Arch | — | — | 4 - 8h |
| 1.1 | P1: Foundation | Database Setup | DB Schema | Fullstack Dev | 1.0 | Supabase/Postgres | 8 - 12h |
| 2.1 | P2: Core App | Dev Daily Report Form | Web Form UI | Fullstack Dev | 1.1 | Mobile-friendly | 12 - 16h |
| 2.2 | P2: Core App | PM Dashboard (Blocker View) | Dashboard UI | Fullstack Dev | 1.1 | Clear highlights | 16 - 24h |
| 3.1 | P3: AI Engine | LLM API Integration | API Module | Fullstack Dev | 1.0 | OpenAI GPT-4o | 8 - 12h |
| 3.2 | P3: AI Engine | Blocker Extraction Prompting | AI Logic | AI Engineer | 3.1 | Text holds context | 12 - 20h |
| 4.1 | P4: Launch | E2E Testing & Bug Fixing | QA Report | QA Engineer | 2.1, 2.2, 3.2 | — | 12 - 16h |
| 4.2 | P4: Launch | User Acceptance (UAT) | Sign-off | Solutions Arch | 4.1 | Client availability | 4 - 8h |

## Milestones

| Milestone | Description | Exit Criteria |
| --- | --- | --- |
| M1: Form Ready | Web form accepts and stores Dev reports | Form submits to DB successfully |
| M2: AI Ready | AI extracts blockers accurately | 90% accuracy on sample text |
| M3: Dashboard Live | PM can see blockers highlighted | UI renders correctly with AI data |
| M4: Launch | Project hand-over and MVP live | All tasks signed off |

## Delivery Assumptions

| ID | Assumption | Status | Impact If False |
| --- | --- | --- | --- |
| DA001 | Devs will type enough text for AI to detect issues | Active | AI extraction will return false negatives |
| DA002 | Client has OpenAI API Key for processing | Active | Development blocked until key provided |
