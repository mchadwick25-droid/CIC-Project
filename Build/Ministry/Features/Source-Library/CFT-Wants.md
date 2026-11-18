# Church Family Tree wants — the Library's list

**Charter (Mark, 2026-11-10):** "launch a library thread that is patterned after previous threads with
full research, organization and render abilities to find the sources you need, public domain in any
language we can find it."

One list of texts the tree's workers need, each tied to the entry or gap it serves. A want is filled
only when the text is vendored in `cic/texts/` with rights read from the host and the title page, and
shelved in `cic/corpus-map/`. Rights rows live in `Build/worlds/_cross-world/download-queue-seed.yaml`.
The page for Mark renders this list (https://claude.ai/artifact/RTJ2uXC4rjqKEguvt4UiDP); this file is the record.

States: **filled** (vendored and shelved) · **held already** (in the Library unused; now shelved) ·
**located** (found and rights clear, not vendored) · **none survives** (no own text exists, so no
search can fill it) · **not found** (searched; where is said) · **queued** (a later batch).

## Tally of vendoring batches, from 2026-11-15

One line per batch that vendored texts. Each batch's own section below holds its rows and cautions; its Open-Gaps entry holds what it left owed.

| date | batch | texts | pull request | Open-Gaps |
|---|---|---|---|---|
| 2026-11-15 | Eras 4-5, third fill | 7 | #1686 | 286 |
| 2026-11-15 | Era 9, batch 1 (the major person rows) | 99 | #1687 | 287 |
| 2026-11-15 | Era 10, batch 1 | 94 | #1689 | 290 |
| 2026-11-15 | Era 8, batch 1 (the global files) | 30 | #1690 | 291 |
| 2026-11-15 | Era 9, batch 2b (Britain, Europe, North America) | 61 | #1693 | 293 |
| 2026-11-15 | Era 10, batch 2 (Africa, Oceania, the Orthodox and Oriental churches) | 71 | #1695 | 295 |
| 2026-11-15 | Era 9, batch 2a (Africa, Asia, Oceania, Latin America, the Caribbean, the Eastern churches) | 71 | #1697 | 294 |
| 2026-11-15 | Era 8, batch 2 (British Isles and Methodists, North America, Catholic Europe) | 37 | #1698 | 298 |
| 2026-11-16 | Era 9, the located volumes | 27 | #1699 | 299 |
| 2026-11-16 | Era 10, batch 2b, the periodicals | 45 | #1704 | 300 |
| | **Total** | **542** | | |

## Batch 1 — the later-worlds people gate (Open-Gaps 164, 2026-11-10)

Source: `Build/Ministry/Operations/Audits/2026-11-10_later-worlds-people/final_rows.json`. Each held
person failed "own words held" (answer C). The want is a text written by them or issued in their name.

| person | want | state | file(s) | unblocks |
|---|---|---|---|---|
| Pamphilus of Caesarea | Apology for Origen, Book I (Rufinus's Latin) | filled | `pamphilus_apologia-pro-origene-rufinus-lat_lommatzsch1846.txt`; second witness `origen_opera-omnia-t7-pamphilus-apologia-pg17-grc-lat_migne1857.txt` | The Apology itself is now held. Mark's question B (a book written jointly with Eusebius) still decides whether it counts. |
| Heraclius | The Ecthesis (638) | held already | `mansi_sacrorum-conciliorum-collectio-tomus-10-lat_welter-facsimile1901.txt`, lines about 100110-100680 (Lateran 649, Secretarius III) | A document issued in his name is now on his home shelf, so the own-words test is met. The count passed already. He can be built. |
| Francis of Assisi | Rule, Testament, letters, Canticle | filled | `francis-assisi_writings-of-saint-francis_robinson1906.txt`; `francis-assisi_opuscula-lat_quaracchi1904.txt` | Own words are held. He is still a founder, so Mark's question A decides. |
| Bonaventure | writings of his own | filled | `bonaventure_life-of-saint-francis-legenda-maior_salter1904.txt`; `bonaventure_tria-opuscula-breviloquium-itinerarium-de-reductione-lat_quaracchi1911.txt` | Own words are held, he founded nothing, and the count passed. He can be built. |
| Priscillian | the Wurzburg tractates | filled | `priscillian_quae-supersunt-lat_schepss1889-csel18.txt` | Own words are held. He is still a founder, so question A decides. |
| Mani | text of his own in Manichaean transmission | not found | Searched archive.org for Müller 1904, the Turfan Estrangelo fragments: not there (HathiTrust is behind a browser check). The Kephalaia (1935-1940) and the Psalm-book (1938) are too late. Augustine's quotations of the Fundamental Epistle (CSEL 25, 1891) are an opponent's quotations. | Nothing. He is a founder anyway. |
| Kaleb | an inscription in his name | not found | Littmann, Deutsche Aksum-Expedition IV (1913), read: it has no Kaleb inscription. Nothing else before 1931 was found. | Nothing. |
| Valdes of Lyon | his profession of faith (c. 1180) | not found | No printing before Dondaine (1946, not public domain) was found on archive.org; Müller 1886 read. | Nothing. |
| Mesrop Mashtots | a work of his own | none survives | No extant work of his own is known; Koriun's Life is about him. | Nothing. |
| Paul of Samosata, Basilides, Valentinus, Maximilla | words of their own | none survives in their own transmission | Only opponents' quotations survive. Valentinus's Gospel of Truth is a 1950s find of disputed authorship. | Nothing. |
| Hilarion of Gaza | words of his own | none survives | Jerome's Life is about him. | Nothing. |
| Johannes Tauler | writing of his own | none survives | His sermons survive as his hearers' notes. Vetter (1910) prints the same notes. | Nothing. |

Located, not vendored: Bonaventure, Opera omnia VIII (Quaracchi 1898), the Latin Legenda maior
(seed row, `not-yet-downloaded`).

## Batch 1 — Library defects (Open-Gaps 165 and 152)

| defect | fix |
|---|---|
| Hippolytus's Refutation shelved as Montanism's own voice | Role set to `context` on `montanism-the-new-prophecy` and on `ebionite-nazoraean-current`, which had the same fault. It stays `tradition` on `roman-church-third-century`, Hippolytus's own church. |
| Nikodemos's Synaxaristes on the 1453-1650 shelf | Removed from `orthodoxy-under-the-ottomans-parish-millet-and-n`; it stays on the 1650-1821 and Kollyvades shelves. The Pedalion (1800) had the same fault; it was moved in batch 2. |
| PO17 described as Petit's Florence documents | The row was right but named the whole volume. Loci now give line ranges: the Lives at 156-17448, Petit's Mark of Ephesus at 17449-49934, the Arabic Synaxary from 49935. |
| The Brosset file is the Introduction volume | The file header now says so. The two chronicle-voice rows are replaced by one `context` row for Brosset's study. The chronicle text itself is a new want (batch 2). |
| "Whole file" loci on multi-work volumes | Fixed for PO17. The general pass (707 staging files say "whole") is batch 2: Langlois's sections, the anf volumes, the PO fascicules. |
| People rows' `year`; the Ephrem alias | The census owner's, not the Library's. Passed on. |
| Busch's Chronicon Windeshemense (ruling 6) | `tradition` on the Devotio Moderna shelf. |
| Love's Mirror | Added as `tradition` on `carthusians-later-middle-ages` (a new shelf). The earlier rows stay as they were. |
| Bell, Part II (the Melitian papyri) | Added as `tradition` on `melitian-schism` (a new shelf). The `desert` row stays: see the open questions. |
| Simeon of Beth Arsham (ruling 5) | Already on the Syriac Orthodox shelf, inside the John of Ephesus and Zachariah rows. No move was needed. |
| Theophilus row to II.1 | Not done: "may move" is a census question, not a Library one. |

### The two cross-world moves (Mark, 2026-11-10: "take both recommendations")

1. Bell 1924, Part II: the row stays on the `desert` shelf, now as `context`. The `melitian-schism`
   row stays `tradition` (batch 2). The M9 gate keeps every desert source record on desert's own
   shelf, and Mark's rule allows it: "if the source is consurant of past and they could likcly know it
   they can point to it".
2. The Pedalion (1800): off the 1453-1650 shelf (batch 2), once data release 32 (#1578) had moved
   the census person row for Nikodemos onto the Philokalia rows. It stays on the 1650-1821 and
   Kollyvades shelves.

## Batch 2 — the eras 8-9 holds (`CiC_Step0_Eras8-9_GlobalSweep_V1_0.md`)

Each row was held "for sources", that is, for a dated primary text. Where the tree entry a text
serves does not exist yet, its shelf row is `needs-ruling` on the nearest existing entry, as the
intake rule says.

| hold | want | state | file(s) | unblocks |
|---|---|---|---|---|
| ME-20, the Tolstoyans | Tolstoy's own writings before 1906 | filled | `tolstoy_what-i-believe_popoff1885.txt`; `tolstoy_kingdom-of-god-is-within-you-v1_garnett1894.txt` (vol. I of II) | The Section A ruling now has its dated text. |
| ME-6, the spiritual Christians | the Dukhobors' and Molokans' own texts | filled for the Dukhobors | `dukhobors_zhivotnaia-kniga-dukhobortsev-rus_bonch-bruevich1909.txt` | The Section A ruling for the Dukhobors. The Molokans were not found. |
| RV-7, the Transylvanian Unitarians | a dated own-voice text of the church | filled (no shelf yet, see batch 3) | `ferencz_short-account-of-the-unitarian-church-of-hungary_1907.txt`; `ferencz_unitarius-kis-tukor-hun_1875.txt` | RV-7, and the living mark graded none (Open-Gaps 162). |
| AP7, Thrissur | the 1861 and 1874 Chaldean bishops | filled, plus one held already | `mackenzie_christianity-in-travancore_1901.txt`; Whitehouse 1873, held already, now shelved | AP7's line, with the link to the Chaldean entry. |
| AP15, Korea | Catholic and Protestant own-voice texts | filled | `dallet_histoire-de-l-eglise-de-coree-t1-fra_1874.txt`, `-t2-`; `korean-repository_v3-1896_seoul1896.txt`; `underwood_call-of-korea_1908.txt` | The Korean Catholic entry gets its history, and AP15 gets dated Protestant sources. Underwood is shelved on korean-protestantism-twentieth-century, tradition. |
| AP12, Australia and New Zealand | a chaplain's or bishop's own words | filled in part | `marsden_life-and-work-of-samuel-marsden_jb-marsden1913.txt` | AP12 has Marsden's own letters. Ullathorne (1837) exists only as a 1963 facsimile, so its rights are unclear. Lang (1834) is located, not vendored. |
| AP11, the Peking mission | the mission's own history | filled to 1808 | `adoratskii_pravoslavnaia-missiia-v-kitae-vyp1-1685-1745-rus_1887.txt`, `-vyp2-1745-1808-` | AP11 to 1808. No issue covering 1808-1906 was found. |
| LA8-6, Haiti | before 1804; Holly after 1860 | filled | `moreau-de-saint-mery_description-partie-francaise-saint-domingue-t1-fra_1797.txt`, `-t2-`; `spirit-of-missions_v39-1874-12-haiti-triennial-report_1874.txt` | Both of LA8-6's lines. A period printing of the 1860 Concordat was not found. |
| LA8-8, Cuba and Puerto Rico | a dated church document | filled | `claret_apuntes-regimen-de-la-diocesis-santiago-de-cuba-spa_1863.txt` | LA8-8. |
| LA8-9, the Bethlemites | the founder's Life, the order's constitutions | filled | `montalvo_vida-admirable-pedro-de-san-jose-betancur-spa_1683.txt`; `garcia-de-la-concepcion_historia-bethlehemitica-spa_1723.txt` | LA8-9. |
| LA8-10, Cancuc and the Talking Cross | the movements' own documents | not found; the church's side found | `juarros_compendio-historia-ciudad-de-guatemala-t2-spa_1809.txt`; `garcia-pelaez_memorias-historia-reyno-de-guatemala-t2-spa_1852.txt` | Not unblocked: both are the Spanish side. No Cruzob or Cancuc text was found before 1931. |
| AF-8, West Africa 1650-1793 | Capitein, Quaque, Thompson | not found | Thompson 1758 is an image-only scan, with nothing readable. No printing of Capitein or Quaque before 1931 was found. | Nothing. |
| ME-4, Antioch after 1815 | a dated Orthodox statement | not found | The 1848 Encyclical was found only in a modern translation (CC BY-NC-ND), and Palmer 1853 does not hold it. Kimmel 1850 could not be downloaded. | Nothing yet. |
| ME-7, the Syriac Orthodox and Catholics | a source from inside the region | not found | Rabbath 1910 (Jesuit and consular papers) and Southgate 1856 (a visitor) are outsiders. Peter III's 1876-77 circulars are for Malabar. | Nothing yet. |
| ME-21, Rabinowitz | his own documents | located, not fetched | Delitzsch's Documente (1884-87) and Rabinowitz's sermons (1885) are full view on Google Books, but downloads were refused (HTTP 429). | Nothing yet. A retry by another route is queued. |
| RV-9, Kosmas the Aitolian | his Teachings before 1931 | not found | All printings found date from 1966 or later. | Nothing. |
| AP10, Hermano Pule | any dated primary | not found | archive.org only. A Spanish-language pass is queued. | Nothing. |
| AP13, Pai Mārire and Ringatū | a Māori source | not found | Only colonial and missionary accounts (Gudgeon 1879, Taylor 1868) were found, and they are hostile. nzetc.victoria.ac.nz blocked the search. | Nothing. |

## Batch 3 — the earliest named gaps (Open-Gaps 158), with two retries

The rule for gap texts: a text gets a shelf row only where an entry already covers its date. A text
for a stretch the tree has no entry for is vendored and listed here, and its shelf waits for the new
entry. A row placed on an entry that ends before the text was written is out of window, the fault
Nikodemos showed.

| gap or hold | state | file(s) | shelf | unblocks |
|---|---|---|---|---|
| The Roman Church, 604 to about 1049 | filled to about 891, with catalogues to about 1003 | `liber-pontificalis_texte-introduction-commentaire-t1-lat-fra_duchesne1886.txt`, `-t2-..._duchesne1892.txt` | none yet | Lives written in Rome inside the gap. Mirbt's Quellen (held) carries papal acts of the tenth and eleventh centuries. |
| The Latin church in the Frankish lands, 888 to about 1049 | filled | `regino-pruem_libri-duo-de-synodalibus-causis-lat_wasserschleben1840.txt` (about 906); `flodoard_annales-lat_lauer1905.txt` (919-966) | none yet | A visitation rule and a canon's annals from inside the gap. |
| Benedictine monasticism after 604 | filled | `cluny_recueil-des-chartes-t1-802-954-lat-fra_bernard-bruel1876.txt` | `cluniac-reform-monasticism`, tradition | Cluny's own charters from 910. |
| The Irish church, 1169 to today | filled | `four-masters_annals-of-the-kingdom-of-ireland-v3-1172-1378-gle-eng_odonovan1856.txt`; `synod-of-thurles_decreta-synodi-plenariae-hiberniae-lat_1851.txt` | none yet | Church annals 1172-1378, and the bishops' own decrees of 1850. |
| The Welsh church, 1282 to today | filled | `welsh-bible_y-beibl-cyssegr-lan-cym_morgan1588.txt`; `welsh-prayer-book_llyfr-gweddi-gyffredin-cym_1664.txt` | the English Reformation entry and the Restoration Church of England entry, tradition | The Welsh church's own Bible (1588) and Prayer Book (1664). The OCR is poor. |
| The Mozarabic community, 1031 to today | filled | `mozarabic-liturgy_missale-mixtum-pl85-lat_migne1862.txt`, `mozarabic-liturgy_breviarium-gothicum-pl86-lat_migne1862.txt`; `mozarabes-de-toledo_documentos-siglos-xii-xiii-v1-spa_gonzalez-palencia1926.txt` | the liturgy on `mozarabic-christianity`; the deeds have none yet | The rite's own texts, and the Toledo community's dated deeds of the twelfth and thirteenth centuries. Held already: Ferotin's Liber Mozarabicus Sacramentorum (1912). |
| Lerins, about 450 to today | filled | `lerins_cartulaire-de-l-abbaye-de-lerins-pt1-lat-fra_moris-blanc1883.txt`; `barralis_chronologia-sanctorum-insulae-lerinensis-lat_1613.txt` | none yet | The abbey's own charters from the eleventh century, and a monk's history of 1613. This bears on "The Lerins entry says the abbey has stood since about 410" (Open-Gaps, 2026-11-10). |
| The Church of Antioch after 312 | held already | Paul of Aleppo, Travels of Macarius (Belfour 1836), two volumes | on the Ottoman 1650-1821 shelf already | Antioch's own patriarch's journey, 1652-1660. |
| The Church of Jerusalem after 450 | filled | `mansi_sacrorum-conciliorum-collectio-tomus-11-lat_welter-facsimile1901.txt` (Sophronius, 634); `papadopoulos-kerameus_analekta-hierosolymitikes-stachyologias-t4-grc_1897.txt` (acts from 1670) | the Heraclian entry and the Ottoman 1650-1821 entry, tradition | Jerusalem's patriarchs in their own words. Held already: Dositheus's synod of 1672. |
| The Georgian church, 1245 to 1917 | filled in part | `brosset_histoire-de-la-georgie-pt2-histoire-moderne-livr2-fra_1857.txt` | none yet | Catholicoi's letters, charters and the exarchate to the nineteenth century. The 1856 first livraison was not found. |
| Judean desert and Sinai monasticism, 614 to today | filled | `antiochus-strategos_sack-of-jerusalem-614_conybeare1910.txt` | none yet | A Mar Saba monk's account from just after 614. Held already: the Life of George of Choziba. No Sinai document was found. |
| The Syriac Orthodox Church, 1300 to 1915 | not found | Only a list of later maphrians, in Lamy's Bar Hebraeus (held). The 1789 Bruns-Kirsch scan is unreadable. | none | Nothing yet. Wright's catalogue of Syriac manuscripts (dated colophons) is the next lead. |
| Arabic-speaking Chalcedonians, 1009 to 1724 | held already, plus one in part | Paul of Aleppo (held); `po18_patrologia-orientalis-t18-yahya-ibn-said-histoire-ara-fra_kratchkovsky-vasiliev1924.txt` | none yet | Paul of Aleppo answers the gap. Yahya's part after 1009 appeared in 1932, which is not public domain. |
| AP10, Hermano Pule | an account found | `montero-y-vidal_historia-general-de-filipinas-t3-spa_1895.txt` | Philippine Catholicism 1815-1906, context | A summary of Apolinario's own sworn declaration, inside a hostile history. |
| ME-21, Rabinowitz | still not fetched | Six full-view Google Books items (ids in the Decision-Log). Google refuses this host's downloads (HTTP 429 and its "sorry" page). No copy was found elsewhere. | | Mark or a browser session could fetch them. |

**Corrected from batch 2.** Ferencz (1875, 1907) had been shelved on the anti-Trinitarian entry
(1517-1650). That is out of window, so both rows are removed. The files stay listed under RV-7
until the entry for the church after 1660 exists.

## Batch 4 — the religious orders (Open-Gaps 158)

Eleven named gaps: the orders, and the Maronites. The Latin church has an entry for every stretch
after 1049: the Gregorian church (1049-1300), Avignon to Lateran V (1300-1517), the Tridentine church
(1517-1650), the ancien-regime church (1650-1815) and the long nineteenth century (1815-1906). An
order's own text is shelved as `tradition` on whichever of these covers its date of writing, as the
Compiegne Carmelites already were. The Orthodox Ottoman entries do the same for Athos. The Maronites
have no entry after 1517, so their text has no shelf yet.

| gap | state | file(s) | shelf | unblocks |
|---|---|---|---|---|
| Athonite monasticism after 1300 | filled | `athos-monasteries_haupturkunden-fur-die-geschichte-der-athoskloster-ger-grc_meyer1894.txt`; `dapontes_kepos-chariton-grc_sophocleous1880.txt`. Held already: Georgirenes (1678) | Meyer: the 1394 typikon on the hesychast entry, context, the documents of 1498-1574 on Ottoman 1453-1650, those of the 17th-18th centuries on Ottoman 1650-1821; Dapontes on Ottoman 1650-1821 | The Holy Mountain's own typika, patriarchal decrees and letters from 1394 to the Kollyva circulars, and a Xeropotamou monk's own book. Meyer's Greek OCR is garbled: second witness for the Greek. |
| The Carthusians after 1534 | filled | `chauncy-maurice_historia-aliquot-martyrum-anglorum-lat_1888.txt`; `chauncy-maurice_history-of-the-sufferings-of-eighteen-carthusians-in-england_1890.txt`; `carthusian-statutes_nova-collectio-statutorum-ordinis-cartusiensis-lat_1681.txt` | Chauncy on the Tridentine church; the statutes on the ancien-regime church | A London Carthusian's own account of 1535 (printed 1550), in Latin and a clean English; the order's statutes as gathered in 1681. Le Couteulx's Annales stop at 1420. |
| The Cistercians after 1300 | filled | `rance_de-la-saintete-et-des-devoirs-de-la-vie-monastique-t1-fra_1683.txt`, `-t2-`; `trappists_constitutions-and-usages-of-the-reformed-cistercians-of-la-trappe-eng-lat_1894.txt`. Held already: the Port-Royal acts (1724) | Rance on the ancien-regime church; the constitutions on the long nineteenth century | La Trappe's abbot in 1683, and the Trappists' own law of 1894. Not found: the 1718 Reglements. Located, not vendored: the Nomasticon Cisterciense (1664; garbled OCR). |
| The Maronites after 1517 | held already; a second scan added, no shelf (corrected in batch 5) | `duwayhi_tarikh-al-taifa-al-maruniyya-ara_shartuni189x.txt` | none yet | Patriarch al-Duwayhi's own history of his church (Beirut, 1890s). The OCR is garbled: second witness. Not found: the 1736 Synod of Mount Lebanon in a readable printing (the Zainati 1926 scan is unreadable), Anaissi's Bullarium. |
| The canons regular after 1246 | filled | `barnwell-priory_observances-in-use-at-barnwell-lat-eng_clark1897.txt`; `premonstratensian-statutes_statuta-renovata-ordinis-praemonstratensis-lat_1626.txt`. Held already: Thomas a Kempis's Chronicle of Mount St Agnes, Busch's Chronicon Windeshemense | Barnwell on the Gregorian church (written 1295-96); the statutes on the Tridentine church | An Augustinian priory's own customary, and the Premonstratensians' renewed statutes of 1626. Not found: Le Paige (1633). |
| The Order of Malta after 1291 | filled | `hospitallers_statuti-della-sacra-religione-di-s-giovanni-gierosolimitano-ita_bosio1589.txt` | the Tridentine church | The Order's own statutes after its chapter of 1584. Located, not vendored: Bosio's Istoria (1594-1602; 5-6.5 MB each), Vertot (1726), the Cartulaire general III-IV. |
| The Carmelites after 1300 | filled | `carmelite-general-chapters_acta-capitulorum-generalium-v1-1318-1593-lat_wessels1912.txt` | the chapters to 1513 on Avignon to Lateran V; those of 1524-1593 on the Tridentine church | The order's general chapters, 1318-1593. Located: Zimmerman's Monumenta (1907); the Speculum Carmelitanum (1680; garbled OCR). |
| The Franciscans after 1517 | filled | `de-luca-giovanni_annales-minorum-t18-1540-1553-lat_1740.txt`; `capuchin-constitutions_constitutiones-fratrum-minorum-capuccinorum-lat_1638.txt` | De Luca on the ancien-regime church (written 1740); the constitutions on the Tridentine church | The order's own annals for 1540-1553, and the Capuchins' own law. Located: Annales tomes XIX (1745) and XX (1794). Not found: Wadding's tome XVI, Boverius. |
| The Dominicans after 1300 | filled | `dominican-general-chapters_acta-capitulorum-generalium-v2-1304-1378-lat_reichert1899.txt`; `...-v6-1601-1628-lat_reichert1902.txt` | Avignon to Lateran V; the Tridentine church | The general chapters' acts, 1304-1378 and 1601-1628. Located: vols. V and VII. Vols. VIII-XII (after 1656) are not on archive.org. |
| The Jesuits after 1650 | filled | `jesuit-relations_thwaites-v36-fra-eng_1896-1901.txt` to `-v40-` (1650-1653); `lettres-edifiantes_memoires-de-la-chine-t19-fra_1781.txt`, `-t20-`, `-t22-` | the Society of Jesus 1650-1814 entry (new in data release 33); the China letters also on Chinese Catholicism 1650-1906 | The Jesuits' own reports from New France after 1650 and from Peking, 1717-1731. These also serve the church in New France after 1650. The two new entries came with data release 33, which landed while this batch was open; the rows went first to the ancien-regime church and were moved before merge. Located: Thwaites 41-46 (1654-1660). |
| The Discalced Carmelites after 1622 | filled | `brother-lawrence_practice-of-the-presence-of-god_allenson1906.txt`; `francisco-de-santa-maria_reforma-de-los-descalzos-t2-spa_1655.txt`. Held already: the Compiegne Carmelites (1836) | the ancien-regime church; Compiegne now also on the long nineteenth century | A Paris lay brother's own letters (1666-1691) and the order's own history (1655). The Reforma's OCR is fair to garbled: second witness. |

**Flagged, not changed.** One row already on main sits on an entry that ends before the text was
written: the Compiegne history (posthumous, 1836) on the ancien-regime church (to 1815). The row carries
a census story, so it stays, and this batch adds the long-nineteenth-century shelf beside it. Moving it
is the census owner's call. The Port-Royal acts, printed in 1724, were written in the 1660s, inside
their entry's window.

## Batch 5 — Rabinowitz, and the early modern mission and Eastern gaps

Data release 33 (eras 8-9) gave four of these gaps entries of their own: the St Thomas Christians
1665-1815, Kongo 1650-1881, Japan's hidden Christians 1650-1865 and Chinese Catholicism 1650-1906.
Their census entries cite texts the Library held but had not shelved there, so this batch shelves those
too. New France after 1650 and Ukrainian Orthodoxy after 1700 still have no entry of their own.

| gap or hold | state | file(s) | shelf | unblocks |
|---|---|---|---|---|
| ME-21, Rabinowitz | filled | `rabinowitz_documente-der-national-judischen-christglaubigen-bewegung-deu-heb_delitzsch1884-bodleian.txt` and `-harvard.txt` (two copies); `rabinowitz_fortgesetzte-documente-...-deu_delitzsch1885.txt`; `rabinowitz_neue-documente-selbstbiographie-und-predigten-deu_delitzsch1887.txt`; `rabinowitz_zwei-predigten-in-dem-gotteshause-bethlehem-in-kischinew-deu_delitzsch1885.txt` | none yet: ME-21 waits for its own row | The hold's "pre-1930 source opened raw": the congregation's Thirteen Theses, articles of faith and March 1884 declaration with their Hebrew originals; Rabinowitz's letters of 1884 (in German); his autobiography and sermons. Mark downloaded the five Google Books PDFs; they are cleared from `_intake/`. |
| ME-21, the Hebrew letters (Bikure ta'anah) | not found | — | — | Google's title is wrong for its item: it is the Fortgesetzte Documente, which prints Rabinowitz's letters only in German (one in his own German, the rest translated from his Hebrew). It has no Hebrew text. The Hebrew letters stay wanted. |
| The St Thomas Christians, 1665-1836 | filled, outsiders only | `paulinus-a-s-bartholomaeo_india-orientalis-christiana-lat_1794.txt`; `buchanan_christian-researches-in-asia_1811.txt`. Held already, now also shelved: Geddes (1694), Raulin (1745), Whitehouse (1873), Philipos (1869) | `st-thomas-christians-two-obediences`, context | A Carmelite's history (1794), which cites a Syriac letter of Mar Thoma VI and his own meeting with him in 1785, and Buchanan's visit of about 1806. No Puthenkoor text of its own was found. |
| The Kongo church after 1650 | filled from held texts, plus an outsider | `bentley_pioneering-on-the-congo-v1_1900.txt`, `-v2-`. Held already, now also shelved: Paiva Manso's documents after 1651, including letters of the Count of Soyo; Carli, Cavazzi, Merolla, Zucchelli | `kongo-christianity-after-1650`: Paiva Manso's later documents as tradition, the rest context | The Kongo court's own letters after 1650 were already held, on the earlier Kongo entry's shelf. No other Kongolese text was found. |
| Japan's hidden Christians, 1650-1865 | filled, mediated | `marnas_religion-de-jesus-ressuscitee-au-japon-t1-fra_1897.txt`, `-t2-` | `japans-hidden-christians` and `japanese-christianity-hidden-emergence-meiji`, context | The Urakami Christians' words to Petitjean in 1865, as he reported them. No orasho or Tenchi hajimari no koto printed before 1931 was found. |
| Chinese Catholics, 1650-1906 | outsider only | `launay_histoire-des-missions-de-chine-kouy-tcheou-t1-fra_1907.txt`. Held already, now also shelved: the Propaganda Collectanea (1907) | `chinese-catholicism-1650-1906`, context | A mission history that names its Chinese priests. Not found: a Chinese Catholic's own text (Andreas Ly's Journal, the 1803 Sichuan synod, Huang Bolu). |
| The church in New France after 1650 | filled | `quebec-bishops_mandements-lettres-pastorales-et-circulaires-v1-fra_tetu-gagnon1887.txt`; `marie-de-l-incarnation-quebec_lettres-t1-fra_richaudeau1876.txt`, `-t2-` | the mandements and tome II on the ancien-regime church; tome I on the New France mission entry (1610-1650); all tradition | The Quebec bishops' own pastoral letters from Laval (1659), and the Ursuline founder's own letters from 1639 to 1672. |
| Ukrainian Orthodoxy, 1700 to today | filled to the 1770s | `arkhiv-iugo-zapadnoi-rossii_ch1-t2-pravoslavie-v-zapadnoi-ukraine-xviii-rus_1864.txt`; `kiev-academy_akty-i-dokumenty-t1-ch2-1721-1750-rus_petrov.txt` | `russian-church-nikon-to-holy-synod` (1652-1815), tradition | The Orthodox clergy's letters of the 1760s and the Kyiv Academy's documents of 1721-1750. The Kyiv metropolis then lay inside the Russian Synodal church; no census entry is Ukrainian Orthodoxy after 1700 (logged as a census gap). Nothing after 1918 was found in print before 1931. |

**Corrected from batch 4.** Al-Duwayhi's history was already held: `duwayhi_tarikh-al-ta-ifa-al-maruniyya-ara_shartuni1890.txt`
(the Bibliotheca Alexandrina scan, October 2026), on the Maronite 1300-1517 shelf. Batch 4's holdings check
looked for "douaih" and "maron" and missed both spellings. Batch 4's file is a second scan of the same
edition. It is kept, and its header and registry entry now name the first scan, whose OCR reads the
preface date as June 1890. Neither scan is clean, and a clean witness is still wanted (Open-Gaps 179,
"a clean Duwayhi"). A re-check of the other twenty-six batch 4 files, by archive id and by title,
found no other duplicate.

## Batch 6 — Europe, 1650-1815 and after

Twenty-five files for ten named gaps of Open-Gaps 158. The batch 5 searchers found the candidates;
this batch re-read every host record and title page, matched every byte count, and compared each body
with the host text. Most of these traditions still have no entry after their first window, so many
files are vendored with no shelf until the entry exists.

| gap | state | file(s) | shelf | unblocks |
|---|---|---|---|---|
| The Transylvanian Unitarians after 1650 | filled | `kereszteny-magveto_kotet-1-hun_kriza-nagy1861.txt`; `unitarian-church-hungary_egyhazi-torveny-a-hazassagi-jogrol-hun_1889.txt`; `unitarian-church-hungary_fotanacs-jegyzokonyvei-1909-1913-hun_boros-csifo.txt` | the 1861 periodical and the 1889 marriage law on `transylvanian-unitarian-church-1660-1906`, tradition; the minutes of 1909-1913 no shelf (after 1906) | The church's own periodical, edited by two Kolozsvár Unitarian ministers, and its own marriage law. The minutes volume binds five sets (1909, 1910 twice, 1912, 1913); the host record names only the 1912 one. |
| The Hutterites after 1785 | outsider only | `wolkan_die-hutterer-deu_1918.txt` | `hutterite-brethren`, context | Wolkan's history to the American colonies, with Hutterite hymns of 1800 and 1849 from Russia in its appendix. The Fraktur OCR is poor. No insider print before 1931 was found. |
| The Waldensians after 1655 | filled | `arnaud_histoire-de-la-glorieuse-rentree-des-vaudois-fra_1880.txt`; `arnaud_glorious-recovery-by-the-vaudois_acland1827.txt`; `muston_israel-of-the-alps-v1_montgomery1866.txt` | Arnaud (both) no shelf; Muston on `the-waldensian-reformed-union` and `waldensians-in-the-alps`, context | The pastor and colonel's own history of the Return of 1689, in French and in Acland's English. The held Perrin volume's 1689 journal is garbled; Arnaud's 1880 text is clean. |
| The Schwenkfelders after 1650 | filled, two of three | `kriebel_genealogical-record-of-the-schwenkfelders_1879.txt`; `seipt_schwenkfelder-hymnology_1909.txt` | no shelf | The Society's family register built on its minister Heebner's record, and Christopher Schultz's chronicle on the 1762 hymn-book. Held back: `lehre-und-ordnungs-regeln` (the sacrament rules, drafted 1838, approved 1858): the upload carries a CC BY-NC-ND licence that does not say what it covers. A call for Mark. The 1762 hymnal itself was not found. |
| The Remonstrants after 1650 | filled | `limborch_compleat-system-of-divinity-v1_1702.txt`; `tideman_remonstrantsche-broederschap-biographische-naamlijst-nld_rogge1905.txt`; `heering_de-remonstranten-gedenkboek-nld_1919.txt` | Limborch no shelf; Tideman and the gedenkboek on `the-remonstrants-and-dort`, context | Limborch's system in English (the title page is missing from the scan, so its date and London imprint are the host's); the Brotherhood's own register of its ministers; its tercentenary essays. |
| The Nordic state churches after 1650 | outsider-leaning histories | `cornelius_svenska-kyrkans-historia-efter-reformationen-swe_1886.txt`; `helweg_den-danske-kirkes-historie-efter-reformationen-v1-dan_1851.txt`, `-v2-dan_1855.txt` | Cornelius and Helweg I on `scandinavian-reformation-kingdoms`, context; Helweg II no shelf | Church histories of Sweden to 1886 and Denmark to 1836. Helweg I's title page reads 1851 on the page image; the OCR says 1831 and the host 1854. Not found: the Church Law of 1686, Pontoppidan's Sandhed, Kingo, Brorson. |
| The Church of Scotland after 1650 | filled | `church-of-scotland_acts-of-the-general-assembly-1638-1842_church-law-society1843.txt`; `wodrow_history-of-the-sufferings-of-the-church-of-scotland-v3_burns1829.txt`; `boston_memoirs-of-the-life-time-and-writings_morrison1899.txt` | the Acts of 1638-1650 on `the-scottish-reformation-and-kirk`, tradition; the rest no shelf | The Assembly's own acts to 1842, with the 1842 Claim of Right; Wodrow's documents of 1679-1683; Boston's own memoir of 1730-1731, which its editor abridged and modernised. |
| English and Welsh Catholics after 1650 | filled in part | `milner_end-of-religious-controversy-part2_1818.txt`; `dodd_church-history-of-england-v4_tierney1841.txt`, `-v5_tierney1843.txt` | Milner on `catholic-church-long-nineteenth-century`, tradition; Dodd-Tierney on `recusant-english-catholicism`, the appendix documents as tradition and the history as context | Milner's own defence of the Catholic Church (1818; the title page reads 1818 on the page image, the OCR 1S16). Dodd-Tierney IV and V reach only 1631 and 1626, so they serve the recusant entry, not the gap after 1650. Kirk's Biographies was not found. |
| The French Reformed after 1787 | filled | `bersier_histoire-du-synode-general-de-l-eglise-reformee-t1-fra_1872.txt`; `vincent_du-protestantisme-en-france-fra_prevost-paradol1860.txt` | no shelf | The general synod of 1872, sitting by sitting; Samuel Vincent's book of 1829. Bersier attended as a Free Church delegate, not a member. |
| The Delaware Swedes after 1786 | filled to 1810 | `clay_annals-of-the-swedes-on-the-delaware_1835.txt`; `holy-trinity-wilmington_records-1697-1773_burr1890.txt` | `swedish-lutherans-of-new-sweden`: the congregations' documents and records to 1786 as tradition, Clay's history as context | The Wilmington congregation's own records from 1697, with vestry minutes to 1810, and the Wicaco wardens' notice of 1684 and the 1765 charter. The records after 1786 wait for an entry. |

**Marsden, the ruling asked for.** P2-G89c read the shelf rule rightly, by the date the letters were
written, not the date the book was printed. But the book's letters begin before 1815 (Parramatta,
26 October 1810; 7 October 1814; Christmas Day 1814), so the book now has two rows: the letters from
1815 on the Victorian Church of England, and those before 1815 on the Restoration and Georgian Church
of England. For the census owner: the Victorian entry's text quotes the two 1814 letters, which fall
before its window.

## Eras 1-3 (70-622): the Who scan's wanted sources and the council records

Twenty-five files for the eras 1-3 rows of `Build/Ministry/Operations/Audits/2026-11-12_wanted-sources-combined/Wanted_Sources.md`:
person rows 1-13, council rows 1-8, and Library-label correction 19. The search record is
`Build/Ministry/Operations/Audits/2026-11-15_library-eras1-3/Search_Log.md`. Every file has a printed imprint of 1930
or earlier, read on its title page. Every modern edition the audits named (Koenen and Römer, Perler, Thomson, Lang,
Dowsett, Schwartz) is in copyright or after 1930, and was replaced by an older public-domain edition or witness, or
reported not found. An Opus reviewer checked every rights row and twelve of the files in depth; its corrections
are in `R1_changes.md` beside the search log.

| want (Wanted Sources row) | state | file(s) | shelf |
|---|---|---|---|
| era 1 row 1 (Mani) | filled with later own texts and two outside witnesses | `manichaean-texts_tuerkische-manichaica-aus-chotscho-1-in-abhandlungen-preuss-akademie-1911-deu-oui_le-coq1911.txt`; `manichaean-texts_traite-manicheen-retrouve-en-chine-pt1-in-journal-asiatique-10-18-fra_chavannes-pelliot1911.txt`; `manichaean-texts_traite-manicheen-retrouve-en-chine-pt2-in-journal-asiatique-11-1-fra_chavannes-pelliot1913.txt`; `manichaean-texts_dr-steins-turkish-khuastuanift-in-jras-1911_le-coq1911.txt`; `mani_mani-seine-lehre-und-seine-schriften-fihrist-deu-ara_fluegel1862.txt`; `biruni_chronology-of-ancient-nations_sachau1879.txt` | manichaeism: the Manichaean texts tradition (the manuscripts are of the 8th-10th centuries); the Fihrist and al-Biruni context. The Cologne Codex, the Kephalaia and the Psalm-Book are in copyright. Müller's Turfan fragments (1904) were not found. |
| era 1 row 2 (Melito of Sardis) | not found | — | The Peri Pascha was first printed in 1940, so no public-domain edition exists. The old fragments are held (Otto 1872, Routh 1846). |
| era 1 row 3 (Ptolemy the Valentinian) | filled | `epiphanius_ancoratus-panarion-haer-1-33-gcs-bd1-grc_holl1915.txt` | valentinian-and-other-gnostic-christianities, tradition (the Letter to Flora) |
| era 1 row 4 (Paul of Samosata) | filled | `paul-samosata_paulus-von-samosata-fragmente-tu44-5-deu-grc_loofs1924.txt`; `paul-samosata_paul-de-samosate-etude-historique-fra-grc_bardy1923.txt` | antiochene-church-third-century, tradition (which fragments are his is disputed) |
| era 2 row 5 (Maron) | filled | `theodoret_opera-omnia-t3-historia-religiosa-pg82-grc-lat_migne1864.txt`; `nau_opuscules-maronites-pt1-syr-fra_1899.txt`; `nau_opuscules-maronites-pt2-syr-fra_1900.txt`; `naironus_dissertatio-de-origine-nomine-ac-religione-maronitarum-lat_1679.txt` | Theodoret's Historia religiosa on the Antiochene entry, tradition; its chapter on Maron on maronite-christianity, antecedent; Nau antecedent on maronite-christianity (date and John Maron's authorship disputed); Naironus none (no Maronite entry covers 1679). Held already: Duwayhi's history in Arabic. |
| era 2 row 6 (Gregory the Illuminator) | filled | `langlois_collection-historiens-armenie-tomes1-2-fra_1867-1869.txt`; `agathangelos_agathangelus-und-die-akten-gregors-von-armenien-grc-deu_lagarde1887.txt` | armenian-christianity-conversion-era, tradition (Agathangelos is usually dated after 451, its date not settled) |
| era 2 row 7 (Ezana of Aksum) | filled | `ezana_deutsche-aksum-expedition-bd4-inschriften-deu-gez-grc_littmann1913.txt`; `budge_history-of-ethiopia-nubia-and-abyssinia-v1_1928.txt` | aksumite-christianity, antecedent (the inscriptions are of the fourth century) |
| era 3 row 8 (Iakob Tsurtaveli) | not found | — | No text of the Martyrdom of Shushanik before 1931 was found in a usable scan. The Armenian version (Venice 1853) is on archive.org with unreadable OCR; not taken. |
| era 3 rows 9, 10 (Vachagan III; Movses Daskhurantsi); council 4 (Aghuen) | filled in part | `movses-daskhurantsi_beitraege-zur-albanischen-geschichte-deu_manandian1897.txt` | church-of-caucasian-albania, tradition (the canons of Aghuen in German). The whole History was not found before 1931. |
| era 3 row 11 (Sabas) | filled in Latin, possibly a paraphrase | `cyril-scythopolis_vita-sabae-in-surius-vitae-sanctorum-v12-december-lat_1880.txt` | chalcedonian-monasticism-judean-desert-and-gaza, context: the volume's heading says the Life may be Metaphrastes's reworking of Cyril. No readable Greek was found. |
| era 3 row 12 (John Malalas) | held already, and filled | `theodore-abu-qurrah_opuscula-with-andrew-crete-malalas-pg97-grc-lat_migne1860.txt` (held; now shelved); `john-malalas_chronographia-grc-lat_dindorf1831.txt` | byzantine-imperial-church-justinianic, context |
| era 3 row 13 (Theophylact Simocatta) | filled | `theophylact-simocatta_historiae-with-genesius-grc-lat_bekker1834.txt` | byzantine-imperial-church-justinianic, context (he writes about 630) |
| council 1 (Rome against Apollinaris, 377) | held already | `mansi_sacrorum-conciliorum-collectio-tomus-3-347-409-lat_welter-facsimile1901.txt` | The notice of the synod, at about file line 47669. No acts survive. |
| council 2 (the Donatist council against Tyconius) | held already, one witness | `augustine_scripta-contra-donatistas-opera-omnia-t9-lat_migne-pl43.txt` | Augustine, Contra epistolam Parmeniani I.1, from about file line 1340. No acts survive. |
| council 3 (Beth Lapat, 484) | none survives | — | The acts were annulled and are lost. |
| councils 5, 7 (Dvin 506 and 554) | filled in German | `ter-minassiantz_armenische-kirche-in-ihren-beziehungen-zu-den-syrischen-kirchen-tu26-deu_1904.txt` | the two Armenian entries of 451-884, tradition (the bishops' letters). The Armenian Book of Letters (1901) has unreadable OCR; not taken. |
| council 6 (Constantinople 536) | filled | `mansi_sacrorum-conciliorum-collectio-tomus-8-492-536-lat_welter-facsimile1901.txt` | byzantine-imperial-church-justinianic, tradition |
| council 8 (Dvin 607-609) | filled, later witness | `brosset_deux-historiens-armeniens-kiracos-oukhtanes-fra_1870.txt` | armenian-christianity-before-the-bagratids and georgian-christianity, context (Ukhtanes writes in the tenth century) |
| correction 19 (Lactantius, CSEL 19, page 411) | filled | `lactantius_divinae-institutiones-epitome-csel19-second-scan-lat_brandt1890.txt` | latin-apologists, tradition |

**Not taken.** Harnack's Brief an die Flora (1904) and de Boor's Simocatta (1887): the OCR of each title page is
unreadable, and the same texts are filled from Holl and Bekker. Every other duplicate, garbled or secondary scan is
listed in the search log. Nothing in this batch is held for Mark.

## Era 4 (622-1054): the Who scan's wanted sources and the council records

Fifty-one files for the era 4 rows of `Build/Ministry/Operations/Audits/2026-11-12_wanted-sources-combined/Wanted_Sources.md`:
41 person sources (5 major) and 7 council records. The search record is
`Build/Ministry/Operations/Audits/2026-11-13_library-era4/Search_Log.md`. Every edition the audits named in
copyright (Kantor, Heppell, Hollingsworth, Franklin, Hamilton, Mango, Lamoreaux, Greenwood and the rest) was
replaced by an older public-domain edition of the same text, or reported not found. Two Opus reviewers checked
every file, and a third rechecked their corrections.

| want (Wanted Sources row) | state | file(s) | shelf |
|---|---|---|---|
| 14 John of Damascus, the Life by John of Jerusalem | filled | `john-damascus_opera-omnia-t1-with-vita-pg94-grc-lat_migne1860.txt` | his works on the Heraclian-iconoclast, iconophile and Melkite entries, tradition; the Life on the Melkite entry, tradition (its date of writing is not given) |
| 15, 21 Anskar; Rimbert | filled | `rimbert_anskar-the-apostle-of-the-north_robinson1921.txt`; `rimbert_vita-anskarii-accedit-vita-rimberti-lat_waitz1884.txt` (the scan stops in ch. 23 of the Life of Rimbert) | `scandinavian-conversion-christianity`, tradition |
| 16 Theodore the Studite | filled | `theodore-studite_opera-omnia-pg99-grc-lat_migne1860.txt` | his works, tradition; Michael's Life, tradition (no date of writing in the volume) |
| 17 Cyril and Methodius | filled in Latin | `ginzel_geschichte-der-slawenapostel-cyrill-und-method-deu-lat_1861.txt`: the Life of Methodius in Latin and John VIII's letters | `cyrillo-methodian-slavic-christianity`: the appendix as tradition, Ginzel's history as context. No Slavonic text with usable OCR was found. |
| 18 Antony and Theodosius of the Caves | filled, later redaction | `kievan-caves-paterik_paterik-kievskago-pecherskago-monastyria-chu_abramovich1911.txt`; the Primary Chronicle (below) | `kievan-rus-christianity`, context (the Cassian redaction of 1462) |
| 19 al-Tabari | filled | `tabari_annales-prima-series-iv-ara-lat_de-goeje1890.txt`; `tabari_annales-prima-series-v-ara-lat_de-goeje1893.txt` | the Heraclian-iconoclast and Silk Road entries, context (outside witness) |
| 20 Ibn Ishaq | filled | `ibn-ishaq_leben-mohammeds-nach-ibn-hischam-deu_weil1864.txt`; `ibn-ishaq_sirat-rasul-allah-ibn-hisham-text-pt1-ara_wuestenfeld1858.txt` | the two Aksumite entries, context (outside witness) |
| 22 Alfred the Great | filled | `alfred-the-great_west-saxon-version-of-gregorys-pastoral-care-ang-eng_sweet1871.txt`; `asser_life-of-king-alfred-lat_stevenson1904.txt`; `asser_life-of-king-alfred_cook1906.txt` | `late-anglo-saxon-christianity`, tradition |
| 23 Dunstan | filled | `dunstan_memorials-of-saint-dunstan-rolls-series-63-lat_stubbs1874.txt` | the same, tradition |
| 24 Æthelwold; the Regularis Concordia | filled | `aelfric_vita-s-aethelwoldi-in-chronicon-monasterii-de-abingdon-v2-lat_stevenson1858.txt`; `wulfstan-winchester_vita-s-ethelwoldi-pl137-lat_migne1853.txt`; `regularis-concordia_de-consuetudine-monachorum-in-anglia-13-lat-ang_logeman1891.txt` | the same, tradition |
| 25 Oswald | filled | `byrhtferth_vita-s-oswaldi-in-historians-of-the-church-of-york-v1-lat_raine1879.txt` | the same, tradition |
| 26 Benedict Biscop and Ceolfrid | filled | `bede_opera-historica-v1-historia-abbatum-lat_plummer1896.txt`; `bede_lives-of-the-first-five-abbots-of-wearmouth-and-jarrow_wilcock1910.txt` | `anglo-saxon-christianity` and `bede-of-jarrow`, tradition |
| 27 Þorgeir; council 15, the Althing | filled, later witness | `ari-thorgilsson_islendingabok-and-kristni-saga-in-origines-islandicae-v1-non-eng_vigfusson-powell1905.txt` | `scandinavian-conversion-christianity`, context (Ari writes 1122-1133) |
| 28 Benedict of Aniane | filled | `benedict-aniane_concordia-regularum-with-ardo-vita-pl103-lat_migne1851.txt` | `carolingian-reform-christianity`, tradition |
| 29-31 Eulogius; Paulus Alvarus; Flora and Maria | filled | `eulogius-cordoba_opera-with-alvarus-vita-eulogii-pl115-lat_migne1852.txt`; `paulus-alvarus_confessio-epistolae-indiculus-luminosus-pl121-lat_migne1852.txt` | `mozarabic-christianity`, tradition |
| 32 Berno | not found | — | The Bibliotheca Cluniacensis (1614) is not on archive.org. PL 133 does not print the testament; the held Cluny Recueil gives its incipit only. |
| 33, 35 Odo of Cluny; Gerald of Aurillac | filled | `odo-cluny_opera-with-john-of-salerno-vita-odonis-pl133-lat_migne1853.txt`; `odo-cluny_occupatio-lat_swoboda1900.txt` | `cluniac-reform-monasticism`, tradition (Nalgod's twelfth-century Life excluded) |
| 34 Odilo of Cluny | filled | `odilo-cluny_opera-with-jotsald-vita-odilonis-pl142-lat_migne1853.txt` | the same, tradition |
| 36 Ibn Hayyan | not found | — | No edition of al-Muqtabis before 1937. |
| 37, 38 Stephen the Younger; Nikephoros I | filled | `nikephoros-cp_opera-with-vita-stephani-iunioris-pg100-grc-lat_migne1860.txt` | Nikephoros's works, tradition; the Life of Stephen, tradition (no date of writing in the volume) |
| 39 Clement of Ohrid | filled | `theophylact-ohrid_opera-t4-with-vita-clementis-pg126-grc-lat_migne1864.txt`; the Latin Life in Ginzel | `cyrillo-methodian-slavic-christianity`, `needs-ruling`: the volume's Monitum disputes the Life's author and date |
| 40 Boris and Gleb | filled, chronicle only | `russian-primary-chronicle_cross1930.txt`; `russian-primary-chronicle_psrl-t1-lavrentevskaia-letopis-orv_1926.txt` | `kievan-rus-christianity`, context. The separate Tale (Abramovich 1916) was not found. |
| 41 Ilarion | filled | `ilarion-kiev_slovo-o-zakone-i-blagodati-chu-rus_gorskii1844.txt` | `kievan-rus-christianity`, tradition |
| 42-45 the Paulicians; Peter of Sicily | filled, hostile witnesses | `peter-of-sicily_historia-manichaeorum-seu-paulicianorum-grc-lat_gieseler1846.txt`; `theophanes-continuatus_historiae-byzantinae-scriptores-post-theophanem-pg109-grc-lat_migne1863.txt` | `paulicians`, context; Peter also on the Macedonian entry as tradition. Peter the Higumen was not found. |
| 46 Michael Keroularios | filled | `will_acta-et-scripta-de-controversiis-ecclesiae-graecae-et-latinae-saec-xi-grc-lat_1861.txt`; `psellos_chronographia-and-orations-in-mesaionike-bibliotheke-v4-grc_sathas1874.txt` | Will on the Macedonian and Gregorian entries, tradition; Psellos context |
| 47 Nicholas I Mystikos | filled | `nicholas-mystikos_epistolae-with-eutychius-alexandrinus-pg111-grc-lat_migne1863.txt`; `vita-euthymii-patriarchae_anecdoton-zur-geschichte-leos-des-weisen-grc-deu_de-boor1888.txt` | the Macedonian entry: the letters as tradition, the Vita Euthymii tradition (no date of writing in the volume) |
| 48 Theophanes the Confessor | filled | `theophanes-confessor_chronographia-pg108-grc-lat_migne1863.txt` | the Heraclian-iconoclast entry, tradition |
| 49 Stepanos of Taron | filled | `stepanos-taron_armenische-geschichte-deu_gelzer-burckhardt1907.txt`; `stepanos-taron_histoire-universelle-deuxieme-partie-fra_macler1917.txt` (book III) | `bagratid-armenian-christianity`, tradition |
| 50 Theodore Abu Qurrah | filled | `theodore-abu-qurrah_opuscula-with-andrew-crete-malalas-pg97-grc-lat_migne1860.txt`; `theodore-abu-qurrah_arabischen-schriften-deu_graf1910.txt` | `melkite-arabic-christianity`, tradition |
| 51 Stephen Mansur | filled in Latin | `acta-sanctorum_martii-tomus-3-lat-grc_palme1865.txt` | the same, tradition. The Greek (Papadopoulos-Kerameus 1907) was not found. |
| 52 Grigol Khandzteli; Giorgi Merchule | filled in Latin | `peeters_histoires-monastiques-georgiennes-in-analecta-bollandiana-36-37-lat-fra_1917-1919.txt` | `georgian-revival-tao-klarjeti`, tradition |
| 53 John the Iberian and John Tornike; Euthymius | filled in Latin | the same | Tao-Klarjeti and the Georgian golden age, tradition on both (their dates against the two windows are not settled) |
| 54 Ishoyahb III | filled | `ishoyahb-iii_liber-epistularum-versio-lat_duval-csco1905.txt` (the Syriac textus is bound in, garbled) | both Church of the East entries, tradition |
| Council 9, Dvin 719 | filled | `john-odzun_opera-arm-lat_aucher1834.txt` | `armenian-christianity-before-the-bagratids`, tradition |
| Councils 10-12, Constantinople 861-880 | filled | `mansi_sacrorum-conciliorum-collectio-tomus-15-lat_welter-facsimile1902.txt`; `-tomus-16-`; `-tomus-17-18-` | the Macedonian entry (and the Carolingian for XV), tradition |
| Council 13, the synod of 843 | not confirmed | `mansi_...-tomus-14-...` held | Not located in Mansi XIV, which covers 814-856. |
| Council 14, Cordoba 852 | filled | `mansi_sacrorum-conciliorum-collectio-tomus-14-lat_welter-facsimile1902.txt` | `mozarabic-christianity` and the Carolingian entry, tradition |

**Not taken.** The 1930 Kyiv Paterik, which prints both 1930 and 1931. The 1930 Loeb Bede, whose record reads
"Permission Granted to Digitize". A CC BY 3.0 upload that may be Graf's Abu Qurrah. All other duplicate
and garbled scans are listed in the search log.

## Era 5 (1054-1300): the Who scan's wanted sources and the council records

Seventy-one files for the era 5 rows of `Build/Ministry/Operations/Audits/2026-11-12_wanted-sources-combined/Wanted_Sources.md`:
person rows 55-98, the four outside-witness rows, and the council rows 16-19. The search record is
`Build/Ministry/Operations/Audits/2026-11-13_library-era5/Search_Log.md`. Every modern edition the audits named
(Powell, Matarasso, Waddell, Tugwell, Armstrong, Upton-Ward, Duggan, Sewter, Tschan, Babcock and Krey, Brooke and the
rest) is in copyright and was replaced by an older public-domain edition of the same text, or reported not found.
Two Opus reviewers checked every file and a third rechecked their corrections.

| want (Wanted Sources row) | state | file(s) | shelf |
|---|---|---|---|
| era 5 row 55 (Innocent III) | filled | `innocent-iii_opera-with-gesta-innocentii-pl214-lat_migne1853.txt` | innocent-iii, latin-papal-church-gregorian, tradition |
| era 5 row 85 (Anselm of Canterbury) | filled | `anselm-canterbury_opera-with-eadmer-vita-anselmi-pl158-lat_migne1864.txt`; `anselm-canterbury_opera-with-eadmer-historia-novorum-pl159-lat_migne1903.txt` | latin-papal-church-gregorian, tradition |
| era 5 row 86 (Thomas Becket) | filled | `thomas-becket_epistolae-with-vitae-pl190-lat_migne1893.txt` | latin-papal-church-gregorian, tradition |
| era 5 row 98 (Peter Abelard) | filled | `abelard_opera-pl178-lat_migne1885.txt` | latin-papal-church-gregorian, tradition |
| era 5 row 67 (Adam of Bremen) | filled | `adam-bremen_gesta-hammaburgensis-ecclesiae-pontificum-lat_schmeidler1917.txt`; `adam-bremen_hamburgische-kirchengeschichte-deu_steinberg1926.txt` | scandinavian-conversion-christianity, tradition |
| era 5 row 84 (William of Tyre); era 5 council row 17 (Council of Jerusalem c.1141) | filled | `william-tyre_historia-rerum-in-partibus-transmarinis-gestarum-v1-lat-fra_rhc1844.txt` | latin-church-of-outremer, tradition |
| era 5 row 84 (William of Tyre) | filled | `william-tyre_historia-rerum-in-partibus-transmarinis-gestarum-v2-lat-fra_rhc1844.txt` | latin-church-of-outremer, tradition; maronite-christianity, context |
| era 5 row 87 (Jacques de Vitry) | filled | `jacques-de-vitry_historia-orientalis-et-occidentalis-lat_1597.txt`; `jacques-de-vitry_briefe-in-zeitschrift-fuer-kirchengeschichte-14-lat-deu_rohricht1894.txt` | latin-church-of-outremer, tradition |
| era 5 council row 16 (Council of Troyes, 1129) | filled | `mansi_sacrorum-conciliorum-collectio-tomus-21-lat_welter-facsimile1903.txt` | military-religious-orders-templars-hospitallers, latin-papal-church-gregorian, tradition |
| era 5 council row 19 (First Council of Lyon, 1245) | filled | `matthew-paris_chronica-majora-v4-rolls-series-57-lat_luard1877.txt` | latin-papal-church-gregorian, context |
| era 5 row 57 (Bernard of Clairvaux); row 66 (Hugh de Payens, the Templars: De laude novae militiae) | filled | `bernard-clairvaux_opera-t1-pl182-lat_migne1879.txt` | cistercian-monasticism, tradition; military-religious-orders-templars-hospitallers, context |
| era 5 row 57 (Bernard of Clairvaux) | filled | `bernard-clairvaux_opera-t2-sermones-pl183-lat_migne1854.txt`; `bernard-clairvaux_life-and-works-v1_eales1889.txt`; `bernard-clairvaux_life-and-works-v2_eales1889.txt`; `bernard-clairvaux_life-and-works-v3_eales1896.txt`; `bernard-clairvaux_life-and-works-v4_eales1896.txt` | cistercian-monasticism, tradition |
| era 5 rows 57 (Bernard of Clairvaux) and 95 (William of St Thierry) | filled | `bernard-clairvaux_opera-t5-with-vita-prima-pl185-lat_migne1855.txt` | cistercian-monasticism, tradition |
| era 5 rows 58 (Robert of Molesme) and 96 (Stephen Harding) | filled | `stephen-harding_charta-caritatis-and-exordium-in-pl166-lat_migne1894.txt` | cistercian-monasticism, tradition |
| era 5 row 59 (Bruno of Cologne) | filled | `le-couteulx_annales-ordinis-cartusiensis-v1-lat_1887.txt`; `bruno-cologne_opera-omnia-with-acta-pl152-lat_migne1879.txt` | carthusian-life, tradition; carthusian-life, context; carthusian-life, tradition (the Commentarium); carthusian-life, context (the Acta) |
| era 5 row 69 (Aelred of Rievaulx) | filled | `aelred-rievaulx_opera-pl195-lat_migne1855.txt` | cistercian-monasticism, tradition |
| era 5 rows 71 (Hugh of Lincoln) and 72 (Adam of Eynsham) | filled | `adam-eynsham_magna-vita-sancti-hugonis-lat_dimock1864.txt` | carthusian-life, tradition |
| era 5 row 60 (Norbert of Xanten) | filled | `norbert-xanten_vita-b-and-sermons-in-pl170-lat_migne1894.txt` | canons-regular-victorine-school, tradition |
| era 5 row 66 (Hugh de Payens) | filled | `templars_la-regle-du-temple-fra-lat_curzon1886.txt`; `templars_die-urspruengliche-templerregel-lat-deu_schnuerer1903.txt` | military-religious-orders-templars-hospitallers, tradition |
| era 5 row 77 (Thomas of Celano) | filled | `thomas-celano_vita-et-miracula-sancti-francisci-lat_d-alencon1906.txt`; `thomas-celano_lives-of-st-francis_howell1908.txt` | the-franciscan-movement, tradition |
| era 5 row 61 (Clare of Assisi) | filled | `clare-assisi_life-of-saint-clare-ascribed-to-thomas-of-celano_robinson1910.txt` | the-franciscan-movement, tradition |
| era 5 row 76 (Brother Leo) | filled | `leo-assisi_scripta-fratris-leonis-lat_lemmens1901.txt`; `speculum-perfectionis_speculum-perfectionis-lat_sabatier1898.txt` | the-franciscan-movement, tradition; the-franciscan-movement, fraticelli-spiritual-franciscan-rigorists, franciscan-order-era-6, tradition |
| era 5 row 78 (Agnes of Prague) | filled | `agnes-prague_some-new-sources-for-the-life-of-blessed-agnes-of-bohemia_seton1915.txt` | the-franciscan-movement, context |
| era 5 row 81 (Gerard de Frachet) | filled | `gerard-de-frachet_vitae-fratrum-lat_reichert1896.txt`; `gerard-de-frachet_lives-of-the-brethren_conway1924.txt` | the-dominican-order, tradition |
| era 5 rows 79 (Jordan of Saxony) and 80 (Diana d'Andalo) | filled | `jordan-saxony_die-briefe-lat-deu_altaner1925.txt` | the-dominican-order, tradition |
| era 5 row 62 (Dominic de Guzman) | filled | `acta-sanctorum_augusti-tomus-1-lat_1750.txt` | the-dominican-order, tradition |
| era 5 row 97 (Humbert of Romans) | filled | `humbert-romans_opera-de-vita-regulari-v1-lat_berthier1888.txt`; `humbert-romans_opera-de-vita-regulari-v2-lat_berthier1889.txt` | the-dominican-order, tradition |
| era 5 row 63 (Thomas Aquinas) | filled | `thomas-aquinas_opera-omnia-t4-summa-theologiae-lat_leonine1888.txt`; `thomas-aquinas_opera-omnia-t5-summa-theologiae-lat_leonine1889.txt`; `thomas-aquinas_opera-omnia-t6-summa-theologiae-lat_leonine1891.txt`; `thomas-aquinas_opera-omnia-t7-summa-theologiae-lat_leonine1892.txt`; `thomas-aquinas_opera-omnia-t8-summa-theologiae-lat_leonine1895.txt`; `thomas-aquinas_opera-omnia-t9-summa-theologiae-lat_leonine1897.txt`; `thomas-aquinas_opera-omnia-t10-summa-theologiae-lat_leonine1899.txt`; `thomas-aquinas_opera-omnia-t11-summa-theologiae-lat_leonine1903.txt`; `thomas-aquinas_opera-omnia-t12-summa-theologiae-lat_leonine1906.txt`; `acta-sanctorum_martii-tomus-1-lat_1735.txt` | the-dominican-order, tradition; the-dominican-order, context |
| era 5 row 64 (Joachim of Fiore) | filled | `joachim-fiore_tractatus-super-quatuor-evangelia-lat_buonaiuti1930.txt`; `acta-sanctorum_maii-tomus-6-lat_1739.txt` | joachimite-current, antecedent (the Tractatus); joachimite-current, context (the Life) |
| era 5 row 65 (Valdes of Lyon) | filled | `stephen-bourbon_anecdotes-historiques-lat_lecoy-de-la-marche1877.txt` | the-waldensians, context |
| era 5 rows 65 (Valdes of Lyon) and 83 (Rainerius Sacconi) | filled | `doellinger_beitraege-zur-sektengeschichte-des-mittelalters-v2-lat-deu_1890.txt` | the-waldensians, cathars-albigensians, context |
| era 5 row 83 (Rainerius Sacconi) | filled | `martene-durand_thesaurus-novus-anecdotorum-v5-lat_1717.txt` | cathars-albigensians, the-waldensians, context |
| era 5 row 82 (Salimbene de Adam) | filled | `salimbene_from-st-francis-to-dante_coulton1907.txt` | joachimite-current, the-franciscan-movement, tradition |
| era 5 row 74 (Marie d'Oignies) | filled | `acta-sanctorum_junii-tomus-5-lat_palme1867.txt` | the-beguines, context |
| era 5 row 75 (Marguerite Porete) | filled | `porete_marguerite-in-revue-historique-54-fra_langlois1894.txt`; `mirror-of-simple-souls_english-version-kirchberger1927.txt` | free-spirit-heresy, the-beguines, context; free-spirit-heresy, the-beguines, tradition |
| era 5 rows 56 (Sava of Serbia) and 92 (Domentijan and Teodosije) | filled | `domentijan_zivot-svetoga-simeuna-i-svetoga-save-chu_danicic1865.txt` | serbian-and-bulgarian-medieval-monasticism, tradition |
| era 5 rows 88 (Anna Komnene) and 89 (Basil the Physician) | filled | `anna-komnene_alexias-grc_reifferscheid1884.txt` | balkan-bogomil-continuation, context |
| era 5 row 89 (Basil the Physician) | filled | `euthymios-zigabenos_narratio-de-bogomilis-grc-lat_gieseler1842.txt` | balkan-bogomil-continuation, context |
| era 5 row 91 (Gregory Pakourianos) | filled | `pakourianos_typikon-in-commentationes-philologae-ienenses-4-grc-lat_mousaios1890.txt` | the-georgian-golden-age, tradition |
| era 5 row 94 (Marco Polo) | filled | `marco-polo_book-of-ser-marco-polo-v1_yule-cordier1903.txt`; `marco-polo_book-of-ser-marco-polo-v2_yule-cordier1903.txt` | church-of-the-east-under-the-mongols, context |
| era 5 row 93 (Cyril III ibn Laqlaq) | filled | `renaudot_historia-patriarcharum-alexandrinorum-jacobitarum-lat_1713.txt` | coptic-christianity-fatimid-to-mamluk, context |
| era 5 outside-witness row 1 (Ibn al-Athir) | filled | `rhc-historiens-orientaux_t1-fra_academie1872.txt`; `rhc-historiens-orientaux_t2-pt1-fra_academie1887.txt` | latin-church-of-outremer, context |
| era 5 outside-witness row 2 (Usama ibn Munqidh) | filled | `usama-ibn-munqidh_arab-syrian-gentleman-and-warrior_hitti1929.txt` | latin-church-of-outremer, context |
| era 5 outside-witness row 3 (Ibn Jubayr) | filled | `ibn-jubayr_rihla-ara_wright1852.txt` | latin-church-of-outremer, context |
| era 5 outside-witness row 4 (Benjamin of Tudela) | filled | `benjamin-tudela_itinerary-heb-eng_adler1907.txt` | latin-church-of-outremer, byzantine-church-after-1054, context |

**Already held, checked this batch (no new file).** Row 68, Nestor: his Life of Theodosius is in the held Abramovich
Paterik, and the chronicle is held; both now also shelved on `kievan-rus-christianity-1054-1240` (the chronicle as
tradition, the Paterik as context). Row 90, George the Hagiorite: his Life is in the held Peeters volume, which was
already on the Georgian golden age entry.

**Not found or not obtainable.** Teodosije's Life of Sava (row 92); Walter Daniel's Life of Ailred (row 70); a Life of
Robert of Molesme (row 58); Clare's Letters, Testament and Process (row 61); Dominic's canonization process (row 62);
Humbert's Legenda (row 97); Waldo's Profession of 1180 as a separate text (row 65); the Old French and Latin Mirror
of Simple Souls (row 75); Cyril III's own record (row 93); Nerses of Lambron's speech at Hromkla (council 18); the
decree text of Lyon I (council 19; Matthew Paris's narrative is held).

**Held for Mark, not vendored.** Hadewijch's Dutch editions (row 73) are on dbnl.org, whose terms give no per-item
licence. Dawes's English Alexiad (row 88) is a transcription whose notice limits it to non-commercial use. The Greek of
Anna Komnene is held.

**Not taken.** Every duplicate, garbled or secondary scan is listed in the search log.

## Eras 4-5, second fill (2026-11-15): the rows left open, and the wants the Who and council batches added

Forty-six files. The wants are the rows the first era 4 and era 5 passes left not found or held, and the Library
wants of Open-Gaps 263, 265, 266, 268 and 272 (one item from 267). The search record is
`Build/Ministry/Operations/Audits/2026-11-15_library-eras4-5/Search_Log.md`. Every file has a printed imprint of 1930
or earlier, read on its title page or, for two volumes, on the scan's page image. Rows in the era 4 and era 5
tables above are not rewritten; where this section changes one, it says so.

| want | state | file(s), with the imprint year | shelf |
|---|---|---|---|
| Open-Gaps 265, Library wanted: Willibald's Life of Boniface (chapter 6, the oak at Geismar) | filled | `willibald_vitae-sancti-bonifatii-mgh-srg-57-lat_levison1905.txt` (1905) | anglo-saxon-christianity, tradition |
| Open-Gaps 265, Library wanted: Willibald's Life of Boniface (chapter 6, the oak at Geismar) | filled | `willibald_life-of-saint-boniface_robinson1916.txt` (1916) | anglo-saxon-christianity, tradition |
| Open-Gaps 266 (major councils, era 4), not held: the Caroline Books, the Frankish answer to Nicaea II | filled | `libri-carolini_caroli-magni-capitulare-de-imaginibus-mgh-concilia-2-suppl-lat_bastgen1924.txt` (1924) | carolingian-reform-christianity, tradition; byzantine-imperial-church-heraclian-iconoclast, context |
| Open-Gaps 266 (major councils, era 4), not held: Hadrian I's reply to Charlemagne on the images | filled | `hadrian-i_epistolae-karolini-aevi-3-mgh-epistolae-5-lat_1899.txt` (1899) | carolingian-reform-christianity, byzantine-imperial-church-heraclian-iconoclast, context |
| Open-Gaps 266 (major councils, era 4), not held: the Anglo-Saxon Chronicle | filled | `anglo-saxon-chronicle_two-of-the-saxon-chronicles-parallel-v1-ang_plummer1892.txt` (1892) | anglo-saxon-christianity, late-anglo-saxon-christianity, tradition |
| Open-Gaps 266 (major councils, era 4), not held: the Anglo-Saxon Chronicle (an English version) | filled | `anglo-saxon-chronicle_newly-translated_gomme1909.txt` (1909) | anglo-saxon-christianity, late-anglo-saxon-christianity, tradition |
| Open-Gaps 266 (major councils, era 4), not held: the Annals of Ulster | filled | `annals-of-ulster_annala-uladh-v1-431-1056-gle-lat-eng_hennessy1887.txt` (1887) | insular-irish-monastic-christianity, medieval-irish-christianity, tradition |
| Open-Gaps 266 (major councils, era 4), not held: Bede's chronicle | filled | `bede_chronica-maiora-in-chronica-minora-3-mgh-aa-13-lat_mommsen1898.txt` (1898) | bede-of-jarrow, anglo-saxon-christianity, tradition |
| Open-Gaps 266 (major councils, era 4), not held: the Latin abridgment of the council of 861 in Deusdedit's collection | filled | `deusdedit_die-kanonessammlung-des-kardinals-deusdedit-bd1-lat-deu_wolf-von-glanvell1905.txt` (1905) | byzantine-imperial-church-macedonian, context; latin-papal-church-gregorian, tradition |
| Open-Gaps 263 and 272: Photius, Contra Manichaeos, a second witness on the Paulicians; Open-Gaps 266: Photius's letters and Mystagogy | filled | `photius_opera-t2-contra-manichaeos-mystagogia-epistolae-pg102-grc-lat_migne1860.txt` (1860) | byzantine-imperial-church-macedonian, tradition; paulicians, context |
| Open-Gaps 266 and 272: the full acts of Nicaea II (Mansi 12-13) | filled | `mansi_sacrorum-conciliorum-collectio-tomus-12-lat_welter-facsimile1901.txt` (1901) | byzantine-imperial-church-heraclian-iconoclast, iconophile-byzantine-monasticism, tradition |
| Open-Gaps 266 and 272: the full acts of Nicaea II (Mansi 12-13) | filled | `mansi_sacrorum-conciliorum-collectio-tomus-13-lat_welter-facsimile1902.txt` (1902) | byzantine-imperial-church-heraclian-iconoclast, iconophile-byzantine-monasticism, tradition |
| Open-Gaps 272: the text of Theodore the Studite's letters to Theophanes the Confessor | filled | `theodore-studite_epistolae-et-fragmenta-in-nova-patrum-bibliotheca-t8-lat_cozza1871.txt` (1871) | iconophile-byzantine-monasticism, byzantine-imperial-church-heraclian-iconoclast, tradition |
| Open-Gaps 266: Ignatius the Deacon's Life of Tarasius, who presided at Nicaea II | filled | `ignatius-deacon_vita-tarasii-in-germanus-tarasius-pg98-grc-lat_migne1860.txt` (1860) | byzantine-imperial-church-heraclian-iconoclast, tradition |
| Open-Gaps 272: Skylitzes and Kedrenos, for the Macedonian-era profiles | filled | `kedrenos-skylitzes_compendium-historiarum-t2-grc-lat_bekker1839.txt` (1839) | byzantine-imperial-church-macedonian, context |
| Open-Gaps 272: Attaleiates, for the Keroularios profile | filled | `attaleiates_historia-grc-lat_bekker1853.txt` (1853) | byzantine-imperial-church-macedonian, byzantine-church-after-1054, context |
| Open-Gaps 272: Zonaras, for the Macedonian-era profiles | filled | `zonaras_epitomae-historiarum-libri-xiii-xviii-t3-grc_buettner-wobst1897.txt` (1897) | byzantine-imperial-church-macedonian, byzantine-imperial-church-heraclian-iconoclast, context |
| Open-Gaps 272: Psellos's accusation of Keroularios before the synod | filled | `psellos_accusation-de-michel-cerulaire-pt1-in-revue-des-etudes-grecques-16-grc-fra_brehier1903.txt` (1903) | byzantine-imperial-church-macedonian, context |
| Open-Gaps 272: Psellos's accusation of Keroularios before the synod | filled | `psellos_accusation-de-michel-cerulaire-pt2-in-revue-des-etudes-grecques-17-grc-fra_brehier1904.txt` (1904) | byzantine-imperial-church-macedonian, context |
| Wanted Sources era 4 row 17 and Open-Gaps 263: the Slavonic Life of Constantine (Cyril) in a readable form | filled | `vita-constantini_die-legende-vom-heiligen-cyrillus-in-denkschriften-wien-19-chu-lat-deu_duemmler-miklosich1870.txt` (1870) | cyrillo-methodian-slavic-christianity, tradition |
| Wanted Sources era 4 row 17 (Cyril and Methodius): the Italian Legend, the Roman account of Cyril | filled | `acta-sanctorum_martii-tomus-2-lat_palme1865.txt` (1865) | cyrillo-methodian-slavic-christianity, context |
| Wanted Sources era 4 row 36 and Open-Gaps 263 (Ibn Hayyan): a later writer who quotes him, since no edition of al-Muqtabis before 1937 exists | filled | `al-maqqari_history-of-the-mohammedan-dynasties-in-spain-v1_gayangos1840.txt` (1840) | mozarabic-christianity, context |
| Wanted Sources era 4 row 36 and Open-Gaps 263 (Ibn Hayyan): a later writer who quotes him, since no edition of al-Muqtabis before 1937 exists | filled | `al-maqqari_history-of-the-mohammedan-dynasties-in-spain-v2_gayangos1843.txt` (1843) | mozarabic-christianity, context |
| Open-Gaps 268: Mansi 22, the acts and constitutions of the Fourth Lateran Council (1215) | filled | `mansi_sacrorum-conciliorum-collectio-tomus-22-lat_welter-facsimile1903.txt` (1903) | latin-papal-church-gregorian, innocent-iii, tradition |
| Open-Gaps 268: Mansi 24, the acts and constitutions of the Second Council of Lyon (1274) | filled | `mansi_sacrorum-conciliorum-collectio-tomus-24-lat_welter-facsimile1903.txt` (1903) | latin-papal-church-gregorian, tradition; byzantine-church-after-1054, context |
| Wanted Sources era 5 council row 19 (Lyon I, 1245): the sentence against Frederick II and a report of the council | filled | `innocent-iv_bulla-depositionis-in-mgh-constitutiones-2-lat_weiland1896.txt` (1896) | latin-papal-church-gregorian, tradition |
| Open-Gaps 268: Pachymeres, the Byzantine account of the union of Lyon and of Michael VIII | filled | `pachymeres_de-michaele-et-andronico-palaeologis-v1-grc-lat_bekker1835.txt` (1835) | byzantine-church-after-1054, tradition |
| Open-Gaps 268: Gregoras, volume 1 (the second volume is held) | filled | `gregoras_byzantina-historia-v1-grc-lat_schopen1829.txt` (1829) | byzantine-church-after-1054, context |
| Open-Gaps 268: John Bekkos's works (PG 141), the unionist patriarch after Lyon II | filled | `bekkos_opera-with-meliteniotes-metochites-pg141-grc-lat_migne1882.txt` (1882) | byzantine-church-after-1054, tradition |
| Open-Gaps 268: George Metochites's Historia dogmatica (the Mai volume) | held already | `theodore-studite_epistolae-et-fragmenta-in-nova-patrum-bibliotheca-t8-lat_cozza1871.txt` (1871) | byzantine-church-after-1054, tradition |
| Open-Gaps 266: Hefele's History of the Councils past 451 (volumes 1-3 are held) | filled | `hefele_history-of-the-councils-v4-451-680_clark1895.txt` (1895) | byzantine-imperial-church-justinianic, byzantine-imperial-church-heraclian-iconoclast, context |
| Open-Gaps 266: Hefele's History of the Councils past 451 (volumes 1-3 are held) | filled | `hefele_history-of-the-councils-v5-626-787_clark1896.txt` (1896) | byzantine-imperial-church-heraclian-iconoclast, context |
| Open-Gaps 268: Fulcher of Chartres, Robert the Monk and the Gesta Francorum, witnesses of the Council of Clermont (1095) | filled | `rhc-historiens-occidentaux_t3-fulcher-robert-raymond-gesta-francorum-lat_academie1866.txt` (1866) | latin-church-of-outremer, latin-papal-church-gregorian, tradition; latin-church-of-outremer, latin-papal-church-gregorian, tradition |
| Open-Gaps 268: Guibert of Nogent, a witness of the Council of Clermont (1095) | filled | `rhc-historiens-occidentaux_t4-baldric-guibert-albert-lat_academie1879.txt` (1879) | latin-church-of-outremer, latin-papal-church-gregorian, tradition |
| Open-Gaps 268: an English of the eyewitness accounts of Clermont and the First Crusade | filled | `krey_first-crusade-accounts-of-eye-witnesses-and-participants_1921.txt` (1921) | latin-church-of-outremer, latin-papal-church-gregorian, tradition |
| Open-Gaps 268: Urban II's letters (PL 151), with the versions of his Clermont speech | filled | `urban-ii_epistolae-et-privilegia-with-orationes-claromontanae-pl151-lat_migne1853.txt` (1853) | latin-papal-church-gregorian, tradition |
| Open-Gaps 268: Roger of Wendover, an English monk's account of the Fourth Lateran Council | filled | `roger-wendover_flores-historiarum-v2-rolls-series-84-lat_hewlett1887.txt` (1887) | latin-papal-church-gregorian, context |
| Open-Gaps 268: Richard of San Germano, a notary's account of the Fourth Lateran Council | filled | `richard-san-germano_chronica-in-usum-scholarum-lat_pertz1864.txt` (1864) | latin-papal-church-gregorian, context |
| Open-Gaps 268: the Lyon II decree Religionum diversitatem and the other Lyon constitutions taken into the Liber Sextus | filled | `corpus-iuris-canonici_pars-2-decretalium-collectiones-lat_friedberg1881.txt` (1881) | latin-papal-church-gregorian, tradition |
| Open-Gaps 268: Innocent III's summons to the Fourth Lateran Council, Vineam Domini (1213) | filled | `innocent-iii_opera-t3-regesta-xiii-xvi-pl216-lat_migne1891.txt` (1891) | innocent-iii, latin-papal-church-gregorian, tradition |
| Open-Gaps 263: Innocent III's own works (De miseria, PL 217); Open-Gaps 268: his sermons at the Fourth Lateran Council | filled | `innocent-iii_opera-t4-sermones-de-contemptu-mundi-pl217-lat_migne1890.txt` (1890) | innocent-iii, latin-papal-church-gregorian, tradition |
| Wanted Sources era 5 row 58 (Robert of Molesme): his Life and letters | filled | `robert-molesme_vita-et-epistolae-in-pl157-lat_migne1899.txt` (1899) | cistercian-monasticism, tradition |
| Wanted Sources era 5 row 58 (Robert of Molesme); Open-Gaps 267: Raymond of Capua's full Legenda of Catherine of Siena | filled | `acta-sanctorum_aprilis-tomus-3-lat_palme1866.txt` (1866) | cistercian-monasticism, tradition; latin-papal-church-avignon-to-lateran-v, tradition |
| Wanted Sources era 5 row 61 (Clare of Assisi): the four letters to Agnes of Prague in a readable print | filled | `acta-sanctorum_martii-tomus-1-lat_palme1865.txt` (1865) | the-franciscan-movement, tradition |
| Wanted Sources era 5 row 61 (Clare of Assisi): the process of canonization | filled | `clare-assisi_processo-di-canonizzazione-in-archivum-franciscanum-historicum-13-ita-lat_lazzeri1920.txt` (1920) | the-franciscan-movement, tradition |
| Wanted Sources era 5 row 70 and Open-Gaps 263 (Walter Daniel): his Letter to Maurice and extracts from his Life of Ailred | filled | `walter-daniel_ailred-of-rievaulx-and-his-biographer-walter-daniel-lat-eng_powicke1922.txt` (1922) | cistercian-monasticism, tradition |
| Wanted Sources era 5 row 73 and Open-Gaps 263 (Hadewijch): the 1875 edition on dbnl, the only one Mark allows | filled | `hadewijch_werken-1-gedichten-dum_heremans-ledeganck1875.txt` (1875) | the-beguines, tradition |
| Wanted Sources era 4 row 32 (Berno's testament) | held already | `odo-cluny_opera-with-john-of-salerno-vita-odonis-pl133-lat_migne1853.txt` | The testament is printed whole at about file line 67228. The first era 4 pass missed it. |
| Wanted Sources era 5 council row 19 (Lyon I): the sentence against Frederick II | held already, and filled | `matthew-paris_chronica-majora-v4-rolls-series-57-lat_luard1877.txt` | Matthew Paris copies the bull at about file line 29303; the MGH text is above. The council's other constitutions (Mansi XXIII) were not found. |
| Open-Gaps 268: Mansi tomus 20 (Clermont) | held for Mark | — | One scan on archive.org; it has no imprint leaf, so the printing's year cannot be read (the host says 1902). |
| Open-Gaps 268: Bernold of Constance | not taken | — | PL 148 holds his chronicle, but no year can be read on its OCR title page. |
| Open-Gaps 268: Akropolites; Peter of Vaux-de-Cernay; Salimbene's Latin; "Zelus fidei"; Hefele-Leclercq V-VI | not found or not taken | — | Akropolites: both scans unusable. Peter: volume I (1926) stops at 1212. Salimbene: no Latin before 1931 on archive.org. Zelus fidei: not in the Liber Sextus. Hefele-Leclercq: found, not taken (a modern historian). |
| Open-Gaps 263 and 272: Peter the Higumen | not found | — | Gieseler's Appendix (1849) is not on archive.org; PG 104 does not print him. |
| Wanted Sources era 4 row 51 (Stephen Mansur): the Greek Passion | not found | — | Papadopoulos-Kerameus (1907) is not on archive.org. The Latin is held. |
| Wanted Sources era 4 row 40 (Boris and Gleb): the Tale | not found | — | The 1899 printing found has unreadable Slavonic; Abramovich, Sreznevskii and Bodianskii are not on archive.org. |
| Wanted Sources era 4 row 17: a Life of Methodius in Slavonic; any readable Slavonic | not found | — | The Latin Life of Methodius (Ginzel) is held. |
| Wanted Sources era 4 council row 13 (the synod of 843) | not found | — | Uspenskii (1893) is not on archive.org. |
| Open-Gaps 272: a readable Greek Life of Euthymius; the Kyiv archive volume on Ilarion; Cummian's Easter letter (266) | not taken | — | Every scan found garbles the wanted text. |
| Open-Gaps 272: an English of Theophanes, Stephen the Younger, Nikephoros, Nicholas Mystikos, Peter of Sicily, Ilarion; Open-Gaps 265: an English of Maximus's trial | none before 1931 | — | No English of these was printed by 1930, so none can be taken under the date rule. |
| Wanted Sources era 5 row 92 (Teodosije); row 89 (Basil the Physician: Cosmas the Priest, as context); council row 18 (Nerses of Lambron's speech) | not found | — | Daničić (1860), Popruzhenko (1907), Aucher (1812) and Neumann (1834) are not on archive.org. |
| Wanted Sources era 5 rows 62 and 97 (Dominic's process; Humbert's Legenda) | not found | — | Quétif and Échard I (1719) describes the inquiries and does not print them in the scan read. |
| Wanted Sources era 5 row 61 (Clare): the Testament; the letters in her own Latin | not found | — | Seraphicae legislationis textus originales (1897) is not on archive.org. |
| Wanted Sources era 5 rows 65 (Valdes's profession), 75 (the French and Latin Mirror), 93 (Cyril III's own record) | none before 1931 | — | Not searched again: each was first printed after 1930. |

**Changes to the rows above.** Era 4 row 32 (Berno): held, not "not found". Era 4 row 36 (Ibn Hayyan): a later
witness is now held; his own book stays not found. Era 4 row 17: the Life of Constantine is now held in Latin. Era 5
rows 58, 61, 70 and 73 (Robert of Molesme, Clare, Walter Daniel, Hadewijch) and council row 19 are filled in part,
as the table says. Hadewijch is no longer held for Mark: the 1875 edition is vendored, with dbnl's own
public-domain notice for that title recorded in the search log.

**Not taken.** Every duplicate, garbled or secondary scan is listed in the search log.

## Eras 4-5, third fill (2026-11-15): the wants of the era 4 Who batches 9 and 11

Seven files. The wants are the Library items of Open-Gaps 269 and 279, which the second fill did not take up. The
search record is `Build/Ministry/Operations/Audits/2026-11-15_library-eras4-5-b/Search_Log.md`. Every file has a
printed imprint of 1930 or earlier, read on its title page or, for Matthew of Edessa, on the scan's page image.
Rows in the tables above are not rewritten.

| want | state | file(s), with the imprint year | words | shelf |
|---|---|---|---:|---|
| Open-Gaps 269: an English of John of Damascus's speeches on the images | filled | `john-damascus_on-holy-images-with-three-sermons-on-the-assumption_allies1898.txt` (1898) | 44,731 | byzantine-imperial-church-heraclian-iconoclast, iconophile-byzantine-monasticism, melkite-arabic-christianity, tradition; the three sermons on melkite-arabic-christianity, tradition |
| Open-Gaps 269: the acts of Nicaea II | filled in English (Mansi XII-XIII held already) | `mendham_seventh-general-council-second-of-nicaea_1850.txt` (1850) | 307,103 | byzantine-imperial-church-heraclian-iconoclast, iconophile-byzantine-monasticism, tradition |
| Open-Gaps 269: a complete Life of Rimbert | filled | `mgh-ss-2_scriptores-tomus-2-with-vita-rimberti-vita-anskarii-lat_pertz1829.txt` (1829) | 544,945 | scandinavian-conversion-christianity, tradition |
| Open-Gaps 269: the Life of Constantine (Cyril) in any language | held already | the Latin of Dümmler and Miklosich (1870), second fill | | |
| Open-Gaps 269: the Slavonic Life of Methodius | not found | Miklosich (1870) and Dümmler in the Archiv 13 (1854) are not on archive.org | | |
| Open-Gaps 269: any work of Clement of Ohrid, and the short Life | not found | Tunitskii (1918) found and not taken: it prints the long Life, held already, and its OCR is garbled | | |
| Open-Gaps 279: an Armenian text or English of Stepanos of Taron | not found | the one Armenian upload has no readable imprint or text; the German and the French part 2 are held | | |
| Open-Gaps 279: Matthew of Edessa | filled in French | `matthew-of-edessa_chronique-with-gregory-the-priest-fra_dulaurier1858.txt` (1858) | 171,092 | armenian-cilicia, tradition; bagratid-armenian-christianity, context |
| Open-Gaps 279: an English of Eulogius and Alvarus | none printed by 1930 | the Latin is held (PL 115, PL 121) | | |
| Open-Gaps 279: the Arabic sources for Cordoba, Ibn Hayyan among them | held as a later witness | al-Maqqari in Gayangos (1840-43), second fill | | |
| Open-Gaps 279: Abu Qurrah (no English printed by 1930) | filled, his own Arabic with a Latin translation | `theodore-abu-qurrah_de-cultu-imaginum-ara-lat_arendzen1897.txt` (1897) | 31,104 | melkite-arabic-christianity, tradition |
| Open-Gaps 279: Abu Qurrah, Bacha's French of a second treatise | held for Mark | the title page names Tripoli and Rome and no year; 1905 is the preface date | | |
| Open-Gaps 279: Michael the Syrian's Book XII | filled | `michael-the-syrian_chronique-tome3-livres-xii-xxi-fra_chabot1905.txt` (1905) | 271,262 | syriac-orthodox-west-syriac-christianity, tradition |
| Open-Gaps 279: the Greek Passion of the Mar Saba martyrs (Papadopoulos-Kerameus 1907) | not found | not searched again; the second fill records the search | | |
| Open-Gaps 279: the Life of Stephen the Wonderworker | filled in Latin | `acta-sanctorum_julii-tomus-3-lat-grc_palme1868.txt` (1867 on the title page, 1868 on the engraved title) | 865,324 | melkite-arabic-christianity, tradition |

**Cautions for profile writers.**
- John of Damascus (Allies 1898): a translation. The Greek is in PG 94, which the OCR cannot give for quotation.
- Nicaea II (Mendham 1850): the translator wrote against the council. His introduction and his notes, with
  extracts from the Caroline Books, share the pages of the acts; a quotation must be the council's text, not a
  note. Sessions V to VIII were not mapped.
- The Life of Rimbert (Pertz 1829): its author is not named; Pertz's preface says it was written in the time of Rimbert's successor Adalgar, by a cleric of Bremen or a monk of Corvey. The chapter count is 25. The footnote
  apparatus is garbled; the text reads cleanly with small OCR errors.
- Matthew of Edessa (Dulaurier 1858): a French translation, with the continuation of Gregory the Priest from
  about file line 14011 and Dulaurier's notes after the text. The chronicle was written after the Bagratid years
  it begins with.
- Abu Qurrah (Arendzen 1897): only Arendzen's Latin can be read; no phrase of the Arabic can be quoted from this
  file. The first 24 lines of the host text are the uploader's cover sheet.
- Michael the Syrian (Chabot 1905): a French translation; the Syriac is not held. Footnotes run in with the text.
- Stephen the Sabaite (Acta Sanctorum 1867-68): Boschius's Latin translation of a Greek Life headed as lacking its
  beginning; the Greek column cannot be read. The Bollandists' notes stand between the chapters.

## Era 6 (1300-1517), filled (2026-11-15): the Who scan's wanted sources and the wants the Who and council batches added

Twenty-seven files. The wants are the era 6 rows of
`Build/Ministry/Operations/Audits/2026-11-12_wanted-sources-combined/Wanted_Sources.md` (person rows 99-112 and
outside-witness rows 5-9) and the Library wants of Open-Gaps 264, 267 and 271. The search record is
`Build/Ministry/Operations/Audits/2026-11-15_library-era6/Search_Log.md`. Every file has a printed imprint of 1930
or earlier, read on its title page or, for ten volumes, on the scan's page image. Three wants were held already.

| want | state | file(s), with the imprint year | shelf |
|---|---|---|---|
| era 6 row 99, Joseph of Volotsk (major): his monastic rule and an early Life | filled | `macarius-metropolitan_velikie-minei-chetii-september-1-13-chu_arkheograficheskaia-kommissiia1868.txt` (1868) | muscovite-monastic-christianity, tradition |
| era 6 row 99, Joseph of Volotsk: the Prosvetitel; Nevostruev's Life | not found | — | Not on archive.org under eight title and author queries. |
| era 6 row 100, Jakoubek of Stříbro (major): a tract of his own on the chalice | filled | `hardt_magnum-oecumenicum-constantiense-concilium-t3-lat_1698.txt` (1698) | the-hussite-and-bohemian-brethren-movement, tradition; latin-papal-church-avignon-to-lateran-v, context |
| era 6 row 101, Zara Yaqob (major): the chronicle of his reign in a usable translation | held already | `zara-yaqob_chroniques-zara-yaeqob-baeda-maryam-gez-fra_perruchon1893.txt` | A running French translation stands beneath the Ge'ez, from about file line 2922. The file's header said there was none; corrected. |
| era 6 row 101, Zara Yaqob: the Mashafa Berhan and Mashafa Milad | not found | — | Dillmann (1884) is not on archive.org; the editions are of the 1960s. |
| era 6 row 102, Ewostatewos (major): the Gadla Ewostatewos | not found | — | Turaev (1905, 1906) is not on archive.org; the Latin of 1955 is out by date. |
| era 6 row 103, Margery Kempe: the short treatise printed about 1501 | held already | `cell-of-self-knowledge_seven-early-english-mystical-treatises_gardner1910.txt` | The only part of her Book printed by 1930. |
| era 6 row 103, Margery Kempe: the Book itself | none before 1931 | — | First printed 1936 and 1940. |
| era 6 row 104, Henry Pomerius: De origine monasterii Viridisvallis, with the Life of Ruusbroec | filled | `pomerius_de-origine-monasterii-viridisvallis-in-analecta-bollandiana-4-lat_1885.txt` (1885) | devotio-moderna-brethren-of-the-common-life, rhineland-mysticism-and-the-friends-of-god, tradition |
| era 6 row 105, Raymond of Capua: his Life of Catherine of Siena | filled (eras 4-5 batch) | `acta-sanctorum_aprilis-tomus-3-lat_palme1866.txt` (1866) | latin-papal-church-avignon-to-lateran-v, tradition |
| era 6 row 106, John of Capistrano: the Life by Nicholas of Fara | filled | `acta-sanctorum_octobris-tomus-10-lat_bruxelles1861.txt` (1861) | observant-reform-and-popular-preaching, tradition |
| era 6 row 107, Euthymius of Tarnovo: his own Life of Hilarion of Moglena | filled | `euthymius-tarnovo_werke-des-patriarchen-von-bulgarien-chu-deu_kaluzniacki1901.txt` (1901) | serbian-and-bulgarian-medieval-monasticism, tradition |
| era 6 row 107, Euthymius of Tarnovo: Gregory Tsamblak's Praise | held for Mark | — | The only scan is the Variorum reprint of 1971 of Kałużniacki's 1901 edition. |
| era 6 row 108, Teodosij of Trnovo: the Life by Kallistos | not found | — | Zlatarski (1904) and Bodianskii (1860) are not on archive.org. |
| era 6 row 109, Stephen of Perm: the Life by Epiphanius the Wise | not found | — | Druzhinin (1897) and Kushelev-Bezborodko (1862) are not on archive.org; two retellings of 1896 not taken. |
| era 6 row 110, Kirill of Beloozero: his own letters and testament | filled | `akty-istoricheskie_t1-1334-1598-rus_arkheograficheskaia-kommissiia1841.txt` (1841) | muscovite-monastic-christianity, tradition |
| era 6 row 110, Kirill of Beloozero: the Life by Pachomius | not found | — | Yablonskii (1908) and Nikolskii are not on archive.org. |
| era 6 row 111, Zosima and Savvatii of Solovki: their Lives | not found | — | Only a retelling of 1897 and descriptions of the monastery; not taken. |
| era 6 row 112, Estifanos of Gwendagwende: his Acts | none found before 1931 | — | The court's account of the revolt is in the held Perruchon volume, at about file line 6720. |
| outside-witness row 5, Rashid al-Din | not found | — | Quatremère (1836) is not on archive.org; the Persian scans cannot be read. |
| outside-witness row 6, Ibn Battuta: the Travels in Arabic with French | filled | `ibn-battuta_voyages-v1-ara-fra_defremery-sanguinetti1853.txt` (1853) | byzantine-church-palaiologan, st-thomas-christians-1300-1517, context |
| outside-witness row 6, Ibn Battuta: the Travels in Arabic with French | filled | `ibn-battuta_voyages-v2-ara-fra_defremery-sanguinetti1854.txt` (1854) | byzantine-church-palaiologan, st-thomas-christians-1300-1517, context |
| outside-witness row 6, Ibn Battuta: the Travels in Arabic with French | filled | `ibn-battuta_voyages-v3-ara-fra_defremery-sanguinetti1855.txt` (1855) | byzantine-church-palaiologan, st-thomas-christians-1300-1517, context |
| outside-witness row 6, Ibn Battuta: the Travels in Arabic with French | filled | `ibn-battuta_voyages-v4-ara-fra_defremery-sanguinetti1858.txt` (1858) | byzantine-church-palaiologan, st-thomas-christians-1300-1517, context |
| outside-witness row 7, Ibn Khaldun: the Prolegomena in French | filled | `ibn-khaldun_prolegomenes-pt1-fra_de-slane1863.txt` (1863) | coptic-christianity-fatimid-to-mamluk, context |
| outside-witness row 7, Ibn Khaldun: the Prolegomena in French | filled | `ibn-khaldun_prolegomenes-pt2-fra_de-slane1865.txt` (1865) | coptic-christianity-fatimid-to-mamluk, context |
| outside-witness row 7, Ibn Khaldun: the Prolegomena in French | filled | `ibn-khaldun_prolegomenes-pt3-fra_de-slane1868.txt` (1868) | coptic-christianity-fatimid-to-mamluk, context |
| outside-witness row 7, Ibn Khaldun: the history of the Berbers in French | filled | `ibn-khaldun_histoire-des-berberes-v1-fra_de-slane1852.txt` (1852) | coptic-christianity-fatimid-to-mamluk, context |
| outside-witness row 7, Ibn Khaldun: the history of the Berbers in French | filled | `ibn-khaldun_histoire-des-berberes-v2-fra_de-slane1854.txt` (1854) | coptic-christianity-fatimid-to-mamluk, context |
| outside-witness row 7, Ibn Khaldun: the history of the Berbers in French | filled | `ibn-khaldun_histoire-des-berberes-v3-fra_de-slane1856.txt` (1856) | coptic-christianity-fatimid-to-mamluk, context |
| outside-witness row 7, Ibn Khaldun: the history of the Berbers in French | filled | `ibn-khaldun_histoire-des-berberes-v4-fra_de-slane1856.txt` (1856) | coptic-christianity-fatimid-to-mamluk, context |
| outside-witness row 8, Abu'l-Fida | held already | `rhc-historiens-orientaux_t1-fra_academie1872.txt` | A French summary from his Annals, about file lines 6059-23098, and his autobiography, about 23101-24592. Reiske's five Latin volumes (1789-94) are located, not taken. |
| outside-witness row 9, al-Qalqashandi: on Egypt | filled | `qalqashandi_geographie-und-verwaltung-von-aegypten-deu_wuestenfeld1879.txt` (1879) | coptic-christianity-fatimid-to-mamluk, context |
| outside-witness row 9, al-Qalqashandi: on Syria | filled | `qalqashandi_la-syrie-a-l-epoque-des-mamelouks-fra_gaudefroy-demombynes1923.txt` (1923) | coptic-christianity-fatimid-to-mamluk, context |
| Open-Gaps 264, Library wanted: Rolle's English Psalter commentary | filled | `rolle_psalter-or-psalms-of-david-and-certain-canticles-enm-lat_bramley1884.txt` (1884) | the-english-mystics-and-devout, tradition |
| Open-Gaps 264, Library wanted: Tauler's Middle High German sermons | filled in part | `tauler_ausgewaehlte-predigten-gmh_naumann1914.txt` (1914) | rhineland-mysticism-and-the-friends-of-god, tradition. A selection after Vetter; Vetter (1910) is not on archive.org. |
| Open-Gaps 264, Library wanted: Kempis's Latin Life of Gerard (Pohl's volume 7) | not found | — | Pohl 7 is not on archive.org; the printings of 1615 and 1728 cannot be read at that place. |
| Open-Gaps 267, Library wanted: Books VI to VIII of Bridget's Revelations | filled | `birgitta_revelationes-libri-vi-viii-tomus-2-lat_duranti1628.txt` (1628) | latin-papal-church-avignon-to-lateran-v, tradition |
| Open-Gaps 267, Library wanted: Bridget's Life by her confessors | filled | `birgitta_vita-auctoribus-petro-et-petro-in-scriptores-rerum-suecicarum-3-lat_annerstedt1876.txt` (1876) | latin-papal-church-avignon-to-lateran-v, tradition |
| Open-Gaps 267, Library wanted: Maffeo Vegio's Life of Bernardino | filled | `acta-sanctorum_maii-tomus-5-lat_palme1866.txt` (1866) | observant-reform-and-popular-preaching, tradition |
| Open-Gaps 267, Library wanted: Ockham's philosophical works | filled in part | `ockham_de-sacramento-altaris-lat-eng_birch1930.txt` (1930) | franciscan-order-era-6, tradition. One treatise. |
| Open-Gaps 267, Library wanted: Ockham's Latin letter to the chapter at Assisi | held for Mark | — | Müller's text (1884) is on archive.org only in a Johnson Reprint. |
| Open-Gaps 267, Library wanted: Kallistos's Life of Gregory of Sinai; Palamas's letter from captivity; Petit's article on the Synodikon of Thessalonica | not found | — | Pomialovskii (1894), Neos Hellenomnemon and Échos d'Orient 18 are not on archive.org. |
| Open-Gaps 267, Library wanted: the full Triads of Palamas | none before 1931 | — | First printed 1959. |
| Open-Gaps 271, not held: Basel's session acts (Mansi 29) | filled | `mansi_sacrorum-conciliorum-collectio-tomus-29-1431-1434-lat_welter-facsimile1904.txt` (1904) | latin-papal-church-avignon-to-lateran-v, tradition; the-hussite-and-bohemian-brethren-movement, context |
| Open-Gaps 271, not held: Basel's documents (Mansi 30) | filled | `mansi_sacrorum-conciliorum-collectio-tomus-30-1431-1439-lat_welter-facsimile1904.txt` (1904) | latin-papal-church-avignon-to-lateran-v, tradition; the-hussite-and-bohemian-brethren-movement, context |
| Open-Gaps 271, not held: a Russian text of the time on the rejection of Florence | filled | `akty-istoricheskie_t1-1334-1598-rus_arkheograficheskaia-kommissiia1841.txt` (1841) | muscovite-monastic-christianity, tradition; byzantine-church-palaiologan, context. Simeon of Suzdal's account was not found. |
| Open-Gaps 271, not held: a witness of the time to the burning of Wyclif's bones | not found | — | Not in the Fasciculi zizaniorum (1858). |
| Open-Gaps 271, not held: a roll of Basel's members; a signed list for Haec sancta; Luther at Leipzig; Coptic, Ethiopian and Armenian texts on Florence | not searched | — | Left for a later batch. |

**Cautions the filled texts carry.** Joseph of Volotsk's Life and rule, Kirill's letters and Euthymius's Life of
Hilarion are in Church Slavonic or old Russian with no translation held, and the OCR has steady letter errors. The
Life of Joseph names no author in the OCR. Ibn Battuta, Ibn Khaldun and al-Qalqashandi are held in their
translators' French and German, not their own words; none was read in depth for its passages on Christians.
Jakoubek's tract is kept inside his opponent's reply. Tauler is a selection. Vegio's Life has approximate bounds.

**Not taken.** Every duplicate, reprint, retelling and unreadable scan is listed in the search log.

## Era 7 (1517-1650), filled (2026-11-15): the Who scan's wanted sources, the outside witnesses and the council records

Fifty-seven files. The wants are the era 7 rows of
`Build/Ministry/Operations/Audits/2026-11-12_wanted-sources-combined/Wanted_Sources.md` (person rows 113-120,
outside-witness rows 10-27 and council row 22), the two council rows the era 7 council batch queued here (the
Marburg Colloquy and the Diet of Worms), and the Library items of Open-Gaps 273 and 278. The search record is
`Build/Ministry/Operations/Audits/2026-11-15_library-era7/Search_Log.md`. Every file has a printed imprint of 1930
or earlier, read on its title page or, for sixteen volumes, on the scan's page image. One want was held already.

| want | state | file(s), with the imprint year | shelf |
|---|---|---|---|
| era 7 row 113, Katharina Schütz Zell: her letter to the citizens of Strasbourg and her answer to Rabus (1557) | filled | `fuesslin_beytraege-kirchen-reformations-geschichten-schweitzerland-theil-5-deu_1753.txt` (1753) | lutheran-wittenberg-and-its-congregations, tradition |
| era 7 row 113, Katharina Schütz Zell: a Life with extracts from her letters and her hymn-book preface | filled | `roehrich_mittheilungen-geschichte-evangelischen-kirche-des-elsasses-bd-3-deu_1855.txt` (1855) | lutheran-wittenberg-and-its-congregations, context |
| era 7 row 113, Katharina Schütz Zell: the Entschuldigung of 1524; the hymn-book preface in full; the Miserere exposition of 1558 | not found | — | No scan under four title and author queries. Wackernagel's Bibliographie (1855) prints the hymn book's title only. |
| era 7 row 114, Marie Dentière: the Epistre tres utile (1539) | filled in part | `herminjard_correspondance-des-reformateurs-t5-1538-1539-fra-lat_1878.txt` (1878) | the-reformed-cities-zurich-and-geneva, tradition The editor left passages out. |
| era 7 row 114, Marie Dentière: an opponent's account of her | filled | `jussie_le-levain-du-calvinisme-fra_revilliod-fick1853.txt` (1853) | the-tridentine-church, tradition; the-reformed-cities-zurich-and-geneva, context |
| era 7 row 114, Marie Dentière: the whole Epistre; La guerre et deslivrance (Rilliet 1881) | not found | — | Tome 20 of the Geneva society's Mémoires et documents is not on archive.org. |
| era 7 row 115, Jerónimo Gracián: a work of his own | filled in part | `gracian_tratado-de-la-redempcion-de-captivos-spa_momarte1609.txt` (1609) | carmelite-reform-and-spanish-mystics, tradition A treatise that speaks of his captivity; not the Peregrinación. |
| era 7 row 115, Jerónimo Gracián: the Peregrinación de Anastasio | not found | — | No scan of the Burgos printing of 1905; the edition of 1932-33 is out by date. Mármol's Life (1619) is on archive.org with OCR that cannot be read; not taken. |
| era 7 row 116, Fabian Fucan: Myotei mondo and Ha Daiusu | none found before 1931 | — | Nothing in a Western language; two Japanese-only volumes of 1923 and 1925 were seen and not taken. |
| era 7 row 117, Xu Guangqi: a writing of his own in translation | filled | `chinese-repository_v19-no3-march-1850-paul-su-apology.txt` (1850) | china-mission-born-christianity, tradition One memorial, in English. |
| era 7 row 118, Guaman Poma de Ayala: the Nueva corónica | none before 1931 | — | First reproduced in 1936. Pietschmann's paper of 1908 is not on archive.org. |
| era 7 row 119, Bartolomé de las Casas: the Historia de las Indias | filled | `las-casas_historia-de-las-indias-t1-spa_fuensanta-sancho-rayon1875.txt` (1875) | new-spain-and-andes-mission-born-christianity, tradition |
| era 7 row 119, Bartolomé de las Casas: the Historia de las Indias | filled | `las-casas_historia-de-las-indias-t2-spa_fuensanta-sancho-rayon1875.txt` (1875) | new-spain-and-andes-mission-born-christianity, tradition |
| era 7 row 119, Bartolomé de las Casas: the Historia de las Indias | filled | `las-casas_historia-de-las-indias-t3-spa_fuensanta-sancho-rayon1875.txt` (1875) | new-spain-and-andes-mission-born-christianity, tradition |
| era 7 row 119, Bartolomé de las Casas: the Historia de las Indias | filled | `las-casas_historia-de-las-indias-t4-spa_fuensanta-sancho-rayon1876.txt` (1876) | new-spain-and-andes-mission-born-christianity, tradition |
| era 7 row 119, Bartolomé de las Casas: the Historia de las Indias | filled | `las-casas_historia-de-las-indias-t5-spa_fuensanta-sancho-rayon1876.txt` (1876) | new-spain-and-andes-mission-born-christianity, tradition |
| era 7 row 119, Bartolomé de las Casas: the Brevísima relación in Spanish | filled | `las-casas_brevissima-relacion-de-la-destruycion-de-las-indias-spa_cadiz1821.txt` (1821) | new-spain-and-andes-mission-born-christianity, tradition |
| era 7 row 119, Bartolomé de las Casas: the Brevísima relación in English, with a Life | filled | `macnutt_bartholomew-de-las-casas-his-life-apostolate-and-writings_1909.txt` (1909) | new-spain-and-andes-mission-born-christianity, tradition; new-spain-and-andes-mission-born-christianity, context |
| era 7 row 120, Bernardino de Sahagún: the Historia general, Books I-XI | filled | `sahagun_historia-general-de-las-cosas-de-nueva-espana-t1-spa_bustamante1829.txt` (1829) | new-spain-and-andes-mission-born-christianity, tradition |
| era 7 row 120, Bernardino de Sahagún: the Historia general, Books I-XI | filled | `sahagun_historia-general-de-las-cosas-de-nueva-espana-t2-spa_bustamante1829.txt` (1829) | new-spain-and-andes-mission-born-christianity, tradition |
| era 7 row 120, Bernardino de Sahagún: the Historia general, Books I-XI | filled | `sahagun_historia-general-de-las-cosas-de-nueva-espana-t3-spa_bustamante1830.txt` (1830) | new-spain-and-andes-mission-born-christianity, tradition |
| era 7 row 120, Bernardino de Sahagún: the Historia general, Book XII | filled | `sahagun_historia-de-la-conquista-de-mexico-libro-12-spa_bustamante1829.txt` (1829) | new-spain-and-andes-mission-born-christianity, tradition |
| era 7 row 120, Bernardino de Sahagún: the Nahuatl of his informants (Seler 1927); the Colloquios | not found; held for Mark | — | Seler (1927) is not on archive.org. The Colloquios (Pou y Martí, 1924) is probably in a volume of the Miscellanea Ehrle that archive.org marks access-restricted; not taken. |
| outside-witness row 10, Kâtib Çelebi | filled in part | `katib-celebi_history-of-the-maritime-wars-of-the-turks-chapters-1-4_mitchell1831.txt` (1831) | orthodoxy-under-the-ottomans-parish-millet-and-n, context Chapters I-IV; no more was translated. |
| outside-witness row 11, Evliya Çelebi: the Travels in English | filled | `evliya-celebi_narrative-of-travels-v1-pt1_hammer1834.txt` (1834) | orthodoxy-under-the-ottomans-parish-millet-and-n, context |
| outside-witness row 11, Evliya Çelebi: the Travels in English | filled | `evliya-celebi_narrative-of-travels-v1-pt2_hammer1846.txt` (1846) | orthodoxy-under-the-ottomans-parish-millet-and-n, context |
| outside-witness row 11, Evliya Çelebi: the Travels in English | filled | `evliya-celebi_narrative-of-travels-v2_hammer1850.txt` (1850) | orthodoxy-under-the-ottomans-parish-millet-and-n, context |
| outside-witness rows 12-14, Peçevi, Mustafa Ali, Selaniki | not found | — | No translation printed by 1930 was found; the Ottoman-script printing of Peçevi (1866) cannot be read in the OCR and was not taken. |
| outside-witness row 15, Joseph ha-Kohen: Divrei ha-Yamim in English | filled | `joseph-ha-kohen_chronicles-of-rabbi-joseph-ben-joshua-ben-meir-v1_bialloblotzky1835.txt` (1835) | the-tridentine-church, context |
| outside-witness row 15, Joseph ha-Kohen: Divrei ha-Yamim in English | filled | `joseph-ha-kohen_chronicles-of-rabbi-joseph-ben-joshua-ben-meir-v2_bialloblotzky1836.txt` (1836) | the-tridentine-church, context |
| outside-witness row 15, Joseph ha-Kohen: Emek ha-Bakha in French | filled | `joseph-ha-kohen_la-vallee-des-pleurs-emek-ha-bakha-fra_see1881.txt` (1881) | the-tridentine-church, context |
| outside-witness row 16, Samuel Usque: the Consolaçam | filled | `usque_consolacam-as-tribulacoens-de-israel-por_mendes-dos-remedios1906.txt` (1906) | the-tridentine-church, context |
| outside-witness rows 17-18, Gedaliah ibn Yahya; David Gans | not found | — | No scan under any spelling tried. |
| outside-witness row 19, Solomon ibn Verga: Shevet Yehudah in Latin | filled | `ibn-verga_historia-judaica-shevet-yehudah-lat_gentius1651.txt` (1651) | the-tridentine-church, context |
| outside-witness row 20, Jacques-Auguste de Thou | located | — | The Latin of 1733 (seven volumes) and the French of 1734 (sixteen) are on archive.org in part; not taken for their length. His De vita sua (1621) has poor OCR and no title page in the scan; not taken. |
| outside-witness row 21, Guicciardini: the Storia d'Italia | filled | `guicciardini_la-storia-d-italia-v1-ita_gherardi1919.txt` (1919) | the-tridentine-church, latin-papal-church-avignon-to-lateran-v, context |
| outside-witness row 21, Guicciardini: the Storia d'Italia | filled | `guicciardini_la-storia-d-italia-v2-ita_gherardi1919.txt` (1919) | the-tridentine-church, latin-papal-church-avignon-to-lateran-v, context |
| outside-witness row 21, Guicciardini: the Storia d'Italia | filled | `guicciardini_la-storia-d-italia-v3-ita_gherardi1919.txt` (1919) | the-tridentine-church, latin-papal-church-avignon-to-lateran-v, context |
| outside-witness row 21, Guicciardini: the Storia d'Italia | filled | `guicciardini_la-storia-d-italia-v4-ita_gherardi1919.txt` (1919) | the-tridentine-church, latin-papal-church-avignon-to-lateran-v, context |
| outside-witness row 22, Machiavelli: his writings in English | filled | `machiavelli_historical-political-and-diplomatic-writings-v1_detmold1882.txt` (1882) | latin-papal-church-avignon-to-lateran-v, the-tridentine-church, context |
| outside-witness row 22, Machiavelli: his writings in English | filled | `machiavelli_historical-political-and-diplomatic-writings-v2_detmold1882.txt` (1882) | latin-papal-church-avignon-to-lateran-v, the-tridentine-church, context |
| outside-witness row 22, Machiavelli: his writings in English | filled | `machiavelli_historical-political-and-diplomatic-writings-v3_detmold1882.txt` (1882) | latin-papal-church-avignon-to-lateran-v, the-tridentine-church, context |
| outside-witness row 22, Machiavelli: his writings in English | filled | `machiavelli_historical-political-and-diplomatic-writings-v4_detmold1882.txt` (1882) | latin-papal-church-avignon-to-lateran-v, the-tridentine-church, context |
| outside-witness row 23, Jean Bodin: the Six Books in English | filled | `bodin_six-bookes-of-a-commonweale_knolles1606.txt` (1606) | the-huguenots, context |
| outside-witness row 23, Jean Bodin: the Colloquium heptaplomeres | filled | `bodin_colloquium-heptaplomeres-lat_noack1857.txt` (1857) | the-huguenots, context |
| outside-witness row 24, Montaigne: the Essays in Florio's English | filled | `montaigne_essays-v1_florio-saintsbury1892.txt` (1892) | the-huguenots, context |
| outside-witness row 24, Montaigne: the Essays in Florio's English | filled | `montaigne_essays-v2_florio-saintsbury1893.txt` (1893) | the-huguenots, context |
| outside-witness row 24, Montaigne: the Essays in Florio's English | filled | `montaigne_essays-v3_florio-saintsbury1893.txt` (1893) | the-huguenots, context |
| outside-witness row 25, Vasari | located | — | Foster's English (1850-52, five volumes) and de Vere's (1912-15, ten) are on archive.org in part; not taken for their length. |
| outside-witness row 26, Leo Africanus | filled | `leo-africanus_history-and-description-of-africa-v1_pory-brown1896.txt` (1896) | the-coptic-church-under-the-ottomans, context |
| outside-witness row 26, Leo Africanus | filled | `leo-africanus_history-and-description-of-africa-v2_pory-brown1896.txt` (1896) | the-coptic-church-under-the-ottomans, context |
| outside-witness row 26, Leo Africanus | filled | `leo-africanus_history-and-description-of-africa-v3_pory-brown1896.txt` (1896) | the-coptic-church-under-the-ottomans, context |
| outside-witness row 27, Busbecq: the Turkish Letters and the letters from France | filled | `busbecq_life-and-letters-v1_forster-daniell1881.txt` (1881) | orthodoxy-under-the-ottomans-parish-millet-and-n, context |
| outside-witness row 27, Busbecq: the Turkish Letters and the letters from France | filled | `busbecq_life-and-letters-v2_forster-daniell1881.txt` (1881) | the-huguenots, context |
| council row, Marburg Colloquy (1529): the colloquy's record, first choice (Schirrmacher) | filled | `schirrmacher_briefe-und-acten-marburg-1529-augsburg-1530-lat-deu_1876.txt` (1876) | lutheran-wittenberg-and-its-congregations, tradition; the-reformed-cities-zurich-and-geneva, context A Latin report of the sessions (OCR lines 1210-1836); the articles are not printed in it. The host calls the item a reprint of 1968, which the scan is not. |
| council row, Marburg Colloquy (1529): the participants' reports and the signed articles (Weimar edition 30/3) | filled | `luther_werke-kritische-gesamtausgabe-bd-30-abt-3-deu-lat_weimar1910.txt` (1910) | lutheran-wittenberg-and-its-congregations, the-reformed-cities-zurich-and-geneva, tradition; lutheran-wittenberg-and-its-congregations, tradition |
| council row, Marburg Colloquy (1529): Jacobs's Book of Concord, vol. II | not taken | — | The only scan is an undated upload whose title-page year was not read. Erichson (1880) is a narrative with poor OCR; not taken. |
| council row, Diet of Worms (1521): the Diet's acts (Reichstagsakten II) | filled | `deutsche-reichstagsakten_juengere-reihe-bd-2-reichstag-zu-worms-1521-deu-lat-fra_wrede1896.txt` (1896) | lutheran-wittenberg-and-its-congregations, tradition; the-tridentine-church, context |
| council row, Diet of Worms (1521): Kidd's Documents (also Marburg and Augsburg) | filled | `kidd_documents-illustrative-of-the-continental-reformation-lat-deu-fra-eng_1911.txt` (1911) | lutheran-wittenberg-and-its-congregations, tradition; the-reformed-cities-zurich-and-geneva, tradition; the-tridentine-church, context |
| Wanted Sources council row 22, Colloquy of Poissy (1561) | held already | — | `beza_histoire-ecclesiastique-t1-fra_baum-cunitz1883.txt`, the chapter 'Le Colloque de Poissy' from about file line 26871, with Beza's speech; the councils scan already says so. |
| Open-Gaps 273, not held: Aleander's dispatches | filled | `balan_monumenta-reformationis-lutheranae-1521-1525-lat-ita_1884.txt` (1884) | the-tridentine-church, tradition; lutheran-wittenberg-and-its-congregations, context |
| Open-Gaps 273, not held: Luther's Worms speech in its own language; Charles V's French declaration; the Edict | filled | — | The Reichstagsakten volume has the hearing, the declaration in French (no. 82) and the Edict in full in German (no. 92). Kidd has the speech in Latin, the declaration in English and the Edict in Latin extracts. |
| Open-Gaps 273, not held: the Confutatio pontificia, Latin | filled | `corpus-reformatorum_v27-confutatio-et-apologia-confessionis-augustanae-lat-deu_bindseil1859.txt` (1859) | the-tridentine-church, tradition; lutheran-wittenberg-and-its-congregations, tradition |
| Open-Gaps 273, not held: the Confutatio pontificia, English | filled | `reu_augsburg-confession-collection-of-sources_1930.txt` (1930) | lutheran-wittenberg-and-its-congregations, tradition; the-tridentine-church, context Imprint 1930. |
| Open-Gaps 273, not held: the full recess of 19 November 1530 | filled in part | `foerstemann_urkundenbuch-reichstag-zu-augsburg-1530-bd-2-deu-lat_1835.txt` (1835) | lutheran-wittenberg-and-its-congregations, tradition The recesses of 22 September and 13 October are printed; the editor leaves out the text of 19 November as well enough known. Kidd and Reu also print the recess of 22 September. |
| Open-Gaps 273, not held: a Campeggio document of 1530 | filled | `laemmer_monumenta-vaticana-historiam-ecclesiasticam-saeculi-xvi-lat-ita_1861.txt` (1861) | the-tridentine-church, tradition; lutheran-wittenberg-and-its-congregations, context |
| Open-Gaps 273, not held: Luther's Coburg letters, in the original | filled | `luther_briefe-sendschreiben-und-bedenken-theil-4-lat-deu_de-wette1827.txt` (1827) | lutheran-wittenberg-and-its-congregations, tradition |
| Open-Gaps 273, not held: Luther's Coburg letters, in English | filled | `luther_letters-of-martin-luther_currie1908.txt` (1908) | lutheran-wittenberg-and-its-congregations, tradition |
| Open-Gaps 273, not held: Herminjard (for Chanforan) | filled | `herminjard_correspondance-des-reformateurs-t2-1527-1532-fra-lat_1868.txt` (1868) | the-waldensian-reformed-union, context (needs-ruling); the-reformed-cities-zurich-and-geneva, tradition A letter from the valleys and the editor's notes; no account of the assembly by one who was there. |
| Open-Gaps 273, not held: Scultetus's Annales | located | — | The scan of 1618 holds the first decade only (1516-1525); von der Hardt's reprint (1717) runs to 1535 but its OCR is poor and the 1532 passage was not found. Neither taken. |
| Open-Gaps 273, not held: the Olivetan Bible with its Apologie du translateur | held for Mark | — | The scan of the 1535 Bible carries the French national library's notice on commercial reuse, and its black letter cannot be read in the OCR. Reuss (1866) describes the preface and does not print it. |
| Open-Gaps 273, not held: the Chanforan manuscript at Dublin | not searched | — | A manuscript; no printing was looked for beyond Herminjard. |
| Open-Gaps 278, Library items: a clean copy of Pallavicino, book 13 | filled | `pallavicino_istoria-del-concilio-di-trento-tomo7-libri13-14-ita_classici-sacri1846.txt` (1846) | the-tridentine-church, context Books XIII and XIV. The lost word is 'nota': 'lungi da ogni nota' (about OCR line 5333). |
| Open-Gaps 278, not held: the colloquy book and agreed articles of Regensburg (1541) | held in part | — | `kidd_documents-illustrative-of-the-continental-reformation-lat-deu-fra-eng_1911.txt`, nos. 136-140 (from about file line 19426): a history of the meeting, the agreement on justification in Latin, and letters. The whole book was not searched. |
| Open-Gaps 278, not held: Calvin's Latin letters of 1541 | not found | — | Volumes X, XII and XIII of the Opera are on archive.org in the series already used; volume XI was not found under four queries. |
| Open-Gaps 278, not held: Massarelli's diaries | held for Mark | — | Every scan of the Concilium Tridentinum volumes on archive.org is dated 1964 by the host; none was opened. |

**Cautions the filled texts carry.**
- Katharina Zell: her own words are in Füsslin's reprint of 1753, in black letter the OCR reads only fairly;
  Rabus's letters stand in the same section. Röhrich is a Life of 1855 that quotes her.
- Marie Dentière: Herminjard prints the Epistre with passages left out. Jeanne de Jussie is an opponent.
- Gracián: the treatise speaks of his captivity; it is not his own account of his life.
- Xu Guangqi: one memorial, in an unnamed translator's English of 1850. The heading dates the charge against the
  Jesuits 1617.
- Las Casas: he speaks as an eyewitness in the first person in every volume; from volume IV he tells his own
  actions in the third person, as "el clérigo Casas". The Historia and the Cádiz Brevísima are in Spanish;
  MacNutt's English of the Brevísima is of 1909.
- Sahagún: Bustamante's Spanish only. The Nahuatl of his informants is not held, and the notes and supplements
  are the editor's.
- Marburg: Schirrmacher's Latin report comes from Aurifaber's collection, the Wittenberg side; it does not print
  the articles, and his German parts are poorly read. The Weimar volume holds the reports of Hedio, the
  Anonymous, Collin, Osiander and Brenz and the articles with their signatures. Kidd prints the fifteenth
  article only, in a Latin version, with nine signatures.
- Worms: the Edict is in full, in German, in the Reichstagsakten (no. 92); Kidd has Latin extracts, and the
  emperor's declaration in English only. Balan's index dates Aleander's letters nos. 61, 64, 67 and 70 to 5, 16,
  18 and 19 April 1521; no. 68 is the "Acta comparitionis Lutheri".
- Trent: the clean Pallavicino volume holds Books XIII and XIV only.
- Augsburg: the recess of 19 November is not held as a text; Förstemann leaves it out as well enough known and
  prints those of 22 September and 13 October. Corpus Reformatorum 27 has the Confutatio in Latin and in German.
  Reu's English uses Jacobs's translations, by his preface; his imprint is 1930 and the preface is dated 15
  December 1930.
- The outside witnesses are held in their translators' English, French and Latin, except Usque (Portuguese),
  Guicciardini (Italian) and Bodin's Colloquium (Latin). None was read in depth. The Latin Shevet Yehudah names
  its author in the translator's preface, not on the title page. Sée's Vallée des pleurs carries the notes and
  appendix of a later "Correcteur" in the text. The first volume of the Chronicles does not name its translator.
  Kâtib Çelebi is four chapters. The title page of Evliya's second part says "Part I".

**Not taken.** Every duplicate, reprint, long set and unreadable scan is listed in the search log.

## Era 9 (1815-1906), batch 1 (2026-11-15): the major figures of the Who scan's wanted sources

Ninety-nine files for the 63 person rows marked major in
`Build/Ministry/Operations/Audits/2026-11-12_wanted-sources-combined/Wanted_Sources.md` (rows 163-225). The search
record is `Build/Ministry/Operations/Audits/2026-11-15_library-era9/Search_Log.md`. Every file has a printed
imprint year of 1930 or earlier, read on its title page or, for eighteen volumes, on the scan's page image. The
rows not marked major (226-330), the era 9 outside witnesses, the council records and the held eras 8-9 items
are left for the next batches. One want was held already.

| want | state | file(s), with the imprint year | shelf |
|---|---|---|---|
| era 9 row 163, Barton W. Stone: his own Biography | filled | `stone_biography-of-elder-barton-warren-stone_rogers1847.txt` (1847); 146,459 words; eng | the-stone-campbell-restoration-movement, tradition |
| era 9 row 164, Alexander Campbell: a Life (Richardson, vol. 1) | filled | `richardson_memoirs-of-alexander-campbell-v1_1868.txt` (1868); 188,994 words; eng | the-stone-campbell-restoration-movement, context |
| era 9 row 164, Alexander Campbell: a Life (Richardson, vol. 2) | filled | `richardson_memoirs-of-alexander-campbell-v2_1870.txt` (1870); 221,572 words; eng | the-stone-campbell-restoration-movement, context |
| era 9 row 164, Alexander Campbell: one volume of the Christian Baptist | filled | `campbell_christian-baptist-v5_bethany1828.txt` (1828); 155,862 words; eng | the-stone-campbell-restoration-movement, tradition |
| era 9 row 165, Charles G. Finney: Lectures on Revivals of Religion | filled | `finney_lectures-on-revivals-of-religion_6th-ed1835.txt` (1835); 207,129 words; eng | the-second-great-awakening-and-camp-meeting-worl, tradition |
| era 9 row 165, Charles G. Finney: his Memoirs | filled | `finney_memoirs-of-rev-charles-g-finney_1876.txt` (1876); 176,972 words; eng | the-second-great-awakening-and-camp-meeting-worl, tradition (decided 15 November, batch 2a) |
| era 9 row 166, Phoebe Palmer: The Way of Holiness | filled | `palmer_way-of-holiness_1843.txt` (1843); 50,843 words; eng | the-holiness-movement, tradition |
| era 9 row 166, Phoebe Palmer: a Life with her letters | filled | `wheatley_life-and-letters-of-mrs-phoebe-palmer_1876.txt` (1876); 235,522 words; eng | the-holiness-movement, context |
| era 9 row 167, Dwight L. Moody: the Life by his son | filled | `moody-w-r_life-of-dwight-l-moody_1900.txt` (1900); 180,120 words; eng | the-sunday-school-and-bible-institute-movement, context |
| era 9 row 172, William Miller: his own Views of the Prophecies | filled | `miller_views-of-the-prophecies-and-prophetic-chronology_himes1842.txt` (1842); 90,391 words; eng | restorationist-apocalyptic-ferment-and-adventism, tradition |
| era 9 row 172, William Miller: a Life told by a disciple | filled | `bliss_memoirs-of-william-miller_1853.txt` (1853); 178,678 words; eng | restorationist-apocalyptic-ferment-and-adventism, context |
| era 9 row 173, Ellen G. White: Life Sketches | filled | `white_life-sketches-of-ellen-g-white_1915.txt` (1915); 140,745 words; eng | restorationist-apocalyptic-ferment-and-adventism, seventh-day-adventist-church-twentieth-century, tradition |
| era 9 row 215, Washington Gladden: Applied Christianity | filled | `gladden_applied-christianity_9th-ed1897.txt` (1897); 76,263 words; eng | the-social-gospel, tradition |
| era 9 row 216, Charles A. Briggs: his own defence at the trial | filled | `briggs_defence-before-the-presbytery-of-new-york_1893.txt` (1893); 87,020 words; eng | the-mainline-century-liberal-and-neo-orthodox, antecedent (decided 15 November, batch 2a) |
| era 9 row 216, Charles A. Briggs: the trial record, part I | filled | `briggs-trial_case-against-professor-briggs-pt1_1892.txt` (1892); 56,636 words; eng | the-mainline-century-liberal-and-neo-orthodox, context (decided 15 November, batch 2a) |
| era 9 row 216, Charles A. Briggs: the trial record, part III | filled | `briggs-trial_case-against-professor-briggs-pt3_1893.txt` (1893); 107,259 words; eng | the-mainline-century-liberal-and-neo-orthodox, context (decided 15 November, batch 2a) |
| era 9 row 217, A. A. Hodge and B. B. Warfield: Inspiration, Presbyterian Review, April 1881 | filled | `presbyterian-review_v2-no6-april-1881-inspiration.txt` (1881); 108,871 words; eng | fundamentalism-1910-1970s, antecedent (decided 15 November, batch 2a) |
| era 9 row 218, David Lipscomb: his own writing (the 1906 census letters were not found) | filled | `lipscomb_queries-and-answers_shepherd1910.txt` (1910); 211,569 words; eng | churches-of-christ-twentieth-century, tradition |
| era 9 row 174, Joseph Smith: his own History | filled | `smith-joseph_history-of-the-church-v1_roberts1902.txt` (1902); 266,920 words; eng | latter-day-saints-lds, tradition |
| era 9 row 174, Joseph Smith: the Doctrine and Covenants | filled | `latter-day-saints_doctrine-and-covenants_kirtland1835.txt` (1835); 117,424 words; eng | latter-day-saints-lds, tradition |
| era 9 row 174, Joseph Smith: a life told by another (his mother) | filled | `smith-lucy_biographical-sketches-of-joseph-smith_1853.txt` (1853); 104,546 words; eng | latter-day-saints-lds, tradition |
| era 9 row 175, Brigham Young: the Journal of Discourses, vol. 1 | filled | `journal-of-discourses_v1_watt1854.txt` (1854); 256,045 words; eng | latter-day-saints-lds, tradition |
| era 9 row 175, Brigham Young: a life told by another | filled | `tullidge_life-of-brigham-young_1876.txt` (1876); 150,550 words; eng | latter-day-saints-lds, context |
| era 9 row 176, Charles Taze Russell: Millennial Dawn, vol. 1 | filled | `russell_millennial-dawn-v1-plan-of-the-ages_1886.txt` (1886); 104,879 words; eng | jehovah-s-witnesses-bible-students, tradition |
| era 9 row 177, Mary Baker Eddy: Science and Health | filled | `eddy_science-and-health-with-key-to-the-scriptures_161st-ed1899.txt` (1899); 215,874 words; eng | christian-science, tradition |
| era 9 row 177, Mary Baker Eddy: Retrospection and Introspection | filled | `eddy_retrospection-and-introspection_1892.txt` (1892); 19,189 words; eng | christian-science, tradition |
| era 9 row 178, John Thomas: Elpis Israel | filled | `thomas_elpis-israel_1849.txt` (1849); 250,733 words; eng | christadelphians, tradition |
| era 9 row 180, John Humphrey Noyes: his own writing | filled | `noyes_history-of-american-socialisms_1870.txt` (1870); 192,303 words; eng | oneida-community, tradition |
| era 9 row 180, John Humphrey Noyes: his talks to the community | filled | `noyes_home-talks-v1_barron-miller1875.txt` (1875); 81,372 words; eng | oneida-community, tradition |
| era 9 row 180, John Humphrey Noyes: his religious experience, compiled from his writings | filled | `noyes_religious-experience-of-john-humphrey-noyes_gw-noyes1923.txt` (1923); 114,933 words; eng | oneida-community, context (decided 15 November, batch 2a) |
| era 9 row 184, Theodore Parker: his own writing | filled | `parker_discourse-of-matters-pertaining-to-religion_3rd-ed1847.txt` (1847); 142,908 words; eng | american-unitarianism-universalism-consolidations, tradition |
| era 9 row 184, Theodore Parker: his sermons | filled | `parker_ten-sermons-of-religion_2nd-ed1861.txt` (1861); 99,459 words; eng | american-unitarianism-universalism-consolidations, tradition |
| era 9 row 184, Theodore Parker: a Life with his letters (vol. 1) | filled | `weiss_life-and-correspondence-of-theodore-parker-v1_1864.txt` (1864); 255,131 words; eng | american-unitarianism-universalism-consolidations, context |
| era 9 row 184, Theodore Parker: a Life with his letters (vol. 2) | filled | `weiss_life-and-correspondence-of-theodore-parker-v2_1864.txt` (1864); 281,575 words; eng | american-unitarianism-universalism-consolidations, context |
| era 9 row 168, Charles Haddon Spurgeon: the Autobiography, vol. 1 | filled | `spurgeon_autobiography-v1-1834-1854_1897.txt` (1897); 175,855 words; eng | nineteenth-century-baptists, tradition |
| era 9 row 168, Charles Haddon Spurgeon: one volume of the Metropolitan Tabernacle Pulpit | filled | `spurgeon_metropolitan-tabernacle-pulpit-v16-1870_1871.txt` (1871); 445,705 words; eng | nineteenth-century-baptists, tradition |
| era 9 row 169, Elias Hicks: his Journal | filled | `hicks_journal-of-the-life-and-religious-labours_1832.txt` (1832); 173,374 words; eng | nineteenth-century-quakerism-separations, tradition |
| era 9 row 169, Elias Hicks: the Orthodox side's account | filled | `philadelphia-yearly-meeting_declaration-respecting-those-who-have-separated_1828.txt` (1828); 68,865 words; eng | nineteenth-century-quakerism-separations, tradition |
| era 9 row 170, Joseph John Gurney: his Observations | filled | `gurney_observations-on-the-religious-peculiarities-of-the-society-of-friends_1824.txt` (1824); 113,272 words; eng | nineteenth-century-quakerism-separations, tradition |
| era 9 row 170, Joseph John Gurney: the Memoirs, vol. 1 | filled | `braithwaite_memoirs-of-joseph-john-gurney-v1_1854.txt` (1854); 189,224 words; eng | nineteenth-century-quakerism-separations, context |
| era 9 row 170, Joseph John Gurney: the Memoirs, vol. 2 | filled | `braithwaite_memoirs-of-joseph-john-gurney-v2_1854.txt` (1854); 199,909 words; eng | nineteenth-century-quakerism-separations, context |
| era 9 row 171, William Knibb: a Life | filled | `hinton_memoir-of-william-knibb_2nd-ed1849.txt` (1849); 217,878 words; eng | caribbean-churches-of-slavery-and-emancipation, context |
| era 9 row 171, William Knibb: a fellow missionary's account of Jamaica | filled | `phillippo_jamaica-its-past-and-present-state_1843.txt` (1843); 137,560 words; eng | caribbean-churches-of-slavery-and-emancipation, tradition |
| era 9 row 179, Edward Irving: his collected writings, vol. 5 | filled | `irving_collected-writings-v5_carlyle1866.txt` (1866); 240,993 words; eng | catholic-apostolic-church-irvingites, tradition (decided 15 November, batch 2a) |
| era 9 row 179, Edward Irving: a Life (vol. 1) | filled | `oliphant_life-of-edward-irving-v1_1862.txt` (1862); 136,028 words; eng | catholic-apostolic-church-irvingites, context |
| era 9 row 179, Edward Irving: a Life (vol. 2) | filled | `oliphant_life-of-edward-irving-v2_1862.txt` (1862); 197,494 words; eng | catholic-apostolic-church-irvingites, context |
| era 9 row 182, Anthony Norris Groves: the memoir by his widow, from his journals and letters | filled | `groves_memoir-of-anthony-norris-groves_3rd-ed1859.txt` (1859); 266,660 words; eng | plymouth-brethren-and-dispensational-formation, tradition |
| era 9 row 182, Anthony Norris Groves: his journal | filled | `groves_journal-of-a-residence-at-bagdad-1830-1831_1832.txt` (1832); 88,199 words; eng | plymouth-brethren-and-dispensational-formation, tradition |
| era 9 row 183, George Muller: his Narrative, fourth part | filled | `muller_narrative-of-the-lords-dealings-pt4_1856.txt` (1856); 171,456 words; eng | plymouth-brethren-and-dispensational-formation, tradition |
| era 9 row 188, John Henry Newman: the Apologia | filled | `newman_apologia-pro-vita-sua_1864.txt` (1864); 169,395 words; eng | the-oxford-movement-and-anglo-catholic-revival, catholic-church-long-nineteenth-century, tradition |
| era 9 row 188, John Henry Newman: Tract 90 | filled | `newman_tract-90-remarks-on-certain-passages-in-the-thirty-nine-articles_2nd-ed1841.txt` (1841); 35,662 words; eng | the-oxford-movement-and-anglo-catholic-revival, tradition |
| era 9 row 189, John Keble: the Assize sermon of 1833 | filled | `keble_national-apostasy-assize-sermon_1833.txt` (1833); 5,642 words; eng | the-oxford-movement-and-anglo-catholic-revival, tradition |
| era 9 row 189, John Keble: a Life (vol. 1) | filled | `coleridge_memoir-of-the-rev-john-keble-v1_2nd-ed1869.txt` (1869); 81,238 words; eng | the-oxford-movement-and-anglo-catholic-revival, context |
| era 9 row 190, Edward Bouverie Pusey: Liddon's Life, vol. 1 | filled | `liddon_life-of-edward-bouverie-pusey-v1_1893.txt` (1893); 209,678 words; eng | the-oxford-movement-and-anglo-catholic-revival, context |
| era 9 row 190, Edward Bouverie Pusey: a sermon of his own | filled | `pusey_do-all-to-the-lord-jesus-sermon_boston1864.txt` (1864); 5,850 words; eng | the-oxford-movement-and-anglo-catholic-revival, tradition |
| era 9 row 190, Edward Bouverie Pusey: his letters | filled | `pusey_spiritual-letters_johnston-newbolt1898.txt` (1898); 97,696 words; eng | the-oxford-movement-and-anglo-catholic-revival, tradition |
| era 9 row 191, William Booth: In Darkest England and the Way Out | filled | `booth_in-darkest-england-and-the-way-out_1890.txt` (1890); 129,128 words; eng | the-salvation-army, tradition |
| era 9 row 214, Evan Roberts: a Life, in Welsh | filled | `phillips_evan-roberts-ai-waith-cym_1912.txt` (1912); 129,838 words; cym | the-1904-07-revival-family-wales-mukti-india-pyo, context (decided 15 November, batch 2a) |
| era 9 row 222, William Clowes: his Journals | filled | `clowes_journals-of-william-clowes_1844.txt` (1844); 115,023 words; eng | nineteenth-century-methodism, tradition |
| era 9 row 222, Hugh Bourne: a Life | filled | `antliff_life-of-the-venerable-hugh-bourne_1872.txt` (1872); 167,409 words; eng | nineteenth-century-methodism, context |
| era 9 row 193, Abraham Kuyper: a Dutch work of his own | filled | `kuyper_tractaat-van-de-reformatie-der-kerken-nld_1883.txt` (1883); 90,480 words; nld | dutch-neo-calvinism-secession-churches, tradition |
| era 9 row 194, Herman Bavinck: an English print of his own lectures | filled | `bavinck_philosophy-of-revelation_1909.txt` (1909); 110,728 words; eng | dutch-neo-calvinism-secession-churches, tradition (decided 15 November, batch 2a) |
| era 9 row 194, Herman Bavinck: his own summary of doctrine, in Dutch (not the Dogmatiek) | filled | `bavinck_magnalia-dei-nld_1909.txt` (1909); 276,477 words; nld | dutch-neo-calvinism-secession-churches, tradition (decided 15 November, batch 2a) |
| era 9 row 196, C. F. W. Walther: Der Lutheraner, the first year | filled | `walther_der-lutheraner-jg1-1844-1845-deu_st-louis1844.txt` (1844); 148,394 words; deu | confessional-lutheran-revival-emigrations, tradition |
| era 9 row 221, Adolf von Harnack: What Is Christianity?, in English | filled | `harnack_what-is-christianity_saunders1901.txt` (1901); 87,707 words; eng | the-mainline-century-liberal-and-neo-orthodox, tradition |
| era 9 row 221, Adolf von Harnack: Das Wesen des Christentums | filled | `harnack_das-wesen-des-christentums-deu_1900.txt` (1900); 66,516 words; deu | the-mainline-century-liberal-and-neo-orthodox, tradition |
| era 9 row 223, Theodor Fliedner: a Life, in English | filled | `fliedner-life_life-of-pastor-fliedner-of-kaiserswerth_winkworth1867.txt` (1867); 54,506 words; eng | the-reveil-and-inner-mission-awakening, context |
| era 9 row 223, the Fliedners: an English account of Kaiserswerth | filled | `kaiserswerth_institution-of-kaiserswerth-on-the-rhine_1851.txt` (1851); 8,938 words; eng | the-reveil-and-inner-mission-awakening, context |
| era 9 row 223, the Fliedners: Kaiserswerth's own jubilee memoir, in German | filled | `disselhoff_jubilate-denkschrift-kaiserswerth-deu_1886.txt` (1886); 188,677 words; deu | the-reveil-and-inner-mission-awakening, tradition (decided 15 November, batch 2a) |
| era 9 row 224, Hendrik de Cock: two of his first writings | filled | `cock_twee-der-eerste-geschriften-nld_1882.txt` (1882); 29,001 words; nld | dutch-neo-calvinism-secession-churches, tradition |
| era 9 row 225, Paul Petter Waldenstrom: a book of his in English | filled | `waldenstrom_blood-of-jesus_princell1888.txt` (1888); 17,269 words; eng | laestadianism-and-the-nordic-revivals, tradition |
| era 9 row 195, Ignaz von Dollinger: his declarations and letters on the Vatican decrees, in English | filled | `dollinger_declarations-and-letters-on-the-vatican-decrees-1869-1887_1891.txt` (1891); 42,789 words; eng | old-catholic-churches-union-of-utrecht, tradition |
| era 9 row 201, Cyril IV: a church history of Egypt before 1931 | filled | `butcher_story-of-the-church-of-egypt-v2_1897.txt` (1897); 144,216 words; eng | coptic-revival-under-cyril-iv, context |
| era 9 row 200, Joseph Audo: the acts of the Vatican council | filled | `collectio-lacensis_t7-acta-et-decreta-concilii-vaticani-lat_1892.txt` (1892); 1,181,347 words; lat | catholic-church-long-nineteenth-century, tradition |
| era 9 row 202, Ioann Veniaminov: his Notes on the Unalaska islands, part 1 | filled | `veniaminov_zapiski-ob-ostrovakh-unalashkinskago-otdela-ch1-rus_1840.txt` (1840); 66,278 words; rus | alaskan-mission-herman-veniaminov, tradition |
| era 9 row 202, Ioann Veniaminov: his Notes on the Unalaska islands, part 2 | filled | `veniaminov_zapiski-ob-ostrovakh-unalashkinskago-otdela-ch2-rus_1840.txt` (1840); 78,182 words; rus | alaskan-mission-herman-veniaminov, tradition |
| era 9 row 202, Ioann Veniaminov: an English account before 1931 | filled | `hale_innocent-of-moscow-apostle-of-kamchatka-and-alaska_1888.txt` (1888); 8,743 words; eng | alaskan-mission-herman-veniaminov, context |
| era 9 row 198, Nikolai of Japan: a Russian account of the Japan mission | filled | `pravoslavie-v-iaponii_pravoslavie-v-iaponii-rus_1889.txt` (1889); 3,933 words; rus | russian-church-synodal-century, japanese-christianity-hidden-emergence-meiji, context |
| era 9 row 185, Hong Xiuquan: the kingdom's own printed books, in translation | filled | `medhurst_pamphlets-issued-by-the-chinese-insurgents-at-nan-king_1853.txt` (1853); 106,466 words; eng | taiping-heavenly-kingdom, tradition |
| era 9 row 185, Hong Xiuquan: an outside account | filled | `callery-yvan_history-of-the-insurrection-in-china_oxenford1854.txt` (1854); 88,299 words; eng | taiping-heavenly-kingdom, context |
| era 9 row 185, Hong Xiuquan: an account that quotes the record of his visions | filled | `lindley_ti-ping-tien-kwoh-v1_1866.txt` (1866); 156,700 words; eng | taiping-heavenly-kingdom, context (decided 15 November, batch 2a) |
| era 9 row 203, Samuel Ajayi Crowther: his journal of 1854 | filled | `crowther_journal-of-an-expedition-up-the-niger-and-tshadda_1855.txt` (1855); 68,238 words; eng | the-missionary-movement-s-native-churches-seramp, tradition |
| era 9 row 203, Samuel Ajayi Crowther: his journal of 1841 | filled | `schon-crowther_journals-of-the-niger-expedition-of-1841_1842.txt` (1842); 98,364 words; eng | the-missionary-movement-s-native-churches-seramp, tradition |
| era 9 row 203, Samuel Ajayi Crowther: a Life | filled | `page_black-bishop-samuel-adjai-crowther_1908.txt` (1908); 146,120 words; eng | the-missionary-movement-s-native-churches-seramp, context (decided 15 November, batch 2a) |
| era 9 row 204, J. Hudson Taylor: a Life (the early years) | filled | `taylor-howard_hudson-taylor-in-early-years_1912.txt` (1912); 206,805 words; eng | the-missionary-movement-s-native-churches-seramp, context (decided 15 November, batch 2a) |
| era 9 row 205, Xi Shengmo (Pastor Hsi): a Life (the early life) | filled | `taylor-howard_one-of-chinas-scholars-pastor-hsi_1909.txt` (1909); 169,725 words; eng | the-missionary-movement-s-native-churches-seramp, context (decided 15 November, batch 2a) |
| era 9 row 206, Ludwig Ingwer Nommensen: the obituary by J. Warneck | filled | `allgemeine-missions-zeitschrift_jg45-46-deu_berlin1918-1919.txt` (1918); 281,883 words; deu | indonesian-christianity-the-independent-century, context |
| era 9 row 209, Johann Ludwig Krapf: his Travels | filled | `krapf_travels-researches-and-missionary-labours-in-eastern-africa_1860.txt` (1860); 169,566 words; eng | east-african-christianity-uganda-martyrs, tradition |
| era 9 row 210, Charles Lwanga: a missionary's account of Uganda (it does not name him) | filled | `ashe_chronicles-of-uganda_1895.txt` (1895); 116,463 words; eng | east-african-christianity-uganda-martyrs, tradition |
| era 9 row 211, Tiyo Soga: a Life | filled | `chalmers_tiyo-soga-a-page-of-south-african-mission-work_1877.txt` (1877); 155,925 words; eng | southern-african-mission-churches, context |
| era 9 row 220, James Thomson: his Letters | filled | `thomson_letters-on-the-moral-and-religious-state-of-south-america_1827.txt` (1827); 76,816 words; eng | nineteenth-century-latin-american-catholicism, context |
| era 9 row 186, Antonio Conselheiro: a second witness in English | filled | `cunninghame-graham_brazilian-mystic-antonio-conselheiro_1920.txt` (1920); 68,385 words; eng | canudos-belo-monte, context (decided 15 November, batch 2a) |
| era 9 row 219, Jerry McAuley: his life and his own account | filled | `offord_jerry-mcauley-his-life-and-work_2nd-ed1885.txt` (1885); 72,189 words; eng | the-rescue-mission-movement, context (decided 15 November, batch 2a) |
| era 9 row 219, Jerry McAuley: his own account | filled | `mcauley_transformed-or-the-history-of-a-river-thief_1876.txt` (1876); 12,743 words; eng | the-rescue-mission-movement, antecedent (decided 15 November, batch 2a) |
| era 9 row 183, George Muller: his Narrative, condensed for American readers | filled | `muller_life-of-trust_wayland1868.txt` (1868); 175,445 words; eng | plymouth-brethren-and-dispensational-formation, tradition |
| era 9 row 191, Catherine Booth: a Life (vol. 1), which tells of her Female Ministry of 1859 | filled | `booth-tucker_life-of-catherine-booth-v1_1893.txt` (1893); 225,473 words; eng | the-salvation-army, context |
| era 9 row 214, Evan Roberts: accounts of the revival printed in 1905 | filled | `story-of-the-welsh-revival_told-by-eyewitnesses_3rd-ed1905.txt` (1905); 30,623 words; eng | the-1904-07-revival-family-wales-mukti-india-pyo, context |
| era 9 row 208, David Jones and David Griffiths: Ellis, History of Madagascar, vol. 1 | filled | `ellis_history-of-madagascar-v1_1838.txt` (1838); 173,516 words; eng | malagasy-christianity, context |
| era 9 row 208, David Jones and David Griffiths: Ellis, History of Madagascar, vol. 2 | filled | `ellis_history-of-madagascar-v2_1838.txt` (1838); 176,610 words; eng | malagasy-christianity, context |
| era 9 row 200, Joseph Audo: an English witness | held already | `badger_nestorians-and-their-rituals-v1_1852.txt`, `-v2_1852.txt` | — |
| era 9 row 181, John Nelson Darby: the Letters and the Collected Writings | not found | — | Only reprints of 1964 and 1974. Four smaller books of his own are located (1863-1900). |
| era 9 row 197, Ambrose of Optina: his letters and an early Life | not found | — | About twelve queries, in Cyrillic and in transliteration. |
| era 9 row 199, Mkrtich Khrimian: his writings | located, not vendored | — | Six Armenian printings (1877-1929); the OCR of the four sampled cannot be read. No English account before 1931. |
| era 9 row 207, Kiai Sadrach: Dutch mission reports | not found | — | archive.org only; dbnl.org not yet searched. |
| era 9 rows 212 and 213, Nehemiah Tile and Mangena Mokone | not found | — | Neither is named in the Native Affairs Commission report of 1903-05 or in five 1896 numbers of the Voice of Missions. Sundkler (1948) is out by date. |
| era 9 rows 186 and 187, Os Sertoes (3rd ed., 1905) | held for Mark | — | `004518-completo` on archive.org: clean OCR and a Public Domain Mark, but the Brasiliana USP notice in the file asks for non-commercial use and no republication without leave. |
| era 9 row 192, Johann Hinrich Wichern: the Denkschrift | located, not vendored | — | Third edition, Hamburg 1889; the black-letter OCR cannot be read. The editions of 1849 were not found. |
| era 9 row 193, Abraham Kuyper: Calvinism, the Stone Lectures | not taken yet | — | Three scans; none prints a year, and the same check is owed. A Life before 1931 was not found. |
| era 9 row 194, Herman Bavinck: the Gereformeerde Dogmatiek | not found | — | The one item has no text on the host. |
| era 9 row 195, Ignaz von Dollinger: Friedrich's Life; the Briefe und Erklarungen in German | located, not vendored | — | Both are black letter with OCR that cannot be read. |
| era 9 row 196, C. F. W. Walther: the constitution of 1847 | located, not vendored | — | Printed in Der Lutheraner, the fourth year (`DerLutheraner04`); no separate print found. |
| era 9 row 173, Ellen G. White: Spiritual Gifts | not found before 1931 | — | A facsimile of 1945 and typed transcriptions only. |
| era 9 row 178, John Thomas: Eureka; a Life | not found | — | About eight queries. |
| era 9 row 183, George Muller: the Narrative, parts 1 to 3 | not found | — | Wayland's Life of Trust (1868), which condenses the four parts, was taken in their place. |
| era 9 row 185, Hong Xiuquan: Hamberg, The Visions of Hung-Siu-tshuen (1854) | not found | — | Lindley (1866) quotes Hamberg's narrative at length. |
| era 9 row 191, Catherine Booth: Female Ministry (1859) | not found before 1931 | — | A reprint of 1975 only. Booth-Tucker's Life, vol. 1, tells of it. |
| era 9 row 204, Hudson Taylor: A Retrospect | not taken yet | — | No scan prints a year on its title page; a dated preface or copyright notice has still to be checked against the catalogue. |
| era 9 row 210, Charles Lwanga: a martyr account that names him | not taken yet | — | Walsh's book has a chapter on him but prints no year; the same check is owed. |
| era 9 row 214, Evan Roberts: his own words; War on the Saints | not found before 1931 | — | Reprints of 1964 to 1994 only. |
| era 9 row 218, David Lipscomb: the 1906 census letters | not found | — | Religious Bodies 1906, vol. 2, does not name him. |
| era 9 row 222, Hugh Bourne: History of the Primitive Methodists (1823) | not found | — | Five queries. |
| era 9 row 224, Hendrik de Cock: the Act of Secession of 1834; a Life | not found | — | Rullmann (1930) is located. |
| era 9 row 225, Paul Petter Waldenstrom: a book in Swedish | located, not vendored | — | One printing of 1875 has OCR that cannot be read; two others carry NC licenses and are held for Mark. |

**Cautions for profile writers (era 9, batch 1)**

- **Translation only.** Harnack (1901), Waldenstrom (1888), Dollinger's Declarations (1891), the Life of
  Fliedner (1867), Callery and Yvan (1854) and the Taiping pamphlets (Medhurst 1853) are English translations.
  Harnack's German is also held. The German of Dollinger and the Swedish of Waldenstrom are not.
- **Not the person's own words.** Row 167 (Moody) is the Life by his son; no volume of his sermons was taken.
  Row 198 (Nikolai of Japan) is a short Russian account by another hand. Row 201 (Cyril IV) is an English
  history that calls him "Cyril the Reformer". Row 206 (Nommensen) is a three-page obituary inside two bound years of a periodical. Row 210 (Lwanga): Ashe's Chronicles of Uganda does not name him. Row 222 (Bourne) is a Life of 1872.
  Row 223 (the Fliedners): none of the three files is in their own words.
- **Author not named on the title page.** Millennial Dawn, vol. 1 (the host names Russell); the Institution of
  Kaiserswerth, 1851 (the host names Florence Nightingale); the Life of Pastor Fliedner; the Russian pamphlet on
  Japan (the host names Makarov); Spurgeon's Autobiography (compiled by his wife and secretary, unnamed); the
  Memoir of Groves ("by his widow"); the two "Case against Professor Briggs" parts.
- **Later editions.** Finney's Lectures (sixth edition, 1835); Parker's Discourse (third, 1847) and Ten Sermons
  (second, 1861); Gladden (ninth, 1897); Hinton's Knibb (second, 1849); Groves's Memoir (third, 1859); Science
  and Health (161st, 1899, not the text of 1875); Tract 90 (second, 1841); Millennial Dawn (the title page reads
  1886; a library stamp reads 1906); One of China's Scholars (the printing of 1909; the same scan holds Pastor Hsi: One of China's Christians, twelfth edition, from OCR line 7854).
- **Part of a larger work.** Vol. 1 only: Spurgeon's Autobiography, Liddon's Pusey, Coleridge's Keble, the
  Journal of Discourses, Home-Talks, the History of the Church, Lindley. Muller's Narrative is the
  fourth part only. Irving's Collected Writings is vol. 5 only. Butcher is vol. 2 only.
- **Mixed voices.** Stone's Biography: his own narrative is chapters I to X; chapters XI and XII and the
  additions are Rogers's. The Philadelphia Declaration of 1828 is bound with four later Friends' pamphlets
  (1838-1852). De Cock's volume: he issued the two pieces; the letters of the second are by others. The Apologia is bound with the Kingsley correspondence. The Journal of Discourses has many
  speakers. The Niger journals of 1842 give Schon first, then Crowther. The Presbyterian Review number holds
  other articles after "Inspiration". The Vatican council volume is about 1.17 million words; Audo is spelled
  "Audu" in it.
- **OCR.** Der Lutheraner (black letter) is fair at best. Veniaminov's Russian is fair, in the old spelling.
  Phillips's Welsh Life has a publisher's list before its title page.
- **No year on the title page.** Offord's McAuley, McAuley's Transformed, Booth-Tucker's Life of Catherine
  Booth, The Story of the Welsh Revival and Ellis's Madagascar are dated from a copyright notice or a preface,
  as their headers say. Ellis, vol. 2, prints no date of its own.
- **Bavinck:** Magnalia Dei is not the Dogmatiek. **Lipscomb:** Queries and Answers (1910) is his own writing,
  not the census letters. **Gurney:** the 1824 title reads "Religious Peculiarities".
## Era 10 (1906 to about 2010), batch 1, filled (2026-11-15): the major people, the conferences, and the Vatican's Acts to 1930

Source: `Build/Ministry/Operations/Audits/2026-11-12_wanted-sources-combined/Wanted_Sources.md`, era 10 rows 331-459 and
council rows 31-46, and the council leads on the era 10 scoping page. Rights: Mark's rulings of 2026-11-15 (R1 to R11 in
`Decision-Log.md`, "Era 10 rights rulings"; R12 in the entry for this batch). The search record, the hosts refused and the
cautions for writers are in `Build/Ministry/Operations/Audits/2026-11-15_library-era10/Search_Log.md`.

94 files, 10,208,969 words. Languages held beside English: Latin (the Acts of the Holy See, 1907, 1910, 1926, 1928), French
(Loisy, Beauduin), German (Barth, Tillich, Bultmann), Russian (Bulgakov), Romanian (the church law of 1925), Spanish (Aglipay,
Braga, the Padilla pamphlet) and Portuguese (Braga).

| want | state | file | imprint or rights basis | words | language | license |
|---|---|---|---|---:|---|---|
| era 10 row 331: Walter Rauschenbusch, Christianity and the Social Crisis. | filled | `rauschenbusch_christianity-and-the-social-crisis_1911.txt` | pd-us-by-date: printed 1911; the title-page year | 136,828 | eng | Public Domain |
| era 10 row 331: Walter Rauschenbusch, Christianizing the Social Order. | filled | `rauschenbusch_christianizing-the-social-order_1919.txt` | pd-us-by-date: printed 1919; the title-page year | 168,872 | eng | Public Domain |
| era 10 row 331: Walter Rauschenbusch, A Theology for the Social Gospel. | filled | `rauschenbusch_theology-for-the-social-gospel_1917.txt` | pd-us-by-date: printed 1917; the title-page year | 80,181 | eng | Public Domain |
| era 10 row 332: J. Gresham Machen, Christianity and Liberalism. | filled | `machen_christianity-and-liberalism_1923.txt` | pd-us-by-date: printed 1923; the title-page year | 62,704 | eng | Public Domain |
| era 10 row 335: Harry Emerson Fosdick, "Shall the Fundamentalists Win?" (1922). | filled | `fosdick_shall-the-fundamentalists-win-in-christian-century-v39-no23_1922.txt` | pd-us-by-date: printed 1922; the masthead date of the issue | 31,387 | eng | Public Domain |
| era 10 row 336: Cyrus Ingerson Scofield, The Scofield Reference Bible (1909; 1917). | filled | `scofield_scofield-reference-bible-new-and-improved-edition_1917.txt` | pd-us-by-date: printed 1917; the title page prints no year, so the date used is the copyright notice of 1917 on its verso | 1,095,114 | eng | Public Domain |
| era 10 row 336: a life of Scofield. | filled | `trumbull_life-story-of-c-i-scofield_1920.txt` | pd-us-by-date: printed 1920; the title page prints no year, so the date used is the copyright notice of 1920 | 30,043 | eng | Public Domain |
| council row 38: World's Christian Fundamentals Conference, Philadelphia 1919; and era 10 row 338: W. B. Riley. | filled | `world-conference-christian-fundamentals_god-hath-spoken-philadelphia_1919.txt` | pd-us-by-date: printed 1919; the title page prints no year, so the date used is the copyright notice of 1919 | 133,800 | eng | Public Domain |
| era 10 row 338: W. B. Riley, his sermons. | filled | `riley_christ-the-incomparable_1924.txt` | pd-us-by-date: printed 1924; the title page prints no year, so the date used is the copyright notice of 1924 | 54,513 | eng | Public Domain |
| era 10 row 406: William Jennings Bryan, the 1925 stenographic transcript. | filled | `scopes-trial_worlds-most-famous-court-trial-tennessee-evolution-case-3e_1925.txt` | pd-us-by-date: printed 1925; the title page prints no year, so the date used is the copyright notice of 1925 | 217,645 | eng | Public Domain |
| era 10 row 334: Reinhold Niebuhr (an early witness). | filled | `niebuhr_does-civilization-need-religion_1927.txt` | pd-us-by-date: printed 1927; the title-page year, read on the page image | 44,921 | eng | Public Domain |
| era 10 row 334: Reinhold Niebuhr, Moral Man and Immoral Society (1932). | filled | `niebuhr_moral-man-and-immoral-society_1936.txt` | US copyright not renewed: an American book copyrighted 1932, in a 1936 printing | 86,550 | eng | Public Domain (not renewed) |
| era 10: Fundamentalism (the census sources); serves rows 332, 336 and 338. | filled | `fundamentals_testimony-to-the-truth-v1_biola1917.txt` | pd-us-by-date: printed 1917; the title page prints no year, so the date used is the copyright notice "Copyrighted by Bible Institute of Los Angeles 1917", in the OCR | 124,021 | eng | Public Domain |
| era 10: Fundamentalism (the census sources); serves rows 332, 336 and 338. | filled | `fundamentals_testimony-to-the-truth-v2_biola1917.txt` | pd-us-by-date: printed 1917; the title page prints no year, so the date used is the copyright notice "Copyrighted by Bible Institute of Los Angeles 1917", in the OCR | 133,501 | eng | Public Domain |
| era 10: Fundamentalism (the census sources); serves rows 332, 336 and 338. | filled | `fundamentals_testimony-to-the-truth-v3_biola1917.txt` | pd-us-by-date: printed 1917; the title page prints no year, so the date used is the copyright notice "Copyrighted by Bible Institute of Los Angeles 1917", read on the page image, leaf 5; the OCR does not carry it | 125,656 | eng | Public Domain |
| era 10: Fundamentalism (the census sources); serves rows 332, 336 and 338. | filled | `fundamentals_testimony-to-the-truth-v4_biola1917.txt` | pd-us-by-date: printed 1917; the title page prints no year, so the date used is the copyright notice "Copyrighted by Bible Institute of Los Angeles 1917", read on the page image, leaf 5; the OCR does not carry it | 120,157 | eng | Public Domain |
| era 10 row 352: Pandita Ramabai, her own books. | filled | `ramabai_high-caste-hindu-woman_1888.txt` | pd-us-by-date: printed 1888; the title-page year | 29,988 | eng | Public Domain |
| era 10 row 352: Pandita Ramabai and the Mukti revival. | filled | `dyer_revival-in-india_1907.txt` | pd-us-by-date: printed 1907; the title-page year | 44,687 | eng | Public Domain |
| era 10 row 352: Pandita Ramabai, a life. | filled | `macnicol_pandita-ramabai-builders-of-modern-india_1926.txt` | pd-us-by-date: printed 1926; the title-page year | 47,853 | eng | Public Domain |
| Era 10, Azusa Street & Early Pentecostalism: an early Pentecostal's own book from outside North America (Mark, for the Library threads: global and any-language pieces). | filled | `barratt_in-the-days-of-the-latter-rain_1909.txt` | pd-us-by-date: printed 1909; the title-page year | 61,776 | eng | Public Domain |
| era 10 row 353: Kil Sŏn-ju, his own words. | filled | `korea-mission-field_v6-no4-april-1910.txt` | pd-us-by-date: printed 1910; the masthead date, read on the page image | 12,335 | eng | Public Domain |
| era 10 row 371: Sergei Bulgakov, his corpus (an early witness). | filled | `bulgakov_dva-grada-tom-2-rus_1911.txt` | pd-us-by-date: printed 1911; the title-page year, read on the page image | 86,006 | rus | Public Domain |
| era 10 row 371: Sergei Bulgakov, his corpus (an early witness). | filled | `bulgakov_tikhie-dumy-rus_1918.txt` | pd-us-by-date: printed 1918; the title-page year | 51,386 | rus | Public Domain |
| era 10 rows 376 and 377: Patriarch Tikhon; Metropolitan Sergius. | filled | `fedotoff_russian-church-since-the-revolution_1928.txt` | pd-us-by-date: printed 1928; "First published 1928", read on the page image | 24,347 | eng | Public Domain |
| era 10 row 376: Patriarch Tikhon, the 1918 anathema. | filled | `spinka_church-and-the-russian-revolution_1927.txt` | pd-us-by-date: printed 1927; the title-page year | 95,285 | eng | Public Domain |
| era 10 rows 376, 377 and 442: Patriarch Tikhon; Metropolitan Sergius, the Declaration of 1927 and the answers to it; Joseph of Petrograd. | filled | `emhardt_religion-in-soviet-russia-anarchy_1929.txt` | pd-us-by-date: printed 1929; the title page prints no year, so the date used is the copyright notice of 1929 | 141,541 | eng | Public Domain |
| era 10 row 443: Miron Cristea and the Romanian patriarchate (1925). | filled | `romanian-orthodox-church_legea-si-statutul-pentru-organizarea-ron_1925.txt` | pd-us-by-date: printed 1925; the title-page year | 20,839 | ron | Public Domain |
| era 10 row 414: George Tyrrell, his published works that drew the 1907 condemnations. | filled | `tyrrell_through-scylla-and-charybdis_1907.txt` | pd-us-by-date: printed 1907; the title-page year | 112,255 | eng | Public Domain |
| era 10 row 414: George Tyrrell, his published works that drew the 1907 condemnations. | filled | `tyrrell_much-abused-letter_1907.txt` | pd-us-by-date: printed 1907; the title-page year | 28,312 | eng | Public Domain |
| era 10 row 414: George Tyrrell, his published works that drew the 1907 condemnations. | filled | `tyrrell_medievalism-reply-to-cardinal-mercier_1908.txt` | pd-us-by-date: printed 1908; the title-page year | 53,784 | eng | Public Domain |
| era 10 row 414: George Tyrrell, his published works that drew the 1907 condemnations. | filled | `tyrrell_christianity-at-the-cross-roads_1909.txt` | pd-us-by-date: printed 1909; the title-page year | 67,156 | eng | Public Domain |
| era 10 row 416: Alfred Loisy, his published work condemned in 1907. | filled | `loisy_autour-d-un-petit-livre-2e-ed-fra_1903.txt` | pd-us-by-date: printed 1903; the title-page year | 61,566 | fra | Public Domain |
| era 10 row 416: Alfred Loisy, his published work condemned in 1907. | filled | `loisy_simples-reflexions-fra_1908.txt` | pd-us-by-date: printed 1908; the title-page year | 53,000 | fra | Public Domain |
| era 10 row 416: Alfred Loisy, his published work condemned in 1907. | filled | `loisy_gospel-and-the-church_home1903.txt` | pd-us-by-date: printed 1903; the title-page year | 58,979 | eng | Public Domain |
| era 10 rows 414 and 416: Lamentabili and Pascendi (1907) as the Roman side. | filled | `acta-sanctae-sedis_v40-lat_1907.txt` | pd-us-by-date: printed 1907; the title-page year | 180,580 | lat | Public Domain |
| era 10: The Catholic Church, Pius X to the Eve of the Council (the Roman side of the modernist crisis). | filled | `acta-apostolicae-sedis_v2-lat_1910.txt` | pd-us-by-date: printed 1910; the title-page year | 344,867 | lat | Public Domain |
| era 10 row 426: Pius XI, his address to the newly consecrated Chinese bishops (28 October 1926). | filled | `acta-apostolicae-sedis_v18-lat_1926.txt` | pd-us-by-date: printed 1926; the title-page year | 180,878 | lat | Public Domain |
| era 10 row 426: Pius XI, the encyclical Mortalium animos (1928). | filled | `acta-apostolicae-sedis_v20-lat_1928.txt` | pd-us-by-date: printed 1928; the title-page year | 140,985 | lat | Public Domain |
| era 10 rows 414 and 416: the modernist side, and Pascendi in an English of the time. | filled | `modernists_programme-of-modernism-with-pascendi_tyrrell1908.txt` | pd-us-by-date: printed 1908; the title-page year | 65,362 | eng | Public Domain |
| era 10 row 333: Karl Barth (Der Römerbrief was not found; this is his own book of addresses). | filled | `barth_wort-gottes-und-die-theologie-deu_1924.txt` | pd-us-by-date: printed 1924; the title-page year | 81,129 | deu | Public Domain |
| era 10 row 333: Karl Barth, in an English of the time. | filled | `barth_word-of-god-and-the-word-of-man_horton1928.txt` | pd-us-by-date: printed 1928; the title page prints no year, so the date used is the copyright notice of 1928 | 92,516 | eng | Public Domain |
| era 10 rows 366 and 342: Dom Lambert Beauduin; Virgil Michel. | filled | `beauduin_liturgy-the-life-of-the-church_michel1926.txt` | pd-us-by-date: printed 1926; the title-page year, confirmed on the page image | 31,045 | eng | Public Domain |
| era 10 row 366: Dom Lambert Beauduin, his own words in French. | filled | `beauduin_notre-piete-pendant-l-avent-fra_1919.txt` | pd-us-by-date: printed 1919; the title-page date | 32,274 | fra | Public Domain |
| era 10 row 399: Paul Tillich (an early witness; his Systematic Theology is in copyright). | filled | `tillich_religioese-lage-der-gegenwart-deu_1926.txt` | pd-us-by-date: printed 1926; the title page prints no year, so the date used is the copyright notice of 1926 | 35,934 | deu | Public Domain |
| era 10 row 400: Rudolf Bultmann (an early witness; his essay of 1941 is in copyright). | filled | `bultmann_jesus-deu_1926.txt` | pd-us-by-date: printed 1926; the title page prints no year; the date used is the dated afterword, "Marburg, März 1926", with which the library catalog date agrees | 54,133 | deu | Public Domain |
| era 10 row 424: the martyrs of the Cristero years (a print of the time, in Spanish). | filled | `padilla_esbozo-de-una-biografia-del-martir-luis-padilla-spa_1929.txt` | pd-us-by-date: printed 1929; the title-page year, read on the page image | 20,620 | spa | Public Domain |
| era 10 row 342: Virgil Michel, Orate Fratres from November 1926. | filled | `orate-fratres_v1-1926-1927.txt` | pd-us-by-date: printed 1926-1927; the dates on the volume title page and on the issues | 167,374 | eng | Public Domain |
| era 10 row 342: Virgil Michel, Orate Fratres from November 1926. | filled | `orate-fratres_v2-1927-1928.txt` | pd-us-by-date: printed 1927-1928; the dates on the volume title page and on the issues | 156,939 | eng | Public Domain |
| era 10 row 342: Virgil Michel, Orate Fratres from November 1926. | filled | `orate-fratres_v3-1928-1929.txt` | pd-us-by-date: printed 1928-1929; the dates on the volume title page and on the issues | 166,233 | eng | Public Domain |
| era 10 row 342: Virgil Michel, Orate Fratres from November 1926. | filled | `orate-fratres_v4-1929-1930.txt` | pd-us-by-date: printed 1929-1930; the dates on the volume title page and on the issues | 225,835 | eng | Public Domain |
| era 10 row 340: Peter Maurin, Easy Essays; and row 364: Dorothy Day. | filled | `maurin_catholic-radicalism-phrased-essays_1949.txt` | the book's own notice, on the verso of the title page: "The contents of this book are not copyrighted. The text may be reproduced by anyone in any desired form. May it be done for the greater honor and glory of God and the... | 60,456 | eng | Owner-declared free |
| era 10 row 364: Dorothy Day, The Catholic Worker paper. | filled | `catholic-worker_v37-no2-june-1969.txt` | the owner's statement, read 2026-11-15 at https://catholicworker.org/about/terms-of-use-and-privacy-policy/: "Content from The Catholic Worker paper is not copyrighted." The issue itself prints no copyright notice. Mark's... | 19,930 | eng | Owner-declared free |
| council row 46: the Third Lausanne Congress (Cape Town Commitment), 2010. | filled | `lausanne-movement_cape-town-commitment_2011.txt` | the document's own notice: "© 2011 The Lausanne Movement. This document may be reproduced in whole or in part without permission. The text should remain unchanged and an acknowledgement to The Lausanne Movement should be... | 22,544 | eng | Owner-declared free |
| council row 31: World Missionary Conference, Edinburgh 1910, the conference reports. | filled | `world-missionary-conference_edinburgh-1910-v1-report-of-commission-1_1910.txt` | pd-us-by-date: printed 1910; the title page prints the year only in the work's own title ("World Missionary Conference, 1910") and carries no separate imprint year, copyright notice or dated preface; the publishers on the... | 153,968 | eng | Public Domain |
| council row 31: World Missionary Conference, Edinburgh 1910, the conference reports. | filled | `world-missionary-conference_edinburgh-1910-v2-report-of-commission-2_1910.txt` | pd-us-by-date: printed 1910; the title page prints the year only in the work's own title ("World Missionary Conference, 1910") and carries no separate imprint year, copyright notice or dated preface; the publishers on the... | 142,690 | eng | Public Domain |
| council row 31: World Missionary Conference, Edinburgh 1910, the conference reports. | filled | `world-missionary-conference_edinburgh-1910-v3-report-of-commission-3_1910.txt` | pd-us-by-date: printed 1910; the title page prints the year only in the work's own title ("World Missionary Conference, 1910") and carries no separate imprint year, copyright notice or dated preface; the publishers on the... | 170,240 | eng | Public Domain |
| council row 31: World Missionary Conference, Edinburgh 1910, the conference reports. | filled | `world-missionary-conference_edinburgh-1910-v4-report-of-commission-4_1910.txt` | pd-us-by-date: printed 1910; the title page prints the year only in the work's own title ("World Missionary Conference, 1910") and carries no separate imprint year, copyright notice or dated preface; the publishers on the... | 128,765 | eng | Public Domain |
| council row 31: World Missionary Conference, Edinburgh 1910, the conference reports. | filled | `world-missionary-conference_edinburgh-1910-v5-report-of-commission-5_1910.txt` | pd-us-by-date: printed 1910; the title page prints the year only in the work's own title ("World Missionary Conference, 1910") and carries no separate imprint year, copyright notice or dated preface; the publishers on the... | 119,993 | eng | Public Domain |
| council row 31: World Missionary Conference, Edinburgh 1910, the conference reports. | filled | `world-missionary-conference_edinburgh-1910-v6-report-of-commission-6_1910.txt` | pd-us-by-date: printed 1910; the title page prints the year only in the work's own title ("World Missionary Conference, 1910") and carries no separate imprint year, copyright notice or dated preface; the publishers on the... | 189,948 | eng | Public Domain |
| council row 31: World Missionary Conference, Edinburgh 1910, the conference reports. | filled | `world-missionary-conference_edinburgh-1910-v7-report-of-commission-7_1910.txt` | pd-us-by-date: printed 1910; the title page prints the year only in the work's own title ("World Missionary Conference, 1910") and carries no separate imprint year, copyright notice or dated preface; the publishers on the... | 71,285 | eng | Public Domain |
| council row 31: World Missionary Conference, Edinburgh 1910, the conference reports. Also row 451: Cheng Jingyi. | filled | `world-missionary-conference_edinburgh-1910-v8-report-of-commission-8_1910.txt` | pd-us-by-date: printed 1910; the title page prints the year only in the work's own title ("World Missionary Conference, 1910") and carries no separate imprint year, copyright notice or dated preface; the publishers on the... | 87,513 | eng | Public Domain |
| council row 31: World Missionary Conference, Edinburgh 1910, the conference reports. Also row 450: V. S. Azariah. | filled | `world-missionary-conference_edinburgh-1910-v9-history-and-records_1910.txt` | pd-us-by-date: printed 1910; the title page prints the year only in the work's own title ("World Missionary Conference, 1910") and carries no separate imprint year, copyright notice or dated preface; the publishers on the... | 121,360 | eng | Public Domain |
| era 10 row 347: John R. Mott, his writings. | filled | `mott_evangelization-of-the-world-in-this-generation_1900.txt` | pd-us-by-date: printed 1900; the title-page year | 54,009 | eng | Public Domain |
| era 10 row 347: John R. Mott, his writings. | filled | `mott_decisive-hour-of-christian-missions_1910.txt` | pd-us-by-date: printed 1910; the title-page year | 62,157 | eng | Public Domain |
| era 10 row 347: John R. Mott, his writings. | filled | `mott_present-world-situation_1915.txt` | pd-us-by-date: printed 1915; the title-page year | 44,375 | eng | Public Domain |
| era 10 row 346: J. H. Oldham, his writings. | filled | `oldham_world-and-the-gospel_1916.txt` | pd-us-by-date: printed 1916; the title-page year | 62,810 | eng | Public Domain |
| era 10 row 346: J. H. Oldham, his writings. | filled | `oldham_christianity-and-the-race-problem_1924.txt` | pd-us-by-date: printed 1924; the title-page year | 103,539 | eng | Public Domain |
| Council leads (Wanted Sources and the era 10 scoping page): the Lambeth Conference of 1908. | filled | `lambeth-conference_1908-encyclical-letter-resolutions-and-reports_spck1908.txt` | pd-us-by-date: printed 1908; the title-page year | 66,812 | eng | Public Domain |
| Council leads (Wanted Sources and the era 10 scoping page): the Lambeth Conference of 1920. | filled | `lambeth-conference_1920-encyclical-letter-resolutions-and-reports_spck1920.txt` | pd-us-by-date: printed 1920; the title-page year | 73,817 | eng | Public Domain |
| Council leads (Wanted Sources and the era 10 scoping page): the Lambeth Conference of 1930. | filled | `lambeth-conference_1930-encyclical-letter-resolutions-and-reports_spck1930.txt` | pd-us-by-date: printed 1930; the title page prints the year only in the work's own title and carries no separate imprint year or copyright notice; the publishers on the title page are the Society for Promoting Christian... | 83,316 | eng | Public Domain |
| Council leads (the era 10 scoping page): Faith and Order, Lausanne 1927. | filled | `faith-and-order_lausanne-1927-proceedings_bate1927.txt` | pd-us-by-date: printed 1927; the title-page year | 203,883 | eng | Public Domain |
| Council leads (the era 10 scoping page): Life and Work, Stockholm 1925. | filled | `life-and-work_stockholm-conference-1925-official-report_bell1926.txt` | pd-us-by-date: printed 1926; the title-page year | 246,905 | eng | Public Domain |
| Council leads (the era 10 scoping page): the Jerusalem meeting of the International Missionary Council, 1928. | filled | `international-missionary-council_jerusalem-meeting-1928-v1_1928.txt` | pd-us-by-date: printed 1928; the title-page year | 152,992 | eng | Public Domain |
| Council leads (the era 10 scoping page): the Jerusalem meeting of the International Missionary Council, 1928. | filled | `international-missionary-council_jerusalem-meeting-1928-v2_1928.txt` | pd-us-by-date: printed 1928; the title-page year | 71,546 | eng | Public Domain |
| Council leads (the era 10 scoping page): the Jerusalem meeting of the International Missionary Council, 1928. | filled | `international-missionary-council_jerusalem-meeting-1928-v3_1928.txt` | pd-us-by-date: printed 1928; the title-page year | 115,375 | eng | Public Domain |
| Council leads (the era 10 scoping page): the Jerusalem meeting of the International Missionary Council, 1928. | filled | `international-missionary-council_jerusalem-meeting-1928-v4_1928.txt` | pd-us-by-date: printed 1928; the title-page year | 68,142 | eng | Public Domain |
| Council leads (the era 10 scoping page): the Jerusalem meeting of the International Missionary Council, 1928. | filled | `international-missionary-council_jerusalem-meeting-1928-v5_1928.txt` | pd-us-by-date: printed 1928; the title-page year | 55,783 | eng | Public Domain |
| Council leads (the era 10 scoping page): the Jerusalem meeting of the International Missionary Council, 1928. | filled | `international-missionary-council_jerusalem-meeting-1928-v6_1928.txt` | pd-us-by-date: printed 1928; the title-page year | 89,482 | eng | Public Domain |
| Council leads (the era 10 scoping page): the Jerusalem meeting of the International Missionary Council, 1928. | filled | `international-missionary-council_jerusalem-meeting-1928-v7_1928.txt` | pd-us-by-date: printed 1928; the title-page year | 40,725 | eng | Public Domain |
| Council leads (the era 10 scoping page): the Jerusalem meeting of the International Missionary Council, 1928. Also row 451: Cheng Jingyi. | filled | `international-missionary-council_jerusalem-meeting-1928-v8_1928.txt` | pd-us-by-date: printed 1928; the title-page year | 63,051 | eng | Public Domain |
| Council leads (the era 10 scoping page): the Panama Congress of 1916. | filled | `congress-christian-work-latin-america_panama-1916-v1_1917.txt` | pd-us-by-date: printed 1917; the title page prints no imprint year, so the date used is the copyright notice of 1917 | 200,575 | eng | Public Domain |
| Council leads (the era 10 scoping page): the Panama Congress of 1916. | filled | `congress-christian-work-latin-america_panama-1916-v2_1917.txt` | pd-us-by-date: printed 1917; the title page prints no imprint year, so the date used is the copyright notice of 1917 | 148,294 | eng | Public Domain |
| Council leads (the era 10 scoping page): the Panama Congress of 1916. | filled | `congress-christian-work-latin-america_panama-1916-v3_1917.txt` | pd-us-by-date: printed 1917; the title page prints no imprint year, so the date used is the copyright notice of 1917 | 199,060 | eng | Public Domain |
| Council leads (the era 10 scoping page): Protestantism in Latin America, the Montevideo Congress of 1925. | filled | `congress-christian-work-south-america_montevideo-1925-v1_1925.txt` | pd-us-by-date: printed 1925; the date used is the copyright notice of 1925 | 169,500 | eng | Public Domain |
| Council leads (the era 10 scoping page): Protestantism in Latin America, the Montevideo Congress of 1925. | filled | `congress-christian-work-south-america_montevideo-1925-v2_1925.txt` | pd-us-by-date: printed 1925; the date used is the copyright notice of 1925 | 159,300 | eng | Public Domain |
| era 10 row 451: Cheng Jingyi, his writings; and the Chinese Church entry. | filled | `national-christian-conference_chinese-church-as-revealed-shanghai-1922_1922.txt` | pd-us-by-date: printed 1922; the title page prints the year only in the work's own title and carries no separate imprint year, copyright notice or dated preface; the publisher on the title page is The Oriental Press, Shanghai,... | 312,338 | eng | Public Domain |
| era 10 row 450: V. S. Azariah, his own writing. | filled | `azariah_christ-in-the-indian-villages_1930.txt` | pd-us-by-date: printed 1930; "First published 3 June 1930" on the verso of the title page | 27,987 | eng | Public Domain |
| Era 10, Japanese Christianity after 1906 (the census names Uchimura): a Japanese Christian's own book in his own English. | filled | `uchimura_how-i-became-a-christian_1922.txt` | pd-us-by-date: printed 1922; the title-page year | 58,849 | eng | Public Domain |
| Era 10, Japanese Christianity after 1906: a Japanese Christian's own book. | filled | `kagawa_before-the-dawn_fukumoto-satchell1925.txt` | pd-us-by-date: printed 1925; the title-page year | 142,780 | eng | Public Domain |
| Era 10, Northeast India & the Mar Thoma Church (the census names Sundar Singh): an Indian Christian's own book. | filled | `sundar-singh_reality-and-religion_1924.txt` | pd-us-by-date: printed 1924; the title-page year | 13,563 | eng | Public Domain |
| Era 10, Northeast India & the Mar Thoma Church (the census names Sundar Singh): an Indian Christian's own book. | filled | `sundar-singh_search-after-reality_1925.txt` | pd-us-by-date: printed 1925; the title-page year | 19,743 | eng | Public Domain |
| Era 10, Protestantism in Latin America: Erasmo Braga's own account of the Panama Congress, in Portuguese. | filled | `braga_pan-americanismo-aspecto-religioso-por_1916.txt` | pd-us-by-date: printed 1916-1917; the title-page year of 1916 and the copyright notice of 1917 | 45,157 | por | Public Domain |
| Era 10, Protestantism in Latin America: Braga's account of the Panama Congress, in Spanish. | filled | `braga_pan-americanismo-aspecto-religioso-spa_monteverde1917.txt` | pd-us-by-date: printed 1917; the title-page year | 48,114 | spa | Public Domain |
| Era 10, The Philippine Independent Church in the Twentieth Century: the church's own catechism, in Spanish. | filled | `aglipay_catequesis-de-la-iglesia-filipina-independiente-spa_1912.txt` | pd-us-by-date: printed 1912; no year is legible on the title page; the date used is the dated prologue, "Madrid, á 25 de Mayo de 1912", with which the library catalog date agrees | 42,606 | spa | Public Domain |

### Era 10, batch 1: wanted rows not filled

| want (row) | result | where it stands |
|---|---|---|
| Alfred Loisy, L'Évangile et l'Église in French, 1902 (416) | held for Mark | The only scan (`lvangileetlglise00lois`) is of a Columbia University preservation film whose target reads "Reproductions may not be made without permission from Columbia University Library". The title page prints 1902. Not taken. The English of 1903 and two later French books are held. |
| Karl Barth, Der Römerbrief (333) | not found | archive.org has only printings after 1930. His addresses are held instead (German 1924, English 1928). The Barmen Declaration is cite and link (R4). |
| Fosdick's autobiography (335) | not searched | Printed after 1930. The sermon is held in its printing of June 8, 1922. |
| A life of Scofield that sets out the dispute (336) | not found | Trumbull's life of 1920 is held; it was printed in Scofield's lifetime. |
| Martin Luther King Jr. (337); the four girls of Sixteenth Street (407) | cite and link | Mark's ruling R10. Nothing searched. |
| W. B. Riley, The Menace of Modernism, 1917 (338) | not found | Two searches. His sermons of 1924 and the 1919 conference report are held. |
| Óscar Romero (339); Rutilio Grande (423) | not held | In copyright; by the era 10 scoping page, Romero's diary is online on a non-commercial permission (R3). Cite and link. |
| Stefan Wyszyński (341); Kominek (421); Klepacz (430); Blachnicki (422) | not searched | Church statements of 1956 and 1965 with no stated terms (R4): cite and link. |
| Virgil Michel, his own books to 1930 (342) | located | Only his 1918 thesis (`criticalprincipl0000unse`) is listed; not taken. Orate Fratres volumes 1 to 4 are held. |
| Watchman Nee, The Spiritual Man, 1928 (343) | not found | Searched in Chinese (屬靈人, 倪柝聲) and in English: only printings after 1960. |
| Dietrich Bonhoeffer (344) | not found | Sanctorum Communio (1930): only reprints of 1954 and later. His other books are in copyright. |
| Martin Niemöller (345) | not searched | The named sermons were printed after 1930. |
| Wei Enbo, the True Jesus Church (348) | not found | Searched in Chinese (真耶穌教會, 魏恩波) and English: nothing printed by 1930. |
| William J. Seymour: The Apostolic Faith, 1906-1908; Doctrines and Discipline, 1915 (349) | not found; located, not obtainable here | archive.org has no scan of the paper. The 1915 book exists only in a reissue of 2000, lending-only. The Flower Pentecostal Heritage Center's scans are on pentecostalarchives.org and its terms say "Photocopied materials and PDF files are for personal research only": held for Mark. |
| T. W. Rātana, Te Whetu Marama (350); M. J. Savage (396) | refused host | Papers Past answers with a bot check. Nothing on archive.org to 1930. |
| Janani Luwum (351); Festo Kivengere (355); William Nagenda (354); Joe Church (387) | not held | The Dictionary of African Christian Biography is CC BY-NC (R3): cite and link. Their own books are in copyright. |
| Pandita Ramabai, A Testimony; the Mukti Prayer-Bell (352) | not found | Her 1888 book, Dyer's Revival in India (1907) and Macnicol's life (1926, quoting A Testimony) are held. Dyer's life of 1900 was found, but the scan is cut off in chapter XII and was not taken. |
| William N. Blair, The Korea Pentecost (390, 353) | no date | The only scan (`koreapentecost00blai`) prints no year, no copyright notice and no dated preface. Not taken. |
| William Wadé Harris (356); Orimolade (357); Kimbangu (358); Babalola (380); Lekganyane (381); Lenshina (388); Spartas (392); Masowe (393); Matswa (394); Kivebulaya (398); Kiwanuka (417); Malula (418); Kagame (427); Abiodun (458); Ositelu (459) | not held | Casely Hayford's William Waddy Harris (1915), Lloyd's Apolo of the Pygmy Forest (1923) and any print of 1921-1930 on Kimbangu were not found on archive.org. The Dictionary of African Christian Biography has entries for most of them, but its licence is CC BY-NC 4.0 (R3) and many entries are reprinted with permission: cite and link. The searcher found no entry there for Lekganyane or Matswa. |
| R. E. McAlister (359); Frank Ewart and Glenn Cook (360) | not found; located, not obtainable here | Nothing printed by 1930. Ewart's Phenomenon of Pentecost exists only in a 1979 printing, lending-only. |
| G. T. Haywood (361) | no date | Three scans of his booklets print no year (`g.t._haywood_-_victim_of_the_flaming_sword`, `apostolicbiblere00hayw`, `teachingsofapost00hayw`). Not taken. |
| Victor Houteff, The Shepherd's Rod (362) | renewal found; wrong edition | Volume 2 (1932) was renewed in 1959 (R244963), so it is not held under R7. The scan offered as volume 1 (1930) is a revision of 1945 or later. |
| Felix Manalo, Pasugo (363) | not searched | The wanted list dates the paper from February 1939. |
| Dorothy Day, her books (364) | not held | In copyright. The paper is held in one scanned issue (June 1969); more original scans of the paper are wanted. |
| Josyf Slipyj (365); Havryil Kostelnyk (415) | not found | Nothing of theirs printed by 1930 was found. |
| Dom Lambert Beauduin, the Malines address of 1909 (366) | not found | The congress report and La piété de l'Église (1914) are not on archive.org. Michel's English of the book (1926) and a French work of 1919 are held. |
| Gabriel Hebert (367); Mother Maria Skobtsova (368); Florovsky (372); Lossky (373); Schmemann (436) | not held | Their named works were printed after 1930; no print of theirs to 1930 was found (Florovsky, Lossky) or searched (Hebert, Skobtsova, Schmemann). |
| Habib Girgis (369); Kyrillos VI (437) | no date | One Arabic book of Girgis (`AAlexandrina-102649`) prints no year. The journal al-Karma was not found. |
| Kyrion II (370); Ambrosi Khelaia (441); Ilia II (457) | not found | Searched in Russian, Georgian and English. |
| Sergei Bulgakov, Svet nevechernii; the Sophia controversy file (371) | not found | Two early books are held in Russian (1911, 1918), with poor OCR. |
| Iosif Trifa (374); Traian Dorz (438); Sandu Tudor (446) | not found | Only modern re-typeset files of Trifa were found. |
| Grigoris Balakian, Armenian Golgotha, 1922 (375); Khoren I (447) | not found | Only the 2009 English translation. The journal Etchmiadzin for 1918-1919 was located (`1918-12`), unchecked. |
| Patriarch Tikhon, a life; the council's acts (376); council row 37 | part filled; located | The anathema of 1918 is held in English (Spinka 1927). The council's Acts are on archive.org only inside a 1994 reprint (a reprint counts by its own date). The 1918 Definitions were not found; the Russian state libraries refuse the connection. |
| Metropolitan Sergius, both sides (377); Joseph of Petrograd (442) | part filled | The declaration is held in English (Emhardt 1929). The Solovki bishops' answer is quoted there in parts only; no full text of a rejection was found. |
| Brother Roger (378); Wierwille (379); Sun Myung Moon (385); Eusebio Joaquín (389); the Rodens (395); Tillich's and Bultmann's later works (399, 400); Keeble (403); Andreasen (404); Dodd (405); Jim Jones (408); Barnhouse (409); Froom (410); Martin (411); Goodpasture (412); Cogdill (413); Tempels (419); Tian (420); Proaño (429); Bugnini (431); Tewophilos (433); Mar Shimun XXIII (434); Basilios (439); Antonios (455); John Sung (449); Peters (452); Ju Gi-cheol (453); Desmond Ford (454); Gatu (456) | not held | In copyright, unprinted, or with no stated terms. Keeble's Biography and Sermons (1931), the Cogdill-Woods Debate (1958) and Andreasen's Letters (1959) were searched as non-renewal candidates: no scan of the first two; the only Andreasen scan is a 1981 reprint. |
| Paul VI (382); Athenagoras I (383); Lefebvre (384); Pius XII (425); John XXIII (432); the Cristero canonization homily (424); Alexy I (435) | cite and link | Vatican texts after 1930 (R1) and church statements with no stated terms (R4). |
| Frank Bartleman, How Pentecost Came to Los Angeles, 1925 (386) | not found; no date | Not on archive.org. His Two Years Mission Work in Europe (`twoyearsmissionw0000fran`) prints no year. |
| Jessie Penn-Lewis (391) | no date; not found | The only scan of War on the Saints (`dli.ernet.238131`, fourth edition) prints no year. The Awakening in Wales was not found in an early printing. |
| Clarence Larkin, Dispensational Truth (401) | located, later printings only | Four scans, all later printings: one "Twenty-eighth printing", three with a ZIP code in the publisher's address. Their only dates are the copyright lines of 1918 and 1920. Not taken. |
| Curtis Lee Laws, the Watchman-Examiner, 1 July 1920 (402) | not found | The only scans of the paper are a 1913 volume and lending-only volumes of 1966-67. The Annual of the Northern Baptist Convention 1920 (`annualofnorthern0000amer_t8j4`) was located; it has the resolutions of the Fundamentals conference and not the word "fundamentalists". Not taken. |
| Surma Khanim, Assyrian Church Customs, 1920 (448) | not found | Three searches. |
| Abdul Masih II and Baselios Paulose I, 1912 (440) | located | Malayalam church monthlies of 1900-1911 (`1911_Malankara_Edavaka_Pathrika_Volume_20_Issue_01-03` and others) and Panjikaran's Syrian Church in Malabar (1912, `cu31924029361338`) were located and not checked. No issue of 1912 was found. |
| Miron Cristea, his own works (443); Dimitrije (444); Kiril (445) | part filled | The Romanian law and statute of 1925 are held. Serbian and Bulgarian prints were not found. |
| Cheng Jingyi, in Chinese (451) | not found | His speeches of 1910, 1922 and 1928 are held in English. |
| Council rows 32 Barmen; 33 Amsterdam 1948; 34 Vatican II; 35 Lausanne 1974; 36 Chicago 1978; 39 Rio 1955; 40 New Delhi 1961; 41 Medellín 1968; 42 Chicago 1973; 43 Taizé 1974; 44 Manila 1989; 45 Moscow 2000 | cite and link | R1, R3 and R4. Nothing held. |

**Held already, found by this batch.** Mirbt's Quellen (1911) and Denzinger (1911) both carry the decree Lamentabili and
the encyclical Pascendi of 1907 in Latin: `mirbt_quellen-zur-geschichte-des-papsttums-3e-aufl-deu-lat_1911.txt` from about
line 29196, and `denzinger_enchiridion-symbolorum-lat_bannwart1911.txt` from about line 32457 (extracts).
## Era 8 (1650-1815), batch 1 (2026-11-15): the global files (Africa, Egypt, Ethiopia, the Syriac churches, Latin America, Asia)

Thirty files. The wants are the era 8 rows of the Who scan's wanted list (`Wanted_Sources.md`, rows 121-162),
the era 8 Open-Gaps items (175-182, 225) and the earlier batches' open rows, for the regions outside Europe and
North America; the rest of era 8 follows in later batches. The master list and the search record are in
`Build/Ministry/Operations/Audits/2026-11-15_library-era8/` (`ERA8_WANTS_MASTER.md`, `Search_Log.md`). Every file
has a printed imprint of 1930 or earlier, read on its title page or the scan's page image; Rhodes's Cathechismus
prints no year on its title page and is dated by the printed licence on the next leaf. Rows in the tables above
are not rewritten.

| want | state | file(s), with the imprint year | words | language | shelf |
|---|---|---|---:|---|---|
| Wanted row 122, 153, 154 (major): Kimpa Vita, Bernardo da Gallo, Pedro IV: the Capuchin relations of da Gallo and da Lucca | not found | no print by 1930 on archive.org; Zucchelli's Italian not found (the German of 1715 is held) | | | |
| Open-Gaps 175 (AF-3): Kongo after 1650, Proyart | filled in French (the English is held in Pinkerton XVI) | `proyart_histoire-de-loango-kakongo-et-autres-royaumes-d-afrique-fra_1776.txt` (1776) | 74,936 | fra | kongo-christianity-after-1650, context (part 1 needs-ruling) |
| Batch 2 (AF-8), Open-Gaps 175: Philip Quaque and the S.P.G. in West Africa | filled, a digest of the Society's records | `pascoe_two-hundred-years-of-the-spg-v1_1901.txt` (1901) | 424,914 | eng | restoration-georgian-church-of-england, context |
| Batch 2 (AF-8): Capitein; Thompson's own account | not found | Capitein only in a modern translation; Thompson (1758) is an image-only scan | | | |
| Open-Gaps 175 (AF-4): the Dutch Reformed Church at the Cape, McCarter | filled | `mccarter_dutch-reformed-church-in-south-africa_1869.txt` (1869) | 29,343 | eng | the-dutch-reformed-church-at-the-cape, tradition |
| Open-Gaps 175 (AF-4): the Acta Synodi of 1857 in Dutch | not searched | era 9 | | | |
| Open-Gaps 175 (AF-5): Ntsikana's hymn in Xhosa | not found | no print by 1930 found | | | |
| Wanted row 152: Ibrahim al-Jawhari: al-Jabarti's obituary | filled in French | `jabarti_merveilles-biographiques-et-historiques-t5-fra_1890.txt` (1890) | 74,540 | fra | the-coptic-church-under-the-ottomans, context |
| Wanted row 152: Butcher, vol. 2 | held already (the era 9 batch vendored it); an era 8 shelf row added | `butcher_story-of-the-church-of-egypt-v2_1897.txt` (1897) | 144,216 | eng | the-coptic-church-under-the-ottomans, context |
| Open-Gaps 175: Vansleb, Histoire de l'Église d'Alexandrie | filled | `vansleb_histoire-de-l-eglise-d-alexandrie-fra_1677.txt` (1677) | 75,236 | fra | the-coptic-church-under-the-ottomans, context |
| Open-Gaps 175: Vansleb on the Copts, his journal | filled in French and in English | `vansleb_nouvelle-relation-d-un-voyage-fait-en-egypte-fra_1677.txt` (1677); `vansleb_present-state-of-egypt_1678.txt` (1678) | 92,156; 74,629 | fra; eng | the-coptic-church-under-the-ottomans, context |
| Open-Gaps 175: the Arabic History of the Patriarchs for the Ottoman patriarchs; the archons' letters and waqf deeds | not found | not on archive.org in a print by 1930 | | | |
| Wanted row 151: Bruce, Travels, vols 2 and 3 | filled | `bruce_travels-to-discover-the-source-of-the-nile-v2_1790.txt`; `bruce_travels-to-discover-the-source-of-the-nile-v3_1790.txt` (1790) | 212,558; 229,966 | eng | ethiopian-christianity-gondar-to-the-zemene-mesafint, context |
| Open-Gaps 175 (AF-1): Guidi, Annales | filled: the Ge'ez text and a French translation | `annales-regum-iyasu-ii-et-iyoas_textus-gez_guidi1910.txt` (1910); `annales-regum-iyasu-ii-et-iyoas_versio-fra_guidi1912.txt` (1912) | 129,417; 113,770 | gez; fra | ethiopian-christianity-gondar-to-the-zemene-mesafint, tradition |
| Open-Gaps 175 (AF-1): Weld Blundell, The Royal Chronicle of Abyssinia (1922) | located, not taken | the one scan has no dated title page, preface or copyright notice | | | |
| Census VII.38, VII.34: Gobat, Journal (London, 1834) | filled | `gobat_journal-of-a-three-years-residence-in-abyssinia_1834.txt` (1834) | 112,098 | eng | ethiopian-christianity-gondar-to-the-zemene-mesafint, context |
| Batch 2 (ME-7), Open-Gaps 179: the Syriac Orthodox patriarchate, Parry (1895) | located, not taken in this batch | the Columbia microfilm scan (sixmonthsinsyria00parr) carries the library's line 'Reproductions may not be made without permission from Columbia University Library'; a Google scan of the same edition (sixmonthsinasyr00parrgoog) is left for the next batch | | | |
| Open-Gaps 179 (ME-2): the Synod of Mount Lebanon, 1736 | not found | Collectio Lacensis, vol. 2, and Mansi 38 are not on archive.org | | | |
| Melkite split of 1724: Charon, tome I | not found | tome I was never printed | | | |
| Open-Gaps 177: the Varthamanappusthakam; Malayalam originals; Ittoop; E. M. Philip | not found | no print by 1930 found | | | |
| Wanted row 123 (major): Vieira, Maria Rosa Mystica | filled | `vieira_maria-rosa-mystica-parte1-por_1686.txt` (1686); `vieira_maria-rosa-mystica-parte2-por_1688.txt` (1688) | 216,909; 192,435 | por | colonial-latin-american-devotional-catholicism, society-of-jesus-1650-1814, tradition |
| Wanted row 123 (major): a Life of Vieira, Barros | filled | `barros_vida-do-apostolico-padre-antonio-vieyra-por_1746.txt` (1746) | 190,875 | por | the same two, tradition |
| Wanted row 123 (major): Vieira's Cartas | filled, tomos 1 and 2 | `vieira_cartas-tomo1-por_1735.txt`; `vieira_cartas-tomo2-por_1735.txt` (1735) | 88,664; 89,293 | por | the same two, tradition |
| Open-Gaps 176 (LA8-4): Antonil | filled | `antonil_cultura-e-opulencia-do-brasil-por_1711.txt` (1711) | 62,040 | por | colonial-latin-american-devotional-catholicism, tradition |
| Open-Gaps 176 (LA8-6): the Code noir (1685) | filled, in a collection of 1767 | `code-noir_recueil-des-reglemens-colonies-francoises-fra_prault1767.txt` (1767) | 68,904 | fra | colonial-latin-american-devotional-catholicism, context (needs-ruling) |
| Wanted row 155: Úrsula de Jesús | not found | no print by 1930; the 2004 edition is in copyright | | | |
| Open-Gaps 176 (LA8-10): Ximénez for Cancuc | held for Mark | vols 1 (1929) and 2 are CC BY-NC-ND 3.0 uploads; vol. 3, with Cancuc, is dated 1931 | | | |
| Open-Gaps 176 (LA8-5): Hernández y Dávalos; Morelos | not found | not on archive.org | | | |
| Wanted row 124 (major): Maigrot's Mandate of 1693 in a printing of the time | filled in Latin | `historia-cultus-sinensium_varia-scripta-de-cultibus-sinarum-lat_1700.txt` (1700) | 155,815 | lat | chinese-catholicism-1650-1906, tradition; Charmot's notes in the same volume, tradition (needs-ruling) |
| Wanted rows 124, 125 (major): Launay, Histoire générale, vol. 1 | filled, tomes 1 and 2 (to 1836) | `launay_histoire-generale-de-la-societe-des-missions-etrangeres-t1-fra_1894.txt`; `launay_histoire-generale-de-la-societe-des-missions-etrangeres-t2-fra_1894.txt` (1894) | 212,971; 208,847 | fra | vietnamese-catholicism-to-1815, chinese-catholicism-1650-1906, context |
| Wanted row 125 (major): Pallu's own Relation | filled | `pallu_relation-abregee-des-missions-et-des-voyages-des-evesques-francois-fra_1682.txt` (1682) | 18,786 | fra | vietnamese-catholicism-to-1815, chinese-catholicism-1650-1906, tradition |
| Wanted row 125 (major): Lambert de la Motte's own writings; the Monita; Launay's Lettres de Mgr Pallu | not found | Launay tome 1 summarizes the Monita | | | |
| Wanted row 126 (major): Rhodes, Divers voyages | filled, the printing of 1682 | `rhodes_divers-voyages-de-la-chine-et-autres-royaumes-de-l-orient-fra_1682.txt` (1682) | 87,428 | fra | vietnamese-catholicism-to-1815, tradition (needs-ruling: the missions it tells come before the window) |
| Wanted row 126 (major), Open-Gaps 178: Rhodes, the Cathechismus | filled; only the Latin can be read | `rhodes_cathechismus-in-octo-dies-divisus-lat-vie_1651.txt` (1651, by the printed licence) | 117,211 | lat, vie | vietnamese-catholicism-to-1815, tradition (needs-ruling) |
| Wanted row 126 (major): Rhodes's history of Tonkin | filled in Latin | `rhodes_tunchinensis-historiae-libri-duo-lat_1652.txt` (1652) | 61,508 | lat | vietnamese-catholicism-to-1815, tradition (needs-ruling) |
| Wanted row 126: Rhodes's catechism in modern Vietnamese | held for Mark | the one upload is CC BY-NC-ND 4.0 | | | |
| Wanted row 127 (major), Open-Gaps 178: the Sketch of the Catholic Church in Ceylon | filled | `ceylon-catholic-church_sketch-of-the-rise-and-progress_1848.txt` (1848) | 8,154 | eng | catholics-of-dutch-ceylon, context (needs-ruling) |
| Wanted row 127 (major): Rego's Life of Joseph Vaz; any English Life | not found | no print by 1930 on archive.org | | | |
| Wanted row 156, Open-Gaps 178: Baldaeus | filled in Dutch and in English | `baldaeus_naauwkeurige-beschryvinge-van-malabar-en-choromandel-en-ceylon-nld_1672.txt` (1672); `baldaeus_true-and-exact-description-of-malabar-and-coromandel-and-ceylon_churchill1703.txt` (1703) | 431,810; 265,623 | nld; eng | protestant-churches-of-the-voc-world, tradition; catholics-of-dutch-ceylon, context |
| Open-Gaps 178: Valentijn, the church of Amboina | filled, the third deel | `valentijn_oud-en-nieuw-oost-indien-deel3-nld_1726.txt` (1726) | 820,153 | nld | protestant-churches-of-the-voc-world, tradition |
| Open-Gaps 178: the Leijdecker Bible of 1733; Ambon church records | not searched | Valentijn's third deel tells the Bible dispute | | | |
| Batch 5, Open-Gaps 177: a Chinese Catholic's own text (Huang Bolu; André Ly; the Sichuan synod) | not found | no scan found | | | |
| Batch 5, Open-Gaps 177: Japan's hidden Christians (Tenchi hajimari no koto; Urakawa) | not found | no print by 1930 found | | | |
| Open-Gaps 279 (era 4), looked at again: Abu Qurrah, Bacha's French of a second treatise | rights now clear, not taken for its OCR | the preface is dated 'Paris, 20 septembre 1905' and the archive.org record's date is 1905; in the one scan (untraitdesesuvr00kurrgoog) about half the pages have the ends of their lines cut off, and the Arabic is not in the OCR | | | |
| Open-Gaps 225: an outside witness of 1650-1815 from the Muslim majority | filled in part | al-Jabarti, tome V, above | | | |

**Cautions for profile writers.**
- Line numbers in every header and row are lines of the host OCR; add 12 for the file's own lines.
- Proyart (1776): the French mission to Loango and Kakongo, not the kingdom of Kongo and not the Antonian
  movement. Letters of the prefects are quoted inside part 2.
- Pascoe (1901): a digest written by the Society's assistant secretary. Philip Quaque's words appear only where the digest
  quotes his letters; quote them as Pascoe prints them. The file is the first bound volume and stops inside the
  chapters on India.
- McCarter (1869): the appendix prints the Church Ordinance, which is not his voice. His preface speaks of
  "several years' pastoral labour among the South African Dutch colonists".
- Bruce (1790): the long s is read as f throughout and vol. 2's OCR is noisy, so check every quotation against
  the page image. The stoning of the missionaries is under King David's reign in vol. 2 (file lines about
  25638-25965); the chapter on religion is in vol. 3.
- Butcher (1897): a secondary account. Ibrahim al-Jawhari is in one footnote, spelled "Ibrahim-el Johari"; the
  name "Johar" elsewhere in the volume is the Fatimid general.
- Al-Jabarti (1890): a French translation by four named translators. The Coptic official is "Moallem Ibrahim el
  Djohari" under the year 1209; the other "El Djohari" passages are other men and a book title.
- Vansleb (1677, 1678): a Dominican's account. His catalog of the patriarchs is drawn from Arabic authors he
  names. The English is signed only "M. D., B. D."; the host's name for the translator is not in the print.
- Gobat (1834): three voices in one volume (the Society's preface, Professor Lee's history, Gobat's journal).
  The OCR is poor; check quotations against the page image.
- Guidi's Annales: the translation is French, not Latin. The Ge'ez text came through in Ethiopic letters but has
  not been checked against the print; treat it as a second witness. The title pages name no author.
- Vieira, Maria Rosa Mystica: sermon XIV (part 1) is headed as preached to the brotherhood of the Blacks of a
  sugar mill in Bahia in 1633; sermons XX and XXVII (part 2) speak of the Blacks and the enslaved in the body of
  the text, not in their headings. Sermon XV's heading was not found. Two columns are run together in places.
- Vieira, Cartas (1735): tomo 2 starts its numbering again at I, so cite the tomo with the letter number.
- Barros (1746): a Life; its subject is Vieira and its voice is Barros.
- The Code noir (1767): a collection of royal acts from 1675 to 1762. The Edict of March 1685 is file lines
  1284-2405; the Louisiana edict of 1724 is a different text.
- Launay (1894): written two centuries after the founders. The first synod of Tonkin (14 February 1670) is told
  in a few lines, not printed; the page appears twice, and the first copy's OCR reads the year as 1679. Maigrot's
  Mandate is quoted in French; the OCR reads its date as "26 mars 1698" where the Latin print has 26 March.
- Historia cultus Sinensium (1700): several authors in one volume. Maigrot's Mandate is file lines 15635-15933;
  the OCR garbles the year in its date line. A second title page follows it. The long first piece is Nicolas
  Charmot's notes, not a narrative history. The Jesuit pieces are in the appendix; cite each piece by its own
  author.
- Pallu (1682): the privileges and approbations at the head name Bourges's Relation and are dated 1665-1666;
  the dedication is dated April 1668; the title page is 1682.
- Rhodes: the Divers voyages is the printing of 1682. In the Cathechismus only the Latin can be quoted; the
  Vietnamese column is garbled and its headings for days 2 to 7 were not found. The title page of the Divers
  voyages names no author; the attribution is the host's. The missions all three describe come before the
  entry's window, which opens in 1650; the prints are of 1651, 1652 and 1682.
- The Sketch of Ceylon (1848): written after the entry's window; no author is named in the print. A regulation of 1806 and a minute of 1819 are
  printed inside the text.
- Baldaeus (1672, 1703): the English is a translation with no translator named; the OCR of its letterpress title
  reads the Dutch year as 1572. Use the Dutch for wording.
- Valentijn (1726): the church of Amboina is the first three books of the first stuk; the fourth and fifth are
  natural history. The second stuk covers other lands, and church matters there were not mapped.

## Era 9 (1815-1906), batch 2b (2026-11-15): rows 227-245, 249-262, 267-278, 323 and 327-330

Sixty-one files for 49 person rows of
`Build/Ministry/Operations/Audits/2026-11-12_wanted-sources-combined/Wanted_Sources.md`, and the date check
batch 1 left on row 223. The search record is
`Build/Ministry/Operations/Audits/2026-11-15_library-era9-b2b/Search_Log.md`. Every file has a printed year of
1930 or earlier: on its title page (six read on the scan's page image), or, for twelve whose title page
prints none, in a copyright notice, a dated preface the catalogue agrees with, or the title itself; each header
says which. Google's own preamble was stripped from twelve files at intake, and each header says what went.
Line numbers in these headers are the file's own lines.

| want | state | file(s), with the year | shelf |
|---|---|---|---|
| era 9 row 227, Walter Scott: a Life told by another | filled | `baxter-w_life-of-elder-walter-scott_1874.txt` (1874); 139,679 words; eng | the-stone-campbell-restoration-movement, context |
| era 9 row 228, 'Raccoon' John Smith: a Life told by another | filled | `williams-j-a_life-of-elder-john-smith_1870.txt` (1870); 184,885 words; eng | the-stone-campbell-restoration-movement, context |
| era 9 row 229, Peter Cartwright: his Autobiography | filled | `cartwright_autobiography-of-peter-cartwright_strickland1857.txt` (1857); 162,070 words; eng | the-second-great-awakening-and-camp-meeting-worl, nineteenth-century-methodism, tradition |
| era 9 row 233, Amanda Berry Smith: her Autobiography | filled | `smith-amanda_autobiography-story-of-the-lords-dealings_1893.txt` (1893); 214,885 words; eng | the-holiness-movement, the-black-church-in-america, tradition |
| era 9 row 234, Hannah Whitall Smith: The Christian's Secret of a Happy Life | filled | `smith-hannah-whitall_christians-secret-of-a-happy-life_rev-ed1888.txt` (1888); 65,664 words; eng | the-holiness-movement, tradition |
| era 9 row 234, Hannah Whitall Smith: her spiritual autobiography | filled | `smith-hannah-whitall_unselfishness-of-god_1903.txt` (1903); 81,241 words; eng | the-holiness-movement, tradition |
| era 9 row 235, John S. Inskip: a Life told by others | filled | `mcdonald-searles_life-of-rev-john-s-inskip_1885.txt` (1885); 123,420 words; eng | the-holiness-movement, context |
| era 9 row 236, Robert P. Wilder: the report of the movement's first convention, with his addresses | filled | `student-volunteer-movement_report-first-international-convention-cleveland_1891.txt` (1891); 99,836 words; eng | the-student-volunteer-movement-and-edinburgh-191, tradition |
| era 9 row 239, William Taylor: Story of My Life | filled | `taylor-william_story-of-my-life_ridpath1895.txt` (1895); 406,560 words; eng | nineteenth-century-methodism, tradition |
| era 9 row 329, Charles M. Sheldon: In His Steps | filled | `sheldon_in-his-steps_1897.txt` (1897); 84,862 words; eng | the-social-gospel, tradition |
| era 9 row 330, George and Sarah Clarke: Sarah Clarke's own account of the mission | filled | `clarke_founding-of-pacific-garden-mission_1914.txt` (1914); 7,438 words; eng | the-rescue-mission-movement, tradition |
| era 9 row 231, Zilpha Elaw: her Memoirs | filled | `elaw_memoirs-of-mrs-zilpha-elaw_1846.txt` (1846); 46,894 words; eng | the-black-church-in-america, tradition |
| era 9 row 232, Julia Foote: A Brand Plucked from the Fire | filled | `foote_brand-plucked-from-the-fire_1879.txt` (1879); 25,037 words; eng | the-black-church-in-america, tradition |
| era 9 row 238, James Varick: Rush's Short Account of the African Methodist Episcopal Church | filled | `rush_short-account-rise-and-progress-african-me-church_1843.txt` (1843); 24,644 words; eng | nineteenth-century-methodism, the-black-church-in-america, tradition |
| era 9 row 240, James Robinson Graves: Old Landmarkism | filled | `graves_old-landmarkism-what-is-it_1880.txt` (1880); 63,892 words; eng | nineteenth-century-baptists, tradition |
| era 9 row 241, William Bullein Johnson: The Gospel Developed | filled | `johnson-w-b_gospel-developed_1846.txt` (1846); 45,426 words; eng | nineteenth-century-baptists, tradition |
| era 9 row 243, John Wilbur: his Journal | filled | `wilbur_journal-of-the-life-of-john-wilbur_1859.txt` (1859); 274,150 words; eng | nineteenth-century-quakerism-separations, tradition |
| era 9 row 244, Lucretia Mott: a Life with her letters | filled | `hallowell_james-and-lucretia-mott-life-and-letters_1884.txt` (1884); 190,741 words; eng | nineteenth-century-quakerism-separations, context |
| era 9 row 245, Levi Coffin: his Reminiscences | filled | `coffin_reminiscences-of-levi-coffin_1876.txt` (1876); 205,688 words; eng | nineteenth-century-quakerism-separations, tradition |
| era 9 row 261, Ralph Waldo Emerson: the Address of 1838 | filled | `emerson_address-before-the-senior-class-in-divinity-college_1838.txt` (1838); 7,788 words; eng | american-unitarianism-universalism-consolidations, tradition |
| era 9 row 261, Ralph Waldo Emerson: a Life told by another (vol. 1) | filled | `cabot_memoir-of-ralph-waldo-emerson-v1_1887.txt` (1887); 96,694 words; eng | american-unitarianism-universalism-consolidations, context |
| era 9 row 262, Dorothea Dix: a Life told by another | filled | `tiffany_life-of-dorothea-lynde-dix_1890.txt` (1890); 125,351 words; eng | american-unitarianism-universalism-consolidations, context |
| era 9 row 249, Hiram Edson: his own discourse of 1849 (his account of the morning after was not found in print) | filled | `edson_time-of-the-end_1849.txt` (1849); 16,050 words; eng | restorationist-apocalyptic-ferment-and-adventism, tradition |
| era 9 row 250, Joseph Bates: his Autobiography | filled | `bates_autobiography-of-elder-joseph-bates_1868.txt` (1868); 97,858 words; eng | restorationist-apocalyptic-ferment-and-adventism, tradition |
| era 9 row 251, Emma Hale Smith: the hymnbook of 1835 | filled | `smith-emma_collection-of-sacred-hymns_kirtland1835.txt` (1835); 20,721 words; eng | latter-day-saints-lds, tradition |
| era 9 row 252, Eliza R. Snow: her poems (vol. 1) | filled | `snow_poems-religious-historical-and-political-v1_1856.txt` (1856); 42,399 words; eng | latter-day-saints-lds, tradition |
| era 9 row 256, John Bate Cardale: Readings upon the Liturgy | filled | `cardale_readings-upon-the-liturgy_1851.txt` (1851); 235,023 words; eng | catholic-apostolic-church-irvingites, tradition |
| era 9 row 257, Henry Drummond: Dialogues on Prophecy, vol. 1 (the volume names no author and no place of meeting) | filled | `dialogues-on-prophecy_v1_1828.txt` (1828); 114,815 words; eng | catholic-apostolic-church-irvingites, antecedent |
| era 9 row 257, Henry Drummond: his speeches in Parliament, with a sketch of his political career (vol. 1) | filled | `drummond-henry_speeches-in-parliament-v1_lovaine1860.txt` (1860); 180,112 words; eng | catholic-apostolic-church-irvingites, tradition |
| era 9 row 259, Benjamin Wills Newton: his own writing | filled | `newton-b-w_thoughts-on-the-apocalypse_2nd-ed1853.txt` (1853); 136,040 words; eng | plymouth-brethren-and-dispensational-formation, tradition |
| era 9 row 259, Benjamin Wills Newton: an account of the division by another | filled | `neatby_history-of-the-plymouth-brethren_1901.txt` (1901); 113,539 words; eng | plymouth-brethren-and-dispensational-formation, context |
| era 9 row 237, Jabez Bunting: a Life told by his son (vol. 1) | filled | `bunting-t-p_life-of-jabez-bunting-v1_1859.txt` (1859); 167,782 words; eng | nineteenth-century-methodism, context |
| era 9 row 242, John Clifford: a Life told by another | filled | `marchant_dr-john-clifford_1924.txt` (1924); 149,558 words; eng | nineteenth-century-baptists, context |
| era 9 row 267, Richard Hurrell Froude: his Remains (part 1, vol. 1) | filled | `froude_remains-pt1-v1_1838.txt` (1838); 130,881 words; eng | the-oxford-movement-and-anglo-catholic-revival, tradition |
| era 9 row 268, Priscilla Lydia Sellon: her bishop's letter to her | filled | `phillpotts_letter-to-miss-sellon_1852.txt` (1852); 6,670 words; eng | the-oxford-movement-and-anglo-catholic-revival, context |
| era 9 row 268, Priscilla Lydia Sellon: a critic's pamphlet of 1852 | filled | `colles_sisters-of-mercy-sisters-of-misery_1852.txt` (1852); 9,194 words; eng | the-oxford-movement-and-anglo-catholic-revival, context |
| era 9 row 271, Lord Shaftesbury: a Life told by another (vol. 1) | filled | `hodder_life-and-work-of-seventh-earl-of-shaftesbury-v1_1887.txt` (1887); 196,699 words; eng | victorian-church-of-england, context |
| era 9 row 272, Samuel Wilberforce: a Life with his diaries and letters (vol. 1) | filled | `ashwell_life-of-samuel-wilberforce-v1_1880.txt` (1880); 201,928 words; eng | victorian-church-of-england, context |
| era 9 row 273, Frederick Denison Maurice: Theological Essays | filled | `maurice_theological-essays_2nd-ed1853.txt` (1853); 141,158 words; eng | victorian-church-of-england, tradition |
| era 9 row 273, Frederick Denison Maurice: a Life told in his letters (vol. 1) | filled | `maurice-f_life-of-frederick-denison-maurice-v1_1884.txt` (1884); 210,263 words; eng | victorian-church-of-england, context |
| era 9 row 274, John William Colenso: The Pentateuch and Book of Joshua, part I | filled | `colenso_pentateuch-and-book-of-joshua-pt1_1862.txt` (1862); 74,466 words; eng | victorian-church-of-england, tradition |
| era 9 row 274, John William Colenso: Ten Weeks in Natal | filled | `colenso_ten-weeks-in-natal_1855.txt` (1855); 101,641 words; eng | victorian-church-of-england, southern-african-mission-churches, tradition |
| era 9 row 275, Charles Longley: the documents of the Lambeth Conference of 1867 | filled | `lambeth-conferences_1867-1878-1888_davidson1889.txt` (1889); 118,657 words; eng | victorian-church-of-england, tradition |
| era 9 row 278, Nicholas Wiseman: Recollections of the Last Four Popes | filled | `wiseman_recollections-of-the-last-four-popes_1858.txt` (1858); 119,694 words; eng | catholic-church-long-nineteenth-century, tradition |
| era 9 row 278, Nicholas Wiseman: his Appeal of 1850 on the hierarchy | filled | `wiseman_appeal-to-the-english-people-catholic-hierarchy_1850.txt` (1850); 14,721 words; eng | catholic-church-long-nineteenth-century, tradition |
| era 9 row 278, Nicholas Wiseman: a Life told by another (vol. 1) | filled | `ward-wilfrid_life-and-times-of-cardinal-wiseman-v1_1897.txt` (1897); 193,407 words; eng | catholic-church-long-nineteenth-century, context |
| era 9 row 328, W. T. Stead: his narrative of the Welsh revival | filled | `stead_welsh-revival-narrative-of-facts_boston1905.txt` (1905); 27,087 words; eng | the-1904-07-revival-family-wales-mukti-india-pyo, context |
| era 9 row 269, Adolphe Monod: the deathbed addresses, in French | filled | `monod_adieux-a-ses-amis-et-a-l-eglise-fra_1857.txt` (1857); 46,097 words; fra | the-reveil-and-inner-mission-awakening, tradition |
| era 9 row 269, Adolphe Monod: the deathbed addresses, in English | filled | `monod_parting-words-to-his-friends-and-the-church_1873.txt` (1873); 51,965 words; eng | the-reveil-and-inner-mission-awakening, tradition |
| era 9 row 270, Guillaume Groen van Prinsterer: Ongeloof en Revolutie, in Dutch | filled | `groen-van-prinsterer_ongeloof-en-revolutie-nld_2e-uitg1868.txt` (1868); 148,185 words; nld | dutch-neo-calvinism-secession-churches, the-reveil-and-inner-mission-awakening, tradition |
| era 9 row 276, Wilhelm Loehe: Three Books concerning the Church, in English | filled | `loehe_three-books-concerning-the-church_horn1908.txt` (1908); 47,484 words; eng | confessional-lutheran-revival-emigrations, tradition |
| era 9 row 277, Bernadette Soubirous: Lasserre, Notre-Dame de Lourdes, in French | filled | `lasserre_notre-dame-de-lourdes-fra_28e-ed1870.txt` (1870); 127,531 words; fra | catholic-church-long-nineteenth-century, context |
| era 9 row 277, Bernadette Soubirous: Lasserre, Our Lady of Lourdes, in English | filled | `lasserre_our-lady-of-lourdes_1870.txt` (1870); 136,577 words; eng | catholic-church-long-nineteenth-century, context |
| era 9 row 323, J. Taylor Hamilton: his history of the Moravian Church | filled | `hamilton-j-taylor_history-of-the-moravian-church_1900.txt` (1900); 245,775 words; eng | moravian-church-after-1815, tradition |
| era 9 row 223, Theodor Fliedner: an English account of Kaiserswerth by a lady | filled | `kaiserswerth_kaiserswerth-deaconesses-by-a-lady_1857.txt` (1857); 15,148 words; eng | the-reveil-and-inner-mission-awakening, context |
| era 9 row 230, Daniel Coker: Payne's history of his church, which tells of Coker (Coker's own Dialogue and Journal were not found in print) | filled | `payne_history-of-the-african-methodist-episcopal-church-v1_1891.txt` (1891); 226,084 words; eng | the-black-church-in-america, nineteenth-century-methodism, tradition |
| era 9 row 254, Robert Roberts: Christendom Astray | filled | `roberts-robert_christendom-astray_1883.txt` (1883); 214,643 words; eng | christadelphians, tradition |
| era 9 row 254, Robert Roberts: The Ways of Providence | filled | `roberts-robert_ways-of-providence_1881.txt` (1881); 102,609 words; eng | christadelphians, tradition |
| era 9 row 255, Mary Campbell and Margaret Macdonald: an outside history that tells of 1830 (vol. 1) | filled | `miller-edward_history-and-doctrines-of-irvingism-v1_1878.txt` (1878); 131,733 words; eng | catholic-apostolic-church-irvingites, context |
| era 9 row 255, Mary Campbell and Margaret Macdonald: the Life of Mary Campbell's minister | filled | `story_memoir-of-the-life-of-the-rev-robert-story_1862.txt` (1862); 136,333 words; eng | catholic-apostolic-church-irvingites, context |
| era 9 row 260, J. G. Bellett: one of his own books (his memoir of the early circle was not found) | filled | `bellett_short-meditation-on-the-moral-glory-of-the-lord-jesus-christ_1865.txt` (1865); 24,349 words; eng | plymouth-brethren-and-dispensational-formation, tradition |

### Rows left unfilled or part-filled

| want | state | what was looked for |
|---|---|---|
| era 9 row 230, Daniel Coker: his Dialogue (1810) and Journal (1820) | part-filled | No original printing found. Payne's History (above) tells of him. Two typescripts of 1900 are on archive.org (`msam.-282-11`, `msam.-282-12`): cite only. |
| era 9 row 249, Hiram Edson: his account of the morning after | part-filled | Not found in print before 1931. His discourse of 1849 is held (above). |
| era 9 row 253, Emmeline B. Wells: the Woman's Exponent and a told life | not-found | No bound volume; partial sets of issues only. No Life found. |
| era 9 row 258, Tirzah Miller: her diaries | not-found | First printed in 2000. |
| era 9 row 327, "Awstin": the Western Mail revival pamphlets | not-found | Nineteen queries, nothing. |
| era 9 row 268, Priscilla Lydia Sellon: her own writing, a Life | part-filled | Nothing of her own found. Two pamphlets of 1852 by others are held (above). |
| era 9 row 260, J. G. Bellett: his memoir of the early circle | part-filled | Not found. One of his own books is held (above). |
| era 9 row 255, Mary Campbell and Margaret Macdonald: Norton's Memoirs (1840) | part-filled | Not found. Miller's history and Story's Memoir are held (above). |
| era 9 row 254, Robert Roberts: his magazine and a Life | part-filled | Not found. Two of his own books are held (above). |
| era 9 row 241, William Bullein Johnson: the Proceedings of 1845 | part-filled | Not found. His own book of 1846 is held (above). |
| era 9 row 242, John Clifford: the Baptist Union's record of 1887-88 | part-filled | Not found. Marchant's Life is held (above). |
| era 9 row 240, J. R. Graves: a Life | part-filled | Hailey (1929) not found. Old Landmarkism is held (above). |
| era 9 row 236, Robert P. Wilder: his own account | part-filled | His history of 1935 not found. The convention report of 1891, with his addresses, is held (above). |
| era 9 row 276, Wilhelm Lohe: his writings in German | part-filled | Drei Bucher von der Kirche not found in German; the Neuendettelsau history of 1907 has OCR that cannot be read. The English Three Books is held (above). |
| era 9 row 277, Bernadette Soubirous: her own depositions | part-filled | Not found. Lasserre in French and English is held (above). |
| era 9 row 270, Groen van Prinsterer: an English print | not-found | None before 1931. The Dutch is held (above). |

### Shelf notes

- Lives and histories written by others are `context`; a person's or a church's own text is `tradition`, with
  any doubt in the row's note. Nothing in this batch is left at `needs-ruling`.
- Dialogues on Prophecy (1828) is `antecedent` on the Catholic Apostolic Church, whose entry opens in 1832. The
  volume names no author, no speaker and no place.
- Payne's History (1891), Rush's Short Account (1843) and Hamilton's History (1900) are each a church's history
  written by one of its own bishops or superintendents inside the entry's window: `tradition`.
- Cartwright's Autobiography (1856) is `tradition` on the Second Great Awakening, whose window closes in 1840,
  and on Nineteenth-Century Methodism. Sarah Clarke's account (1914) is `tradition` on the Rescue Mission
  Movement. Marchant's Life of Clifford (1924) is `context`.
- Hamilton's History opens the shelf `moravian-church-after-1815`, and the convention report opens
  `the-student-volunteer-movement-and-edinburgh-191`.
- No census gap was met: every row has an entry.

### Cautions for profile writers (batch 2b)

- **No year on the title page.** Both books of Hannah Whitall Smith, the Life of Inskip, Coffin,
  Sarah Clarke and Stead are dated from a copyright notice. Tiffany's Dix (the scan has no title page at all),
  Bates, Christendom Astray, Miller's Irvingism and Marchant's Clifford are dated from a preface or a
  'First published' line, with the catalogue. The Student
  Volunteer report is dated from the year in its title. Each header says so.
- **Author not named, or named by initials.** Readings upon the Liturgy names no author (the host names
  Cardale). Dialogues on Prophecy names none. Bellett's book is by "J. G. B." The Unselfishness of God is by
  "H. W. S. (Mrs. Pearsall Smith)". The Kaiserswerth account is "by a Lady". The author's name on Story's Memoir
  cannot be read in the OCR. Both translations (Monod, Lasserre) name no translator.
- **Not the person's own words.** Row 230: Payne tells of Coker; nothing of Coker's is held. Row 238: Rush's
  account is the source for Varick. Row 255: Miller is a hostile outside history, and Story's Memoir does not
  name Margaret Macdonald (it tells of the M'Donald family and leaves the sister's name blank). Row 268: both
  pamphlets are by Sellon's critics; the bishop's letter quotes her in part. Row 277: Lasserre, not Bernadette.
  Row 236: a convention report with many speakers; Wilder's addresses are located in the shelf row.
- **Later editions.** The Christian's Secret (revised and enlarged, copyright 1888, not the text of 1875);
  Newton's Thoughts on the Apocalypse (second, 1853); Maurice's Theological Essays (second, 1853); Ongeloof en
  Revolutie (second, 1868); Lasserre in French (twenty-eighth, 1870); Monod in French (1857; the English of 1873
  says it follows the fifth Paris edition); Taylor's Story of My Life (title page 1895, with matter of June
  1896); In His Steps (1897); Cartwright (1857, 'eleventh thousand', copyright 1856); Wiseman's Appeal (a
  later impression under the 1850 title page).
- **Part of a larger work.** Vol. 1 only: Bunting, Hodder's Shaftesbury, Ashwell's Wilberforce, the Life of
  Maurice, Ward's Wiseman, Cabot's Emerson, Drummond's Speeches, Dialogues on Prophecy, Snow's Poems, Payne,
  Miller. Froude's Remains is part 1, vol. 1. Colenso's Pentateuch is part I.
- **Mixed voices.** Hallowell prints the Motts' letters inside her own narrative. The Life of Maurice is told
  in his letters, edited by his son. Sarah Clarke's book prints converts' own accounts after hers. Colenso's
  Ten Weeks prints others' letters and subscription lists at the end. The bishop's Letter to Miss Sellon has an
  appendix of two other clergymen's letters. Stead's pamphlet holds a second piece by G. Campbell Morgan. The
  Lambeth volume holds three conferences; the 1867 documents are located in the shelf row. Drummond's Speeches
  open with a sketch of his political career by the editor.
- **Text faults.** Elaw's Memoirs: rough OCR, and the file breaks off in mid-sentence at its end. Rush: the
  contents list a sketch of the author's life that the scan does not hold. Coffin: the first contents page is
  absent. Lasserre in French: the first page of the papal brief is missing from the OCR. Stead: a note and a
  page are printed twice. Tiffany: no title page. Emma Smith's hymnbook is a microfilm copy with fair OCR.
- **Dialogues on Prophecy:** its own preface says the printed dialogues use made-up names and differ from the
  real conversations. It does not name Albury or Drummond.
## Era 10 (1906 to about 2010), batch 2, filled (2026-11-15): Africa, Oceania, the Orthodox and Oriental churches in their own languages

Source: the rows batch 1 left open in `Build/Ministry/Operations/Audits/2026-11-12_wanted-sources-combined/Wanted_Sources.md` (era 10
rows 331-459 and council row 37), worked by region as batch 1's handover proposed. Rights: as batch 1 (R1 to R12). The search
record, the calls, the shelf rows settled and the cautions for writers are in
`Build/Ministry/Operations/Audits/2026-11-15_library-era10-b2/Search_Log.md`; the list of items for Mark to fetch by hand is
`Hand_Fetch_List.md` beside it.

71 files, 4,273,101 words: 32 in English and 39 in other languages. Russian (28: the Paris journal Путь, numbers 1 to 25, and
three books), French (2), Zulu (2), Malayalam (2), Māori (1), Arabic (1), Armenian (1), German (1) and Greek (1).

Most of what was found for the African and Assyrian rows is an outside witness, and the table says so row by row. No first-hand
print of William Wadé Harris, Kimbangu, Kivebulaya, Rātana or Surma was found.

| want | state | file | imprint or rights basis | words | language | license |
|---|---|---|---|---:|---|---|
| Wanted Sources (2026-11-12), era 10 rows 356 (William Wadé Harris), 358 (Simon Kimbangu) and 398 (Apolo Kivebulaya): an outside account printed in their lifetimes. | filled | `gollock_sons-of-africa_1928.txt` | pd-us-by-date: printed 1928; the title page prints no year; the date used is the copyright notice, "Copyright, 1928" | 50,959 | eng | Public Domain |
| Wanted Sources (2026-11-12), era 10 row 358 (Simon Kimbangu): an outside witness printed by 1930. | filled | `international-review-of-missions_v11_1922.txt` | pd-us-by-date: printed 1922; the year on the volume title leaf | 252,403 | eng | Public Domain |
| Wanted Sources (2026-11-12), era 10 row 356 (William Wadé Harris): an outside witness printed by 1930. | filled | `international-review-of-missions_v12_1923.txt` | pd-us-by-date: printed 1923; the year on the volume title leaf | 240,925 | eng | Public Domain |
| Wanted Sources (2026-11-12), era 10 row 356 (William Wadé Harris): an outside witness printed by 1930. | filled | `international-review-of-missions_v17_1928.txt` | pd-us-by-date: printed 1928; the year on the volume title leaf | 282,488 | eng | Public Domain |
| Wanted Sources (2026-11-12), era 10 row 356: William Wadé Harris, an outside witness printed by 1930. | filled | `marty_etudes-sur-l-islam-en-cote-d-ivoire-fra_1922.txt` | pd-us-by-date: printed 1922; the title-page year | 143,380 | fra | Public Domain |
| Wanted Sources (2026-11-12), era 10 row 356 (a passing notice of William Wadé Harris); the conference's own resolutions on Africa. | filled | `smith_christian-mission-in-africa-le-zoute-1926_1926.txt` | pd-us-by-date: printed 1926; the title-page year | 82,173 | eng | Public Domain |
| Wanted Sources (2026-11-12), era 10 row 398: Apolo Kivebulaya, an outside witness printed in his lifetime. | filled | `tucker_eighteen-years-in-uganda-and-east-africa-v2_1908.txt` | pd-us-by-date: printed 1908; the title-page year | 125,327 | eng | Public Domain |
| Era 10, Africa: a church's own hymnal in an African language, printed by 1930. | filled | `american-zulu-mission_amagama-okuhlabelela-zul_1911.txt` | pd-us-by-date: printed 1911; the title page prints no year; the date used is the copyright notice, "Copyright 1911", with "Published March 10, 1911" beside it | 117,605 | zul | Public Domain |
| Era 10, Africa: an African writer's own book from the Lovedale mission press, printed by 1930. | filled | `jabavu_black-problem-2e_1921.txt` | pd-us-by-date: printed 1921; the title page prints no year; the date used is the dated foreword, "12th December 1920", with which the library catalog date (1920) agrees; the author's preface to this second edition is dated January 1921 | 54,706 | eng | Public Domain |
| Era 10, Africa: a church's own print in an African language, by 1930. | filled | `wanger_imfundiso-yebandhla-elikatolike-zul_1912.txt` | pd-us-by-date: printed 1912; the title-page year; a bishop's leaf dated 29 April 1915 is bound with it | 146,134 | zul | Public Domain |
| Wanted Sources (2026-11-12), era 10 row 350: T. W. Rātana, an outside witness printed by 1930. | filled | `te-karere_v24-mri_1930.txt` | pd-us-by-date: printed 1930; the masthead dates of the numbers in the file, all of 1930 ("21 o Mei 1930" read on the page image); the host record gives the series date 1907 | 56,695 | mri | Public Domain |
| Wanted Sources (2026-11-12), era 10, the Sayfo entry: a churchman's own account printed by 1930 (it does not serve row 448: Surma is not named). | filled | `naayem_shall-this-nation-die_1921.txt` | pd-us-by-date: printed 1921; the title page prints no year; the date used is the copyright notice, "Copyright, 1921" | 65,893 | eng | Public Domain |
| Wanted Sources (2026-11-12), era 10 row 448: Surma Khanim, an outside witness printed in 1920. | filled | `austin_baqubah-refugee-camp_1920.txt` | pd-us-by-date: printed 1920; the title-page year | 28,911 | eng | Public Domain |
| Wanted Sources (2026-11-12), era 10 row 448 and the Sayfo entry: an outside witness printed in 1920. | filled | `wigram_our-smallest-ally_1920.txt` | pd-us-by-date: printed 1920; the title-page year, read on the page image | 16,060 | eng | Public Domain |
| Era 10, Egypt: a Coptic press writer's own book printed by 1930, with the Patriarch's encyclical of 1911 in English (the rows for Habib Girgis, 369, stay unfilled). | filled | `mikhail_copts-and-moslems-under-british-control_1911.txt` | pd-us-by-date: printed 1911; the title-page year | 38,028 | eng | Public Domain |
| Era 10, Egypt: a history of the Coptic Church in Arabic by a writer the host record styles القمص, printed by 1930. | filled | `manassa-yuhanna_tarikh-al-kanisa-al-qibtiyya-ara_1924.txt` | pd-us-by-date: printed 1924; the title-page year, read on the page image ("الطبعة الأولى سنة ١٩٢٤ م"); the OCR misreads the last digit | 214,010 | ara | Public Domain |
| Era 10, the Armenian church: a catholicos's own works in Armenian, printed by 1930; the rows for Balakian (375) and Khoren I (447) stay unfilled. | filled | `khrimian_amboghjakan-yerker-hye_1929.txt` | pd-us-by-date: printed 1929; the title-page year | 268,990 | hye | Public Domain |
| Era 10, the Armenian church: the church's own liturgy in an English made by its priests, printed by 1930. | filled | `armenian-church_divine-liturgy_1908.txt` | pd-us-by-date: printed 1908; the title-page year, read on the page image ("MCMVIII"; the verso reads "First Published in 1908") | 19,858 | eng | Public Domain |
| Wanted Sources (2026-11-12), era 10 row 440 (located by batch 1, now checked): it does not carry the events of 1912. | filled | `panjikaran_syrian-church-in-malabar_1912.txt` | pd-us-by-date: printed 1912; the title-page year | 21,642 | eng | Public Domain |
| Wanted Sources (2026-11-12), era 10 row 440 and the Mar Thoma entry: a Malayalam church monthly from before the division of 1912. | filled | `malankara-sabha-tharaka_v6-no12-mal_1910.txt` | pd-us-by-date: printed 1910; the year in the imprint on the cover, read on the page image | 10,675 | mal | Public Domain |
| Wanted Sources (2026-11-12), era 10 row 440 and the Malankara entry: a Malayalam church monthly of the 1920s. | filled | `catholic-sabha_v2-nos5-6-mal_1922.txt` | pd-us-by-date: printed 1922; the year printed on the calendar leaf after the cover, read on the page image ("1922" and the Malayalam-era year "1098") | 14,239 | mal | Public Domain |
| Wanted Sources (2026-11-12), era 10 rows 371 (Sergei Bulgakov) and 372 (Georges Florovsky): their own articles in the Paris school's journal; the debate on Metropolitan Sergius (row 377). | filled | `put_n01-rus_1925.txt` | pd-us-by-date: printed 1925; the masthead date | 79,630 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10 rows 371 (Sergei Bulgakov) and 372 (Georges Florovsky): their own articles in the Paris school's journal; the debate on Metropolitan Sergius (row 377). | filled | `put_n02-rus_1926.txt` | pd-us-by-date: printed 1926; the masthead date ("№ 2. Январь 192[6]": the OCR garbles the last digit; number 1 is dated September 1925 and number 3 is dated 1926) | 64,394 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10 rows 371 (Sergei Bulgakov) and 372 (Georges Florovsky): their own articles in the Paris school's journal; the debate on Metropolitan Sergius (row 377). | filled | `put_n03-rus_1926.txt` | pd-us-by-date: printed 1926; the masthead date | 62,694 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10 rows 371 (Sergei Bulgakov) and 372 (Georges Florovsky): their own articles in the Paris school's journal; the debate on Metropolitan Sergius (row 377). | filled | `put_n04-rus_1926.txt` | pd-us-by-date: printed 1926; the masthead date | 87,349 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10 rows 371 (Sergei Bulgakov) and 372 (Georges Florovsky): their own articles in the Paris school's journal; the debate on Metropolitan Sergius (row 377). | filled | `put_n05-rus_1926.txt` | pd-us-by-date: printed 1926; the masthead date | 49,136 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10 rows 371 (Sergei Bulgakov) and 372 (Georges Florovsky): their own articles in the Paris school's journal; the debate on Metropolitan Sergius (row 377). | filled | `put_n06-rus_1927.txt` | pd-us-by-date: printed 1927; the masthead date | 58,452 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10 rows 371 (Sergei Bulgakov) and 372 (Georges Florovsky): their own articles in the Paris school's journal; the debate on Metropolitan Sergius (row 377). | filled | `put_n07-rus_1927.txt` | pd-us-by-date: printed 1927; the masthead date | 58,544 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10 rows 371 (Sergei Bulgakov) and 372 (Georges Florovsky): their own articles in the Paris school's journal; the debate on Metropolitan Sergius (row 377). | filled | `put_n08-rus_1927.txt` | pd-us-by-date: printed 1927; the masthead date | 75,488 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10 rows 371 (Sergei Bulgakov) and 372 (Georges Florovsky): their own articles in the Paris school's journal; the debate on Metropolitan Sergius (row 377). | filled | `put_n09-rus_1928.txt` | pd-us-by-date: printed 1928; the masthead date | 43,565 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10 rows 371 (Sergei Bulgakov) and 372 (Georges Florovsky): their own articles in the Paris school's journal; the debate on Metropolitan Sergius (row 377). | filled | `put_n10-rus_1928.txt` | pd-us-by-date: printed 1928; the masthead date | 34,672 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10 rows 371 (Sergei Bulgakov) and 372 (Georges Florovsky): their own articles in the Paris school's journal; the debate on Metropolitan Sergius (row 377). | filled | `put_n11-rus_1928.txt` | pd-us-by-date: printed 1928; the masthead date | 37,011 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10 rows 371 (Sergei Bulgakov) and 372 (Georges Florovsky): their own articles in the Paris school's journal; the debate on Metropolitan Sergius (row 377). | filled | `put_n12-rus_1928.txt` | pd-us-by-date: printed 1928; the masthead date | 34,731 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10 rows 371 (Sergei Bulgakov) and 372 (Georges Florovsky): their own articles in the Paris school's journal; the debate on Metropolitan Sergius (row 377). | filled | `put_n13-rus_1928.txt` | pd-us-by-date: printed 1928; the masthead date | 30,408 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10 rows 371 (Sergei Bulgakov) and 372 (Georges Florovsky): their own articles in the Paris school's journal; the debate on Metropolitan Sergius (row 377). | filled | `put_n14-rus_1928.txt` | pd-us-by-date: printed 1928; the masthead date ("№ 14. Декабрь 1928") | 32,732 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10 rows 371 (Sergei Bulgakov) and 372 (Georges Florovsky): their own articles in the Paris school's journal; the debate on Metropolitan Sergius (row 377). | filled | `put_n15-rus_1929.txt` | pd-us-by-date: printed 1929; the masthead date | 37,120 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10 rows 371 (Sergei Bulgakov) and 372 (Georges Florovsky): their own articles in the Paris school's journal; the debate on Metropolitan Sergius (row 377). | filled | `put_n16-rus_1929.txt` | pd-us-by-date: printed 1929; the masthead date | 28,295 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10 rows 371 (Sergei Bulgakov) and 372 (Georges Florovsky): their own articles in the Paris school's journal; the debate on Metropolitan Sergius (row 377). | filled | `put_n17-rus_1929.txt` | pd-us-by-date: printed 1929; the OCR misreads the masthead year as "1939"; numbers 16 and 18 are both dated 1929, and a piece in this number is dated "23. III. 1929" | 30,931 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10 rows 371 (Sergei Bulgakov) and 372 (Georges Florovsky): their own articles in the Paris school's journal; the debate on Metropolitan Sergius (row 377). | filled | `put_n18-rus_1929.txt` | pd-us-by-date: printed 1929; the masthead date | 34,339 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10 rows 371 (Sergei Bulgakov) and 372 (Georges Florovsky): their own articles in the Paris school's journal; the debate on Metropolitan Sergius (row 377). | filled | `put_n19-rus_1929.txt` | pd-us-by-date: printed 1929; the masthead date | 34,490 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10 rows 371 (Sergei Bulgakov) and 372 (Georges Florovsky): their own articles in the Paris school's journal; the debate on Metropolitan Sergius (row 377). | filled | `put_n20-rus_1930.txt` | pd-us-by-date: printed 1930; the masthead date | 34,023 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10 rows 371 (Sergei Bulgakov) and 372 (Georges Florovsky): their own articles in the Paris school's journal; the debate on Metropolitan Sergius (row 377). | filled | `put_n21-rus_1930.txt` | pd-us-by-date: printed 1930; the masthead date | 40,253 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10 rows 371 (Sergei Bulgakov) and 372 (Georges Florovsky): their own articles in the Paris school's journal; the debate on Metropolitan Sergius (row 377). | filled | `put_n22-rus_1930.txt` | pd-us-by-date: printed 1930; the masthead date | 40,498 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10 rows 371 (Sergei Bulgakov) and 372 (Georges Florovsky): their own articles in the Paris school's journal; the debate on Metropolitan Sergius (row 377). | filled | `put_n23-rus_1930.txt` | pd-us-by-date: printed 1930; the masthead date | 36,224 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10 rows 371 (Sergei Bulgakov) and 372 (Georges Florovsky): their own articles in the Paris school's journal; the debate on Metropolitan Sergius (row 377). | filled | `put_n24-rus_1930.txt` | pd-us-by-date: printed 1930; the masthead date | 34,112 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10 rows 371 (Sergei Bulgakov) and 372 (Georges Florovsky): their own articles in the Paris school's journal; the debate on Metropolitan Sergius (row 377). | filled | `put_n25-rus_1930.txt` | pd-us-by-date: printed 1930; the masthead date | 36,029 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10: Orthodox documents of 1920-1930 in a contemporary English print (rows 370, 376, 377, 441 and the Greek Church entry). | filled | `christian-east_v1-no3-september-1920.txt` | pd-us-by-date: printed 1920; the cover date | 28,462 | eng | Public Domain |
| Wanted Sources (2026-11-12), era 10: Orthodox documents of 1920-1930 in a contemporary English print (rows 370, 376, 377, 441 and the Greek Church entry). | filled | `christian-east_v2-no2-july-1921.txt` | pd-us-by-date: printed 1921; the cover date | 23,829 | eng | Public Domain |
| Wanted Sources (2026-11-12), era 10: Orthodox documents of 1920-1930 in a contemporary English print (rows 370, 376, 377, 441 and the Greek Church entry). | filled | `christian-east_v3-no2-july-1922.txt` | pd-us-by-date: printed 1922; the cover date | 23,709 | eng | Public Domain |
| Wanted Sources (2026-11-12), era 10: Orthodox documents of 1920-1930 in a contemporary English print (rows 370, 376, 377, 441 and the Greek Church entry). | filled | `christian-east_v3-no3-october-1922.txt` | pd-us-by-date: printed 1922; the cover date | 25,508 | eng | Public Domain |
| Wanted Sources (2026-11-12), era 10: Orthodox documents of 1920-1930 in a contemporary English print (rows 370, 376, 377, 441 and the Greek Church entry). | filled | `christian-east_v4-no1-march-1923.txt` | pd-us-by-date: printed 1923; the cover date | 27,274 | eng | Public Domain |
| Wanted Sources (2026-11-12), era 10: Orthodox documents of 1920-1930 in a contemporary English print (rows 370, 376, 377, 441 and the Greek Church entry). | filled | `christian-east_v4-no2-may-1923.txt` | pd-us-by-date: printed 1923; the cover date | 36,142 | eng | Public Domain |
| Wanted Sources (2026-11-12), era 10: Orthodox documents of 1920-1930 in a contemporary English print (rows 370, 376, 377, 441 and the Greek Church entry). | filled | `christian-east_v4-no3-august-1923.txt` | pd-us-by-date: printed 1923; the cover date | 28,975 | eng | Public Domain |
| Wanted Sources (2026-11-12), era 10: Orthodox documents of 1920-1930 in a contemporary English print (rows 370, 376, 377, 441 and the Greek Church entry). | filled | `christian-east_v4-no4-november-1923.txt` | pd-us-by-date: printed 1923; the cover date | 18,970 | eng | Public Domain |
| Wanted Sources (2026-11-12), era 10: Orthodox documents of 1920-1930 in a contemporary English print (rows 370, 376, 377, 441 and the Greek Church entry). | filled | `christian-east_v8-no4-winter-1927.txt` | pd-us-by-date: printed 1927; the cover date | 22,873 | eng | Public Domain |
| Wanted Sources (2026-11-12), era 10: Orthodox documents of 1920-1930 in a contemporary English print (rows 370, 376, 377, 441 and the Greek Church entry). | filled | `christian-east_v10-no1-spring-1929.txt` | pd-us-by-date: printed 1929; the cover date | 24,626 | eng | Public Domain |
| Wanted Sources (2026-11-12), era 10: Orthodox documents of 1920-1930 in a contemporary English print (rows 370, 376, 377, 441 and the Greek Church entry). | filled | `christian-east_v11-no1-spring-1930.txt` | pd-us-by-date: printed 1930; the cover date | 23,275 | eng | Public Domain |
| Wanted Sources (2026-11-12), era 10: Orthodox documents of 1920-1930 in a contemporary English print (rows 370, 376, 377, 441 and the Greek Church entry). | filled | `christian-east_v11-no2-summer-1930.txt` | pd-us-by-date: printed 1930; the cover date | 22,199 | eng | Public Domain |
| Wanted Sources (2026-11-12), era 10 row 376: Patriarch Tikhon, his own words in Russian in a print of his lifetime. | filled | `nikolaevskii-sobor_ko-dniu-dvadtsatipiatiletiia-patriarkha-tikhona-rus_1922.txt` | pd-us-by-date: printed 1922; the title-page year | 12,952 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10 row 376 and council row 37: Patriarch Tikhon's epistle of January 1918 in Russian, in a print of 1923; the renovationist side. | filled | `vvedensky_tserkov-i-gosudarstvo-rus_1923.txt` | pd-us-by-date: printed 1923; the title-page year, read on the page image | 75,691 | rus | Public Domain |
| Wanted Sources (2026-11-12), era 10 row 376: Patriarch Tikhon, his epistle of February 1922 in Russian; the New Martyrs entry. | filled | `valentinov_chernaia-kniga-rus_1925.txt` | pd-us-by-date: printed 1925; the title-page year | 94,550 | rus | Public Domain |
| Era 10, the Balkan Orthodox entry: an Orthodox theologian's own account of his church, printed by 1930 (the rows for Kiril, 445, stay unfilled). | filled | `zankov_eastern-orthodox-church_lowrie1929.txt` | pd-us-by-date: printed 1929; the title-page year, read on the page image; the OCR misreads it as 1939 | 38,678 | eng | Public Domain |
| Era 10, the Balkan Orthodox entry: an Orthodox theologian's own account of his church in the language he gave it in, printed by 1930. | filled | `zankov_orthodoxe-christentum-des-ostens-deu_1928.txt` | pd-us-by-date: printed 1928; the title-page year | 55,349 | deu | Public Domain |
| Wanted Sources (2026-11-12), era 10, the Balkan Orthodox entry (row 444, Dimitrije, stays unfilled): a Serbian churchman's own words printed by 1930. | filled | `velimirovic_soul-of-serbia_1916.txt` | pd-us-by-date: printed 1916; the title-page year | 22,969 | eng | Public Domain |
| Wanted Sources (2026-11-12), era 10, the Balkan Orthodox entry (row 444, Dimitrije, stays unfilled): a Serbian churchman's own words printed by 1930. | filled | `velimirovic_agony-of-the-church_1917.txt` | pd-us-by-date: printed 1917; the title-page year | 19,756 | eng | Public Domain |
| Wanted Sources (2026-11-12), era 10, the Balkan Orthodox entry (row 444, Dimitrije, stays unfilled): a Serbian churchman's own words printed by 1930. | filled | `velimirovic_religion-and-nationality-in-serbia_1915.txt` | pd-us-by-date: printed 1915; no year is legible on the title page in the OCR; the date used is the dated prefatory note, "June 15, 1915", with which the library catalog date agrees | 5,415 | eng | Public Domain |
| Wanted Sources (2026-11-12), era 10, the Balkan Orthodox entry (row 444, Dimitrije, stays unfilled): a Serbian churchman's own words printed by 1930. | filled | `velimirovic_serbia-in-light-and-darkness_1916.txt` | pd-us-by-date: printed 1916; the title-page year, read on the page image | 30,156 | eng | Public Domain |
| Wanted Sources (2026-11-12), era 10, the Balkan Orthodox entry (row 444, Dimitrije, stays unfilled): a Serbian churchman's own words printed by 1930. | filled | `velimirovic_christianity-and-war_1915.txt` | pd-us-by-date: printed 1915; the year on the printed cover, read on the page image; the pamphlet has no separate title page | 9,208 | eng | Public Domain |
| Era 10, the Greek Church and the Ecumenical Patriarchate entry: the Patriarchate's own print in Greek, 1920 (the encyclical of 1920 in Greek was not found). | filled | `ecumenical-patriarchate_mavri-vivlos-ell_1920.txt` | pd-us-by-date: printed 1920; the title-page year, read on the page image | 37,978 | ell | Public Domain |
| Wanted Sources (2026-11-12), era 10: the encyclical of the Ecumenical Patriarchate of January 1920 (not found by batch 1), in the English of 1924. | filled | `bell_documents-on-christian-unity-1920-24_1924.txt` | pd-us-by-date: printed 1924; the title-page year | 119,836 | eng | Public Domain |
| Wanted Sources (2026-11-12), era 10 row 416: Alfred Loisy, L'Évangile et l'Église in French (the first edition of 1902 is still wanted). | filled | `loisy_evangile-et-l-eglise-3e-ed-fra_1904.txt` | pd-us-by-date: printed 1904; the title-page year, read on the page image | 58,500 | fra | Public Domain |

### Era 10, batch 2: wanted rows not filled

| want (row) | result | where it stands |
|---|---|---|
| William Wadé Harris, his own teaching (356); Kimbangu, the trial record and his church's prints (358); Kivebulaya's diary (398) | outside witnesses only | Held now: missionary and colonial accounts of 1908-1928 (see the table). Not found: Casely Hayford's William Waddy Harris (1915), Lloyd's Apolo of the Pygmy Forest (1923), Walker's Story of the Ivory Coast (1926), any Belgian print on the trial of 1921. On the hand-fetch list. |
| Orimolade (357); Babalola (380); Lekganyane (381); Spartas (392); the other African-Initiated Churches and Revival people | not found | Nothing printed by 1930 on archive.org. The hymn book of the National Church of Nigeria and the Cameroons (`hymnsprayersforu00abaniala`) prints no year and was not taken. The Dictionary of African Christian Biography stays cite and link (R3). |
| T. W. Rātana, Te Whetu Marama (350) | an outside witness only; refused host | Te Karere for 1930 is held (another church's paper). Te Whetu Marama is reported to be on Papers Past, which was not opened: on the hand-fetch list. Two Māori tracts by Wiremu Takana (`hekupuwhakamaram00gard`, `hekupuwhaiwhakaa00kara`) print no year and were not taken. |
| Māori and Pacific church prints of 1896-1918 (batch 1: located, unchecked) | held for Mark | The Auckland Sunday School Union's Māori hymnal of 1916 (`hehimenemotekara00unse`), a Māori tract of 1897 and a Tongan hymnal of 1912 carry a host field claiming copyright for Intellectual Reserve, Inc. Not taken. Latter-day Saint hymnals in Tahitian (1921) and Hawaiian (1907) are free of that field but serve no wanted row. |
| The Catholic Worker, more scans of the printed paper (364) | not found | No other issue of the New York paper is on archive.org; the three "Catholic Worker" pamphlets there (two of them of 1947) are the Melbourne paper's. |
| The Moscow council of 1917-18, its Acts and Definitions (council row 37; 376) | located, reprints only | Every scan on archive.org is a reprint of 1994 or later. The print of 1918 is on the hand-fetch list (rusneb.ru, the Russian State Library). Tikhon's epistle of January 1918 is now held in Russian inside Vvedensky (1923). |
| Metropolitan Sergius, the declaration of 1927 in Russian (377); Joseph of Petrograd (442) | part filled | The letter of 16/29 July 1927 is now held in the English of The Christian East (winter 1927), printed "in full"; Путь numbers 9, 10 and 11 argue about it from both sides. No Russian print of the text and no full rejection of it was found. |
| Sergei Bulgakov, Svet nevechernii; the Sophia file (371) | part filled | His articles in Путь to 1930 are held. Свет невечерний and the books of 1927-1929 were not found; the controversy of 1935-37 is after 1930. |
| Vladimir Lossky (373) | not found | No piece of his is in Путь to 1930; every "Лосскій" there is N. O. Lossky. |
| Kyrion II (370); Ambrosi Khelaia (441) | part filled | The Christian East prints Ambrose's Genoa memorandum in English (May 1923; the scan lacks its last page) and outside articles on Kyrion II. Nothing of Kyrion's own was found. |
| The encyclical of January 1920 in Greek; the Pan-Orthodox acts of 1923 in Greek | not found | Both are held in English (Bell 1924; The Christian East, November 1923). Ἐκκλησιαστικὴ Ἀλήθεια was not found. |
| Cristea (443); Dimitrije (444); Kiril (445); Trifa (374) | not found | Serbian, Bulgarian and Romanian church journals are not on archive.org. Velimirović's English books of 1915-1917 and Zankov's book are held. |
| Grigoris Balakian, Armenian Golgotha, 1922 (375); Khoren I (447) | not found; located | Not on archive.org. A record at the Deutsche Digitale Bibliothek (a Bavarian State Library copy) is on the hand-fetch list. The journal Էջմիածին for 1918-19 (`1918-12`) prints no Gregorian date and has unusable OCR. |
| Habib Girgis (369); Kyrillos VI (437) | not found | `AAlexandrina-102649` is a printing of 1970 (its preface is dated April 1970). No other dated book of his and no issue of al-Karma was found. |
| Surma Khanim, Assyrian Church Customs, 1920 (448) | outside witnesses only | Austin (1920) and Wigram (1920) are held. Her own book was not found; Naayem's book does not name her. Yohannan's Death of a Nation (1917) is on archive.org with a third of its text missing and was not taken. |
| Abdul Masih II and Baselios Paulose I, 1912 (440) | part filled | Two Malayalam monthlies (1910, 1922) and Panjikaran (1912) are held; none carries the consecration of 1912. Three issues of the Malankara Edavaka Pathrika (volume 20) and one of the Suriyani Sabha print only Malayalam-era numerals and were not taken. Mizo and Khasi church prints of 1912-1930 were located and not opened. |
| Alfred Loisy, L'Évangile et l'Église, the first edition of 1902 (416) | held for Mark | The third edition (1904) is now held. A search result reports the first on Gallica, which refused a plain fetch: on the hand-fetch list, to be confirmed. |
| The Apostolic Faith; Fosdick in The Christian Work; Larkin; Bartleman; Penn-Lewis; Blair; Riley; Laws; Bonhoeffer; Barth's Römerbrief; Haywood, Ewart, McAlister; Seymour 1915 | hand-fetch list | `Hand_Fetch_List.md` gives the record and edition for each, or says that none was found. |
## Era 9 (1815-1906), batch 2a (2026-11-15): Africa, Asia, Oceania, Latin America, the Caribbean and the Eastern churches

Seventy-one files for the era 9 person rows of
`Build/Ministry/Operations/Audits/2026-11-12_wanted-sources-combined/Wanted_Sources.md` that lie outside
Britain, Europe and North America (rows 226, 246-248, 263-266, 279-322 and 324-326), with batch 1's not-found
rows tried by new routes and the date checks batch 1 left owing. The search record is
`Build/Ministry/Operations/Audits/2026-11-15_library-era9-b2a/Search_Log.md`. Twenty-six files are in the
tradition's own language: Russian (7), Spanish (5), French (4), Portuguese (3), Ukrainian (2), Dutch (2),
Greek, German and Italian (1 each). Every file rests on a printed year of 1930 or earlier; the header of each
names where the year stands. At intake Google's preamble and the lines that hold only the scanner's page mark
were removed, and each header says what was removed. In three Google scans (Jessup vol. 1, My Life in Christ,
Reyes) the OCR broke the page mark over two lines or misread it; those lines remain, and the headers say so. Rows 227-245, 249-262, 267-278, 323 and 327-330 are left for batch 2b.

Batch 1's eighteen `needs-ruling` shelf rows were decided in this batch by the shelf principle Mark ruled on 15
November; the table of batch 1 above shows the roles as they now stand. No row of this batch is left at
`needs-ruling`.

| want | state | file(s), with the imprint year | shelf |
|---|---|---|---|
| era 9 row 181, John Nelson Darby: lectures of his own | filled | `darby_seven-lectures-on-the-second-coming-of-the-lord_toronto1863.txt` (1863); 61,086 words; eng | plymouth-brethren-and-dispensational-formation, tradition |
| era 9 row 181, John Nelson Darby: lectures of his own, translated from the French | filled | `darby_studies-on-the-book-of-daniel_3rd-ed1864.txt` (1864); 40,206 words; eng | plymouth-brethren-and-dispensational-formation, tradition |
| era 9 row 181, John Nelson Darby: a book of his own, printed without his name | filled | `darby_dialogues-on-the-essays-and-reviews_2nd-ed1863.txt` (1863); 187,982 words; eng | plymouth-brethren-and-dispensational-formation, tradition |
| era 9 row 181, John Nelson Darby: a history of the Brethren by another hand | held already | `neatby_history-of-the-plymouth-brethren_1901.txt` (vendored by era 9 batch 2b); chapter IX, on Darby's supremacy, is at lines 7779-8463 | plymouth-brethren-and-dispensational-formation, context (added to that file's map row) |
| era 9 row 186, Antonio Conselheiro: an army officer's account of the war, in Portuguese | filled | `macedo-soares_a-guerra-de-canudos-por_1902.txt` (1902); 75,880 words; por | canudos-belo-monte, context |
| era 9 row 191, Catherine Booth: Aggressive Christianity | filled | `booth-catherine_aggressive-christianity_boston1883.txt` (1883); 56,711 words; eng | the-salvation-army, tradition |
| era 9 row 191, Catherine Booth: Godliness, her addresses of 1881 | filled | `booth-catherine_godliness_1883.txt` (1883); 50,227 words; eng | the-salvation-army, tradition |
| era 9 row 207, Kiai Sadrach: a Dutch missionary's account | filled | `adriaanse_sadrachs-kring-nld_1899.txt` (1899); 171,390 words; nld | indonesian-christianity, context |
| era 9 row 207, Kiai Sadrach: a Dutch mission history | filled | `coolsma_de-zendingseeuw-voor-nederlandsch-oost-indie-nld_1901.txt` (1901); 621,962 words; nld | indonesian-christianity, context |
| era 9 rows 210 and 318, Charles Lwanga and Joseph Mukasa Balikuddembe: a French account that names both | filled | `klein_le-cardinal-lavigerie-et-ses-oeuvres-d-afrique-fra_1897.txt` (1897); 105,124 words; fra | east-african-christianity-uganda-martyrs, context |
| era 9 row 213, Mangena Mokone: an entry in the African Methodist Episcopal Church's encyclopaedia | filled | `wright_centennial-encyclopaedia-of-the-african-methodist-episcopal-church_1916.txt` (1916); 300,374 words; eng | african-initiated-churches-harrist-aladura-zioni, the-black-church-in-the-twentieth-century, context |
| era 9 row 226, Herman of Alaska: the Valaam monastery's account of the Kodiak mission, with his letters | filled | `valaam_ocherk-iz-istorii-amerikanskoi-pravoslavnoi-missii-rus_1894.txt` (1894); 66,319 words; rus | alaskan-mission-herman-veniaminov, context |
| era 9 rows 246 and 248, Samuel Sharpe and Henry Bleby: Bleby's narrative | filled | `bleby_death-struggles-of-slavery_3rd-ed1868.txt` (1868); 119,414 words; eng | caribbean-churches-of-slavery-and-emancipation, tradition |
| era 9 row 247, John Smith of Demerara: a Life | filled | `wallbridge_demerara-martyr-memoirs-of-the-rev-john-smith_1848.txt` (1848); 119,293 words; eng | caribbean-churches-of-slavery-and-emancipation, context |
| era 9 row 247, John Smith of Demerara: the trial record | filled | `london-missionary-society_report-of-the-proceedings-against-the-late-rev-j-smith-of-demerara_1824.txt` (1824); 120,575 words; eng | caribbean-churches-of-slavery-and-emancipation, context |
| era 9 rows 263 to 266, the Taiping leaders and Issachar Roberts: an outside account | filled | `meadows_chinese-and-their-rebellions_1856.txt` (1856); 263,387 words; eng | taiping-heavenly-kingdom, context |
| era 9 rows 263 to 266, the Taiping leaders and Issachar Roberts: an outside account | filled | `brine_taeping-rebellion-in-china_1862.txt` (1862); 135,441 words; eng | taiping-heavenly-kingdom, context |
| era 9 rows 263 to 266, the Taiping leaders: Lindley, vol. 2 | filled | `lindley_ti-ping-tien-kwoh-v2_1866.txt` (1866); 151,958 words; eng | taiping-heavenly-kingdom, context |
| era 9 row 279, Andrey Sheptytsky: a pastoral letter on repentance | filled | `sheptytsky_o-pokaianiiu-lyst-pastyrskii-ukr_1901.txt` (1901); 11,631 words; ukr | ruthenian-greek-catholic-polotsk-to-galicia, tradition |
| era 9 row 279, Andrey Sheptytsky: his book for the Ruthenians of Canada | filled | `sheptytsky_kanadiiskym-rusynam-ukr_1911.txt` (1911); 20,317 words; ukr | ruthenian-greek-catholic-polotsk-to-galicia, tradition |
| era 9 row 280, Isabelo de los Reyes: his memorial on the revolution of 1896-97 | filled | `reyes_la-sensacional-memoria-spa_1899.txt` (1899); 45,366 words; spa | philippine-catholicism-gomburza-to-aglipay, tradition |
| era 9 row 280, Gregorio Aglipay: documents of the Iglesia Filipina Independiente | filled | `iglesia-filipina-independiente_documentos-interesantes-spa_1906.txt` (1906); 10,653 words; spa | philippine-catholicism-gomburza-to-aglipay, tradition |
| era 9 row 280, Gregorio Aglipay: the church's catechism | held already | `aglipay_catequesis-de-la-iglesia-filipina-independiente-spa_1912.txt` (vendored by the era 10 batch) | — |
| era 9 row 281, Apolinario de la Cruz: a note on the Cofradia de San Jose | filled | `blair-robertson_philippine-islands-v52_1907.txt` (1907); 109,796 words; eng | philippine-catholicism-gomburza-to-aglipay, context |
| era 9 row 282, Niijima Jo: a Life with his letters | filled | `hardy_life-and-letters-of-joseph-hardy-neesima_1891.txt` (1891); 109,790 words; eng | japanese-christianity-hidden-emergence-meiji, context |
| era 9 row 282, Niijima Jo: a sketch of his life by a colleague | filled | `davis_sketch-of-the-life-of-rev-joseph-hardy-neesima_1890.txt` (1890); 37,841 words; eng | japanese-christianity-hidden-emergence-meiji, context |
| era 9 row 283, Uchimura Kanzo: his own account | filled | `uchimura_diary-of-a-japanese-convert_1895.txt` (1895); 61,745 words; eng | japanese-christianity-hidden-emergence-meiji, tradition |
| era 9 row 284, Fabre Geffrard: a later account of the Concordat of 1860 | filled | `leger_haiti-her-history-and-her-detractors_1907.txt` (1907); 124,684 words; eng | haitian-church-rupture-to-concordat, context |
| era 9 row 284, Fabre Geffrard: the text of the Concordat of 1860, in a Vatican collection | filled | `mercati_raccolta-di-concordati-ita-fra-lat_1919.txt` (1919); 529,974 words; ita | haitian-church-rupture-to-concordat, catholic-church-long-nineteenth-century, tradition |
| era 9 row 285, Benito Juarez: the Reform laws, 1856 to 1861 | filled | `mexico_codigo-de-la-reforma-spa_1861.txt` (1861); 133,919 words; spa | nineteenth-century-latin-american-catholicism, context |
| era 9 row 286, Gabriel Garcia Moreno: his writings and speeches, vol. 1 | filled | `garcia-moreno_escritos-y-discursos-t1-spa_1887.txt` (1887); 116,857 words; spa | nineteenth-century-latin-american-catholicism, tradition |
| era 9 row 286, Gabriel Garcia Moreno: his official writings, vol. 2 | filled | `garcia-moreno_escritos-y-discursos-t2-spa_1888.txt` (1888); 110,819 words; spa | nineteenth-century-latin-american-catholicism, tradition |
| era 9 row 286, Gabriel Garcia Moreno: a Life, in English | filled | `berthe_garcia-moreno-president-of-ecuador_herbert1889.txt` (1889); 88,155 words; eng | nineteenth-century-latin-american-catholicism, context |
| era 9 row 287, Vital Maria Goncalves de Oliveira: his own defence | filled | `vital_o-bispo-de-olinda-e-os-seus-accusadores-por_1873.txt` (1873); 40,202 words; por | nineteenth-century-latin-american-catholicism, tradition |
| era 9 row 287, Antonio de Macedo Costa: his own account of the religious question | filled | `macedo-costa_a-questao-religiosa-do-brazil-perante-a-santa-se-por_1886.txt` (1886); 123,834 words; por | nineteenth-century-latin-american-catholicism, tradition |
| era 9 row 289, Minh Mang: the edict of 1833 in a mission history, in French | filled | `louvet_la-cochinchine-religieuse-v2-fra_1885.txt` (1885); 166,328 words; fra | vietnamese-catholicism-1815-1906, context |
| era 9 row 289, Minh Mang: the edict of 1833 in the Paris Mission's history, in French | held already | `launay_histoire-generale-de-la-societe-des-missions-etrangeres-t2-fra_1894.txt` (vendored by the era 8 batch); the edict of 6 January 1833 is at lines 47316-47419 | vietnamese-catholicism-1815-1906, context (a second map row on that file) |
| era 9 row 289, Minh Mang: an English history of the persecutions | filled | `shortland_persecutions-of-annam_1875.txt` (1875); 125,161 words; eng | vietnamese-catholicism-1815-1906, context |
| era 9 row 290, Peter Paul Massaad: an outside account of the Maronites, 1840 to 1860 | filled | `churchill_druzes-and-the-maronites-under-the-turkish-rule_1862.txt` (1862); 55,762 words; eng | maronite-church-1815-1906, context |
| era 9 rows 293 and 197, Macarius and Ambrose of Optina: the monastery's own history | filled | `optina_istoricheskoe-opisanie-kozelskoi-optinoi-pustyni-rus_1902.txt` (1902); 62,887 words; rus | the-optina-elders-and-russian-ascetic-renewal, tradition |
| era 9 row 294, Ivan Kireevsky: his collected works, vol. 1 | filled | `kireevsky_polnoe-sobranie-sochinenii-t1-rus_gershenzon1911.txt` (1911); 94,973 words; rus | the-optina-elders-and-russian-ascetic-renewal, tradition |
| era 9 row 295, Theophan the Recluse: his sermons to the Tambov flock | filled | `feofan_slova-k-tambovskoi-pastve-rus_1861.txt` (1861); 80,406 words; rus | the-optina-elders-and-russian-ascetic-renewal, russian-church-synodal-century, tradition |
| era 9 row 295, Theophan the Recluse: sermons on the godly life | filled | `feofan_bogougodnaia-zhizn-voobshche-rus_2nd-ed1899.txt` (1899); 26,781 words; rus | the-optina-elders-and-russian-ascetic-renewal, russian-church-synodal-century, tradition |
| era 9 row 296, Makary (Glukharev): materials for his biography | filled | `filimonov_materialy-dlia-biografii-arkhimandrita-makariia-rus_1888.txt` (1888); 73,160 words; rus | russian-church-synodal-century, context |
| era 9 row 297, John of Kronstadt: extracts from his diary, in Russian, vol. 1 | filled | `ioann-kronshtadtskii_moia-zhizn-vo-khriste-t1-rus_1891.txt` (1891); 57,652 words; rus | russian-church-synodal-century, tradition |
| era 9 row 297, John of Kronstadt: extracts from his diary, in English | filled | `ioann-kronshtadtskii_my-life-in-christ_goulaeff1897.txt` (1897); 272,797 words; eng | russian-church-synodal-century, tradition |
| era 9 row 299, Grigor Odian: the Armenian National Constitution in English, in an appendix | filled | `lynch_armenia-travels-and-studies-v2_1901.txt` (1901); 247,209 words; eng | armenian-christianity-zartonk, context |
| era 9 rows 300 and 301, Theoklitos Pharmakidis: a pamphlet against Konstantinos Oikonomos | filled | `pharmakidis_oikonomos-ho-ex-oikonomon-ell_1849.txt` (1849); 63,973 words; ell | orthodoxy-after-1821-balkan-autocephalies, tradition |
| era 9 row 302, Antim I: the firman of 1870 in German, in a dissertation | filled | `scheffler_das-bulgarische-exarchat-und-der-mazedonische-kirchenstreit-deu_1909.txt` (1909); 13,792 words; deu | orthodoxy-after-1821-balkan-autocephalies, context |
| era 9 row 303, Thomas Jones: an entry in a Welsh biographical dictionary | filled | `evans_biographical-dictionary-of-ministers-and-preachers-of-the-welsh-calvinistic-methodist-body_1907.txt` (1907); 154,508 words; eng | northeast-india-revivals-and-the-mar-thoma-refor, context |
| era 9 row 304, Edwin W. Clark: his wife's account of the Naga mission | filled | `clark_corner-in-india_1907.txt` (1907); 40,734 words; eng | northeast-india-revivals-and-the-mar-thoma-refor, tradition |
| era 9 row 304, Edwin W. Clark: the Assam Mission's jubilee papers | filled | `assam-mission_papers-and-discussions-of-the-jubilee-conference-1886_1887.txt` (1887); 103,908 words; eng | northeast-india-revivals-and-the-mar-thoma-refor, tradition |
| era 9 rows 306 and 307, Tewodros II and Abuna Salama III: a captive missionary's account | filled | `stern_captive-missionary_1868.txt` (1868); 97,522 words; eng | ethiopian-christianity-tewodros-to-menelik, context |
| era 9 rows 306 and 307, Tewodros II and Abuna Salama III: a captive's account | filled | `blanc_narrative-of-captivity-in-abyssinia_1868.txt` (1868); 107,104 words; eng | ethiopian-christianity-tewodros-to-menelik, context |
| era 9 rows 308, 309 and 310, Yohannes IV, Menelik II and Taytu: the royal chronicle, in French, tome I | filled | `guebre-sellassie_chronique-du-regne-de-menelik-ii-t1-fra_coppet1930.txt` (1930); 220,265 words; fra | ethiopian-christianity-tewodros-to-menelik, tradition |
| era 9 row 308, Yohannes IV: an outside account | filled | `wylde_modern-abyssinia_1901.txt` (1901); 252,750 words; eng | ethiopian-christianity-tewodros-to-menelik, context |
| era 9 row 311, Liang Fa: Morrison's Memoirs, vol. 2 | filled | `morrison_memoirs-of-the-life-and-labours-of-robert-morrison-v2_1839.txt` (1839); 234,648 words; eng | the-missionary-movement-s-native-churches-seramp, context |
| era 9 row 311, Liang Fa: a list of his works | filled | `wylie_memorials-of-protestant-missionaries-to-the-chinese_1867.txt` (1867); 139,374 words; eng | the-missionary-movement-s-native-churches-seramp, context |
| era 9 row 311, Liang Fa: the missionary's account of a baptism in 1816 | filled | `milne_retrospect-of-the-first-ten-years-of-the-protestant-mission-to-china_1820.txt` (1820); 112,281 words; eng | the-missionary-movement-s-native-churches-seramp, context |
| era 9 row 312, Ta'unga: a missionary's account that quotes his reports | filled | `gill_gems-from-the-coral-islands-western-polynesia_1855.txt` (1855); 69,182 words; eng | the-missionary-movement-s-native-churches-seramp, context |
| era 9 row 313, Joeli Bulu: his autobiography, in translation | filled | `bulu_joel-bulu-the-autobiography-of-a-native-minister-in-the-south-seas_2nd-ed1884.txt` (1884); 31,438 words; eng | the-missionary-movement-s-native-churches-seramp, tradition |
| era 9 rows 314, 315 and 316, Rasalama, Rafaravavy and Ranavalona I: the missionaries' narrative of the persecution | filled | `freeman-johns_narrative-of-the-persecution-of-the-christians-in-madagascar_1840.txt` (1840); 98,021 words; eng | malagasy-christianity, context |
| era 9 rows 316 and 317, Ranavalona I and Ranavalona II: Ellis's later narrative | filled | `ellis_martyr-church-christianity-in-madagascar_1870.txt` (1870); 115,449 words; eng | malagasy-christianity, context |
| era 9 row 318, Joseph Mukasa Balikuddembe: a mission history that names him | filled | `stock_story-of-uganda-and-the-victoria-nyanza-mission_1892.txt` (1892); 63,830 words; eng | east-african-christianity-uganda-martyrs, context |
| era 9 row 319, James Hannington: a Life | filled | `dawson_james-hannington-a-history-of-his-life-and-work_1887.txt` (1887); 148,671 words; eng | east-african-christianity-uganda-martyrs, context |
| era 9 row 319, James Hannington: his last journals | filled | `hannington_last-journals-of-bishop-hannington_dawson1888.txt` (1888); 49,043 words; eng | east-african-christianity-uganda-martyrs, tradition |
| era 9 row 320, Mwanga II: a missionary's Life, with his letters | filled | `mackay_a-m-mackay-pioneer-missionary-to-uganda_by-his-sister1891.txt` (1891); 126,026 words; eng | east-african-christianity-uganda-martyrs, context |
| era 9 row 321, Ntsikana: his hymn in English, in a later history | filled | `molema_bantu-past-and-present_1920.txt` (1920); 158,701 words; eng | southern-african-mission-churches, context |
| era 9 row 322, Moshoeshoe: Casalis, The Basutos | filled | `casalis_basutos_1861.txt` (1861); 102,140 words; eng | southern-african-mission-churches, tradition |
| era 9 row 322, Moshoeshoe: Casalis, Les Bassoutos, in French | filled | `casalis_les-bassoutos-fra_1859.txt` (1859); 95,204 words; fra | southern-african-mission-churches, tradition |
| era 9 row 324, Pliny Fisk: a Memoir | filled | `bond_memoir-of-the-rev-pliny-fisk_1828.txt` (1828); 151,100 words; eng | arab-evangelical-churches, context |
| era 9 rows 324, 325 and 326, Pliny Fisk, the Arabic Bible translators and Asaad es Shidiak: Jessup's memoir, vol. 1 | filled | `jessup_fifty-three-years-in-syria-v1_1910.txt` (1910); 152,788 words; eng | arab-evangelical-churches, tradition |
| era 9 row 325, Butrus el Bistany and Nasif el Yazigy: Jessup's memoir, vol. 2 | filled | `jessup_fifty-three-years-in-syria-v2_1910.txt` (1910); 159,805 words; eng | arab-evangelical-churches, tradition |
| era 9 row 326, Asaad es Shidiak: a Memoir | filled | `shidiak-memoir_memoir-of-asaad-esh-shidiak_1834.txt` (1834); 22,343 words; eng | arab-evangelical-churches, context |
| era 9 rows 298 and 299, Nerses Varzhapetian and Grigor Odian: an Armenian patriarch's account of his church | held already | `ormanian_church-of-armenia_gregory1912.txt` | — |
| era 9 row 193, Abraham Kuyper: Calvinism, the Stone Lectures | not taken | — | Date check done: three English scans and two Dutch ones print no year and have no copyright notice or dated preface. On the hand-fetch list. |
| era 9 row 204, Hudson Taylor: A Retrospect | not taken | — | Date check done: no scan has a dated title page, copyright notice or dated preface. On the hand-fetch list. |
| era 9 row 210, Charles Lwanga: Walsh on the Uganda martyrs | not taken | — | Date check done: no year, notice or dated preface; the catalogue says "[between 1920 and 1929?]". Klein (1897) was taken in its place. |
| era 9 row 191, Catherine Booth: Female Ministry (1859) | not found before 1931 | — | A reprint of 1975 only. |
| era 9 row 181, John Nelson Darby: the Letters, the Collected Writings, a Life | not found | — | Reprints of 1964 and 1974 only. Three books of his own and Neatby's history were taken. |
| era 9 row 197, Ambrose of Optina: his letters and an early Life | not found | — | About thirty queries over two batches. The Optina history of 1902 tells of him. On the hand-fetch list. |
| era 9 row 207, Kiai Sadrach: Dutch mission reports beyond Adriaanse and Coolsma | not fetched | — | dbnl.org disallows automated clients. On the hand-fetch list. |
| era 9 row 212, Nehemiah Tile | not found | — | Not named in ten printed works searched. Du Plessis (1911) has one sentence on an ex-Wesleyan "Nehemiah" in Tembuland. On the hand-fetch list. |
| era 9 row 185, Hong Xiuquan: Hamberg, The Visions of Hung-Siu-tshuen (1854) | not found | — | Meadows (1856) and Brine (1862) discuss and extract it. |
| era 9 rows 186 and 187, Os Sertoes: a printing of 1902 to 1911 other than the 1905 one | not found | — | The other items on the host are modern editions or the same Brasiliana file. |
| era 9 row 186, Antonio Conselheiro: his own words | not found | — | — |
| era 9 row 281, Apolinario de la Cruz: Mas, Informe (1843) | located, not vendored | — | It tells of him, but the title page is wanting, the page images cannot be read and the OCR is badly garbled. Another scan is CC BY-NC-ND. |
| era 9 row 288, Philiphe Binh: his own book | not found before 1931 | — | A modern printing only. Louvet, Launay and Shortland do not tell of him. |
| era 9 row 291, Joseph Dolci: the acts of the Maronite synod of 1818 | not found | — | — |
| era 9 row 292, Elias Hoyek | not found | — | An Arabic history of the Maronites (al-Dibs, 1905) has OCR that cannot be read. |
| era 9 row 298, Nerses Varzhapetian: the National Assembly's records and his reports | not found | — | — |
| era 9 row 301, Konstantinos Oikonomos: his own writing | located, not vendored | — | Peri ton O' hermeneuton, vol. 1: the title-page year cannot be read. Pharmakidis's pamphlet against him was taken. |
| era 9 row 302, Antim I: the acts of the council of 1872 | not found | — | The firman of 1870 is held in German (Scheffler, 1909). |
| era 9 row 305, Iakov Netsvetov | not found before 1931 | — | His journals are in modern editions only. |
| era 9 row 311, Liang Fa: his tract | not found | — | — |
| era 9 row 312, Ta'unga: his own narrative | not found before 1931 | — | Gill (1855) quotes short reports of his. |
| era 9 row 321, Ntsikana: Bokwe's Ntsikana | not found | — | — |
| era 9 rows 293 and 295, Macarius of Optina and Theophan the Recluse: their letters | not found | — | On the hand-fetch list. |
| era 9 row 280, the Iglesia Filipina Independiente: Doctrina y Reglas Constitucionales (1904), Oficio Divino (1906) | not found | — | — |

**Cautions for profile writers (era 9, batch 2a)**

- **Not the person's own words.** Row 226 (Herman): a Valaam monastery compilation of 1894; his own letters
  are in its Appendix I. Rows 293 and 197 (Macarius and Ambrose of Optina): the monastery's history of 1902
  tells of them; their letters are not held. Row 296 (Makary Glukharev): materials for a biography, by another.
  Row 290 (Massaad): Churchill does not name him. Row 299 (Odian): Lynch prints the National Constitution in
  English in an appendix and does not name him. Row 303 (Thomas Jones): one entry in a dictionary of Welsh
  ministers. Row 304 (Clark): his wife's book, and one paper of his own in the Assam jubilee volume. Rows
  306-310 (the Ethiopian rulers and Salama III): two captives' accounts, a consul's book and the royal
  chronicle in French. Rows 263-266 (the Taiping leaders and Roberts): three outside accounts. Row 282
  (Niijima): two Lives. Row 320 (Mwanga): told inside a missionary's Life. Row 322 (Moshoeshoe): told by
  Casalis. Rows 246 and 247 (Sharpe; Smith of Demerara): Bleby reports Sharpe's words to him; the Demerara
  volume is the court martial record, with the prisoner's defence and his letters in the appendix.
- **Names as the files spell them.** Row 311: Milne (1820) tells of the baptism of 'Leang-kung-fah' in 1816 and
  does not say he is Liang Fa; Morrison's Memoirs print 'Leang-Afa'. Row 318: Stock prints 'Balikudembe
  Mukasa'. Rows 210 and 318: Klein prints 'Charles Louanga' and 'Joseph Mkasa'. Row 312: Gill prints
  'Taunga', in two short quoted reports only. Row 213: the African Methodist Episcopal encyclopaedia has no
  entry headed Mokone; he is told of in its entry 'Africa, South'. Row 302: Scheffler prints 'Anthimos'. Ellis's
  Martyr Church often reads a capital R as E ('Eanavalona').
- **Translation only.** The Chronicle of Menelik II is a French translation from Amharic. Joel Bulu's
  autobiography was 'translated by a missionary', who is not named. The firman of 1870 is in Scheffler's German.
  Berthe's Garcia Moreno is from the French. Darby's Studies on Daniel is from the French, revised by him. My
  Life in Christ is from the Russian, of which vol. 1 is also held. Casalis is held in French and in English.
- **Author not named on the title page.** The Pharmakidis pamphlet and Darby's Dialogues (the host record
  names each); Wylie's Memorials; the Memoir of Asaad Esh Shidiak (the host names Isaac Bird); Mackay ('by his
  sister'); the Valaam book; the Optina history ('E. V.'); the materials on Makary ('D. D. Fil-nova'); Lindley
  ('Lin-Le'); Dom Vital ('pelo mesmo Bispo'); the collection of concordats (its foreword is signed Angelo
  Mercati). The title pages of the Documentos interesantes and of Macedo Costa cannot be read
  in the OCR; their titles are from the catalogue record.
- **Later editions and printings.** Bleby (third edition, 1868); Joel Bulu (second, 1884); Darby's Studies
  (third, 1864) and Dialogues (second, 1863); Theophan's Bogougodnaia zhizn (second, 1899); Mackay (tenth
  thousand, 1891); Ellis's Martyr Church (third thousand, 1870); Aggressive Christianity (the American printing of 1883); Klein (a 'nouvelle edition', 1897).
