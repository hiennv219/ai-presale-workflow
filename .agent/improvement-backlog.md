# Pipeline Improvement Backlog

> Recorded from review on 2026-05-20. Modify when time permits.

## Completed / Implemented

- [x] #7 — Cascade preview before executing updates (presale-update Step 1 already includes impact summary + confirmation prompt)
- [x] #1 — Allow pasting input directly in `/presale-run` (updated presale-run.md + presale-init.md)
- [x] #2 — `/presale-preview` command runs concat on-demand without gating (presale-preview.md + CLAUDE.md)
- [x] #3 — Automatic deal complexity classification after Discovery (discovery SKILL.md + wbs SKILL.md, min level 3)
- [x] #4 — Add "Next Action" + "Blockers" + "Deal Complexity" to status.md template (no separate command needed)
- [x] #15 — Dynamic & Customizable Proposal Template (self-customizable Proposal structure)

## To Do

### #5 — Flexible Question Format
- **Issue**: Forcing 3 options + 1 recommendation for all questions → open-ended questions feel artificially formatted
- **Solution**: Allow 3 question types: open-ended, yes/no confirmation, and multi-option (keep 3-option format for decision-making)
- **Effort**: Low

### #6 — PDF Export
- **Issue**: Only HTML is generated, but presale processes require PDF to email to clients
- **Solution**: Add `--pdf` flag to `presale_cli.py` using puppeteer (implemented)
- **Effort**: Medium

### #8 — Slide Deck Generation ✅
- **Issue**: Presale always requires slides for meetings, currently done manually
- **Solution**: `/presale-slides` — skill to summarize proposal → Markdown slides, handoff to GPT/Gemini
- **Implemented**: workflow + skill (17 fixed slides, content-dependent expansion)

### #10 — Multi-Project Dashboard
- **Issue**: A presale engineer handles 3-5 deals simultaneously, lacks overview
- **Solution**: `/presale-dashboard` scans all `projects/`, displays a summary table: deal, stage, last updated, blockers
- **Effort**: High

### #11 — Input Pruning (Dynamic input selection per Proposal Section)
- **Issue**: LLM reads the entire workspace (~100 KB) for every section in Stage 5, wasting tokens.
- **Solution**: Configure an Input Dependency table in `proposal/SKILL.md` to filter only relevant input files (Overview reads context+scope, Budget reads wbs, etc.).
- **Effort**: Low (~67% reduction in Stage 5 input tokens)

### #12 — ~~Offline Scope Coverage Matrix & Local Linter~~ ✅ DONE
- **Issue**: Cross-checks like Scope↔WBS and WBS↔Budget are done by the LLM, which is slow and token-heavy.
- **Solution**: Write a local Python script (integrate into `presale_cli.py --lint`) to automate static checks, blocking errors before calling Stage 6 Review.
- **Effort**: Medium (~30k tokens saved per review, speed <1s)
- **Implemented**: Added `--lint` flag to `shared/scripts/presale_cli.py` with 5 checks (Scope↔WBS, Roles↔Budget, Financial Math, Milestones). Review skill runs lint first.

### #13 — Batch Proposal Generation (Multiple sections in one turn)
- **Issue**: Generating 8 sections with 8 separate API calls repeats the system prompt and rules redundantly.
- **Solution**: Allow the LLM to output multiple sections in a single turn using section markers (`<!-- SECTION:XX -->`), then use a local script to split them.
- **Effort**: Medium (~96k tokens saved per project)

### #14 — ~~Incremental Translation (Translate by Section)~~ ✅ DONE
- **Issue**: Translation is currently done on the full compiled `proposal-full.md` file; small edits force a complete re-translation.
- **Solution**: Support translating individual section files and concating them later to avoid re-translating unchanged sections.
- **Effort**: Low (~20k tokens saved per edit)
- **Implemented**: Added Incremental Mode to `transale/SKILL.md` — manifest-based change detection, per-section translation, auto-concat.

### #16 — Agent Model

[ CLIENT IDEAS ]
                      |
                      v
                 --> ( + )
                |     |
                |     +===============================+
                |     | 1. INGESTION & INTERROGATION  |
                |     |      (Agent: Senior BA)       |
                |     +===============================+
                |                    |
                |                    v
                |             /=============\
                |            /  INFORMATION  \
                |            \  VERIFICATION /
                |             \=============/
                |              |     |     |
                |     +--------+     |     +---------+
                |     |              |               |
                | (Missing Core)     |       (Missing Details)
                | (Stop Rule)  (Sufficient Info) (Assume Rule)
                |     |              |               |
                |     v              |               v
                | +---------------+  |       +----------------+
                | |  HOLD STATUS  |  |       | AUTO ASSUME    |
                | +---------------+  |       | (Call skill:   |
                |     |              |       | Assumption     |
                |     v              |       | Ledger)        |
                | +---------------+  |       +----------------+
                | |Agent: COMM HUB|  |               |
                | |(Tone Switcher)|  |               |
                | +---------------+  |               |
                |     |              |               |
                |     v              |               |
                | [Ask Client]       |               |
                |     |              |               |
                '-----+              |               |
                 (Client responds)   |               |
                                     v               v
                              +===============================+
                              |    2. SCOPING & PRUNING       |
                              |  (Agent: Solution Architect)  |
                              +===============================+
                                             |
                                             v
                              +===============================+
                              |   3. ARTIFACT GENERATION      |
                              |       (Agent: Senior PM)      |
                              |     (Skill: WBS Generator)    |
                              +===============================+
                                             |
                                             v
                             [ OUTPUT: PROPOSAL + WBS TABLE  ]
                             [    (With Assumptions list)    ]