# Git Conventions for VADER

A lightweight, optional layer that maps VADER's artifacts onto Git so transitions between stages and waves leave a legible trail. These are *conventions*, not enforcement: nothing in VADER's skills depends on git being used, and skills never run git commands themselves. The human lead runs commits and tags; the skills suggest messages.

The point of these conventions is two-fold. First, the git log becomes a readable narrative of how the project was developed — which stage, which wave, what changed, in what order. Second, downstream skills (`wave-audit` for diff scoping, `vader-next` for state detection, any future tooling that walks history) can rely on stable signals.

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

**Skills suggest, humans commit.** No VADER skill runs `git commit` or `git tag`. The skill's handoff section ends with a suggested commit message; you decide whether and when to commit. This preserves the human-lead model: the moment of committing is itself a checkpoint.

**One commit per artifact write.** Each skill produces a coherent unit of work — a vision draft, an architecture draft, a wave doc redraft, an execution diff, a report. That coherent unit gets one commit. Mixing artifacts and code in a single commit makes downstream history harder to read.

**Conventions are not gates.** A wave can be audited and redrafted without any git tags being set. The reports themselves are the gate — git just makes navigation easier. If you forget to tag a wave-end, the project is not broken; the next vader-next invocation may need slightly more context, and the audit's diff baseline may need a manual reference.

## 2. Commit prefixes

Each commit message starts with a short prefix identifying which stage of the loop produced the change. The prefix is the artifact category, not the skill name — multiple skills produce the same artifact category and share a prefix.

| Prefix       | Used for                                                              | Skills that produce it                |
|--------------|-----------------------------------------------------------------------|---------------------------------------|
| `vision:`    | Vision doc — initial draft or pivot revision                          | `vision-shaper`, `vision-pivot`       |
| `arch:`      | Architecture doc, ADRs (initial, ratified, or superseded)             | `architect-draft`                     |
| `wave:`      | Wave doc creation, redraft, or vision-pivot reconciliation            | `wave-draft`, `wave-redraft`          |
| `exec:`      | Code changes from executing a wave                                    | `wave-execute`                        |
| `audit:`     | Audit report                                                          | `wave-audit`                          |
| `arch-review:` | Architect-review report; proposed ADR files                         | `architect-review`                    |
| `revert:`    | Prefix-on-prefix when undoing a prior commit                          | (manual)                              |
| `redo:`      | Prefix-on-prefix when re-attempting a stage after a failure           | (manual)                              |

Examples in section 7.

The body of a good commit message names the artifact specifically and the most consequential decision or outcome — same shape that the wave doc's change-log entries take. Keep subjects under ~70 characters; put detail in the body.

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

Tags mark boundaries. They are how `wave-audit` finds a clean diff baseline, how `vader-next` orients to the most recent transition, and how a curious reader navigates the project's history.

| Tag                       | Set when                                              | Set by    |
|---------------------------|-------------------------------------------------------|-----------|
| `vision-v<N>`             | After committing vision-version N (initial or pivot)  | Manual    |
| `arch-v<N>`               | After committing architecture-version N (ratified)    | Manual    |
| `wave-doc-v<N>`           | After committing wave-doc-version N (any redraft)     | Manual    |
| `W<N>-start`              | At the moment `wave-execute` begins on W<N>           | Manual    |
| `W<N>-complete`           | After `wave-redraft` closes W<N>                      | Manual    |

The numbered `vision-v<N>`, `arch-v<N>`, and `wave-doc-v<N>` tags match the artifacts' frontmatter version fields — so `git checkout vision-v2` lands you on the commit where the vision was at version 2, exactly.

The wave-paired tags `W<N>-start` and `W<N>-complete` bracket each wave's work. Their primary use is `wave-audit`'s diff: `git diff W<N>-start..HEAD` is exactly the wave's changes. They also let you quickly navigate "what happened in W3?" via `git log W3-start..W3-complete`.

Tags are recommended at the major boundaries above. You don't need a tag at every commit; the prefixes carry enough information for everyday navigation. Tags are for the moments where you're likely to want a stable reference point.

## 5. Branches and pivots

For normal cycles, work happens on the main branch. The cycle's commits sit on top of each other; tags mark the boundaries.

