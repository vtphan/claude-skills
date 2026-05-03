# Git Conventions for VADER

A lightweight, optional layer that maps VADER's artifacts onto Git so transitions between stages and waves leave a legible trail. These are *conventions*, not enforcement: nothing in VADER's skills depends on git being used. When git is in use, each VADER skill runs `git commit` (and `git tag` where applicable) itself after the human approves the artifact it produced — the skill knows the right prefix, message, co-author trailer, and tag set. The human's checkpoint is the explicit approval before save; the commit is the durable record of what was approved. Override is straightforward (`git reset --soft HEAD~1`, amend, recompose).

The point of these conventions is two-fold. First, the git log becomes a readable narrative of how the project was developed — which stage, which wave, what changed, in what order. Second, `wave-update`'s review subagent (and any future tooling that walks history) can rely on stable signals for diff scoping and orientation.

## Contents

1. [Philosophy](#1-philosophy)
2. [Commit prefixes](#2-commit-prefixes)
3. [Co-authorship](#3-co-authorship)
4. [Tags](#4-tags)
5. [Branches and pivots](#5-branches-and-pivots)
6. [How VADER skills use git history](#6-how-vader-skills-use-git-history)
7. [Examples](#7-examples)
8. [What this is not](#8-what-this-is-not)

---

## 1. Philosophy

Three principles thread through the conventions:

**Skills commit after human approval; humans can override.** Each VADER skill, after the human approves the final state of the artifact it produced, runs `git commit` (and `git tag` where appropriate). The skill knows what it changed, the right prefix, the co-author trailer, and any tag to set; it's wasteful to make the human compose all of that manually. The human's checkpoint is the *approval before save* (which the skill's interactive flow already enforces); the commit is the durable record of what was approved. If the human disagrees with the resulting commit, override is straightforward: `git reset --soft HEAD~1` to unstage; amend or recompose; commit again.

**Skills detect git presence.** If `git rev-parse --is-inside-work-tree` succeeds, the skill commits. If not, the skill saves files normally and notes in its handoff that no commit was made (because no git repo). VADER works fine on projects without git — git just unlocks better diff scoping for `wave-update`'s review subagent.

**One commit per artifact write.** Each skill produces a coherent unit of work — a vision draft, an architecture draft, a wave plan update, an execution diff. That coherent unit gets one commit. Mixing artifacts across skills in a single commit makes downstream history harder to read; that's why each skill commits its own artifact at the moment it finalizes.

**Tags mark boundaries.** Skills set the boundary tags described in [Section 4](#4-tags) at the moments they commit. Tags are not gates — a wave can be updated without any tags being set — but they make navigation and `wave-update`'s diff scoping much easier. If a skill encounters an existing tag with the same name (e.g., `wave-plan-v2` already exists), it warns the user rather than silently overwriting.

## 2. Commit prefixes

Each commit message starts with a short prefix identifying which stage of the loop produced the change.

| Prefix       | Used for                                                              | Skills that produce it          |
|--------------|-----------------------------------------------------------------------|---------------------------------|
| `vision:`    | Vision doc — initial draft or pivot revision                          | `vision` (draft and pivot modes)|
| `arch:`      | Architecture doc, Decision Log entries (initial draft, ratified, or promoted to ADR files) | `architect` (draft and ratify modes) |
| `wave:`      | Wave plan creation or update (close current, expand next, absorbed findings, ADR ratification) | `wave-plan`, `wave-update`      |
| `exec:`      | Code changes from executing a wave; execution report                  | `wave-execute`                  |
| `revert:`    | Prefix-on-prefix when undoing a prior commit                          | (manual)                        |
| `redo:`      | Prefix-on-prefix when re-attempting a stage after a failure           | (manual)                        |

Examples in section 7.

The body of a good commit message names the artifact specifically and the most consequential decision or outcome — same shape that the wave plan's change-log entries take. Keep subjects under ~70 characters; put detail in the body.

## 3. Co-authorship

When a VADER skill (i.e., an LLM agent) produced the artifact you're committing, mark the commit with a `Co-authored-by:` trailer. This is how downstream tooling (and you, six months later) distinguish human-only commits from LLM-collaborative ones.

```
exec: W2 — query parser, executor, find subcommand

[message body...]

Co-authored-by: Claude <noreply@anthropic.com>
```

If you wrote the artifact entirely yourself (e.g., you hand-edited the vision doc to fix a roles section), no co-author trailer is needed. If you took the LLM's output and revised it substantially, still use the trailer — the artifact is collaborative.

This convention is what makes the difference between a project where the human ratified everything and a project where the human did half the writing detectable from history. Future tooling (and your future self) will care.

## 4. Tags

Tags mark boundaries. They are how `wave-update`'s review subagent finds a clean diff baseline and how a curious reader navigates the project's history.

| Tag                       | Set when                                              | Set by              |
|---------------------------|-------------------------------------------------------|---------------------|
| `vision-v<N>`             | On the vision-N commit                                | `vision` skill      |
| `arch-v<N>`               | On the architecture-N (ratified) commit               | `architect` (ratify mode) |
| `wave-plan-v<N>`          | On the wave-plan-N commit                             | `wave-plan` (W1) or `wave-update` (later) |
| `W<N>-start`              | On the wave-plan commit that establishes W<N> as the current wave (wave-plan for W1; wave-update for W2+) | `wave-plan` or `wave-update` |
| `W<N>-end`                | On the `wave-execute` commit at end of W<N>'s work    | `wave-execute`      |
| `W<N>-complete`           | On the `wave-update` commit that closes W<N>          | `wave-update`       |

The numbered `vision-v<N>`, `arch-v<N>`, and `wave-plan-v<N>` tags match the artifacts' frontmatter version fields — so `git checkout vision-v2` lands you on the commit where the vision was at version 2, exactly.

The wave-paired tags bracket each wave's work. `wave-update`'s review subagent uses `git diff W<N>-start..W<N>-end` to scope the wave's diff exactly. `git log W<N>-start..W<N>-complete` shows the full set of commits within wave N (from plan/expansion through execution to update).

If a skill is about to set a tag and the same name already exists (e.g., `wave-plan-v2` exists), the skill warns the user rather than silently overwriting. The user can then either rename their existing tag, accept the new one (manually delete the old), or note the conflict for later cleanup.

## 5. Branches and pivots

For normal cycles, work happens on the main branch. The cycle's commits sit on top of each other; tags mark the boundaries.

For **vision pivots**, optionally use a branch. A pivot is a high-stakes operation: the vision changes, the wave plan must be reconciled, possibly some Decision Log entries need to be superseded. Doing this on a branch lets you experiment with the cascade before committing the team to the new direction.

Convention:

```
git checkout -b pivot/v<N>-<short-name>
# invoke `vision pivot`, then `wave-update` (which produces a vision-pivot-update entry)
# review the cascaded state
git checkout main
git merge --no-ff pivot/v<N>-<short-name>
```

The `--no-ff` ensures the pivot shows up as a single merge commit on main, which makes the pivot's shape obvious in `git log --graph`. The branch name embeds the new vision version and a short slug describing the pivot's nature (e.g., `pivot/v2-shared-organizers`).

Branches are not required for pivots — small pivots with confident next steps can stay on main. But the branch gives you a clean "abandon" path if reviewing the cascade reveals a deeper problem.

Substantial-updates stay on main; they're not pivots.

## 6. How VADER skills use git history

Git is **strongly recommended**. VADER works without it, but several properties degrade:

- **`wave-update`'s review subagent** uses `git diff <wave_start_ref>..<wave_end_ref>` to scope its scope-leakage check exactly. Without git, the review must fall back to the execution report's claims about what changed and to working-tree heuristics — both less reliable.
- **`wave-update`** records refs/tags in change-log entries when present, giving the change log a cross-reference into history.
- **The pivot branch convention** (`pivot/v<N>-<short-name>`) lets you experiment with cascading reconciliation before merging back to main.

Where a skill needs a specific ref (e.g., the review's baseline), the ref is recorded in the execution report's YAML frontmatter — `wave_start_ref` (set by wave-execute before work begins) and `wave_end_ref` (set by wave-execute after its commit). When git is in use, both fields are populated and reliable. When git is absent, both are empty and the review subagent does its best from the report and working-tree state.

## 7. Examples

A clean linear sequence for a small project's first three commits:

```
commit ac3b41e
  vision: initial draft for bookclub project

  Drafted from a 30-min sounding-board session. Five roles, three
  in-scope capabilities, eight open questions. Vision-version 1.

  Co-authored-by: Claude <noreply@anthropic.com>

  (tag: vision-v1)

commit 9d27f0a
  arch: ratify initial architecture, ADR-001 through ADR-005

  Five seed ADRs. Architecture-version 1. Modules: auth, clubs,
  polls, schedule, notes. Ratified after one revision pass on
  ADR-003 (deployment).

  Co-authored-by: Claude <noreply@anthropic.com>

  (tag: arch-v1)

commit b8a1290
  wave: initial wave plan, W1 walking skeleton, W2-W4 sketched

  W1 exercises all five modules with a trivial happy-path login flow.
  Wave-plan-version 1.

  Co-authored-by: Claude <noreply@anthropic.com>

  (tags: wave-plan-v1, W1-start)
```

A cycle's worth of commits within a single wave (two events per wave):

```
commit ce4012a  exec: W2 — query parser, executor, find subcommand    (tag: W2-end)
commit 27d0a4c  wave: update after W2 — A2→A6, ADR-007 supersedes ADR-004, expand W3
                                                                       (tags: wave-plan-v2, W2-complete, W3-start)
```

Notice `W2-start` was set on the previous `wave-plan-v1` commit (or on the prior `W1-complete` for waves W2+); `W2-end` is set by `wave-execute`; `W2-complete` is set by `wave-update`. `git diff W2-start..W2-end` shows exactly the wave's execution diff. `git log W2-start..W2-complete` shows all commits in W2.

A pivot branch:

```
* commit f3a8b1c (HEAD -> main, tag: vision-v2)
|\  Merge pivot/v2-shared-organizers
| * commit a7d2e09  wave: vision-pivot-update after v2; retire W4
| * commit b1c4f27  vision: pivot v2 — co-organizers replace solo organizer
|/
* commit 27d0a4c (tag: W2-complete) ...
```

The `--no-ff` merge keeps the pivot visible as a discrete unit in the graph.

## 8. What this is not

These conventions are deliberately not:

- **Enforced gates.** A wave can be updated without any tags being set. The artifacts are the gate; git is the navigator.
- **A code-review process.** No PR conventions, no required reviewers, no merge policies. If you want those, layer them on top — they're orthogonal to VADER.
- **CI signals.** No skill watches for tags or commit prefixes to trigger automation. Building CI on top of these conventions is straightforward but not part of VADER itself.
- **Required for VADER to work.** Every VADER skill works fine on a project with no git repo at all. Git makes some things easier and powers some downstream tooling; absence of git makes those things slightly fuzzier but not broken.

---

This doc is the contract for how VADER artifacts map onto Git. Skills run `git commit` and `git tag` themselves after the human approves the artifact — the conventions specify the exact commit messages and tags they use. The human can override any commit (`git reset --soft HEAD~1`, amend, recompose) at any point.
