## 4. Risks, Assumptions & Acceptance Criteria

### 4.1 Strategic Assumptions
| # | Category | Assumption | Note |
|:--|:---------|:-----------|:-----|
| A1 | Adoption | Developers will consistently use the web form instead of chat channels | Form must be ultra-fast (<30s to fill) |
| A2 | AI Accuracy | GPT-4o will accurately differentiate between standard updates and critical blockers | Prompt tuning required during Phase 2 |
| A3 | Scale | Initial team size ~50 developers | Affects infra sizing decisions |

### 4.2 Risk & Mitigation
| # | Risk | Severity | Impact | Mitigation |
|:--|:-----|:--------:|:-------|:-----------|
| R1 | Low adoption by devs | High | No data to extract blockers from | Make the form ultra-fast (3 fields) and mobile-friendly. |
| R2 | AI missing hidden blockers | Medium | False sense of security for PMs | Allow devs to explicitly tag blockers, plus prompt-tuning. |

### 4.3 Acceptance Criteria
| # | Item | Measurement Criteria | Phase |
|:--|:-----|:---------------------|:------|
| AC1 | Form Submission | Devs can submit form and data saves to DB correctly. | Phase 1 |
| AC2 | Blocker Extraction | AI correctly flags blockers in 90% of test inputs. | Phase 2 |
| AC3 | Dashboard Visibility | PM dashboard renders active blockers clearly above normal logs. | Phase 3 |
