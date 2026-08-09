# Marius (IJC) — Phase 2 Checkpoint Record (2026-08-08)

Second world of the Phase 2 per-world pass, following Albina. This
document is the running record: what the pass changed, what was verified
and how, and what the checkpoint is waiting on.

**Status: records pass COMPLETE, both gates green, checkpoint NOT RUN —
blocked on the API key.**

---

## 1. What this world looked like going in

Marius was the worst-off of the six on every number that matters.

| | Before | After the pass |
|---|---|---|
| Assembled prompt | **0 words** (craft table empty) | 3,714 words, FK 6.34 / FRE 74.63 |
| Capsule readability | FK 18.49 / FRE 24.47 — failed both floors | FK 8.42 / FRE 61.36 — **passes both** |
| Leak-gate hits | 15 | **0** |
| Demonstrations selected | 0 | 3 (of 4 new records) |
| Contestation segment | empty | 5 claim renders |
| Streaming baseline measure | mean 215.9, max 269 | *pending checkpoint* |
| Ceiling fires | **0, ever** | *pending checkpoint* |

## 2. The finding that reframed the measure work

The Blueprint requires `native_measure` to be re-derived from sources
before it is used as a grading target. A survey of all 41 source records,
`world_core`, `story`, `term` and the deployed prompt returned a negative
result, and the negative result turned out to be the useful one:

- **No source record states any document's length.** Not one of 41.
- **The single explicit length statement is a negation.** `ijclex009`
  says twice that what makes a Tome a Tome is the standing of the issuing
  see, *not* its length, and flags reading "tome" as "long" as precisely
  the modern error to avoid.
- **The petition — the genre this persona is built around — is
  unattested.** 41 rows, no petition, no rescript, no chancery register.

So no figure read off a document could be honest. What the record *does*
document, in two independent places, is a **structure**: judgment is
delivered in stages across turns — heard, precedent recalled, finding
stated, and only under further pressing what the finding leaves open —
stated outright as "You do not deliver a full judgment at once."

That means a native turn carries **one stage**, not the whole judgment.
And it means his 215.9-word mean is not a style running long: it is the
entire staged judgment arriving in a single turn, which his own Section 4
forbids. **The measure defect and the staging defect are one defect**,
which is why the pass treats them together — the craft table states the
staging rule once, the demonstrations carry it, and the ceiling enforces
it.

Re-derived: **typical 115, ceiling 150** (was 120/180, neither ever
derived — 120 was declared provisional, 180 was set deliberately
counter-empirically).

## 3. The dead zone: his ceiling had never fired, once

`RETRY_TRIGGER_MULTIPLES` set IJC at 1.5. Against the old 180 ceiling the
retry trigger sat at **270**. His streaming baseline's max was **269**.

All 8 turns were over the ceiling. All 8 were under the trigger. None
ever regenerated. The dead zone was 90 words wide — the widest in the
fleet — and the ceiling was decorative.

Fixed the way Albina's was at her checkpoint 4 (1.2 → 1.0, which took her
sustained mean to 128 with zero turns over ceiling): **IJC → 1.0**, so
the trigger now sits on the ceiling itself.

## 4. Two system-level findings, both outside this world

### 4a. The grounding anchor was naming modern scholarship as a world's own record — in production

The segment tells the Representative that a derived list is "the
genuinely attributed core of **this world's own** vetted record", but
selected on `attribution_status` alone. That field answers a different
question — is an attribution genuine rather than pseudonymous — and says
nothing about whether a document belongs to the world.

Papnoute's **deployed** prompt named David Brakke's *Athanasius and the
Politics of Asceticism* (Oxford: Clarendon Press, 1995; reissued Johns
Hopkins, 1998), *Demons and the Making of the Monk* (Harvard UP, 2006),
and Samuel Rubenson's *The Letters of St Antony* (Fortress, 1995) — with
publishers and reissue histories — as part of a 4th-century monk's own
record.

149 of 254 renderable source records fleet-wide are modern scholarship.
Only Desert surfaced any, and only because the list truncates at the
first 8 by id — **every other world was spared by sort order, not by the
filter.**