- **Part of a larger work.** Vol. 1 only: Kireevsky; John of Kronstadt in Russian. Vol. 2 only: Lynch, Louvet,
  Launay, Morrison's Memoirs. Lindley's vol. 2 joins vol. 1 from batch 1. Blair and Robertson is vol. 52. The
  Chronicle of Menelik II is tome I only: the host file also holds tome II (1932), which was cut away. Jessup
  and Garcia Moreno are complete in two volumes each.
- **Mixed voices.** Darby's Dialogues is bound with 'Dr. Colenso and the Pentateuch'. The Assam jubilee volume
  and the African Methodist Episcopal encyclopaedia are by many hands. The Codigo de la Reforma is the state's
  laws. In the collection of concordats the Haitian concordat of 1860 is no. CVIII, in Italian and French
  columns that the OCR interleaves; it names Fabre Geffrard.
- **Dates.** No year on the title page: Hardy, Uchimura, Jessup (both volumes), both Catherine Booth books,
  Stern, the Documentos interesantes and Macedo Costa; each header names the copyright notice
  or the dated preface used. Macedo Costa's book carries two prefixed letters of January 1887 against the
  catalogue's 1886. A Guerra de Canudos prints 1902 on its title page; the OCR misreads it as 1903.
- **Row 308, Boru Meda.** The Chronicle of Menelik II has a chapter on the assembly at 'Borou-Mieda'; its
  locus is in the shelf row. **Row 285:** the Codigo begins with 1856, so the Ley Juarez of 1855 is not in it.
  **Row 286:** the consecration decree was not found in Garcia Moreno's two volumes; Berthe tells of it.
