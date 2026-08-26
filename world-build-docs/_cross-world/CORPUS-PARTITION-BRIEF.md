# Brief: untangling the source ecology by world

**Mark, 2026-08-26:** *"we have to untangle the source documents so each world
has its set of sources as its sources, so the search is not having to decide
if this is in the world or not every time... then the search can be content,
not selecting the right voice."*

Right, and it dissolves the blocker that stopped `corpus_probe.py` being
useful: scope resolved at query time meant probing `desert` searched Augustine
and Chrysostom and duly returned them. Scope decided once, at build time,
makes search a content question inside an already-correct universe.

Four things worth settling before a thread starts, three of them cheap and one
of them load-bearing.

---

## 0. The Atlas is the bucket set — Mark's ruling, and it is the right one

*"use the atlas as the buckets as many authors don't have a place to go... the
atlas should align with our built worlds so we shouldn't have crossover."*

This dissolves a problem the rest of this brief was working around. Six worlds
cannot home 65 authors: Basil, the Gregories, Chrysostom, Augustine, Ambrose,
Optatus and Tertullian belong to none of them, and "not in any built world"
was the only thing the tooling could say about them — which reads as
irrelevance and is nothing of the kind.

The census already holds their homes, and most are entries the project has
**already selected**:

| material | Atlas entry | census status |
|---|---|---|
| Basil, Gregory Nazianzen, Gregory of Nyssa | `cappadocian-nicene-pastoral-monastic-tradition` | Selected — Not Yet Built |
| Chrysostom (6 volumes) | `antiochene-exegetical-christianity-chrysostom-…` | Possible Future World |
| Augustine (8 volumes) | `latin-pastoral-congregational-christianity` | Selected — Not Yet Built |
| Augustine anti-Donatist, Optatus | `donatism` | Selected — Not Yet Built |
| Augustine anti-Pelagian | `pelagianism` | Possible Future World |
| Ambrose | `ambrosian-milan-standalone` | Possible Future World |
| Tertullian | `tertullian-s-voice` | Possible Future World |
| Cyril of Jerusalem | `jerusalem-liturgical-pilgrimage-christianity` | Possible Future World |

**No second taxonomy is created.** Every built world *is* a census movement —
`desert-monasticism`, `alexandria-catechetical` and the rest are rows in the
same 274-entry table. Assigning to the Atlas assigns to the built worlds too,
which is what "should align... so we shouldn't have crossover" means: one
bucket system, not two kept in sync.

It also changes what F-25 in the audit *means*. Basil going unread by six
worlds is not a gap in those worlds — it is material correctly waiting for
`cappadocian`, and every hour spent placing it now is an hour world #7 does
not spend hunting for its own sources.

`corpus_review` has been extended accordingly: rank
`belongs-to-another-atlas-entry` plus an `atlas_id`, and
`gate_corpus_accounted` verifies the id is a real census movement. A ruling
that says **where material goes** is worth more than one saying it is not
here.

---

## 1. Split by author section, not by volume — it is mechanically clean

The tangle is inside the volumes, not between them. `anf02` alone holds five
authors belonging to different worlds:

| section | words | plausibly whose |
|---|---|---|
| The Pastor of Hermas | 52,782 | `pahc` |
| Tatian | 19,040 | `syr` (the Diatessaron's own author) |
| Theophilus | 31,714 | `pahc` |
| Athenagoras | 33,787 | `pahc` |
| Clement of Alexandria | 388,305 | `alx` |

CCEL's ThML `div1` boundaries give exact byte ranges and each section is
self-contained — the extracted Clement section opens precisely at his
introductory note. `cic/engine/corpus_authors.py` already reads this structure
for attribution, so the splitter is a small extension of a tool that exists,
not new machinery.

Splitting whole volumes instead would hand `alx` Tatian along with Clement,
which is the same defect the file-keyed `corpus_review` had.

---

## 2. A world's sources are not only its own authors — THE load-bearing one

**`desert`'s single most important source is Athanasius' *Vita Antonii*, and
Athanasius is `alx`'s author.** Measured: `npnf204` is cited by 48 `alx`
records and 43 `desert` records. An exclusive partition — each author to one
world — silently destroys desert's entire evidential base. It is the one way
this project could go badly wrong, and it would look tidy while doing it.

So the unit is **author × work**, not author:

- Athanasius, *Vita Antonii* → `desert`
- Athanasius, *Against the Arians* / *De Incarnatione* → `alx`, `ijc`
- Jerome, *Letter 22* → `desert` (its ascetic sections) and `hal`
- Origen, *Philocalia* → `alx`; Origen as read by later readers → elsewhere

A work may belong to several worlds — Mark: *"some people may influence more
than one world and that's ok."* Nothing here should be exclusive by default,
and any partition that produces one-world-per-author should be treated as a
bug report about the partition, not a finding about the corpus.

Note this is not in tension with "no crossover". The thing that must not
cross over is the TAXONOMY: one bucket system (the Atlas), not two. A single
author×work mapping to several Atlas entries is expected and correct.

---

## 3. Keep one verified vault; derive the per-world extracts

`cic/engine/texts_registry.py` verifies each file's rights basis by reading
that file's **own header, every run, never trusting a claim made when it was
added**. Loose per-world copies break that: the same edition gets verified N
times, and a rights correction has to land N times or the copies drift.

    cic/texts/                     the verified vault - unchanged, one copy
    cic/texts/by-world/<world>/    derived extracts, regenerable, never edited

Every extract carries a provenance header naming its source volume, edition,
translator, rights basis and the `div` path it was cut from — otherwise a
record citing an extract cannot be traced back to a rights-checked original.
Derived and deterministic, exactly as compiled packages already are: rebuilt
from source, never hand-maintained.

---

## 4. Land the assignment as rulings, not as a pile of files

The thread is making real historical judgments — whether Theophilus of
Antioch belongs to `pahc`, whether Optatus reaches `ijc` through the Donatist
controversy. Those should be **reviewable and arguable**, not implicit in a
directory listing.

`corpus_review` (added 2026-08-26, `engine/m1/schemas.py`) is already the
place: one record per world, each entry a file with a rank and a reason. Its
rank vocabulary was written for this exact decision. The thread's output
should be those rulings plus the extraction manifest, so
`gate_corpus_accounted` can check nothing was silently skipped and a reviewer
can disagree with any single call.

The schema will want its `file` key widened to author-and-work once the split
exists. That is a small change and should follow the partition, not precede
it.

---

## First job for the thread: the 52 unattributed works

A corpus cannot be split by author where it has no author. `cic/texts/AUTHORS.md`
reports 52 works across 13 volumes that CCEL's own metadata does not attribute,
and they need three different answers:

- **Authors the metadata simply omits** — `anf01` names only `irenaeus` while
  its sections carry Clement of Rome, Mathetes, Polycarp, Ignatius, Barnabas,
  Papias and Justin Martyr. Recoverable by reading the section headers.
- **Genuinely anonymous or collective** — the Didache, the Apostolic
  Constitutions, the conciliar acts, the Testaments. These want to be
  first-class entities in the partition, not forced under an author: "the
  Didache" is a thing a world sources.
- **Pseudonymous** — the Pastor of Hermas, the Clementine literature. A ruling
  is needed on whether they file under the attributed name, the real one, or
  their own.

Nothing in the current tooling guesses at any of these, deliberately.

---

## What this unblocks

`corpus_probe.py`'s three stated blockers, in order:

1. **Scope is not real** — solved outright by the partition.
2. **The cell vocabulary is conversational** — untouched by this work and still
   the real blocker for content search. `{believe, people, good, make, teach}`
   finds prose about anything.
3. **Passages carry no locus** — improved, since a splitter walking `div`
   structure can carry the reference down as it cuts.

So the partition fixes one of three and helps a second. It is worth doing on
its own terms and it does not, by itself, make corpus search work.
