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
| Ukrainian Orthodoxy, 1700 to today | filled to the 1770s, `needs-ruling` | `arkhiv-iugo-zapadnoi-rossii_ch1-t2-pravoslavie-v-zapadnoi-ukraine-xviii-rus_1864.txt`; `kiev-academy_akty-i-dokumenty-t1-ch2-1721-1750-rus_petrov.txt` | `russian-church-nikon-to-holy-synod` (1652-1815), `needs-ruling` | The Orthodox clergy's letters of the 1760s and the Kyiv Academy's documents of 1721-1750. The Kyiv metropolis then lay inside the Russian Synodal church; whether Ukrainian Orthodoxy belongs on that entry is the tree's call. Nothing after 1918 was found in print before 1931. |

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
