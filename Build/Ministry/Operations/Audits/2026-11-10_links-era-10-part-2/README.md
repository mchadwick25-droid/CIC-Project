# Church Family Tree links, era 10, part 2 (P2-L10) — 2026-11-10

- **Method:** the same as part 1. See `../2026-11-10_links-era-10-part-1/README.md`, the method
  brief `../2026-11-06_census-lineage-rigor/Drafting_Brief.md` with its 2026-11-10 amendments, and
  `Drafting_Brief_Era10.md` here.
- **Scope:** part 2 is the 33 era 10 movements outside the Protestant, Pentecostal and bridge
  lanes. That means the Greek East, Latin West, Africa, Syriac East, Caucasus, Non-Nicene,
  Greek/Latin, Africa/Latin and Latin/Protestant lanes. `Roster.json` lists them.
- **Ownership:** part 1 (data release 27, PR #1569) owned every relationship a part 1 text names.
  Part 2 drew none of those pairs again.

## Rulings in force (Mark, 2026-11-10)

All are recorded in the Atlas Decision-Log, 2026-11-10.

- **Era 10 evidence (b):** sources read online support a link up to Widely Accepted. Documented
  needs a Library quote.
- **"member of":** the seventh link type, never major.
- **Writers' own dated texts:** they count when the entry names the writer as a carrier.
- ***Religious Bodies 1906*:** a denomination's own statement counts as that body's own text.
- **Membership rolls:** a body's own dated membership record alone carries a "member of" link to
  Widely Accepted. This settled Open-Gaps 143.

## Rounds

1. **Inventory** (Haiku): `Inventory.json`. 33 movements and 109 named relationships. The drafters
   added more than twenty it missed and corrected its wrong matches.
2. **Draft** (Opus, four groups G to J): `Draft_GroupG.json` to `Draft_GroupJ.json`, merged in
   `Drafting_Record.json`. Two links were drafted twice; the record keeps one of each and gives
   the reasons in `merge_dropped`.
3. **Online quote check:** `Online_Quote_Check.json`. 113 quotes.
   - 107 were matched by raw download and exact match.
   - The rest were confirmed by a second check: page images for part 1's kept link, the
     non-www address of the Saint-Serge page, and the round 1 reviewer's raw fetch of the
     wrldrels.org profile.
   - The coordinator's own fetches of wrldrels.org met a CAPTCHA, and no attempt was made to get
     past it.
4. **Review round 1** (separate Opus agent, full): `Opus_Review_Round1.json`. Verdict: revise.
   It found no fabrication and nothing blocking, but 6 substantial and 11 minor findings:
   - two links rested on the World Council of Churches' summaries of other churches;
   - two rested on studies that do not cover them, or that were confirmed by title only;
   - Lviv 1946 rested on facts no listed source gives;
   - a map word appeared in a note;
   - Taizé and Iona contradicted themselves.
5. **Revision round 1** (Opus): `Revision_Round1.json`. All 17 findings were fixed, three of them
   differently, with reasons.
   - The Balkan → Greek church link now rests on the Church of Greece's own history.
   - The two American Orthodoxy links now rest on a passage read in Plekon, *Religions* 7 (2016).
   - The Lviv link is Dominant Modern Reconstruction on Bociurkiw.
6. **Review round 2** (separate Opus agent, targeted recheck):
   `Opus_Review_Round2_TargetedRecheck.json`. Verdict: pass, with no findings.

Two of the three rounds in the cap were used. No finding is open.

## Counts

- **Links added: 33.**
  - Grades: Widely Accepted 24, Dominant Modern Reconstruction 9, Documented 0.
  - Types: gave rise to 10, influenced 9, continued as 7, in contact with 3, member of 2, broke
    with 1, argued against 1.
- **"member of" links:** the Church of Greece to the World Council of Churches (1948), and the
  Kimbanguist church, through the African-initiated churches entry (1969).
- **Existing links:** 3 changed, 16 kept. From, to and type are unchanged on each changed link. The
  Tridentine → post-Vatican II link was regraded from Inferential-Thin to Widely Accepted on
  Summorum Pontificum (2007). No link was retired.
- **Census links:** 611 before this pass, 644 after. This is data release 28 (2026-11-10).
- **Major by outcome:** 8 links carry `outcome`.
  - Malankara and Antioch (1975).
  - Georgia and Russia (1943).
  - The Georgian tomos.
  - Anglican → Philippine Independent Church (the 1947 Declaration).
  - The liturgical movement → post-Vatican II (Sacrosanctum Concilium).
  - Tridentine → post-Vatican II (Summorum Pontificum).
  - Pius X → Chinese Catholicism (Ad Apostolorum Principis).
  - Part 1's Pius X → ecumenical movement link (Mortalium Animos), kept.
- **Dispositions (161):** link 58, kept-as-is 45, no-entry 35, qualify 8, out-of-scope 8,
  remove 5.
- **Prose:** 18 movement fields changed. Each scores Reading Ease 60 or more and FK 10 or less on
  `score_turn`, and no sentence runs past 25 words.

## Era 10 after both parts

- **Coverage:**
  - 66 links were added across the two parts (data releases 27 and 28).
  - Era 10 movements with no "gave rise to" or "continued as" link coming in went from 48 of 71 to
    28.
  - 9 have no link at all: IX.7, IX.30, IX.51, IX.54, IX.58, IX.60, IX.61, IX.70, IX.73. For
    each, either its text names no relationship to a census movement that a source opened in the
    run supports, or the relationship is held for a ruling or a text (Open-Gaps 149).

## Two-way check

- **Prose to links:** every relationship named in a part 2 movement's four fields has a
  disposition (`Drafting_Record.json`). Round 1 found one missed claim, Taizé and Iona's "modern
  heirs", and it was fixed.
- **Links to prose:** every link added or changed is named in its movements' text, and each carries
  a disposition with its `link_id`.

## Open items (Open-Gaps)

- **147:** the Sayfo entry's "gone quiet after about 1300".
- **148:** joint declarations, and no entry for Rome after 1962. Two links use the post-Vatican II
  parish entry with stated reasons.
- **149:** the 9 era 10 movements still unlinked, and two more stale tree recordings.

## Wanted texts

41 entries in `Drafting_Record.json`, `wants`. Among them:
- the 1918 collection of the Moscow council's definitions;
- the Acta of the 1899 Plenary Council of Latin America;
- the 1850 Tomos and the 1928 Act of the Church of Greece;
- the Medellín and Puebla conclusions in an edition that opens;
- the CELAM founding decree;
- Naayem (1921);
- Houteff's 1930 printing.
