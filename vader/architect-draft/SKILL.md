---
name: architect-draft
description: Use this skill when a vision doc exists and an initial architecture doc plus seed ADRs are needed before drafting the wave doc. Triggers include phrases like "draft the architecture for this project", "produce an architecture doc and initial ADRs from this vision", "what's the architecture for X", "design the modules and key interfaces for this project", or whenever the user wants the structural decisions for a new project committed to writing before wave planning starts. Also trigger when a vision pivot has invalidated the existing architecture and the user wants the architecture re-drafted from the new vision (rare; usually architect-review handles incremental change). Do NOT use for incremental architectural revision after a wave's audit — that's architect-review. Do NOT use to produce code, scaffolding, or implementation; this skill produces decision documents only.
---

# Architect Draft

Produce the initial architecture doc and seed ADRs for a project, drawing structural decisions from the vision doc. This is the second skill in the VADER loop, between `vision-shaper` and `wave-draft`. The output gives `wave-draft` a stable structural target to plan against.

Before doing anything else, read `references/architecture-schema.md` in full. The schema defines the artifacts' shape, the ADR template, and the supersession rules. This SKILL.md describes the judgment calls that produce a *useful* initial architecture.

## What this skill does

Take a vision doc and produce two things: a single architecture doc that describes how the system will be built, and a small set of ADRs (typically 3-7) that capture the most consequential structural decisions made during the draft. Together they answer "if you're going to start building this tomorrow, what shape is the system, and which choices are already made?"

The skill does *not* design every detail. It commits the choices that would be expensive to revise later — persistence, auth, deployment, key interfaces, language/runtime — and explicitly leaves the rest for later waves to settle. Over-committing now is exactly as wrong as under-committing.

## Inputs and output

**Inputs:**
- The vision doc (`<project-slug>-vision.md`). Required. The architecture inherits goal, scope, non-goals, constraints, and success metrics from it.
- (Optional) Any prior art the user wants considered — existing systems they want to mirror or avoid, prior projects' architecture docs, reference architectures.
- (Optional) Hard constraints not in the vision — e.g., "must run in this team's existing GCP project."

**Outputs:**
- `<project-slug>-architecture.md` written to the project's `docs/` directory.
- `<project-slug>-adr/ADR-001-<slug>.md` through `ADR-NNN-<slug>.md` for each seed ADR. Frontmatter and body conform to schema Section 4. **Each ADR's initial status is `Proposed (YYYY-MM-DD). Drafted by architect-draft.`** — *not* `Accepted`. ADRs are accepted only after the human reviews and ratifies them (see step 7 below).
- The architecture doc's frontmatter has `architecture_version: 1`, `status: active`.

This skill has two modes: **draft mode** (the default — produce the proposed architecture) and **ratify mode** (invoked after human review — flip all `Proposed` ADRs to `Accepted`). Both are described in the workflow below.

## Workflow

### 1. Read the vision carefully

Extract the structural inputs:
- **Constraints (§7)** are non-negotiable. They constrain ADRs directly.
- **Non-goals (§5)** prevent over-architecture. If the vision says "no cloud sync," do not design for cloud sync.
- **In scope (§4)** is the set of capabilities that must be supported by the modules in Section 2 of the architecture doc.
- **Roles (§2)** influence auth and session model.
- **Success metrics (§6)** influence non-functional considerations (performance budgets in particular).
- **Open questions (§9)** become future-ADR candidates rather than current-ADR commitments.
- **Core journeys (§10), if present.** For product-heavy projects, the journeys are the strongest input to module decomposition. Walk each journey end-to-end and ask: which module owns each step? Where do steps cross module boundaries (those are key interfaces)? Where does a journey reveal that two notional modules should be one (or vice versa)? The friction-now line on each journey often points to where a non-functional consideration matters most.

If the vision lacks Section 10 and the project is product-heavy, push back: "the journeys would be useful here — want to add them before I commit to a module decomposition?" If the project is infra/tech, the absence of Section 10 is normal and expected.

If the vision is genuinely incomplete on something the architecture must address, ask the user one focused question. Don't fabricate an answer.

### 2. Sketch the system overview first

Before deciding on persistence or auth or anything specific, write a 2-3 paragraph system overview describing what runs where and what the request lifecycle looks like end to end. Do this even for trivial systems — "this is a single-binary CLI invoked locally; there is no server" is itself a structural statement worth writing down.

