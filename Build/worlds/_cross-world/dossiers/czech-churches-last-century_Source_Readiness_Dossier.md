# Source Readiness Dossier — The Czech Churches' Last Century (Utraquists and Unitas)

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and why it exists.

**Atlas ID:** VI.24
**Corpus-map slug:** `czech-churches-last-century`
**Time window:** 1517 to c. 1627
**Region(s):** Bohemia, Moravia
**Dossier author / date:** source-research thread, one-world agent for VI.24, 2026-10-16 (resumed 2026-10-23 after a usage stop; no earlier dossier existed)
**Corpus-map / `cic/texts/` state as of:** 2026-10-23. The corpus-map bucket `cic/corpus-map/czech-churches-last-century.yaml` holds one merged file (Comenius, 1702). Nine files were vendored this session and sit in `cic/corpus-map/_staging/` until the lead merges them. `python3 cic/engine/corpus_map_merge.py --check` passes with them.

The census gives this world a floor note of "No question" and a status of Pre-Survey Candidate. It names four kinds of source: the Bohemian Confession of 1575, the Kralice Bible (1579 to 1593), the Unity's discipline records and Comenius's writings from exile.

## 1. Already assigned

**Merged (one file):**

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Historia Fratrum Bohemorum, eorum ordo et disciplina ecclesiastica (Halle, 1702; contains the Ratio Disciplinae, a Historiola and the Panegersia) | comenius | context | provisional | ~719K chars; second witness, long s read as f, word-form coverage 0.42 | `comenius_historia-fratrum-bohemorum-lat_1702.txt` |

**Vendored and staged this session (nine files, ~13.0M chars):**

| work | author | role here | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Collectio confessionum in ecclesiis reformatis publicatarum (Niemeyer, Leipzig 1840). Holds the Bohemian confession of 1535 (Additamentum 2), the Bohemian confession of 1575 (Additamentum 3, Latin of Frankfurt 1619) and the Consensus of Sendomir. Also staged provisionally to six sibling worlds (Lutheran Wittenberg, Reformed Cities, Huguenots, Dutch, Scottish, English), on headings only. | niemeyer | tradition (1535, 1575); context (Sendomir) | assigned; provisional | ~2.57M chars; Latin OCR noisy, second witness | `niemeyer_collectio-confessionum-lat_niemeyer1840.txt` |
| Dekrety Jednoty bratrské (Gindely, Prague 1865) | unity-of-the-brethren | tradition (also Hussite world, provisional) | assigned | ~901K chars; clean Czech | `unity-of-the-brethren_dekrety-jednoty-bratrske-ces_gindely1865.txt` |
| Obraz Jednoty českobratrské: Lasicki, Book VIII on the Unity's customs and orders, published by Comenius 1649 (Czech edition, Prague 1869) | lasicki | tradition (also Hussite world context, Moravian Church antecedent) | assigned | ~524K chars; clean Czech | `lasicki_obraz-jednoty-ceskobratrske-ces_1869.txt` |
| Historie o těžkých protivenstvích církve české, 894 to 1632 (Prague 1890) | unity-of-the-brethren | tradition (also Hussite context, Moravian antecedent) | assigned | ~627K chars; clean Czech | `unity-of-the-brethren_historie-tezkych-protivenstvi-cirkve-ceske-ces_1890.txt` |
| Pavel Skála ze Zhoře, Historie česká, vol. III, 1619 to March 1620 (Prague 1867) | skala | context | assigned | ~1.50M chars; clean Czech | `skala_historie-ceska-1619-1620-ces_tieftrunk1867.txt` |
| Vilém Slavata, Paměti, vol. I, 1608-09 and 1618-19 (Prague 1866) | slavata | context (also Tridentine, provisional) | assigned | ~1.29M chars; readable Czech | `slavata_pameti-1608-1619-dil1-ces_jirecek1866.txt` |
| The Labyrinth of the World (Comenius; Lutzow, London 1901), English | comenius | tradition (also Moravian antecedent, provisional) | assigned | ~449K chars; clean | `comenius_labyrinth-of-the-world_lutzow1901.txt` |
| Labirynt swěta a rág srdce (Czech, 1809 printing) | comenius | tradition | assigned, second witness | ~285K chars; blackletter OCR garbled (5,865 long s converted) | `comenius_labyrint-sveta-a-raj-srdce-ces_1809.txt` |
| Biblí svatá, text of the Kralice edition of 1613 (Prague 1887) | kralice-bible | tradition | assigned | ~4.87M chars; readable Czech, marginal-reference noise | `kralice-bible_biblj-svata-kralicka-ces_bfbs1887.txt` |

