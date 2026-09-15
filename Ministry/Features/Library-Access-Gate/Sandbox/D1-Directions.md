# Library Access Gate — D1 (divergent): five confinement architectures

**Sandbox artifact, 2026-09-15. Phase: D1, divergent.** Not a deliverable and not a ruling. Five directions for the confinement mechanism, written to be argued against independently in D2 (Opus adversarial review), after which Mark converges. Nothing here ranks the directions or recommends one; the last section says what each should be probed on.

Scope, per `README.md` in this workstream: design the mechanism that confines a world to its own tradition's source material, at 100+ worlds over a much larger library. Which works belong to which tradition is `cic/corpus-map/`'s job and is not touched by any direction below. Each direction takes the classification as given, however imperfect, and asks only: where and how is it enforced, what does that cost, what still fails, and what happens at two orders of magnitude.

---

## 1. What I read, and what I measured

Everything below is from the checkout as of 2026-09-15, measured by running the project's own tools or counting files, not taken from prose. Where my numbers differ from the charter's, I say so rather than pick one.

### 1.1 The library and the map

- `cic/texts/`: 250 MB on disk, 117 vendored files (38 ThML `.xml`, 79 plain `.txt`) plus the generated `README.md`/`AUTHORS.md`/`STRUCTURE.md` and the hand-written `INTAKE.md`. `STRUCTURE.md` (3,826 lines) is the generated `div` outline; the plain-text files mostly outline as a single section (e.g. `addai_doctrine-of-addai.txt`: 1 section, ~17k words; `anan-isho_paradise-v2-sayings_budge1907.txt`: 1 section, ~166k words).
- `cic/engine/corpus_index.py` already turns every file into passage units addressed `cic:<file>:<div-id>` (falling back to `whole-file` for files with no markers) into an FTS5 SQLite index that is **not committed**, and its `--entry <census-id>` flag scopes a search to the *files* of one bucket via `files_for_entry()` — file grain, not locus grain.
- `python cic/engine/corpus_map.py` today: **836 assignment rows across 55 buckets**; roles `tradition` 649 / `context` 170 / `transmission` 12 / `antecedent` 5; confidence `assigned` 681 / `provisional` 148 / `needs-ruling` 7. Validation (`validate()`) checks: bucket name is a census id, `ROLES`/`CONFIDENCES` enums, `REQUIRED` fields present, `source_file` is actually vendored, `author` is a known or ruled slug. It does **not** check `locus`, which is free prose (e.g. `div2 5.4 — On Baptism, Against the Donatists (7 books)`, `Pars III, short item`, `whole volume`). A rough regex over `_staging/` finds roughly 470 rows whose locus names a `divN` path in prose, ~17 that say whole volume/work, ~50 other prose; treat those three numbers as approximate.
- Non-exclusivity, two measurements that disagree on grain:
  - The charter and `CiC_Repo_Structure_Tracking.md` (measured 2026-09-14): 677 staged works, 47 (7%) single-tradition, median work claimed by 4, one by 19.
  - My re-measure today through `corpus_map.load()` at the `(source_file, work)` grain: **563 distinct pairs, 357 single-tradition, median 1, max 6.** At the *file* grain: 109 files carry assignments, 64 belong to one tradition only, median 1, **max 18 traditions on one file.** I could not reproduce "677 / median 4 / one by 19" and suspect a different counting unit (perhaps work title pooled across files, or the file grain for the "19"). D2 should re-measure once with a stated unit; it matters because every direction below has to choose the grain at which confinement is enforced, and file grain is provably too coarse either way (`donatism` shares 10 of its 21 bucket files with other entries).
- `cic/corpus-map/WORKS.yaml`: 4 seed entries (`athanasius-vita-antonii`, `augustine-confessiones`, `cyprian-epistulae`, `palladius-lausiac-history`), hand-maintained, append-only, "no guessed identifiers"; its own header says to adopt corpus-map's staging pattern if it outgrows one file. `cic/engine/works_registry.py` validates it and cross-checks `work_id` usage in records.
- `cic/engine/corpus_map.py`'s docstring names the check nobody has built: *"that no `register: emic` record ever cites a context work — becomes checkable at integration."* And: *"INTEGRATION IS DELIBERATELY NOT DESIGNED HERE."* This workstream is that integration.

### 1.2 The records and their backfill state

Nine formation worlds under `records/` (plus `fix` and `_fleet`); 1,927 record files total. Per world:

| world | source | quote | story | `work_id` on source | `address` on quote/story | `locus` on quote/story |
|---|---:|---:|---:|---:|---:|---:|
| alx | 25 | 26 | 8 | 2 | 0 | 34 |
| cappadocian | 111 | 20 | 19 | 0 | 0 | 39 |
| desert | 29 | 59 | 10 | 3 | 5 | 69 |
| don | 76 | 5 | 12 | 0 | 0 | 17 |
| gallic | 36 | 3 | 15 | 0 | 0 | 18 |
| hal | 28 | 32 | 12 | 2 | 0 | 44 |
| ijc | 30 | 39 | 11 | 1 | 0 | 50 |
| pahc | 23 | 25 | 14 | 0 | 0 | 39 |
| syr | 40 | 34 | 10 | 2 | 0 | 44 |
| **total** | **398** | **243** | **111** | **10** | **5** | **354** |

