# Proposal: DailyTools MVP
**Author**: Antigravity AI
**Date**: 2026-05-18
**Version**: Final (8-Section Standardized)

---

## 1. Project Overview & Business Value

### 1.1 Context & Problem Statement
Project Managers (PMs) currently lack immediate visibility into critical blockers. Daily updates from the development team are often unstructured, too long, or buried in chat channels. This leads to PMs missing critical issues and wasting time manually parsing text.

**Core Pain Points:**
- **Lack of visibility into dev blockers** — Daily reports are too long or unstructured. High risk of delays.
- **Manual parsing of updates** — Devs write unstructured text in chat, forcing PMs to manually extract status.

> 💡 **CRITICAL FOCUS**: To solve this, we must absolutely **optimize effort for PMs** by fully automating the extraction of blockers from raw text.

### 1.2 Goals & Business Impact
- **Goal**: Provide a lightweight, automated way to collect dev updates and instantly extract blockers using AI.
- **Type**: Greenfield MVP Development (Simple Trial)

**Business Benefits**:
- **Effort Optimization (Priority)** — Drastically reduce PM effort in parsing daily reports by automatically summarizing and highlighting issues.
- **Risk Mitigation** — Catch and highlight blockers immediately before they cause timeline delays.
- **Developer Experience** — A frictionless, 3-field form that takes 30 seconds to fill out, ensuring high adoption.

## 2. Proposed Solution & UX

### 2.1 Solution Overview
DailyTools is a centralized daily reporting hub that automatically surfaces development bottlenecks. By parsing unstructured developer updates, it immediately alerts PMs to potential risks without requiring developers to log into complex project management tools.

### 2.2 Key Features
*(The following features are designed to directly address the highest priority requirements from the Deal Context).*

**Developer Workspace**
- **Frictionless Web Form (Critical)**: A fast, mobile-friendly interface for developers to quickly note down what they did, their plans, and any challenges, without disrupting their workflow.
- **Zero-Login Submission**: Magic links or simple authentication to ensure developers actually use the tool.

**AI Engine**
- **Smart Blocker Extraction (Critical)**: Automatically reads through daily logs and identifies hidden risks or issues, even if the developer doesn't explicitly label them as problems.

**Project Management Console**
- **Alert Dashboard**: A prioritized view that automatically pushes all detected roadblocks to the top, ensuring critical issues are addressed first.

### 2.3 User Flow
Developers submit daily reports through a simple web form. The AI engine scans each submission for blockers. If a blocker is detected, it is highlighted on the PM Dashboard for immediate action. Otherwise, the report is logged as a normal status update.

```mermaid
graph TD
    A([Dev opens DailyTools]) --> B[Fills out Daily Report Form]
    B --> C[Submit]
    C --> D[AI Scans Text for Blockers]
    D --> E{Blocker Found?}
    E -- Yes --> F[Highlight on PM Dashboard]
    E -- No --> G[Log as normal status]
    F --> H([PM Reviews Blockers])
```

### 2.4 High-Level Wireframe

**Dev Form**
```text
┌─────────────────────────────────────┐
│  📋 Daily Standup                   │
├─────────────────────────────────────┤
│                                     │
│  What I did yesterday:              │
│  ┌─────────────────────────────┐    │
│  │                             │    │
│  └─────────────────────────────┘    │
│                                     │
│  What I will do today:              │
│  ┌─────────────────────────────┐    │
│  │                             │    │
│  └─────────────────────────────┘    │
│                                     │
│  Blockers (optional):               │
│  ┌─────────────────────────────┐    │
│  │                             │    │
│  └─────────────────────────────┘    │
│                                     │
│           [ Submit ]                │
└─────────────────────────────────────┘
```

