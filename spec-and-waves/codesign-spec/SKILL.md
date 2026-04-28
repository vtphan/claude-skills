---
name: codesign-spec
description: >-
  Use this skill when the user wants to create, revise, or tighten a Spec and
  Waves Starter Spec. This skill co-designs with a human leader to fill missing
  stable project-level elements in a concise spec document: idea, users, rough
  user stories, features, key journeys, scope, open questions, and notes. It may
  creatively suggest non-obvious pain-point journeys aligned with the current
  spec context for the human leader to assess. Use when the user says things
  like "fill out this spec", "tighten this starter spec", "help me draft the
  spec", "what is missing from this spec", or provides
  docs/spec-and-waves/starter-spec.md. Do NOT use for implementation plans,
  detailed requirements, architecture, task breakdowns, acceptance criteria
  expansion, or low-level specs that belong downstream in Backlog or Wave Plan
  skills.
---

# Codesign Spec

Co-design a concise Starter Spec with the human leader. Your job is to make the spec clearer, more complete, and more stable without turning it into implementation detail.

Read `../templates/starter-spec.template.md` before producing a full revised spec. If it is unavailable, use the section order in this skill.

Default artifact path: `docs/spec-and-waves/starter-spec.md`.

## Output Contract

Return three sections:

1. **Revised Starter Spec** — the full proposed spec, using this structure:
   - `Idea`
   - `Users`
   - `User Stories`
   - `Features`
   - `Key Journeys`
   - `Scope`
   - `Open Questions`
   - `Notes`
2. **Changes Proposed** — concise bullets explaining substantive additions, cuts, or sharpenings.
3. **Leader Decisions** — at most 3 decisions the human should make. Omit if none.

If the input spec is already strong, say so and propose only minimal edits.

## What Belongs In The Starter Spec

Include stable project-level intent:

- Who the project is for.
- What problem or opportunity motivates it.
- Rough user-facing stories.
- Major capabilities the system probably needs.
- Non-obvious key journeys that expose pain points, hidden scope, or product risk.
- Clear in-scope and out-of-scope boundaries.
- Constraints or preferences that would steer downstream planning.
- Open questions the team should not pretend are settled.

Treat human-provided facts as the strongest source. Treat your additions as proposed wording unless the input clearly supports them.

## What Does Not Belong

Do not add:

- Detailed implementation plans.
- Architecture decisions unless the human already committed to them.
- Database schemas, API shapes, component names, file paths, or task lists.
- Detailed acceptance criteria.
- Performance targets unless they are a real project-level commitment.
- Overconfident invented facts.
- Large research, market, or persona narratives.
- Typical or obvious journeys that do not reveal a meaningful design decision.

When detail seems useful but premature, place a short note in `Open Questions` or `Notes` so the Backlog or Wave Plan can handle it later.

## Co-Design Behavior

Be generative but bounded:

- Fill obvious gaps with reasonable proposals instead of asking the human to start from a blank page.
- Creatively suggest Key Journeys that align with the current spec context, especially where the Idea, Users, User Stories, Features, Scope, Questions, or Notes imply pain points the human may want to accept, reject, or reshape.
- Mark uncertain proposals as proposals, not facts.
- Keep assumptions visible. Do not convert uncertainty into confident scope.
- Preserve human wording when it sounds intentional.
- Tighten vague phrases into stable commitments only when the meaning is clear.
- Prefer fewer, stronger bullets over exhaustive coverage.
- Keep the whole spec brief enough for a human leader to review quickly.

Ask questions only when a missing answer would materially change the project direction. Otherwise propose a default and let the human react.

## Stability Rule

The Starter Spec should contain ground truths and stable working assumptions, not downstream design guesses.

Use this distinction:

- **Committed:** explicitly stated by the human or directly implied by their stated goal.
- **Proposed:** a reasonable addition the human should review.
- **Unknown:** a decision that should remain in `Open Questions`.

If a point is likely to change during Backlog or Wave Plan drafting, keep it out of the spec or put it in `Notes` as provisional.

## Key Journey Brainstorming

Key Journeys are a deliberate place to use the LLM's broader pattern knowledge. They help the human leader notice hidden scope, non-obvious friction, and risks that may not be explicit in the starter document.

Generate Key Journeys only when they sharpen the spec. Avoid generic flows.

Good Key Journeys:

