## Round Stance

**Round 4**
- Stance: critique
- Perspective I'm adopting: skeptical learning-sciences reviewer
- Substantive changes: Ran an 8-point soundness audit of the pedagogy. Two findings forced edits to the Proposed Solution: (i) the "raises extraneous load *only* on the outsourcing path" claim was too strong — softened to "raises extraneous load *more* on the outsourcing path than on the germane path"; (ii) the verification dial was sharpened to require critique evidence *bound to student-specific inputs* (otherwise students can have AI critique its own output). Other findings (marginal-student dependence, affective factors, on-substrate thinking) live in the Rationale as caveats and in Consider This as new questions. Produced a candidate pedagogy diagram in Notes that the user can choose to paste into Idea (I cannot edit Idea).
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
The inherent cognitive cost of the topic for *this* student given their schemas. Manipulated only by curriculum-level choices (topic sequencing, prerequisite structure). If intrinsic load exceeds the cohort's working-memory budget, no assignment-level dial can rescue the design.

**The three dials.**

- **Scaffolding dial** — helps the student manage intrinsic load. Worked examples, partial code skeletons, lecture-aligned decomposition, timely feedback. Aim: free working-memory headroom for germane processing.
- **Resistance dial** — *raises extraneous load on the outsourcing path more than on the germane path.* (Round-3 phrasing of "only on outsourcing path" was too strong — see Rationale.) Multimodal artifacts, no-copy-paste environment, per-student seeds. The asymmetry is what matters: the *increment* in extraneous cost is larger on the outsourcing path.
- **Verification dial** — converts AI output into germane processing. Submission contracts that require critique. **Critical refinement (round 4):** the critique must be *bound to evidence the AI cannot easily fabricate* — typically student-specific inputs (per-student seeded graphs, traces from the student's own code execution, empirical timing curves on the student's assigned n-values). Generic "is this correct?" critique fails because students can route it back through AI.

**The full load calculus.**

```
   germane_path_cost   ≈ intrinsic_load
                       + extraneous_load_on_germane_path        (kept low)
                       + germane_load (productive — the learning)

   outsourcing_path_cost ≈ intrinsic_load
                         + extraneous_load_on_outsourcing_path  (raised by resistance)
                         + verification_germane_load            (forced by verification)
```

Intrinsic load appears on *both* sides — both paths must process the substrate. Total cost ordering depends on the *differences*: the asymmetric extraneous-load increment plus the verification-forced germane work. Design wins for marginal students when:

```
   extraneous_load_on_outsourcing_path - extraneous_load_on_germane_path
   + verification_germane_load
   > germane_load
```

i.e., the outsourcing path's net extra cost exceeds the germane work the student would otherwise do. This is the load-calculus inequality the design is trying to engineer.

---

The three Algorithms templates from rounds 2–3 are unchanged in shape:
1. **"Modify Dijkstra's"** — coding-construction, all dials high, intrinsic load high.
2. **"Compose and Reconcile"** — runtime analysis, verification-led, intrinsic load high on derivation.
3. **"Greedy Verdict"** — correctness/counterexample, verification-only, intrinsic load moderate.

For each, the verification deliverables now must explicitly bind to per-student elements (Template 1: trace on **G_s**; Template 2: log-log plot from student's n-values; Template 3: counterexample input verified against student's parameter values). This was implicit in earlier drafts — round 4 makes it a hard requirement.

### Cross-cutting infrastructure (unchanged)

Locked editor / per-student seeds / edit-history logs / optional in-environment AI scratchpad / assignment metadata recording dial settings.

## Rationale

The user asked: *verify the logic to ensure the pedagogy is sound.* What follows is an 8-point soundness audit. Each item names what was claimed, tests it, and gives a verdict.

**(1) Premise 1 — path of least resistance.** *Claim:* students outsource when outsourcing < doing it themselves in cognitive load.
*Test:* Cohorts have three subgroups: (a) students who always engage regardless of cost (intrinsic motivation, identity-as-learner), (b) students who always outsource regardless of cost (transactional/grade-only orientation), (c) marginal students whose choice depends on cost. The design only acts on subgroup (c).
*Verdict:* **Sound for marginal students; effectiveness scales with the size of subgroup (c).** A cohort dominated by (a) doesn't need the design; one dominated by (b) is unreachable by it. This is a real bound on impact but not a logic flaw.

**(2) Premise 2 — critical thinking equals effective learning.** *Claim:* if the student thinks (either by solving or by reformulating for AI), learning happens.
*Test:* "Reformulating a problem for AI" is a cognitive activity, but it can be on the *wrong substrate* — the student may be learning prompt-engineering, not Algorithms. Idea move (1) implicitly conflates these.
*Verdict:* **Sound only if thinking is on-substrate.** The verification dial is what enforces this. Pure resistance (Idea moves 1–3) without verification can produce thinking *about how to outsource better*, not thinking *about the algorithm*. The Proposed Solution's emphasis on verification (and the now-required evidence binding) addresses this — but the Idea as written under-specifies it.

