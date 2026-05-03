# VADER — A Lightweight Rolling-Wave Loop for Solo Human + LLM Software Projects

A set of five Claude skills that together implement a disciplined but lightweight rolling-wave workflow for AI-assisted software projects. The loop is designed for one human lead working with an LLM coding agent on small to medium projects. It keeps the safeguards that matter most — clear intent, explicit architecture, visible tradeoffs, acceptance checks, review before plan mutation, controlled scope — and removes the ceremony a solo project is unlikely to sustain.

## The idea in one paragraph

Most attempts to use LLMs for software development trip on the same step: the agent does what looks like the right thing, but it does *more* than the plan asked for, *less* than acceptance demands, or it silently drifts from a structural decision made earlier. Detail-rich plans don't fix this; they just give the agent more rope. VADER fixes it by separating concerns across artifacts and across skills. A short **vision doc** captures intent. A single **architecture doc** with an embedded Decision Log captures structural choices. A unified **wave plan** carries requirements and plan together, organized one wave at a time. Each wave is built by an executor that does only the current wave; then a `wave-update` skill spawns a fresh-context review subagent that re-derives the answer from the artifacts, surfaces findings to the human for approval, applies any architectural changes, closes the current wave, and expands the next. The whole loop is invoked by the human; no skill auto-invokes the next.

## The VADER loop

```
                    ┌─────────────────┐
                    │     vision      │   one-time at project start
                    │  (draft mode)   │   (revisable later via pivot mode)
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    architect    │   one-time per project
                    │  (draft, then   │   (mid-cycle changes via wave-update)
                    │  ratify modes)  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    wave-plan    │   one-time per project
                    │  (W1 walking    │   W1 fully planned;
                    │   skeleton)     │   W2+ sketched
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
              ┌────▶│  wave-execute   │   builds current wave;
              │     │ + execution rpt │   produces execution report
              │     └────────┬────────┘
              │              │
              │              ▼
              │     ┌─────────────────┐
              │     │   wave-update   │   spawns review subagent;
              │     │ (review +       │   presents findings to human;
              │     │  apply changes  │   applies approved changes;
              │     │  + expand next) │   closes current wave; expands next
              │     └────────┬────────┘
              │              │
              └──────────────┘
                  (one cycle per wave until project complete)

      ╔══════════════════════════════════════════════╗
      ║ At any cycle: `vision pivot` mode can revise ║
      ║ the vision, triggering a vision-pivot-update ║
      ║ on the next wave-update invocation.          ║
      ╚══════════════════════════════════════════════╝
```

## The five skills

**`vision`** (modes: draft, pivot)
- *draft mode* — produces the initial vision doc through a sounding-board conversation. Captures intent: problem, target users, value hypothesis, in-scope, non-goals, success metrics, constraints, prior art, open questions, optional core journeys.
- *pivot mode* — revises the vision when later-wave learning invalidates a core part of it. Rare; explicit confirmation required.

**`architect`** (modes: draft, ratify)
- *draft mode* — produces the initial architecture doc with embedded Decision Log entries (status `Proposed`). Cites the vision throughout.
- *ratify mode* — flips Proposed seed entries to Accepted after human review. Then `architect` is essentially idle for the rest of the project; mid-cycle architectural change goes through `wave-update`.

**`wave-plan`**
- One-time. Produces the wave plan from the vision and architecture. W1 defaults to a walking skeleton that exercises every module. Future waves are sketched as themes; no premature detail. Refuses to run if any cited Decision Log entry is still Proposed.

**`wave-execute`**
- Per wave. Implements the current wave's tasks, flips checkboxes, runs the repro, produces an execution report. Does not modify the wave plan structurally; does not build future-wave work; does not silently violate Decision Log entries. Captures `wave_start_ref` and `wave_end_ref` (when git is in use) for the review subagent's diff scoping.

