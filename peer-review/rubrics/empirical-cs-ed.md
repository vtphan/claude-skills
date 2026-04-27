# Rubric: empirical CS Ed studies

Use this rubric for empirical studies whose primary contribution is evidence about teaching, learning, or student behavior in a computing context. Studies range from controlled experiments to classroom interventions to observational analyses to qualitative inquiry. The rubric covers concerns that recur across this range; not every item applies to every paper.

This rubric supports the skill's reading; it is not a checklist to mechanically tick through. In Phase 1, scan the rubric to identify which items the paper engages with and where the paper might fall short. In Phase 2, the items most worth raising as questions are those where the paper's choice is defensible-or-not depending on framing.

## Research question and contribution

- Is there a clear research question, or is the paper organized around a tool / intervention without a question? Tool-first papers are legitimate but should be reviewed against `rubrics/tools-systems.md` instead or in addition.
- Does the question matter to CS Ed practitioners or researchers, and is the paper explicit about who should care?
- Is the contribution claim calibrated to the evidence? Authors sometimes overclaim ("our intervention improves learning" when they measured satisfaction) or underclaim (a strong qualitative finding presented as preliminary).

## Study design

- **Setting and population.** Single section / multi-section / multi-institution. Course level. Prior CS background of students. Selection mechanism (required course, elective, intro vs. upper-division). The skill should know which of these are described and which are missing.
- **Comparison condition, if any.** Between-subjects, within-subjects, historical comparison, no comparison. Each has known threats. Historical comparisons are common in CS Ed and often defensible — flag them as a weighting question for the user, not an automatic flaw.
- **Instructor role.** Is the instructor also a researcher / author? This is extremely common in CS Ed and not by itself disqualifying, but it interacts with measurement: were the people scoring student work blind to condition? Did the instructor know what would count as a positive result?
- **Sample size.** Calibrate skepticism to the claim. A within-subjects qualitative analysis with n=15 may be plenty; a between-subjects effect-size claim with n=23 per condition usually is not. Power for the specific claim being made matters more than absolute n.
- **Recruitment and consent.** Were students offered alternatives if they did not want to participate? IRB approval mentioned? Vulnerable-population concerns (under-18, students whose grades depend on the instructor)?

## Measurement

- **What is being measured.** Learning outcomes, performance on specific tasks, self-reported confidence, satisfaction, engagement, behavioral traces. These are not interchangeable. Claims about learning need learning measures, not satisfaction proxies. This recurs frequently in AI-in-education submissions and is worth flagging when it appears.
- **Validity of the measure.** Is the assessment instrument validated, adapted from a validated instrument, or ad hoc? Ad hoc is fine for many CS Ed studies, but the paper should describe how the instrument was developed and piloted.
- **Reliability.** For human-coded data: was inter-rater reliability reported, and is it adequate for the claim? For quantitative measures: any internal-consistency or test-retest information?
- **Blinding.** Were graders/coders blind to condition? If not, this is often a real threat in CS Ed papers, especially when the instructor is also a researcher.

## Analysis

- **Match between analysis and question.** Statistical tests appropriate to the data type and design? Qualitative analysis method (thematic, grounded, content) named and applied consistently?
- **Effect sizes alongside p-values.** Especially with small samples, p-values alone are easy to misread.
- **Multiple comparisons.** When the paper reports many tests, is correction discussed or are post-hoc tests presented as if pre-registered?
- **Qualitative analysis depth.** Were quotes selected to illustrate themes or were themes derived from systematic coding? Saturation discussed?
- **Mixed-methods integration.** If the paper claims mixed-methods, is the integration substantive or are the strands stapled together?

## Threats to validity

The paper should discuss its own threats. The skill should also identify ones the paper missed. Common threats in CS Ed:

- Novelty effects (any new intervention is more interesting than the status quo).
- Hawthorne / observation effects.
- Instructor enthusiasm confound (the new approach was taught by its inventor).
- Selection effects in opt-in studies.
- Ceiling and floor effects in assessments.
- Generalizability across institutions, populations, course levels, programming languages.
- Dosage and fidelity (was the intervention actually delivered as designed?).

## Engagement with prior work

- Are foundational CS Ed citations present where they should be? See `references/foundational-citations.md` for common ones.
- Does the paper engage with the relevant sub-literature, or only with the most recent / most fashionable adjacent work? In AI-in-education, this is a recurring concern: papers cite recent LLM work and skip the educational technology and learning sciences literature that should ground them.
- Are competing or contradictory findings in the literature acknowledged, or only supportive ones?

## Reproducibility and openness

- Materials shared (instruments, prompts, code, intervention materials)?
- Data shared, with appropriate de-identification, or rationale for not sharing?
- Enough methodological detail that a competent reader could replicate?

## Reporting and writing

- Are the limitations section's limitations the actual important ones or boilerplate?
- Are the results clearly distinguished from the discussion?
- Are tables and figures legible and necessary?
- Threats and limitations integrated thoughtfully or relegated to a perfunctory section?

## What to do with this rubric in Phase 2

For each question candidate, ask: is this a defensible-or-not depending on framing? Those are the ones that belong in Phase 2 — they need the user's judgment. Items that the paper either clearly addresses or clearly fails are not Phase 2 material; they go directly into the eventual draft as strengths or weaknesses with citations.
