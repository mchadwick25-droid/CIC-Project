# P2-G3b build: drafting brief for the person entries (data release after 30)

Mark ruled (2026-11-10, "take every recommendation"): 14 people named across the later worlds get
person entries. You draft some of them. Repo root `/tmp/claude-0/-home-user-CIC-Project/169e494a-41f0-5483-9c1c-9d54f9275f46/scratchpad/g3b/lib1577` (a read-only checkout of the Library PR that vendors the texts you need; read every repo path there). **Do not edit any file
in the repo.** Write only into your own folder. No model calls, no network.

## Read first

1. `CLAUDE.md`, "Trust and source fidelity" and "Accessible and rigorous". Nothing is invented. A
   fact you cannot tie to a vendored file (`cic/texts/`) or a source the census already cites is
   left out.
2. `Build/Ministry/Operations/Audits/2026-11-10_agreed-entries/G3_Drafting_Brief.md`: the record
   shape, prose target, fact table and links rules of release 29. Follow its "Record shape",
   "Person entries", "Prose" and "Output" sections. Its links section applies only as below.
3. The person entries release 29 shipped, as models: in `cic-website/data/world-census.json`, the
   records with `kind: "person"`, especially `origen`, `athanasius-of-alexandria`,
   `gregory-of-nyssa`, `gregory-the-great`, `john-calvin`. Copy their field set, order, tone,
   length (`longDescription` three short paragraphs) and status fields exactly.
4. Your `packets.json`: for each person, the reviewed row from the later-worlds count
   (`final_row`: home, dates, own words, counted later traditions with verified quotes), the home
   tradition's record, its people-row item for the person, and existing links whose note or quotes
   name the person.

## What to draft for each person

- **The record.** `kind: "person"`, `toldWithin`: the home id in `final_row.home`. Status
  "Within Another World (A5)", chip "exc", glyph "a5", statusWord and statusDescription copied
  from `origen`. `era`, `lane`, `laneLabel`, `laneOrder`, `regions` from the home tradition unless
  the person's own places say otherwise. `dates`/`start`/`end`: life or working years from a
  source (fact-table row each). `modernCountries`: copy IDs from an existing census entry naming
  the same place; never type an ID from memory; leave a place out rather than guess. `id`: a new
  lowercase-hyphen slug (check `movements` and `retiredMovements`). `atlasId: "TBD"`. `entry`:
  null. `living`: false. `reviewStatus`: "AI-checked". No `people` field.
- **The prose.** sourcing, floorNote, relationsSummary, why, teaser, longDescription, voices,
  legacy. Say plainly where the person is told ("Told within ..."). `legacy` should say, from the
  verified quotes in `final_row.counted_traditions`, which later traditions name them and how; it
  is the reason this person has an entry. Every factual sentence gets a fact-table row with file,
  lines and a verbatim quote (or the census source it rests on). Contested claims name both sides
  (for example Pamphilus's Apology: Eusebius calls it joint; Jerome denies it).
- **concerns.** For each link in `links_naming_person`, read the note and quotes. If they are about
  this person, add `{"link_id": ..., "concerns": "<new person id>"}`. Do not overwrite a link whose
  `concerns` is already set; list it in `flags`. One person per link; if a link names two of the
  new people, choose the one whose words or acts its sources quote, and say so in `flags`.
- **people row.** The home tradition's row item for the person (`people_row_items`) is replaced by
  `{"person": "<id>"}`. Write `{"movement": home id, "replace_name": "<row name or null>",
  "person": id}` in `rows`. If there is no item, `replace_name` is null (the item is added).
- **links.** Draft no new link unless the entry's own prose states a relationship between two
  traditions that the census lacks; then follow the link method in the G3 brief. Being named or
  cited by a later writer is not a link: say "names him" or "cites him", not "influenced".

## Output: `<your folder>/Draft.json`

`{"entries": [...], "fact_table": [...], "concerns": [...], "rows": [...], "links": [],
"wants": [...], "flags": [...]}`.

Run, and fix every line it prints:

    cd /tmp/claude-0/-home-user-CIC-Project/169e494a-41f0-5483-9c1c-9d54f9275f46/scratchpad/g3b/lib1577 && python3 /tmp/claude-0/-home-user-CIC-Project/169e494a-41f0-5483-9c1c-9d54f9275f46/scratchpad/g3b/build/check_draft.py <your Draft.json>

Prose must score Reading Ease 60+ and FK grade 10 or less per paragraph. Plain words, short
sentences, active voice, no hedging filler, no AI tells. Finish with a short summary.

## For these three (added after the Library filled their wants, PR #1577)

The 13 entries of data release 31 are on branch `claude/p2-g3b-entries` (census
`cic-website/data/world-census.json` there; read it with `git -C /home/user/CIC-Project show
claude/p2-g3b-entries:cic-website/data/world-census.json`). Use them as your models too, above all
`basil-of-caesarea`, `gregory-vii` and `innocent-iii`, and avoid their IDs. Their reviews fixed
these points; do not repeat them: floorNote is only the doctrinal-floor note ("Not in question.");
caveats go in sourcing; no English rendering of your own (quote the English edition, or give the
Latin with no rendering and flag it); dates from a source.

- **Pamphilus of Caesarea** (`final_row.home`: alexandria-catechetical). His own words: the Apology
  for Origen, Book I, in Rufinus's Latin (`pamphilus_apologia-pro-origene-rufinus-lat_lommatzsch1846.txt`;
  PG 17 as a second witness). Eusebius calls the Apology written by him and Pamphilus together;
  Jerome denies Pamphilus wrote it. Mark's ruling B counts a jointly written work as his own words:
  say so plainly, and name Jerome's view as the other side. He is told within the catechetical
  school, where the Library shelves the Apology.
- **Bonaventure** (home: the-franciscan-movement). His own works: the Legenda maior in Salter's
  English (1904) and the Tria opuscula in Latin (1911). He founded nothing.
- **Heraclius** (home: byzantine-imperial-church-heraclian-iconoclast). His own words: the Ecthesis
  (638), a document issued in his name, in Mansi X (Lateran 649, Secretarius III, lines about
  100110-100680 of the Mansi tome 10 file). Say who the sources say drafted it only if a vendored
  line says so. His dates: the reviewed row notes that 610-641 is not yet sourced from a Library
  line; find one or leave the dates as the census gives them and say so.

Write `Draft.json` in `/tmp/claude-0/-home-user-CIC-Project/169e494a-41f0-5483-9c1c-9d54f9275f46/scratchpad/g3b/build/p5/`.
