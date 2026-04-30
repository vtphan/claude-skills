## Round Stance

**Round 6**
- Stance: restructure
- Perspective I'm adopting: framework consolidator
- Substantive changes: At user's explicit direction, **rewrote the Idea from scratch** to reflect the accumulated theoretical framework — the CLT three-way decomposition, two-path load calculus, reframing-germane on the outsource path, scaffolding's bifurcated effect, path preference as an explicit design choice, and the tool-analogy framing. Replaced the round-1 enumeration (four design moves + five lettered additions) with a coherent presentation. Embedded the pedagogy diagram in the Idea (where the user originally requested it). Restructured the Proposed Solution around **four knobs** instead of three dials: scaffolding-extraneous (free move), scaffolding-germane (tradeoff), resistance (asymmetric extraneous + reframing-germane inducement), verification (evidence-bound). Re-characterized Template 3 as a *higher-order-primary* template rather than a quirky exception. Pruned Consider This items resolved by the rewritten Idea.
- Recommendation: continue

## Idea

**Context.** This is an instructional-design framework for homework assignments in an undergraduate **Algorithms** course (algorithm construction in code, running-time analysis, correctness arguments) under the working assumption that students *will* have access to LLMs. The framework does not try to prevent AI use; it channels it.

**Two foundational premises.**

1. **Path of least resistance.** Students choose the cheaper-cost path through an assignment, where cost is measured in cognitive load. The design's job is to set the relative costs of the available paths.
2. **On-substrate critical thinking is what produces learning.** Whether a student arrives at a solution by *constructing* the algorithm themselves (synthesis) or by *framing* the problem precisely for an LLM and *evaluating* its output (specification + verification), both routes produce learning — provided the thinking is on the substrate (Algorithms), not adjacent (prompt-engineering for its own sake).

**Productive resistance** is the design lever — the deliberate friction introduced to keep students struggling productively rather than escaping the struggle by outsourcing. It operationalizes *productive struggle* (a recognized learning principle) for an AI-saturated environment.

**Cognitive Load Theory framing.** The design uses CLT's three-way decomposition:

- **Intrinsic load** — the inherent cost of the topic for the student given their schemas. Set by curriculum sequencing; not tunable at the assignment level.
- **Extraneous load** — load not contributing to learning (e.g., transcribing a hand-drawn graph). Standard CLT says minimize it. *This framework's contribution:* extraneous load is tuned **asymmetrically toward the instructor-intended path** — kept low on the path the design wants students to take, and allowed to remain (or actively raised) on the non-intended path. Under synthesis-primary intent this means scaffolding extraneous away on the germane path while raising it on the outsourcing path via the resistance knob; under higher-order-primary intent it means keeping the outsourcing path paste-friendly while withholding extraneous-load scaffolding from the germane path. Note the small asymmetry between intents: under synthesis-primary, extraneous load is *actively raised* on the outsourcing path (resistance knob), because doing so also induces productive reframing-germane; there is no analogous knob on the germane path under higher-order-primary, so extraneous load there is allowed to remain at its natural level rather than actively raised.
- **Germane load** — load contributing to schema construction. Sustained at productive levels.

**Two paths through the assignment.**

- **Germane path:** engage directly with the substrate. Germane work = *algorithm synthesis*.
- **Outsourcing path:** route the substrate through an LLM. Germane work = *problem reframing* (input side: extracting abstract problem structure to ask AI cleanly) + *AI-output critique* (output side: evaluating against evidence).

Both paths produce germane work; the design is **path-tolerant**. They produce *different kinds* of learning — synthesis on one, specification + verification + AI-collaboration on the other.

**Path preference is a design choice the instructor declares.**

| Pedagogical intent | Cheapest path | What students learn |
|---|---|---|
| **Synthesis-primary** | germane | constructing algorithms by hand |
| **Higher-order-primary** | outsourcing | specifying, verifying, collaborating with AI |
| **Mixed** | roughly equal | both |

This is a *normative* choice. Synthesis-primary is the default for foundational early-term assignments where schema construction is the central goal. Higher-order-primary is appropriate for senior or capstone work where students should learn to deploy and verify AI-assisted solutions. Different instructors will reasonably choose differently; the framework's job is to make whichever choice was made implementable.

