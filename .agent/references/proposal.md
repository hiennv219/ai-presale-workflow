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

### 1.4 Company Showcase (Optional)
{{showcase}}

## 2. Scope & Solution
### 2.1 In-Scope
{{in_scope_phases}}

### 2.2 Out-of-Scope
{{out_of_scope}}

## 3. User Flow & Wireframe
<!-- Chỉ vẽ cho tính năng chính (core features), không vẽ hết tất cả flows -->

### 3.1 User Flow
{{user_flow_description}}

```mermaid
{{user_flow_diagram}}
```

### 3.2 High-Level Wireframe
<!-- Use wireframe skill. Draw ASCII wireframes for each core screen. Never use text-only descriptions. -->

## 4. Risks, Assumptions & Acceptance Criteria

### 4.1 Strategic Assumptions
| # | Category | Assumption | Note |
|:--|:---------|:-----------|:-----|
| A1 | {{category_1}} | {{assumption_1}} | {{note_1}} |

### 4.2 Risk & Mitigation
| # | Risk | Severity | Impact | Mitigation |
|:--|:-----|:--------:|:-------|:-----------|
| R1 | {{risk_1}} | {{level}} | {{impact}} | {{mitigation}} |

### 4.3 Acceptance Criteria
| # | Item | Measurement Criteria | Phase |
|:--|:-----|:---------------------|:------|
| AC1 | {{item_1}} | {{criteria_1}} | {{phase}} |

## 5. Technical Architecture

<!-- Brownfield: include 5.1 AS-IS, 5.2 TO-BE, 5.3 Migration, 5.4 Tech Stack, 5.5 Data Flow, 5.6 Capacity -->
<!-- Greenfield: skip AS-IS and Migration, start with Target Architecture. Renumber accordingly. -->
<!-- Use architecture skill for all diagrams. ASCII box art for static views, Mermaid sequence for dynamic flows. -->

### 5.1 AS-IS Architecture (brownfield only)
```text
{{as_is_diagram_ascii_box_art}}
```
**Core Issue**: {{core_architecture_problem}}

### 5.2 Target Architecture
```text
{{to_be_diagram_ascii_box_art}}
```

### 5.3 Migration Strategy (brownfield only)
- **Method**: {{migration_method}}
- **Steps**:
{{migration_steps}}

### 5.4 Tech Stack
| Layer | Technology | Role | Why |
|:------|:-----------|:-----|:----|
| {{layer}} | {{tech}} | {{role}} | {{why}} |

### 5.5 Data Flow
```mermaid
sequenceDiagram
    {{data_flow_sequence}}
```

### 5.6 Capacity Planning & Infrastructure Sizing
#### Traffic Estimation
| Metric | Value | Calculation |
|:-------|:------|:------------|
| {{metric}} | {{value}} | {{formula}} |

#### Infrastructure Sizing
{{infra_sizing}}

## 6. Implementation Plan
### 6.1 Product Roadmap
| Phase | Feature | Duration | Timeline | {{month_headers}} |
|-------|---------|----------|----------|{{month_separators}}|
{{roadmap_rows}}

**Legend:** `███` = Active development period

**Key Highlights:**
{{roadmap_highlights}}

### 6.2 Project Milestone Breakdown
| # | Milestone | Target Date | Key Modules | DoD | Verification Tool |
|---|-----------|-------------|-------------|-----|-------------------|
| M1 | {{milestone_1}} | {{date}} | {{modules}} | {{dod}} | {{tool}} |

### 6.3 Delivery Plan
{{delivery_plan}}

## 7. WBS & Resources
### 7.1 WBS Details
{{wbs_detail}}

### 7.2 Resource Plan
| Role | FTE | Responsibility |
|:-----|:---:|:---------------|
| {{role}} | {{count}} | {{responsibility}} |

### 7.3 Resource Estimation
| Phase | Dev/Ops (h) | QA (h) | Total | Target | Quick summary |
|:------|:-----------:|:------:|:-----:|:-------|:--------------|
| {{phase}} | {{dev_h}} | {{qa_h}} | {{total_h}} | {{deadline}} | {{summary}} |

## 8. Budget & Commercials
### 8.1 Development Cost
- **Total Effort**: {{total_hours}} working hours.
- **Development Cost**: {{dev_cost_note}}

### 8.2 Operational Cost & Scaling Strategy
| Phase | Capacity | Infra Cost/month | Main Components |
|:------|:---------|:-----------------|:----------------|
| {{phase}} | {{capacity}} | {{infra_cost}} | {{components}} |

### 8.3 3rd-Party Vendor & Pass-Through Costs
| Service | Vendor | Ownership | Pass-through Cost Model |
|:--------|:-------|:----------|:------------------------|
| {{service}} | {{vendor}} | {{ownership}} | {{cost_model}} |
