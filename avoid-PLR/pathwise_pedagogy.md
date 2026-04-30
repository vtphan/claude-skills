# Pathwise Pedagogy

## Designing the Path of Least Resistance for Learning in the Age of AI

### Purpose

Pathwise Pedagogy is an instructional-design approach for AI-accessible education. It begins from a simple premise: when students have access to AI, they can often produce competent-looking work without developing the competence that the work is meant to demonstrate. The problem is not merely cheating. The deeper problem is that AI weakens the relationship between visible performance and actual learning.

Pathwise Pedagogy responds by designing learning environments in which the easiest successful path still passes through the student's own disciplinary thinking.

This document develops the approach in three layers:

1. A conceptual framework for education in the age of AI.
2. A pedagogical model for designing learning paths.
3. An application to undergraduate Algorithms, including a homework platform and assignment patterns.

This draft focuses on the first layer: the conceptual framework.

## 1. Conceptual Framework

### 1.1 The Traditional Learning Arc

The foundation of Pathwise Pedagogy is the Zone of Proximal Development (ZPD). For instructional design, the ZPD can be understood through three zones:

| Zone | Student Experience | Instructional Meaning |
|---|---|---|
| **Frustration Zone** | I cannot do this yet, even with ordinary support. | The task is currently out of reach. |
| **Learning Zone** | I can do this with support. | The task is within the ZPD; this is where instruction should focus. |
| **Comfort Zone** | I can do this independently. | The skill has become part of the student's independent competence. |

Traditional education tries to move students through these zones. A student begins unable to do some target task. The instructor places the student in the Learning Zone by providing explanation, modeling, feedback, collaboration, worked examples, hints, or other forms of scaffolding. Over time, that support is faded. What the student could once do only with help becomes something the student can do independently.

In this model, the goal is not permanent struggle. The goal is earned comfort: the ease that comes from competence.

### 1.2 The Pre-AI Assumption: Comfort as Evidence of Independence

Before widely available AI, classroom performance was never a perfect measure of student competence, but it was often a usable signal. If a student produced a correct proof, program, analysis, explanation, or design, the instructor could often infer that the student had done at least some of the intended thinking.

In that environment, the Comfort Zone roughly aligned with the Independent Zone:

- The student could do the work.
- The student felt increasingly comfortable doing the work.
- The submitted performance gave some evidence of the student's independent competence.

Education and work were also more closely aligned. The difference between "what I cannot do" and "what I can do" in the classroom resembled the difference between "what I cannot do" and "what I can do" in professional practice. The educational task was to help students move from incapacity, through supported practice, into independent capability.

AI changes this relationship.

### 1.3 The AI Disruption: Comfort Without Competence

AI can produce competent-looking work on behalf of the student. This creates a new possibility: a student may feel comfortable completing a task not because they can do it independently, but because they can depend on AI to do much of the work.

This is borrowed comfort.

Borrowed comfort feels like mastery from the inside. The student has a working answer, polished language, plausible code, or a coherent-looking explanation. The assignment is complete. The anxiety has dropped. But the comfort may come from dependence rather than competence.

This creates two illusions:

- **The student-side illusion:** "I can do this," when the more accurate statement is, "I can get AI to produce this."
- **The instructor-side illusion:** "The student can do this," when the more accurate statement is, "The student submitted work that looks like someone competent did this."

The result is performative competence: a product that resembles mastery without reliably showing whether mastery exists.

Pathwise Pedagogy is built to address this disruption.

![Figure 1. Competence and Challenge Define the Learning Zone](figures/skill_load_model.svg)

Figure 1 represents each point as a learner-task state: a particular student encountering a target task under particular support conditions. The horizontal axis is **independent competence**. Movement to the right means the student can do more of this kind of work without help. The vertical axis is **effective challenge**. This is not the task's objective difficulty in isolation; it is the challenge the task presents to the student under the current conditions of support, scaffolding, tool use, and independence. Scaffolding can lower effective challenge without immediately increasing competence. Fading support can raise effective challenge while competence increases. AI substitution can lower the apparent challenge of completion without increasing competence.

The zones are defined by the relationship between competence and effective challenge. When challenge is low relative to competence, the student is in the Comfort Zone. When challenge is calibrated just beyond independent competence, the student is in the Learning Zone. When challenge is too high relative to competence, the student is in the Frustration Zone.