**Tool-analogy.** Calculators, high-level languages, and libraries each raised the level at which students engaged with their material. LLMs can continue this pattern — *but only if* assignments are structured so the tool replaces lower-level work while leaving specification and verification to the student. Without that structure, LLMs replace not computation but thinking.

**Pedagogy diagram.**

```
                CURRICULUM-LEVEL CHOICE
        ┌─────────────────────────────────────┐
        │ INTRINSIC LOAD = topic × schemas    │
        │ (substrate; set by sequencing,      │
        │  not tunable per assignment)        │
        └──────────────────┬──────────────────┘
                           │
                  ┌────────▼────────┐
   instructor    │  ASSIGNMENT     │
   declares  ──▶ │  with declared  │
   path pref     │  path preference│
                 └────────┬────────┘
                           │
              Student chooses cheaper path
                           │
        ┌──────────────────┴──────────────────┐
        │                                     │
   GERMANE PATH                       OUTSOURCING PATH
   (algorithm synthesis)              (specify + verify)
        │                                     │
   knobs:                              knobs:
   • scaffolding-extraneous            • resistance
     (free — lowers waste)              (asymmetric extraneous
   • scaffolding-germane                 + induces productive
     (tradeoff — cheaper                 reframing-germane on
     path, less learning)                input side)
                                       • verification
                                         (evidence-bound critique
                                         = back-end germane on
                                         output side)
        │                                     │
        ▼                                     ▼
   ╔═════════════════════════════════════════════╗
   ║   GERMANE PROCESSING OF SUBSTRATE           ║
   ║   = LEARNING                                ║
   ║                                             ║
   ║   germane path → algorithm synthesis        ║
   ║   outsource path → specification +          ║
   ║                    verification +           ║
   ║                    AI-collaboration         ║
   ╚═════════════════════════════════════════════╝

   Design wins (for a marginal student in the ZPD) when the
   instructor's preferred path is the cheaper one.
```

## Proposed Solution

The design has three layers: a **substrate** (set at curriculum level), an **intent** (path preference, declared per assignment), and **four knobs** (tuned per assignment to realize the intent).

### Layer 1 — Substrate: intrinsic load

Determined by topic × student schemas. Manipulated only via curriculum sequencing and prerequisite structure. If intrinsic load exceeds the cohort's working-memory budget, no assignment-level knob can rescue the design — students will outsource regardless because they cannot do germane work either way.

### Layer 2 — Intent: path preference

Declared explicitly at assignment design time. One of {synthesis-primary, higher-order-primary, mixed}. The intent dictates how the four knobs should be turned.

### Layer 3 — Four knobs

The previous "three dials" framing collapsed two distinct scaffolding effects into one. The corrected framework has four knobs:

| Knob | Path it acts on | Effect | Tradeoff |
|---|---|---|---|
| **Scaffolding-extraneous** | germane | lowers extraneous load (clearer rubrics, partial code skeletons for plumbing, timely feedback) | none — free move |
| **Scaffolding-germane** | germane | lowers germane synthesis load (worked examples, decomposition into sub-steps) | each unit of synthesis given away to scaffolding is a unit of learning forfeit |
| **Resistance** | outsourcing | raises extraneous load (transcription, parsing non-OCR artifacts, formulating prose around per-student inputs) **and** induces productive reframing-germane (forces abstraction of the problem structure to ask AI cleanly) | dual effect; artifact design biases the productive-vs-unproductive reframing ratio |
| **Verification** | outsourcing | converts AI output into back-end germane processing via critique deliverables | works only when critique is **evidence-bound** to per-student elements (specific traces, empirical timing curves, counterexamples on student-specific parameters); otherwise students can route critique back through AI |

### Load calculus

```
   germane_path_cost  ≈ intrinsic_load
                      + extraneous_germane    (lowered by scaffolding-extraneous — free)
                      + germane_synthesis     (lowered by scaffolding-germane — tradeoff)

   outsourcing_path_cost ≈ intrinsic_load
                         + extraneous_outsourcing  (raised by resistance)
                         + reframing_germane       (induced by resistance)
                         + verification_germane    (forced by verification)
```

`intrinsic_load` cancels on both sides (both paths process the substrate). The **synthesis-primary inequality** (design wins for marginal students when germane path is cheaper) reduces to:

