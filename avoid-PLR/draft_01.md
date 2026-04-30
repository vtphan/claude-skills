## Round Stance

**Round 1**
- Stance: restructure + expand
- Perspective I'm adopting: cognitive-load-theory-informed instructional designer
- Substantive changes: Reorganized the Proposed Solution around the user's new theoretical scaffolding — Cognitive Load Theory (extraneous vs. germane load), Vygotsky's ZPD, and "productive resistance" as the operationalized form of productive struggle. Specialized the Solution to the Algorithms course context (coding, runtime analysis, proofs/correctness, traces). Replaced the prior generic "Strategy A/B" framing with a load-calculus framing: productive resistance raises the *extraneous* load of *outsourcing only*, leaving germane load as the cheaper path *given adequate scaffolding*. Resolved two of my prior `[Q from LLM]` items (discipline, instruction-vs-assessment) using the user's additions; carried forward the failure-case question. Added new `[Q from LLM]` items about scaffolding diagnostics and what evidence would falsify the design.
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

The design is a **load-calculus** for assignments: deliberately tune three quantities so that *for a typical student in the ZPD*, doing the germane work is cheaper than outsourcing.

```
   germane_load(problem | scaffolding)         <
   extraneous_load(outsourcing path | resistance)
```

Three design dials:

- **Scaffolding dial** — lowers germane load to a tractable level (without trivializing the problem). Worked examples, partial code skeletons, lecture-aligned problem decomposition, peer discussion structures, and timely feedback.
- **Resistance dial** — raises the extraneous load of *the outsourcing path specifically*. Multimodal artifacts, no-copy-paste environment, contextual references the student must add, custom-generated inputs.
- **Verification dial** — converts any AI output that does sneak through into further germane work, by making the deliverable include critique, justification, or empirical validation. (This is the user's design move #4.)

For Algorithms specifically, the dials translate into concrete tactics:

**A. Algorithm-construction problems (germane = synthesizing an algorithm)**

- Problems are presented as a multimodal artifact: a hand-drawn input graph, a screenshot of a real-world dataset's structure, a video of an algorithm running on a small instance, or a printed worksheet that students photograph.
- Inputs are *student-specific*: each student gets a distinct seed graph or array (generated per student), so no two students can share an AI prompt and outputs cannot be cached across the class.
- Submission requires both code *and* a hand-traced execution on the student's specific input — the trace is what the student annotates, not just the answer.

**B. Running-time analysis problems (germane = constructing the analysis)**

- Pose runtime questions on *composed* algorithms (e.g., "you call algorithm X inside a loop that depends on the output size of algorithm Y") rather than textbook canonical forms. AI handles canonical forms easily; composed forms are where it confidently miscounts.
- Require an empirical companion: the student writes timing code, runs it on inputs they generated, plots the curve, and reconciles theory with observation. Discrepancies must be explained.
- Rubric weights the *reconciliation* (germane) more heavily than the asymptotic answer (easily AI-derivable).

**C. Correctness / counterexample problems (germane = adversarial reasoning)**

- "Here is a proposed algorithm. Either prove it correct or produce an input on which it fails." AI is notoriously confident-and-wrong on counterexample generation, so naive outsourcing produces wrong answers that students must catch.
- Submission format: prompt used + AI response + student's verdict + supporting evidence (executable test or proof step). The deliverable centers on the verdict, not the proposed algorithm.

**D. Coding environment (the resistance dial in practice)**

- A locked browser-based editor or notebook that:
  - Disables paste from outside (allow within-document paste so refactoring isn't punished).
  - Logs keystrokes / edit history so the trajectory of the solution is visible and gradable.
  - Renders the problem statement as a non-selectable image or as text that includes student-specific elements that must be re-typed in any external prompt.
- Optional: an "AI scratchpad" *inside* the environment, so students can use AI but every prompt and response is logged and submittable. This trades surveillance against the ergonomic friction of forcing students to use external tools.

**E. Submission contract (the verification dial)**

Each problem requires:
1. The student's solution (code, analysis, or proof).
2. A short transparency statement: *if* AI was used, what was the prompt and what came back.
3. A critique of any AI output relied on, or a brief reflective note if AI was not used.
4. Evidence specific to the student's input (a trace, a timing plot, a counterexample).

The combination forecloses both shortcut paths: pure outsourcing is blocked by friction (B + D), and silent transcription is blocked by the deliverable shape (E) and the input specificity (A).

## Rationale

The user's additions lock in a tighter theoretical model than round 0 had. Three threads now do the work:

**1. The load calculus.** CLT distinguishes extraneous load (irrelevant to learning) from germane load (constructive — building schemas). The original four design moves all manipulate one of these. Critically, productive resistance does *not* raise germane load — it raises the extraneous load of *one specific path* (outsourcing). Properly calibrated, it leaves the germane path of solving-it-yourself untouched in cost, while making outsourcing more expensive than it was. The student then chooses germane work *because it has become cheapest*, satisfying the path-of-least-resistance assumption rather than fighting it.

This reframes what "good" friction looks like. Bad friction (e.g., a clunky LMS, opaque grading) raises extraneous load on *all* paths and harms learning. Good friction raises extraneous load *only on the outsourcing path*. That is the design target.

**2. ZPD as the precondition.** The germane path is only cheap if the student can actually walk it. If germane load exceeds the student's capacity, outsourcing remains cheaper *no matter how much resistance you add*, and you also create a learning failure. Hence the need for scaffolding (worked examples, partial skeletons, decomposition, feedback) calibrated to the cohort's ZPD. The Solution above leans hard on this — student-specific seed inputs, traces, and partial structure are scaffolds, not just authentication moves.

**3. Output-side verification as a robustness hedge.** The Algorithms course has an unusual feature: the AI's output is often executable, so its correctness is checkable in a way that prose isn't. This makes counterexample-and-reconcile problems especially powerful — the student gets a bonus learning signal from the AI's confident errors. Verification is also a hedge against the friction dial decaying as multimodal AI capability improves.

**Mapping to Consider This items from round 0:**

- *Instruction vs. assessment goal:* The user's addition (c) — "this instructional design introduces productive resistance" — locks in instructional design as the goal. The design produces learning; assessment of learning is a secondary, derivative concern. Removed that question.
- *Target discipline:* Answered by addition (a). Solution is now Algorithms-specific. Removed that question.
- *Failure case:* Carried forward. Still a live question that should shape evaluation.

**Assumptions worth challenging in later rounds:**

- That instructors can build and maintain the locked editor / per-student input infrastructure. This is a real engineering ask.
- That "scaffolding to ZPD" is achievable in practice across a heterogeneous cohort. Some students will be below the ZPD floor and will outsource regardless; some will be above and will find the friction merely annoying.
- That productive resistance does not interact badly with accessibility (e.g., students with motor or visual disabilities for whom transcription is a real barrier, not a productive one). A general policy needs accommodations baked in.

## Consider This

- `[from user, round 0]` (carried) `[Q from LLM]` What's the failure case you're most worried about? "Students get good grades but learn nothing" and "Students get penalized for using AI well" are both real risks, and a design that minimizes one can worsen the other.
- `[Q from LLM]` Diagnostics: how does the instructor *detect* when scaffolding has failed and germane load has exceeded a student's ZPD? Without a signal, the design silently degrades — students outsource, the friction looks "successful" (low overt cheating), but learning collapses. A good answer probably involves the keystroke / edit-history log and the transparency statement, but I'd like to know what specifically you'd watch.
- `[Q from LLM]` Falsifiability: what observation would convince you the design *isn't* working? E.g., "students complete assignments at the same rate but exam performance drops," "transparency statements show 80% pure transcription with no critique," etc. Pinning this down early shapes which data the rollout should collect.
- `[Q from LLM]` Position on the AI-allowed spectrum: is the goal (i) AI strictly forbidden, with friction as enforcement; (ii) AI permitted but channeled toward verification work; (iii) AI required as a tool the student must learn to evaluate? The Proposed Solution above currently mixes (ii) and (iii). The course's stated stance affects rubric design and the transparency-statement format.

## Perspective I'm Contributing From

_(user fills in next round)_

## Notes

- Round-0 framing of "Strategy A (input-side friction) vs. Strategy B (output-side verification)" is preserved in spirit but renamed/recast as the *resistance dial* and *verification dial* of the load calculus. The third dial — *scaffolding* — is new this round and is doing important conceptual work: it is what prevents productive resistance from collapsing into mere obstruction.
- The "load calculus" formulation is a candidate central metaphor. Worth pressure-testing in a later critique round: does it actually predict design choices, or is it post-hoc dressing on the four ideas?
