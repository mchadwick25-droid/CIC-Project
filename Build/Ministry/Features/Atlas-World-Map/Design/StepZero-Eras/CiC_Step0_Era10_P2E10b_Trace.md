# Era 10, P2-E10b: trace of every new sentence

Companion to `CiC_Step0_Era10_P2E10b_Proposed.json`. Each new sentence in that file is listed here with the evidence it rests on. "E" and "item" numbers are the evidence lists in `CiC_Step0_Era10_Movements_V1_0.md`, under the candidate named. "SectionA_Research" is `CiC_Step0_Era10_P2E10b_SectionA_Research.md` (2026-11-08). "repo" marks a relation that rests on census text (release 21), as the movements record's own Overlap lines do; these are flagged, since census text is counted apart from verified items.

## Revision log (after Round 2)

Against `CiC_Step0_Era10_P2E10b_Review_Round2.md`. The mechanical fixes only; S2-2 is held for Mark.

- **S2-1** Done. IX.54 floorNote is the review's text: "Citygate Network, the name the union took later ... The only copy seen was undated and recent."
- **S2-2** Not acted on. IX.53 stays held, pending Mark (Open-Gaps, "IX.53, faith missions, held").
- **M2-1** Done. IX.57 statusDescription: "hands on to the Vineyard, formed in 1982."
- **M2-2** Done. IX.16 legacy: "Court records were part of these bodies' public record too." The last sentence is deleted.
- **M2-3** Done. IX.52 `why` and `longDescription` say "the Lambeth Conference".
- **M2-4** Done. Open-Gaps entries 127 to 131: the `kind` question, Pueblo and the arena, the IX.53 hold, the Vineyard publisher's dated copy, the 2012 AGRM capture.
- **C2-1** Done. IX.52 legacy now reads "Kevin Ward found that by 2006 most of its members belonged to churches outside the West."
- **C2-2** Done. IX.24 "At the 1974 Congress", matching release 21.
- **C2-3** Done. IX.52 longDescription: "a moral obligation", Resolution 15's word.
- **C2-4** Done. IX.55 floorNote: "leaders, directors and staff".
- **C2-5** Done. IX.16 relationsSummary: "Three separately founded bodies share this entry."

## Revision log (after Round 1)

Against `CiC_Step0_Era10_P2E10b_Review_Round1.md`, with the thread's direction of 2026-11-08 and `CiC_Step0_Era10_P2E10b_SectionA_Research.md`.

- **S-1** Done. IX.33 now reads "Billy Graham's Los Angeles campaign of 1949 ran for more than eight weeks instead of the three planned." The source note stays.
- **S-2** Done. IX.52 and IX.58 are graded CR (Contemporary-Reported). IX.52 stays "settled". IX.53's grade is moot: the row is held (below); its added evidence, M5 E4, is carried in the held note.
- **S-3** Changed approach, by direction. The row is kept, not held. G-64's condition is met: Section A is now settled on a carrier's dated statement, HSLDA's "What We Believe" (22 April 2020). IX.55's floorNote clears on it.
- **S-4** Done, reworded. The quotation and its attribution are gone. The legacy reads "In 2001 Mitchell Stevens told the story of homeschooling as a social movement." The book's own subtitle ("the Homeschooling Movement") supports that. It is plainer than the review's "a university-press study could treat" (FRE 46.6 against 11.1).
- **S-5** Done. Edit [0] on IX.24 is dropped. All the IX.24 sentences now follow "...how separated churches should act together." They run in order: the Winters' paper ("At the 1974 congress"), the IMB and CPM, Tearfund, then Stanley and Graham. "Its age" became "this evangelical age", so it cannot be read as Tearfund's.
- **M-1** Done. IX.51 now says "presented", and "set out its teaching".
- **M-2** Done, by direction. The statusDescription pointer is deleted. The relationsSummary now ends "Iglesia ni Cristo has its own entry." (the direction's plain pointer, not the review's "in the same lane"). The legacy's dangling "one" is fixed, as the review gave it.
- **M-3** Done. Seven IX.16 text fields are whole-field `set` edits, with plain sentences: statusDescription, floorNote, relationsSummary, why, teaser, longDescription and legacy. The teaser keeps the three body names that the review's rewrite left out. "Row" became "entry", since "row" is an internal word. "Descends from" became "grew out of", the past tense ruling 4 asks for. "Packed on one register row for roster economy" and "for the map's economy" are removed.
- **M-4** Changed approach. IX.53 is moot (held). IX.56 and IX.57 keep their modernCountries as drafted. Adding the United States raised two validator errors: `validate-census.mjs` requires each modern country's place to stand on the place label. No row gives "N. America" a country, and a label names at most two places. Relabeling IX.57 as "United States" would drop Toronto, where the 1994 revival began.
- **M-5** Superseded. IX.54 and IX.55 now clear Section A. Both floorNotes are rewritten in the past tense, with no present-tense claim.
- **M-6** Done, in both relationsSummary and statusDescription.
- **M-7** Done. "With 47 not voting" is dropped.
- **M-8** Done. The sentence ends at "men's movement".
- **M-9** Moot (IX.53 held). The fix is carried in the held note.
- **M-10** Kept as ruled (G-28). `_meta.kind` says P2-E10c rules on the field, IX.57 included. The fit question is noted below for P2-E10c. The Open-Gaps entry is not made here, because this revision edits only its two files. It is flagged for the thread.
- **M-11** Done. Every listed rewrite is applied, and every other listed field of the new rows is made plainer. The before and after table is below.
- **M-12** Done. IX.30 now reads "In 2021 Lester Ruth and Lim Swee Hong published a history of contemporary praise and worship."
- **C-1** Done. The new rows follow the key order of the 49 era 10 rows, with `kind` last.
- **C-2** Moot (IX.53 held). The fix is carried in the held note.
- **C-3** Done. The text now says "where Fenwick and Spinks close the Catholic movement".
- **C-4** Done. The text now says "on birth control".
- **C-5** Changed approach. "From Boulder" is dropped: neither an evidence item nor the Movements review's reading records it. Pueblo and the arena stay. They are traced to E2's article as Movements Review Round 1 M-12 read it. E2's item text in `CiC_Step0_Era10_Movements_V1_0.md` should still record them. That file is outside this revision, so the gap is flagged for the thread.
- **C-6** Done. The applier now applies `metaEdits` as written and checks them against a recount. Its sentence and readability checks read the applied fields, not the trace data.
- **Found in revision.** IX.55's sourcing called Milton Gaither's book a university-press study, but its publisher is Palgrave Macmillan. It now reads "two studies from university presses ... and a history by Milton Gaither (2008)". IX.57's sourcing said "four academic studies" for five works by four scholars. It now says "the work of four scholars".
- **Direction 1 (IX.53).** Held, the same way the rulings hold the healing revival and the Oxford Group (G-69, G-72): no statement of faith was found, so Section A cannot be assessed. The row is removed from newRows, and its atlasId stays reserved. Its named lines are listed under "Held with IX.53". `metaEdits` are now 301 to 307 rows and 219 to 225 Pre-Survey Candidates. No other row or edit referred to IX.53.


