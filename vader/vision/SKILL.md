---
name: vision
description: Use this skill at two distinct moments in a VADER project. (Mode = draft) When the user has a rough idea for a software product or system and wants help shaping it into a vision document. Triggers include phrases like "I have an idea for X, help me think it through", "shape this into a vision doc", "draft a vision for this", "let's brainstorm this product idea", or whenever the user describes an idea conversationally and asks for help making it concrete enough to plan against. (Mode = pivot) When an existing vision doc needs revision because something learned during execution has invalidated a core part of it. Triggers include phrases like "the vision needs to change because of W3", "we need to pivot — the value hypothesis didn't hold", "update the vision to reflect <core change>", or whenever the user explicitly says "vision pivot". Do NOT use to draft requirements, stories, or features (those live in the wave plan). Do NOT use for cosmetic edits or clarifications that don't change the project's direction (those are not pivots).
---

# Vision

Shape or revise a software project's vision doc — the upstream artifact that captures intent, target users, value hypothesis, scope, non-goals, and success metrics. The vision is the source of truth for *why* the project exists; everything downstream (architecture, wave plan, executions) inherits from it.

This skill has two modes: **draft** (initial vision; conversational sounding-board) and **pivot** (deliberate revision when later-wave learning invalidates a core part of the vision). Modes are explicit — the user invokes the skill with the mode they intend.

Before doing anything else, read `references/vision-schema.md` in full. The schema defines the doc's shape, the nine required sections (plus optional Section 10 Core Journeys), and pivot semantics.

## Mode: draft

The default. Used at project start — or when applying VADER to an existing codebase that has no vision doc yet (brownfield adoption). Walk the user through the questions that turn an idea into a vision they can plan against.

**Workflow:**

0. **Detect brownfield and orient.** Before opening the conversation, check whether the working directory contains existing source code (look for `package.json`, `Cargo.toml`, `pyproject.toml`, `go.mod`, `Makefile`, a `src/` or `lib/` directory, or any non-trivial code outside `docs/`). If yes, this is a *brownfield* vision: there is already a system, and you're documenting intent in retrospect. Read the top-level structure: directory layout, build/test entry points, primary dependencies, and a representative file or two — the same orientation `architect` will perform later, done now so the vision conversation is grounded in what actually exists. Goal is not exhaustive reverse-engineering — it's enough orientation that the value hypothesis, target users, and in-scope/non-goals can be tested against the system the user has, not the one they imagine. Briefly tell the user what you observed before drafting starts; they may correct or contextualize. Brownfield visions tend to need extra attention to *why this project exists distinct from what was already built* — the value hypothesis often gets sharper when there's an existing system to compare against. On greenfield projects (no existing code), skip this step and proceed to step 1.

1. **Listen first, ask second.** Open by inviting the user to describe what they're thinking, in their own words. Let them ramble. Note what they emphasize and what they skip — those gaps are usually the most fruitful conversation territory.

2. **Pressure-test the value hypothesis early.** The single most consequential section. It is a one-paragraph testable claim: "If we build X for Y, they will Z, because of W." Push back on vague claims ("users will love it", "saves time") until the user can state it as a single falsifiable sentence.

3. **Get the roles right before anything else.** A role is what someone is trying to accomplish, not their job title. "User" is rarely useful — break it apart. Ask the user to walk you through one specific person they have in mind for each role.

4. **Make non-goals as load-bearing as goals.** Push the user, deliberately, to say what the system won't do. Non-goals serve scope discipline downstream; without them, scope creep has nothing to bounce off.

5. **Surface open questions; don't paper over them.** Section 9 is meant to be substantial — 5 to 15 entries in a freshly drafted vision. Each open question should be specific. The open questions seed the wave plan's assumptions register.

6. **Decide whether to draft Core Journeys (Section 10).** Optional. Include 1-3 short journeys when the product is user-facing and users navigate flows that span multiple modules. Skip when the product is a CLI, library, build tool, or other infra/tech where users don't navigate flows. List candidate journeys in Open Questions if you can't yet say what the core journeys are.

7. **Draft, then converge.** Show the user a draft. Invite revision. Expect 2-3 rounds. Save the file only when the user is satisfied. Frontmatter: `vision_version: 1`, `status: active`.

