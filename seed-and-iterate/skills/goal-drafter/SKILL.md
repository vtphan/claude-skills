---
name: goal-drafter
description: Use this skill when the user wants to draft or revise a Goal document in the seed-and-iterate process. Triggered by requests like "draft the goal," "what should we build first," "scope the next iteration," or any time the user has an accepted Context and is ready to commit to what to build in the current iteration. Also use when the user shares a Goal draft and wants it sharpened, when they want to close a current Goal and start the next one, or when iteration learning suggests the Goal needs revision. Do NOT use this skill for drafting Context, Journey, or Story documents — those have their own skills. Do NOT use this skill to revise the Seed — that is the Seed Reader's job.
---

# Goal Drafter

Read the accepted Seed and Context, plus any indication from the user about what they want to achieve in this iteration, and produce a Goal document. The Goal commits to what is being built or learned in the current iteration — bounded scope, explicit cuts, observable definition of done.

If a Goal document already exists and the user wants it revised, treat the existing document as the input and produce a revised version with a change summary. The behavior is the same in both cases.

## What a Goal document is

A Goal answers "what specifically am I building right now, in this iteration, and how will I know when I'm done?" It is the most consequential single artifact in the process for keeping the project from drifting, because it converts open-ended strategy into bounded commitment.

A Goal is iteration-scoped. There is one current Goal at a time. New Goals are written for each iteration; past Goals are archived but not edited.

A Goal contains:

- **Statement** — one or two sentences on what specifically is being built or achieved.
- **In scope** — explicit list of what is being built or addressed.
- **Out of scope** — explicit list of what is deliberately not being built in this iteration.
- **Definition of done** — concrete, observable conditions for "this goal is achieved."
- **Time horizon** — rough timeframe (weeks to months).
- **Linked context** — which vision elements, strategic bets, success outcomes, and personas this goal serves.
- **Success signals** — observable signals at the goal's timescale that tell you whether the goal is on track.
- **Open questions** — what completing this goal might answer.

Read `~/seed-and-iterate/templates/conventions.md` and `~/seed-and-iterate/templates/goal.template.md` before producing output. If those files are not available in the working context, ask the user where they live.

## What you do

Given an accepted Seed and Context (and any user input about iteration intent), produce a Goal that converts strategic commitments into a bounded iteration commitment. The Goal must be small enough to actually achieve in its time horizon and large enough to deliver meaningful learning or value.

You may:

- **Propose the iteration's scope** based on the Context's strategy, the Seed's bets, and any user input about what to focus on. If the user says "first pilot," that's a strong signal about scope; if they say nothing, infer from the Context what would be the most valuable first commitment.
- **Aggressively cut scope** in the out-of-scope section. The out-of-scope list is the most important part of the Goal — it's where you say "yes, these things matter and we're not doing them now." Cutting too little is the most common failure mode.
- **Define done observably.** Done conditions should be things that will be true or false after the iteration, not things that will be "in progress" or "improved." If a condition can't be checked at the end, it doesn't belong.
- **Pick a time horizon honestly.** Estimate based on the scope, not the deadline you'd like. A scope that takes three months should not have a one-month time horizon just because the user wants to ship sooner.
- **Tie back to Context.** Every Goal must serve specific elements of the Context's strategy and outcomes. If you can't articulate which strategic bets this Goal advances, the Goal is probably misaligned.

You may NOT:

- **Re-decide what the Seed or Context has committed to.** If the Context says "single-section pilot," the Goal honors that; it doesn't quietly broaden scope.
- **Conflate Goal with vision or strategy.** The Goal is what's being built right now, not the long-term aspiration. Don't restate the vision.
- **Write a Goal that just describes the whole project.** A Goal that says "build the homework system" isn't a Goal — it's the project. A Goal that says "build the editor and event pipeline for one assignment in the algorithms course" is a Goal.
- **Define done using leading indicators rather than trailing ones.** "Started using the system" is a leading indicator; "completed at least one assignment cycle with N students" is a trailing one. Trailing wins.
- **Hide ambiguity.** If you're not sure what scope makes sense, surface the question rather than guessing.

## How to scope a Goal

Goal scoping is the most consequential skill the Goal Drafter exercises. A few principles:

**Default to smaller.** When you're not sure whether to include something, leave it out. You can always add scope in the next iteration; you can't recover the time spent on too-large scope this one.

**Choose what de-risks the most.** A Goal should reduce the project's biggest uncertainty. For an early iteration, that's usually the load-bearing infrastructure (data layer, auth, core flows). For later iterations, it might be a specific feature, a specific user behavior question, or a specific integration.

**Choose what teaches the most.** Goals are also learning instruments. A Goal whose successful completion would teach you something important about the project (what users actually do, whether a hypothesis holds, whether a technical approach works) is worth more than one whose completion just adds capability.

**Keep the time horizon honest.** A Goal scoped for "six to ten weeks" is more honest than "six weeks" if you don't actually know. Ranges are fine.

**Be ruthless about out-of-scope.** Each item in out-of-scope should be something a reasonable person might assume is in scope. If your out-of-scope items are obvious non-features, they're not doing work. If they're tempting features that you're explicitly excluding, they're doing work.

## Definition of done

Definition of done is where Goals most often go wrong. Common failures:

**Vague completion criteria.** "The system works for students" is not done. "At least 8 students in the algorithms course completed at least one homework assignment using the system, with full event capture and no greater than 0.5% data loss" is done.

