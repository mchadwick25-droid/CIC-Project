# Handover: Library, era 8 (1650-1815), 2026-11-15

From the first Era 8 Library session (session_01JMNsSBvnKXYr9NyFkoAnSQ), which stopped at a clean break for its
context size. The brief, the coordinator's additions A to J, Mark's widening ("add the church family needs and
global and any language pieces") and his model change ("use our free fable and stop all opus work except the
rewrite process": no Opus anywhere; the review is one fresh Fable subagent) all still stand. The coordinator is
session_01JMNsSAmN1HUCBWPQWS4gro; batch reports also go to session_01JMNsSD4wzPQYRHkAq6uKE3.

## State after batch 1 (second session, session_01JMNsSDAHDEA8fp5UjRHuYa)

Batch 1, the global files, is done on `claude/library-era8-1`: 30 files vendored (Africa, Egypt, Ethiopia, Latin
America, Asia). Its records: `Search_Log.md`, `R1_review.md`, `R1_changes.md`, `R2_recheck.md`,
`Mapper_Reports_batch1.md`, and the "Era 8 (1650-1815), batch 1" section of
`Build/Ministry/Features/Source-Library/CFT-Wants.md`. The two tables below headed "Africa, Latin America, Coptic,
Ethiopian, Syriac" and "Asia" are spent; the first two ("British Isles and Methodists", "North America and
Catholic Europe") are batch 2's starting list.

How batch 1 was worked, as a pattern: `fetch` every candidate by identifier and compare bytes (a short script);
read each title page in the OCR, and on the page image where the year is garbled (a contact sheet of the first
leaves finds the title leaf, then a crop of the imprint); `MAPPER_BRIEF.md` for Sonnet mappers, about eight files
each, who hand back contents maps; `mkspec1.py` as the spec; `intake.py` (it now writes `authors_ruled`); the
recipe below. A slug that is not a filename prefix needs an `authors_ruled` entry. A process note or a date in a
header's rights line fails `check_live_commentary.py`; keep rulings in the Search_Log.

Before vendoring, list `origin/main`'s `cic/texts/` again: the era 9 Library thread works the same day and took
Butcher's vol. 2 while batch 1 was in review.

A rule the coordinator announced on 15 November, to start once the coverage fix lands on main: each Library
batch runs `python cic/engine/corpus_coverage.py` after its last map or text change and commits the result before
the pull request. Check that the script is on main before relying on it.

Open-Gaps numbers come from the coordinator at go time; batch 1's entry is 291.

Carried into batch 2:
- Parry, Six Months in a Syrian Monastery (1895): take the Google scan `sixmonthsinasyr00parrgoog` (not fetched
  yet). The Columbia scan was dropped for its "Reproductions may not be made without permission" line. The census
  has no entry for the Syriac Orthodox between 1650 and 1906; the nearest shelf is
  `the-sayfo-and-the-syriac-diaspora`, context, needs-ruling.
- Dobrizhoffer (Latin and English), Muratori, Rancé, Fontaine, du Fossé, Quesnel: batch 2, with Catholic Europe.
- Vieira's Sermões: early volumes located, none chosen.
- Located and left for era 9: Pascoe vol. 2 (`twohundredyearso02pasc`), Launay tome 3 (`cihm_54002`).
- Mark's rulings of 15 November as the coordinator relayed them: a title page with no year may be dated by a
  copyright notice of 1930 or earlier, or by a dated preface (the coordinator adds: a printed licence or
  approbation leaf) when the library catalog's date agrees, the date and its place recorded in the header;
  "All rights reserved" on a print of 1930 or earlier does not block it; a part of a collection takes its date
  from the collection volume's own title page. Host additions (Google's sheet, archive.org notices) may be
  stripped at intake only, with what was stripped recorded in the Provenance note; batch 1 did not strip
  anything, since its line maps were made against the host text.
- Review lesson: say in the header where each title-page fact was read (OCR or page image); never credit the
  title page with a name, publisher or source that only the host record or outside knowledge gives.

## A rights widening, relayed and not yet used