**(3) The load calculus as a model of student behavior.** *Claim:* students rationally compare path costs and pick the cheaper.
*Test:* Real students also make path choices based on confidence, fatigue, peer behavior, time pressure, and identity (e.g., "I'm not the kind of person who cheats"). At 2am the night before a deadline, fatigue dominates the cost calculus and pushes toward outsourcing regardless of asymmetry.
*Verdict:* **Useful approximation; not complete.** The model predicts central tendency well but misses tails. Robustness comes from the verification dial — affective/temporal factors push toward outsourcing, but if outsourcing still requires germane work via critique-with-evidence, the design is robust to *some* of this. Not all: a student who pastes everything and writes "the AI said so" still produces a low-quality submission that grading should catch.

**(4) Asymmetric-extraneous-load claim.** *Round-3 claim:* the resistance dial "raises extraneous load on the outsourcing path *only*."
*Test:* Hand-drawn graph artifact. Does the student on the germane path also pay extraneous cost? Yes — they have to parse handwriting, infer scale, etc. The cost is *lower* than transcribing the graph into a coherent prompt for AI, but it is not zero.
*Verdict:* **Partially sound.** The asymmetry is real and useful, but the absolute claim was too strong. **Edited the Proposed Solution: "raises extraneous load *more* on the outsourcing path than on the germane path."** What matters is the *delta*, not zero-on-germane. This also clarifies why the design should work to *minimize* extraneous load on the germane path even while *maximizing* it on the outsourcing path — they are independent levers.

**(5) Does the verification dial actually convert outsourcing into germane work?** *Round-2/3 claim:* required AI critique forces germane processing.
*Test:* Can students paste AI output and then ask AI to critique its own output? Yes. AI can simulate plausible self-critique. Without binding evidence, the critique loop closes within the AI.
*Verdict:* **Sound only with evidence binding.** **Edited the Proposed Solution: critique deliverables must require evidence bound to per-student elements (specific traces, empirical measurements, counterexamples on per-student parameters).** This is the strongest mitigation — AI can simulate critique but cannot easily fabricate empirical data against unknown student-specific seeds without itself being asked to run code (which leaves a detectable trail in the locked editor).

**(6) Scaffolding at the ZPD across heterogeneous cohorts.** *Claim:* scaffolding places the student inside the ZPD.
*Test:* Cohorts have a *distribution* of prior knowledge. Scaffolding calibrated to the median may leave the bottom quartile above-ZPD (where outsourcing is the only escape) and the top quartile below-ZPD (where the assignment is trivial and the resistance dial is just an annoyance).
*Verdict:* **Sound for the typical student; weak at the tails.** This is a known tension in any single-assignment design, not specific to this pedagogy. Mitigations: differentiated scaffolding (optional hint cascades), tiered problem statements (extension questions for the top), or a separate non-graded check-in for surfacing above-ZPD students. The hint-request mechanism flagged in round 3 partially addresses this.

**(7) Internal consistency of Idea moves 1–4.** *Claim:* the four moves are independent design dials.
*Test:* Move 1 ("make describing the problem to AI cognitively demanding") is the *consequence* of moves 2 and 3 (multimodal + no-paste produce exactly this load). Move 4 is the verification dial. So the four moves are really two strategies (resistance, verification) plus a precondition (scaffolding to the ZPD).
*Verdict:* **Internally consistent but redundant in enumeration.** No contradiction; just over-counting. The Proposed Solution's three-dial framework consolidates this cleanly.

**(8) Generalizability beyond Algorithms.** *Out-of-scope but worth noting.* The verification dial leans on AI being confidently wrong on counterexample/empirical/composed problems — true for Algorithms, less true for syntactically-routine coding tasks or for domains where AI is uniformly correct. The Idea limits scope to Algorithms (point a), so this is not a soundness issue *for the stated scope*. It does mean the framework's portability to other courses is not free — moving it to, say, an introductory-programming course would weaken the verification dial substantially.

**Summary of the audit.** The pedagogy is *substantively sound within its stated scope*, with the following verified bounds:
- Effective on the *marginal* subgroup of students; tails (always-engage / always-outsource) are unreached.
- Requires the verification dial to be evidence-bound — without that, "thinking" can drift off-substrate.
- Affective/temporal factors are out of model and create a robustness margin to design for.
- Asymmetric extraneous load is *partial*, not absolute — but the asymmetry is what matters and it holds.
- Scaffolding is calibrated to a distribution; tails are under-served by any single assignment.

No finding kills the pedagogy. Two findings forced edits to the Proposed Solution (items 4 and 5). The rest are caveats that bound the design's claims and shape future rounds.

**Mapping to Consider This items from round 3:**

