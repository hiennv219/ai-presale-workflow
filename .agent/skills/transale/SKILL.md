---
name: transale
description: Translate Markdown documents between English, Japanese, and Vietnamese while preserving structure, formatting, and technical accuracy.
---

# Presale Transale

Translate presale artifacts (proposals, WBS, scope, discovery) between supported languages while maintaining document integrity, professional tone, and technical precision.

## Trigger

`/presale-transale <file-or-directory-path> [target-language]`

### Modes

| Mode | Trigger | Behavior |
|------|---------|----------|
| **Single file** | Path to a `.md` file | Translate that file |
| **Directory** | Path to a directory | Translate all `.md` files inside |
| **Incremental** | `proposal` or path to `workspace/proposal/` | Translate only changed sections, concat result |

### Supported Languages

| Code | Language   | Native Name |
|------|------------|-------------|
| `en` | English    | English     |
| `ja` | Japanese   | 日本語      |
| `vi` | Vietnamese | Tiếng Việt  |

### Prerequisites

1. Resolve target path:
   - Name only (e.g. `proposal`) → `workspace/proposal/` (incremental mode)
   - Directory (e.g. `workspace/proposal/`) → incremental mode if contains numbered section files (`01-*.md`, `02-*.md`...)
   - Full path to single file → single file mode
2. File(s) must exist and be non-empty.
3. Target language must be one of: `en`, `ja`, `vi`.
   - If not provided → ask user to choose.
4. Detect source language (auto-detect from content).
5. If source language = target language → report "File is already in {{language}}", stop.

If not met → report what's missing, do NOT translate.

## Procedure

### Standard Mode (single file or non-proposal directory)

1. Read source file(s) completely.
2. Detect source language.
3. Validate target language ≠ source language.
4. Translate section-by-section, following rules below.
5. Run quality checks.
6. Write output file(s):
   - Same directory as source.
   - Filename: `{{original_name}}_{{lang_code}}.md` (e.g. `wbs_ja.md`)
   - Already-translated file (e.g. `proposal_ja.md` → Vietnamese): output `proposal_vi.md`, not `proposal_ja_vi.md`.
7. Report output summary.

### Incremental Mode (proposal sections)

Triggered when target is `workspace/proposal/` or shorthand `proposal`.

1. Identify section files: all `NN-*.md` files in `workspace/proposal/` (e.g. `01-project-overview.md`).
2. Determine output directory: `workspace/proposal_{{lang_code}}/` (e.g. `workspace/proposal_ja/`).
3. **Change detection** — for each section file:
   - If translated version does NOT exist → mark as **needs translation**.
   - If translated version exists → compare source file's modification time vs translated file's modification time.
     - Source is newer → mark as **needs translation**.
     - Source is same or older → mark as **skip** (already up-to-date).
4. Report change detection summary:
   ```
   Incremental translation ({{source_lang}} → {{target_lang}}):
     - Needs translation: {{list of changed files}}
     - Up-to-date (skipped): {{list of unchanged files}}
   ```
5. Translate only the files marked as **needs translation**, following Translation Rules below.
6. Write each translated section to `workspace/proposal_{{lang_code}}/{{same_filename}}`.
7. Run quality checks on each translated section.
8. **Concat** — concatenate all translated sections (in sort order) into `workspace/proposal-full_{{lang_code}}.md`.
9. Report output summary.

## Translation Rules

### 1. Structure Preservation

- Keep ALL Markdown formatting intact: headings, lists, tables, code blocks, links, images, bold, italic.
- Preserve heading hierarchy (`#`, `##`, `###`, etc.) exactly as source.
- Preserve table column count, alignment, and separators.
- Preserve code blocks and inline code — do NOT translate code.
- Preserve file paths, URLs, and link references unchanged.
- Preserve Markdown comments (`<!-- ... -->`) unchanged.
- Preserve frontmatter (`---` YAML blocks) unchanged.

### 2. Technical Terms — Do NOT Translate