Fixed in the render path: exclude `source_type: S`; exclude
build-authored artifacts via a new `in_world_record: false` (checked
first — excluding S alone would have *promoted* `srcDES025`, this build's
own paraphrase, into Desert's list, a worse leak than the original);
de-duplicate repeated authors; strip markdown asterisks. Desert's
deployed prompt was swapped, one line changed.

### 4b. Albina shipped with no contestation segment — recorded, not fixed

Found while authoring Marius's claim renders. The contestation segment
reads `claim_renders`, so a world with an empty mapping renders
**nothing**. Desert has six renders. **Albina has zero.**

Her checkpoint-4 sustained-disagreement performance therefore came
entirely from her post-history guard and her demonstrations, with the
segment specifically designed to carry "what we hold when pushed, what we
concede" silent throughout.

This does not invalidate her checkpoint — she passed the bar as measured,
and Mark's read of record stands. It does mean her build has a real gap.
**Not fixed here**: authoring her contestation prose is her own
follow-up, not Marius's pass.

I found this because I had written a comment in `craft_ijc.py` asserting
the segment renders from the claim records themselves. That was false,
and checking it is what surfaced the gap.

## 5. What was verified, and how

- **Readability**: prompt FK 6.34 / FRE 74.63; capsule FK 8.42 / FRE
  61.36, `violations: []`. Floors are FK ≤ 10, FRE ≥ 60.
- **Leak gate** (`--data-dir wrs/views/staging`): IJC **0**, down from
  15. Control run against `data/`, which still carried the old text,
  returned 15 — confirming the gate scans these files and the zero is a
  real pass, not a skip.
- **Apparatus sweep**, prompt *and* capsule: `Doc_0N` 0, `Force N` 0,
  `Candidate N` 0, `Strand A/B/C` 0, `Row N` 0, `G0N` 0, section marks 0,
  `Phase-N` 0, double-spaces 0, prompt asterisks 0. The capsule's 64
  asterisks are markdown bold — checked against Albina's capsule, same
  convention, not a leak.
- **Assembly identity**: all six worlds PASS.
- **Demonstrations**: `assert_ready()` passes; selector takes
  ijcdemo005 (required), 007, 006.
- **Measure by construction**: every Marius turn across the four new
  demonstrations is 65–76 words against a 115 typical and 150 ceiling.
  Word counts in the trait notes were hand-counted first and three were
  off by one; corrected to measured values.
- **Indices**: rebuilt from the candidate chunks and asserted to contain
  the rewritten term prose, because `app/rag/retriever.py` calls
  `load_index()` first and only falls back to `index_lexicon()` on
  failure — a stale index survives a records change silently.

## 6. What the checkpoint is waiting on

The harness (`ijc_checkpoint1.py`) is written and preflighted. It passes
every configuration assertion:

```
[cfg] prompt words   = 3714
[cfg] per-world guard export ACTIVE for imperial-juridical-christianity
[cfg] IJC retry trigger 1.0 ACTIVE
[cfg] ceiling 150 ACTIVE (re-derived)
```

and then stops at the first API call with
`authentication_error: invalid x-api-key`.

**The API key is not available in this session.** It was pasted in chat
earlier in the thread and, per standing practice, was never written to
any file — so it did not survive the context boundary. The checkpoint
needs it re-supplied.

It carries forward the two harness bugs already found and fixed at
Albina's checkpoints: the sustained retry helper calls `sdb._stream_turn`
(not the probe module's same-named function with a different return
shape), and verdicts are read from the `challenge_adjudicated` event in
`EVENT_STORE` rather than from `run_repair_intercept()`, which returns
`None` on every stage and reports zero concessions *and* zero holds.

**Nothing about Marius's voice has been measured.** The targets above are
derivation and construction. What he actually does at 115/150 with a 1.0
trigger is exactly what the checkpoint decides, and no swap happens
before it is green and read.

## 7. Next, in order

1. Run `ijc_checkpoint1.py` (probe + sustained halves) once the key is
   available.
2. Mark's ten-question read per R4 — the human-read step that replaced
   the cancelled Objective-3 comparison.
3. Swap on green; extend `assembly_identity.DEPLOYED_WORLDS` to IJC.
4. Albina follow-up: author her contestation renders (§4b).
5. Remaining worlds: Theon (Alexandria), Papnoute (Desert), Chloe (PAHC),
   Yausep (Syriac).
