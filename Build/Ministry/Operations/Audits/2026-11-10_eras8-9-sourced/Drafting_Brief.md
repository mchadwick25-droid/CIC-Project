# P2-G89c drafting brief: the held eras 8 and 9 items whose sources the Library now holds

Repo root `/home/user/CIC-Project`. You are one drafter among several. **Do not edit any file in
the repo.** Write only into your own scratch directory (named in your task). No metered model calls
of any kind.

## The authority

Mark ruled the eras 8 and 9 gate "take every recommendation" (2026-11-10). Some items were held only
because their sources were not in the Library. The Library has since vendored them (its batches 2
and 3). Entering a held item once its source exists carries out the same ruling, as the same change
order (G89-6 a). Each item's recommendation is in the sweep record
`Build/Ministry/Features/Atlas-World-Map/Design/StepZero-Eras/CiC_Step0_Eras8-9_GlobalSweep_V1_0.md`
(§8, the gate questions; and the item's own section). Change only what the recommendation names. A
frozen row's other text stays as it is.

**First job for each item: does the vendored source really support the recommendation's line or
row?** Read the source. If it does, draft it. If it supports only part, draft the part and list the
rest in `holds`. If it does not, draft nothing for it and say why in `holds`. Do not stretch a source
to fit.

## Binding documents (read these first)

1. `CLAUDE.md`, "Trust and source fidelity" and "Accessible and rigorous".
2. `Build/Ministry/Operations/Audits/2026-11-10_eras8-9-rulings/Drafting_Brief.md`: the G89b brief.
   It binds you (record shape, evidence rule, links, living, prose, output format), except as below.
3. The worked example: `Build/Ministry/Operations/Audits/2026-11-10_eras8-9-rulings/drafts/` (look
   at one slice's `Draft.json` for the shape of `neighbor_changes`, `links` and `fact_table`).
4. The census `cic-website/data/world-census.json`: the rows your items touch, and neighbours.
5. Each source file's own header in `cic/texts/` (its content note gives line hints; the header
   says how to map OCR lines to file lines).

## Differences from the G89b brief

- **Your sources are Library files.** Quote with `file` and `lines` (1-based file lines, as the
  checker reads them). A Library quote can be checked `verified-direct`, and a link can then be
  Documented on a primary quote. Raw online texts are only for a study you open yourself.
- **Non-English quotes.** Keep the original, verbatim (OCR errors included, noted in `flags`). Give
  an English rendering beside it, marked as a rendering (`"rendering": "..."` on the source, and the
  prose says "in English, ..." where it quotes). A rendering must carry every clause, add nothing,
  and put no word in whose modern sense misleads. Where the OCR is too damaged to quote safely, do
  not quote it; say so in `flags`.
- **Shelf rule (Library).** A text sits on an entry only if the entry covers its date of writing.
  Nothing after 1815 enters an era 8 history; nothing after 1906 an era 9 history.
- **Country IDs** only from census rows (copy them from a row that carries the same country); the
  country's place must be on the row's place label. If none, leave it out and list it in `flags`.
- Every new row: `sources` list, `livingEvidence` (if living), `people: []` and `peopleNote`.
- Every factual sentence has a `fact_table` row. Prose: each paragraph Flesch Reading Ease 60+ and
  FK grade 10 or less. Run, from the repo root:

      python3 Build/Ministry/Operations/Audits/2026-11-10_eras8-9-rulings/check_draft.py <scratch>/Draft.json <scratch>/raw

  and fix every line it prints except frozen paragraphs you carry unchanged (say which in `flags`).

## Output

`<scratch>/Draft.json` in the G89b shape (`entries`, `fact_table`, `neighbor_changes`, `links`,
`retire_links`, `holds`, `wants`, `flags`), with a `ruling` on each entry, change and link (the G89
question, and "G89c: source now held" where the item was held). Then a short reply: what you
drafted, what you held and why, and every flag.
