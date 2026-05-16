# Deal Context: DailyTools

## Metadata

- Customer: DailyTools
- Context Version: 1.0
- Current Stage: Stage 2: Context
- Last Updated: 2026-05-16

## Rolling Summary

DailyTools is an AI-powered management tool for Project Managers. The MVP focuses on reducing PM manual effort by automatically summarizing meeting content. The solution will integrate directly with meeting platforms (Zoom, Teams) and push summaries into existing project management tools (Jira, Notion). Success is measured by time saved per PM.

## Confirmed Requirements

| ID | Requirement | Source | Priority |
| --- | --- | --- | --- |
| REQ001 | Capture meeting content from platforms (Zoom, Teams) | Client Answer (Q001) | High |
| REQ002 | Generate summaries of meeting content | Client Input | High |
| REQ003 | Push summaries to PM tools (Jira, Notion) | Client Answer (Q002) | High |
| REQ004 | Focus on effort optimization for PMs | Client Input | High |

## Unconfirmed Requirements

| ID | Requirement | Why It Matters |
| --- | --- | --- |
| REQ005 | Support for manual file uploads | Backup if integration fails |
| REQ006 | Notification system (Slack/Email) | Alternative delivery method |

## Scope Register

### In Scope

| ID | Item | Source | Status |
| --- | --- | --- | --- |
| SCOPE001 | Meeting platform integrations (Zoom/Teams) | Q001 | Confirmed |
| SCOPE002 | AI Summarization engine | Client Input | Confirmed |
| SCOPE003 | PM Tool Push (Jira/Notion) | Q002 | Confirmed |

### Out Of Scope

| ID | Item | Reason |
| --- | --- | --- |
| SCOPE004 | Real-time live transcription | MVP focuses on summary, not live text |

### Future Phase

| ID | Item | Reason |
| --- | --- | --- |
| SCOPE005 | Advanced analytics on meeting trends | Post-MVP optimization |

## Assumptions

| ID | Assumption | Status | Impact If False |
| --- | --- | --- | --- |
| AS001 | PM tools have accessible APIs for pushing content | Active | Requires manual copy/paste |
| AS002 | Meeting platforms provide recording/transcript access | Active | Requires manual upload |

## Risks

| ID | Risk | Severity | Mitigation |
| --- | --- | --- | --- |
| RSK001 | AI summary inaccuracy | Medium | Human-in-the-loop review option |
| RSK002 | API breaking changes from Zoom/Teams | Low | Modular integration design |

## Decisions

| ID | Decision | Source | Date | Impact |
| --- | --- | --- | --- | --- |
| DEC001 | Use direct platform integration (Zoom/Teams) | Q001 | 2026-05-16 | High: automation level |
| DEC002 | Deliver summaries to PM tools (Jira/Notion) | Q002 | 2026-05-16 | High: workflow integration |
| DEC003 | Success metric is "Time Saved" | Q003 | 2026-05-16 | Medium: design focus |

## Open Questions

| ID | Question | Owner | Impact |
| --- | --- | --- | --- |
| Q004 | Target timeline for MVP | Client | Timeline planning |
