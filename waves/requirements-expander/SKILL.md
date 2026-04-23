---
name: requirements-expander
description: Use this skill whenever the user has a high-level product or system specification (goal, scope, intended user roles) and wants it expanded into a concrete, buildable requirements document containing user stories, user journeys, and supporting features. Triggers include phrases like "turn this spec into user stories", "expand these requirements", "write user stories and journeys for this", "draft a PRD from this brief", "what features do we need for this product", or whenever a markdown file describes a system's goal, scope, and roles and the user wants the next level of detail. Also trigger when the user provides a vision document, one-pager, or project brief and asks for requirements, a backlog, or a feature list. Do NOT use when the user wants code, architectural diagrams, UI mockups, or a market analysis — this skill produces product requirements prose, not engineering artifacts.
---

# Requirements Expander

## What this skill does

Given an input spec that names a software system's **goal, scope, and intended user roles**, produce a markdown document that expands those high-level intentions into three concrete, cross-linked layers of detail:

1. **User stories** — narrow, testable statements of value from each role's perspective.
2. **User journeys** — the end-to-end paths those roles actually walk through the system to get value.
3. **Features** — the capabilities the system must provide to support the stories and journeys above.

The goal is to take a spec that's useful for aligning stakeholders and turn it into something useful for planning work — concrete enough that a product manager could prioritize it and an engineer could estimate it, but still framed in terms of user value rather than implementation.

## Workflow

### Step 1 — Read the input spec

Read the input document carefully. Extract and note:

- The **goal** — what problem is the system solving, and for whom.
- The **scope** — what the system does and, just as importantly, what it deliberately does *not* do.
- The **user roles** — who interacts with the system. A role is defined by what the person is trying to accomplish, not their job title. Capture each role's responsibilities if stated.
- Any **constraints, non-goals, or success metrics** explicitly mentioned.

If any of these are missing or ambiguous enough that you'd be guessing at core behavior, stop and ask the user one focused clarifying question before proceeding. Don't pepper them with questions — pick the single thing that would most change the output.

### Step 2 — Generate user stories

Write one story per (role, goal) pair. A story here is a single unit of user value, small enough to be implementable and testable on its own.

Use this exact format:

```
**US-<role-prefix>-<N>: <short title>**
As a <role>,
I want to <goal>,
so that <benefit>.

Acceptance criteria:
- Given <context>, when <action>, then <outcome>.
- Given <context>, when <action>, then <outcome>.

Priority: Must-have | Should-have | Nice-to-have
```

Apply the **INVEST** heuristic as a quality filter (Independent, Negotiable, Valuable, Estimable, Small, Testable). If a story feels bloated — multiple disconnected outcomes, or unbounded scope — split it. If it feels like implementation detail ("as a user, I want a dropdown..."), rewrite it at the value level.

Aim for roughly 3-6 stories per role. If you have one role with 20 stories and another with one, something is off — revisit whether roles are right or whether some stories are really features dressed up as stories.

### Step 3 — Generate user journeys

A journey is not a story — it's the connected sequence of actions a role takes over time to accomplish an end-to-end outcome that typically spans multiple stories.

For each primary role, draft at least one journey that walks through how they'd actually use the system from entry to outcome. Use this format:

```
**UJ-<role-prefix>-<N>: <journey name>**
Role: <role>
Trigger: <what starts this journey — event, need, schedule>
Outcome: <what "done" looks like for this role>

| Phase | User action | System response | Pain points / emotions |
|-------|-------------|-----------------|------------------------|
| 1. Discover | ...        | ...             | ...                    |
| 2. Set up   | ...        | ...             | ...                    |
| 3. Use      | ...        | ...             | ...                    |
| 4. Review   | ...        | ...             | ...                    |

Supporting stories: US-..., US-...
```

Use whichever phase names fit the journey — common shapes are **Discover → Onboard → Use → Review → Share**, or **Trigger → Plan → Execute → Close**. Don't force a fixed set of phases; the right phases are whatever describes how this role moves through time.

The **"pain points / emotions"** column is load-bearing — it surfaces moments where UX design matters, and often reveals stories or features you missed. Don't leave it empty.

### Step 4 — Derive features

A feature is a coherent chunk of system capability that one or more stories and journeys depend on. Features cut across stories; stories live inside features.

For each feature, use this format:

