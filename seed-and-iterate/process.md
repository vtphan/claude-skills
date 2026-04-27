# Seed-and-Iterate: A Process for AI-Assisted System Design

## Overview

This document describes a lightweight process for designing and developing systems with AI assistance. The process is built around a core principle: **the human commits to a small set of bounded decisions; the AI drafts everything else; the human reacts rather than generates**.

The process is designed for a domain expert working on systems within their area of knowledge, who wants rigorous artifacts and traceability without spending days on specification or discovery work.

## Core Principles

**The human does discriminative work; the AI does generative work.** Generation from a blank page is expensive cognitive work for humans and cheap for AI. Recognizing what's right or wrong about a draft is where human judgment is sharpest and AI is weakest. The process is designed around this division of labor.

**Specification is co-authored; elaboration is the AI's job.** The seed document captures the decisions only the human can commit to, but the human and the AI co-author it through alternating revisions. The AI elaborates the committed seed into a full set of design artifacts. Every change to the seed passes through human review, so the seed always reflects what the human has committed to.

**Reacting is cheaper than asking.** Where possible, the AI drafts a specific position rather than asking an open question. The human reacts to the draft. This is faster than question-and-answer because reactions are bounded while answers require the human to generate from scratch.

**Iterate in stages, not all at once.** The AI drafts one layer at a time, with a brief human review between layers. This keeps each review small and lets each layer be validated before the next builds on it.

**The seed is the source of truth.** Drafted artifacts are derived from the seed. When something downstream feels wrong, the human edits the seed and the affected artifacts are regenerated. This keeps human commitments durable while letting elaborations evolve.

## The Schemas

The process uses five schemas. The Seed is co-authored by the human and the AI through alternating revisions; the others are drafted by the AI.

### Seed (co-authored)

The minimal specification the human has committed to. The Seed is a living document that the human and the AI revise in turn — the human writes or revises, the AI reads and proposes a revised version, the human accepts or edits, and the cycle continues until the seed is stable. Every revision passes through human review, so the seed always reflects what the human has committed to.

Contains:

- **Project description.** One paragraph orienting the project.
- **Non-obvious bets.** Two to four bullets capturing the choices that make this project specific. These are the things hardest for the AI to guess correctly.
- **Out of scope.** Two to four bullets explicitly excluding things the AI might otherwise include.
- **Constraints.** Institutional, technical, ethical, or resource constraints that bound the design.
- **Anchor personas.** A list of persona names and roles, without details.
- **Anchor journeys.** A list of journey titles, without content.
- **Open questions.** Things the human is uncertain about and wants the AI to engage with explicitly.
- **Change log.** A short append-only list of recent revisions — what changed and why — appended on each accepted revision.

The seed is short — typically one page or less. The discipline is bullet points and short phrases, not prose. If a field requires paragraphs to express, it likely belongs in a drafted document instead, with a pointer in the seed.

### Context (AI-drafted)

The persistent layers of the project, drafted from the seed. Contains:

- **Vision.** One or two sentences on why the project exists.
- **Strategy.** Three to five bullets on how the vision will be achieved, including scope at the strategic level.
- **Success outcomes.** Three to five measurable conditions for "the vision is being achieved" over a meaningful time horizon.
- **Personas.** Full persona descriptions for each anchor persona — traits, contexts, goals, frustrations, with source tags (`observed`, `literature`, `assumed`).
- **Constraints.** Elaborated from the seed.
- **Open assumptions.** Things being proceeded on but not validated, each with a "how we'd find out" note.

### Goal (AI-drafted)

What is being built or achieved in this iteration. Contains:

- **Statement.** One or two sentences on what specifically is being built or achieved.
- **In scope and out of scope.** Explicit lists. The out-of-scope list matters as much as the in-scope list.
- **Definition of done.** Concrete, observable conditions for "this goal is achieved."
- **Time horizon.** Rough timeframe for completion.
- **Linked context.** Which vision, strategy, outcomes, and personas this goal serves.
- **Success signals.** Lighter-weight observable signals at the goal's timescale.
- **Open questions.** What completing this goal might answer.