- **OCR.** The Russian and Ukrainian files are fair, in the old spelling. The Greek of Pharmakidis is noisy.
  Launay is a microfiche scan with page fragments inside the edict passage. Milne reads the long s as f.

## Era 8 (1650-1815), batch 2 (2026-11-15): the British Isles and the Methodists, North America, Catholic Europe and the Jesuits

Thirty-seven files, 5,346,333 words. The wants are the era 8 rows of the Who scan's wanted list for Britain,
North America and Catholic Europe, Open-Gaps items 181 and 225, and the volumes batch 1 found and left. No new
search was run: the candidates are the era 8 handover's two unspent tables and its list of volumes found and not
vendored. The record is in `Build/Ministry/Operations/Audits/2026-11-15_library-era8-b2/` (`Search_Log.md`, with
the page-image reads, three judgement calls and the cautions for writers). Every file has a printed imprint of
1930 or earlier, read on its title page or on the scan's page image; Love's Samson Occom prints no year on its
title page and is dated by the copyright notice of 1899 on the verso. Rows in the tables above are not rewritten.

| want | state | file(s), with the imprint year | words | language | shelf |
|---|---|---|---:|---|---|
| Wanted row A135: Anne Dutton, her own account | filled, the printing of 1750 in three parts, with her letter on printing by a woman | `dutton-anne_brief-account-of-the-gracious-dealings-of-god_1750.txt` (1750) | 139,335 | eng | the-baptists, tradition |
| Wanted row A136: Gibbons, Memoirs of Isaac Watts | filled | `gibbons-thomas_memoirs-of-isaac-watts_1780.txt` (1780) | 126,632 | eng | english-old-dissent, tradition (the letters to Watts: context) |
| Wanted row A137: Orton, Memoirs of Doddridge | filled, in the Edinburgh reprint of 1825 with Russell's essay | `orton_memoirs-of-philip-doddridge_russell1825.txt` (1825) | 99,840 | eng | english-old-dissent, tradition (Russell's essay: context) |
| Wanted row A139: Roberts, Memoirs of Hannah More | filled in part, vol. 1 (to 1785), third edition; vols. 2-4 not taken | `roberts-william_memoirs-of-hannah-more-v1_3rd-ed1835.txt` (1835) | 137,635 | eng | restoration-georgian-church-of-england, context |
| Wanted row A140: the Life of Thomas Bray (1746) | filled, in Todd's second edition with the Associates' proceedings for 1807 | `todd-henry-john_publick-spirit-life-and-designs-of-thomas-bray_2nd-ed1808.txt` (1808) | 30,773 | eng | restoration-georgian-church-of-england, tradition |
| Wanted row A141: the Life of William Wilberforce by his sons | filled in part, vol. 1 (to 1792); the scan stops inside the appendix; vols. 2-5 not taken | `wilberforce-robert-and-samuel_life-of-william-wilberforce-v1_1838.txt` (1838) | 109,172 | eng | restoration-georgian-church-of-england, context |
| Wanted row A159: Robert Raikes | filled, a Life of 1877 that prints his letters of 1783 and 1785 as extracts | `gregory-alfred_robert-raikes-journalist-and-philanthropist_1877.txt` (1877) | 42,296 | eng | the-sunday-school-and-bible-institute-movement and restoration-georgian-church-of-england, context |
| Wanted row A133: Sarah Crosby and the Methodist women preachers | filled, Taft's two volumes in one file | `taft_biographical-sketches-of-holy-women-v1-v2_1825-1828.txt` (1825, 1828) | 228,227 | eng | the-methodist-revival, context |
| Wanted row A128: Samson Occom | filled in part: Love's history, with the opening of Occom's narrative of 1768 only | `love-william-deloss_samson-occom-and-the-christian-indians-of-new-england_1899.txt` (1899, by its copyright notice) | 147,651 | eng | the-evangelical-awakening-in-new-england, context (Occom's extract: tradition) |
| Wanted row A131: Nathan Cole | filled in part: the extract Walker printed | `walker-george-leon_some-aspects-of-the-religious-life-of-new-england_1897.txt` (1897) | 52,955 | eng | the-evangelical-awakening-in-new-england, context (Cole's extract: tradition) |
| Wanted row A132: Lemuel Haynes | filled, Cooley's Life with Haynes's sermons and letters | `cooley_sketches-of-the-life-and-character-of-lemuel-haynes_1837.txt` (1837) | 111,138 | eng | the-evangelical-awakening-in-new-england and the-black-church-in-america, context (Haynes's own pieces: tradition) |
| Wanted row A134: Samuel Davies, with the memoirs of him | filled, vol. 1 of the Philadelphia edition (vol. 3 of another edition is held) | `davies_sermons-on-important-subjects-v1_campbell1794.txt` (1794) | 224,732 | eng | the-evangelical-awakening-in-new-england, tradition (the memoirs: context) |
| Wanted row A138: Judith Sargent Murray | filled, The Gleaner in three volumes | `murray-judith-sargent_the-gleaner-v1_1798.txt`, `-v2_1798.txt`, `-v3_1798.txt` (1798) | 124,740; 117,586; 112,173 | eng | early-american-unitarians-universalists, tradition |
| Wanted row A157: James McGready | filled, with his narrative of the revival (1801) | `mcgready_posthumous-works_smith1837.txt` (1837) | 245,663 | eng | the-second-great-awakening-and-camp-meeting-worl, tradition |
| Wanted row A158: Thomas Campbell, Declaration and Address | filled, in the line-for-line reprint of 1908 | `campbell-thomas_declaration-and-address-centennial-edition_1908.txt` (1908) | 31,251 | eng | the-stone-campbell-restoration-movement, tradition |
| Wanted row A158: Richardson, Memoirs of Alexander Campbell, vol. 1 | held already | `richardson_memoirs-of-alexander-campbell-v1_1868.txt` | | | |
| Wanted row A146: Muratori, the Life by his nephew | filled | `soli-muratori_vita-del-proposto-lodovico-antonio-muratori-ita_napoli1758.txt` (1758) | 170,531 | ita | catholic-church-ancien-regime, tradition (the appendices: context) |
| Wanted row A146: Muratori on the Paraguay missions | filled in Italian (part 1) and in the English of 1759 | `muratori_il-cristianesimo-felice-nelle-missioni-del-paraguai-ita_1743.txt` (1743); `muratori_relation-of-the-missions-of-paraguay_1759.txt` (1759) | 104,940; 80,663 | ita; eng | society-of-jesus-1650-1814, context (Cattaneo's letters in the Italian: tradition) |
| Wanted row A147: Rancé, Marsollier's Life | filled, two volumes, with Rancé's Pensées in tome 2 | `marsollier_vie-de-dom-armand-jean-le-bouthillier-de-rance-t1-fra_1758.txt`, `-t2-fra_1758.txt` (1758) | 105,028; 126,574 | fra | catholic-church-ancien-regime, tradition |
| Wanted row A148: Fontaine, Mémoires | filled, two volumes | `fontaine-nicolas_memoires-pour-servir-a-l-histoire-de-port-royal-t1-fra_1738.txt`, `-t2-fra_1738.txt` (1738) | 174,150; 194,316 | fra | port-royal-jansenism, tradition (the editors' pieces in tome 1: context) |
| Wanted row A148: du Fossé, Mémoires | filled | `du-fosse_memoires-pour-servir-a-l-histoire-de-port-royal-fra_1739.txt` (1739) | 140,822 | fra | port-royal-jansenism, tradition (the editors' Life: context) |
| Open-Gaps 225: Quesnel, Réflexions morales | filled in part, tome 1 (Matthew and Mark); the later tomes not located | `quesnel_nouveau-testament-avec-des-reflexions-morales-t1-fra_1693.txt` (1693) | 267,423 | fra | port-royal-jansenism, tradition; catholic-church-ancien-regime, context, needs-ruling |
| Open-Gaps 181: Dobrizhoffer, in English | filled, three volumes | `dobrizhoffer_account-of-the-abipones-v1_1822.txt`, `-v2_1822.txt`, `-v3_1822.txt` (1822) | 102,833; 100,086; 91,380 | eng | society-of-jesus-1650-1814, tradition |
| Open-Gaps 181: Dobrizhoffer, in Latin | filled in part, pars I; parts 2 and 3 not located | `dobrizhoffer_historia-de-abiponibus-pars1-lat_1784.txt` (1784) | 125,048 | lat | society-of-jesus-1650-1814, tradition |
| Wanted row A123: Vieira's Sermões | filled in part, three of the parts | `vieira_sermoens-parte3-por_1683.txt` (1683); `vieira_sermoens-parte5-por_1689.txt` (1689); `vieira_sermoens-parte12-por_1699.txt` (1699) | 194,892; 200,485; 153,744 | por | colonial-latin-american-devotional-catholicism and society-of-jesus-1650-1814, tradition |
| Batch 1's list: Pascoe, vol. 2 | filled | `pascoe_two-hundred-years-of-the-spg-v2_1901.txt` (1901) | 522,673 | eng | victorian-church-of-england and restoration-georgian-church-of-england, context |
| Batch 1's list: Launay, tome 3 | filled | `launay_histoire-generale-de-la-societe-des-missions-etrangeres-t3-fra_1894.txt` (1894) | 224,891 | fra | chinese-catholicism-1650-1906, context |
| Batch 1's list: the Continuatio of the Historia cultus Sinensium | filled | `historia-cultus-sinensium_continuatio-lat_1700.txt` (1700) | 34,768 | lat | chinese-catholicism-1650-1906, tradition, needs-ruling |
| Batch 2 (ME-7): Parry, Six Months in a Syrian Monastery | filled, the Google scan | `parry_six-months-in-a-syrian-monastery_1895.txt` (1895) | 149,287 | eng | the-sayfo-and-the-syriac-diaspora, context, needs-ruling |
| Batch 1's list: Valentijn, deel 2 | not taken | no church section was found in it; deel 3, held, has Amboina's church | | | |
| Batch 1's list: Code noir, the collection of 1743 | not taken | the acts that touch the church are in the held collection of 1767 | | | |
| Batch 1's list: Gobat, New York 1850 | not taken | a later printing of the held London print of 1834 | | | |
| Not found by the first era 8 search | not found | Hindmarsh (1861); Ann Griffiths in Welsh; Kirk's Biographies (1909); Davenport's Confession; Herman of Alaska; the Methodist gaps (Wesley's Letters and later Sermons, Charles Wesley's Journal vol. 2, Whitefield's later Journals, Fletcher's Checks, the Arminian Magazine) | | | |

## Era 9 (1815-1906), the located volumes (2026-11-16): the follow-on to batch 2b

Twenty-seven files, 4,092,114 words: the volumes batch 2b located and did not take, with the items it named
without an identifier. The record is in `Build/Ministry/Operations/Audits/2026-11-16_library-era9-located/`
(`Search_Log.md`, with the page-image reads, the corrections to the list, four calls and the cautions for
writers). Every file has a printed imprint of 1930 or earlier, read on its title page or on the scan's page
image. Rows in the tables above are not rewritten.

| want | state | file(s), with the imprint year | words | language | shelf |
|---|---|---|---:|---|---|
| era 9 row 257, Henry Drummond: Dialogues on Prophecy, vols. 2 and 3 | filled; the work is now held whole | `dialogues-on-prophecy_v2_1828.txt` (1828); `dialogues-on-prophecy_v3_1829.txt` (1829) | 98,344; 139,301 | eng | catholic-apostolic-church-irvingites, antecedent |
| era 9 row 257: the Morning Watch | filled in part, vols. I (1829) and III (1831) | `morning-watch_v1-1829_1830.txt` (1830); `morning-watch_v3_1831.txt` (1831) | 389,469; 268,314 | eng | catholic-apostolic-church-irvingites, antecedent |
| era 9 row 257, Henry Drummond: his speeches and pamphlets, vol. 2 | filled; the work is now held whole | `drummond-henry_speeches-in-parliament-v2_lovaine1860.txt` (1860) | 159,032 | eng | catholic-apostolic-church-irvingites, tradition |
| era 9 row 272, Samuel Wilberforce: the Life, vols. 2 and 3 | filled; the work is now held whole | `wilberforce-reginald_life-of-samuel-wilberforce-v2_1881.txt` (1881); `-v3_1882.txt` (1882) | 165,419; 178,217 | eng | victorian-church-of-england, context |
| era 9 row 271, Lord Shaftesbury: the Life, vols. 2 and 3 | filled; the work is now held whole | `hodder_life-and-work-of-seventh-earl-of-shaftesbury-v2_1887.txt` (1887); `-v3_1886.txt` (1886) | 191,569; 182,948 | eng | victorian-church-of-england, context |
| era 9 row 273, Frederick Denison Maurice: the Life, vol. 2 | filled; the work is now held whole | `maurice-f_life-of-frederick-denison-maurice-v2_1884.txt` (1884) | 293,220 | eng | victorian-church-of-england, context |
| era 9 row 278, Nicholas Wiseman: the Life, vol. 2 | filled; the work is now held whole | `ward-wilfrid_life-and-times-of-cardinal-wiseman-v2_1897.txt` (1897) | 232,475 | eng | catholic-church-long-nineteenth-century, context |
| era 9 row 261, Ralph Waldo Emerson: the Memoir, vol. 2 | filled, in the eighth edition (vol. 1 is the printing of 1887) | `cabot_memoir-of-ralph-waldo-emerson-v2_8th-ed1895.txt` (1895) | 114,536 | eng | american-unitarianism-universalism-consolidations, context |
| era 9 row 267, Richard Hurrell Froude: his Remains, the other three volumes | filled; the work is now held whole | `froude_remains-pt1-v2_1838.txt` (1838); `froude_remains-pt2-v1_1839.txt` (1839); `froude_remains-pt2-v2_1839.txt` (1839) | 108,907; 129,136; 198,507 | eng | the-oxford-movement-and-anglo-catholic-revival, tradition |
| era 9 row 274, John William Colenso: The Pentateuch, a further part | filled, part III (the list said part 2; part II was not found) | `colenso_pentateuch-and-book-of-joshua-pt3_1863.txt` (1863) | 129,798 | eng | victorian-church-of-england, tradition |
| era 9 row 274, John William Colenso: a Life | filled in part, vol. 1 of 2 | `cox-george-w_life-of-john-william-colenso-v1_1888.txt` (1888) | 257,341 | eng | victorian-church-of-england and southern-african-mission-churches, context |
| The Student Volunteer Movement: Mott's history and Wilder's pledge pamphlet | filled | `mott_history-of-the-student-volunteer-movement_1892.txt` (1892); `wilder_pledge-of-the-student-volunteer-movement_1890.txt` (1890) | 7,371; 3,866 | eng | the-student-volunteer-movement-and-edinburgh-191, tradition |
| era 9 row 323, J. Taylor Hamilton: his history of the Moravians in the United States | filled, in the American Church History volume with two Reformed histories | `corwin-dubbs-hamilton_american-church-history-v8-reformed-and-moravian_1895.txt` (1895) | 160,235 | eng | moravian-church-after-1815, tradition (Hamilton's part only) |
| era 9 row 277, Bernadette Soubirous: Lasserre in Sisk's English | filled, a second English version | `lasserre_our-lady-of-lourdes_sisk1872.txt` (1872) | 117,513 | eng | catholic-church-long-nineteenth-century, context |
| era 9 row 254, Robert Roberts: The Trial, and his debate with Bradlaugh | filled | `roberts-robert_the-trial_1908.txt` (1908); `roberts-bradlaugh_is-the-bible-divine-six-nights-discussion_1876.txt` (1876) | 134,261; 138,725 | eng | christadelphians, tradition |
| era 9 row 260, J. G. Bellett: two more of his books | filled; the Evangelists scan holds John only | `bellett_minor-prophets_1870.txt` (1870); `bellett_evangelists-gospel-by-st-john_7th-ed1886.txt` (1886) | 25,691; 57,272 | eng | plymouth-brethren-and-dispensational-formation, tradition |
| era 9 row 252, Eliza R. Snow: her Life of Lorenzo Snow | filled | `snow_biography-and-family-record-of-lorenzo-snow_1884.txt` (1884) | 206,667 | eng | latter-day-saints-lds, tradition |
| The Pacific Garden Mission's annual reports | filled in part: the report for the year ended September 1908; the statement of 1916 prints no year and is held for Mark; the report of 1895 not found | `pacific-garden-mission_thirty-first-annual-report_1908.txt` (1908) | 3,980 | eng | the-rescue-mission-movement, tradition |
| In His Steps in printings of 1899; Newton's Thoughts on the Apocalypse in the printing of 1904 | not taken | later printings of texts already held | | | |

## Era 10, batch 2b, the periodicals (2026-11-16): the follow-on to batch 2

Forty-five files, 4,325,430 words: the numbers of The Christian East and the volumes of The International
Review of Missions that batch 2 found and did not take. The record is in
`Build/Ministry/Operations/Audits/2026-11-16_library-era10-b2b-periodicals/` (`Search_Log.md`, with the
page-image reads, seven calls and the cautions for writers). Every file has a printed date of 1930 or earlier,
on its masthead, cover or title leaf. Rows in the tables above are not rewritten.

| want | state | file(s) | words | language | shelf |
|---|---|---|---:|---|---|
| The Christian East, the numbers to 1930 not yet held | filled but for one: 31 numbers. With the twelve held, every number of vols. I-X is held and vol. XI lacks no. 4 | `christian-east_v<vol>-no<no>-<month or season>-<year>.txt`: I.1, I.2, I.4 (1920); II.1, II.3, II.4 (1921); III.1, III.4 (1922); V.1-4 (1924); VI.1-3 (1925), VI.4 (January 1926); VII.1-4 (1926); VIII.1-3 (1927); IX.1-4 (1928); X.2-4 (1929); XI.3 (1930) | 761,254 in all | eng; some French, Latin and Greek | the-anglican-communion-twentieth-century, tradition (each number whole); 39 rows for single documents on the Greek, Russian, émigré, Balkan and Syriac entries, and one on the ecumenical movement |
| The Christian East, vol. XI, no. 4 | not taken, held for Mark: it prints "Winter, 1930-31" and cites a letter of March 1931 | | | | |
| The International Review of Missions, 1914-1920 | filled: seven volumes | `international-review-of-missions_v3_1914.txt` to `_v9_1920.txt` | 1,757,789 | eng | the-student-volunteer-movement-and-edinburgh-191, tradition; rows for the survey's note on Garrick Braid (1917), Willis on the Uganda church (1918), the Mar Thoma statement and the China plan of union (1920) |
| The International Review of Missions, 1921, 1924-1927, 1929, 1930 | filled: seven volumes. With the three held, every volume from 1914 to 1930 is held | `international-review-of-missions_v10_1921.txt`, `_v13_1924.txt` to `_v16_1927.txt`, `_v18_1929.txt`, `_v19_1930.txt` | 1,806,387 | eng | the-ecumenical-movement-and-the-wcc, tradition; rows for the National Christian Council of China (1924), Speer on Montevideo (1925), Loram on the separatist churches (1926), Kriele on Nias (1927), Braga, the Bishop of Dornakal and Kozaki (1929) |
| Proceedings of the Church Missionary Society, 1910-1921 | not taken, and ruled out by Mark on 2026-11-16: the microfilm they were scanned from carries "© MM 1967, reproduction of this film prohibited" | twelve items located, `per_proceedings-church-missionary-soc-for-africa-a_<year>` | | | |

## Later — queued

- ME-21 by a browser; Lang 1834 and the Peking mission after 1808; the
  Brosset Additions (1851) and part II (1856-57); the 1860 Concordat in a period printing.
- **Living traditions with no entry after a date** (Open-Gaps 158): 79 gaps, worked by era. Batches 3 to 6
  took 40; next are the gaps after 1815 (batch 7), then those after 1906.
- **Families the tree doesn't reach** (Open-Gaps 159): the Patriarchate of Alexandria, Cyprus, the
  Polish, Czech-Slovak and Macedonian churches, and the Eastern Catholic churches never named.
- **Living marks graded none** (Open-Gaps 162): Kongo, Transylvania, the Schwenkfelders, New France.
  These want dated own-voice items after 2010. That is mostly the web, not public-domain print.
- **The loci pass** for multi-work volumes.
