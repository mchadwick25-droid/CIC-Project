# Handover: Library, card-check fetch list, eras 1-7 (2026-11-15)

From the first session of this batch (session_01JMNsSEBeazzXCpEwX6BWdW), which stopped at the 400k-token mark
its brief set. Branch: `claude/library-cards-eras1-4` (keep the name; it now covers eras 1-7). No pull request is
open. **Nothing is vendored yet**: no file in `cic/texts/`, no registry, map or wants row has been written. The
searching is done; the intake is the next session's work.

## The brief, as it stands

- The list: "Texts to fetch, by era" on https://claude.ai/artifact/DAZgxvjPbCyAjzYadhREMW, eras 1 to 7 (the first
  coordinator widened the scope from eras 1-4 on 15 November). A text copy of the whole section is
  `dedupe/card-check-fetch-list_all-eras.txt`.
- Coordinator: session_01JMNsSCBTsM2UVaFpDa3BTF (it took over from session_01JMNsSADg2CkWvhgudEDKFw at 20:47 UTC;
  the first coordinator confirmed the handover itself). Report only to it, with `send_message`.
- Method: the Library's own rules (`cic/texts/INTAKE.md`; `Build/Ministry/Features/Source-Library/Decision-Log.md`,
  rulings R1-R12 and the shelf principle of the "Shelf rulings" entry; the title-page imprint test). One
  independent review, then at most a targeted recheck. Add a "from the card check" section to `CFT-Wants.md`
  naming the card each text serves, and log every title not found, with its card.
- Before the last commit: `python cic/engine/corpus_coverage.py`, and commit
  `cic-website/data/corpus-coverage.json` (the script is on main). Run the local checks of the era 8 batch 1 recipe
  (below). One draft pull request, one push after the checks pass, one line to the coordinator, then wait for its
  go. The Open-Gaps number comes from the coordinator at go time. Merges are sequenced one at a time.
- Nothing paid; no engine model calls.

## Relayed during the session (through the coordinators; not heard from Mark directly)

- Mark, as the first coordinator quoted him: "each of them are vendering all the sources they find into the
  library". Every find that passes the rights rules is vendored in this batch, with header, registry entry and
  shelf rows. Nothing stays as "located, not yet taken". Out: rights failures (logged with the reason) and
  hand-fetch sites (listed for Mark).
- Mark, as quoted: "we can also download texts that are public domain and remove any domain additions the archive
  added". Host additions may be stripped at intake only, with what was stripped recorded in the Provenance note;
  keeping the bytes whole is also fine; say which in each header. This session chose to keep the bytes whole.
- `cic/texts/INTAKE.md` does not carry that leave (its section 4 is the header template). The first coordinator
  asked that this be logged in this batch's Open-Gaps entry as a documentation gap, not fixed here.
- The second coordinator, on scans whose OCR cannot be read: "for now, vendor nothing from them. Log each one in
  your Open-Gaps entry as 'located, OCR unreadable', with its link, and Mark will rule on them later. That's a
  holding answer, not a new rule."

## What is done

1. **Dedupe by author and work** against `cic/texts/` and `REGISTRY.yaml`. 189 list rows are 155 distinct wants.
   Eras 5-7: `dedupe/era5.md`, `era6.md`, `era7.md` (Sonnet checkers; their "edition to search" column is from
   memory). Eras 1-4 were deduped by the Library thread; the results are in the table below.
2. **Searches**: nine Sonnet searchers on archive.org (the only host tried; the earlier logs record gallica,
   HathiTrust, Google Books downloads, MDZ and documentacatholicaomnia as blocked or broken from this sandbox).
   Their picks, with title-page words, imprint, host rights fields, OCR quality and the wanted passages' OCR
   line ranges, are merged in `candidates.json` (one object per picked file; `searcher` says which run).
   The era 6 rows 18-34 searcher (E6b) had not reported when this file was first written: see the last section.
