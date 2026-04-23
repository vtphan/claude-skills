# DEAR — Rolling-Wave Skills for AI-Assisted Development

A set of four Claude skills that together implement a disciplined rolling-wave workflow for AI-assisted software projects. Each wave ends with an independent audit gate, so the spec and the plan stay honest as the project learns.

## The idea in one paragraph

Traditional development treats specification and implementation as separate phases — you write a full PRD, then build against it. That works when you already know your users and your tech. When you don't, most of the PRD is speculation; you learn the real requirements during implementation, and the written spec drifts from reality. This approach unifies requirements and plan into a single **wave doc**, organized wave by wave. The current wave is specified and planned in full; future waves are sketched as themes. Between waves, execution produces a report, an independent audit verifies the claims, and a redraft absorbs the learnings into the next wave. The loop — **D**raft → **E**xecute → **A**udit → **R**edraft — is how the doc stays honest across cycles instead of drifting into fiction.

## The DEAR loop

```
                          ┌─────────────────┐
                          │   brief / spec  │
                          └────────┬────────┘
                                   │
                                   ▼
                          ┌─────────────────┐
                          │   wave-draft    │   (D)  one-time per project
                          │   walking       │
                          │   skeleton W1   │
                          └────────┬────────┘
                                   │
                                   ▼
                          ┌─────────────────┐
                    ┌────▶│  wave-execute   │   (E)  builds current wave,
                    │     │   + execution   │        writes execution report
                    │     │     report      │
                    │     └────────┬────────┘
                    │              │
                    │              ▼
                    │     ┌─────────────────┐
                    │     │   wave-audit    │   (A)  independent verifier,
                    │     │  + audit report │        gates closeout
                    │     │  (pass/fail)    │
                    │     └────────┬────────┘
                    │              │
                    │              ▼
                    │     ┌─────────────────┐
                    │     │  wave-redraft   │   (R)  closes current wave,
                    │     │  next wave now  │        expands next from sketch
                    │     │     current     │        to full detail
                    │     └────────┬────────┘
                    │              │
                    └──────────────┘
                       (one cycle per wave until project complete)
```

The four skills:

- **`wave-draft`** takes a brief or vision doc and produces the initial unified wave doc. W1 defaults to a **walking skeleton** — a thin vertical slice that instantiates the whole architecture. Future waves are sketched as themes.
- **`wave-execute`** reads the wave doc, implements the current wave's tasks, and produces an execution report. Flips task checkboxes. Writes code; everything else in the doc is off-limits.
- **`wave-audit`** runs as an independent verifier. Reads the plan and the report, runs the repro, re-verifies exit criteria, checks that architectural commitments weren't silently violated, and issues a verdict: `pass`, `pass-with-findings`, or `fail`.
- **`wave-redraft`** reads the wave doc plus both reports, closes the current wave, expands exactly one future wave's sketch into full detail, and appends a change-log entry. This is the skill that absorbs learning.

## The wave doc

A single markdown file per project, `<project-slug>-wave-doc.md`. Requirements and plan live in the same file, organized by wave. The structure makes rolling-wave discipline physical:

- **Current wave** carries full detail — stories with acceptance, features, plan tasks with acceptance, exit criteria, a repro path, architectural commitments it respects or establishes.
- **Future waves** carry only sketches — theme, candidate story titles (no acceptance criteria), anticipated features (no definitions), sketched entry/exit criteria, 2–4 sentence approach sketch.
- **Past waves** carry compact closeout summaries — what was delivered, which assumptions resolved, which commitments established, links to archived reports.

Three registers give the doc its memory:

- **Assumptions** — beliefs about the world we're choosing to proceed with. Closed out via validation during execution.
- **Risks** — things that could go wrong even if assumptions hold. Closed out via materialization or retirement.
- **Architectural commitments** — decisions about *how* the system is built. Rationale mandatory. Supersession preserves history.

All three registers are append-only. Broken assumptions and superseded commitments are never deleted; they stay as the trail of what we once believed and why the doc looks the way it does.

The full format, including all invariants, lives in [`references/wave-schema.md`](references/wave-schema.md).

## Why these specific design choices

### Walking skeleton as W1

W1 defaults to a vertical slice that exercises the whole architecture with trivial functional content — "user logs in and sees Hello, <username>." This forces the scariest handoffs (auth, persistence, deployment, interface) into the first wave, when the doc is still flexible. A horizontal foundation W1 ("set up the data layer") defers integration risk into late waves and is allowed only with explicit justification.