**`wave-update`**
- Per wave. The cycle's hub. Spawns a fresh-context review subagent that re-derives findings from the artifacts (wave plan, execution report, architecture, code, repro). Presents findings interactively to the human for approval. Applies approved changes: closes the current wave, ratifies any new/superseded Decision Log entries inline, applies architecture body edits, expands the next wave's sketch into full detail. Saves wave plan and architecture atomically. Findings live in the change-log entry of the wave plan — no separate review report.

## The artifacts

Three primary documents per project, plus one report per wave:

- **`docs/<project>-vision.md`** — the vision doc. One file. Short.
- **`docs/<project>-architecture.md`** — the architecture doc, including the embedded `## 8. Decision Log` section.
- **`docs/<project>-wave-plan.md`** — the wave plan.
- **`docs/<project>-wave-plan.reports/wave-W<N>-execution.md`** — execution report (one per wave).

Optional, when the project earns it:

- **`docs/<project>-adr/ADR-NNN-<slug>.md`** — promoted Decision Log entries (split out of the architecture doc when the project has many decisions, frequent supersession, or extensive cross-references). Promotion preserves IDs.

## Why these specific design choices

### Vision is upstream and revisable

The vision is the cheapest place to be wrong, and the most expensive place to leave wrong. VADER makes it a deliberate first artifact. The `vision` skill's draft mode is a sounding-board conversation; pivot mode revises explicitly when learning invalidates the vision, with cascading reconciliation handled by the next `wave-update`.

### Architecture is one explicit document

The architecture doc describes how the system is built; the embedded Decision Log captures structural choices with rationale. ADRs are entries by default — entries live next to the architecture they govern. Separate ADR files are *optional*, adopted when the project earns the separation (typically: more than ~7 entries, or supersession history grows). Promotion preserves IDs; nothing breaks.

### Propose-then-ratify gate for initial architecture

Initial Decision Log entries from `architect draft` start as `Proposed`. They become `Accepted` only when the human ratifies — by re-invoking `architect ratify`, or by manually flipping each `Status` field. This gives the human lead an explicit moment of architectural signoff before wave planning starts. `wave-plan` and `wave-execute` refuse to run while any cited entry is Proposed.

### Walking skeleton as W1

W1 defaults to a vertical slice that exercises the whole architecture with trivial functional content. This forces the scariest handoffs (auth, persistence, deployment) into the first wave, when the plan is still flexible.

### Independent review by fresh-context subagent

`wave-update` spawns a fresh subagent to do the review, with isolated context — it reads only the committed artifacts, not the executor's reasoning or `wave-update`'s own conversation. The subagent re-derives findings; the executor's report is one input, not the truth. This preserves audit independence within a single skill, without requiring a separate review skill.

### Findings absorb into the change log, not a separate report

The change-log entry of the wave plan captures both the audit verdict and the absorbed findings/decisions. There's no separate review report — the change log is rich enough, and one fewer artifact per cycle is one less thing to maintain.

### Pivots reach all the way back

When `vision pivot` revises the vision, the next `wave-update` produces a `vision-pivot-update` change-log entry that reconciles the wave plan, retires affected waves, and (in the same invocation) supersedes any Decision Log entries that conflict with the new vision. Pivot status is cleared by the next successful execute → update cycle.

### The human invokes every step

No skill auto-invokes the next. Each transition is yours.

## How to use

### Starting a new project

1. Invoke **`vision`** (draft mode) with a rough description of your idea. Iterate conversationally until the vision reflects your intent.
2. Invoke **`architect`** (draft mode) with the saved vision. Review the architecture doc and proposed Decision Log entries.
3. Invoke **`architect`** (ratify mode) to flip Proposed entries to Accepted (or manually edit each Status).
4. Invoke **`wave-plan`** with the vision and architecture. Get back a wave plan with W1 fully planned (walking skeleton) and future waves sketched.
5. Review the wave plan. Hand-edit if the draft got something wrong.

### Running each wave cycle

6. Invoke **`wave-execute`** to build the current wave. Produces an execution report.
7. Invoke **`wave-update`**. The skill spawns a review subagent, presents findings to you, applies your approved changes, closes the current wave, and expands the next wave. The wave plan (and architecture, if applicable) are saved atomically.
8. Repeat from step 6 for each wave.