If you cannot describe the system shape coherently in three paragraphs, the project is too ambitious for this draft pass — push back on scope rather than producing a vague architecture.

### 3. Identify the modules

A module is a unit of responsibility, not a file. The right granularity is "what could plausibly be replaced or significantly revised without rewriting everything else?" For most projects this lands at 4-10 modules. More than that and you're over-decomposing; fewer and you're under-thinking the seams.

For each module, write the responsibility in one sentence. Don't write the implementation. The wave doc's tasks will reference these modules; if a module's responsibility is murky, those tasks will be too.

### 4. Identify the consequential decisions

Walk through the categories — persistence, auth, deployment, key interfaces, language/runtime, data model — and for each, decide whether the project's vision and constraints determine the choice obviously, or whether there's a real decision to be made.

For each *real* decision, plan an ADR. For obvious choices (e.g., "we'll write this in Python because that's the team's language"), don't create an ADR — note them in the architecture doc body as context, not as decisions.

A good rule of thumb: an ADR's `Consequences` section must have at least one negative consequence. If you can't think of a downside to the choice, it's an obvious choice and not ADR-worthy.

### 5. Draft the ADRs

For each consequential decision, write a full ADR file conforming to schema Section 4. Status is `Accepted` and is dated today. Established by `W1 architect-draft`.

Order the ADRs by the order in which the decisions logically depend on each other. Persistence usually comes first; auth often depends on persistence; deployment often depends on both.

Each ADR has its own file: `<project-slug>-adr/ADR-NNN-<slug>.md`. Numbered sequentially. Don't skip numbers.

### 6. Fill in the architecture doc body

Now that the ADRs exist, write the architecture doc body. Each section cites the relevant ADRs.

- **System overview (§1):** the paragraphs from step 2, refined.
- **Module decomposition (§2):** the modules from step 3, with the ADR(s) that govern each.
- **Key interfaces (§3):** the contracts between modules. Don't invent detail; if an interface is not yet decided, leave it as "TBD in W<N>" with a note.
- **Data model (§4):** persistence schema at the table/collection level. Cite ADRs.
- **Auth and identity (§5):** the identity model. Cite ADRs.
- **Deployment and operations (§6):** how it runs. Cite ADRs. Even "no operational surface — local-only" is a section.
- **Non-functional considerations (§7):** performance budgets from success metrics, security posture, anything cross-cutting.

### 7. Save in draft mode (Proposed)

