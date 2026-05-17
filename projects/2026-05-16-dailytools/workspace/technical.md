# Technical Decisions: DailyTools

## System Architecture

```
CLIENT LAYER        → Web Dashboard (React/Next.js)
                      │
API GATEWAY         → API Gateway / Auth (NextAuth/Cognito)
                      │
SERVICE LAYER       → ┌─────────────────────┐   ┌─────────────────────┐
                      │ Integration Service │   │ AI Summary Service  │
                      │ - Syncs Zoom/Teams  │   │ - Transcribes Audio │
                      │ - Pushes to Jira    │   │ - Generates Summary │
                      └─────────┬───────────┘   └─────────┬───────────┘
                                │                         │
DATA LAYER          → ┌─────────▼───────────┐   ┌─────────▼───────────┐
                      │ Relational DB       │   │ Object Storage      │
                      │ - Users & Configs   │   │ - Temp Audio Files  │
                      └─────────────────────┘   └─────────────────────┘
```

## Component Communication

**Communication between core components (MVP Vision):**
- **Phase 1 (MVP):** 
  - The Web Dashboard talks to the API Gateway to configure integration tokens.
  - The Integration Service receives webhooks from Zoom/Teams when a meeting ends, downloads the recording to Object Storage.
  - An event triggers the AI Summary Service which calls the transcription and summarization APIs (OpenAI).
  - The result is stored in the DB and pushed back via the Integration Service to Jira/Notion.

## Tech Stack

| Layer | Technology | Reason |
| --- | --- | --- |
| Frontend | Next.js, TailwindCSS | Fast development, SEO-friendly, easy admin panel |
| Backend | Node.js (NestJS) or Next.js API | Non-blocking I/O perfect for webhooks and API calls |
| Database | PostgreSQL (Supabase/RDS) | Relational data integrity for users and tokens |
| Storage | AWS S3 / Cloudflare R2 | Cheap storage for temporary meeting audio |

## 3rd-Party Vendor & Ecosystem

| Service | Vendor | Ownership | Pass-through Cost Model |
| --- | --- | --- | --- |
| Cloud Infrastructure | AWS or Vercel | Client | Billed directly to Client's credit card |
| AI / LLM API | OpenAI (Whisper & GPT-4o) | Client | Billed by usage (Pay-as-you-go) |
| Integrations | Zoom, Teams, Jira, Notion | Client | Uses Client's existing enterprise licenses |

## Key Technical Decisions

| ID | Decision | Rationale | Status |
| --- | --- | --- | --- |
| TECH001 | Use OpenAI APIs for processing | Highest accuracy for meeting summaries, minimal custom training needed. | Proposed |
| TECH002 | Store audio temporarily only | Privacy requirement (RSK001) - files are deleted after processing. | Proposed |

## Technical Risks

| ID | Risk | Mitigation |
| --- | --- | --- |
| TR001 | OpenAI API rate limits | Implement exponential backoff and queuing mechanism. |

## Technical Assumptions

| ID | Assumption |
| --- | --- |
| TA001 | Zoom and Teams APIs allow downloading cloud recordings via OAuth apps. |
