# Era 10 links: drafting brief (addendum)

Era 10 is the global church era, 1906 to about 2010. It has 71 movements and runs in two parts,
split by lane. Each part has its own audit folder, review rounds and pull request.

- **Part 1** (38 movements): the Protestant and Evangelical lane, the Global Revival and
  Pentecostal lane, the Syriac East / Protestant bridge, the Greek East / Protestant span and the
  Cross-Family lane. Folder `Build/Ministry/Operations/Audits/2026-11-10_links-era-10-part-1/`.
- **Part 2** (33 movements): every other era 10 lane. Folder
  `.../2026-11-10_links-era-10-part-2/`.

Each folder's `Roster.json` lists its movements.

The launch prompt is
`Build/Ministry/Features/Church-Family-Tree/Launch-Prompts/CFT_Phase2_Links_Era_Launch_2026-11-07.md`.
The method is `Build/Ministry/Operations/Audits/2026-11-06_census-lineage-rigor/Drafting_Brief.md`:
the six types, the five grades, the note rules, and "grade the relationship, not the events". It
applies unchanged, except for the evidence rule below. Read it in full first.

`Build/Ministry/Operations/Audits/2026-11-08_links-era-9-part-1/Drafting_Brief_Era9.md` shows the
dispositions (link, qualify, remove, no-entry, out-of-scope, kept-as-is) and the
existing-link actions (keep, rewrite, regrade, retype, remove). Use them as written there.

## The evidence rule for era 10 (change order, Mark, 2026-11-10: "b")

Atlas World Map Decision-Log, "Change order: evidence for era 10 links". Most era 10 sources
fall after the Library's public-domain reach (about 1930). The recent-movement evidence rule of
2026-11-08 therefore also applies to links:

- **A church body's own dated text read online.** A basis of union, a constitution, a founding
  charter, an official statement or a conference report may be a `primary` source when you
  opened it yourself in this run.
  - Give `work` (title, date, the body or publisher), `url` (https), `accessed` (YYYY-MM-DD),
    `locus` (article, section or page), a verbatim `quote` copied from the page as you read it,
    and `license` ("rights reserved; short quotation" unless the page states otherwise).
  - Do not give `file` or `lines`.
  - Keep each quote short: one or two sentences.
- **A scholarly study not yet cited in the repo.** It may be cited once you have confirmed its
  author, title, publisher and year in this run, from a publisher or library page. Give `url` and
  `accessed` for that page.
  - A study confirmed only by its details supports nothing beyond its title. It is support named
    but not read (`named-not-rechecked`).
  - To rest a claim on what a study says, you must have read the passage (for example a preview
    page). Then quote it, with `url` and `accessed`.
- **The cap.** A link resting on sources read online can reach Widely Accepted at most, never
  Documented. Documented still needs a primary quote held in the Library (`cic/texts/`), which
  anyone can re-check word for word. The validator enforces this. Put the text that would raise
  the link on the `wants` list.
- **`verification_state`.**
  - Use `verified-online` when the quote the link rests on was read online in this run.
  - Use `verified-direct` only for quotes checked in a Library file.
- **What never counts.** A search-engine snippet, a summary, an encyclopedia mirror or Wikipedia
  is never a source. An item you could not open stays out, and goes to `wants`.
- **Nothing after 2010** appears in a note or an outcome. A source dated later may still support
  an earlier fact; say so in `drafter_flags`.

## Who owns a relationship

- **Eras 1 to 9 are done.** A relationship between an era 10 movement and an earlier movement is
  yours when the era 10 text names it. If a link for it is already on main, review it as an
  existing link. If only the earlier movement's text names it, that era's pass owned it: leave it,
  unless it is missing, and then flag it.
- **The new rows IX.59 to IX.73** (data release 25) have no links yet. Their parents in eras 8
  and 9, named in their own text, are yours to draft.
- **Between the two parts:** part 1 owns a relationship whenever a part 1 text names it. Part 2
  drafts a cross-part relationship only when the part 2 text alone names it.

## Rulings of 2026-11-10 (Mark), after the part 1 drafts

- **Membership:** use the seventh type, `member of` (method brief amendment of the same date).
- **A movement writer's own dated text:** for a movement that never became a church body, a dated
  text by a writer the entry itself names as a carrier counts as the movement's own text. It is
  read online and capped at Widely Accepted.
- **Religious Bodies 1906:** each denomination's own statement in the report counts as that
  body's text. The Bureau's general statements do not.

