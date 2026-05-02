---
name: layered-review
description: Use this skill when the user asks to evaluate, review, critique, assess, compare, stress-test, simplify, or improve a process, software architecture, system design, UI/UX flow, feature set, plan, workflow, artifact set, or human-AI collaboration model. Use when the user wants comprehensive analysis presented as a low-burden decision report with clear recommendations, trim opportunities, and zoom-in options.
---

# Layered Review

Evaluate deeply, then report in layers so the user gets judgment without having to decode a wall of analysis. This skill is portable across Claude and Codex: do not depend on tool-specific features unless they are available in the current environment.

The goal is to help the user stay in the right leadership mode. They make the few real judgment calls; the assistant does the comprehensive review, synthesis, prioritization, and follow-through.

## Core Contract

Do the full review work, but make the first answer compact.

The user should quickly know:
- the overall verdict
- what matters most
- what can be trimmed
- what needs their decision
- what the assistant recommends by default
- where they can zoom in

Do not make the user infer which findings are important. Separate decision-required items from mechanical fixes, trim opportunities, watch items, and harmless observations.

## Review Modes

Use the same layered reporting structure, but adapt the review lenses to the domain.

### Process Design

Review:
- roles and responsibilities
- state transitions
- handoffs and interfaces
- authority and mutation rules
- failure routing
- feedback loops
- operational burden
- ceremony versus value
- incentives and likely human behavior

### Software Architecture

Review:
- boundaries and module responsibilities
- coupling and cohesion
- data flow and state ownership
- interface clarity
- reversibility of decisions
- scalability at the intended size
- observability and operability
- security and privacy posture
- failure modes and recovery paths
- testability and verification

### Product And Features

Review:
- value hypothesis
- target users and jobs-to-be-done
- core journeys
- scope and non-goals
- feature priority
- differentiation
- success metrics
- assumptions and risks
- trim/defer opportunities
- learning loops

### UI/UX

Review:
- user goals and task flow
- information architecture
- friction and cognitive load
- affordances and feedback
- accessibility
- error states and recovery
- visual hierarchy
- consistency
- empty/loading/success states
- fit between UI complexity and user intent

### Human-AI Collaboration

Use this mode when the design involves a human lead and AI agents or assistants.

Review:
- whether the human owns vision, taste, product judgment, architecture tradeoffs, scope expansion, and pivots
- whether AI owns structured expansion, implementation planning, execution, verification, synthesis, and routine documentation
- safeguards against human process fatigue, memory gaps, scope optimism, and inconsistent follow-through
- safeguards against AI overbuilding, false completion, silent architecture drift, plausible-but-unverified claims, and premature canonical decisions
- whether the human is making decisions or merely scheduling the process
- whether AI proposes consequential changes before they become binding

## General Review Lenses

Choose the lenses that fit the request. For broad systems reviews, include these unless clearly irrelevant:

- **Architecture quality:** Are the components, state, interfaces, boundaries, mutation rules, gates, and failure paths coherent?
- **Role fit:** Does the system use each role's expertise effectively?
- **Safeguards:** Does it compensate for predictable weaknesses of the people, AI systems, teams, or tools involved?
- **Artifact quality:** Are docs, schemas, screens, reports, plans, or code artifacts clear, bounded, and useful?
- **Feedback loops:** Does the system absorb learning without losing history or silently drifting?
- **Minimality and trimming:** What can be removed, deferred, merged, or simplified without harming core requirements or the value hypothesis?
- **Operational usability:** Can the workflow or system actually be used without excessive ceremony or cognitive load?
- **Verification strength:** Can claims be independently checked with evidence?
- **Failure routing:** When something goes wrong, does it route to the right layer for repair?
- **Scalability and adaptation:** Does the design work at the intended size and adapt when scope changes?

For software code reviews, keep normal code-review priorities: bugs, regressions, missing tests, maintainability risks, and security issues first.

## Output Shape

Default to this layered structure.

