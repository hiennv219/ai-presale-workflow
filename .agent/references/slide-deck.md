---
marp: true
theme: default
paginate: true
header: "Proposal: {{project_name}}"
footer: "© {{year}} Antigravity AI — Confidential"
style: |
  section {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }
  h1, h2, h3 {
    color: #001f3f;
  }
  h1 { font-size: 2.5em; border-bottom: 4px solid #0074D9; padding-bottom: 0.2em; margin-bottom: 1em; }
  h2 { font-size: 2em; border-left: 5px solid #0074D9; padding-left: 0.4em; }
  blockquote {
    border-left: 4px solid #0074D9;
    padding-left: 1rem;
    color: #555;
    background: #f4f6f8;
    border-radius: 4px;
    font-style: italic;
  }
  .columns {
    display: flex;
    gap: 2rem;
  }
  .column {
    flex: 1;
  }
  .card {
    background: #f4f6f8;
    padding: 1.5rem;
    border-radius: 8px;
    margin-bottom: 1rem;
    border-left: 4px solid #0074D9;
  }
  .highlight { color: #0074D9; font-weight: 700; }
  table { width: 100%; border-collapse: collapse; }
  th { background-color: #001f3f; color: white; }
  td, th { padding: 12px; border-bottom: 1px solid #ddd; }
---

<!-- _class: lead -->
# {{project_name}}
## Executive Proposal & Strategy

**Presented for**: {{client_name}}
**Date**: {{date}}
**Author**: {{author}}

---

## Agenda

1. **Context & Problem** — Understanding current pain points
2. **Proposed Solution** — How we solve the problem
3. **Project Scope** — What is included (and excluded)
4. **Architecture & Tech** — The technical foundation
5. **Timeline & Milestones** — Our delivery roadmap
6. **Commercials & Budget** — Resource investment and costs

---

## 1. Context & The Problem

<div class="columns">
<div class="column">

### Current State
{{current_state_narrative}}

### Core Pain Points
- 🔴 **{{pain_point_1}}** — {{impact_1}}
- 🔴 **{{pain_point_2}}** — {{impact_2}}

</div>
<div class="column">

<div class="card">
<h3>Business Impact</h3>
<p><b>{{core_goal}}</b></p>
<ul>
  <li>✅ {{benefit_1}}</li>
  <li>✅ {{benefit_2}}</li>
</ul>
</div>

</div>
</div>

---

## 2. Proposed Solution

### {{solution_overview_title}}
> {{solution_overview}}

### Key Features (Business Value)
<div class="columns">
<div class="column">

**{{feature_group_1}}**
- 🔹 **{{feature_1}}**: {{feature_1_val}}
- 🔹 **{{feature_2}}**: {{feature_2_val}}

</div>
<div class="column">

**{{feature_group_2}}**
- 🔹 **{{feature_3}}**: {{feature_3_val}}
- 🔹 **{{feature_4}}**: {{feature_4_val}}

</div>
</div>

---

## 3. How It Works (User Flow)

```mermaid
{{user_flow_diagram}}
```

<!-- Speaker notes: Walk through the core flow clearly, explaining the user journey without deep tech terms -->

---

## 4. Project Scope (MVP Focus)

<div class="columns">
<div class="column">

### ✅ In-Scope (Must Have)
- {{in_scope_item_1}}
- {{in_scope_item_2}}
- {{in_scope_item_3}}

</div>
<div class="column">

### ❌ Out-of-Scope (Future Phases)
- {{out_scope_item_1}}
- {{out_scope_item_2}}

### ⚠️ Key Assumptions
- {{assumption_1}}
- {{assumption_2}}

</div>
</div>

---

## 5. Technical Architecture

<div class="columns">
<div class="column">

### Target Architecture
```text
{{architecture_ascii}}
```

</div>
<div class="column">

### Tech Stack
- **Frontend**: <span class="highlight">{{frontend_tech}}</span>
- **Backend**: <span class="highlight">{{backend_tech}}</span>
- **Database**: <span class="highlight">{{database_tech}}</span>
- **Infra**: <span class="highlight">{{infra_tech}}</span>

</div>
</div>

---

## 6. Implementation Roadmap

### Total Duration: <span class="highlight">{{total_duration}}</span>

| Phase | Milestone | Goal / Deliverable | Target Date |
|:---:|---|---|---|
| **1** | **{{milestone_1}}** | {{goal_1}} | {{date_1}} |
| **2** | **{{milestone_2}}** | {{goal_2}} | {{date_2}} |
| **3** | **{{milestone_3}}** | {{goal_3}} | {{date_3}} |
| **4** | **{{milestone_4}}** | {{goal_4}} | {{date_4}} |

---

## 7. Budget & Investment

<div class="columns">
<div class="column">

### Development Cost
- **Total Effort**: {{total_hours}} hours
- **Resource Plan**: {{resource_summary}}
- **Delivery Model**: {{model}}

<div class="card">
<h3>Total Dev Cost: <span class="highlight">{{total_cost}}</span></h3>
</div>

</div>
<div class="column">

### Operational / Monthly Costs
- **Cloud Infra**: ~{{infra_cost}}/mo
- **3rd-Party APIs**: {{api_cost_note}}

### Payment Terms
- {{payment_term_1}}
- {{payment_term_2}}

</div>
</div>

---

<!-- _class: lead -->
## Next Steps

1. **Review & Sign-off** on Proposal
2. **Project Kick-off**: {{proposed_date}}
3. **Environment Setup & Start Phase 1**

### Q&A
**{{contact_email}}** | **{{contact_phone}}**
