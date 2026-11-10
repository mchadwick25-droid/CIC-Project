# P2-G3 drafting brief: the agreed entries for the Church Family Tree

Repo root: `/home/user/CIC-Project`. You are one drafter among several. **Do not edit any file in
the repo.** Write only into your own scratch directory (named in your task). No metered model
calls of any kind (no API keys, no engine command that calls a model).

## Read first (in this order; skim what is long)

1. `CLAUDE.md`: "Trust and source fidelity" and "Accessible and rigorous" bind every word.
   Nothing is invented. A fact you cannot tie to a vendored file (`cic/texts/`) or to a source
   already cited in the census is left out, or stated as thin, and its text goes on `wants`.
2. `Build/Ministry/Features/Church-Family-Tree/Decision-Log.md`, entry "2026-11-09 — The gap
   sweep ruled (P2-G1)" (rulings, people on the map, principles 1-6, principle M).
3. `Build/Ministry/Operations/Audits/2026-11-08_tree-gap-sweep/Rulings_2026-11-09.md`, and your
   items in `candidates.md` / `candidates.json` (citations and vendored files are listed there).
4. `Build/Ministry/Operations/Audits/2026-11-06_census-lineage-rigor/Drafting_Brief.md`: the
   six link types, five grades and source shape. Binding for every link you draft.
5. `Build/Ministry/Features/Church-Family-Tree/Launch-Prompts/CFT_Phase2_Links_Era_Launch_2026-11-07.md`,
   steps 2 to 4b (the per-era link method, including major links and `outcome`).
6. The worked example of a new entry made to the census Step 0 bar:
   `Build/Ministry/Operations/Audits/2026-11-08_armenian-apostolic-era-8/` (README.md, Final.json).
   Also look at one era 10 row in `Build/Ministry/Features/Atlas-World-Map/Design/StepZero-Eras/CiC_Step0_Era10_P2E10h_Proposed.json`
   and its `_Trace.md`, for how each field is sourced and graded.
7. `tools/validate-census.mjs`: what a record and a link must carry to pass.
8. The census, `cic-website/data/world-census.json`: copy the field set and conventions of
   comparable existing entries (neighbors in the same lane and era). The person entry
   `tertullian-s-voice` is the model for a person record.

## Record shape

Every new entry has the full field set of an existing movement: id (lowercase-hyphen slug,
new and never used before; check `retiredMovements` too), `atlasId: "TBD"` (assigned at apply),
era, name, shortName (20 characters or fewer), informalName, dates, start, end, region,
placeLabel (at most two places from `region`, " · " between, optional " and beyond"),
modernCountries, regions, lane, laneLabel, laneOrder, beyondFloor, status, chip, glyph,
statusWord, statusDescription, living, overlayCurrent, c2, sourcing, floorNote,
relationsSummary, why, entry: null, teaser, longDescription, voices, legacy, streams (where
neighbors carry it), continuesAs (only where a source shows the same community continues),
livingEvidence (living traditions: copy the shape; add `descentConfidence` with `basis`),
documentedStories (optional, at most two, each checked directly against a vendored text, with
the shape existing entries use), `people: []` (movements; rows are filled in a separate pass),
`reviewStatus: "AI-checked"`.

- **modernCountries:** copy `countryId`, `placeId` and `pleiadesId` from an existing census
  entry that names the same place. Never type an ID from memory. If no entry has the place,
  pick a label place that does exist in some entry, or leave the ID out and put it on `flags`.
- **status:** a new movement is normally "Pre-Survey Candidate" with chip/glyph "psc"; copy
  statusWord and statusDescription from a comparable entry and say why in the fact table.
- **Person entries:** `kind: "person"`, `toldWithin` (the movement ID, or null), no `people`
  field. Model on `tertullian-s-voice` (status "Within Another World (A5)" when told within a
  tradition). For a person told within no tradition, propose a status and say why in `flags`.
  The page says plainly what the person's place is ("told within ...", "founded ...", or "known
  only through ..."). A person's dates are their life or working years from a source.

## Prose: the reading target

Every paragraph of every prose field (relationsSummary, why, teaser, longDescription, legacy,
sourcing, floorNote, story text, link notes, outcomes): Flesch Reading Ease 60 or more and FK
grade 10 or less, scored with `engine.m7.turn_readability.score_turn`. Short sentences, active
voice, one idea per paragraph, the tradition's own imagery kept. No AI tells, no filler hedges.
Contested claims are tagged and both sides named. Run the helper before you finish:

    cd /home/user/CIC-Project && python3 <scratch>/../check_draft.py <your Draft.json>

It scores every prose field and checks every quote verbatim. Fix every line it prints.

## Links

Draft the links each new entry's own text names, by the per-era link method (types, grades,
verbatim quotes, `outcome` only for major links of the judged types per step 4b, `concerns` on a
link only where its note or a quote names the person entry). IDs: `from--to`, or `from--to--2`
when the pair already has a link. Symmetric types in alphabetical order. Check existing
`edges` for the pair first. Do the two-way check: every relationship your prose names has a
link or its sentence is qualified; every link is named in the prose.

## Output: one file, `<your scratch dir>/Draft.json`

```json
{"entries": [ <full records> ],
 "fact_table": [ {"entry": id, "field": "longDescription", "sentence": "...",
                  "file": "cic/texts/...", "lines": "a-b", "quote": "verbatim",
                  "grade": "Documented|..."} ],
 "neighbor_changes": [ {"id": existing id, "set": {"field": "new value"}, "reason": "..."} ],
 "links": [ <full edge records> ],
 "retire_links": [ {"id": ..., "reason": ..., "replacedBy": ...} ],
 "wants": [ "text wanted, and why" ],
 "flags": [ "anything for the coordinator or Mark" ]}
```

Every sentence of prose that states a fact has a fact-table row. A fact resting on a source the
census already cites (a secondary work, not vendored) may cite it by work and locus with no
file, graded no higher than that source allows.
