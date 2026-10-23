# Source Readiness Dossier — Maronite Christianity, the Union Formalized

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** V.22
**Corpus-map slug:** `maronite-christianity-era-6`
**Time window:** 1300–1517
**Region(s):** Mount Lebanon (the Qadisha valley, the Kesrwan) and Cyprus
**Dossier author / date:** Library thread, Era VI session (east batch), October 2026
**Corpus-map / `cic/texts/` state as of:** October 2026, branch `library/era-vi-2026-10`. No bucket file `cic/corpus-map/maronite-christianity-era-6.yaml` existed before this pass. Three files were vendored for this world, each with a staging file that passes `corpus_map_merge.py --check`. Their registry entries, seed rows and cross-link rows sit in the lead's fragment files until merged. Four shelf files that carry Maronite matter are proposed as cross-links (§2).

Census inputs (checked October 2026 in `world-census.json`): status Pre-Survey Candidate, floor note "No question — the monothelete dispute is an argument about the church's early history, not about what Maronites confess now." Sourcing line: "Thin to moderate, and much of it from the Roman side: the Florence union act of 1445 and the Fifth Lateran reception of 1516. Little survives from the patriarchal archive itself for this period." The only voices line reads: "Named individuals are scarce in this window ... the era's Maronite voice survives chiefly in liturgical manuscripts and scribes' notes." The census has no `sources` list for this world.

## 1. Already assigned