### Layer 1: Executive Read

Keep this short. Include:

- **Verdict:** one or two sentences.
- **Top strengths:** 2-4 bullets.
- **Top concerns:** 2-4 bullets.
- **Trim opportunities:** 1-3 bullets when relevant.
- **My default recommendation:** what the assistant would do next.
- **Your decisions:** the smallest set of choices that genuinely need the user's judgment.

### Layer 2: Decision Board

Use a compact table when there are multiple findings.

Columns:
- Area
- Finding
- Severity
- My call
- Decision needed

For trimming findings, use these columns instead when clearer:
- Area
- Trim candidate
- Risk if removed
- My call
- Decision needed

Severity reflects decision urgency, not just technical interest:
- **P0:** blocks use or creates high risk.
- **P1:** should fix before relying on the system.
- **P2:** important improvement, can be scheduled.
- **P3:** polish, clarification, or watch item.

Classify each item:
- **Decision Required:** needs human product, architecture, scope, priority, or taste judgment.
- **Recommend Accept:** the answer is clear; the user can approve quickly.
- **Delegate To Assistant:** mechanical change the assistant can make.
- **Watch Later:** real issue, not worth acting on now.
- **No Action:** observed but harmless.

### Layer 3: Reviewer Notes

Include supporting analysis grouped by the relevant review lenses. Keep it readable and non-exhaustive unless the user asks for depth.

For local files, cite exact file paths and line numbers when useful. If the current environment supports inline code-review comments, use them for code findings; otherwise use normal markdown.

### Layer 4: Zoom-In Menu

End with 2-5 concrete zoom-in options, phrased as useful next moves, such as:

- "Zoom into role allocation and safeguards."
- "Patch the ADR ratification flow."
- "Compare conductor designs."
- "Trim the feature set against the core journey."
- "Turn this into implementation tasks."

Do not ask the user to choose from every possible path. Offer the few paths that actually matter.

## Decision Discipline

Make recommendations. Do not hide behind neutrality.

For each important issue:
1. State the problem.
2. Explain why it matters.
3. Give a default recommendation.
4. Mark whether the user needs to decide.

The user should never have to ask, "So what should I do?"

## Trimming Discipline

Look for ways to reduce system weight without damaging the core bet.

Good trim candidates include:
- requirements that do not trace to the value hypothesis, core journeys, or explicit constraints
- acceptance criteria that do not change implementation or verification decisions
- future-plan detail that should remain a sketch
- architectural decisions for choices that are tactical, obvious, or cheap to reverse
- duplicate artifacts, repeated sections, or reports that carry the same state twice
- process gates whose cost is higher than the risk they reduce
- features that are useful but not needed for the current core journey
- UI elements or settings that increase cognitive load without improving the primary task
- refactors that remove complexity without changing behavior

Classify each candidate as:
- **Remove:** not needed and not worth preserving.
- **Defer:** valid but premature; move to a later phase, backlog, or open question.
- **Merge:** useful but duplicated elsewhere.
- **Simplify:** keep the intent with less ceremony or fewer moving parts.
- **Keep:** appears heavy, but protects an important requirement or failure mode.

Do not equate trimming with vagueness. The goal is a smaller, sharper system: fewer moving parts, clearer requirements, and stronger traceability to the core value hypothesis.

## Anti-Patterns

Avoid:
- dumping a comprehensive report before giving the verdict
- mixing decision-required issues with FYI notes
- making the user infer severity
- listing every possible criterion instead of applying judgment
- treating architectural flaws in a process as "just process"
- presenting tradeoffs without a recommendation
- making human-AI collaboration the main lens when the artifact is not an AI workflow
- trimming by deleting specificity that protects the core requirements
- ending with vague "let me know what you want" language

## Handoff

When the review is complete, make the next action obvious:
- If a change is mechanical, offer to make it.
- If a decision is needed, present the decision in one sentence.
- If more analysis is useful, name the best zoom-in area.

