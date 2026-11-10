# Church Family Tree links, era 10, part 1 (P2-L10) — 2026-11-10

- **Launch prompt:** `Build/Ministry/Features/Church-Family-Tree/Launch-Prompts/CFT_Phase2_Links_Era_Launch_2026-11-07.md`.
- **Method:** `Build/Ministry/Operations/Audits/2026-11-06_census-lineage-rigor/Drafting_Brief.md`, amended 2026-11-10 for the seventh type.
- **Era addendum:** `Drafting_Brief_Era10.md`. It covers the era 10 evidence rule and the rulings of 2026-11-10.

## Era 10 runs as two pull requests

Era 10 has 71 movements, split by lane.

- **Part 1 (this folder): 38 movements.** These are the Protestant and Evangelical lane, the Global Revival and Pentecostal lane, the Syriac East / Protestant bridge, the Greek East / Protestant span and the Cross-Family lane. `Roster.json` lists them.
- **Part 2 (`../2026-11-10_links-era-10-part-2/`): 33 movements.** These are every other lane.

Part 1 owns a relationship whenever a part 1 text names it.

## Rulings made during this pass (Mark, 2026-11-10)

1. **Evidence for era 10 links: (b).** A church body's own dated text read online may be a primary source. So may a study confirmed in the run. A link resting on them reaches Widely Accepted at most. Documented still needs a quote held in the Library. The validator enforces the cap. Atlas Decision-Log, "Change order: evidence for era 10 links".
2. **The drafters' questions.**
   - **Q1, membership: (b).** A seventh link type, "member of". It is never major and carries no outcome.
   - **Q2, a movement writer's own dated text:** counts when the entry names the writer as a carrier, capped at Widely Accepted.
   - **Q3, *Religious Bodies 1906*:** each denomination's own statement counts as its text, while the Census Bureau's general statements do not.
   - Atlas Decision-Log, "Change order: a seventh link type".

## Rounds

1. **Inventory** (Haiku): `Inventory.json`. 38 movements, 193 named relationships, 127 with a census match. The drafters corrected it.
2. **Draft** (Opus, six groups A to F): `Draft_GroupA.json` to `Draft_GroupF.json`. The merge is in `Drafting_Record.json`.
   - Five links were drafted twice. One was kept each time, with the reason in `merge_dropped`.
3. **Online quote check** (a script, then a second method): `Online_Quote_Check.json`. All 78 online quotes were found verbatim.
   - 64 matched by raw download and exact match.
   - 14 were confirmed by a second method:
     - 7 scanned pages, against their page images, by a separate agent;
     - the Adventist Year Book, against the drafter's saved copy, because the site blocks plain downloads;
     - two-column PDFs, by plain text extraction;
     - one page whose markup puts a space before a comma.
   - The first runs of the check reported false failures. A cut-off download and HTML stripping applied to plain text caused them, and both are fixed in the script.
4. **Review round 1** (separate Opus agent, full): `Opus_Review_Round1.json`. Verdict: revise. 0 blocking, 8 substantial, 11 minor, no fabrication. The substantial findings were:
   - a false "first year" sentence about Korea;
   - a quote credited to the Disciples' statement that is the Census Bureau's own;
   - a link resting on the Bureau's text alone;
   - two writers' texts not flagged for Q2;
   - a study cited for more than its title;
   - new map wording in rewritten fields;
   - a source misdescribed;
   - "the family's own" said of Lausanne's critiques.
5. **Revision round 1** (Opus): `Revision_Round1.json`. All 19 were fixed, three of them differently from the reviewer's fix, with reasons. The rulings were then applied:
   - the Disciples to the World Council of Churches became "member of";
   - the mainline "gave rise to" link to the World Council of Churches was removed, because its source shows who joined, not descent;
   - the Q2 and Q3 links were regraded or confirmed.
6. **Review round 2** (separate Opus agent, targeted recheck): `Opus_Review_Round2_TargetedRecheck.json`. Verdict: pass. Three minor findings (a note's referent, the audit trail on two links, two dispositions resting on a publisher's description) were applied as written.

Two of the three rounds in the cap were used. No finding is open.

## Counts

- **Links added: 33.**
  - Grades: Widely Accepted 20, Dominant Modern Reconstruction 9, Inferential-Thin 3, Contested 1, Documented 0.
  - Types: influenced 13, gave rise to 10, argued against 6, continued as 2, broke with 1, member of 1.
- **No link is Documented.** The Library holds no text for these movements. Every primary is a text read online, so the cap holds.
- **Existing links:** 8 changed, 7 kept. From, to and type are unchanged on every one. No link was retired, and every published ID stands.
- **Census links:** 578 before this pass, 611 after. This is data release 27 (2026-11-10).
- **Dispositions (261):** link 97, no-entry 78, kept-as-is 48, qualify 34, remove 2, out-of-scope 2.
- **Prose:** 41 movement fields changed. Every changed paragraph, and every new or rewritten note and outcome, scores Reading Ease 60 or more and FK grade 10 or less on `engine.m7.turn_readability.score_turn`. No sentence runs past 25 words.

## Major links

- **Major by type:** 13 (gave rise to 10, continued as 2, broke with 1).
- **Major by outcome:** 2.
  - The Catholic Church, 1906-1962, argued against the ecumenical movement. Pius XI, *Mortalium Animos* (1928): "Rome would not take part in the movement's meetings and Catholics could not lawfully support it."
  - The East African Revival influenced the Anglican Communion. Bishop Stuart's "The New Way" (1943), a fourteen-point program for how the church and the revival should work together.
- **Judged and found minor:** the other links of the judged types. Each reason is on the link's `major` block in `Drafting_Record.json`.

## Two-way check

- **Prose to links:** every relationship named in a part 1 movement's four fields has a link, or its sentence was qualified or removed, or it names no census movement, or part 2 owns it, or it is not a relationship claim. The per-relationship record is `Drafting_Record.json`, `dispositions`.
- **Links to prose:** every link added or changed is named in the text of one of its movements (`named_in_text` on each link). Round 1 confirmed both directions.

## Open items

These are logged in `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md`:
- **143:** what grade a "member of" link takes on a council's own record alone. This is for part 2, which holds the Greek church and its 1948 membership.
- **144:** the 1904-07 revival entry calls the three revivals "unconnected". Dyer (1913) says news of Wales reached Mukti. The fix runs through three fields, so it is left for the entry's owner.
- **145:** five tree-page recordings now read old descriptions. These are Global South Pentecostal, Hebrew Roots, Rātana, the Chinese church and the ecumenical movement. Re-voicing them is a paid run, so it is Mark's call, after a sample.

## Wanted texts

There are 72 entries in `Drafting_Record.json`, `wants`. These public-domain texts could be vendored into the Library and would let links rise to Documented:
- *The Apostolic Faith* (1906-08), the Azusa Street mission's paper;
- the Assemblies of God General Council minutes (1914-16);
- *Religious Bodies: 1906*, Part II;
- the 1920 Lambeth Conference report;
- Jones and Noble, *The Korean Revival* (1910);
- Dyer's life of Pandita Ramabai (1913);
- *Christian Work in Latin America* (1917);
- Machen, *Christianity and Liberalism* (1923);
- Barth, *Der Römerbrief* (1919).
