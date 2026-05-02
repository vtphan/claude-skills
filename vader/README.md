# VADER — A Five-Role Software Development Loop

A set of nine Claude skills (eight core, one helper) that together implement a disciplined rolling-wave workflow for AI-assisted software projects. The loop maps cleanly to the five roles a thoughtful human lead wants Claude to play: **Vision-shaping, Architecture, Drafting, Execution, and Redrafting** — with two verification gates baked in (audit and architect-review) and a deliberate path for pivots that reach all the way back to the vision. A small `vader-next` helper reads project state and orients you to the next step.

## The idea in one paragraph

Most attempts to use LLMs for software development trip on the same step: the agent does what looks like the right thing, but it does *more* than the plan asked for, or *less* than acceptance demands, or it silently drifts from a structural decision made earlier. Detail-rich plans don't fix this; they just give the agent more rope. VADER fixes it by separating concerns across artifacts and across skills. A short **vision doc** captures intent. An **architecture doc** plus an append-only **ADR log** capture structural choices. A unified **wave doc** carries requirements and plan together, organized one wave at a time. Each wave is built by an executor that does only the current wave, audited by an independent agent that re-derives the answer from the artifacts, reviewed by an architect that decides whether structural choices need to revise, and absorbed by a redrafter that closes the wave and expands the next. The whole loop is invoked by the human; no skill auto-invokes the next.

## The VADER loop

```
                    ┌─────────────────┐
                    │  vision-shaper  │   one-time at project start
                    │   vision doc    │   (revisable later by vision-pivot)
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ architect-draft │   one-time per project
                    │  arch doc + ADRs│   (revisable later by architect-review)
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   wave-draft    │   one-time per project
                    │   wave doc      │   W1 = walking skeleton
                    │   (W1 full,     │   W2+ sketched
                    │    W2+ sketch)  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
              ┌────▶│  wave-execute   │   builds current wave
              │     │ + execution rpt │   produces execution report
              │     └────────┬────────┘
              │              │
              │              ▼
              │     ┌─────────────────┐
              │     │   wave-audit    │   independent verification
              │     │  + audit report │   verdict gates the rest
              │     │ (pass/fail)     │
              │     └────────┬────────┘
              │              │
              │              ▼
              │     ┌─────────────────┐
              │     │ architect-review│   structural revision check
              │     │ + arch-rev rpt  │   proposes ADRs/supersessions
              │     └────────┬────────┘
              │              │
              │              ▼
              │     ┌─────────────────┐
              │     │  wave-redraft   │   closes current wave,
              │     │ ratifies arch,  │   expands next wave,
              │     │ next wave full  │   ratifies ADR proposals
              │     └────────┬────────┘
              │              │
              └──────────────┘
                  (one cycle per wave until project complete)

      ╔══════════════════════════════════════════════╗
      ║ At any cycle: vision-pivot can revise the    ║
      ║ vision doc, triggering a vision-pivot-       ║
      ║ redraft on the next wave-redraft invocation. ║
      ╚══════════════════════════════════════════════╝
```

## The eight skills

The five-letter acronym **VADER** names the main path: Vision → Architect → Draft → Execute → Redraft. Two verification gates and a pivot escape hatch sit alongside.

**Vision (V)**

- **`vision-shaper`** — conversational, sounding-board skill that turns a rough idea into a short, opinionated vision doc. Captures intent: problem, target users, value hypothesis, in-scope, non-goals, success metrics, constraints, prior art, open questions.
- **`vision-pivot`** — revises the vision doc when later-wave learning invalidates a core part of it (the value hypothesis is wrong, the role model is wrong, a non-goal needs retiring). Rare and high-stakes; explicit confirmation required.

**Architect (A)**

- **`architect-draft`** — produces the initial architecture doc and seed ADRs from the vision. Commits the choices that are expensive to revise later (persistence, auth, deployment, key interfaces); leaves everything else for waves to settle.
- **`architect-review`** — runs every cycle, after `wave-audit` and before `wave-redraft`. Reads the wave's reports, decides whether ADRs need supersession or new ADRs need to be drafted, and produces an architect-review report the redrafter consumes. The mechanism for keeping architecture revisable while preserving history.

**Draft (D)**

- **`wave-draft`** — produces the initial wave doc from the vision and architecture. W1 defaults to a walking skeleton — a vertical slice exercising every module. Future waves are sketched as themes; no premature detail.

**Execute (E)**

- **`wave-execute`** — implements the current wave's tasks, flips checkboxes, runs the repro, produces an execution report. Does not modify the wave doc structurally; does not build future-wave work; does not silently violate ADRs.
- **`wave-audit`** — runs as an independent verifier. Re-derives the answer from the artifacts (wave doc, code, repro, ADRs) without trusting the executor's narrative. Produces an audit report with a verdict — `pass`, `pass-with-findings`, or `fail`. The verdict gates everything downstream.

**Redraft (R)**

