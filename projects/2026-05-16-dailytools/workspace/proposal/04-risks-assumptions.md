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