### When the vision was wrong

If somewhere in the cycle you realize the vision itself is wrong:

9. Invoke **`vision`** in pivot mode with a description of what specifically is wrong. The skill confirms with you, edits the vision, sets it to `pivoted`, and tells you what downstream reconciliation is needed.
10. The next **`wave-update`** invocation will produce a `vision-pivot-update` that reconciles the wave plan and (in the same invocation) supersedes any architecture entries the new vision invalidated.
11. After a complete normal cycle, vision and wave-plan statuses return to `active` / `in_progress`.

## Git integration (optional)

VADER ships with a lightweight set of Git conventions in `references/git-conventions.md`. They're optional — every skill works on a project without git — but using them makes the project's history a legible narrative and unlocks cleaner behavior in `wave-update`'s review subagent. The conventions cover commit prefixes (`vision:`, `arch:`, `wave:`, `exec:`), tags at the natural boundaries (`vision-v<N>`, `arch-v<N>`, `wave-plan-v<N>`, `W<N>-start`, `W<N>-complete`), a co-author trailer for LLM-collaborative commits, and a branch pattern for vision pivots.

**Skills run `git commit` and `git tag` themselves after the human approves the artifact.** The human's checkpoint is the explicit approval before save, which the skill's interactive flow already enforces; the commit is the durable record of what was approved. If the human disagrees with a resulting commit, override is straightforward: `git reset --soft HEAD~1` to unstage, amend or recompose, commit again. If a tag name already exists (e.g., a previous run set it), the skill warns rather than silently overwriting.

## When this is the right tool

- Solo human lead working with an LLM on small to medium software projects.
- Projects with moderate-to-high uncertainty about users, requirements, or implementation. Rolling-wave pays off when you'll learn things during execution that change the plan.
- Situations where the human owns judgment, taste, product direction, and architectural tradeoffs, while the LLM drafts, implements, verifies, and summarizes quickly.
- Projects where you want real discipline (acceptance criteria, append-only history, walking skeleton, scope control) without heavyweight process.

## When it isn't

- Trivial projects — a one-day hack doesn't need this ceremony.
- Well-understood domains where the vision and architecture are already crisp — a short PRD plus straightforward execution may be faster.
- Multi-agent or team coordination contexts where independent audit artifacts and stronger separation between roles are central risks (the discipline can be extended for those, but VADER is shaped for solo).
- Certification-grade reliability contexts (medical devices, safety-critical systems). The approach is audit-friendly but not certification-grade.

## Files in this folder

```
vader/
├── README.md                       (this file)
├── references/
│   ├── vision-schema.md            vision-doc contract
│   ├── architecture-schema.md      architecture-doc + Decision Log contract
│   ├── wave-schema.md              wave-plan + execution-report contract
│   └── git-conventions.md          optional Git integration conventions
├── vision/
│   └── SKILL.md                    modes: draft, pivot
├── architect/
│   └── SKILL.md                    modes: draft, ratify
├── wave-plan/
│   └── SKILL.md                    one-time
├── wave-execute/
│   └── SKILL.md                    per wave
└── wave-update/
    └── SKILL.md                    per wave; spawns review subagent
```

Each `SKILL.md` carries the judgment calls that shape good use of the skill — the schemas define format, the SKILL describes good taste. Skills read from the canonical `../references/` directory directly; per-skill mirrors are not used.

## Related work

The sibling folder `../waves/` contains an earlier four-skill phase-plan pipeline that splits requirements and plan into separate documents. The sibling folder `../dear/` contains a four-skill loop (Draft → Execute → Audit → Redraft) that unifies requirements and plan into a single wave doc. VADER is the latest iteration: vision-first, explicit architecture with embedded Decision Log, walking-skeleton W1, fresh-context review inside `wave-update`, propose-then-ratify gate for initial architecture, optional Git integration, and a deliberate pivot path back to the vision. It is shaped specifically for solo human + LLM work — proportional, not exhaustive.
