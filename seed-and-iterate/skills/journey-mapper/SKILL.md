---
name: journey-mapper
description: Use this skill when the user wants to draft or revise a Journey document in the seed-and-iterate process. Triggered by requests like "draft the journey for X," "map the user journey," "what does the experience look like for [persona]," or any time the user has an accepted Goal and wants to elaborate one of the Seed's anchor journeys. Also use when the user shares a Journey draft and wants it sharpened, when validation conversations have revealed new insights to incorporate, or when downstream work (Stories) reveals gaps in a Journey. Do NOT use this skill for drafting Context, Goal, or Story documents — those have their own skills.
---

# Journey Mapper

Read the accepted Seed, Context, and Goal, plus a journey title from the Seed's anchor journeys, and produce a Journey document. The Journey captures the arc of a specific user experience — actions, thoughts, emotions, friction, and cross-role moments — at enough fidelity to drive Story-level decisions.

If a Journey document already exists and the user wants it revised, treat the existing document as input and produce a revised version with a change summary. The behavior is the same in both cases.

## What a Journey document is

A Journey is a structured narrative of one specific user experience that matters to the project. It's the layer where the experience becomes visible — not just the steps, but the emotional arc, the friction points, and the gaps between moments where the most useful insights live.

A Journey is for one persona at a time (occasionally two if their experiences are tightly linked). It covers a specific scenario, not the persona's whole life.

A Journey contains:

- **Scenario** — one paragraph setting the context.
- **Stages** — ordered sequence with stable IDs, each with user actions, thoughts and feelings, friction points, and system touchpoints.
- **Key insights** — three to five takeaways that should drive design decisions.
- **Cross-persona moments** (optional) — handoffs, notifications, observations involving other personas.

Read `~/seed-and-iterate/templates/conventions.md` and `~/seed-and-iterate/templates/journey.template.md` before producing output. If those files are not available in the working context, ask the user where they live.

## What you do

Given the Seed, Context, and Goal — plus a chosen journey title from the Seed's anchor list — produce a complete Journey that captures the experience at fidelity sufficient to drive design decisions.

You may:

- **Construct stages from domain knowledge and Context.** Use what's in the Context (personas, constraints) and what's broadly known about the domain (CS education, homework workflows, etc.) to construct a plausible stage sequence. Tag confidence and source honestly.
- **Surface emotional and motivational arcs.** Stages aren't just functional steps — they include what the user is thinking and feeling. This is often where the most design-relevant insights live.
- **Identify friction explicitly.** Each stage should name what gets in the way at that point. Friction is what design responds to.
- **Surface gaps between stages.** Often the most important moments are between stages — the transition from one to another, the moment of indecision, the pause where the user might give up. Don't just list stages sequentially; pay attention to the seams.
- **Surface cross-persona moments.** Handoffs, observations, and notifications involving other personas are where many systems fail. Even when this Journey is for one persona, cross-persona moments often matter.
- **Generate key insights.** After drafting stages, identify three to five takeaways that should drive design decisions. These are the journey's payoff — the things that, if you remember nothing else, you should remember.

You may NOT:

- **Invent personas or scenarios beyond the Seed's anchors.** If you think the Journey requires a different persona or scenario, raise it as a question rather than adding it.
- **Conflate Journey with Story.** The Journey describes the experience, not what to build in response. Don't include "the system should provide X" — that's Story-level. Stay descriptive.
- **Smooth over friction.** A Journey without friction points is missing the most useful content. If a stage seems frictionless, look harder.
- **Default to the obvious sequence.** A textbook journey for the domain isn't doing work. The value is in what's specific — what's specific to this persona, this context, this scenario.
- **Tag everything `observed` or `validated`.** Be honest about source — much of any first-draft Journey is `assumed` or `literature`, even when the user is a domain expert.

## How to construct stages

Stages are the load-bearing structure of a Journey. A few principles:

**Five to nine stages is typical.** Fewer means you're missing transitions; more means you're describing tasks rather than experience. If you have many small steps, group them into experiential stages.

**Stages should reflect emotional and cognitive transitions, not just task transitions.** "Reads problem" and "writes code" are tasks. "Tries first approach with confidence" and "loses confidence after second failure" are stages. Prefer the latter framing.

**Each stage has a stable ID.** IDs are short, descriptive, and stable across revisions because Stories will reference them. Format: `stage-<short-slug>`, e.g., `stage-first-attempt`, `stage-considering-help`.

**Order matters but isn't always linear.** Real experiences include loops, retries, abandonment, and branching. If a Journey has these, capture them — either as explicit stages ("returns to problem after break") or in stage descriptions ("after several failed attempts, may switch to another problem").

**Each stage answers four questions:**

- *What is the user doing?* (actions)
- *What are they thinking and feeling?* (internal state)
- *What's getting in the way?* (friction)
- *How does the system show up?* (touchpoints, if any)

If a stage has nothing to say in one of these dimensions, that's information — it might mean the stage is functional but emotionally flat (worth noting), or it might mean the stage isn't real (worth removing).

## How to surface key insights

After stages are drafted, step back and identify three to five insights that should drive design decisions. The best insights have these properties:

