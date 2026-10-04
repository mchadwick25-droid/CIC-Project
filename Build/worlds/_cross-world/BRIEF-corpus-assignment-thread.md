# Brief: assign the source corpus to the Atlas

**For:** a dedicated thread (Fable)
**Supersedes:** `CORPUS-PARTITION-BRIEF.md`, which reached the same conclusion
by a longer route and assumed six buckets instead of 274.

---

## 1. The job, in one paragraph

**This is primarily a parsing exercise**, and that should
set your posture throughout. The work is mechanical extraction and
assignment: read what the files say about themselves, place each work, record
the placement. Historical judgment enters only where placement genuinely
requires it, and where it does, `needs-ruling` is the right answer far more
often than a confident call. You are not being asked to adjudicate the
Christian tradition; you are being asked to sort a library and flag what you
cannot shelve.

Every author and work in the 46 vendored volumes under `cic/texts/` is
assigned to one or more Atlas census entries, so that a world's sources become
a derived fact rather than whatever a build thread happened to reach for. The
output is a reviewable assignment table plus, where it helps, per-author text
extracts. **You are not writing world content and not touching any world's
records** beyond the one file this brief names.

---

## 2. Why — the diagnosis, with the numbers

A participant asked `desert` "who is Jesus" and got the story of Antony's
conversion. The pipeline was working: the voice was served
`desert.dw.jesus`, the **single** record covering canon cell C-I, and rendered
it faithfully. The problem was upstream.

Three measurements, all from this tree:

- **61 of the fleet's 168 world-cells answer from a single record.** Every one
  passes the M1 coverage gate as "substantive", because that gate asks whether
  a cell has ≥1 substantive record and stops. It measures presence, not depth.
- **`desert` draws on 6 of 46 vendored volumes**, and only 76% of its sourced
  records rest on text the pipeline can verify offline — lowest in the fleet,
  against `pahc` at 99%.
- **20 of 46 volumes are read by no world at all**, including Basil, both
  Gregories, Chrysostom and eight volumes of Augustine.

The root cause is not laziness in any thread. It is that **nothing has ever
recorded which sources belong to which world.** There was no way to ask "did
Alexandria consider Basil?" except to grep for his name and infer — a proxy
this audit ran and got wrong, matching *"Basil"* against *"Basilidean"* and
*"Leo"* against *"Leonides"*, Origen's father.

Mark's instruction: *"each world built and representing the sources of the
Christian tradition... it concerns me we have sources not being accessed and a
part of the conversation. yes latency is important, but getting the accurate
full answer is more important."*

---

## 3. The unit of work: author × work

**Not the volume.** `anf02` alone holds Hermas, Tatian, Theophilus,
Athenagoras and Clement of Alexandria, belonging to different traditions. A
volume-level assignment hands Alexandria Tatian along with Clement.

**Not the bare author either.** The same author's different works belong to
different places:

- Athanasius, *Vita Antonii* → `desert-monasticism`
- Athanasius, *Against the Arians*, *De Incarnatione* → `alexandria-catechetical`, and arguably `imperial-juridical-christianity`
- Augustine, *Confessions* → the Latin pastoral entry; *anti-Donatist writings* → `donatism`; *anti-Pelagian writings* → `pelagianism`

So the unit is a **work** (or a coherent group of works), attributed to an
author, assigned to one or more Atlas entries.

---

## 4. The bucket set: the Atlas census, all 274 entries

`cic-website/data/world-census.json`, `movements[]`. Assign to the `id` field.

**Every built world is itself a census entry** — `desert-monasticism`,
`alexandria-catechetical`, `post-apostolic-house-church`,
`hieronymian-ascetic-literary`, `syriac-edessa-nisibis`,
`imperial-juridical-christianity` are rows in the same table. There is one
taxonomy, not two, which is the point: assigning to the Atlas assigns to the
built worlds automatically, and nothing has to be kept in sync.

Entries carry a `status`. All of these are valid assignment targets:

| status | count | means |
|---|---|---|
| Built & Live | 6 | a world participants can speak to today |
| Selected - Not Yet Built | 3 | chosen for its era; construction not started |
| Possible Future World (on record) | 6 | named candidate, reasoning on record |
| Deferred by Step 0 | 4 | considered, held for a later era |
| Contested - Evidentiary | 6 | the record is genuinely disputed |
| Excluded - Doctrinal Floor (C1) | 4 | outside the tradition on stated creedal grounds |
| Pre-Survey Candidate | 215 | that era's survey has not run |

