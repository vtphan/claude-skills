## Round Stance

**Round 2**
- Stance: expand
- Perspective I'm adopting: instructor sketching real homework
- Substantive changes: Did NOT modify the Idea — the user's request to add "Algorithms course, coding + analytical problems" is already captured in Idea point (a). Honored the second half of the user's directive ("use this context in your proposed solutions") by expanding the Proposed Solution with three fully worked-out homework templates (one coding-construction, one analytical/runtime, one correctness/counterexample) — each showing the artifact, the student-specific element, the submission contract, the rubric weights, and how the three dials manifest concretely. Tightened the dial-to-learning-outcome mapping in the Rationale.
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

Additional grounding (added by user before round 1):

- **(a) Course context: Algorithms.** Students must construct algorithms in code and perform running-time analysis. Deliverables include working programs, asymptotic analyses, and (where relevant) correctness arguments.
- **(b) Productive struggle benefits learning; "productive resistance" operationalizes productive struggle.** Productive struggle is the recognized learning principle; productive resistance is the design lever — the deliberate friction introduced into the assignment to keep students struggling productively rather than escaping the struggle by outsourcing.
- **(c) This instructional design introduces productive resistance** as its central mechanism.
- **(d) There is an interplay between extraneous load and germane load** at work in the design. The four design moves manipulate this balance.
- **(e) Scaffolding can place students in a sufficiently comfortable Zone of Proximal Development (ZPD) such that germane load is *less than* the extraneous load incurred by outsourcing** (e.g., the load of transcribing a problem under a no-copy-paste regime). Under that condition, the path of least resistance becomes the *germane* path — i.e., doing the learning work — because it is now genuinely cheaper than the outsourcing path.

## Proposed Solution

The design is a **load calculus** for assignments: deliberately tune three dials so that, for a typical student in the ZPD, doing the germane work is cheaper than outsourcing.

```
   germane_load(problem | scaffolding)         <
   extraneous_load(outsourcing path | resistance)
```

**The three dials**

- **Scaffolding dial** — lowers germane load to a tractable level (without trivializing the problem). Worked examples, partial code skeletons, lecture-aligned decomposition, peer discussion structures, and timely feedback.
- **Resistance dial** — raises the extraneous load of *the outsourcing path specifically*. Multimodal artifacts, no-copy-paste environment, contextual references the student must add, custom-generated inputs, student-specific seeds.
- **Verification dial** — converts any AI output that does sneak through into further germane work, by making the deliverable include critique, justification, or empirical validation.

The rest of this section makes the dials concrete via three worked homework templates. Each is a real assignment shape an instructor could deploy.

---

### Template 1 — Coding-construction homework: "Modify Dijkstra's"

**Learning goal.** Students extend a known algorithm to a non-canonical setting and produce both code and an asymptotic argument.

**Problem artifact.** A printed (or PDF-image) worksheet shows a graph **G_s** drawn by hand, where `s` is the student's ID. Edges are annotated with weights *and* a small icon indicating direction-conditional cost (e.g., a one-way symbol means the weight applies only one direction). Below the graph, in prose: *"Modify Dijkstra's algorithm to compute shortest paths from node A in graphs of this kind. Implement, test, and analyze."*

- The graph is rendered as a non-OCR-friendly raster image.
- Each student receives a different `G_s` generated from their seed; the seed is printed at the top of the sheet.
- The "direction-conditional cost" twist is intentionally non-standard, so canonical Dijkstra explanations from any source will not apply directly.

