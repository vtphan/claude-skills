---
name: story-generator
description: Use this skill when the user wants to draft or revise Stories and Requirements in the seed-and-iterate process. Triggered by requests like "generate stories from the journeys," "what should we build for this iteration," "draft the requirements," or any time the user has accepted Journeys and wants to decompose them into deliverable units of work with concrete technical requirements. Also use when the user wants to revise the story set, prune it further, sharpen specific requirements, or update stories based on iteration learning. Do NOT use this skill for drafting Context, Goal, or Journey documents — those have their own skills.
---

# Story Generator

Read the accepted Seed, Context, Goal, and Journeys, and produce a pruned set of Stories with full Requirements. The Story set is the deliverable layer of the design — what gets built, in what order, with what acceptance criteria and what technical specifications.

If a Story set already exists and the user wants it revised, treat existing Stories as input alongside the upstream artifacts. The behavior is the same in both cases: produce a set that traces cleanly to journey moments and Goal scope, with concrete and testable requirements.

## What a Story-and-Requirements document is

A Story is a deliverable unit of work tied to specific journey moments. It captures the user-facing intent ("as a [role], I want [capability], so that [benefit]"), the acceptance criteria, and a list of concrete technical requirements that define what must be built.

Each Story is a single document. Multiple Stories make up a Story set for an iteration.

A Story-and-Requirements document contains:

- **Story statement** — the standard "as a..., I want..., so that..." form.
- **Journey moments served** — explicit references to journey stages this Story addresses.
- **Acceptance criteria** — what "done" looks like from the user's perspective.
- **Requirements** — typed, specified, verifiable technical conditions.
- **Priority** — `must`, `should`, `could`, or `won't` for this iteration.
- **Status** — `draft`, `ready`, `in-progress`, `done`.

Read `~/seed-and-iterate/templates/conventions.md` and `~/seed-and-iterate/templates/story.template.md` before producing output. If those files are not available in the working context, ask the user where they live.

## What you do

Given accepted upstream artifacts (Seed, Context, Goal, Journeys), produce a pruned Story set with complete Requirements. The set must trace cleanly: every Story references journey moments, every Requirement references its Story, and the set as a whole stays within the Goal's scope.

You may:

- **Generate stories from journey moments.** Each journey stage may produce zero, one, or several stories. Friction points and key insights from the Journey are particularly fertile sources.
- **Prune aggressively.** Generate more candidates than survive, then cut. The pruning rationale matters as much as the keeps. Show your cuts.
- **Expand stories into concrete requirements.** Each story must produce testable, quantified requirements with verification methods. Vague requirements are not acceptable.
- **Tie scope to the Goal.** Stories outside the Goal's scope are cut, even if they're valuable — they belong in a future iteration. The out-of-scope list in the Goal is your boundary.
- **Suggest priorities.** `must`, `should`, `could`, `won't`. The Goal's definition of done helps you decide — Stories whose absence would violate the done conditions are `must`.

You may NOT:

- **Generate stories that reference no journey moment.** Every story must trace to at least one. If you find a story you want to include without a journey moment, the journey is incomplete — surface it as a question.
- **Generate stories outside the Goal's scope.** If a story would cross into out-of-scope territory, cut it and note the cut.
- **Produce vague requirements.** "Should be performant" is not a requirement. "Autosave latency from edit to server-side persistence is no more than 500ms at p95" is a requirement.
- **Hide tradeoffs.** If a story's requirements have tension with each other (e.g., a latency target and a throughput target that compete), surface the tension explicitly.
- **Reproduce the entire system.** A Story set for one iteration is bounded by the Goal. Don't generate a hundred stories — generate the set that this iteration needs.

## How to generate candidate stories

Start broad, then prune. The candidate-generation pass should be inclusive; the pruning pass cuts.

For each Journey, walk through the stages and ask:

- **What capability would the system need to support this stage well?** That's a candidate story.
- **What capability would relieve the friction at this stage?** That's another candidate.
- **What capability does the key insight imply?** That's another.
- **What capability does the cross-persona moment require?** That's another, possibly for a different persona.

Many candidates will overlap, be redundant, or be out of scope. That's fine — the next pass cuts them.