- **Product names**: brand names, tool names, platform names
- **Technical acronyms**: API, SDK, SLA, NFR, MVP, POC, UAT, CI/CD, SSO, RBAC, etc.
- **Programming terms**: frontend, backend, microservices, database, cache, queue, etc.
- **Framework/library names**: React, Next.js, Spring Boot, PostgreSQL, Redis, etc.
- **File names and paths**: `discovery.md`, `workspace/proposal/`, etc.
- **Status labels**: In-Scope, Out-of-Scope, Future Phase, Open, Closed, etc.
- **Reference IDs**: `SC-01`, `WBS-2.1`, `R-03`, etc.
- **Effort estimates**: `40h`, `2 sprints`, etc.

### 3. Tone & Style by Language

#### English (`en`)
- Professional, concise, action-oriented.
- Use active voice where possible.
- Standard business English for proposals.

#### Japanese (`ja`)
- Use です/ます (desu/masu) polite form consistently.
- Use 敬語 (keigo) appropriately for client-facing documents.
- Technical terms: keep English with カタカナ reading where natural.
  - Example: "API（エーピーアイ）" on first use, then "API" subsequently.
- Preserve numbered lists as Arabic numerals (1, 2, 3), not Japanese numerals.
- Date format: YYYY年MM月DD日 for inline dates, keep YYYY-MM-DD in metadata/tables.

#### Vietnamese (`vi`)
- Professional, clear, natural Vietnamese business writing.
- Avoid overly literal translations — prioritize natural phrasing.
- Technical terms: keep English original, no forced Vietnamese translation.
  - Example: "API" stays "API", not "giao diện lập trình ứng dụng".
- Use Vietnamese diacritics correctly.
- Date format: DD/MM/YYYY for inline dates, keep YYYY-MM-DD in metadata/tables.

### 4. Section-Specific Guidelines

#### Tables
- Translate header labels and cell content.
- Do NOT translate column values that are: numbers, dates, file paths, status codes, technical identifiers.
- Keep table structure (`|---|---|`) exactly as source.

#### Proposal Sections
- Translate section titles to target language equivalent.
- Keep section numbering unchanged.
- Translate body text naturally — not word-for-word.

### 5. Quality Checks

Before outputting translated file:

1. **Structure match**: Heading count, table count, list item count must match source.
2. **No missing content**: Every paragraph/item in source must appear in translation.
3. **No added content**: Do not add explanations, notes, or content not in source.
4. **Technical terms intact**: Spot-check that technical terms were not translated.
5. **Links preserved**: All `[text](url)` links must remain functional.
6. **Code blocks untouched**: All fenced code blocks identical to source.

## Output

Single file:
```
Translated ({{source_lang}} → {{target_lang}}):
  - {{output_file_path}} ({{file_size}})
Source: {{source_file_path}}
```

Multi-file (directory):
```
Translated ({{source_lang}} → {{target_lang}}):
  - {{file_1_path}} ({{size}})
  - {{file_2_path}} ({{size}})
  ...
Total: {{count}} files translated
Source directory: {{source_dir}}
```

Incremental (proposal sections):
```
Incremental translation ({{source_lang}} → {{target_lang}}):
  Translated ({{count_translated}} sections):
    - {{section_file_1}} ({{size}})
    - {{section_file_2}} ({{size}})
  Skipped ({{count_skipped}} sections, unchanged):
    - {{section_file_3}}
    - {{section_file_4}}
  Concatenated: workspace/proposal-full_{{lang_code}}.md ({{total_words}} words)
  Saved ~{{tokens_saved}} tokens by skipping unchanged sections.
```

## Edge Cases

- **Mixed-language source**: Treat the dominant language as source. Translate only the source-language portions; keep other-language technical terms as-is.
- **Empty sections**: Keep empty sections with translated headings.
- **Images with alt text**: Translate alt text, keep image path unchanged.
- **Force re-translate all**: If user says "force" or "all" with incremental mode, skip change detection and translate every section.
- **New section added**: A new source section without a translated counterpart is always translated.
- **Section deleted from source**: If a translated section exists but source was removed, delete the orphaned translated file and exclude from concat.
