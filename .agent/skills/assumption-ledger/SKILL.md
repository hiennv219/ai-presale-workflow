---
name: assumption-ledger
description: Track all assumptions created during pipeline execution. Shared skill callable by any agent.
---

# Assumption Ledger

## Purpose

Theo dõi tập trung mọi giả định được tạo ra trong suốt pipeline. Cung cấp visibility cho Review gate và khách hàng.

## Trigger

Bất kỳ agent nào trigger Assume Rule → gọi skill này để ghi nhận.

## Procedure

### Ghi Assumption Mới

1. Đọc `workspace/assumption-ledger.md` (tạo từ template nếu chưa có)
2. Tạo ID mới: `A-{n}` (sequential, never reuse)
3. Ghi entry với: ID, nội dung, Created By (agent), Stage, Impact, Status=Active, Date, Note
4. Cập nhật Overview table (totals)
5. Lưu file

### Phân Loại Impact

| Impact | Định nghĩa | Ví dụ |
|--------|-------------|-------|
| Low | Sai → chỉ thay đổi implementation detail, không ảnh hưởng scope/cost | Caching engine, logging tool |
| Medium | Sai → thay đổi effort estimate hoặc timeline | Số user roles, API complexity |
| High | Sai → thay đổi scope, cost, hoặc architecture | Migration required, compliance, platform choice |

### Status Lifecycle

```
Active → Confirmed (khách xác nhận)
Active → Rejected (khách phủ nhận → cần re-scope)
Active → Replaced (thay bằng assumption khác)
Pending confirm → Confirmed / Rejected
```

### Escalation

- Assumption Active > 7 ngày + impact Medium → escalate lên Stop Rule ở stage tiếp theo
- Assumption bị Rejected bởi khách → trigger re-scope (loop back)

## Tích Hợp Với Review Gate

Review agent (Stage 6) PHẢI kiểm tra Assumption Ledger:
- impact=High + status≠Confirmed → **BLOCK finalization**
- impact=Medium + status=Active > 7 ngày → **WARNING**
- Liệt kê tất cả Active assumptions trong proposal (Section: Assumptions & Risks)

## Output

File: `workspace/assumption-ledger.md`
Template: `references/assumption-ledger.md`
