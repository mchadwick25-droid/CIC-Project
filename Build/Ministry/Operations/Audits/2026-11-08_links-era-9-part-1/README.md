# Church Family Tree links, era 9, part 1 (P2-L9) — 2026-11-08

Launch prompt: `Build/Ministry/Features/Church-Family-Tree/Launch-Prompts/CFT_Phase2_Links_Era_Launch_2026-11-07.md`, with the major-links step (4b, Mark, 2026-11-08). Method unchanged from `Build/Ministry/Operations/Audits/2026-11-06_census-lineage-rigor/Drafting_Brief.md`; this era's addendum is `Drafting_Brief_Era9.md` in this folder.

## Era 9 runs as two pull requests

Era 9 has 51 movements. Per the launch prompt it is split by lane, and each part has its own review rounds and its own three-round cap:

- **Part 1 (this folder):** the Protestant and Evangelical lane, plus the Syriac East / Protestant bridge. 24 movements.
- **Part 2:** every other era-9 lane, 27 movements, in `../2026-11-08_links-era-9-part-2/`, its own pull request after this one.

Ownership between the parts: part 1 owns any relationship a part-1 text names. That is why this part carries two links into part-2 movements (the Stone-Campbell debate with the Catholic Church; the mission tracts read by the Taiping founder).

## Rounds

1. **Inventory** (Haiku): `Inventory.json`. 24 movements, 377 named relationships, 290 with no census match. The drafters read each movement's four fields themselves and corrected the matches.
2. **Draft** (Opus, six groups of three to five movements): `Draft_GroupA.json` to `Draft_GroupF.json`, merged in `Drafting_Record.json`. One link was drafted twice (the Kentucky revival and the Stone-Campbell movement); the merge note says which draft was kept and why. Each drafter ran the quote and reading checks on its own file.
3. **Review round 1** (separate Opus agent, full review): `Opus_Review_Round1.json`. Revise: 0 blocking, 4 substantial, 17 minor, no fabrication; every quote matched its file. The substantial findings: the Mar Thoma note dated Whitehouse's account of the Antiochene bishop to the 1860s (his text says 1853); the Baptist note said the old confession stayed in use, where its own source says the English confessions fell out of use; the Brethren note credited Sandeen with a detail the drafter gave from memory; the Second Great Awakening prose had the whole Stone-Campbell movement grow "straight out of" the revival, where the evidence covers Stone's side only.
4. **Revision** (Opus): `Revision_Round1.json`. All 21 findings fixed, 8 of them differently from the proposed fix, with reasons. 19 links rewritten, 7 prose changes (six supersede drafting changes, one new). No published link's ID, ends or type changed.
5. **Review round 2** (separate Opus agent, targeted recheck): `Opus_Review_Round2_TargetedRecheck.json`. Pass: 0 blocking, 0 substantial, 1 minor (the revised links were labeled "revise" in the audit file, though unpublished). Relabeled "new" in `Revision_Round1.json` as written; the census is unaffected.

Two of the three rounds of the cap were used. No finding is open.

After review, the spelling check flagged one note: Carey's book title "Enquiry". The title is now set in quotes so it keeps the edition's spelling (Decision-Log 77); no words changed (`Spelling_Fix.json`).

## Counts

- Links touching a part-1 movement: 40. This pass added 34 and rewrote the notes of 3 (Holiness to Azusa Street; Stone-Campbell to the Churches of Christ and to the Disciples, for reading level). 3 were already on main and unchanged (from the era 8 movements). No link retired; every published ID stands.
- Census links in all: 364 before this pass (after era 6, merged first as data release 11), 398 after. Data release 12 (2026-11-08). Era 6's links touch no part-1 movement, and none of this pass's links repeats one of them.
- Grades of the links added: Dominant Modern Reconstruction 21, Documented 6, Widely Accepted 5, Inferential-Thin 2. Most of this lane's own texts (the founders' sermons, minutes and confessions) are not vendored; see wanted texts.
- Types of the links added: influenced 15, gave rise to 9, continued as 5, broke with 3, argued against 2.
- Dispositions of the named relationships (drafting, 351): no-entry 135, kept-as-is 94, link 76, qualify 30, out-of-scope 9, remove 7. "no-entry" means the other party has no census movement; its claim was still checked, and qualified where no vendored or repo-cited source supports it.
- Prose: 28 movement fields changed. Every changed paragraph, and every new or rewritten link note, scores Reading Ease 60 or more and FK grade 10 or less with `engine.m7.turn_readability.score_turn` (`Readability_Scores.json`, 65 scored, 0 failing).
- Quote check: `node tools/validate-census.mjs --base <main's census> --atlas cft-website/index.html --tree cft-website/tree`, 0 errors. Every primary quote appears verbatim at its stated lines. Several keep the edition's OCR errors exactly (McNemar's "fiinccre"); each is in the link's drafter flags.

