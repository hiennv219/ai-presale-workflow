# Proposal: {{project_name}}
**Author**: {{author}}
**Date**: {{date}}
**Version**: {{version}}

---

## 1. Project Overview
### 1.1 Context & Problem Statement
- **Current State**: {{current_state}}
- **Root Cause Analysis**:

| # | Pain Point | Root Cause | Severity |
|:--|:-----------|:----------------|:------:|
| P1 | {{pain_point_1}} | {{root_cause_1}} | {{severity_1}} |

### 1.2 Goals & Business Impact
- **Goal**: {{core_goal}}
- **Type**: {{project_type}}
- **Business Benefits**:
    - [x] {{benefit_1}}
    - [x] {{benefit_2}}
    - [x] {{benefit_3}}

### 1.3 Proposed Solution Overview
{{solution_overview}}

## 2. Project Scope
### 2.1 In-Scope
{{in_scope_phases}}

### 2.2 Out-of-Scope
{{out_of_scope}}

### 2.3 Strategic Assumptions
{{assumptions}}

## 3. Solution Approach
### 3.1 Risk & Mitigation
| # | Risk | Severity | Impact | Mitigation |
|:--|:-----|:--------:|:-------|:-----------|
| R1 | {{risk_1}} | {{level}} | {{impact}} | {{mitigation}} |

### 3.2 Acceptance Criteria
| # | Item | Measurement Criteria | Phase |
|:--|:-----|:---------------------|:------|
| AC1 | {{item_1}} | {{criteria_1}} | {{phase}} |

## 4. Technical Requirement Analysis
### 4.1 Design Principles
{{design_philosophy}}

| Principle | Explanation | Accepted Trade-off |
|:----------|:------------|:-------------------|
| {{principle_1}} | {{explanation}} | {{tradeoff}} |

### 4.2 Capacity Planning
#### Traffic Estimation
| Metric | Value | Calculation |
|:-------|:------|:------------|
| {{metric}} | {{value}} | {{formula}} |

#### Infrastructure Sizing
{{infra_sizing}}

#### Scaling Strategy
| Phase | Target Load | Action | Est. Infra Cost/month |
|:------|:-----------|:-------|:----------------------|
| {{phase}} | {{load}} | {{action}} | {{cost}} |

## 5. Technical Solutions Propose

<!-- Brownfield: include 5.1 AS-IS, 5.2 TO-BE, 5.3 Migration, 5.4 Tech Stack, 5.5 UI/UX -->
<!-- Greenfield: skip AS-IS and Migration, start with Target Architecture. Renumber accordingly. -->

### 5.1 AS-IS Architecture (brownfield only)
```text
{{as_is_diagram}}
```
**Core Issue**: {{core_architecture_problem}}

### 5.2 Target Architecture
```text
{{to_be_diagram}}
```
**Component Communication:**
{{component_communication}}

### 5.3 Migration Strategy (brownfield only)
- **Method**: {{migration_method}}
- **Steps**:
{{migration_steps}}

### 5.4 Tech Stack
| Layer | Technology | Role |
|:------|:-----------|:-----|
| {{layer}} | {{tech}} | {{role}} |

### 5.5 UI/UX Concept
{{ui_ux_concept}}

## 6. Product Roadmap

| Phase | Feature | Duration | Timeline | {{month_headers}} |
|-------|---------|----------|----------|{{month_separators}}|
{{roadmap_rows}}

**Legend:** `███` = Active development period

**Key Highlights:**
{{roadmap_highlights}}

### 6.1 Delivery Plan
{{delivery_plan}}

## 7. Master Schedule
### 7.1 Master Schedule Overview
- **Total Duration**: {{duration}}
- **Methodology**: {{methodology}}

### 7.2 Project Milestone Breakdown
| # | Milestone | Target Date | Key Modules | DoD | Verification Tool |
|---|-----------|-------------|-------------|-----|-------------------|
| M1 | {{milestone_1}} | {{date}} | {{modules}} | {{dod}} | {{tool}} |

## 8. WBS & Quotations
### 8.1 Work Breakdown Structure (WBS)
{{wbs_detail}}

### 8.2 Resource Plan
| Role | FTE | Responsibility |
|:-----|:---:|:---------------|
| {{role}} | {{count}} | {{responsibility}} |

### 8.3 Resource Estimation
| Phase | Dev/Ops (h) | QA (h) | Total | Target | Quick summary |
|:------|:-----------:|:------:|:-----:|:-------|:--------------|
| {{phase}} | {{dev_h}} | {{qa_h}} | {{total_h}} | {{deadline}} | {{summary}} |

### 8.4 Budget
- **Total Effort**: {{total_hours}} working hours.
- **Development Cost**: {{dev_cost_note}}
- **Operational Cost (Infrastructure Estimation)**:

| Phase | Capacity | Infra Cost/month | Main Components |
|:------|:---------|:-----------------|:----------------|
| {{phase}} | {{capacity}} | {{infra_cost}} | {{components}} |

- **Note**: {{budget_notes}}