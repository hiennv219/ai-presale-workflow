# Refactor: Mô Hình Agent cho Presale Pipeline

## Tổng Quan

Chuyển đổi hệ thống presale từ mô hình "orchestrator + flat skills" sang mô hình
"orchestrator + agents + skills" — trong đó mỗi agent là một persona chuyên gia
sở hữu một nhóm stages, có logic phân nhánh (Stop/Assume Rule), và giao tiếp
với khách hàng qua Comm Hub chuẩn hóa.

**Giữ nguyên:** Pipeline 7 stages, tất cả skill procedures, references, output format.
**Thêm mới:** Layer agents phía trên skills, Comm Hub, Assumption Ledger.

---

## Kiến Trúc Tổng Thể (ASCII)

```
                              [ USER INPUT ]
                                    |
                                    v
      +================================================================+
      |                        ORCHESTRATOR                             |
      |                                                                 |
      |  1. Đọc status.md → xác định stage hiện tại                    |
      |  2. Map stage → agent owner                                     |
      |  3. Load agents/<agent>/AGENT.md                                |
      |  4. Agent chọn skill (stage) để chạy                            |
      |  5. Nhận kết quả → handoff hoặc loop                           |
      +================================================================+
                  |                    |                    |
                  v                    v                    v
      +====================+  +====================+  +====================+
      |    SENIOR BA       |  | SOLUTION ARCHITECT |  |    SENIOR PM       |
      |    (Agent)         |  |    (Agent)         |  |    (Agent)         |
      |                    |  |                    |  |                    |
      | Owns:              |  | Owns:              |  | Owns:              |
      |  Stage 1: Discovery|  |  Stage 3: Scope    |  |  Stage 4: WBS      |
      |  Stage 2: Context  |  |  Stage 3.5: Tech   |  |  Stage 5: Proposal |
      |                    |  |                    |  |  Stage 6: Review   |
      +=========+=========++  +=========+=========++  +=========+==========+
                |          |            |          |            |          |
                v          v            v          v            v          v
      +====================================================================+
      |                         SKILLS LAYER                                |
      |                                                                     |
      |  discovery | context | scope | technical | wbs | proposal | review  |
      |  architecture | wireframe | slides | transale                       |
      +====================================================================+
                          |                          |
            +-------------+                          +-------------+
            v                                                      v
      +------------------+                              +--------------------+
      |    COMM HUB      |                              | ASSUMPTION LEDGER  |
      |  (Shared Agent)  |                              |  (Shared Skill)    |
      |                  |                              |                    |
      | - Tone Switcher  |                              | - Ghi giả định     |
      | - Batch câu hỏi  |                              | - Phân loại impact |
      | - Format chuẩn   |                              | - Track status     |
      +--------+---------+                              | - Gate cho Review  |
               |                                        +--------------------+
               v                                                   |
      +----------------+                                           |
      |  KHÁCH HÀNG    | --(trả lời)--> Orchestrator loop          |
      +----------------+                                           |
                                                                   v
      +====================================================================+
      |                    WORKSPACE (Shared State)                          |
      |                                                                     |
      |  discovery.md | deal-context.md | backlog-questions.md              |
      |  pain-scope.md | technical.md | wbs.md | proposal/                  |
      |  assumption-ledger.md | status.md | change-log.md | context.md      |
      +====================================================================+
                                       |
                                       v
      +====================================================================+
      |                    REFERENCES (Templates)                            |
      +====================================================================+
```

---

## Luồng Xử Lý Chi Tiết

