# Pathwise Pedagogy

## Designing the Path of Least Resistance for Learning in the Age of AI

### Purpose

Pathwise Pedagogy is an instructional-design approach for AI-accessible education. It begins from a simple premise: when students have access to AI, they can often produce competent-looking work without developing the competence that the work is meant to demonstrate. The problem is not merely cheating. The deeper problem is that AI weakens the relationship between visible performance and actual learning.

Pathwise Pedagogy responds by designing learning environments in which the easiest successful path still passes through the student's own disciplinary thinking.

This document develops the approach in three layers:

1. A conceptual framework for education in the age of AI.
2. A pedagogical model for designing learning paths.
3. An application to undergraduate Algorithms, including a homework platform and assignment patterns.

This draft focuses on the conceptual framework and the pedagogical model.

## 1. Conceptual Framework

Pathwise Pedagogy begins with a basic instructional problem: learning environments ask students to move from supported performance toward independent competence, but AI can make completion look successful even when that movement has not happened.

The framework therefore separates three things that are easy to confuse:

- **completion**: producing an acceptable answer, product, proof, program, explanation, or artifact;
- **comfort**: the task feels manageable to the student;
- **competence**: the student can perform the target thinking with increasing independence.

Before AI, these three were never perfectly aligned, but they were often close enough for classroom work to function. AI weakens that alignment. A student can now complete work and feel comfortable without developing the competence the work is meant to demonstrate.

### 1.1 Learning as Movement Toward Independent Competence

The foundation of Pathwise Pedagogy is the Zone of Proximal Development (ZPD). For instructional design, the ZPD can be understood through three zones:

| Zone | Student Experience | Instructional Meaning |
|---|---|---|
| **Frustration Zone** | I cannot do this yet, even with ordinary support. | The challenge exceeds the student's current competence. |
| **Learning Zone** | I can do this with support, but not yet independently. | The task is reachable with scaffolded effort. |
| **Comfort Zone** | I can do this independently. | The task is manageable through independent competence. |

Traditional instruction tries to move students through these zones. A student encounters a target task that is currently out of reach. The instructor lowers the effective challenge through explanation, modeling, feedback, worked examples, hints, decomposition, collaboration, or other scaffolds. Over time, that support is faded. What the student could once do only with help becomes something the student can do independently.

The goal is not permanent struggle. The goal is **earned comfort**: the ease that comes from competence.

### 1.2 The AI Disruption: Borrowed Comfort

AI creates a different route to comfort. It can generate plausible answers, polished language, working code, coherent explanations, or complete analyses on behalf of the student. This creates **borrowed comfort**: the student feels capable because completion has become easier, but the ease comes from dependence rather than competence.

Borrowed comfort creates two illusions:

- **The student-side illusion:** "I can do this," when the more accurate statement may be, "I can get AI to produce this."
- **The instructor-side illusion:** "The student can do this," when the more accurate statement may be, "The student submitted work that looks like someone competent did this."

The result is **performative competence**: work that resembles mastery without reliably showing whether mastery exists.

Pathwise Pedagogy is built around this disruption. The problem is not simply that students may use AI. The problem is that AI can make the path to completion bypass the path to competence.

![Figure 1. Scaffolded Learning vs. AI Substitution](figures/skill_load_model.svg)

Figure 1 represents each point as a **learner-task state**: a particular student encountering a target task under particular support conditions. The horizontal axis is **independent competence**. Movement to the right means the student can do more of this kind of work without help. The vertical axis is **effective challenge**. This is not the task's objective difficulty in isolation; it is the challenge the task presents under current conditions of scaffolding, tool use, and independence.

The zones are defined by the relationship between competence and effective challenge. When challenge exceeds current competence, the student is in the Frustration Zone. When the task is reachable with support but not yet independent, the student is in the Learning Zone. When the task is manageable through independent competence, the student is in the Comfort Zone.

The green path shows scaffolded learning. At **A1**, the unscaffolded target challenge exceeds the student's current competence. At **A2**, scaffolding brings the task into the Learning Zone, where productive struggle becomes possible. At **A3**, guided practice supports emerging competence. At **A4**, support is gradually released as the student carries more of the work independently. By **A5**, the student reaches earned comfort through competence.

The orange path shows AI substitution. From **A2** to **B**, the student can lower the effective challenge of completion without moving rightward in independent competence. This is borrowed comfort: the task feels easier, but the student has not developed the target capability.

### 1.3 The Path of Least Resistance

Students do not choose paths through assignments randomly. They tend to choose the route that feels cheapest relative to the goal they believe they are being asked to satisfy. Cost may include time, effort, uncertainty, cognitive load, anxiety, grade risk, tool friction, and social expectations.

Pathwise Pedagogy calls this the **path of least resistance**.

In an AI-accessible environment, the path of least resistance may no longer pass through the student's own learning. A student can sometimes move from confusion to submission by routing the target thinking through AI. The submitted work may look like Comfort Zone performance even if the student never moved through the Learning Zone.

The central design problem is therefore:

> How can we shape the available paths so that the easiest successful route still requires the student to do the intended cognitive work?

### 1.4 Load and Productive Struggle

Cognitive load helps explain why one path feels cheaper than another. A path feels costly when it demands too much working memory, too much uncertainty, or too much effort unrelated to the target learning.

For this framework, three forms of load matter:

| Load Type | Meaning | Design Implication |
|---|---|---|
| **Intrinsic load** | The inherent difficulty of the material for this learner, given their current schemas. | Sequence tasks so the target thinking is reachable. |
| **Extraneous load** | Effort that does not contribute to the learning goal. | Reduce barriers that distract from the target competence. |
| **Germane load** | Effort that contributes to schema construction and transferable understanding. | Preserve enough difficulty for learning to occur. |

The Learning Zone is not the absence of difficulty. It is the presence of the right difficulty. Productive struggle is the learner's effortful engagement with a challenge that is reachable and directed at the target concept or practice.

AI intensifies the load problem because it can reduce the felt effort of completion without preserving the germane effort needed for learning. Pathwise design therefore asks not only "How hard is this task?" but also "Where does the difficulty live, and whose thinking does it require?"

### 1.5 The Core Claim

Pathwise Pedagogy can be summarized in one sentence:

> In the age of AI, instructors must design the path of least resistance so that successful completion still moves students through productive struggle toward earned comfort.

Or, more formally:

> Pathwise Pedagogy designs AI-accessible learning environments so that the easiest successful path remains coupled to the student's development of independent competence.

## 2. Pedagogical Model

The pedagogy is path design. Pathwise Pedagogy does not try to remove AI from the learning environment. It changes the conditions of successful completion so that AI substitution is less sufficient than learning.

The model has two coordinated moves:

1. **Make the intended learning path reachable.** Use scaffolding to bring the task into the Learning Zone without removing the target thinking.
2. **Shape friction on the AI substitution path.** Add requirements that make completion without understanding harder, less reliable, or insufficient.

### 2.1 Support the Intended Learning Path

The first move is scaffolding. The instructor lowers effective challenge enough to move students from the Frustration Zone into the Learning Zone. This does not mean removing the intellectual work. It means reducing barriers that prevent students from beginning the work.

On the intended path, scaffolding should:

- reduce extraneous load,
- make the task reachable,
- preserve the target thinking,
- create conditions for productive struggle,
- fade as competence increases.

This is the green path in Figure 1. Scaffolding brings the task into the Learning Zone; guided practice develops competence; gradual release transfers more responsibility to the student; earned comfort emerges when the student can perform the target work with increasing independence.

### 2.2 Shape Friction on the AI Substitution Path

The second move is the distinctive pathwise move: shape friction on the AI substitution path.

**Path-shaping friction** is not difficulty added for its own sake. It is task structure that makes bypassing the learning goal harder, less attractive, or less sufficient. It acts on routes that would produce a correct-looking submission without the intended thinking.

Path-shaping friction may include:

- student-specific inputs,
- required traces or intermediate reasoning,
- evidence-bound verification,
- critique of AI output against concrete evidence,
- in-class extensions or oral checks,
- transfer to a nearby but non-identical problem,
- restrictions on direct copying when the environment is designed for in-task reasoning.

These mechanisms work because they change what counts as successful completion. A generic AI-generated answer is no longer enough; the student must specify, adapt, verify, explain, critique, or transfer in ways that require disciplinary understanding.

The goal is not surveillance. The goal is alignment: completion should require evidence that the student has done enough of the intended thinking to move toward independent competence.

### 2.3 Require Evidence of Competence

Evidence of competence is the main mechanism for shaping friction. Because AI can produce polished final products, final products alone are weak evidence. Assignments must ask for evidence tied to the student's own reasoning.

Evidence of competence may include:

- traces of decisions, attempts, tests, or revisions;
- explanations of why a solution works;
- error analysis and counterexamples;
- student-specific examples or data;
- comparison between AI output and student evidence;
- oral explanation or live defense;
- transfer to a nearby but non-identical problem.

This evidence makes AI substitution less sufficient. A student may still use AI, but successful completion now depends on understanding, judgment, and adaptation rather than merely obtaining a plausible output.

### 2.4 Preserve Productive Struggle

Scaffolding and path-shaping friction must be balanced. Too little support leaves students in frustration. Too much completion support removes the germane effort needed for learning. Too little friction leaves the AI substitution path cheaper than the learning path. Too much friction turns the assignment into obstacle management.

Productive resistance is the design choice that preserves useful struggle on the intended path. The instructor withholds just enough completion support to keep the student reasoning, while providing enough scaffold to keep the task reachable.

In an Algorithms assignment, for example, the instructor might provide boilerplate code to reduce irrelevant implementation burden while withholding the recurrence, invariant, correctness argument, or complexity analysis that students must construct themselves. The support lowers extraneous load; the resistance preserves the target thinking.

### 2.5 Design Cycle

The model can be used as a compact design cycle:

1. **Name the target competence.** What should students become able to do independently?
2. **Place the task in the Learning Zone.** What scaffold makes productive struggle possible?
3. **Preserve the target thinking.** What support would accidentally do the work for the student?
4. **Identify the AI substitution path.** How could AI produce completion without competence?
5. **Add path-shaping friction.** What evidence or task structure makes substitution less sufficient?
6. **Fade support.** What can be removed as students move toward earned comfort?

The cycle is not anti-AI. It is anti-illusion. AI becomes a problem when it turns dependence into the appearance of independence. Pathwise Pedagogy responds by making the easiest successful path pass through learning.

## 3. Application to Algorithms

_To be drafted after the pedagogical model section._