At 17:15 UTC on 2026-11-15 the coordinator relayed a ruling as Mark's ("Yes, all eras now"; "Allow it generally"):
an American book printed 1931 to 1963 whose copyright was never renewed counts as free, with the renewal search
(where searched, what found) recorded in the header's rights line; US federal government works are free whatever
their date; a printed court or government record counts by its imprint; unprinted archive records are cite only;
take a non-renewed book only where it is the best source for a want, and log each one in the Search_Log. The rest
of rule B stands. The first session took nothing under this widening and did not hear it from Mark directly. It
loosens a rights rule, so it was checked: it is on main as ruling R7 of "Era 10 rights rulings: eleven questions
answered" (2026-11-15) in `Build/Ministry/Features/Source-Library/Decision-Log.md`. Read that entry before the
first file is taken under it.

## Done

- Batch 0 (eras 4-5, third fill): seven files, branch `claude/library-wants-eras4-5-b`, records in
  `Build/Ministry/Operations/Audits/2026-11-15_library-eras4-5-b/`.
- Era 8: the master list of wants, and four searches. NOTHING of era 8 is vendored yet. The downloads sat in the
  first session's scratchpad and are gone; re-fetch each by its identifier (a few minutes) and re-check the byte
  count against the host.

## Tools kept beside this file

- `SEARCHER_BRIEF.md`: the brief every Sonnet searcher read (rights rule, the only command shapes allowed, the
  hand-back table). Searchers ran with no permission stall on those shapes.
- `intake.py`: vendors files from a JSON spec: 12-line header, registry entry, seed row, staging row with
  `language` and `date`. `mkspec0.py` is the batch 0 spec, as a pattern.
- `ERA8_WANTS_MASTER.md`: 83 de-duplicated wants in 13 groups, with what is held, plus 16 council leads and the
  51 era 8 census entries.

Recipe after `intake.py`: `python cic/engine/texts_registry.py --write-readme`; `corpus_map_merge.py`, then
`--check`; `texts_registry.py --check`; `works_registry.py --check`; `author_ids.py --check`;
`corpus_index.py --build`; `tests_corpus_index.py --reuse-index`, `tests_corpus_structure.py`,
`tests_passage_index.py`, `tests_corpus_map.py` (the four take about 25 minutes: run them in the background);
`Build/worlds/_cross-world/gen_download_queue.py`; `tools/check_live_commentary.py --base origin/main --enforce`;
`tools/check_spelling.py --base origin/main --enforce`. An author slug the index has not seen needs an
`authors_ruled` block in its staging file. A shelf file the batch touches must lose any commentary already in it
(fix the staging file, then merge).

Lessons from the batch 0 review: give ranges from the heading line, never a running head; where a volume has an
engraved title and a letterpress title, read both years; a Life's subject is not its author; say when a scan opens
with Google's sheet or an uploader's cover sheet, and count its lines.

## Era 8 candidates found (identifier; imprint as read; call)

"Read" means the Library thread read the title-page lines itself. "Searcher" means only the searcher did, so the
Library thread still has to. Page images: `https://archive.org/download/<identifier>/page/n<leaf>.jpg`.

### British Isles and Methodists (all eight read by the Library thread: take)

| want | identifier | imprint | note |
|---|---|---|---|
| A135 Anne Dutton, A Brief Account of the Gracious Dealings of God | bim_eighteenth-century_a-brief-account-of-the-g_dutton-anne_1750 | London, 1750 (title page noisy; year clear) | the 1750 printing in three parts, not 1743; long-s OCR; letters appended |
| A136 Gibbons, Memoirs of Isaac Watts | memoirsofrevisaa00gibb | London: Buckland and Gibbons, MDCCLXXX | long-s read as f |
| A137 Orton, Memoirs of Doddridge | memoirsoflifecha00orto | Edinburgh: Waugh and Innes, M.DCCC.XXV | later edition with David Russell's essay; the 1766 first edition (10062810bsb) has noisy OCR |
| A139 Roberts, Memoirs of Hannah More, vol. 1 | memoirslifeandc00moregoog | London: Seeley and Burnside, MDCCCXXXV, third edition | vols 2-4 not taken; vol. 2 memoirsoflifecor02robe (1834, Harper) seen |
| A140 Smith, Life of Thomas Bray, ed. Todd | publickspiritil00toddgoog | London: Rivington, 1808, second edition | Todd adds much; the 1746 print's year is garbled |
| A141 Wilberforce, Life, vol. 1 | lifewilliamwilb04wilbgoog | London: John Murray, MDCCCXXXVIII | vols 2-5 located: lifewilliamwilb02wilbgoog, lifewilliamwilb12wilbgoog, lifeofwilliamwil04wilbuoft; vol. 5 only as a lending copy |
| A159 Gregory, Robert Raikes | robertraikesjou00alfrgoog | London: Hodder and Stoughton, 1877 | the 1784 letter is discussed at about OCR 2273-2374; whether printed whole was not read |
| A133 Taft, Holy Women, vols 1-2 (Sarah Crosby) | taft-biographical-sketches-of-the-lives-and-public-ministry-of-various-holy-women | 1825 (vol. 1) and 1828 (vol. 2) | a user upload of 2025; Crosby's memoir in vol. 2 from about OCR 20081 |