- *Failure case (carried, partly addressed):* Audit item (1) sharpens this. The most-worrying failure case is now: marginal students plus above-ZPD students misclassified by the design. Edit-history logs detect the second; the first requires evidence-bound verification.
- *Above-ZPD diagnostics (carried):* Audit (6) re-affirms the case for a hint-request mechanism.
- *Falsifiability (carried):* Still open. The audit gives candidate failure signals: subgroup-(b) outsourcing rates, off-substrate prompts in the AI scratchpad, evidence-binding violations in submissions.
- *AI-allowed spectrum (carried, partly addressed):* Audit item (8) reinforces that early-term AI-forbidden assignments are appropriate for foundational topics where the verification dial would be weakest.
- *Implementation cost (carried):* Untouched this round.
- *Privacy / surveillance (carried):* Untouched this round.
- *Idea (e) terminology (carried):* Round 4's audit doesn't depend on resolving this — the Proposed Solution uses strict CLT terms. Idea (e) remains the user's call.

## Consider This

- `[from user, round 0]` (carried, sharpened) `[Q from LLM]` Failure case. Audit names two: marginal students who outsource because resistance < threshold, and above-ZPD students invisible to friction-based detection. Which is the bigger worry for you?
- `[Q from LLM]` (carried) Above-ZPD diagnostics — hint-request mechanism, mid-assignment formative check, or other?
- `[Q from LLM]` (carried, audit-supported) Falsifiability. Candidates from this round: (i) post-deadline survey shows >X% of students reporting they outsourced and could not produce the evidence-bound critique meaningfully, (ii) edit-history logs show flat trajectories with bursty submission, (iii) exam performance on assignment-correlated topics drops vs. prior cohorts. Endorse, modify, or reject?
- `[Q from LLM]` (carried) AI-allowed spectrum.
- `[Q from LLM]` (carried) Implementation cost.
- `[Q from LLM]` (carried) Privacy / surveillance norms.
- `[Q from LLM]` (carried) Idea (e) terminology.
- `[Q from LLM]` (new, from audit item 2) Should the Idea's premise 2 be sharpened to "**on-substrate** critical thinking equals effective learning"? The audit shows that thinking-about-how-to-outsource is cognitively demanding but doesn't produce Algorithms learning. The verification dial implicitly assumes on-substrate; making it explicit in the framing would tighten the pedagogy. (I cannot edit Idea — flagging.)

## Perspective I'm Contributing From

_(user fills in next round)_

## Notes

**Candidate pedagogy diagram (for Idea, if you choose to paste it in — I cannot edit Idea myself).**

```
                  CURRICULUM-LEVEL CHOICE
   ┌─────────────────────────────────────────────────┐
   │  intrinsic load  ←  topic × student schemas     │
   │  (the substrate — set by sequencing)            │
   └────────────────────┬────────────────────────────┘
                        │
                ┌───────▼────────┐
                │  Assignment    │  ← multimodal artifact,
                │  (artifact +   │     per-student seed,
                │   contract)   │     locked editor
                └───────┬────────┘
                        │
                Student weighs paths
                        │
       ┌────────────────┴────────────────┐
       │                                 │
  GERMANE PATH                    OUTSOURCING PATH
       │                                 │
[scaffolding gives                [resistance dial:
 footholds for                     transcription cost,
 intrinsic load;                   non-OCR artifact,
 extraneous load                   per-student inputs
 kept LOW]                         raise extraneous
       │                            load HIGHER here]
       │                                 │
       │                                 ▼
       │                          AI output produced
       │                                 │
       │                          [verification dial:
       │                           critique must cite
       │                           evidence bound to
       │                           per-student trace /
       │                           empirical data /
       │                           counterexample]
       │                                 │
       ▼                                 ▼
   ╔═════════════════════════════════════════════╗
   ║   germane processing of substrate           ║
   ║   = LEARNING                                ║
   ╚═════════════════════════════════════════════╝

   Design wins when, for marginal students:
     (extraneous_outsourcing - extraneous_germane)
     + verification_germane
     > germane_load_of_doing_it_yourself
```

Read the diagram top-down: curriculum sets the substrate; the assignment artifact is the entry point; the student chooses a path; both paths must converge on germane processing for learning to happen; the design's job is to make the rightward (outsourcing) path's extra cost exceed the leftward (germane) path's productive work, so a cost-minimizing student picks left. If they pick right anyway, the verification dial routes them back to germane processing at the bottom.

**Other notes.**

- The audit moved this draft from "expanding theory" mode (rounds 1–3) into "stress-testing theory" mode. That was overdue — the Notes in round 3 explicitly anticipated this round.
- After this round, the natural next moves are: (i) a `subtract` round to trim anything that didn't survive the audit, (ii) an `ask` round to actually get answers to the long Consider This list, or (iii) a stop if the user feels the framework is at sufficient fidelity for whatever comes next (paper, syllabus, prototype). Two consecutive small-diff rounds would be needed to converge formally; this round is not small-diff.