```
**F-<N>: <feature name>**
Description: <one or two sentences describing the capability>
Supports stories: US-..., US-..., US-...
Supports journeys: UJ-..., UJ-...
Priority: Must-have | Should-have | Nice-to-have
Notes: <dependencies, open questions, constraints — if any>
```

Group related features under section headers if there are more than roughly 8 features total (e.g., "Core workflow", "Administration", "Integrations"). Ordering within a group should roughly follow priority, then dependency order.

Every story and journey should be referenced by **at least one** feature. If a story doesn't map to any feature, something is missing — either the feature list is incomplete, or the story is out of scope and should be flagged.

### Step 5 — Assemble the output document

Write the final markdown document using this exact structure:

```
# <System name> — Requirements

## 1. Context
Brief restatement of the goal, scope, and roles drawn from the input spec. Two or three short paragraphs. This is not filler — a reader should be able to understand the rest of the document from this section alone.

## 2. User roles
Table of roles with a one-line description of what each role is trying to accomplish in the system.

## 3. User stories
Grouped by role. All stories in the US-<role-prefix>-<N> format above.

## 4. User journeys
All journeys in the UJ-<role-prefix>-<N> format above.

## 5. Features
All features in the F-<N> format above, grouped if the list is long.

## 6. Traceability matrix
A compact table mapping stories → features → journeys so a reader can spot coverage gaps at a glance.

## 7. Open questions
Anything you couldn't resolve from the input spec. Be specific — not "scope unclear" but "the spec says admins can 'manage users' — does that include deleting accounts, or only disabling them?"
```

Save the file as `<system-slug>-requirements.md` alongside the input spec unless the user specified a different name or location.

## Principles to keep in mind

**Value over implementation.** Stories are about what someone wants to achieve, not which button they click. If a story reads like a UI spec, rewrite it.

**Every role earns its place.** If you're generating fewer than two stories for a role, that role may not belong in the system — flag it in Open questions rather than padding with weak stories.

**Scope discipline.** The input spec is a boundary, not a suggestion. If a compelling story would clearly be out of scope, put it in Open questions ("Should X be in scope? The current spec says no, but without it journey Y breaks at step 3.") — don't silently expand scope.

**Traceability is a correctness check, not bureaucracy.** If you can't trace a story to a feature or a journey to stories, the document has a hole. Use the matrix to find those holes before handing the document to the user.

**Don't invent facts.** When the spec doesn't say something, don't fill it in with plausible-sounding details — name the gap in Open questions. A hundred precise questions are more useful than a hundred invented answers.

## Worked example (truncated)

Input spec says:
> A pet-sitting marketplace where pet owners book sitters. Roles: pet owner, sitter, admin. In scope: browsing sitters, booking, payments. Out of scope: live video check-ins.

One story:

```
**US-OWN-1: Find a sitter near me**
As a pet owner,
I want to browse available sitters by location and date,
so that I can find someone nearby for the dates I need.

Acceptance criteria:
- Given I enter a zip code and a date range, when I search, then I see a list of sitters with availability overlapping my dates.
- Given a sitter is fully booked for my dates, when I search, then they do not appear in results.

Priority: Must-have
```

One journey (abbreviated):

```
**UJ-OWN-1: First booking as a new pet owner**
Role: Pet owner
Trigger: Upcoming trip, needs sitter
Outcome: Confirmed booking with a chosen sitter

| Phase | User action | System response | Pain points / emotions |
|-------|-------------|-----------------|------------------------|
| 1. Discover | Visits site, searches by zip/date | Shows matching sitters | Overwhelmed by choice |
| 2. Evaluate | Reads profiles and reviews | Shows verified reviews | Anxious — is this person trustworthy? |
| 3. Book     | Requests dates with a sitter | Sends request, holds slot | Uncertain — will they accept? |
| 4. Confirm  | Receives acceptance, pays | Processes payment, confirms | Relieved |

Supporting stories: US-OWN-1, US-OWN-2, US-OWN-3
```

One feature:

```
**F-1: Sitter search and discovery**
Description: Allows pet owners to search for sitters by location and date range, with results ranked by relevance and availability.
Supports stories: US-OWN-1, US-OWN-2
Supports journeys: UJ-OWN-1
Priority: Must-have
Notes: Depends on sitter profile data (F-2) and availability calendar (F-3).
```

## When the input is thin

If the spec is one paragraph and says almost nothing, don't write a 40-page document of invented detail. Produce a shorter document that genuinely reflects what's known, and put everything else in Open questions. A short honest document is much more useful than a long confident one.
