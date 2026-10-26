# REVISED 2026-10-26 (supersedes the decision below)

After the Opus review Mark re-decided: **`imperial-juridical-christianity` as `tradition` for the Constantinople-preached series only.** The Antioch-preached series stay with the Antiochene world. **No `context` rows for Jerome's, Gallic or Cappadocian worlds.** A passage index can still reach all of Chrysostom for pastors without making him any world's "we".

Which series count as Constantinople is not settled in this folder. The reviewer named Acts, Hebrews, Colossians and the Thessalonian letters; the place of preaching of several series (Romans, Ephesians, the Pastorals, Philemon) is debated by scholars. The Library thread should establish the place for each of the 16 series from the vendored edition's own introductions (npnf111 to 114) and record the evidence and any doubt in the row note before adding `imperial-juridical-christianity`. Where the place is uncertain, leave the row as it is. Apply with the merge (`python cic/engine/corpus_map.py`), not by editing the generated buckets.

The sections below are the superseded first proposal; use them only for the list of rows.

---

# Change list: map Chrysostom's homilies (npnf110 to 114) to built worlds

Prepared 2026-10-26 by the question-design thread. **Not applied.** Nothing in `cic/corpus-map/` was edited from this thread. Decision by Mark, 2026-10-26: `imperial-juridical-christianity` (ijc) as `tradition`; `hieronymian-ascetic-literary` (hal), `gallic-monastic-ascetic-christianity` (gallic) and `cappadocian-nicene-pastoral-monastic-tradition` (cappadocian) as `context`; no download.

## How it is written

A row carries one role for all its `atlas_ids` (README: where a single row needs two roles it splits into two rows). So for each work: (1) add `imperial-juridical-christianity` to the existing `tradition` row's `atlas_ids`; (2) add a second row, same work and locus, with the three context ids and `role: context`. Buckets are generated, so run the merge after (`python cic/engine/corpus_map.py`) and do not hand-edit the bucket files.

## Question for the Library thread before applying

`context` is defined as the view from outside (a pagan critic, a civil historian, a contemporary opponent). Chrysostom is none of those for hal, gallic or cappadocian: he is a neighbour and a fellow preacher. The survey proposed `context` as the nearest existing role. If the Library thread prefers a different treatment (a new role, or `context` with a note), the three context ids and the second rows are the only part that changes.

## Scope notes

- npnf109 (Priesthood, ascetic homilies, Statues) is not in this change: it is not verse-by-verse commentary, and the ijc row for the Eutropius homily already exists.
- Romans Homily XXIII is already `tradition` for ijc in `fleet-sweep-additions-npnf111.yaml`. Skip adding ijc to the Romans row for that one locus only if the merge flags a duplicate.

## Rows to change

### npnf110_chrysostom-homilies-matthew.yaml

- `npnf110_chrysostom-homilies-matthew--homilies-on-the-gospel-of-st-matthew` — Homilies on the Gospel of St. Matthew
  - edit: add `imperial-juridical-christianity` to `atlas_ids` (stays `tradition`)
  - new row: `npnf110_chrysostom-homilies-matthew--homilies-on-the-gospel-of-st-matthew--context`, same work and locus, `atlas_ids: [hieronymian-ascetic-literary, gallic-monastic-ascetic-christianity, cappadocian-nicene-pastoral-monastic-tradition]`, `role: context`, `confidence: assigned`

### npnf111_chrysostom-homilies-acts-romans.yaml

- `npnf111_chrysostom-homilies-acts-romans--homilies-on-the-acts-of-the-apostles` — Homilies on the Acts of the Apostles
  - edit: add `imperial-juridical-christianity` to `atlas_ids` (stays `tradition`)
  - new row: `npnf111_chrysostom-homilies-acts-romans--homilies-on-the-acts-of-the-apostles--context`, same work and locus, `atlas_ids: [hieronymian-ascetic-literary, gallic-monastic-ascetic-christianity, cappadocian-nicene-pastoral-monastic-tradition]`, `role: context`, `confidence: assigned`
