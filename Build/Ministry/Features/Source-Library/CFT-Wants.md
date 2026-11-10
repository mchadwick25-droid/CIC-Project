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
| AP15, Korea | Catholic and Protestant own-voice texts | filled | `dallet_histoire-de-l-eglise-de-coree-t1-fra_1874.txt`, `-t2-`; `korean-repository_v3-1896_seoul1896.txt`; `underwood_call-of-korea_1908.txt` | The Korean Catholic entry gets its history, and AP15 gets dated Protestant sources. |
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
| Athonite monasticism after 1300 | filled | `athos-monasteries_haupturkunden-fur-die-geschichte-der-athoskloster-ger-grc_meyer1894.txt`; `dapontes_kepos-chariton-grc_sophocleous1880.txt`. Held already: Georgirenes (1678) | Meyer: the 1394 typikon on the hesychast entry (`needs-ruling`), the documents of 1498-1574 on Ottoman 1453-1650, those of the 17th-18th centuries on Ottoman 1650-1821; Dapontes on Ottoman 1650-1821 | The Holy Mountain's own typika, patriarchal decrees and letters from 1394 to the Kollyva circulars, and a Xeropotamou monk's own book. Meyer's Greek OCR is garbled: second witness for the Greek. |
| The Carthusians after 1534 | filled | `chauncy-maurice_historia-aliquot-martyrum-anglorum-lat_1888.txt`; `chauncy-maurice_history-of-the-sufferings-of-eighteen-carthusians-in-england_1890.txt`; `carthusian-statutes_nova-collectio-statutorum-ordinis-cartusiensis-lat_1681.txt` | Chauncy on the Tridentine church; the statutes on the ancien-regime church | A London Carthusian's own account of 1535 (printed 1550), in Latin and a clean English; the order's statutes as gathered in 1681. Le Couteulx's Annales stop at 1420. |
| The Cistercians after 1300 | filled | `rance_de-la-saintete-et-des-devoirs-de-la-vie-monastique-t1-fra_1683.txt`, `-t2-`; `trappists_constitutions-and-usages-of-the-reformed-cistercians-of-la-trappe-eng-lat_1894.txt`. Held already: the Port-Royal acts (1724) | Rance on the ancien-regime church; the constitutions on the long nineteenth century | La Trappe's abbot in 1683, and the Trappists' own law of 1894. Not found: the 1718 Reglements. Located, not vendored: the Nomasticon Cisterciense (1664; garbled OCR). |
| The Maronites after 1517 | filled, no shelf | `duwayhi_tarikh-al-taifa-al-maruniyya-ara_shartuni189x.txt` | none yet | Patriarch al-Duwayhi's own history of his church (Beirut, 1890s). The OCR is garbled: second witness. Not found: the 1736 Synod of Mount Lebanon in a readable printing (the Zainati 1926 scan is unreadable), Anaissi's Bullarium. |
| The canons regular after 1246 | filled | `barnwell-priory_observances-in-use-at-barnwell-lat-eng_clark1897.txt`; `premonstratensian-statutes_statuta-renovata-ordinis-praemonstratensis-lat_1626.txt`. Held already: Thomas a Kempis's Chronicle of Mount St Agnes, Busch's Chronicon Windeshemense | Barnwell on the Gregorian church (written 1295-96); the statutes on the Tridentine church | An Augustinian priory's own customary, and the Premonstratensians' renewed statutes of 1626. Not found: Le Paige (1633). |
| The Order of Malta after 1291 | filled | `hospitallers_statuti-della-sacra-religione-di-s-giovanni-gierosolimitano-ita_bosio1589.txt` | the Tridentine church | The Order's own statutes after its chapter of 1584. Located, not vendored: Bosio's Istoria (1594-1602; 5-6.5 MB each), Vertot (1726), the Cartulaire general III-IV. |
| The Carmelites after 1300 | filled | `carmelite-general-chapters_acta-capitulorum-generalium-v1-1318-1593-lat_wessels1912.txt` | the chapters to 1513 on Avignon to Lateran V; those of 1524-1593 on the Tridentine church | The order's general chapters, 1318-1593. Located: Zimmerman's Monumenta (1907); the Speculum Carmelitanum (1680; garbled OCR). |
| The Franciscans after 1517 | filled | `de-luca-giovanni_annales-minorum-t18-1540-1553-lat_1740.txt`; `capuchin-constitutions_constitutiones-fratrum-minorum-capuccinorum-lat_1638.txt` | De Luca on the ancien-regime church (written 1740); the constitutions on the Tridentine church | The order's own annals for 1540-1553, and the Capuchins' own law. Located: Annales tomes XIX (1745) and XX (1794). Not found: Wadding's tome XVI, Boverius. |
| The Dominicans after 1300 | filled | `dominican-general-chapters_acta-capitulorum-generalium-v2-1304-1378-lat_reichert1899.txt`; `...-v6-1601-1628-lat_reichert1902.txt` | Avignon to Lateran V; the Tridentine church | The general chapters' acts, 1304-1378 and 1601-1628. Located: vols. V and VII. Vols. VIII-XII (after 1656) are not on archive.org. |
| The Jesuits after 1650 | filled | `jesuit-relations_thwaites-v36-fra-eng_1896-1901.txt` to `-v40-` (1650-1653); `lettres-edifiantes_memoires-de-la-chine-t19-fra_1781.txt`, `-t20-`, `-t22-` | the ancien-regime church | The Jesuits' own reports from New France after 1650 and from Peking, 1717-1731. These also serve the church in New France after 1650 and Chinese Catholics 1650-1906 (later in Open-Gaps 158). Located: Thwaites 41-46 (1654-1660). |
| The Discalced Carmelites after 1622 | filled | `brother-lawrence_practice-of-the-presence-of-god_allenson1906.txt`; `francisco-de-santa-maria_reforma-de-los-descalzos-t2-spa_1655.txt`. Held already: the Compiegne Carmelites (1836) | the ancien-regime church; Compiegne now also on the long nineteenth century | A Paris lay brother's own letters (1666-1691) and the order's own history (1655). The Reforma's OCR is fair to garbled: second witness. |

**Flagged, not changed.** One row already on main sits on an entry that ends before the text was
written: the Compiegne history (posthumous, 1836) on the ancien-regime church (to 1815). The row carries
a census story, so it stays, and this batch adds the long-nineteenth-century shelf beside it. Moving it
is the census owner's call. The Port-Royal acts, printed in 1724, were written in the 1660s, inside
their entry's window.

## Later — queued

- ME-21 by a browser; Lang 1834 and the Peking mission after 1808; the
  Brosset Additions (1851) and part II (1856-57); the 1860 Concordat in a period printing.
- **Living traditions with no entry after a date** (Open-Gaps 158): 79 gaps, worked by era. Batches 3 and 4
  took 24; next are the St Thomas Christians, the Kongo church, Japan and China, then the Protestant gaps.
- **Families the tree doesn't reach** (Open-Gaps 159): the Patriarchate of Alexandria, Cyprus, the
  Polish, Czech-Slovak and Macedonian churches, and the Eastern Catholic churches never named.
- **Living marks graded none** (Open-Gaps 162): Kongo, Transylvania, the Schwenkfelders, New France.
  These want dated own-voice items after 2010. That is mostly the web, not public-domain print.
- **The loci pass** for multi-work volumes.