## Notes for review

- **atlasIds.** IX.52 The Anglican Communion; IX.54 rescue missions; IX.55 the Christian homeschool movement; IX.56 the liturgical movement; IX.57 the Third Wave; IX.58 Promise Keepers. IX.53 is unused and reserved for the faith-mission movement, held (below). IX.50 stays reserved for G-15.
- **Section A, assessed on the carriers' statements** (SectionA_Research, method A1). The grades stay here in the record. Participant text gives only the past-tense content, and a date where one is seen.
  - IX.54 clears directly on Citygate Network's "Statement of Faith". It covers the Trinity, Christ's deity, the virgin birth and the bodily resurrection. Grade: post-2010 and undated. The only copy seen is the live page, read 2026-11-08; its earliest capture is 2025-08-23 [S]. It is evidence for the later network's confession, not the IUGM's of 1913. The 2012 AGRM capture (agrm.org/agrm/Statement_of_Faith.asp, contents unseen) is the lead for an earlier date.
  - IX.55 clears directly on HSLDA's "What We Believe", dated 22 April 2020. That date is 37 years after the founding, and post-2010. The statement binds HSLDA's leaders, directors and employees, not its members. This meets G-64's condition ("settled on a carrier's dated statement before the entry is built").
  - IX.57 clears directly on the Vineyard "Statement of Faith". Its content is verified on the publisher's own booklet (Vineyard USA, *Core Values & Beliefs*, 2023). Its adoption by the AVC board in November 1994 is seen only on copies published by others: [S] as to the publisher. The publisher's own dated copies, the Wayback captures of 2002 and 2009, are still to be read.
  - IX.53 cannot be assessed: no IFMA or CrossGlobal Link doctrinal text was seen. It is held.
- **No row now carries a "not yet assessed" floorNote**, so the review's method-page note on that state no longer applies to this proposal.
- **Relations resting on census text.** Each new row's relationsSummary, and one sentence in each of three statusDescriptions, places the row against existing entries, as the record's Overlap lines do. They rest on release-21 census text, not on a verified item. They are marked "repo" below.
- **Fields left empty or absent.** `documentedStories` is `[]` on all six rows: the record drafts no stories. `streams` is left off, as on 31 of the 49 era 10 rows: no item names a stream. `entry` is null (nothing built). `c2` is null (no c2 run). `modernCountries` is `[]` on IX.57: its place label is "N. America", which carries no country on any row. IX.56 has no Belgium entry, because no Belgium ID is used anywhere in the census. Neither row can add the United States without a validator error (M-4, above).
- **Region choices.** IX.54's region is "New York, then the U.S. and Canada". The draft's "U.S., Canada" has no single gazetteer place, and New York's IDs are VIII.19's. IX.56 drops the draft's "Germany": no verified item names a German carrier. IX.57 drops the draft's "UK": no verified item places the movement there.
- **Living evidence** is kept in `livingEvidence`. Per G-51(a), the same items sit in `sources[]` with the note "Evidence for the living mark only". Only IX.57 (Bialecki, university-press fieldwork) is CD. The rest are CR or n/a (S-2).
- **IX.58.** The Stand in the Gap figure is a crowd estimate (formation_confidence: Contested). The copy says "estimated", and the statusDescription says the size "rests on a crowd estimate".
- **`kind` (M-10).** The five movement rows carry `kind: "cross-church movement"` as ruled (G-28). IX.52 is a church body and carries no kind. For P2-E10c: the review asks whether IX.57 fits. Its unit includes the Association of Vineyard Churches, a church association carried inside the Third Wave, while G-28 gives the kind to "a movement outside church bodies". P2-E10c should rule on it explicitly, and on whether the value enters before c defines the field.
- **Named lines placed:** frontier missions and CPM (IX.24, G-58(b), G-59(a)); relief and development (IX.24, G-61(a)); mass evangelism (IX.24 and IX.33, G-34(a)); broadcasting (IX.33, G-65(a)); Word of Faith (IX.45, G-75(a)); Jesus music (IX.45) and praise and worship (IX.30, G-76(a)); the Toronto Blessing (IX.57, G-74(a)); the new monasticism (IX.28, G-67(b)). Bible translation (Camp Wycliffe, G-56(a)) is held with IX.53.
- **Frontier missions** is held as an entry (G-79(c)), but G-58(b) makes it a named line in IX.24 now, and G-59(a) puts CPM beside it. The two lines are separate sentences, so the frontier line can be dropped on its own if "held" is read as covering the line.
- **Not placed, with the reason:** Keswick (G-70(a): "nothing new"; VIII.4 is frozen). The UBS and Eugene Nida (G-56(a)) go to the cross-era Bible-translation thread, which has no census row. MacArthur and Grace to You (G-18(b)): no verified item; the record has only [S] (W22). IX.11's prosperity line already stands under G-54(a), so nothing is added there. The healing revival, the Oxford Group, the student movement, frontier missions and now the faith-mission movement get no rows.
- **IX.16, fields beyond the list.** Removing Iglesia ni Cristo also changes `dates` and `start`, from 1914 to 1926, the founding of La Luz del Mundo (from the row's own text). It also changes `region`, `placeLabel` and `modernCountries` (Philippines out; South Korea in, with VIII.21's IDs). `statusWord` still says "the row-split fork stays open". It is left as it is, since splitting the other three bodies was not ruled. The row's `id` keeps "iglesia-ni-cristo-..." because ids are permanent.
- **Meta.** Applying the rows needs `meta.totalEntries` 301 to 307 and `statusCounts["Pre-Survey Candidate"]` 219 to 225 (`metaEdits`).


## Readability, before and after Round 1

Flesch Reading Ease per field, with `engine/m7/readability.py`'s syllable counter and formula applied to every field (the module itself leaves fields under 30 words unscored), as the review measured. "Names" gives the score with each capitalized word after the first in a sentence stood in by a one-syllable word; where that score clears 60, the field stays below 60 only because of proper names and titles.

