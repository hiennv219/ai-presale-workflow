# Technical Decisions: DailyTools

## System Architecture

```text
┌─ CLIENT (Next.js / React) ───────────────┐
│  ┌──────────────┐  ┌──────────────────┐  │
│  │ Dev Report   │  │ PM Dashboard     │  │
│  │ Form         │  │ (Blockers View)  │  │
│  └──────────────┘  └──────────────────┘  │
└──────────────────────────────────────────┘
              │
              ▼
┌─ API (Next.js API Routes) ───────────────┐
│  [Auth]  [Submit Report]  [Get Blockers] │
└──────────────────────────────────────────┘
              │
              ▼
┌─ SERVICE ────────────────────────────────┐
│  ┌─────────────────────────────────────┐ │
│  │ AI Blocker Extraction (GPT-4o)     │ │
│  │ • Scan text for hidden blockers    │ │
│  │ • Classify severity                │ │
│  └─────────────────────────────────────┘ │
└──────────────────────────────────────────┘
              │
              ▼
┌─ DATA (PostgreSQL / Supabase) ───────────┐
│  • reports    • blockers    • users      │
└──────────────────────────────────────────┘
```

## Component Communication

**Communication between core components (MVP Vision):**
- **Phase 1 (MVP):** 
  - The Dev logs in and submits a text-based daily report via the Web Form.
  - The Next.js API receives the form data and stores it in the Relational DB.
  - The API triggers the AI Blocker Service which sends the text to an LLM (OpenAI GPT-4o).
  - The LLM returns extracted blockers (if any), which are saved to the DB.
  - The PM views the Dashboard, which queries the DB for today's aggregated blockers.

## Tech Stack

| Layer | Technology | Reason |
| --- | --- | --- |
| Frontend | Next.js, TailwindCSS | Fast development, unified full-stack framework |
| Backend | Next.js API Routes | Sufficient for handling form submissions and AI calls |
| Database | PostgreSQL (Supabase/Vercel Postgres) | Relational data integrity for users and reports |

## 3rd-Party Vendor & Ecosystem

| Service | Vendor | Ownership | Pass-through Cost Model |
| --- | --- | --- | --- |
| Cloud Infrastructure | Vercel | Client | Billed directly to Client's credit card |
| AI / LLM API | OpenAI (GPT-4o) | Client | Billed by usage (Pay-as-you-go) |

## Key Technical Decisions

| ID | Decision | Rationale | Status |
| --- | --- | --- | --- |
| TECH001 | Use OpenAI GPT-4o for processing | High accuracy for extracting actionable blockers from unstructured text. | Proposed |
| TECH003 | Monolithic Next.js Architecture | Simplest and fastest time-to-market for a form-based MVP. | Proposed |

## Technical Risks

| ID | Risk | Mitigation |
| --- | --- | --- |
| TR001 | OpenAI API rate limits | Negligible for text-only MVP, but will implement basic retry logic. |

## Technical Assumptions

| ID | Assumption |
| --- | --- |
| TA002 | Devs will provide enough context in text for AI to detect blockers. |
