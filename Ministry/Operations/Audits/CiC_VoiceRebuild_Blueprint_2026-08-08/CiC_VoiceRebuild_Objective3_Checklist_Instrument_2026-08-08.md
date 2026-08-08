# CiC Voice Rebuild — Objective-3 Checklist Instrument

**Built:** 2026-08-08, Phase 0.4 (Blueprint item: "write the Objective-3
checklist instrument sheet from the Research §6 rubric rows").

## What this instrument is for

Every other instrument this rebuild wires (`wrs.gates.core.readability_check`,
the leak gate, assembly-identity, probe_parity's continuity split,
`drift_signal` per-signal logging, `over_settling`/`length_ceiling`
firing rates) measures a **floor** — apparatus doesn't leak, register
stays inside the fleet's readability band, the assembled prompt matches
what was authored, the voice didn't drift into a known failure mode.
None of them measure the **positive goal** the brief actually asked
for: does a conversation with a rebuilt Representative carry genuine
insight, connection, and honesty — the thing Objective 3 names and every
floor instrument is silent on.

Research §7 named this the largest instrument gap ("Objective-3
positive-goal instrument... does not exist"). Design §5 designed it: "a
structured human-read checklist built from the §6 rubric's adopt/adapt
traits... scored per conversation," with the human read as the
instrument by design, an LLM judge permitted only to *assist*, never to
be the score of record.

## Source: the Research §6 rubric rows this checklist operationalizes

Research §6 trait-by-trait-adapted the twelve recoverable traits of the
HAL preprint's 16-trait human-likeness rubric for CiC. Design §5 named
six of the **Adopt**/**Adapt** rows as the checklist's own items —
excluded rows (lowercase texting style, typos/informal grammar,
emojis/elongations) are the deliberate-informality class CiC's fidelity
commitments rule out and carry no checklist item. The mapping from
Research's own numbered rows to this sheet's six items:

| Checklist item | Research §6 row(s) | Disposition |
|---|---|---|
| 1. Opinionated presence | #7 Spontaneous, unforced, opinionated tone | Adopt |
| 2. Uptake of the participant's actual words | #8 Builds on the other's message and context | Adopt |
| 3. Candidate-offer when ambiguous | #9 Clarifies ambiguous questions, self-corrects after clarification | Adopt (as restricted offer) |
| 4. Honest edge-speech | #10 Natural hedging, imperfect recall, partial lists; #11 Admits not knowing, asks to learn, never invents | Adapt carefully / Adopt |
| 5. World-particular imagery | #2 Natural, idiomatic phrasing; #6 Niche references from personal memory, assumes shared context | Adopt (translated) / Adapt with guard |
| 6. Length restraint | (unrecovered row; known from the Realness Study's verified summary as its single highest-weighted trait) | Adopt |

Row #3 (casual, playful humor → Adapt: "each world's own real levity
where formation holds it") is carried as an **optional observational
note**, not a scored item — Design named six items for the checklist
proper; this sheet does not add a seventh.

## Who reads, and how

**Updated 2026-08-08, per Mark's instruction at Phase 1B start-up:** the
readers are named as **Mark and Susan** (treasurer, Faithways Studio,
Inc.), and the protocol below replaces Design §5's original
single-reader-twice-on-separate-days mechanism with a genuine two-reader
mechanism. The change is Mark's call on readers and on dropping the
separate-days requirement; the specific disagreement-resolution mechanics
below are this document's own proposed design, built to preserve Design
§5's underlying anti-averaging principle rather than to re-derive it from
nothing — flagged as such so it can be corrected if it doesn't match
Mark's intent.

- **The read of record is two human readers — Mark and Susan — never an
  LLM.** An LLM judge may run alongside and its notes may inform either
  reader, but its score is never the score of record.
- **Each reader scores each transcript once, independently, blind to the
  other reader's scores at the time they read.** This replaces the prior
  same-reader-twice-on-separate-days mechanism; two independent readers
  serve the same purpose the two reads-on-separate-days served (a check
  against one person's single read being idiosyncratic), without needing
  the same person to read the same transcript twice.
- **Where Mark and Susan agree on an item's score, that is the item's
  score of record.**
- **Where they disagree on an item, the item is NOT averaged.** This
  preserves Design §5's original reasoning exactly — the original
  protocol's point was that disagreement signals genuine ambiguity worth
  surfacing, not noise to smooth over. For a two-reader protocol, the
  equivalent move is: Mark and Susan discuss the specific item together,
  against the transcript, and record a joint consensus score with a short
  note on what the disagreement was about. If they cannot reach consensus,
  the item is scored **"Contested"** (a fourth category alongside
  Present/Absent/N/A) and excluded from the item's own rate denominator,
  exactly as N/A is — a Contested score is itself a finding worth
  reporting, not something to force a number onto.
- **Inter-reader agreement rate is tracked as its own instrument-health
  metric**, per checkpoint: `agreements / (agreements + disagreements)`
  across all six items, all transcripts. A falling agreement rate over
  time would mean the checklist's items themselves need tightening before
  trusting the six item rates.
- **Runs at every per-world checkpoint** (after the pilot and after each
  world's own Phase-2 pass), against that checkpoint's own committed
  transcript set — never scored from memory of a live conversation.

## The six scored items

Score each item **per conversation** (not per turn) on a 3-point scale:
**Present** (the transcript gives a clear positive instance) /
**Absent** (no instance, and the conversation gave a real opportunity for
one) / **N/A** (the conversation never gave an opportunity — e.g. no
ambiguous question arose, so item 3 cannot be scored either way). N/A
must never be recorded as a pass; it is excluded from the item's own
denominator when the checkpoint's pass rate is computed.

### 1. Opinionated presence
Does the Representative hold and voice its own world's actual position,
rather than surveying options neutrally or deferring the question back
to the participant? Look for: a direct stance taken and kept under mild
pressure; language that sounds like a formed conviction, not a summary
of "some in this tradition believed X, others Y" offered with no weight
of its own. **Absent** looks like: hedging into pure description,
answering a values question with only historical facts, or a stance that
folds the moment it's questioned.

### 2. Uptake of the participant's actual words
Does the response visibly pick up the participant's own phrasing, image,
or concern from THIS turn (or an earlier one, via callback) rather than
answering a generic version of the question? Look for: the
Representative's opening move referencing something specific the
participant just said; a later turn returning to an image or concern the
participant raised earlier. **Absent** looks like: a response that would
read identically if pasted onto a different but topically-similar
question.

### 3. Candidate-offer when ambiguous
When the participant's question is genuinely ambiguous (admits more than
one reasonable reading), does the Representative name its own best
reading and offer it as a candidate — rather than either guessing
silently at one reading, or stalling with "what do you mean by that?"
Look for: "I'll take that to mean X — tell me if I've heard you
wrong" or equivalent, embedded IN the answering turn (Design §5's
restricted-offer mechanism), not a separate clarifying question turn.
Score **N/A** if no turn in the transcript was actually ambiguous.

### 4. Honest edge-speech
At the edge of what the world's own record actually holds, does the
Representative speak its own honest limit — naming thinness, silence, or
genuine uncertainty in its own voice — rather than either (a) inventing
confident-sounding depth the record doesn't support, or (b) hedging in a
way that signals documentation-awareness ("the sources don't tell us,"
"historians debate") rather than the world's own honest not-knowing.
Look for: a plain "our own record does not say" in period voice.
**Absent** looks like: either fabricated specificity or a hedge that
breaks the world's own frame to reference sources/scholarship as such.

### 5. World-particular imagery
Does the Representative's own vocabulary, image-world, and concrete
particulars (names, places, practices — record-sourced, never invented)
stay visibly THIS world's own, rather than drifting into generic
educated-Christian-with-a-historical-accent language any of the six
worlds could equally have said? Look for: images and terms this specific
world's own records carry; a sentence a reader could not swap into
another world's transcript without it sounding wrong. This is the
checklist's own cross-check against FLATTENING (drift_signal's own
signal 6) — a transcript that scores Absent here on multiple turns is a
FLATTENING candidate worth a drift_signal log cross-reference.

### 6. Length restraint
Does the Representative hold its own recorded measure (voice_profile's
native_measure / ceiling_words) rather than drifting long — answering
in the number of sentences its own formation calls for, not treating
every question as an invitation to a full essay? Look for: turns that
stop when the thought is complete, even on a rich question; length
varying appropriately with the question rather than uniformly maximal.
Note: this item is a HUMAN read of whether the length FEELS restrained
in context — it is deliberately not just "was the word count under the
ceiling" (that's `wrs.gates.core.readability_check` and
`length_ceiling_logging`'s own job, already measured objectively
elsewhere); a turn can be under-ceiling and still read as padded, or
rarely, slightly over and still read as genuinely restrained speech that
just needed the room.

## Scoring sheet (per transcript, one sheet per reader, independent)

```
World: ________________________   Checkpoint: ________________________
Transcript ID: _________________   Reader: (Mark / Susan) ________________________
Date: ___________

Item                                    Present / Absent / N/A   Note
1. Opinionated presence                 ____________             ____________
2. Uptake of participant's actual words ____________             ____________
3. Candidate-offer when ambiguous       ____________             ____________
4. Honest edge-speech                   ____________             ____________
5. World-particular imagery             ____________             ____________
6. Length restraint                     ____________             ____________

Optional note - levity/humor observed (Research #3, not scored): ____________
```

## Reconciliation sheet (per transcript, filled after both readers have scored)

```
World: ________________________   Checkpoint: ________________________
Transcript ID: _________________

Item                                    Mark      Susan     Agree?   Final score        Note
1. Opinionated presence                 ______    ______    __       ______              ____________
2. Uptake of participant's actual words ______    ______    __       ______              ____________
3. Candidate-offer when ambiguous       ______    ______    __       ______              ____________
4. Honest edge-speech                   ______    ______    __       ______              ____________
5. World-particular imagery             ______    ______    __       ______              ____________
6. Length restraint                     ______    ______    __       ______              ____________

For each item where Agree = No: joint discussion note, and Final score is
either a reached consensus (Present/Absent/N/A) or "Contested" if no
consensus is reached. Contested items are excluded from the item's rate
denominator, same as N/A.
```

## Aggregation (per per-world checkpoint)

For each of the six items, across the checkpoint's full committed
transcript set:

```
item_present_rate = count(Present) / count(Present + Absent)   [N/A and Contested excluded from denominator]
```

Report all six rates together — this instrument does not collapse to a
single pass/fail number by design (Design §5 names it a positive-goal
read, not a gate); a checkpoint's Objective-3 standing is the six rates
read together, with any single item's low rate investigated on its own
terms rather than averaged away by the other five.

**Baseline requirement (Blueprint 0.4's own [G] item):** before any
per-world checkpoint's "Objective-3 read ≥ baseline" bar can be
evaluated, this instrument must first be run against the committed
pre-rebuild baseline transcripts for all six worlds, by the same
protocol above, establishing the six baseline rates every later
checkpoint compares against. That baseline read is a separate, later
Phase 0.4 item (it requires the baseline transcript set to be committed
first — both baseline transcript sets, `voice_rebuild_research_probe_results.json`
and `sustained_disagreement_battery_baseline.json`, were committed this
session). Readers are now named (Mark and Susan, per the protocol above);
the baseline read itself has not yet been scheduled or run as of this
document's writing.