```
                          [ USER INPUT ]
                                |
                                v
                       +------------------+
                       |   ORCHESTRATOR   |
                       +--------+---------+
                                |
                +---------------+---------------+
                |  Routing logic:               |
                |  1. Đọc status.md             |
                |  2. Map stage → agent         |
                |  3. Load AGENT.md             |
                +---------------+---------------+
                                |
                                v
                +===============================+
                |        ACTIVE AGENT           |
                +===============================+
                                |
                                v
                +-------------------------------+
                |   Chạy Skill (stage procedure)|
                +---------------+---------------+
                                |
                                v
                       /==================\
                      /   KIỂM TRA INFO    \
                      \   (Stop/Assume)    /
                       \==================/
                         |       |       |
             +-----------+       |       +-----------+
             |                   |                   |
       (Thiếu Cốt Lõi)    (Đủ Info)        (Thiếu Chi Tiết)
        STOP RULE                             ASSUME RULE
             |                   |                   |
             v                   |                   v
      +-------------+           |         +-------------------+
      |    HOLD     |           |         | ASSUMPTION LEDGER |
      +------+------+           |         +--------+----------+
             |                  |                  |
             v                  |                  |
      +-------------+          |                  |
      |  COMM HUB   |          |                  |
      +------+------+          |                  |
             |                  |                  |
             v                  |                  |
      [Hỏi Khách Hàng]         |                  |
             |                  |                  |
             v                  |                  |
      [Khách Trả Lời]          |                  |
             |                  |                  |
             v                  v                  v
             +------------------+------------------+
                                |
                                v
                +-------------------------------+
                |   AGENT HOÀN THÀNH STAGE      |
                |   → Ghi artifact vào workspace|
                |   → Cập nhật status.md        |
                +---------------+---------------+
                                |
                                v
                       +------------------+
                       |   ORCHESTRATOR   |
                       |   Handoff Logic  |
                       +--------+---------+
                                |
                +---------------+---------------+
                |                               |
                v                               v
      +-------------------+          +--------------------+
      | NEXT STAGE        |          | HANDOFF SANG       |
      | (cùng Agent)      |          | AGENT TIẾP THEO    |
      +-------------------+          +--------------------+
```

---

## Cấu Trúc Thư Mục

```
.agent/
├── README.md                            ← Cập nhật: mô tả mô hình mới
├── rules.md                             ← Cập nhật: thêm Stop/Assume Rule
├── improvement-backlog.md
│
├── agents/                              ← MỚI
│   ├── senior-ba/
│   │   └── AGENT.md
│   ├── solution-architect/
│   │   └── AGENT.md
│   ├── senior-pm/
│   │   └── AGENT.md
│   └── comm-hub/
│       └── AGENT.md
│
├── skills/                              ← Giữ nguyên + thêm 1
│   ├── orchestrator/SKILL.md            ← Cập nhật: routing 2 tầng
│   ├── discovery/SKILL.md
│   ├── context/SKILL.md
│   ├── scope/SKILL.md
│   ├── technical/SKILL.md
│   ├── wbs/SKILL.md
│   ├── proposal/SKILL.md
│   ├── review-finalize/SKILL.md
│   ├── assumption-ledger/SKILL.md       ← MỚI
│   ├── architecture/SKILL.md
│   ├── wireframe/SKILL.md
│   ├── transale/SKILL.md
│   └── slides/SKILL.md
│
├── workflows/                           ← Cập nhật nội dung
│   ├── presale-run.md                   ← Cập nhật: flow qua agents
│   ├── presale-update.md                ← Cập nhật nhẹ
│   ├── presale-init.md
│   ├── presale-finalize.md
│   ├── presale-preview.md
│   ├── presale-slides.md
│   └── presale-export.md
│
├── references/                          ← Giữ nguyên + thêm 1
│   ├── assumption-ledger.md             ← MỚI: template
│   ├── backlog-questions.md
│   ├── change-log.md
│   ├── checklist.md
│   ├── deal-context.md
│   ├── pain-scope.md
│   ├── proposal-index.md
│   ├── proposal-template-default.md
│   ├── status.md
│   ├── wbs.md
│   └── designs/
│       ├── documents.md
│       ├── export-template.html
│       └── slides.md
│
└── scripts/
    └── presale_cli.py
```

---

## Chi Tiết Từng Agent

### Agent: Senior BA

**File:** `agents/senior-ba/AGENT.md`

**Persona:** Business Analyst cấp cao với 10+ năm kinh nghiệm presale. Tập trung vào
việc hiểu đúng nhu cầu khách hàng trước khi bất kỳ ai bắt đầu thiết kế giải pháp.

**Stages owned:**
- Stage 1: Discovery (skill: `discovery`)
- Stage 2: Context (skill: `context`)

**Trách nhiệm:**
- Normalize raw input từ khách hàng
- Phân loại thông tin: fact / assumption / decision / open question
- Xác định thông tin còn thiếu
- Duy trì deal-context.md như single source of truth