```
   germane_synthesis  <  Δ_scaffolding_extraneous
                       + Δ_scaffolding_germane
                       + (extraneous_outsourcing - extraneous_germane)
                       + reframing_germane
                       + verification_germane
```

The right-hand side is what the instructor controls, in priority order:
1. **Free move first.** Crank scaffolding-extraneous as high as possible — no learning cost.
2. **Asymmetric extraneous + reframing-inducement.** Crank resistance — multimodal artifacts, per-student seeds, locked editor.
3. **Verification with evidence binding.** Crank verification.
4. **Last resort.** Reach for scaffolding-germane only when intrinsic load is too high for the cohort and curriculum cannot be re-sequenced — each unit costs learning.

The **higher-order-primary inequality** is the reverse: instructor wants outsourcing path cheapest, so the priority order flips. Resistance is *low* (paste-friendly artifacts), scaffolding-germane is *low* (hands-on synthesis stays expensive), verification is *very high* (evidence-bound critique is the central deliverable).

### Three Algorithms templates, characterized by intent

**Template 1 — "Modify Dijkstra's" (synthesis-primary).**
Hand-drawn graph **G_s** (per-student seed) with a directional-cost twist. Students implement, trace on **G_s**, analyze runtime, and submit AI-use disclosure with critique. Resistance high (multimodal, locked editor). Scaffolding-extraneous high (priority-queue boilerplate). Scaffolding-germane medium (lecture-aligned decomposition; *not* a worked example of the modified algorithm). Verification high (trace + critique).

**Template 2 — "Compose and Reconcile" (synthesis-primary, verification-led).**
Pseudocode of two algorithms F (calling H inside an output-size-dependent loop). Students derive runtime, implement, run on per-student n-values, plot log-log, reconcile theory with measurement. Resistance medium. Scaffolding-extraneous high. Scaffolding-germane medium-high on derivation (worked example of similar composed analysis), low on coding. Verification high (reconciliation paragraph is largest rubric line).

**Template 3 — "Greedy Verdict" (higher-order-primary).**
Three scenarios with proposed greedy strategies; two are correct, one fails; student gives verdict + argument-or-counterexample for each. Required AI exhibit: produce AI verdicts, agree/disagree with cited evidence. **This is a higher-order-primary template** — resistance is intentionally low (scenarios paste cleanly), and the dominant deliverable is evidence-bound AI critique. The learning goal is *evaluating AI verdicts on greedy correctness*, which transfers beyond Algorithms.

### Cross-cutting infrastructure

- Locked browser-based editor (paste-from-outside disabled; edit-history logged).
- Per-student seed function `seed = hash(student_id, assignment_id)` for graphs, n-values, parameter choices.
- Optional in-environment AI scratchpad with prompt/response logging.
- Assignment metadata recording the declared path preference and the four knob settings, so instructor can correlate design choices with outcomes across a semester.

## Rationale

This round consolidates several corrections that accumulated in conversation since round 4:

1. **Reframing-germane on the outsource path (round 5).** Idea move (1) — "either they solve or they reframe; either way they think" — only holds if reframing is on-substrate germane work. The load calculus had to include this term explicitly.

2. **Scaffolding's bifurcated effect (this round).** Strict CLT says intrinsic load is fixed by topic × schemas; scaffolding cannot reduce it. What scaffolding *does* is reduce extraneous load on the germane path (free move) and reduce germane synthesis (tradeoff: cheaper path, less learning). Treating scaffolding as a single dial obscured the tradeoff. The four-knob framing makes it visible.

3. **Path preference as explicit design choice (this round).** Earlier drafts implicitly preferred the germane path because synthesis is the central learning in foundational Algorithms work. The user's tool-analogy argument generalizes this: in some courses or for some assignments, the higher-order skills (specification, verification, AI-collaboration) *are* the central learning. The framework now makes path preference a declared property of the assignment, not an implicit assumption.

4. **Higher-order skills are durable but not LLM-specific.** Specification, scope articulation, and output evaluation are general-engineering skills that students could develop without LLMs (specs-before-implementation, code review, black-box testing). LLMs add availability and immediacy — every student has an on-demand cognitive partner. This is a real instructional asset, but the framework should not over-claim that LLMs are *necessary* for these skills.