**What the new files change.** Before this session the world held one Latin second witness of a later Unity history. It now holds the Unity's own discipline in Czech (Gindely's Dekrety; Lasicki Book VIII, which is the 1649 text Comenius published), the Czech exiles' own history of the suppression, Comenius's Labyrinth in both languages, the Kralice Bible text, and both Bohemian confessions in Latin. It also holds a Protestant eyewitness (Skála) and a Catholic opposing witness (Slavata) of the revolt years.

**Witness grades.** Quotable once checked against the page image: Dekrety, Obraz Jednoty, Historie o těžkých protivenstvích, Skála, Slavata, Lützow's Labyrinth, the Kralice text. Second witness: Niemeyer (Latin OCR has systematic letter misreads, for example "Bohoemica"), the 1809 Czech Labyrinth (blackletter), and the 1702 Comenius.

**Honest limits on the Czech and Utraquist side.**

- The Confession of 1575 is in the corpus only as a Latin translation (Frankfurt 1619, in Niemeyer). The Czech text is not vendored.
- The Kralice file is the 1613 text as printed in 1887. It is not the 1579 to 1593 first edition.
- No text from the Utraquist church's own consistory is vendored. The Utraquists speak through the joint confession of 1575 and through Skála and Slavata. This is a real thinness, since the world's title names both bodies.
- Authorship of `historie-tezkych-protivenstvi` rests on the host catalogue (Comenius, with Adam Hartmann named in the text at about file line 7529). The file prefix is therefore the Unity, not Comenius.
- The 1535 confession was read only at its headings and the editor's note that it went to Wittenberg and was approved by Luther and Melanchthon. The relevant passages of each row marked provisional were placed on headings and line hits, not read in full.

## 2. Cross-link opportunities

Checked 2026-10-16 and 2026-10-23: header lines and bodies of the vendored corpus searched for "Bohemia", "Bohemian", "Utraquist", "Comenius", "Majestät", "White Mountain", "Žerotín", "Gindely" and "Slavata". Files with real hits were opened at the hit. Rows for five of them are in `crosslink_fragment.yaml` for the lead to add to the existing staging files.

- **Seifferth, Church Constitution of the Bohemian and Moravian Brethren (1866).** `unity-of-the-brethren_church-constitution_seifferth1866.txt`. Latin and English. The Ratio Disciplinae of 1632/33 is the Unity's own constitution at the end of this window. Its Introduction (file line 184 on) tells the Letters Patent of 11 July 1609 (line 447) and the Lissa synod of 1632 (line 856). Currently in the Hussite world as context. Tier: same time-place. Proposed here: tradition, assigned.
- **Lützow, Bohemia: An Historical Sketch (1920).** Chapter VII (1526 to 1620) from file line 11041, with the signing of the Letter of Majesty on 9 July 1609 at line 12626; Chapter VIII (1620 onward) from line 14890. Currently Hussite context. Tier: same time-place. Proposed: context, assigned.
- **Luther's 1520 writings.** `luther_works-v2-selected_jacobs-spaeth1916.txt` lines 4286 to 4426 (Address to the Christian Nobility on the Bohemians and a union with them); `luther_first-principles-reformation_wace-buchheim1885.txt` lines 6940 to 7100 and 10196 to 10481 (the Bohemians and communion in both kinds). Lutheran Wittenberg bucket. Tier: same time-different region. Proposed: context, provisional.
- **Hutterite Geschicht-Buch (Wolkan 1923, clean scan).** `hutterite-brethren_geschicht-buch-deu_wolkan1923.txt`. The Chronicle's contents list (lines 1576 to 1578 and 1718) records Cardinal Dietrichstein's mandate in the emperor's name that the Hutterites leave Moravia within four weeks (1622). Anabaptist bucket. Tier: same time-place (Moravia). Proposed: context, provisional. The pages themselves were not read.
- **Hussite world files that continue into this window.** The Latin Confession to King Vladislav in `gratius_fasciculus-rerum-expetendarum-v1-lat_brown1690.txt` (1508 or 1504) and Chelčický's `Síť víry` are antecedent to the Unity of this window. Both are Hussite-bucket texts and fall before 1517. Tier: out-of-window (antecedent). No row proposed; the Hussite staging already carries them.
- **Comenius's 1702 Historia (merged).** Already in this world's bucket as context, provisional. Its Ratio Disciplinae is the same work as the Seifferth Latin. The 1702 file's printed parts are the Historiola (file line 1269), Ratio Disciplinae (1241, 9932), Panegersia (5219) and "Lectori amico" (4120). A READER trailer for it is in `registry_append_fragment.yaml`.
- **Jesuit sources.** `polanco_chronicon-v1-lat_1894.txt` (line 13288) and `lainez_epistolae-et-acta-v8-lat_1917.txt` (index entry "Utraquistae, v. Calixtini") name the Utraquists. Society of Jesus bucket. Tier: same time-place. Not proposed as rows; the hits are single and the passages were not read.
- **The Moravian Church at Herrnhut (VIII).** No Herrnhut text is vendored. The census says a remnant of the Unity became the seed of the Moravian Church; the new Unity files are staged to it as antecedent, provisional.