| row | field | before | after | names |
|---|---|---|---|---|
| IX.16 | floorNote | 53.4 | 63.2 |  |
| IX.16 | legacy | 67.8 | 71.9 |  |
| IX.16 | longDescription | 37.0 | 55.7 | 83.7 |
| IX.16 | relationsSummary | 49.5 | 65.1 |  |
| IX.16 | sourcing | 62.8 | 62.8 |  |
| IX.16 | statusDescription | 58.5 | 69.1 |  |
| IX.16 | teaser | 5.1 | 53.2 | 92.9 |
| IX.16 | why | 37.5 | 59.4 | 79.6 |
| IX.51 | longDescription | 63.4 | 62.5 |  |
| IX.52 | floorNote | 68.1 | 68.1 |  |
| IX.52 | legacy | 67.8 | 67.8 |  |
| IX.52 | longDescription | 51.6 | 55.6 | 80.7 |
| IX.52 | relationsSummary | 54.0 | 64.3 |  |
| IX.52 | sourcing | 48.4 | 50.4 | 84.9 |
| IX.52 | statusDescription | 41.6 | 56.0 | 83.4 |
| IX.52 | teaser | 63.9 | 63.9 |  |
| IX.52 | why | 53.5 | 69.2 |  |
| IX.54 | floorNote | 85.9 | 67.3 |  |
| IX.54 | legacy | 47.8 | 74.0 |  |
| IX.54 | longDescription | 46.4 | 50.9 | 76.6 |
| IX.54 | relationsSummary | 58.4 | 62.7 |  |
| IX.54 | sourcing | 32.5 | 50.6 | 87.6 |
| IX.54 | statusDescription | 62.4 | 62.4 |  |
| IX.54 | teaser | 73.2 | 73.2 |  |
| IX.54 | why | 49.3 | 55.7 | 62.5 |
| IX.55 | floorNote | 48.6 | 74.3 |  |
| IX.55 | legacy | 18.8 | 46.6 | 60.7 |
| IX.55 | longDescription | 60.2 | 60.2 |  |
| IX.55 | relationsSummary | 42.8 | 50.5 | 69.8 |
| IX.55 | sourcing | 38.2 | 52.0 | 72.3 |
| IX.55 | statusDescription | 64.1 | 64.1 |  |
| IX.55 | teaser | 40.6 | 63.9 |  |
| IX.55 | why | 45.8 | 55.7 | 61.7 |
| IX.56 | floorNote | 42.6 | 58.7 | 91.0 |
| IX.56 | legacy | 46.1 | 55.4 | 95.8 |
| IX.56 | longDescription | 47.3 | 46.1 | 82.2 |
| IX.56 | relationsSummary | 50.9 | 64.9 |  |
| IX.56 | sourcing | 74.1 | 74.1 |  |
| IX.56 | statusDescription | 52.9 | 55.7 | 81.1 |
| IX.56 | teaser | 28.8 | 52.9 | 78.2 |
| IX.56 | why | 37.5 | 41.1 | 79.3 |
| IX.57 | floorNote | 64.2 | 67.8 |  |
| IX.57 | legacy | 42.7 | 57.1 | 78.2 |
| IX.57 | longDescription | 46.5 | 48.9 | 77.7 |
| IX.57 | relationsSummary | 55.3 | 66.5 |  |
| IX.57 | sourcing | 49.5 | 79.8 |  |
| IX.57 | statusDescription | 49.5 | 51.0 | 70.9 |
| IX.57 | teaser | 46.9 | 55.2 | 75.3 |
| IX.57 | why | 56.9 | 66.5 |  |
| IX.58 | floorNote | 69.8 | 69.8 |  |
| IX.58 | legacy | 0.5 | 0.5 | 30.3 |
| IX.58 | longDescription | 51.9 | 51.9 | 68.6 |
| IX.58 | relationsSummary | 33.3 | 53.2 | 62.6 |
| IX.58 | sourcing | 4.6 | 58.4 | 64.4 |
| IX.58 | statusDescription | 55.6 | 61.2 |  |
| IX.58 | teaser | 47.8 | 71.3 |  |
| IX.58 | why | 47.8 | 76.3 |  |

- **Still below 60.** Every field that stays below 60 clears 60 once names are stood in, except IX.58 `legacy`. That field is a verbatim quotation, kept as the review asked. IX.55 `legacy` only just clears without names (60.7); "homeschooling" sets the rest. The house form "Tiered Viable, secondary (Tier 2)" counts as names in the statusDescriptions. IX.51's other fields are release-21 text that this proposal does not edit.
- **Added sentences on the old rows** (scored alone, before and after): IX.24 relationsSummary 35.7 to 49.2; IX.33 relationsSummary 32.5 to 38.2; IX.45 relationsSummary 61.7 to 70.8; IX.45 legacy 35.0 to 38.6; IX.30 legacy 48.5 to 50.6; IX.28 relationsSummary 56.6 to 67.3. The rest is names and titles (National Religious Broadcasters, Maranatha! Music, Calvary Chapel, International Mission Board).
- **Sentence length.** No new or rewritten sentence passes 25 words; the longest is 23. Release-21 sentences in the edited old-row fields still pass 25 words: IX.24 relationsSummary (37 and 31), IX.33 relationsSummary (30 and 41), IX.45 relationsSummary (73) and IX.45 legacy (29 and 28). They are other entries' existing text, which this proposal does not rewrite. They are flagged for the census-wide readability pass.


## Held with IX.53 (the faith-mission movement)

IX.53 is held: no IFMA or CrossGlobal Link statement of faith was seen, so Section A cannot be assessed. The hold follows the rulings' holds on the healing revival (G-72) and the Oxford Group (G-69). The atlasId IX.53 stays unused and reserved for it. When a carrier's statement is staged and Section A is settled on it, the row is built from its draft in `CiC_Step0_Era10_Movements_V1_0.md` §1 M5, with the fixes below.

**Named lines held with it.** They are not placed elsewhere.
- Bible translation (G-56(a)): "Its training began at Camp Wycliffe, which W. Cameron Townsend and L. L. Legters founded in Arkansas in 1934." Evidence: §1 M1 E3 (Encyclopedia of Arkansas, verified). With it: "Wycliffe Bible Translators grew from the same culture" (§1 M5 E8, Svelmoe).
- Voice: "W. Cameron Townsend and L. L. Legters — who founded Camp Wycliffe in Arkansas in 1934 to train Bible translators" (§1 M1 E3).
- Source: Encyclopedia of Arkansas, 'Sulphur Springs (Benton County)', which records Camp Wycliffe, founded in June 1934 by Townsend and Legters to train Bible translators.

**Round 1 fixes to apply when it is built.** S-2: grade CR, and add §1 M5 E4 (Christian Post, the 2012 merger of CrossGlobal Link into Missio Nexus) to its living evidence. M-4: `modernCountries` and region follow the North American carriers, under the validator's rule that a country's place stands on the label. M-9: "Klaus Fiedler (1994) tells it as one story. William Svelmoe (2008) places Wycliffe inside it." C-2: tell the Fiedler sentence once or twice, not three times, with "the Africa of his day". M-11: the plainer teaser, why and legacy the review gives.

**Wanted** (for the source-research thread):
- Edwin L. Frizen Jr., *75 Years of IFMA, 1917–1992* (William Carey Library, 1992). It probably reprints the IFMA Confession of Faith.
- Records of the Interdenominational Foreign Mission Association of North America, Collection 352, Billy Graham Center Archives, Wheaton College. The collection page was behind a human check.
- Wayback captures of ifmamissions.org from 1999 onward, once that host can be reached.
- The Missio Nexus statement of faith, which is behind a member login. It is post-2012 and belongs to a successor body, so it is a lead only.



## IX.52 The Anglican Communion in the Twentieth Century

