# Mark's ruling on the five-arm blind read — 2026-08-10

**The read:** ten blinded conversations (two seatings × five arms:
Sonnet/current, Sonnet/v4, Haiku/current, Haiku/v4, Haiku/v4+guard),
built by `scripts/table_read_pack.py` from the committed artifacts,
read blind against the six-dimension grid.

**The ruling, in Mark's words (2026-08-10):** "i have read through and
feel i cant tell a difference between the haiku and what i read
earlier. i am going to just say for now pass on all and let the pilot
group tell me if they are finding inconsistencies or bad responses. i
think we are looking at very subtle differences that 90% of people
would never catch and its not an integrity or trust problem."

**What this decides:**

1. **The 90% criterion is met by the ruled instrument.** The reader who
   wrote the voice standard could not distinguish Haiku voices from
   Sonnet across ten conversations. Per the standing Goodhart rule the
   human read is the score of record; numeric scoresheets were offered
   and declined as harder than the judgment itself.
2. **Haiku voices are approved for the Table, pending pilot feedback.**
   The pilot group becomes the live quality instrument: inconsistencies
   or bad responses reported there reopen this ruling.
3. **Instrument facts that stand with the ruling** (not overridden by
   it): every arm passed the B2 hard edge; divergence and vocabulary
   ownership held on all arms; Haiku's measured weaknesses (length
   ceiling non-compliance that neither retries nor the guard-slot fix
   corrected — a clean null result; fewer question-backs; fewer
   glosses; more fabrication-screen survivors; two FIRST_PERSON high
   signals on desert) are on record for the pilot period's watch.

**Explicitly NOT settled by this ruling:**

- ~~The 1B fabrication watchlist: PENDING MARK~~ **RULED 2026-08-10,
  same day, on the side-by-side evidence
  (`T2_fabrication_side_by_side_2026-08-10.md`): "pass on all but #3,
  add the countermeasure for that class."** Entries #1/#2 are grounded
  retrieval-miss false positives; the abstraction class (#4–#8) passes
  as WATCH; entry #3 (the invented vignette — particular people and
  events spoken as communal memory with nothing in the record) is the
  one blocked class. **Countermeasure implemented the same day: the
  fabrication gate** — the existing screen+adjudicator run pre-emission
  on the buffered draft, Haiku voices only, one corrective regeneration
  on a surviving flag, fail-open (nodes.py, `[fabrication_gate]` log
  lines; verification arm `haiku-v4-guard-fabgate-table`).
- **Solo Deep Interview on Haiku** — the read covered the Table only.
  "Everything to Haiku" includes the free tier's solo mode, which is
  unmeasured on Haiku; the existing solo checkpoint instrument covers
  it cheaply before any solo swap.
- **Which block version ships** (current vs v4 — measurably near-
  neutral on emitted turns), **the round-shape cap** (A3 — still the
  dominant cost lever, untouched by model choice), **ceiling posture
  for Haiku's longer turns** (fight with max_tokens, or retune
  ceilings if the longer measure reads fine — a voice-design question,
  since the short measure IS formation for desert), and **the Sonnet
  trigger recalibration** (56% of Sonnet fires were marginal ≤1.3×).
  All route to the Phase 2 design document.