The Goal's scope is the most important constraint during pruning. Even excellent stories outside the Goal get cut and noted.

## How to prune

Pruning is where the Story Generator earns its keep. The discipline is to default to fewer stories rather than more.

Cut candidates that:

- **Are out of scope for the Goal.** These belong in a future iteration. Note the cut and tag the would-be story for later.
- **Overlap with another candidate.** Keep one; cut the other; possibly merge them.
- **Don't trace to a journey moment.** If a candidate has no journey grounding, it's probably premature or speculative.
- **Are too small to be a Story.** A story that's a single requirement isn't a story — it's a requirement of a larger story. Fold it in.
- **Are too large to be a Story.** A story whose acceptance criteria spans many concerns is actually multiple stories. Split it.
- **Have unclear user value.** If you can't articulate why this Story matters to a user, cut it.
- **Duplicate existing capability.** If the system already does this, no new story is needed.

After pruning, the Story set should be the smallest set that meets the Goal's definition of done while honoring the Journey insights.

## How to write requirements

Requirements convert user-facing intent into testable technical conditions. Each requirement has:

- **Type:** `functional` (what the system does), `non-functional` (how well it does it — performance, reliability, security), `data` (schema, persistence, exportability), or `edge-case` (failure modes, unusual inputs, boundary conditions).
- **Specification:** what must be true, with concrete numbers and thresholds where applicable.
- **Verification:** how to confirm this is met — automated test, manual test, observation, etc.

Specifications must be quantified where quantifiable. Examples of bad and good:

- *Bad:* "Saves work quickly." *Good:* "Persists edits to server within 500ms at p95, measured from keystroke to server-side write confirmation."
- *Bad:* "Handles network drops." *Good:* "On network failure during save, retries with exponential backoff (initial 1s, max 30s, max 5 attempts), and surfaces a visible indicator if all retries fail."
- *Bad:* "Logs are clean." *Good:* "Event log loss rate is no more than 0.5% across a full assignment cycle, measured by reconciling client-side event sequence numbers against server-side records."

If you can't quantify a requirement, ask whether it's really a requirement or whether it's a value or principle that belongs elsewhere.

A typical Story has three to seven requirements. Fewer means the Story is probably underspecified; more means it might be multiple stories.

## Acceptance criteria vs. requirements

Acceptance criteria are user-facing; requirements are technical. They overlap but aren't the same.

- **Acceptance criteria** answer: "How does the user know this works?" They're observable from outside the system. Example: "After typing in the editor, the student can close the browser, reopen it later, and see their work intact."
- **Requirements** answer: "What technical conditions must hold for this to work?" They're internal to the system. Example: "Autosave persists edits to server within 500ms at p95."

Both are needed. Acceptance criteria validate the Story serves real user value; requirements ensure the implementation is sound.

A useful test: if you stripped the requirements and only had acceptance criteria, could you build the Story? If yes, the requirements are over-specified. If no, the requirements are doing real work.

## Priority

Priority is the iteration-scoped ranking. Use the Goal's definition of done as your guide:

- **`must`:** Absence violates a done condition. The iteration cannot succeed without this Story.
- **`should`:** Absence weakens but does not block iteration success. Important but not load-bearing.
- **`could`:** Nice to have. Doesn't affect iteration success directly.
- **`won't`:** Explicitly deferred. (Rare in a Story set — if a story is `won't`, it usually shouldn't be in the set at all. But sometimes it's useful to keep it visible as a "considered and deferred" item.)

If most of your stories are `must`, scope is probably too tight or the Goal is over-ambitious. If most are `could`, the Goal is probably under-ambitious.

## Decision points

Every Story set delivery includes a set-level "Decision points" section, listing three to seven things the user should react to. The most important decision points for a Story set are usually:

- The cuts (candidates pruned and why).
- The priority assignments (especially `must` vs. `should` boundaries).
- Specific requirements with quantifications the user might want to adjust.
- Stories whose journey moment grounding is weak.
- Tensions between requirements within or across stories.

Format:

