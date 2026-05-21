---
name: wireframe
description: Draw ASCII wireframes for UI screens in proposals. Always visual, never text-only descriptions.
---

# Presale Wireframe

## Core Rule

**Wireframe = visual layout.** Never describe a screen with bullet points or prose alone. Every wireframe section MUST contain ASCII box-drawing diagrams showing spatial layout, field placement, and visual hierarchy.

## When to Use

- Proposal section 3.2 (High-Level Wireframe)
- Any time a UI screen needs to be communicated in a markdown deliverable
- When `proposal` skill delegates wireframe work

## Procedure

1. Identify screens to wireframe from scope/user-flow (core features only).
2. For each screen, draw ASCII wireframe showing:
   - Page title / navigation context
   - Content hierarchy (what's on top vs bottom)
   - Input fields with labels
   - Action buttons with placement
   - Data display areas with sample data
   - Alert/notification zones
3. Add brief annotation below each wireframe only if interaction behavior is non-obvious.

## ASCII Format Rules

```
┌─────────────────────────────────────┐  ← Screen boundary
│  Title / Header                     │
├─────────────────────────────────────┤  ← Section divider
│                                     │
│  Label:                             │  ← Field label
│  ┌─────────────────────────────┐    │  ← Input field
│  │ placeholder text            │    │
│  └─────────────────────────────┘    │
│                                     │
│         [ Button ]                  │  ← Action
└─────────────────────────────────────┘
```

### Characters

- Box-drawing: `┌ ┐ └ ┘ │ ─ ├ ┤ ┬ ┴`
- Buttons: `[ Label ]`
- Tabs: `[ Tab1 | Tab2 | Tab3 ]`
- Checkbox: `[x] Selected  [ ] Unselected`
- Radio: `(•) Selected  ( ) Unselected`
- Dropdown: `[ Selected value     ▼ ]`
- Icons/indicators: use emoji sparingly (⚠️ for alerts, 📊 for data)

### Layout Patterns

**Form screen:**
```
┌───────────────────────┐
│  Form Title           │
├───────────────────────┤
│  Field 1: [_______]   │
│  Field 2: [_______]   │
│  Field 3: [_______]   │
│       [ Submit ]      │
└───────────────────────┘
```

**Dashboard screen:**
```
┌───────────────────────────────────┐
│  Dashboard Title                  │
├───────────────────────────────────┤
│  ⚠️ Alert Section                 │
│  ┌─────────────────────────────┐  │
│  │ alert items                 │  │
│  └─────────────────────────────┘  │
│                                   │
│  📋 List Section                  │
│  ┌─────────────────────────────┐  │
│  │ item 1                      │  │
│  ├─────────────────────────────┤  │
│  │ item 2                      │  │
│  └─────────────────────────────┘  │
└───────────────────────────────────┘
```

**Table/List screen:**
```
┌──────────────────────────────────────┐
│  [Search: _________ ] [ Filter ▼ ]  │
├──────┬──────────┬────────┬───────────┤
│ Col1 │ Col2     │ Col3   │ Actions   │
├──────┼──────────┼────────┼───────────┤
│ data │ data     │ data   │ [Edit]    │
│ data │ data     │ data   │ [Edit]    │
└──────┴──────────┴────────┴───────────┘
```

## Rules

- Keep width under 80 characters for readability.
- Use sample/realistic data inside wireframes (not "lorem ipsum").
- One wireframe per screen — don't combine multiple views into one diagram.
- Show the default/loaded state. Add a second wireframe for important alternate states (empty, error, loading) only if it affects the proposal's clarity.
- Presale level only — show what the user sees, not implementation details.
