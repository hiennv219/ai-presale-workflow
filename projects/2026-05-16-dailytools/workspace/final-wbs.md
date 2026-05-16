# WBS: DailyTools MVP
**Version**: Final
**Date**: 2026-05-16

## Metadata

- Artifact ID: WBS-DT-001
- Version: Final
- Status: Approved
- Context Version: 1.0
- Date: 2026-05-16

## WBS

| WBS ID | Phase | Task | Deliverable | Owner Role | Dependency | Assumption | Estimate Range | Acceptance Criteria | Scope Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.0 | P1: Foundation | Project Kickoff & Env Setup | Dev Environment | SA / Lead Dev | — | — | 8 - 12h | Repo setup, CI/CD ready | SCOPE004 |
| 1.1 | P1: Foundation | Zoom API Integration | Integration Module | Backend Dev | — | Zoom OAuth access | 24 - 40h | Can fetch recordings from Zoom | SCOPE001 |
| 1.2 | P1: Foundation | Teams API Integration | Integration Module | Backend Dev | — | Teams OAuth access | 24 - 40h | Can fetch recordings from Teams | SCOPE001 |
| 2.1 | P2: AI Core | Audio-to-Transcript Layer | Transcript JSON | AI Engineer | 1.1, 1.2 | LLM API availability | 16 - 24h | High accuracy transcript output | SCOPE002 |
| 2.2 | P2: AI Core | AI Summarization Engine | Summary JSON | AI Engineer | 2.1 | PM-optimized prompts | 24 - 32h | Summaries contain Action Items/Decisions | SCOPE002 |
| 3.1 | P3: Delivery | Jira Integration (Push) | Jira Add-on/App | Fullstack Dev | 2.2 | Jira API Write access | 20 - 30h | Summary appears as Jira ticket/comment | SCOPE003 |
| 3.2 | P3: Delivery | Notion Integration (Push) | Notion Integration | Fullstack Dev | 2.2 | Notion API Write access | 16 - 24h | Summary appears as Notion page | SCOPE003 |
| 4.1 | P4: Launch | E2E Testing & Bug Fixing | QA Report | QA | 3.1, 3.2 | — | 16 - 24h | Zero critical bugs in flow | ALL |
| 4.2 | P4: Launch | User Acceptance (UAT) | Sign-off | PM | 4.1 | Client availability | 8 - 16h | Client confirms UX meets goals | REQ004 |

## Milestones

| Milestone | Description | Exit Criteria |
| --- | --- | --- |
| M1: Capture Ready | Successful recording fetch from Zoom/Teams | Functional API connection in dev env |
| M2: Engine Ready | Reliable meeting summarization (text-to-summary) | 80%+ accuracy on test cases |
| M3: Integration Ready | End-to-end flow from meeting to Jira/Notion | Integrated workflow without manual copy |
| M4: Launch | Project hand-over and MVP live | All P0/P1 tasks completed and signed off |

## Delivery Assumptions

| ID | Assumption | Status | Impact If False |
| --- | --- | --- | --- |
| DA001 | Meeting recordings provide high-quality audio | Active | Summarization accuracy will drop |
| DA002 | OAuth permissions are granted by Client/IT | Active | Integration will be blocked |
| DA003 | Third-party LLM (OpenAI/Claude) is used for summary | Active | Internal model training needed (higher cost) |