Not found: Hindmarsh, Rise and Progress (1861); Ann Griffiths in Welsh (Hughes, Morris Davies, O. M. Edwards;
Y Traethodydd for 1846 not identified among many scans); Kirk's Biographies (1909).
Methodist shelf, missing: Wesley's Letters; Wesley's Sermons after vol. 1; Charles Wesley's Journal vol. 2;
Whitefield's later Journals; Fletcher's Checks; the Arminian Magazine. Held: Curnock's Journal, all eight volumes.

### North America and Catholic Europe (searcher only; check each title page)

| want | identifier | imprint as the searcher read it | note |
|---|---|---|---|
| A128 Love, Samson Occom | samsonoccomchris00love | Boston: Pilgrim Press; only "Copyright, 1899" quoted: read the imprint | Love prints about 25 lines of Occom's 1768 narrative (OCR 1327-1354), not the whole |
| A131 Walker, Some Aspects of the Religious Life of New England | someaspectsofrel00walk | New York: Silver, Burdett, 1897 | an extract of Nathan Cole at about OCR 3155-3235; no full printing by 1930 found |
| A132 Cooley, Lemuel Haynes | sketchesoflifech00cool | New York: Harper, 1837 | mixed voices: Cooley, Haynes's sermons and letters |
| A134 Davies, Sermons, vol. 1 | sermonsonimporta179401davi | Philadelphia: Campbell; year garbled ("M.DCC.xeiv"): read the page image | memoir at about OCR 598, Finley 636, Gibbons 1715 |
| A138 Judith Sargent Murray, The Gleaner, 3 vols | gleanermiscellan01murr; bim_eighteenth-century_the-gleaner-a-miscellan_murray-judith-sargent_1798_2; gleanermiscellan03murr | Boston: Thomas and Andrews, 1798 | essays under a pen name; her life only indirectly. John Murray's Records (1816) is held; whether it carries her chapters was not checked |
| A157 McGready, Posthumous Works | posthumousworkso00mcgr | Nashville: J. Smith, 1837, two volumes in one | the Narrative of the Revival, a letter of 23 Oct 1801, from OCR 222 |
| A158 Thomas Campbell, Declaration and Address | declarationaddre00campiala | Pittsburgh, Centennial edition, 1906 on the title page (host says 1908) | a line-for-line reprint, not the 1809 print |
| A158 Richardson, Memoirs of Alexander Campbell, vol. 1 | memoirsalexande00unkngoog | Philadelphia: Lippincott, 1868 | Thomas Campbell's early life in chapters I-II |
| A146 Soli Muratori, Vita | bub_gb_S09fcFzVIu4C | Naples, MDCCLVIII | the Venice 1756 scan shows no year |
| A146 Muratori, Il cristianesimo felice | A118051 | Venice: Pasquali, MDCCXLIII | |
| A146 A Relation of the Missions of Paraguay | bim_eighteenth-century_a-relation-of-the-missio_muratori-lodovico-anton_1759 | London; year garbled ("M. Dec. LIX."): check | English from the French |
| A147 Marsollier, Vie de Rancé, 2 vols | laviededomarmand01mars; laviededomarmand02mars | Paris: Savoye; year garbled ("M. Dec LVIII"): check | Gonod's Lettres de Rancé (lettresrecueill00rancgoog) reads "4846": check the page image |
| A148 Fontaine, Mémoires, 2 vols | memoirespourser01fontgoog; memoirespourser00fontgoog | Cologne, M DCC XXXVIII (host says Utrecht 1739) | |
| A148 du Fossé, Mémoires | memoirespourser00fossgoog | Utrecht; year garbled ("M Dec XXXIX"): check | Bouquet's edition (1876-79) vols 1-3 located, not taken |
| OG225 Quesnel, Réflexions morales, tome 1 | bub_gb_GmCin_UcwIcC | Paris: Pralard, M. DC. XCIII | opens with a mandement; the Gospels not checked |
| OG181 Dobrizhoffer, Account of the Abipones, 3 vols | accountofabipone18221dobr; cu31924104090935; cu31924104095033 | London: John Murray, 1822 | |
| OG181 Dobrizhoffer, Historia de Abiponibus, pars 1 | historiadeabipon00dobr | Vienna: Kurzbek, 1784 | which pars was not confirmed |