**PM Dashboard**
```text
┌─────────────────────────────────────┐
│  📊 PM Dashboard                    │
├─────────────────────────────────────┤
│                                     │
│  ⚠️  Active Blockers (2)            │
│  ┌─────────────────────────────┐    │
│  │ • John: API timeout issue   │    │
│  │ • Mai: Waiting for design   │    │
│  └─────────────────────────────┘    │
│                                     │
│  ─────────────────────────────────  │
│                                     │
│  📅 Today's Updates                 │
│  ┌─────────────────────────────┐    │
│  │ John - 10:02 AM             │    │
│  │ Did: Fixed auth module      │    │
│  │ Will: Start API integration │    │
│  │ ⚠️ Blocker: API timeout     │    │
│  ├─────────────────────────────┤    │
│  │ Mai - 09:45 AM              │    │
│  │ Did: Completed wireframes   │    │
│  │ Will: Build prototype       │    │
│  │ ⚠️ Blocker: Waiting design  │    │
│  └─────────────────────────────┘    │
│                                     │
└─────────────────────────────────────┘
```

## 3. Project Scope

### 3.1 In-Scope
- **Web Form for Dev Daily Reports**: Responsive, mobile-friendly. 3 text fields + submit. Platform: iOS Safari, Android Chrome, Desktop. Deliverable: deployed page + API endpoint.
- **AI extraction of Blockers from text**: GPT-4o integration with custom prompt. Confidence scoring (0–1). Deliverable: extraction service + prompt documentation.
- **PM Dashboard to view Blockers**: Active blockers view (sorted by severity) + historical daily logs (filterable by date/person). Deliverable: deployed dashboard + role-based access.

### 3.2 Out-of-Scope & Future Phases
- **Real-time live transcription**: MVP focuses on daily text reports only.
- **Meeting platform integrations (Zoom/Teams)**: Deferred to Phase 2.
- **AI Voice Summarization engine**: Deferred to Phase 2.
- **PM Tool Push (Jira/Notion)**: Deferred to Phase 2.

## 4. Risks & Strategic Assumptions

### 4.1 Strategic Assumptions
This proposal is built upon the following assumptions:
- **PM tools APIs** — PM tools have accessible APIs for pushing content (N/A for MVP, assumed for Phase 2).
- **Adoption** — Devs will reliably fill out the Daily Report web form. If this fails, there will be no blockers to aggregate.

### 4.2 Risk & Mitigation
- 🔴 **R1: Low adoption by dev team (High)**
  Developers might resist using a new tool if it takes too much time.
  → *Mitigation*: Keep the form extremely short (3 fields max) and fast (<30s to submit). Make it mobile-friendly so they can do it on the go.
- 🟡 **R2: AI summary inaccuracy (Medium)**
  GPT-4o might miss subtle blockers or flag false positives.
  → *Mitigation*: Implement a Human-in-the-loop review option, allowing PMs to manually adjust or tune the prompt if needed.

## 5. Technical Architecture

> 💡 DailyTools uses a modern, serverless Next.js monolithic architecture for rapid MVP delivery, ensuring low cost and high scalability.

### 5.1 Target Architecture
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

### 5.2 Tech Stack
- **Frontend & Backend**: **Next.js / TypeScript** — Single codebase for both UI and API routes. Rapid MVP delivery, SSR for fast load times.
- **AI Engine**: **OpenAI GPT-4o** — Best-in-class understanding for text analysis and blocker extraction with low integration effort.
- **Database & Auth**: **PostgreSQL (Supabase)** — Managed service, built-in auth (JWT), real-time subscriptions, free tier is fully sufficient for MVP.
- **Infrastructure**: **Vercel** — Zero-config deployment, native Next.js support, serverless auto-scaling.

### 5.3 Data Flow
```mermaid
sequenceDiagram
    participant Dev
    participant Form as Web Form
    participant API as API Route
    participant AI as GPT-4o
    participant DB as PostgreSQL
    participant PM as PM Dashboard

    Dev->>Form: Fill daily report
    Form->>API: POST /api/reports
    API->>AI: Extract blockers from text
    AI-->>API: {blockers: [...], severity}
    API->>DB: Save report + blockers
    API-->>Form: Success

    PM->>API: GET /api/blockers
    API->>DB: Query active blockers
    DB-->>API: Results
    API-->>PM: Render blockers list
```

### 5.4 Capacity & Sizing
- **Target Users**: ~50 Developers.
- **Concurrent Connections**: Low. ~50 reports/day, each report <5KB. Total storage <1MB/day.
- **Storage Strategy**: Relational storage in Supabase PostgreSQL is more than enough. The entire system will run comfortably on free/hobby tiers until scaling past 200+ users.

