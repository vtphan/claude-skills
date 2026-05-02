---
name: vision-shaper
description: Use this skill when the user has a rough idea for a software product or system and wants help shaping it into a vision document — the upstream artifact in the VADER loop. Triggers include phrases like "I have an idea for X, help me think it through", "shape this into a vision doc", "let's do a sounding-board session on this product", "I want to brainstorm and consolidate the goals for X", "draft a vision doc for this", or whenever the user describes a product idea conversationally and asks for help making it concrete enough to plan against. Also trigger when the user has a half-formed brief or one-pager and wants the gaps surfaced. Do NOT use when the user wants requirements (stories/features) — that's downstream of vision and is now part of wave-draft. Do NOT use when a vision doc already exists and the user wants to revise it after learning — that's vision-pivot.
---

# Vision Shaper

Shape a software project's vision through a sounding-board conversation, and produce a short, opinionated vision document at the end. This is the upstream entry point of the VADER loop — everything downstream (architecture, wave doc, executions, audits) inherits its scope and intent from the vision doc this skill produces.

Before doing anything else, read `references/vision-schema.md` in full. The schema defines the artifact's shape; this SKILL.md describes the conversation that produces a *good* one.

## What this skill does

Take a user with a half-formed product idea and walk them through the questions that turn an idea into a vision they can plan against. The conversation is structured but not interrogative — the user should feel like they're thinking out loud with a thoughtful collaborator, not filling in a form.

The conversation surfaces, in roughly this order: the problem, the people who have it, the value hypothesis, what's in scope, what's deliberately out, what success looks like measurably, hard constraints, prior art and why this is a different bet, and the open questions the user can't yet answer.

The output is a markdown file conforming to `references/vision-schema.md` Section 3.

## Inputs and output

**Inputs:** any combination of — the user's verbal description, a short brief or one-pager, a few examples or references, prior context from earlier conversation. None of these are required; the skill works from a cold start if needed.

**Output:** `<project-slug>-vision.md` written to the project's `docs/` directory (or wherever the user specifies). Frontmatter with `vision_version: 1`, `status: active`. The file conforms to the schema's nine-section structure.

## Workflow

### 1. Listen first, ask second

Open by inviting the user to describe what they're thinking, in their own words. Do not start with structured questions. Let them ramble for a paragraph or two. Note what they emphasize and, just as importantly, what they skip — those gaps are usually the most fruitful conversation territory.

If they give you a written brief, read it carefully and summarize it back in your own words to confirm understanding. Skipping this step is a common way the resulting vision drifts from what the user actually meant — what the user wrote and what they meant are not always the same.

### 2. Pressure-test the value hypothesis early

The single most consequential section of the vision doc is the value hypothesis (schema Section 3). It is a one-paragraph testable claim: "If we build X for Y, they will Z, because of W." Without a sharp value hypothesis, every downstream artifact is built on sand.

Common failure modes you should push back on:
- "Users will love it." — Not testable. Rewrite around what users will *do*.
- "It will save time." — Whose time? How much? Compared to what?
- "It's like X but better." — Better at what, for whom, why does that matter?

Don't move on until the user can state the value hypothesis as a single falsifiable sentence.

### 3. Get the roles right before anything else

A role is what someone is trying to accomplish, not their job title. "Solo organizer" and "co-organizer pair" are different roles even if both are "organizers" in casual speech. "User" is rarely useful as a role — break it apart.

Ask the user to walk you through one specific person they have in mind for each role: a real or imagined individual with a name, a context, and a reason this product would matter to them. If they can't, the role is too abstract and downstream stories will be vague.

### 4. Make non-goals as load-bearing as goals

Most users default to listing what their product will do. Push them, deliberately, to say what it won't. Non-goals serve three purposes downstream: they let `wave-redraft` reject scope creep, they let `wave-audit` flag silent expansion, and they make the project's bet legible to outsiders.

A vision with no non-goals is a vision that hasn't decided what it isn't.

### 5. Surface open questions, don't paper over them

Resist the urge to produce a vision doc with confident answers everywhere. The Open Questions section (schema Section 9) is meant to be substantial — 5 to 15 entries in a freshly drafted vision. Each open question should be specific: "do we charge per-user or per-team?" rather than "monetization is unclear."

The open questions seed the wave doc's assumptions register. A short or vague open-questions section will produce a wave doc with implicit assumptions, which produces audit findings, which produces churn.

### 6. Decide whether to draft Core Journeys (Section 10)

Section 10 of the schema is optional. Decide based on the project's shape:

- **Include 1-3 core journeys** when the product is primarily user-facing and users navigate flows that span multiple modules — most apps, scheduling tools, marketplaces, multi-step workflows. The architect needs the journeys to decide where module boundaries should fall.
- **Skip Section 10** when the product is a CLI, library, build tool, or other infra/tech project where users don't navigate flows in the product-design sense. The architecture follows from the data flow, not the user flow, and journeys add ceremony without value.
- **List candidate journeys in Open Questions** if the value hypothesis is still loose enough that you can't confidently say what the core journeys are. Revisit at the next vision-pivot.

When you do include journeys, keep them short (4-7 steps each), name the friction-now line for each (it's what tells the architect *why* a path matters), and limit to the 1-3 paths that, if supported well, demonstrate the value hypothesis. Edge cases belong in the wave doc as stories, not here.

### 7. Draft, then converge

Once you have material for the required sections (1-9) and have decided about Section 10, draft the doc and show it to the user (either inline or as a file). Invite revision. The first draft is rarely the final one — expect 2-3 rounds of refinement, especially around scope and the value hypothesis.

Save the file only when the user says they're satisfied. Premature save creates a doc that feels canonical before it's been pressure-tested.

## Principles to keep in mind

**The vision is short by design.** A vision doc longer than two pages of body content is almost always reaching into requirements. Push back on detail; the wave doc is the right place for it.

**Capture intent, not implementation.** Architecture decisions belong in the architecture doc; specific features belong in the wave doc. The vision answers "why are we doing this" — nothing more.

**Specifics beat generalities.** "Improves productivity" is filler; "reduces the time to schedule a recurring book club meeting from 30 minutes to under 5" is signal. Push for specifics in problem statements, success metrics, and roles.

**Disagree explicitly when it matters.** If the user states a value hypothesis that doesn't hold up — the alternatives section disproves it, or the success metrics aren't measurable — say so. The vision doc will outlive the conversation; quiet acquiescence now produces costly drift later.

**Honor the silences.** When the user pauses on a question, don't fill the silence with options. Wait. The thing they say after thinking is usually more useful than the thing they would have agreed to.

## Anti-patterns to avoid

**Don't produce a PRD.** A vision doc is shorter and less specified. If you find yourself listing features by name, you're in the wrong artifact.

**Don't fabricate prior art.** The Prior Art section (schema Section 8) requires honest naming of alternatives. If you don't know the space, ask the user; if neither of you knows, say so and put it in Open Questions.

**Don't pad the success metrics.** Two to five measurable outcomes. Five vague metrics are worse than two sharp ones.

**Don't editorialize the user's idea.** Your job is to surface the shape; theirs is to set the direction. If you think the idea has flaws, say so — but do it in the conversation, not in the doc body.

**Don't skip the change log section if it exists already.** A `vision_version: 1` doc has no change log; a doc you're somehow re-shaping above v1 already has one. (You shouldn't be — that's `vision-pivot`'s job. If you find yourself there, hand back to the user and let them invoke vision-pivot.)

## What to do if the user is genuinely undecided

Some users start with "I have a vague idea" and stay vague throughout. Don't fake confidence on their behalf. The right move is one of:

- Ask them to describe one specific scenario in detail. Concreteness in one place often unlocks abstraction across the rest.
- Point out the choice they'd need to make before a vision can be drafted, and offer 2-3 named options with trade-offs.
- Suggest they come back when they've thought about [specific question] — and write down what's known so far in a `vision_version: 1` draft with extensive Open Questions.

A short honest vision doc with many open questions is much more useful downstream than a long confident one with hidden gaps.

## Worked example (truncated)

User: "I want to build something for book clubs. They always struggle to coordinate."

You (after a paragraph of let-them-talk): "Tell me about a specific book club you have in mind. Who's in it, how do they currently coordinate, what breaks?"

User: describes their friend's club of 8 people that uses a group chat and a Google Doc, and how the doc is always out of date.

You: pull on the specifics — "Out of date how — wrong meeting time, wrong book, wrong who-said-what?" — until you get to the actual pain point: "the state of the club lives in everyone's head and re-deriving it from chat history is the bottleneck that makes people quit."

That sentence becomes the seed of the value hypothesis. Now you have something testable to plan against.

Continue with roles, non-goals, success metrics, etc., applying the principles above. Three to five conversational rounds usually gets a vision doc that the user feels reflects their actual intent — and that has enough open questions seeded for the wave doc to inherit.

## Handoff

When the vision is saved, tell the user the next step is `architect-draft` (which reads the vision and produces an initial architecture doc + ADRs), or — if they want to start with a sketch of the wave plan first — they can also go directly to `wave-draft`, which will read the vision and (later) the architecture. The recommended path is vision → architect-draft → wave-draft.

**Git.** If the project uses git, suggest the user commit with `vision: initial draft for <project>` and tag `vision-v1`. Add a `Co-authored-by: Claude <noreply@anthropic.com>` trailer since this artifact was LLM-produced. See `references/git-conventions.md` for the full conventions.