Not found: Davenport's Confession and Retractions (try Tracy, The Great Awakening, 1842); Herman of Alaska.

### Africa, Latin America, Coptic, Ethiopian, Syriac (searcher only; check each title page)

| want | identifier | imprint as the searcher read it | note |
|---|---|---|---|
| OG175 Proyart, Histoire de Loango | histoiredeloango00proy_0 | Paris and Lyon, M. DCC. LXXVI | the mission from about OCR 7287; not the Antonian movement |
| B2 AF-8 Pascoe, Two Hundred Years of the S.P.G., 2 vols | twohundredyearso01pasc; twohundredyearso02pasc | London, 1901 | a digest of the Society's records; Quaque at about v1 OCR 25694-25800 |
| OG175 McCarter, Dutch Reformed Church in South Africa | dutchreformedchu00mcca | Edinburgh: Inglis, 1869 | mostly era 9 |
| A151 Bruce, Travels, vols 2 and 3 | travelstodiscov02bruc; travelstodiscov03bruc | Edinburgh: Ruthven, MDCCXC (v2 noisy) | first edition |
| A152 Butcher, Story of the Church of Egypt, vol. 2 | storyofchurchofe02butc | 1897 quoted from a shelfmark line: read the imprint | a secondary account |
| OG175 Vansleb, Histoire de l'Église d'Alexandrie | bub_gb_m3GZP6sZZJMC | Paris: Clousier, M. DC. LXXVII | |
| OG175 Vansleb, Nouvelle relation | bub_gb_8n2JTTnOoMIC | Paris: Michallet, M. DC. LXXVII | |
| OG175 Vansleb, The Present State of Egypt | presentstateofeg00wans | London, 1678 | |
| A152 al-Jabarti, Merveilles, tome V | merveillesbiogra05jaba | Cairo: Imprimerie nationale, 1890 | Ibrahim "el Djohari" at about OCR 9380-9410; years 1209 and 1210 at 8995 and 9432 |
| VII.38 Gobat, Journal of Three Years in Abyssinia | journalthreeyea01bairgoog | New York, 1850 (host wrongly 1834) | Clark's English from the French, with Baird's sketch |
| B2 ME-7 Parry, Six Months in a Syrian Monastery | sixmonthsinsyria00parr | London: Horace Cox, 1895 | a visitor's account; a Columbia notice at the head |
| A123 Vieira, Maria Rosa Mystica, parts 1 and 2 | mariarosamystica00viei; mariarosamystica01viei | Lisbon: Deslandes, M. DC. LXXXVI; Craesbeeck, M. DC. LXXXVIII | |
| A123 Barros, Vida do padre Antonio Vieyra | vidadoapostolico00barr | Lisbon: Officina Sylviana, M. D.CC.XLVI | |
| A123 Vieira, Cartas, tomos 1 and 2 | cartasdopantonio00viei; cartasdopantonio01viei | Lisbon, M.DCC.XXXV | |
| OG176 Antonil, Cultura e opulencia do Brasil | culturaeopulenci00anto | Lisbon, 1711 | |
| OG176 Le Code noir | BSG_8F403_7INV2830RES | Paris: Prault, M. DCC. LXVII; host rights "Domaine public" | prints the edict of 1685 |

Imprint unreadable in the OCR, page image to check: Weld Blundell, Royal Chronicle of Abyssinia
(royalchronicleof00welduoft); Merolla, A Voyage to Congo (voyagetocongosev00mero); Gobat 1834
(journalathreeye00leegoog); Code noir 1743 (codenoirourecuei00fran). Guidi's Annales regum Iyasu II et Iyo'as
(1910; annalesregumiysu01guid, 02guid; Ge'ez and Latin) located, not fetched.
Held for Mark: Ximénez, Historia de la provincia de San Vicente de Chiapa y Guatemala, vols 1 (1929) and 2 under
the Biblioteca Goathemala uploads, licence CC BY-NC-ND 3.0. Vol. 3, with Cancuc, is dated 1931: out.
Not found: the relations of Bernardo da Gallo and Lorenzo da Lucca (no print by 1930); Zucchelli's Italian;
Capitein; Thompson (image only); Ntsikana's hymn; the Synod of Mount Lebanon 1736 (Collectio Lacensis vol. 2
is not on archive.org); Hernández y Dávalos and Morelos; Úrsula de Jesús. Charon's tome I was never printed.
Vieira's Sermões: many early volumes exist (sermoensdopanton01viei 1683, 07viei 1689, 00viei 1699); none chosen.

