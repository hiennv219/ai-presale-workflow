---
name: slide-deck
description: Generate Marp slide deck from final-proposal.md. Extracts key points per section into visual, presentation-ready slides.
---

# Slide Deck Generator

## Purpose

Convert a finalized proposal into a concise slide deck for client presentations. Slides are storytelling-focused — not a copy-paste of the doc.

## Input

- `workspace/final-proposal.md` (must exist and be finalized)

## Output

- `workspace/slide-deck.md` (Marp-compatible Markdown)

## Slide Structure (8–12 slides)

| # | Slide | Source | Content |
|---|-------|--------|---------|
| 1 | Cover | Metadata | Project name, client, date, author |
| 2 | The Problem | 1.1 | Pain points — 2-3 bullet max, empathy-driven |
| 3 | Our Solution | 1.3 + 1.4 | Solution overview + key features (business language) |
| 4 | How It Works | 3.1 | User flow diagram (Mermaid or simplified visual) |
| 5 | What You'll See | 3.2 | 1-2 wireframe screenshots or ASCII (optional) |
| 6 | Architecture | 5.2 | Target architecture diagram (simplified) |
| 7 | Tech Stack | 5.5 | Grouped by layer, 1 line each |
| 8 | Roadmap | 6.1 | Timeline visual — phases + durations |
| 9 | Team & Effort | 7.2 + 8.1 | Resource plan + total effort |
| 10 | Investment | 8.1 + 8.2 + 8.3 | Pricing, payment schedule, monthly OpEx |
| 11 | What's Next | 6.4 | Post-MVP vision (if applicable) |
| 12 | Next Steps / CTA | — | Call to action: sign-off, kick-off date, contact |

## Rules

- Max 12 slides. Mỗi slide tối đa 5 bullet hoặc 1 diagram.
- Không copy nguyên văn từ proposal — rewrite ngắn gọn, presentation-friendly.
- Dùng business language cho slide 1–4, 9–12. Technical language chỉ cho slide 6–8.
- Diagrams: giữ nguyên Mermaid/ASCII từ proposal nếu đủ gọn. Nếu quá phức tạp, simplify.
- Slide 5 (wireframe) là optional — skip nếu wireframe quá chi tiết cho slide format.
- Mỗi slide phải có speaker notes (comment block) gợi ý presenter nói gì.

## Marp Format

```markdown
---
marp: true
theme: default
paginate: true
---

# Slide Title

Content here

<!-- Speaker notes: what to say -->

---

# Next Slide
```

## Export

Handled by `/presale-deck` workflow — not this skill's responsibility.
