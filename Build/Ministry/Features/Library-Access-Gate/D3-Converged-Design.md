# Library Access Gate — D3 (convergent): the Compiled Shelf

**FROZEN — Mark, 2026-09-15 ("Freeze it.").** This is the converged design.
A change to anything below is now a **change order**, named and reasoned
(`Decision-Log.md`), never a quiet edit — the same discipline Website V2's
own post-freeze changes followed. D4 (the build, §7) proceeds from here.

**Sandbox artifact, 2026-09-15. Phase: D3, convergent — for Mark's freeze.**
One design, not a menu. It synthesizes D1's five directions, D2's struggle
findings, the two Q7 measurements and the nine Decision-Log rulings (entries
3–13) into a single buildable mechanism. Where it only partially satisfies an
invariant, it says so. Where it extrapolates beyond what D1/D2/the
measurements/the log established, the sentence is marked **[extrapolation]**.
Mark's own word freezes it; this document does not.

**Revision note (2026-09-15).** This is the fixed version, after Opus's
independent freeze check (`Sandbox/D3-Freeze-Check.md`) and Mark's four
rulings on it (Decision-Log entries 15–17). All 16 required fixes (RF-1
through RF-16) are applied below; each is marked inline where it lands.
R-1/R-2/R-3 (one ruling, at three grains) changed the `voicing-pair`
mechanism itself — see §1.4 and §3's new CM-8 — not just a number. R-4
(waiver scope) changed §4.2's enforcement rule for new worlds.

Every file path, function name and number below was read or measured against
the checkout on 2026-09-15. The few numbers measured fresh for this document
(§4.3, §8) are labelled as such and were computed at file grain with the same
`cic/texts/<file>` regex `engine/m1/gates.py` already uses (`_EDITION_PATH`);
they are a superset of D2 §2's quote+story population because they cover
every emic record type that carries `sources[]`.

---

## 1. The converged mechanism: the Compiled Shelf

### 1.1 In one paragraph

