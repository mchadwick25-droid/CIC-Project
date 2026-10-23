# Source Readiness Dossier — Family of Love & Spiritualists (Franck, Niclaes)

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and why it exists.

**Atlas ID:** VI.16
**Corpus-map slug:** `family-of-love-and-spiritualists-franck-niclaes`
**Time window:** c. 1540–1600
**Region(s):** Rhineland, Low Countries, England
**Dossier author / date:** source-research thread (Era VII one-world agent), October 2026; work resumed and finished October 2026
**Corpus-map / `cic/texts/` state as of:** October 2026. No bucket file exists for this slug. Eleven files are vendored and staged in `cic/corpus-map/_staging/` (see §1); they await the lead's merge of the registry and staging files. The census status is Floor Question (register). No Step 0 or Doc_01 exists.

## 1. Already assigned

No `cic/corpus-map/family-of-love-and-spiritualists-franck-niclaes.yaml` exists. Eleven files vendored this pass, all staged. Every file is a second witness for exact wording, because the English texts are EEBO microfilm OCR and the German is Fraktur OCR (mark under the OCR ruling of September 2026). Scale is about 930,000 words in all. Readable-token share is the share of tokens in five 700-character samples (10/30/50/70/90 percent) that read as words.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Evangelium Regni (A Joyfull Message of the Kingdom), English, London 1652 reprint | niclaes | tradition | assigned | ~58,600 words, 0.83 readable | `niclaes_evangelium-regni_london1652.txt` |
| Terra Pacis, English, 1575 | niclaes | tradition | assigned | ~43,100 words, 0.82 | `niclaes_terra-pacis_1575.txt` |
| The Principall Epistles of HN, English, 1575 (twenty epistles) | niclaes | tradition | assigned | ~111,000 words, 0.86 | `niclaes_principall-epistles_bohmberg1575.txt` |
| A brief Rehersall of the Beleef of the Goodwilling in Englande (the English Familists' own confession), 1575 | family-of-love | tradition | assigned | ~1,900 words, 0.82 | `family-of-love_brief-rehersall-of-the-beleef_1575.txt` |
| Mirabilia opera Dei (Tobias on Niclaes's calling), 1650 reprint | tobias-familist | tradition | assigned | ~31,200 words, 0.83 | `tobias-familist_mirabilia-opera-dei_1650.txt` |
| The Displaying of an horrible secte (Rogers), 1579 | rogers-john | context here; context to VI.4 (provisional) | assigned | ~49,400 words, 0.91 | `rogers-john_displaying-of-an-horrible-secte_bishop1579.txt` |
| A Confutation of Certaine Articles delivered unto the Familye of Love (Wilkinson), 1579 | wilkinson-william | context here; context to VI.4 (provisional) | assigned | ~57,300 words, 0.87 | `wilkinson-william_confutation-of-certaine-articles_daye1579.txt` |
| A Confutation of monstrous and horrible Heresies (Knewstub), 1579 | knewstub-john | context here; context to VI.8 and VI.4 (provisional) | assigned | ~81,200 words, 0.89 | `knewstub-john_confutation-of-monstrous-heresies-familie-of-loue_dawson1579.txt` |
| The Forbidden Fruit, English 1640 (title page "August. Eluthenius"; Franck by host attribution) | franck | tradition | **needs-ruling** | ~43,800 words, 0.90 | `franck_forbidden-fruit_anon1640.txt` |
| Paradoxa Ducenta Octoginta (280 Paradoxa), German, Pforzheim 1559 | franck | tradition | assigned | ~172,000 words, 0.75, Fraktur | `franck_paradoxa-deu_rab1559.txt` |
| Annals of the Reformation vol. II pt 2 (Strype, Oxford 1824), 1576–1580 | strype | context here; context to VI.4 (assigned) | assigned | ~281,300 words, 0.94 | `strype_annals-of-the-reformation-v2-pt2_1824.txt` |

What the files give the world. Niclaes now speaks in three English works (his gospel, his allegory, his letters), which carry the founder-shaped side the census names. The English community speaks in its own short confession (1575) and, through hostile hands, in the two Familist letters Rogers prints and the articles with an Elder's exposition (Theophilus) that Wilkinson prints. Tobias gives the follower's account of Niclaes's calling. Strype quotes the examinations of Christopher Vitells and Crinel (the coerced-testimony strand). Franck is thin: one German work in garbled OCR and one English print whose attribution needs a ruling.

Main loci, by file line: Rogers prints the Familists' letters at 7597 and 8586 with his answers at 8220; Wilkinson's articles with Theophilus start about 3012; Knewstub's David George confutation is at 10841 and 11001; Strype's Familist chapters run about 14519–16100 (Vitells 15849, Henry Nicolas 15895 and 15957; Wilkinson and Knewstub noted at 16662–16700).

## 2. Cross-link opportunities

Checked October 2026 by grepping every vendored `.txt` for "family of love", "Familist", "Niclaes", "Franck", "Barrefelt", "Schwenckfeld", "Coornhert" and "libertines", and opening the loci of the files below. Rows proposed in the agent's `crosslink_fragment.yaml`.

- **Rutherford, Letters (Bonar 1891).** `rutherford_letters_bonar1891.txt`, Letter CCCIX (1644) lists Familists among London's sects (line 32774) and the editor's footnote (line 32803) summarises David George, Henry Nicholas and Christopher Vivet with sources. Tier: same time-different region (1644, Scotland and London). Role: context, provisional. One proposed row. Out of window and a 19th-century editor's summary.
- **Wallington, Historical Notices vol. 1 (Webb 1869).** Editor's note 26 (line 1878) on the Familists and Fuller. A pointer only. Tier: out-of-window (Charles I). No row.
- **Latimer, Sermons (Corrie 1844).** Editor's footnote (line 13480) calls the Familists followers of David George, under the year 1549. Out-of-window and an editor's gloss. No row.
- **Winthrop, Journal vol. 1 (Hosmer 1908) and Shepard, Autobiography (1832).** New England's "Familists" of the 1630s are the Antinomian controversy's insult, not Niclaes's movement (Winthrop's own *Short Story* of 1644 is a lead, §3). Tier: out-of-window. No row.
- **Name hits not opened (named-never-opened):** `menno-simons_complete-works_funk1871.txt`, `dirk-philips_enchiridion_kolb1910.txt`, `calvin_*` (Institutes, Letters, Commentary on Genesis), `jewel_apology-of-the-church-of-england_bacon-morley1888.txt`, `perkins_golden-chaine-and-treatises_legat1600.txt`, `van-braght_martyrs-mirror_sohm1886.txt` matched the search pattern but were not opened; the pattern also matches ordinary words, so none is claimed as a link. A build thread should search them by "Familist" or "libertine". Calvin's *Contre la secte des Libertins* is a possible target and is not in the corpus.
- **Sibling dossiers.** `the-english-reformation-and-elizabethan-settleme_Source_Readiness_Dossier.md` and `puritanism_Source_Readiness_Dossier.md` do not name the Familist texts. Rogers, Wilkinson, Knewstub and Strype are staged to VI.4 (and Knewstub to VI.8) as provisional context rows; those threads decide their weight.
- **The Anabaptists (VI.3).** No vendored text here names Anabaptists in a way read for this pass, so no VI.3 row is proposed. Rembert 1899 (§3) ties Franck and Campanus to the Anabaptist milieu if the VI.3 thread wants it.

## 3. Verified acquisition leads

Checked on archive.org by metadata fetch and, where marked, by sampling the OCR. "Vendored" rows are in §1.

| title | author | translator/ed. | year | url | rights basis | verified by |
|---|---|---|---|---|---|---|
| The eleven vendored items (§1) | see §1 | none named | 1559–1824 | archive.org items named in each file header and in `seed_fragment.yaml` | pd-us-by-date; hosts carry no rights field for the EEBO scans (Internet Archive microfilm, not access-restricted); Paradoxa 1559 carries Public Domain Mark 1.0; Strype carries NOT_IN_COPYRIGHT | direct fetch, five-point OCR sample, October 2026 (Knewstub October 2026). **Vendored.** |
| The Church History of Britain, vol. IV (Fuller; Brewer ed. 1845) | Thomas Fuller | J. S. Brewer | 1845 (work 1655) | archive.org `churchhistoryofb04fulluoft` | pd-us-by-date; host NOT_IN_COPYRIGHT | direct fetch, OCR 0.88; read at file lines about 24200–24640. Its footnote cites the 1580 proclamation (Wilkins IV.297) and Knewstub's imprint. Not vendored this pass. |
| Church History of Britain, vol. V (Fuller) | Thomas Fuller | Brewer | 1845 | archive.org `churchhistoryofb05fulluoft` | pd-us-by-date; host NOT_IN_COPYRIGHT | direct fetch, OCR 0.86; read at lines 17840–17990 (the Familists' 1604 petition to James I). Not vendored. |
| Sebastian Francks lateinische Paraphrase der deutschen Theologie und seine holländisch erhaltenen Traktate | Alfred Hegler | none | 1901 | archive.org `sebastianfrancks00hegl` | pd-us-by-date (no rights field) | direct fetch, OCR 0.96 clean. German scholarship with edited text; not vendored. |
| Geist und Schrift bei Sebastian Franck | Alfred Hegler | none | 1892 | archive.org `geistundschrift00heglgoog` | pd-us-by-date; host NOT_IN_COPYRIGHT | direct fetch, OCR 0.63 (garbled); the Letter to Campanus is discussed from p. 50, not printed. Not vendored. |
| Die Wiedertäufer im Herzogtum Jülich | Karl Rembert | none | 1899 | archive.org `diewiedertuferim00remb` | pd-us-by-date (no rights field) | direct fetch, OCR 0.91. Discusses Franck's 1531 letter to Campanus (about line 11525) and cites Cornelius, *Münsterische Aufruhr* II, Beilage VI, as the printing. Scholarship; not vendored. |
| A Survey of the Spirituall Antichrist (Familisme and Antinomianisme) | Samuel Rutherford | none | 1648 | archive.org `survspiva00ruth` | pd-us-by-date (no rights field) | metadata only; djvu.txt present (1.8 MB); text not opened. Outside the window. Not vendored. |
| A Short Story of the Rise, Reign and Ruin of the Antinomians, Familists and Libertines | John Winthrop | none | 1644 | archive.org `shortstoryofrise00wint_0` | pd-us-by-date (no rights field) | search listing only. New England, out of window; not opened. |
| Chronica, tijtboeck en gheschiet bibel (Dutch) | Sebastian Franck | none | 1583 | archive.org `chronicatijtboec00fran` | pd-us-by-date (no rights field) | direct fetch, OCR 0.69 (blackletter); 7 MB, whole-world chronicle with the "heretic history" part a small share. Dutch, not the German of 1531. Not vendored. |
| Güldin Arch (German) | Sebastian Franck | none | 1538 | archive.org `bim_early-english-books-1641-1700_gulden-arch_franck-sebastian_1538` | pd-us-by-date | direct fetch, OCR 0.76, 1.8 MB. Not vendored this pass. |
| Mirabilia opera Dei (1575 print); Terra Pacis (1649 reprint); The Displaying (1578 editions); Forbidden Fruit (1642 reprint); Paradoxa (1558 printing) | as above | none | as given | the item ids named in `registry_fragment.yaml` notes | pd-us-by-date | sampled October 2026; duplicates of vendored texts, readable-token shares 0.66–0.90. Not vendored. |
| Other English Niclaes prints: Exhortatio I (1574, two items), Introductio (1575), Revelatio Dei (1575), Epistola XI (1574), Comoedia (1574), Dicta HN (1574), Proverbia (1575), Cantica (1575), Prophecy of the spirit of love (1649), Figure of the true tabernacle (1655), An Epistle sent unto two daughters of Warwick (1608), A Publishing of the Peace upon Earth (1574) | Hendrik Niclaes | none | 1574–1655 | archive.org items `bim_early-english-books-*_niclas-hendrik_*` | pd-us-by-date | Exhortatio, Introductio, Revelatio, Epistole HN and the 1608 Epistle sampled 0.77–0.90; the rest listed by metadata only. Not vendored: the Principall Epistles, Terra Pacis and Evangelium carry the voice. |
| An Introduction to the holy understanding of the glasse of righteousnesse (H. N. and Christopher Vitell) | Niclaes and Vitell | none | 1649 | archive.org `anintroductiont00vitegoog` | pd-us-by-date; host NOT_IN_COPYRIGHT | direct fetch, OCR 0.78. Not vendored; the 1575 Introductio is a duplicate. |
| Tudor and Stuart Proclamations 1485–1714 (calendar) | R. Steele | Earl of Crawford | 1910 | archive.org `tudorstuartprocl02crawuoft` | pd-us-by-date; host NOT_IN_COPYRIGHT | metadata only; not opened, so whether it carries the 1580 proclamation is unchecked. |
| A Faithful Narrative of God's gracious dealings with Hiel | Hendrik Jansen | not read | 1781 | archive.org `bim_eighteenth-century_a-faithful-narrative-of-_jansen-hendrik_1781` | unconfirmed | search listing only; not opened. |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Niclaes's Dutch or Low German originals; Dutch Familist prints | The English prints are "translated out of Base-Almayne" | archive.org searches on the Dutch titles (Spiegel der Gerechtigheit, Evangelium, Huys der Liefden, Terra pacis) returned only the English EEBO items. KB items checked by title search found none. No original-language text in hand. Closed October 2026. |
| Hiel (Hendrik Jansen van Barrefelt) prints | Census names the Hiel schism | archive.org searches on "Barrefelt", "Barrevelt", "Hiel" returned only the 1781 English print (§3, unopened) and unrelated hits. No Hiel text vendored. Closed October 2026. |
| The 1580 royal proclamation, text | Census names it | Not found as a standalone item. Strype II.ii prints only the September 1579 proclamation against Stubbs's book, and does not print the 1580 one (searched the vendored file). Fuller's footnote cites Wilkins, *Concilia* IV.297; Wilkins is not located. Steele's calendar (§3) unchecked. Closed as not located, October 2026. |
| Franck's Chronica (1531), German | Census names it | No German Chronica on archive.org (title and creator searches); the Dutch 1583 (§3) is garbled and enormous; the 1969 English item `chronica0000seba` is access-restricted and in copyright. Closed October 2026. |
| Franck's Letter to Campanus | Census names the Williams and Mergal 1957 English | `spiritualanabapt0000unse` (1957) is access-restricted and in copyright. No public-domain printing of the letter found (Rembert 1899 and Hegler 1892 discuss it; the printing is in Cornelius, not located). Closed October 2026. |
| 280 Paradoxes in English (Furcha 1986) | Census names it | `280paradoxesorwo0000fran` is access-restricted and in copyright. No public-domain English of the Paradoxa. Closed October 2026. |
| Hamilton 1981, Marsh 1994 | Census names them | In copyright; leads for readers only, not hosted. Closed. |
| Familist wills, parish and visitation records (Marsh's evidence base) | The census counter-evidence to "one man" | These live in county archives and Marsh's book; no digitised public-domain text found on a reachable host. Closed October 2026. |
| Cambridge History of Christianity vol. 6 | Census reference | In copyright; reference only. |
| Spiritual and Anabaptist Writers, Williams and Mergal 1957 | Translations of Franck, Schwenckfeld and others | Access-restricted, in copyright (as above). |
| Hegler 1892 as a source for the Letter to Campanus | Discusses it at length | OCR 0.63 and no printing of the letter; scholarship. |
| A 1649 reprint of the Principal Epistles or Terra Pacis as a cleaner witness | Possibly cleaner than 1575 | Terra Pacis 1649 sampled 0.83, no better than 1575 (0.82); no clean witness exists. Both remain second witnesses. |

## 5. Open cross-world questions

- **Is the Forbidden Fruit Franck's?** The title page names "August. Eluthenius"; the attribution to Franck rests on the host catalogue. Staged `needs-ruling`. The 1640 date also puts it outside the window. Whether to treat it as Franck's voice is the lead's or the project lead's call.
- **Franck and Niclaes in one world.** The census bundles them. They are not one community: Franck wrote in the 1530s and died in 1542; the sources in hand connect him to the Anabaptist-Spiritualist milieu (Rembert 1899), not to Niclaes. Whether VI.16 is one world or two is a cross-world mapping question. Related: the Schwenckfelders and the anti-Trinitarian current (VI.14) also read the creeds inwardly; their threads report separately.
- **Anabaptists (VI.3).** If Franck and Campanus are placed with the radical Reformation, VI.3's thread should say so. This dossier does not decide it.
- **English Reformation (VI.4) and Puritanism (VI.8).** Rogers, Wilkinson, Knewstub and Strype are staged there as provisional context. Whether the polemic belongs mainly to those worlds is for those threads.
- **Everything is second witness.** No clean scan of any Niclaes or Franck text exists. Quoting waits on page-image verification.

## 6. Step 0 scope notes and recommendation

**Floor question (census floorNote).** The writers read the creeds' content symbolically and inwardly, not as statements about outward, historical realities. The sources in hand bear on this directly. The English Familists' Brief Rehersall (1575) professes the Apostles' Creed, and the hostile writers say they also read scripture as allegory: Fuller (1655, read at the 1845 edition) says they "attenuated the Scriptures into Allegories" and "yoked" the words of H. Nicholas with God's word as equally infallible. Knewstub's and Wilkinson's quotations of the Evangelium Regni show Niclaes's own phrases, among them the "godded" Elders (Rogers, section "How the Elders are godded with God"). The floor test cannot be settled from a hostile reading alone, and the Familists' own outward conformity is part of the design. This is Mark's decision.

**Tradition or one man (second census question).** What the sources show, without settling it:
- *For founder-shaped.* Tobias's *Mirabilia* is an Elder's account of Niclaes's divine calling. The Epistles and the Evangelium are written as prophetic scripture. Rogers charges (1578 edition) that the Family teaches that none can speak the truth but H. N. or his Elders. Fuller says the Familists put Niclaes's words alongside God's.
- *For a community that outlived him, or split from him.* Strype and Rogers name Christopher Vitells as the patriarch of the English household (Strype says he recanted); Rogers prints letters from English Familists answering him in their own voice. The 1575 Brief Rehersall is a community statement. Fuller reports a petition from Familists to James I in 1604, decades after the 1570s prints, in which they seek to be kept apart from the Puritans.
- *Not in the corpus.* Wills, parish offices and conformity of known households (Marsh) and the Hiel schism have no text here. The "outlived the prophet" side therefore rests on hostile reports and one petition, not on community records.

**Uniqueness and overlap.** The Family overlaps VI.3 (Anabaptists, the same Low Countries milieu), VI.4 and VI.8 (the English polemic and who hunted them), and VI.14 and the Schwenckfelders (spiritualist reading of scripture). Its own mark is the secret fellowship with outward conformity, which no sibling tells.

**Scale.** Eleven files, about 930,000 words, of which 172,000 are German. About 245,000 words are Niclaes and his follower; about 190,000 are hostile English witnesses; 281,000 is Strype; Franck is about 216,000 (garbled German and an unsure English). Every Niclaes and Franck file is a second witness.

**Recommendation, for Mark to decide, not a decision: open question.** Floor (A1) is genuinely unsettled and the census itself says so; it should be ruled before any build. Sourcing (B1) is real for Niclaes and the English polemic, but Franck is thin and all the primary voices are second witnesses. Ecology (B2) is lopsided toward a founder and his hostile readers, with the community's own records absent. Uniqueness (B3) holds for the Family but the Franck bundle is in doubt. If Mark rules against the floor, the fallback is **atlas only**. If he rules for it and for a Family-only world, the sources above are enough to start Step 0.
