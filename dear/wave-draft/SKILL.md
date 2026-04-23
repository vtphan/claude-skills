---
name: wave-draft
description: Use this skill whenever the user has a product brief, one-pager, vision doc, or short spec and wants to start a rolling-wave build — producing a unified wave doc with the first wave (walking skeleton) fully specified and planned, and future waves sketched as themes. Triggers include phrases like "draft a wave doc from this brief", "start rolling-wave planning for this spec", "what's the first wave for this project", "turn this brief into stories and a plan", "plan the walking skeleton", "set up a DEAR loop for this project", or whenever a short product/vision document is provided and the next step is defining both requirements and a phased implementation in wave form. Also trigger when the user shares a PRD fragment, product concept, or project brief and asks for a unified spec+plan organized in waves. Do NOT use when a wave doc already exists (use wave-redraft to advance it), when the user wants only requirements without any plan (that's a different artifact), when the user wants a complete waterfall PRD, or when the user wants code written directly without any planning.
---

# Wave Draft

Produce the first version of a unified wave doc — requirements and plan, organized by wave, with the first wave specified and planned in full and future waves sketched. Before doing anything else, read `references/wave-schema.md` in full. The schema is the contract. This SKILL.md covers the **judgment calls** that shape good wave docs; the schema covers **format**.

## Inputs and output

**Input:** a brief, one-pager, vision doc, or short spec that names (at minimum) the system's goal and intended users. The input doesn't need to be structured; read it for the substance, not the shape.

**Output:** a single file named `<project-slug>-wave-doc.md`, written in the project's `docs/` directory (or alongside the input if no `docs/` exists). Confirm the file path with the user before writing if it's ambiguous.

## Workflow

### 1. Read the input thoroughly

Extract, even if the input structures them differently than you expect:

- **Goal** — what problem the system solves, and for whom.
- **Non-goals** — what the system deliberately does *not* do. Ask if these aren't stated; non-goals are load-bearing for scope discipline.
- **Roles** — who interacts with the system, defined by what they're trying to accomplish, not by job title.
- **Constraints** — tech stack, platform, timeline, user environment, compliance obligations.
- **Success metrics** if present.

If any of these are genuinely missing — not just differently named — and the wave doc can't be drafted without them, stop and ask the user one focused question. Don't interrogate them; pick the single thing that would most change the output.

### 2. Decide the walking-skeleton shape

This is the hardest decision in the draft. Before you write anything, sketch to yourself:

- **What is the thinnest end-to-end slice** that exercises the whole architecture?
- **Which architectural commitments does that slice force?** (Stack, persistence, auth, deployment model, interface.)
- **What user-observable behavior would demonstrate the slice works?**

The walking skeleton is W1. It is architecturally complete and functionally thin. A good walking skeleton's exit criterion reads like: "a user can X end-to-end, where X is the most trivial thing the system can do that still touches auth, persistence, the core domain logic, and the user-facing interface."

See [Walking skeleton principles](#walking-skeleton-principles) for detail. Only deviate from the walking-skeleton default (i.e., make W1 a horizontal foundation instead) if the input spec genuinely requires it, and justify the deviation in the Goal section.

### 3. Decide the wave ladder

After W1, decide the sequence of future waves. Each future wave should:

- Deliver an observable increment of user value.
- Extend the skeleton rather than rebuild it.
- Tackle risk in a priority-ordered way — scariest unknowns first.
- Fit comfortably in one wave-sized unit of work (roughly a few sessions to a week).

Aim for **3–6 waves total**. Fewer than 3 is usually too coarse for a rolling-wave project worth organizing this way. More than 6 suggests you're over-sketching future work whose shape you don't yet know — trim or fold.

See [Wave ordering principles](#wave-ordering-principles) for how to pick the sequence.

### 4. Write W1 in full

Expand W1 into the schema's current-wave detail: stories with acceptance, features, plan tasks with acceptance, exit criteria, a repro path, entry criteria, assumptions the wave depends on, risks it's exposed to, and the architectural commitments it will establish.

For a walking-skeleton W1, the commitment list is usually long (the slice forces many architectural choices). Surface them explicitly in the W1 section's `New commitments proposed:` field, with an entry per commitment in Section 7 of the wave doc carrying a rationale line.

Every task must have acceptance. Every story must have acceptance. See [Task and story sizing](#task-and-story-sizing) for the quality bar.

### 5. Sketch future waves

Each future wave gets the sketch fields from the schema — goal, theme, candidate stories (titles only, no acceptance), anticipated features (titles only, no definitions), sketched entry/exit criteria, assumptions/risks/commitments references, 2–4 sentence approach sketch.

**No task breakdowns. No per-story acceptance criteria. No feature descriptions.** If you find yourself drafting detail for a future wave, stop — that's work whose shape you don't yet know, and pre-drafting it defeats rolling-wave.

### 6. Seed the three registers

Walk the input for open questions, unstated assumptions, foreseeable risks, and architectural commitments the system will need. For each, decide which register it belongs in:

- **Assumption** — a belief about the world or users that we're choosing to accept in order to proceed. Closes out via validation.
- **Risk** — something that could go wrong even if assumptions hold. Closes out via occurrence or mitigation.
- **Architectural commitment** — a choice about how the system is built that's expensive to reverse. Established (not "resolved") when a wave commits to it.

Assign each entry to the wave where it first matters. Entries for future waves are fine as `untested` / `open` — they'll be exercised when their wave arrives.

### 7. Write Section 9 — Themes not yet waved

Product-vision themes that you've noticed in the input but decided not to plan into waves yet. One bullet per theme. This section is where scope conversation lives without bleeding into future-wave sketches. It's also where you put anything the input mentions that you're deferring without committing to a wave for.

### 8. Fill the frontmatter and change log

Set `wave_doc_version: 1`, `created` and `last_updated` to today, `current_wave: W1`, `status: in_progress`. Write the initial change-log entry with type `initial-draft`, briefly naming the waves and register seed counts.

### 9. Verify before writing

Final read-through against the invariants in `references/wave-schema.md` section 11. In particular:

- No task detail in future waves.
- Every W1 task has acceptance.
- Every W1 story has acceptance.
- W1 has a repro path and exit criteria.
- Every story and feature is traced to a wave or listed in Section 9.
- Architectural commitments have rationale lines.
- Walking-skeleton W1, or explicit justification if horizontal.

If any invariant is violated, fix it before writing the file.

## Walking skeleton principles

The W1 default matters more than almost any other decision in the wave doc. Get it right and every subsequent wave has a home to land in; get it wrong and wave 2 spends effort relitigating architecture instead of adding value.

### What a walking skeleton is

A vertical slice that exercises the full architectural stack with minimal functional content. The canonical examples:

- **Web app**: user signs up, logs in, sees a page that says "Hello, <username>." Exercises auth, frontend, backend, DB, deployment.
- **CLI tool**: `tool <one-file>` reads one file, does the minimal version of the core transformation, writes one row of output. Exercises the main pipeline, persistence, CLI parsing.
- **Multi-service system**: service A receives one request, calls service B, returns one response. Exercises deployment topology, inter-service protocol, observability.

The functional content is deliberately trivial. The goal isn't to deliver value in W1; the goal is to **commit to the architectural choices and prove the handoffs work**.

### Why this default is strong

**Integration risk surfaces early.** Dangerous bugs live in handoffs between layers. A walking skeleton forces those handoffs into W1, when the wave doc is still flexible.

**Every subsequent wave has a place to land.** Once the skeleton exists, W2 can extend it in one direction (add a feature to the query engine), W3 in another (add persistence of user preferences), etc. Without a skeleton, each wave wrestles with where it fits.

**Architectural commitments become visible and auditable.** W1's `New commitments proposed:` list becomes Section 7 entries. Future waves reference them. If a future wave wants to violate one, it has to do so visibly — via a supersede — not silently.

**The repro path is easy.** W1's demo script is the first end-to-end test of the system, usable by the auditor and by all subsequent waves as a regression check.

### When to override the default

Default hard to walking skeleton. Override only when the input spec makes it clear that a horizontal foundation is genuinely required:

- The product hinges on a novel capability that doesn't exist yet (custom algorithm, research-level component). You need to prove it works before any slice can be built on top of it.
- Hard compliance requirements shape every layer and can't be retrofitted (end-to-end encryption, audit trail, data residency).
- Multi-system integration where the integration boundary is the single hardest part; a trivial slice wouldn't exercise it meaningfully.

If overriding, the Goal section of the wave doc states explicitly why the walking-skeleton default was rejected. A horizontal W1 still needs user-observable exit criteria — even "prove the algorithm works" should exit with a demonstrable test, not team satisfaction.

## Wave ordering principles

After W1, ordering the remaining waves is a judgment call with a clear priority order when the criteria conflict.

### Principle 1: Risk-first

Among candidate next waves, put the one that most reduces uncertainty first. Scariness is a function of:

- **Technical uncertainty** — "we don't know if the tagger will be accurate enough" is scarier than "we need a settings page."
- **Requirements uncertainty** — "we don't know if users will accept magic-link auth" is scarier than "we know we need CRUD on clubs."
- **Dependency weight** — things many future waves depend on are scarier than leaf features.

Rolling-wave's value is maximized when each wave reduces the most uncertainty. If a wave doesn't reduce meaningful uncertainty, ask whether it should be later.

### Principle 2: Value as tiebreaker

When two candidate waves have similar risk profiles, pick the one delivering more user value. Keeps stakeholders' confidence up and ensures that if the project stops after any wave, the built system is still useful.

### Principle 3: Size for learning, not tidiness

Each wave should be small enough to specify comprehensively without guessing, and large enough to produce something observable. If two waves look "uneven," fine — uneven wave sizes are not a bug. Awkward-sized waves usually mean you're optimizing for plan aesthetics instead of for learning rate.

A wave sized for one developer-agent session to a week of sessions is usually about right. Beyond a week, split.

### Principle 4: Continuity with commitments

Later waves should extend, not rebuild, the architecture. If a candidate wave would require superseding a W1 commitment, think hard — is that the right next wave? Sometimes yes (the commitment was premature and execution proved it). Often the real answer is that the candidate wave was mis-scoped and should be rethought to fit within the existing commitments, with the commitment revisited only when its actual cost is clear.

## Task and story sizing

Within the current wave (W1), tasks and stories have specific quality bars.

### Story quality

Every story has:

- **Role + goal + benefit** in a single sentence structure.
- **At least one acceptance bullet** in given/when/then form.
- **Priority** — must-have, should-have, or nice-to-have. For W1, default most stories to must-have; the walking skeleton shouldn't carry polish stories.

A story that reads like a UI spec ("as a user I want a dropdown") is wrong. Rewrite it at the value level ("as a user I want to pick from options I know about"). A story with three disconnected acceptance bullets is two stories; split it.

### Feature quality

Every feature:

- Has a one- or two-sentence description.
- Names the stories it supports. A feature without stories is either plumbing (label it) or scope creep.
- Is a capability, not a component. "Search" is a feature; "Elasticsearch" is a component.

### Task quality

Every task:

- Fits in one agent session (a few hours of focused work). If the description has "and then" or "followed by", split.
- Has at least one testable acceptance criterion. Good acceptance is specific:

  Bad: "The scan command works."
  Good: "`filetagger scan <dir>` exits 0 on a directory of mixed files, writes at least one row per file to `~/.filetagger/index.db`, and produces stderr only on actual errors."

- Cites what it serves — a story or feature ID, or "plumbing" for implicit scaffolding. Silent scope drift sneaks in as untagged plumbing; name it.
- Has an ordering intent. The first task should be the one that most reduces uncertainty — usually the end-to-end integration task, even if "bigger" than unit tasks.

### The repro path task

Every wave has a repro path, and it's usually worth making it an explicit task in the wave. Something like:

> T<N>.4 — End-to-end demo and repro.
> Acceptance: `scripts/demo-w<N>.sh` exists, is executable, exercises all of this wave's exit criteria, and prints PASS/FAIL per check. Passes in CI.
> Serves: plumbing (repro path).

This makes the auditor's job mechanical: run the demo script, read the output. Without an explicit repro task, the demo scaffolding tends to sprawl across other tasks and get lost.

## Filling each section

See `references/wave-schema.md` for format. Per-section notes the schema doesn't say explicitly:

**Goal and non-goals**: rewrite in your own words — don't quote the input. The wave doc is a fresh artifact and the goal should read as if written for it. Non-goals are load-bearing; include them even if the input didn't.

**Roles**: if the input names job titles, translate to role definitions ("what are they trying to do?"). If the input lists five roles but three would do most of the work, flag the redundancy in your head but capture what's stated — only consolidate if the user confirms.

**Waves overview**: the one-line goal sharpens the wave. If you can't describe a wave's goal in ten words, the wave is fuzzy — sharpen the wave, not the description.

**Future-wave sketches**: keep them short. The schema permits 2–4 sentences for the approach sketch. More than that and you're over-planning.

**Assumptions**: distinguish from architectural commitments carefully. "We'll use SQLite" is a commitment (a choice). "SQLite will be fast enough for 10k files" is an assumption (a belief about the world). The same technical decision can have both.

**Commitments**: every commitment has a rationale. Pad-protection — if a commitment's rationale is "it seemed easier," either delete the commitment or do the thinking to find its real rationale.

## Handoff to the next skill

The wave doc's W1 is now ready for execution. The next step in the user's workflow is `wave-execute`, which reads the doc and implements W1. When writing the doc, imagine an executor agent opening W1 and trying to start work — would they know exactly what to do? If yes, you're done. If no, W1 needs more concreteness (usually in acceptance criteria or exit criteria, not in more text).

After wave-execute completes, `wave-audit` runs independently, then `wave-redraft` advances the doc. The four skills form the DEAR loop: Draft → Execute → Audit → Redraft. Your job is the first D.

## When the input is thin

If the input is one paragraph, don't produce a 40-page doc of invented detail. Produce a shorter doc that genuinely reflects what's known, put everything else in Section 9 (Themes not yet waved) or in the assumptions register as `untested`. A short honest wave doc is much more useful than a long confident one.

If the input names a goal but no roles, ask for roles before drafting — roles shape the whole stories section. If the input names roles but no non-goals, proceed but raise the non-goals question in the Open questions embedded in Section 1 (as part of goal/non-goals prose) so the user sees the gap.

## Principles to keep in mind

**Current in detail, future in sketch.** The structural distinction between W1 and future waves is load-bearing. Don't blur it.

**Every claim is traceable.** Stories cite features, features cite stories, tasks cite what they serve. A draft whose traceability doesn't work is a draft with hidden scope issues.

**Scope discipline.** The input is a boundary, not a suggestion. Compelling ideas that are out of scope go in Section 9 with a one-line note, not silently into future-wave sketches.

**Walking-skeleton bias.** When in doubt about W1's shape, default to the thinnest vertical slice that instantiates the architecture. The comfort of a "comprehensive foundations" W1 is almost always the wrong comfort.

**Don't invent facts.** When the input doesn't say something, say so. An assumption register entry with `untested` is more useful than a confident guess in the goal section.

## Invariants — things to never do

From the schema, worth repeating:

1. **No task-level detail in future waves.** Even if a future task is "obvious," don't write it down.
2. **No per-story acceptance criteria or feature definitions in future waves.** Titles only.
3. **Every current-wave task and story has acceptance.** No exceptions.
4. **W1 has a repro path.** A wave that can't be exercised end-to-end can't be audited.
5. **Every commitment has a rationale.** No bare commitments.
6. **Every story and feature traces to a wave or to Section 9.** No floating requirements.
7. **Walking-skeleton default unless explicitly justified.** Horizontal W1 needs a reason in the Goal section.