A new Goal is written for each iteration. Context is revised rarely; Goals are revised every iteration.

### Journey (AI-drafted)

A user experience relevant to the current Goal. One document per journey. Contains:

- **ID and title.** Stable ID plus human title.
- **Persona reference.** Which persona(s) this journey applies to.
- **Scenario.** One paragraph setting the context.
- **Stages.** Ordered list, each with: stage ID, name, user actions, user thoughts and feelings, friction points, and system touchpoints.
- **Key insights.** Three to five takeaways that should drive design decisions.
- **Source tags.** Per stage or per insight — `observed`, `literature`, `assumed`, `validated`.

Stable stage IDs are essential because stories will reference them.

### Story-and-Requirements (AI-drafted)

The deliverable units of work. One document per story, with requirements nested. Contains:

- **ID and title.**
- **Story statement.** Standard "as a [role], I want [capability], so that [benefit]."
- **Journey moment reference.** Which journey stage(s) this story serves.
- **Acceptance criteria.** What "done" looks like from the user's perspective.
- **Requirements.** A list, each with: type (`functional`, `non-functional`, `data`, `edge-case`), specification with concrete numbers and thresholds, and verification method.
- **Priority.** Lightweight ranking such as `must`, `should`, `could`.
- **Status.** `draft`, `ready`, `in-progress`, `done`.

### Schema Conventions

All schemas share two conventions that support the draft-and-react interaction model.

**Confidence tags.** Each section or field includes a confidence tag — `high`, `medium`, or `low` — indicating the AI's confidence in the draft. The human reacts preferentially to low-confidence items.

**Decision points list.** Each AI-drafted document includes a top-of-document list of three to seven decision points the human should react to. The rest of the document can be skimmed; the decision points are where review effort is concentrated.

## The Skills

Five skills implement the process. Each has a defined input contract (what it reads) and output contract (what it produces).

### Seed Reader

**Input:** the current Seed document.

**Behavior:** Reads the seed and produces a revised version that, in its judgment, better reflects what the seed should be. May add missing items, sharpen vague language, flag contradictions, surface open questions, restructure organization, remove redundancy, or capture decisions that came up in recent conversation but didn't make it into the seed. Presents the revised seed alongside a short summary of changes.

**Output:** a proposed revised seed and a change summary.

The skill is invoked whenever the human wants to refine the seed — before any downstream stage, between stages, or at the end of an iteration as a closing review. The cycle ends when the AI proposes no further changes or the human accepts the proposal as final.

### Context Builder

**Input:** a `ready` Seed.

**Behavior:** Drafts a complete Context document — vision, strategy, personas, outcomes, constraints, assumptions — based on the seed plus available memory and domain knowledge. Surfaces decision points at the top of the document and tags confidence per section. Revises based on human reactions.

**Output:** an accepted Context document.

### Goal Drafter

**Input:** an accepted Context document and an indication of what the human wants to achieve in this iteration.

**Behavior:** Drafts a complete Goal document with bounded scope, explicit cuts, definition of done, and time horizon. Presents in-scope and out-of-scope lists prominently. Revises based on human reactions.

**Output:** an accepted Goal document.

### Journey Mapper

**Input:** an accepted Context, an accepted Goal, and a journey title from the Seed.

**Behavior:** Drafts a complete Journey document with stages, emotional annotations, friction points, and key insights. Runs an internal adversarial pass — re-reads from each persona's perspective — before presenting. Surfaces decision points and tags confidence. Revises based on human reactions.

**Output:** an accepted Journey document.

Run once per journey. Multiple journeys can be drafted in parallel since they're independent.

### Story and Requirements Generator

**Input:** the accepted Journey documents and the accepted Goal.

