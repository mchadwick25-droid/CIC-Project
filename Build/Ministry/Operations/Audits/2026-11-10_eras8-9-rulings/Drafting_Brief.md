# P2-G89b drafting brief: carrying out Mark's rulings on the eras 8 and 9 sweep

Repo root: `/home/user/CIC-Project` (branch `claude/p2-g89b-rulings`). You are one drafter among
several. **Do not edit any file in the repo.** Write only into your own scratch directory (named in
your task). No metered model calls of any kind (no API keys, no engine command that calls a model).

## The ruling

Mark, 2026-11-10: "take every recommendation" on the P2-G89 gate, G89-1 to G89-55, including the
sub-questions (G89-6 i and i, G89-26 i, G89-42 i). Eras 8 and 9 are frozen, so the ruling is a
change order: every new row, named line, link and field change you draft is one named item of it
(G89-6 a). Change only what a recommendation names. A frozen row's other text stays as it is.

## Read first (in this order; skim what is long)

1. `CLAUDE.md`: "Trust and source fidelity" and "Accessible and rigorous" bind every word.
2. The sweep record,
   `Build/Ministry/Features/Atlas-World-Map/Design/StepZero-Eras/CiC_Step0_Eras8-9_GlobalSweep_V1_0.md`:
   §0 (lines 43-127, the rules and verification legends), §2 (145-260), §2b (261-297), your own
   section(s) (named in your task), §8 (the gate questions, 2901-2991) and §10 (data flags,
   3077-end). The record is the reviewed text. Where a pass file in
   `Build/Ministry/Operations/Audits/2026-11-10_g89-sweep/passes/` differs, the record wins.
3. `Build/Ministry/Operations/Audits/2026-11-10_agreed-entries/G3_Drafting_Brief.md`: the record
   shape (every field), the prose target and the output format. It binds you except where this
   brief differs.
4. The worked example of a sweep gate carried out: one row of
   `Build/Ministry/Features/Atlas-World-Map/Design/StepZero-Eras/CiC_Step0_Era10_P2E10h_Proposed.json`
   and its `_Trace.md` (how each sentence is tied to an evidence item, and what is "not used").
5. `Build/Ministry/Operations/Audits/2026-11-06_census-lineage-rigor/Drafting_Brief.md` (the link
   types, five grades, source shape) and
   `Build/Ministry/Features/Church-Family-Tree/Launch-Prompts/CFT_Phase2_Links_Era_Launch_2026-11-07.md`
   steps 2 to 4b (the link method, major links and `outcome`).
6. `Build/Ministry/Features/Atlas-World-Map/Design/CiC_Step0_LivingEra_Protocol_Addendum_V1_0.md`
   (R2 to R4): the living mark.
7. `tools/validate-census.mjs`: what a record and a link must carry.
8. The census `cic-website/data/world-census.json`: the rows your items touch, and neighbors in the
   same lane and era, for field conventions.

## Evidence (the record's rule for these eras)

- Only an item the record marks **V** carries a sentence. **V-s** supports a study's title and
  details only. **[S]** carries nothing. Draft from the sources the record cites. Never add a
  source the record does not cite, unless you open it yourself raw and it is public domain; then
  say so in `flags`.
- **Library first.** Texts in `cic/texts/`: quote with `file` and `lines` (1-based, as in the
  census).
- **Public-domain editions opened raw.** archive.org and similar, fetched with `curl` (full text,
  e.g. `https://archive.org/download/<id>/<id>_djvu.txt`). WebFetch output is a model's summary and
  is never quoted. Save every raw text you quote from as `<scratch>/raw/<short-name>.txt`, and list
  it in `<scratch>/raw/SOURCES.json` as `{"<short-name>": {"url": ..., "accessed": "2026-11-10",
  "work": ...}}`. **Re-open each item the record quotes and re-check the quote yourself.** A quote
  you cannot find verbatim in the raw text is not used; put it in `flags`.
- **Quotes are verbatim**, OCR errors included (keep them; note them in `flags`). A rendering into
  English is marked as a rendering. Non-English quotes keep the original beside the rendering.
- Nothing after 1906 enters an era 9 history (and nothing after 1815 an era 8 one), except the
  living mark.

## What to draft