- `npnf111_chrysostom-homilies-acts-romans--homilies-on-the-epistle-to-the-romans` — Homilies on the Epistle to the Romans
  - edit: add `imperial-juridical-christianity` to `atlas_ids` (stays `tradition`)
  - new row: `npnf111_chrysostom-homilies-acts-romans--homilies-on-the-epistle-to-the-romans--context`, same work and locus, `atlas_ids: [hieronymian-ascetic-literary, gallic-monastic-ascetic-christianity, cappadocian-nicene-pastoral-monastic-tradition]`, `role: context`, `confidence: assigned`

### npnf112_chrysostom-homilies-corinthians.yaml

- `npnf112_chrysostom-homilies-corinthians--homilies-on-first-corinthians` — Homilies on First Corinthians
  - edit: add `imperial-juridical-christianity` to `atlas_ids` (stays `tradition`)
  - new row: `npnf112_chrysostom-homilies-corinthians--homilies-on-first-corinthians--context`, same work and locus, `atlas_ids: [hieronymian-ascetic-literary, gallic-monastic-ascetic-christianity, cappadocian-nicene-pastoral-monastic-tradition]`, `role: context`, `confidence: assigned`
- `npnf112_chrysostom-homilies-corinthians--homilies-on-second-corinthians` — Homilies on Second Corinthians
  - edit: add `imperial-juridical-christianity` to `atlas_ids` (stays `tradition`)
  - new row: `npnf112_chrysostom-homilies-corinthians--homilies-on-second-corinthians--context`, same work and locus, `atlas_ids: [hieronymian-ascetic-literary, gallic-monastic-ascetic-christianity, cappadocian-nicene-pastoral-monastic-tradition]`, `role: context`, `confidence: assigned`

### npnf113_chrysostom-homilies-galatians-philemon.yaml

- `npnf113_chrysostom-homilies-galatians-philemon--commentary-on-galatians` — Commentary on Galatians
  - edit: add `imperial-juridical-christianity` to `atlas_ids` (stays `tradition`)
  - new row: `npnf113_chrysostom-homilies-galatians-philemon--commentary-on-galatians--context`, same work and locus, `atlas_ids: [hieronymian-ascetic-literary, gallic-monastic-ascetic-christianity, cappadocian-nicene-pastoral-monastic-tradition]`, `role: context`, `confidence: assigned`
- `npnf113_chrysostom-homilies-galatians-philemon--homilies-on-ephesians` — Homilies on Ephesians
  - edit: add `imperial-juridical-christianity` to `atlas_ids` (stays `tradition`)
  - new row: `npnf113_chrysostom-homilies-galatians-philemon--homilies-on-ephesians--context`, same work and locus, `atlas_ids: [hieronymian-ascetic-literary, gallic-monastic-ascetic-christianity, cappadocian-nicene-pastoral-monastic-tradition]`, `role: context`, `confidence: assigned`
- `npnf113_chrysostom-homilies-galatians-philemon--homilies-on-philippians` — Homilies on Philippians
  - edit: add `imperial-juridical-christianity` to `atlas_ids` (stays `tradition`)
  - new row: `npnf113_chrysostom-homilies-galatians-philemon--homilies-on-philippians--context`, same work and locus, `atlas_ids: [hieronymian-ascetic-literary, gallic-monastic-ascetic-christianity, cappadocian-nicene-pastoral-monastic-tradition]`, `role: context`, `confidence: assigned`
- `npnf113_chrysostom-homilies-galatians-philemon--homilies-on-colossians` — Homilies on Colossians
  - edit: add `imperial-juridical-christianity` to `atlas_ids` (stays `tradition`)
  - new row: `npnf113_chrysostom-homilies-galatians-philemon--homilies-on-colossians--context`, same work and locus, `atlas_ids: [hieronymian-ascetic-literary, gallic-monastic-ascetic-christianity, cappadocian-nicene-pastoral-monastic-tradition]`, `role: context`, `confidence: assigned`
- `npnf113_chrysostom-homilies-galatians-philemon--homilies-on-first-thessalonians` — Homilies on First Thessalonians
  - edit: add `imperial-juridical-christianity` to `atlas_ids` (stays `tradition`)
  - new row: `npnf113_chrysostom-homilies-galatians-philemon--homilies-on-first-thessalonians--context`, same work and locus, `atlas_ids: [hieronymian-ascetic-literary, gallic-monastic-ascetic-christianity, cappadocian-nicene-pastoral-monastic-tradition]`, `role: context`, `confidence: assigned`
