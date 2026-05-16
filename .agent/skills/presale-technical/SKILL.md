---
name: presale-technical
description: Propose technical decisions when SA has not provided them. Optional — skipped if tech decisions already in context.
---

# Presale Technical

## Trigger Condition

Run ONLY when deal-context has no confirmed technical decisions (tech stack, architecture pattern, infrastructure approach). Skip if SA has already provided these.

## Procedure

1. Read approved scope + constraints + non-functional requirements from deal-context.
2. Propose: architecture pattern, tech stack, infrastructure approach, key technical trade-offs.
3. Draw system architecture as ASCII box diagram (see format below).
4. Write component communication narrative grouped by delivery phases.
5. Mark all outputs as status: proposed (not confirmed).
6. Present to user/SA for approval before proceeding.

## Architecture Diagram Format

Use ASCII box art with clear layers. Structure top-to-bottom:

```
CLIENT LAYER        → Apps, portals, dashboards
API GATEWAY         → Routing, auth check, rate limit
SERVICE LAYER       → Core services with responsibilities listed inside boxes
DATA LAYER          → Databases, caches
EVENT/MESSAGING     → Async communication channels
```

Rules for the diagram:
- Use box-drawing characters: `┌ ┐ └ ┘ │ ─ ┬ ┴ ├ ┤ ▼ ▶`
- Label each box with service name + bullet list of responsibilities
- Show connections with arrows and protocol labels (REST, gRPC, WebSocket, Pub/Sub)
- Annotate phase-specific components with `(Phase N)`
- Keep width under 80 characters for terminal readability

## Component Communication Section

After the diagram, write a **phase-by-phase narrative** explaining how components interact:

```
**Communication between core components (N-Year Vision):**
- **Phase 1 (name):** [which service does what, how they communicate]
- **Phase 2 (name):** [what changes, what stays]
- **Phase N (name):** [expansion, no arch changes needed because...]
```

Focus on: who owns what responsibility, what events flow between services, why the architecture doesn't need to change in later phases.

## Output

Write to `workspace/technical.md`:
- System architecture diagram (ASCII box art)
- Component communication narrative (per phase)
- Tech stack table (Layer | Technology | Reason)
- Key technical decisions (ID | Decision | Rationale | Status: proposed)
- Technical risks
- Technical assumptions

## Rules

- All decisions marked "proposed" until SA/user confirms.
- SA input via /presale-update always overrides proposed decisions.
- Do not block WBS if user chooses to skip this stage.
- Keep diagrams at presale level — show system boundaries and data flow, not internal class structure.
