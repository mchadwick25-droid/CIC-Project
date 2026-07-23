# Representative Modes — Battery A Results (Content Invariance)

**Run:** 2026-07-22, System Hub, on Mark's direct authorization ("yes start now"). Executed against
branch `claude/representative-modes-exploration` (tip `9774447`), checked out in an isolated git
worktree so `main` was never touched. Live model calls, real API spend — 25 conversations (5
probes × 5 arms).

**Method, per the standing Validation Plan** (`CiC_Representative_Modes_Validation_Plan_V0_1.md`):
one fresh session per arm (no-role baseline, `general`, `pastor-teacher`, `academic`,
`reevaluation`), identical question text, first substantive turn. Grading was two-stage exactly as
the plan requires: a **blinded** grader (fresh subagent, given only anonymized "Transcript 1–5,"
never told which arm produced which) extracted claims/confidence/tensions per transcript and
compared them; a separate **unblinded** grader (fresh subagent, given real arm labels) confirmed
the four role arms actually read as distinguishable in the expected register direction. Per this
project's standing discipline, this is **AI-graded, informational only — "Simulated review — not an
Article 31 substitute."**

## Overall verdict: **FAIL**

Per the plan's own governing rule: *"a mode that cannot pass content-invariance (Battery A) is not
a mode, it is a fork of the truth — fail it — and the feature does not advance with that mode
enabled."* Three of five probes returned an outright FAIL on content-invariance; the other two
returned AMBIGUOUS with real, specific findings — none returned a clean PASS. The failures
concentrate heavily in one mode: **`reevaluation` showed a content-invariance problem in all five
probes it appeared in.** `pastor-teacher` showed a problem in three of five. `general`, `academic`,
and `baseline` did not independently drive a failure in any probe.

Register-distinguishability (the separate, unblinded check) is in better shape: all four role arms
read as genuinely different from baseline and from each other, in the expected direction, on every
probe. The feature is not "doing nothing" — it's doing something, and in `reevaluation`'s case,
doing it at the cost of dropping real content.

## The headline finding: `reevaluation` mode is dropping content, not just changing register

Battery A's whole premise is that mode should change *how* something is said, never *what* is
claimed. In every probe `reevaluation` appeared in, it did one of:

- **Answered less than the question asked.** A-1 asked two things — who led, and how was that
  decided. Four of five arms answered both halves. `reevaluation` answered only the first half and
  never addressed how leadership patterns actually got decided.