Write the architecture doc and all ADR files. **Each ADR's `Status` field is `Proposed (today's date). Drafted by architect-draft.`** Save these as actual files — they are real artifacts, just not yet ratified. Iterate with the user (1-2 rounds of revision is normal); each iteration revises the proposed file in place. The user is heavily involved in architecture by design — don't rush them past review.

### 8. Ratify on user signoff (the second mode)

Once the user has reviewed the architecture and ADRs and explicitly approves, ratify them. Two acceptable mechanisms:

- **Re-invoke `architect-draft` with the instruction "ratify"** — the skill walks every ADR file in the ADR directory whose status is `Proposed (date). Drafted by architect-draft.` and updates each to `Accepted (today's date). Established by W1 architect-draft, ratified <today>.`. The architecture doc's status is confirmed as `active`.
- **Or the user manually edits each ADR's `Status` field** to `Accepted (date). Established by W1 architect-draft.` — this is acceptable for users who prefer reviewing changes diff-by-diff in their editor.

`wave-draft` will refuse to run while any cited ADR is still `Proposed`. So ratification (by either mechanism) is the gate that unblocks wave planning.

### 9. Hand off

After ratification, tell the user the next step is `wave-draft`, which will read both the vision doc and the architecture doc and produce a wave doc with W1 fully planned as a walking skeleton.

## Principles to keep in mind

**Commit only what's expensive to revise later.** Persistence, auth, deployment, language/runtime, key interfaces between modules. Don't commit to algorithms, UI components, or anything that lives inside a module.

**An ADR with no downsides hasn't been thought through.** Force yourself to write at least one negative consequence for every ADR. If you can't, the decision is either obvious (don't ADR it) or under-considered (think harder).

**Cite the vision.** Every ADR's Context section should ground the decision in the vision. "Constraint §7 specifies budget under $50/month, which rules out X" is the kind of grounding that makes ADRs durable.

**Modules are responsibilities, not files.** "auth", "polls", "scheduling" are modules. "src/lib/utils.py" is not.

**Leave gaps deliberately.** If the wave doc will be the right place to settle a decision (e.g., the exact wire format for a CLI subcommand), the architecture doc says "TBD in W<N>" and explains why this particular gap is being held open.

**Walking skeleton requires architectural completeness.** W1 in the wave doc will be a vertical slice through every module. That means every module needs to exist *in name and responsibility* in the architecture doc, even if its inside is empty in W1. If the architecture doc is missing a module that a vertical slice would need to exercise, the wave doc draft will fail.

## Anti-patterns to avoid

**Over-architecture.** Drafting a microservices diagram for a project that is plausibly a single binary. Cite the vision's scale and constraints; make the simplest architecture that fits.

**Decision-by-default.** "We'll use PostgreSQL" without justifying it against the vision is decision-by-default. If PostgreSQL is right, an ADR explaining why (and what the alternatives were) makes that durable. If it's not right, the question gets asked.

**Premature interface lock-in.** Specifying RPC signatures or HTTP routes in detail at this stage is over-commitment. Stick to the level of "module A exposes a method to do X to module B" and let the wave that builds it nail down the signature.

**Hidden assumptions.** If your ADR depends on an assumption from the vision's Open Questions, cite the assumption ID. Don't quietly assume the open question resolves your way.

**Architecture drift from vision constraints.** Re-read the vision's Constraints (§7) and Non-goals (§5) before declaring the draft done. Architecture choices that violate either are bugs.

## What to do if the vision is thin

A vision doc with one or two open questions is well-shaped. A vision doc with twenty open questions and a vague value hypothesis is thin. In the latter case, *do not* compensate by inventing structural detail.

The preferred response is to hand back to the user and suggest a vision-shaping pass (re-invoking `vision-shaper`) to tighten the value hypothesis and reduce open questions before architecture is committed. Architecture drafted on a thin vision will be either over-confident (inventing detail to fill the gap) or fragile (likely to be substantially revised when the vision tightens).

Only when the user has explicit time pressure and accepts the trade-off, fall back to producing a deliberately minimal architecture: a system overview, a module list with terse responsibilities, and 2-3 ADRs covering only the decisions that the existing vision strictly requires. Mark every other section "TBD in later waves" and say so explicitly. Note in your handoff that this is a deliberate corner-cutting move and that the architecture should be revisited (via `architect-review` or a fresh `architect-draft` pass) once the vision tightens.

## Worked mini-example (truncated)

Vision: a local CLI that tags files by content (filetagger). Solo dev, 6-month build, runs on user laptops only.

Modules (4):
- `walker` — directory traversal, file discovery.
- `tagger` — content extraction + LLM call to derive tags.
- `index` — persistence of tags, query.
- `cli` — argument parsing, output formatting.

Consequential decisions (each becomes an ADR):
- ADR-001: Persistence — SQLite at `~/.filetagger/index.db`. (Vision constraint: zero-ops, embedded.)
- ADR-002: Tagger backend — remote LLM API, configurable provider. (Vision: tag quality is the product; local models not yet competitive.)
- ADR-003: Distribution — single-binary CLI via PyInstaller. (Vision: users install one file.)

Non-decisions (don't ADR):
- Language: Python (team's language; the vision doesn't constrain this; it's not a deep choice).
- Module structure inside `walker`: out of scope at this stage.

Architecture doc references each ADR by ID. Section 7 (Non-functional) cites the vision's success metric "under 2s for 10k files" as a performance budget without making it an ADR (it's a target, not a structural decision).

## Handoff

After the architecture is drafted and the ADRs are saved (as `Proposed`), tell the user the next steps are: review the architecture and ADRs; ratify them (either by manually flipping each ADR's `Status` to `Accepted (date)` and bumping the architecture doc to status `active` ratified, or by re-invoking `architect-draft` in `ratify` mode); then run `wave-draft`. `wave-draft` will refuse to run while any cited ADR is still `Proposed`.

**Git.** If the project uses git, suggest the user make two commits — one when the proposed draft is saved (`arch: initial draft, ADR-001 through ADR-NNN (proposed)`), and a second after ratification (`arch: ratify initial architecture, ADR-001 through ADR-NNN`). Tag `arch-v1` on the ratified commit. Add a `Co-authored-by: Claude <noreply@anthropic.com>` trailer on both. See `references/git-conventions.md`.
