# Source Readiness Dossier — Mission-Born Christianities (Kirishitan Japan; Kongo; China; New Spain/Andes)

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is.

**Atlas ID:** VI.13
**Corpus-map slug:** `mission-born-christianities-kirishitan-japan-kon` (the census id is truncated at this length; it is the real bucket filename)
**Time window:** 1491–1650
**Region(s):** Japan; Kongo; China; New Spain and the Andes (census regions: Africa, Greater Asia)
**Dossier author / date:** source-research thread, Era VII session, VI.13 world agent, October 2026
**Corpus-map / `cic/texts/` state as of:** October 2026, branch `library/era-vii-2026-10`, before the lead merges this agent's registry, seed and cross-link fragments. The six §3 vendored files and their staging files are in place; their registry entries and the cross-link rows are in the fragments the lead merges.

This world is four regions. The dossier keeps them apart. Each region is scored on its own in §6, because the census's own floor question (whose story survives, the mission's or the converts') has a different answer in each.

## 1. Already assigned

Before this pass the bucket held one work.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| De Christiana expeditione apud Sinas (Trigault, from Ricci), Latin 1615 | trigault | context | provisional | one volume, five books; OCR garbled (long s as f, lost spaces), second witness only | `trigault_de-christiana-expeditione-apud-sinas-lat_1615.txt` |

Vendored this pass and assigned in `cic/corpus-map/_staging/` (one staging file per volume):

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Letters, charters and inquests of D. Afonso I of Kongo, 1512–1540s (Portuguese) | afonso-i-of-kongo (metadata-omission ruling) | tradition | assigned | some forty documents inside a 1.0 MB volume | `paiva-manso_historia-do-congo-documentos-por_1877.txt` |
| Historia do Congo (Documentos), the whole corpo diplomatico 1492 onward | paiva-manso | context | assigned | 1.0 MB, Portuguese with some Latin | same file |
| Annexes: letters of Japanese Christians 1598–1651, in French translation | pages | tradition | assigned | a dozen or more letters inside a 1.1 MB volume | `pages_histoire-religion-chretienne-japon-annexes-fra_1870.txt` |
| Annexes: missionary, episcopal, papal and royal documents on Japan 1598–1651 | pages | context | assigned | the rest of the same 1.1 MB volume | same file |
| Memorials of the Empire of Japon: 'The Kingdome of Japonia' and the letters of William Adams | rundall | context | assigned | 0.5 MB, English | `rundall_memorials-of-the-empire-of-japon_1850.txt` |
| The Jesuit China mission in English: Purchas's 1625 Trigault/Ricci and Pantoja's 1602 letter (Chapters V–VIII) | purchas | context | assigned | about 0.7 MB of a 1.6 MB volume | `purchas_hakluytus-posthumus-pilgrimes-v12_1906.txt` |
| The Natural and Moral History of the Indies, Vol. II (Books V–VII), Grimston's English | acosta | context | assigned | 0.6 MB, English | `acosta_natural-and-moral-history-of-the-indies-v2_grimston-markham1880.txt` |
| Historia de los indios de la Nueva España (Spanish) | motolinia | context | assigned | 0.85 MB, Spanish | `motolinia_historia-de-los-indios-de-la-nueva-espana-spa_sanchez-garcia1914.txt` |

Non-exclusive placements made at the same time: Afonso's letters also to `the-antonian-movement-in-kongo` (antecedent, provisional); the Pagès Jesuit letters, Purchas Chapters V–VIII and Acosta also to `the-society-of-jesus` (context); Purchas Chap. III to `philippine-catholicism` (context, provisional, placed on the Table of contents only); Acosta Book V and Motolinía to `colonial-latin-american-devotional-catholicism` (antecedent, provisional).

What kind of witness each is: Afonso's letters are a convert voice (the Kongo court writing in Portuguese). The Pagès letters are a convert voice two steps removed (Japanese Christians in Pagès's French from the missionaries' Portuguese and Spanish). Everything else is the mission's or an outsider's pen.