**Stop Rule (thông tin cốt lõi — PHẢI hỏi khách):**
- Business goal / mục tiêu kinh doanh
- Target users / đối tượng sử dụng
- Budget range / ngân sách
- Timeline / deadline cứng
- Platform choice (web / mobile / both)
- Số lượng user roles chính
- Integrations bắt buộc với hệ thống bên ngoài

**Assume Rule (chi tiết phụ — tự giả định được):**
- Caching strategy (Redis vs Memcached)
- CI/CD tooling
- Library/framework choices (nếu không ảnh hưởng scope)
- Internal naming conventions
- Monitoring/logging stack
- Development methodology (Agile/Scrum — mặc định Scrum)

**Handoff sang Solution Architect khi:**
- `workspace/discovery.md` tồn tại
- `workspace/deal-context.md` tồn tại
- Không còn câu hỏi Stop Rule chưa được trả lời
- Hoặc: câu hỏi đã hỏi > 2 lần không có phản hồi → promote to assumption + ghi Ledger

---

### Agent: Solution Architect

**File:** `agents/solution-architect/AGENT.md`

**Persona:** Solution Architect với expertise về system design và technical trade-offs.
Biến business requirements thành solution scope có thể deliver được.

**Stages owned:**
- Stage 3: Scope (skill: `scope`)
- Stage 3.5: Technical (skill: `technical`)

**Sub-skills có thể gọi:**
- `architecture` — vẽ ASCII diagram
- `wireframe` — vẽ wireframe cho UI screens

**Trách nhiệm:**
- Chuyển requirements thành pain points + business impact
- Xây dựng scope register (in/out/future)
- Đề xuất technical decisions (nếu SA thật chưa cung cấp)
- Kiểm soát scope creep

**Stop Rule (thông tin cốt lõi — PHẢI hỏi khách):**
- Greenfield vs Brownfield
- Compliance/regulatory requirements (PCI, HIPAA, SOC2)
- Performance requirements (concurrent users, response time)
- Data migration requirements
- 3rd-party system constraints (API versions, rate limits)

**Assume Rule (chi tiết phụ — tự giả định được):**
- Database engine (PostgreSQL mặc định)
- Cloud provider (AWS mặc định)
- API style (REST mặc định, gRPC cho internal)
- Authentication method (JWT + OAuth2 mặc định)
- Container orchestration (Kubernetes mặc định cho enterprise)

**Handoff sang Senior PM khi:**
- `workspace/pain-scope.md` tồn tại
- Scope register có ít nhất 1 approved in-scope item
- `workspace/technical.md` tồn tại HOẶC stage 3.5 được skip (tech đã có trong context)

**Loop back sang Senior BA khi:**
- Phát hiện scope item không map được về requirement nào trong deal-context
- Khách feedback mở rộng scope → cần Context update trước

---

### Agent: Senior PM

**File:** `agents/senior-pm/AGENT.md`

**Persona:** Project Manager cấp cao chuyên về delivery planning và proposal writing.
Biến scope thành deliverables cụ thể và proposal thuyết phục.

**Stages owned:**
- Stage 4: WBS (skill: `wbs`)
- Stage 5: Proposal (skill: `proposal`)
- Stage 6: Review & Finalize (skill: `review-finalize`)

**Sub-skills có thể gọi:**
- `wireframe` — vẽ wireframe cho proposal
- `slides` — tạo slide deck

**Trách nhiệm:**
- Tạo WBS từ approved scope
- Viết proposal multi-section
- Review consistency giữa tất cả artifacts
- Gate finalization

**Stop Rule (thông tin cốt lõi — PHẢI hỏi khách):**
- Payment terms / điều kiện thanh toán
- Preferred delivery model (fixed price / T&M / hybrid)
- Team composition preferences (onshore / offshore / mixed)
- Warranty/support period requirements
- Specific milestone deadlines (nếu có)

**Assume Rule (chi tiết phụ — tự giả định được):**
- Sprint duration (2 weeks mặc định)
- Buffer percentage (15-20% mặc định)
- Communication cadence (weekly status report)
- Documentation deliverables (standard set)
- QA approach (manual + automated mặc định)

