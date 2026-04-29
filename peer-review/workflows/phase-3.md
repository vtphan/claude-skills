# Phase 3 — Evidence and claim verification

Medium depth, citation-heavy. Loaded when Phase 3 begins along with one or two rubrics from `rubrics/` matching the Phase 1 classification.

Phase 3 consumes the claims list confirmed at the end of Phase 1 and renders, for each claim, whether the paper's evidence supports it. Output is per-claim verdicts with citations — not strengths, not weaknesses, not revision suggestions. Strength/weakness comes in Phase 4b; revisions come in Phase 4d.

## Loading rubrics

Phase 1 named the classification and which rubric(s) apply. Load them now. Rubrics shape which threats to validity matter for this paper type; they are not checklists to walk mechanically.

For mixed papers, load both rubrics (e.g., `tools-systems.md` and `empirical-cs-ed.md` for a tool with a classroom evaluation). Apply each to the claims it bears on.

## Pacing

Driven by the number of claims:

- 1–4 claims: one turn.
- 5–8 claims: two turns, batched (first half, then second half).
- More than 8: rare; ask the user if the claims list should be tightened before walking it.

## Per-claim verdict

Walk the claims list in the order Phase 1 confirmed. For each claim, produce:

1. **The evidence offered.** Where in the paper does the work back this claim? Cite section, figure, table, or page.
2. **The strongest threat.** What most undermines the inference from evidence to claim — drawn from the rubric's emphases for this paper type or from the paper itself. Methodological soundness, measurement validity, sample, comparison condition, blinding, analysis match, generalizability, construct validity for traces, and so on.
3. **The verdict.** One of:
   - **Supported** — the evidence backs the claim adequately.
   - **Underreported** — the work may support the claim but the paper does not report enough detail to confirm. Fix is more reporting.
   - **Unsupported** — the evidence presented does not back the claim. Fix is either more evidence or dropping the claim.
   - **Overclaimed** — the evidence supports a weaker claim than what is stated. Fix is softening the claim.

The distinction between *unsupported* and *overclaimed* matters: they imply different revisions. Be precise.

4. **Venue-weighting flag, if any.** If the verdict depends on a methodological convention where reasonable methodologists disagree (e.g., n=23 is sufficient or not depending on venue standards; single-instructor design is fatal or acceptable depending on paper type), mark it for Phase 4. Do not resolve in Phase 3.

## Cross-claim findings

Some methodological issues affect multiple claims at once — an analysis-pipeline problem touches every empirical claim it produces; a measurement-validity issue touches every claim built on that measure. After the per-claim walk, surface cross-claim findings as a short list. Each cites the paper and names which claims it touches.

## Closing questions

Surface 1–3 questions where the user's judgment is needed. For Phase 3, these typically fall in two buckets:

- **Methodological convention.** Where reasonable methodologists land in different places and the user reads the sub-area better than the LLM (e.g., "is this analysis approach standard for [sub-field]?").
- **Severity of underreported vs. unsupported.** Where the LLM is uncertain whether a claim is fixable with more reporting or has a deeper problem.

Format per question: the question with paper citations, the LLM's tentative read and counter-reading, what would shift the view.

## Off-ramp

After the closing questions, offer:

> Ready to move to Phase 4 (synthesis and draft), or stop here?

Phase 4 is the only remaining phase, so skipping is not a meaningful option.

## What this phase outputs to working state

- Per-claim verdicts: each Phase 1 claim paired with evidence citation, strongest threat, and verdict (supported / underreported / unsupported / overclaimed).
- Cross-claim methodological findings, citation-grounded.
- Venue-weighting flags, marked for Phase 4 to resolve.
- Open Phase 3 questions, tagged pivotal or shaping.