**Aspirational criteria.** "Students learn better" is not a Goal-level done condition; it's a project-level outcome. Goal-level conditions are about what's been built and observed in this iteration, not about long-term effects.

**Done = "shipped."** Shipping is necessary but not sufficient. A Goal whose done condition is just "shipped to users" doesn't tell you whether the iteration succeeded. Add the conditions that distinguish a successful iteration from a shipped-but-unsuccessful one.

**Too many conditions.** Three to six done conditions is typical. More than that, and you're probably mixing levels.

A useful test: read the done conditions and imagine answering "yes" or "no" to each one at the end of the iteration. If you couldn't honestly answer because the condition is vague or aspirational, rewrite it.

## Linked context

Every Goal references specific elements of the Context. This is the traceability that makes the Goal accountable to strategy.

For each linked element:

- **Vision served** — which part of the vision does this iteration advance?
- **Strategy bets served** — which strategic bets does this iteration enact or test?
- **Success outcomes contributed to** — which long-term outcomes does completing this Goal move toward?
- **Primary personas** — which personas are central to this iteration's work?

If you can't articulate at least one strategic bet this Goal serves, the Goal is probably misaligned with the Context. Surface the misalignment as a question.

## Open questions

Goals should usually have one to three open questions — things that completing the Goal will help answer. These are different from the Seed's open questions (which are about what the project should commit to). Goal-level open questions are about what the iteration will reveal.

Examples:

- "Is the autosave cadence fast enough that students don't lose work in practice?"
- "Does the stuck-score signal correlate with intervention-worthy moments?"
- "Is the event volume from a single section sustainable on existing infrastructure?"

Surfacing these makes the Goal partly a learning artifact, not just a delivery artifact.

## Decision points

Every Goal document includes a "Decision points" section near the top of the body, listing three to seven specific things the user should react to. The most important decision points for a Goal are usually:

- The scope cuts (out-of-scope items the user might disagree with).
- The definition of done (whether the conditions are right).
- The time horizon (whether the estimate is honest).
- Any tension between the proposed Goal and the Context.

Format:

```markdown
## Decision points

1. I cut "TA queue" from this iteration based on the Seed's out-of-scope list and the focus on infrastructure. Confirm or push back?
2. The done condition "at least 8 students completed an assignment" assumes you'll have that many in the section. If the section is smaller, this needs to change — what's the realistic minimum?
3. I scoped this iteration at 6-10 weeks. Honest, or should it be shorter or longer?
4. The Goal serves three of the four strategic bets but not "research utility." Should this iteration make at least token progress on research utility (a clean export at minimum), or is that explicitly deferred?
```

## What output looks like

Your output has two parts: the Goal document, and a brief summary.

### Part 1: The Goal document

Present the full Goal in the same template format. Use stable IDs and proper frontmatter. Update the change log if revising.

### Part 2: Summary

Three to six bullets covering:

- The most consequential scope decisions you made (especially cuts).
- Any tension between the proposed Goal and the Context that's worth flagging.
- The reasoning behind the time horizon, if it's not obvious.
- Anything you held back from including because the Context didn't support it.

## Examples

### Example 1: First Goal of a new project

The user has an accepted Context and is starting iteration one. There is no prior Goal.

You should:

- Propose a scope that focuses on de-risking and learning, not breadth.
- Be aggressive about out-of-scope — most things should be cut.
- Choose done conditions that demonstrate the load-bearing infrastructure works, not that all features exist.
- Tie linked context back to early-iteration strategic bets (often infrastructure-first or learning-oriented bets).
- Time horizon: usually weeks to a couple of months for a first iteration.

### Example 2: Goal for an iteration after a completed previous one

A previous Goal was completed (or partially completed) and the user wants to draft the next.

You should:

- Read the prior Goal and any iteration notes the user provides about what was learned.
- Build on what was completed; don't re-do prior work.
- Address things the prior iteration revealed but didn't resolve.
- Continue the strategic arc; don't pivot without reason.
- Reference the prior Goal in the change log or summary, not in the new Goal's content.

### Example 3: Revising a Goal mid-iteration

The user is partway through an iteration and reality has diverged from the plan. They want to revise the Goal.

You should:

- Be cautious about expanding scope mid-iteration. Usually the right move is to cut, not add.
- If something has been learned that changes what's worth building, surface it explicitly.
- Update the change log with what changed and why.
- If the revision is substantial, ask whether closing this Goal and starting a new one would be cleaner than revising.

## Calibration

**You're scoping too large when:**

- The done conditions describe most of what the system will eventually do.
- The time horizon stretches past three months.
- The out-of-scope list is short or obvious.
- You can't articulate one or two specific things this iteration will teach.

**You're scoping too small when:**

- The done conditions are entirely about infrastructure with no user-facing surface.
- The Goal serves no strategic bet beyond "build the basics."
- The iteration would produce nothing observable to the user.
- You can't imagine learning anything from completing it.

The right size: small enough to ship in its time horizon, large enough to test something meaningful, with cuts that actually do work.

## A note on tone

A Goal is a commitment artifact. It should read with crispness and confidence — not aspirational language, not hedging, not marketing. Plain statements of what will be built and how completion will be checked.

When in doubt, prefer concrete to abstract, observable to aspirational, smaller to larger.

## What the user does next

After reading your output, the user will:

- Accept the Goal as-is.
- Edit specific elements (often the scope or done conditions) and save.
- Reject and ask for substantial revisions, possibly after updating the Context or Seed.
- Move forward to drafting Journeys for this Goal.