## Major links

- Major by type (links touching part 1, after this pass): 20. Gave rise to 12, continued as 5, broke with 3.
- Major by outcome: **0**. No `outcome` field was added.
- Judged and found minor (17 "influenced" or "argued against" links; reasons in `Drafting_Record.json` and `Revision_Round1.json`, field `major`):

| Link | Why it is minor |
|---|---|
| `the-second-great-awakening-and-camp-meeting-worl--the-holiness-movement` | A practice taken up; no institutional act. |
| `the-black-church-in-america--azusa-street-and-early-pentecostalism` | Worship carried into a later movement. |
| `the-stone-campbell-restoration-movement--catholic-church-long-nineteenth-century` | A public debate (1837); no council, split or changed rule. |
| `restoration-georgian-church-of-england--the-oxford-movement-and-anglo-catholic-revival` | A tradition taken up by a later party. |
| `the-holiness-movement--the-salvation-army` | Teaching taken up. |
| `plymouth-brethren-and-dispensational-formation--the-sunday-school-and-bible-institute-movement` | Teaching taken up by schools. |
| `plymouth-brethren-and-dispensational-formation--dispensational-prophecy-culture` | A reading scheme taken up in print. |
| `the-moravian-church-at-herrnhut--the-missionary-movement-s-native-churches-seramp` | A writer taking up another body's example. |
| `the-methodist-revival--the-missionary-movement-s-native-churches-seramp` | A writer citing another body's work. |
| `the-missionary-movement-s-native-churches-seramp--taiping-heavenly-kingdom` | A tract read by another movement's founder. |
| `the-missionary-movement-s-native-churches-seramp--african-initiated-churches-harrist-aladura-zioni` | Influence only; no institutional act shown. |
| `german-pietism-spener-francke-halle--the-haugean-awakening` | Influence of teaching only. |
| `german-pietism-spener-francke-halle--laestadianism-and-the-nordic-revivals` | Influence only. |
| `german-pietism-spener-francke-halle--the-reveil-and-inner-mission-awakening` | Influence only. |
| `the-moravian-church-at-herrnhut--the-reveil-and-inner-mission-awakening` | Influence only. |
| `lutheran-wittenberg-and-its-congregations--confessional-lutheran-revival-emigrations` | Confessions taken up as a standard: reception. |
| `russian-church-synodal-century--russian-evangelicals-stundists--2` | Polemical books and missions; the 1894 decree against the Stundists is not vendored, so no source on the link shows the act. |

The round 1 reviewer checked all 17 calls and agreed with each.

## Two-way check

### Prose to links

Every relationship named in a part-1 movement's `relationsSummary`, `longDescription`, `why` or `legacy` has a link, or its sentence was qualified or removed, or it names no census movement, or another session owns it, or it is not a relationship claim (per-relationship record: `Drafting_Record.json`, `dispositions`). The round 1 reviewer found no gap.

Texts that were wrong, not just unsupported, each fixed in about a sentence:

- Confessional Lutherans (summary, description, why): Prussian persecution was given as the cause of the 1838 Saxon emigration and the Missouri Synod. The Saxon company left the Kingdom of Saxony, outside the Prussian Union. The false cause is removed.
- Russian evangelicals (summary, description): the two strands were said to join as the Russian Baptist Union in 1884. The movement's own story has the police break up the 1884 congress, and the strands stayed apart until 1944.
- Salvation Army (why): women "commissioned as officers" in 1859, when there was no Army and no officers until 1878.
- Nineteenth-century Baptists (why): two dating errors (Spurgeon died in 1892).
- Mar Thoma (summary): "Malankara Orthodox (Jacobite)" names a division that came only in 1912.
- Student Volunteer Movement (summary, legacy): it did not itself become the International Missionary Council, and that council merged into the World Council of Churches in 1961, as the ecumenical entry's own text says, not at its founding in 1948.

The main sentences qualified or removed (full list with reasons in `Drafting_Record.json`, `prose_changes`, and `Revision_Round1.json`):

