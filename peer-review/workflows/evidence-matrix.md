# Evidence matrix

This workflow runs silently before any Phase 1 output. Its purpose is to make the later review auditable and to reduce weak or generic criticism.

## Output shape

Build a compact internal table with one row per important evaluative point. Each row should contain:

- `topic`: contribution, method, theory, system, literature, ethics, reporting, or venue fit
- `claim-or-issue`: the paper's claim or the skill's candidate evaluative point
- `paper-support`: what in the paper supports it
- `citation`: section, figure, table, or page reference
- `counter-reading`: the strongest plausible reading in the other direction
- `venue-sensitivity`: whether this matters more for research-heavy, practitioner-heavy, or methods-heavy venues
- `status`: `supported`, `underreported`, `unsupported`, `overclaimed`, or `open-question`

## How to build it

1. Extract the authors' central contribution claims from abstract, introduction, and conclusion.
2. For each claim, locate the strongest evidence the paper offers.
3. Identify the main threats, omissions, or ambiguities.
4. Mark whether each issue is:
   - `underreported`: the paper may have done the work but did not report enough detail
   - `unsupported`: the paper's conclusion is not supported by the presented evidence
   - `overclaimed`: the paper presents a stronger contribution than the evidence justifies
5. For theory or framework papers, treat conceptual architecture, engagement with prior theory, and explanatory usefulness as evidence.
6. For tools or AIED papers, include both the artifact claim and the educational-evaluation claim if both are present.

## What belongs in Phase 2

Rows marked `open-question` or rows where venue sensitivity is high are likely Phase 2 material. Rows that are clearly supported or clearly weak do not need user judgment; they should flow directly into the draft later.

## Guardrail

If a candidate criticism cannot be tied to a row with a citation and a clear counter-reading, do not foreground it.