**Assigning to an unbuilt entry is a success, not a failure.** Basil and the
Gregories go to `cappadocian-nicene-pastoral-monastic-tradition`, which the
census already marks *Selected - Not Yet Built*. When that world is built its
sources are already assembled. Most of the corpus that no current world reads
is in exactly this position.

**The four excluded entries are also valid targets.** `marcion-marcionism`,
`valentinian-and-other-gnostic-christianities`, `manichaeism` and
`homoian-arian-christianity` are outside the doctrinal floor and will never be
built as worlds — but material *about* them, which the corpus carries
heresiologically (Irenaeus, Tertullian, Hippolytus, Epiphanius), still needs a
home. Assign it to those entries. A built world may then draw on it **only as
`register: etic`** — described from outside, never as its own voice. That
distinction is already enforced per-record; you are not changing it, only
making sure the material is findable.

---

## 5. The output

### 5a. A standalone corpus map, outside `records/` entirely — SETTLED

The assignment table stays separate from the built worlds, with clear
buckets that align to them; how best to integrate it into each world is
worked out separately, once the parsing and organizing is done.

So the assignment table does **not** live inside any world, and it does not
live in `engine/<module>/records/` either — `compile_world()` loads the fleet records
on every build (`build_coverage_json`, `build_canon_map_json`, and the
manifest itself), so anything put there moves all seven package hashes and is
not separate in any meaningful sense.

**Home: `cic/corpus-map/`** — beside the texts it describes and the tooling
that reads them (`cic/texts/`, `cic/engine/`), and touched by nothing in the
compile path. One file per Atlas entry, named for the census `id`:

    cic/corpus-map/desert-monasticism.yaml
    cic/corpus-map/cappadocian-nicene-pastoral-monastic-tradition.yaml
    cic/corpus-map/imperial-juridical-christianity.yaml

That is what "clear buckets that align" means concretely: the filename **is**
the census id, so alignment is structural rather than something to keep in
sync, and integration later is a join on a key that already matches.

```yaml
atlas_id: desert-monasticism        # == the filename, == a census movements[].id
works:
  - work: "Vita Antonii (Life of Antony)"
    author: athanasius              # a slug from cic/texts/AUTHORS.md
    source_file: npnf204_athanasius-select-works-letters.xml
    locus: "div1 'Life of Antony'"
    role: tradition                 # tradition | context  (§11a)
    confidence: assigned            # assigned | provisional | needs-ruling
    note: >
      Athanasius' own account of Antony. Also assigned to
      alexandria-catechetical as its author's own work - assignment is not
      exclusive (§6.1).
```

**Integration is explicitly a later, separate decision.** This thread produces
the map; how a world's records come to draw on it is designed afterwards, with
the map in hand. Do not build toward any particular integration.

*Superseded:* a `corpus_review` record type was added to all six worlds
earlier the same day, per-world and keyed by file. It was the wrong shape
under this ruling and has been removed — records, schema, gate and the
retrieval guard that existed only to keep it out of the voice's candidate
pool. All seven packages recompiled; every world's content is byte-identical
to its prior state.

**The format is built and gated — do not hand-build one and hope it
validates.** `cic/engine/corpus_map.py` loads and checks every file in
`cic/corpus-map/`, and `cic/corpus-map/desert-monasticism.yaml` is a seeded
worked example holding two real works, both already vendored and already cited
by that world. Copy its shape; run the validator as you go:

    python cic/engine/corpus_map.py            # validate + report
    python cic/engine/corpus_map.py --coverage # also list vendored files with nothing assigned yet

What it enforces, so you know what will bounce:

| rule | why |
|---|---|
| filename == `atlas_id` == a real `movements[].id` | the alignment mechanism; a typo would create a silent orphan bucket |
| `work`, `author`, `source_file`, `role`, `confidence` all present | an assignment missing any of these cannot be acted on later |
| `role` ∈ {`tradition`, `context`, `antecedent`, `transmission`} · `confidence` ∈ {`assigned`, `provisional`, `needs-ruling`} | §11a, §6.6, and the antecedent rule below |
| `source_file` names a file in `cic/texts/` | catches a source that was cited but never vendored |
| `author` is a slug in `cic/texts/AUTHORS.md` | §6.2 — derived from the markup, not from your own patristics |
| the same work twice in ONE entry | a duplicate. The same work in SEVERAL entries is expected and correct (§6.1) — the validator will never complain about that |

