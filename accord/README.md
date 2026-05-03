# ACCORD

ACCORD is a lightweight process for a human lead and a capable LLM to develop a greenfield software project together. It surfaces design judgment at the moments where bad design tends to creep in — vague intent, weak architecture, debt-prone plans, drifting execution — and stays out of the way otherwise.

## Principles

1. **Five skills.** `intent`, `design`, `plan`, `execute`, `review-update`. No additional skills.
2. **Brainstorm-this codesign.** `intent` and `design` adopt the discipline of the `brainstorm-this` skill: numbered drafts, round stances, immutable core after round 0, required critique pass before convergence, strict non-overwrite. The discipline is the protection against premature consensus.
3. **Greenfield only.** ACCORD assumes the project starts under ACCORD. There is no brownfield adoption path.
4. **Auto-git.** Approved phase boundaries become commits and lightweight tags. Git history is the framework's durable state.
5. **The agent is capable.** ACCORD does not micromanage the LLM. Schemas protect handoff between phases; they do not script the LLM's thinking inside a phase.
6. **Approval gates are real but advised.** The agent always seeks approval at phase boundaries. With each request, it advises whether the approval is consequential (real choice for the human) or procedural (rubber stamp). This concentrates human attention where it counts and prevents approval theater.
7. **Quality over protocol.** ACCORD exists to prevent bad design — debt, redundancy, contradiction. Every constraint should serve that goal; trim anything that doesn't.
8. **Two modes.** Codesign mode (`intent`, `design`) is human-and-agent iterating together. Agent-led mode (`plan`, `execute`, `review-update`) is the agent leading with the human approving at gates.
9. **Cross-LLM, cross-conversation handoff.** Any skill — most often `review-update` — may be invoked in a fresh conversation, with a different LLM. ACCORD's artifacts (canonical files, `plan.md`, execution reports, `accord-state.md`, commits, tags) must be sufficient for this handoff without conversational context from a prior session. This sets the quality bar for every artifact the framework produces.

## Modes

### Codesign mode — `intent` and `design`

The human lead and the agent build the project's intent and design together via brainstorm-this draft rounds. The agent's posture is **elicitive and generative** — drawing out aspects the human hasn't yet articulated, and proposing transformative alternatives the human can react to, redirect, or reject. This applies especially to UI/UX, which is part of design: the agent proposes interaction models, information architecture, and accessibility considerations rather than waiting to be asked. The discipline (round stances, immutable core after round 0, required critique pass before convergence) keeps this from sliding into sycophantic refinement or premature consensus. The approved draft is promoted to a clean canonical artifact (`intent.md`, `design.md`).

This is where the human's mental model of the project gets built and tested. Approval gates here are usually consequential.

### Agent-led mode — `plan`, `execute`, `review-update`

After design is approved, the agent leads. It plans, builds, verifies, and recovers from its own mistakes informed by the approved intent and design. The human reviews the agent's reasoning at gates. Approval gates here are usually procedural — the agent advises when one is consequential.

`plan` uses lightweight drafts for consistency with intent and design, but the default is one round: the agent produces `draft_00.md`, the human approves, it becomes `plan.md`. Multiple rounds happen only when the human pushes back.

In `plan`, the agent must inform the human *why* the chosen plan shape fits *this* design and scope. Generic shape justifications are insufficient; the rationale must reference the specific design artifact.

`review-update` is typically invoked in a fresh conversation, often with a different LLM, so the review reads the executed work cold against the committed artifacts. The execution report, the unit's acceptance criteria in `plan.md`, the design decisions in `design.md`, and the diff under review must together be sufficient for an unfamiliar agent to issue a verdict without asking the executor for context.

## Skills

- `intent` — codesign project intent. Brainstorm-this draft rounds, then promote to `intent.md`.
- `design` — codesign architecture and consequential decisions. Brainstorm-this draft rounds, then promote to `design.md`.
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

After bootstrap, ongoing work lives in a loop. The agent approves a new unit in `plan.md`, executes it, reviews it, and either approves the next unit or enters recovery:

```
plan → execute → review-update
       ↑                     ↓
       └─── approve next ────┘
```

Adding a new unit that fits the existing approved plan does not re-run intent or design. The agent proposes the unit in `plan.md`; the human approves; execution proceeds.

### Re-entry at intent for new features or revisions

When the human lead wants to add a new feature or revise an existing one, re-invoke `intent`. The agent runs a brainstorm-this round to test whether intent has actually shifted:

- **If intent still holds**, the round converges quickly (stance `stop`); canonical `intent.md` stays as-is and the work moves to `design`.
- **If intent has shifted**, real codesign happens; an updated `intent.md` is promoted and tagged.

The same pattern applies to `design`. The work eventually lands at `plan`, which produces a new plan draft incorporating the feature or revision.

Every feature addition or revision is *checked* against intent and design before reaching execution. Most checks converge fast; the discipline catches the cases where a change quietly shifts the project's direction. Skipping the check is what produces contradiction and debt over time.

The boundary between "new unit within the existing plan" and "feature revision that re-enters intent" is the agent's first call, declared with an advisory; the human can disagree.

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
  intent/
    draft_00.md
    intent.md
  design/
    draft_00.md
    design.md
  plan/
    draft_00.md
    plan.md
  reports/
    exec-<unit-id>.md
```

Drafts are never overwritten. A draft after a canonical artifact is a proposed revision; it becomes accepted only when promoted.

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