## 3. Verified acquisition leads

Every row below was checked on archive.org by metadata fetch and the djvu text sampled at five points (10, 30, 50, 70 and 90 percent of the file). Date checked: 2026-10-16 (Gindely's Brethren history, Bost and the others in this table); items vendored this session are in §1.

| title | author | translator/ed. | year | url | rights basis | verified by |
|---|---|---|---|---|---|---|
| Akty Jednoty bratrské, vol. I | Jaroslav Bidlo (ed.) | none (Czech) | 1915 (Brno) | archive.org `aktyjednotybratr01bidluoft` | pd-us-by-date; host NOT_IN_COPYRIGHT | title page read; five-point sample clean Czech. Not vendored: the passages sampled are 15th-century, so it serves the Hussite world first. |
| Akty Jednoty bratrské, vol. II | Jaroslav Bidlo (ed.) | none (Czech) | 1923 (Brno) | archive.org `aktyjednotybratr02bidl` | pd-us-by-date (1923 imprint; item has no rights field) | title page read; five-point sample clean Czech. Not vendored: 15th-century treatises. |
| Geschichte der Gegenreformation in Böhmen | Anton Gindely, ed. Theodor Tupetz | none (German) | 1894 | archive.org `geschichtedergeg00ginduoft` | pd-us-by-date; host NOT_IN_COPYRIGHT | title page read; five-point sample clean German. Not vendored: scholarship on the 1620s, and the corpus is near its size trigger. |
| Geschichte der Böhmischen Brüder (vol. II) | Anton Gindely | none (German, with Latin and Czech documents) | the OCR reads "Prag 1858"; the host record gives a 1968 Osnabrück reprint | archive.org `geschichtederbh00gindgoog` | pd-us-by-date if the scanned book is the 1858 Prague print; host says NOT_IN_COPYRIGHT but dates it 1968, so confirm the imprint on the page image | Fraktur body garbled at the sampled points, Latin documents readable. Not vendored: second witness only. |
| Confessio Bohemica Evangelica (German of 1621) | Bohemian Estates | none (German) | 1621 | archive.org `bub_gb_uVxVAAAAcAAJ` | pd-us-by-date; no rights field on the item | Fraktur unreadable at all five points. Not vendored. A German witness of the 1575 Confession that a better scan could replace. |
| History of the Bohemian and Moravian Brethren | Ami Bost | none (English) | 1834 | archive.org `historyofbohemia00bost` | pd-us-by-date; host: Library of Congress is unaware of any copyright restrictions | metadata only; text not opened. English secondary history. |
| Czech Bible of Kralice, 1613 New Testament | Jan Blahoslav and others | none (Czech) | the item's title page reads "Brno 2009" | archive.org `BibleKralickNovZkon` | not cleared: a 2009 reprint with no rights statement | Not vendored; see §4. |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| The Czech text of the Bohemian Confession of 1575 | The census names it first | No Czech printing found on archive.org by title searches ("konfesse", "vyznání", "confessio bohemica"). Only the Latin of 1619 (Niemeyer, vendored) and the German of 1621 (garbled, §3) turned up. A later pass with other search terms could still find it. |
| English translation of the Confession of 1575 or 1535 | The brief asks for English beside every non-English text | None found. The 1535 confession is in Latin only in the corpus. Schaff's Creeds volume 3 was not found to carry it; not opened. Recorded as a gap: no public-domain English located. |
| Kralice Bible, first edition (1579 to 1593) | The census names it as the primary source | No scan of the 1579 to 1593 printing was found by title search. The 1887 Prague printing of the 1613 text was vendored. The `BibleKralickNovZkon` item is a 2009 Brno reprint with no rights statement, so it is not vendorable. Search for "Kralice", "kralická" and "Kraliçe" returned the Kralice items listed above and unrelated results. |
| English translation of the Kralice Bible | Checking for a public-domain counterpart | Not applicable: an English Bible would not translate the Czech. Not pursued. |
| Letter of Majesty of 1609, separate text | The census names it in the relations summary | No separate printing found by title search ("Majestätsbrief", "Majestát"). The event is in Seifferth's Introduction (line 447) and Lützow (line 12626), both in the corpus. Slavata's memoirs print a German "Majestat-Brieff" passage (file line 8866) in the body; not read in full. |
| The Renewed Land Ordinance of 1627 | The brief asks for the religious articles | The only hit was a 1753 German reprint of Ferdinand II's ordinance (`bub_gb_ibZJAAAAcAAJ`), listed as undated in the host record and not opened. A search for its Czech title returned nothing. Lead only if someone opens that item. |
| Habsburg suppression decrees | The brief asks for them | No standalone collection found. Gindely's Gegenreformation (§3) prints many; not vendored. |
| The Unity's hymnals (Czech 1561, 1615) | The brief asks for them | Searches for "kancionál", "písně duchovní" and "Cithara sanctorum" returned only a 1928 and a 1952 modern item (`pisneduchovni0008cith`, `duchovnipisne0000unse`), neither cleared. No pre-1930 Unity hymnal scan was found. |
| Comenius, Historia Fratrum Bohemorum (clean scan) | The brief asks whether another scan is cleaner | `bub_gb_WoZLAAAAcAAJ` is the vendored 1702 print. A second scan of the same printing is `bub_gb_dmdTAAAAcAAJ` (noted in the Hussite dossier). The Ratio Disciplinae is also in the clean Seifferth 1866 Latin and English; that covers the Ratio. The Historiola and Panegersia remain only in the garbled 1702. |
| Comenius, Kurzgefaßte Kirchen-Historie (1739, German), Martyrologium Bohemicum (1766) | German renderings of the Brethren's history | `bub_gb__A5WAAAAcAAJ`, `10448790bsb`, `10026103bsb` are listed with no rights field; not opened. The Czech Historie o těžkých protivenstvích is vendored instead. Leads only. |
| Holl, Comenius | The brief names it | No such item on archive.org by title and creator search. Laurie (1881, `jacomenius00lauriala`) and Monroe (1900, `comeniusandbegi03monrgoog`) are English educational biographies; not opened and outside the church-history purpose. |
| Žerotín, Gindely's documentary volumes | The brief names them | A creator and title search for Žerotín found nothing. Gindely's Dekrety (vendored) and his Rudolf II volumes (`gindely-rudolf-ii-and-seine-zeit-1600-1612`, `10015883bsb`, `11427014bsb`) exist; the Rudolf volumes are not opened. |
| Slavata vol. II | Completes the memoirs | `pamtinejvyhokan01slavgoog` is mis-titled on the host as an unrelated work; not opened. Only vol. I is vendored. |
| Skála, other volumes | Completes the history | `historieeskodr03sk` is vol. III of the edition. Other volumes did not turn up in a creator search. Only vol. III is vendored. |
| Nejedlý, Prameny k synodám (1900) | Hussite confession sources | `pramenyksynodm00nejeuoft`, NOT_IN_COPYRIGHT. For the Hussite world's window (1441 to 1444); not opened. |
| Labyrinth, German of 1908 (Baudnik) | German rendering | `daslabyrinthder00baudgoog`: Fraktur garbled at all five points. Not vendored. |
| Lützow's own edition of the Labyrinth, 1905 and later printings | Cleaner scan | `labyrinthofworld00comeuoft` (1905) is the same translation; the 1901 edition was vendored. |

## 5. Open cross-world questions

- **The Hussite world (V.6).** The Hussite world's window ends at 1517. This world begins there. The Unity's own texts straddle the boundary: Gindely's Dekrety hold rulings from 1488, 1499 and 1504, and Bidlo's Akty are mostly 15th-century. Whether those belong to the Hussite world, this one or both is a mapping decision. Dekrety is staged to both; Bidlo is held as a lead. The Seifferth Ratio Disciplinae is currently Hussite context and is proposed here as tradition.
- **Lutheran Wittenberg (VI.1).** The 1535 Bohemian confession went to Wittenberg and was approved by Luther and others (Niemeyer's note). Staged to Wittenberg as context, provisional. The Wittenberg thread decides its weight.
- **Anabaptist Movements (VI.3).** The Hutterite Chronicle records the 1622 expulsion from Moravia. Whether Moravian Anabaptists belong in this world's ecology or only in theirs is not decided here.
- **The Moravian Church at Herrnhut (VIII).** The census states continuity. The antecedent rows are provisional and the Herrnhut thread owns that line.
- **Niemeyer is placed to six sibling worlds** on headings only (Lutheran Wittenberg, Reformed Cities, Huguenots, Dutch, Scottish, English). Each is provisional and the sibling thread should confirm or drop its row.
- **Utraquists and Unitas as one world.** The two bodies had different churches, offices and sources (the Utraquist consistory, the Unity's synods). The sources vendored are heavily Unity-side. Whether one build can hold both is a question for Step 0.

## 6. Step 0 scope notes and recommendation

**Floor question (A1).** The census floorNote reads "No question". Nothing in the files read contradicts it. The tail of the 1575 text as Niemeyer prints it names the Apostles' Creed and the Nicene symbol (near file line 50000). Step 0 has not tested the five commitments against either confession. Not tested here.

**Uniqueness and overlap.** Siblings are the Hussite world (V.6, whose window ends where this one starts and whose sources reach into it), Lutheran Wittenberg (VI.1), the Tridentine Church (1517 to 1650) and the later Moravian Church (VIII). This world's story is the last century of a national church under the Reformation, the Letter of Majesty, White Mountain and exile. No sibling tells that story. The formation logic differs from the Hussite world's (survival and suppression against founding and reform), but the Unity's discipline texts are shared across the boundary.

**Scale.** About 13.0M characters in nine new files plus 0.72M in the merged Comenius. About 10M characters are in Czech, a language none of the sibling worlds relies on for quotation. English exists for the Labyrinth, the Ratio Disciplinae (Seifferth) and the secondary Lützow. No English was found for the Dekrety, Obraz Jednoty, the persecution history, Skála, Slavata or the Kralice text. Under the 2026-09-25 ruling the Czech and Latin originals are primary evidence where the scan is clean. The weak points are the Latin-only Confession of 1575, the second-witness Niemeyer, the missing Utraquist voice and the missing hymnals.

**Recommendation, for Mark to decide, not a decision: build, sequenced after the Hussite world.** Floor (A1): the census says no question and nothing read contradicts it; Step 0 would confirm it. Sourcing (B1): the Unity side is now strong in Czech (discipline, history of the suppression, the Bible, Comenius's allegory) with clean scans, and the 1535 and 1575 confessions are in Latin as second witnesses. The Utraquist side is thin. Ecology (B2): lopsided to the Unity and to the political revolt, with two opposed lay witnesses (Skála, Slavata). Uniqueness (B3): holds, because no sibling covers the survival and suppression phase. Audiences (B4) and scale (B5) are for the Step 0 pass. This world should not be folded into the Hussite world: the window, the question and the Representative's moment differ. It should be built after the Hussite world, because the Unity's texts are shared and the Hussite build will settle the 1517 boundary rows named in §5. If the Utraquist voice cannot be found, Doc_01 should state the world as the Unity's last century with the Utraquists seen through the joint confession and the chroniclers.