Pre-Survey Candidate entries **are** valid targets. 215 of
the census's 274 movements sit in eras whose Step 0 survey has not run, and
material plainly belonging to one of them belongs there rather than held back.
Placing a source is not a claim that the era's survey has run.

`python -m engine.m1.cross_world` reports each built world's assignment count
from this map — the join is `registry census_id → corpus-map filename`, with
no lookup table — plus a count of entries holding material for worlds not yet
built. That last number is the point of §4: Basil waiting in
`cappadocian-nicene-pastoral-monastic-tradition` is material correctly placed,
not a gap.

### 5b. Per-author extracts — optional, and second

Splitting volumes into per-author text files is mechanically clean: CCEL's
`div1` boundaries give exact byte ranges, and `anf02` cuts into five
self-contained files (Hermas 52,782 words · Tatian 19,040 · Theophilus 31,714
· Athenagoras 33,787 · Clement of Alexandria 388,305). The extracted Clement
section opens precisely at his introductory note.

**Do this only after the assignment table exists**, and observe one rule:

> `cic/texts/` is a **verified vault**. `cic/engine/texts_registry.py` reads
> each file's rights basis from that file's own header, every run, never
> trusting a claim made when it was added. Extracts therefore go to
> `cic/texts/by-world/<census-id>/`, are **derived and regenerable**, are never
> hand-edited, and each carries a provenance header naming its source volume,
> edition, translator, rights basis and `div` path. Loose copies would mean the
> same edition verified N times and a rights correction landing N times or
> drifting.

---

## 6. Rules and cautions

**6.1 — Non-exclusive by default. This one is load-bearing.**
Mark: *"some people may influence more than one world and that's ok."* More
than ok — required. `desert`'s most important source is Athanasius' *Vita
Antonii*, and Athanasius is Alexandria's author: `npnf204` is cited by 53
`alx` records and 43 `desert` records. **An exclusive author-to-world
partition silently destroys desert's entire evidential base, and would look
tidy while doing it.** If your output has one world per author, treat that as
a bug in the assignment, not a finding about the corpus.

**6.1b — `antecedent` is the third relation, and it is narrow.** A work is
`antecedent` to an entry
when it is the authority that entry argued *from*, written before the entry
existed — not its own voice (`tradition`) and not an outside observer's
(`context`). **The rule: an antecedent assignment requires that the entry's own
vendored sources argue from the text.** Admiration and descent are not enough,
or Augustine ends up assigned to every Reformation entry. A *contemporary*
opponent is `context`, not `antecedent`.

