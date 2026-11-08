# Church Family Tree links, era 9, part 2 (P2-L9) — 2026-11-08

Launch prompt: `Build/Ministry/Features/Church-Family-Tree/Launch-Prompts/CFT_Phase2_Links_Era_Launch_2026-11-07.md`, with the major-links step (4b, Mark, 2026-11-08). Method unchanged from `Build/Ministry/Operations/Audits/2026-11-06_census-lineage-rigor/Drafting_Brief.md`; the era addendum is `../2026-11-08_links-era-9-part-1/Drafting_Brief_Era9.md`.

## Era 9 runs as two pull requests

Era 9 has 51 movements, split by lane, each part with its own rounds and its own three-round cap. Part 1 (`../2026-11-08_links-era-9-part-1/`, the Protestant and Evangelical lane and the Syriac East / Protestant bridge, 24 movements) merged first as data release 12. This is part 2: every other era-9 lane, 27 movements (Greek East, Caucasus, Africa, Latin West, the Greek East / Latin West bridge, the Syriac East, and the movements beyond the floor). Part 1 owns any relationship a part-1 text names; part 2 drafted a cross-part relationship only when part-2 text alone names it.

## Rounds

1. **Inventory** (Haiku): `Inventory.json`. 27 movements, 270 named relationships, 203 with no census match. The drafters read each movement's four fields themselves and corrected the matches.
2. **Draft** (Opus, seven groups of three or four movements, G to M): `Draft_GroupG.json` to `Draft_GroupM.json`, merged in `Drafting_Record.json`. Three links were drafted twice (the Russian church to the Alaskan mission, to Japanese Orthodoxy and to the Ruthenian Greek Catholics); the merge notes say which draft was kept and why. Two links the era-6 and era-7 branches had already drawn into this part were left to them.
3. **Review round 1** (separate Opus agent, full review): `Opus_Review_Round1.json`. Revise: 1 blocking, 8 substantial, 10 minor, no fabrication. The blocking finding: the Ecuador concordat's outcome said it "made" Catholicism the state religion, where its article 1 says the religion "shall continue" to be. The substantial findings: the Ecuador major call itself; the Philippine "broke with" (the breakaway church has no entry of its own); the Coptic "continued as" across about 550 years; the colonial-to-nineteenth-century Latin American "continued as" over-graded on one Mexican devotion; and four relationships the texts name with no link (Optina's continuation, Rome's 1830 confirmation of the Chaldean patriarch, the 1877 and 1879 missions to Uganda, Theophan's Russian Philokalia).
4. **Revision** (Opus): `Revision_Round1.json`. All 19 fixed, 6 of them differently from the proposed fix, with reasons. 5 links added, 17 changed, 1 removed (the Philippine "broke with"; never published). The Ecuador outcome now rests on article 3 (schools and religion books). The Coptic link stays, regraded to Dominant Modern Reconstruction, its note saying plainly that it spans five centuries on modern lists of patriarchs.
5. **Review round 2** (separate Opus agent, targeted recheck): `Opus_Review_Round2_TargetedRecheck.json`. Revise: 0 blocking, 1 substantial, 1 minor. The substantial finding: the Guadalupe sentence dated Leo XIII's order to 1895, which no cited source does (1895 is the coronation's year). The minor: "this tree" wording in the Coptic note. Both applied as the reviewer wrote them (`Revision_Round2.json`).
6. **Review round 3** (separate Opus agent, targeted recheck of the two sentences): `Opus_Review_Round3_TargetedRecheck.json`. Pass, 0 findings.

All three rounds of the cap were used. No finding is open.

## Counts

- Links touching a part-2 movement: 38. This pass added 31 and rewrote the note of 1 (`desert-monasticism--the-kollyvades-and-greek-renewal`); the era-6 links into the Optina elders and part 1's links into the Catholic Church, the Taiping and the Chaldeans stand as merged. No link retired; every published ID stands.
- Census links in all: 399 before this pass (after part 1, data release 12), 430 after. Data release 13 (2026-11-08).
- Grades of the links added: Documented 10, Dominant Modern Reconstruction 9, Widely Accepted 8, Inferential-Thin 4.
- Types of the links added: continued as 9, gave rise to 7, in contact with 7, influenced 4, argued against 2, broke with 2.
- Dispositions of the named relationships (drafting, 250): no-entry 95, link 69, kept-as-is 36, out-of-scope 28, qualify 22. Revision round 1 restated 9 of them (`Revision_Round1.json`, `dispositions`).
- Prose: 21 movement fields changed. Every changed paragraph, and every new or rewritten link note and outcome, scores Reading Ease 60 or more and FK grade 10 or less with `engine.m7.turn_readability.score_turn` (`Readability_Scores.json`, 56 scored, 0 failing).
- Quote check: `node tools/validate-census.mjs --base <main's census> --atlas cft-website/index.html --tree cft-website/tree`, 0 errors. Every primary quote appears verbatim at its stated lines.

## Major links

- Major by type (links this pass added): 18. Continued as 9, gave rise to 7, broke with 2.
- Major by outcome: **3**, all "rule-changed":

| Link | Outcome | Evidence |
|---|---|---|
| `russian-church-synodal-century--ruthenian-greek-catholic-polotsk-to-galicia` (argued against) | In 1839 the Russian Holy Synod took the Greek Catholic bishops, priests and people of Russia's western lands into its church. The emperor confirmed it. | A. N. Mouravieff; `mouravieff_history-of-the-church-of-russia_blackmore1842.txt` lines 20203-20210 |
| `catholic-church-long-nineteenth-century--nineteenth-century-latin-american-catholicism` (influenced) | In 1862 Pope Pius IX and Ecuador agreed that every school would follow Catholic teaching. Only bishops would choose the books used to teach religion. | Mirbt; `mirbt_quellen-zur-geschichte-des-papsttums-3e-aufl-deu-lat_1911.txt` lines 25590-25594 |
| `catholic-church-long-nineteenth-century--church-of-the-east-chaldean-consolidation` (in contact with) | Rome recognized Mutran Hanna as head of the Chaldeans on one condition: he must make none of his kin bishops. That ended passing the office down in one family. | George Percy Badger; `badger_nestorians-and-their-rituals-v1_1852.txt` lines 8648-8650 |