### 5.5 Security & Privacy
- **Transport**: TLS 1.3 (Vercel default).
- **Storage**: AES-256 encryption (Supabase default).
- **Auth**: Supabase Auth (JWT) with RBAC (Dev = submit only, PM = read dashboard).
- **LLM Privacy**: Zero-retention API — OpenAI does not store or train on input data. Report text will be anonymized before sending to GPT-4o.

## 6. Execution & Delivery Plan

### 6.1 Product Roadmap
The MVP is designed for a rapid 4-week delivery, divided into logical phases to validate core assumptions early. We deploy the Form first to test adoption, followed by AI integration, and finally the PM dashboard.

| Phase | Feature | Duration | Timeline | W1 | W2 | W3 | W4 |
|-------|---------|----------|----------|:--:|:--:|:--:|:--:|
| P1 | Form & Database | 1 week | Week 1 | ███ |    |    |    |
| P2 | AI Blocker Engine | 1 week | Week 2 |     | ███ |    |    |
| P3 | PM Dashboard View | 1 week | Week 3 |     |     | ███ |    |
| P4 | UAT & Launch | 1 week | Week 4 |     |     |     | ███ |

### 6.2 Milestones & Acceptance Criteria
The project is accepted by Milestones. Below is the Definition of Done (DoD) and corresponding acceptance criteria for each phase.

| # | Milestone | Target Date | Key Deliverables | Acceptance Criteria |
|---|-----------|-------------|------------------|---------------------|
| M1 | Form Ready | End of W1 | Web Form & DB | Devs can submit form and data saves correctly |
| M2 | AI Ready | End of W2 | AI Extraction | AI correctly flags blockers in 90% of test inputs |
| M3 | Dashboard | End of W3 | PM UI | Dashboard renders active blockers clearly above normal logs |
| M4 | Launch | End of W4 | Live Deploy | Signed off UAT on production environment |


## 7. Budget & Commercials

### 7.1 Resource Allocation
We allocate a cross-functional team on a Fixed-Price model to deliver the MVP within 4 weeks.

| Position | Seniority | Unit Price | P1 | P2 | P3 | P4 | Total Effort |
|:---------|:----------|:-----------|:--:|:--:|:--:|:--:|:------------:|
| Solutions Arch | Senior | $60/hr | 4h | 2h | 2h | 0h | 8h |
| Fullstack Dev | Mid | $40/hr | 20h| 18h| 20h| 8h | 66h|
| AI Engineer | Senior | $60/hr | 0h | 12h| 0h | 2h | 14h|
| QA Engineer | Mid | $30/hr | 4h | 4h | 6h | 10h| 24h|
| **Total**| | | **28h** | **36h**| **28h**| **20h**| **112h**|

### 7.2 Operational Cost (Infra)
By utilizing a Serverless architecture, we keep MVP running costs near zero, only scaling costs when adoption grows significantly.

| Phase | Users | Infra Cost/month | Main Components |
|:----------|:------|:-----------------|:----------------|
| MVP | 50 Devs | ~$0 | Vercel (Hobby), Supabase (Free Tier) |
| Phase 2 | 200+ | ~$50–100 | Vercel Pro, Supabase Pro |

### 7.3 3rd-Party Vendor Costs
- **OpenAI (GPT-4o)**: ~$5–15/month — Estimated at 50 reports/day × ~$0.01/call.

## 8. Development Cost & Payment Schedule
Summary of the total contract value for the development and handover of the DailyTools MVP.

- **Total Development Cost**: **$4,680**
*(Note: This is the total fixed price payable to the development team. It excludes operational infrastructure and 3rd-party vendor costs which are paid directly to those providers).*

**Payment Schedule**:
- **Advance Payment**: 30% upon contract signing (kick-off).
- **Milestone P2**: 30% upon delivery of the AI engine (End of W2).
- **Milestone P4**: 40% upon UAT sign-off and launch (End of W4).

---
*Company Showcase and relevant Case Studies are attached in the appendix PDF if requested.*
