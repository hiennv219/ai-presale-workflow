# Deal Context: DailyTools

## Metadata

- Customer: DailyTools
- Context Version: 1.0
- Current Stage: Stage 2: Context
- Last Updated: 2026-05-16

## Rolling Summary

DailyTools is an AI-powered management tool for Project Managers. Following a scope pivot, the MVP now focuses on the simplest possible trial: a lightweight Web Form to collect daily reports from the development team and aggregate blockers to display on the PM Dashboard. Advanced features like Zoom/Teams voice integration, complex AI summarization, and Jira/Notion sync have been deferred to Future Phases.

## Confirmed Requirements

| ID | Requirement | Source | Priority |
| --- | --- | --- | --- |
| REQ001 | Capture meeting content from platforms (Zoom, Teams) | Client Answer (Q001) | Future Phase |
| REQ002 | Generate summaries of meeting content | Client Input | Future Phase |
| REQ003 | Push summaries to PM tools (Jira, Notion) | Client Answer (Q002) | Future Phase |
| REQ004 | Focus on effort optimization for PMs | Client Input | High |
| REQ007 | Collect Daily Reports from dev team via Web Form | Client Input | High |
| REQ008 | Aggregate and extract Blockers from daily reports | Client Input | High |

## Unconfirmed Requirements

| ID | Requirement | Why It Matters |
| --- | --- | --- |
| REQ005 | Support for manual file uploads | Backup if integration fails |
| REQ006 | Notification system (Slack/Email) | Alternative delivery method |

## Scope Register

### In Scope

| ID | Item | Source | Status |
| --- | --- | --- | --- |
| SCOPE006 | Web Form for Dev Daily Reports | Client Pivot | Confirmed |
| SCOPE007 | AI extraction of Blockers from text | Client Pivot | Confirmed |
| SCOPE008 | PM Dashboard to view Blockers | Client Pivot | Confirmed |

### Out Of Scope

| ID | Item | Reason |
| --- | --- | --- |
| SCOPE004 | Real-time live transcription | MVP focuses on daily text reports |

### Future Phase

| ID | Item | Reason |
| --- | --- | --- |
| SCOPE001 | Meeting platform integrations (Zoom/Teams) | Deferred per Client Pivot |
| SCOPE002 | AI Voice Summarization engine | Deferred per Client Pivot |
| SCOPE003 | PM Tool Push (Jira/Notion) | Deferred per Client Pivot |
| SCOPE005 | Advanced analytics on meeting trends | Post-MVP optimization |

## Assumptions

| ID | Assumption | Status | Impact If False |
| --- | --- | --- | --- |
| AS001 | PM tools have accessible APIs for pushing content | Deferred | N/A for MVP |
| AS002 | Meeting platforms provide recording/transcript access | Deferred | N/A for MVP |
| AS003 | Devs will reliably fill out the Daily Report web form | Active | No blockers to aggregate |

## Risks

| ID | Risk | Severity | Mitigation |
| --- | --- | --- | --- |
| RSK001 | AI summary inaccuracy | Medium | Human-in-the-loop review option |
| RSK003 | Low adoption by dev team for filling forms | High | Keep form extremely short (3 fields max) |

## Decisions

| ID | Decision | Source | Date | Impact |
| --- | --- | --- | --- | --- |
| DEC001 | Use direct platform integration (Zoom/Teams) | Q001 | 2026-05-16 | Deferred |
| DEC002 | Deliver summaries to PM tools (Jira/Notion) | Q002 | 2026-05-16 | Deferred |
| DEC003 | Success metric is "Time Saved" | Q003 | 2026-05-16 | Medium: design focus |
| DEC004 | Pivot MVP to Daily Report Blockers only | Client | 2026-05-17 | High: complete re-scope |

## Open Questions

| ID | Question | Owner | Impact |
| --- | --- | --- | --- |
| Q004 | Target timeline for MVP | Client | Timeline planning |