| Movement | Field | Change |
|---|---|---|
| the-second-great-awakening-and-camp-meeting-worl | relationsSummary, why, legacy | "Edwardsean lines" removed (no vendored source); the Stone-Campbell descent limited to Stone's side; Holiness descent qualified to its Methodist origin; the Chautauqua claim removed. |
| nineteenth-century-baptists | relationsSummary, why, legacy | "Divided British Baptists" made exact; the Down-Grade as a template for later fundamentalist battles removed. |
| restorationist-apocalyptic-ferment-and-adventism | relationsSummary | "Child of the Awakening's ferment" qualified; the link is Inferential-Thin, resting on timing. |
| the-salvation-army | relationsSummary | "Child of Holiness" made exact: the Booths took up Holiness teaching; their people came from Methodism. |
| the-oxford-movement-and-anglo-catholic-revival | legacy | The claim on twentieth-century liturgical reform removed. |
| the-missionary-movement-s-native-churches-seramp | relationsSummary, legacy | "Catholic mission lines" removed; Carey's ranking of the Moravians and Methodists made exact; map-layout wording removed. |
| indonesian-christianity | legacy | Map-layout wording removed; a fragment repaired. |
| the-haugean-awakening | relationsSummary, longDescription | "Child of Pietism" stated as the modern biographies' reading; a fragment repaired. |
| the-reveil-and-inner-mission-awakening | relationsSummary, longDescription, legacy | "Child of" stated as the histories' reading; the 1834 Dutch secession no longer told as the awakening's own outcome. |
| laestadianism-and-the-nordic-revivals | relationsSummary, legacy | "Part of Pietism's long line" stated as a common classification; internal wording removed. |

### Links to prose

Every link added or changed is named in the text of one of its movements (`named_in_text` on each link). None stands alone.

## Merge with other sessions

- Eras 6, 7 and 8 run at the same time. Relationships their own movements' texts name were left to them (9 dispositions "out-of-scope"). This pass drew two era-8-to-era-9 links that only the era-9 text names: `the-methodist-revival--nineteenth-century-methodism` and `the-baptists--nineteenth-century-baptists` (both "continued as"). Era 8's branch had not applied any link when this pass applied.
- Era 7's branch carries `st-thomas-christians-under-portuguese-pressure-d--northeast-india-revivals-and-the-mar-thoma-refor` ("continued as"). Its era-7 text says the Kerala and Northeast India churches descend from the St Thomas Christians. The northeast hill churches came from Welsh and American missions; only the Mar Thoma half descends. Flagged for era 7's owner, not touched (Open-Gaps, "Era 7's St Thomas entry and the Northeast India churches", 2026-11-08).
- The link work now covers eras 1 to 9, and era 10 is deferred (Decision-Log, "The link work covers eras 1 to 9", 2026-11-08). Era 10's movements stay on the map, so the links era-9 text names to them stand: 13 links, 10 new and 3 already on main. They run to Azusa Street (two), the Churches of Christ, the Disciples, the Seventh-day Adventists, dispensational prophecy culture, the Chinese church, the African initiated churches, the ecumenical movement, independent Indonesia, twentieth-century Northeast India and Mar Thoma, the Malankara churches, and the Communist-era persecuted churches.

## Open items

Logged in `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` (2026-11-08):

- Well-known facts with no vendored source, era 9 part 1: added to the open method question.
- Page recordings now read old descriptions on 4 part-1 pages. A paid voice run, for Mark.
- Era 7's St Thomas entry and the Northeast India churches (above).
- Text owners' items: the Chinese church's "owed nothing to the foreign missions" (era 10); the Student Volunteer Movement's `continuesAs` pointer to the ecumenical entry; the Sunday-school "graded" lessons of the 1870s (the 1872 series was uniform); the place of the 1884 Russian Baptist meeting; the Victorian Church of England entry has no source list; the era-8 Baptist legacy's claim that Carey "opened the era" of Protestant missions, which Carey's own words contradict; the era-10 dispensational entry's "grew out of" Brethren teaching.
- Two possible links that no text names (Kuyper's edition of Voetius; Conybeare tracing Stundism to Pietism), not drafted.

## Wanted texts

69 entries in `Drafting_Record.json`, `wants`, by group. The most useful: the 1784 Methodist Discipline and Asbury's journal; Allen's Life, Experience and Gospel Labors (for the African Methodist break, now resting on Allen's side only); Campbell's Declaration and Address (1809); the minutes of the Millerite conferences; Newman's Apologia and the Tracts for the Times; Booth's In Darkest England; Darby's Collected Writings; the Edinburgh 1910 reports; the 1847 and 1876 Malankara documents in full; Hauge's and Laestadius's own writings; the 1834 Act of Secession; the 1894 decree on the Stundists.
