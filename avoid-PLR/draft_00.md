## Round Stance

**Round 0**
- Stance: expand
- Perspective I'm adopting: collaborative ideator with a learning-design lens
- Substantive changes: Seeded the Idea from the free-text invocation. Drafted an initial Proposed Solution that distinguishes two strategy families ("input-side friction" vs. "output-side verification") that the four ideas implicitly mix. Surfaced three `[Q from LLM]` items in Consider This about goal (assessment vs. instruction), discipline scope, and what "effectiveness" is being measured against.
- Recommendation: continue

## Idea

Design homework / coursework assignments under the working assumption that students *will* use AI. Two premises drive the design:

1. **Path of least resistance.** Students outsource to AI whenever solving the problem themselves carries more cognitive load than handing it off. So the assignment must make outsourcing at least as effortful as engaging.
2. **Critical thinking equals effective learning.** Whether students arrive at the solution by *solving* the problem or by carefully *framing* it for an AI, both routes produce learning — as long as the route requires real thought.

Four candidate design moves:

1. Make the act of describing the problem to an AI itself cognitively demanding. Then students either solve it themselves or have to reframe it to outsource — either way, they think.
2. Use lengthy, multimodal problems (text + images + diagrams) that resist easy transcription.
3. Build an assignment environment where copy-paste is disabled, so any handoff to AI requires transcription or reformulation.
4. Design problems where a naive paste-and-prompt yields AI output that the student must still interpret, debug, or evaluate — pushing the cognitive work to the back end.

The goal is to design assignments where, even in an AI-saturated environment, the student cannot escape doing the kind of thinking that constitutes the learning.

## Proposed Solution

Treat the four ideas as instances of two distinct strategies, then design assignments that combine them deliberately.

**Strategy A — Input-side friction (Ideas 1, 2, 3).**
Raise the cost of outsourcing by making the *transfer* of the problem to an AI hard. Concretely:
- Problems are presented as multimodal artifacts: hand-drawn diagrams, annotated screenshots, photos of physical setups, audio clips, or scanned pages with marginalia. The "problem statement" is not a prose paragraph that pastes cleanly into a chat box.
- Problems embed context that only makes sense relative to in-class discussion, a lab dataset the student generated themselves, or a peer's earlier submission. The artifact is necessary but not sufficient — the student must add context to ask the AI anything coherent.
- The submission environment (a custom web app, a locked-down notebook, an iPad PDF, or a paper packet) makes copy-paste either impossible or low-fidelity (e.g., images are rasterized; equations are rendered, not LaTeX).

**Strategy B — Output-side verification (Idea 4).**
Lower the bar to *getting* an AI answer, but design the problem so the AI answer is *not the deliverable*. The deliverable is the student's evaluation of it. Concretely:
- Submissions require: (a) the prompt the student used, (b) the AI's raw response, (c) the student's annotated critique — what is correct, what is wrong, what is incomplete, and what evidence supports each judgment.
- Problems are tuned to provoke confident-but-wrong AI output: edge cases, recently-changed facts, domain conventions the AI gets subtly wrong, or problems where multiple valid answers exist and the AI commits prematurely.
- Grading rubrics weight the *critique* heavily and the *answer* lightly. A student who pastes the AI output verbatim and writes "looks correct" fails even if the answer was right.

**Combine the two strategies in a single assignment.** A typical homework looks like:
- Multimodal problem artifact (Strategy A)
- Required deliverable: prompt + AI response + critique + corrected solution (Strategy B)
- Optional: a short reflection on which parts the student outsourced and why

This combination forecloses both shortcuts: pure outsourcing is blocked at the input by friction, and pure transcription is blocked at the output by the critique requirement.

## Rationale

The user's two premises give an interesting design constraint: rather than fighting AI use, the design *expects* AI use and channels it toward thinking-producing forms.

Splitting the four ideas into two strategy families clarifies what each move is buying:
- Ideas 1–3 all manipulate the cost of *handing off* the problem. They are variations on the same lever.
- Idea 4 is fundamentally different: it manipulates what counts as a finished deliverable. It is more robust because it does not depend on the AI being weak at transcription — only on the AI being imperfect at the problem.

Combining the two strategies hedges against each other's failure modes:
- Strategy A alone is brittle. AI multimodal capability is improving; what's friction today (a hand-drawn diagram) may be paste-able tomorrow. Friction-only designs decay with model capability.
- Strategy B alone risks becoming a critique-the-AI exercise where students never actually learn the underlying material. The multimodal/contextual problem in Strategy A keeps the substance front and center.

The "submit the prompt + response + critique" deliverable also has a side benefit for the *instructor*: it surfaces what students struggle to articulate, which is itself a diagnostic signal about understanding.

Assumptions I'm making (worth challenging):
- Students have roughly equal access to AI tools. If not, friction designs may disadvantage students who *would* engage thoughtfully but are slowed by transcription burden.
- The instructor can grade the critique reliably. This is more labor-intensive than grading a final answer.
- "Outsourcing to AI" is roughly binary. In practice it's a spectrum (autocomplete → drafted paragraph → full solution), and the design should probably address that spectrum.

## Consider This

- `[Q from LLM]` The Idea says "test the effectiveness of instruction." Two readings: (a) design assignments that *produce* effective learning (instructional design), or (b) design assignments that *measure* whether instruction was effective (assessment design). The Proposed Solution above leans toward (a). Which do you mean — or both?
- `[Q from LLM]` Is there a target discipline or course level? AI-resistance design looks very different in introductory programming, in upper-division proofs, in a lab science, and in a writing-intensive humanities course. The Strategy A/B framing generalizes, but specific tactics will differ a lot.
- `[Q from LLM]` What's the failure case you're most worried about? "Students get good grades but learn nothing" and "Students get penalized for using AI well" are both real risks, and a design that minimizes one can worsen the other.

## Perspective I'm Contributing From

_(user fills in next round)_

## Notes

The framing "AI use is assumed; design for it" is the most generative move in the original prompt. A lot of current academic-integrity discourse is trying to *prevent* AI use, which is a losing battle and also misaligned with the second premise (thinking is the goal, not abstinence). This skill's draft trajectory should probably keep that framing load-bearing.