So: `locus` (free text) is on every quote and story; the machine-resolvable `address` is on 5 (all desert, all in `evagrius_praktikos_dysinger.txt`); `work_id` is on 10 source records naming 3 of the 4 seeded work ids. Records name 83 distinct `cic/texts/` paths in their `edition`/`locus` prose.

Record `register`: quotes 225 `emic` / 21 `etic`; sources 110 `emic` / 290 `etic`; stories 112 `emic`; doctrinal_witness 155 `emic`. The `sources[]` envelope on any record is `{source_id (required), locus, license, address}` (`engine/m1/schemas.py`). Source records carry `author/work/edition/rights_status/attribution_status/discovery_channel` plus optional `work_id`.

One live edge case: `records/gallic/source/gallic.source.augustine-letters-221-226-absence.md` is a source record whose whole subject is an *absence* from `cic/texts/npnf101_augustine-confessions-letters.xml` — a file that is **not** in `gallic-monastic-ascetic-christianity.yaml`'s bucket (9 files, none Augustine's `npnf101`). `gallic.contested.beginning-of-good-will` cites the same absence in a `locus`. Every direction has to say what a strict shelf check does with a record that cites an off-shelf file in order to document that the file does not contain something.

### 1.3 What is enforced today, and one correction to the baseline

- `engine/m1/gates.py`: 18 gates in `GATES`. The ones near this problem: `gate_quote_recording` checks `license ∈ {verbatim, paraphrase-only, do-not-voice}` and that `text`/`speaker_or_author` are non-blank; `gate_canonical_address` checks an `address` is well-formed and its file exists; `gate_edition_rights_consistency` checks a cited edition file exists and its licence line agrees; `gate_referential` checks `sources[].source_id` resolves to a record in the world or the fleet. Each gate is `(records, fleet, registry) -> list[str]`, admitted only with a seeded defect in `fixtures/seeded_defects.yaml` (25 today) and selftest proof (the bar `gates_experimental.py`'s docstring states). `gates.py` deliberately imports nothing from `cic/engine/` (its own comments at `_TEXTS_DIR` and `_ADDRESS_RE`).
- **Correction.** The tracking doc's Question 1c says `gate_quote_recording` checks "verbatim presence in the file." It does not; no gate in `gates.py` reads a quote's `text` against any file under `cic/texts/`. The only verbatim check in the engine is runtime: `engine/m4/grounding_net.py::_span_in_records` window-matches quoted spans in an *answer* against the world's own tagged *records* (the package), and `engine/m4/grounding.py::find_do_not_voice_violation` matches `do-not-voice` quotes. `gate_quote_fidelity_recording`, named in `cic/texts/README.md`, exists nowhere in `engine/`. Verbatim verification against the vendored file is a human step recorded in each quote's `locus` prose ("independently re-located and re-read this session … line 15788"). This matters for every direction: today the pointer is checked, the bytes are not.
- `engine/m1/cross_world.py::observe_corpus_map` reads each world's bucket via `census_id` and reports counts — an observation, not a defect. `observe_second_hand_sources` derives an "opened" set from `cic/texts/…` paths in `edition` fields.
- `tools/gen_shelf.py` (committed, never run in anger): parses a bucket with a minimal reader, renders `SHELF.md` (markdown, a table). It writes to `<repo>/worlds/<code>/`, a directory that does not exist (D4's phase-2 merge is pending); run today with defaults it writes zero shelves. It also hard-codes a `CANDIDATES` dict of world codes (`gallic`, `lpc`, `latap`, `grkap`) — `gallic` is now registered, and spec principle 4 forbids world identifiers in code.
- The runtime never opens the library. `engine/m2/compiler.py::compile_world` builds a package from `records/<world>/` only (records copied byte-for-byte, then compiled views: `prompt.txt`, `quotes.json`, `repository.json`, chunks, indexes), hash-chained by `manifest.json`; `engine/m4/world_loader.py` verifies the hash and refuses on mismatch; `engine/Dockerfile` copies `cic/texts/` into the image only so that the two file-reading gates pass during `restore`. `run_voice_turn_for_world` scopes a Table voice to one world's package — isolation "falls out of this line" (its comment). Packages today: 1.5–3.4 MB each, prompts 59–151 KB, `packages/` 33 MB for nine worlds.
- CI (`.github/workflows/ci.yml`): three engine jobs run `python -m engine.m2.cli restore` (recompile every pinned world, verify every hash) and a fourth runs the staleness sweep. GitHub minutes were exhausted 10 days into a cycle on 2026-09-10; per-job path filters were the fix. Build cost is already linear in the number of worlds per CI run.
- Editing anything under `records/` changes the package hash; repinning touches `records/worlds.yaml`, the file active world branches conflict on (Gate A, B1).

### 1.4 The decided baseline this sits inside

- **D5** (Mark, 2026-09-14): one flat library; each world gets a generated shelf via `census_id`, narrowed by Step 2; the barrier is a build gate (WO-4); runtime unchanged, the package is the seal.
- **WO-4 as specified**: (a) every `source.work_id` resolves to a work on the shelf; (b) every quote/story `address` falls inside that work's locus; (c) `context`/`antecedent`/`transmission` works citable as evidence, never voiced. Prerequisite backfill: ~333 `work_id`, ~330 `address`, `WORKS.yaml` growth.
- Program-Spec principles that bind any direction: 4 (one registry, everything derived), 6 (fail open toward the pre-guard state, direction stated per check, never silently), 9 (every generated artifact verifies against its source), 11 (risky substitutions land last and alone), 12 (gate integrity; a gate that never fails is checking nothing), 14 (only public-domain texts vendored), 16b (packages in S3-compatible object storage, WO-1). M2 must never import M3. `records = what's true; prompt = how to speak.`
- Source fidelity (root `CLAUDE.md`): never invent; every quote re-verified verbatim against the vendored file before review; contested claims carry the five-level confidence vocabulary. Note there are three distinct confidence vocabularies in play: the bucket's `assigned/provisional/needs-ruling`, the record's `confidence:` block (`citation_specificity`, `verification_state`, `evidentiary_weight`, `formation_confidence`), and the prose five-level one. None of them currently says anything about *voicing permission*; the vocabularies that do are the record's `register` (`emic`/`etic`) and the quote's `license`.

---

## 2. The problem stated as invariants

Every direction is trying to hold some subset of these. Naming them lets D2 check each direction against the same list.

- **I1 — Citation on shelf.** Every source a world's records cite resolves to a work assigned to that world's tradition in `cic/corpus-map/`.
- **I2 — Locus within work.** Every passage a record cites lies inside the assigned locus of that work, in that file (two worlds share `npnf104`; only the works inside it that are assigned to each may be reached).
- **I3 — Role-gated voicing.** Material assigned as `context`/`antecedent`/`transmission` may be cited as evidence but never spoken as the world's own voice.
- **I4 — Bytes match.** A quote's `text` is actually present, verbatim, at the cited place in the vendored file (today: human-verified only).
- **I5 — Influence, not just citation.** Nothing off-shelf shaped the world's prose fields (`story.text`, `doctrinal_witness.text`, `term.plain_meaning`…) even without a citation. This is the invariant no mechanical check fully reaches; directions differ in how close they get and where they stop honestly.
- **I6 — Runtime seal.** A live turn draws only on its own package.

I6 holds today by construction. I1–I3 are specified (WO-4) and unbuilt. I4 is believed built and is not. I5 is held by process.

---

## 3. Five directions

Each: how it works concretely; what it costs; what still fails; how it behaves at 100+ worlds over a 10× library (call it W = 100 worlds, ~20k records, ~1,000 files, ~2.5 GB).

### Direction A — Finish WO-4 as specified: the pointer gate at compile time

**The idea.** Confinement is a property of the *records*, checked when the package is compiled. The shelf is a generated list; three new gates in `engine/m1/gates.py` check every record's pointers against it. This is D5's letter.

**How it works.**

1. Make the shelf machine-readable. `SHELF.md` is a markdown table; a gate cannot sensibly parse it. Generate a sibling `shelf.yaml` (or have the gate read the bucket directly). Because `gates.py` refuses to import `cic/engine/`, the pragmatic shape is a small bucket reader inside `engine/m1/` (the 14-line `parse_bucket` in `gen_shelf.py` is already that), keyed by `registry[world].census_id` — the same join `cross_world.observe_corpus_map` makes. Retire `gen_shelf.py`'s `CANDIDATES` dict: unregistered worlds have no shelf until they have a registry code (principle 4).
2. `gate_shelf_membership` (I1): for every `source` record with a `work_id`, resolve `WORKS.yaml` → `expressions[].items[]` addresses → files, and require that (file, work) is a row in the world's bucket. Fail closed on a `work_id` that resolves to nothing on the shelf.
3. `gate_address_within_locus` (I2): for every `sources[].address` of the form `cic:<file>:<locus>`, require the file to be on the shelf and the `<locus>` to fall inside the bucket row's locus. This needs the bucket `locus` to be resolvable to div ids — a new structured field on staging rows (say `locus_ids: [div2 5.4]`), because today it is prose.
4. `gate_role_voicing` (I3): for every record with `register: emic` (or a quote with `license: verbatim`/`paraphrase-only`), every cited source's shelf role must be `tradition`. A `context`/`antecedent`/`transmission` source may be cited only by `register: etic` records or `do-not-voice` quotes. This is the check `corpus_map.py`'s docstring predicted.
5. Each gate ships with a seeded defect in `fixtures/seeded_defects.yaml` and a fixture-world bucket (the fixture has `census_id: null` today — it needs a synthetic bucket or the gate is inert on it, which principle 12 forbids).
6. Backfill: `work_id` on ~388 source records, `address` on ~349 quote/story records, `WORKS.yaml` from 4 to the several hundred works the nine worlds actually cite — all "never guessed," per the existing sign-off.

**What it costs.** The gates themselves are a few hundred lines in house style, a day or two each with tests and seeded defects. The backfill is the real cost: three hand-maintained joins (`work_id` → `WORKS.yaml`, `address` → file structure, bucket `locus` → div ids), each under a no-guessing rule, each per record. At today's scale that is ~740 record edits plus a `WORKS.yaml` an order of magnitude bigger than its header says one file should hold. Every backfilled record changes its package hash, so every world is rebuilt and repinned, touching `worlds.yaml` on every active branch.

**What still fails under it.**

- It checks the pointer, never the bytes (I4 untouched). A quote lifted from an off-shelf work and filed under an on-shelf `source_id` with a plausible `address` passes. `gate_canonical_address`'s own docstring already concedes the gate "does not and cannot confirm the `<locus>` half actually points at the right passage."
- It is only as strong as the backfill. `work_id` and `address` are optional; a record without them is invisible to gates 2 and 3. Either the gates are inert until backfill is complete (principle 12), or `COMPLETION_REQUIRED` grows and every world fails to compile until its backfill lands.
- Absence records (the gallic case) fail I1 unless the schema learns a `kind: absence` source that is exempt — a new rule, not a backfill.
- `WORKS.yaml` becomes a fleet-wide serialization point: many world threads appending to one hand-maintained file, exactly the shape corpus-map moved *away* from with `_staging/`.
- Bucket `confidence: provisional` / `needs-ruling` (155 rows) is not consulted; a provisionally-assigned `tradition` work is voiceable.
- I5 is not addressed at all.

**At 100 worlds, 10× library.** Gate compute is trivial (O(records × shelf) per world; the sweep is linear in W and already runs). The backfill is what scales badly: ~4,000 source records and ~4,000 quote/story records to join by hand, and a `WORKS.yaml` of several thousand entries. A corpus-map re-merge that renames or reassigns a work turns red every world whose shelf lost it — a classification edit becomes a fleet-wide build failure (blast radius: all worlds citing that work, at once). Adding a new source: vendor, stage, merge, add to `WORKS.yaml`, then each world's source record. Adding a world: one bucket, one registry row, then its records must be born with `work_id`/`address` (cheap if born that way; the cost is entirely in the existing fleet).

---

### Direction B — Bytes, not pointers: the materialized per-world shelf and a verbatim-in-shelf gate

**The idea.** Do not check where a record *says* its text came from; check that the text *is in* the world's own slice of the library and nowhere it shouldn't be. The shelf stops being a list and becomes a derived, hashed, per-world text extract — the physical projection of the bucket. D5 rejected copying *sources* into worlds (duplication, rights headers, size); a derived, uncommitted, regenerable extract answers those three objections the same way `packages/*/compiled/` and `INDEX.sqlite` already do.

**How it works.**

1. A new pure module (say `engine/m9/shelf.py`, house style: no I/O in the core function, thin CLI, mirrored tests) takes `(bucket, passage_units per file)` and returns the world's shelf extract: every passage unit (`corpus_index.passage_units` already yields `{locus, title, apparatus, text}` per `div`) whose file+locus falls inside an assigned row, tagged with that row's `role` and `confidence`. Output: `shelf/<world>/<hash>/units.jsonl` + `manifest.json`, derived, gitignored, regenerated by `restore`, hash recorded in the world's package manifest so package ↔ shelf provenance is verifiable (principle 9).
2. `gate_quote_in_shelf` (I1+I2+I4 in one): a quote with `license: verbatim` must window-match (reuse `grounding_net._normalize` / the 6-word window) inside its own world's extract. A quote that matches only in units tagged `context`/`antecedent`/`transmission` may not be `register: emic` (I3). A quote that matches nowhere in the extract fails, whatever its `source_id` says. This is the check the tracking doc believed already existed, built at the right grain.
3. `gate_story_grounded_in_shelf` (partial I5): a story's `text` is retold, not verbatim, so use the existing grounding-ratio primitives (`engine/prose.py`: `content_words`, `grounding_ratio`, already used by the runtime net) against the extract — report-only until a baseline earns it a bar (principle 10).
4. Bucket `locus` must resolve to units. Same structured `locus_ids` requirement as Direction A step 3, but here it gates *extraction*, so an unresolvable locus is visible immediately as an empty or whole-file extract, not as a silent pass.
5. Authoring-time use, free: a build thread can be told to read only `shelf/<world>/` for its Step-2 and record work; `corpus_index --entry` becomes locus-scoped instead of file-scoped.

**What it costs.** The extractor is small (the unit walker exists). The resolver from bucket locus to units is the real build: ThML files resolve by `div` id; the 79 plain-text files need markers, and many outline as one section, so their extract is whole-file. A per-world extract store: `don`'s bucket alone spans 21 files including whole-volume scholarship (Monceaux ×3, CIL VIII), so a single extract could be tens of MB. CI has to regenerate extracts before gates run, or cache them by (bucket hash, file hash). No `work_id`/`address`/`WORKS.yaml` backfill is required for the verbatim gate — the join is text → extract, not record → registry. (The FRBR registry remains useful for its own purpose, cross-world "same work?" questions, but stops being on the confinement critical path.)

**What still fails under it.**

- Plain-text files without markers collapse to whole-file units; where such a file is shared by traditions (file grain max 18 today), locus confinement inside it is impossible until markers are added. The gate must fail *closed* on a shared whole-file unit, which will block real quotes until the file is structured — honest, and expensive.
- Verbatim matching is only for `verbatim`-licensed quotes. `paraphrase-only` quotes, `modern_rendering`, stories, witnesses and terms are reached only by ratio instruments that this project has so far kept report-only.
- Original-language second witnesses (the CSEL/Migne Latin files) and English translations are separate works in the bucket; a quote of an English rendering the world made itself ("modern_rendering is a light modernization of the NPNF's own published translation") will not window-match the Latin and only sometimes the English. Normalization rules will accrete.
- Absence records still need a rule; here it is easier — an absence record cites no text, so it is outside the verbatim gate's domain, but I1 for `source` records themselves still needs a decision.
- A quote that appears in *two* traditions' extracts because the underlying work is assigned to both (the Vita Antonii case) passes in both — correct by the map's own design, but the gate cannot tell "shared work" from "over-assigned work." That is corpus-map's problem by charter; the gate should surface it as an observation, not decide it.

**At 100 worlds, 10× library.** Extract storage is O(Σ shelf sizes): if the average shelf is 30 MB, 100 worlds is ~3 GB of derived data that must be regenerable and cached, never committed. Verbatim gating is O(quotes × extract) substring search, fine at seconds per world. The resolver work is O(files), done once per file, amortized across every world that shares the file — better than per-record backfill. Blast radius of a corpus-map change: only the worlds whose extract changed get re-gated, and the diff is *which passages* left the shelf — far more legible than a dangling `work_id`. Adding a source: vendor, structure (markers), stage; every world whose bucket gains it gets a new extract. Adding a world: its extract is one command. The scaling risk is CI minutes: regenerating 100 extracts on every engine change is the exact shape that exhausted the Actions budget on 2026-09-10 — caching by content hash is not optional here.

---

### Direction C — Derive, don't check: source records synced from the bucket

**The idea.** Spec principle 4 is "one registry; everything derived." Today a `source` record's bibliographic core (`author`, `work`, `edition` path, rights basis) is hand-typed per world, and a gate would check it *after the fact* against the bucket. Invert it: the bibliographic core of a world's source records is *generated from* its bucket row, the way `engine/m6/census_sync.py` generates the census's registry-derivable fields, with a `check` mode that fails CI on drift. A world then cannot hold a source record for a work off its shelf, because the only way a source record's core comes into being is `sync`. Interpretive fields (evidentiary weight, the body, `discovery_channel`) stay hand-authored beside the synced core.

**How it works.**

1. A pure `sync_sources(bucket, existing_source_records) -> (new_records, changes)` in a new engine module, `m6`-shaped: `sync` writes, `check` diffs. The join key is the bucket's own `(source_file, work)` string pair — no `WORKS.yaml`, no `work_id`, no address backfill. Each source record gains a generated block, e.g. `shelf: {source_file, work, role, confidence, atlas_id}`, and the schema marks those keys as sync-owned.
2. `gate_source_shelf_sync` (I1): every source record's `shelf` block equals what `sync` would produce for this world; a record with no `shelf` block is a defect unless it is `kind: absence` (a small schema addition for the gallic case, where the synced block would carry the file and `role: absence`).
3. `gate_role_voicing` (I3) as in Direction A, but reading `shelf.role` off the source record — no lookup through a registry at gate time, and `repository.json` in the package therefore carries the role, so the package is self-describing about voicing permission.
4. Optionally, `shelf.confidence` participates: a `provisional`/`needs-ruling` row may be synced but flagged, and I3 can be tightened to "voiceable only when `assigned`" — a policy knob this direction exposes cheaply because the value travels with the record.
5. I2 (locus) is *not* solved here on its own; `sources[].locus` stays prose, and the `address` field stays optional. This direction is honest that it confines at the work grain.

**What it costs.** One sync module plus tests (the `m6` pattern is a direct template; `census_sync.py` is 135 lines). A one-time migration: for each of 398 source records, match its prose `edition`/`work` to a bucket row and write the `shelf` block — a real, human, per-record pass, but a *copy* of a string that exists, not the invention of an identifier under a no-guessing rule. Every migrated record changes its package hash (same repin churn as A). Ongoing cost goes *down*: a new world's source records are scaffolded from its bucket, which is what Step 2 (Source Ecology) does by hand today.

**What still fails under it.**

- Pointer-level: I4 (bytes) and I5 (influence) are untouched.
- Work grain only: two traditions assigned different works inside `npnf104` are confined to their works by the synced block, but nothing checks that a quote's `locus` lies inside that work. I2 needs Direction A's address or Direction B's extract on top.
- A hand-typed `sources[].source_id` can still point at a source record whose *interpretive* fields claim more than the bucket row does; the sync owns only the block it owns.
- Sync semantics have to be defined for deletions: when a bucket row disappears, does `check` fail (a world now cites an unassigned work) or does `sync` delete the record? `census_sync` only ever advances status; sources need a stated direction per principle 6.

**At 100 worlds, 10× library.** Sync is O(bucket size) per world, embarrassingly parallel, and reads only the world's own bucket — no fleet-wide file. Drift from a corpus-map re-merge shows as a per-world `check` diff naming the row that changed, so the blast radius is visible and bounded before anything goes red. Adding a source: stage → merge → each affected world runs `sync` and sees a new stub to annotate. Adding a world: `sync` writes its source-record cores in one command. The one scaling worry is the migration debt: it is a one-time 398-record pass now and a ~4,000-record pass if deferred to 100 worlds.

---

### Direction D — The attested package: the shelf travels in the package, and the loader is the choke point

**The idea.** D5 says "the package is the seal." Take that literally for confinement: put the shelf attestation *in* the package and enforce at the one place every world must pass through in production — `engine/m4/world_loader.py`'s verified load — rather than only at compile time, where a gate can be edited on a branch, a stale package can be pinned, or a package can arrive from object storage (WO-1) built elsewhere. Compile-time gates still run; this direction adds the layer that holds when they were bypassed.

**How it works.**

1. `compile_world` emits `compiled/shelf.json`: the world's bucket rows (file, work, locus, role, confidence) as of `records_commit`, plus a per-record coverage map: for every citable record, which shelf row(s) its sources resolve to and the role of each. Hash-chained in `manifest.json` like every other file. (`package_schema` bumps 1 → 2; every package is rebuilt and repinned.)
2. `verify_package_dict` (`engine/m2/loader_stub.py`, already the refusal point for hash mismatch) gains a second refusal: any `quotes.json` entry or `repository.json` record whose sources resolve to no `shelf.json` row, or whose `register: emic` resolves to a non-`tradition` row, raises `PackageRefused`. Fail-closed at load: the world does not come up.
3. Runtime role check (I3, per turn): `grounding_net.check_turn` already decides per sentence whether a quoted span is verbatim in a tagged record; add the role dimension — a span grounded only in a record whose shelf role is `context`/`antecedent`/`transmission` cannot stream as the voice's own words. This is the existing net's own instrument, with one more field to read from `shelf.json`; it is not a new per-turn police (principle 2) if it is genuinely the same check with role awareness — D2 should test that claim.
4. Audit (Artifact-8): `engine/m7` can verify confinement offline from a package alone, without the repo, because the attestation is inside it.

**What it costs.** A builder for `shelf.json` (the same bucket reader Direction A needs), a schema bump, a rebuild of nine packages, changes to the loader's refusal logic and its tests (`test_stub_loader_refuses_*` are the template), and the runtime net change — which touches `engine/m4/turn.py`'s live path and therefore sits under principle 11 (lands last and alone) and principle 5's safety-rerun boundary if anything near the Facilitator is touched (it should not be).

**What still fails under it.**

- It is still pointer-level unless combined with B; the attestation says what the records *claim*, verified against the bucket, not that the bytes match.
- Fail-closed at load has the largest blast radius of any direction: a bad attestation takes a world offline in production rather than failing a build. Principle 6 says the direction must be stated and the failure never silent; "world unavailable" is loud, but it is a participant-facing outage caused by a bibliographic defect.
- The runtime role cut is participant-visible degradation (`degraded_by_net`), and a false positive on an `antecedent` work (a Donatist rightly citing Cyprian as the authority argued *from*) would cut a correct sentence. The line between "citing as evidence" and "voicing as our own" is not a mechanical one at turn time; the record's `register` already encodes the builder's judgment, and the net would be second-guessing it.
- The bucket snapshot inside a package goes stale the moment corpus-map changes; the staleness sweep must learn that a bucket change stales a package (today only `records/` and the registry do).

**At 100 worlds, 10× library.** Per-package cost is O(records); per-turn cost is O(citations); neither scales with W or library size. The attestation is what makes WO-1 (object-storage packages, per-world updates without a full redeploy) safe to do for confinement — a package fetched at runtime carries its own proof. Blast radius shifts from CI to production; at 100 worlds, "one world refused at load" is contained (WO-2's lazy loader already isolates worlds), but a fleet-wide `shelf.json` format bug refuses every world at once. Adding a source or a world is unchanged; every corpus-map merge now stales packages fleet-wide, which at 100 worlds is a rebuild storm unless the staleness check is made bucket-row-aware rather than bucket-hash-aware.

---

### Direction E — Confine the reader, not the record: scoped authoring tools and an access ledger

**The idea.** Every leak begins when a build session *reads* a file. The four directions above check the record after it is written; this one changes what a session can conveniently read and makes reading leave a trace that a gate can reconcile. It is the ingestion-time / authoring-time enforcement point. On its own it cannot be a hard guarantee (a session with a filesystem can open anything), so its honest role is as the layer that catches I5 — influence without citation — which nothing else here reaches.

**How it works.**

1. Scoped reading. `cic/engine/corpus_index.py --entry` already scopes search to a bucket's files. Extend it to loci (needs the same `locus_ids` resolution as B), and add a `cic/engine/shelf_open.py <world> <address>` that returns a passage only if it is on the world's shelf, refusing with the shelf row that *would* cover it otherwise. Build-cycle briefs and the `cic-build-cycle` skill point sessions at these tools instead of `Read` on `cic/texts/` directly.
2. The ledger. `search_record` already exists as build provenance (excluded from packages by `_PACKAGE_EXCLUDED_RECORD_TYPES`) and `observe_second_hand_sources` already derives an "opened" set from `edition` prose. Make the ledger explicit: the scoped tools append `search_record`s naming the address opened; a new gate, `gate_cited_is_opened`, requires every `sources[].address` (or, until addresses exist, every `cic/texts/` path in `locus`/`edition`) to appear in the world's own ledger — and every ledger entry to be on-shelf. A cited passage nobody opened through the scoped tool is a defect.
3. Influence sweep (I5, report-only): for prose fields the runtime net already treats as voice (`_PERSPECTIVE_FIELDS`, `_chunk_text` inputs), run the grounding-ratio instrument against the *complement* of the shelf — passages in files the world's bucket shares with other traditions but which are assigned to those traditions only — and report high-overlap sentences. A world whose story text grounds better in a neighbour's locus than in its own is the leak this whole workstream is about, made measurable.

**What it costs.** Tooling: locus-scoped search and open (shared with B's resolver), a ledger writer, one gate, one report-only instrument. Process: brief and skill updates so sessions actually use the tools. No record backfill — but the gate is inert on the existing fleet until addresses exist (it can run on the file grain today using the paths already in prose, which is weaker but not nothing).

**What still fails under it.**

- It is advisory against a determined or careless session; a `Read` on `cic/texts/` leaves no ledger entry, and the gate only knows what the ledger says. The complement sweep is the backstop, and it is a ratio instrument, not proof.
- Ledger volume: every open becomes a record file; at hundreds of opens per world that is thousands of `search_record` files, in `records/` (hashed into the package's `records/` copy even though excluded from `repository.json`) — a bloat vector unless the ledger lives outside `records/`, which then means outside the hash chain.
- The complement sweep has no baseline yet; principle 10 keeps it report-only until it earns a bar, so I5 stays "measured and read by a human," not gated.

**At 100 worlds, 10× library.** Scoped tools cost nothing extra per world. The complement sweep is O(prose × complement size) per world; the complement of a busy world's shelf inside shared files could be large (a file shared by 18 traditions has 17 traditions' worth of complement), so it needs the same cached extracts as B. Blast radius: a ledger gap fails only the authoring world. Adding a source: it appears in scoped search for every bucket it is staged into, automatically. Adding a world: its ledger starts empty and grows. The scaling risk is human, not compute: at many concurrent build sessions, "use the scoped tool" is a discipline, and disciplines drift — the ledger gate is what notices.

---

## 4. How the directions combine, and where the existing vocabularies bite

These are not five whole answers to choose one of; D2 may find the salvage is in combinations, as Website V2's own D2 did. Some observed seams:

- **A, C and D share one dependency**: a machine-readable shelf keyed by `census_id`, readable from inside `engine/m1/` without importing `cic/engine/`. Whoever builds any of them builds that first. B and E share a different one: bucket `locus` resolvable to passage units, which means a structured `locus_ids` on staging rows (a corpus-map *schema* change, though not a *classification* change — D2 should rule whether that is inside this workstream's charter) and markers in the plain-text files.
- **Grain.** A confines at work grain via a registry; C at work grain via the bucket's own strings; B at locus grain via bytes; D at whatever grain its inputs have; E at locus grain via the ledger. Only B and E reach I2 without an `address` backfill.
- **Bytes.** Only B reaches I4. A, C and D are pointer-level and inherit the false belief in section 1.3 unless they say so in their own docstrings.
- **Role vocabulary.** All five map `tradition` → voiceable and the other three roles → evidence-only, and all five need the mapping onto the *record's* existing vocabulary made explicit: `register: emic` ↔ `tradition`; `register: etic` or `license: do-not-voice` ↔ `context`/`antecedent`/`transmission`. The 21 `etic` quotes and 110 `emic` source records in the fleet are the first test set. `antecedent` is the hard case: Cyprian is on the Donatist shelf precisely so the Representative can argue from him; "cite, never voice" must not become "never quote."
- **Confidence vocabularies.** None of the directions is forced to consult bucket `confidence`, and WO-4 as written does not. 155 rows are `provisional` or `needs-ruling`. A design that ignores them treats a provisional assignment as a permission; one that gates on them makes corpus-map's confidence field a voicing switch it was not designed to be. Either is a decision, and it should be a stated one.
- **"Never invent."** The no-guessing rule is why A's backfill is slow (identifiers must be verified, not inferred) and why C's is fast (a copied string is not a guess). It is also why B's normalization rules are dangerous: every fuzzy-match tolerance added to make an English rendering match is a small licence to be wrong about bytes, the one thing the rule exists to forbid.
- **Absence records.** Every direction needs the same small schema rule for a source record that documents what an edition does *not* contain. Whichever direction wins, this is a change order on `engine/m1/schemas.py`, not a shelf question.
- **Rebuild churn.** A, C and D all change bytes under `records/` or the package schema, so all three repin every world and touch `worlds.yaml` on every branch. B and E do not touch records at all until their gates are made blocking. That is a sequencing fact, not a merit.

---

## 5. What a reviewer should probe hardest, per direction

Not a ranking. Each item is the place I think the direction is most likely to break, or where I was least able to verify a claim.

**A — Finish WO-4.**
- Is a pointer gate with an optional-field backfill inert in the sense principle 12 forbids? Measure: with `work_id` on 10 of 398 source records, what fraction of citations would gate 2 actually see on day one?
- Can `WORKS.yaml` be the join key at fleet scale under its own "one file, no guessed identifiers" rules, or does the FRBR registry need to be moved off the critical path (C's move) before A can finish?
- Does a corpus-map re-merge turning N worlds red at once meet "fail open toward the pre-guard state, direction stated per check"?

**B — Materialized shelf.**
- The 79 plain-text files: how many are shared across traditions *and* outline as one section? That number is the size of the hole locus confinement cannot close without structuring work, and it should be measured before B is costed.
- Will verbatim-in-extract actually match the quotes the fleet already holds (Latin variants in brackets, NPNF's own bracketed readings, `modern_rendering`)? Run it against the 225 emic quotes before believing the direction; a low match rate is either a real finding about the records or a sign the gate is unusable as blocking.
- Is a derived multi-GB extract store compatible with the CI budget that was exhausted on 2026-09-10 without content-hash caching, and who owns that cache?

**C — Derived source records.**
- Does "sync owns the bibliographic core" survive contact with the 76 Donatist source records whose `work`/`edition` prose is richer than a bucket row (two records for the same Cyprian council, one per edition)? What is the migration's real match rate when tried on one world?
- What is the stated direction when a bucket row is removed — does a world's synced record vanish, fail, or freeze? `census_sync` never demotes; sources cannot inherit that silently.
- It confines at work grain only. Is that acceptable as a first increment, or does it lock in a grain the shared-compendium files (max 18 traditions on one file) make insufficient?

**D — Attested package.**
- Is a load-time refusal on a bibliographic defect an acceptable production failure mode, given it is the only direction whose blast radius is a participant-facing outage? Under WO-2's lazy loader, is it really contained to one world?
- Is adding role to `grounding_net.check_turn` the same instrument with one more field, or a new per-turn quality police under principle 2? The answer decides whether D's runtime half is even permitted.
- Does the staleness sweep need to become bucket-row-aware to avoid a fleet-wide rebuild on every corpus-map merge, and is that in scope?

**E — Scoped tools and ledger.**
- Is a mechanism that a `Read` call can bypass worth building as anything but the I5 backstop? Ask specifically whether the complement sweep, run today on the file grain against the nine worlds, finds anything — if it finds nothing, that is either reassurance or an inert instrument, and the difference matters.
- Where does the ledger live, given `records/` is hashed into packages and `search_record` is already excluded from `repository.json` but not from the package's `records/` copy?

**Cross-cutting, for all five.**
- Reconcile the two non-exclusivity measurements (section 1.1) with a stated unit, since the grain argument rests on it.
- Confirm the correction in section 1.3 independently: is there any verbatim-against-file check anywhere in the build path that I missed? I searched `engine/` for `verbatim` and for `gate_quote_fidelity` and found only the runtime net and a README mention; a second reader should check `cic/engine/texts_registry.py` and `engine/m1/reports/` before the memo's baseline is trusted.
- Decide whether structured `locus_ids` on staging rows is a classification change (out of scope) or a schema change (in scope). Two of five directions depend on the answer.
- For whichever direction or hybrid converges: what is the seeded defect in `fixtures/seeded_defects.yaml` that proves it fires, and what does the fixture world need (a synthetic bucket, since `fix` has `census_id: null`) for the gate not to be inert on the one world the selftest runs against?
