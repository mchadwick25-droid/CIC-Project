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
| `<census-id>.yaml` | one file per **Atlas entry** → the works assigned to it | **generated.** Never hand-edit; edit the staging file for the source volume instead |

A bucket edited by hand is **not** overwritten. Each one carries a
`# content-digest:` of what the merge last wrote; if the contents no longer
match it, the merge leaves that file alone, names it, and exits non-zero. It
cannot tell which side is right, so it stops rather than guess. That guard was
added 2026-09-15, after a full merge was found to silently revert two works
vendored into `gallic-monastic-ascetic-christianity` and a source-fidelity
correction in `alexandria-catechetical`.

The bucket filename **is** the census movement id. That is the whole alignment
mechanism: no lookup table, nothing to keep in sync, and integration later is
a join on a key that already matches. `engine/m1/cross_world.py` performs that
join on every fleet run, so if the buckets ever stop lining up it shows there.

## Four relations

`role` says how a work stands to the entry it is assigned to.

| role | means | count |
|---|---|---:|
| `tradition` | the entry's own voice — a work of that community | 580 |
| `context` | the view from outside: a pagan critic, a civil historian, or a **contemporary opponent**. Augustine on the Manichaeans, Cyprian on the Novatian schism he lived through | 124 |
| `antecedent` | the authority the entry argued *from*, written before it existed. Cyprian and Donatism | 4 |
| `transmission` | **custody, not voice** — this tradition preserved and passed on a work that is not its own. Syriac scribes and a Greek apology; Christian scribes and the Jewish pseudepigrapha | 10 |

The counts are a snapshot, taken 2026-08-27, and they had already drifted once
before that — typed numbers describing generated data always do. For the live
figures run `python cic/engine/corpus_map.py`, which prints them and is the
authority; this table is here for the shape, not the arithmetic.

Both of the narrow two were added 2026-08-26, each on a measured case, and each
carries a rule that keeps it narrow.

**`transmission` is custody.** An assignment qualifies when the work
*originates outside* the entry and the entry's people are why we still have it.
Two things it is **not**, and the distinction is what stopped it swallowing
twenty-five rows:

- **embedded voice** — an opponent's words survive *inside* a work of this
  tradition. Celsus inside Origen's refutation, Petilian inside Augustine's.
  The containing work is the tradition's own; marking it would make every
  polemic a transmission.
- **attested-by** — a lost work survives as fragments quoted by a later author,
  Alexander of Jerusalem via Eusebius. A fact about the source record, not a
  relation between an entry and a work.

A work the tradition *composed* stays `tradition` however widely it was later
copied. And an entry whose whole subject is preserved material —
`apocryphal-and-pseudepigraphal-literature` — holds it as `tradition`, because
there it is the content rather than the custody. The Testaments of the Twelve
Patriarchs are `tradition` in the apocrypha entry and `transmission` in
`post-apostolic-house-church`, whose scribes kept them.

A test pins the invariant that makes the role mean anything: **every
transmitted work has its voice assigned somewhere else.** Custody of nothing
is a mis-used `tradition`.

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

## Why non-exclusivity is load-bearing

`desert`'s most important source is Athanasius' *Vita Antonii*, and Athanasius
is Alexandria's author. An exclusive partition — each author to one entry —
would silently strip desert of its evidential base while looking tidy. If an
assignment run produces one entry per author, that is a bug in the run, not a
finding about the corpus.

## Working files

| file | what it is |
|---|---|
| `ATLAS-TARGETS.md` | every census entry with the fields that place a work. Generated by `cic/engine/atlas_targets.py`. |
| `UNATTRIBUTED.yaml` | authors and work-entities CCEL's markup does not supply, each with the evidence for its ruling. Generated from the `authors_ruled` blocks in staging. `corpus_map.py` accepts these as valid `author` values — a slug is legal because a *ruling* exists, never because a session was confident. |
| `WORKS.yaml` | one entry per ancient **Work** (not per vendored file) — the FRBR-style Work/Expression join this map's own bucket files don't carry: is the "Vita Antonii" one world cites the same Work another world calls "The Life of Saint Anthony (Syriac recension)"? Hand-maintained, seeded not complete (four entries as of 2026-09-02) — see the file's own header for scope and the no-guessed-identifiers discipline it follows. Validated by `cic/engine/works_registry.py`, not corpus_map.py. |
| `AUTHOR-IDS.yaml` | Wikidata/VIAF identity keys per author slug — keyed to `cic/texts/AUTHORS.md`'s own slugs (a real, documented mismatch against `WORKS.yaml`'s longer author slugs — see the file's own header). Seeded, five of 77 authors as of 2026-09-02, each verified via WebSearch. Validated by `cic/engine/author_ids.py`. |
| `_staging/` | the writers' files. This is where the work happens. |

