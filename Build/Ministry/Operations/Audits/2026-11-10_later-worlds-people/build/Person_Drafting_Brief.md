# P2-G3b build: drafting brief for the person entries (data release after 30)

Mark ruled (2026-11-10, "take every recommendation"): 14 people named across the later worlds get
person entries. You draft some of them. Repo root `/home/user/CIC-Project`. **Do not edit any file
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

    cd /home/user/CIC-Project && python3 Build/Ministry/Operations/Audits/2026-11-10_agreed-entries/check_draft.py <your Draft.json>

Prose must score Reading Ease 60+ and FK grade 10 or less per paragraph. Plain words, short
sentences, active voice, no hedging filler, no AI tells. Finish with a short summary.
