---
name: vision-pivot
description: Use this skill when an existing vision doc needs revision because something learned during execution has invalidated a core part of it — the value hypothesis turned out to be wrong, the wrong roles were named, an in-scope capability proved unnecessary, a non-goal needs to be retired, or a success metric is unmeasurable as stated. Triggers include phrases like "the vision needs to change because of what we learned in W3", "we need to pivot — let's revise the vision doc", "update the vision: <core change>", "the value hypothesis didn't hold up — let's redo the vision", or whenever the user explicitly invokes "vision pivot" or "we need a pivot at the vision level". Do NOT use for the initial drafting of the vision (that's vision-shaper). Do NOT use for cosmetic edits or clarifications that don't change the project's direction (those are not pivots and should not bump vision_version). Do NOT use to revise the wave doc or architecture doc — those have their own skills.
---

# Vision Pivot

Revise the vision doc when learning from later waves invalidates a core part of it. This is a deliberately rare and high-stakes operation. The vision is the upstream source of truth for goal, roles, value hypothesis, scope, and non-goals; changing it cascades into everything downstream. The skill's primary job is to make sure that cascade is intentional, traceable, and not silent.

Before doing anything else, read `references/vision-schema.md` in full — particularly Section 4 (Pivot semantics), Section 5 (Change log), and Section 6 (Invariants).

## What constitutes a pivot

Not every edit to the vision is a pivot. The schema reserves "pivot" for changes that *invalidate downstream artifacts*. Examples that are pivots:

- Changing the value hypothesis (§3) so that the project's central bet is now different.
- Replacing or removing a role (§2) — e.g., realizing the product needs co-organizers, not solo organizers.
- Adding to or removing from In Scope (§4) in a way that affects which waves are needed.
- Removing a non-goal (§5) — broadening the project to include something previously excluded.
- Replacing or significantly revising a success metric (§6) so the audit's verdict criteria change.

Examples that are *not* pivots:
- Tightening a success metric numerically (60% → 65%).
- Adding to Open Questions (§9). That's not a pivot; that's just learning.
- Fixing a typo or clarifying a sentence without changing meaning.
- Adding a paragraph to Prior Art (§8).

If you're not sure whether a change is a pivot, ask the user. The cost of being wrong about this is high in both directions: a non-pivot recorded as a pivot triggers an unnecessary cascade; a real pivot recorded as a minor edit leaves downstream artifacts inconsistent with the vision.

## Inputs and output

**Inputs:**
- The current vision doc (`<project-slug>-vision.md`).
- The trigger for the pivot — usually one or more wave-audit reports, an architect-review report, or a direct user observation. The user should provide or point to this input; if they don't, ask.
- (Recommended) The current wave doc, so you can think about what cascading reconciliation will be required.

**Outputs:**
- The vision doc, edited in place. `vision_version` incremented. `last_updated` set to today. `status` set to `pivoted`.
- A new change-log entry appended (Section 5 of the schema's structure).
- A handoff message to the user listing what downstream reconciliation is now required.

## Workflow

### 1. Confirm the pivot is real

Before editing anything, summarize back to the user what you understand the pivot to be. State explicitly which sections of the vision will change and which downstream artifacts are likely to be affected. Wait for confirmation. This is not a formality; it is the cheapest way to avoid an expensive mistake.

If the user is uncertain or the trigger is weak (one ambiguous data point, or a single user-test session with three users), push back. Suggest they wait for more signal, or treat the change as a wave-doc-level substantial-redraft instead. Pivots are a tool, not a default response to surprise.

### 2. Identify which sections change

Walk through the nine sections of the vision doc and decide, for each: unchanged, edited, or replaced. Be specific. "The value hypothesis is changing" is not enough — the new hypothesis must be drafted before the old one is touched.

If a role is being replaced, the new role needs a description and a "what they're trying to do" line. If a success metric is being replaced, the new metric needs a measurement method. Don't edit until you can show the user the new content for every section being changed.

### 3. Edit the body

Apply the edits in place. Do not preserve old content inline as "previous version" prose — the change log holds the history. The body should read as a clean, current statement of intent.

The exception: when a metric or non-goal is being replaced rather than removed, the change-log entry preserves the old text. The body shows only the new.

### 4. Bump frontmatter

- `vision_version` += 1.
- `last_updated`: today's date, ISO format.
- `status: pivoted`.

The `pivoted` status is what signals downstream skills (especially `wave-redraft`) that a reconciling cycle is required.

### 5. Append the change-log entry

The change-log entry is the canonical record of the pivot. It must be detailed enough that, six months later, a reader can understand what changed and why. Format follows schema Section 5:

```markdown
### YYYY-MM-DD — Pivot vN
Type: pivot
- Section <N> (<name>): <what changed, with old text preserved if replaced>.
- ...
- Triggers downstream reconciliation. Vision status: pivoted until next wave-redraft.
```

Be specific. "Updated section 3" is useless. "Section 3 (Value hypothesis): replaced 'users will return weekly to interact with state' with 'organizers will return weekly because they handed off duty cleanly'; the W3 audit revealed members do not actually interact with state weekly — only organizers do" is useful.

### 6. Hand off with explicit reconciliation list

Tell the user:
- Vision status is now `pivoted`.
- The wave doc must be reconciled at the next `wave-redraft` invocation. Specifically, list which sections of the wave doc are likely affected (Goal/Non-goals, Roles, the wave ladder, possibly the assumptions register).
- The architecture doc may need a corresponding architect-review pass if architectural choices were made that depend on now-changed vision elements.
- The pivoted status will clear only after the next successful execute → audit → architect-review → redraft cycle.

Do not invoke any downstream skill yourself. The user is the lead.

## Principles to keep in mind

**A pivot is a deliberate event, not a drift response.** If you're tempted to run vision-pivot every few weeks, the project either has unstable foundations (in which case go back and shape the vision more carefully) or you're over-reacting to noise.

**The change log is the audit trail.** A reader two years from now should be able to reconstruct the project's decisions from the vision doc's change log alone. Skimping on detail here corrupts the project's memory.

**Body changes are clean; history lives in the change log.** Don't preserve "previously: X" markers in the body. The reader of the body should see the current state, not a layered palimpsest.

**Removing a non-goal is itself a pivot, and the most expensive kind.** It silently broadens the project. Be unambiguous about it. The change-log entry should name it as such.

**Pivots cascade, but only one layer at a time.** The vision pivot is the source. The wave-redraft cycle reconciles the wave doc. Architect-review reconciles the ADR log. Don't attempt to do all three in one skill invocation; that's how mistakes compound.

## What to do if the trigger is ambiguous

Sometimes the user shows up with "we need to change the vision" and the actual trigger is a frustration with the wave doc, an unhappy stakeholder, or a single data point. Before pivoting, ask:

- What specifically changed your mind? (Get a concrete answer.)
- Could this be addressed at the wave-doc level instead — substantial-redraft, scope renegotiation, or new waves?
- Are downstream artifacts (the wave doc and architecture) actually inconsistent with the new direction, or is this preference?

If the answer is "preference, not inconsistency," it's not a pivot. Point them at the wave-redraft skill.

## Things to never do

1. **Never edit the vision body without bumping `vision_version` and writing a change-log entry.** Silent edits violate the contract.
2. **Never reuse old vision_version numbers.** A vision once at version 3 stays past version 3 forever.
3. **Never edit the wave doc or architecture doc as part of this skill.** Hand off; let the user invoke the appropriate downstream skill.
4. **Never pivot without confirming the trigger with the user.** Even if it seems obvious from a report, explicit confirmation is required.
5. **Never compress multiple changes into one vague change-log entry.** Each section's change gets its own bullet.
6. **Never clear `pivoted` status from this skill.** Only a successful downstream cycle clears it. If you set it, you don't unset it.

## Worked mini-example

Trigger: a wave-audit report from W3 finds that the "solo organizer" role is rejected by every observed real club; clubs have organizing rotations of 2-3 people. The user asks: "we need to pivot — the role model is wrong."

Workflow:

1. Confirm: "You're saying Section 2 (roles) and Section 3 (value hypothesis) need to change to reflect organizing as a shared activity, not a solo one — is that right? This will likely retire the 'single-organizer onboarding wizard' from In Scope and trigger wave-doc reconciliation. Confirm before I edit?"

2. User confirms. Identify changes:
   - §2 Roles: "Solo organizer" replaced with "Organizing group (2-3 co-organizers)".
   - §3 Value hypothesis: rewritten around shared organizing.
   - §4 In scope: "single-organizer onboarding wizard" removed; "co-ownership and handoff" added.
   - §5 Non-goals: "We do not support nested sub-clubs" added (preempts a recurring scope-creep request from the new role model).
   - §6 Success metrics: M2 ("weekly active users") replaced with M4 ("weekly active clubs with ≥ 2 active organizers").

3. Edit the body for those five sections.

4. Bump frontmatter: `vision_version: 1 → 2`, `last_updated: 2026-06-15`, `status: pivoted`.

5. Append change-log entry with old metric text preserved as M2 (retired).

6. Hand off: "Vision pivoted to v2. Wave doc reconciliation required at next wave-redraft. Likely affected: wave doc Goal/Roles, wave ladder (W4 'solo organizer onboarding' may need to be retired or rescoped), assumptions register may need new entries about co-organizer dynamics. Architect-review at next cycle should check whether ADRs about session/auth assume one organizer per club."

That's the shape of a clean pivot.

## Handoff

After saving the pivoted vision, tell the user concisely what changed and what the downstream reconciliation looks like. The next step is theirs — usually invoking `wave-redraft` to produce the `vision-pivot-redraft` that reconciles the wave doc to the new vision.

**Git.** If the project uses git, suggest the user commit with `vision: pivot v<N> — <short description>` and tag `vision-v<N>` after the commit. For high-stakes pivots, suggest doing the cascade on a branch (`pivot/v<N>-<short-name>`) so the reconciliation can be reviewed before merging back to main. Add a `Co-authored-by: Claude <noreply@anthropic.com>` trailer. See `references/git-conventions.md`.