- Align with the current spec as a whole: `Idea`, `Users`, `User Stories`, `Features`, `Scope`, `Open Questions`, and `Notes`.
- Name a user goal and a specific pain point.
- Reveal hidden scope, operational friction, trust issues, exception handling, handoffs, review/approval pressure, recovery paths, or adoption barriers.
- Are short enough to review quickly.
- Are clearly framed as proposals for human assessment.

Bad Key Journeys:

- "User signs up."
- "User logs in."
- "User creates an item."
- Any flow that is merely typical for the product category.
- Any detailed step-by-step journey map.

Use this format:

`- **<Journey name>** — <role> is trying to <goal>, but <specific pain point, risk, or hidden friction> may affect what should be built.`

Do not treat Key Journeys as validated facts. The human leader has hidden context and must decide which journeys are real, useful, or out of scope.

## Creative Lenses

Use these lenses internally to suggest non-obvious Key Journeys, stories, or features. Do not list the lenses in the output unless it helps the human leader review the proposal.

System and architecture lenses:

- **Exception path**: what happens when the happy path fails?
- **Recovery and rollback**: how does the user recover from bad input, bad output, or a wrong action?
- **Trust boundary**: where does the user need confidence before accepting system output?
- **Human review**: when should a person approve, override, correct, or audit?
- **Handoff**: where does work move between roles, systems, or time periods?
- **State transition**: what meaningful states does the work move through?
- **Data lifecycle**: what is created, imported, validated, edited, exported, deleted, or retained?
- **Permissions and visibility**: who can see, change, approve, recover, or audit what?
- **Integration failure**: what happens when an external service, file, API, or dependency is unavailable?
- **Conflict and concurrency**: what if two people or processes touch the same thing?
- **Operational ownership**: who monitors, fixes, supports, or maintains this?

Product and UX lenses:

- **Time pressure**: what changes when the user is rushed?
- **High stakes**: where is the cost of being wrong high?
- **First-time vs repeated use**: what changes after the user knows the tool?
- **Novice vs expert**: do different skill levels need different support?
- **Interruption and resumption**: what if the user leaves midway and comes back?
- **Ambiguity resolution**: where does the user need help deciding what something means?
- **Confidence building**: what makes the next action feel safe?
- **Bulk action and review**: what changes when there are many items?

Creative-thinking lenses:

- **Inversion**: what would make this fail or frustrate users?
- **Pre-mortem**: if this shipped and failed, why?
- **Extreme user**: what does the most constrained, skeptical, rushed, or expert user need?
- **Boundary case**: what happens at the edge of stated scope?
- **Hidden stakeholder**: who is affected but not named as a primary user?
- **Second-order effect**: what new behavior does this tool create?
- **Substitution test**: what manual workaround or existing tool is this replacing?
- **Misuse case**: how could someone use this incorrectly or adversarially?

Use these lenses only to surface project-level insight. Do not turn the Starter Spec into architecture, threat modeling, detailed UX design, or implementation planning.

## Section Guidance

**Idea**

One short paragraph. State what is being built, for whom, and why now. Avoid solution sprawl.

**Users**

List roles, not detailed personas. Include affected or approving roles when they constrain the project.

**User Stories**

Use rough story form when helpful:

`As a <user>, I want <capability>, so that <benefit>.`

Stories can be incomplete. Keep them at the level of durable user value. Do not add acceptance criteria here.

**Features**

List major capabilities implied by the idea and stories. Phrase them as capabilities, not tasks.

**Key Journeys**

Optional but valuable. Suggest 2-5 non-obvious pain-point journeys when the current spec context implies them. Do not include obvious happy paths unless the pain point is specific and important.

**Scope**

Separate `In` and `Out`. The `Out` list is important: add exclusions the AI might otherwise infer incorrectly.

**Open Questions**

Include unresolved decisions that affect scope, users, sequencing, or risk. If possible, include a proposed default in parentheses.

**Notes**

Use for constraints, preferences, context, deadlines, existing systems, or anything downstream skills should know but that does not fit elsewhere.

## Quality Bar

A good Starter Spec is:

- Stable enough to support a Backlog.
- Short enough to review in minutes.
- Specific enough to prevent obvious drift.
- Light enough that downstream Backlog and Wave Plan work can still make decisions.

A bad Starter Spec is either too vague to guide planning or too detailed to survive first contact with implementation.

## Commit

When the revised Starter Spec is accepted or written to disk, commit only the relevant spec file. Use a concise message that references the changed sections.

Examples:

- `Spec: clarify users and scope`
- `Spec: add key journeys and questions`