**Behavior:** Drafts a story set tied to journey stages, with internal pruning that defaults to fewer stories rather than more. Expands surviving stories into requirements with concrete specifications and verification methods. Refuses vague language; forces quantification. Runs traceability check to ensure every story links to a journey moment and every requirement links to a story. Surfaces both the keeps and the cuts with rationale. Revises based on human reactions.

**Output:** an accepted set of Story-and-Requirements documents.

### Reviewer

**Input:** any artifact or set of artifacts, plus a review mode.

**Behavior:** Runs a structured critique in the requested mode. Modes include `skeptical-engineer`, `frustrated-user`, `methodologist`, `privacy-officer`, and `traceability-check`. For traceability mode, identifies orphans, staleness, and contradictions across artifacts. Returns findings as a list with severity tags.

**Output:** a structured critique.

The Reviewer is a cross-cutting skill that can be invoked at any point in the process or as a standalone check between stages.

## The Process

The process runs in stages with explicit gates between them. Each stage is short; the cumulative time investment for the human is hours, not days.

### Stage 0: Seed Cycle

The human writes an initial seed — possibly very sparse, even just a paragraph and a few bullets. The human runs the Seed Reader skill, which reads the current seed and proposes a revised version with a summary of changes. The human accepts, edits, or rejects the proposal. The cycle continues until the AI proposes no further changes or the human accepts the proposal as final.

The seed cycle is not a one-time event. It can be re-entered at any later point in the process whenever new understanding suggests the seed should evolve.

Time: 15 to 45 minutes for the initial cycle; shorter for subsequent re-entries.

**Gate to next stage:** the human considers the seed ready for downstream drafting. (It can still evolve later.)

### Stage 1: Context

The human runs the Context Builder skill. The skill drafts a Context document. The human reviews the decision points and any low-confidence sections. The skill revises. The human accepts.

Time: 20 to 40 minutes.

**Gate to next stage:** the Context document accurately reflects the human's intent and assumptions are honestly tagged.

### Stage 2: Goal

The human runs the Goal Drafter skill. The skill drafts a Goal document with explicit in-scope and out-of-scope lists. The human reacts to the cuts and the definition of done. The skill revises. The human accepts.

Time: 15 to 30 minutes.

**Gate to next stage:** the Goal is bounded, the scope cuts are deliberate, and the definition of done is observable.

### Stage 3: Journeys

The human runs the Journey Mapper skill on each anchor journey. The skill drafts each Journey document. The human reviews the decision points and reacts to specific stages. The skill revises. The human accepts.

Time: 30 to 60 minutes per journey, depending on complexity.

**Gate to next stage:** each journey produces design-driving insights and the source tagging is honest.

### Stage 4: Validation

The human conducts a small number of short conversations — typically one per major role — to validate the Context and Journey documents against reality. The AI helps prepare focused questions and synthesize notes after.

The human updates the affected documents based on what is learned. Source tags are updated from `assumed` to `validated` where appropriate.

Time: 20 to 30 minutes per conversation, plus the conversations themselves.

**Gate to next stage:** at least some assumption tags have been updated as a result of validation. If nothing changed, assumptions were probably not honestly identified earlier.

### Stage 5: Stories and Requirements

The human runs the Story and Requirements Generator skill against the journey set. The skill drafts a pruned story set with full requirements. The human reacts to the cuts and to specific requirements that matter most. The skill revises. The human accepts.

Time: 45 to 90 minutes for the first pass.

**Gate to next stage:** every story traces to a journey moment, every requirement traces to a story, and the pruning rationale is documented.

### Stage 6: Phase Planning and Implementation

The human, with AI assistance, orders the story set into phases — vertical slices, prioritized by what de-risks or teaches the most. The Reviewer skill in `traceability-check` mode confirms phasing covers high-priority journey moments.

Implementation proceeds one phase at a time, using whatever code-generation tools the human prefers. After each phase, the process loops back to the Seed Cycle and Stage 1 or Stage 2 — Seed, Context, and Goal are revisited based on what was learned, and the next iteration begins.

**Gate to next iteration:** upstream artifacts have been updated based on what was learned in implementation.

