# Context Builder: Example Interaction

This file shows a complete Context Builder pass on the homework system seed (continuing from the Seed Reader example). It exists to calibrate the skill's behavior — what good elaboration looks like, where to stop, how to handle confidence and source tags.

## Input: an accepted Seed

This is the Seed produced by the Seed Reader example, after the user accepted it.

```markdown
---
id: seed
project_name: homework system for algorithms course
status: accepted
---

# Seed

## Project description

A homework system for my algorithms course that captures fine-grained behavioral data, supports instructor intervention during assignment windows, and provides exportable data for learning research.

## Non-obvious bets

- **Infrastructure first, not features.** Build event logging, editor with autosave, and exportable data layer before any feature breadth.
- **Single course pilot before generalizing.** Algorithms course at one institution for the first iteration; multi-section and multi-course support deferred.
- **Research utility and pedagogical utility weighted equally.** Design decisions that serve only one are weaker than those that serve both.
- **Instructor-led adoption.** Students use the system because the course requires it, not because they choose it standalone.

## Out of scope

- Gradebook or LMS integration.
- Multi-institution deployment.
- Mobile clients.
- Content authoring UI for instructors.
- Human help routing or TA queue.

## Constraints

- FERPA compliance for any student data captured.
- IRB approval required before any data is used for research.
- Single instructor maintaining the system.
- Must run on existing infrastructure available to the instructor.

## Anchor personas

- Student in the algorithms course.
- Instructor (the project owner).
- Teaching assistant for the course.
- Learning scientist collaborator.

## Anchor journeys

- Completing a homework assignment.
- Getting unstuck on a problem.

## Open questions

- How much experimental infrastructure should be in phase one?
- Does the first iteration need any researcher-facing tooling?
```

## Output

### Part 1: The Context document

