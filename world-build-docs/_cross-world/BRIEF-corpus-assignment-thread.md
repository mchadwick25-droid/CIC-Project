# Brief: assign the source corpus to the Atlas

**For:** a dedicated thread (Fable) · **Raised by:** Mark, 2026-08-26
**Supersedes:** `CORPUS-PARTITION-BRIEF.md`, which reached the same conclusion
by a longer route and assumed six buckets instead of 274.

---

## 1. The job, in one paragraph

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

### 5a. One fleet-level assignment table — *recommended, please read*

The existing `corpus_review` record type is **per world** and keyed by file. It
was built before Mark's Atlas ruling and it is now the wrong shape: if Basil
belongs to `cappadocian`, that is *one fact*. Six worlds each writing
"Basil — belongs-to-another-atlas-entry — cappadocian" states it six times and
creates six chances to disagree.

Recommended instead: **one fleet-owned assignment table**, at
`records/_fleet/corpus_assignment/`, with each world's scope *derived* from it
— my sources are every work assigned to my `census_id`. That matches the
project's own standing principle (Artifact-1 §2: one registry, everything
else derived) and it is how `records/_fleet/canon_question/` already works.

Proposed shape, one record per work:

```yaml
id: _fleet.corpus.athanasius-vita-antonii
record_type: corpus_assignment
schema_version: 2
work: "Vita Antonii (Life of Antony)"
author: athanasius                       # a slug from cic/texts/AUTHORS.md
source_file: npnf204_athanasius-select-works-letters.xml
locus: "div1 'Life of Antony'"           # where in the volume
atlas_ids:                               # one or more census movement ids
  - desert-monasticism
  - alexandria-catechetical
confidence: assigned                     # assigned | provisional | needs-ruling
reason: >
  Athanasius' own account of Antony, and the single most influential text
  about the desert world though written from outside it. Belongs to desert as
  primary evidence and to Alexandria as its author's own work.
```

I will write the schema, the loader wiring and the gate for whatever shape you
settle on — **do not hand-build a format and hope it validates.** Say what you
need and it will be gated properly.

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

**6.5 — Scripture is out.** Mark's ruling: the Bible is in the corpus only as
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
- `python -m engine.m1.cross_world` reports zero new defects.
- `gate_corpus_accounted` (`engine/m1/gates_experimental.py`) is green for
  all six built worlds.

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
| `cic/engine/corpus_probe.py` | asks what the corpus holds for a world + canon cell. **Prototype** — its docstring names three reasons its output is not yet usable. |
| `engine/m1/cross_world.py` | fleet-level consistency checks; `corpus_tier()` ranks a volume against a world by date and region. |
| `engine/m1/gates_experimental.py` | `gate_corpus_accounted` — every volume sourced or ruled, and every `atlas_id` real. |
| `world-build-docs/_cross-world/CORPUS-USE.md` | what each world currently draws on, and the 20 unread volumes. |

---

## 11. Open questions for Mark — answer before starting, they change the work

1. **The assignment table's home and shape** (5a). Fleet-level record with
   per-world scope derived, or keep per-world `corpus_review`? Recommendation:
   fleet-level. The schema follows your answer.
2. **Granularity.** One assignment per *work* (Augustine's ~40 treatises) or
   per *coherent group* (Augustine's anti-Pelagian writings as one)? Group is
   cheaper and probably sufficient; per-work is more precise for a corpus
   search that will eventually want loci.
3. **Pre-Survey Candidate entries** (215 of 274). Are these live assignment
   targets, or should material only go to entries that have been surveyed?
   Assigning into an unsurveyed era may pre-empt a Step 0 judgment.
4. **The Pastor of Hermas and the Clementines** — under the attributed name,
   the real one, or their own entity? (7, third bullet.)

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