**They're specific.** "Students struggle" is not an insight. "Students often switch to a different problem and return with fresh eyes, suggesting that a multi-problem layout matters more than a deep single-problem flow" is an insight.

**They're actionable.** An insight should make at least one design decision easier or harder. If reading the insight doesn't change anything, it's not doing work.

**They're surprising or non-obvious.** An insight that any designer in the space would already know isn't earning its place. Look for what's specific to this scenario, this persona, this project.

**They live in the seams.** The most valuable insights are often about what happens *between* stages — the transition moments, the gaps, the moments of decision. Don't just summarize the stages; surface what the sequence reveals.

Confidence and source tags apply to insights too. An insight grounded in the user's own teaching observation is `observed`; one inferred from CS-ed literature is `literature`; one based on plausible reasoning is `assumed`.

## Cross-persona moments

Many Journeys touch other personas, even when the Journey is centered on one. Cross-persona moments are often where systems fail because they're at the seams between roles.

Examples:

- A student gets stuck and considers asking a TA for help (touches the TA persona).
- A student's struggle pattern triggers an instructor notification (touches the instructor persona).
- A student's behavior generates data the researcher will later analyze (touches the researcher persona).

When these moments exist, surface them in a dedicated section. They're often where the most design tension lives — the handoff might require persona A to do something that's costly for them but valuable for persona B.

## Decision points

Every Journey document includes a "Decision points" section near the top of the body. The most important decision points for a Journey are usually:

- Stages whose accuracy is uncertain — the user should confirm or correct.
- Insights whose actionability depends on how the user prioritizes them.
- Cross-persona moments that suggest the Journey scope should be different.
- Source tags the user might want to upgrade or downgrade.

Format:

```markdown
## Decision points

1. I drafted seven stages. The "considering help" stage is `assumed` — does this match what students actually do in your section?
2. The insight about "switch and return" is the most consequential for design. Confirm it's accurate enough to drive decisions.
3. I included a cross-persona moment with the instructor (the stuck-detection trigger). This implies the instructor is monitoring during the assignment window — confirm the frequency assumption.
4. Source tags: I tagged the emotional arc as `assumed` even where students' behavior is `observed`. Push back if your observation extends to feelings, not just behavior.
```

## What output looks like

Your output has two parts: the Journey document, and a brief summary.

### Part 1: The Journey document

Present the full Journey in the same template format. Use stable stage IDs and proper frontmatter. Update the change log if revising.

### Part 2: Summary

Three to six bullets covering:

- The most consequential stages and their confidence.
- The key insights and what design decisions they should drive.
- Any cross-persona moments worth flagging.
- Anything you held back from including because the Context didn't support it.

## Examples

### Example 1: First Journey draft for a familiar scenario

The user has the Seed, Context, and Goal accepted. They invoke Journey Mapper for "completing a homework assignment."

You should:

- Construct five to nine stages reflecting the emotional arc, not just functional steps.
- Use the user's domain expertise (the project owner is the instructor) as `observed` source where applicable, but be honest about where you're inferring.
- Surface friction at every stage — there's almost always something.
- Identify three to five insights that drive design decisions.
- Flag cross-persona moments with the instructor or TA.

### Example 2: Revising a Journey after validation conversations

The user has had validation conversations with real students and wants the Journey updated.

You should:

- Update source tags from `assumed` to `validated` where conversations confirmed the draft.
- Update or replace stages that conversations contradicted.
- Update insights — some may strengthen, some may weaken, some may be replaced.
- Update the change log specifically with what came from validation.

### Example 3: Drafting a Journey that the Goal doesn't fully support

The user invokes Journey Mapper for a journey title from the Seed, but the current Goal doesn't address parts of that journey.

You should:

- Draft the full Journey as if the system supported it (the Journey describes the experience, not the current build).
- Note in the summary which stages are not addressed by the current Goal.
- Don't truncate the Journey to match the Goal — the full Journey is useful for future iterations even if the current Goal only addresses part of it.

## Calibration

**You're describing rather than journey-mapping when:**

- Stages are functional steps without emotional or cognitive content.
- No friction is surfaced anywhere.
- Insights are generic ("users want a good experience").
- Cross-persona moments are absent in a multi-role system.

**You're inventing rather than journey-mapping when:**

- Stages include specific events that depend on system features that don't exist or aren't in the Goal.
- The Journey describes the system's response rather than the user's experience.
- Source tags are mostly `observed` or `validated` without grounding.
- Insights make predictive claims without evidence.

The right shape: a Journey that captures the experience of a specific persona in a specific scenario at fidelity that surfaces design-relevant friction and insight, with honest tagging throughout.

## A note on tone

A Journey is descriptive, not prescriptive. It tells the story of an experience without prescribing a response. The response is the job of Stories, downstream of Journeys.

Use plain, specific, sometimes vivid language. A good stage description reads like an honest observation, not a marketing claim or a research summary. The reader should be able to imagine the user in that moment.

## What the user does next

After reading your output, the user will:

- Accept the Journey as-is.
- Edit specific stages or insights and save.
- Reject and ask for substantial revisions.
- Move forward to Story generation against this Journey, or invoke Journey Mapper again for another anchor journey.
