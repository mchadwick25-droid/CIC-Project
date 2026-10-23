# Source Readiness Dossier — Philippine Catholicism

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is.

**Second pass, October 2026 (Era VII library session, second-pass agent):** nothing was vendored for this world. The two leads the pass was told to weigh were run down: Blair and Robertson vol. XXXV was fetched and its contents table read, and it carries no convert voice (Dominican, Recollect and Franciscan mission extracts, royal decrees, a Mercedarian's report), so it is closed (§4); Colin's tomos II and III stay a low-priority lead for size. A search for a Filipino-authored text in the window (Tomas Pinpin's Librong of 1610, Blancas de San Jose) found nothing on archive.org, and Google Books could not be queried (API quota exceeded, site errors). The renewal check §4 said was not run is now run: the NYPL cce-renewals data for 1974, 1975 and 1976 holds no renewal for the 1947 Doctrina facsimile (details in §4). The recommendation in §6 does not change.

**Atlas ID:** VI.19
**Corpus-map slug:** `philippine-catholicism` (census continues as `philippine-catholicism-era-8`, 1650-1815, then `philippine-catholicism-gomburza-to-aglipay`, 1815-1906)
**Time window:** 1565-1650
**Region(s):** Philippines (Greater Asia)
**Dossier author / date:** source-research thread, one-world library agent, October 2026; finished October 2026 after a usage-limit stop
**Corpus-map / `cic/texts/` state as of:** October 2026. No `cic/corpus-map/philippine-catholicism.yaml` bucket exists yet. Ten files are vendored and staged in `cic/corpus-map/_staging/` (see §1); they await the lead's registry and staging merge.

## 1. Already assigned

Nothing was merged before this pass. The ten files below were vendored and staged on October 2026. The "scale" column is the body word count of the vendored file.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Doctrina Christiana, Manila 1593 (Library of Congress facsimile of 1947, Wolf's essay, Gutenberg transcription) | doctrina-christiana | tradition | assigned | ~30,000 words, proofread, clean | `doctrina-christiana_manila-1593-tgl-spa_wolf1947.txt` |
| The Philippine Islands, Vol. VII (Plasencia, Customs of the Tagalogs, 1589; Salazar) | blair-robertson | tradition | assigned | ~87,000 words, clean | `blair-robertson_philippine-islands-v07_1903.txt` |
| The Philippine Islands, Vol. XII (Chirino's Relacion, first part; documents 1601-1603) | chirino | tradition | assigned | ~88,000 words, clean | `blair-robertson_philippine-islands-v12_1904.txt` |
| The Philippine Islands, Vol. XIII (Chirino's Relacion, concluded; documents 1604-1605) | chirino | tradition | assigned | ~87,000 words, clean | `blair-robertson_philippine-islands-v13_1904.txt` |
| The Philippine Islands, Vol. XXXIV (Augustinian, Franciscan, Dominican and Jesuit letters 1565-1605; Salazar's council and cathedral) | blair-robertson | tradition | assigned | ~118,000 words, clean (Pigafetta Italian opens the volume) | `blair-robertson_philippine-islands-v34_1906.txt` |
| Morga, Sucesos, English (Blair and Robertson 1907, both volumes) | morga | context | assigned | ~152,000 words, clean | `morga_sucesos-islas-filipinas_blair-robertson1907.txt` |
| Morga, Sucesos, Spanish (Rizal 1890) | morga | context | assigned | ~150,000 words, clean OCR | `morga_sucesos-islas-filipinas-spa_rizal1890.txt` |
| Chirino, Relacion de las Islas Filipinas, Spanish (Manila 1890) | chirino | tradition | assigned | ~89,000 words, readable OCR with page-boundary noise | `chirino_relacion-islas-filipinas-spa_manila1890.txt` |
| Colin, Labor evangelica, Tomo I (Pastells 1900) | colin | tradition | assigned | ~839,000 words; about half is the whole work's index | `colin_labor-evangelica-t1-spa_pastells1900.txt` |
| Aquino de Belen, Tagalog prayers for the dying and verse Passion (Manila 1760) | aquino-de-belen | tradition (to the Era-8 entry) | assigned there; context, needs-ruling, here | ~33,000 words, garbled OCR, second witness | `aquino-de-belen_pasyon-and-manga-panalangin-tgl_manila1760.txt` |

Also staged beyond this world: Chirino (both languages) and Colin to `the-society-of-jesus` (VI.11) as tradition; all Philippine files except the Doctrina's Spanish-only rows to `mission-born-christianities-kirishitan-japan-kon` (VI.13) as provisional context; Rizal's Morga to `philippine-catholicism-gomburza-to-aglipay` as provisional context; the Belen pasyon to `philippine-catholicism-era-8` as tradition. The staging files pass `corpus_map_merge.py --check`.

What the corpus now holds, stated plainly. The Doctrina is the only text here in the converts' language, and the friars made it. Everything else is a missionary or an official writing about the converts. No Filipino convert, catechist or confraternity member speaks in a window-period document in the corpus. The census says this itself (Chirino is "written by the missionaries themselves, not the converts").

Rights notes. The B&R volumes and Morga English are Gutenberg transcriptions of 1903-1907 printings: public domain by date, with Gutenberg's own declaration. The Doctrina is the 1947 Library of Congress facsimile edition: the 1593 text is public domain by date, but the 1947 essay and notes could not be renewal-checked (the NYPL `cce-renewals` data was not reachable: the paths tried returned 404 and the GitHub API was refused). The Gutenberg declaration and the Library of Congress statement are the recorded basis. The registry trailer limits republication of that file to passages.

## 2. Cross-link opportunities

Checked October 2026 by searching the vendored corpus for "Philippin", "Manila", "Tagalog", "Luzon", "Legazpi" and opening the hits.

- **Institutum Societatis Iesu, vol. 1 (1892).** `society-of-jesus_institutum-societatis-iesu-v1-lat_1892.txt`, lines 51400, 53788, 53892 name the Philippines and Manila. Lives in the Society of Jesus bucket. Tier: same time-different-region. Matching lines only were read. A provisional row is in `crosslink_fragment.yaml`.
- **Francis Xavier, Life and Letters (Coleridge 1872), vol. 1.** Lines 19818 to 22816 mention the Philippines as geography around the Moluccas mission. Passing references, no row proposed. Tier: same time-different-region.
- **Trigault, De Christiana expeditione apud Sinas (1615).** Passing mentions of the Philippines at lines 934, 7382, 9464, 9469. Second witness already; no row.
- **Council of Trent canons (Waterworth).** The friars worked under Trent's rules, but no text in the Philippine files was checked against it. Named only as a likely link to `the-tridentine-church` (VI.22); no row.
- Not relevant: hits on "Manila" in Augustine, Alcuin and Theodosian files are Latin words ("manilla" forms), not the city. The hits for "Cebu" in `society-of-jesus_monumenta-paedagogica-lat-spa_1901.txt` were not opened and are probably a word-form match; flagged for a later pass, not claimed.

## 3. Verified acquisition leads

Each row was checked on archive.org or Gutenberg by metadata fetch. Vendored rows are in §1. Rows below are not vendored.

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| Labor evangelica, Tomos II and III (Pastells ed.) | Francisco Colin, S.J. | none (Spanish) | 1900 | archive.org `laborevangelicam02coli`, `laborevangelicam03coli` | pd-us-by-date (1900 imprint; no host rights field). Google scans of the same edition `laborevangelica00pastgoog` and `laborevangelica00chirgoog` are NOT_IN_COPYRIGHT | metadata fetched; Tomo I opened and sampled; II and III not opened, October 2026. Not vendored for scale (about 4.5M to 5.4M characters each). Second pass, October 2026: left as a low-priority lead for the same reason; a build on 1616 onward may want them. |
| The Philippine Islands, Vols. XXIII-XXIV (Medina, Augustinian history, 1630) | Juan de Medina, O.S.A. | Blair and Robertson | 1905 | gutenberg #16451, #18102 | pd-us-by-date; Gutenberg declaration | files fetched, contents tables read, October 2026. Not vendored: the Augustinian chronicle is the best remaining inside voice for the Augustinians; a build may want it. |
| The Philippine Islands, Vol. XXXV (Dominican, Recollect and early Franciscan missions) | Santa Cruz, Juan de la Concepcion, others | Blair and Robertson | 1906 | gutenberg #45101 | pd-us-by-date; Gutenberg declaration | file fetched, contents table read, October 2026. Not vendored. Second pass, October 2026: fetched again and the contents read in full; closed in §4 (no convert voice). |
| The Philippine Islands, Vols. XXX-XXXII (Aduarte, Dominican history) | Diego Aduarte, O.P. | Blair and Robertson | 1906 | archive.org `thephilippineisl39054gut`, `thephilippineisl42399gut`, `thephilippineisl42458gut` | NOT_IN_COPYRIGHT (host field) | metadata only, October 2026. Not vendored. |
| Chronicas de la apostolica Provincia de S. Gregorio (Franciscans) | Juan Francisco de San Antonio, O.F.M. | none (Spanish) | 1738 | archive.org `chronicasdelaapo00sana` (also `_0`, `_1`) | pd-us-by-date (1738 imprint) | OCR sampled at five points: long s read as f, second witness only, October 2026. Not vendored. |
| Sucesos de las Islas Filipinas (Retana 1909) | Antonio de Morga | W. E. Retana (ed.) | 1909 | archive.org `sucesosdelasisla00morg_0` | pd-us-by-date (1909 imprint) | five-point sample readable, October 2026. Not vendored: Rizal 1890 is the clean Spanish already in. |
| Sucesos de las islas Filipinas (Mexico 1609, original print) | Antonio de Morga | none | 1609 | archive.org `sucesosdelasisla00morg` (John Carter Brown Library) | pd-us-by-date | metadata only, October 2026. Not vendored. |
| Historia de la Provincia de Philipinas de la Compania de Jesus, segunda parte | Pedro Murillo Velarde, S.J. | none (Spanish) | 1749 | archive.org `historiadelaprov00muri` | pd-us-by-date | metadata only, October 2026. Out of window in composition; not vendored. |
| La primera imprenta en Filipinas (with Tomas Pinpin material) | Manuel Artigas y Cuerva | none | 1910 | archive.org `apz3238.0001.001.umich.edu`, `adr6689.0001.001.umich.edu` | pd-us-by-date (1910 imprint) | metadata only, October 2026. Not vendored: scholarship on the first press with printed appendices. |
| Vocabulario de la lengua tagala | Juan de Noceda and Pedro de Sanlucar | none | 1860 reprint of 1754 | archive.org `vocabulariodela00sanlgoog` | NOT_IN_COPYRIGHT (host field) | metadata only, October 2026. A dictionary, not a voice; not vendored. |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Earliest pasyon text (Aquino de Belen, 1704) | The census names the pasyon as the world's inside voice | The earliest surviving text is 1704, after the window (the census says so). The only copy found is the 1760 Manila print (`magapanalagingpa00vill`), vendored as a second witness for the Era-8 entry. No 1704 scan found on archive.org (searches on "pasion", "pasyon", "Belen", "tagalog"). |
| Blancas de San Jose, Memorial de la vida cristiana (1605) | Named in the brief as a Tagalog catechetical text | archive.org search on "blancas" returned only unrelated items (court records, a Spanish chronicle of Aragon). No scan found, October 2026. |
| Plasencia's Spanish originals and his Doctrina | The census names Plasencia as a catechism author | Plasencia survives here only in B&R's English (Vol. VII, and the Pampangas appendix in Vol. XVI). archive.org search on "plasencia" with Tagalog/Filipinas terms found only Paterno's *Los Tagalog* (1894, scholarship). No Spanish manuscript edition found. |
| Ribadeneira, Historia de las islas del archipielago filipino (1601) | Named in the brief | The only scan found (`historiadelasisl00riba`) is the Madrid 1947 transcription of the 1601 print. A 1947 Spanish publication is foreign and post-1930, so in copyright; also, access rights not checked further. Not vendorable. The 1601 print was not found on archive.org. |
| Blair and Robertson, Vol. XV and XVI separately | Morga's Sucesos sits in series vols. XV-XVI | The Gutenberg item for vol. 15 did not appear in the search lists; the separate 1907 Morga issue (gutenberg #7001) carries the same text and was vendored instead. The Plasencia Pampangas appendix of vol. XVI is not in that issue; Gutenberg #15157 holds it and is a lead, unvendored. |
| Phelan, *The Hispanization of the Philippines* (1959); Rafael, *Contracting Colonialism* (1988) | Census secondary sources | In copyright by date (1959, 1988); not sought on any host. Scholarship, not a source for the library. |
| NYPL cce-renewals renewal check for the 1947 Doctrina facsimile | Required by INTAKE for 1931-1963 US publications | Not run in the first pass: `raw.githubusercontent.com/NYPL/cce-renewals/master/data/<year>.tsv` and four other path guesses returned 404, the GitHub API refused the session, and the repository tree page returned an empty page. **Run in the second pass, October 2026:** the files are at `data/<year>-1.tsv` on the `master` branch (`main` does not exist; the tree page, the API and codeload all answer 403, so the layout was found by trial). `1974-1.tsv` (8,719 rows, registrations of 1946-1947), `1975-1.tsv` (8,379 rows, 1947-1948) and `1976-1.tsv` (8,455 rows, 1948-1949) were searched in title, author and full text for "Doctrina Christiana", "Wolf, Edwin" and "first book printed in the Philippines": no renewal. A 1947 registration had to be renewed in its 28th year, which these files cover. The registry trailer's passages-only limit can be lifted if the lead accepts this check; a note is proposed in the second-pass agent's `registry_append_fragment.yaml`. |
| Blair and Robertson, Vol. XXXV (1640-1649), gutenberg #45101 (**second pass**) | The brief asked for it only if it carries a convert voice | Contents read in full: Santa Cruz's Dominican history (1635-39), Recollect mission extracts (1625-40), unsigned news of 1640-44, royal decrees of Felipe IV, Juan de los Angeles on the loss of Formosa, Jesuit concessions, a fiscal's report on Sangley licences, the erection of Santo Tomas as a university, Fray Joseph Fayol's report of 1647, and an unsigned Franciscan account of 1649. Every document is a missionary's or an official's. No convert voice. Closed for that purpose; it remains a public-domain volume for the 1640s if a build wants the decade. |
| A Filipino-authored text in the window: Tomas Pinpin, Librong pagaaralan nang manga Tagalog nang uicang Castila (Manila, 1610); Blancas de San Jose's Tagalog works (**second pass**) | The one printed book by a Filipino in the window would be the convert voice §6 lacks | archive.org searches for "pinpin", "librong tagalog" and "blancas tagala" return nothing of either (only Mentrida's 1630 Ritual, `ritualparaadmini00ment`, a Spanish friar's book). Google Books could not be queried this pass (API 429 quota exceeded; books.google.com 500 and redirect). Artigas y Cuerva's 1910 La primera imprenta en Filipinas (§3) is the printed lead for Pinpin material and was not opened. Not found; stays open. |
| Gutendex lookup of B&R volumes | A quick listing of all 55 volumes | gutendex.com is blocked by the proxy (403). The volumes were listed through the archive.org mirror search instead. |
| Confraternity (cofradia) records and a convert-voiced document in the window | Census sourcing line | None found in any host searched. Not a gap this pass can close; see §6. |

## 5. Open cross-world questions

- **VI.11 Society of Jesus.** Chirino and Colin are placed there as tradition. The Jesuit world's thread decides how much weight a mission account from Asia carries beside the Society's founding corpus.
- **VI.13 Mission-born Christianities.** All Philippine files carry provisional context rows to the mission-born entry. Whether the Philippines belong inside that entry or stand alone is a mapping decision this dossier does not make.
- **The Belen pasyon file.** It is placed as tradition for the Era-8 entry and as context (needs-ruling) here, because it is dated after the window. A ruling is needed on whether a later print may stand as context for the earlier entry.
- **Morga and Rizal.** Rizal's 1890 notes belong to the Gomburza-to-Aglipay entry's concerns. The staging file gives that entry a provisional context row. The Spanish text itself serves this window.
- **Doctrina republication limit.** If a ruling prefers whole-text republication, the renewal check in §4 must run first.
- **Etic limit.** Every inside voice here is a missionary or an official. The converts speak only through the friars' Tagalog (the Doctrina) and, later, the pasyon.

## 6. Step 0 scope notes and recommendation

**Floor question (A1).** The census floorNote reads "No question". Nothing in the Doctrina, Chirino or Plasencia raises one: the Doctrina gives the Pater noster, Credo, commandments and sacraments in Spanish and Tagalog.

**Uniqueness and overlap (B3).** Spanish colonial Catholicism is the parent, and the nearest sibling entries are the Tridentine Church (VI.22), the Society of Jesus (VI.11) and Mission-born Christianities (VI.13). The Philippines add something none of them tells: a mission church whose first book was a vernacular catechism in the converts' own script, and a lay devotional form (the pasyon) that grew from it. The overlap is in the sources (the friars' orders), not in the formation story.

**Sourcing (B1) and ecology (B2).** The library now holds a catechism (30,000 words), about 300,000 words of English mission documents (B&R VII, XII, XIII, XXXIV), Morga in both languages, Chirino in both languages, and Colin's Tomo I in Spanish only. This is a strong outside-and-institutional base: the friars writing about the converts, and a colonial judge. It has no convert voice, no confraternity record and no pasyon in the window. The census predicted exactly this limit. The strongest inside genre it names (the pasyon) falls after 1650 and the one print in hand is a garbled second witness. A Doc_02 would state the missing convert voice as an absence, not fill it.

**Scale (B5) and audiences (B4).** About 1.5 million words in English and Spanish, with real depth in the 1580s to 1610s, thin for 1620 to 1650 except in unvendored B&R volumes (XXIII-XXV, XXXV) and Colin's later tomos. The window is long (85 years) but the sources cluster around two decades. Not tested here: audience demand, left to Step 0.

**Recommendation, for Mark to decide, not a decision: build, with the convert-voice limit stated up front.** The floor clears, the Doctrina is a genuine native-language primary text, and the mission documents are rich and clean. The thin spot is honest and nameable. If Mark judges that a world without any convert-authored text should wait for the 1704 pasyon, the fallback is **part of another world**: fold this window into `philippine-catholicism-era-8` as its first segment. The coordinator should note this choice turns on whether the Doctrina (a friars' translation) counts as enough inside voice.

**Second pass, October 2026: the recommendation is unchanged.** The pass vendored nothing: the one further volume weighed (Blair and Robertson XXXV) has no convert voice, and the one Filipino-authored print of the window (Pinpin, 1610) was not found on any reachable host. The renewal check on the 1947 Doctrina facsimile found no renewal (§4), which strengthens the Doctrina's standing as the world's one native-language primary text.
