# ACCORD Design Contract

`design` codesigns architecture and consequential decisions with the human lead. Draft rounds carry proposed thinking. Canonical `design.md` is accepted by human approval.

## Draft Rounds

Use one monotonic draft sequence in `docs/accord/design/`:

```text
draft_00.md
draft_01.md
design.md
draft_02.md
```

Drafts are never overwritten. A draft after `design.md` is a proposed revision. Re-invoking `design` after implementation should seed the next draft from the current canonical `design.md`, `accord-state.md`, recent plan/review history, execution reports, and current implementation.

## Minimum Canonical Contract

`design.md` must include:

```text
## Architecture Summary
## Boundaries and Ownership
## Key Interfaces
## Data and State
## Project Commands
## Verification Expectations
## Decisions
## Handoff to Plan
```

## Decision Entries

Human approval of canonical `design.md` makes listed decisions accepted by default. Do not require a separate ratify mode.

Minimum decision entry:

```text
### D-001: <decision title>
Decision:
Rationale:
Consequences:
Revisability:
```

Scale up a decision entry when needed:

```text
Status:
Supersedes:
Superseded by:
Evidence:
```

Use decision entries only for choices that constrain planning or execution. Do not create records for tactical choices that are cheap to reverse.

## Scale Up When

- architecture choices are expensive to reverse
- dependencies introduce lock-in, cost, security, or operational burden
- state ownership is unclear
- persistence, migration, auth, privacy, or deployment are involved
- module boundaries are unclear
- brownfield code conflicts with proposed design
- implementation learning invalidates prior design decisions

## Human Decision Points

- durable architecture tradeoffs
- dependency choices with meaningful consequences
- data model commitments
- deployment model
- security posture
- accepted risks or debt

## LLM Discretion Zone

- conventional file layout
- local naming
- routine test structure
- implementation conventions
- obvious adapter or glue patterns

## Preserve From VADER

- brownfield orientation before architecture drafting
- explicit project commands
- durable decision records for consequential decisions
- consequences, including negative consequences, for material decisions
- refusal to over-commit to cheap-to-reverse implementation details
- clear separation between architecture decisions and code

## Promotion

On approval:

- promote the approved draft into `docs/accord/design/design.md`
- do not include a canonical change log
- update `docs/accord/accord-state.md` with source draft and tag
- commit explicit paths
- tag `accord-design-v<N>`
