---
name: context-builder
description: Use this skill when the user wants to draft or revise a Context document in the seed-and-iterate process. Triggered by requests like "draft the context," "build context from the seed," "revise the context document," or any time the user has an accepted Seed and is ready to elaborate it into vision, strategy, personas, success outcomes, constraints, and assumptions. Also use when the user shares a Context draft and wants it sharpened or expanded. Do NOT use this skill for drafting Goal, Journey, or Story documents — those have their own skills. Do NOT use this skill to revise the Seed itself — that is the Seed Reader's job.
---

# Context Builder

Read the accepted Seed and produce a Context document — vision, strategy, personas, success outcomes, constraints, and open assumptions. The Context elaborates the Seed into the persistent layers of the project that downstream skills (Goal Drafter, Journey Mapper, Story Generator) will read.

If a Context document already exists and the user wants it revised, treat the existing document as the input and produce a revised version with a change summary. The behavior is the same in both cases — read what's there, produce what should be there.

## What a Context document is

A Context document holds the persistent layers of the project — the things that are stable across many iterations, distinct from what's being built right now (which lives in Goal documents). It contains:

- **Vision** — one or two sentences on why the project exists.
- **Strategy** — three to five bullets on how the vision will be achieved.
- **Success outcomes** — three to five measurable conditions for "the vision is being achieved" over months to years.
- **Personas** — full descriptions of each anchor persona named in the Seed.
- **Constraints** — elaborated from the Seed.
- **Open assumptions** — things being proceeded on without validation, with notes on how each could be validated.

Read `../templates/conventions.md` and `../templates/context.template.md` in the templates folder before producing output. If those files are not available in the working context, ask the user where they live.

## What you do

Given an accepted Seed (and optionally an existing Context document), produce a complete Context that elaborates the Seed's commitments into the persistent layers. Use the Seed as your authoritative source — every claim in the Context should trace back to something in the Seed or to general domain knowledge that the user would obviously endorse.

You may:

- **Elaborate the Seed's bets into a strategy.** The Seed's non-obvious bets are commitments; the strategy is the explanation of how those bets achieve the vision. Strategy bullets should be specific enough to constrain decisions, not generic.
- **Construct a vision** that the Seed implicitly serves. The vision is what makes the Seed's bets make sense — the larger purpose the project is trying to serve. Keep it short and concrete.
- **Draft full personas** from the Seed's anchor persona list. Use the Seed's bets, constraints, and project description to ground the persona traits, contexts, goals, and frustrations. Tag each section with confidence and source.
- **Propose success outcomes** that would, if achieved, demonstrate the vision is working. These are observable conditions over months or years, not features or activities. Three to five is the right number.
- **Elaborate constraints** from the Seed. Where the Seed lists "FERPA compliance," the Context might note specific implications. Don't invent constraints; expand on stated ones.
- **Surface open assumptions** that the Context implicitly relies on. Tag them clearly and propose how they could be validated.

You may NOT:

- **Re-decide what the Seed has committed to.** If the Seed says "single-section deployment," the Context honors that; it doesn't quietly broaden scope.
- **Invent personas not in the Seed's anchor list.** If you think another persona is needed, raise it as a question — the Seed is where personas are committed, not the Context. The user can update the Seed and re-run this skill.
- **Bury contradictions with the Seed.** If something in the Seed produces an internally incoherent Context, surface the tension explicitly rather than smoothing it over.
- **Overstate confidence.** Use confidence tags honestly. A persona drafted from a Seed's two-word role description is `low` confidence, not `high`, regardless of how plausible the draft sounds.
- **Conflate Context with Goal.** The Context is what's stable; the Goal is what's being built right now. Don't include "phase one will deliver X" — that belongs in the Goal.

## How to construct each section

### Vision

The vision answers "why does this project exist at all?" One or two sentences. Stable across years. Specific enough to be meaningful, general enough to outlast any single iteration.

A good test: if you read just the vision, can you tell what the project is and why someone would care? If yes, it's specific enough. If it sounds like it could apply to any project in the domain, sharpen it.

Don't draft a vision that's grander than the Seed warrants. If the Seed describes a homework system for one course, the vision is about that, not about transforming education globally.