| field | sentence | evidence |
|---|---|---|
| statusDescription | Tiered Viable, secondary (Tier 2). | §3 Anglicanism Tier; G-78(a) |
| statusDescription | It rests on the records of Lambeth and of the Anglican Consultative Council, and on two standard histories. | §3 Anglicanism E1-E5; B1 |
| statusDescription | Its window opens in 1906, where the Victorian Church of England entry ends. | §3 Anglicanism Overlap (repo: VIII.30 ends 1906); G-78(a) dates |
| sourcing | Rich: the records of the Lambeth Conference and of the Anglican Consultative Council. | §3 Anglicanism B1; E1-E3 |
| sourcing | Two standard histories, by Kevin Ward (2006) and William Sachs, ed. (2017), come from university presses. | §3 Anglicanism B1; E4, E5 |
| floorNote | No question. | §3 Anglicanism Section A |
| floorNote | In 1920 the bishops at Lambeth named the Nicene Creed as the sufficient statement of the Christian faith. | §3 Anglicanism E1 |
| relationsSummary | It carries on from the Victorian Church of England and the Oxford Movement. | §3 Anglicanism Overlap (repo: VIII.30, VIII.5); B3 |
| relationsSummary | Both of those entries end in 1906. | §3 Anglicanism Overlap (repo: VIII.30, VIII.5) |
| relationsSummary | In this era Anglicans also appear inside other stories, such as the East African Revival and the Church of South India. | §3 Anglicanism Overlap (repo: IX.3, IX.32) |
| why | By 2006, Kevin Ward found, most Anglicans lived outside the West. | §3 Anglicanism E4 |
| why | Their bishops met at Lambeth. | §3 Anglicanism E1, E3, E9 |
| why | There they spoke on Christian unity, on birth control and on sexuality. | §3 Anglicanism E1, E9, E3 |
| teaser | A worldwide family of churches whose bishops met at Lambeth, and whose members came to live mostly outside the West. | §3 Anglicanism E1, E4 |
| longDescription | The bishops of the Anglican churches met at Lambeth in 1920, 1930, 1968 and 1998, among other years. | §3 Anglicanism E1, E9, E2, E3 |
| longDescription | In 1920 they sent out an Appeal to All Christian People. | §3 Anglicanism E1 |
| longDescription | It named the Scriptures, the Nicene Creed, the two sacraments and a shared ministry as the ground of a future unity. | §3 Anglicanism E1 |
| longDescription | In 1930 they voted 193 to 67 on limiting or avoiding parenthood. | §3 Anglicanism E9 (the abstentions, 46 or 47 by source, are left out) |
| longDescription | Where a couple clearly felt a moral duty to do so, they said, the method must be decided on Christian principles. | §3 Anglicanism E9 |
| longDescription | In 1968 Lambeth proposed an Anglican Consultative Council. | §3 Anglicanism E2 |
| longDescription | It first met at Limuru, Kenya, in 1971. | §3 Anglicanism E2 |
| longDescription | Over the century most of the Communion came to live outside the West. | §3 Anglicanism E4 |
| longDescription | In 1998 the bishops passed a resolution on human sexuality. | §3 Anglicanism E3 |
| longDescription | In June 2008 the first Global Anglican Future Conference (GAFCON) met in Jerusalem. | §3 Anglicanism E6 |
| longDescription | It issued the Jerusalem Declaration. | §3 Anglicanism E6 |
| legacy | By 2006, Kevin Ward found, most of its members belonged to churches outside the West. | §3 Anglicanism E4 |
| legacy | Ward and William Sachs both tell its twentieth century as one Communion's story. | §3 Anglicanism E4, E5; Overlap |
| voices | The Lambeth Conference of 1920 — whose Appeal to All Christian People named the Nicene Creed as the sufficient statement of the Christian faith | §3 Anglicanism E1 |
| voices | The Lambeth Conference of 1930 — whose resolution on limiting parenthood was the only one that year with a recorded vote | §3 Anglicanism E9 |
| voices | The Anglican Consultative Council — proposed at Lambeth in 1968, and first meeting at Limuru, Kenya, in 1971 | §3 Anglicanism E2 |
| voices | The Global Anglican Future Conference — which met in Jerusalem in June 2008 and issued the Jerusalem Declaration | §3 Anglicanism E6 |

## IX.54 The Rescue Mission Movement

| field | sentence | evidence |
|---|---|---|
| statusDescription | Tiered Viable, secondary (Tier 2). | §1 M12 Tier; G-60(a) |
| statusDescription | Its window opens in 1906, when mission leaders in New York formed a federation of gospel missions. | §1 M12 E3; G-60(a) |
| statusDescription | Its first missions are older, from 1872, and are told here as its beginning. | §1 M12 E2; G-60(a) reach-back disclosed |
| sourcing | Moderate: one study by a scholar, Norris Magnuson's Salvation in the Slums (1977). | §1 M12 B1; E7 |
| sourcing | The network's own history adds to it. | §1 M12 B1; E3 |
| sourcing | So do a 1972 article in Christianity Today and the Billy Graham Center Archives. | §1 M12 B1; E6, E2 |
| floorNote | No question. | SectionA_Research IX.54 (A1: clears directly on content) |
| floorNote | The union, later named Citygate Network, published a statement of faith. | SectionA_Research IX.54 (Citygate Network, 'Statement of Faith', verified; undated); E3 (renamed Citygate Network in 2018) |
| floorNote | It named one God, eternally Father, Son and Holy Spirit. | SectionA_Research IX.54 ('one God, eternally existing as Father, Son, and Holy Spirit', verified) |
| floorNote | It said that Jesus Christ was God, born of a virgin, and that he rose bodily from the dead. | SectionA_Research IX.54 ('the Lord Jesus Christ is Deity, that He was born of a virgin ... that He bodily resurrected', verified) |
| relationsSummary | The Salvation Army did the same kind of work, but as a church body. | §1 M12 Overlap (repo: VIII.6) |
| relationsSummary | Norris Magnuson counts the rescue missions among the revival-based welfare movements of 1865 to 1920. | §1 M12 E7 |
| why | In 1872 Jerry McAuley opened a mission on Water Street in New York. | §1 M12 E2 |
| why | Others followed. | §1 M12 E2 |
| why | In 1906 mission leaders in New York joined in a federation. | §1 M12 E3 |
| why | A historian counts these missions among the revival-based welfare movements of 1865 to 1920. | §1 M12 E7 |
| teaser | City gospel missions, from New York's Water Street in 1872 to a union of missions in 1913. | §1 M12 E2, E3 |
| longDescription | In 1872 Jerry McAuley opened a mission on Water Street in New York. | §1 M12 E2 |
| longDescription | Others followed. | §1 M12 E2 |
| longDescription | In 1877 Colonel George Clarke and his wife Sarah opened the Pacific Garden Mission in Chicago, it seems with no tie to McAuley. | §1 M12 E6, E2, E4 |
| longDescription | It aimed to be 'a harbor for wrecked and ruined lives'. | §1 M12 E4 |
| longDescription | In 1906 mission leaders in New York formed a National Federation of Gospel Missions. | §1 M12 E3 |
| longDescription | On 17 September 1913 a wider body followed, the International Union of Gospel Missions, with about fifty missions. | §1 M12 E3, E6 |
| longDescription | The historian Norris Magnuson counts the rescue missions among the revival-based welfare movements of 1865 to 1920. | §1 M12 E7 |
| longDescription | He argues that their welfare work came from their commitment to evangelism and personal holiness. | §1 M12 E7 |
| longDescription | By 1972 the union counted some 350 members. | §1 M12 E6 |
| longDescription | In 2000 it became the Association of Gospel Rescue Missions. | §1 M12 E3 |
| legacy | The union took a new name in 2000, the Association of Gospel Rescue Missions. | §1 M12 E3 |
| legacy | In 2010 it was still the movement's network. | §1 M12 E3 (AGRM from 2000; renamed Citygate Network only in 2018) |
| voices | Jerry McAuley — whose mission on Water Street, New York, opened in 1872 | §1 M12 E2 |
| voices | Colonel George Clarke and Sarah Clarke — who opened the Pacific Garden Mission in Chicago in 1877 | §1 M12 E2, E4, E6 |
| voices | Sidney Whittemore — who led the International Union of Gospel Missions at its founding in 1913 | §1 M12 E3 |

