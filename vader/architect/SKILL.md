---
name: architect
description: Use this skill at two distinct moments in a VADER project. (Mode = draft) When a vision doc exists and an initial architecture doc is needed before drafting the wave plan. Triggers include phrases like "draft the architecture for this project", "produce an architecture doc and Decision Log from this vision", "design the modules and key interfaces for X", or whenever the user wants the structural decisions for a new project committed to writing before wave planning starts. (Mode = ratify) After the user has reviewed the proposed architecture and decisions, to flip Proposed Decision Log entries to Accepted in one pass. Trigger when the user says "ratify the architecture" or "accept the proposed decisions". Do NOT use for mid-cycle architectural revision — that's handled by `wave-update`'s review subagent. Do NOT use to produce code, scaffolding, or implementation; this skill produces decision documents only.
---

# Architect

Produce or ratify the initial architecture doc + embedded Decision Log for a project. This is essentially a one-shot upfront tool plus a short follow-up to ratify. Mid-cycle architectural change is detected and applied by `wave-update`, not here.

This skill has two modes: **draft** (initial drafting; produces architecture.md with Proposed Decision Log entries) and **ratify** (after human review, flips Proposed entries to Accepted).

Before doing anything else, read `references/architecture-schema.md` in full. The schema defines the doc shape, the Decision Log entry format, the lifecycle, and the graduation rules for promoting entries to separate ADR files.

## Mode: draft

**Inputs:** the vision doc (`<project-slug>-vision.md`); optionally prior art the user wants considered; optionally hard constraints not in the vision.

**Output:** `<project-slug>-architecture.md` with frontmatter `architecture_version: 1`, `status: active`, `adr_promoted_log: false`. Embedded Decision Log section contains seed entries with status `Proposed`.

**Workflow:**