**Handoff (kết thúc pipeline) khi:**
- Review gate PASS
- Assumption Ledger: không có item impact High chưa confirmed
- Tất cả finalization conditions met

**Loop back sang Solution Architect khi:**
- WBS task không map được về scope item nào
- Phát hiện scope conflict hoặc gap
- Technical assumption cần SA confirm

---

### Agent: Comm Hub

**File:** `agents/comm-hub/AGENT.md`

**Persona:** Communication specialist — không sở hữu stage nào, chỉ được gọi khi
agent khác cần hỏi khách hàng (Stop Rule triggered).

**Trigger:** Bất kỳ agent nào gặp Stop Rule → gọi Comm Hub trước khi output câu hỏi.

**Chức năng:**

1. **Tone Switcher:**
   - Khách là CTO/Tech Lead → ngôn ngữ kỹ thuật, ví dụ cụ thể
   - Khách là CEO/Business → ngôn ngữ business value, ROI
   - Khách là PM/PO → ngôn ngữ delivery, timeline, risk
   - Mặc định: business tone (nếu chưa biết stakeholder type)

2. **Batching:**
   - Nếu có > 1 câu hỏi pending → gom thành 1 block
   - Tối đa 5 câu hỏi / lần hỏi (tránh overwhelm)
   - Ưu tiên câu hỏi blocking trước

3. **Format chuẩn (giữ từ hệ thống cũ):**
   - Mỗi câu hỏi: 3 options + 1 recommendation
   - Ghi rõ impact: ảnh hưởng scope / timeline / cost / risk
   - Đánh số để khách dễ trả lời

4. **Language matching:**
   - Vietnamese input → Vietnamese questions
   - English input → English questions
   - Không mix ngôn ngữ

---

## Chi Tiết Shared Skill: Assumption Ledger

**File:** `skills/assumption-ledger/SKILL.md`

**Mục đích:** Theo dõi tập trung mọi giả định được tạo ra trong suốt pipeline.
Cung cấp visibility cho Review gate và khách hàng.

### Khi nào được gọi

Bất kỳ agent nào trigger Assume Rule → gọi Assumption Ledger để ghi nhận.

### Cấu trúc dữ liệu

```markdown
## Assumption Ledger

| ID   | Assumption                    | Created By | Stage     | Impact | Status           | Note                    |
|------|-------------------------------|------------|-----------|--------|------------------|-------------------------|
| A-1  | Redis for session caching     | SA         | Technical | Low    | Active           | Swap-able, no scope hit |
| A-2  | 3 user roles (Admin/User/PM)  | BA         | Discovery | Medium | Pending confirm  | Asked 2025-05-20        |
| A-3  | No legacy data migration      | SA         | Scope     | High   | Confirmed        | Client confirmed email  |
| A-4  | PostgreSQL as primary DB      | SA         | Technical | Low    | Active           | Standard choice         |
```

### Phân loại Impact

| Impact | Định nghĩa | Ví dụ |
|--------|-------------|-------|
| Low | Sai → chỉ thay đổi implementation detail, không ảnh hưởng scope/cost | Caching engine, logging tool |
| Medium | Sai → thay đổi effort estimate hoặc timeline | Số user roles, API complexity |
| High | Sai → thay đổi scope, cost, hoặc architecture | Migration required, compliance, platform choice |

### Status lifecycle

```
Active → Confirmed (khách xác nhận)
Active → Rejected (khách phủ nhận → cần re-scope)
Active → Replaced (thay bằng assumption khác)
Pending confirm → Confirmed / Rejected
```

### Tích hợp với Review Gate

Review agent (Stage 6) PHẢI kiểm tra Assumption Ledger:
- Có assumption nào impact=High mà status≠Confirmed → **BLOCK finalization**
- Có assumption nào impact=Medium mà status=Active > 7 ngày → **WARNING**
- Liệt kê tất cả Active assumptions trong proposal (Section: Assumptions & Risks)

### Output

File: `workspace/assumption-ledger.md`
Template: `references/assumption-ledger.md`

---

## Quy Tắc Tương Tác Giữa Các Thành Phần

### Nguyên tắc 1: Agents KHÔNG gọi nhau trực tiếp