- Judged and found minor: 11. The Kollyvades and the desert monks (a compilation); the Russian church and the Old Believers (a hedged secondary report, and a veto from 1812); Optina and the Paris school (teaching taken up); the Chaldeans and the Church of England (a mission and a welcome); the three Bonn reunion conferences with the Old Catholics (shared theses that bound no church); the Chinese books and the Korean Catholics (books read); Rome and Japan's hidden Christians at Oura (a meeting and a return to communion); the Coptic and Ethiopian churches (a standing tie, no act in the sources); the Kollyvades and the Russian church (a translation taken up). Each reason is on the link's `major` block.

## Two-way check

### Prose to links

Every relationship named in a part-2 movement's `relationsSummary`, `longDescription`, `why` or `legacy` has a link, or its sentence was qualified or removed, or it names no census movement, or another session owns it, or it is not a relationship claim (per-relationship record: `Drafting_Record.json` and `Revision_Round1.json`, `dispositions`). Round 1 found four gaps; revision closed all four with links. Each era-9 `continuesAs` in this part now has a graded "continued as" link (Open-Gaps, "'Continues as' with no graded link", 2026-11-08).

Texts that were wrong, not just unsupported, each fixed in about a sentence:

- Orthodoxy after 1821 (description, why): the revolt did not open with the patriarch's hanging; Walsh, at Constantinople in 1821, hears of the rising first, and the hanging came on Easter Sunday.
- Ethiopia (description): Tewodros did not crown himself; Yohannes was not his direct successor.
- The Optina elders (description, why, legacy): the Optina books were Slavonic translations for Russian readers, and Paisius's Slavonic Philokalia had been printed in 1793, so not "into Russian" and not the first time.
- American Unitarians and Universalists (summary, description): Channing's 1819 sermon did not name the movement (the label was in use by 1815), and the Universalists did not share a refusal of creeds (the Winchester Profession).
- The Taiping (summary): Hong Xiuquan and Feng Yunshan, not Hong alone, founded the God Worshippers.
- The Chaldeans (why): the mountain village was the patriarch's seat, not the size of the church.

Other sentences qualified or removed (reasons in the drafting and revision records): the Korean Catholics as a "precursor" of the Protestant missions; the Old Catholic Bonn agreements as "a model for many since"; the Latin American conferences "grew from that precedent"; the Coptic revival as "parent" of everything the modern Coptic Church is known for; the Jehovah's Witnesses' break "without reference to inherited teaching" (now the circle's aim); the Malagasy "standard proof". Two fields with internal or telegraphic wording (the Haitian and Taiping summaries) were rewritten in plain sentences.

### Links to prose

Every link added or changed is named in the text of one of its movements (`named_in_text` on each link).

## Merge with other sessions

- Era 6 (data release 11) drew two links into the Optina elders; they stand, and this pass drew none on those pairs. Era 7's branch draws `kirishitan-japan` to the Meiji Japanese church and `church-of-the-east-schism-of-1552` to the Chaldeans; those pairs were left to era 7. Era-8-owned relationships (their own text names them) were left out (28 out-of-scope dispositions in all, including part 1's).
- Era 10 is deferred (Decision-Log, "The link work covers eras 1 to 9", 2026-11-08), but its movements stay on the map. The links era-9 text names into era 10 stand, among them the four "continued as" links that close this part's `continuesAs` fields.

## Open items

Logged in `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` (2026-11-08):

- The Philippine Independent Church has no entry of its own; it sits inside the Philippine Catholic entry. Whether it needs one is a portfolio question for Mark.
- Map gaps: no Coptic movement between about 1300 and 1854 (the link now spans it on modern lists), and no Ethiopian movement between 1650 and 1855 (not bridged).
- Optina's `continuesAs` points a monastic renewal to the whole Russian Church under Soviet rule, while the synodal Russian church has no `continuesAs` of its own. A layout question.
- The Unitarian-Universalist floor note calls the Universalists "arguably floor-clean"; their own 1903 centennial volume calls them Unitarian in their doctrine of God. A floor question for Mark; the status line also prints an internal atlas code.
- Well-known facts with no vendored source, era 9 part 2: added to the open method question.
- Page recordings now read old descriptions on 6 part-2 pages. A paid voice run, for Mark.
- Text owners' items: the Alaskan "Tlingit alphabets"; Oneida's 1880 or 1881 dissolution; sentence fragments in the Catholic, Old Catholic, Oneida, Christadelphian and Unitarian-Universalist texts; the placeholder "-" relations summaries of four beyond-the-floor entries.
- Possible links that no text names, not drafted: the Urmia Assyrians' 1896 submission to the Russian church; John Thomas and the Stone-Campbell movement; Russell and the Adventists; Eddy and Quimby.

## Wanted texts

63 entries in `Drafting_Record.json`, `wants`, by group. The most useful: the Russian Synod's acts of 1839 in their own edition; the Vatican I constitutions and the Old Catholic Utrecht Declaration of 1889 in a public-domain edition; the Haitian concordat of 1860; Cyril IV's own reforms in an Arabic or translated edition; the Uganda mission journals (CMS and White Fathers); Theophan's Russian Philokalia; the Meiji-era records of Nikolai's mission.