New source, not yet in `cic/texts/` at all? Start at
`cic/texts/INTAKE.md` instead — the full procedure from an attached file
to a vendored, registered, and assigned text, including the rights
checklist and naming convention for original-language witnesses.

## Commands

```
python cic/engine/corpus_structure.py --write   # cic/texts/STRUCTURE.md — what is in each volume
python cic/engine/atlas_targets.py              # ATLAS-TARGETS.md — where things can go
python cic/engine/corpus_map_merge.py --check   # validate staging, write nothing
python cic/engine/corpus_map_merge.py --write-only <token>  # write+validate only the bucket(s)
                                                 # <token>'s own staging file touches, no pruning -
                                                 # use this from inside one world's own build
                                                 # thread (2026-09-03); see merge()'s own docstring
python cic/engine/corpus_map_merge.py           # full merge: write every bucket, prune orphans -
                                                 # a deliberate whole-corpus pass, not a mid-build one
                                                 # refuses to overwrite a bucket edited by hand since
                                                 # it was generated (--force-overwrite discards it)
python cic/engine/corpus_map.py --coverage      # what is assigned, and what is not yet
python cic/engine/works_registry.py --check     # validate WORKS.yaml — unique work_ids, item addresses resolve
python cic/engine/author_ids.py --check         # validate AUTHOR-IDS.yaml — well-formed Wikidata/VIAF ids
python cic/engine/corpus_index.py --build       # (re)build cic/texts/INDEX.sqlite — NOT committed, see .gitignore
python cic/engine/corpus_index.py "QUERY" [--entry ID] [--limit N]   # full-text search, ranked, with canonical addresses
python cic/engine/corpus_coverage.py            # cic-website/data/corpus-coverage.json — Atlas-facing vendored-coverage feed
```

## Atlas-facing coverage feed

`cic-website/data/corpus-coverage.json` (2026-09-02, Mark's sign-off) is the
public join between this map and the census: for all 292 census entries, the
vendored works corpus-map has actually assigned, or an honest empty list.
Scoped to vendored coverage only — the acquirable-PD/purchasable/no-edition-
exists breakdown `WANTS-REGISTER.md` carries is deliberately left out, since
that data only has real content for the 7 already-built formation worlds
today (see `cic/engine/corpus_coverage.py`'s own docstring for the full
reasoning). Generated, not hand-edited; not yet wired into `atlas-v3.html`'s
rendering — that's separate front-end work.

## Canonical addresses

`WORKS.yaml`'s `items` fields use a project-local address form rather than
raw line numbers: `cic:<file-stem>:<locus>`, where `<locus>` is the file's
own ThML `div` id where one exists (`cic:npnf204_athanasius-select-works-letters.xml:xvi`),
or a plain-text file's own section/letter marker. This is deliberately not
a full CTS-URN adoption (that would require converting every vendored
volume to TEI first) — it borrows the *idea*, stable structural addressing
instead of a byte offset, at a cost this corpus can actually afford today.

The same form is also a real, optional field on any record's `sources[]`
entry, `address` — a sibling to the existing free-text `locus`, not a
replacement for it (Mark's sign-off, 2026-09-02: a new field, `locus`
itself untouched; optional/best-effort, backfilled only where an existing
citation unambiguously resolves to a real marker in the actual file, never
guessed). `engine/m1/gates.py`'s `canonical-address` gate checks any
`address` that's set is well-formed and names a file that exists under
`cic/texts/` — it does not and cannot confirm the `<locus>` half actually
points at the right passage; that's still on whoever set it, same as
`locus` itself always was.

The brief that governs this work is
`world-build-docs/_cross-world/BRIEF-corpus-assignment-thread.md`.
