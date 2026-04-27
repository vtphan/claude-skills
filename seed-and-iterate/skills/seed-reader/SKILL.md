---
name: seed-reader
description: Use this skill when the user wants to revise, refine, or sharpen a Seed document in the seed-and-iterate process. Triggered by requests like "review my seed," "revise the seed," "what should I add to the seed," or any time the user shares a seed.md and wants feedback on it. Also use proactively at the start of an iteration when a Seed exists and the user is preparing to draft Context, Goal, or Journey documents — propose a Seed Reader pass first to make sure the seed is in good shape. Do NOT use this skill for drafting Context, Goal, Journey, or Story documents — those have their own skills.
---

# Seed Reader

Read the current Seed document and produce a revised version that, in your judgment, better reflects what the seed should be. Present the revised seed alongside a short summary of what changed and why.

## What a Seed is

A Seed is the minimum specification a human commits to for a project. It captures the decisions only the human can make — the non-obvious bets, what's out of scope, constraints the AI cannot infer, anchor personas, anchor journeys, and open questions. It is short — typically one page — and uses bullet points and short phrases rather than prose.

Read `../templates/conventions.md` and `../templates/seed.template.md` in the templates folder to understand the schema, file format, and tagging conventions before producing any output. If those files are not available in the working context, ask the user where they live.

## What you do

Given a current Seed (which may be sparse, partial, contradictory, or already polished), produce a revised version that better reflects what the seed should be. You have wide latitude here — your job is to use good judgment about what the seed needs.

You may:

- **Add items** the seed seems to be missing — bets that follow from what's already there, out-of-scope items the seed should make explicit, constraints the user mentioned in conversation but didn't write down, personas implied by the project description, journeys implied by the bets and personas, or open questions the seed is silently glossing over.
- **Sharpen vague language** — replace "support multiple users" with "support up to 30 students per section," replace "be performant" with concrete speed goals, replace "research-friendly" with the specific research uses being supported.
- **Flag and resolve contradictions** — if the bets say "infrastructure-first" but an anchor journey is content-authoring, surface the tension and propose a resolution.
- **Surface implicit decisions** — if the user has clearly committed to something in conversation but it's not in the seed, propose adding it.
- **Restructure** if the seed has drifted — items in the wrong section, redundancy across sections, sections that have grown too large.
- **Remove** items that no longer fit, that duplicate other items, or that are too vague to be useful.

You may NOT:

- Silently accept your own proposals. Every change is a proposal until the user commits.
- Resolve open questions on the user's behalf. You can propose candidate answers and explain tradeoffs, but the choice is the user's.
- Paraphrase content the user wrote into something different in meaning. Preserve their phrasing where they've clearly committed.
- Expand the seed beyond its purpose — it should stay short, even after revision. If you'd be writing paragraphs, that content belongs in a drafted document (Context, Goal, etc.), not the seed.

## How to make proposals

The seed cycle works because the user can review proposals quickly. To make that fast:

- **Be specific.** "Consider adding 'single-section deployment' as a constraint" is reviewable. "The constraints section could be expanded" is not.
- **Be opinionated by default.** When you're uncertain, commit to a specific proposal rather than asking an open question. The user can reject; that's cheaper than answering "what should this be?"
- **Show your reasoning briefly.** One sentence per substantial change. Not paragraphs of justification.
- **Distinguish strong proposals from suggestions.** If you think something is missing and important, say so plainly. If you're floating an idea, say that.

## How to handle open questions

When the seed contains open questions, or when you identify a question that should be open:

- Propose two or three candidate resolutions if you can.
- Note the tradeoff between them in one short sentence each.
- Make a recommendation only if you have a clear basis for one — otherwise leave the choice to the user.
- Never silently resolve an open question by writing it as a decided item.

## How to handle the non-obvious bets

The bets are the most important section of the seed because they distinguish this project from a generic version of it. Be especially careful here:

- If you propose a new bet, it should be one the user could plausibly hold but might not have surfaced. Don't invent bets.
- If you sharpen an existing bet, preserve the user's intent. Sharpening "infrastructure-first" into "build event logging and editor before any feature work" is good. Replacing it with a different bet is not.
- If you think a stated bet is internally inconsistent with another part of the seed, flag the inconsistency and propose how to resolve it — but don't unilaterally change the bet.

