# Internal Checklist

> This file is for internal validation only. It is NOT exported to the client.

## Overview

| # | Check | Status | Action if Failed |
| --- | --- | --- | --- |
| 1 | Scope Coverage | — | Add missing WBS tasks for orphan scope items |
| 2 | Role Registry | — | Align Proposal 7.1 with WBS roles |
| 3 | Milestone-WBS Mapping | — | Assign orphan tasks to milestones |
| 4 | Proposal ↔ WBS Scope | — | Sync scope between both artifacts |
| 5 | Risk Consistency | — | Unify risks across all artifacts |

**Legend**: Pass / Fail / N/A

---

## 1. Scope Coverage Check

Verify every `S-{n}` from the approved In-Scope register has at least 1 WBS task referencing it.

| Scope ID | Scope Item | WBS Coverage | Status |
| --- | --- | --- | --- |
| S-1 | {{item}} | {{WBS IDs}} | Covered / Gap |

**Orphan scope items** (in-scope but no WBS task):
- (none)

## 2. Role Registry

Unique roles extracted from WBS. This list MUST match Proposal Section 7.1 (Resource Allocation table).

| Role | WBS Tasks | In Proposal 7.1? |
| --- | --- | --- |
| {{role}} | {{WBS IDs}} | Yes / No |

## 3. Milestone-WBS Mapping

Each milestone must reference specific WBS IDs. No orphan tasks allowed.

| Milestone | WBS IDs | Unassigned Tasks |
| --- | --- | --- |
| M1 | {{IDs}} | (none) |

## 4. Cross-Artifact Consistency

| Check | Status | Notes |
| --- | --- | --- |
| Proposal scope = WBS scope | — | |
| WBS roles = Proposal 7.1 roles | — | |
| Milestones cover all WBS tasks | — | |
| Risks consistent across artifacts | — | |