A world's shelf is **computed, not stored**: at compile time the compiler
joins `records/worlds/<code>.yaml → census_id → cic/corpus-map/<census_id>.yaml`
(the join `engine/m1/cross_world.py::observe_corpus_map` already makes, using
the real YAML loader `cic/engine/corpus_map.load()` — never `tools/gen_shelf.py`'s
`parse_bucket`, which D2 §1.3(a) showed truncates 30% of rows), and writes the
result into the package as `compiled/shelf.json`, hash-chained like every
other compiled file. Against that shelf a new pure module, `engine/m9/`,
runs a small battery of confinement checks and writes
`validation/confinement-report.json` beside the existing
`validation/gates-report.json`. Three of those checks are what makes this
design different from WO-4 as specified: **(i)** a verbatim quote's `text`
must window-match, byte for byte, inside the world's own shelf files
(Direction B's bet, which Q7 measured at 98.2% on real data); **(ii)** a
source record names its own shelf row by a stable id (`shelf_row`), a
copied string that exists, never a guessed identifier (Direction C's key,
hand-authored rather than synced, so a corpus-map edit never rewrites a
record); **(iii)** voicing permission for material on a non-`tradition` row
is decided by a documented **tradition-pair relationship** in corpus-map
(Q2's rule), not by the row's role tag — and, per Mark's R-1/R-2/R-3 ruling,
a pair relationship only makes voicing *possible*: the specific row still
needs its own explicit tag confirming it was actually part of the documented
exchange, not merely produced by an aware party (§1.4, §3 CM-8). A CI job asserts, for every real
world, that the M1 gate battery and the M9 confinement battery are clean
except for findings named in a waiver list with counts and deadlines (Q3).
The runtime is untouched: no loader refusal, no per-turn role cut — the
package remains the seal exactly as today (I6), and the attestation inside
it is what `engine/m7` can audit offline.

### 1.2 What it draws from each direction, and what it refuses

| direction | taken | refused, and why |
|---|---|---|
| **A** — finish WO-4 | the compile-time location; the seeded-defect admission bar; three named checks at the same `(records, …) -> list[str]` shape | `work_id`/`WORKS.yaml` as the join (D2 §3/A pt 4: a 4-entry hand-maintained file cannot be the fleet's serialization point); the `address` backfill as a prerequisite (5 of 358 records; the byte check reaches I2 without it, §2) |
| **B** — bytes, not pointers | `gate_quote_in_shelf`, reusing `engine/m4/grounding_net._normalize` and the 6-word window unmodified (exactly what Q7-B ran); locus grain once `locus_ids` exist, with no `address` backfill | the **materialized extract store** (D2 §3/B pt 2: 4.1× amplification, ~10 GB at scale, the `INDEX.sqlite` precedent). The shelf text is loaded in memory for the duration of one world's check and discarded — Q7-B's own run needed nothing else. Also refused: B's fail-closed rule on shared single-unit files (blocks `don` and `ijc` outright, D2 §3/B pt 1) — those degrade to file grain with an observation, §2/I2 |
| **C** — derive, don't check | the record carries a key to its bucket row (`shelf_row`), so the package is self-describing about which row each source is | the `sync` that writes derived fields into `records/` (D2 §3/C pt 1: permanent repin churn proportional to corpus-map's edit rate, and no monotonicity to make it safe). Role, confidence and `voice_of` are resolved at compile time into `compiled/shelf.json`, never written into the record |
| **D** — attested package | the compile-time half only: `compiled/shelf.json` with a per-record resolution map (D2 §3/D defence: "close to free and the best audit artifact on this list") | the load-time refusal (D2 §3/D pt 1–2: a second lock on the same door, and a category change to a 20-line function) and the runtime role cut (D2 §3/D pt 4: withholds 11% of grounded emic citations; under Q2 the verdict is a pair judgment, which is not a per-turn decision) |
| **E** — confine the reader | the free half: build briefs and the `cic-build-cycle` skill point sessions at `cic/engine/corpus_index.py --entry <census_id>` (already correct, already scoped); the sharp half of the complement instrument (verbatim window-match of quoted spans against off-shelf files) as a report-only observation | the ledger gate (D2 §3/E pt 1: it forbids the off-shelf read that produced `gallic.source.augustine-letters-221-226-absence`, which Q5 now explicitly licenses at build time); the ratio instrument (Q7-I5: ~0.98 against both shelf and complement, near-inert) |

The two seams D2 §4 flagged are closed rather than papered over:

- **A+B precedence.** There is no pointer gate on quotes to disagree with the
  byte gate. Source records are checked by key (`shelf_row`); quotes are
  checked by bytes; each finding names its own fix. A quote can carry both a
  `shelf-row` finding (its source record names a row not on the shelf) and a
  `verbatim-in-shelf` finding (its bytes are not in the shelf), and both are
  true and independently actionable. Neither depends on an incomplete backfill
  of the other.
- **C+D.** D's runtime half is not built, so nothing needs the role on the
  record at turn time. The attestation is compiled from the resolved rows.

### 1.3 The module: `engine/m9/`

House style, read from `engine/m2` and `engine/m6`: a pure function with no
filesystem I/O that a determinism check can call twice in memory; a thin CLI
that does the disk, git and wall-clock work; a mirrored `tests/`; a CI job that
runs `check` and returns non-zero. Concretely:

```
engine/m9/
  __init__.py
  shelf.py         build_shelf(bucket_rows, pairs, parties, units_by_file) -> Shelf     # pure
  confinement.py   CHECKS = {name: fn}; run_all(records, shelf) -> dict[str, list[str]]  # pure
  loader.py        the ONLY place that touches cic/corpus-map/ and cic/texts/ (strict; raises)
  enforce.py       ACCEPTED_OPEN waivers (Q3) + GRANDFATHERED_WORLDS; evaluate(reports) -> exit code
  selftest.py      mirrors engine/m1/selftest.py over fixtures/seeded_defects.yaml `layer: M9`
  cli.py           report <world> | check | shelf <world> [--stdout] | selftest
  reports/         selftest-report.json, confinement-report.json (committed evidence, as m1/m2 do)
  tests/
```

`loader.py` lifts the import pattern `cross_world.py:940` already uses
(`sys.path.insert(... cic/engine); from corpus_map import load`) **without**
the `try/except` that lets the observer swallow failure — a gate cannot
(D2 §1.3(b)). It reads bucket rows with `corpus_map.load()`, pair rulings
from `cic/corpus-map/PAIRS.yaml` (§3), and passage units with
`corpus_index.passage_units()` (the same extractor Q7-B and Q7-I5 both reused).
Nothing in `engine/m9/` imports `engine/m1/gates.py`'s internals or is
imported by it; `gates.py` keeps its "imports nothing from `cic/engine/`"
convention intact.

The `Shelf` value is:

```
Shelf
  world_key, census_id
  rows: {row_id: {source_file, work, author, role, confidence, locus, locus_ids|None, voice_of|None, documented_exchange|None}}
  # documented_exchange added here on build (increment 3): CM-8 (Mark's
  # R-1/R-2/R-3 ruling) landed in SS1.4's voicing-pair check and SS3's CM-8
  # dependency spec during the RF-fix pass, but this literal field listing
  # was missed then - a mechanical gap, not a design change; the field's
  # existence and meaning were already decided everywhere else in this
  # document.
  files: {source_file: [row_id, ...]}
  units: {source_file: [{locus, text_normalized}, ...]}     # in memory only, never serialized
  pairs: {frozenset({a, b}): {relation, direction|None, confidence}}
  parties: {slug: {kind, evidence}}
```

`compiled/shelf.json` serializes everything except `units` (the text never
travels in the package — the package must stay a projection of `records/`,
not a copy of the library; D5 ruled out sources inside worlds) plus a
per-record resolution map:

```
resolution:
  <source record id>: {row_id, role, confidence, voice_of, kind}
  <citable record id>: {sources: [{source_id, row_id|null, role|null, voiceable: true|false|null, reason}]}
```

### 1.4 The confinement battery (`engine/m9/confinement.py`)

Each check is `(records, shelf) -> list[str]`, admitted only with a seeded
defect in `fixtures/seeded_defects.yaml` and selftest proof, the same bar
`engine/m1/gates_experimental.py`'s docstring states. Names below are the
`gate:` ids the catalog will use. "Emic" throughout means `register: emic`;
"citable record" means any record with a non-empty `sources[]`; a `sources[]`
entry whose `source_id` resolves to a record of any type other than `source`
(a story citing a term, 374 such entries fleet-wide today, 373 of them
excluding the one that points at a `search_record` — this rule follows all
374 the same way, the `search_record` case included, **RF-4**) is an
intra-world reference and is **not** followed — that target record is
checked on its own.

| check | what it asserts | invariant | measured day-one findings (§8) |
|---|---|---|---|
| `source-kind` | every `source` record's `kind` (§5) agrees with its `edition`: `vendored` ⇔ `edition` names an existing `cic/texts/` file; `unvendored` ⇔ it names none; `absence` ⇔ it names an existing file and carries `absence_probes`. A missing `kind` is a finding | Q4/Q5 | 398 across the nine worlds (no record carries `kind` yet) |
| `shelf-row` | every `kind: vendored` source record carries `shelf_row`, and it names a row in **this** world's bucket whose `source_file` is the file its `edition` names | I1, work grain | ~283 (every vendored source record; 23 of them will also be genuinely off-shelf per D2 §2) |
| `emic-vendored-only` | no emic citable record's `sources[]` names a `kind: unvendored` or `kind: absence` source record | Q4 | 166 citations across 6 worlds — 152 to `unvendored`, 14 to `gallic`'s two `absence` records (fresh, §8; **RF-2** corrects an earlier 152-only count that omitted the `absence` half of this check's own definition) |
| `absence-probe` | for every `kind: absence` record, none of its `absence_probes` strings window-matches in the named file; the read is logged in the report under `off_shelf_reads` with the record id and file | Q5 | 0 findings; 2 records exercise it (both `gallic`) |
| `verbatim-in-shelf` | every emic quote with `license: verbatim` window-matches inside the world's shelf files, at file grain (any role) | I4 (+I1 for quotes) | 4 of 221 (Q7-B: 3 complement-only, 1 OCR no-match) |
| `voicing-pair` | for every emic citable record, each cited `source` record resolves to a row that is either `role: tradition`, or a non-tradition row that clears **two** gates (Mark's R-1/R-2/R-3 ruling — a pair makes voicing *possible*, not automatic): its `voice_of` forms a pair with this world's `census_id` ruled `mutual-awareness` in `PAIRS.yaml`, **and** the row itself carries `documented_exchange: confirmed` (CM-8, §3) — corpus-map's own judgment that *this specific work*, not merely an aware party's other output, is part of the exchange on record. A source record with no resolvable row at all (`kind: unvendored`, or vendored but off-shelf) is skipped here — it is already caught by `emic-vendored-only` or `shelf-row` respectively, and this check would otherwise double-report the same defect under a second name (**RF-14**). Missing `voice_of`, missing pair, `one-way`, `none`, `needs-ruling`, or `documented_exchange` absent/`not-confirmed`/`needs-ruling` are each a distinct finding text | I3 as re-specified by Q2, and by R-1/R-2/R-3 | file-grain floor 296 citations to `context` (277) and `antecedent` (19) rows; true row-grain count (the grain this check actually runs at) is **296–407**, not a fixed ceiling — see §4.3 (**RF-3**). D2's quote+story subset is 47 |
| `locus-within-work` | **[lands with CM-4, §3]** the passage unit a `verbatim-in-shelf` match landed in has a `locus` inside the `locus_ids` of *some* row on this world's shelf for that file. There is deliberately no single "resolved row" here — §1.2's A+B precedence means the byte check never consults the source record's pointer, so on a file where more than one row shares the same `source_file` (the 16 shared single-unit files above all), this is a weaker claim than "inside the cited row's own locus": it says the byte landed somewhere shelvable, not that it landed inside the specific row the citation names (**RF-5**). On a file whose only unit is `whole-file`, this check emits an observation, not a finding | I2 | not measurable until `locus_ids` exist |
| `shelf-confidence` | no emic citable record resolves to a row with `confidence: needs-ruling` (`provisional` passes and is counted in the report's observations) | the stated decision D1 §4 asked for | not measured; 7 `needs-ruling` rows fleet-wide |

Report-only observations in the same report (never findings, per spec
principle 10 — no baseline has earned them a bar): `complement-verbatim`
(each quoted span in `_PERSPECTIVE_FIELDS` text that window-matches in an
off-shelf file and nowhere on the shelf — the sharp half of Q7-I5's
instrument, which found 13 hits fleet-wide, all coincidence or disclosed
paraphrase); `provisional-rows-cited`; `single-unit-shared-files` (the 16
files D2 §3/B listed, per world). The ratio instrument is not carried
forward at all.

What the compiler does with a finding: **nothing.** It records it. It never
drops a quote from `quotes.json`, never flips a register, never rewrites a
record. The fix is always in `records/` (the world's thread) or in
`cic/corpus-map/` (the classification thread), and the waiver list (§4) is
what keeps `don` shipping while that happens.

---

## 2. How it satisfies each invariant — honestly

**I1 — citation on shelf.** Satisfied at **work grain** for every
`kind: vendored` source record via `shelf_row` → bucket row, and at file grain
for every verbatim emic quote via bytes. Not satisfied for the ~115 unvendored
source records (D2: 117) — corpus-map holds only vendored works, so they have
no row and never will; Q4 resolves that by confining them to the etic layer
rather than pretending they can be shelved. Partially satisfied for
non-verbatim citable records (stories, witnesses, terms): they inherit the
`shelf-row` verdict of the source records they cite, which is work grain, not
passage grain.

**I2 — locus within work.** Satisfied, at *shelf* grain rather than *row*
grain, for verbatim emic quotes once corpus-map supplies `locus_ids` (CM-4):
the byte match already lands in a specific passage unit, so no `address`
backfill is needed to know *where* the quote is — but on a file more than one
row shares, `locus-within-work` confirms the passage is inside some row's
locus on this shelf, not verifiably inside the cited row's own locus
specifically (**RF-5**; §1.4). Until CM-4 lands, I2 is not held by this
design any better than today. Structurally unreachable on the 16 shared
single-unit plain-text files (3.5 MB Gregory of Nyssa, the two Theodosian
Code files, Optatus, the Collatio acts, …) until markers are added to those
files — vendoring work outside this charter; §8 carries it. Not satisfied for
non-verbatim citable records at all: a story's `locus` stays prose.

**I3 — role-gated voicing.** Re-specified by Q2 and satisfied *as
re-specified*: the check is a pair-relationship lookup, not a role→voice
map, and it is exactly the mapping all five D1 directions got wrong (D2 §2,
§5.1). Mark's R-1/R-2/R-3 ruling then sharpened it further: a pair alone is
not enough — the specific row must also carry a corpus-map-judged
`documented_exchange` tag (CM-8), so voicing is never granted to an entire
tradition's output just because *some* of it was part of a live argument.
This is a real, deliberate widening of the corpus-map judgment burden (two
inputs to rule on instead of one), taken because the cheaper version
over-granted voicing — Cyprian for `don`, Dionysius-via-Eusebius for `alx` —
in ways Mark's own wording never intended (§8 documents both cases as
resolved). It is only as good as three corpus-map inputs now — `voice_of`
(CM-2), `PAIRS.yaml` (CM-3), and `documented_exchange` (CM-8) — so on day one
every one of the 296+ emic citations to non-tradition rows is a
`voicing-pair` finding and every one is waived. That is the honest shape: the
gate is real and fires; the classification it depends on does not exist yet,
and per Q1 this workstream does not write it.

**I4 — bytes match.** Satisfied for `license: verbatim` emic quotes (221 of
243 quote records) with `_normalize` and no wider tolerance — D2 §3/B pt 4's
"normalization trap" is a source-fidelity risk and this design does not open
it; the one OCR-defeated quote (`don.quote.emeritus-magno-argumento`) is a
waiver and a re-scan item, not a matcher tolerance. Not satisfied for
`paraphrase-only` quotes (0 today), `modern_rendering`, stories, witnesses,
terms: those are ratio territory and the ratio instrument is inert (Q7-I5).
This is the check the tracking doc believed already existed; it will exist
for roughly a third of voiced material and be asserted for nothing else.

**I5 — influence without citation.** Partially and report-only. The
verbatim complement observation is the sharp half of the only instrument
anyone has run, and Q7-I5 found no live evidence of leakage with it. It is
blind, by construction, on shared single-unit files (the complement is the
same bytes), and it reaches only quoted spans plus whatever a reviewer reads.
The remaining I5 control is process: E's scoped search in the briefs, and
the human review discipline root `CLAUDE.md` already requires. This design
does not claim to gate I5.

**I6 — runtime seal.** Unchanged, by construction: `compile_world` still
reads only `records/`, the registry and (newly) `cic/corpus-map/` and
`cic/texts/` at build time; `run_voice_turn_for_world` still scopes to one
package; `verify_package_dict` stays 20 lines of hashing. The one thing this
design adds to the sealed artifact is the attestation, which makes the seal
*auditable* offline (`engine/m7`) without making it *conditional* on
anything new. D2's warning that Direction D weakens availability is why the
loader is not touched.

---

## 3. The corpus-map dependency (Q1: structure yes, judgment no)

Everything below is a **dependency spec** for `cic/corpus-map/`'s own thread
to pick up as a tracked work order. This workstream builds the readers and
the fixture tolerance (CM-6) and nothing else in this list; it never fills a
field whose value is a classification judgment.

| id | structure needed | judgment involved (corpus-map's) | blocks which check |
|---|---|---|---|
| **CM-1** | a stable, unique `row_id` on every staging row (`_staging/<volume>.yaml`), carried through `corpus_map_merge.py`'s `_KEEP` into the bucket, checked unique by `corpus_map.validate()`. **[extrapolation]** proposed shape: `<file-stem>--<work-slug>`, assigned once by a `corpus_map_merge.py --assign-ids` pass that writes back into staging, never regenerated from a later title edit | none — mechanical; the point is that a later title correction does not move the id (the failure mode D2 §3/A pt 5 named) | `shelf-row`, `voicing-pair`, the attestation |
| **CM-2** | `voice_of: <census-id \| ruled party slug>` on every row whose `role` is not `tradition`: the tradition (or ruled non-tradition party, e.g. the imperial court, a pagan critic) whose own voice the work is. Required by `validate()` on non-tradition rows once the field exists; absent today on all 187 such rows. **Must be added to `corpus_map_merge.py::_KEEP`** (today a fixed tuple, `("work","author","source_file","locus","role","confidence","note")`) or the field is dropped at the next merge (**RF-8**) | per row: whose voice is Optatus (`latin-pastoral-congregational-christianity`, per the staging note already there); whose is Eusebius' HE; whose is the Collatio tribunal | `voicing-pair` |
| **CM-3** | `cic/corpus-map/PAIRS.yaml`: `pairs: [{a, b, relation: mutual-awareness \| one-way \| none, direction: a->b \| b->a (one-way only), evidence, confidence: assigned \| provisional \| needs-ruling}]` plus `parties: {slug: {kind, evidence}}` for non-census parties, the same "a slug is legal because a ruling exists" shape `UNATTRIBUTED.yaml` already uses. **Placement (RF-9):** must be added to **both** non-bucket-file lists — `corpus_map.NON_BUCKET_FILES` and `corpus_map_merge.py`'s own second, hand-synced list (`_NOT_A_BUCKET \| {"UNATTRIBUTED.yaml", "WORKS.yaml", "AUTHOR-IDS.yaml"}`) — or the merge's cleanup pass reports it as an orphan (that script's own comment: keep the two lists in sync by hand). **Provenance (RF-9):** unlike `UNATTRIBUTED.yaml`, which is *generated* by `corpus_map_merge.py` from `authors_ruled:` blocks scoped to one staging volume, a pair ruling isn't naturally scoped to a single volume — this design proposes `PAIRS.yaml` as hand-authored directly at top level, not generated; corpus-map's own thread may choose otherwise | which tradition pairs were in documented argument (Q2's own examples: Donatists ↔ Optatus' Catholics = mutual-awareness; Alexandria ↔ Eusebius' tradition = one-way) | `voicing-pair` |
| **CM-4** | `locus_ids: [<passage-unit locus>, ...]` on every row, resolvable against `corpus_index.passage_units()`'s `locus` values (the file's own `div` id, or `whole-file`); `validate()` checks each id exists in the named file. Also needs `_KEEP` (**RF-8**, same gap as CM-2). D1 §1.1's rough count: ~470 rows already name a `divN` path in prose, ~17 say whole volume, ~50 other prose | mostly mechanical transcription of what `locus` prose already says; a real judgment only where the prose is vague | `locus-within-work` (I2) |
| **CM-5** | no new structure — **rows that are missing.** Q7-B's 3 complement-only quotes (`hal`→npnf211, `syr`→Palladius, `syr`→npnf203), D2's 23 off-shelf source records and 3 files in no bucket, and the file-grain off-shelf citations measured fresh (§8: `gallic` cites npnf203 **56** times, across 55 records, and it is not in `gallic`'s bucket — **RF-4** corrects an earlier 52) | every one is a "does this work belong to this tradition, and in what role" ruling | `shelf-row`, `verbatim-in-shelf` |
| **CM-6** | `corpus_map.validate()` tolerates a bucket carrying `fixture: true`: it skips the census-movement-id and known-author checks for that bucket only, and applies every other rule. `PAIRS.yaml` entries and `parties` may likewise carry `fixture: true` | none — Q8 put this in scope here; this workstream builds it | the M9 selftest |
| **CM-7** | no new structure — a *rare, stronger* re-rowing corpus-map may choose: giving an embedded own-voice work its own `tradition` row entirely (rather than tagging the existing row via CM-8). `corpus_map.py`'s docstring currently declines to encode "attested-by" as a row; whether that stands is corpus-map's call. Since R-1/R-2/R-3 (below), CM-8 is the expected mechanism for most cases; CM-7 stays available for the rarer case where a work deserves its own tradition row outright, not just an exchange tag | entirely judgment | changes which `voicing-pair` findings exist |
| **CM-8** | **[new, from Mark's R-1/R-2/R-3 ruling]** `documented_exchange: confirmed \| not-confirmed \| needs-ruling` on every non-`tradition` row whose pair (CM-3) is already `mutual-awareness`. Meaningless, and left unset, on rows whose pair is `one-way` or `none`. Also needs `_KEEP` (RF-8) | per row, only where the pair already qualifies: was *this specific work* actually part of the documented exchange, or merely produced by a party who happened to be aware of the other tradition? Resolves both cases D3 originally left open: Cyprian (`antecedent` for `don`) gets no automatic tag — he predates the schism by decades, so no exchange to confirm, even though his `voice_of` pair (`don` ↔ the wider Carthage/Hippo tradition) is itself `mutual-awareness`; Dionysius-via-Eusebius stays untagged for `alx` unless corpus-map finds a specific documented exchange to confirm, which is a lower bar than CM-7's full re-rowing | `voicing-pair` |

The first `python -m engine.m9.cli report <world>` run on each of the nine
worlds emits, as part of its findings text, the exact worklist for CM-2, CM-3,
CM-5 and CM-8: every non-tradition row an emic record cites (needs
`voice_of`), every `(census_id, voice_of)` pair the fleet needs a ruling on,
every pair already ruled `mutual-awareness` whose rows still need a
`documented_exchange` call, every file a world cites that its bucket lacks.
That list, not this document, is the hand-off to corpus-map's thread — and it
is regenerated on every run, so it cannot go stale.

---

## 4. Enforcement and rollout (Q3)

### 4.1 Where the gate lives, argued from the invariants

I1–I4 are properties of *records against the library*; they are decidable
the moment a record is written and do not change at runtime. That is compile
time, and it is where D5 put WO-4. I6 is held by the package hash and the
loader and needs nothing added. I5 is not decidable mechanically and stays a
report. So: **compile time computes; CI asserts; the loader is untouched.**

D2 §1.3(e) is the finding that reshapes this section: today no gate blocks
anything. `validation.build_gates_report` writes `overall_pass` into the
package and `cmd_build` never reads it; `restore` verifies bytes, so a package
pinned with failing gates restores green forever; `don` ships with 52
`reciprocity` findings and `syr` with 1 `voice-perspective` finding, CI green.
Adding checks alone would only change report bytes, stale the packages, get
repinned, and ship — findings and all.

### 4.2 The assertion: `engine/m9/enforce.py` and the CI job

A new CI job, `m9-confinement-check`, runs on every engine or library path
change (§6.3) and does three things, in order:

1. `python -m pytest engine/m9/tests -q` (unit tests, the selftest, the
   waiver-hygiene tests below);
2. `python -m engine.m9.cli check` — for every registry world whose `state`
   is in `{built, admitted, open}` (the same set `staleness_sweep` already
   uses), run `engine.m1.gates.run_all` **and** `engine.m9.confinement.run_all`
   from records on disk (no `restore` step needed — same reasoning as the
   staleness job), then evaluate every finding against `ACCEPTED_OPEN`;
3. exit 1 on any un-waived finding, any stale waiver, any expired waiver, or
   any waiver naming a world that is not grandfathered.

`ACCEPTED_OPEN` follows the *spirit* of `engine/m1/cross_world.py`'s existing
waiver dict — a dict in code, each entry owned by a named finding and thread —
but is not that same registry, and does not claim to be (**RF-10**): it lives
in `engine/m9/enforce.py`, keyed `<layer>:<check>/<world>` rather than
`<check>/<world>` (so an M1 finding and an M9 finding on the same world never
collide), and its values are a `Waiver` object (count, deadline, owner)
rather than a bare string, because Q3 needs count-exactness and dated expiry
the existing registry doesn't carry. This makes two `ACCEPTED_OPEN` lists in
two modules; the relationship, stated rather than assumed: `engine/m9/enforce.py`'s
list is authoritative for everything M9's `check` command evaluates — every
`m9:` key, plus the two live M1 findings it re-hosts below so CI's blocking
step has one list to read — while `cross_world.py`'s own list stays
authoritative for the cross-world findings M9 never touches (e.g.
`census-display-name/alx`). An unlisted defect is new drift against whichever
list actually owns its check, never both and never neither:

```python
ACCEPTED_OPEN: dict[str, Waiver] = {
    "m1:reciprocity/don":        Waiver(count=52, deadline="YYYY-MM-DD", owner="… the finding and thread that own it"),
    "m1:voice-perspective/syr":  Waiver(count=1,  deadline="YYYY-MM-DD", owner="…"),
    "m9:voicing-pair/don":       Waiver(count=192, deadline="YYYY-MM-DD", owner="CM-2/CM-3 (corpus-map); don thread"),
    ...
}
GRANDFATHERED_WORLDS = frozenset({"alx", "cappadocian", "desert", "don", "gallic", "hal", "ijc", "pahc", "syr"})
```

Rules, each with a test in `engine/m9/tests/test_enforce.py` in the same
spirit as `test_cross_world.py`'s two hygiene tests:

- **Unlisted finding → red.** New drift fails the run (root `CLAUDE.md`).
- **Count is exact.** The report's count for that key must equal `count`.
  Fewer means a repair landed and the waiver was not lowered — stale, red
  ("a stale waiver for something already fixed also fails — remove it").
  More means new drift under an old excuse — red.
- **Deadline passed → red.** The waiver stops suppressing. A deadline is a
  date, not a comment.
- **Grandfathering is closed.** A waiver key whose world is not in
  `GRANDFATHERED_WORLDS` fails the hygiene test. That is what "new worlds must
  pass clean before admission" means mechanically: the tenth world can never
  be added to the waiver list, so it cannot reach `state: built` in CI with a
  single un-waived finding. `GRANDFATHERED_WORLDS` is the nine worlds with a
  real `census_id` on the day increment 4 (§7) lands, and it only ever shrinks.
  **Stated consequence (RF-7):** as written, this makes every check
  un-waivable for a new world — including `voicing-pair`, which cannot be
  cleared by any world's own thread until CM-2/CM-3 land (§3). Taken literally,
  no tenth world can reach `admitted` until corpus-map's own thread finishes
  that work, which this workstream does not control.
- **New-world carve-out for `voicing-pair` only (Mark's R-4 ruling, "stage
  the closure").** Every other check stays fully un-waivable for a new world
  from day one, exactly as above. `voicing-pair` is the one exception, because
  it is the one check with a real external dependency this workstream cannot
  finish itself: `evaluate()` checks whether `PAIRS.yaml` contains any
  non-`fixture` entry yet. While it has none, a new (non-grandfathered)
  world's `voicing-pair` findings are demoted to report-only observations
  instead of failing the run; every other check on that world still blocks
  normally. The day corpus-map lands its first real pair, the carve-out ends
  on its own — no manual toggle, no code change, nothing to remember to flip
  back. Grandfathered worlds are unaffected either way: their `voicing-pair`
  findings are already governed by the normal waiver mechanism above.
- **Fixture is exempt from waivers and never grandfathered**: `fix` must be
  clean by construction (it is the selftest's own baseline).

`deadline` values are Mark's to set at freeze, per world, with the owning
thread. **[extrapolation]** Recommended default: 90 days from the landing of
increment 4 for record-side classes (`source-kind`, `shelf-row`,
`emic-vendored-only`), because those are per-world thread work with no
external dependency; and "30 days after CM-2/CM-3 land" for `voicing-pair`,
because no world thread can clear those before corpus-map rules. A deadline
that the enforcing thread cannot meet on its own is not a deadline.

### 4.3 What the waiver list looks like on day one

Counts measured fresh for this document, file grain, every emic record type,
`fix` excluded (they are the ceilings increment 4 will need; the exact values
come from the first real run, not from here):

| class | alx | cappadocian | desert | don | gallic | hal | ijc | pahc | syr |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `m9:source-kind` (no `kind` yet) | 25 | 111 | 29 | 76 | 36 | 28 | 30 | 23 | 40 |
| `m9:emic-vendored-only` (emic citations to `unvendored` **or `absence`** sources — **RF-2**, corrects an earlier count that omitted the `absence` half) | 0 | 62 | 20 | 20 | **24** | 0 | 2 | 0 | 38 |
| `m9:voicing-pair` (emic citations to `context`/`antecedent` rows, **file grain — a floor, not a ceiling; RF-3**) | 37 | 8 | 4 | 173+19 | 0 | 0 | 13 | 13 | 29 |
| `m9:off-shelf-citation` — emic citations to files absent from this world's own bucket, file grain (**renamed from an earlier `m9:shelf-row` label that conflated this with the structural finding below — RF-1**) | 8 | 6 | 0 | 2 | 56 | 10 | 18 | 0 | 16 |
| `m9:verbatim-in-shelf` (Q7-B) | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 2 |
| `m1:reciprocity` / `m1:voice-perspective` (D2) | | | | 52 | | | | | 1 |

**`m9:shelf-row`** — a distinct class from `off-shelf-citation` above (**RF-1**):
every `kind: vendored` source record before it carries `shelf_row`, which day
one is *all* of them, since the field is new. Fleet total **~283**; the
per-world split is not measured for this document — it comes from the first
real `m9 report` run, not invented here.

Three things this table says plainly, after the fixes. First,
`emic-vendored-only` is the largest *record-side* class and it is not a
design choice — it is Q4 applied: **166** emic citations today ground a
voice record in a source the library does not hold or explicitly does not
contain (152 `unvendored` + 14 `gallic` `absence` citations — the 14 are not
a rounding error, they come from 12 real `gallic` formation records:
`gallic.gravity.named-example`, `gallic.gravity.interior-road`,
`gallic.figure.cassian`, `gallic.story.germanus-scruple-at-morning-service`,
`gallic.term.virgin-virginity`, `gallic.term.perfection`,
`gallic.term.illusion`, `gallic.term.purity-of-heart`,
`gallic.force.transmission`, `gallic.force.contest-over-antiquity`,
`gallic.force.transmission-in-ending`,
`gallic.force.africa-and-rome-pressure` — gravities and forces, the world's
formation spine, not its footnotes). Each fix is either dropping the citation
where the record is also grounded in vendored material, or re-registering the
record etic — build-thread judgment. Second, `voicing-pair`'s 296 is measured
at file grain, but the check itself resolves a *specific* row via
`shelf_row` — 111 further emic citations (alx 4, cappadocian 14, desert 19,
don 6, hal 21, ijc 34, pahc 3, syr 10) sit on files carrying **both** a
`tradition` row and a non-tradition row, and become a `voicing-pair` finding
if their `shelf_row` names the non-tradition one. The true day-one count is
somewhere in **296–407**; increment 4 seeds each waiver's `count` from the
first real row-grain run, not from this table (**RF-3**). Third,
`voicing-pair` is `don`'s whole documentary base (192 of 296) and cannot be
cleared by `don`'s thread at all until CM-2/CM-3/CM-8 land; its waiver is
honest about that in its `owner` text, and per R-4 above it does not block a
*new* world's admission either, while it doesn't block `don`'s.

### 4.4 Admission

`state: admitted` is a registry commit (Artifact-1 §2). This design adds no
new state machine; it makes the existing CI job red for any non-grandfathered
world with findings at `built` or later (subject to R-4's `voicing-pair`
carve-out above), so a world cannot sit at `built` long enough to be admitted
unless it is clean. The M3 admission harness (`engine/m3`) is not touched —
but not for the reason a quick read suggests (**RF-11**). M3 does not read
`validation/gates-report.json` at all: `engine/m2/validation.py::build_admission_results`
writes `status: "not_yet_run"` into every package, and M2 is deliberately
barred from importing M3; M3's own `overall_pass` comes from its own probe
battery, written to `validation/admission/results.json`. M9 follows the same
separation — `confinement-report.json` sits beside `gates-report.json` as a
sibling M3 doesn't read either, not as a file M3 already tolerantly ignores.

### 4.5 What is *not* enforced, stated so nobody assumes it

Findings do not stop `python -m engine.m2.cli build`; a thread can still
compile a red world locally to see its report. Findings do not stop
`restore` or the Docker image. Findings never reach a participant: the
compiler records, the runtime ignores.

---

## 5. Schema changes (`engine/m1/schemas.py`, plus one bucket-side schema)

All additive; every existing record validates unchanged until a check (not
the schema) asks for the field, the same split `schemas.py`'s own header
states ("requiredness beyond the floor is the field-completion gate's job").

**`TYPE_PROPERTIES["source"]`** gains:

```python
# Q4/Q5 (Decision-Log 6, 7). What this record's subject IS in relation to the
# library. Checked for agreement with `edition` by engine/m9's source-kind.
"kind": {"enum": ["vendored", "unvendored", "absence"]},
# Q5. For kind: absence only - strings that must NOT window-match in the file
# `edition` names. The compiler reads that (possibly off-shelf) file to verify,
# and logs the read; the Representative never sees it. Necessary, not
# sufficient: absence of a heading string is evidence the claim was checked,
# not proof of the claim.
"absence_probes": {"type": "array", "items": {"type": "string"}, "minItems": 1},
# CM-1 (this workstream, Decision-Log 3). The bucket row this source IS,
# copied from cic/corpus-map/<census_id>.yaml's own row_id - a string that
# exists, never guessed. Resolved (role, confidence, voice_of) at compile
# time into compiled/shelf.json; nothing derived is ever written here.
"shelf_row": {"type": "string"},
```

`COMPLETION_REQUIRED["source"]` is **not** changed: making `kind` required
there would fail every existing source record (398 across the nine worlds,
400 with the fixture's two) at the schema layer on day one, which is the
same finding `source-kind` already reports with a waiver and a deadline. New
worlds' source records are born with all three fields because `source-kind`
and `shelf-row` fire on them un-waivable.

**Envelope** — no change. `register` already carries the emic/etic
distinction Q4 extends; `sources[].address` stays optional and untouched
(the byte check reaches I2 without it).

**Bucket-side** (`cic/corpus-map/`, built by corpus-map's thread per §3, read
by `engine/m9/loader.py`): `row_id`, `voice_of`, `locus_ids`,
`documented_exchange` (CM-8, Mark's R-1/R-2/R-3 ruling) on rows; `PAIRS.yaml`;
`fixture: true` tolerance in `validate()`.

**Absence records, the whole rule in one place.** `kind: absence` ⇒
`register: etic` (an absence grounds nothing voiceable); `edition` names an
existing `cic/texts/` file which **may be off this world's shelf**;
`absence_probes` is non-empty; `sources: []`; no `shelf_row` (there is no
row — D2 §3/C showed no derived field can exist for a row that does not);
`rights_status`/`attribution_status` may say "not applicable" as
`gallic.source.augustine-letters-221-226-absence` already does. Both gallic
absence records (`augustine-letters-221-226-absence`,
`cassian-conferences-xii-xxii-absence`) become conformant by adding `kind`
and probes; the mechanical check they gain is that the letters/conferences
they say are missing are in fact not in the file. An emic record citing an
absence record is an `emic-vendored-only` finding.

**`kind: unvendored`, the rule in one place.** ⇒ `register: etic`; no
`shelf_row`; may be cited by etic records only. Today 115 source records name
no vendored file and only 2 of them are emic (`desert` 1, `ijc` 1), so the
register flip is tiny; the register-flip rule here goes one step beyond what
entry 6 itself said — entry 6 governs which *citing* record may reference
unvendored material, not the register of the source record carrying the
citation. Cheap (2 records) and a defensible reading, but it is an addition;
flagged for Mark to confirm at freeze rather than treat as inherited
(**RF-16**). The 152 emic *citations* to `unvendored` sources, plus 14 more to
`gallic`'s `absence` records (166 total), are the real cost (§4.3, **RF-2**).

---

## 6. The fixture and the CI wiring

### 6.1 The fixture world (Q8, in scope here)

`fix` is the one world the selftest runs against, and every M9 check must
fire on a mutation of it and stay silent on the clean copy (`engine/m1/selftest.py:73`'s
inertness rule, mirrored). Today `fix.census_id` is `null` and its two source
records cite "Fixture Edition 1", no file. The fixture gains, in one PR:

- `records/worlds/fix.yaml`: `census_id: "fixture-synthetic"`. `census_sync`
  skips ids not in the census (`census_sync.py:76`); `check_census_link` runs
  on formation worlds only; nothing else reads it.
- `cic/corpus-map/fixture-synthetic.yaml` with `fixture: true` (CM-6) and two
  rows: the witness scroll (`role: tradition`) and the later summary
  (`role: context`, `voice_of: fixture-synthetic-neighbour`,
  `documented_exchange: confirmed` — CM-8, so the selftest's clean baseline
  actually exercises a *voiceable* non-tradition row, not just an unvoiceable
  one), each with `row_id` and `locus_ids: [whole-file]`.
- `cic/corpus-map/PAIRS.yaml` gains `{a: fixture-synthetic, b: fixture-synthetic-neighbour, relation: mutual-awareness, fixture: true, …}`
  and a `parties` entry for the neighbour, `fixture: true`. A seeded defect
  (below) flips the later summary's `documented_exchange` to `not-confirmed`
  to prove the negative case fires too — otherwise CM-8 would only ever be
  tested in the direction that passes.
- `cic/texts/fixture-synthetic_witness-scroll.txt` and
  `cic/texts/fixture-synthetic_later-summary.txt`: short, plainly synthetic,
  each with a provenance header declaring it authored for the fixture and
  public domain (CC0), containing the exact `text` of the fixture's verbatim
  quotes. `gate_edition_rights_consistency` reads the licence line, so the
  header must carry one it accepts. The generated `cic/texts/README.md` /
  `AUTHORS.md` will list them — a known, accepted trace, to be stated in
  each file's header rather than hidden. **[extrapolation]** This follows
  Decision-Log entry 10's wording ("a vendored fixture text") literally; if
  Mark prefers the synthetic texts rooted under `fixtures/` instead, the
  only change is a second texts root in `engine/m9/loader.py` keyed on
  `registry[world].kind == "fixture"`, and nothing in `cic/texts/` changes.
- `records/fix/source/fix.source.witness-scroll.md` and
  `fix.source.secondary-summary.md` rewritten: `edition` names the vendored
  fixture file, `kind: vendored`, `shelf_row` set. A third fixture source,
  `fix.source.lost-letters-absence.md` (`kind: absence`, probes naming
  letters the scroll does not contain — the same lost letters
  `fix.search.lost-letters-search` already searched for), gives
  `absence-probe` a real positive case.
- `fixtures/seeded_defects.yaml` gains one `layer: M9` entry per check, and
  the catalog's mutation vocabulary gains `target_kind: record | bucket | pairs`
  so a defect can flip the fixture pair to `one-way`, delete a row's
  `voice_of`, or point `shelf_row` at a row the bucket does not hold —
  applied to in-memory copies by `engine/m9/selftest.py`, never to files.
- The fixture package is rebuilt and repinned (its hash moves — the two
  rewritten source records are copied byte-for-byte into it).

### 6.2 The compiler integration (change orders, named)

`compile_world` gains two outputs — `compiled/shelf.json` and
`validation/confinement-report.json` — and one input: it now reads
`cic/corpus-map/` and `cic/texts/` through `engine/m9/loader.py`. Three
existing decisions are touched and each is a **change order, not a quiet
edit**:

1. `engine/m2/compiler.py`'s docstring names five determinism inputs;
   corpus-map and texts content join them. `records_commit` already names a
   commit of the whole repository, so provenance is still truthful; the
   check itself (`determinism_twice`, same disk twice) is unaffected. The
   docstring and `engine/m2/tests/test_compiler.py`'s determinism test
   description are amended.
2. `cic/engine/corpus_map.py`'s docstring says the map is "touched by
   nothing in the compile path" and "INTEGRATION IS DELIBERATELY NOT DESIGNED
   HERE." This design is that integration; the docstring is amended to name
   `engine/m9` as the reader.
3. `engine/Dockerfile` deliberately excludes `cic/corpus-map/` and
   `cic/engine/`. `restore` runs inside the image build and will now need
   both (`corpus_map.load`, `corpus_index.passage_units`), so the image adds
   `COPY cic/corpus-map/ cic/corpus-map/` and `COPY cic/engine/ cic/engine/`
   (small: YAML and Python; the 250 MB of texts is already copied). The
   Dockerfile comment is rewritten to say why.
4. **(RF-13)** `fixtures/seeded_defects.yaml`'s own header calls its mutation
   vocabulary (`set_field`/`delete_field`/`add_field`/`remove_record`) "small,
   closed." M9's selftest needs `target_kind: record | bucket | pairs` to
   mutate corpus-map/pairs fixtures in memory (§6.1) — a real extension to a
   vocabulary that file declares closed, named here rather than added quietly.

Consequence D2 §1.3(c) named and Q6 accepted: every corpus-map merge that
changes a shelf stales that world's package. That is now *wanted* — it is
how a classification edit reaches the sealed artifact — and §6.3's auto-repin
is what makes it survivable. Increment ordering in §7 puts the auto-repin
**before** the integration for exactly this reason.

### 6.3 CI (`.github/workflows/ci.yml`)

Mirroring `m2-staleness-check` / `m6-census-sync-check`'s shape:

```yaml
  m9-confinement-check:
    needs: changes
    if: needs.changes.outputs.engine == 'true' || needs.changes.outputs.library == 'true'
    name: M9 confinement (compiled shelf; M1+M9 findings vs waivers)
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: {python-version: "3.11", cache: pip, cache-dependency-path: engine/m1/requirements.txt}
      - run: pip install -r engine/m1/requirements.txt
      - run: python -m pytest engine/m9/tests -q
      - run: python -m engine.m9.cli check
```

A new `library` group in the `changes` filter — `cic/corpus-map/**`,
`cic/texts/**`, `.github/workflows/**` — runs **only** this job and
`m2-staleness-check`, not the full twelve-job engine battery (D2 §3/B pt 3's
budget warning; the 2026-09-10 minutes exhaustion is the precedent).
`m2-staleness-check` also gains `|| needs.changes.outputs.library == 'true'`.
**(RF-12)** the `changes` job's own `outputs:` block needs a `library:` line
added alongside `engine`/`frontend`/`census` — the filter group alone isn't
enough; nothing downstream can read `needs.changes.outputs.library` without it.

**The auto-repin (Q6b).** A second workflow (or job), `repin-on-library-change`,
runs on `push` to `main` when the `library` filter matches: `staleness-check`;
for each stale world, `python -m engine.m2.cli build <world>`, `git rm` the
manifest the pin left behind, update `records/worlds/<code>.yaml`'s
`manifest_hash`/`location`, and open one PR per world on a `repin/<code>`
branch. One PR per world is what the registry split buys: two repin PRs
never touch the same file, and an active world branch conflicts with at most
its own repin. **[extrapolation]** Build-time facts to verify, not assumed:
a PR opened with the default `GITHUB_TOKEN` does not itself trigger the
`pull_request` workflow, so these PRs need a token that does (a PAT or GitHub
App), or they can never earn the 11-of-11 checks branch protection requires;
and the job needs `contents: write` + `pull-requests: write`.

### 6.4 The registry split (Q6a)

`records/worlds.yaml` becomes `records/worlds/<code>.yaml`, one entry per
file, same shape per world. `engine/m1/registry.py::load_registry` stays the
single reader (spec principle 4) and globs the directory; every engine caller
already goes through it. The direct readers that do not — `engine/api/config.py`'s
`CIC_API_WORLDS_YAML` (becomes a directory), `engine/api/dev_server.py:113`,
the `WORLDS_YAML` constants in the by-hand evidence scripts
(`engine/m4/lazy_load_measure.py`, `live_table_run.py`, `live_turn_run.py`,
`live_table_battery.py`, `engine/m3/live_admission_run.py`,
`engine/m8/live_cost_run.py`, `live_memory_growth_run.py`), the
`engine/api/README.md` line documenting the env var, and **two more found on
independent recheck (RF-12): `engine/api/tests/conftest.py:88` and
`engine/m4/tests/test_world_loader.py:14`**, both of which `yaml.safe_load`
the path directly and would break on this increment — are repointed in the
same PR (`render.yaml` and `wrangler.jsonc` do not name the path; checked).
Package bytes do not change (the registry entry's *content* is what
`build_capsule`/`build_frame_json` read), so no repin. `tools/gen_shelf.py`'s
own line-regex registry reader is retired with the tool (§7, increment 9).

---

## 7. Build increments (D4) — one focused PR each, in this order

Sequencing dependencies are stated; nothing here waits on anything not
named. Model routing per the workstream README: Sonnet carries these;
mechanical migrations go to Haiku.

| # | PR | depends on | what lands | hash/repin effect |
|---|---|---|---|---|
| 1 | **Registry split** (Q6a) | — | `records/worlds/<code>.yaml`; `load_registry` globs; direct readers repointed; tests | none |
| 2 | **Schema + fixture** (Q8, §5, §6.1) | 1 | `kind`, `absence_probes`, `shelf_row` in `schemas.py`; `fix` census id, bucket, two texts, three rewritten/added source records; `validate()` fixture tolerance (CM-6); `PAIRS.yaml` skeleton with the fixture pair only | `fix` repinned |
| 3 | **`engine/m9` core** | 2 | `shelf.py`, `confinement.py` (the battery of §1.4 minus `locus-within-work`), `loader.py`, `cli.py report/shelf`, `selftest.py`, `layer: M9` seeded defects, tests; `m9-confinement-check` job in **report mode** (runs tests + selftest; `check` not yet wired) | none (nothing in the compile path yet) |
| 4 | **Enforcement** (Q3) | 3 | `enforce.py` with `ACCEPTED_OPEN` populated from the first real run, `GRANDFATHERED_WORLDS`, deadlines as Mark sets them; hygiene tests; `cli check`; job flips to blocking. Mark reads the waiver list before merge — it is the grandfathering record | none |
| 5 | **Auto-repin + library filter** (Q6b, §6.3) | 1 | `library` path group; `repin-on-library-change`; token/permissions verified live once | none |
| 6 | **Compiler integration** (§6.2) | 3, 5 | `compiled/shelf.json`, `validation/confinement-report.json`; the three change orders; `package_schema` stays 1 (additive files) **[extrapolation: if the M4 loader or M7 needs to distinguish, bump to 2 here]** | all nine repinned — the first exercise of increment 5 |
| 7 | **Fleet record migration**, one PR per world, Haiku | 2 (**and CM-1 for the `shelf_row` half specifically — RF-6**) | `kind` on every source record (mechanical from `edition`, proceeds without CM-1); `shelf_row` where the row exists (copied, never guessed — **blocked until CM-1 lands**; there is no `row_id` to copy before then, and the no-guessing rule forbids inventing one); the 2 unvendored emic source records flipped etic; `absence_probes` on gallic's two absence records; waiver counts lowered as each lands | that world repinned |
| 8 | **Locus grain** (I2) | 3, CM-4 | `locus-within-work` check; `single-unit-shared-files` observation; seeded defect; `verbatim-in-shelf` reports the unit it matched in | none until rows change |
| 9 | **Retire `tools/gen_shelf.py`** | 3 | `python -m engine.m9.cli shelf <world> --stdout` renders the same `SHELF.md` table from the real shelf (the `CANDIDATES` dict and `parse_bucket` are gone); render target follows the cleanup's phase-2 `worlds/<code>/` when it exists | none |
| 10 | **E's free half** | 3 | build briefs and the `cic-build-cycle` skill name `corpus_index.py --entry <census_id>` as the way a session reads the library; `complement-verbatim` observation in the report | none |

> **Amended by change order CO-5 (`Decision-Log.md` entry 22, 2026-09-15).**
> The table above is the table as originally frozen; the numbers stay as
> identifying labels for each increment's own scope, unchanged. The
> *execution order* changed: a halfway architecture review, run after
> increment 5 landed, found that `Shelf.rows` is empty for every real world
> until CM-1 lands (no bucket row carries a `row_id` yet), so increment 6 as
> originally sequenced would seal an attestation reading "no row on this
> world's shelf" into all nine real sealed packages — which would then need
> a *second* repin the day CM-1 lands. Mark's ruling: increment 6 moves
> behind CM-1. Real order from increment 5 onward: **increment 7's `kind`-
> only half** (RF-6 already establishes this half is not CM-1-blocked) →
> **increment 9** (retiring `tools/gen_shelf.py`, which has raised on every
> call since increment 1 and carries no working alternative to protect) →
> **increment 10** (no CM-1 dependency at all) → *[CM-1 lands]* → **increment
> 6** → **increment 7's `shelf_row` half** → *[CM-4 lands]* → **increment 8**.

Not in any increment, because it is corpus-map's work: CM-1 through CM-5,
CM-7 and CM-8. Increment 4's waivers are what let 1–10 land without waiting
for them. **Corrected dependency statement (RF-6):** increment 7's
`shelf_row` half cannot complete until CM-1 lands (only its `kind` half can
proceed before then), and increment 8 cannot ship until CM-4 exists —
increment 8 is not the *only* one waiting on corpus-map, as an earlier draft
of this section said. `voicing-pair` becomes clearable — and its waiver
deadline becomes real — only after CM-2/CM-3/CM-8; until then, R-4's carve-out
(§4.2) is what keeps new-world admission from being hostage to that timeline.

---

## 8. Residual risk and open items — for the freeze decision

Ordered by how much they could move the design, not by how easy they are.

1. **RESOLVED at freeze (R-1, R-2, R-3 — Decision-Log entries 15–17).**
   Q2's rule, applied literally with only a pair-level check, would have
   unvoiced a world's own bishop in one direction (Dionysius of Alexandria's
   words inside Eusebius' HE, `npnf201`, `context` for `alx` — voiceable only
   if the pair itself were ruled `mutual-awareness`, and Mark's own Q2 example
   names that exact pair one-way) while over-granting voicing in the other
   (Cyprian becoming voiceable for `don` just because the wider Carthage/Hippo
   pair qualifies, even though he predates the schism by decades and was never
   part of the argument — see former item 2, folded in here since R-1/R-2/R-3
   are one ruling at three grains, per **RF-15**'s own framing of it as one
   question asked at three grains). **Mark's ruling: a pair relationship makes
   voicing possible in principle, never automatic — each individual row still
   needs its own explicit `documented_exchange` tag (CM-8, §3) confirming it
   was actually part of the exchange on record, not merely produced by an
   aware party.** This is now built into `voicing-pair` (§1.4) and CM-8 (§3),
   not left open. Consequences: Cyprian (`antecedent` for `don`, 19 citations)
   gets no automatic tag and stays citable-not-voiceable, since there is no
   documented exchange to confirm for his specific words. `alx`'s Dionysius
   citations (37, fresh count; D2's quote+story subset is 9) stay unvoiced
   unless corpus-map finds and tags a specific documented exchange — a lower
   bar than CM-7's full re-rowing, and still entirely corpus-map's judgment,
   per Q1. No per-record override was added to the mechanism; the escape
   valve stays a classification call, where Q1 put it.
2. **The waiver list is large on day one and most of it is not this
   design's doing.** 398 `source-kind`, ~283 `shelf-row`, 166
   `emic-vendored-only` (**RF-2**), 296–407 `voicing-pair` (a file-grain floor,
   not a ceiling — **RF-3**), 116 file-grain off-shelf citations (§4.3). The
   first three are one-time migration classes with a mechanical majority; the
   fourth is `don`'s entire evidential base and waits on corpus-map (though
   R-4's carve-out means it no longer blocks a *new* world's admission); the
   fifth (`gallic`→npnf203, **56** citations across 55 records — **RF-4**
   corrects an earlier 52 — above all) is bucket completeness. A waiver list
   that big is honest and it is also a list a reader could stop reading.
   Increment 7's per-world PRs are sized to burn it down visibly.
3. **I2 is not held until CM-4, and never on 16 files — and even once CM-4
   lands, it is a shelf-grain claim, not a row-grain one (RF-5).** The shared
   single-unit plain-text files are Donatism's and IJC's spines
   (`optatus_against-the-donatists.txt`, the 5.1 MB Collatio scan, both
   Theodosian Code files). Marker work on them is vendoring, outside this
   charter, and nobody has costed it. Until then two of the worlds that
   need locus grain most have file grain, reported as such.
4. **I4 covers a third of voiced material and no more.** Stories,
   witnesses, terms, `modern_rendering` stay human-verified. The ratio
   instrument that might have reached them is inert (Q7-I5) and this design
   does not pretend otherwise.
5. **One vendored scan defeats the byte check on a hand-verified quote.**
   `don.quote.emeritus-magno-argumento` against the Migne Collatio OCR. The
   fix is a re-scan/re-OCR of that file or a second witness, not a wider
   matcher; the record's own `divergence_note` already documents the line.
   A waiver with no deadline this workstream can set.
6. **Every corpus-map merge now stales every affected world.** Wanted, and
   automated by increment 5 — but the auto-repin's PR-trigger token question
   (§6.3) is unverified until it runs once, and at 100 worlds a fleet-wide
   re-role would open up to 100 PRs. Q6 accepted this shape; the number is
   worth watching.
7. **Compile time grows.** `passage_units` over `ijc`'s 19 files (~62 MB
   normalized, D2's upper bound) on every `restore` and every staleness
   sweep, for every world. Q7-B ran the whole fleet in one sitting without a
   cache, so it is minutes, not hours, but it is paid on every engine CI
   run. **[extrapolation]** If it bites, the shelf's normalized units can be
   cached in-process by `(file sha256)` for the duration of one sweep; a
   persisted cache is the store this design refused, and should stay refused.
8. **`kind` is inferred from `edition` prose by regex.** `_EDITION_PATH`
   is the same anchored regex `gates.py` already uses, and it has already
   been wrong once (the trailing-period case its comment records). The
   `source-kind` check exists to make disagreement loud rather than to trust
   the regex; a record whose `edition` cites a file in words the regex does
   not catch will show as `unvendored` until fixed. Acceptable, visible,
   noted.
9. **Non-exclusivity is still corpus-map's problem.** A verbatim quote
   present in two traditions' shelves passes in both (D2 §3/B pt 6). The
   report counts `shared-rows-cited` as an observation so the overlap is
   visible, and rules on nothing.
10. **The fixture's synthetic texts live under `cic/texts/`.** Entry 10's
    wording, followed literally (§6.1); one clean alternative exists and is
    a loader change, not a design change. Mark's call at freeze.
11. **RF-16 — flag, not fully resolved.** `kind: unvendored ⇒ register: etic`
    on the source record itself (§5) goes one step beyond what entry 6
    literally said. Cheap (2 records) and defensible, but named here as still
    needing Mark's one-line confirmation at freeze, not inherited silently.

What this design does not build, so the list is closed: no load-time
refusal, no runtime role cut, no ledger gate, no materialized extract store,
no `WORKS.yaml` growth, no `address` backfill, no per-record speaker
attribution, no ratio instrument, no compiler-side mutation of records. CM-8
(R-1/R-2/R-3) is a bucket-*row* tag, corpus-map's own classification data —
not a per-citing-record override, which is the thing this list already
refuses and stays refused.