The green path shows the intended learning trajectory. At **A1**, the unaided target task is too challenging for the student's current competence. At **A2**, scaffolding lowers the effective challenge enough for productive struggle to begin inside the Learning Zone. From **A2** through **A5**, support is gradually faded while competence increases. By **A5**, the student has reached earned comfort: the task can be handled with independence because competence has grown. The orange dotted bypass shows the AI disruption. From **A2**, AI can create a shortcut to **B**, borrowed comfort, where completion feels easier but independent competence has not increased.

### 1.4 The Central Question: Scaffold or Substitute?

AI is not inherently harmful to learning. The key question is whether AI is functioning as a scaffold or as a substitute.

**AI as scaffold** helps the student work inside the Learning Zone. It may explain a concept, ask guiding questions, help interpret feedback, suggest a test case, identify a bug pattern, or model a partial strategy. The student still has to engage the disciplinary substance of the task. AI support helps the student do what they are close to being able to do.

**AI as substitute** performs the target thinking in place of the student. It writes the proof, produces the algorithm, explains the runtime, summarizes the reading, or generates the critique in a way that lets the student bypass the intended learning work. 

The same tool can play either role. The difference is not the technology itself. The difference is the design of the task, the surrounding supports, the expected evidence, and the path of least resistance.

The central design question is therefore:

> Does the assignment make AI function as a scaffold for learning, or as a substitute for learning?

### 1.5 Path of Least Resistance

Students do not choose paths through assignments randomly. They tend to choose the path that feels cheapest relative to the goal they believe they are being asked to satisfy. That cost may include time, effort, uncertainty, cognitive load, anxiety, grade risk, tool friction, and social expectations.

Pathwise Pedagogy calls this the path of least resistance.

In an AI-accessible environment, the path of least resistance may no longer pass through the student's own learning. A student can sometimes move directly from confusion to submission by routing the task through AI. The submitted work may look like Comfort Zone performance, even when the student never moved through the Learning Zone.

The instructional-design problem is to shape the available paths so that the easiest successful route still requires the student to do the intended cognitive work.

This does not mean every assignment should make AI hard to use. Sometimes the intended work is algorithm synthesis, proof construction, or independent analysis. In those cases, AI must not be allowed to substitute for the central act of learning. Other times the intended work is specification, critique, verification, comparison, or tool-mediated judgment. In those cases, AI use may be part of the intended path.

The key is not whether AI is present. The key is whether the path of least resistance passes through learning.

### 1.6 Cognitive Load: Why Paths Feel Cheap or Costly

Cognitive Load Theory helps explain why students choose one path rather than another. A path feels costly when it demands too much working memory, too much uncertainty, or too much effort unrelated to the target learning.

For this framework, three forms of load matter:

| Load Type | Meaning | Design Implication |
|---|---|---|
| **Intrinsic load** | The inherent difficulty of the material for this learner, given their current schemas. | Managed mainly through sequencing, prerequisites, and task selection. |
| **Extraneous load** | Effort that does not contribute to the learning goal. | Usually reduced on the intended learning path. |
| **Germane load** | Effort that contributes to schema construction and transferable understanding. | Preserved at a productive level. |

The Learning Zone is not the absence of difficulty. It is the presence of the right difficulty. If intrinsic load is too low, the student remains in the Comfort Zone and learns little. If intrinsic load is too high, the student enters the Frustration Zone and may disengage or outsource. If extraneous load is too high, the student may spend their effort on the wrong thing. If germane load is removed, the student may complete the task without building the intended competence.

AI intensifies these tradeoffs because it offers a way to reduce felt load without necessarily producing learning. The student can lower the effort of completion by handing the task to AI. Pathwise design therefore asks not only "How hard is this task?" but "Where does the difficulty live, and whose thinking does it require?"

### 1.7 Productive Struggle, Productive Resistance, and Path-Shaping Friction

Productive struggle is the learner's effortful engagement with a task that is challenging but reachable. It belongs in the Learning Zone. It is productive because the struggle is directed at the target concept or practice, not at irrelevant obstacles.

Pathwise Pedagogy preserves productive struggle through careful design of friction. But not all friction is the same.

**Productive resistance** is friction on the intended learning path that sustains useful thinking. It prevents the task from becoming so scaffolded, procedural, or automated that students no longer have to reason. For example, an Algorithms assignment may provide priority-queue boilerplate to remove irrelevant coding burden while withholding the key recurrence, invariant, or correctness argument that students must construct themselves.

**Path-shaping friction** is friction that prevents students from bypassing the learning goal. It acts on routes that would produce a correct-looking submission without the intended thinking. For example, student-specific inputs, evidence-bound traces, oral checks, or critique requirements can make it harder to submit AI-generated work without understanding it.