3. **Second download by the Library thread** of every pick (`tools/refetch.py`): byte count equal to the host's
   listed size for every file (`library_thread_refetch.match` in `candidates.json`). The scratch downloads are
   gone with the session: fetch each again by identifier (`tools/refetch.py <id> ...` writes `dl/<id>__<djvu name>`
   and `dl/manifest.json` under the folder above `tools/`; copy `tools/` to a scratch folder first, since the
   downloads must not land in the repo).

## Eras 1-4: the result, want by want

Held already (no download): the two letters of Africanus and Origen on Susanna (`anf04_...xml`, file lines 35052
and 35126); the Chronograph of 354 (`prosper_chronica-minora-1-lat_mommsen1892.txt`, and the Liberian Catalogue
in Duchesne's Liber Pontificalis t. 1, Hippolytus's exile at file line 66699); the Chronicles of 741 and 754
(`chronica-minora-2_...mommsen1894.txt`, contents at file lines 177-179); the Gesta of Aquileia 381 (Mansi III,
about file lines 59650-60960); Palladius's fragments (`auxentius-durostorum_..._kauffmann1899.txt`); Victorinus on
the Apocalypse in English (ANF 7, file line 11541); Philostorgius (Walford 1855); Ezana's inscriptions (Littmann
1913); Jerome's Letter 3 and Innocent I to John of Jerusalem in English (NPNF 2.6, file lines 3752 and 28454);
Lazar of Pharp in French (Langlois t. 2); Martin I's letters and the Commemoratio (Mansi X, file lines 87154,
87305, 87561, 88434); Yahya of Antioch for 937-970 (PO 18); the Book of the Laws of Countries in English (ANF 8).

To vendor (26 files; imprint read by the Library thread in the OCR unless a leaf is named):

