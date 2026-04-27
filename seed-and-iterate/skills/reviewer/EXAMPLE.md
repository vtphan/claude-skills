# Reviewer: Example Interactions

This file shows two Reviewer passes on the homework system — one in `traceability-check` mode and one in `frustrated-user` mode — to calibrate the skill's behavior across different review perspectives.

## Example 1: Traceability check

### Input

User invokes: "Run a traceability check across the artifact set."

Artifacts available: `seed.md`, `context.md`, `goal-first-pilot.md`, `journey-completing-assignment.md`, and 11 story files in `stories/`.

### Output

```markdown
## Review findings

Mode: traceability-check
Artifacts reviewed: seed.md, context.md, goal-first-pilot.md, journey-completing-assignment.md, stories/ (11 files)
Total findings: 6 (0 critical, 2 major, 3 minor, 1 nit)

### Critical (0)

None.

### Major (2)

1. **[coverage-gap]** Goal done condition "Devon can identify at least one student who would benefit from intervention" is not explicitly served by any Story. The closest is `story-instructor-query-interface`, but its acceptance criteria don't include the identification scenario. Add the criterion or document the implicit linkage.

2. **[orphan]** `story-event-schema-versioning` doesn't reference any journey moment. The story is technically necessary for the research bet but doesn't trace to a user experience. Acceptable, but should be explicitly tagged as infrastructure-grounded rather than journey-grounded — or surfaced as a "considered and kept despite weak grounding" item.

### Minor (3)

3. **[coverage-gap]** Journey insight "switching between problems is part of the work, not a failure of focus" is referenced by `story-autosave-progress` but is also relevant to `story-problem-navigation`, which does not currently reference it. Add the reference to make the link visible.

4. **[stale-dependency]** Journey was last updated before Story generation. No conflict was found, but two Story acceptance criteria reference behavior that may have evolved. Worth a quick re-read of the journey alongside `story-event-pipeline` and `story-autosave-progress`.

5. **[dangling-reference]** `story-test-runner` references `journey-completing-assignment#stage-iteration`, but the journey stage is named `stage-iterating`. Update the reference.

### Nit (1)

6. **[persona-drift]** `story-event-pipeline` references "instructor (and downstream researcher)" in its story statement. The Context defines "Devon" as the instructor persona and "Ana" as the researcher. Consistency would prefer using persona names; functionally equivalent.

## Summary

The artifact set traces well overall. The two major findings — the missing explicit linkage for the identification done condition, and the unanchored event-schema-versioning Story — are worth addressing before phase planning, but neither indicates a deep design problem. The dangling-reference finding is a fast fix. The journey-vs-stories staleness is worth a quick check but is unlikely to require substantial rework.
```

---

## Example 2: Frustrated-user review

### Input

User invokes: "Review the stories from a student's perspective — what would frustrate them?"

Mode: `frustrated-user`. Artifacts: stories/ (with focus on student-facing stories), `journey-completing-assignment.md` for context.

### Output

```markdown
## Review findings

Mode: frustrated-user
Artifacts reviewed: 7 student-facing stories (autosave, editor, run-tests, problem-navigation, submit, test-results-display, error-feedback), with journey-completing-assignment.md as context
Total findings: 5 (0 critical, 2 major, 2 minor, 1 nit)

### Critical (0)

None.

### Major (2)

1. **[recourse-gap]** `story-autosave-progress` requires that on persistent network failure, "edits are queued client-side and a non-modal indicator surfaces." From the student's perspective, this is uncomfortable: she's typing into the void, with a small indicator she may not notice, hoping her work survives. The Journey identifies "anxiety between submitting and confirmation" as a real moment; this is a similar moment magnified. Consider: more visible state communication, or the option to download/copy current code as a fallback.

2. **[friction-not-addressed]** Journey identifies "test failure messages may be unhelpful" as friction at `stage-iterating`. The current `story-test-results-display` requires that pass/fail per case is shown but doesn't address message quality. From a frustrated student's perspective, a system that runs tests and just says "wrong" without useful information is barely better than no tests. Either add a requirement for test message quality, or document that this is deliberately deferred.

### Minor (2)

3. **[ambiguous-state]** `story-submit-assignment` requires submission confirmation within 2 seconds. The student perspective: what happens if she submits, sees no confirmation for 5 seconds, and submits again? Double-submission handling is not specified. Either add an idempotency requirement or document the expected behavior on multiple submissions.

4. **[implicit-assumption]** `story-problem-navigation` assumes students will switch between problems within an assignment. The Journey supports this. But there's no acceptance criterion confirming that switching is a quick, low-cognitive-cost action. From the student's perspective, if switching takes a long animation or asks "are you sure?", the productive-switching pattern is broken even if technically supported.

### Nit (1)

5. **[mild-friction]** `story-editor` requires the editor to "handle code formatting." Unspecified whether autoformat-on-save is included. From the student's perspective, autoformat-on-save can be welcome (clean code) or hostile (rearranges work mid-thought). Worth specifying which.

## Summary

The student-facing Stories are mostly sound, but two findings are worth addressing before build: the autosave failure communication (which could undermine trust at exactly the worst moment) and the absent test message quality requirement (which the journey explicitly identified as friction). The double-submission and switching-cost issues are smaller but real. From a student's perspective, the Stories are functional but a few user-experience details need explicit decisions before they can be built well.
```

---

## What these examples illustrate

A few things worth noticing:

**Severity is calibrated.** Neither pass produced any `critical` findings. Both produced two `major` findings, which feels right for an artifact set in late development. Producing many `critical` findings would suggest miscalibration.

**Findings are specific and actionable.** Each finding names what's wrong and what should change. "Add the criterion or document the implicit linkage." "Consider: more visible state communication, or the option to download/copy current code as a fallback." The user doesn't have to figure out what to do.

**Modes stay in their lane.** The traceability check focused on references and coverage, not UX. The frustrated-user check focused on UX and didn't flag the dangling reference even though it would have noticed it. Each mode applies its specialized lens.

**Findings reference specific locations.** "story-autosave-progress requires...," "Journey identifies...at stage-iterating." Findings are grounded in specific artifact locations, not abstract complaints.

**Summary is brief and oriented.** Three to four sentences identifying the most important findings and giving the user a sense of how to triage. Not a restatement of the findings list.

**The frustrated-user mode produces different findings.** Same artifacts, different perspective. The traceability check missed the test-message-quality issue entirely (it traces fine — the absence is just a coverage gap from the journey, not a traceability error). This is why having multiple review modes matters.

## Counter-example: over-reviewing

> **Findings: 47 (3 critical, 12 major, 18 minor, 14 nit)**

If a reviewer pass produces this many findings, something is wrong. Either:

- The artifacts are genuinely terrible (rare).
- The reviewer is in critique mode rather than review mode (looking for things to flag).
- Severity is miscalibrated (everything reads as `major`).
- Multiple modes are being mixed.

The fix: ask whether each finding is something a thoughtful reviewer in this domain would actually flag. Drop the ones that are pedantic, redundant, or out-of-mode.

## Counter-example: under-reviewing

> **Findings: 0**

If a reviewer pass on artifacts in development produces zero findings, that's also a signal — usually that the reviewer is being too gentle. Drafts almost always have issues at the level of `minor` or `major`. Producing zero findings either means the artifacts are unusually polished (uncommon during development) or the review missed real issues.

The fix: read the artifacts again specifically looking for the things the chosen mode is supposed to find. If still nothing, the artifacts may genuinely be in good shape — but verify before declaring success.
