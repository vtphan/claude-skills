## Round Stance

**Round 3**
- Stance: expand
- Perspective I'm adopting: cognitive-load-theorist tightening the framework
- Substantive changes: Made intrinsic load explicit as the *substrate* of the design — the topic-student pairing that the assignment is *about*, set by curriculum and prior knowledge, not directly tunable at the assignment level. Repositioned the scaffolding dial as the lever that helps students *manage* intrinsic load (rather than as a lever that "lowers germane load," which conflated two CLT constructs). Added an intrinsic-load characterization to each of the three templates. Surfaced a `[Q from LLM]` flagging that Idea point (e) uses "germane load" loosely in CLT terms — only the user can decide whether to clean that up directly.
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

The design has two layers: a **substrate** (intrinsic load, set by topic and student) and three **dials** (scaffolding, resistance, verification) that the instructor turns at the assignment level.

**The substrate: intrinsic load.**
Intrinsic load is the inherent cognitive cost of the topic, *for this student, given their current schemas*. It is a function of:
- The element interactivity of the material — how many concepts must be held in working memory simultaneously to make sense of the problem (e.g., shortest paths involves graph + relaxation + priority order + invariant; counting sort involves only one).
- The student's prior knowledge — well-formed schemas chunk multiple elements into one, so a student who has internalized "BFS" treats it as a single element rather than a queue + visited-set + level-order procedure.

Intrinsic load is *not directly tunable at the assignment level*. The instructor manipulates it by:
- **Topic choice and sequencing** (curriculum-level): "we cover greedy after divide-and-conquer, after sorting, after recursion."
- **Worked-example density and decomposition** in the assignment: more decomposition does not lower intrinsic load itself, but lets the student traverse it in smaller chunks.

A correctly-pitched assignment has intrinsic load + minimum-necessary extraneous load + headroom for germane processing all fitting under the student's working-memory ceiling.

**The three dials.**