- **`wave-redraft`** — closes the current wave, ratifies architect-review's ADR proposals, applies architecture body edits, expands exactly one future wave's sketch into full detail, re-sketches remaining waves where required. The skill that absorbs learning. Also handles the cascade when a vision pivot has invalidated downstream artifacts.

**Helper**

- **`vader-next`** — read-only orientation helper. Reads project state from existing artifacts, identifies the next step in the cycle, presents a 4-line summary, and (on confirmation) dispatches the next skill as a fresh subagent. Useful both when you're in-context (quick approve-and-go) and when you're returning to a project after a break (state recap before deciding what to do). Optional; the eight core skills remain individually invocable.

## The artifacts

Three documents per project, plus reports per cycle:

- **`<project>-vision.md`** — the vision doc. One file. Short. Source of truth for intent.
- **`<project>-architecture.md`** — the architecture doc. One file. Source of truth for the system's current shape.
- **`<project>-adr/ADR-NNN-<slug>.md`** — one file per ADR. Append-only log; supersession preserves history.
- **`<project>-wave-doc.md`** — the wave doc. One file. Source of truth for the wave plan, requirements, registers, and project-level history.
- **`<project>-wave-doc.reports/wave-W<N>-execution.md`** — execution report.
- **`<project>-wave-doc.reports/wave-W<N>-audit.md`** — audit report.
- **`<project>-wave-doc.reports/wave-W<N>-architect-review.md`** — architect-review report.

Each cycle produces one of each report. They are append-only artifacts; never edited after they're written.

## Why these specific design choices

### Vision is upstream and revisable

A vision is the cheapest place to be wrong, and the most expensive place to leave wrong. VADER makes the vision a deliberate first artifact, with `vision-shaper` providing a sounding-board conversation rather than a blank-template fill. When learning later invalidates the vision, `vision-pivot` revises it explicitly — and that pivot cascades into the wave doc and (potentially) the architecture, instead of becoming a quiet drift between what the vision says and what the project actually is.

### Architecture is a separate doc with an ADR log

Most projects let architectural decisions stay implicit in the code. That works until a year in, when no one remembers why the auth model is what it is. VADER makes architecture explicit: a thin, *current* picture of the system in the architecture doc, plus a durable *history* of choices in the ADR log. ADRs are append-only; supersession preserves the prior decision. Modules and tasks cite ADRs by ID, so audit can mechanically check that wave 4 doesn't silently violate a commitment made in wave 1.

### Architect-review every cycle

Architecture is allowed to evolve — the user explicitly doesn't know everything at the start. `architect-review` is the deliberate per-cycle pass where structural choices are revisited in light of what the wave just learned. It runs after audit (so it has independent verification of adherence claims) and before redraft (so the redrafter can ratify its proposals atomically). The result is architecture that revises with discipline, not decay.

### Independent audit gate

The executor self-reports have a structural bias: the executor is the one making errors and has no reason to describe them. `wave-audit` runs as a separate skill (ideally a separate agent run with no executor context). It reads the report as a set of claims to verify, runs the repro, re-checks ADR adherence, walks the diff for scope leakage, and produces a verdict. The verdict gates architect-review and redraft.

### Walking skeleton as W1

W1 defaults to a vertical slice that exercises the whole architecture with trivial functional content — "user logs in and sees Hello, &lt;username&gt;." This forces the scariest handoffs (auth, persistence, deployment) into the first wave, when the doc is most flexible. Horizontal foundation W1s ("set up the data layer first") defer integration risk into late waves and are allowed only with explicit justification.

### One wave expanded per redraft

Exactly one future wave — the new current wave — is expanded from sketch to full detail per redraft. Waves beyond it stay as sketches until their turn. This is the invariant most likely to be violated under pressure, because pre-planning wave N+2 feels productive. It isn't; it's speculation that ages into fiction before wave N+1 has taught you anything.

### Pivot reaches all the way back

Some projects discover their vision was wrong. VADER's pivot path doesn't bury that — `vision-pivot` revises the vision doc explicitly, sets it to `pivoted` status, and the next `wave-redraft` produces a `vision-pivot-redraft` change-log entry that reconciles the wave doc to the new vision (including retiring waves whose goals no longer fit). Architecture follows in the next architect-review cycle. The cascade is deliberate, traceable, and the prior state is preserved as history.

### The human invokes every step

No skill auto-invokes the next. Each transition is yours. This is the point — the loop is built around a human lead who delegates each role to the LLM as the moment calls for it, not around an autonomous pipeline that runs on its own.

## How to use

### Starting a new project

1. Invoke **`vision-shaper`** with a rough description of your idea. Iterate conversationally until the vision doc reflects your intent.
2. Invoke **`architect-draft`** with the saved vision doc. Review the architecture doc and seed ADRs; iterate if needed.
3. Invoke **`wave-draft`** with the vision and architecture. Get back a wave doc with W1 fully planned (walking skeleton) and future waves sketched.
4. Review the wave doc. Hand-edit if the draft got something wrong — the skills tolerate hand edits.