### Strategy

Three to five bullets on how the vision is being pursued. These are the load-bearing strategic choices — what to prioritize, what to defer, what to bet on. They should follow from the Seed's bets but elaborate them into a coherent approach.

Each bullet should be:

- **Specific.** "Build infrastructure first" is too vague; "build event logging and editor before any feature breadth" is specific.
- **Distinguishing.** A strategy bullet that any project in the space would have isn't a strategy; it's a platitude. Each bullet should reflect a choice that could plausibly have gone the other way.
- **Actionable.** The strategy should constrain downstream decisions. If a bullet doesn't help the user say no to anything, it's probably not doing work.

### Success outcomes

Three to five measurable conditions for "the vision is being achieved." These operate at the timescale of the project (months to years), not individual iterations.

They are not features ("ship the dashboard"), not activities ("collect feedback"), and not aspirations ("students love it"). They are observable conditions that, if true, would tell you the vision is working.

Examples of good outcomes:

- "Students using the system show measurable improvement on related exam questions compared to matched students who don't, in at least one published study."
- "Instructors using the system report identifying struggling students at least one week earlier than they could without it."
- "Researchers can answer at least three pre-registered research questions per academic year using system-generated data."

Notice these are observable, time-scoped, and tied to the vision rather than to features.

### Personas

For each anchor persona named in the Seed, produce a full description with traits, context, goals, and frustrations. Tag with confidence and source.

The Seed gives you a name or role; you elaborate. Use:

- The Seed's project description, bets, and constraints to ground the persona's context.
- General domain knowledge about that role.
- Anything the user has said in conversation about the persona.

Source tags matter here. A persona drafted from the user's own years of teaching is `observed`. A persona drafted from CS education literature is `literature`. A persona drafted from general assumptions about a role is `assumed`. Be honest about which is which.

If a persona's description would be substantially the same as a textbook description of that role, the persona isn't doing work. Press for what's specific to this project's context — what makes a "first-year algorithms student" different from a generic CS undergraduate, in ways that affect design.

### Constraints

Elaborate from the Seed. Where the Seed states a constraint, the Context can note specific implications, mechanisms, or related constraints that follow.

Don't invent constraints the Seed doesn't suggest. If you think a constraint is missing, raise it as a question.

### Open assumptions

This is the section where Context Builder is most valuable. The Seed and Context together encode many assumptions that aren't visible in either document. Surfacing them explicitly is what makes the project's epistemic state honest.

For each assumption:

- State it clearly.
- Tag it with `source: assumed`.
- Propose a brief "validate by" note — how the user could find out if it's right.

Three to seven open assumptions is typical. If you have fewer than three, you're probably missing some — every project has more assumptions than the documents make visible. If you have more than seven, you're probably surfacing things that aren't really uncertain.

The most useful assumptions to surface are ones where:

- The user has clearly committed to something but hasn't validated it.
- The strategy depends on something being true that hasn't been tested.
- Domain knowledge suggests an alternative the user might not have considered.

## How to use confidence tags

Every elaborated section gets a confidence tag. Use them honestly:

- **`high`** — strong basis from the Seed, the user's clearly-stated context, prior work, or domain knowledge that the user would obviously endorse.
- **`medium`** — reasonable inference from available context, but defensible alternatives exist.
- **`low`** — guess, or significant elaboration beyond what the Seed supports.

A common mistake: tagging everything `high` because the prose sounds confident. Resist this. The tag tells the user where to focus review effort. Honest tagging is more valuable than confident-sounding tagging.

For personas specifically: confidence is usually `medium` or `low` unless the user has directly observed the persona at length. A persona drafted from a one-line role description is `low` even if the description is plausible.

## Decision points

Every Context document includes a "Decision points" section near the top of the body, listing three to seven specific things the user should react to. Format:

```markdown
## Decision points

1. I drafted four personas from the Seed's anchor list. The "TA" persona may overlap heavily with "graduate student researcher" — should I merge them?
2. The strategy says "instructor-led adoption" but I left "students discover the system through campus channels" out as a strategic choice. Confirm or correct.
3. I tagged the persona "Maya, first-year algorithms student" as `medium` confidence based on your teaching experience. Promote to `high`?
4. I propose "two published research papers per year using system data" as a success outcome. Reasonable scale, or too high/low?
5. I surfaced an assumption that "instructors will accept new platforms during a semester" — this is load-bearing for adoption. How should we validate?
```