```markdown
---
id: context
project_name: homework system for algorithms course
seed_ref: seed
status: draft
---

# Context

## Decision points

1. I drafted four personas. "Maya" (the student) is `medium` confidence based on your teaching experience; the other three are also `medium` but lean weaker. Promote, demote, or sharpen any?
2. I propose "two to four published research papers using system data within three years" as a success outcome. Reasonable scale, or wrong altitude?
3. The strategy includes "design decisions are evaluated against both pedagogical and research utility" — this operationalizes the Seed's bet but is also a hard discipline to maintain. Confirm this is what you intend, or soften?
4. I surfaced an assumption that "students will accept fine-grained behavioral logging if disclosed transparently." This is load-bearing — if students opt out at high rates, the research bet is in trouble. How should we validate before iteration one?
5. I left "instructor-led adoption" as a strategic bet but did not propose a specific adoption mechanism (required vs. extra credit vs. default-with-opt-out). This is a design choice that should probably be a Goal-level decision; flagging here so we can revisit.

## Vision

*confidence: high*

A homework environment for college-level algorithms courses where the act of doing the work generates evidence that improves the work — better support for students, earlier intervention from instructors, and honest data for researchers studying how learning happens.

## Strategy

*confidence: medium*

- **Build the load-bearing infrastructure before any feature breadth.** Event logging, editor with reliable autosave, and exportable data are foundational; everything else is built on top of them. Resist the temptation to ship features that depend on infrastructure that isn't yet solid.
- **Treat single-course pilot as a learning instrument, not a stepping stone.** The first iteration is designed to teach what the system needs, not to be a minimum viable version of an eventual product. Generalization comes after the pilot teaches what it should.
- **Evaluate design decisions against pedagogical and research utility together.** A decision that serves only students or only researchers is weaker than one that serves both; ties are broken by which is harder to retrofit later.
- **Adoption is instructor-led, not student-driven.** Students use the system because the course requires it. This means design priorities reflect what makes the system viable for the instructor (reliability, low maintenance, reasonable workload), not what would attract students standalone.

## Success outcomes

*confidence: medium*

- Students complete homework using the system without losing work, getting confused by the interface, or opting out at rates that compromise the research signal — sustained over multiple semesters.
- The instructor can identify at least one student per assignment cycle who would benefit from intervention earlier than they could without the system, and can act on it within the assignment window.
- Two to four research papers using system-generated data are published within three years, drawing on data the system was designed from the start to capture cleanly.
- At least one design decision in a future iteration is changed because of evidence the system itself surfaced — i.e., the system informs its own evolution.
- The system runs through at least three semesters with the original maintainer (the instructor) without requiring a dedicated ops investment.

## Personas

### Maya — first-year student in the algorithms course

*source: observed*  *confidence: medium*

- **Traits:** Variable prior programming experience; strong incentive to do well in the course but uncertain about how to study effectively; may or may not have a peer network in the course.
- **Context:** Works on homework in evenings and the day before deadlines, often on a laptop, sometimes after long days of other classwork. Has access to tools (browser, AI assistants, classmates) that she could use to circumvent learning, and is aware her instructor cares about this tension.
- **Goals:** Complete homework correctly. Understand the material well enough to do well on exams. Avoid feeling stupid or behind.
- **Frustrations:** Not knowing whether her struggle on a problem means "push harder" or "your strategy is wrong." Social cost of asking for help. Losing work when something goes wrong with the tools.

### Devon — instructor (the project owner)

*source: observed*  *confidence: medium*

- **Traits:** Domain expert in algorithms and CS education; teaches the course annually; runs research on student behavior alongside teaching; limited time for system maintenance during semesters.
- **Context:** Maintains the system during semesters while teaching multiple courses and supervising graduate students. Cannot rely on dedicated ops staff. Wants the system to work without daily attention but expects to fix things between semesters.
- **Goals:** Teach algorithms effectively. Identify and intervene with struggling students before grades reflect their struggle. Generate research-quality data from real teaching contexts.
- **Frustrations:** Tools that are pedagogically good but research-hostile, or research-friendly but not viable in a real course. Maintenance burden that competes with teaching and research time. Adoption costs that fall on him rather than the students.

### Priya — graduate teaching assistant for the course

*source: assumed*  *confidence: low*

- **Traits:** Graduate student, takes the TA role partly for funding and partly for teaching experience; familiar with the course material but not as deeply as the instructor; balances TA duties with their own research.
- **Context:** Holds office hours, grades work, may answer student questions on a course platform. Limited bandwidth for system features that require active engagement.
- **Goals:** Help students who need help; fulfill TA responsibilities efficiently; not become the bottleneck for student support.
- **Frustrations:** Not knowing which students most need help when many are asking. Office hours that are over-attended or under-attended for unpredictable reasons.

### Ana — learning scientist collaborator

*source: observed*  *confidence: medium*

- **Traits:** Faculty colleague at the same institution or another; published in CS education or learning sciences; collaborates on study design and analysis but is not the system's day-to-day operator.
- **Context:** Engages with the system's data, not the system itself. Reads exports, writes analyses, contributes to study design before deployment.
- **Goals:** Answer research questions that are credible, novel, and replicable. Work with data that's clean enough to analyze without heroic preprocessing.
- **Frustrations:** Data that's almost good enough but missing one critical field. Schemas that change without warning. Studies that can't be replicated because the underlying instrument changed.

## Constraints

*confidence: high*

- **FERPA compliance.** Student records and behavioral data are protected; deidentification is required for any export beyond the instructor and IRB-covered researchers; access logs are required for instructor-side views.
- **IRB approval required for research use.** No data is used for research analysis or publication without an approved protocol covering it. The system must support distinguishing between operational data (used for teaching) and research data (used under IRB).
- **Single-maintainer operations.** No dedicated DevOps. The system must be deployable, monitorable, and recoverable by the instructor alone, with reasonable time investment.
- **Existing infrastructure.** The system runs on infrastructure already available to the instructor (institutional servers, existing storage, existing collaboration tools). No procurement of new platforms.

## Open assumptions

- *source: assumed* Students will accept fine-grained behavioral logging when it is disclosed transparently and presented as part of a course requirement. — *validate by:* a brief explanatory disclosure shown to students at first login, plus monitoring of opt-out rates if opt-out is allowed.
- *source: assumed* The instructor's existing IRB framework can be extended to cover this system without a substantial new application. — *validate by:* a conversation with the IRB before iteration one ships.
- *source: assumed* Event volume from a single section's behavior will be tractable on existing infrastructure without specialized analytics tooling. — *validate by:* a quick load estimate based on expected events per student per assignment, run against current storage capacity.
- *source: assumed* Instructors and researchers want to use the same underlying data, just filtered or aggregated differently — i.e., one event log can serve both purposes. — *validate by:* sketching the queries the instructor needs and the queries the researcher needs against the same schema, and checking they're both clean.
- *source: assumed* The "infrastructure first" bet does not undermine instructor adoption — i.e., the instructor (you) is willing to use a system that has thin features but solid pipes for at least one full semester. — *validate by:* honest self-check, ideally with a backup plan if the early pilot is too thin to be useful for teaching.

## Change log

- 2026-04-27: Initial draft from accepted Seed.
```

