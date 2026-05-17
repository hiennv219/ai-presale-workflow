## 8. WBS & Quotations

### 8.1 Work Breakdown Structure (WBS)
Refer to the detailed [WBS Document](../wbs.md) for task-level estimates and dependencies.

### 8.2 Resource Plan
| Role | FTE | Responsibility |
|:-----|:---:|:---------------|
| Solutions Architect | 0.2 | System design and API strategy |
| Backend Developer | 1.0 | API integrations and core processing |
| AI Engineer | 0.5 | Prompt engineering and transcription tuning |
| Frontend Developer | 0.5 | PM Dashboard UI/UX |
| QA Engineer | 0.3 | End-to-end testing and validation |

### 8.3 Resource Estimation
| Phase | Dev/Ops (h) | QA (h) | Total | Target | Quick summary |
|:------|:-----------:|:------:|:-----:|:-------|:--------------|
| P1: Foundation | 80 | 16 | 96 | Month 1 | Setup and platform integrations |
| P2: AI Core | 60 | 12 | 72 | Month 2 | Summarization engine logic |
| P3: Delivery | 50 | 10 | 60 | Month 3 | Jira/Notion sync modules |
| P4: Launch | 20 | 10 | 30 | Month 3 | Final testing and UAT |

### 8.4 Budget
- **Total Effort**: 258 working hours.
- **Development Cost**: Based on a blended rate (TBD by final resource allocation).
- **Operational Cost (Infrastructure Estimation)**:

| Phase | Capacity | Infra Cost/month | Main Components |
|:------|:---------|:-----------------|:----------------|
| Pilot | 20 PMs | $200 | AWS Lambda, Whisper API, S3 |
| MVP | 100 PMs | $650 | Dedicated RDS, High-tier LLM API |

### 8.5 3rd-Party Vendor & Pass-Through Costs
| Service | Vendor | Ownership | Pass-through Cost Model |
|:--------|:-------|:----------|:------------------------|
| Cloud Infrastructure | AWS / Vercel | Client | Billed directly to Client's credit card |
| AI / LLM API | OpenAI (Whisper/GPT-4o) | Client | Pay-as-you-go based on volume |
| Integrations | Zoom, Teams, Jira, Notion | Client | Uses Client's existing enterprise licenses |
