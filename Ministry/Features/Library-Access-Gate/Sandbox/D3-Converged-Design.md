# Library Access Gate — D3 (convergent): the Compiled Shelf

**Sandbox artifact, 2026-09-15. Phase: D3, convergent — for Mark's freeze.**
One design, not a menu. It synthesizes D1's five directions, D2's struggle
findings, the two Q7 measurements and the nine Decision-Log rulings (entries
3–13) into a single buildable mechanism. Where it only partially satisfies an
invariant, it says so. Where it extrapolates beyond what D1/D2/the
measurements/the log established, the sentence is marked **[extrapolation]**.
Mark's own word freezes it; this document does not.

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
(Q2's rule), not by the row's role tag. A CI job asserts, for every real
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
  rows: {row_id: {source_file, work, author, role, confidence, locus, locus_ids|None, voice_of|None}}
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
(a story citing a term, 373 such entries fleet-wide today) is an intra-world
reference and is **not** followed — that target record is checked on its own.

| check | what it asserts | invariant | measured day-one findings (§8) |
|---|---|---|---|
| `source-kind` | every `source` record's `kind` (§5) agrees with its `edition`: `vendored` ⇔ `edition` names an existing `cic/texts/` file; `unvendored` ⇔ it names none; `absence` ⇔ it names an existing file and carries `absence_probes`. A missing `kind` is a finding | Q4/Q5 | 398 across the nine worlds (no record carries `kind` yet) |
| `shelf-row` | every `kind: vendored` source record carries `shelf_row`, and it names a row in **this** world's bucket whose `source_file` is the file its `edition` names | I1, work grain | ~283 (every vendored source record; 23 of them will also be genuinely off-shelf per D2 §2) |
| `emic-vendored-only` | no emic citable record's `sources[]` names a `kind: unvendored` or `kind: absence` source record | Q4 | 152 citations across 6 worlds (fresh, §8) |
| `absence-probe` | for every `kind: absence` record, none of its `absence_probes` strings window-matches in the named file; the read is logged in the report under `off_shelf_reads` with the record id and file | Q5 | 0 findings; 2 records exercise it (both `gallic`) |
| `verbatim-in-shelf` | every emic quote with `license: verbatim` window-matches inside the world's shelf files, at file grain (any role) | I4 (+I1 for quotes) | 4 of 221 (Q7-B: 3 complement-only, 1 OCR no-match) |
| `voicing-pair` | for every emic citable record, each cited `source` record resolves to a row that is either `role: tradition`, or a non-tradition row whose `voice_of` forms a pair with this world's `census_id` ruled `mutual-awareness` in `PAIRS.yaml` (confidence not `needs-ruling`). Missing `voice_of`, missing pair, `one-way`, `none`, or `needs-ruling` are each a distinct finding text | I3 as re-specified by Q2 | 296 citations to `context` (277) and `antecedent` (19) rows (fresh, §8; D2's quote+story subset is 47) |
| `locus-within-work` | **[lands with CM-4, §3]** the passage unit a `verbatim-in-shelf` match landed in has a `locus` inside the resolved row's `locus_ids`. On a file whose only unit is `whole-file`, this check emits an observation, not a finding | I2 | not measurable until `locus_ids` exist |
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

**I2 — locus within work.** Satisfied for verbatim emic quotes **once
corpus-map supplies `locus_ids` (CM-4)** — the byte match already lands in a
specific passage unit, so no `address` backfill is needed to know where the
quote is. Until CM-4 lands, I2 is not held by this design any better than
today. Structurally unreachable on the 16 shared single-unit plain-text
files (3.5 MB Gregory of Nyssa, the two Theodosian Code files, Optatus, the
Collatio acts, …) until markers are added to those files — vendoring work
outside this charter; §8 carries it. Not satisfied for non-verbatim citable
records at all: a story's `locus` stays prose.