- **New rows** for every "enter" and "enter once" item in your slice, as its recommendation says
  (dates, homes, lines inside it, links). Where the record says one part enters now and another
  after a named source is read: draft the part that enters now. You may open the named source
  (raw, public domain). If you read it and it gives what the record asks, draft that part too and
  say so in `flags`; if not, list the part in `holds` with the source it waits for.
- **Named lines** on existing rows: a sentence or two added to the row's `longDescription` (and
  `voices`, `sources`, `relationsSummary`, `modernCountries`, dates only where the recommendation
  says), as `neighbor_changes`, each giving the **whole new value** of every field it sets and a
  `ruling` naming the G89 question. Change nothing else in the row.
- **Holds** (your slice's "hold" items, and parts held): `holds`, each `{item, g89, reason,
  waits_for}`, in the record's own words where possible. These go to Open-Gaps.
- **IDs:** a new row's `id` is a new lowercase-hyphen slug (check `movements` and
  `retiredMovements`). `atlasId: "TBD"`. Use an existing `lane`/`laneLabel`/`laneOrder` triple.
- **People:** `people: []` and `peopleNote` (one plain sentence why), unless a voice's own words are
  quoted from a `cic/texts/` file (then a people row, per the G3 brief).
- **status** "Pre-Survey Candidate", chip/glyph "psc", statusWord and statusDescription modeled on
  comparable rows (say the tier and the window). `reviewStatus: "AI-checked"`.
- **continuesAs:** only where the record says the same church continues (e.g. VI.25 to AF-1 to
  VIII.49). When a new row sits between two rows already joined by a "continued as" link, the old
  link is retired (`retire_links`, with `replacedBy`) and two new links take its place, and the
  older row's `continuesAs` is changed in `neighbor_changes`.

## Links (the P2-L1 to L10 standard)

Draft the links each new row's own text names, and the record's named links (e.g. "in contact
with" AF-1 to AF-2). Types, grades, verbatim quotes, `outcome`, IDs and the two-way check as in the
G3 brief and the lineage brief.

- **Major:** lineage and breaks ("continued as", "gave rise to", "broke with") are major by type.
  Any other link is major only for an institutional act shown in its own sources, and then carries
  an `outcome`.
- **Grades and states.** A quote checked in a Library file: `verified-direct`; Documented needs
  one. A quote read in a raw public-domain text online: the source carries `url` and `accessed`
  (no `file`/`lines`), the link is `verified-online`, and it can be Widely Accepted at most (the
  validator enforces the cap). A study named but not read: `named-not-rechecked`.
- A link's quotes must sit in its own `sources`.

## Living

`living: true` only for a tradition alive today (2026), shown by dated evidence graded CD or CR
(R2, R3), with present-tense humility (R4). Copy the `livingEvidence` shape of a neighbor. A new row
that continues a row already marked living may cite that row's own dated evidence, saying so in
`basis`. If you cannot meet R2 to R4, set `living: false` and say why in `flags`. List every row you
mark living in `flags` ("LIVING: <id> — evidence").

## Prose

Every paragraph of every prose field, link note and outcome: Flesch Reading Ease 60 or more and FK
grade 10 or less. Short sentences, active voice, the church's own words and imagery kept, no AI
tells, contested claims tagged with both sides. The thinness of the evidence is stated plainly in
`sourcing` (e.g. "almost every text is a missionary's"). Run before you finish, from the repo root:

    python3 Build/Ministry/Operations/Audits/2026-11-10_eras8-9-rulings/check_draft.py <scratch>/Draft.json <scratch>/raw

It scores every prose field and checks every quote verbatim (Library files at their lines; raw
texts by `raw_file`). Fix every line it prints.

## Output: `<scratch>/Draft.json`

The G3 shape, plus `holds`, and a `ruling` on each entry, neighbor change and link:

```json
{"entries": [...], "fact_table": [{"entry", "field", "sentence", "file", "lines", "quote"} or
  {"entry", "field", "sentence", "url", "accessed", "raw_file", "quote"} or
  {"entry", "field", "sentence", "record": "§3 AF-1 e2 (V)", "note"}],
 "neighbor_changes": [{"id", "set": {...}, "ruling", "reason"}],
 "links": [...], "retire_links": [...], "holds": [...], "wants": [...], "flags": [...]}
```

In link and fact-table sources read online, add `"raw_file": "raw/<short-name>.txt"` beside `url`
(the checker uses it; it never reaches the census). Every factual sentence has a fact-table row.
