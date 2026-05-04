# ACCORD

ACCORD is a lightweight process for a human lead and a capable LLM to develop a greenfield software project together. It surfaces design judgment at the moments where bad design tends to creep in — vague intent, weak architecture, debt-prone plans, drifting execution — and stays out of the way otherwise.

ACCORD pays its cost up front to prevent debt that compounds downstream: intent drift, architectural contradiction, acceptance creep, sycophantic refinement, and the same-session blindness that lets a model feel confident about code that doesn't do what was intended. Every principle below targets a specific class of debt. The bet is that catching these during `intent`, in `design`'s critique pass, or at a fresh-context review is cheaper than catching them in the fourth feature — when the cost shows up as rework, not as a bug you can point to.

## Quick Start For Human Leads

Use ACCORD in a new git-backed project. Invoke each skill manually; the skills do not auto-run the next phase.

1. Start with `accord intent` and describe the project you want to build.
2. Review the intent draft, push back where needed, then approve promotion to `docs/accord/intent.md`.
3. Invoke `accord design`, review the architecture and UX decisions, then approve promotion to `docs/accord/design.md`.
4. Invoke `accord plan`; the agent will choose a plan shape, explain why it fits the design, and define the next approved unit.
5. Invoke `accord execute` to implement the approved unit.
6. Invoke `accord review-update` after execution. Use a fresh conversation when the plan says `Review mode: fresh-required`.
7. At each gate, approve, reject, or ask for changes. The agent will say whether the approval is consequential or procedural.

The human lead's job is to supply direction, answer consequential questions, push back on drafts or plans that do not match the project, and approve phase boundaries. The agent's job is to maintain the ACCORD artifacts, make routine process choices, implement approved work, verify it, and preserve handoff through git commits and tags.

| Invoke | What It Produces | Human Action |
| --- | --- | --- |
| `accord intent` | `intent-draft.md`, then `intent.md` | Decide whether the project goal, users, success criteria, non-goals, and constraints are right. |
| `accord design` | `design-draft.md`, `design.md`, usually `commands.md` | Decide whether architecture, boundaries, UX, dependencies, and verification strategy are acceptable. |
| `accord plan` | `plan-draft.md`, then `plan.md` with a current approved unit | Approve the unit scope, acceptance criteria, verification, and review mode. |
| `accord execute` | Code changes and `reports/exec-<unit-id>.md` | Approve the implementation result or request revisions before commit/tag. |
| `accord review-update` | Review log updates in `plan.md`, state updates, next unit or recovery | Accept the verdict, approve recovery if needed, or route back to plan/design/intent. |

The detailed artifact contracts live in `references/`. A human lead normally does not need to read them unless debugging the process or changing ACCORD itself.

## Principles

1. **Five ACCORD skills.** The framework comprises exactly five skills: `intent`, `design`, `plan`, `execute`, `review-update`. ACCORD itself does not grow additional skills, and depends on nothing outside this directory. Users remain free to invoke unrelated tools alongside ACCORD; the principle bounds ACCORD's surface, not the user's toolkit.
2. **Codesign discipline.** `intent` and `design` use a strict codesign discipline: a single self-contained draft file overwritten freely, a Draft Stance block declaring the agent's posture, default away from `refine`, required critique pass before declaring `ready`, and explicit naming of any framing change. The discipline protects against premature consensus and sycophantic refinement; it is fully described in `references/draft-conventions.md`.
3. **Greenfield only.** ACCORD assumes the project starts under ACCORD. There is no brownfield adoption path.
4. **Auto-git.** Approved phase boundaries become commits and lightweight tags. Git history is the framework's durable state; without it, recovery loses its baseline and cross-conversation handoff loses its anchor.
5. **The agent is capable.** ACCORD does not micromanage the LLM. Schemas protect handoff between phases; they do not script the LLM's thinking inside a phase. Over-scripting produces compliance theater rather than judgment.
6. **Approval gates are real but advised.** The agent always seeks approval at phase boundaries. With each request, it advises whether the approval is consequential (real choice for the human) or procedural (rubber stamp). This concentrates human attention where it counts and prevents approval theater.
7. **Quality over protocol.** ACCORD exists to prevent bad design — debt, redundancy, contradiction. Every constraint should serve that goal; trim anything that doesn't.
8. **Two modes.** Codesign mode (`intent`, `design`) is human-and-agent iterating together. Agent-led mode (`plan`, `execute`, `review-update`) is the agent leading with the human approving at gates.
9. **Cross-LLM, cross-conversation handoff.** Any skill — most often `review-update` — may be invoked in a fresh conversation, with a different LLM. ACCORD's artifacts must be sufficient for this without conversational context. Concretely: `intent.md` conveys project direction; `design.md` conveys architecture and UX; `plan.md`'s acceptance criteria for the current unit are checkable against a diff; execution reports use concrete pointers (file paths, function names, test names) rather than vague claims; `commands.md` is re-runnable; `accord-state.md` says what happened and what runs next; commits and tags reflect phase boundaries. This is the quality bar for every artifact the framework produces. Other files reference principle 9 rather than restating it. The debt this prevents is context death — work that becomes unrecoverable when the original conversation ends or a different model picks it up.

