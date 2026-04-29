# Phase 2 -- Venue Judgment and Draft

Loaded when Phase 2 begins. Also load `references/venue-norms.md`.

Phase 2 is the drafting and revision phase. The LLM turns the Phase 1 brainstorming into a review draft, applies the venue lens, answers the required reviewer questions, and revises in response to the user's feedback.

Four sub-steps, with a fast path when the venue is already clear. Settle the venue standard (2a) -> produce a draft review plan (2b) -> write the draft and venue-form answers (2c) -> revise from user feedback (2d).

If the user reached Phase 2 by asking to draft early, carry forward whatever Phase 1 produced. Missing Phase 1 findings are noted as gaps.

---

## 2a -- Venue standard

Open `references/venue-norms.md`.

### If the venue is on file

Read the stored entry and review it actively before surfacing. Check:

- **Currency.** Anything that may be outdated: chair priorities, methodological emphases, artifact requirements, journal review-form questions.
- **Gaps relative to this paper.** For example, an LLM-based educational tool may raise AI, ethics, reproducibility, or evaluation expectations the older entry does not address.
- **Internal inconsistencies.** Contradictory or vague guidance.
- **Reviewer form schema.** If the entry includes a reviewer form, surface it alongside the durable character. Remind the user to verify the current question set against the venue's reviewer instructions before submitting.

Surface the stored standard and the LLM's concerns together. For each concern give specific reasoning. Do not rubber-stamp.

Remind the user once to verify the venue's current reviewer AI-assistance policy directly. Do not infer it, and do not write it into `references/venue-norms.md`.

The user adjudicates each concern. If the user updates the durable standard, write the edits back to `references/venue-norms.md` after approval, in the file's existing entry format.

### Fast path for settled on-file venues

Use this path when all three conditions hold:

- the venue is on file
- the LLM sees no currency concerns, no paper-specific gaps, and no internal inconsistencies
- the stored reviewer form, if any, is adequate for the paper

In that case, summarize the standard in one or two lines, state that no concerns were found, ask for quick approval, and proceed to 2b after the user approves.

### If the venue is not on file

Propose a draft entry based on general knowledge of similar venues. State explicitly: this is the LLM's best read, not authoritative -- the user must sanity-check against the current CFP, reviewer instructions, and any editor or chair guidance. Cover at minimum: orientation, methodological expectations, literature-engagement expectations, contribution expectations, common red-line issues, and recommendation taxonomy.

Ask the user whether the venue uses a structured reviewer form. If so, capture the questions verbatim under a `### Reviewer form` subsection in the entry. The form drives 2c's draft structure.

Remind the user once to verify the venue's current reviewer AI-assistance policy directly. Do not infer it, and do not write it into `references/venue-norms.md`.

After the user edits and approves, append the durable new entry to `references/venue-norms.md` matching the file's format.

### Hold

Do not move to 2b until the venue standard is approved, unless the user explicitly asks for a rough draft.

---

## 2b -- Draft review plan

Inputs: all Phase 1 cluster outputs -- what the authors propose/did, intellectual move, conceptual interest, contribution and novelty, claim/evidence/literature-support verdicts, literature-positioning findings, gaps/flaws/weaknesses-as-findings, soundness/coherence read, venue-question preview, and venue-sensitive flags.

2b is where the LLM converts Phase 1 findings into a compact plan for the draft. Do this in one pass unless the case is unusually complex: for example, mixed paper types require multiple rubrics, the venue standard has unresolved gaps, the recommendation depends on several contested findings, or the paper has many central claims.

### Plan by the seven review questions

Organize the plan around the canonical seven review questions in `workflows/phase-1.md`. If the seven questions are not already in context, read the opening section of `workflows/phase-1.md` before drafting the plan. For question 6, carry forward Phase 1's soundness/coherence read and translate it into publishability in the named venue.

For each item, state the likely draft content, the paper evidence that anchors it, and any venue norm that changes its significance.

### Map findings to the venue

Propose how it maps under the venue standard:

- **Strength.** Cite the specific venue norm that makes it count as a strength.
- **Weakness.** Cite the specific venue norm. Include context: what the weakness is, why it qualifies under the standard, and what it implies for the paper. Weaknesses must have substance.
- **Minor issue.** Use this for typos, figure legibility, citation formatting, small missing details, or local writing problems that do not affect the paper's contribution or evidence.
- **Neither.** Some findings are real but venue-neutral.
- **Norm silent.** If the venue standard does not address the finding, surface it back to 2a as a gap.

Do not propose a weakness unless it meaningfully affects the paper's contribution, evidence, or venue fit. If substance and consequence cannot be articulated, drop the candidate or route it to minor issues.

### 2b output

A compact draft plan:

- Seven-question synthesis, including the paper citations each section will rely on.
- Venue-aligned strengths, weaknesses, minor issues, and norm-silent gaps.
- Proposed venue-relative publishability judgment and recommendation.
- Venue-form questions to answer, if any.

---

## 2c -- Draft and venue questions

Once the draft plan is settled or the user asks to proceed, write the draft to `review-<short-title>.md` in the user's invoking working directory or project directory, not inside the skill directory unless the user invoked the skill from there intentionally. State the exact output path before writing.

### Required draft structure

The draft has two layers when the venue uses a reviewer form: a **decision-support layer** and a **form-response layer**. When the venue has no form on file, only the decision-support layer and closing sections apply.

**Decision-support layer**, always present, organized as a synthesis of the canonical seven review questions from `workflows/phase-1.md`. If the seven questions are not already in context, read the opening section of `workflows/phase-1.md` before drafting. Use concise section headings, and make question 6 explicitly venue-relative: **Soundness/coherence and venue publishability**.

Use the venue's recommendation taxonomy: accept / weak accept / borderline / weak reject / reject for conferences, or accept / minor revision / major revision / reject for journals, unless the stored venue form says otherwise.

The publishability reasoning must be auditable:

- which strengths support publication
- which weaknesses block or limit publication
- whether weaknesses are fixable with revision or require new work
- how the balance lands under the venue standard

The user decides the recommendation. The LLM only pushes back if the user's choice is internally inconsistent with their Phase 1 findings and 2b plan. If the user confirms it is a weighting call, defer.

**Form-response layer**, only when the venue has a reviewer form in `references/venue-norms.md`:

Answer each question verbatim from the venue's form, in the venue's order. Draw on the decision-support layer; do not re-derive findings already covered above. Read each question literally. Questions such as "Have the authors emphasized strengths?" or "Have the authors stated limitations?" ask about the manuscript's self-presentation, not the reviewer's own assessment.

For **Computers and Education Open**, answer all stored questions directly:

- objectives and rationale
- replicability/reproducibility
- statistical analyses, controls, sampling, and reporting if applicable
- tables and figures
- whether conclusions are supported by data
- whether authors emphasize strengths
- whether authors state limitations
- structure, flow, and writing
- language editing

**Closing sections**, always:

1. **Questions for authors.** Genuine questions whose answers would change something. Not rhetorical or veiled criticisms. This is the one section addressed to the authors directly.
2. **Minor issues.** Typos, figure legibility, citation formatting, local wording issues. Brief.

---

## 2d -- User feedback and revision

After writing the draft, invite targeted feedback. Revise the draft directly when the user gives changes, while preserving citation discipline and venue-form coverage.

Common revision requests:

- change recommendation or severity
- strengthen or soften a weakness
- add a missing strength
- convert a criticism into a question for authors
- make the form responses more direct
- shorten, anonymize, or change tone

If the user's requested revision conflicts with paper evidence, point out the conflict and ask what paper evidence they want to rely on. If it is a weighting choice, defer to the user.

### Discipline

- Address the program committee or editor throughout, except in Questions for Authors.
- Every evaluative claim cites paper evidence. Never invent paper-internal citations; if a section, page, table, or figure cannot be found, say that and either cite a reachable location or leave the claim out.
- Severity is committed, not conditional -- 2a/2b have already resolved the venue-weighting question. The one exception is findings 2b flagged as norm-silent gaps.
- No confidence labels.
- Plain prose with section headers. Bullets only for genuinely list-like content.

### Handing over

Tell the user the file path. The review is theirs; revisions are theirs to request. Do not summarize the conversation, do not run a calibration ritual, do not ask if they want anything else. If they come back with edits, revise.
