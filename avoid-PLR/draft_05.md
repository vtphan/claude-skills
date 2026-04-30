## Round Stance

**Round 5**
- Stance: refine
- Perspective I'm adopting: model-tightener
- Substantive changes: Added a `reframing_germane_load` term to the outsourcing-path cost — round 4's formula was missing the front-end germane work that Idea move (1) explicitly relies on. Re-characterized the resistance dial as inducing *two* effects (extraneous friction + productive reframing), not one. Qualified audit item (2): productive reframing (extracting abstract problem structure) is on-substrate; unproductive reframing (prose-generation for AI) is off-substrate — the design wants the former to dominate. Noted that the design is *path-tolerant* (both paths produce learning) but not *path-indifferent* (synthesis is the central learning goal in an Algorithms course; reframing + verification are adjacent skills). Updated the diagram to show reframing-germane on the outsourcing branch.
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
The inherent cognitive cost of the topic for *this* student given their schemas. Manipulated only by curriculum-level choices. If intrinsic load exceeds the cohort's working-memory budget, no assignment-level dial can rescue the design.

**The three dials.**

- **Scaffolding dial** — helps the student manage intrinsic load. Worked examples, partial code skeletons, lecture-aligned decomposition, timely feedback. Aim: free working-memory headroom for germane processing.
- **Resistance dial** — imposes *asymmetric cost on the outsourcing path*. The dial does two things at once:
  - Raises **extraneous load** on outsourcing more than on the germane path (transcription, parsing non-OCR artifacts, formulating prose around per-student inputs).
  - Induces **productive reframing germane load**: to ask AI a clean question, the student must extract the problem's abstract structure ("this is shortest-paths with a directional constraint") — schema-level work on the substrate.

  Both effects work in the same direction: the first pushes marginal students toward the germane path; the second ensures that if they take the outsourcing path anyway, they have done some germane work on the front end. The design wants the *productive* reframing to dominate the *unproductive* reframing (mere prose-generation for prompts), which is what makes the artifact's specifics matter — see below.
- **Verification dial** — converts AI output into back-end germane processing. Submission contracts that require critique *bound to evidence the AI cannot easily fabricate* (per-student traces, empirical timing curves on student-assigned n-values, counterexamples on student-specific parameter values).

**Productive vs. unproductive reframing.**
Not all reframing is on-substrate. Two kinds:

- **Productive (on-substrate):** the student abstracts the problem to its algorithmic structure to formulate a precise AI query. This is the same schema-construction work the germane path requires.
- **Unproductive (off-substrate):** the student translates the artifact into prose mechanically — describing the graph node-by-node, dictating the diagram. Cognitively demanding, but builds prompt-writing schemas, not Algorithms schemas.

Artifact design influences the ratio. A problem stated in dense prose with embedded notation tends to invite *unproductive* reframing — students just retype it. A problem stated as a hand-drawn graph with student-specific structure tends to invite *productive* reframing — the student has to identify what *kind* of problem this is to ask AI anything coherent. Multimodal artifacts and per-student seeds therefore are not just resistance-dial inputs; they bias the reframing toward the productive kind.

**The full load calculus.**

```
   germane_path_cost   ≈ intrinsic_load
                       + extraneous_load_on_germane_path        (kept low)
                       + germane_load_synthesis                 (the central learning)

   outsourcing_path_cost ≈ intrinsic_load
                         + extraneous_load_on_outsourcing_path  (raised by resistance)
                         + reframing_germane_load               (induced by resistance)
                         + verification_germane_load            (forced by verification)
```

`intrinsic_load` is on both sides — both paths must process the substrate. Cancelling, the design wins for marginal students (i.e., the germane path is cheaper) when:

```
   germane_load_synthesis - reframing_germane_load - verification_germane_load
   < extraneous_load_on_outsourcing_path - extraneous_load_on_germane_path
```

In words: the *extra* germane work the synthesis path requires (over and above the germane work the outsourcing path also forces) must be less than the asymmetric extraneous-load increment between the two paths. Push the right side up (resistance) and/or the left side down (scaffolding for synthesis), and marginal students migrate to the germane path.