**6.1c — `transmission` is custody, not voice.** Use it when
the entry's people *preserved* a work that originates outside them and is why
we still have it — Syriac scribes and a Greek apology, Christian scribes and
the Jewish pseudepigrapha. **Not** for an opponent quoted *inside* a work of
the tradition (Celsus in Origen — the containing work is Origen's), and **not**
for a lost work surviving as fragments in a later author (that is a fact about
the source record). A work the tradition composed stays `tradition` however
widely it was copied. Rule of thumb: if the work's own voice has no home
elsewhere in the map, you have not found a transmission — you have found a
`tradition` you mislabelled.

**6.2 — Derive, do not assert.** Every author name should come from the
files' own CCEL markup (`<DC.Creator>` slugs, `<div1>` titles), which
`cic/engine/corpus_authors.py` already extracts. Where the markup is silent,
**say so rather than filling it in from your own knowledge of patristics.**
Two failures from building that tool, both recorded in its source, are worth
knowing:

- minting `div1` titles as authors produced 183 "authors" including
  `introductory-notice` and `the-gospel-of-peter`;
- attributing every work in a single-author volume to that author is sound for
  NPNF (whose `div1`s are works) and badly wrong for ANF (whose `div1`s are
  author sections) — unguarded it gave Clement of Rome, Mathetes, Polycarp,
  Ignatius, Barnabas, Papias and Justin Martyr **to Irenaeus**.

**6.3 — Editors are not authors.** Schaff, Coxe, Menzies, McGiffert, Wace and
Freemantle appear in `DC.Creator` because they made the volume. Already
filtered; do not reintroduce them.

**6.4 — Anonymous and collective works are first-class.** The Didache, the
Apostolic Constitutions, the conciliar acts, the Testaments of the Twelve
Patriarchs are things a world sources. They need assignment without being
forced under an author.

**6.5 — Scripture is out.** The Bible is in the corpus only as
the authors themselves used it; this project does not interpret it directly.
`webbe_world-english-bible-british-edition.xml` gets no assignment, and
neither does `anf10`, a bibliographic index with no text.

**6.6 — Where you are unsure, say `needs-ruling`.** A flagged uncertainty is
worth more than a confident wrong assignment, and Mark can clear a list of
them quickly. Do not spend judgment you do not have.

---

## 7. Order of work

**First: the 52 unattributed works.** A corpus cannot be split by author where
it has none. `cic/texts/AUTHORS.md` lists 52 works across 13 volumes that CCEL's
metadata does not attribute. They need three different answers:

- **Metadata omissions** — `anf01` names only `irenaeus` while its sections
  carry Clement of Rome, Mathetes, Polycarp, Ignatius, Barnabas, Papias and
  Justin Martyr. Recoverable by reading the section headers.
- **Genuinely anonymous** — the Didache, Apostolic Constitutions, conciliar
  acts, apocrypha. Per 6.4, these become entities of their own.
- **Pseudonymous** — the Pastor of Hermas, the Clementine literature. A ruling
  is needed on whether they file under the attributed name, the real one, or
  their own.

**Then:** the 65 attributed authors, work by work, assigned to Atlas entries.

**Then, if wanted:** the per-author extracts (5b).

Suggested order within the second phase: the volumes no world currently reads
(20 of 46) first — they are where the assignment adds most, and where the
Cappadocian, Antiochene, Latin-pastoral and Donatist entries will get most of
their future corpus.

---

## 8. What "done" looks like

- Every vendored file except `webbe` and `anf10` has every one of its works
  assigned to at least one census `id`, or flagged `needs-ruling`.
- Every `atlas_id` resolves to a real movement in `world-census.json` — this
  is checked mechanically, not by eye.
- No assignment is exclusive where the material genuinely serves several
  entries (6.1).
- `python cic/engine/corpus_map.py` exits 0 — every file valid.
- `python -m engine.m1.cross_world` reports zero new defects, and its
  `corpus-map/<world>` observations show a real count for all six built
  worlds rather than "no corpus-map file".

---

## 9. Out of scope

- **World content.** You are not writing or editing `doctrinal_witness`,
  `term`, `story`, `quote` or any other record type. Assignment says a source
  *belongs*; a build thread decides what it *says*.
- **Recompiling packages.** Adding fleet records changes every manifest hash.
  Leave it; it will be done once, at the end, with the determinism and
  staleness checks.
- **The retrieval layer.** `engine/m4` retrieves only over compiled records
  and that is deliberate — a raw passage carries no `register`, `confidence`,
  rights check or citable id, so wiring texts into a turn would give fuller
  answers that are less checkable. This work makes sources *findable by
  builders*; records still mediate everything a participant meets.
- **`cic-poc/backend`.** The suspended POC. Not part of this.

---

## 10. Tooling that already exists

| tool | what it does |
|---|---|
| `cic/engine/corpus_authors.py` | author index from CCEL markup → `cic/texts/AUTHORS.md`. `--json` for machine use. |
| `cic/engine/texts_registry.py` | verifies each vendored file's rights basis from its own header; `--write-readme`. |
| `cic/engine/corpus_probe.py` | asks what the corpus holds for a world + canon cell, scoped by this map. **Prototype** — its docstring names why its output is not yet usable. Each entry you assign narrows it. |
| `engine/m1/cross_world.py` | fleet-level consistency checks; `corpus_tier()` ranks a volume against a world by date and region. |
| `cic/engine/corpus_map.py` | **the validator for your output.** Loads `cic/corpus-map/*.yaml`, checks every rule in §5a, `--coverage` lists vendored files with nothing assigned yet. |
| `Build/worlds/_cross-world/CORPUS-USE.md` | what each world currently draws on, and the 20 unread volumes. |

---

## 11. Open questions and their answers

Kept with their answers rather than deleted, so the thread can see what was
decided and why rather than inheriting rules with no reasoning attached.

1. ~~The assignment table's home and shape~~ — **settled**: a
   standalone `cic/corpus-map/`, one file per Atlas entry, outside `records/`
   entirely. See §5a.
2. ~~Granularity~~ — **settled: per work.** Augustine's treatises
   are assigned individually, not as groups. More entries, and the right call
   for a corpus search that will eventually want loci: a group assignment
   cannot say *which* of forty treatises a passage came from.
3. ~~Pre-Survey Candidate entries~~ — **settled: yes, assign to
   them.** All 274 movements are live targets. Placing a source in an
   unsurveyed era is not a claim that its Step 0 survey has run; it is
   material waiting where it belongs, and 215 of the 274 sit in eras that
   have not been surveyed.
4. **The Pastor of Hermas and the Clementines** — under the attributed name,
   the real one, or their own entity? (7, third bullet.)

Context material carries a `context` marker on the world it gives context
for, not a bucket of its own (§11a).

---

## 11a. A second corpus: the Pearse "More Fathers" collection

The CCEL/Tertullian-project *More Fathers*
collection can be uploaded as text or RTF — **not ThML-marked**. It is several hundred files
and far more diverse than ANF/NPNF. Segment it into the same assignment table.

**Its rights profile is already established here.** Seven of the eight
non-ANF/NPNF files in `cic/texts/` came from this collection — Ephraim's
*Prose Refutations*, Aphrahat's *Demonstrations 2 and 7*, the *Chronicle of
Edessa*, the *Doctrine of Addai*, Optatus, Palladius' *Lausiac History*,
Origen's *Philocalia*. Same provenance discipline applies: public domain
only, rights read from each file's own header.

### What it closes, against the measured gap list

Checked against the source records that currently carry bibliography with no
text:

| gap | what this supplies |
|---|---|
| `ijc.source.ammianus-marcellinus` — *Res Gestae* 27.3, no vendored text | Ammianus, Books 14–31 |
| `ijc` reaches Ambrose only through `npnf210` | Ambrose's *Letters 1–91*. `ijc.figure.ambrose` names the Altar of Victory (384), the basilica standoff (386), Callinicum (388) and Thessalonica (390) — those are these letters |
| `hal` is built on Jerome's translation work and holds one preface as a quote | Jerome's 22 *Biblical Prefaces*, plus the *Chronicle*, *Commentary on Daniel*, Letter 120 |
| `syr.figure.rabbula` is sourced only to a modern secondary study | Rabbula's own *Admonitions to the monks* |
| every world names women's own words as its thinness | Gregory of Nyssa, *Life of St. Macrina* — one of the few lives of a woman narrated at length in this period |
| `syr` on apostolic origins | the Syriac *Apocryphal Acts* — Judas Thomas, Thecla |
| the Antiochene entry has no corpus | Theodore of Mopsuestia on the Nicene Creed, the Lord's Prayer, baptism and eucharist |
| the Latin pastoral entry has no corpus | Possidius, *Life of St. Augustine*; Pacian of Barcelona |
| `cappadocian` has only NPNF | Basil *To Young Men*, Nazianzen's *Invectives Against Julian*, Nyssa's *Macrina* |

### What it does NOT close — say this plainly

- **The Apophthegmata is not in it.** 42 `desert` records depend on that
  source and it still has no vendored text. Budge vol. 2 remains the only
  public-domain English and is still the single highest-value acquisition in
  the project.
- **Evagrius and Antony's *Letters* are not in it either.** Both remain
  rights-blocked; no public-domain English exists.
- The modern secondary works every world consults — Rubenson, Brock, Harvey,
  GEDSH, Petersen, Drijvers — are in copyright and never vendorable. They stay
  bibliography.

### The appendix: context, never theology

*"the outside sources do add an ecology level we need, but for context not
theology."* Settled, and the mechanism for it already exists and is unused.

The `ambient` record type has been in the schema since stage 1:

```
"ambient": {"detail": {"type": "string"},
            "formation_claim_barred": {"const": True}}
```

`formation_claim_barred` is a JSON-Schema `const` — an ambient record
**cannot** carry a formation claim, enforced at validation, not by anyone
remembering. `gate_completion_per_type` requires both fields, and
`build_chunks` compiles the type to its own `compiled/chunks/ambient/`
directory. **No world holds a single ambient record.** Built, gated,
compiled, entirely unused.

That is exactly the disposition this material needs:

- Julian, Porphyry, Libanius, Ammianus, Zosimus, Eunapius, Martial, Juvenal,
  Proclus → **`ambient` detail**, contributing texture, setting, hostile
  perception and social fact.
- Never a `doctrinal_witness`, never `register: emic`. These voices are not
  the tradition speaking; several are the tradition's opponents.
- **Assignment: a `context` marker on the world it gives context for.** So
  context material takes a normal `atlas_id` — the entry it surrounds — plus
  `role: context`. Libanius and Julian to `imperial-juridical-christianity`,
  whose world they are the outside of; Porphyry to
  `alexandria-catechetical`, whose teachers answered him.

  This is better than a separate bucket on both counts. It keeps one taxonomy
  (§4), and it says what the material is *for* rather than only what it is
  not: Libanius is not loose classical literature, he is the view from
  outside `ijc`, and a world that wants its lived ecology wants exactly that.

The value is real and specific: this is the best evidence of **how Christians
were seen from outside**, which no Christian source can supply and which every
world's "lived ecology" is thinner without.

**`role: context` is an enforceable invariant, not just a label.** Once the
assignment table exists, one check states the whole ruling mechanically:

> No record carrying `register: emic` may cite a source assigned
> `role: context`, and no `doctrinal_witness` may cite one at all.

A world may say what Libanius saw; it may never say it *as its own voice*, and
it may never build a doctrinal witness on him. That is "context, not theology"
in a form a gate can check on every commit rather than a discipline someone
has to remember. I will write it against whatever shape the table takes.

### The Atlas has no bucket for it

Julian's *Against the Galileans*, Porphyry's *Against the Christians*,
Libanius, Ammianus, Zosimus, Eunapius, Herodian, Martial, Juvenal, Proclus.
This is **the non-Christian world these worlds lived inside** — the society,
the opponents, the satirists. It is exactly the "lived ecology" material the
project says it wants, and it is the best evidence available for how
Christians were seen from outside.

But the census is a taxonomy of **Christian movements**. It has no entry for
fourth-century Roman paganism or for Neoplatonism, so this material has
nowhere to go under the Atlas scheme. It needs a disposition of its own, and
whatever that is, material from it must never be `register: emic` — it is by
definition a view from outside.

**This is a question for Mark, not a decision for the thread.**

### Format: no ThML, but the filenames are the metadata

`corpus_authors.py` reads `<DC.Creator>` and `<div1>`; text and RTF have
neither. The Pearse filenames, however, are a consistent and parseable
convention — `gregory_macrina_1_life`, `ambrose_letters_03_letters21_30`,
`optatus_03_book3` — carrying author, work and part in that order.

So: **upload with the filenames unchanged.** They are the attribution. The
extractor for this corpus reads names rather than markup, and every vendored
file still needs a provenance header on arrival, per §3's rule.

### Scale

Several hundred files. Upload in priority order rather than all at once — the
gap table above is that order, and it front-loads the material that closes
measured holes over material that is merely interesting.

---

## 11b. Keep a running wants register

Mark: *"currently we are restricted to only open source, but that doesn't mean
we won't raise funds to purchase other sources in the future, so a list of
other sources and their value would be helpful."*

`WANTS-REGISTER.md` already exists and is **generated, not maintained**
(`gen_wants_register.py`). It reads every `source` record whose `edition`
names no vendored file, and ranks by how many records depend on it — value as
a measured fact, not an opinion about a work's importance. Current state: 38
sources, 173 record dependencies, in four groups.

Two things it already says that matter for fundraising:

- The **Apophthegmata Patrum sits at value 42** — the highest in the fleet by
  a wide margin — and it is in the *acquirable, public domain* group. It costs
  nothing but someone's attention.
- **Evagrius (14) and the Pachomian corpus (12)** are in *no edition exists*.
  Money does not fix those; they stay honest limits.

**Your part:** when you meet a source this collection does not contain and no
world has yet recorded — and you will, working a collection this size —
write it as a `source` record with `edition: "not vendored"` and a
`discovery_channel` saying where you saw it. It then appears in the register
at value 0, which is honest: real, findable, nothing depends on it yet. That
is the whole mechanism; there is no separate list to keep.

Seven entries currently sit in `unclassified` — Tacitus, Suetonius, Lucian,
Ammianus, Auxentius, Paulinus of Milan. Most are the context material §11a
covers, and several are in the Pearse appendix, so they should resolve as you
go.

---

## 12. One thing this does not fix

Assignment solves *scope* — the search will no longer have to decide whether a
voice belongs to a world. It does **not** solve *content matching*.
`corpus_probe.py`'s second blocker stands: the canon-cell vocabulary is
conversational, derived from questions like *"Who was Jesus, to you and your
people?"*, which yields `{believe, people, good, make, teach}`. Those words
find prose about anything. Making corpus search actually work needs a
theological index vocabulary per cell, which the fleet does not have.

That is a separate piece of work, it is probably larger than this one, and it
should not be smuggled into this thread.