### Running each wave cycle

5. Invoke **`wave-execute`** to build the current wave. Produces an execution report.
6. Invoke **`wave-audit`** (ideally as a fresh agent run) to verify independently. Produces an audit report with a verdict.
7. If the verdict is `pass` or `pass-with-findings`, invoke **`architect-review`** to check structural choices against what was learned. Produces an architect-review report.
8. Invoke **`wave-redraft`** to close out the current wave, ratify architect-review's proposals, and expand the next wave.
9. Repeat from step 5 for each wave.

### When the vision was wrong

If somewhere in the cycle you (or an audit, or an architect-review) realize the vision itself is wrong:

10. Invoke **`vision-pivot`** with a description of what specifically is wrong. The skill confirms with you, edits the vision doc, sets it to `pivoted`, and tells you what downstream reconciliation is needed.
11. The next **`wave-redraft`** invocation will produce a `vision-pivot-redraft` that reconciles the wave doc to the new vision.
12. The next **`architect-review`** cycle will reconcile any ADRs the new vision invalidated.

After a complete normal cycle, vision and wave-doc statuses return to `active` / `in_progress`.

## When this is the right tool

- Projects with moderate-to-high uncertainty about users, requirements, or implementation. Rolling-wave pays off when you'll learn things during execution that change the plan.
- AI-assisted solo or small-team development, where you want real discipline without heavyweight process.
- Situations where the human lead wants the LLM to play distinct roles — sounding-board, architect, builder, auditor — at distinct moments, with clear handoffs.
- Multi-agent collaborations, where a shared wave doc is the coordination surface and the audit + architect-review steps preserve trust between agents.
- Projects where traceability matters — regulated contexts, systems with safety implications, or any context where decisions might need to be justified later.

## When it isn't

- Trivial projects — a one-day hack doesn't need this ceremony.
- Well-understood domains where the vision and architecture are already clear — a short PRD plus straightforward execution may be faster.
- Certification-grade reliability contexts (medical devices, safety-critical systems). The approach is audit-friendly but not certification-grade.
- Large parallel teams with many simultaneous workstreams. The approach assumes mostly sequential wave execution.

## Git integration (optional)

VADER ships with a lightweight set of Git conventions in `references/git-conventions.md`. They're optional — every skill works on a project without git — but using them makes the project's history a legible narrative and unlocks cleaner behavior in `wave-audit` and the `vader-next` helper. The conventions cover commit prefixes (`vision:`, `arch:`, `wave:`, `exec:`, `audit:`, `arch-review:`), tags at the natural boundaries (`vision-v<N>`, `arch-v<N>`, `wave-doc-v<N>`, `W<N>-start`, `W<N>-complete`), a co-author trailer for LLM-collaborative commits, and a branch pattern for vision pivots. Skills *suggest* commit messages in their handoff sections; the human runs the actual commands.

## Files in this folder

```
vader/
├── README.md                       (this file)
├── references/
│   ├── vision-schema.md            vision-doc contract
│   ├── architecture-schema.md      architecture-doc + ADR contract
│   ├── wave-schema.md              wave-doc + reports contract
│   └── git-conventions.md          optional Git integration conventions
├── vision-shaper/
│   ├── SKILL.md
│   └── references/                 (mirrored)
├── vision-pivot/
│   ├── SKILL.md
│   └── references/
├── architect-draft/
│   ├── SKILL.md
│   └── references/
├── architect-review/
│   ├── SKILL.md
│   └── references/
├── wave-draft/
│   ├── SKILL.md
│   └── references/
├── wave-execute/
│   ├── SKILL.md
│   └── references/
├── wave-audit/
│   ├── SKILL.md
│   └── references/
├── wave-redraft/
│   ├── SKILL.md
│   └── references/
└── vader-next/                     (helper — read-only orientation + dispatch)
    ├── SKILL.md
    └── references/
```

Each `SKILL.md` carries the judgment calls that shape good use of the skill — the schemas define format, the SKILL describes good taste. Start with the schemas to understand the artifacts' shape; then read the individual SKILL.md files when you're about to invoke the corresponding step.

## Related work

The sibling folder `../waves/` contains a four-skill phase-plan pipeline that splits requirements and plan into separate documents and has no architecture or audit steps. The sibling folder `../dear/` contains a four-skill loop (Draft → Execute → Audit → Redraft) that unifies requirements and plan into a single wave doc and adds an audit gate. VADER extends DEAR with three new pieces:

- A **vision** stage upstream (separating intent from requirements + plan).
- A **dedicated architecture artifact** (separate doc + ADR log) instead of an inline commitments register.
- A **per-cycle architect-review** step that catches drift when it happens, not opportunistically.
- A **vision-pivot** mechanism that lets pivots reach all the way back to the project's intent, not just the wave plan.

VADER, DEAR, and Waves all preserve the same core idea: rolling-wave development with append-only history and structural invariants that make discipline mechanical rather than aspirational. Use whichever fits your project's needs.