For **vision pivots**, optionally use a branch. A pivot is a high-stakes operation: the vision changes, the wave doc must be reconciled, possibly some ADRs need to be superseded. Doing this on a branch lets you experiment with the cascade before committing the team to the new direction.

Convention:

```
git checkout -b pivot/v<N>-<short-name>
# invoke vision-pivot, then wave-redraft (vision-pivot-redraft mode), etc.
# review the cascaded state
git checkout main
git merge --no-ff pivot/v<N>-<short-name>
```

The `--no-ff` ensures the pivot shows up as a single merge commit on main, which makes the pivot's shape obvious in `git log --graph`. The branch name embeds the new vision version and a short slug describing the pivot's nature (e.g., `pivot/v2-shared-organizers`).

Branches are not required for pivots — small pivots with confident next steps can stay on main. But the branch gives you a clean "abandon" path if reviewing the cascade reveals a deeper problem.

Substantial-redrafts and scope-renegotiation-redrafts stay on main; they're not pivots.

## 6. How VADER skills use git history

The skills don't *require* git, but several of them benefit when git is present:

- **`wave-audit`** uses `git diff <wave_start_ref>..HEAD` (or `W<N>-start..HEAD`) to scope its scope-leakage check. Without git, the auditor relies on the report's claims about what changed.
- **`vader-next`** reads the most recent commit and tags to orient when the artifact frontmatter alone is ambiguous.
- **`wave-redraft`** can include commit shas in change-log entries to cross-reference history (optional but useful for traceability).
- **`vision-pivot`** suggests the pivot branch convention in its handoff.

Where the skill needs a specific ref (e.g., audit's baseline), the ref is recorded in the relevant report's YAML frontmatter — `wave_start_ref` and `wave_end_ref` on the execution report. The skill doesn't need to interact with git itself; it reads the ref out of the artifact.

If git is not in use on a project, those frontmatter fields are simply absent, and audit's diff scope falls back to "every change since the prior wave's reports" as documented in its conventional behavior.

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
  wave: initial wave doc, W1 walking skeleton, W2-W4 sketched

  W1 exercises all five modules with a trivial happy-path login flow.
  Wave-doc-version 1.

  Co-authored-by: Claude <noreply@anthropic.com>

  (tag: wave-doc-v1)
```

A cycle's worth of commits within a single wave:

```
commit ce4012a  exec: W2 — query parser, executor, find subcommand  (tag: W2-start)
commit 51f9fde  audit: W2 — pass-with-findings (F1 ADR-004 violation)
commit 9c8e7b1  arch-review: W2 — propose ADR-007 supersedes ADR-004
commit 27d0a4c  wave: redraft after W2 — ratify ADR-007, expand W3   (tags: wave-doc-v2, W2-complete)
```

Notice the `W2-start` tag is set at the start of `exec:` work and `W2-complete` at the end of the redraft. `git diff W2-start..W2-complete` shows exactly what W2 produced.

A pivot branch:

```
* commit f3a8b1c (HEAD -> main, tag: vision-v2)
|\  Merge pivot/v2-shared-organizers
| * commit a7d2e09  wave: vision-pivot-redraft after v2; retire W4
| * commit b1c4f27  vision: pivot v2 — co-organizers replace solo organizer
|/
* commit 27d0a4c (tag: W2-complete) ...
```

The `--no-ff` merge keeps the pivot visible as a discrete unit in the graph.

## 8. What this is not

These conventions are deliberately not:

- **Enforced gates.** A wave can be audited without any tags being set. A redraft can run without a co-author trailer on prior commits. The artifacts are the gate; git is the navigator.
- **A code-review process.** No PR conventions, no required reviewers, no merge policies. If you want those, layer them on top — they're orthogonal to VADER.
- **CI signals.** No skill watches for tags or commit prefixes to trigger automation. Building CI on top of these conventions is straightforward but not part of VADER itself.
- **Required for VADER to work.** Every VADER skill works fine on a project with no git repo at all. Git makes some things easier and powers some downstream tooling; absence of git makes those things slightly fuzzier but not broken.

---

This doc is the contract for how VADER artifacts map onto Git. Skills' handoff sections suggest specific commit messages and tags in line with these conventions; the human runs the actual commands.