## 2. Cross-link opportunities

Run against the whole corpus by the `Title:`/`Creator:` header lines, then by reading the relevant parts. Rows proposed in `crosslink_fragment.yaml` for the lead to add to the existing staging files.

- **Xavier, Life and Letters, Vol. II (Coleridge 1872)**, now only in `the-society-of-jesus`. Book V (file line 13181) is the Japan mission 1549–1552 in Xavier's own letters, Book VI the China plan. Tier: same time-place. Proposed row: context, assigned.
- **Monumenta Xaveriana, Tomus I (1899–1900)**, now only in `the-society-of-jesus`. The Japan letters in the languages written (the letter dated Cangoxima 3 November 1549 at file line 29054 and those after it; Valignano's Life on Japan at line 5424). Tier: same time-place. Proposed row: context, assigned.
- **Trigault, De Christiana expeditione (Latin 1615)**: already assigned here as a second witness. The Purchas volume vendored this pass is its English counterpart; the lead may add that to the existing row's note.
- **Jesuit Relations (Thwaites), vols. 1–35**: New France, 1610–1650. Same time, a different region that this census entry does not name (its regions are Japan, Kongo, China, Americas, and the Jesuit Relations belong to the New France mission). Not linked. If Mark widens 'Americas' beyond New Spain and the Andes, these 35 volumes become the largest single block of mission-era primary material in the corpus.
- **Polanco, Chronicon, vols. 1–6; Lainez, Nadal, Borgia letters**: the Society's generalate records 1539–1572 carry news from the Japan, India and Brazil missions. Tier: same time-different-region. Not read for this world this pass; no row proposed.
- Nothing in the corpus touches Kongo, New Spain or the Andes apart from the files vendored this pass.

## 3. Verified acquisition leads

All vendored this pass (see §1); each checked on archive.org by the metadata API and a direct fetch of the OCR, October 2026.

| title | author | translator/ed. | year | url | rights basis | verified by |
|---|---|---|---|---|---|---|
| Historia do Congo (Documentos) | Paiva Manso (comp.); Afonso I of Kongo and others | none (Portuguese) | 1877 | archive.org `historiadocongod00jorduoft` | pd-us-by-date; NOT_IN_COPYRIGHT | metadata API and direct fetch; Afonso's letters located by heading (file lines 441, 584 onward); OCR clean. Vendored. |
| Memorials of the Empire of Japon | Rundall (ed.); Adams | English | 1850 | archive.org `memorialsofempir00rundrich` | pd-us-by-date; NOT_IN_COPYRIGHT | metadata API and direct fetch; OCR clean. Vendored. |
| Histoire de la religion chrétienne au Japon, seconde partie: Annexes | Pagès | Pagès (French) | 1870 | archive.org `histoiredelarel01paggoog` | pd-us-by-date; NOT_IN_COPYRIGHT; Google notice | metadata API and direct fetch; identified as the Annexes volume from the scan's half-title; letters of Japanese Christians located by heading. Vendored. |
| Purchas His Pilgrimes, Vol. XII | Purchas | Purchas's 1625 English of Trigault and Pantoja | 1906 | archive.org `hakluytusposthum12purc` | pd-us-by-date (no status field; year from the title page MCMVI) | metadata API and direct fetch; China chapters located (file lines 13995–end). Vendored. |
| Natural and Moral History of the Indies, Vol. II | Acosta | Grimston 1604; Markham | 1880 | archive.org `naturalmoralhist61acosrich` | pd-us-by-date; NOT_IN_COPYRIGHT | metadata API and direct fetch; OCR clean. Vendored. |
| Historia de los indios de la Nueva España | Motolinía | none (Spanish); Sánchez García | 1914 | archive.org `historiadelosind00moto` | pd-us-by-date; NOT_IN_COPYRIGHT | metadata API and direct fetch; language field 'eng' is a catalogue error. Vendored. |

Verified and not vendored (rows in `seed_fragment.yaml` as `not-yet-downloaded`, with the reason): Acosta Vol. I (`naturalmoralhist60acosrich`, 1880); Cocks's Diary 1615–1622, 2 vols. (`diaryrichardcoc00unkngoog`, 1883; also Gutenberg #46803 and #48012); Semedo's History of China (`historyofthatgre00seme`, 1655, long-s OCR); Crasset's History of the Church of Japan in the 1705 English (`bim_eighteenth-century_the-history-of-the-churc_crasset-jean_1705_1` and `_2`); Sahagún's Historia general, Bustamante edition 1829, 3 vols. (`historiagenerald01saha` and sisters); the Third Lima Council's Doctrina christiana 1584 (`doctrinachristia00cath`, OCR garbled past use); Pagès's Lettres de Saint François-Xavier (`lettresdesaintf00xavigoog`, 1855, French, not needed beside the Coleridge and Monumenta files).

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Ricci, Tianzhu shiyi (Chinese) | The census's own China source; Ricci's Chinese catechism | Three scans on archive.org: `JapSin-1-44` (ARSI, 1607 print) carries a CC BY-NC-ND 3.0 licence, which the library does not accept; `02099353.cn` and `02099354.cn` (Universal Library) carry no rights statement and 24–28 KB of OCR per volume, so no usable text. Chinese Wikisource was rate-limited (HTTP 429) through most of this pass; its one answered search for the title returned nothing, and a search for Ricci returned only Aleni's 1630 life of Ricci and the anti-Christian Pixie lun. Lead, not a download. |
| Ricci's letters, Tacchi Venturi, Opere storiche (Italian, 1911–13) | Named in the task brief | archive.org creator search for Tacchi Venturi returns only his Storia della Compagnia di Gesù in Italia and a 1900 pamphlet; no scan of the Opere storiche found. The 1622 Italian Entrata nella China (`entratanellachin00ricc`) is the Trigault text in Italian, not Ricci's own letters. Not found. |
| Xu Guangqi, Yang Tingyun, Li Jiubiao's Kouduo richao (the converts' own Chinese texts) | The census lists them first for China | No scan or transcription found on the reachable hosts; Chinese Wikisource searches for Xu Guangqi's Bianxue zhangshu and for Yang Tingyun were refused (429). Kouduo richao exists in English only in Zürcher 2007 (in copyright). Closed for this pass as not found; the Wikisource searches should be re-run from a session that is not rate-limited. |
| Semedo, History of China, 1655 English | Named in the task brief | Verified public domain (`historyofthatgre00seme`), but a 1655 long-s scan and a second Jesuit narrative where Purchas already carries Trigault. Left as a verified lead. |
| Fróis, Historia de Japam; Fróis's 1597 martyr relation in English | The Jesuit eyewitness to the Kirishitan church | Historia de Japam exists only in the 1976–84 Lisbon edition (in copyright); creator search for Fróis on archive.org returns nothing of his. No 1894 English of the 1597 relation found under 'japan martyrs' (only Wilberforce's 1897 Dominican Missions and Martyrs in Japan, a secondary work). The 1597 martyrs are reached instead through Pagès's Annexes and the Purchas Chap. V narrative. |
| Dochirina Kirishitan; Tenchi hajimari no koto; Fabian Fucan's Ha Daiusu and Myōtei mondō | The census's own Japanese-language sources | archive.org title searches return nothing but modern scholarship (Laures's Kirishitan Bunko 1951/1957, Kirishitan fudoki 1960, Oike 1925). Japanese Wikisource holds chapters of the Dochirina from Muraoka's 1926 Kirishitan bungaku shō (public domain by date): chapter 7 was fetched (page rev 220402) and is a real transcription, but with furigana the contributor added; chapter 6 and the Ha Daiusu, Tenchi and Myōtei searches were refused (429). The NDL scan of the 1926 book (dl.ndl.go.jp) is blocked from this sandbox. Recorded as a lead that waits on a ruling (seed row), not closed. |
| Rundall 1850 and Cocks 1883 | Named in the task brief | Rundall vendored; Cocks verified and left (two large volumes of a trader's day-book). |
| Guaman Poma, Nueva corónica (1615) | The census's native Andean Christian voice | The 1936 Paris facsimile is a 1936 foreign publication (record only, and not found on archive.org). The archive.org items (`primer-nueva-coronica-y-buen-gobierno-vol-1-1615`, `nueva-coronica-y-buen-gobierno-1`, the 1980 Tomo I/II OCR items) are modern uploads of unknown provenance, the last a 1980 edition in copyright. Spanish Wikisource has a chapter transcription (index page rev 1665657, marked incomplete) whose conventions match the Royal Danish Library's 2001 Adorno–Murra online edition; kb.dk is blocked (CONNECT 403), so its terms could not be read, and the Wikisource pages carry no licence template. Lead that waits on a ruling, not vendored. |
| Huarochirí manuscript (Quechua) | Census source | Trimborn 1939 is a 1939 foreign publication; Salomon and Urioste 1991 in copyright. Not searched further; nothing public domain exists. |
| Nahuatl testaments (Testaments of Culhuacan) | Census source | 1976 edition in copyright; no earlier printing. Closed. |
| Sahagún, Florentine Codex | The Nahuatl voice behind the Historia general | archive.org items `florentine-codex-vol1`–`vol3` and `florentine-codex` are modern uploads of the manuscript facsimile with no public-domain text; Anderson and Dibble's English (1950–82) is in copyright. The Bustamante 1829 Spanish is verified (seed row) but not vendored. |
| Mendieta, Historia eclesiástica indiana | Named in the task brief | archive.org creator search for Mendieta (1800–1930) returns only unrelated Mendietas (Salvador, Lucio). The 1870 García Icazbalceta edition was not found by this search. Not found; a title search on another host may do better. |
| Arriaga, Extirpación de la idolatría del Pirú (1621) | Hostile evidence the census names | Two JCB scans of the 1621 print (`extirpaciondelai00arri`, `01arri`); a 1621 Spanish print whose OCR was not sampled this pass because the Lima 1584 catechism scan of the same press family proved unusable. Keith 1968 English in copyright. Lead to sample, not closed. |
| Third Lima Council catechism 1584 | The Quechua and Aymara catechism | Verified (JCB and Princeton scans) but the trilingual 1584 OCR is noise at every sample point. Seed row; not vendored. |
| Kikongo Doutrina christãa 1624 | Census source | No scan found on archive.org (title search for 'doutrina christãa' returns only Brazilian catechisms). Not found. |
| Afonso I's letters in English | The one convert voice the census stresses | English excerpts exist only in modern readers (Brásio's Monumenta Missionaria Africana, 1952 onward, and later anthologies, all in copyright). No public-domain English. Gap, stated in the Paiva Manso header. |
| Motolinía in English (Foster 1950; Steck 1951) | Would pair the Spanish with an English | United States publications of 1950–51; the NYPL cce-renewals `data/<year>.tsv` paths returned nothing from raw.githubusercontent.com this pass (the files sit under another layout), so the renewal check was not completed. Gap recorded as 'no public-domain English settled'; a later pass should finish the renewal check. |
| Pagès, premiere partie: Texte (1869) | Companion to the vendored Annexes | Not on archive.org by title, creator or subject. Seed row with no URL. |

## 5. Open cross-world questions

- **One world or four?** The census entry bundles Japan, Kongo, China and New Spain/Andes. The sources pull apart: Kongo has a convert's own letters in one Portuguese volume; Japan has converts' letters in French translation and a large outside literature; China has only the mission's pen in public domain (Trigault/Purchas, Pantoja) with the converts' own Chinese texts unfound; New Spain/Andes has rich mission-pen narrative (Motolinía, Acosta, Sahagún) and the native voices (Guaman Poma, Florentine Codex, Huarochirí) locked behind modern editions or unsettled transcriptions. Passed to Mark undecided; §6 recommends.
- **The Society of Jesus (VI.11)** holds Xavier, Trigault, Acosta and the Pagès Jesuit letters as its own voice. This world holds them as context. Both buckets now carry them; whichever Doc_02 runs first should say who holds native register.
- **Philippine Catholicism (VI.19)**: Purchas Chap. III ('First discoverie of the Philippinas') placed provisionally; Morga's Sucesos in Stanley's 1868 English (`philippineisland00morg`, NOT_IN_COPYRIGHT) was seen in passing and is that world's own lead, not vendored here.
- **The Antonian Movement in Kongo (VI.1, 1704–1706)** and **Colonial Latin American Devotional Catholicism (c. 1600–1810)** receive antecedent rows from this pass; their own agents should confirm or drop them.
- **Later mission entries** in `ATLAS-TARGETS.md` (the Missionary Movement's Native Churches 1793–1906; Japanese Christianity, the Hidden Christians' Emergence 1865–1906; the Chinese Church 1920s–present) are the heirs of these strands. No text vendored this pass reaches their windows, so no rows were placed; the Hidden Christians entry is the one that will want the Dochirina and Tenchi leads when they clear.

## 6. Step 0 scope notes and recommendation

**Floor question (A1).** The census says there is no creedal question, and the sources agree: the Dochirina, the Lima catechism, Ricci's catechism and Afonso's letters are Catholic teaching and Catholic profession. The real question is the one the census names: whose story the record carries. Scored by region: Kongo, the convert's own voice survives (Afonso's letters, vendored); Japan, it survives in translation and in martyr acts (Pagès), with the Japanese-language texts in reach but not yet cleared; China, it does not survive in anything public domain found this pass; New Spain/Andes, it survives in native-authored texts that are all behind copyright or unsettled transcriptions.