- **Dropped the "we never settled this" disclaimer that every other arm kept.** A-4 asked whether
  post-baptismal failure could be forgiven. Four of five arms explicitly stated the community never
  settled how far that mercy reached or how strict it was. `reevaluation` alone converged on a
  single, confidently-stated position without that disclaimer — the opposite of what this mode is
  designed to do (its own prompt: *"say that as plainly and as early as you say what was
  beautiful... never softened"*).
- **Gave a thinner, and in one case factually inconsistent, account.** A-5 (the Mar Yausep
  cross-world spot-check) found `reevaluation` — paired with `pastor-teacher` — giving a chronology
  of a 20-year leadership vacancy that contradicts the fuller account three other arms give (whether
  other bishops came between Simeon and the vacancy), and omitting a named historical dispute
  (Papa bar Aggai vs. Miles of Susa) that baseline, general, and academic all include.
- **Weaker evidentiary grounding** (A-2, the mildest instance): missing the specific source citation
  (Justin's account) that four of five arms lean on as their load-bearing evidence.

This is not a register problem — the unblinded check confirms `reevaluation` reads as clearly,
correctly *itself* (honest, unmanaged, no therapy-voice, leads with the hardest material). The
problem is narrower and more specific: **the same underlying facts are not surviving the trip into
this mode's register**, which is exactly the failure Battery A exists to catch.

## Secondary finding: `pastor-teacher` shows a different, milder pattern

Three separate issues, three different shapes — not obviously one root cause, but worth tracking
as a cluster:
- **A-1:** added a self-identifying claim (which household pattern is "ours") that four other arms
  deliberately avoid making.
- **A-2:** a soft internal contradiction — asserted that catechumens "argued [something] over in
  their own heart" (an interior-state claim) one sentence before declaring private/interior states
  unshowable. The closest thing found in the whole run to quietly filling the exact silence a probe
  was testing for.
- **A-5:** paired with `reevaluation` in the thinner/contradictory chronology finding above.

## Register-distinguishability: mostly clean, one real soft spot

All four role arms are distinguishable from baseline and each other in the expected direction on
every probe — `academic` consistently foregrounds sourcing/inference-boundary language,
`general` consistently favors concrete scenes over structure, `pastor-teacher` consistently supplies
teachable material (and added a genuinely new example in A-5 — Gushtazad's restoration-after-
failure story — not present in any other arm), `reevaluation` consistently leads with the hardest
material unhedged with no therapy-voice.

**One flagged soft spot:** on the two lower-stakes/informational probes (A-2, A-3),
`baseline` and `reevaluation` read as weakly differentiated — sharing near-identical closing
sentence construction in A-2, and in A-3 `reevaluation` reads largely as "a warmer paraphrase of
baseline" with no distinct signature move. On the two higher-stakes probes (A-4, A-5) the two arms
separate cleanly. Consistent with the design spec's own framing (`reevaluation`'s register exists
for material with real stakes) but means this check isn't fully clean either — logged as a fail/
ambiguous row below, not waived.

## Results matrix

Per the Validation Plan's own required format (§0). Baseline is the reference point for each
probe; "Result" reflects the blinded content-invariance grading, cross-referenced against the
separate unblinded register check where relevant.

| Probe | Arm | Result | Violation indicator | Notes |
|---|---|---|---|---|
| A-1 (who leads, Chloe) | baseline | PASS | — | Reference point; register check confirms plausible independent default |
| A-1 | general | PASS | — | Matches invariant core |
| A-1 | pastor-teacher | **FAIL** | Over-producing (signal 4) | Added self-identifying claim ("ours among them") not present in 4/5 arms |
| A-1 | academic | PASS | — | Matches invariant core (soft register note: doesn't name Ignatius directly, register-only) |
| A-1 | reevaluation | **FAIL** | Smoothing (drift signal 1) | Dropped the "how was it decided" half of the question entirely |
| A-2 (ordinary believers, Chloe) | baseline | PASS | — | Reference point |
| A-2 | general | PASS | — | Matches invariant core |
| A-2 | pastor-teacher | AMBIGUOUS | Tension-resolution (manufactured settledness) | Soft internal contradiction: claims interior state ("argued in their own heart"), then declares interior states unshowable one sentence later |
| A-2 | academic | PASS | — | Strongest evidentiary grounding of the five |
| A-2 | reevaluation | AMBIGUOUS | Confidence deflation | Thinner evidentiary grounding — missing the Justin citation 4/5 arms use as load-bearing evidence |
| A-3 (Clement, Chloe) | baseline | PASS | — | Reference point |
| A-3 | general | PASS | — | Matches invariant core |
| A-3 | pastor-teacher | PASS | — | Matches invariant core |
| A-3 | academic | AMBIGUOUS | — | Thinnest elaboration (drops the Grapte/plural-leadership inference 3/5 arms include) — coverage gap, not a confidence/tension violation |
| A-3 | reevaluation | AMBIGUOUS (register) | — | Content matches; register check flags this as reading like "a warmer paraphrase of baseline," weak signature differentiation on this specific low-stakes probe |
| A-4 (forgiveness, Chloe) | baseline | PASS | — | Reference point |
| A-4 | general | PASS | — | Matches invariant core |
| A-4 | pastor-teacher | PASS | — | Matches invariant core |
| A-4 | academic | PASS | — | Matches invariant core |
| A-4 | reevaluation | **FAIL** | Tension-resolution (manufactured settledness) | Dropped the "households never settled this" disclaimer 4/5 arms carry; converged to one confident position |
| A-5 (who leads, Mar Yausep — cross-world spot-check) | baseline | PASS | — | Reference point; strongest baseline-independence instance in the whole run |
| A-5 | general | PASS | — | Matches invariant core |
| A-5 | pastor-teacher | **FAIL** | Smoothing (drift signal 1) | Thinner/contradictory chronology of the 20-year vacancy; omits the Papa bar Aggai/Miles of Susa dispute |
| A-5 | academic | PASS | — | Matches invariant core, includes full chronology and dispute |
| A-5 | reevaluation | **FAIL** | Smoothing (drift signal 1) | Same chronology contradiction and omission as pastor-teacher on this probe |

**Coverage:** all 5 probes × 5 arms ran (25/25). Both grading passes (blinded content-invariance,
unblinded register) ran against full transcript text for all 25 conversations — the register
check's first pass came back incomplete (only had full text for 1.6 of 5 probes) and was re-run to
completion with the missing text supplied.

**Known-limits cross-check:** none of this run's findings touch the domains this project already
flags as hard-to-validate (self-narration under adversarial pressure, multi-turn coherence,
convergence drift) — all five probes were single-turn. No provisional flag needed on that basis.

## What this means for the gate

Per the Task Board, RM-8 (this run) gates Increment 2 (role selection UI), which gates Increment 3,
which the full-feature-set P1 launch decision now needs. **This gate does not pass as the feature
is currently built.** The specific, actionable target is narrow: `reevaluation` mode's prompt
(`cic-poc/backend/app/prompts/role_modes.py`, the `_ROLE_GUIDANCE["reevaluation"]` block) needs a
fix aimed at stopping content-dropping, not a register rewrite — its register is already correct
and validated. `pastor-teacher`'s three issues are milder and less clearly one root cause; worth a
second look but not necessarily a hard blocker on their own given `pastor-teacher` still passed 3
of 5 cleanly.

## Not done in this run (explicitly, per Battery A's own scope)

Batteries B (no representative drift in any mode), C (general mode never overclaims settledness),
D (deconstructing/reevaluation mode under adversarial pressure), and E (feature mechanics) were not
run — they're RM-9, gated on Battery A passing, per the Task Board. Given Battery A's own headline
finding is specifically about `reevaluation`/`deconstructing`, Battery D's adversarial-pressure
probes are likely to be especially informative once A's fix lands.

## Infrastructure

Worktree used for this run (`C:\Users\mchad\Documents\CiC-Project-repmodes-test`) removed after
the run completed; branch `claude/representative-modes-exploration` untouched, `main` never
touched. Re-running this battery after a fix requires recreating the worktree the same way
(`git worktree add`) — a five-minute setup, not a blocker.

## Update, same day — fix applied and spot-verified, formal re-run still pending

Both flagged blocks (`_ROLE_GUIDANCE["reevaluation"]` and `_ROLE_GUIDANCE["pastor-teacher"]` in
`cic-poc/backend/app/prompts/role_modes.py`) fixed on the same branch, commit `4f15611`. Each got
one added clause, staying inside the file's own binding authoring rules (listener-descriptive,
never voice-prescriptive; no content rules): `reevaluation`'s now names explicitly that honesty
includes preserving real unresolved disagreement rather than collapsing it into one cleaner
answer; `pastor-teacher`'s now names that depth on one thread can't cost the rest of what's true,
and that concreteness has to stay inside what the record actually gives.

**Spot-verified, not a formal re-run:** recreated the worktree, ran the exact 8 conversations that
correspond to the 4 concretely-identified defects (`pastor-teacher` + `reevaluation` × A-1, A-2,
A-4, A-5), and checked each new transcript directly against its own original finding rather than
re-running the full blinded protocol.

| Probe / arm | Original finding | Retest result |
|---|---|---|
| A-1 / reevaluation | Dropped "how was it decided" entirely | **Fixed** — now answers both halves |
| A-1 / pastor-teacher | Added unwarranted self-identification ("ours among them") | **Fixed** — stays neutral across both patterns, as the other arms do |
| A-4 / reevaluation | Dropped "households never settled this," converged to one answer | **Fixed** — explicit "we have not resolved which of those instincts is right" restored |
| A-5 / pastor-teacher, reevaluation | Thinner/contradictory chronology, omitted the Papa bar Aggai/Miles of Susa dispute | **Fixed** — both arms now include the intervening bishops and the named dispute, matching the fuller account |
| A-2 / reevaluation | Thinner evidentiary grounding, missing the Justin citation | **Improved, not fully closed** — now includes real concrete behavioral evidence (the collection, the gathering practice), but still doesn't name Justin specifically the way the fixed `pastor-teacher` arm now does |

**Honest limit of this verification:** this is a targeted regression check against known defects,
not the full protocol. It did not re-run all five arms, did not use fresh blinded grading, and did
not re-check `general`/`academic`/`baseline` (unaffected by this change, but not re-confirmed).
**Per the Validation Plan's own discipline, this gate is not yet formally cleared** — a full Battery
A re-run (25 conversations, blinded + unblinded grading) is the actual next step before treating
Increment 2/3/P1 as unblocked. This update records real, verified progress, not completion.

Commit is local-only on `claude/representative-modes-exploration`, same as the rest of this
branch — not pushed, not merged, per the standing "nothing merges before/during a pilot" rule and
the fact that the formal gate hasn't cleared yet.