```
❌  Senior BA gọi Solution Architect
✅  Senior BA → trả kết quả → Orchestrator → load Solution Architect
```

Orchestrator là trung tâm điều phối duy nhất.

### Nguyên tắc 2: Agent chỉ gọi skills mình own

```
Senior BA active:
  → skills/discovery/SKILL.md    ✅ (thuộc ownership)
  → skills/scope/SKILL.md        ❌ (thuộc SA)
```

### Nguyên tắc 3: Shared skills/agents gọi được từ bất kỳ đâu

- Comm Hub: bất kỳ agent nào cần hỏi khách
- Assumption Ledger: bất kỳ agent nào tạo assumption

### Nguyên tắc 4: Giao tiếp qua workspace artifacts

Agents không message nhau. Giao tiếp = đọc artifact của agent trước đó:

| Artifact | Viết bởi | Đọc bởi |
|----------|----------|----------|
| discovery.md | Senior BA | SA, PM |
| deal-context.md | Senior BA | Tất cả |
| backlog-questions.md | Senior BA | Comm Hub cập nhật |
| pain-scope.md | Solution Architect | PM |
| technical.md | Solution Architect | PM |
| wbs.md | Senior PM | Review |
| proposal/ | Senior PM | Review |
| assumption-ledger.md | Tất cả (ghi) | Review (kiểm tra) |
| status.md | Orchestrator | Tất cả (đọc) |
| context.md | Senior BA (Context skill) | Tất cả (resume) |

### Nguyên tắc 5: Handoff có điều kiện

| Từ → Sang | Điều kiện |
|-----------|-----------|
| BA → SA | discovery.md + deal-context.md EXISTS, không còn Stop Rule active |
| SA → PM | pain-scope.md EXISTS, scope register có ≥1 approved item |
| PM → Done | Review gate PASS, Ledger không có High unconfirmed |
| SA → BA (loop back) | Scope item không map về requirement |
| PM → SA (loop back) | WBS conflict với scope |
| Any → Comm Hub | Stop Rule triggered |
| Any → Assumption Ledger | Assume Rule triggered |

---

## Thay Đổi Cần Thực Hiện Cho rules.md

### Thêm mới: Stop Rule / Assume Rule (thay thế rule #1 và #2)

```markdown
## 1. Stop Rule — Thông tin cốt lõi

Khi agent phát hiện thiếu thông tin thuộc danh sách Stop Rule của mình:
1. Dừng stage hiện tại
2. Đánh dấu status = HOLD
3. Gọi Comm Hub để format câu hỏi
4. Chờ khách trả lời trước khi tiếp tục

Ranh giới: "Nếu thông tin này SAI sẽ thay đổi scope, effort, hoặc cost → Stop Rule."

## 2. Assume Rule — Chi tiết phụ

Khi agent phát hiện thiếu thông tin thuộc danh sách Assume Rule của mình:
1. Chọn giá trị mặc định hợp lý
2. Gọi Assumption Ledger để ghi nhận (ID, nội dung, impact, status=Active)
3. Tiếp tục stage — không dừng, không hỏi khách

Ranh giới: "Nếu thông tin này SAI chỉ thay đổi implementation detail → Assume Rule."

## Escalation

- Assumption đã Active > 7 ngày + impact Medium → escalate lên Stop Rule ở stage tiếp theo
- Assumption bị Rejected bởi khách → trigger re-scope (loop back)
```

### Giữ nguyên (đánh số lại)

- Rule #3: Every scope item needs a source
- Rule #4: Proposal ↔ WBS must match
- Rule #5: Never expand scope silently
- Rule #6: Greenfield vs Brownfield
- Rule #7: Think before generating
- Rule #8: Stages run in order (CẬP NHẬT: thêm handoff conditions)
- Rule #9: Artifact must exist before marking Done
- Rule #10: Match the client's language
- Rule #11: Conserve tokens

---

## Thay Đổi Cần Thực Hiện Cho Orchestrator

### Orchestrator mới: Routing 2 tầng