| want; card | identifier | imprint | note |
|---|---|---|---|
| Chrysostom, Adversus Judaeos; The Eight Sermons Against the Judaisers | patrologicursus104migngoog | PG 48, Migne, 1863 (OCR 190) | sermons at OCR 43014-57715 |
| Jerome, In Hiezechielem; Rufinus Translates Origen... | sanctieusebiihie05jero | Migne, Jerome t. 5, 1884 (OCR 204) | the 'Scorpius' prologue at OCR 483: check; a Garnier reprint by its own date |
| Jerome, letters in Latin; Hieronymian Ascetic-Literary | sanctieusebiihie01jero | Migne, Jerome t. 1, 1877 (OCR 103) | Innocent's letters at OCR 94245-94420 |
| Vigilius, Encyclica; The Pope Clings to the Altar Columns | patrologiaecursu69mign | PL 69, Migne, 1865 (page image leaves 4 and 6; OCR 123 reads '18G5') | encyclical at OCR 4141 to about 5050 |
| Pachomius, Greek Vita prima and Latin; Desert Monasticism | actasanctorum16unse | Acta Sanctorum Maii III, Palmé, 1866 (OCR 202, 238) | Greek about 169880-176590, poor to fair |
| Pachomius, Bohairic Life in French; Desert Monasticism | monumentspourser00amel | Amélineau, Paris, Leroux, 1889 (OCR 60-75, year reads 'I 889') | Vie de Pakhôme from OCR 4877 |
| Chronicon Paschale; Byzantine Imperial Church (Heraclian-Iconoclast) | bub_gb_N3AGAAAAQAAJ | Dindorf, Bonn, Weber, 1832 (OCR 40, 68) | vol. 1; host carries the Public Domain Mark |
| Ulrich of Zell, Consuetudines; Cluniac Reform Monasticism | patrologiaecursu0149mign | PL 149, 1882 (OCR 160, 271) | OCR 48646 to about 59425 |
| Admonitio generalis; Carolingian Reform Christianity | capitulariaregum01bore | MGH Capitularia I, Hannover, Hahn, 1883 (OCR 76, 94; a part title reads 1881 at 28) | no. 22 at OCR 4095-4777 |
| Bardaisan, Book of the Laws of Countries; Bardaisan and the Bardaisanites | spicilegiumsyria00cureuoft | Cureton, London, Rivington, 1855 (OCR 144) | English at OCR 1251-3419; the Syriac is not in the OCR |
| Ephrem, against the heresies, Latin of 1740; Bardaisan and the Bardaisanites | assemani-et-alii-1732-1746-ephraem-syri-opera-omnia-syr-2 | Rome, Vatican press, 1740 (OCR 3588-3591, 'M, DCC XL') | 'Sermones polemici' at OCR 94718-118272; Syriac unreadable, Latin readable with long s |
| Ibn Abd al-Hakam, Futuh Misr; Nubian Christianity | historyofconques00ibnauoft | Torrey, New Haven, Yale, MDCCCCXXII (page image leaf 6, read) | Arabic, OCR poor to fair: decide whether it counts as readable |
| al-Maqrizi on the baqt, in English; Nubian Christianity | travelsinnubia00burc | Burckhardt, London, Murray, 1819 (OCR 52) | Appendix III at OCR 27315-28750 |
| Pseudo-Samuel of Qalamun; The Lament Over the Lost Language | revuedelorientch2019151917pari | Revue de l'Orient chrétien 20, '1915-1917' on the volume title (OCR 32) | Ziadeh at OCR 18104-19309 |
| Chronicle of 1234, Syriac; Syriac Orthodox under Islam | chroniconanonymi01chab | Chabot, Paris, MDCCCCXX (OCR 95, 136) | Syriac only: decide whether the OCR counts as readable |
| Deir al-Surian's library; Syriac Orthodox under Islam | catalogueofsyria03brituoft | Wright, Catalogue part III, London, 1872 (OCR 82, 141) | preface from OCR 174 |
| Faras; Makurian Nubian Christianity | annals-of-archaeology-and-anthropology_1926_13_3-4; ..._1927_14_3-4 | Liverpool, MCMXXVI (OCR 27); MCMXXVII (OCR 38) | Griffith at OCR 361-2209 and 318-2882 |
| History of the Patriarchs, Mennas I to Joseph (767-849); Post-Aksumite Ethiopian Christianity | patrologiaorient10pariuoft | Patrologia Orientalis X, 1915 (OCR 66) | Evetts's part listed at OCR 42-46; its line range is not mapped yet |
| Xi'an stele, Dunhuang hymn, edict of 845; The Church of the East on the Silk Road | christiansinchin00moul; nestorianmonumen00saek; nestorianmonumen00legg | Moule, London, SPCK, 1930 (OCR 78); Saeki, 'First Published 1916, Reprinted 1928' (OCR 76-77); Legge, 1888 (OCR 110) | Moule: stele 2650-2905, hymn 3691-4115, edict 4745-4860 |
| Sermo Lupi; Late Anglo-Saxon Christianity | wulfstansammlung00wulf; cu31924032226783 | Napier, Berlin, Weidmann, 1883 (OCR 35); Cook and Tinker, Ginn, no year on the title page, 'copyright, 1907' at OCR 77 (ruling R12) | sermon at OCR 7126-7648; translation at 8229-8460 |
| Jelling stones; Scandinavian Conversion Christianity | gri_33125007805548 | Wimmer, Copenhagen, 1895 (OCR 37) | Danish; Jelling at OCR 826-4300 |
| Kollam plates; Who Signed the Kollam Plates; St Thomas Christians of India | madrasjournalofl1318madr | Madras Journal XIII, MDCCCXLV (leaf 6 per the searcher; OCR 72 reads 'MDCCOXLY'): read the leaf | Gundert at OCR 6557-8520 |

Not taken, eras 1-4 (for the Search_Log, the CFT-Wants rows and the Open-Gaps entry):
- Victorinus, CSEL 49: both scans (victoriniepiscop49victuoft, corpusscriptorum0049unse) are Johnson Reprint 1965.
- Philostorgius, Bidez 1913 (kirchengeschicht21philuoft): Greek OCR unreadable. Located, OCR unreadable.
- History of the Patriarchs, Agathon to Michael I (historyofpatriar0000beve): the title leaf prints no year. The
  whole-volume scans of PO 5 and PO 10 other than the Toronto PO 10 are CC BY-NC-ND per the searcher: held for Mark.
