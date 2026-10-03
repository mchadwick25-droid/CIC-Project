# Q7 — Measurement: the I5 complement sweep, run today, file grain, nine worlds

**Commissioned by Mark, 2026-09-15**, before the design converges, because it
bears on whether Direction E's hard half (or any I5 mechanism beyond report-only)
is worth building at all. This is the measurement both D1 ("Direction E — Confine
the reader," §5) and D2 (Opus, §3/E and §5.7) asked for and neither had run:
*"run the complement sweep today, on the nine worlds, at file grain, and see
whether it finds anything."* This document reports what actually happened when
it was run against the real repo data. It is a measurement, not a ruling — it
answers the open question D1 posed; it does not decide anything about which
direction converges.

## 1. Methodology actually used

**Scope.** The 9 real worlds with a non-null `census_id` in `records/worlds.yaml`:
`alx`, `desert`, `pahc`, `hal`, `syr`, `ijc`, `cappadocian`, `gallic`, `don`.
`fix` (`census_id: null`) is out of scope per the charter.

**Shelf, at file grain.** For each world, `cic/engine/corpus_index.py::files_for_entry(census_id)`
— the exact function the runtime search-scoping tool already uses — reading the
world's own `cic/corpus-map/<census_id>.yaml` bucket and returning the set of
`source_file` values across all `role`s (`tradition`/`context`/`antecedent`/
`transmission`; the charter's shelf is the whole bucket, not just `tradition`
rows). This is a set of filenames under `cic/texts/`, nothing finer — corpus-map
staging rows' `locus` field is free prose today (per D1 §1.1), so there is no
resolvable sub-file grain to sweep at; "file grain" here means literally that.

**Complement, at file grain.** All 55 corpus-map bucket files (`cic/corpus-map/*.yaml`,
excluding `WORKS.yaml`/`AUTHOR-IDS.yaml`/`UNATTRIBUTED.yaml`, which are not
buckets) were read the same way. For a given world, the complement is the union
of every *other* bucket's files, minus that world's own shelf files. This is
wider than "the other 8 built worlds" — it is every one of the 55 census
entries corpus-map currently tracks, which is what "assigned to those
traditions only" means once the library is read as a whole, not just the built
fleet (matching the charter's own framing of confinement at 100+-world scale).

**Prose scored.** Exactly the fields `engine/m1/gates.py::_PERSPECTIVE_FIELDS`
names as what `engine/m2/builders.py::_chunk_text()`/`build_prompt()` turn into
the voice's own speech — `term.plain_meaning`/`quick_meaning`,
`story.tellable_as`/`text`, `ambient.detail`, `doctrinal_witness.text`,
`honest_limit.statement` — plus the `demonstration` record's
`exchange[].text` where `speaker: representative`, which `gate_voice_perspective`
itself scopes to alongside that dict. Pulled from the real, built
`records/<world>/` YAML frontmatter (not `worlds/`, which holds
construction documents, not the compiled records) — 4,524 sentences across the
9 worlds (`engine.prose.quote_aware_sentences`, the same splitter
`grounding_net.py` uses).

**The matching logic — reused unmodified, both instruments `grounding_net.py`
actually contains:**

1. **`grounding_ratio`/`content_words`** (`engine/prose.py`, imported by
   `grounding_net.py` unchanged) — for every sentence, `content_words(sentence)`
   scored against `content_words` of the *whole* shelf-file-set text and,
   separately, the *whole* complement-file-set text (file text pulled via
   `cic/engine/corpus_index.py::passage_units()`, the same tag-stripped
   extraction the real FTS index uses — not a re-implementation).
2. **The verbatim window-match** — `grounding_net.py::_span_in_records`'s exact
   shape (`_normalize`, imported directly from `engine.m4.grounding_net`; 6-word
   sliding windows), applied against a combined, `\x00`-separated haystack of
   the shelf's/complement's own file text, instead of a tagged record's text.
   Run on (a) every quoted span inside a perspective field
   (`grounding_net.py::_quoted_spans`, imported directly — the literal
   population this instrument exists to check) and (b) the ratio pass's own
   highest-margin candidates (below).

**Sampling and why.** A full sentence-by-sentence verbatim sweep does not
finish in reasonable time: measured directly, one combined-haystack search
over a world's complement (~90 files, up to 114MB of normalized text) takes
~30ms, and a sentence needs up to ~15 such searches (one per 6-word window);
at 400–1,185 sentences per world that is tens of minutes per world. The ratio
pass ran on **every** sentence (cheap, O(1) set operations once the two word-sets
are built). The verbatim pass ran on **every** quoted span in perspective-field
text (405 spans fleet-wide — small, and the exact case the instrument is built
for) plus, per world, the top-25 highest-margin sentences the ratio pass itself
flagged as grounding better in the complement than in the world's own shelf —
using the coarser, full-coverage instrument to pick candidates for the sharper,
capped one. This is a real limitation: the verbatim check did not run against
every one of the 4,524 sentences, only against 405 quoted spans (all of them)
plus 225 ratio-flagged candidates (621 checked in total) — see §4 for what that
means for the verdict's confidence.

**What was not done.** No new code went into `engine/`, `cic/engine/`, or any
gate. No record, package, or corpus-map file was touched. The one throwaway
script is `/tmp/.../scratchpad/i5_complement_sweep.py` (session-local, not in
the repo).

## 2. Per-world results

| world | shelf files | complement files | shelf files also shared w/ other traditions | sentences scored (ratio) | ratio-flagged "grounds better in complement" | quoted spans checked (verbatim) | verbatim window-match hits (any) | verbatim hits **not** also explainable from own shelf |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| alx | 14 | 95 | 12 | 462 | 72 | 8 | 2 | 0 |
| desert | 13 | 96 | 9 | 454 | 16 | 1 | 5 | 1 |
| pahc | 12 | 97 | 10 | 492 | 45 | 33 | 9 | 0 |
| hal | 7 | 102 | 7 | 503 | 68 | 0 | 1 | 1 |
| syr | 15 | 94 | 12 | 514 | 60 | 1 | 1 | 1 |
| ijc | 19 | 90 | 18 | 473 | 30 | 13 | 9 | 1 |
| cappadocian | 18 | 91 | 11 | 675 | 86 | 7 | 8 | 4 |
| gallic | 9 | 100 | 2 | 766 | 189 | 329 | 69 | 3 |
| don | 21 | 88 | 10 | 1,185 | 79 | 13 | 5 | 2 |
| **total** | | | | **4,524** | **645** | **405** | **109** | **13** |

The rightmost column is the whole ballgame: 13 sentences fleet-wide where the
voice's own wording verbatim-matches *something in the complement* and does
**not** also verbatim-match anywhere in the world's own shelf. Every one of
these 13 was read by hand.

## 3. Two separate findings, not one

**Finding A — the ratio instrument, run this way, does not discriminate.**
Measured directly on `don` (the largest shelf, 21 files): the world's own
shelf's content-word vocabulary is ~394,000 unique word-forms; the complement's
is ~384,000. Mean `grounding_ratio` against the *own* shelf across a 200-
sentence sample was 0.987 (median 1.0); against the *complement*, 0.978
(median 1.0). Both sides are saturated near the ceiling for nearly every
sentence, in every world (`complement_clears_floor` — sentences whose ratio
against the complement alone clears the live net's own `WITHHOLD_FLOOR` of
0.4 — is 452–1,184 out of 454–1,185 sentences per world; effectively all of
them). This is not a bug in the run: at file-grain, whole-bucket-union scoring,
almost any sentence's ordinary-English content words will appear *somewhere*
in a ~90-file, ~300–400k-word corpus of translated patristic prose, on either
side. The 645 "ratio-flagged" rows in the table are sentences where the
complement ratio edged narrowly above the (already near-1.0) own-shelf ratio —
reading the actual flagged sentences and their shared words (e.g. `don`:
"He would say we are being **selective**." flagged because "selective"/"say"
happen to occur, once each, somewhere across a 90-file complement, vs. not at
all in the 21-file shelf) confirms this is short-sentence noise, not signal.
This is a sharper, fleet-wide version of the exact concern D2/Opus raised for
the narrower case of byte-identical shared single-unit files (§3/E point 3 of
D2-Struggle.md) — the instrument's own denominator problem, not a defect in
how it was applied here.

A second, related structural fact worth naming: on average, over half of a
world's own shelf files (7 of 7 for `hal`; 18 of 19 for `ijc`; the fleet mean
is roughly 60%) are files *also* claimed by some other tradition's bucket.
"Grounds well in the world's own shelf" and "grounds well in a neighbour's
territory" are frequently checks against the *same physical bytes* — which
further explains why the ratio pass cannot cleanly separate "own" from
"other" at this grain, independent of the vocabulary-saturation problem above.

**Finding B — the verbatim window-match, the sharper instrument, found nothing
real.** All 13 "not explainable from own shelf" hits were read in context
against their source record. Every one falls into one of two buckets:

- **Generic phrase collision.** Short (often ≤6-word) common English strings —
  "of one being" (Trinitarian boilerplate), "seven deadly sins", "abundance of
  power", "In the year 325, the bishops of the whole world gathered at Nicaea"
  (a plain historical fact narrated the same way across any text that mentions
  the council) — that recur, by chance, once each across dozens of unrelated
  19th–20th-century translation volumes covering different subjects entirely.
  Checking the actual matched context (e.g. `don.dw.what-we-did-with-the-
  power-we-had`'s "you would not be able to tell" matches `npnf205`'s "you
  would not be able to **tell me what means you have of arriving at any
  knowledge of** deity" — a different sentence about a different subject that
  happens to share six function-heavy words) confirms coincidence, not
  borrowing.
- **Properly cited, explicitly disclosed paraphrase.** `hal.story.marcella-
  standing`, `gallic.story.honoratus-and-the-island`, `cappadocian.story.
  money-changers-unbegotten`, `desert.story.virgin-who-hid-athanasius` are all
  cited to a source record on the world's *own* shelf (Jerome's letters for
  `hal`; Hilary of Arles's *Vita Honorati* for `gallic`; Gregory of Nyssa for
  `cappadocian`; Palladius's *Paradise* for `desert`), several with the
  record's own `divergence_note` explicitly warning the wording is a
  paraphrase or Inferential-Thin rendering, never to be voiced as a direct
  quote. Their incidental overlap with an unrelated complement file (a
  Chrysostom homily, a Tertullian treatise) is the same generic-vocabulary
  effect as above, landing on records that were already honest about not
  being verbatim.

No hit, inspected, showed a world's own story or doctrinal-witness prose
carrying content that actually originates in — rather than coincidentally
echoes a common phrase from — a neighbouring tradition's exclusive material.

## 4. Answering D1's own question directly

D1 §5/E asked: *"if it finds nothing, that is either reassurance or an inert
instrument, and the difference matters."* The honest answer, from what was
actually run: **both, and they are separable.**

- The **ratio half**, run at file grain against a whole-bucket-union
  complement, is close to an inert instrument on this fleet — it clears the
  live net's own grounding floor for nearly every sentence in both directions,
  so a "clean" result from ratio alone would not have been reassurance; it
  would have been the instrument having no power to fail.
- The **verbatim window-match half** is not inert — it discriminates (109
  hits out of 621 checks, a real minority, not near-universal saturation),
  and it is a hand-inspectable, low-false-positive check. Applied to every
  quoted span in the fleet plus a targeted sample of the ratio pass's own
  strongest candidates, it found **nothing** that survives inspection as
  genuine cross-tradition influence. That is reassurance, within the bounds
  of what it actually checked (see the coverage caveat in §1 — 621 of 4,524
  sentences got the verbatim check, not all of them; the other 3,903 got only
  the near-inert ratio check, which cannot rule I5 out for them on its own).

## 5. Verdict

**No live evidence was found, today, that I5 (cross-tradition content
leakage) is an active problem in the current 9-world fleet.** Every
verbatim-checkable case of a world's own voice-prose wording coinciding with
material outside its own shelf, across all 9 worlds, resolves either to
common-English-phrase coincidence across a large, stylistically homogeneous
19th–20th-century translation corpus, or to a paraphrase already correctly and
honestly sourced to the world's own shelf. This measurement does not merely
fail to *look* — it looked at all 405 quoted spans in the fleet's voice-prose
and at the 225 sentences per world (aggregate) the broader instrument itself
flagged as most suspicious, and came back clean on all of them.

That said, this is not the same as a clean bill of health for the *mechanism*
question. Two qualifiers, stated plainly rather than shaded either way:

1. The instrument the direction proposed (grounding-ratio at file grain
   against the whole-bucket complement) is, as measured here, too coarse to
   discriminate on this corpus — it is closer to the "inert instrument" branch
   of D1's own question than the "reassurance" branch. Anyone citing "the
   complement sweep found nothing" as support for dropping I5 mechanisms
   entirely should cite the verbatim-match result, not the ratio result — the
   ratio result alone would not have been meaningful evidence either way.
2. Coverage is real but partial: 4,524 sentences were scored by the (weak)
   ratio check; 621 of those also got the (strong) verbatim check. A
   determined or careless leak that used none of a passage's own distinctive
   6-word phrasing, and that never surfaced among the ratio pass's own
   highest-margin candidates, would not have been caught here. That is a
   description of the check's limits, not a hedge on the result it did
   produce.

Put together with the fleet's own numbers: at 9 worlds, run once, by hand,
finding nothing is a real, if bounded, data point in favour of I5 being a
process-held invariant that is in fact holding, not a paper assurance — which
is exactly the kind of evidence D1 and D2 both said was missing before this
ran.