## Modes

### Codesign mode — `intent` and `design`

The human lead and the agent build the project's intent and design together via the codesign draft. The agent's posture is **elicitive and generative** — drawing out aspects the human hasn't yet articulated, and proposing transformative alternatives the human can react to, redirect, or reject. This applies especially to UI/UX, which is part of design: the agent proposes interaction models, information architecture, and accessibility considerations rather than waiting to be asked. The discipline (Draft Stance block, default away from `refine`, required critique pass before declaring `ready`, framing changes named explicitly) keeps this from sliding into sycophantic refinement or premature consensus. The approved draft is promoted to a clean canonical artifact (`intent.md`, `design.md`).

This is where the human's mental model of the project gets built and tested. Approval gates here are usually consequential.

### Agent-led mode — `plan`, `execute`, `review-update`

After design is approved, the agent leads. It plans, builds, verifies, and recovers from its own mistakes informed by the approved intent and design. The human reviews the agent's reasoning at gates. Approval gates here are usually procedural — the agent advises when one is consequential.

`plan` uses the same single-draft-file mechanism as intent and design, but with a lighter discipline: the default is one iteration. The agent produces `plan-draft.md`, the human approves, it becomes `plan.md`. Iteration happens only when the human pushes back.

In `plan`, the agent must inform the human *why* the chosen plan shape fits *this* design and scope. Generic shape justifications are insufficient; the rationale must reference the specific design artifact.

`review-update` is typically invoked in a fresh conversation, often with a different LLM, so the review reads the executed work cold against the committed artifacts. The execution report, the unit's acceptance criteria in `plan.md`, the design decisions in `design.md`, and the diff under review must together be sufficient for an unfamiliar agent to issue a verdict without asking the executor for context.

## Skills

- `intent` — codesign project intent. Iterate the single draft under codesign discipline, then promote to `intent.md`.
- `design` — codesign architecture and consequential decisions. Iterate the single draft under codesign discipline, then promote to `design.md`.
- `plan` — agent-led planning. The agent picks the plan shape, explains why it fits the design, defines the next approved unit, and informs the human. Lightweight drafts.
- `execute` — agent-led implementation of the approved unit. Writes code and an execution report.
- `review-update` — fresh-context verification, typically in a new conversation and possibly with a different LLM. Reads the executed work against artifacts, issues a verdict, decides recovery direction, and advances `plan.md` and state.

The human lead invokes each skill manually. Skills do not auto-invoke the next skill. Continuity comes from canonical artifacts, `accord-state.md`, commits, and tags.

## Lifecycle

### Bootstrap (greenfield setup)

A new project runs the full Path once:

```
intent → design → plan → execute → review-update
```

Each phase ends with an approved canonical artifact, a commit, and a tag.

### The plan-execute-review loop

After bootstrap, ongoing work lives in a loop. The agent prepares or advances the next unit in `plan.md`, the human approves it, the agent executes it, and `review-update` either advances the next approval or enters recovery:

```
plan → execute → review-update
       ↑                     ↓
       └─── approve next ────┘
```

Adding a new unit that fits the existing approved plan does not re-run intent or design. The agent proposes the unit in `plan.md`; the human approves; execution proceeds.

### Re-entry at intent for new features or revisions

When the human lead wants to add a new feature or revise an existing one, re-invoke `intent`. The agent produces a draft to test whether intent has actually shifted:

- **If intent still holds**, the draft closes quickly with stance `ready` and no substantive change; canonical `intent.md` stays as-is and the work moves to `design`.
- **If intent has shifted**, real codesign happens; an updated `intent.md` is promoted and tagged.

