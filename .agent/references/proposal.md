# Proposal: {{project_name}}
**Author**: {{author}}
**Date**: {{date}}
**Version**: {{version}}

---

## 1. Project Overview & Business Value

### 1.1 Context & Problem Statement
{{current_state_narrative — 2-3 sentences describing the current state, written in prose}}

**Core Pain Points:**
- **{{pain_point_1}}** — {{root_cause_1}}. {{impact_if_not_solved}}.
- **{{pain_point_2}}** — {{root_cause_2}}. {{impact_if_not_solved}}.

> 💡 {{key_insight — 1 sentence summarizing why this problem needs immediate resolution}}

### 1.2 Goals & Business Impact
- **Goal**: {{core_goal — 1 clear sentence}}
- **Type**: {{project_type}}

**Business Benefits**:
- **{{benefit_1_title}}** — {{benefit_1_detail}}.
- **{{benefit_2_title}}** — {{benefit_2_detail}}.

## 2. Proposed Solution & UX

### 2.1 Solution Overview
{{solution_overview — 3-5 sentences describing the overall solution, written in prose}}

### 2.2 Key Features
*(List 3-5 core features using business language. Group by module (Admin, User App, etc.) for large projects. Absolutely do not use complex technical jargon)*

**{{module_or_feature_group_1}}**
- **{{feature_1_name}}**: {{feature_1_business_value}}
- **{{feature_2_name}}**: {{feature_2_business_value}}

### 2.3 User Flow
{{user_flow_description — 2-3 sentences of prose describing the main flow}}

```mermaid
{{user_flow_diagram}}
```

### 2.4 High-Level Wireframe
{{wireframes_here}}

## 3. Project Scope

### 3.1 In-Scope
- **{{phase_or_module_1}}**: {{description}}
- **{{phase_or_module_2}}**: {{description}}

### 3.2 Out-of-Scope
- **{{item_1}}**: {{reason_for_deferral}}
- **{{item_2}}**: {{reason_for_deferral}}

## 4. Risks & Strategic Assumptions

### 4.1 Strategic Assumptions
{{intro — 1 sentence: "This proposal is built upon the following assumptions:"}}
- **{{category_1}}** — {{assumption_1}}.
- **{{category_2}}** — {{assumption_2}}.

### 4.2 Risk & Mitigation
**🔴 R1: {{risk_name}} (High)**
{{risk_description}}
→ *Mitigation*: {{specific_solution}}

## 5. Technical Architecture

> 💡 {{1 sentence summarizing the architecture philosophy}}

### 5.1 Target Architecture
```text
{{to_be_diagram_ascii_box_art}}
```

### 5.2 Tech Stack
- **Frontend**: **{{tech}}** — {{why}}.
- **Backend**: **{{tech}}** — {{why}}.
- **Database**: **{{tech}}** — {{why}}.
- **Infrastructure**: **{{tech}}** — {{why}}.

### 5.3 Data Flow
```mermaid
sequenceDiagram
    {{data_flow_sequence}}
```

### 5.4 Capacity & Sizing
- **Target Users**: {{number}}
- **Concurrent Connections**: {{number}}
- **Storage Strategy**: {{strategy}}

### 5.5 Security & Privacy
- **Transport**: {{approach}}
- **Storage**: {{approach}}
- **Auth**: {{approach}}

## 6. Execution & Delivery Plan

### 6.1 Product Roadmap
{{2-3 sentences of prose describing the overall timeline allocation strategy, why it is divided into these phases, and when the delivery point is.}}

| Phase | Feature | Duration | Timeline | {{month_headers}} |
|-------|---------|----------|----------|{{month_separators}}|
{{roadmap_rows}}

### 6.2 Milestones & Acceptance Criteria
{{2-3 sentences of prose specifying the acceptance method. E.g., "The project is accepted by Milestones. Below is the Definition of Done (DoD) and corresponding acceptance criteria for each phase."}}

| # | Milestone | Target Date | Key Deliverables | Acceptance Criteria |
|---|-----------|-------------|------------------|---------------------|
| M1 | {{milestone_1}} | {{date}} | {{modules}} | {{ac_1}} |


## 7. Budget & Commercials

### 7.1 Resource Allocation & Development Cost
{{Prose explaining the pricing model (Fixed price or T&M), total project duration, and budget commitment for the agreed Scope.}}

| Position | Seniority | Unit Price | {{Month 1}} | {{Month 2}} | {{Month 3}} | Total Effort | Total Cost |
|:---------|:----------|:-----------|:-----------:|:-----------:|:-----------:|:------------:|:-----------|
| {{Role}} | {{Level}} | {{Price}} | {{FTE}} | {{FTE}} | {{FTE}} | {{Total FTE}} | {{Cost}} |
| **Total**| | | | | | | **{{total_cost}}** |

### 7.2 Operational Cost (Infra)
{{Prose explaining the server cost optimization philosophy (E.g., "Use serverless to save 80% cost when there is no traffic").}}

| Phase | Users | Infra Cost/month | Main Components |
|:----------|:------|:-----------------|:----------------|
| {{phase}} | {{cap}} | {{cost}} | {{components}} |

### 7.3 3rd-Party Vendor Costs
- **{{Vendor 1}}**: {{cost}} — {{note}}
- **{{Vendor 2}}**: {{cost}} — {{note}}

## 8. Development Cost & Payment Schedule
{{1-2 sentences summarizing the total contract value for the development services.}}

- **Total Development Cost**: **{{total_dev_cost}}** 
*(This is the total amount payable to the development team. It excludes operational infrastructure and 3rd-party vendor costs which are paid directly to those providers).*

**Payment Schedule**:
- **Milestone 1 Payment**: {{conditions}}
- **Milestone 2 Payment**: {{conditions}}

---
*Company Showcase is attached in the appendix PDF if requested by the customer.*