- Indian Antiquary III, Burnell on the Pahlavi crosses (india.history.resource.100291): the scan has no title page.
- Barsanuphius and John (Venice 1816); Kekelidze's Jerusalem lectionary (1912); Shushanik; the Travancore
  Archaeological Series text of the Kottayam plates; Griffith's Christian Documents from Nubia: not found.
- Hrabar: Jagić 1913 (entstehungsgesch00jagiuoft) discusses, prints no translation; Bodyansky 1862 is Cyrillic.
- Cosmas the Priest: Jireček 1876 only paraphrases.
- Paschal II's bull for Lund (1103/04): it appears lost. Jaffé's Regesta (regestapontificu01cath, no. 5994, OCR
  76400) registers it from the Lund chronicle; Gertz, Scriptores minores 2 (scriptoresminore02gert, OCR 5127-5134)
  quotes its opening words only.
- Yahya's continuation after 970 is PO 23 (1932), out by date. Cheikho's Eutychius (annaleseuty00euty, Beirut
  1906) located; which volume holds Yahya was not confirmed.
- Chronicle of 1234, vol. 2 (chroniconanonymi02chab): imprint not read.
- Modern only, no older print: the Cologne Mani Codex, the Kephalaia, Polotsky's Homilies (1934), Munro-Hay's
  coin catalogue, the Dunhuang translations of 2022; the Armenian Book of Letters (1901, unreadable OCR, an
  earlier batch); 'Deir al-Surian manuscripts' and 'Aksumite coin sequence' are not texts.

## Eras 5-7: the result so far

The searchers' own reports were returned as messages, not files; their substance is in `candidates.json`
(the `row` field is the row number in `dedupe/era5.md`, `era6.md`, `era7.md`). Calls by the Library thread:

- **Do not vendor**: Steele, Tudor and Stuart Proclamations (b24872763_0001): the host rights field carries a
  rightsstatements.org "In Copyright" statement; held for Mark. Theiner's Acta genuina (bub_gb_LeoCAAAAQAAJ): no
  year printed. Platina in Benham's English: no year printed. Caspar's Register of Gregory VII
  (dasregistergrego00cath): a 1955 reprint. The Trebnyk of 1646 (3-._20240402): a 1996 reprint. Nerses
  Shnorhali's letters (ShnorhaliNamakani, ShnorhaliTughtk), Arakel (india.history.resource.117162), Ibn al-Assal
  (AAlexandrina-224077): unreadable OCR or unread imprint; located.
- **Imprint still to be read by the Library thread on the page image** (the searcher read it there, or the OCR
  is garbled): bub_gb_IlodL0qDTsUC (Richard of St Victor, 1621, leaf 7); bub_gb_aPZ9FypObOoC (Speculum
  Carmelitanum II, 1680, leaf 9); nicetaechoniata01chongoog (Bekker 1835, leaf 7); olaipetrisvensk00klemgoog
  (1860, leaf 8); historiaeruthen00stargoog (1842, leaf 303); ChroniqueDeMaitreGuillaume (OCR '4864'); cgohvol1
  (1894); lachansondelacro01guiluoft and 02; procsdestempli01tempuoft (1841) and 02 (1851);
  bub_gb_n07s4-Y5K5EC (Tissier: 1660 or 1669, leaf 1); bub_gb_jP-quXiTDE4C (Platina, Louvain 1572, OCR 46);
  NeveExposeDesGuerresDeTamerlan (1860 or 1861); leduespedizioni00grasgoog (1886, leaf 16); ldpd_14360158_000
  (Eukleria 1673, leaf 6); coleccindedocu05madruoft (1844, leaf 9); berichtederaugen00corn (1853, leaf 7);
  envisitatzbogin00fremgoog (Palladius: no year on the title leaf; the editor's note at OCR 2223 and the host
  say 1872: ruling R12 needs the catalogue date to agree). `tools/imprint.py <id> <leaf>...` stacks the bottom
  third of each leaf into one small image.