### Part 2: Summary

- Drafted four personas with `medium` to `low` confidence. The student persona ("Maya") is grounded in the user's teaching experience; the instructor persona ("Devon") is essentially the user themselves; the TA and learning scientist personas are weaker and may need sharpening or validation.
- Strategy operationalizes the Seed's bets into concrete decision-shaping bullets. The third bullet ("evaluate decisions against pedagogical and research utility together") is a hard discipline to maintain — flagged in decision points so the user can confirm or soften.
- Success outcomes are scoped at the project level (two to four research papers in three years) rather than iteration level. The "system informs its own evolution" outcome is unusual but seems consistent with the research bet — flagged for confirmation.
- Surfaced five open assumptions, three of which are load-bearing (student acceptance of logging, IRB extension feasibility, and the dual-purpose data assumption). Each has a brief validation note.
- One thing I deliberately did not propose: a specific adoption mechanism (required, extra credit, default-with-opt-out). This is a design choice that should be a Goal-level commitment, not a Context-level one. Flagged in decision points.

---

## What this example illustrates

A few things to notice about this example, since they show what calibrated Context Builder output looks like:

**Vision is grounded but not grand.** The vision sentence is specific to this project — homework, algorithms courses, evidence-generating — rather than aspiring to transform education. It connects to all three of the Seed's user roles (students, instructors, researchers) without inflating the project's scope.

**Strategy bullets do real work.** Each strategy bullet would help the user say no to something. "Build infrastructure first" excludes a class of feature-driven prioritization. "Single-course pilot as a learning instrument" excludes treating it as a generalizable v1. "Evaluate decisions against both utilities" excludes optimizing only one. "Instructor-led adoption" excludes student-marketing concerns. None of these are platitudes.

**Success outcomes are observable, time-scoped, and tied to the vision.** They're not features ("ship the dashboard") and not aspirations ("students love it"). The "system informs its own evolution" outcome is unusual and worth surfacing in decision points.

**Personas are calibrated honestly.** "Maya" gets `medium` confidence — the user has taught the course, but the specific persona is still a draft. "Priya" (the TA) gets `low` confidence because the user hasn't been a TA in this context recently. The temptation to tag everything `high` or `medium` was resisted.

**Constraints are elaborated, not invented.** Each Seed constraint became a Context constraint with specific implications. No new constraints were introduced; they would have required Seed-level commitment.

**Open assumptions surface load-bearing uncertainties.** The assumption about student acceptance of logging is the kind of thing that, if wrong, would compromise the research bet entirely. Surfacing it explicitly is more useful than letting it propagate silently.

**Decision points are specific.** Each one names a concrete thing the user should react to — not "review the personas" but "promote, demote, or sharpen the persona confidence tags." The user can answer each in a sentence.

## Counter-example: when a Seed isn't ready

For contrast, here's what good Context Builder output looks like when the Seed is too sparse to elaborate from. Input: a Seed with only a project description and one bet, no personas listed, no constraints listed, no journeys.

Output:

> The Seed is too sparse to produce a useful Context. I would be guessing more than elaborating in most sections — particularly personas, where the Seed names no anchor roles, and constraints, where the Seed lists none.
>
> I recommend running another Seed Reader pass to populate the Seed's anchor personas, constraints, and out-of-scope sections before invoking Context Builder. Specifically:
>
> - Anchor personas: which roles should the Context elaborate?
> - Constraints: institutional, technical, or ethical constraints the Context should honor?
> - Out of scope: at least a few items so that the strategy has something to constrain against?
>
> Once those are in the Seed, Context Builder can produce a draft that's grounded rather than speculative.

That's the entire output. Refusing to draft when the Seed isn't ready is more useful than producing a Context full of `low` confidence inventions.