0. **Detect brownfield and orient.** Before drafting, check whether the working directory contains existing source code (manifest files, `src/` / `lib/` directories, top-level scripts). If yes, this is a *brownfield* architecture draft: the system already exists in some form, and the architecture doc documents what's there plus what should change. Read the top-level structure: directory layout, build/test entry points, primary dependencies, and a representative file or two from each apparent module. Goal is not exhaustive reverse-engineering — it's enough orientation that the modules you propose match the names and boundaries the code already establishes (or, where they shouldn't, you can name the divergence explicitly as a Decision Log entry: "ADR-NNN: rename the existing `core` module to `engine` because…"). On greenfield projects (no existing code), skip this step and propose modules from the vision directly.

1. **Read the vision carefully.** Extract: constraints (§7), non-goals (§5), in-scope capabilities (§4), roles (§2), success metrics (§6), open questions (§9), and core journeys (§10) if present. Constraints and non-goals constrain decisions directly; in-scope capabilities determine what modules must exist; success metrics shape non-functional considerations.

2. **Read core journeys if present.** For product-heavy projects, journeys are the strongest input to module decomposition. Walk each journey end-to-end and ask: which module owns each step? Where do steps cross module boundaries (those become key interfaces)? Where does a journey reveal that two notional modules should be one (or vice versa)?

3. **Sketch the system overview first.** 2-3 paragraphs describing what runs where and what the request lifecycle looks like end to end. Even for trivial systems — "this is a single-binary CLI invoked locally; there is no server" is itself worth writing down.

4. **Identify the modules.** A module is a unit of responsibility, not a file. The right granularity is "what could plausibly be replaced or significantly revised without rewriting everything else?" For most projects this lands at 4-8 modules.

   For each module, mark its **W1 activation status** in the Section 2 module table:
   - `required` (default) — must be exercised by W1's walking skeleton.
   - `deferred (W<N>)` — the module is part of the system but doesn't need to be in W1's vertical slice; expected to come online in W<N>. Use only when you can name *why* W1 doesn't need it and *which* wave brings it online.

   `wave-plan` uses this column to scope its walking-skeleton completeness check. Default to `required`; mark `deferred` only when you have a clear reason. See `references/architecture-schema.md` Section 3 for the full column format.

5. **Identify the consequential decisions.** For each category — persistence, auth, deployment, key interfaces, language/runtime, data model — decide whether the vision determines the choice obviously or whether there's a real decision. For real decisions, draft a Decision Log entry. For obvious choices, note them in the body without an entry. Rule of thumb: an entry's `Consequences` section must include at least one negative consequence; if you can't think of one, it's an obvious choice.

6. **Draft the Decision Log entries.** Status `Proposed (today's date). Drafted by architect draft.` Use the entry format from architecture-schema §4 — title, Status, Context, Decision, Consequences (including negative), Supersedes/Superseded by. Sequential ADR-NNN IDs, never reused. Keep the architecture.md decision log embedded — don't promote to separate files until the project earns it.

7. **Fill in the architecture doc body.** Sections 1-7 cite Decision Log IDs in module descriptions, key interfaces, data sections. Mark sections "TBD in W<N>" if a detail is deliberately deferred to a wave.

8. **Save and hand off.** Write the doc with all entries marked `Proposed`. Iterate with the user (1-2 rounds is normal). Each iteration revises the proposed entries in place. The user is heavily involved in architecture by design — don't rush them past review.

**Principles:**

- Commit only what's expensive to revise later. Persistence, auth, deployment, language/runtime, key interfaces between modules. Don't commit to algorithms or anything that lives inside a module.
- Cite the vision. Every Decision Log entry's Context grounds the decision in the vision.
- Modules are responsibilities, not files.
- Leave gaps deliberately. If the wave plan is the right place to settle something, mark "TBD in W<N>" in the architecture body.
- Walking-skeleton requires architectural completeness. Every module needed for the vertical-slice W1 must exist in name and responsibility, even if its inside is empty in W1.

**When the vision is thin:** push back. Suggest the user re-invoke `vision draft` to tighten the value hypothesis and reduce open questions before architecture is committed. Architecture drafted on a thin vision will be either over-confident (inventing detail) or fragile (substantially revised when the vision tightens). Only fall back to a deliberately minimal architecture if the user has explicit time pressure and accepts the trade-off.

## Mode: ratify

**Inputs:** an existing architecture doc whose Decision Log contains one or more entries with `Status: Proposed (date). Drafted by architect draft.`

**Output:** the same architecture doc, with each Proposed seed entry's `Status` line updated to `Accepted (today's date). Established by architect draft, ratified <today>.`

**Workflow:**

1. Confirm with the user that they've reviewed the proposed architecture and entries. Don't ratify without explicit signoff.
2. Walk every entry in the Decision Log section. For each with status starting `Proposed (...). Drafted by architect draft.`, update to `Accepted (today). Established by architect draft, ratified <today>.`
3. Bump the architecture doc's frontmatter `last_updated` to today.
4. Save the doc.
5. Hand off — `wave-plan` is now unblocked.

**Note:** This mode is for *initial* seed entries only. Mid-cycle Proposed entries (those with `Drafted by wave-update review`) are not this skill's concern; wave-update ratifies them inline within its own invocation.

## Things to never do

1. **Never write architecture body changes without a corresponding Decision Log entry.** Body and decisions stay in lockstep.
2. **Never mark an entry Accepted in draft mode.** Initial entries always start Proposed; ratification is a separate human-confirmed step.
3. **Never edit an Accepted entry's body.** If the decision needs to change, that's a wave-update concern (a new entry supersedes the old).
4. **Never re-invoke draft mode against an existing architecture doc** unless the user wants a wholesale rethink (rare). Most architectural change is incremental and goes through wave-update.
5. **Never produce code or scaffolding.** This skill produces decision documents only.
6. **Never reuse retired or superseded ADR IDs.**

## Handoff

After draft mode, tell the user to review the proposed architecture and entries, then re-invoke this skill in `ratify` mode (or manually flip each `Status` field). After ratify mode, tell the user the next step is `wave-plan`.

**Git.** Check whether git is in use (`git rev-parse --is-inside-work-tree`). If yes, after the user approves the artifact, commit yourself:
- Draft mode: `git commit -m "arch: initial draft, ADR-001 through ADR-NNN (proposed)" -m "Co-authored-by: Claude <noreply@anthropic.com>"`. No tag yet — the architecture is not yet ratified.
- Ratify mode: `git commit -m "arch: ratify initial architecture, ADR-001 through ADR-NNN" -m "Co-authored-by: Claude <noreply@anthropic.com>"` then `git tag arch-v1`.

Tell the user about each commit (sha, tag if any). Override with `git reset --soft HEAD~1` if amending is needed. If git is not in use, save normally and note no commit was made. See `../references/git-conventions.md`.
