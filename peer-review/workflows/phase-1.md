# Phase 1 -- Paper Assessment

The deepest phase. Loaded when Phase 1 begins. Phase 1 is a brainstorming conversation: the LLM leads with informed, citation-grounded suggestions; the user asks questions, challenges interpretations, and calibrates significance. Expect two or three turns for a full paper.

Phase 1 produces paper-level findings, not final venue-relative strengths, weaknesses, or recommendations. It explores the seven review questions:

1. What do the authors propose to do, in what context, and with what rationale?
2. What is the core conceptual idea, mechanism, construct, or argument, and why is it intellectually interesting, if it is?
3. What is the impact or contribution to the field, and is it novel?
4. What do the authors claim, and are those claims substantiated by the paper's evidence and by appropriate literature support?
5. What are the gaps, flaws, and weaknesses?
6. Is the work sound and coherent enough to be a plausible scholarly contribution before applying the venue lens?
7. What venue-specific questions will Phase 2 need to answer?

## Reading the paper

Read end to end before producing output. If only metadata is available (title or abstract pasted), say so and ask for the full paper -- Phase 1 cannot proceed from an abstract.

## Loading rubrics and references

First classify the paper, then load one or two matching rubrics from `rubrics/`:

- `empirical-cs-ed.md`
- `tools-systems.md`
- `ai-in-education.md`
- `theoretical-framework.md`
- `position-argument.md`
- `replication.md`
- `learning-analytics.md`

For mixed or unclear papers, load the two closest-fit rubrics and announce the pairing. Common pairings include tools/systems + empirical CS Ed, tools/systems + AI-in-education, AI-in-education + empirical CS Ed, learning analytics + empirical CS Ed, or theoretical/framework + position/argument.

For experience reports, load `empirical-cs-ed.md` and use its **Experience report mode** section rather than looking for a separate experience-report rubric file.

Use `references/literature-grounding-checks.md` and `references/literature-red-flags.md` when assessing conceptual interest, novelty, impact, and literature positioning.

Rubrics shape which threats to validity matter for this paper type; they are not checklists to walk mechanically.

## Brainstorming clusters

Phase 1 proceeds by clusters of related questions, not one question at a time and not as a single monolithic assessment. The user may interrupt any cluster with questions. Treat those questions as the point of the phase, not as derailments.

### Cluster 1 -- Understanding and conceptual framing

Addresses questions 1-3 and uses sections 1-3 below:

- What the authors propose, in what context, and with what rationale.
- The core conceptual idea, mechanism, construct, or argument.
- Conceptual interest, impact, contribution, novelty, and initial literature positioning.

Also classify the paper and load the relevant rubric(s). End by inviting the user to ask questions or challenge the framing.

### Cluster 2 -- Claims, support, and weaknesses

Addresses questions 4-5 and uses sections 4-6 below. This cluster may span two turns for a full paper: first confirm the claims list, then walk the confirmed claims through evidence, literature support, threats, and verdicts.

- Draft and confirm the authors' central claims.
- Assess each claim against paper evidence and literature support.
- Surface gaps, flaws, weaknesses-as-findings, and cross-claim issues.

The claims-list confirmation controls the claim/evidence/literature-support assessment, but do not require ritual approval if the user is clearly ready to continue. End by asking what the user wants to probe or recalibrate before moving to soundness and venue prep.

### Cluster 3 -- Soundness and venue preparation

Addresses questions 6-7 and uses sections 7-8 below:

- Give the preliminary soundness/coherence read.
- Preview which venue-specific questions Phase 2 will need to answer.
- Surface closing questions and offer the off-ramp.

### Fast path

If the user explicitly asks for a fast review, compress the three clusters into one response, but preserve the cluster headings so the reasoning stays auditable.

Fast path compresses the pacing, not the analysis. Still produce the claim/evidence/literature-support verdicts, gaps/flaws, soundness/coherence read, venue-question preview, and closing questions.

## 1. Paper-type classification

One short paragraph. Name the type and the rubric(s) used: empirical CS Ed, experience report, tools/systems, AI-in-education intervention, theoretical/framework, position/argument, replication, learning analytics, or mixed/unclear with explanation. For mixed or unclear papers, name the two closest-fit rubrics. Announce so the user can correct.

## 2. What the authors propose and did

A neutral description the authors would recognize as accurate, even if they disagreed with later evaluation. Cover:

- The research question, objective, design problem, or thesis.
- The rationale: why the authors say the work is needed.
- The method, intervention, system, dataset, analysis, or argument as executed.
- The setting: population, course context, scale, instructor role, duration, platform, or corpus as relevant.
- What was actually done, not only what was planned or promised.

Cite section numbers throughout. Do not paraphrase the abstract; use the body of the paper as ground truth. Never invent paper-internal citations. If a section, page, table, or figure cannot be found, say so and either cite a reachable location or omit the claim.

For theoretical or argumentative papers, describe the argument's structure and moves rather than empirical execution.

## 3. Conceptual interest, impact, and novelty

Assess the work's conceptual interest and field contribution before deciding whether the evidence supports it. Keep conceptual interest distinct from impact and novelty.

Cover:

- **Conceptual idea.** What is the paper's central construct, mechanism, theoretical move, design principle, explanatory account, or argument? This is about the idea's intellectual shape, not about venue fit, scale, or practical importance.
- **Conceptual interest.** Why would that idea be worth thinking with if the claims hold? Does it clarify a confusing construct, reveal a mechanism, connect traditions, challenge an assumption, provide a useful lens, or make a design/evaluation problem newly tractable? If it is not conceptually interesting, say why plainly.
- **Impact and audience.** Who should care -- practitioners, researchers, tool-builders, policymakers, or a specific sub-community -- and what might change if the work is sound.
- **Contribution and novelty.** What appears new: context, method, system, theory, dataset, empirical finding, synthesis, or application. Also note if novelty is doubtful, narrower than the authors claim, or dependent on missing literature.
- **Literature positioning.** Whether the paper engages the intellectual ancestors, adjacent traditions, and competing work needed to make the contribution credible.