## The Iteration Loop

The process is iterative, not linear. After each implementation phase:

1. The human reviews what was learned — from real users, from observed behavior, from what was harder or easier than expected.
2. The Seed is updated if anything fundamental changed. The Context is updated if personas or assumptions shifted. The Goal is closed and a new Goal is drafted for the next iteration.
3. Affected Journeys and Stories are flagged for review or regeneration.
4. The next phase begins.

This loop is what makes the process agile. The artifacts stay alive rather than becoming stale documentation. Every iteration sharpens the artifacts based on contact with reality.

## What the Human Actually Does

The total human investment for one full iteration of the process, from blank state to ready-for-implementation, is roughly:

- 15-45 minutes on the Seed Cycle.
- 20-40 minutes reviewing Context.
- 15-30 minutes reviewing Goal.
- 30-60 minutes per journey reviewing Journeys.
- 20-30 minutes per validation conversation, plus the conversations themselves.
- 45-90 minutes reviewing Stories and Requirements.
- Variable time on phase planning.

The total is typically a few hours of focused review work, spread across several sittings, plus the validation conversations. This excludes implementation time, which uses code-generation tools downstream of the artifact set.

## What the AI Does

The AI does the bulk of the generative work:

- Drafting the Context document from the seed.
- Drafting Goal documents.
- Drafting Journey documents with internal adversarial review.
- Generating and pruning the story set with rationale.
- Expanding stories into requirements with concrete specifications.
- Running cross-cutting reviews on demand.
- Maintaining traceability across the artifact set.
- Flagging stale or orphaned artifacts when upstream changes occur.

The AI is configured to commit to specific drafts rather than hedge, to surface decision points prominently rather than burying them, and to preserve human-specified content verbatim rather than paraphrasing it away.

## What This Process Is Not

A few things this process explicitly is not:

- **Not a research methodology.** Validation conversations are lightweight and targeted. Heavy research is appropriate for unfamiliar domains, not for projects where the human is already a domain expert.
- **Not a project management framework.** It produces design artifacts. Implementation tracking, sprint planning, and team coordination are separate concerns.
- **Not a substitute for human judgment.** The AI drafts; the human commits. Decisions about scope, priority, ethics, and design tradeoffs remain with the human.
- **Not waterfall.** The process loops. Each implementation phase informs the next iteration's Seed, Context, and Goal.

## When to Use This Process

This process is well-suited for:

- New systems where the design is not yet settled.
- Multi-role systems where stories alone don't capture cross-role dynamics.
- Systems with research or analytics dimensions that depend on capturing process, not just outcomes.
- Projects where the human is a domain expert but has limited time for specification work.

This process is overkill for:

- Small features within an established system.
- Maintenance and refactoring work.
- Pure infrastructure projects with no user-facing dimension.
- Quick prototypes intended for throwaway use.

For those cases, a single Seed plus direct implementation is usually sufficient.

## Maintenance

The process itself is a product. After each completed project, the human reviews what worked and what didn't:

- Did any schema field consistently go unused? Drop it.
- Did any review consistently surface the same kind of issue? Add a gate.
- Did any skill consistently hedge or ask too many questions? Revise the skill prompt.
- Did any stage take significantly longer or shorter than expected? Recalibrate.

The schemas, skills, and process are versioned and evolved deliberately. Improvements compound across projects.

## Summary

The process consists of five schemas (Seed, Context, Goal, Journey, Story-and-Requirements), five skills (Seed Reader, Context Builder, Goal Drafter, Journey Mapper, Story and Requirements Generator) plus a cross-cutting Reviewer, and seven stages (Seed Cycle plus six downstream stages) with explicit gates and a loop back to the start.

The human and the AI co-author the Seed through alternating revisions; the AI drafts everything else. The human reviews AI-drafted artifacts at each stage, conducts a few short validation conversations, and makes the bounded decisions only they can make.

The total human investment is a few hours of reactive work per iteration, producing rigorous, traceable artifacts ready for implementation.