This distinction matters. Extra difficulty is not automatically educational. Friction is valuable only when it either sustains productive struggle on the intended path or prevents a bypass path from replacing the intended learning.

### 1.8 Borrowed Comfort and Earned Comfort

The goal of Pathwise Pedagogy is not to keep students uncomfortable. The goal is to create earned comfort.

| Type of Comfort | Source | Educational Status |
|---|---|---|
| **Borrowed comfort** | The student feels capable because AI can produce or polish the answer. | Risky when it hides dependence. |
| **Earned comfort** | The student feels capable because they can perform the work independently. | The desired outcome of learning. |

AI can be part of the movement toward earned comfort when it functions as scaffold. It becomes a problem when it lets students settle into borrowed comfort while appearing independently competent.

This is why Pathwise Pedagogy does not simply ask, "Did the student use AI?" It asks:

> Did AI help the student move toward independence, or did it make dependence look like independence?

### 1.9 Evidence of Competence

Because AI can produce polished outputs, final products are no longer enough. Assignments must ask for evidence that is harder to fake without doing the relevant thinking.

Evidence of competence may include:

- intermediate reasoning,
- traces of decisions,
- student-specific examples,
- error analysis,
- counterexamples,
- tests and interpretations,
- oral explanation,
- revision history,
- comparison between AI output and student evidence,
- transfer to a nearby but non-identical problem.

The point is not surveillance for its own sake. The point is alignment: the evidence required for completion should reveal whether the student is moving from supported performance toward independent competence.

### 1.10 The Core Claim

Pathwise Pedagogy can be summarized in one sentence:

> In the age of AI, instructors must design the path of least resistance so that successful completion still moves students from borrowed comfort, through productive struggle, toward earned comfort.

Or, more formally:

> Pathwise Pedagogy designs AI-accessible learning environments so that AI can serve as scaffold inside the Learning Zone without becoming a substitute for the student's movement into independent competence.

## 2. Pedagogical Model

The conceptual framework identifies the problem: AI can make dependence look like competence. The pedagogical model describes the instructional response.

Pathwise Pedagogy asks instructors to design learning paths, not just assignments. A learning path specifies what competence is being developed, what support is available, how AI may be used, what evidence of thinking is required, and how students are moved from supported performance toward independent performance.

The model has seven design principles.

### 2.1 Declare the Target Competence

Every assignment should begin with a clear statement of the competence students are meant to develop. The competence should name the kind of disciplinary thinking the student must eventually be able to perform independently.

Examples include:

- constructing an algorithm,
- proving correctness,
- analyzing running time,
- interpreting a source,
- designing an experiment,
- critiquing an argument,
- specifying requirements,
- verifying an AI-generated solution.

This matters because AI can assist with many surface products. Unless the instructor names the target competence, it is easy to mistake a polished product for learning.

The central question is:

> What should the student be able to do without AI by the end of this learning sequence?

Not every assignment must aim at AI-free performance. Some assignments may legitimately target AI-mediated competence, such as specification, critique, verification, or comparison of outputs. But even then, the target competence must be explicit. The student should know whether AI is being used as a scaffold for some later independence, or as a tool within the competence itself.

### 2.2 Locate the Learning Zone

Once the target competence is declared, the instructor estimates where the task sits relative to students' current independent competence.

The task should not live entirely in the Comfort Zone. If students can already do it independently, the assignment may confirm competence but will not develop much new competence. The task also should not live mostly in the Frustration Zone. If students cannot make meaningful progress with available support, they are likely to disengage, imitate, or outsource.

The instructional target is the Learning Zone: difficult enough to require new thinking, but reachable with support.

This is where cognitive load matters. The instructor should ask:

- Is the task demand appropriate for students' current schemas?
- Which parts of the task create intrinsic load?
- Which parts create extraneous load that should be removed?
- Which parts create germane load that should be preserved?

The goal is not to reduce all difficulty. The goal is to place the difficulty where learning happens.

### 2.3 Distinguish AI as Scaffold from AI as Substitute

AI use should be evaluated by function, not by mere presence.

AI functions as scaffold when it helps students operate in the Learning Zone while leaving the target thinking to the student. It can ask guiding questions, explain a concept, clarify an error message, suggest a test, or help the student compare alternatives. In these cases, AI reduces unproductive burden or provides temporary support while the student remains responsible for the disciplinary move.

