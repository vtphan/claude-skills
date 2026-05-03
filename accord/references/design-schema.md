# ACCORD Design Contract

`design` codesigns architecture, UI/UX, and consequential decisions with the human lead. Draft rounds carry proposed thinking. Canonical `design.md` is accepted by human approval.

## Posture

The agent's posture is **elicitive and generative** (same as intent). For design, this especially applies to:

- architectural alternatives and tradeoffs
- dependency and platform choices
- boundary and ownership reframings
- **UI/UX**: interaction model, information architecture, accessibility, error/empty/loading states. The agent proposes these rather than waiting to be asked. UI/UX is part of design, not an afterthought.

Brainstorm-this discipline applies. See `draft-conventions.md`.

## Draft Rounds

Use one monotonic draft sequence in `docs/accord/design/`:

```
draft_00.md
draft_01.md
design.md
draft_02.md
```

Drafts are never overwritten. Re-invoking `design` mid-project should seed the next draft from the current canonical `design.md`, `accord-state.md`, recent plan/review history, execution reports, and current implementation.

`Consider This` uses three-tag convention: `[from user]`, `[Q from LLM]`, `[suggestion from LLM]`.

## Minimum Canonical Contract

`design.md` must include:

```
## Architecture Summary
## Boundaries and Ownership
## Key Interfaces
## Data and State
## User Experience
## Project Commands
## Verification Expectations
## Decisions
## Handoff to Plan
```

`User Experience` covers interaction model, information architecture, accessibility expectations, and error/empty/loading states. Use `n/a` with a reason if the project has no user-facing surface.

`Project Commands` may be a short pointer to `docs/accord/commands.md`. Prefer `commands.md` for concrete commands so routine drift does not force a new `design.md` version.

`design.md` must be self-sufficient for cross-LLM handoff (principle 9). A future agent reviewing or extending the design without conversational context should be able to verify implementation against this artifact alone.

## Decision Entries

Human approval of canonical `design.md` makes listed decisions accepted by default.

Minimum decision entry:

```
### D-001: <decision title>
Decision:
Rationale:
Consequences:
Revisability:
```

Scale up when needed: `Status:`, `Supersedes:`, `Superseded by:`, `Evidence:`.

Use decision entries only for choices that constrain planning or execution. Do not create records for tactical choices that are cheap to reverse.

## Scale Up When

- architecture choices are expensive to reverse
- dependencies introduce lock-in, cost, security, or operational burden
- state ownership is unclear
- persistence, migration, auth, privacy, or deployment are involved
- module boundaries are unclear
- UI/UX must support accessibility, multiple device classes, or specific quality bars
- mid-project implementation invalidates prior design decisions

## Human Decision Points

- durable architecture tradeoffs
- dependency choices with meaningful consequences
- data model commitments
- deployment model
- security posture
- accepted risks or debt
- UI/UX commitments that durably constrain interaction

## LLM Discretion Zone

- conventional file layout
- local naming
- routine test structure
- implementation conventions
- obvious adapter or glue patterns
- internal-only UI affordances that don't constrain users

## Promotion

On approval:

- promote the approved draft into `docs/accord/design/design.md`
- update `docs/accord/accord-state.md` with source draft and tag
- create or update `docs/accord/commands.md` when concrete commands are known
- commit explicit paths
- tag `accord-design-v<N>`
