# Rubric: tools and systems papers

Use this rubric when the paper's main contribution is a tool, system, platform, workflow, or infrastructure artifact. Many papers in this category also include an empirical evaluation; if so, pair this rubric with an empirical or AI-in-education rubric.

Use rubric themes lightly in Phases 1–2 if helpful for classification, literature-positioning, or question selection. Apply the rubric in full in Phase 3.

## Problem and user need

- Is the educational or research problem concrete and worth solving?
- Is the intended user clear: students, instructors, researchers, administrators, or platform builders?
- Does the paper explain why existing tools or workflows are insufficient?

## System contribution

- What is actually new here: architecture, interaction design, orchestration, evaluation workflow, data pipeline, or integration?
- Is the technical contribution substantive, or is it mostly a thin wrapper around existing components?
- Are the system boundaries and assumptions clear?

## Design rationale

- Are major design decisions motivated by user needs, theory, prior work, or deployment constraints?
- Are alternatives acknowledged, or does the paper present the chosen design as self-evident?
- If the system uses AI or LLMs, is the AI doing meaningful work rather than cosmetic automation?

## Evaluation

- Is the evaluation matched to the claim: usability, deployment feasibility, learning impact, instructor efficiency, robustness, or adoption?
- If the paper claims learning benefit, does it measure learning rather than satisfaction alone?
- If the paper claims workflow improvement, are baseline workflows or comparison conditions clear?

## Reliability, robustness, and failure modes

- Does the paper discuss known failure modes, breakdown cases, and limits?
- For AI systems, are hallucination, over-reliance, privacy, equity, and academic-integrity issues addressed where relevant?
- Is the system stable enough that the reported experience is meaningful rather than anecdotal debugging?

## Reproducibility and transfer

- Could another group reproduce or adapt the system from the description?
- Are prompts, interfaces, schemas, or code shared when possible?
- Does the paper give enough detail about deployment context for readers to judge transferability?

## Common review pivots

Questions often worth escalating to Phase 2:

- Is the artifact contribution itself enough for this venue, or is the evaluation too thin?
- Is the paper really a systems contribution, or primarily an experience report with a tool attached?
- Does the educational evaluation support the strength of the system claims?