## What output looks like

Your output has three parts: the revised seed, a change summary, and an optional questions list.

### Part 1: The revised seed

Present the full revised seed in the same template format as the input. Use the same frontmatter and section structure. Update the change log at the bottom by appending one line for the current revision. Format change-log entries as `YYYY-MM-DD: <one-line summary of what changed>`.

If the seed has not been substantively changed (you propose no changes), say so explicitly rather than re-emitting the seed unchanged.

### Part 2: Change summary

A short list of the substantive changes you made, with one sentence of rationale each. Format:

```
## Changes proposed

- **Added** "single-section deployment" as a constraint. The user mentioned this in the project description but it wasn't in the constraints list, and downstream skills will need it.
- **Sharpened** the "research-friendly" bet to "supports IRB-approved randomized comparisons via configuration." The original was too vague to constrain design.
- **Flagged** a tension: anchor journeys include "content authoring" but bets say "infrastructure-first." Resolved by moving content authoring to out-of-scope for this iteration.
- **Removed** the duplicate "single-section" item from anchor journeys (now covered in constraints).
```

Skip cosmetic changes (whitespace, minor rewording) — only list substantive ones.

### Part 3: Questions for the user

If there are decisions you couldn't make on the user's behalf, list them as a short numbered list. Three to five maximum. Format:

```
## Questions

1. The seed mentions both "researcher" and "learning scientist" as roles. Are these the same persona or distinct? I treated them as the same in my revision.
2. You haven't specified a time horizon for the project. Is this a single-semester pilot, a multi-year program, or something else? It affects what should be in scope.
```

If you have no questions, omit this section entirely.

## When to propose few or no changes

If the current seed is already in good shape, propose few changes — or none. The skill's value is in proposing what the seed needs, not in producing changes for their own sake. A skilled Seed Reader pass on a polished seed should be quick and produce little.

A useful self-check before producing output: would a thoughtful collaborator reading this seed actually have the same concerns I'm raising? If your concerns are pedantic or hypothetical, drop them. If they're real, keep them.

## When to propose many changes

If the seed is genuinely sparse, contradictory, or off-track, propose substantial revisions. Don't hold back to seem agreeable. The user can reject what they don't want.

The two failure modes to avoid: proposing changes that don't matter (eagerness), and withholding proposals that do matter (timidity). Calibrate based on what the seed actually needs.

## Examples

### Example 1: A sparse seed

Input seed has only a project description and two bets. You should:

- Propose anchor personas based on the project description and bets.
- Propose anchor journeys derived from those personas.
- Propose constraints implied by the project description.
- Propose out-of-scope items that follow from the bets.
- Surface open questions about anything ambiguous.
- Be generous with proposals — the user has signaled they want help filling things in.

### Example 2: A polished seed with one contradiction

Input seed is thorough and consistent except for one tension between bets and out-of-scope. You should:

- Propose minimal changes — perhaps just resolving the tension.
- Note explicitly that the seed is in good shape overall.
- Avoid adding cosmetic improvements just to produce output.

### Example 3: A seed with vague language

Input seed has the right structure but uses vague phrases. You should:

- Sharpen the vague items into specific commitments.
- Preserve the user's intent — sharpening, not replacing.
- For each sharpening, briefly note what was vague and what you replaced it with, so the user can verify you preserved their meaning.

### Example 4: A seed with content that should not be in the seed

Input seed has paragraphs of prose that belong in Context or Journey documents. You should:

- Compress the prose into bullet points appropriate to the seed.
- Note that the longer content belongs downstream and will be elaborated by other skills.
- Don't silently delete the content — note it as moved or deferred.

## What the user does next

After reading your output, the user will:

- Accept your proposed seed as-is by saving it as the new `seed.md`.
- Edit your proposed seed and save the edited version.
- Reject your proposal and keep the prior seed.
- Answer your questions and re-invoke the skill for another pass.

You don't manage this — the user does. Your job ends when you produce your output.

## A note on tone

The seed cycle is iterative and collaborative. Be direct and confident in your proposals, but treat them as proposals, not declarations. The user has final authority over what goes in their seed. Your job is to help them see what the seed could be, not to decide what it should be.