- **Scaffolding dial** — *helps the student manage the intrinsic load of the substrate.* Worked examples (which provide a partial schema the student can borrow), partial code skeletons (which lower element interactivity by absorbing routine plumbing), lecture-aligned decomposition (which sequences sub-problems), and timely feedback (which prevents wrong schemas from solidifying). Scaffolding does not reduce intrinsic load — it gives the student footholds for processing it within working-memory limits.
- **Resistance dial** — *raises the extraneous load of the outsourcing path specifically.* Multimodal artifacts, no-copy-paste environment, contextual references the student must add, per-student seeds. The crucial property: this dial leaves intrinsic load and germane processing alone; it adds extraneous load *only* to the outsourcing path. (Standard CLT prescriptions say "minimize extraneous load," and that still applies *on the germane path* — the design's contribution is to load the *outsourcing* path with extraneous cost without polluting the germane one.)
- **Verification dial** — *converts AI output into further germane processing.* Submission contracts that require critique, justification, or empirical reconciliation. Pushes the cognitive work to the back end of the assignment.

**The full load calculus.**

For a given student, the cost of each path is roughly:

```
   germane_path_cost   = intrinsic_load (managed by scaffolding)
                       + extraneous_load_on_germane_path  (kept low)
                       + germane_load (the learning work itself, productive)

   outsourcing_path_cost = extraneous_load_on_outsourcing_path  (raised by resistance dial)
                         + verification_germane_load  (forced by verification dial)
```

The design wins when `germane_path_cost < outsourcing_path_cost` for the typical student in the cohort's ZPD. This requires:
- Intrinsic load to be matched to the cohort (curriculum / topic sequencing).
- Scaffolding sufficient that the student has working-memory headroom for germane processing.
- Resistance high enough that outsourcing is actually expensive.
- Verification high enough that even successful outsourcing forces germane work.

If intrinsic load is too high relative to the student's prior knowledge, *no resistance level can fix this*. The student lacks the working-memory budget to do germane work even if outsourcing is forbidden, so the design fails into one of two ways: (i) student outsources anyway, paying extraneous cost without learning; (ii) student gives up. This is why intrinsic load is the substrate, not a dial — getting it wrong cannot be fixed at the assignment level.

---

The three Algorithms-course templates from round 2 are unchanged in shape but now characterized along the substrate axis as well.

### Template 1 — Coding-construction: "Modify Dijkstra's"

- **Intrinsic load (substrate):** High. Element interactivity is significant — graph representation + priority-queue invariant + relaxation + the new direction-conditional twist. Assumes prior schemas: BFS/DFS, basic Dijkstra, simple proof-of-correctness style.
- **Scaffolding dial:** Medium-high. Lecture decomposition + partial code skeleton + per-student seeded graph as a concrete anchor.
- **Resistance dial:** High. Multimodal artifact, locked editor, per-student seed.
- **Verification dial:** High. Trace on student's specific input + critique of any AI output.

### Template 2 — Analytical / runtime: "Compose and Reconcile"

- **Intrinsic load (substrate):** High on the derivation side (composed runtime requires holding both algorithms' costs and their dependency in working memory simultaneously). Moderate on coding. Assumes recurrence-solving, basic asymptotic comparison, and log-log plotting.
- **Scaffolding dial:** High on derivation (worked example of similar composed analysis, recurrence cookbook). Low on coding.
- **Resistance dial:** Medium. The artifact's resistance lives in hand-drawn traces and per-student n-values; pseudocode itself is paste-friendly by design.
- **Verification dial:** High. The reconciliation paragraph between theory and empirical data is the largest single rubric item.

### Template 3 — Correctness / counterexample: "Greedy Verdict"

- **Intrinsic load (substrate):** Moderate. Element interactivity is contained per scenario (one greedy strategy + one problem at a time), but exchange arguments and cut arguments require schemas the student must have available. Assumes recent lecture coverage of these proof patterns.
- **Scaffolding dial:** High. Verdict-deliverable structure is fully prescribed; lecture-prescribed argument templates.
- **Resistance dial:** Low — deliberately. Scenarios paste cleanly. The friction is not at input.
- **Verification dial:** Very high. Required AI-agreement-with-evidence exhibit forces interrogation of AI verdicts.

---

### Cross-cutting infrastructure (unchanged from round 2)

Locked editor / per-student seeds / edit-history logs / optional in-environment AI scratchpad / assignment metadata recording dial settings.

## Rationale

The user's question — "what role does intrinsic load play?" — exposed that the prior framing was treating CLT as two-way (extraneous vs. germane) when CLT is three-way (intrinsic + extraneous + germane). That conflation has been load-bearing in the previous drafts, and it shows up as imprecision in Idea point (e) and in the round-1/2 description of the scaffolding dial.

Three things change as a result of separating intrinsic load out:

1. **Scaffolding's job is sharpened.** Round-1/2 said scaffolding "lowers germane load to a tractable level." That was wrong as stated — scaffolding doesn't lower germane load (you *want* high germane load; that's the learning). Scaffolding helps students manage *intrinsic* load so that germane processing has working-memory room. The dial description now reflects this.

2. **The design's failure mode at high intrinsic load is now visible.** If a topic is too hard for a student's current schemas, no friction design can rescue it: the student will outsource regardless because they cannot do germane work even if outsourcing were forbidden. This means the design is *complementary to good curriculum sequencing*, not a substitute for it. Productive resistance only works when intrinsic load is already matched to the cohort.

3. **The "good extraneous load" move becomes more defensible.** Standard CLT prescription is to *minimize* extraneous load. The resistance dial appears to violate this — but only because standard CLT does not consider the case where there are *two paths* through the assignment with different load profiles. The design's contribution to the CLT literature, if you wanted to write it up, is the asymmetric extraneous-load argument: extraneous load on the germane path should be minimized; extraneous load on the outsourcing path should be maximized. Intrinsic load and germane load are equal across both paths (the topic is the topic), so the differentiator is extraneous load on each path.

**A note on Idea (e).** Strictly in CLT terms, Idea (e) reads "germane load is less than the extraneous load incurred by outsourcing." If "germane load" is read as germane-load-narrowly, this is fine — the productive thinking work is cheaper than the friction of paste-and-prompt under the no-paste regime. If "germane load" is read loosely as "the cost of doing the work yourself" (which probably encompasses intrinsic load too), the statement is still substantively right, but uses the term loosely. This is not a defect — Idea statements are working framing, not formal definitions — but if the design is written up later (paper, talk, syllabus), point (e) is worth tightening. I cannot edit it; flagging in Consider This.

**Mapping to Consider This items from round 2:**

- *Failure case (carried):* Intrinsic load now provides a sharper articulation of the second-most-worrying failure case: students for whom intrinsic load exceeds their schemas, who outsource regardless of the friction. This subgroup is invisible to friction-based detection — they pay the extraneous cost willingly because the alternative (give up) is worse for them.
- *Diagnostics (carried, partly addressed):* Edit-history logs detect *behavior*; they don't detect intrinsic-load failure. A student stuck above ZPD might produce zero edits and no AI prompts before giving up. Adding a "hint-request" mechanism (low-cost, ungraded) might surface this.
- *Falsifiability (carried):* Still open. A round on this would be valuable.
- *AI-allowed spectrum (carried, partly addressed):* The intrinsic-load articulation strengthens the case for *some* assignments at the AI-forbidden end of the spectrum — specifically, foundational early-term assignments where intrinsic load is already high relative to the cohort's schemas, and adding any AI temptation could collapse the design.
- *Implementation cost (new in round 2):* Untouched this round. Worth a critique-style round on whether the cross-cutting infrastructure is realistic for a single instructor.
- *Privacy / surveillance (new in round 2):* Untouched this round.

**Assumptions:**

- That intrinsic load can be reasonably estimated for a cohort. In practice instructors do this implicitly via "this topic should be possible for students after week N." A more rigorous version might use diagnostic pre-assessments.
- That a single assignment serves a cohort with a *distribution* of prior knowledge, so any "intrinsic load" claim is really a claim about the typical student. This is an under-served population at the tails, particularly the low-prior-knowledge tail.

## Consider This

- `[from user, round 0]` (carried) `[Q from LLM]` What's the failure case you're most worried about? "Students get good grades but learn nothing" and "Students get penalized for using AI well" are both real risks, and a design that minimizes one can worsen the other.
- `[Q from LLM]` (carried, sharpened) Diagnostics for above-ZPD students: edit-history logs detect *behavior*, but a student above their ZPD may produce no edits and no AI prompts before giving up — invisible to the friction mechanism. Should the design include a low-cost ungraded hint-request mechanism (or similar) to surface intrinsic-load failure?
- `[Q from LLM]` (carried) Falsifiability: what observation would convince you the design *isn't* working? Pinning this down shapes which data the rollout should collect.
- `[Q from LLM]` (carried, partly addressed) Position on the AI-allowed spectrum. Round-3 case: foundational early-term assignments may warrant AI-forbidden status. Endorse, modify, or reject?
- `[Q from LLM]` (carried) Implementation cost — locked editor, per-student seeds, edit-history logs. Design-first or deployable-first?
- `[Q from LLM]` (carried) Privacy / surveillance norms around edit-history logging.
- `[Q from LLM]` (new) **Idea (e) terminology.** As written, point (e) says "germane load is less than the extraneous load incurred by outsourcing." Read narrowly, this is accurate. Read broadly (germane load standing in for "the cost of doing it yourself," which includes intrinsic load), it is loose in CLT terms. Do you want to keep it as-is (working language), or is this the moment to refine it? I can't edit the Idea — but I can sharpen the Rationale and Proposed Solution to use the strict three-way decomposition while you decide.

## Perspective I'm Contributing From

_(user fills in next round)_

## Notes

- This round responds to a question about the framing rather than the artifact, and the response was to *expand* the conceptual scaffolding rather than change the templates. That is a reasonable answer to a framing question, but it's also the kind of move that can lead to over-theorizing. A future round should probably ask: does the substrate-plus-dials articulation actually change a design choice, or does it just dress up what was already there? If it doesn't change a choice, it's clarification, not insight.
- Candidate central thesis if this is ever written up: *"Productive resistance is asymmetric extraneous-load loading: minimize extraneous load on the germane path, maximize it on the outsourcing path, with intrinsic load held constant by curriculum sequencing."* That sentence summarizes the round-3 framework in one breath.