- **Judge before vendoring**: pamtkdrevnhopsem00safr (Šafařík 1851: the Slavonic of Sava's Life has poor OCR);
  catalogueofarmen00bodl (a stand-in for Hakobyan's colophons, not the want); histoiredesving00bouigoog (Bouix
  1862, a retelling that cites Fróis); the two Roget volumes (a history quoting the Geneva Consistory registers);
  annalesecclesias30barouoft (Raynaldus gives the date of Id nostri cordis and a summary, not the bull);
  richardisanctovi00rich (the host title is wrong: the body is PL 176, Hugh of St Victor, 1880).
- Everything else in `candidates.json` for eras 5-7: take, once its imprint line is read.
- The dedupe verdict for era 5 row 17 was wrong: Cyril III is held in Renaudot 1713 (about file line 34564).
- Not found, eras 5-7 (log each with its card from the dedupe tables): era 5 rows 2b, 23, 37, 40; era 6 rows 1,
  4, 9 (the series itself), 12, 13, 14, 15, 16, 17; era 7 rows 1, 2, 3, 7, 9, 10, 13, 14, 15, 17, 18, 20, 30, 31,
  34, 35. Several of these are worth one more look by the Library thread before they are logged, since the
  searchers only tried title and creator queries: the chronicles of Susenyos (Pereira, Lisbon 1892-1900) and
  Galawdewos (Conzelman, Paris 1895); Hierotheos of Monemvasia (printed in Sathas's study of Jeremias II, Athens
  1870); Luther's Weimar edition for the visitation instruction; Foxe's Acts and Monuments for the Norwich
  trials; Giamil's Genuinae relationes (Rome 1902) for Sulaqa.

## What the next session does

1. Read `CLAUDE.md`, this file, `cic/texts/INTAKE.md`, and the era 8 batch 1 records on `main` once merged (or on
   `origin/claude/library-era8-1`): its `Handover.md` holds the recipe and the review lessons.
2. Copy `tools/` to a scratch folder; refetch every identifier marked take; read the outstanding imprints.
3. Have fresh Sonnet checkers map each file from its text (the era 8 `MAPPER_BRIEF.md`, about eight files each)
   and write the content notes and loci only from what the file shows.
4. Write the spec and run `tools/intake.py SPEC.json /home/user/CIC-Project "<batch label>"` (the era 8 tool:
   12-line header, registry entry, seed row, staging row). Name files by `INTAKE.md` section 3. Shelves: the card's
   own census entry (the ids are the file names in `cic/corpus-map/`); a tradition's own text is `tradition`, a
   later historian or outside witness `context`, a text earlier than the window `antecedent`.
5. Recipe after intake: `python cic/engine/texts_registry.py --write-readme`; `corpus_map_merge.py`, then
   `--check`; `texts_registry.py --check`; `works_registry.py --check`; `author_ids.py --check`;
   `corpus_index.py --build`; `tests_corpus_index.py --reuse-index`, `tests_corpus_structure.py`,
   `tests_passage_index.py`, `tests_corpus_map.py` (about 25 minutes: run in the background);
   `Build/worlds/_cross-world/gen_download_queue.py`; `tools/check_live_commentary.py --base origin/main --enforce`;
   `tools/check_spelling.py --base origin/main --enforce`; `python cic/engine/corpus_coverage.py`.
6. Records: `Search_Log.md` in this folder; a "from the card check" section in `CFT-Wants.md` (want, card, state,
   file, shelf; every not-found title with its card); a Decision-Log entry; the Open-Gaps entry at go time,
   carrying the "located, OCR unreadable" list with links, the held-for-Mark list, and the INTAKE.md gap.
7. One independent review (a fresh subagent given the files, not the conclusions), then at most a targeted recheck.
8. Draft pull request, one push, one line to the coordinator, wait for its go.
