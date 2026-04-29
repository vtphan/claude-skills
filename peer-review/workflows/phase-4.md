# Phase 4 — Synthesis, venue fit, and draft

Loaded when Phase 4 begins. Also loads `references/venue-norms.md`.

Four sub-steps, each a distinct dialogue moment. Do not skip ahead. Settle the venue standard (4a) → translate findings into venue-relative strengths and weaknesses (4b) → settle the recommendation (4c) → write the draft (4d).

If the user reached Phase 4 by skipping ahead, carry forward whatever Phases 1–3 produced. 4b works with what is available; missing earlier-phase findings are noted as gaps.

---

## 4a — Venue standard

Open `references/venue-norms.md`.

### If the venue is on file

Read the stored entry and review it actively before surfacing. Check:

- **Currency.** Anything that may be outdated — chair priorities, methodological emphases that have shifted, artifact requirements.
- **Gaps relative to this paper.** An AIED submission may raise expectations the older entry does not address.
- **Internal inconsistencies.** Contradictory or vague guidance.
- **Reviewer form schema.** If the entry includes a reviewer form, surface it alongside the durable character. Remind the user to verify the current question set against the journal's reviewer instructions before submitting — forms change. The form is what the draft answers in 4d.

Surface the stored standard and the LLM's concerns together. For each concern give specific reasoning ("this paper raises [X], the stored standard does not address it, recommended addition is [Y]"). Do not rubber-stamp.

Remind the user once to verify the venue's current reviewer AI-assistance policy directly. Do not infer it, and do not write it into `references/venue-norms.md`.

The user adjudicates each concern. If the user updates the durable standard, write the edits back to `references/venue-norms.md` after approval, in the file's existing entry format.

### If the venue is not on file

Propose a draft entry based on general knowledge of similar venues. State explicitly: this is the LLM's best read, not authoritative — the user must sanity-check against the current CFP, reviewer instructions, and any chair guidance. Cover at minimum: orientation (practitioner / research / hybrid), methodological expectations, literature-engagement expectations, common red-line issues.

Ask the user whether the venue uses a structured reviewer form (a fixed set of questions reviewers must answer). If so, capture the questions verbatim under a `### Reviewer form` subsection in the entry. The form drives 4d's draft structure.

Remind the user once to verify the venue's current reviewer AI-assistance policy directly. Do not infer it, and do not write it into `references/venue-norms.md`.

After the user edits and approves, append the durable new entry to `references/venue-norms.md` matching the file's format.

### Hold

Do not move to 4b until the venue standard is approved.

---

## 4b — Venue-lens assessment

Inputs: all findings from Phases 1–3 — Phase 1's coherence and intellectual-move findings, Phase 2's relevance findings, Phase 3's per-claim verdicts and cross-claim methodological findings.

4b is where findings become venue-relative strengths and weaknesses, or neither.

### Batch by category

Group findings into batches: methodology, conceptual merit, evidence, impact, literature engagement, reporting. Walk one batch at a time; the user adjudicates each batch before the next.

### For each finding

Propose how it maps under the venue standard:

- **Strength.** Cite the specific venue norm that makes it count as a strength.
- **Weakness.** Cite the specific venue norm. Include context: what the weakness is, why it qualifies under the standard, what it implies for the paper. Weaknesses must have substance — stylistic, trivial, or nit-pick findings do not become weaknesses; they become minor issues. If substance and consequence cannot be articulated, drop the candidate.
- **Neither.** Some findings are real but venue-neutral — note and move on.
- **Norm silent.** If the venue standard does not address the finding, surface it back to 4a as a gap.

Severity of weaknesses is resolved here. Phase 1–3 used conditional severity ("if the venue weights X heavily…"); 4b makes the call under the approved standard.

### 4b output

A venue-aligned list:
- Strengths (with paper citations and venue-norm citations)
- Weaknesses (with paper citations, venue-norm citations, context, consequence)
- Minor issues (trivial findings routed away from weaknesses)
- Any new gaps in the venue standard, surfaced for 4a to fix

---

## 4c — Recommendation

Propose a recommendation grounded in 4b. Use the recommendation taxonomy the venue uses (accept / weak accept / borderline / weak reject / reject; or accept / minor revision / major revision / reject for journals — whatever the venue standard from 4a specifies).

State reasoning the program committee can audit: which weaknesses drive a "no," which strengths support a "yes," and how the balance lands. The chain from 4b to recommendation must be visible.

The user decides. The LLM only pushes back if the user's choice is internally inconsistent with their 4b adjudications — that is a logic check, not a weighting disagreement. If 4b adjudicated several weaknesses as fatal but the user picks "accept," ask them to reconcile. If they confirm it is a weighting call, defer.

---

## 4d — Draft

Once 4c is settled, write the draft to `review-<short-title>.md` in the working directory.

### Structure

The draft has two layers when the venue uses a reviewer form: a **decision-support layer** (helps the user judge accept/reject) and a **form-response layer** (what gets submitted). When the venue has no form on file, only the decision-support layer and the closing sections apply.

**Decision-support layer**, always present, in this order:

1. **Summary of contribution.** Two to four sentences, neutral, drawn from Phase 1 — the kind of summary the authors would recognize as fair.
2. **Strengths.** Each a claim with paper citation and, where it sharpens the case, the venue-norm justification.
3. **Weaknesses.** Each a paragraph: what the weakness is, why it matters under the venue standard, what it implies for the paper, paper citations. No nit-picks. If a candidate weakness's substance and consequence cannot be stated, it does not appear here.
4. **Recommendation with reasoning.** From 4c. The reasoning chain auditable.

**Form-response layer**, only when the venue has a reviewer form in `references/venue-norms.md`:

5. **Reviewer form responses.** Answer each question verbatim from the venue's form, in the venue's order. Draw on the decision-support layer; do not re-derive findings already covered above. For "If applicable" questions where the paper does not engage that dimension, say so explicitly and move on. Read each question literally — questions of the form "have the authors emphasized strengths" or "have the authors stated limitations" are asking about the manuscript's *self-presentation*, not the reviewer's own assessment of strengths and limits, and should be answered at that meta level.

**Closing sections**, always:

6. **Questions for authors.** Genuine questions whose answers would change something. Not rhetorical or veiled criticisms. The one section addressed to the authors directly.
7. **Minor issues.** Typos, figure legibility, citation formatting. Brief.

### Discipline

- Address the program committee throughout, except in Questions for Authors.
- Every evaluative claim cites paper evidence.
- Severity is committed, not conditional — 4a/4b have already resolved the venue-weighting question. The one exception is findings 4b flagged as norm-silent gaps, where the draft may note conditional severity and surface the gap for the PC.
- No confidence labels.
- Plain prose with section headers. Bullets only for genuinely list-like content (questions for authors, minor issues).

### Handing over

Tell the user the file path. The review is theirs; revisions are theirs to request. Do not summarize the conversation, do not run a calibration ritual, do not ask if they want anything else. If they come back with edits, revise.