5. **Value-laden caveat.** "LLMs are an abstraction layer like calculators" is a contested position. Some CS faculty hold that the central job of an Algorithms course is for students to construct algorithms by hand, full stop. They are not wrong by definition — they hold a different pedagogical theory. The framework's path-preference layer makes their position implementable too: synthesis-primary is exactly the AI-channeled-but-synthesis-required design.

**Mapping to Consider This items from round 5 (with closures from this round's restructure):**

- *Failure case.* Carried, with this round's specifications: (i) for synthesis-primary assignments, dial-misconfiguration that makes outsourcing cheaper; (ii) for any assignment, marginal students above ZPD invisible to friction-based detection.
- *Above-ZPD diagnostics.* Carried.
- *Falsifiability.* Carried; sharper signals now available (for synthesis-primary: "good reframing in submissions but weak code construction").
- *AI-allowed spectrum.* **Resolved** by path preference layer. The framework now allows the full spectrum to be expressed via path-preference + knob settings.
- *Implementation cost.* Carried.
- *Privacy / surveillance.* Carried.
- *Idea (e) terminology.* **Resolved** — Idea was rewritten from scratch this round.
- *Premise 2 wording (round 4 question).* **Resolved** — premise 2 in the rewritten Idea explicitly says "on-substrate critical thinking."
- *Path preference vs. path indifference (round 5 question).* **Resolved** — path preference is now an explicit declared property.

## Consider This

- `[from user, round 0]` (carried, sharpened) `[Q from LLM]` Failure case priority. The framework now articulates two distinct failure modes:
  (i) *Dial misconfiguration relative to declared path preference* — for a synthesis-primary assignment, students take the outsourcing path anyway, learning specification but not synthesis.
  (ii) *Above-ZPD students* — invisible to friction-based detection; produce zero edits and no AI prompts before giving up.
  Which is the bigger worry for a first deployment?
- `[Q from LLM]` (carried) Above-ZPD diagnostics. Hint-request mechanism, mid-assignment formative check, or other?
- `[Q from LLM]` (carried) Falsifiability. Candidate signals: (i) submissions show good reframing but weak synthesis (synthesis-primary failure); (ii) edit-history flat with bursty submission; (iii) exam performance on assignment-correlated topics drops vs. prior cohorts. Endorse, modify, or reject?
- `[Q from LLM]` (carried) Implementation cost. Locked editor + per-student seeds + edit-history logs is a real engineering project. Design-first, or constrain to deployable-now tools (standard LMS + Jupyter)?
- `[Q from LLM]` (carried) Privacy / surveillance norms around edit-history logging. Opt-in, mandatory, or seed-only authentication (no keystroke capture)?
- `[Q from LLM]` (new) **Cohort calibration.** The synthesis-primary inequality assumes a *typical* student in the ZPD. Heterogeneous cohorts have tails. Should the framework include a tail-mitigation layer — e.g., differentiated scaffolding, optional hint cascades, tiered problem statements — or is that an implementation concern outside the framework's scope?
- `[Q from LLM]` (new) **Path-preference distribution across a semester.** A foundational Algorithms course probably wants most assignments synthesis-primary, with a few higher-order-primary assignments later. What's the right ratio, and on what schedule? (This is curriculum design, not just per-assignment design.)

## Perspective I'm Contributing From

_(user fills in next round)_

## Notes

- This restructure round consolidates rounds 4–5 plus three conversational corrections (reframing-germane, scaffolding bifurcation, path preference). The framework should now be coherent end-to-end. Worth a short critique round next to verify nothing was lost in consolidation.
- The four-knob framing replaces three-dial. The new knob (scaffolding bifurcation) is genuinely new; the others are renames for clarity.
- Template 3's status changed: it was a "verification-only" exception in earlier drafts; it's now a deliberate *higher-order-primary* example. This retroactively justifies its low-resistance design.
- Candidate one-line thesis (updated): *Productive resistance is asymmetric extraneous load tuned toward the instructor-intended path, combined with evidence-bound verification, with intrinsic load held constant by curriculum.* That sentence summarizes the full round-6 framework. (Earlier phrasing said "asymmetric extraneous-load loading," which implied one-directional addition and was calibrated only to synthesis-primary intent.)
- After this round, two consecutive small-diff rounds would close convergence. The current draft is unlikely to be small-diff (substantial restructure); a critique round next would either find more to fix or set up small-diff convergence after that.