**Path-tolerance, not path-indifference.**
A consequence of including reframing-germane and verification-germane in the outsourcing-path cost: *both paths produce germane work*. The design is therefore *path-tolerant* — it does not catastrophically fail when students choose the outsourcing path, because some learning still happens on that path. But it is not *path-indifferent*: the two paths produce *different kinds* of learning.

- **Germane path → synthesis** (constructing the algorithm).
- **Outsourcing path → abstraction + evaluation** (framing the problem precisely + critiquing AI output).

In an Algorithms course where the stated goal is to *construct* algorithms, synthesis is the central learning target; abstraction and evaluation are adjacent skills. The design therefore retains a mild preference for the germane path: the load calculus should be tuned so that the germane path is the *cheaper* path for the typical student in the cohort's ZPD. If the dials are tuned wrong and the outsourcing path is cheaper, the cohort will still learn — but they'll be learning the adjacent skills more than the central one.

---

The three Algorithms templates from rounds 2–4 are unchanged in shape:
1. **"Modify Dijkstra's"** — coding-construction, all dials high, intrinsic load high.
2. **"Compose and Reconcile"** — runtime analysis, verification-led, intrinsic load high on derivation.
3. **"Greedy Verdict"** — correctness/counterexample, verification-only, intrinsic load moderate.

Each template's verification deliverables remain bound to per-student elements (round 4's hard requirement). New observation (round 5): each template *also* biases the front-end reframing — Template 1's hand-drawn graph with directional twist forces productive reframing (classify the problem); Template 2's pseudocode-with-hand-drawn-traces does similarly for the analysis side; Template 3's three scenarios force the student to classify each as a known problem-shape.

### Cross-cutting infrastructure (unchanged)

Locked editor / per-student seeds / edit-history logs / optional in-environment AI scratchpad / assignment metadata.

## Rationale

This round responds to the user's question: *should reframing germane load be part of the outsourcing-path cost?* The answer is yes, and the omission was load-bearing.

**Why the round-4 formula was incomplete.** The original Idea move (1) explicitly says students who reframe to outsource *think* — and the design relies on that. If the resistance dial only raised extraneous (off-substrate) cost, the dial would push marginal students to the germane path but produce no learning on the outsourcing path. The Idea's claim that "either way, they think" requires reframing to be (at least partly) germane.

**Sharpening of audit item (2).** Round 4 said critical-thinking-→-learning holds only if the thinking is "on-substrate," and treated reformulation-for-AI as potentially off-substrate. That was too binary. The corrected position:

- *Productive* reframing — extracting the algorithmic structure to ask a clean question — *is* on-substrate. It is the same schema-level work the germane path requires; in fact, it is the schema-construction step *without* the synthesis step.
- *Unproductive* reframing — mechanical prose generation for prompts — is off-substrate.