The same pattern applies to `design`. The work eventually lands at `plan`, which produces a new plan draft incorporating the feature or revision.

Every feature addition or revision is *checked* against intent and design before reaching execution. Most checks converge fast; the discipline catches the cases where a change quietly shifts the project's direction. Skipping the check is what produces contradiction and debt over time.

#### Within-plan unit vs. feature re-entry — how to tell

The agent advises which of the following applies; the human can disagree.

- **Within-plan unit.** The work fits the approved intent (no change to goal, users, success criteria, non-goals, constraints, or quality bar) AND the approved design (no change to architecture, boundaries, dependencies, deployment, security, or UX commitments). Examples: implementing the next anticipated unit; fixing a bug in code under the approved unit; adding tests for already-approved behavior; refining a UI detail that doesn't change a UX commitment. Route: skip intent and design re-entry; the agent proposes the unit in `plan.md`.
- **Feature addition or revision (re-enter at `intent`).** The work expands or changes intent: new users, new success criteria, new constraints, weakened non-goals, or a goal that grows beyond what `intent.md` says.
- **Design revision (re-enter at `design`).** The work doesn't change goal but does change architecture, boundaries, ownership, dependencies, deployment, security, or UX commitments. Often the agent reaches this conclusion *after* the intent draft closes with stance `ready` and no substantive change.

When in doubt, re-enter at `intent`. Closing a draft with no change is cheap; missing a real intent shift is not.

### Recovery — `repair`, `redo`, `replan`

When `review-update` finds a problem, it issues one of three recovery verdicts:

- `repair` — implementation is mostly correct but needs targeted follow-up. A new repair unit (`u-NNN-slug-repair-01`) is approved in `plan.md`.
- `redo` — implementation should not stand. The agent reverts if needed, then a retry unit (`u-NNN-slug-r02`) is approved.
- `replan` — execution showed the plan or design is wrong. The agent revises `plan.md` or routes back to `design`.

Recovery loops within `plan` / `execute` / `review-update`. It does not re-run `intent` unless the goal itself was invalidated.

## Approval pattern

The agent seeks approval at every phase boundary and advises whether the approval is consequential or procedural. Consequential gates state the real choice and tradeoffs; procedural gates state what changed and why, with the agent's recommendation to approve. The human can always override the advisory.

## Artifacts

```
docs/accord/
  accord-state.md
  commands.md
  intent.md
  intent-draft.md
  design.md
  design-draft.md
  plan.md
  plan-draft.md
  reports/
    exec-<unit-id>.md
    review-<unit-id>.md
```

Each phase has a single draft file (`<phase>-draft.md`) overwritten freely as work progresses. The draft moves forward only and always holds the current best thinking — there is no round-by-round comparison. A new draft opened after the canonical artifact is a proposed revision; it becomes accepted only when promoted.

## Unit IDs

Stable IDs in `plan.md` and tags:

```
u-001-auth-login
u-002-profile-cache
u-003-docs-typos
```

Never reuse a unit ID. For repair or retry, use suffixes:

- `u-001-auth-login-repair-01`
- `u-001-auth-login-r02`

## Auto-git

Lightweight tags at approved boundaries:

- `accord-intent-v<N>`
- `accord-design-v<N>`
- `accord-plan-v<N>`
- `accord-exec-<unit-id>`
- `accord-review-<unit-id>`
- `accord-complete-v1`

Commit prefixes: `intent:`, `design:`, `plan:`, `exec:`, `review:`, `commands:`.

Commits use explicit paths and never sweep unrelated user work into a phase commit. Version tags increment when canonical `intent.md`, `design.md`, or `plan.md` is promoted again.

If git is unavailable, save artifacts normally and warn the human that recovery and review have a weaker baseline.

## Completion

When no next unit remains, `review-update` may close the project: set `accord-state.md` status to `complete`, add a final entry to `plan.md`, commit with `review: complete ACCORD project`, tag `accord-complete-v1`. If new work later re-enters at `intent`, do not move or recreate `accord-complete-v1`; resume normal phase tags.

## References

Each skill reads the focused contracts it needs:

- `references/state-schema.md`
- `references/commands-schema.md`
- `references/draft-conventions.md`
- `references/intent-schema.md`
- `references/design-schema.md`
- `references/plan-schema.md`
- `references/execution-report-schema.md`
- `references/git-conventions.md`

These define minimum contracts and scale-up triggers. They are not exhaustive templates.
