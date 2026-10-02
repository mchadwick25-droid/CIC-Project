# Library Access Gate — D2 (struggle): adversarial review of the five directions

**Sandbox artifact, 2026-09-15. Phase: D2, the groan zone.** This is a filed
review, not a verdict. It attacks each of Fable's five directions as hard as I
can, then defends each one honestly, then says where its own stated cost or
scope looks optimistic. It does not pick a winner and does not rank. The
convergent decision is Mark's.

Everything numeric below that is not explicitly attributed to the D1 memo or the
tracking doc is my own measurement, run against this checkout today. Where my
read of the code contradicts the memo, I say so and show the line. Where I could
not reproduce a number the charter relies on, I say that too rather than pick
one.

---

## 1. What I re-verified, and what changed

Root `CLAUDE.md` is explicit that a blocking finding "can't be dismissed by
self-certification — it needs independent re-confirmation." That applies to
D1's own findings, so I re-read the same files rather than inherit its
conclusions.

### 1.1 Confirmed — the memo is right

| Claim (D1) | Verified |
|---|---|
| `gate_quote_recording` does **not** check verbatim text against `cic/texts/` | **Confirmed.** `engine/m1/gates.py:192-203` checks only that `license ∈ {verbatim, paraphrase-only, do-not-voice}` and that `text`/`speaker_or_author` are non-blank. |
| No verbatim-against-file check exists anywhere in the build path | **Confirmed independently.** I swept `engine/` and `cic/engine/` for `verbatim`. Every hit is the runtime net (`engine/m4/grounding_net.py`, `grounding.py`), a test, a comment, or the license enum. `gate_quote_fidelity_recording` exists nowhere. `cic/engine/texts_registry.py` has no such function — its surface is `read_header` / `rights_declared` / `rights_clears` / `citing_records`. `engine/m1/reports/` holds only `cell_voice.py` and a JSON report. **So the tracking doc's Question 1c ("checks license validity and verbatim presence in the file") is wrong, and the correction stands.** That sentence should be corrected at its source, since it is currently load-bearing for a decided D5. |
| 18 gates in `GATES` | Confirmed. |
| `tools/gen_shelf.py` writes to `<repo>/worlds/<code>/`, which does not exist | Confirmed — `ls -d worlds` fails; with defaults the tool writes zero shelves and prints "no world directory". |
| `gen_shelf.py` hard-codes world codes, and `gallic` is now registered | Confirmed, and worse than stated: `main()` builds `{**registry_map(), **CANDIDATES}`, so the hard-coded dict **overrides** the one registry. Principle 4 with the precedence backwards. |
| Backfill state | Confirmed: `work_id` on 10 source records, machine-resolvable `address` on 5 quote/story records, `locus` on 358 (Fable's 354 excludes the fixture), `WORKS.yaml` 4 entries. My per-world counts match Fable's table exactly once the `fix` fixture is added back (source 400 vs 398, quote 246 vs 243, story 112 vs 111). |
| `python cic/engine/corpus_map.py`: 836 rows, 55 buckets, roles 649/170/12/5, confidence 681/148/7 | Confirmed exactly. |
| 117 vendored files (38 `.xml`, 79 `.txt`), ~250 MiB | Confirmed. |
| Non-exclusivity re-measure at `(source_file, work)`: 563 distinct, 357 single-tradition, median 1, max 6; file grain 109 files, 64 single, max 18 | **Confirmed to the row.** |
| `fix` has `census_id: null` | Confirmed. |
| `compile_world` reads `records/` + `records/worlds.yaml` only | Confirmed (`engine/m2/compiler.py`). |
| `verify_package_dict` is the refusal point for hash mismatch | Confirmed — and it is 20 lines of pure hashing, which matters for Direction D (below). |
| `observe_corpus_map` does the `census_id` join as an observation | Confirmed (`engine/m1/cross_world.py:914`). |

### 1.2 Could not reproduce — the charter's non-exclusivity figures

The charter and `CiC_Repo_Structure_Tracking.md` (measured 2026-09-14) state:
*"677 staged works; 47 assigned to a single tradition (7%); median work claimed
by 4 traditions; one by 19."*

**The 677 is right.** `cic/corpus-map/_staging/` holds exactly 677 `assignments:`
entries across 115 files. Everything after it is not reproducible at any grain I
could construct:

| Counting unit | distinct | single-tradition | median | max |
|---|---:|---:|---:|---:|
| staging assignment entry, by its own `atlas_ids` list | 677 | **547 (81%)** | **1** | **5** |
| merged `(source_file, work)` pair | 563 | 357 (63%) | 1 | 6 |
| work title pooled across files | 559 | 352 (63%) | 1 | 6 |
| `source_file` alone | 109 | 64 (59%) | 1 | 18 |

Nothing yields 47 / 7% / median 4 / max 19. The nearest thing to "19" in the
data is 18 traditions on `npnf214_seven-ecumenical-councils.xml`, which is a
*file*, not a work. My best reading is that the 2026-09-14 measurement inverted
or mis-joined something, and that the "median work claimed by 4" figure — which
is the single sentence in the charter doing the most rhetorical work, because it
is what makes the library sound irreducibly entangled — **overstates the
entanglement by roughly a factor of four.** The honest statement is: *most works
belong to exactly one tradition (63%); the entanglement is concentrated in a
small number of compendium files.*

This is not pedantry. It changes the shape of the problem. If the median work
were claimed by four traditions, work-grain confinement would be nearly useless
and only locus-grain would do. At median 1 and max 6, **work grain is genuinely
discriminating for most of the library**, and the locus problem collapses to a
named, countable set of shared compendia. Direction C's "work grain only" —
which Fable flags as its chief limitation — is a much better deal than the
charter's numbers imply.

**Open item:** the tracking doc's figures should be corrected at source with a
stated unit, per `CLAUDE.md`'s own "fix the map first, then the list" rule.

### 1.3 Corrections to the D1 memo

**(a) `gen_shelf.py`'s `parse_bucket` is not a usable bucket reader, and must
not be promoted.** The memo proposes it as the ready-made reader for Direction A
("the 14-line `parse_bucket` in `gen_shelf.py` is already that") and Direction D
inherits the same assumption. I ran it against all 55 buckets and diffed every
field against a real `yaml.safe_load`:

- **251 of 836 rows (30%) carry at least one wrong field.**
- **207 `locus` values are wrong; 113 of those are materially truncated.**
  The generated buckets wrap long scalars, and the line reader drops every
  continuation line. Example, `gallic-monastic-ascetic-christianity.yaml`:
  real locus `div1 21, div2 type=Book 'A Treatise on the Gift of Perseverance'
  (structure path 21.3)`; parsed locus stops at `(structure path`.
- **57 `work` titles wrong, 53 materially truncated.**
- `.strip("'\"")` also eats the closing quote of a legitimately quoted value:
  `div1 'Life of Antony'` parses as `div1 'Life of Antony`. YAML's escaped
  apostrophes (`''`) are never unescaped.

The locus field is the *exact* thing Directions A, B, D and E need to resolve.
A reader that silently truncates a quarter of them is worse than no reader,
because it fails open and invisibly. A correct reader already exists twice —
`cic/engine/corpus_map.load()` and `cic/engine/corpus_index.files_for_entry()`,
both real YAML. Whichever direction converges, **the finding is: use one of
those, and treat `gen_shelf.py` as a prototype to be replaced, not a component
to be lifted.** No `SHELF.md` has ever been committed, so nothing downstream has
consumed the truncated output yet. That is luck, not design.

**(b) The `engine/m1` → `cic/engine` boundary is narrower than the memo
assumes.** The memo (following `gates.py`'s own comments) treats "engine/m1
imports nothing from cic/engine" as a package rule, and builds Direction A's
design around it. It is a `gates.py` convention. `engine/m1/cross_world.py:940`
already does `sys.path.insert(...cic/engine)` and imports `corpus_map.load`,
inside a `try/except` that can never fail the fleet run. So the import path
exists and works; what does not exist is a version of it a *gate* could use,
because a gate cannot swallow the exception. This weakens the argument for
writing a second bucket reader inside `engine/m1/` and strengthens the case for
either (i) lifting the observer's import pattern with strict error handling, or
(ii) doing the read outside the gate entirely, which is Direction C's move.

**(c) The staleness claim is backwards.** The memo says Direction D means "the
staleness sweep must learn that a bucket change stales a package (today only
`records/` and the registry do)." It does not need to learn anything.
`staleness_sweep` (`engine/m2/checks.py:54`) recompiles each world with
`compile_world` and diffs every file hash against the pinned manifest. The
moment `compile_world` reads `cic/corpus-map/`, **every corpus-map merge stales
every world automatically, and there is no way to switch it off.** The real
problem is the inverse of the one named: not that staleness will miss bucket
changes, but that it will catch all of them, fleet-wide, and each stale world
needs a repin in `records/worlds.yaml` — the one file every active world branch
already conflicts on (Gate A finding B1). At 100 worlds that is a hundred-line
conflict on every classification edit.

**(d) Package sizes.** The memo says "packages today: 1.5–3.4 MB each."
`packages/don/` is 8.6 MB. Minor, but it is the world every size projection
should be sized against, not the median.

**(e) The biggest one: gates do not block compilation, and never have.**

Every direction in the memo — and D5 itself, and the charter — rests on "a world
whose records cite anything off its shelf fails to compile (WO-4)." No mechanism
in this repo does that.

`engine/m2/validation.py:19` writes gate findings into
`validation/gates-report.json` *inside the package*, with an `overall_pass`
field. `engine/m2/cli.py:33 cmd_build` never reads it. `restore_package` verifies
that the bytes match the pinned manifest — so a package pinned with failing gates
restores green forever. `grep overall_pass` across `engine/` and `.github/` finds
no caller outside M3's admission harness. The M1 selftest CI job runs the battery
against the **fixture world only**.

Verified live: running the current battery against the real fleet, **`don` carries
52 `reciprocity` findings and `syr` carries 1 `voice-perspective` finding, today,
with CI green.** The fleet is already shipping with recorded gate failures.

So the actual effect of adding any new gate is: its findings change
`gates-report.json`'s bytes → every world's package hash changes → the staleness
sweep goes red → someone repins → green again, **findings and all**. "Add a gate"
and "enforce confinement" are two different projects, and only the first is
costed anywhere in D1. Whichever direction converges, **something has to assert
`overall_pass` for real worlds, and that is a separate, unscoped work order that
will turn `don` red on day one for reasons unrelated to shelves.** This is the
single most important thing D1 missed, and it is upstream of all five directions.

---

## 2. The measurement that reframes the whole problem

D1 states I3 ("role-gated voicing") as settled in principle: `tradition` →
voiceable; `context`/`antecedent`/`transmission` → citable as evidence, never
voiced. All five directions implement that mapping. Fable flags one worry —
"`antecedent` is the hard case: Cyprian is on the Donatist shelf precisely so the
Representative can argue from him" — and moves on.

I measured it. For every `register: emic` quote and story record in the fleet, I
resolved each `sources[].source_id` to its source record, pulled the
`cic/texts/` file out of that record's `edition`, and asked what role that file
carries in the world's own bucket:

| world | emic citations | on shelf, `tradition` | on shelf, **no `tradition` row** | **off shelf** | source names no vendored file |
|---|---:|---:|---:|---:|---:|
| alx | 38 | 28 | 9 | 1 | 0 |
| cappadocian | 65 | 45 | 2 | 1 | 17 |
| desert | 67 | 66 | 0 | 0 | 1 |
| don | 31 | **11** | **19** | 0 | 1 |
| gallic | 33 | 32 | 0 | 1 | 0 |
| hal | 47 | 45 | 0 | 2 | 0 |
| ijc | 54 | 46 | 4 | 4 | 0 |
| pahc | 39 | 35 | 4 | 0 | 0 |
| syr | 51 | 32 | 9 | 7 | 3 |
| **total** | **425** | **340 (80%)** | **47 (11%)** | **16 (4%)** | **22 (5%)** |

**I3 as specified fails on 47 citations in the existing nine-world fleet, and on
61% of Donatism's.** Not as a false positive — as the rule working exactly as
written, on a corpus where the rule is wrong.

Look at what the 47 are:

- **alx**: Dionysius of Alexandria's own words, quoted inside Eusebius'
  *Historia Ecclesiastica*. npnf201 is `context` for Alexandria — correctly, it
  is a Palestinian historian writing about them. But the *quoted voice* is
  Alexandria's own bishop.
- **don**: essentially the whole world. Optatus (`context` — an anti-Donatist
  polemicist), the CIL VIII inscriptions (`context`), the Migne *Collatio
  Carthaginiensis* acts (`context`), Monceaux (`context`, modern scholarship).
  Donatism is a tradition known almost entirely through its opponents' books and
  through the records of the tribunal that condemned it.
- **cappadocian**: Julian's own rescript, as `context` — quoted because the
  Cappadocians were the ones it was aimed at.

`cic/engine/corpus_map.py`'s own docstring already knows about this and
explicitly refuses to encode it. It names the "embedded voice" case ("an
opponent's words survive INSIDE a work of this tradition… the quoted voice has no
separate custody relation, and marking one would make every polemic a
transmission") and the "attested-by" case ("a lost work survives as fragments
quoted by a later author — Alexander of Jerusalem via Eusebius. **That is a fact
about the source record, not a relation between an entry and a work.**").

That last sentence is the finding. **Corpus-map's `role` is a property of the
work. Voicing permission is a property of the speaker quoted inside the work.
Every one of the five directions maps one onto the other, and all five are
therefore wrong in the same place.** Direction D is the worst affected because it
would apply the mapping live, per turn, in front of a participant.

Two further structural facts from the same sweep:

- **117 of 400 source records (29%) name no `cic/texts/` file at all.** Modern
  scholarship (Chadwick, Casiday, Monceaux at thesis level), unvendored primary
  texts (Prosper's *Contra Collatorem*), editorial apparatus. `corpus_map.validate()`
  requires every `source_file` to be actually vendored, so **these records can
  never resolve to any shelf row under any of the five directions.** I1 is
  structurally unreachable for nearly a third of the source corpus, and no
  direction says what happens to them.
- **23 of the 283 source records that do name a file name one off their own
  shelf.** 20 are `register: etic` — exactly the context/testimony material the
  role vocabulary exists for, which corpus-map simply has not assigned to those
  buckets. 3 are `emic` and off-shelf (`ijc.source.augustine-confessions`,
  `ijc.source.hilary-de-synodis`, `ijc.source.paulinus-vita-ambrosii`) — those
  three are the only genuine confinement findings the whole existing fleet
  produces at file grain, and 2 of the 3 are cases where the file is in *no*
  bucket at all. Three vendored, cited files (`ammianus-marcellinus_…`,
  `paulinus-milan_vita-ambrosii_…`, `suetonius_lives-…`) belong to zero buckets.

**The consequence every direction inherits:** making any of these gates blocking
requires adding rows — and probably a new role — to `cic/corpus-map/`. That is
classification work, which this workstream's charter puts explicitly out of
scope. The mechanism cannot be finished without commissioning the thing the
mechanism was chartered not to touch. See §5.3.

---

## 3. Direction by direction

### Direction A — Finish WO-4 as specified (compile-time pointer gates)

**Attack.**

1. *The gate is inert where it matters and blocking where it doesn't.* `work_id`
   is on 10 of 400 source records; `address` on 5 of 358. `gate_shelf_membership`
   keyed on `work_id` sees 2.5% of the corpus on day one. `gate_address_within_locus`
   sees 1.4%. Under the selftest's own inertness rule (`engine/m1/selftest.py:73`:
   `overall_pass` requires `not inert_gates`) a gate that never fires fails the
   build — so A cannot ship the gates and defer the backfill. It must ship them
   *with* a complete backfill, or not at all. That converts A from "a few hundred
   lines in house style, a day or two each" into a project gated on ~740 hand
   verifications under a no-guessing rule, and ~4,000 at 100 worlds. The memo says
   this; it does not draw the conclusion that the gates and the backfill cannot be
   sequenced apart.
2. *The gate cannot be admitted at all against the fixture.* `fix` has
   `census_id: null`, and its two source records name `"Fixture Edition 1"` — no
   vendored file. To make a shelf gate non-inert on the fixture you need: a
   synthetic census id, a bucket file, a vendored fixture text, and rewritten
   fixture source records. But `corpus_map.validate()` rejects a bucket whose
   filename is not a real census movement id *and* whose `source_file` is not in
   `cic/texts/`. So the fixture bucket has to live outside `cic/corpus-map/` or
   corpus-map has to learn a fixture exemption. Rewriting `fix.source.witness-scroll`
   also moves the fixture package hash and touches the seeded-defect mutations
   that already target it. **Nobody costed this, and A, C, D and E all pay it.**
3. *The proposed reader is broken.* See §1.3(a). A's step 1 names `parse_bucket`
   as the shape to lift; it truncates 113 locus values. A's step 3 then asks that
   truncated locus to be resolved to div ids.
4. *`WORKS.yaml` as the join key does not survive its own header.* The file says
   in its own text: hand-maintained, append-only, one file "is enough at this
   size," expand "as work actually needs a join," never guess an identifier, and
   *"if this grows past what one person can safely edit at once, adopt corpus-map's
   staging pattern."* A requires it to go from 4 entries to several hundred
   immediately and several thousand at fleet scale, written by many concurrent
   world threads. A is asking the registry to become the thing its own author said
   to stop doing before it got there.
5. *A corpus-map re-merge is a fleet-wide red.* A work renamed or re-assigned
   turns every world citing it red at once. Principle 6 wants failure direction
   stated per check; "N worlds fail to build because a classification thread
   corrected a title" is a stated direction, but it is also a standing incentive
   not to correct titles.
6. *`confidence` is ignored.* 155 rows are `provisional` or `needs-ruling`. A
   provisionally-assigned `tradition` work is fully voiceable under A. That is a
   real permission granted by silence.

**The gallic absence case, concretely.** `gallic.source.augustine-letters-221-226-absence`
has `register: etic`, `sources: []`, **no `work_id`**, and names
`cic/texts/npnf101_augustine-confessions-letters.xml` only in `edition:` prose.
npnf101 is in six buckets, none of them gallic's. Under A today, the record is
**invisible**: `gate_shelf_membership` keys on `work_id`, which is absent, so the
record passes silently. `gallic.contested.beginning-of-good-will` cites it via
`source_id` with no `address`, so `gate_address_within_locus` skips that too.
So A's answer to the hardest case in the fleet is not "it fails and needs an
exemption" — it is "it never gets looked at." That is a cleaner statement of the
same problem: **A's day-one behaviour on the one record everyone worries about is
exactly the inertness principle 12 forbids.** The exemption only becomes necessary
once `work_id` is made required, and at that point no `WORKS.yaml` entry can
legitimately be written for it, because there is no work — the record's subject is
an absence.

**Defence.**

A is the only direction that is already a *decision*. D5 chose it, the tracking
doc records the reasoning, and WO-4 is written down. Re-opening it costs the
project something real. It is also the only direction that needs no new module,
no new artifact store, no schema bump, and no change to the runtime or the
package format: three functions in `engine/m1/gates.py`, in the exact shape the
other 18 already take, admitted through the exact bar the other 18 were admitted
through. The blast radius of getting it wrong is a CI failure, not an outage and
not a rewritten corpus.

And the backfill, while expensive, buys something none of the other directions
buy: `work_id` and `address` are *durable, reusable identifiers*. Once a record
carries `cic:npnf105_…:div1 21.3`, every later question — which world cites this
passage, has this passage moved, is this the same work as that one — is
answerable mechanically. Directions B, C and E all leave the corpus exactly as
illegible as it is now and put the intelligence in the tooling. A puts it in the
records, which is where `records = what's true` says it belongs. If the fleet is
really going to 100 worlds and a 10× library, the argument that you should pay
once per record to make records self-describing is not a weak one.

**Where A's own cost claim looks optimistic.** "A day or two each with tests and
seeded defects" is credible for the gate functions and not credible for the gates
as *admissible* artifacts — the fixture problem in point 2 is a multi-day project
on its own, before the first backfilled record. And "Backfill: `work_id` on ~388
source records" quietly assumes all 388 *can* carry one; 117 of them name no
vendored work at all, and a further 23 name a work on nobody's shelf. The honest
backfill number is ~260 records that can be joined, plus ~140 that need a
decision nobody has made.

---

### Direction B — Bytes, not pointers (materialized per-world extract + verbatim gate)

**Attack.**

1. *Fail-closed on shared whole-file units blocks the two worlds that need it
   most.* This is B's own stated rule ("the gate must fail *closed* on a shared
   whole-file unit"). Fable asked D2 to measure how big that hole is. I did.
   Walking `corpus_index.passage_units` over all 117 vendored files: **16 files
   are shared by two or more traditions and collapse to a single passage unit.**

   | traditions | size | file |
   |---:|---:|---|
   | 4 | 3.49 MB | `npnf205_gregory-nyssa-dogmatic-treatises.txt` |
   | 4 | 0.64 MB | `ephraim_prose-refutations_mitchell1912-1921.txt` |
   | 4 | 0.55 MB | `palladius_paradise-v1-syriac_budge1907.txt` |
   | 3 | 3.55 MB | `theodosianus-16_mommsen-meyer1905.txt` |
   | 3 | 1.78 MB | `codex-theodosianus_latinlibrary.txt` |
   | 3 | **0.70 MB** | **`optatus_against-the-donatists.txt`** |
   | 3 | 0.47 MB | `origen_philocalia_lewis1911.txt` |
   | 3 | 0.25 MB | `philostorgius_ecclesiastical-history_walford1855.txt` |
   | 2 | **5.10 MB** | **`pl11-zeno-optatus-collatio-carthaginiensis_migne.txt`** |
   | 2 | 2.20 MB | `prosper_chronica-minora-1-lat_mommsen1892.txt` |
   | 2 | 1.13 MB | `codex-canonum-ecclesiae-africanae_bruns-pars1-1839.txt` |
   | 2 | 0.89 MB | `anan-isho_paradise-v2-sayings_budge1907.txt` |
   | 2 | 0.20 MB | `julian_letters-1-73_wright1923.txt` |
   | 2 | 0.07 MB | `aphrahat_demonstrations-2-7_hallock1932.txt` |
   | 2 | 0.05 MB | `chronicle-of-edessa_cowper.txt` |
   | 2 | 0.05 MB | `eunomius_first-apology_whiston1711.txt` |

   The two bolded rows are Donatism's entire documentary base and the *Collatio*
   acts. `theodosianus-16` is ijc's legal spine. **B's fail-closed rule, applied
   today, blocks Donatism and Imperial-Juridical Christianity outright** until
   someone hand-marks multi-megabyte plain-text files. That is not a cost B can
   absorb late; it is the first thing that happens when B is turned on.
2. *Amplification, measured.* Fable estimates "average shelf 30 MB, 100 worlds
   ≈ 3 GB." Summing the bytes of each bucket's files across the **existing 55
   buckets** gives **1,064 MB over a 250 MiB library — 4.1× amplification**. The
   nine built worlds alone are 355 MB. That ratio will rise, not fall, as the map
   fills (only 109 of 117 files are assigned at all today, and 46 of the 55 buckets
   serve worlds that do not exist yet). At 100 worlds over a 2.5 GB library the
   honest projection is ~10 GB of derived extract, not 3 GB. Locus-grain extraction
   reduces this for the 38 XML files and reduces it *not at all* for the 16
   single-unit shared files above, whose extract is the whole file by definition.
3. *CI.* `.github/workflows/ci.yml`'s `engine` path filter is
   `engine/** records/** packages/** fixtures/** cic-website/data/world-census.json
   .github/workflows/**`. It contains **neither `cic/corpus-map/**` nor
   `cic/texts/**`.** B requires both to be added, which means every corpus-map
   merge and every vendoring fires the full engine battery — four `restore` jobs
   plus the staleness sweep — across every world. That is precisely the shape that
   exhausted the Actions budget on 2026-09-10, and B is the direction that adds
   the most work per fire.
4. *The normalization trap is a source-fidelity risk, not just an engineering
   one.* The memo says it well and then under-weights it. `CLAUDE.md`'s "never
   invent" exists because misattributed and mis-transcribed quotes are "a real,
   recurring defect here." Every tolerance added to a window-matcher so an English
   rendering matches a Latin witness is a small licence to be wrong about bytes.
   The failure mode is not a red build; it is a gate that quietly accepts a quote
   it should have rejected, while the project believes bytes are now verified.
   A gate that is trusted and slightly wrong is worse than the honest human step
   it replaces.
5. *Coverage is narrower than the pitch.* The verbatim gate reaches `license:
   verbatim` quotes only. Of 246 quote records, `paraphrase-only`,
   `do-not-voice`, `modern_rendering`, all 112 stories, 155 doctrinal witnesses
   and 272 terms are reached only by ratio instruments the project keeps
   report-only under principle 10. So I4 is genuinely solved for maybe a third of
   the voiced material and asserted for the rest.
6. *The shared-work case it explicitly cannot decide.* A quote appearing in two
   traditions' extracts passes in both. B's own text concedes this and hands it
   to corpus-map. Fair — but it means B's strongest claim ("check that the text
   *is in* the world's own slice and nowhere it shouldn't be") is only half
   delivered: it checks presence, never exclusivity.

**The gallic absence case, concretely.** B survives it, by not looking at it. The
absence record quotes nothing, so it is outside the verbatim gate's domain
entirely; `gallic.contested.beginning-of-good-will` is a `contested_claim`, not a
quote, likewise outside. This is honest and it is also the precise limit of B:
**B has nothing to say about `source` records at all.** I1 for sources is
unaddressed, which the memo admits in one clause and then does not carry into its
cost. In a world where 400 source records exist and 23 of them are off-shelf, B
leaves the whole of that surface untouched.

**Defence.**

B is the only direction that closes I4, and I4 is the invariant this project
believed it had and did not. Given that `CLAUDE.md` names verbatim
re-verification as a standing discipline and that the tracking doc's claim about
it was simply false, there is a strong argument that the first thing to build is
the check everyone thought existed. Everything else on this list guards a pointer;
only B guards the sentence a participant will read.

Its cost structure is also the best of the five in one specific way: **the
resolver work is per-file, not per-record.** Structuring `optatus_against-the-donatists.txt`
once serves every world that ever cites it, forever. A's backfill is per-record
and grows linearly with the fleet; B's is per-file and amortizes across it. At
100 worlds over 1,000 files that difference is the whole argument.

And B is the only direction whose failure output is legible to a human. A dangling
`work_id` tells you a string did not match. B tells you *which passage left the
shelf*. For a project whose review discipline is humans re-reading findings, that
matters more than it sounds.

Finally, B alone gives the authoring side something real for free: a build thread
told to read `shelf/<world>/` instead of `cic/texts/` is confined at the point of
reading, which is where leaks actually begin.

**Where B's own cost claim looks optimistic.** "The extractor is small (the unit
walker exists)" — true, and irrelevant next to the marker work. "A single extract
could be tens of MB" understates it: the measured file-grain upper bound for `ijc`
alone is 62 MB and for `alx` 55 MB. "Caching by content hash is not optional here"
is right, and the memo does not name an owner, a store, or a size budget for a
multi-gigabyte derived artifact that CI must produce on every run. The project has
been here before: `cic/texts/INDEX.sqlite` is uncommitted and ungenerated in CI
today, which is the same problem at 1/10th the size, unsolved.

---

### Direction C — Derive, don't check (source records synced from the bucket)

**Attack.**

1. *`census_sync` is not the precedent C claims.* `engine/m6/census_sync.py`
   writes into `cic-website/data/world-census.json` — a downstream, generated view.
   C writes into `records/`, which is the authored corpus, copied **byte-for-byte**
   into every package and hashed by the manifest (`compiler.py::_frozen_records_copy`).
   That is not the same operation wearing a different hat. It means **every
   corpus-map re-merge rewrites records and repins packages**, not once at
   migration but forever. A classification thread fixing a work's title becomes a
   commit touching N worlds' records, N package hashes, and `records/worlds.yaml`
   — the file Gate A finding B1 already identified as the cross-branch conflict
   point. The memo calls this "same repin churn as A"; it is not. A's churn is a
   one-time backfill. **C's churn is permanent and proportional to corpus-map's
   edit rate.**
2. *`census_sync` only ever advances; sources cannot.* The module's own comment:
   "status: only ever advances toward Built & Live, never demotes or invents a
   not-yet-built category the registry has no concept of." That monotonicity is
   what makes it safe to run unattended. Source sync has no monotone direction: a
   bucket row can be removed, re-roled, re-loci'd. The memo raises this as an open
   question. It is more than that — **monotonicity is the property that made the
   m6 pattern safe, and C cannot inherit it.** Without it, `sync` is a tool that
   can delete a hand-annotated record's core because a classification thread
   changed its mind, and `check` is a CI job that goes red for reasons no world
   thread controls.
3. *Work grain is not the limitation the memo thinks, but it is still a
   limitation on the files that matter.* Per §1.2, work grain discriminates for
   63% of works outright and median-1 overall — better than the charter implies.
   But the entanglement is concentrated exactly where worlds actually read:
   `npnf214` (18 traditions), `anf08` (16), `anf07` (16), `anf06` (13), `anf05`
   (10), `npnf203` (9). C confines you to *a work inside* `anf05`; it never checks
   that the passage you quoted is inside that work. For Cyprian-in-`anf05`,
   shared with ten traditions, that is a real gap.
4. *The migration's match rate is unmeasured and looks poor.* The memo estimates
   "a *copy* of a string that exists, not the invention of an identifier." I
   checked the join it depends on. Of 400 source records, **117 name no
   `cic/texts/` file at all** — there is no bucket row to copy from, because
   corpus-map only holds vendored works. A further 23 name a file that is not in
   their own bucket. So the sync can produce a `shelf` block for at most 260 of
   400 records (65%), and the remaining 140 need a hand-made decision per record.
   The memo's "one-time 398-record pass" is really "a 260-record mechanical pass
   plus a 140-record policy problem."
5. *Sync owns the block, not the claim.* C's own admission — a record's
   interpretive fields can claim more than the bucket row does — is sharper than
   it reads. `don.source.optatus-against-the-donatists` would sync cleanly with
   `role: context`, and then 19 emic Donatist quotes would cite it anyway. C
   makes the role *visible on the record*, which is genuinely useful, and does
   nothing at all about the 47-citation problem in §2.

**The gallic absence case, concretely.** This is where C is weakest, and the memo
gets the mechanism wrong. Fable proposes `kind: absence` records carry a synced
block "carrying the file and `role: absence`." But there is **no gallic bucket row
for npnf101 to sync from** — the file is in six other buckets and not this one.
A derived field cannot be derived from a row that does not exist. So the absence
record's `shelf` block would have to be **hand-authored inside a sync-owned
field**, which directly contradicts C's founding premise ("the only way a source
record's core comes into being is `sync`"). The alternatives are both worse:
either corpus-map gains an `absence` role and a gallic row for npnf101 — a
corpus-map schema *and* classification change, out of charter — or `gate_source_shelf_sync`
grows a hard-coded exemption class that is exactly the hand-maintained join C
exists to abolish. **C does not have a coherent answer to the gallic case, and
the same problem recurs for all 117 unvendored-source records.**

**Defence.**

C is the only direction that is a straightforward instance of this codebase's
own house style: a pure function plus a thin `sync`/`check` CLI plus a CI gate,
135 lines of precedent sitting in `engine/m6/` written three weeks ago. It needs
no new gate admitted through the seeded-defect bar, no fixture bucket, no
extract store, no schema bump, no runtime change and no `WORKS.yaml` growth. If
the question is "what can actually be built and merged in this repo in a week
without a change order against three other decisions," C is the answer.

It is also the only direction that makes the package **self-describing about
voicing permission**. Once `shelf.role` travels on the source record, it is in
`repository.json`, which means the runtime already has it — which is the
difference between Direction D's runtime role check being "one more field on an
existing instrument" and being "a new input to the live path." C is the
enabling move for half of D (see §4).

And its ongoing cost genuinely does go down rather than up. A new world's source
records scaffold from its bucket in one command — which is exactly what Step 2
(Source Ecology) does by hand today, nine times so far and 91 more to come. At
100 worlds that is the only direction here whose per-world marginal cost is
negative.

**Where C's own cost claim looks optimistic.** "Ongoing cost goes *down*" is true
for authoring and false for maintenance — see point 1, the permanent repin churn.
"A *copy* of a string that exists" is true for 65% of records. And "`m6` is a
direct template" is true of the code shape and false of the safety property
(monotonicity) that made the template trustworthy.

---

### Direction D — The attested package (shelf travels in the package; loader is the choke point)

**Attack.**

1. *The threat model does not hold up.* D's stated justification is that
   compile-time gates can be bypassed: "a gate can be edited on a branch, a stale
   package can be pinned, or a package can arrive from object storage (WO-1) built
   elsewhere." But `compiled/shelf.json` is built by the same compiler, in the same
   repo, on the same branch, and pinned by the same `manifest_hash` in the same
   `records/worlds.yaml`. **Anyone who can edit `gates.py` on a branch can edit the
   shelf builder on the same branch.** A stale pinned package is already caught by
   the staleness sweep. And the manifest hash pinned in the registry already proves
   an object-storage package is byte-identical to what CI compiled. D adds a second
   lock to the same door, keyed to the same key. The one case it genuinely covers —
   a package compiled by an *older* compiler version whose gates did not exist yet —
   is already what `compiler_version` and staleness exist for.
2. *It changes what `verify_package_dict` is.* That function
   (`engine/m2/loader_stub.py`) is 20 lines: recompute the manifest hash, compare
   every file hash, raise. It has no JSON-schema knowledge, no record semantics,
   no concept of a citation. D turns it into a semantic policy validator that
   parses `quotes.json` and `repository.json` and resolves sources against a shelf.
   That is a category change to the one piece of the system whose whole value is
   that it is small enough to be obviously correct. Its docstring's own framing —
   "a wrong world is worse than an absent one" — was written about *corrupted
   bytes*, not about bibliographic policy.
3. *It breaks `compile_world`'s stated determinism contract.* The compiler's
   docstring: "Same world_key + records tree content + package_id + records_commit
   + compiler_version in => byte-identical package … every time (Artifact-2 §3, the
   stage-2 gate)." Reading `cic/corpus-map/` adds an input that is in none of those
   five and is not named by `records_commit`. The determinism check would still
   pass (it calls the function twice against the same disk), so **the contract
   would become false while the test that guards it stayed green.** That is the
   worst kind of drift.
4. *The runtime role cut would withhold correct sentences at a measured rate.*
   §2's table is the refutation. `check_turn` currently withholds a sentence when
   its quoted span is not verbatim in a tagged record. Adding "…or when the tagged
   record's shelf role is not `tradition`" would withhold **11% of grounded emic
   citations fleet-wide and the majority of Donatism's**. These are not false
   positives to be tuned away; they are the specification applied to a corpus it
   does not fit. A Donatist Representative that cannot quote Optatus cannot speak,
   and the participant-visible symptom is `degraded_by_net` — the world going
   hollow, which `CLAUDE.md` names as a failure ("held": doesn't cave or go hollow
   under real pushback).
5. *It is the only direction whose blast radius is a participant-facing outage.*
   The memo says this. I would put it more sharply: fail-closed at load means a
   **bibliographic** defect produces an **availability** incident. Under WO-2's
   lazy loader it is contained to one world, which is true and is not much comfort
   if the world is the one someone opened. And a format bug in `shelf.json` refuses
   every world at once.
6. *Every corpus-map merge stales the entire fleet, unavoidably.* See §1.3(c).
   At 100 worlds, one classification edit means 100 recompiles and 100 registry
   repins in the file every branch conflicts on.

**The gallic absence case, concretely.** D refuses a `repository.json` record
"whose sources resolve to no `shelf.json` row." `gallic.source.augustine-letters-221-226-absence`
has `sources: []` — it resolves to nothing. So D faces a dilemma with no good
horn: if "no sources" refuses, **gallic goes offline in production because of a
correctly-authored absence record**; if "no sources" passes, the check is
trivially evaded by omitting `sources`. And it gets worse one hop out:
`gallic.contested.beginning-of-good-will` carries nine `sources[]` entries, of
which the absence record, Prosper's *Contra Collatorem* ("unvendored"), Chadwick
and Casiday ("thesis-level, not read") and the NPNF editorial apparatus can none
of them resolve to a gallic shelf row. Under D as written, **gallic refuses to
load.** Not because anything is wrong with it — because a contested claim did its
job and documented what the library does not contain.

**Defence.**

D is right about one thing nobody else addresses: **WO-1 puts packages in
object storage, and at that point the repo is no longer the thing serving the
world.** A package that carries its own attestation can be audited offline, by
`engine/m7`, without a checkout — and "can you prove, from this artifact alone,
that this world only drew on its own tradition" is a question this project will
eventually be asked by someone who is not Mark. None of A, B, C or E can answer it
from the artifact.

D is also the only direction that puts the shelf where `records = what's true`
would actually put it: inside the sealed thing, hash-chained, versioned with the
package, rather than in a repo file that can drift out from under a package that
was built last month. If confinement is a property of a *world as served*, and the
package is the seal, then the attestation belongs in the seal. That is a coherent
and arguably more principled reading of D5 than A's.

And its *compile-time* half — emit `compiled/shelf.json` with a per-record
coverage map — is cheap, non-blocking, and immediately useful as an observation
even if the loader never refuses anything. Split from its load-time and runtime
halves, that half is close to free and is the best audit artifact on this list.

**Where D's own cost claim looks optimistic.** "A schema bump, a rebuild of nine
packages, changes to the loader's refusal logic and its tests" omits the
determinism contract (point 3), the Docker image (`engine/Dockerfile` deliberately
excludes `cic/corpus-map/`: "cic/corpus-map/ and cic/engine/ … are deliberately
left out" — D's builder runs inside `restore` inside the image build, so the image
must now carry corpus-map, a change order against an explicit decision), and the
fleet-wide staleness consequence. And the claim D2 was asked to test — "it is not
a new per-turn police if it is genuinely the same check with role awareness" — is
**false as D stands and true only on top of C**: `check_turn`'s signature is
`(tagged_text, repository_records, *, thin_topics, grounding_floor)`. The role is
not in `repository_records` unless something put it on the record. D alone must
add a parameter, and a new input to the live path is a new instrument. C's synced
`shelf.role` block is what makes D's own claim true.

---

### Direction E — Confine the reader (scoped tools + access ledger + complement sweep)

**Attack.**

1. *The hard half is incompatible with legitimate research, and the gallic record
   proves it.* `gate_cited_is_opened` requires (i) every `cic/texts/` path in a
   record's `locus`/`edition` to appear in the world's ledger, and (ii) every
   ledger entry to be on-shelf. The gallic absence record was established by a
   builder reading npnf101 — **an off-shelf file** — in full, to establish that
   Letters 221-226 are not in it. Under E, `shelf_open('gallic', 'cic:npnf101…')`
   **refuses the read that produced the record**, and the record then fails both
   halves of the gate: it names an off-shelf path, and no ledger entry exists
   because the tool would not permit one. E is the only direction where the gallic
   case breaks the *tool*, not just the gate. The memo does not notice this at all;
   it discusses only E's ledger bloat.

   The general form is worse than the instance. Establishing an *absence* requires
   reading off-shelf. So does establishing that a neighbouring tradition's
   attribution is wrong, or that a modern scholar misread a passage. A confinement
   mechanism that forbids reading outside the shelf forbids the class of research
   that makes confinement claims checkable.
2. *It is advisory, and the memo knows it.* A `Read` on `cic/texts/` leaves no
   trace. So the ledger gate does not measure what was read; it measures what was
   read *through the tool*, which is a measure of compliance, not of confinement.
3. *The complement sweep's discriminating power is unmeasured and structurally
   weak.* The complement of a world's shelf inside a shared file is, by
   construction, the *same file* — often the same single passage unit, for the 16
   single-unit shared files in §3/B. For `optatus_against-the-donatists.txt`,
   shared by three traditions at one unit, the "complement" is the identical text.
   A ratio instrument comparing a Donatist story against a complement that is
   byte-identical to its own shelf will report high overlap for every story, which
   is noise, not signal. **E's only claim to I5 rests on an instrument that cannot
   discriminate on exactly the files where confinement is hardest.**
4. *Ledger placement has no good home.* Inside `records/`, every open becomes a
   hashed record file in the package (`search_record` is excluded from
   `repository.json` but *not* from `_frozen_records_copy`, which copies every
   parsed record's bytes). Outside `records/`, it is outside the hash chain and
   therefore not evidence. There are already 110 `search_record` files; hundreds
   of opens per world × 100 worlds is a five-figure file count with no owner.
5. *The scaling risk is human and the memo says so.* "Disciplines drift — the
   ledger gate is what notices." But the ledger gate notices only drift *by
   sessions that used the tool*, which is the population that did not drift.

**Defence.**

E is the only direction that addresses I5 at all, and I5 is the only invariant
that describes the failure everyone is actually afraid of: a Representative that
sounds like a neighbouring tradition because a build session read the wrong book,
with no citation to catch it. A, B, C and D all check citations. A world can be
thoroughly wrong with perfect citations.

E is also the cheapest thing on this list by a wide margin, and the only one that
acts *before* the defect is written rather than after. `cic/engine/corpus_index.py --entry`
already scopes search to a bucket's files, using a correct YAML reader
(`files_for_entry`, line 135). Pointing build briefs and the `cic-build-cycle`
skill at it is a documentation change. That is a real reduction in leak
probability for approximately zero engineering, available this week, compatible
with every other direction, and it does not touch a single record byte or package
hash.

And E's report-only half is the correct shape under principle 10: measure first,
earn a bar later. Fable's own probe is the right one — *run the complement sweep
today, on the nine worlds, at file grain, and see whether it finds anything.*
Nobody has. That measurement is cheap and it is the difference between E being a
backstop and E being theatre.

**Where E's own cost claim looks optimistic.** "No record backfill" is true and
the gate is then inert on the whole existing fleet — which, per the selftest's
inertness rule, means it cannot be admitted as a gate at all until addresses
exist. So E's hard half is blocked behind A's backfill, and E's honest near-term
scope is: scoped tools (documentation), plus one report-only instrument. That is
a smaller and much better proposal than the one written, and it should be costed
as such.

---

## 4. Do the combinations actually cohere?

Fable's §4 gestures at combination. Tested:

**C + B — genuinely complementary, least overlap.** C confines at work grain via
derived strings on the record (I1, I3-as-specified); B confines at locus grain via
bytes (I2, I4). They share one dependency (a correct bucket reader), they touch
different fields, and their failure messages do not overlap. C's synced
`shelf.role` also tags B's extract units for free, which is a real saving rather
than a coincidence. **This is the only pairing where the second direction makes
the first cheaper rather than merely adding to it.** The combined cost is still
dominated by B's marker work on the 16 shared single-unit files, and both need
`cic/corpus-map/**` added to the CI path filter.

**C + D — coherent, and D depends on it.** Per §3/D, D's runtime claim ("the same
instrument with one more field") is only true if the role is already on the
record, which is C's move. And D's `compiled/shelf.json` becomes near-trivial if
`repository.json` already carries the synced block. So the honest statement is not
"C and D combine" but **"D's runtime half is not buildable as specified without
C."** That is a sequencing constraint Mark should know about before treating them
as independent options.

**A + B — additive cost, duplicated failure surface, and no stated precedence.**
Both check the same citation, at different grains, with different inputs and
different backfills (A: `work_id`/`address`/`WORKS.yaml`; B: `locus_ids` +
markers). The failure modes cross: a quote can fail A (its `work_id` resolves off
shelf) and pass B (its bytes are in the extract), or the reverse. **Nobody has
stated which wins**, and "both must pass" means the union of two incomplete
backfills blocks the fleet. This pairing is where "hybridize" would be a mistake.

**A + D — near-pure duplication.** D's `shelf.json` is built by the same reader
A's gate uses, checking the same facts, against the same bucket, at a second
moment inside the same pipeline. Per §3/D point 1, the second check adds real
coverage only for packages this repo's CI did not build — which does not exist
until WO-1, and is already covered by the pinned manifest hash when it does.

**E + anything — the report-only half composes with everything; the ledger gate
composes with nothing.** The scoped tools and the complement sweep conflict with
no direction and cost nearly nothing. `gate_cited_is_opened` conflicts with every
direction, because it forbids the off-shelf reads that absence records, attribution
corrections and contested claims require. **E should be split in two before it is
compared to anything.**

---

## 5. Cross-cutting

### 5.1 Which invariants does no single direction actually satisfy?

| | I1 citation on shelf | I2 locus within work | I3 role-gated voicing | I4 bytes match | I5 influence | I6 runtime seal |
|---|---|---|---|---|---|---|
| **A** | work grain, gated on a field present on 2.5% of records | needs `address` (5 of 358) | as specified — see below | no | no | unchanged |
| **B** | sources untouched | yes, except the 16 shared single-unit files | partial, via extract tags | **yes**, for `license: verbatim` only | no | unchanged |
| **C** | work grain, derived — cleanest reach | no | as specified — see below | no | no | unchanged |
| **D** | mirrors whatever it is given | no | as specified, **live** | no | no | **weakens it** (availability) |
| **E** | file grain, via ledger | yes, if `locus_ids` exist | no | no | report-only, and blind on shared single-unit files | unchanged |

**I3 is the invariant no direction satisfies, and all five fail it identically.**
Not through under-implementation — through a specification error. Per §2, 47 of
425 emic citations in the existing fleet resolve to on-shelf files with no
`tradition` row, including 61% of Donatism's. All five directions map "work's
role" onto "voicing permission." `corpus_map.py`'s own docstring already says
that mapping does not hold for embedded and attested voices, and refuses to
encode it. **There is no version of I3 that can be implemented against
corpus-map's current role vocabulary without breaking Donatism.** That is a
design finding, not an engineering one, and it belongs to Mark.

**I4 is the invariant only one direction reaches**, and B reaches it for roughly
a third of voiced material. Given that the project *believed* I4 was already held
and it is not, this gap is the largest distance between what the tracking doc says
is true and what is true.

**I1 has a floor no direction can cross**: 117 of 400 source records (29%) name
no vendored work, so corpus-map — which validates that every `source_file` is in
`cic/texts/` — has no row for them and never will. Every direction needs a stated
rule for "cited, real, and outside the library." None has one.

**I5 is reached only by E, only report-only, and structurally blind** on the shared
single-unit files where it would matter most.

**I6 holds today by construction** (`compile_world` reads only `records/`;
`run_voice_turn_for_world` scopes to one package). The only direction that touches
I6 makes availability worse, not isolation better.

### 5.2 Which directions fit this codebase's house style?

The house pattern, read directly from `engine/m2` and `engine/m6`: **a pure
function with no I/O that the determinism check can call twice in memory; a thin
CLI that does wall-clock, git and filesystem work; a CI job that runs `check` and
returns non-zero.** `census_sync.py` is 135 lines and `m6/cli.py` is 62, with
`sync` writing and `check` diffing — its own docstring says "Same shape as
engine/m2/cli.py's build/staleness-check pair."

- **C is a direct instance.** It is the m6 pattern applied to a second join. It
  needs no gate admitted, no fixture bucket, no schema bump, no new artifact
  store. If "fits the house style" is the criterion, C wins it outright — with the
  caveat in §3/C that it inherits the *shape* of m6 without the *monotonicity*
  that made m6 safe.
- **B is a clean instance of the pattern and a bad fit for the house economy.**
  Pure extractor, thin CLI, cached artifact — textbook. But a multi-gigabyte
  derived store that CI must regenerate is against the grain of a repo whose only
  comparable artifact (`INDEX.sqlite`) is uncommitted and ungenerated in CI to
  this day, and whose Actions budget has already been exhausted once.
- **A is house style for `engine/m1` specifically** — three more functions in a
  battery of 18, admitted through the seeded-defect bar. The catch is that the bar
  is real and A cannot currently clear it: §3/A point 2.
- **D is the least house-style of the five**, because it is the only one that
  changes *contracts* rather than adding modules — `package_schema` 1→2,
  `compile_world`'s documented input set, `verify_package_dict`'s nature, and the
  Docker image's deliberate exclusion of `cic/corpus-map/`. Principle 11 ("risky
  substitutions land last and alone") is aimed at exactly this shape.
- **E is not an engine module at all.** Its cheap half is documentation and a
  flag on an existing tool; its expensive half is a gate that cannot be admitted
  until addresses exist.

### 5.3 The real fork in the road

It is not "pointers or bytes." A and B are not alternatives — A guards the
citation, B guards the sentence, and the memo's own combination section already
concedes they answer different questions. Presenting them as rivals is the false
fork.

The real fork has two prongs, and both are Mark's, not an engineer's:

**Fork 1 — is the confinement gate allowed to drive corpus-map work, or must it
stay strictly downstream of it?**

The charter says: *"Judging which works belong to which tradition is
`cic/corpus-map/`'s job and stays out of scope here."* But the measurements say
that no direction can be made blocking without corpus-map changing:

- 23 source records cite files not in their own bucket; 3 cite files in *no*
  bucket (`ammianus`, `paulinus-milan`, `suetonius`).
- 47 emic citations resolve to on-shelf files with no `tradition` row.
- 117 source records cite material corpus-map structurally cannot hold.
- B's locus grain needs `locus_ids` on staging rows — a corpus-map *schema*
  change, which the memo correctly flags as needing a ruling on whether it is in
  scope.
- I3 as specified may need a *new role* (or a per-source-record "attested voice"
  flag) to express "this tradition's own voice, preserved inside another
  tradition's book."

If the answer is "stay downstream," then every direction ships report-only for a
long time, and the workstream's deliverable is an instrument plus a worklist for
the classification thread — which is a legitimate and honest outcome, and should
be named as one rather than arrived at by attrition.

If the answer is "the gate may drive it," then the real first deliverable is not
a gate at all: it is the ~190-item corpus-map worklist the measurements above
already produce, and the mechanism follows it.

**Fork 2 — is voicing permission a property of the work, or of the speaker inside
the work?**

Every direction assumes the former. Donatism, Alexandria-via-Eusebius and the
Syriac transmission corpus say otherwise, at 47 measured citations. This is a
Representative-voice question — `CLAUDE.md`'s default table says "Representative
identity, title, or voice decision: **Always ask**" — and it cannot be settled
inside an enforcement-architecture choice. Until it is settled, I3 is
unimplementable and three of the five directions are half-specified.

Everything else — grain, storage, which module, when it blocks — is downstream of
those two.

---

## 6. Open questions for Mark

Not ranked, not a recommendation. One question at a time, in the order I think
they unblock each other.

1. **Scope.** Does this workstream's mechanism get to require changes to
   `cic/corpus-map/` — new rows, a new role, a `locus_ids` field — or must it
   confine itself to what the map already says? Every direction's answer to "can
   this ever be blocking?" turns on this, and the charter currently says no while
   the data says it must.

2. **Voicing.** Is a tradition's own voice, quoted inside another tradition's
   work (Dionysius inside Eusebius; the Donatist bishops inside Optatus and inside
   the Carthage acts), voiceable by that tradition's Representative? If yes, the
   role→voice mapping in all five directions is wrong and needs replacing; if no,
   Donatism loses 61% of its emic citation base. This is a voice decision, not an
   engineering one.

3. **Enforcement.** Given that gate findings currently do not block anything
   (§1.3(e)) and that `don` ships today with 52 recorded findings, what is
   supposed to make confinement *enforced* rather than *recorded*? Is asserting
   `overall_pass` for real worlds in CI part of this workstream, or a separate
   work order? It has to exist somewhere or every direction is a report.

4. **Unvendored sources.** 117 of 400 source records cite real material that the
   library does not and may never hold — modern scholarship, unvendored primary
   texts, editorial apparatus. What is the rule? Exempt by a `kind:` field?
   Required to be `register: etic`? Barred from `sources[]` on emic records?
   Whatever it is, it is a `engine/m1/schemas.py` change order and every direction
   needs it.

5. **Absence records.** Does a source record documenting what an edition does
   *not* contain get an explicit schema kind, and does it carry a standing licence
   to cite off-shelf? Related: does the build process get to *read* off-shelf to
   establish an absence — which is the question Direction E's scoped tools answer
   "no" to by construction.

6. **Corpus-map churn.** If a bucket edit stales every world that cites the
   affected work (automatic under C and D, unavoidable), who repins, and does
   `records/worlds.yaml` need to stop being one file before that is survivable at
   100 worlds? Gate A finding B1 already named this file as the cross-branch
   conflict point.

7. **Two measurements worth commissioning before D3, both cheap:**
   (a) run E's complement sweep today at file grain against the nine worlds — if
   it finds nothing, I5 has no evidence of being a live problem and E's expensive
   half can be dropped; if it finds something, that is the first hard evidence any
   of this is needed. (b) run B's verbatim window-match against the 225 emic
   quotes before costing B — a low match rate is either a real finding about the
   records or proof the gate cannot be blocking.

8. **The fixture.** Admitting any shelf gate requires `fix` to have a census id, a
   bucket, a vendored fixture text and rewritten source records, and requires
   `corpus_map.validate()` to tolerate a synthetic bucket. Is building a
   confinement fixture world in scope here, or is it its own work order? Four of
   five directions are blocked behind it.

9. **Correct the record.** Two published numbers are wrong and are being cited as
   settled: `CiC_Repo_Structure_Tracking.md`'s Question 1c claim that
   `gate_quote_recording` checks verbatim presence in the file (it does not —
   independently re-confirmed here), and the "47 single-tradition / median 4 / one
   by 19" figures, which I could not reproduce at any grain. Both sit in a
   standing decision doc and both currently inform the charter. Per `CLAUDE.md`,
   fix the map first.
