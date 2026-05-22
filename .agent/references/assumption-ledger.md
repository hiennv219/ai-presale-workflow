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