- `npnf113_chrysostom-homilies-galatians-philemon--homilies-on-second-thessalonians` — Homilies on Second Thessalonians
  - edit: add `imperial-juridical-christianity` to `atlas_ids` (stays `tradition`)
  - new row: `npnf113_chrysostom-homilies-galatians-philemon--homilies-on-second-thessalonians--context`, same work and locus, `atlas_ids: [hieronymian-ascetic-literary, gallic-monastic-ascetic-christianity, cappadocian-nicene-pastoral-monastic-tradition]`, `role: context`, `confidence: assigned`
- `npnf113_chrysostom-homilies-galatians-philemon--homilies-on-first-timothy` — Homilies on First Timothy
  - edit: add `imperial-juridical-christianity` to `atlas_ids` (stays `tradition`)
  - new row: `npnf113_chrysostom-homilies-galatians-philemon--homilies-on-first-timothy--context`, same work and locus, `atlas_ids: [hieronymian-ascetic-literary, gallic-monastic-ascetic-christianity, cappadocian-nicene-pastoral-monastic-tradition]`, `role: context`, `confidence: assigned`
- `npnf113_chrysostom-homilies-galatians-philemon--homilies-on-second-timothy` — Homilies on Second Timothy
  - edit: add `imperial-juridical-christianity` to `atlas_ids` (stays `tradition`)
  - new row: `npnf113_chrysostom-homilies-galatians-philemon--homilies-on-second-timothy--context`, same work and locus, `atlas_ids: [hieronymian-ascetic-literary, gallic-monastic-ascetic-christianity, cappadocian-nicene-pastoral-monastic-tradition]`, `role: context`, `confidence: assigned`
- `npnf113_chrysostom-homilies-galatians-philemon--homilies-on-titus` — Homilies on Titus
  - edit: add `imperial-juridical-christianity` to `atlas_ids` (stays `tradition`)
  - new row: `npnf113_chrysostom-homilies-galatians-philemon--homilies-on-titus--context`, same work and locus, `atlas_ids: [hieronymian-ascetic-literary, gallic-monastic-ascetic-christianity, cappadocian-nicene-pastoral-monastic-tradition]`, `role: context`, `confidence: assigned`
- `npnf113_chrysostom-homilies-galatians-philemon--homilies-on-philemon` — Homilies on Philemon
  - edit: add `imperial-juridical-christianity` to `atlas_ids` (stays `tradition`)
  - new row: `npnf113_chrysostom-homilies-galatians-philemon--homilies-on-philemon--context`, same work and locus, `atlas_ids: [hieronymian-ascetic-literary, gallic-monastic-ascetic-christianity, cappadocian-nicene-pastoral-monastic-tradition]`, `role: context`, `confidence: assigned`

### npnf114_chrysostom-homilies-john-hebrews.yaml

- `npnf114_chrysostom-homilies-john-hebrews--homilies-on-the-gospel-of-st-john` — Homilies on the Gospel of St. John
  - edit: add `imperial-juridical-christianity` to `atlas_ids` (stays `tradition`)
  - new row: `npnf114_chrysostom-homilies-john-hebrews--homilies-on-the-gospel-of-st-john--context`, same work and locus, `atlas_ids: [hieronymian-ascetic-literary, gallic-monastic-ascetic-christianity, cappadocian-nicene-pastoral-monastic-tradition]`, `role: context`, `confidence: assigned`
- `npnf114_chrysostom-homilies-john-hebrews--homilies-on-the-epistle-to-the-hebrews` — Homilies on the Epistle to the Hebrews
  - edit: add `imperial-juridical-christianity` to `atlas_ids` (stays `tradition`)
  - new row: `npnf114_chrysostom-homilies-john-hebrews--homilies-on-the-epistle-to-the-hebrews--context`, same work and locus, `atlas_ids: [hieronymian-ascetic-literary, gallic-monastic-ascetic-christianity, cappadocian-nicene-pastoral-monastic-tradition]`, `role: context`, `confidence: assigned`


Total: 17 works, 17 edits and 17 new rows.