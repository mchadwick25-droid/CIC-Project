# Source Readiness Dossier — The Old Believers

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and why it
exists.

**Atlas ID:** VII.7
**Corpus-map slug:** `the-old-believers` (census id; matches `cic-website/data/world-census.json`'s own `id` field)
**Time window:** 1666–1815
**Region(s):** Russian north (Solovki, Pustozersk, Vyg), Moscow, Siberia; census `regions`: North Europe
**Dossier author / date:** first written by the obel library-stage source-research pass (Claude); refreshed and extended by Claude, Library thread, Era VIII source-research pass, 2026-10-23, at the project lead's direction that the two worlds with an existing Doc_02 (this one and the Methodist Revival) be brought to the same library standard as the rest of the era
**Corpus-map / `cic/texts/` state as of:** branch `library/era-viii-2026-10`, this pass. Before it the world had two Avvakum files (the Harrison-Mirrlees English of 1924 and an undated Wikisource transcription of the Life) and three antecedent rows (Stoglav, Domostroi). The Library pass added thirteen files.

## 1. Already assigned

Twenty-five works across eighteen vendored files in `cic/corpus-map/the-old-believers.yaml`.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| The monk Avraamii's Christianoopasnyi shchit very, petition and other writings (Materialy, vol. VII, 1885) | avraamii-inok | tradition | assigned | the works; Subbotin's introduction excluded | `avraamii-inok_khristianoopasnyi-shchit-very-materialy-v7-rus_subbotin1885.txt` |
| Avvakum's letters to Morozova and to his family, and his petitions from Pustozersk (in Barskov, 1912) | avvakum | tradition | assigned | documents 11, 12, 16, 18, 20, 22 and 23 | `barskov_pamiatniki-pervykh-let-russkogo-staroobriadchestva-rus_1912.txt` |
| Avvakum's petitions, epistles and letters (Materialy, vol. V, 1879) | avvakum | tradition | assigned | the numbered works; Subbotin's apparatus excluded | `avvakum_sochineniia-materialy-v5-rus_subbotin1879.txt` |
| Newly found works of Avvakum (Materialy, vol. VIII, 1887) | avvakum | tradition | assigned | section 1, the newly found works | `subbotin_materialy-dlia-istorii-raskola-v8-avvakum-zhitie-morozovoi-rus_1887.txt` |
| The Life of the Archpriest Avvakum by Himself | avvakum | tradition | assigned | whole work (Harrison and Mirrlees, 1924) | `avvakum_life-of-archpriest-avvakum_harrison-mirrlees1924.txt` |
| Zhitie protopopa Avvakuma, im samim napisannoe (first printed edition, Tikhonravov 1861) | avvakum | tradition | assigned | whole work | `avvakum_zhitie-rus_tikhonravov-kozhanchikov1861.txt` |
| Zhitie protopopa Avvakuma, im samim napisannoe (original-language text) | avvakum | tradition | assigned | whole work; Wikisource transcription | `avvakum_zhitie-protopopa-avvakuma-orv_wikisource-transcription-nd.txt` |
| The Solovki petition, interrogations and case papers (in Barskov, 1912) | barskov | context | assigned | documents 6-10, 24-26 and the rest | `barskov_pamiatniki-pervykh-let-russkogo-staroobriadchestva-rus_1912.txt` |
| Russian Dissenters (Conybeare, 1921) | conybeare | context | assigned | Book I, the Old Believers | `conybeare_russian-dissenters_1921.txt` |
| Pomorskie otvety, the answers of the Vyg community to the Synod's questions (1723) | denisov-andrei | tradition | assigned | the preface and the numbered answers | `denisov-andrei_pomorskie-otvety-rus_1911.txt` |
| Domostroi (Yakovlev 1867) | domostroi | antecedent | provisional | the Domostroi text | `domostroi_domostroi-rus_yakovlev1867.txt` |
| Deacon Fyodor Ivanov's writings (Materialy, vol. VI, 1881) | fedor-ivanov-diakon | tradition | assigned | the works; Subbotin's introduction excluded | `fedor-ivanov-diakon_sochineniia-materialy-v6-rus_subbotin1881.txt` |
| Istoriia Vygovskoi staroobriadcheskoi pustyni (Ivan Filippov, to c. 1744) | filippov-ivan | tradition | assigned | whole work | `filippov-ivan_istoriia-vygovskoi-staroobriadcheskoi-pustyni-rus_kozhanchikov1862.txt` |
| The priest Lazar's petition and writings (in Materialy, vol. IV, 1878) | lazar-romanov | tradition | assigned | Lazar's works under his name | `subbotin_materialy-dlia-istorii-raskola-v4-chelobitnye-rus_1878.txt` |
| Boyarynia Feodosia Morozova's letters to Avvakum and his family (in Barskov, 1912) | morozova | tradition | assigned | documents 13, 14, 15 and 19 | `barskov_pamiatniki-pervykh-let-russkogo-staroobriadchestva-rus_1912.txt` |
| The Life of Boyarynia Feodosia Morozova (anonymous; in Materialy, vol. VIII, 1887) | morozova-zhitie | tradition | assigned | the Life under its own title | `subbotin_materialy-dlia-istorii-raskola-v8-avvakum-zhitie-morozovoi-rus_1887.txt` |
| Ivan Neronov's letters and petitions (in Materialy, vol. II, 1875) | neronov | tradition | assigned | the Neronov documents | `subbotin_materialy-dlia-istorii-raskola-v2-dokumenty-rus_1875.txt` |
| Nikita Dobrynin's petition to Tsar Alexei (in Materialy, vol. IV, 1878) | nikita-dobrynin | tradition | assigned | Nikita's petition | `subbotin_materialy-dlia-istorii-raskola-v4-chelobitnye-rus_1878.txt` |
| The Solovetsky Monastery's petitions and papers, 1666-1676 (in Materialy, vol. III, 1876) | solovetsky-monastery | tradition | assigned | the monastery's petitions and letters with their signatures | `subbotin_materialy-dlia-istorii-raskola-v3-dokumenty-solovki-rus_1876.txt` |
| Le Stoglav ou les Cent Chapitres (1551), French translation (Duchesne 1920) | stoglav | antecedent | provisional | the hundred chapters in translation | `stoglav_stoglav-fra_duchesne1920.txt` |
| The Stoglav (Hundred Chapters), the Moscow church council of 1551 (Kozhanchikov 1863) | stoglav | antecedent | assigned | the council's text from line 889 | `stoglav_stoglav-chu_kozhanchikov1863.txt` |
| Archimandrite Antonii's petition and other writings (in Materialy, vol. VIII, 1887) | subbotin | tradition | provisional | the remaining works of the volume | `subbotin_materialy-dlia-istorii-raskola-v8-avvakum-zhitie-morozovoi-rus_1887.txt` |
| Government papers on the Solovki siege (in Materialy, vol. III, 1876) | subbotin | context | assigned | the Moscow side's orders and reports | `subbotin_materialy-dlia-istorii-raskola-v3-dokumenty-solovki-rus_1876.txt` |
| Materialy dlia istorii raskola, vol. I: documents on the Nikonian reform and its first opponents (1874) | subbotin | context | assigned | the numbered documents | `subbotin_materialy-dlia-istorii-raskola-v1-dokumenty-rus_1874.txt` |
| The 1666-67 council's investigations of Avvakum, Lazar and Deacon Fyodor (in Materialy, vol. II, 1875) | subbotin | context | assigned | the council and interrogation documents | `subbotin_materialy-dlia-istorii-raskola-v2-dokumenty-rus_1875.txt` |

What the census names and the table covers: Avvakum's Life in English (1924) and in two Russian witnesses (the 1861 first edition and a transcription), with his Pustozersk letters and petitions in Subbotin's edition and in Barskov; Boyarynia Morozova in her own letters (Barskov) and in the anonymous Life (Subbotin vol. VIII); the Solovki petitions with the brethren's signatures and the siege papers; the Vyg community in the Pomorskie otvety and in its abbot Ivan Filippov's history; the first schism-teachers (Neronov, Nikita, Lazar, Deacon Fyodor, the monk Avraamii) in their own writings; and the establishment record of the 1666–67 council and its interrogations, which the census asks to be read as coerced testimony.

What the census names and the table does not cover: Semyon Denisov's Vinograd rossiiskii and his history of the Solovki fathers; the popovtsy settlement records; the 1685 Articles against the schism as a standalone text; Evfrosin's Otrazitel'noe pisanie against self-immolation. See §3 and §4. All the new texts are Russian or Church Slavonic; only the Life has a public-domain English translation.

## 2. Cross-link opportunities

The obel pass found none in the corpus as it then stood. The Library pass placed Subbotin vols. I and II as `context` in both this world and the Russian Church, Nikon to the Holy Synod (VII.21), since the reform documents and the council's investigations belong to both. Nothing else in the corpus names the schism.

## 3. Verified acquisition leads

Public-domain editions not yet vendored, confirmed against the host as marked.

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| The Patriarch and the Tsar (Nikon's Replies to the boyar Streshnev and other papers, in English), vols. I and V | William Palmer | Palmer | 1871-76 | https://archive.org/details/patriarchandtsa00palmgoog | pd-us-by-date; host NOT_IN_COPYRIGHT | metadata API, djvu 2.0 MB, 23 October 2026; also `patriarchtsar0001will`. The reformer's own case in English; belongs first to the Russian Church world (VII.21) |
| Raskol na Donu v kontse XVII veka (the schism on the Don, with documents) | V. G. Druzhinin | — (Russian) | 1889 | https://archive.org/details/raskolnadonu00druz | pd-us-by-date | search hits (three copies), 23 October 2026 |
| The Russian Church and Russian Dissent | Albert F. Heard | — | 1887 | https://archive.org/details/russianchurchan00heargoog | pd-us-by-date | search hits, 23 October 2026; English scholarship, context |
| Kniga besed protopopa Avvakuma | Avvakum | — (Russian) | 1917 | https://archive.org/details/knigabesedprotopopaavvakuma20 | pd-us-by-date | metadata API and download, 23 October 2026; OCR too poor to vendor (under half its lines readable). Avvakum's Book of Conversations; the texts overlap Subbotin vol. V |
| Povest' o boyaryne Morozovoi, extended redaction (Wikimedia Commons PDF) | anonymous | — (Russian) | — | upload.wikimedia.org (Commons file named in the obel dossier) | pd-old | the obel pass found it and was rate-limited; the Life is now vendored from Subbotin vol. VIII, so this is a second witness only |

## 4. Checked and closed

Rows carried from the obel pass, with the Library pass's outcomes added.

| candidate | why it looked promising | why it's closed |
|---|---|---|
| archive.org `lifeofarchpriest0000avva` (Archon Books, 1963) | Same translated text, different scan | `access-restricted-item: true` (lending only); superseded by the vendored 1924 first edition |
| archive.org `bwb_KR-696-874` (Hogarth Press, 1963 reprint) | Same translated text | Same finding, lending only |
| HathiTrust `mdp.39015014696838` | The 1924 Hogarth edition, full view | HathiTrust returns a bot challenge from this sandbox; not needed once the 1924 archive.org copy cleared |
| `az.lib.ru` and `krotov.info` | Transcriptions of the Life and the Tale of Morozova | Hosts not in this sandbox's egress allowlist. The Life is now vendored from the 1861 printed edition and the Tale from Subbotin vol. VIII |
| Pomorskie otvety on Wikisource and rusneb.ru | The founding bespopovtsy document | The Wikisource page is a stub. Closed by vendoring the 1911 printing from archive.org (Library pass) |
| The Solovki petitions (1667), clean transcription | The monastery's own case | Closed by vendoring Subbotin vol. III and Barskov (Library pass), which print the petitions from the Synodal scrolls |
| Evfrosin, Otrazitel'noe pisanie (1691) | Internal Old Believer dissent against self-immolation | Still only scholarly discussion and a modern edition (Bubnov, 1895, not found on open hosts by this pass's search, 23 October 2026) |
| Istoriia Solovetskikh ottsov (1914 printing) | The Solovki fathers' history by Semyon Denisov | The research worker found the scan's OCR garbled; not vendored. Denisov's Vinograd rossiiskii was not found on open hosts |
| Esipov, Raskol'nich'i dela XVIII stoletiia, vols. I-II | Eighteenth-century case papers | The research worker found vol. II's OCR doubled and unusable; not re-checked this pass |
| Sobornyi svitok (1853) | The 1666-67 council's acts | Not found on archive.org by title search, 23 October 2026; the council's investigations are in Subbotin vol. II |

## 5. Open cross-world questions

- **The Russian Church, Nikon to the Holy Synod (VII.21).** The two worlds share the 1666–67 council and the reform documents. Subbotin vols. I and II are placed as `context` in both; Palmer's Patriarch and Tsar (Nikon's own case) is a lead for VII.21 first. Which world tells the council as its own story is a Doc_01 question for the two threads.
- **Cappadocian and later Greek East worlds.** Carried from the obel pass: no overlap with the Built Cappadocian world. Subbotin vol. I prints the Nikon–Paisios correspondence with the Greek text of Paisios's letter; that is the first Greek-patriarchal material touching this world, and it bears on Orthodoxy under the Ottomans (VII.18) as context. Not placed there yet.
- **Edinoverie and Belokrinitsa.** The census names both as later boundary events (1800, 1846); nothing in the library covers them yet, and Belokrinitsa falls outside the window.

## 6. Recommendation (portfolio decision for the project lead; does not block library work)

**Build**, as the obel thread's own Step 0 already found. The Library pass changes the ground under that thread's Doc_02: the census's communities' layer (Solovki, Vyg, the Pomorskie otvety), Morozova's own voice and Avvakum's letters and petitions are now vendored, in Russian. The world's single inside voice in English is still the Life; every other own-voice text is Russian or Church Slavonic in Subbotin's and Barskov's nineteenth-century editions, so a Representative's quotation from them would be the Library's own rendering, marked as such. Subbotin edited for an anti-schism journal; his introductions are polemical and are excluded from every tradition row. The obel thread should revise Doc_02's Missing Voices section against the refreshed §1 table before Doc_03.