Nothing was assigned to this world before this pass. The three files below were vendored this pass. Scale is characters in the vendored file, counted.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Tarikh al-ta'ifa al-maruniyya (History of the Maronite Community), Arabic, ed. Shartuni, Beirut 1890 | duwayhi | tradition | provisional | 773,535 characters | `duwayhi_tarikh-al-ta-ifa-al-maruniyya-ara_shartuni1890.txt` |
| Bibliotheca orientalis Clementino-Vaticana, tomus I (Assemani, Rome 1719): the Maronite writers and patriarchs, Gabriel Barclai of Nicosia | assemani | context | assigned | 2,417,337 characters in the file; the Maronite chapter list is 13 lines (file lines 6435–6447) | `assemani_bibliotheca-orientalis-tomus1-de-scriptoribus-syris-orthodoxis-lat_1719.txt` |
| Annales ecclesiastici, tomus 28 (Raynaldus; Theiner's edition, 1874): the Cyprus union of 1445 and the bull Benedictus sit Deus | raynaldus | context | assigned | 4,039,630 characters in the file; the Cyprus passage is paragraph 21 under 1445 (file line 62418 onward) | `raynaldus_annales-ecclesiastici-tomus28-1424-1453-lat_theiner1874.txt` |

What kind of witness each is:

- **The Roman side.** Raynaldus prints the bull of 1445 by which Eugenius IV received the Cypriot Chaldaeans (the Nestorians of the island) and the Maronites. It names Timothy, the Chaldaean metropolitan, and Elias, bishop of the Maronites. This is the document the census calls the Florence union act, and the Maronites do not speak in it.
- **The Maronite scholar in Rome.** Assemani (a Maronite priest and scriptor of Syriac and Arabic in the Vatican Library) catalogues the Syriac writers and gives chapters to the Maronite patriarchs and to Gabriel Barclai, bishop of Nicosia. It is a Roman-side Maronite voice from 1719, not the church's own archive.
- **The later Maronite historian.** Duwayhi's history of the Maronite community is the church's own account, in Arabic, edited in 1890. The OCR is heavily damaged. The sections on 1300 to 1517 were not located. It is a locator only.

## 2. Cross-link opportunities

Checked by searching the headers and bodies of every `cic/texts/*.txt` for Maronit*, Maroni, Kesrwan, Qadisha and Lebanon, then opening the hits. Proposed rows are in the lead's `crosslinks.yaml`.

- **Mansi, tomus 32, `mansi_sacrorum-conciliorum-collectio-tomus-32-1438-1549-lat_welter-facsimile1901.txt`** (bucket: the Latin papal church; staged only for Lateran V and the Pisan conciliabulum). Tier: same time. It carries the one place where a Maronite patriarch speaks in the window: the contents list a "Mandatum patriarchae Maronitarum" (line 851); the orator of the Maronite patriarch's obedience is at lines 63569 and 63581; "EPISTOLA PATRIARCHAE MARONITARUM" is at 98303 and "LITERA MARONITARUM AD LEONEM X" at 98365, where "Petrus patriarcha" writes to Leo X; the election and oath of the patriarch run from 98633 to 98979. Proposed row: tradition / assigned.
- **Mansi, tomus 26, `mansi_sacrorum-conciliorum-collectio-tomus-26-1344-1409-lat_welter-facsimile1901.txt`.** Tier: same time-place. The Constitutions and Synodicon of Nicosia begin at line 29451. The attendance list near line 35519 names Greek bishops, "fratre Georgio, Maronitarum" and "fratre Gregorio, Armenorum", and line 36036 names interpreters between Latins and Maronites, Jacobites and Nestorians. Assemani dates the council to 1340. Proposed row: context / assigned.
- **Assemani, Bibliotheca orientalis III.2, `assemani_bibliotheca-orientalis-tomus3-pars2-de-syris-nestorianis-lat_1728.txt`.** Tier: same time-place, second witness. Lines 29125–29216 record that Timothy of Tarsus, Chaldaean metropolitan in Cyprus, abjured the Nestorian error before Eugenius IV, and that the bull is dated "VII. Non. Aug. anno 1445", that is 7 August 1445. The bull names the profession of Isaac, envoy of Elias, bishop of the Maronites in Cyprus. This gives the date that the Raynaldus extract does not. Proposed row: context / assigned.
- **Barhebraeus, Chronicon ecclesiasticum vol. 3, `barhebraeus_chronicon-ecclesiasticum-vol3-lat_abbeloos-lamy1877.txt`.** Tier: out-of-window (the chronicle is thirteenth-century; the note is the editor's, 1877). The index entry "Maronitae an semper fuerint orthodoxi, 404" is at line 32675, and Lamy's addendum, citing Debs's book against Joseph David, at 34767–34780. The Syriac Orthodox side of the argument on the church's early history. Proposed row: context / provisional.
- **Michael the Syrian, Chronique tome 2, `michael-the-syrian_chronique-tome2-livres-viii-xi-fra_chabot1901.txt`.** Tier: out-of-window (twelfth century). The West Syriac patriarch's account of the Maronites and the monothelete dispute (lines 39327–39349, with a note on the name at 34738). Proposed row: antecedent / provisional.
- **Noted, no row proposed:** Cyril Lucaris, *Lettres anecdotes* (1718 printing; thirteen hits for the Maronites), the Propaganda Fide collection (`propaganda-fide_collectanea-decreta-instructiones-rescripta-v1-lat_1907.txt`, 49 hits, from 1622), the Magnum Bullarium vol. 2 (six hits, 1560–1591), the seventeenth-century travellers (Vincenzo Maria, Sebastiani, Tavernier) and Wigram (1929). All are after the window. The Mansi tomus 2 file names "Maronita e Libano" in an early-church volume. Mansi 31 (Florence) has no "Maronit" hit in its OCR.

## 3. Verified acquisition leads

Each lead was checked on its host. Item records were read for date, `possible-copyright-status`, licence and the text file. Texts fetched were sampled at opening, middle and end. All are public domain by date unless a row says otherwise.

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| Tarikh al-ta'ifa al-maruniyya | Isṭifān al-Duwayhī; ed. Rashīd al-Khūrī al-Shartūnī | none (Arabic) | 1890 | archive.org `AAlexandrina-142168` | pd-us-by-date on the host date; the printed year is not legible | metadata read; 1.4 MB fetched; heavily damaged Arabic; October 2026. **Vendored as second witness only.** |
| Bibliotheca orientalis Clementino-Vaticana, tomus primus | Giuseppe Simone Assemani | none (Latin) | 1719 | archive.org `BOClementino1` | pd-us-by-date; Public Domain Mark 1.0 | metadata and the line "ROME, MDCCXIX" read; 2.5 MB fetched; Latin with long s read as f, about 0.45 matched against a clean Latin list; October 2026. **Vendored.** A second scan, `india.history.resource.71761` (2.3 MB), was not vendored. |
| Annales ecclesiastici, tomus 28 (1424–1453) | Baronius, Raynaldus, Laderchi; ed. Augustin Theiner | none (Latin) | 1874 (the host says 1864) | archive.org `annalesecclesias28barouoft` | pd-us-by-date; no rights field | metadata and title page read; 4.0 MB fetched; Latin with moderate OCR damage; October 2026. **Vendored.** |
| Missione apostolica al patriarca, e maroniti del Monte Libano | Girolamo Dandini | none (Italian) | 1656 | archive.org `bub_gb_T5TPhzEBjA4C` | Public Domain Mark 1.0 | metadata read; 0.44 MB fetched; readable Italian, long s; October 2026. A papal envoy's mission to the Maronite patriarch, published after the window; not vendored. |
| La Syrie: précis historique | Henri Lammens | none (French) | 1921 | archive.org `lasyrieprcishi01lamm` | pd-us-by-date on the host date | metadata read; 0.63 MB fetched; clean; October 2026. Context on Lebanon under the Mamluks; not vendored. |
| Tarikh al-ta'ifa al-maruniyya, books4all.net reprint | Isṭifān al-Duwayhī | none (Arabic) | no year | archive.org `tarekh_taefa_marounia` | not established: no date, rights or licence field | metadata read; text not fetched; October 2026. A modern reprint with no rights statement; not vendored. |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Duwayhi in a clean scan | The patriarchal history, named in the task | Three Arabic items found: the Alexandria scan (vendored, damaged), the books4all reprint (rights unstated) and a 2020s upload (`20261008_20261008_2117`, `20221027_20221027_1703`, no metadata). No clean, rights-clear copy. |
| Assemani BO I, other chapters | Maronite writers | Vendored whole; BO III.2 is on the shelf and is proposed as a cross-link. |
| The Florence Maronite bull in Mansi 31 and the Bullarium Romanum | The task named "Mansi 31, Bullarium Romanum" for the 1445 act | Mansi 31 (on the shelf) has no "Maronit" hit in its OCR. The Magnum Bullarium on the shelf is vol. 2 (1560–1591). The bull is printed in Raynaldus under 1445 (vendored) and cited in Assemani III.2. |
| Lateran V (Mansi 32) | The 1516 reception | Already on the shelf and staged for the Latin papal church only; proposed here as tradition (see §2). |
| Dandini, A voyage to Mount Libanus (English, 1698, `bim_early-english-books-1641-1700_a-voyage-to-mount-libanu_dandini-girolamo_1698`) | Named in the task as the English | Fetched (75 KB). Microfilm OCR is noise, and it is after the window. |
| Quaresmius, Elucidatio Terrae Sanctae (1639) | The Franciscan custodian's account of the Maronites | Searched archive.org for "Quaresmi", "Quaresmius" and "Elucidatio Terrae Sanctae"; nothing found. |
| Nairon, Euoplia fidei and the other seventeenth-century Maronite apologetics | Maronite self-defence | Searched "Faustus Naironus", "Euoplia fidei", "De origine nomine ac religione Maronitarum"; only a coffee treatise by the same author turned up. |
| Dib, *Histoire de l'Église maronite* (1930) | Named in the task | Not found by title or creator on the host. The English *History of the Maronite Church* (`history-of-the-maronite-church-dib`, host date 1962, translated by Beggiani) is assumed in copyright. |
| Ibn al-Qila'i (Gabriel Barclai) and the Maronite manuscripts | The one named Maronite author of the window | Searched "Ibn al-Qila'i", "Gabriel Ibn al-Qilai". No text found. Assemani lists his works in BO I (lines 116455 to 126339 of the vendored file), in Latin catalogue form. |
| Debs, Summa confutationum (Beirut, 1871) | Maronite defence of orthodoxy, cited by Lamy | Not found on the host. |
| Maronite liturgical manuscripts and scribes' notes | The census says they are the era's voice | None on the host in a form the library can read. |
| Mamluk and Ottoman sources on the Kesrwan campaigns of 1305 | The census opens the window with them | Not searched in Arabic; none in a language the OCR can read. |

## 5. Open cross-world questions

- **The earlier Maronite world.** The census has a first Maronite entry (IV.10, c. 1100–1300). The sources for the two overlap almost completely (Assemani, Duwayhi, the Roman records). Whether the line is built as one world or two is the question this dossier's recommendation turns on.
- **The Latin papal church.** Lateran V and the Nicosia constitutions are in the Latin papal church's volumes (V.14). The proposed rows add this world to Mansi 32 and Mansi 26. How the union story is divided between the two worlds is open.
- **The Church of the East in Cyprus.** The 1445 bull received the Cypriot Chaldaeans (called Nestorians before) along with the Maronites. The Church of the East worlds may claim the same bull. Nothing in the library says where the Cypriot Chaldaeans sit in the Atlas.
- **Armenian Cyprus.** The Nicosia attendance list names an Armenian bishop. The Armenian-after-the-kingdom world (V.21) shares the island.
- **The union claim.** The census says the Maronites hold they were never out of communion with Rome. The Roman documents here record a reception in 1445 and a letter of obedience in 1516. The two readings are both part of the world's story. A Doc_01 must say how it treats the claim.
- **The date.** The 1445 date (7 August) comes from Assemani's text in the shelf file, a second witness, not from the Raynaldus extract. Doc_02 should check the date against the bull's own closing line.

## 6. Step 0 scope notes and recommendation

**Floor (A1).** The census says the dispute is about early history, not present confession. Nothing found changes that. The bull of 1445 forbids calling the Cypriot Chaldaeans and Maronites heretics (Assemani's summary at lines 29210–29216 of the shelf file). That is Rome's statement about their standing, not a statement of belief. Lamy's note and Michael the Syrian give the Syriac Orthodox side of the older dispute.

**Sourcing (B1).** The census says "thin to moderate, much from the Roman side", and that holds. The Maronites speak directly in only a few places: Patriarch Peter's letter to Leo X (in a Latin version in the shelf's Mansi 32), the professions sent by the bishop Elias and the metropolitan Timothy to Eugenius IV (as Raynaldus and Assemani report them), and the bishops named at Nicosia. Duwayhi's own history is a locator at best. There is no public-domain English for any of them.

**Ecology (B2).** One side only is on the page: Rome. The union is told from its receiving end. The risk the sources show is a Representative who recites the Roman record as the church's own memory.

**Uniqueness (B3).** Against the earlier Maronite world the overlap is almost total in sources. Against the Latin papal church it is the council record. Against the Church of the East it is the Cyprus bull. Each is a boundary to state.

**Audiences (B4).** The Maronite church is the largest Christian body in Lebanon and has a worldwide diaspora, so the audience is large and reachable.

**Scale (B5).** About 8.0 MB vendored in three files, of which the Raynaldus volume is 4.0 MB. Three placements in this world's staged rows. Five cross-link rows are proposed on shelf files (Mansi 32, Mansi 26, Assemani III.2, Barhebraeus, Michael the Syrian).

**Recommendation: part of another world.** In this window the Maronites speak in one patriarch's letter, two envoys' professions and a list of bishops at a council, all through Latin, and the library holds no public-domain English for any of them. The first Maronite entry (IV.10) rests on the same few sources and the same Roman documents. One Maronite world across both windows would give a Representative a longer record to draw on than a third thin world. If the lead does not build the earlier entry, this one should stay atlas only. This is a recommendation for Mark to weigh, not a decision.