The artifact controls the ratio. Multimodal + per-student-seeded problems tend to make the productive form cheaper than the unproductive form (you can't just retype a hand-drawn graph fluently — you have to abstract it). Dense-prose problems do the opposite. Audit (2)'s caveat now resolves: the design's dependence on on-substrate thinking is real, and the way to enforce it is artifact design, not just exhortation.

**Path-tolerance is a desirable property, not a concession.** Three lines of argument:
- Robustness to AI-capability decay: as AI handles more multimodal artifacts, the resistance dial weakens. If the design were path-indifferent — both paths producing equal learning — that decay would matter less. The design's mild preference for the germane path means dial decay erodes some learning quality, but doesn't collapse it.
- Robustness to affective/temporal factors (audit item 3): a fatigued student at 2am is more likely to outsource regardless of cost. Path-tolerance means this still produces some learning.
- Equity: students with lower transcription tolerance (motor/visual disabilities, ESL) face higher extraneous cost on the outsourcing path. If the design were intolerant of the outsourcing path, accommodation would have to bypass the design. With path-tolerance, accommodation can lower the resistance dial for individual students without abandoning the pedagogy.

**Mapping to Consider This items from round 4:**
- *Failure case (carried):* Round-5 update — the most-worrying failure case is now: **dials tuned so that the outsourcing path is consistently cheapest for the cohort, producing learning of adjacent skills (abstraction + evaluation) rather than the central skill (synthesis).** Detectable in submission patterns: most submissions contain AI prompts with strong abstraction (good reframing!) but minimal independent code construction.
- *Audit item (2) in light of round 5:* resolved within Rationale; carry the question forward only as it relates to Idea premise 2's wording.
- Other carried items unchanged.

**Assumptions still load-bearing:**
- That artifact design can reliably bias reframing toward the productive kind. Plausible for multimodal + per-student seeds in Algorithms; needs empirical testing.
- That graders can distinguish productive from unproductive reframing in submitted prompts. The transparency-statement deliverable supports this, but rubric language has to be specific.

## Consider This

- `[from user, round 0]` (carried, round-5 update) `[Q from LLM]` Failure case. The audit + round-5 refinement names the most precise version: *dials tuned so that the outsourcing path is consistently cheaper, producing adjacent-skill learning at the cost of central-skill learning.* Endorse, refine, or reject?
- `[Q from LLM]` (carried) Above-ZPD diagnostics — hint-request mechanism, mid-assignment formative check, or other?
- `[Q from LLM]` (carried, round-5 supported) Falsifiability. Candidates now: (i) submissions show good reframing but weak synthesis (the path-tolerance failure), (ii) edit-history flat with bursty submission, (iii) exam performance on assignment-correlated topics drops vs. prior cohorts.
- `[Q from LLM]` (carried) AI-allowed spectrum.
- `[Q from LLM]` (carried) Implementation cost.
- `[Q from LLM]` (carried) Privacy / surveillance norms.
- `[Q from LLM]` (carried) Idea (e) terminology.
- `[Q from LLM]` (round 4, carried) Premise 2 wording: tighten to "**on-substrate** critical thinking equals effective learning"? Round-5 update: this should also distinguish productive vs. unproductive reframing as the two flavors of on-substrate / off-substrate thinking on the outsourcing path.
- `[Q from LLM]` (new) Path preference vs. path tolerance. The round-5 framing says the design has a *mild* preference for the germane path because synthesis is the course's stated central goal. Is that the right characterization, or do you actually want path indifference (both paths equally valid)? The two stances imply different rubric weights — path-preference grades synthesis-on-germane-path higher than abstraction-on-outsourcing-path; path-indifference treats them as equivalent learning outcomes.

## Perspective I'm Contributing From

_(user fills in next round)_

## Notes

**Updated pedagogy diagram (candidate for Idea — I cannot edit Idea myself).**

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
                │   contract)    │     locked editor
                └───────┬────────┘
                        │
                Student weighs paths
                        │
       ┌────────────────┴────────────────┐
       │                                 │
  GERMANE PATH                    OUTSOURCING PATH
       │                                 │
[scaffolding gives                [resistance dial:
 footholds for                     extraneous (transcription,
 intrinsic load;                   parsing) RAISED HIGHER here
 extraneous load                   AND
 kept LOW]                         productive reframing
       │                            (abstract the problem
       │                            structure) — germane
       │                            work on the substrate]
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
   ║                                             ║
   ║   germane path → synthesis (central)        ║
   ║   outsourcing → abstraction + evaluation    ║
   ║                  (adjacent)                 ║
   ╚═════════════════════════════════════════════╝

   Design wins for marginal students when:
     germane_synthesis - reframing_germane - verification_germane
     < extraneous_outsourcing - extraneous_germane

   i.e., the *extra* germane work the synthesis path requires
   over the outsourcing path is less than the asymmetric
   extraneous-load increment.
```

**Other notes.**

- Round 5 is a model-tightening round prompted by a single sharp question. It illustrates a useful pattern: even in critique-and-refine cycles, missing a load term in a formula can hide for several rounds. The added term retroactively justifies Idea move (1) more rigorously than rounds 0–4 did.
- The path-tolerance argument is the strongest defence the design has against AI-capability decay over time. Worth keeping prominent in any later writeup.
- Two consecutive small-diff rounds would be needed to converge formally. Round 5 is not small-diff (a new term entered the load calculus and the audit was qualified). Round 6 could be a `subtract` round to prune the long Consider This list once the user starts answering questions, or a stop if the framework is now sufficient for the next deliverable.