## IX.55 The Christian Homeschool Movement

| field | sentence | evidence |
|---|---|---|
| statusDescription | Tiered Viable, secondary (Tier 2). | §2 M13 Tier; G-64(a) |
| statusDescription | Its window opens in March 1983, when the Home School Legal Defense Association was launched. | §2 M13 item 10; G-64(a) |
| statusDescription | The Christian day schools and a book of 1975 came before it and are told here as background. | §2 M13 items 1, 3, 5; G-64(a) disclosed prelude |
| statusDescription | It covers only the Christian root of homeschooling that Mitchell Stevens names, not the movement as a whole. | §2 M13 item 1; Section A |
| sourcing | Moderate: two studies from university presses, by Mitchell Stevens (2001) and Alan Peshkin (1986), and a history by Milton Gaither (2008). | §2 M13 B1; items 1, 2, 3 (Gaither's publisher is Palgrave Macmillan, not a university press) |
| sourcing | The carriers' own texts add to them. | §2 M13 items 5, 6, 10 |
| floorNote | No question. | SectionA_Research IX.55 (A1: clears directly on content); G-64(a) condition met |
| floorNote | In 2020 its legal defense association set out what it believed. | SectionA_Research IX.55 (HSLDA, 'What We Believe', byline 22 April 2020, verified) |
| floorNote | It named one God in three Persons. | SectionA_Research IX.55 ('one God, who exists eternally in three Persons (the Trinity)', verified) |
| floorNote | It said that God became a human being in Jesus Christ, the Son, who rose bodily from the dead. | SectionA_Research IX.55 ('God became a flesh-and-blood human ... Jesus Christ, the Son'; 'He then rose bodily from the dead', verified) |
| floorNote | The statement bound the association's leaders and staff, not its members. | SectionA_Research IX.55 (binds 'leaders, directors, and employees'; 'We do not require members of HSLDA to be Christian', verified) |
| relationsSummary | Alan Peshkin studied a fundamentalist Baptist school. | §2 M13 item 3 |
| relationsSummary | That ties this entry to Fundamentalism. | §2 M13 Overlap (repo: IX.33) |
| relationsSummary | Mitchell Stevens also traced a second root of homeschooling, a liberal one. | §2 M13 item 1 |
| relationsSummary | It was not Christian, so it stays outside this entry. | §2 M13 item 1; Overlap |
| why | Sociologist Mitchell Stevens found that homeschooling was an organized movement, not a scatter of private choices. | §2 M13 item 1 |
| why | He traced one of its two roots to the Christian day schools of the 1960s and 1970s. | §2 M13 item 1 |
| why | In 1983 a legal defense group for homeschool families followed. | §2 M13 items 6, 10 |
| teaser | In 1983 two lawyers, both fathers who taught their children at home, set up a legal defense group for homeschool families. | §2 M13 items 6, 10 |
| longDescription | Sociologist Mitchell Stevens traced one root of homeschooling to the Christian day-school movement of the 1960s and 1970s. | §2 M13 item 1 |
| longDescription | Alan Peshkin spent eighteen months in one such school, a Baptist school in Illinois, in the late 1970s. | §2 M13 item 3 |
| longDescription | He called it a 'total world'. | §2 M13 item 3 |
| longDescription | Raymond and Dorothy Moore's Better Late Than Early (1975) argued that formal lessons should wait until a child was older. | §2 M13 item 5 |
| longDescription | Around 1982 James Dobson interviewed Raymond Moore about the book on the air. | §2 M13 item 10 |
| longDescription | Some families who heard the broadcast began to teach their children at home. | §2 M13 item 10 |
| longDescription | In March 1983 two homeschooling fathers, the lawyers Michael Farris and J. Michael Smith, launched the Home School Legal Defense Association with their wives. | §2 M13 items 10, 6 |
| longDescription | At the time, homeschooling was legal in only a handful of states. | §2 M13 item 6 |
| longDescription | A reviewer of Stevens's study summed the movement up as 'a woman's enterprise, in which men are usually junior partners'. | §2 M13 item 9 |
| legacy | In 2001 Mitchell Stevens told the story of homeschooling as a social movement. | §2 M13 item 1 (the book's subtitle, 'the Homeschooling Movement'; the publisher's description; no quotation is attributed to Stevens) |
| voices | Raymond and Dorothy Moore — whose Better Late Than Early (1975) argued that formal lessons should wait until a child was older | §2 M13 item 5 |
| voices | Michael Farris and J. Michael Smith — homeschooling fathers and lawyers who launched the Home School Legal Defense Association in March 1983 | §2 M13 items 6, 10 |
| voices | Mitchell Stevens — the sociologist whose Kingdom of Children (2001) traced homeschooling's Christian root | §2 M13 item 1 |

## IX.56 The Liturgical Movement

| field | sentence | evidence |
|---|---|---|
| statusDescription | Tiered Viable, secondary (Tier 2). | §2 M11 liturgical Tier; G-68(a) |
| statusDescription | Its window closes in 1962, at the Second Vatican Council, where Fenwick and Spinks close the Catholic movement. | §2 M11 liturgical item 6 (chapter 'the Roman Catholic Liturgical Movement 1900-62'); G-68(a) |
| statusDescription | The parish after the Council has its own entry. | §2 M11 liturgical Overlap (repo: IX.23); G-68(a) |
| sourcing | Rich: its own journal from 1926 and its English handbooks of 1935 and 1937. | §2 M11 liturgical B1; items 3, 4 |
| sourcing | Two academic histories, by Keith Pecklers (1998) and by John Fenwick and Bryan Spinks (1995), tell its story. | §2 M11 liturgical B1; items 5, 6 |
| floorNote | No question. | §2 M11 liturgical Section A |
| floorNote | Its carriers were Benedictine houses of the Catholic Church and Anglican parishes. | §2 M11 liturgical items 1, 3, 4 |
| floorNote | Both churches held to the Nicene Creed. | §2 M11 liturgical Section A |
| relationsSummary | It ran through Benedictine abbeys, journals and parishes, not through the Vatican. | §2 M11 liturgical Overlap; items 3, 4 |
| relationsSummary | The entry on the Catholic Church before the Council names it once. | §2 M11 liturgical item 8 (repo: IX.47) |
| relationsSummary | The entry on the parish after the Council takes up what came of it. | §2 M11 liturgical Overlap (repo: IX.23) |
| why | Historians date the popular liturgical movement from an address at Malines, Belgium, in 1909. | §2 M11 liturgical item 1 |
| why | It reached America through Saint John's Abbey in Collegeville. | §2 M11 liturgical item 3 |
| why | There the journal Orate Fratres was founded in 1926. | §2 M11 liturgical item 3 |
| why | In England, Gabriel Hebert's books gave the Parish Communion movement its handbook. | §2 M11 liturgical item 4 |
| teaser | A movement to renew worship began with a talk in Malines in 1909. | §2 M11 liturgical item 1 |
| teaser | It spread to Catholic abbeys and Anglican parishes. | §2 M11 liturgical items 3, 4 |
| longDescription | In 1909 Dom Lambert Beauduin spoke at the National Congress of Catholic Action in Malines, Belgium. | §2 M11 liturgical item 1 |
| longDescription | Historians date the popular liturgical movement from that address. | §2 M11 liturgical item 1 |
| longDescription | In 1926 Virgil Michel of Saint John's Abbey in Minnesota founded the journal Orate Fratres, the movement's voice. | §2 M11 liturgical item 3 |
| longDescription | He also set up the Liturgical Press. | §2 M11 liturgical item 3 |
| longDescription | Keith Pecklers showed how closely its American leaders tied worship to social justice in the 1930s and 1940s. | §2 M11 liturgical item 5 |
| longDescription | In England, Gabriel Hebert published Liturgy and Society in 1935. | §2 M11 liturgical item 4 |
| longDescription | The Church Times later called it 'the Bible of the Parish Communion Movement'. | §2 M11 liturgical item 4 |
| longDescription | Hebert's collection The Parish Communion (1937) set out a practice that changed the pattern of Sunday-morning worship. | §2 M11 liturgical item 4 |
| legacy | John Fenwick and Bryan Spinks tell its story across many churches: Catholic, Anglican, Eastern and North American. | §2 M11 liturgical item 6 |
| legacy | They close the Catholic part in 1962. | §2 M11 liturgical item 6 |
| voices | Dom Lambert Beauduin — whose address at Malines in 1909 historians take as the movement's start | §2 M11 liturgical item 1 |
| voices | Virgil Michel — who founded the journal Orate Fratres at Saint John's Abbey in 1926 | §2 M11 liturgical item 3 |
| voices | Gabriel Hebert — whose Liturgy and Society (1935) was called 'the Bible of the Parish Communion Movement' | §2 M11 liturgical item 4 |

## IX.57 The Third Wave & the Vineyard

| field | sentence | evidence |
|---|---|---|
| statusDescription | Tiered Viable, secondary (Tier 2). | §3 Third Wave Tier; G-73(b) |
| statusDescription | Its window opens in 1982, when the Signs and Wonders course began at Fuller Seminary. | §3 Third Wave E1; G-73(b) |
| statusDescription | The entry on the charismatic renewal and the Jesus movement ends where the Vineyard began, in 1982. | §3 Third Wave Overlap (repo: IX.45 teaser, 'closing at the Vineyard's founding'; relationsSummary, 'the Vineyard association (1982, the start of the third wave)') |
| sourcing | Rich: Fuller Seminary's archive of the course and its founders' books. | §3 Third Wave B1; E1, E4 |
| sourcing | Fuller's own study of the course and the work of four scholars add to them. | §3 Third Wave B1; E5-E9 (Poloma, Percy, Miller, Bialecki: five works by four scholars) |
| floorNote | No question. | SectionA_Research IX.57 (A1: clears directly on content) |
| floorNote | The Vineyard churches' statement of faith named one God in three persons of one substance. | SectionA_Research IX.57 ('three persons of one substance', verified on Vineyard USA's own booklet and on the 1994-labelled copy) |
| floorNote | It called Christ fully God and fully human in one person, raised from the dead on the third day. | SectionA_Research IX.57 ('fully God and fully human in one person'; the 1994-labelled copy reads 'man'; 'raised from the dead on the third day', verified) |
| floorNote | Copies of it published by others date its adoption by the association's board to November 1994. | SectionA_Research IX.57 (bible.ca and religionfacts.com, verified as reproductions; the date [S] as to the publisher) |
| relationsSummary | It follows the charismatic renewal and the Jesus movement. | §3 Third Wave Overlap (repo: IX.45) |
| relationsSummary | That entry names the Vineyard of 1982 as the start of the third wave. | §3 Third Wave Overlap (repo: IX.45 relationsSummary) |
| relationsSummary | The Toronto Blessing of 1994 grew inside one of its churches. | §3 Toronto Blessing E2, E3; G-74(a) |
| why | In 1982 John Wimber began teaching 'Signs and Wonders' at Fuller Seminary. | §3 Third Wave E1 |
| why | C. Peter Wagner called the stream 'the Third Wave'. | §3 Third Wave E3 |
| why | Its people sought the gifts of the Spirit. | §3 Third Wave E3 |
| why | But they did not take on Pentecostal or charismatic theology or worship styles. | §3 Third Wave E3 |
| teaser | It began with a seminary course called 'Signs and Wonders'. | §3 Third Wave E1 |
| teaser | Its churches sought the gifts of the Spirit without becoming Pentecostal. | §3 Third Wave E3 |
| longDescription | In 1982 John Wimber and C. Peter Wagner began teaching MC510, 'Signs and Wonders', at Fuller Theological Seminary in Pasadena. | §3 Third Wave E1 |
| longDescription | The course ran until 1985 and drew controversy. | §3 Third Wave E1, E5 |
| longDescription | Fuller's faculty dropped it in early 1986 and published its own study, Ministry and the Miraculous, in 1987. | §3 Third Wave E5 |
| longDescription | Wagner called the stream 'the Third Wave'. | §3 Third Wave E3 |
| longDescription | Its people believed in the power and gifts of the Holy Spirit. | §3 Third Wave E3 |
| longDescription | Yet they did not adopt Pentecostal or charismatic theology or worship styles. | §3 Third Wave E3 |
| longDescription | Wimber set out his method in Power Evangelism in 1985. | §3 Third Wave E4 |
| longDescription | In 1994 a revival called the Toronto Blessing began at the Toronto Airport Vineyard. | §3 Toronto Blessing E2 (year and name, verified); named line, G-74(a) |
| longDescription | The Vineyard association cut its ties with that church in December 1995. | §3 Toronto Blessing E3 |
| longDescription | Margaret Poloma published a study of the revival in 1997. | §3 Toronto Blessing E4 |
| longDescription | Jon Bialecki later studied 'the Third Wave' by name, and the Vineyard as 'an American charismatic movement'. | §3 Third Wave E8, E9 |
| legacy | In 1997 Donald Miller studied the Vineyard beside two other new church networks. | §3 Third Wave E7 |
| legacy | Jon Bialecki's study of its churches followed in 2017. | §3 Third Wave E9 |
| voices | John Wimber — who taught the Signs and Wonders course at Fuller and wrote Power Evangelism (1985) | §3 Third Wave E1, E4 |
| voices | C. Peter Wagner — who taught the course with Wimber and coined the name 'Third Wave' | §3 Third Wave E1, E3 |
| voices | Ministry and the Miraculous (1987) — Fuller Seminary's own study of the course it had dropped | §3 Third Wave E5 |

## IX.58 Promise Keepers & the Christian Men's Movement

| field | sentence | evidence |
|---|---|---|
| statusDescription | Tiered Viable, secondary (Tier 2). | §3 Promise Keepers Tier; G-77(a) |
| statusDescription | Its window opens in 1990, when Promise Keepers began. | §3 Promise Keepers E2, E3; G-77(a) |
| statusDescription | The size of its 1997 rally in Washington rests on a crowd estimate. | §3 Promise Keepers E2, E3; Trace note (formation_confidence: Contested) |
| sourcing | Moderate. | §3 Promise Keepers B1 |
| sourcing | A study by John Bartkowski (2004) comes from a university press. | §3 Promise Keepers E5 |
| sourcing | An encyclopedia entry, the movement's own book of 1994 and news reports of the time add to it. | §3 Promise Keepers E3, E4, E1, E2 |
| floorNote | No question, on a reported text. | §3 Promise Keepers Section A |
| floorNote | In 1997 a newspaper reported its statement of faith. | §3 Promise Keepers E1 |
| floorNote | It named one God in three persons, the deity of Jesus, and salvation through his death. | §3 Promise Keepers E1 |
| relationsSummary | Its setting was evangelical, like that of the megachurches and of Lausanne-era evangelicals. | §3 Promise Keepers Overlap (repo: IX.30, IX.24) |
| relationsSummary | But its focus on men was its own. | §3 Promise Keepers Overlap (repo: IX.30, IX.24); E2, E5 |
| relationsSummary | James Mathisen set it apart from the wider men's movement. | §3 Promise Keepers E2; Overlap |
| why | In 1990 a college football coach and a friend started a ministry for men. | §3 Promise Keepers E2, E3 |
| why | Its first members called themselves Promise Keepers. | §3 Promise Keepers E2 |
| why | By 1996 its rallies had filled 22 stadiums with nearly 1.2 million men. | §3 Promise Keepers E2 |
| why | Each man made seven promises. | §3 Promise Keepers E4 |
| why | Among them, he would keep close friendships with other men, stay pure and keep his marriage strong. | §3 Promise Keepers E3, E4 |
| why | He would also reach across lines of race and church. | §3 Promise Keepers E3, E4 |
| teaser | In 1990 a football coach had an idea. | §3 Promise Keepers E2, E3 |
| teaser | It filled stadiums with men who made seven promises, and in 1997 it reached Washington. | §3 Promise Keepers E2, E3, E4 |
| longDescription | On 20 March 1990, Bill McCartney, the University of Colorado football coach, drove with a friend to Pueblo. | §3 Promise Keepers E2 (the drive of 20 March 1990; Pueblo is in E2's article, as Movements Review Round 1 M-12 read it) |
| longDescription | From that trip grew a group of about seventy men who called themselves Promise Keepers. | §3 Promise Keepers E2 |
| longDescription | In 1991, 4,200 men met at the university's basketball arena. | §3 Promise Keepers E2 (4,200 men in 1991; the arena is in E2's article, as Movements Review Round 1 M-12 read it) |
| longDescription | In 1996, 22 stadium rallies drew nearly 1.2 million men. | §3 Promise Keepers E2 |
| longDescription | Each man made seven promises, published in 1994 as Seven Promises of a Promise Keeper. | §3 Promise Keepers E4 |
| longDescription | They pledged purity, strong marriages, and friendship across racial and denominational barriers. | §3 Promise Keepers E3 |
| longDescription | On 4 October 1997 a crowd estimated at about a million men gathered in Washington, D.C., for Stand in the Gap. | §3 Promise Keepers E3 (crowd estimate; formation_confidence: Contested) |
| longDescription | In March 1998 the ministry began laying off 345 paid staff. | §3 Promise Keepers E2 |
| longDescription | Sociologist John Bartkowski later traced the rise and fall of this Christian men's movement. | §3 Promise Keepers E5 |
| legacy | In 2001 James Mathisen called it 'the decade's most unexpected and immediately successful movement within the American church'. | §3 Promise Keepers E2 |
| voices | Bill McCartney and Dave Wardell — who founded Promise Keepers in 1990 | §3 Promise Keepers E3 |
| voices | Seven Promises of a Promise Keeper (1994) — the book of the promises each man made | §3 Promise Keepers E4 |
| voices | James A. Mathisen — whose 2001 essay called it the decade's most unexpected and immediately successful movement within the American church | §3 Promise Keepers E2 |

## IX.24 Lausanne-Era Global Evangelicalism

| field | sentence | evidence |
|---|---|---|
| relationsSummary | At the 1974 congress, Ralph and Roberta Winter prepared a paper on the peoples that existing missions did not reach. | §1 frontier missions E12 (Christianity Today, 21 January 1983, verified); G-58(b) |
| relationsSummary | In 1997 the Southern Baptist International Mission Board took up an approach called the Church Planting Movement. | §1 M3 E2 (Massey 2012: IMB adoption in 1997); G-59(a) |
| relationsSummary | David Garrison set it out in a book in 2004. | §1 M3 E1 (Garrison 2004 book, verified); G-59(a) |
| relationsSummary | Evangelical relief agencies worked on the same ground, and some were older than the congress. | §1 M7 E4 (Shin 2022: World Vision and Tearfund as evangelical humanitarianism); G-61(a) reach-back disclosed |
| relationsSummary | Tearfund grew out of the Evangelical Alliance in 1968. | §1 M7 E3 (Freeman 2019, verified); G-61(a) |
| relationsSummary | Brian Stanley's history names this evangelical age after Billy Graham and John Stott. | §1 M4 E3 (Stanley, The Age of Billy Graham and John Stott, verified); G-34(a) |
| relationsSummary | Graham's evangelistic association was incorporated in 1950. | §1 M4 E1 (BGEA timeline: incorporated September 1950); G-34(a) |

## IX.33 Fundamentalism

| field | sentence | evidence |
|---|---|---|
| relationsSummary | The networks gave radio evangelists such as Paul Rader and Charles Fuller no free time, so they bought airtime instead. | §2 M8 item 5 (Hangen 2002, verified); G-65(a) |
| relationsSummary | In 1944 evangelical broadcasters formed the National Religious Broadcasters, at the invitation of the National Association of Evangelicals. | §2 M8 item 2 (Wheaton NRB records; NAE, verified); G-65(a) |
| relationsSummary | Billy Graham's Los Angeles campaign of 1949 ran for more than eight weeks instead of the three planned. | §1 M4 E1 (BGEA timeline, verified as BGEA states it: extended from three weeks to more than eight); G-34(a) |

## IX.45 Charismatic Renewal & the Jesus Movement

| field | sentence | evidence |
|---|---|---|
| relationsSummary | The Word of Faith movement grew in the same years. | §3 Word of Faith E3 (Coleman 2000: a Faith ministry within charismatic Christianity); G-75(a) |
| relationsSummary | Kenneth Hagin's Rhema Bible Training Center dates from 1974. | §3 Word of Faith E1 (Harrison, 'Word of Faith Movement', Contemporary American Religion, verified); G-75(a) |
| legacy | Chuck Smith of Calvary Chapel founded Maranatha! Music in 1971. | §3 contemporary worship E1 (Maranatha! Music 'About', verified); G-76(a) |
| legacy | Larry Eskridge's history of the Jesus People gives Jesus music a chapter. | §3 contemporary worship E3 (Eskridge 2013, verified); G-76(a) |

## IX.30 The Megachurch & Seeker Movement

| field | sentence | evidence |
|---|---|---|
| legacy | In 2021 Lester Ruth and Lim Swee Hong published a history of contemporary praise and worship. | §3 contemporary worship E4 (Ruth and Lim 2021, verified); G-76(a) |

## IX.28 The Emerging Church & Post-Evangelical Movement

| field | sentence | evidence |
|---|---|---|
| relationsSummary | The new monasticism began in the same years. | §2 new monasticism item 1; G-67(b) |
| relationsSummary | In 2004 more than sixty people in Durham, North Carolina, drafted its twelve marks. | §2 new monasticism item 1 (Houston Catholic Worker, 1 October 2004, verified); G-67(b) |

## IX.16 The Way International; Unification Church; La Luz del Mundo

| field | sentence | evidence |
|---|---|---|
| statusDescription | A composite entry covering three distinct bodies. | G-14(a) |
| statusDescription | Each is assessed on its own dated texts, not treated as one group. | release-21 text, kept |
| statusDescription | Its window starts in 1926, the founding of the earliest body it covers. | IX.16 longDescription (release 21): La Luz del Mundo founded 6 April 1926 |
| floorNote | Each of these three movements is assessed on its own published confession and claims of authority, not as one group. | release-21 text, kept; G-14(a) |
| floorNote | Each body's own teaching made its own claim for its founder's authority. | release-21 text, kept |
| floorNote | On their own texts up to 2010, none of the three affirmed the Trinity or Christ's divinity as the historic creeds meant them. | release-21 text, kept |
| relationsSummary | Three separately founded bodies share this entry because none is large or well studied enough to have its own. | release-21 text, kept; G-14(a) |
| relationsSummary | They did not share a confession, and each body's own texts carry its own finding. | release-21 text, kept |
| relationsSummary | La Luz del Mundo grew out of the Oneness Pentecostal movement. | release-21 text, kept ('descends from'), past tense |
| relationsSummary | Iglesia ni Cristo has its own entry. | G-14(a); IX.51 in release 21 |
| why | Three separately founded movements share this entry. | release-21 text, kept; G-14(a) |
| why | The Way International grew out of Victor Paul Wierwille's radio ministry in the 1940s. | release-21 text, kept |
| why | Sun Myung Moon founded the Unification Church in Seoul in 1954. | release-21 text, kept |
| why | La Luz del Mundo was founded in Guadalajara in 1926, and from 1964 a second apostle led it in succession from its founder. | release-21 text, kept |
| why | Each has its own scripture, founder claim and history, told here on its own terms. | release-21 text, kept |
| teaser | North America, Korea and Mexico, from 1926. | release-21 text, kept; G-14(a) |
| teaser | The Way International, the Unification Church and La Luz del Mundo share this entry, but not a confession. | release-21 text, kept |
| teaser | Each is assessed on its own published texts. | release-21 text, kept |
| longDescription | Three separately founded bodies share this entry, but not a confession. | release-21 text, kept; G-14(a) |
| longDescription | Each is described from its own published texts. | release-21 text, kept |
| longDescription | The Way International began in 1942 as Victor Paul Wierwille's Vesper Chimes radio ministry. | release-21 text, kept |
| longDescription | It took its later name in 1955. | release-21 text, kept |
| longDescription | His Power for Abundant Living appeared in 1971, and Jesus Christ Is Not God in 1975, a title that states its own position. | release-21 text, kept |
| longDescription | Sun Myung Moon founded the Unification Church in Seoul on 1 May 1954. | release-21 text, kept |
| longDescription | It was later known as the Family Federation for World Peace and Unification. | release-21 text, kept |
| longDescription | Moon's Divine Principle appeared in Korean in 1966. | release-21 text, kept |
| longDescription | Eusebio Joaquín González founded La Luz del Mundo in Guadalajara on 6 April 1926. | release-21 text, kept |
| longDescription | From 1964 a second apostle led it, in succession from him. | release-21 text, kept |
| legacy | All three were still active in 2010. | release-21 text, kept; G-14(a) |
| legacy | La Luz del Mundo had one change of leader, in 1964. | release-21 text, kept |
| legacy | The Way had two after its founder. | release-21 text, kept |
| legacy | The Unification Church was still led by its founder. | release-21 text, kept |
| legacy | Court records are part of these bodies' public record too. | release-21 text, kept |
| legacy | The Way's leadership changes ran alongside litigation, and in 1982 a federal jury convicted Sun Myung Moon of filing false tax returns. | release-21 text, kept |
| legacy | Those are matters of public record and part of any honest telling. | release-21 text, kept |

## IX.51 Iglesia ni Cristo

| field | sentence | evidence |
|---|---|---|
| longDescription | Iglesia ni Cristo, 'the Church of Christ', was registered with the government of the Philippines on 27 July 1914. | V1.0 IX.16 per-body note (registered 27 Jul 1914, verified); IX.16/IX.51 sources ('the 1914 government registration'); IX.51 informalName |
| longDescription | It was registered under Felix Y. Manalo, and its own history presented him as God's messenger for the last days. | IX.16 voices (release 21: 'under whom Iglesia ni Cristo was registered in July 1914'); V1.0 (the Messenger claim per the church's own history pages, own voice, verified) |
| longDescription | It honored Jesus as Lord and Savior but taught that he was not God. | IX.51 floorNote (release 21); V2.0 IX.16 Section A ('messenger claim, non-trinitarian') |
| longDescription | From February 1939 its magazine Pasugo, in Tagalog and English, set out its teaching. | V1.0 (Pasugo from Feb 1939, verified); IX.16 sources ('Pasugo/God's Message (Feb 1939-, Tagalog and English)') |
| longDescription | It passed through two changes of leader, in 1963 and 2009. | IX.51 statusDescription and legacy (release 21); V1.0 (successions 1963, 2009 [S], carried) |
| longDescription | By its own counts it was, by 2010, the largest church founded in the Philippines. | IX.16 legacy and IX.51 why (release 21); V2.0 confidence note (the church's own counts) |
| longDescription | No independent count is cited here, and independent scholarship on the church is thin. | IX.51 why and sourcing (release 21); IX.16 Barker source note |