```markdown
## Stage → Agent Mapping

| Stage | Agent | Skill |
|-------|-------|-------|
| 1. Discovery | Senior BA | discovery |
| 2. Context | Senior BA | context |
| 3. Scope | Solution Architect | scope |
| 3.5. Technical | Solution Architect | technical |
| 4. WBS | Senior PM | wbs |
| 5. Proposal | Senior PM | proposal |
| 6. Review | Senior PM | review-finalize |

## Routing Procedure

1. Đọc `workspace/status.md` → xác định current stage
2. Map stage → agent (bảng trên)
3. Load `agents/<agent>/AGENT.md` (persona + rules)
4. Load `skills/<skill>/SKILL.md` (procedure)
5. Agent chạy skill với Stop/Assume logic
6. Kết quả:
   - Stage hoàn thành → kiểm tra handoff conditions → next stage/agent
   - Stop Rule triggered → load Comm Hub → HOLD
   - Assume Rule triggered → gọi Assumption Ledger → tiếp tục
   - Loop back needed → quay lại agent trước

## Handoff Conditions

BA → SA:
  - workspace/discovery.md EXISTS
  - workspace/deal-context.md EXISTS
  - Không còn Stop Rule question chưa trả lời

SA → PM:
  - workspace/pain-scope.md EXISTS
  - Scope register có ≥1 approved in-scope item
  - workspace/technical.md EXISTS hoặc skip condition met

PM → Done:
  - Review gate PASS
  - assumption-ledger.md: không có impact=High + status≠Confirmed

## Loop Back Triggers

SA → BA: scope item không map về requirement trong deal-context
PM → SA: WBS task không map về scope item, hoặc scope conflict detected
Any → same agent (retry): khách trả lời sau HOLD → resume stage
```

---

## Thay Đổi Cần Thực Hiện Cho presale-run.md

### Cập nhật flow

```markdown
## Trigger

1. Load `.agent/rules.md` (once per session)
2. Load orchestrator routing table
3. Locate active project folder
4. Check client-input.md has content
5. Orchestrator xác định current stage + agent
6. Load AGENT.md → load SKILL.md → chạy stage
7. Sau mỗi stage: state output, check handoff, recommend next

## Stages (giữ nguyên bảng, thêm cột Agent)

| # | Agent | Skill | In | Out | Gate |
|---|-------|-------|----|----|------|
| 1 | Senior BA | discovery | Raw input | Intake, facts, questions | Unknowns visible |
| 2 | Senior BA | context | Answers, feedback | Deal context, change log | Info classified |
| 3 | Sol. Architect | scope | Context, requirements | Pain points, scope register | Items mapped |
| 3.5 | Sol. Architect | technical | Scope, NFRs | Architecture, tech decisions | Optional |
| 4 | Senior PM | wbs | Scope, solution | WBS draft, milestones | WBS maps to scope |
| 5 | Senior PM | proposal | All artifacts | Proposal (multi-section) | Proposal = WBS scope |
| 6 | Senior PM | review-finalize | All artifacts | Review findings or approval | Gates pass |
```

---

## Template: references/assumption-ledger.md

```markdown
# Assumption Ledger

## Overview

| Total | Active | Confirmed | Rejected | High Impact Unconfirmed |
|-------|--------|-----------|----------|------------------------|
| 0     | 0      | 0         | 0        | 0                      |

## Ledger

| ID | Assumption | Created By | Stage | Impact | Status | Date | Note |
|----|-----------|------------|-------|--------|--------|------|------|
|    |           |            |       |        |        |      |      |

## Rules

- ID format: A-{n} (sequential, never reuse)
- Impact: Low / Medium / High
- Status: Active / Pending confirm / Confirmed / Rejected / Replaced
- High + unconfirmed → blocks finalization
- Medium + Active > 7 days → escalate to Stop Rule
```

---

## Ví Dụ Flow End-to-End