**Principles:**

- The vision is short by design. Two pages of body content is the soft cap. Push back on detail; the wave plan is the right place for it.
- Capture intent, not implementation. Architecture decisions and specific features belong elsewhere.
- Specifics beat generalities. Push for measurable success metrics, named roles, named alternatives in prior art.
- Disagree explicitly when it matters. Quiet acquiescence now produces costly drift later.

## Mode: pivot

Used when later-wave learning invalidates a core part of the vision. Pivots are deliberately rare and high-stakes.

**What constitutes a pivot:** changes to the value hypothesis, target users, in-scope set, non-goals, or success metrics that invalidate downstream artifacts. *Not* a pivot: adding open questions, tightening a metric numerically, fixing a typo, adding to prior art.

**Workflow:**

1. **Confirm the pivot is real.** Before editing anything, summarize back to the user what you understand the pivot to be. State which sections will change and which downstream artifacts are likely affected. Wait for explicit confirmation. If the trigger is weak (one ambiguous data point, one user-test session), push back — suggest waiting for more signal or treating the change as a wave-plan substantial-update instead.

2. **Identify which sections change.** Walk the nine (or ten) sections; for each, decide unchanged / edited / replaced. Don't edit until you can show the user the new content for every section being changed.

3. **Edit the body in place.** Don't preserve old content as inline "previous version" prose — the change log holds history. The body should read as a clean, current statement of intent.

4. **Bump frontmatter.** `vision_version` += 1; `last_updated` = today; `status: pivoted`.

5. **Append change-log entry** (Section 5 of the doc, which exists for vision_version 2+). Be specific. Each section's change gets its own bullet. Replaced metrics or non-goals preserve the old text in the change log.

6. **Hand off with explicit reconciliation list.** Tell the user: vision is now `pivoted`; the wave plan must be reconciled at the next `wave-update` invocation (which will produce a `vision-pivot-update` change-log entry); the architecture's Decision Log may need ratification of supersessions in the same wave-update. The pivoted status clears only after a successful execute → update cycle.

**Principles for pivot mode:**

- Pivots are deliberate events, not drift responses. If you find yourself running pivot every few weeks, the vision was poorly shaped initially — go back to draft mode for a wholesale rethink.
- The change log is the audit trail. Skimping on detail here corrupts the project's memory.
- Removing a non-goal is itself a pivot, and the most expensive kind. Be unambiguous about it.
- Pivots cascade, but only one layer at a time. This skill edits the vision; `wave-update` cascades downstream.

## Things to never do

1. **Never write to the vision body in any mode other than draft (initial) or pivot.** Other reads of the vision are read-only.
2. **Never edit the vision body without bumping `vision_version` and writing a change-log entry.** (Initial draft is the exception — version 1 has no change log.)
3. **Never reuse old vision_version numbers.**
4. **Never edit the wave plan or architecture as part of this skill.** Hand off; let the user invoke wave-update.
5. **Never pivot without explicit user confirmation of the trigger.**
6. **Never compress multiple changes into one vague change-log entry.** Each section's change gets its own bullet.

## Handoff

After draft mode, tell the user the next step is `architect draft`. After pivot mode, tell the user the next step is `wave-update` (which will produce a `vision-pivot-update` reconciling the wave plan to the new vision).

**Git.** If git is in use, after the user approves the vision, commit and tag yourself:
- Draft mode: `git commit -m "vision: initial draft for <project>" -m "Co-authored-by: Claude <noreply@anthropic.com>"` then `git tag vision-v1`.
- Pivot mode: `git commit -m "vision: pivot v<N> — <short description>" -m "..." -m "Co-authored-by: Claude <noreply@anthropic.com>"` then `git tag vision-v<N>`. For high-stakes pivots, the user may have created a `pivot/v<N>-<short-name>` branch beforehand — commit on that branch; merging to main is the user's call.

Tell the user the sha and tag. Override: `git reset --soft HEAD~1`. If git is not in use, save normally and note no commit was made. See `../references/git-conventions.md` for full conventions and the `git rev-parse --is-inside-work-tree` detection.