```markdown
## Decision points

1. I generated 31 candidate stories and pruned to 14. The cuts are listed below; argue with any of them.
2. I made "autosave" `must` because the Goal's done condition cites no-data-loss. The autosave latency target is 500ms at p95 — adjust if you have stronger or weaker targets in mind.
3. The "instructor manual query interface" story is `must` based on the done condition "Devon can identify a struggling student." Confirm — or do you want this softened to `should` so the iteration can succeed without it?
4. Two stories have weak journey grounding (story-event-schema-versioning, story-deidentification). Both are technically necessary but don't serve a specific journey moment. Accept their inclusion or push back.
5. The "test runner" story has a tension: the Journey says students rely on test feedback, but the Goal's "single recursion assignment" doesn't dictate test richness. I drafted minimal test runner requirements; expand if you want richer student-facing test feedback.
```

## What output looks like

Your output has three parts: the Story set summary, the cuts list, and the Story documents themselves.

### Part 1: Story set summary

Brief overview of the set: number of stories, distribution by priority, journey coverage, and any tensions worth flagging.

### Part 2: Cuts

A clear list of candidates that were pruned, with one-sentence rationale each. Format:

```markdown
## Pruned candidates

- **story-stuck-score** — Out of scope for this Goal (Goal explicitly cuts predictive analytics).
- **story-instructor-dashboard** — Out of scope for this Goal (Goal explicitly cuts the dashboard).
- **story-hint-system** — Out of scope for this Goal (Goal explicitly cuts pedagogical scaffolding).
- **story-classmate-chat** — Not grounded in the current Journey or Seed; would require Seed update.
- **story-mobile-editor** — Out of scope for this Goal (Goal cuts mobile clients).
```

### Part 3: Story documents

Either:

- The full Story documents inline if the set is small (typically up to 6 stories), or
- A summary table plus the full documents linked separately if the set is large.

Each Story document follows the template format with frontmatter, story statement, journey moment refs, acceptance criteria, requirements, priority, and status.

## Examples

### Example 1: First Story set for a new Goal

The user has accepted Seed, Context, Goal, and one or more Journeys. They invoke Story Generator.

You should:

- Generate a broad candidate set from the Journeys.
- Prune to the smallest set that meets the Goal's done conditions.
- Show the cuts prominently.
- Tag priorities based on the Goal's done conditions.
- Surface any stories with weak journey grounding as decision points.

### Example 2: Revising a Story set after Goal change

The Goal has been revised mid-iteration (or a new Goal has been drafted for the next iteration). The user wants the Story set updated.

You should:

- Identify which existing Stories are still in scope, which are now out of scope, and which need revision.
- Identify gaps where the new Goal requires Stories that don't yet exist.
- Update priorities based on the new done conditions.
- Update the change log on each affected Story.
- In the summary, focus on what changed and why.

### Example 3: Sharpening requirements after iteration learning

The user has run an iteration and learned things. They want to update Story requirements based on what they observed.

You should:

- Update specific requirements based on observed reality (e.g., adjust latency targets if observed performance was different from spec).
- Update acceptance criteria if observed user behavior differs from what was anticipated.
- Update source tags on Story documents if applicable.
- Surface any insights that suggest the Journey or Goal should be updated.

## Calibration

**Generating too many stories when:**

- The set is larger than what the Goal's time horizon supports.
- Many stories are `could` priority — they're nice-to-have, not load-bearing.
- The set covers capabilities the Goal explicitly excludes.
- You can't articulate why each Story matters for this iteration.

**Generating too few stories when:**

- The Goal's done conditions cannot be met by the proposed Stories.
- Significant Journey friction points have no Stories addressing them.
- Cross-persona moments are entirely absent from the set.
- The set looks like infrastructure-only without user-facing surface.

The right shape: the smallest set whose completion would meet the Goal's done conditions, with priorities that reflect what's load-bearing versus nice.

## A note on tone

Story documents are working artifacts for engineering. They should be precise and unambiguous, with quantified specifications where possible, and with verification methods that are actually verifiable. Avoid marketing language. Avoid hedging. Each requirement should be something you could write a test for.

When in doubt, prefer concrete to abstract, observable to inferred, smaller to larger.

## What the user does next

After reading your output, the user will:

- Accept the Story set as-is.
- Edit specific stories or requirements and save.
- Reject and ask for substantial revisions.
- Move forward to phase planning and implementation, with the accepted Story set as input.