**I3 — role-gated voicing.** Re-specified by Q2 and satisfied *as
re-specified*: the check is a pair-relationship lookup, not a role→voice
map, and it is exactly the mapping all five D1 directions got wrong (D2 §2,
§5.1). It is only as good as two corpus-map inputs — `voice_of` on
non-tradition rows (CM-2) and `PAIRS.yaml` (CM-3) — so on day one every one
of the 296 emic citations to non-tradition rows is a `voicing-pair` finding
("row has no `voice_of`") and every one is waived. That is the honest shape:
the gate is real and fires; the classification it depends on does not exist
yet, and per Q1 this workstream does not write it. Two consequences of the
rule as Mark stated it, both left to corpus-map's judgment rather than
handled by a code exception, are listed in §8 (items 1 and 2).

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
| **CM-2** | `voice_of: <census-id \| ruled party slug>` on every row whose `role` is not `tradition`: the tradition (or ruled non-tradition party, e.g. the imperial court, a pagan critic) whose own voice the work is. Required by `validate()` on non-tradition rows once the field exists; absent today on all 187 such rows | per row: whose voice is Optatus (`latin-pastoral-congregational-christianity`, per the staging note already there); whose is Eusebius' HE; whose is the Collatio tribunal | `voicing-pair` |
| **CM-3** | `cic/corpus-map/PAIRS.yaml` (added to `NON_BUCKET_FILES`): `pairs: [{a, b, relation: mutual-awareness \| one-way \| none, direction: a->b \| b->a (one-way only), evidence, confidence: assigned \| provisional \| needs-ruling}]` plus `parties: {slug: {kind, evidence}}` for non-census parties, the same "a slug is legal because a ruling exists" shape `UNATTRIBUTED.yaml` already uses | which tradition pairs were in documented argument (Q2's own examples: Donatists ↔ Optatus' Catholics = mutual-awareness; Alexandria ↔ Eusebius' tradition = one-way) | `voicing-pair` |
| **CM-4** | `locus_ids: [<passage-unit locus>, ...]` on every row, resolvable against `corpus_index.passage_units()`'s `locus` values (the file's own `div` id, or `whole-file`); `validate()` checks each id exists in the named file. D1 §1.1's rough count: ~470 rows already name a `divN` path in prose, ~17 say whole volume, ~50 other prose | mostly mechanical transcription of what `locus` prose already says; a real judgment only where the prose is vague | `locus-within-work` (I2) |
| **CM-5** | no new structure — **rows that are missing.** Q7-B's 3 complement-only quotes (`hal`→npnf211, `syr`→Palladius, `syr`→npnf203), D2's 23 off-shelf source records and 3 files in no bucket, and the file-grain off-shelf citations measured fresh (§8: `gallic` cites npnf203 52 times and it is not in `gallic`'s bucket) | every one is a "does this work belong to this tradition, and in what role" ruling | `shelf-row`, `verbatim-in-shelf` |
| **CM-6** | `corpus_map.validate()` tolerates a bucket carrying `fixture: true`: it skips the census-movement-id and known-author checks for that bucket only, and applies every other rule. `PAIRS.yaml` entries and `parties` may likewise carry `fixture: true` | none — Q8 put this in scope here; this workstream builds it | the M9 selftest |
| **CM-7** | no new structure — a *possible* re-rowing corpus-map may choose: giving an embedded own-voice work its own `tradition` row (the Donatist inscriptions inside CIL VIII, which the Donatists composed; Dionysius' letters inside Eusebius). `corpus_map.py`'s docstring currently declines to encode "attested-by" as a row; whether that stands is corpus-map's call | entirely judgment | changes which `voicing-pair` findings exist (§8 item 1) |

The first `python -m engine.m9.cli report <world>` run on each of the nine
worlds emits, as part of its findings text, the exact worklist for CM-2, CM-3
and CM-5: every non-tradition row an emic record cites (needs `voice_of`),
every `(census_id, voice_of)` pair the fleet needs a ruling on, every file a
world cites that its bucket lacks. That list, not this document, is the
hand-off to corpus-map's thread — and it is regenerated on every run, so it
cannot go stale.

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

`ACCEPTED_OPEN` follows `engine/m1/cross_world.py`'s convention exactly —
a dict in code, keyed `<layer>:<check>/<world>`, each entry owned by a named
finding and thread — with two additions Q3 requires:

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
| `m9:emic-vendored-only` (emic citations to unvendored sources) | 0 | 62 | 20 | 20 | 10 | 0 | 2 | 0 | 38 |
| `m9:voicing-pair` (emic citations to `context`/`antecedent` rows) | 37 | 8 | 4 | 173+19 | 0 | 0 | 13 | 13 | 29 |
| `m9:shelf-row` — off-shelf at file grain, before `shelf_row` even exists | 8 | 6 | 0 | 2 | 56 | 10 | 18 | 0 | 16 |
| `m9:verbatim-in-shelf` (Q7-B) | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 2 |
| `m1:reciprocity` / `m1:voice-perspective` (D2) | | | | 52 | | | | | 1 |

Two things this table says plainly. First, `emic-vendored-only` is the
largest *record-side* class and it is not a design choice — it is Q4 applied:
152 emic citations today ground a voice record in a source the library does
not hold (62 of them in `cappadocian`, 38 in `syr`). Each fix is either
dropping the citation where the record is also grounded in vendored material,
or re-registering the record etic — build-thread judgment. Second,
`voicing-pair` is `don`'s whole documentary base (192 of 296) and cannot be
cleared by `don`'s thread at all until CM-2/CM-3 land; its waiver is honest
about that in its `owner` text.

### 4.4 Admission

`state: admitted` is a registry commit (Artifact-1 §2). This design adds no
new state machine; it makes the existing CI job red for any non-grandfathered
world with findings at `built` or later, so a world cannot sit at `built`
long enough to be admitted unless it is clean. The M3 admission harness
(`engine/m3`) is not touched — it reads the package's `validation/` folder
today and will see `confinement-report.json` beside `gates-report.json`
without change.

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
by `engine/m9/loader.py`): `row_id`, `voice_of`, `locus_ids` on rows;
`PAIRS.yaml`; `fixture: true` tolerance in `validate()`.

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
register flip is tiny; the 152 emic *citations* to them are the real cost (§4.3).

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
  (`role: context`, `voice_of: fixture-synthetic-neighbour`), each with
  `row_id` and `locus_ids: [whole-file]`.
- `cic/corpus-map/PAIRS.yaml` gains `{a: fixture-synthetic, b: fixture-synthetic-neighbour, relation: mutual-awareness, fixture: true, …}`
  and a `parties` entry for the neighbour, `fixture: true`.
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
and the `WORLDS_YAML` constants in the by-hand evidence scripts
(`engine/m4/lazy_load_measure.py`, `live_table_run.py`, `live_turn_run.py`,
`live_table_battery.py`, `engine/m3/live_admission_run.py`,
`engine/m8/live_cost_run.py`, `live_memory_growth_run.py`) and the
`engine/api/README.md` line documenting the env var — are repointed in the
same PR (`render.yaml` and `wrangler.jsonc` do not name the path; checked). Package
bytes do not change (the registry entry's *content* is what
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
| 7 | **Fleet record migration**, one PR per world, Haiku | 2 | `kind` on every source record (mechanical from `edition`); `shelf_row` where the row exists (copied, never guessed); the 2 unvendored emic source records flipped etic; `absence_probes` on gallic's two absence records; waiver counts lowered as each lands | that world repinned |
| 8 | **Locus grain** (I2) | 3, CM-4 | `locus-within-work` check; `single-unit-shared-files` observation; seeded defect; `verbatim-in-shelf` reports the unit it matched in | none until rows change |
| 9 | **Retire `tools/gen_shelf.py`** | 3 | `python -m engine.m9.cli shelf <world> --stdout` renders the same `SHELF.md` table from the real shelf (the `CANDIDATES` dict and `parse_bucket` are gone); render target follows the cleanup's phase-2 `worlds/<code>/` when it exists | none |
| 10 | **E's free half** | 3 | build briefs and the `cic-build-cycle` skill name `corpus_index.py --entry <census_id>` as the way a session reads the library; `complement-verbatim` observation in the report | none |

Not in any increment, because it is corpus-map's work: CM-1 through CM-5
and CM-7. Increment 4's waivers are what let 1–10 land without waiting for
them; increment 8 is the only one that cannot ship until CM-4 exists.
`voicing-pair` becomes clearable — and its waiver deadline becomes real —
only after CM-2/CM-3.

---

## 8. Residual risk and open items — for the freeze decision

Ordered by how much they could move the design, not by how easy they are.

1. **Q2's rule, applied literally, unvoices a world's own bishop.** Under
   entry 4 as written, Dionysius of Alexandria's words preserved inside
   Eusebius' HE (`npnf201`, `context` for `alx`) are voiceable by `alx` only
   if the pair (`alexandria-catechetical`, Eusebius' tradition) is ruled
   `mutual-awareness` — and Mark's own example names exactly this as one-way.
   `alx.quote.dionysius-nepos` and 37 emic `alx` citations to `context` rows
   (fresh count; D2's quote+story subset is 9) therefore stay unvoiced unless
   corpus-map gives the Dionysian letters their own `tradition` row (CM-7),
   which its docstring currently declines to do. Same shape for `DEO LAVDES`
   in CIL VIII (`context` for `don`): the Donatists composed it, and
   corpus-map's own rule ("a work the tradition COMPOSED is `tradition`")
   would re-row it. This design deliberately adds **no** per-record override
   — one mechanism, and the escape valve is a classification, which is where
   Q1 put it. Mark should confirm at freeze that this consequence is intended;
   if not, the smallest change is a per-record `voice_of` override on the
   *citing* record, which reintroduces the speaker-attribution field D1 and
   D2 gestured at and this design left out on purpose.
2. **Pair grain makes `antecedent` voiceable by accident.** Cyprian is
   `antecedent` for `don`; his `voice_of` is the Carthage/Hippo tradition
   Optatus and Augustine also belong to; that pair is `mutual-awareness`; so
   Cyprian's words become voiceable for `don` even though he died fifty
   years before the schism and never knew them. Q2 said "not the role tag
   alone", so this is the rule working as stated. If Mark wants
   `antecedent` to stay citable-not-voiceable regardless of pair, that is a
   one-line rule in `voicing-pair` and a seeded defect; it is not decided
   here. 19 `don` citations turn on it.
3. **The waiver list is large on day one and most of it is not this
   design's doing.** 398 `source-kind`, ~283 `shelf-row`, 152
   `emic-vendored-only`, 296 `voicing-pair`, 116 file-grain off-shelf
   citations (§4.3). The first three are one-time migration classes with a
   mechanical majority; the fourth is `don`'s entire evidential base and
   waits on corpus-map; the fifth (`gallic`→npnf203 ×52 above all) is
   bucket completeness. A waiver list that big is honest and it is also a
   list a reader could stop reading. Increment 7's per-world PRs are sized
   to burn it down visibly.
4. **I2 is not held until CM-4, and never on 16 files.** The shared
   single-unit plain-text files are Donatism's and IJC's spines
   (`optatus_against-the-donatists.txt`, the 5.1 MB Collatio scan, both
   Theodosian Code files). Marker work on them is vendoring, outside this
   charter, and nobody has costed it. Until then two of the worlds that
   need locus grain most have file grain, reported as such.
5. **I4 covers a third of voiced material and no more.** Stories,
   witnesses, terms, `modern_rendering` stay human-verified. The ratio
   instrument that might have reached them is inert (Q7-I5) and this design
   does not pretend otherwise.
6. **One vendored scan defeats the byte check on a hand-verified quote.**
   `don.quote.emeritus-magno-argumento` against the Migne Collatio OCR. The
   fix is a re-scan/re-OCR of that file or a second witness, not a wider
   matcher; the record's own `divergence_note` already documents the line.
   A waiver with no deadline this workstream can set.
7. **Every corpus-map merge now stales every affected world.** Wanted, and
   automated by increment 5 — but the auto-repin's PR-trigger token question
   (§6.3) is unverified until it runs once, and at 100 worlds a fleet-wide
   re-role would open up to 100 PRs. Q6 accepted this shape; the number is
   worth watching.
8. **Compile time grows.** `passage_units` over `ijc`'s 19 files (~62 MB
   normalized, D2's upper bound) on every `restore` and every staleness
   sweep, for every world. Q7-B ran the whole fleet in one sitting without a
   cache, so it is minutes, not hours, but it is paid on every engine CI
   run. **[extrapolation]** If it bites, the shelf's normalized units can be
   cached in-process by `(file sha256)` for the duration of one sweep; a
   persisted cache is the store this design refused, and should stay refused.
9. **`kind` is inferred from `edition` prose by regex.** `_EDITION_PATH`
   is the same anchored regex `gates.py` already uses, and it has already
   been wrong once (the trailing-period case its comment records). The
   `source-kind` check exists to make disagreement loud rather than to trust
   the regex; a record whose `edition` cites a file in words the regex does
   not catch will show as `unvendored` until fixed. Acceptable, visible,
   noted.
10. **Non-exclusivity is still corpus-map's problem.** A verbatim quote
    present in two traditions' shelves passes in both (D2 §3/B pt 6). The
    report counts `shared-rows-cited` as an observation so the overlap is
    visible, and rules on nothing.
11. **The fixture's synthetic texts live under `cic/texts/`.** Entry 10's
    wording, followed literally (§6.1); one clean alternative exists and is
    a loader change, not a design change. Mark's call at freeze.

What this design does not build, so the list is closed: no load-time
refusal, no runtime role cut, no ledger gate, no materialized extract store,
no `WORKS.yaml` growth, no `address` backfill, no per-record speaker
attribution, no ratio instrument, no compiler-side mutation of records.