AI functions as substitute when it performs the target competence for the student. It writes the argument, constructs the solution, performs the analysis, or produces the critique in a way that lets the student complete the assignment without developing the intended competence.

This distinction should be reflected in the assignment itself. The instructions should make clear which uses of AI are scaffold-like and which uses would replace the intended learning.

The design question is:

> What forms of AI help keep the student in the Learning Zone, and what forms let the student bypass it?

### 2.4 Shape the Path of Least Resistance

Students tend to follow the path that feels cheapest relative to the visible goal. If the visible goal is simply "submit a correct answer," then AI may create a cheaper path that bypasses learning. Pathwise Pedagogy therefore designs the visible goal, support structure, and required evidence so that the easiest successful path includes the intended thinking.

This does not require making every non-preferred path impossible. It requires making the preferred path more coherent, more supported, and more reliably successful than bypassing the learning.

The instructor has several design moves:

- reduce extraneous load on the intended path,
- preserve germane load on the intended path,
- provide scaffolds that help students begin,
- require evidence that is difficult to produce without understanding,
- make unsupported AI substitution unreliable or incomplete,
- align grading with reasoning, process, verification, and transfer.

The path of least resistance should not be the path of least thinking. It should be the path where thinking is most clearly supported and most clearly required.

### 2.5 Use Productive Resistance and Path-Shaping Friction

Pathwise Pedagogy uses friction carefully. The purpose is not to make learning unpleasant or to punish AI use. The purpose is to preserve the relationship between effort, thinking, and competence.

**Productive resistance** belongs on the intended learning path. It is the deliberate withholding of just enough completion support to keep students reasoning. An instructor may provide a code skeleton while withholding the key algorithmic idea, give a worked example of a related problem but not the assigned one, or offer hints that point students toward a structure without giving away the structure.

**Path-shaping friction** belongs on bypass paths. It prevents students from completing the task through AI substitution without engaging the target competence. This may include student-specific data, required traces, oral checks, in-class extensions, version histories, counterexamples, or verification tasks tied to the student's own work.

The two forms of friction should not be confused. Productive resistance sustains learning on the intended path. Path-shaping friction protects the assignment from routes that produce performance without competence.

A useful test is:

> Does this friction create disciplinary thinking, or merely inconvenience?

If the answer is merely inconvenience, the design should be reconsidered.

### 2.6 Require Evidence of Competence

In AI-accessible settings, the final answer is insufficient evidence. The assignment must require evidence that shows how the student is thinking and whether the student can transfer, explain, verify, or adapt the result.

Evidence should be tied to the target competence. If the goal is synthesis, evidence might include intermediate designs, failed attempts, traces, invariants, or explanations of why alternatives fail. If the goal is verification, evidence might include tests, counterexamples, empirical checks, or critique of AI output against student-generated evidence. If the goal is interpretation, evidence might include annotations, comparisons, or application to a new case.

The strongest evidence is evidence-bound: it depends on details specific to the student's task, data, reasoning, or decisions. Evidence-bound work is harder to outsource wholesale because it requires the student to connect general claims to particular artifacts.

The goal is not to monitor every keystroke. The goal is to make competence visible.

### 2.7 Fade Support Toward Earned Comfort

The endpoint of the model is earned comfort: students become comfortable because they can perform the work independently, not because AI can perform it for them.

This requires fading. Early assignments may provide more scaffolding, more examples, more structured prompts, more feedback, and more explicit checkpoints. Later assignments should remove some of that support, combine skills, ask for transfer, or require students to decide which tools and strategies are appropriate.

Fading is also how the instructor distinguishes scaffold from substitute. A scaffold can be gradually removed while competence remains. A substitute cannot be removed without performance collapsing.

The pedagogical question is:

> What support can be faded, and what competence remains when it is gone?

### 2.8 The Pedagogical Cycle

The model can be used as a repeatable design cycle:

1. **Name the target competence.**
2. **Estimate the Learning Zone.**
3. **Decide the intended role of AI.**
4. **Shape the path of least resistance.**
5. **Add productive resistance on the intended path.**
6. **Add path-shaping friction against bypass paths.**
7. **Require evidence of competence.**
8. **Fade support toward independence.**

The cycle is not anti-AI. It is anti-illusion. AI is welcome when it helps students move through the Learning Zone toward earned comfort. It is pedagogically dangerous when it lets borrowed comfort masquerade as independent competence.

## 3. Application to Algorithms

_To be drafted after the pedagogical model section._