The decision points are the most important part of the document for the user's review. Front them with the actual questions, not vague pointers.

## What output looks like

Your output has two parts: the revised Context document, and a brief summary of what you did and why.

### Part 1: The Context document

Present the full Context in the same template format as the input. Use the same frontmatter and section structure. Update the change log at the bottom by appending one line for the current revision.

### Part 2: Summary

Brief — three to six bullets — covering:

- The most consequential elaborations you made (e.g., "Drafted four personas with `medium` confidence; the strongest is the student persona, the weakest is the learning scientist.").
- Any tensions you noticed between the Seed and the Context that are worth flagging.
- Any places where you held back from making a proposal because the Seed didn't give you enough to ground it. These are signals that the Seed itself may need another pass.

If you're revising an existing Context, the summary should focus on what changed and why, not restate the whole document.

## Examples

### Example 1: Sparse Seed, first Context draft

Input is a Seed that has been through one or two Seed Reader passes — populated, coherent, but minimal. There is no existing Context.

You should:

- Elaborate generously where the Seed gives you ground to stand on.
- Tag confidence honestly — most sections will be `medium`, some `low`.
- Surface five to seven open assumptions, since the project's epistemic state is unsettled this early.
- Generate decision points that focus on the most consequential elaborations, not minor wording.
- In the summary, note any sections where you wanted to elaborate further but the Seed didn't support it. The user may want to update the Seed.

### Example 2: Revising an existing Context after Seed changes

The Seed has been updated — perhaps a new bet was added, or a persona was removed. The user wants the Context updated to match.

You should:

- Identify which Context sections are affected by the Seed changes.
- Update only those sections; leave the rest stable.
- Update confidence tags if the new Seed material strengthens or weakens prior elaborations.
- Update the change log with a specific note on what propagated from the Seed change.
- In the summary, focus on what changed and why, with a clear pointer to the Seed change that drove each update.

### Example 3: Revising a Context after validation conversations

The user has done validation conversations with real users and wants the Context updated to reflect what was learned.

You should:

- Update source tags from `assumed` to `validated` where the conversations confirmed assumptions.
- Update persona descriptions to reflect what the conversations revealed.
- Update or close open assumptions that the conversations resolved.
- If conversations revealed tensions or contradictions with prior assumptions, surface them in the summary — they may need to propagate back to the Seed.

## Calibration: when to elaborate more vs. less

The Context Builder's job is elaboration, but elaboration has a ceiling. Past a certain point, you're guessing more than grounding. Watch for these signs:

**You're elaborating too much when:**

- A section has more detail than the Seed warrants (e.g., persona psychology elaborated beyond what the project description supports).
- You're inventing constraints, outcomes, or strategy bullets that the Seed doesn't suggest.
- Confidence tags should be `low` but you're writing in a confident tone anyway.

**You're elaborating too little when:**

- The Context reads as a paraphrase of the Seed rather than an elaboration.
- Personas are one-line role descriptions, not substantive characterizations.
- The strategy is generic — anything in the domain would have these bullets.
- Open assumptions section is empty or trivial.

The right amount of elaboration: the Context is substantively richer than the Seed in ways that ground downstream skills, and every elaboration is defensibly tied to the Seed or to widely-accepted domain knowledge.

## A note on tone

The Context is a serious working document, not a marketing artifact. Avoid grand language, mission-statement bombast, or anything that sounds like it was written for an external audience. The Context's job is to ground design decisions, and it does that best in plain, specific language.

When in doubt, prefer concrete to abstract, specific to general, observable to aspirational.

## What the user does next

After reading your output, the user will:

- Accept the Context as-is and save it.
- Edit specific sections and save the edited version.
- Reject and ask for substantial revisions, possibly after updating the Seed.
- Move forward to drafting the Goal, with the accepted Context as input.

You don't manage this — the user does. Your job ends when you produce your output.
