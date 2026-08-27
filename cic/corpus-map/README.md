# `cic/corpus-map/` — which works belong to which Atlas entry

Mark, 2026-08-26: *"lets keep this separate from the built worlds with clear
buckets that align, then we can figure out how best to integrate this into
each world after we do the parsing and organizing."*

So this sits outside `records/` entirely — beside the texts it describes and
the tooling that reads them, touched by nothing in the compile path. Changing
anything here moves no package hash and no world's content.

## Two shapes, one relation

Assignment is **per work** and **non-exclusive**: a work may belong to as many
Atlas entries as need it. That makes the writing view and the reading view
different projections of the same data, and the tooling keeps both.

| | shape | who writes it |
|---|---|---|
| `_staging/<volume>.yaml` | one file per **source volume** → many works, each naming its `atlas_ids` | the assignment thread — one worker owns one file, so parallel work cannot race |
| `<census-id>.yaml` | one file per **Atlas entry** → the works assigned to it | **generated.** Never hand-edit; a re-merge overwrites it |

The bucket filename **is** the census movement id. That is the whole alignment
mechanism: no lookup table, nothing to keep in sync, and integration later is
a join on a key that already matches. `engine/m1/cross_world.py` performs that
join on every fleet run, so if the buckets ever stop lining up it shows there.

## Three relations, not two

`role` says how a work stands to the entry it is assigned to.

| role | means |
|---|---|
| `tradition` | the entry's own voice — a work of that community |
| `context` | the view from outside: a pagan critic, a civil historian, or a **contemporary opponent**. Augustine on the Manichaeans, Cyprian on the Novatian schism he lived through |
| `antecedent` | the authority the entry argued *from*, written before it existed. Added 2026-08-26 for Cyprian and Donatism |

**`antecedent` carries a rule, and it needs one.** If "a later movement claimed
him" were sufficient, Augustine would be assigned to every Reformation entry
and Origen to everything after him, and the map would say nothing. So an
antecedent assignment requires that **the entry's own vendored sources argue
from the text** — that reading this entry means reading that work. Demonstrable
in the corpus, not asserted from what a tradition later said about itself.
Augustine's *On Baptism, Against the Donatists* names Cyprian 306 times in
92,000 words; that is the kind of evidence the rule wants.

One author can hold two relations to two entries, and Cyprian does: antecedent
to `donatism`, context for `novatianism`. Where a single row needs both, it
splits into two — the same shape non-exclusivity already uses.

## Open: should there be a fourth role, `transmission`?

**Raised 2026-08-26, deliberately not decided.** Three of the four works in the
`syriac-edessa-nisibis` pile carried notes saying the same thing in different
words — *"syr marks only where the Syriac transmission preserved it"*,
*"preserved in Syriac … not a demonstrated Edessene provenance"*. What they are
describing is a work a tradition **copied and kept** without it being that
tradition's own voice, its opponent, or its authority. None of the three
existing roles says that.

It generalises past this pile. The Jewish pseudepigrapha in
`apocryphal-and-pseudepigraphal-literature` — the Testaments of the Twelve
Patriarchs, the Life of Adam and Eve, the Testament of Abraham — survive
*only* because Christian scribes went on copying them after Judaism had let
them go. Same relation.

**Why it was not just added.** A pattern-scan of every note describing
preservation returned 25 rows, and reading them showed the scan was conflating
three different things:

| | |
|---|---|
| **transmission** | this tradition preserved a text that is not its own voice — the Syriac apology, the Jewish pseudepigrapha |
| **embedded voice** | an opponent's words survive *inside* a work of this tradition — Celsus inside Origen, Petilian inside Augustine, Mani inside Augustine |
| **attested-by** | a lost work survives as fragments quoted by a later author — Alexander of Jerusalem via Eusebius |

Only the first is a relation between an entry and a work. A fourth role added
without that boundary drawn would be misapplied to the other two immediately,
which is the same explosion risk `antecedent` had to be ruled against.

And unlike `antecedent`, this one is **not forced**: every work in the pile had
an honest role available without it. `antecedent` existed because four Cyprian
works had *no* truthful role at all. This would be an improvement, not a
necessity — so it is Mark's to rule rather than a build thread's to impose one
turn after the last schema change.

## Why non-exclusivity is load-bearing

`desert`'s most important source is Athanasius' *Vita Antonii*, and Athanasius
is Alexandria's author. An exclusive partition — each author to one entry —
would silently strip desert of its evidential base while looking tidy. If an
assignment run produces one entry per author, that is a bug in the run, not a
finding about the corpus.

## Working files

| file | what it is |
|---|---|
| `ATLAS-TARGETS.md` | all 274 census entries with the fields that place a work. Generated by `cic/engine/atlas_targets.py`. |
| `UNATTRIBUTED.yaml` | authors and work-entities CCEL's markup does not supply, each with the evidence for its ruling. Generated from the `authors_ruled` blocks in staging. `corpus_map.py` accepts these as valid `author` values — a slug is legal because a *ruling* exists, never because a session was confident. |
| `_staging/` | the writers' files. This is where the work happens. |

## Commands

```
python cic/engine/corpus_structure.py --write   # cic/texts/STRUCTURE.md — what is in each volume
python cic/engine/atlas_targets.py              # ATLAS-TARGETS.md — where things can go
python cic/engine/corpus_map_merge.py --check   # validate staging, write nothing
python cic/engine/corpus_map_merge.py           # merge staging → buckets, then validate
python cic/engine/corpus_map.py --coverage      # what is assigned, and what is not yet
```

The brief that governs this work is
`world-build-docs/_cross-world/BRIEF-corpus-assignment-thread.md`.
