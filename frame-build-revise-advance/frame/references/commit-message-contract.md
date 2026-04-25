# FBRA Commit Message Contract

Use this contract when the human permits commits. Commit history is part of the implementation record: it should help a human or LLM auditor trace wave requirements to code, affected behavior, and verification.

Git already records the changed files. Commit messages should explain intent, scope, affected surfaces, and receipts.

## Template

```text
<type>: <short change summary>

Wave: W<N> - <wave name>
Implements:
- W<N>-MH<K>: <short label>

Affects:
- <behavioral/product surface>
- <data/API/security surface when relevant>
- <test/verification surface when relevant>

Notable files:
- <optional; only when a file is semantically important>

Notes:
- <constraint, non-goal, deferred scope, or decision>

Verified:
- <command/manual check and observed result>
```

## Types

- `feat` - user-facing feature or story.
- `fix` - bug fix or correction after failed verification.
- `test` - test-only change.
- `refactor` - behavior-preserving restructuring.
- `docs` - wave doc, README, or implementation notes.
- `chore` - config, tooling, setup, dependency plumbing.
- `revert` - revert a prior commit.

## Rules

- Commit at coherent implementation, decision, verification, or wave-document boundaries.
- Reference stable must-have IDs for `feat`, `fix`, and behavior-changing commits.
- Prefer exact must-have IDs plus a short label over paraphrasing long requirements.
- Include auth, security, data model, persistence, API, billing, or workflow surfaces under `Affects` when touched.
- If verification was not run, write `Verified: Not run - <reason>`.
- Do not claim a whole wave unless the commit completes and verifies that wave.
- Do not list changed files by default. Use `Notable files` only for migrations, public entry points, config contracts, security-sensitive files, generated/vendored files, or large moves/renames.
- Never include unrelated user changes in a commit. Inspect a dirty worktree before staging.

## Wave Document History

The wave doc is part of the implementation record. Any material change to it should be committed when commits are permitted, or the human should be asked whether to commit it.

Material changes include:

- Requirement IDs or requirement text.
- Must-have, nice-to-have, task, decision, verification, or note changes.
- Task completion checkboxes.
- Deferred, dropped, or superseded scope.
- Wave state changes and active-wave transitions.

Prefer separate `docs` commits for scope, decision, verification, and wave-state changes. Small checkbox updates may be included with an implementation commit only when they describe exactly the same completed and verified work.