### Asia (searcher only; check each title page)

| want | identifier | imprint as the searcher read it | note |
|---|---|---|---|
| A124, A125 Launay, Histoire générale de la Société des Missions-Étrangères, tome 1 | cihm_54000 | Paris: Téqui, 1894 | Pallu and Lambert from about OCR 619; Tonkin synod 12416-13792; Maigrot at 27731, 28563, 30832-30881. Tomes 2 and 3: cihm_54001, cihm_54002 |
| A125 Pallu, Relation abrégée | relationabregeed00pall | Paris; year garbled ("M DC. LXXXfL", host 1682): check | the volume opens with the privilege for Bourges's Relation (1666); what it holds was not checked |
| A126 Rhodes, Divers voyages | bub_gb_74U28QLld2UC | Paris: Journel, M. DC. LXXXII | a 1682 reprint; the 1854 edition also located |
| A127 Sketch of the Catholic Church in Ceylon | ASketchOfTheRiseAndProgress | Colombo, 1848 | author not on the title page; Vaz at about OCR 754-908 |
| A156 Baldaeus, Naauwkeurige beschryvinge | naauwkeurigebesc00bald | Amsterdam, 1672 | Dutch; long-s |
| A156 Baldaeus in English (Churchill) | trueexactdescrip00bald | London: Churchill; year reads "L703": check | |
| OG178 Valentijn, Oud en Nieuw Oost-Indiën, deel 2 | oudennieuwoostin02vale | Dordrecht and Amsterdam, MDCCXXIV | the church-affairs book was not located; deel 3 (oudennieuwoostin03vale) failed three times with HTTP 500 |

Imprint unreadable, page image to check: Rhodes's Cathechismus (bub_gb_p8UC5ZZ21Q8C; Latin and Vietnamese, the
Vietnamese garbled); Rhodes, Tunchinensis historiae (bub_gb_GxWRJap5LkMC_3); Historia cultus Sinensium
(bub_gb_vW4zWSxsvhIC, and its Continuatio bub_gb_rG8lStorjTwC), which holds notes on Maigrot's Mandate and the
Jesuit reply, not the Mandate. Held for Mark: phep-giang-tam-ngay (Rhodes's catechism, CC BY-NC-ND 4.0).
Maigrot's Mandate of 1693 is not in the held Propaganda Collectanea (one unrelated mention, file line 35922).
Not found: Launay's Lettres de Pallu and Documents historiques; the Monita; Rego's Life of Vaz before 1930 and
any English Life; Huang Bolu; André Ly's Journal; the Sichuan synod; Urakawa; Tenchi hajimari; the
Varthamanappusthakam; Ittoop; E. M. Philip (1908). dbnl.org was not tried for Valentijn.

## Not yet searched

Groups 1 (Orthodox: Tikhon of Zadonsk, Kosmas, Athanasios Parios, Klein and Nilles, Georgia), 7 (Petersen,
Arnold, Rebecca Protten, Ammann, Hamilton 1901, Hutterites), 8 (Hauge; the Nordic church law, Pontoppidan,
Kingo, Brorson), 13 (Hungarian Protestants) and the 16 council leads of the master list; the Old Believers world
(`obel`, 1666-1815) and the Methodist gaps above; census entries with a thin shelf (VII.43, VII.47, VII.49,
VII.45, VII.40).

## Suggested batches, one pull request each

1. `claude/library-era8-1`: the global files (Africa, Latin America, Coptic, Ethiopian, Syriac, Asia).
2. `claude/library-era8-2`: British Isles, Methodists, North America, Catholic Europe.
3. `claude/library-era8-3`: a new search of the groups not yet searched, then their files.
Before each merge: one line to the coordinator, wait for its go, and take the Open-Gaps number from it.
