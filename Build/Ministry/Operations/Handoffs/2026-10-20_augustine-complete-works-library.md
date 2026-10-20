# Handoff — Augustine's complete works for lpc (Library) — 2026-10-20

From session: lpc source-research thread ("Run the Fable vs Opus 5.5 discovery test on lpc") · World or workstream: Library Build Engine, for `lpc` · Branch / PR: `claude/lpc-augustine-sourcing-topic-map`

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| Mark decided the scope is Augustine's complete works ("all works"), sourced through the Library, to support a topic map for lpc | `Build/worlds/lpc/lpc_Decision_Log.md`, 2026-10-20 entry, items 2–4 |
| Mark kept OCR ruling "a" for these works; the page-image correction proposal is withdrawn | Same entry, item 4; ruling text in `Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md`, 2026-09-25 |
| Listed what is already vendored and in lpc scope: Migne PL 33, 36–37, 38, 39, 40, 43; Morin 1917 and 1930; Caillau 1842; CSEL 33, 34, 36, 40, 41, 44, 51–53, 57; NPNF Series I | `ls cic/texts` and a parse of `cic/corpus-map/latin-pastoral-congregational-christianity.yaml` on `main`, 2026-10-20 (44 Augustine files assigned to lpc) |
| Located archive.org copies of Migne PL 32, 34, 35, 41, 42, 44, 45, 46, 47 | archive.org advanced search, 2026-10-20: `patrologiae_cursus_completus_lat_vol_034` (Public Domain Mark), and `bim_early-english-books-1641-1700_patrologiae-cursus-completus-_<year>_<vol>` items in collection `pub_patrologia-latina` (no host rights statement). PL 46 contents read from its full text: indices, "Sermones inediti" p. 817, Monte Cassino sermons p. 945, supplement p. 1003 |

## 2. Not done

- **Vendoring the volumes still missing.** Migne PL 32, 34, 35, 41, 42, 44–47 are unvendored. For each work they hold, check first whether a cleaner witness exists. A `csel-dev` TEI text of a public-domain CSEL volume would be cleaner under ruling "a". The Library already uses `csel-dev` for CSEL 41 (CC BY-SA 4.0, per those files' headers).
- **A works inventory.** No single inventory yet maps every Augustine work to its vendored witnesses. Checklists from his own world: the *Retractations* (`augustine_retractationes-lat_knoll-csel36.txt`) and Possidius's catalogue of his works (PL 46). Per work: genre, date, audience and place where known, English availability, census worlds.
- **Doc_02 and `Source_Registry.md`.** New rows for whatever is vendored, plus an organizing layer over Augustine's corpus (genre, date, audience and place) that the topic map can query.
- **Corpus-map assignment** of new works. Moving a work between worlds or newly double-placing it (Pelagianism, Donatism, Manichaeism, Hieronymian, Ambrosian Milan, Gallic monastic) goes to Mark as a proposal.

## 3. Re-check before you trust it

- The archive.org identifiers and rights — re-read each item page before downloading. Volume contents were read only for PL 39 and PL 46.
- "No file for PL 32, 34, 35, 41, 42, 44–47" — this was a filename search. A volume vendored under a non-Migne filename would not show up. Check `cic/texts/REGISTRY.yaml`.
- OG-24 lists queued and partly done items (Migne PL 35, CSEL 25.1, 42 and 43, Raulx tomes) — check their current status before re-searching.

## 4. Waiting on Mark

- Downloads — filenames, sources and sizes to be stated in your session before fetching.
- Cross-world placements — proposals, with options and a recommendation, in an Artifact.

## 5. Next step

Build the works inventory from the *Retractations* and Possidius's catalogue against `cic/texts/`, and from it list the works with no vendored witness. That list drives what to fetch.

## 6. Spend

Allowance share used: this session ran the 2026-09-24 model test (two discovery runs and four graders) and the 2026-10-20 research; weekly allowance was at 50% on 2026-10-20 (reset 2026-10-23). Metered: none.