**Sourcing (B1) and ecology (B2).** After this pass the world has eight assigned works in six new files, about 5.7 MB, in Portuguese, French, English and Spanish, plus the Latin Trigault and the Xavier cross-links. That is a workable base for Kongo and Japan and a mission-pen-only base for China and the Americas. The ecology is lopsided by design: three or four missionary and outsider witnesses for every convert text, which is the world's own historical shape and should be built as such, not hidden.

**Uniqueness (B3).** Each strand is unique on the Atlas for its window. But the four strands have no common actor, language or liturgy beyond the Catholic mission itself, and the Society of Jesus (VI.11) already owns the common actor. A single Representative would have to speak for a Kongo king, a Nagasaki catechist, a Chinese literatus and an Andean cacique at once, which no source supports.

**Audiences (B4).** Strong: the question of whose story survives is the question a modern participant brings to mission history. Each strand carries it in a different key.

**Scale (B5).** As one world: large and uneven, with two strands buildable now and two not. As four: Kongo is small and clean (one volume, one voice); Japan is medium and rich; China and the Americas are not yet buildable on public-domain convert sources.

**Recommendation (for Mark, not a decision):** **open question**, leaning to a split. Keep VI.13 as the census umbrella, but build it as separate worlds in sequence, Kongo first (smallest, cleanest convert voice, one Portuguese volume to read) and Japan second (convert letters in Pagès, outside witnesses in Rundall and Cocks, Japanese-language texts pending a ruling on the Wikisource transcriptions), while China and New Spain/Andes stay **atlas only** until a public-domain convert text clears (Ricci's Chinese catechism or a Xu Guangqi text for China; Guaman Poma's transcription for the Andes). The reasoning: B3 fails for a single world (no shared voice), B1 passes for two strands and fails for two, and A1's floor question has four different answers. If Mark rules for one world, the Representative should be a Facilitator-adjacent mission-era voice, not a convert, and the dossier's convert texts become its tensional evidence rather than its own speech.