Do not bluff citations. If the LLM is uncertain whether a tradition or finding is active in the sub-field, ask the user.

## 4. What the authors claim

A numbered list. Each claim:

- Phrased as the authors phrase it, not as the LLM's interpretation.
- Cited, typically from the abstract, introduction, contribution paragraph, results, discussion, or conclusion.
- Categorized informally: objective/rationale, contribution, empirical, theoretical, normative, system, generalizability, or implication.

Aim for 3-8 claims. Flag any claim that appears in the abstract or conclusion but is not supported in the body -- that is itself a finding to test.

Ask the user to confirm or edit the list before doing detailed claim/evidence/literature-support verdicts, unless the user explicitly asks to proceed without stopping.

## 5. Claim, evidence, and literature-support verdicts

Walk the confirmed claims list in order. For each claim, produce:

1. **Evidence offered.** Where in the paper does the work back this claim? Cite section, figure, table, or page.
2. **Literature support.** What prior work does the paper use to ground this claim? Does the literature support the claim, merely motivate it, contradict it, or leave it under-grounded? Name missing adjacent or foundational literature only when it materially affects the claim's credibility, novelty, or framing. Do not invent citations.
3. **Strongest threat.** What most undermines the inference from evidence and literature support to claim, drawing from the relevant rubric(s): methodological soundness, measurement validity, sample, comparison condition, analysis match, construct validity, generalizability, literature grounding, system robustness, or argument coherence.
4. **Verdict.** One of:
   - **Supported** -- the evidence backs the claim adequately.
   - **Underreported** -- the work may support the claim but the paper does not report enough detail to confirm. Fix is more reporting.
   - **Unsupported** -- the evidence presented does not back the claim. Fix is either more evidence or dropping the claim.
   - **Overclaimed** -- the evidence supports a weaker claim than what is stated. Fix is softening the claim.
5. **Venue-sensitive flag, if any.** If the verdict itself is clear, state it. If the severity or interpretation reasonably depends on venue standards or sub-field convention, carry that dependency to Phase 2.

The distinction between unsupported and overclaimed matters: they imply different revisions.

## 6. Gaps, flaws, and weaknesses-as-findings

Synthesize findings across claims. These are not yet final weaknesses for the review; Phase 2 decides what matters under the venue standard.

Consider:

- Conceptual coherence: constructs distinct, argument internally consistent, work-as-described actually instantiates the claimed contribution.
- Impact and novelty: contribution meaningful or incremental, novelty credible or overstated.
- Literature grounding: foundational work, adjacent traditions, and competing findings.
- Methodology and evidence: design, measures, analysis, comparison, sampling, reliability, limitations, and overclaiming.
- Reporting and reproducibility: enough detail to evaluate, replicate, or adapt.
- Ethics and deployment risks where relevant: privacy, consent, bias, surveillance, hallucination, academic integrity, over-reliance.

Surface cross-claim findings separately when one issue affects several claims.

## 7. Preliminary soundness/coherence read

Give a provisional, venue-independent read of whether the work is coherent and substantiated enough to be a plausible scholarly contribution. This is not a publishability recommendation and should not replace Phase 2's venue judgment. Frame it as:

- **Sound as framed**, if the contribution, argument, evidence, and literature grounding are coherent. Example: the paper claims a bounded design insight and provides enough method, context, and evidence to support that bounded claim.
- **Sound only with reframing**, if the work is useful but the claims are too strong or the contribution is mispositioned. Example: learning-gain claims are too strong, but the work would be coherent as an experience report or feasibility study.
- **Not yet sound without substantial new work**, if the evidence or argument does not support the central contribution. Example: the central claim requires outcome evidence, but the paper reports only satisfaction or anecdotal use.
- **Not coherent as scholarly work**, if there is no clear contribution, evidence base, or argument. Example: the paper describes an activity or tool but does not articulate a research, design, theoretical, or practice contribution.

Name the one uncertainty most likely to change this read.

## 8. Venue-question preview

Preview what Phase 2 will need to answer for the named venue. If the venue has a stored reviewer form, name the form sections most likely to matter. For Computers and Education Open, preview objectives/rationale, replicability/reproducibility, statistical reporting if applicable, tables/figures, support for conclusions, stated strengths, stated limitations, structure/flow/writing, and language editing.

## Closing questions

Surface 1-3 questions where the user's judgment is needed. Tag each as **recommendation-pivotal** or **shaping**.

Format per question:

- The question, with paper citations.
- The LLM's tentative read and the strongest counter-reading.
- What answer or evidence would shift the LLM's view.

Default to the smallest useful set. If two questions resolve most of the uncertainty, ask two.

## Off-ramp

After the closing questions, offer:

> Ready for Phase 2 (venue judgment and draft), draft now with these unresolved questions noted, or stop here?

If the user stops, end the session without a draft. If they ask to draft immediately, continue to Phase 2 and note which Phase 1 questions remain unresolved.

## What this phase outputs to working state

- Paper classification and rubric(s) used.
- What the authors propose/did, context, and rationale.
- Intellectual-move, conceptual-interest, impact, novelty, and literature-positioning findings.
- Confirmed claims list and per-claim evidence/literature-support verdicts.
- Gaps, flaws, weaknesses-as-findings, and cross-claim findings.
- Preliminary soundness/coherence read and the uncertainty most likely to shift it.
- Venue-question preview.
- Venue-sensitive flags attached to the findings they qualify.
- Open Phase 1 questions, tagged pivotal or shaping.
