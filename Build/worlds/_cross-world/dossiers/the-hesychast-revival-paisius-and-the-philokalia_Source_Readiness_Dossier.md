# Source Readiness Dossier — The Hesychast Revival - Paisius & the Philokalia

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and why it
exists.

**Atlas ID:** VII.8
**Corpus-map slug:** `the-hesychast-revival-paisius-and-the-philokalia`
**Time window:** 1746-1815
**Region(s):** Athos, Moldavia, Russia; census `regions`: Asia Minor, Mediterranean, North Europe
**Dossier author / date:** Claude, Library thread, Era VIII source-research pass, 2026-10-23
**Corpus-map / `cic/texts/` state as of:** branch `library/era-viii-2026-10`, this pass.

## 1. Already assigned

10 works across 5 vendored files in `cic/corpus-map/the-hesychast-revival-paisius-and-the-philokalia.yaml`.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Writings of the Elder Basil of Poiana Marului: prefaces to Gregory of Sinai, Philotheus, Hesychius and Nil Sorsky; on forbidden foods | basil-of-poiana-marului | tradition | assigned | section II (pages 72-164 of the printed book) | `paisius-velichkovsky_zhitie-i-pisaniia-chu_optina1847.txt` |
| Visits to Monasteries in the Levant (1849): the Mount Athos chapters | curzon | context | provisional | the part on Mount Athos (Curzon's visit of 1837) | `curzon_visits-to-monasteries-in-the-levant_1849.txt` |
| Life of the Moldavian Elder Paisius (compiled at Neamt from Mitrofan's account) | mitrofan-schemamonk | tradition | assigned | section I, the brotherhood's foreword and the Life (pages 1-71 of the printed book) | `paisius-velichkovsky_zhitie-i-pisaniia-chu_optina1847.txt` |
| Prooimion to the Philokalia (Nikodemos the Hagiorite, 1782) | nikodemos-hagiorite | tradition | assigned | the heading 'PROOIMION' near the start of the volume (about raw scan line 607) to the first father's texts | `philokalia_ton-ieron-neptikon-v1-grc_tzelatis1893.txt` |
| Letters of the Neamt elders Sofronii (1797) and Athanasius to Mother Maria Protas'eva of Arzamas | paisius-velichkovsky | tradition | provisional | the letters after Paisius's writings (headings 'Pis'mo startsa Sofroniia' and 'Pis'mo ottsa Afanasiia', abo... | `paisius-velichkovsky_zhitie-i-pisaniia-chu_optina1847.txt` |
| Vostorgnutye klasy (Paisius's Slavonic translations of Chrysostom, Palamas, Mark the Ascetic and others; Optina 1849) | paisius-velichkovsky | tradition | assigned | whole volume | `paisius-velichkovsky_vostorgnutye-klasy-chu_optina1849.txt` |
| Writings of Paisius Velichkovsky: the scroll on mental prayer in chapters, the commentary on 'Lord have mercy', and other pieces | paisius-velichkovsky | tradition | assigned | section III (from page 165 of the printed book) to the letters | `paisius-velichkovsky_zhitie-i-pisaniia-chu_optina1847.txt` |
| Dedication of the 1893 edition to the hesychast fathers of Mount Athos (P. Ath. Tzelatis) | philokalia | transmission | provisional | the dedication after the title page, before the prooimion | `philokalia_ton-ieron-neptikon-v1-grc_tzelatis1893.txt` |
| Philokalia ton hieron neptikon, vol. 1 (Venice 1782; Athens 2nd ed. 1893): the anthology as compiled | philokalia | tradition | assigned | the patristic texts in the order the compilers set them, from Antony the Great onward | `philokalia_ton-ieron-neptikon-v1-grc_tzelatis1893.txt` |
| Philokalia ton hieron neptikon, vol. 2 (Venice 1782; Athens 2nd ed. 1893): the anthology as compiled | philokalia | tradition | assigned | whole volume, the compilers' selection from Peter of Damascus to the end | `philokalia_ton-ieron-neptikon-v2-grc_tzelatis1893.txt` |

## 2. Cross-link opportunities

| file | locus | why | suggested role / confidence |
|---|---|---|---|
| `nikodemos-hagiorite_pedalion-canons-grc_1886.txt` | whole; Nikodemos's commentary | The co-compiler's other great editorial work (first printed 1800). Already linked to the Ottoman and Kollyvades worlds. | tradition / provisional |
| `nikodemos-hagiorite_synaxaristes-vol1-sep-feb-grc_1900.txt`, `-vol2-mar-aug-grc_1900.txt` | whole | Nikodemos's Synaxaristes; the scan is garbled, so second witness only | tradition / provisional |
| `sathas_mesaionike-bibliotheke-v3-grc_1872.txt` | Makraios's Hypomnemata (from file line 13524) | An eyewitness church memoir of 1750-1800; the corpus map asks for a check of how it treats the Kollyvades | context / provisional |
| `macarius_fifty-spiritual-homilies_mason1921.txt` | whole | Pseudo-Macarius, whose paraphrase by Symeon Metaphrastes stands in Philokalia vol. II | antecedent / provisional |
| `cassian_institutes-and-contra-nestorium_petschenig1888.txt` | Institutes | The Philokalia prints Cassian on the eight thoughts | antecedent / provisional |
| `evagrius_praktikos_dysinger.txt` | whole | Evagrian chapters stand in the Philokalia, partly under Nilus's name | antecedent / provisional |
| `georgirenes_present-state-samos-nicaria-patmos-athos_denton1678.txt` | the Athos part | Athos seventy years before Paisius arrived | context / provisional |

## 3. Verified acquisition leads

| title | author | translator | year | url | rights basis | verified by |
|---|---|---|---|---|---|---|
| Nevidimaya bran' (Unseen Warfare), 4th Panteleimon edition | Nikodemos the Hagiorite, freely reworked | Theophan the Recluse | 1904 (in a 1991 Leningrad facsimile) | https://archive.org/details/B-001-027-773-ALL | text PD by date (1904); the 1991 front matter and the publisher's adverts at the end are modern and would need stripping | metadata API, djvu 0.89 MB, 23 October 2026 |
| Kriny sel'nye ili tsvety prekrasnye | attributed to Paisius Velichkovsky | Russian rendering from a manuscript at the St Elias skete (Athos) | St Elias skete edition, year not shown in the pages read; modern Krasnodar diocesan reprint | https://archive.org/details/PrpPaisiusVelichkovsky (file "Prp. Paisius Velichkovsky. Kriny selniye...") | underlying edition probably PD but the year is not legible in what was read; modern blessing page | metadata API, djvu 0.25 MB, 23 October 2026 |
| Bibliion psychopheles (the Exomologetarion) in Karamanli Turkish | Nikodemos the Hagiorite | translator not named in the metadata | 1799 | https://archive.org/details/u.-... | PD by date | metadata API, djvu 0.83 MB, OCR 0.63, 23 October 2026. Karamanli in Greek letters, borderline OCR; a specialist witness |
| Athos, or the Mountain of the Monks | Athelstan Riley | none | 1887 | https://archive.org/details/athosormountaino00rile | PD by date | metadata API, djvu 0.76 MB, 23 October 2026. A visit of the 1880s, too late for this window |
| Dobrotolyubie v russkom perevode (Theophan's Russian Philokalia) | Theophan the Recluse | Theophan | 1877-1890 | https://archive.org/details/PhilokaliaRussian | PD by date | metadata API, no djvu text, 23 October 2026. For the Optina world |
| Istoricheskoe opisanie Kozel'skoi Optinoi pustyni | Erast | none | 1902 | https://archive.org/details/istoricheskoeopisaniekozelskojoptinojpu0 | PD by date | metadata API, djvu 0.76 MB, 23 October 2026. For the Optina world |
| Optina Pustyn': istoricheskii ocherk | Sergii Chetverikov | none | 1926 (Paris, YMCA) | https://archive.org/details/1926_20251015 | PD by date (1926) under the project's rule | metadata API, 23 October 2026. For the Optina world |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Dobrotolyubie (Moscow 1793), item Dobrotolyubie1793, main file | Paisius's own Slavonic Philokalia, named in the census | Garbled. The OCR model read the Slavonic as Bulgarian plus Greek and produced nonsense; the 0.74 measure is false. Read at head and middle. |
| Philokalia, Venice 1782 (first edition) | The anthology as first printed | No scan found on archive.org under Greek, transliterated or English searches |
| Heortodromion (Venice 1836), item u-u-u-u_202102 | Nikodemos's festal commentary | OCR done with a Cyrillic model: Greek turned into Cyrillic and Latin junk (measure 0.67 is false) |
| Kepos chariton (1819), item u-._20210206 | Nikodemos | Same uploader and same garbling (0.64) |
| Hermeneia eis tas hepta katholikas epistolas (Venice 1806), item u-.-u-... | Nikodemos | Same garbling (0.71 measure, unreadable) |
| Zhitie startsa Paisiia (Optina, 1906), file in PrpPaisiusVelichkovsky | The Life in Russian | The upload is a modern edition with a modern preface, which is in copyright; the 1847 Slavonic Life is vendored instead |
| Zhitie i pisaniia (1847), the second scan in PrpPaisiusVelichkovsky | Same book | A modern facsimile reprint with a Tula printer's colophon; the clean 1847 scan was used |
| The Way of a Pilgrim (Otkrovennye rasskazy strannika), item strannik_202301 | Named in the census as a fruit of the revival | A modern edition with a modern preface; the text itself dates from the 1850s-1880s, after the window. R. M. French's English (1930) was not found on archive.org |
| "SpiritualQuest - The Philokalia", item philokalia-4 | Marked public domain by its uploader | It is the Palmer, Sherrard and Ware English (Faber, 1979 onward), in copyright. The PD mark is wrong |
| Philokalia vols. A-C, items 20240317_20240317_1609 / _1611 / _1730 | Greek Philokalia | Galitis's modern Greek translation (first edition 1985, fifth 2006), in copyright |
| Kadloubovsky and Palmer, Writings from the Philokalia | English | 1951; in copyright (not searched further) |
| Ho Aoratos Polemos, item AGIOS_NIKODHMOS_AGIOREITHS-AORATOS_POLEMOS | Unseen Warfare in Greek | Modern, CC BY-NC-ND, no text file. No pre-1930 scan of the Venice 1796 edition was found |
| Romanian Nicodim Aghioritul and Paisie items | Romanian Neamt tradition | All modern publications |
| Chetverikov, Starets Paisii Velichkovskii (English 1980) | Named in the census | In copyright |

## 5. Open cross-world questions

- Nikodemos and Macarius belong to both this entry and the Kollyvades entry (VIII.12). The Philokalia is placed here, and the prooimion is provisional for VIII.12. Should Nikodemos's other works go to VIII.12 by default?
- The 1847 and 1849 Optina editions are this world's texts and also Optina's first publishing acts. Should the Optina preface count as a tradition text for VIII.11, which the census dates from 1821?
- The fourteenth-century texts in Philokalia vol. II are placed as provisional transmission for the Palamite world (V.4). Does that world want its sources only in its own editions?

## 6. Recommendation (portfolio decision for the project lead; does not block library work)

**Build.** The world's own voice is deep and now in hand in the original languages. The Greek Philokalia is complete in two volumes; it is the census's central formation evidence. Paisius speaks in his own treatise on the prayer of the mind and in his translations, and the Life by his disciples is here with his teacher-companion Basil's prefaces. No floor question arises. The weakness is language: there is no public-domain English of the Philokalia, the Life or Paisius's writings (Kadloubovsky 1951, Featherstone 1990 and Palmer-Sherrard-Ware 1979 are all in copyright). Builders will work from Greek and Church Slavonic, and Doc_02 should say so plainly. The Slavonic Dobrotolyubie of 1793 is the one large gap: its only scan is unreadable. This world stands apart from the Kollyvades entry because its centre is the anthology and the Neamt school rather than the Athonite dispute.