### Architectural commitments as a first-class register

Most methodologies leave architectural decisions implicit in the code. Here they are named, IDed, cited by waves that respect them, and superseded explicitly when learning makes them wrong. This lets the audit skill mechanically check that wave 4 doesn't silently violate a commitment made in wave 1.

### Audit as a separate skill

Executor self-reports have a structural bias: the executor is the one making the errors and has no reason to describe them. The audit skill reads the report as a set of claims to be verified, not a narrative to be accepted. It runs the repro, re-verifies exit criteria, cross-references the diff against the plan, and produces a verdict that gates redraft closeout. For real independence, invoke the audit as a separate agent run.

### One wave expanded per redraft

Exactly one future wave — the new current wave — is expanded from sketch to full detail each redraft cycle. Waves beyond it stay as sketches until their turn. This is the invariant most likely to be violated under pressure, because pre-planning wave N+2 feels productive. It isn't; it's speculation that ages into fiction before wave N+1 has taught you anything.

### Repro paths are mandatory

Every wave ships a script (e.g., `scripts/demo-w2.sh`) that exercises the wave's exit criteria from a clean state. The audit runs it. Later waves run it as a regression check. Without a repro, "the wave works" becomes a matter of the reader's faith in the writer.

## How to use

Starting a new project:

1. Write a brief — a one-pager naming the goal, non-goals, roles, and any hard constraints. Short is fine.
2. Invoke **`wave-draft`** with the brief. Get back a wave doc with W1 fully planned (walking skeleton) and future waves sketched.
3. Review the wave doc. Hand-edit if the draft got something wrong — the skills tolerate hand edits.

Running each wave cycle:

1. Invoke **`wave-execute`** to build the current wave. It writes code, runs tests, flips task checkboxes, and produces an execution report.
2. Invoke **`wave-audit`** (ideally as a fresh agent run) to verify independently. It produces an audit report with a verdict.
3. If the verdict is `pass` or `pass-with-findings`, invoke **`wave-redraft`** to close out the current wave and expand the next. The doc advances.
4. If the verdict is `fail`, either loop back to `wave-execute` to address the findings, or renegotiate scope explicitly via `wave-redraft` with user agreement (this becomes a conspicuous change-log entry).

Repeat until the wave ladder is complete. Each wave ends with more signal than it started with.

## When this is the right tool

- Projects with moderate-to-high uncertainty about users, requirements, or implementation. Rolling-wave pays off when you'll learn things during execution that change the plan.
- AI-assisted solo or small-team development, where you want real discipline without heavyweight process.
- Situations where traceability matters — regulated contexts, systems with safety implications, teams that need to justify decisions later.
- Multi-agent collaborations, where a shared wave doc is the coordination surface and the audit step preserves trust.

## When it isn't

- Trivial projects — a one-day hack doesn't need this ceremony; the overhead outweighs the benefit.
- Well-understood domains where the full spec and architecture are already clear — a short PRD plus straightforward execution may be faster.
- Certification-grade reliability contexts (medical devices, safety-critical systems). The approach is audit-friendly but not certification-grade; you'd layer formal verification, external QA, and change control on top.
- Large parallel teams with many simultaneous workstreams. The approach assumes mostly sequential wave execution.

## Files in this folder

```
dear/
├── README.md                       (this file)
├── references/
│   └── wave-schema.md              canonical schema — the contract
├── wave-draft/
│   ├── SKILL.md
│   └── references/wave-schema.md   (mirrored copy)
├── wave-execute/
│   ├── SKILL.md
│   └── references/wave-schema.md
├── wave-audit/
│   ├── SKILL.md
│   └── references/wave-schema.md
└── wave-redraft/
    ├── SKILL.md
    └── references/wave-schema.md
```

Each `SKILL.md` carries the judgment calls that shape good use of the skill — the schema defines format, the SKILL describes good taste. Start with the schema to understand the wave doc's shape; then read the individual SKILL.md files when you're about to invoke the corresponding step.

## Related

The sibling folder `../waves/` contains an earlier "phase-plan" pipeline — a rolling-wave *plan* skill set that reads a separately-produced requirements document. That pipeline is preserved for comparison; the DEAR approach here unifies the spec and plan into one evolving document and adds the audit gate. Use whichever matches your project's needs.