```
1. User paste email khách hàng (tiếng Việt)

2. Orchestrator:
   - status.md: chưa có stage nào → Stage 1
   - Map: Stage 1 → Senior BA → discovery skill
   - Load: agents/senior-ba/AGENT.md + skills/discovery/SKILL.md

3. Senior BA chạy Discovery:
   - Normalize input → extract facts
   - Kiểm tra Stop Rule list:
     ✗ Business goal: có (trong email)
     ✗ Target users: có
     ✗ Budget: THIẾU → Stop Rule triggered
     ✗ Timeline: THIẾU → Stop Rule triggered
   - Kiểm tra Assume Rule list:
     ✗ CI/CD: thiếu → assume GitHub Actions → gọi Assumption Ledger (A-1, Low)
   - 2 câu hỏi Stop Rule → gọi Comm Hub

4. Comm Hub:
   - Detect: stakeholder chưa rõ → dùng business tone (mặc định)
   - Batch: 2 câu hỏi → 1 block
   - Format: 3 options + 1 rec mỗi câu
   - Output câu hỏi cho user
   - Status = HOLD

5. User paste câu trả lời khách

6. Orchestrator:
   - Status = HOLD → resume Senior BA
   - Load: agents/senior-ba/AGENT.md + skills/context/SKILL.md (Stage 2)

7. Senior BA chạy Context:
   - Classify input: budget = fact, timeline = decision
   - Update deal-context.md
   - Kiểm tra: không còn Stop Rule items thiếu
   - Stage 2 done

8. Orchestrator:
   - Handoff check: discovery.md ✓, deal-context.md ✓, no Stop Rule active ✓
   - Handoff → Solution Architect
   - Load: agents/solution-architect/AGENT.md + skills/scope/SKILL.md

9. Solution Architect chạy Scope:
   - Đọc deal-context.md
   - Build pain points + scope register
   - Kiểm tra Stop Rule: Greenfield? → có trong context ✓
   - Kiểm tra Assume Rule: DB engine thiếu → assume PostgreSQL → Ledger (A-2, Low)
   - Stage 3 done

10. ... tiếp tục đến Stage 6 Review
```

---

## Checklist Thực Hiện Refactor

### Phase 1: Tạo agents/ (không phá gì cũ)

- [x] Tạo `agents/senior-ba/AGENT.md`
- [x] Tạo `agents/solution-architect/AGENT.md`
- [x] Tạo `agents/senior-pm/AGENT.md`
- [x] Tạo `agents/comm-hub/AGENT.md`

### Phase 2: Tạo Assumption Ledger

- [x] Tạo `skills/assumption-ledger/SKILL.md`
- [x] Tạo `references/assumption-ledger.md` (template)

### Phase 3: Cập nhật rules.md

- [x] Thay rule #1, #2 bằng Stop Rule / Assume Rule
- [x] Giữ nguyên rule #3-#11 (đánh số lại nếu cần)

### Phase 4: Cập nhật Orchestrator

- [x] Thêm Stage → Agent mapping table
- [x] Thêm routing 2 tầng logic
- [x] Thêm handoff conditions
- [x] Thêm loop back triggers

### Phase 5: Cập nhật workflows

- [x] Cập nhật `presale-run.md`: thêm cột Agent, flow qua agents
- [x] Cập nhật `presale-update.md`: revision đi qua đúng agent owner

### Phase 6: Cập nhật documentation

- [x] Cập nhật `README.md`: mô tả mô hình mới
- [x] Cập nhật `CLAUDE.md`: routing table mới

### Phase 7: Test

- [ ] Chạy thử /presale-run với project mới
- [ ] Verify handoff BA → SA hoạt động
- [ ] Verify handoff SA → PM hoạt động
- [ ] Verify Stop Rule → Comm Hub → HOLD → resume hoạt động
- [ ] Verify Assume Rule → Ledger ghi đúng
- [ ] Verify Review gate check Ledger

---

## Rủi Ro & Mitigation

| Rủi ro | Mức | Mitigation |
|--------|-----|-----------|
| Agent persona quá dài, tốn token | Trung bình | Giữ AGENT.md < 80 dòng, chỉ chứa persona + rules, không chứa procedure |
| Orchestrator phức tạp hơn, dễ routing sai | Trung bình | Handoff conditions rõ ràng, dựa trên file existence (dễ verify) |
| Comm Hub thêm 1 bước → chậm hơn | Thấp | Comm Hub chỉ format, không generate content mới |
| Assumption Ledger bị quên gọi | Thấp | Nhúng reminder vào mỗi AGENT.md: "Khi assume → gọi Ledger" |
| Backward compatibility với projects cũ | Thấp | Skills giữ nguyên procedure, chỉ thêm layer agent phía trên |