**Submission contract.**
1. Code: the student's modified algorithm, written in the locked editor.
2. A 5-line trace of the algorithm running on **G_s** (the student's specific graph), captured in a notebook cell that re-renders **G_s** from the seed.
3. Asymptotic analysis with explicit reasoning about the modification's contribution to runtime.
4. AI-use disclosure: prompts used, AI responses received, and the student's annotated critique of those responses (what was correct, what was wrong, what they had to fix).
5. A 3-sentence reflective note on which subtask was hardest and why.

**Rubric weights.** Code correctness 30% / specific-trace correctness on **G_s** 20% / asymptotic analysis quality 20% / AI critique quality 20% / reflective note 10%. *Note that the AI critique is weighted equal to the trace and the analysis.* A student who pastes AI output and writes "looks good" can score at most 70%, even if the AI was right.

**Dial settings.**
- *Scaffolding* (medium): lecture-aligned decomposition is provided ("you will need to decide how to handle direction conditions when relaxing edges"). A partial code skeleton with priority-queue boilerplate is given. The hard germane work — the modification logic — is what the student must produce.
- *Resistance* (high): multimodal artifact, student-specific seed, locked editor with paste disabled from outside, OCR-resistant graph image.
- *Verification* (high): trace must run on **G_s**; rubric forces critique of any AI output.

---

### Template 2 — Analytical / runtime homework: "Compose and Reconcile"

**Learning goal.** Students analyze the running time of a composed algorithm where the inner call's cost depends on the outer call's state, and reconcile theoretical analysis with empirical measurement.

**Problem artifact.** A two-page handout. Page 1 shows pseudocode for two algorithms, **F** and **H**, where **F** invokes **H** inside a loop whose iteration count depends on the *output size* of **H**, not the input size. Page 2 shows three small example traces (drawn by hand on grid paper, photographed) and asks: *"Derive the asymptotic running time of **F** in terms of n. Implement **F** and **H** in your editor; for n ∈ {your assigned values}, measure runtime and produce a log-log plot. Reconcile theory with observation."*

- The student's "assigned values" of n come from a per-student seed.
- The hand-drawn traces are deliberately included to anchor reasoning and to make the artifact non-pasteable.

**Submission contract.**
1. Asymptotic derivation: written-out reasoning, not just a Big-O answer. Recurrence (if applicable). Explicit identification of what dominates.
2. Working code for **F** and **H** in the locked editor.
3. A log-log plot generated from runs on the student's assigned n values.
4. A "reconciliation paragraph": where do theory and measurement agree, where do they diverge, and what explains the divergence (constant factors, cache effects, lower-order terms still dominating)?
5. AI-use disclosure as in Template 1.

**Rubric weights.** Derivation rigor 30% / code correctness 15% / plot quality 15% / reconciliation paragraph 30% / AI critique 10%.

**Dial settings.**
- *Scaffolding* (high on derivation, lower on coding): a worked example of a similar composed algorithm (with derivation) is included in the lecture notes; a recurrence cookbook is provided. Code is unscaffolded.
- *Resistance* (medium): hand-drawn traces and per-student n values raise outsourcing cost. The pseudocode itself *is* paste-friendly, by design — the friction is on the inputs and outputs.
- *Verification* (high): the reconciliation paragraph is the largest single rubric item. AI cannot produce this without the student's specific empirical data, and an AI's invented data can be detected by re-running the student's code.

---

### Template 3 — Correctness / counterexample homework: "Greedy Verdict"

**Learning goal.** Students evaluate whether a proposed greedy algorithm is correct on a specified problem, producing either a correctness argument or a concrete counterexample.

**Problem artifact.** Three short scenarios are presented, each as a one-paragraph problem statement plus a proposed greedy strategy. (E.g., interval scheduling variant; coin-change variant; minimum-spanning-tree variant.) For two of the three, the greedy is correct; for one, it fails. Which is which is *not* disclosed. Each student gets a permutation of the three with seed-specific parameter values.

**Submission contract.** For each of the three:
1. The student's verdict: correct, or fails on input X.
2. If correct: an argument (exchange argument, cut argument, or a reduction to a known result), at the level of a homework proof — not a full formal proof.
3. If incorrect: the counterexample input, and a trace showing the greedy's output and the optimal output side-by-side.
4. Required AI-use exhibit: students must produce at least one AI verdict per scenario, paste it into the disclosure, and explicitly agree, disagree, or partially disagree with the AI — citing evidence.

**Rubric weights.** Verdicts 15% (5% × 3) / arguments-or-counterexamples 45% (15% × 3) / AI agreement-with-evidence 30% (10% × 3) / writing clarity 10%.

**Dial settings.**
- *Scaffolding* (high): the structure of each verdict deliverable is fully prescribed; lecture covered exchange arguments and cut arguments the prior week.
- *Resistance* (low): this assignment deliberately *invites* AI use. The scenarios paste cleanly. The friction is not at input.
- *Verification* (very high): AI is known to produce confident-and-wrong verdicts on greedy correctness, especially on parameter-shifted variants. The required "AI agreement-with-evidence" exhibit forces students to interrogate the AI rather than echo it. *This is the template most leveraged on the verification dial.*

---

### Cross-cutting infrastructure

- **Locked editor / submission environment.** A browser-based notebook (e.g., a JupyterLite or VSCode-Web instance) configured to:
  - Disable external paste; allow within-document paste.
  - Log keystroke timing and edit-history snapshots, attached to the submission as a non-graded artifact (for diagnostic and integrity review).
  - Render student-specific inputs from a seed at the top of the assignment.
  - Optionally embed an "AI scratchpad" panel that wraps an AI API and logs every prompt/response — opt-in per assignment.
- **Per-student seeds.** A simple `seed = hash(student_id, assignment_id)` scheme is enough to make graphs, n-values, and parameter choices unique.
- **Assignment metadata for the gradebook.** Each problem records its dial settings (scaffolding/resistance/verification level) so the instructor can see, across a semester, which mix actually correlates with learning gains and which doesn't.

## Rationale

The user's round-2 directive — make the proposed solutions Algorithms-concrete — is the main shaping force this round. The three templates are the response.

**Why three, and why these three?** They span the deliverable types named in Idea (a):
- Coding (Template 1)
- Analytical / runtime (Template 2)
- Correctness/proof (Template 3)

They also span the dial settings in interesting ways:
- Template 1 cranks all three dials high — the "default" assignment shape.
- Template 2 trades resistance for scaffolding-on-derivation — useful when the germane work is heavy and the artifact must be partly paste-friendly.
- Template 3 deliberately *lowers* the resistance dial and leans almost entirely on the verification dial — useful as a once-or-twice-per-semester move where the goal is for students to learn to evaluate AI output directly.

That last point is the strongest argument for the dial framework: it gives the instructor a vocabulary for *why* a given assignment looks the way it does, and lets different assignments serve different sub-goals without abandoning the underlying load calculus.

**Mapping to Consider This items from round 1:**

- *Failure case (carried from round 0):* The templates lean on per-student seeds, edit-history logs, and weighted critique deliverables to make the "good grades, no learning" failure mode detectable. Edit-history logs are particularly load-bearing here — they let the instructor see the trajectory, not just the artifact.
- *Scaffolding diagnostics:* Template-level visibility (per-student edit history + reflective note) is the proposed instrument. Open question: is this enough, or does it need a separate per-week formative check?
- *Falsifiability:* Not yet pinned down at the design level. Worth raising again — see Consider This below.
- *AI-allowed spectrum:* The three templates implicitly stake out a position: AI is *permitted and disclosed*. Template 3 explicitly *requires* AI use. Templates 1 and 2 permit it but force critique. None of them forbid AI. This is closer to the "AI required as a tool the student must learn to evaluate" pole than "AI strictly forbidden."

**Assumptions still worth challenging in later rounds:**

- That instructors can build/maintain the locked editor + per-student seed infrastructure. This is a non-trivial software project; without it, the resistance dial collapses.
- That the rubric weights will hold up against grade-grubbing pressure. A 30% rubric line for "AI agreement-with-evidence" will be contested by some students who want a binary right/wrong. Defensible rubric language matters.
- That edit-history logs do not run afoul of student privacy norms or institutional policy. Worth a `[Q from LLM]` next round if the user wants to push this design toward implementation.

## Consider This

- `[from user, round 0]` (carried) `[Q from LLM]` What's the failure case you're most worried about? "Students get good grades but learn nothing" and "Students get penalized for using AI well" are both real risks, and a design that minimizes one can worsen the other.
- `[Q from LLM]` (carried, partly addressed) Diagnostics: edit-history logs + reflective notes are the current instruments. Is that enough to detect when scaffolding has failed and germane load has exceeded a student's ZPD? Or do you want a separate formative check (weekly muddy-point survey, mid-assignment hint-request mechanism, etc.)?
- `[Q from LLM]` (carried) Falsifiability: what observation would convince you the design *isn't* working? E.g., "students complete assignments at the same rate but exam performance drops," "transparency statements show 80% pure transcription with no critique," etc.
- `[Q from LLM]` (carried, partly addressed) Position on the AI-allowed spectrum: the templates as drafted permit-and-disclose, with Template 3 explicitly requiring AI use. Is that the right stance, or would you prefer some templates that forbid AI for foundational topics (e.g., a first-week assignment on basic recursion analysis)?
- `[Q from LLM]` (new) Implementation cost: the locked editor + per-student seeds + edit-history logs is a real engineering project. Is the goal to design assignments first and treat tooling as future work, or do you want the design to stay strictly within tools that already exist (e.g., a standard LMS + Jupyter)? This bounds what's actually deployable next semester.
- `[Q from LLM]` (new) Privacy / surveillance norms: edit-history logging crosses a real line. Some students and institutions will object. Should the design assume opt-in logging, mandatory logging, or seed-only authentication (no keystroke capture)?

## Perspective I'm Contributing From

_(user fills in next round)_

## Notes

- The three-template structure is now the load-bearing artifact of the Proposed Solution. A future critique round should pressure-test it on at least two axes: (i) does Template 3 actually work — i.e., are AI verdicts on textbook-adjacent greedy problems still confidently wrong as of the model generation students will use, or is that assumption decaying? (ii) does the per-student seed scheme survive against students sharing seeds and pooling AI prompts?
- The dial framework has now been used to justify three different concrete assignments with different dial settings. That's the first piece of evidence it predicts design choices rather than just describing them post-hoc. Worth keeping an eye on whether it continues to do work in subsequent rounds.
