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
| era 1 row 1 (Mani) | filled with later own texts and two outside witnesses | `manichaean-texts_tuerkische-manichaica-aus-chotscho-1-in-abhandlungen-preuss-akademie-1911-deu-oui_le-coq1911.txt`; `manichaean-texts_traite-manicheen-retrouve-en-chine-pt1-in-journal-asiatique-10-18-fra_chavannes-pelliot1911.txt`; `manichaean-texts_traite-manicheen-retrouve-en-chine-pt2-in-journal-asiatique-11-1-fra_chavannes-pelliot1913.txt`; `manichaean-texts_dr-steins-turkish-khuastuanift-in-jras-1911_le-coq1911.txt`; `mani_mani-seine-lehre-und-seine-schriften-fihrist-deu-ara_fluegel1862.txt`; `biruni_chronology-of-ancient-nations_sachau1879.txt` | manichaeism: the Manichaean texts `needs-ruling` (the manuscripts are later than the window); the Fihrist and al-Biruni context. The Cologne Codex, the Kephalaia and the Psalm-Book are in copyright. Müller's Turfan fragments (1904) were not found. |
| era 1 row 2 (Melito of Sardis) | not found | — | The Peri Pascha was first printed in 1940, so no public-domain edition exists. The old fragments are held (Otto 1872, Routh 1846). |
| era 1 row 3 (Ptolemy the Valentinian) | filled | `epiphanius_ancoratus-panarion-haer-1-33-gcs-bd1-grc_holl1915.txt` | valentinian-and-other-gnostic-christianities, tradition (the Letter to Flora) |
| era 1 row 4 (Paul of Samosata) | filled | `paul-samosata_paulus-von-samosata-fragmente-tu44-5-deu-grc_loofs1924.txt`; `paul-samosata_paul-de-samosate-etude-historique-fra-grc_bardy1923.txt` | antiochene-church-third-century, `needs-ruling` (which fragments are his is disputed) |
| era 2 row 5 (Maron) | filled | `theodoret_opera-omnia-t3-historia-religiosa-pg82-grc-lat_migne1864.txt`; `nau_opuscules-maronites-pt1-syr-fra_1899.txt`; `nau_opuscules-maronites-pt2-syr-fra_1900.txt`; `naironus_dissertatio-de-origine-nomine-ac-religione-maronitarum-lat_1679.txt` | Theodoret's Historia religiosa on the Antiochene entry, tradition; its chapter on Maron on maronite-christianity, antecedent; Nau `needs-ruling`; Naironus none yet (no Maronite entry covers 1679). Held already: Duwayhi's history in Arabic. |
| era 2 row 6 (Gregory the Illuminator) | filled | `langlois_collection-historiens-armenie-tomes1-2-fra_1867-1869.txt`; `agathangelos_agathangelus-und-die-akten-gregors-von-armenien-grc-deu_lagarde1887.txt` | armenian-christianity-conversion-era, `needs-ruling` (Agathangelos is usually dated after 451) |
| era 2 row 7 (Ezana of Aksum) | filled | `ezana_deutsche-aksum-expedition-bd4-inschriften-deu-gez-grc_littmann1913.txt`; `budge_history-of-ethiopia-nubia-and-abyssinia-v1_1928.txt` | aksumite-christianity, antecedent (the inscriptions are of the fourth century) |
| era 3 row 8 (Iakob Tsurtaveli) | not found | — | No text of the Martyrdom of Shushanik before 1931 was found in a usable scan. The Armenian version (Venice 1853) is on archive.org with unreadable OCR; not taken. |
| era 3 rows 9, 10 (Vachagan III; Movses Daskhurantsi); council 4 (Aghuen) | filled in part | `movses-daskhurantsi_beitraege-zur-albanischen-geschichte-deu_manandian1897.txt` | church-of-caucasian-albania, tradition (the canons of Aghuen in German). The whole History was not found before 1931. |
| era 3 row 11 (Sabas) | filled in Latin, possibly a paraphrase | `cyril-scythopolis_vita-sabae-in-surius-vitae-sanctorum-v12-december-lat_1880.txt` | chalcedonian-monasticism-judean-desert-and-gaza, `needs-ruling`: the volume's heading says the Life may be Metaphrastes's reworking of Cyril. No readable Greek was found. |
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
| 14 John of Damascus, the Life by John of Jerusalem | filled | `john-damascus_opera-omnia-t1-with-vita-pg94-grc-lat_migne1860.txt` | his works on the Heraclian-iconoclast, iconophile and Melkite entries, tradition; the Life on the Melkite entry, `needs-ruling` (its date of writing is not given) |
| 15, 21 Anskar; Rimbert | filled | `rimbert_anskar-the-apostle-of-the-north_robinson1921.txt`; `rimbert_vita-anskarii-accedit-vita-rimberti-lat_waitz1884.txt` (the scan stops in ch. 23 of the Life of Rimbert) | `scandinavian-conversion-christianity`, tradition |
| 16 Theodore the Studite | filled | `theodore-studite_opera-omnia-pg99-grc-lat_migne1860.txt` | his works, tradition; Michael's Life, `needs-ruling` |
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
| 37, 38 Stephen the Younger; Nikephoros I | filled | `nikephoros-cp_opera-with-vita-stephani-iunioris-pg100-grc-lat_migne1860.txt` | Nikephoros's works, tradition; the Life of Stephen, `needs-ruling` |
| 39 Clement of Ohrid | filled | `theophylact-ohrid_opera-t4-with-vita-clementis-pg126-grc-lat_migne1864.txt`; the Latin Life in Ginzel | `cyrillo-methodian-slavic-christianity`, `needs-ruling`: the volume's Monitum disputes the Life's author and date |
| 40 Boris and Gleb | filled, chronicle only | `russian-primary-chronicle_cross1930.txt`; `russian-primary-chronicle_psrl-t1-lavrentevskaia-letopis-orv_1926.txt` | `kievan-rus-christianity`, context. The separate Tale (Abramovich 1916) was not found. |
| 41 Ilarion | filled | `ilarion-kiev_slovo-o-zakone-i-blagodati-chu-rus_gorskii1844.txt` | `kievan-rus-christianity`, tradition |
| 42-45 the Paulicians; Peter of Sicily | filled, hostile witnesses | `peter-of-sicily_historia-manichaeorum-seu-paulicianorum-grc-lat_gieseler1846.txt`; `theophanes-continuatus_historiae-byzantinae-scriptores-post-theophanem-pg109-grc-lat_migne1863.txt` | `paulicians`, context; Peter also on the Macedonian entry as tradition. Peter the Higumen was not found. |
| 46 Michael Keroularios | filled | `will_acta-et-scripta-de-controversiis-ecclesiae-graecae-et-latinae-saec-xi-grc-lat_1861.txt`; `psellos_chronographia-and-orations-in-mesaionike-bibliotheke-v4-grc_sathas1874.txt` | Will on the Macedonian and Gregorian entries, tradition; Psellos context |
| 47 Nicholas I Mystikos | filled | `nicholas-mystikos_epistolae-with-eutychius-alexandrinus-pg111-grc-lat_migne1863.txt`; `vita-euthymii-patriarchae_anecdoton-zur-geschichte-leos-des-weisen-grc-deu_de-boor1888.txt` | the Macedonian entry: the letters as tradition, the Vita Euthymii `needs-ruling` |
| 48 Theophanes the Confessor | filled | `theophanes-confessor_chronographia-pg108-grc-lat_migne1863.txt` | the Heraclian-iconoclast entry, tradition |
| 49 Stepanos of Taron | filled | `stepanos-taron_armenische-geschichte-deu_gelzer-burckhardt1907.txt`; `stepanos-taron_histoire-universelle-deuxieme-partie-fra_macler1917.txt` (book III) | `bagratid-armenian-christianity`, tradition |
| 50 Theodore Abu Qurrah | filled | `theodore-abu-qurrah_opuscula-with-andrew-crete-malalas-pg97-grc-lat_migne1860.txt`; `theodore-abu-qurrah_arabischen-schriften-deu_graf1910.txt` | `melkite-arabic-christianity`, tradition |
| 51 Stephen Mansur | filled in Latin | `acta-sanctorum_martii-tomus-3-lat-grc_palme1865.txt` | the same, tradition. The Greek (Papadopoulos-Kerameus 1907) was not found. |
| 52 Grigol Khandzteli; Giorgi Merchule | filled in Latin | `peeters_histoires-monastiques-georgiennes-in-analecta-bollandiana-36-37-lat-fra_1917-1919.txt` | `georgian-revival-tao-klarjeti`, tradition |
| 53 John the Iberian and John Tornike; Euthymius | filled in Latin | the same | Tao-Klarjeti and the Georgian golden age, `needs-ruling` |
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
| era 5 rows 58 (Robert of Molesme) and 96 (Stephen Harding) | filled | `stephen-harding_charta-caritatis-and-exordium-in-pl166-lat_migne1894.txt` | cistercian-monasticism, tradition (needs-ruling) |
| era 5 row 59 (Bruno of Cologne) | filled | `le-couteulx_annales-ordinis-cartusiensis-v1-lat_1887.txt`; `bruno-cologne_opera-omnia-with-acta-pl152-lat_migne1879.txt` | carthusian-life, tradition; carthusian-life, context; carthusian-life, tradition (needs-ruling) |
| era 5 row 69 (Aelred of Rievaulx) | filled | `aelred-rievaulx_opera-pl195-lat_migne1855.txt` | cistercian-monasticism, tradition |
| era 5 rows 71 (Hugh of Lincoln) and 72 (Adam of Eynsham) | filled | `adam-eynsham_magna-vita-sancti-hugonis-lat_dimock1864.txt` | carthusian-life, tradition |
| era 5 row 60 (Norbert of Xanten) | filled | `norbert-xanten_vita-b-and-sermons-in-pl170-lat_migne1894.txt` | canons-regular-victorine-school, tradition (needs-ruling) |
| era 5 row 66 (Hugh de Payens) | filled | `templars_la-regle-du-temple-fra-lat_curzon1886.txt`; `templars_die-urspruengliche-templerregel-lat-deu_schnuerer1903.txt` | military-religious-orders-templars-hospitallers, tradition |
| era 5 row 77 (Thomas of Celano) | filled | `thomas-celano_vita-et-miracula-sancti-francisci-lat_d-alencon1906.txt`; `thomas-celano_lives-of-st-francis_howell1908.txt` | the-franciscan-movement, tradition |
| era 5 row 61 (Clare of Assisi) | filled | `clare-assisi_life-of-saint-clare-ascribed-to-thomas-of-celano_robinson1910.txt` | the-franciscan-movement, tradition |
| era 5 row 76 (Brother Leo) | filled | `leo-assisi_scripta-fratris-leonis-lat_lemmens1901.txt`; `speculum-perfectionis_speculum-perfectionis-lat_sabatier1898.txt` | the-franciscan-movement, tradition (needs-ruling); the-franciscan-movement, fraticelli-spiritual-franciscan-rigorists, franciscan-order-era-6, tradition (needs-ruling) |
| era 5 row 78 (Agnes of Prague) | filled | `agnes-prague_some-new-sources-for-the-life-of-blessed-agnes-of-bohemia_seton1915.txt` | the-franciscan-movement, context (needs-ruling) |
| era 5 row 81 (Gerard de Frachet) | filled | `gerard-de-frachet_vitae-fratrum-lat_reichert1896.txt`; `gerard-de-frachet_lives-of-the-brethren_conway1924.txt` | the-dominican-order, tradition |
| era 5 rows 79 (Jordan of Saxony) and 80 (Diana d'Andalo) | filled | `jordan-saxony_die-briefe-lat-deu_altaner1925.txt` | the-dominican-order, tradition |
| era 5 row 62 (Dominic de Guzman) | filled | `acta-sanctorum_augusti-tomus-1-lat_1750.txt` | the-dominican-order, tradition |
| era 5 row 97 (Humbert of Romans) | filled | `humbert-romans_opera-de-vita-regulari-v1-lat_berthier1888.txt`; `humbert-romans_opera-de-vita-regulari-v2-lat_berthier1889.txt` | the-dominican-order, tradition |
| era 5 row 63 (Thomas Aquinas) | filled | `thomas-aquinas_opera-omnia-t4-summa-theologiae-lat_leonine1888.txt`; `thomas-aquinas_opera-omnia-t5-summa-theologiae-lat_leonine1889.txt`; `thomas-aquinas_opera-omnia-t6-summa-theologiae-lat_leonine1891.txt`; `thomas-aquinas_opera-omnia-t7-summa-theologiae-lat_leonine1892.txt`; `thomas-aquinas_opera-omnia-t8-summa-theologiae-lat_leonine1895.txt`; `thomas-aquinas_opera-omnia-t9-summa-theologiae-lat_leonine1897.txt`; `thomas-aquinas_opera-omnia-t10-summa-theologiae-lat_leonine1899.txt`; `thomas-aquinas_opera-omnia-t11-summa-theologiae-lat_leonine1903.txt`; `thomas-aquinas_opera-omnia-t12-summa-theologiae-lat_leonine1906.txt`; `acta-sanctorum_martii-tomus-1-lat_1735.txt` | the-dominican-order, tradition; the-dominican-order, context |
| era 5 row 64 (Joachim of Fiore) | filled | `joachim-fiore_tractatus-super-quatuor-evangelia-lat_buonaiuti1930.txt`; `acta-sanctorum_maii-tomus-6-lat_1739.txt` | joachimite-current, tradition (needs-ruling); joachimite-current, context (needs-ruling) |
| era 5 row 65 (Valdes of Lyon) | filled | `stephen-bourbon_anecdotes-historiques-lat_lecoy-de-la-marche1877.txt` | the-waldensians, context |
| era 5 rows 65 (Valdes of Lyon) and 83 (Rainerius Sacconi) | filled | `doellinger_beitraege-zur-sektengeschichte-des-mittelalters-v2-lat-deu_1890.txt` | the-waldensians, cathars-albigensians, context |
| era 5 row 83 (Rainerius Sacconi) | filled | `martene-durand_thesaurus-novus-anecdotorum-v5-lat_1717.txt` | cathars-albigensians, the-waldensians, context |
| era 5 row 82 (Salimbene de Adam) | filled | `salimbene_from-st-francis-to-dante_coulton1907.txt` | joachimite-current, the-franciscan-movement, tradition |
| era 5 row 74 (Marie d'Oignies) | filled | `acta-sanctorum_junii-tomus-5-lat_palme1867.txt` | the-beguines, context |
| era 5 row 75 (Marguerite Porete) | filled | `porete_marguerite-in-revue-historique-54-fra_langlois1894.txt`; `mirror-of-simple-souls_english-version-kirchberger1927.txt` | free-spirit-heresy, the-beguines, context; free-spirit-heresy, the-beguines, tradition (needs-ruling) |
| era 5 rows 56 (Sava of Serbia) and 92 (Domentijan and Teodosije) | filled | `domentijan_zivot-svetoga-simeuna-i-svetoga-save-chu_danicic1865.txt` | serbian-and-bulgarian-medieval-monasticism, tradition |
| era 5 rows 88 (Anna Komnene) and 89 (Basil the Physician) | filled | `anna-komnene_alexias-grc_reifferscheid1884.txt` | balkan-bogomil-continuation, context |
| era 5 row 89 (Basil the Physician) | filled | `euthymios-zigabenos_narratio-de-bogomilis-grc-lat_gieseler1842.txt` | balkan-bogomil-continuation, context |
| era 5 row 91 (Gregory Pakourianos) | filled | `pakourianos_typikon-in-commentationes-philologae-ienenses-4-grc-lat_mousaios1890.txt` | the-georgian-golden-age, tradition (needs-ruling) |
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
| Open-Gaps 266: Ignatius the Deacon's Life of Tarasius, who presided at Nicaea II | filled | `ignatius-deacon_vita-tarasii-in-germanus-tarasius-pg98-grc-lat_migne1860.txt` (1860) | byzantine-imperial-church-heraclian-iconoclast, tradition (needs-ruling) |
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
| Wanted Sources era 5 row 58 (Robert of Molesme): his Life and letters | filled | `robert-molesme_vita-et-epistolae-in-pl157-lat_migne1899.txt` (1899) | cistercian-monasticism, tradition (needs-ruling) |
| Wanted Sources era 5 row 58 (Robert of Molesme); Open-Gaps 267: Raymond of Capua's full Legenda of Catherine of Siena | filled | `acta-sanctorum_aprilis-tomus-3-lat_palme1866.txt` (1866) | cistercian-monasticism, tradition (needs-ruling); latin-papal-church-avignon-to-lateran-v, tradition (needs-ruling) |
| Wanted Sources era 5 row 61 (Clare of Assisi): the four letters to Agnes of Prague in a readable print | filled | `acta-sanctorum_martii-tomus-1-lat_palme1865.txt` (1865) | the-franciscan-movement, tradition (needs-ruling) |
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
| era 6 row 105, Raymond of Capua: his Life of Catherine of Siena | filled (eras 4-5 batch) | `acta-sanctorum_aprilis-tomus-3-lat_palme1866.txt` (1866) | latin-papal-church-avignon-to-lateran-v, tradition (needs-ruling) |
| era 6 row 106, John of Capistrano: the Life by Nicholas of Fara | filled | `acta-sanctorum_octobris-tomus-10-lat_bruxelles1861.txt` (1861) | observant-reform-and-popular-preaching, tradition |
| era 6 row 107, Euthymius of Tarnovo: his own Life of Hilarion of Moglena | filled | `euthymius-tarnovo_werke-des-patriarchen-von-bulgarien-chu-deu_kaluzniacki1901.txt` (1901) | serbian-and-bulgarian-medieval-monasticism, tradition (needs-ruling) |
| era 6 row 107, Euthymius of Tarnovo: Gregory Tsamblak's Praise | held for Mark | — | The only scan is the Variorum reprint of 1971 of Kałużniacki's 1901 edition. |
| era 6 row 108, Teodosij of Trnovo: the Life by Kallistos | not found | — | Zlatarski (1904) and Bodianskii (1860) are not on archive.org. |
| era 6 row 109, Stephen of Perm: the Life by Epiphanius the Wise | not found | — | Druzhinin (1897) and Kushelev-Bezborodko (1862) are not on archive.org; two retellings of 1896 not taken. |
| era 6 row 110, Kirill of Beloozero: his own letters and testament | filled | `akty-istoricheskie_t1-1334-1598-rus_arkheograficheskaia-kommissiia1841.txt` (1841) | muscovite-monastic-christianity, tradition |
| era 6 row 110, Kirill of Beloozero: the Life by Pachomius | not found | — | Yablonskii (1908) and Nikolskii are not on archive.org. |
| era 6 row 111, Zosima and Savvatii of Solovki: their Lives | not found | — | Only a retelling of 1897 and descriptions of the monastery; not taken. |
| era 6 row 112, Estifanos of Gwendagwende: his Acts | none found before 1931 | — | The court's account of the revolt is in the held Perruchon volume, at about file line 6720. |
| outside-witness row 5, Rashid al-Din | not found | — | Quatremère (1836) is not on archive.org; the Persian scans cannot be read. |
| outside-witness row 6, Ibn Battuta: the Travels in Arabic with French | filled | `ibn-battuta_voyages-v1-ara-fra_defremery-sanguinetti1853.txt` (1853) | byzantine-church-palaiologan, st-thomas-christians-1300-1517, context (needs-ruling) |
| outside-witness row 6, Ibn Battuta: the Travels in Arabic with French | filled | `ibn-battuta_voyages-v2-ara-fra_defremery-sanguinetti1854.txt` (1854) | byzantine-church-palaiologan, st-thomas-christians-1300-1517, context (needs-ruling) |
| outside-witness row 6, Ibn Battuta: the Travels in Arabic with French | filled | `ibn-battuta_voyages-v3-ara-fra_defremery-sanguinetti1855.txt` (1855) | byzantine-church-palaiologan, st-thomas-christians-1300-1517, context (needs-ruling) |
| outside-witness row 6, Ibn Battuta: the Travels in Arabic with French | filled | `ibn-battuta_voyages-v4-ara-fra_defremery-sanguinetti1858.txt` (1858) | byzantine-church-palaiologan, st-thomas-christians-1300-1517, context (needs-ruling) |
| outside-witness row 7, Ibn Khaldun: the Prolegomena in French | filled | `ibn-khaldun_prolegomenes-pt1-fra_de-slane1863.txt` (1863) | coptic-christianity-fatimid-to-mamluk, context (needs-ruling) |
| outside-witness row 7, Ibn Khaldun: the Prolegomena in French | filled | `ibn-khaldun_prolegomenes-pt2-fra_de-slane1865.txt` (1865) | coptic-christianity-fatimid-to-mamluk, context (needs-ruling) |
| outside-witness row 7, Ibn Khaldun: the Prolegomena in French | filled | `ibn-khaldun_prolegomenes-pt3-fra_de-slane1868.txt` (1868) | coptic-christianity-fatimid-to-mamluk, context (needs-ruling) |
| outside-witness row 7, Ibn Khaldun: the history of the Berbers in French | filled | `ibn-khaldun_histoire-des-berberes-v1-fra_de-slane1852.txt` (1852) | coptic-christianity-fatimid-to-mamluk, context (needs-ruling) |
| outside-witness row 7, Ibn Khaldun: the history of the Berbers in French | filled | `ibn-khaldun_histoire-des-berberes-v2-fra_de-slane1854.txt` (1854) | coptic-christianity-fatimid-to-mamluk, context (needs-ruling) |
| outside-witness row 7, Ibn Khaldun: the history of the Berbers in French | filled | `ibn-khaldun_histoire-des-berberes-v3-fra_de-slane1856.txt` (1856) | coptic-christianity-fatimid-to-mamluk, context (needs-ruling) |
| outside-witness row 7, Ibn Khaldun: the history of the Berbers in French | filled | `ibn-khaldun_histoire-des-berberes-v4-fra_de-slane1856.txt` (1856) | coptic-christianity-fatimid-to-mamluk, context (needs-ruling) |
| outside-witness row 8, Abu'l-Fida | held already | `rhc-historiens-orientaux_t1-fra_academie1872.txt` | A French summary from his Annals, about file lines 6059-23098, and his autobiography, about 23101-24592. Reiske's five Latin volumes (1789-94) are located, not taken. |
| outside-witness row 9, al-Qalqashandi: on Egypt | filled | `qalqashandi_geographie-und-verwaltung-von-aegypten-deu_wuestenfeld1879.txt` (1879) | coptic-christianity-fatimid-to-mamluk, context (needs-ruling) |
| outside-witness row 9, al-Qalqashandi: on Syria | filled | `qalqashandi_la-syrie-a-l-epoque-des-mamelouks-fra_gaudefroy-demombynes1923.txt` (1923) | coptic-christianity-fatimid-to-mamluk, context (needs-ruling) |
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
| era 7 row 113, Katharina Schütz Zell: her letter to the citizens of Strasbourg and her answer to Rabus (1557) | filled | `fuesslin_beytraege-kirchen-reformations-geschichten-schweitzerland-theil-5-deu_1753.txt` (1753) | lutheran-wittenberg-and-its-congregations, tradition (needs-ruling) |
| era 7 row 113, Katharina Schütz Zell: a Life with extracts from her letters and her hymn-book preface | filled | `roehrich_mittheilungen-geschichte-evangelischen-kirche-des-elsasses-bd-3-deu_1855.txt` (1855) | lutheran-wittenberg-and-its-congregations, context (needs-ruling) |
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
| outside-witness row 10, Kâtib Çelebi | filled in part | `katib-celebi_history-of-the-maritime-wars-of-the-turks-chapters-1-4_mitchell1831.txt` (1831) | orthodoxy-under-the-ottomans-parish-millet-and-n, context (needs-ruling) Chapters I-IV; no more was translated. |
| outside-witness row 11, Evliya Çelebi: the Travels in English | filled | `evliya-celebi_narrative-of-travels-v1-pt1_hammer1834.txt` (1834) | orthodoxy-under-the-ottomans-parish-millet-and-n, context (needs-ruling) |
| outside-witness row 11, Evliya Çelebi: the Travels in English | filled | `evliya-celebi_narrative-of-travels-v1-pt2_hammer1846.txt` (1846) | orthodoxy-under-the-ottomans-parish-millet-and-n, context (needs-ruling) |
| outside-witness row 11, Evliya Çelebi: the Travels in English | filled | `evliya-celebi_narrative-of-travels-v2_hammer1850.txt` (1850) | orthodoxy-under-the-ottomans-parish-millet-and-n, context (needs-ruling) |
| outside-witness rows 12-14, Peçevi, Mustafa Ali, Selaniki | not found | — | No translation printed by 1930 was found; the Ottoman-script printing of Peçevi (1866) cannot be read in the OCR and was not taken. |
| outside-witness row 15, Joseph ha-Kohen: Divrei ha-Yamim in English | filled | `joseph-ha-kohen_chronicles-of-rabbi-joseph-ben-joshua-ben-meir-v1_bialloblotzky1835.txt` (1835) | the-tridentine-church, context (needs-ruling) |
| outside-witness row 15, Joseph ha-Kohen: Divrei ha-Yamim in English | filled | `joseph-ha-kohen_chronicles-of-rabbi-joseph-ben-joshua-ben-meir-v2_bialloblotzky1836.txt` (1836) | the-tridentine-church, context (needs-ruling) |
| outside-witness row 15, Joseph ha-Kohen: Emek ha-Bakha in French | filled | `joseph-ha-kohen_la-vallee-des-pleurs-emek-ha-bakha-fra_see1881.txt` (1881) | the-tridentine-church, context (needs-ruling) |
| outside-witness row 16, Samuel Usque: the Consolaçam | filled | `usque_consolacam-as-tribulacoens-de-israel-por_mendes-dos-remedios1906.txt` (1906) | the-tridentine-church, context (needs-ruling) |
| outside-witness rows 17-18, Gedaliah ibn Yahya; David Gans | not found | — | No scan under any spelling tried. |
| outside-witness row 19, Solomon ibn Verga: Shevet Yehudah in Latin | filled | `ibn-verga_historia-judaica-shevet-yehudah-lat_gentius1651.txt` (1651) | the-tridentine-church, context (needs-ruling) |
| outside-witness row 20, Jacques-Auguste de Thou | located | — | The Latin of 1733 (seven volumes) and the French of 1734 (sixteen) are on archive.org in part; not taken for their length. His De vita sua (1621) has poor OCR and no title page in the scan; not taken. |
| outside-witness row 21, Guicciardini: the Storia d'Italia | filled | `guicciardini_la-storia-d-italia-v1-ita_gherardi1919.txt` (1919) | the-tridentine-church, latin-papal-church-avignon-to-lateran-v, context (needs-ruling) |
| outside-witness row 21, Guicciardini: the Storia d'Italia | filled | `guicciardini_la-storia-d-italia-v2-ita_gherardi1919.txt` (1919) | the-tridentine-church, latin-papal-church-avignon-to-lateran-v, context (needs-ruling) |
| outside-witness row 21, Guicciardini: the Storia d'Italia | filled | `guicciardini_la-storia-d-italia-v3-ita_gherardi1919.txt` (1919) | the-tridentine-church, latin-papal-church-avignon-to-lateran-v, context (needs-ruling) |
| outside-witness row 21, Guicciardini: the Storia d'Italia | filled | `guicciardini_la-storia-d-italia-v4-ita_gherardi1919.txt` (1919) | the-tridentine-church, latin-papal-church-avignon-to-lateran-v, context (needs-ruling) |
| outside-witness row 22, Machiavelli: his writings in English | filled | `machiavelli_historical-political-and-diplomatic-writings-v1_detmold1882.txt` (1882) | latin-papal-church-avignon-to-lateran-v, the-tridentine-church, context (needs-ruling) |
| outside-witness row 22, Machiavelli: his writings in English | filled | `machiavelli_historical-political-and-diplomatic-writings-v2_detmold1882.txt` (1882) | latin-papal-church-avignon-to-lateran-v, the-tridentine-church, context (needs-ruling) |
| outside-witness row 22, Machiavelli: his writings in English | filled | `machiavelli_historical-political-and-diplomatic-writings-v3_detmold1882.txt` (1882) | latin-papal-church-avignon-to-lateran-v, the-tridentine-church, context (needs-ruling) |
| outside-witness row 22, Machiavelli: his writings in English | filled | `machiavelli_historical-political-and-diplomatic-writings-v4_detmold1882.txt` (1882) | latin-papal-church-avignon-to-lateran-v, the-tridentine-church, context (needs-ruling) |
| outside-witness row 23, Jean Bodin: the Six Books in English | filled | `bodin_six-bookes-of-a-commonweale_knolles1606.txt` (1606) | the-huguenots, context (needs-ruling) |
| outside-witness row 23, Jean Bodin: the Colloquium heptaplomeres | filled | `bodin_colloquium-heptaplomeres-lat_noack1857.txt` (1857) | the-huguenots, context (needs-ruling) |
| outside-witness row 24, Montaigne: the Essays in Florio's English | filled | `montaigne_essays-v1_florio-saintsbury1892.txt` (1892) | the-huguenots, context (needs-ruling) |
| outside-witness row 24, Montaigne: the Essays in Florio's English | filled | `montaigne_essays-v2_florio-saintsbury1893.txt` (1893) | the-huguenots, context (needs-ruling) |
| outside-witness row 24, Montaigne: the Essays in Florio's English | filled | `montaigne_essays-v3_florio-saintsbury1893.txt` (1893) | the-huguenots, context (needs-ruling) |
| outside-witness row 25, Vasari | located | — | Foster's English (1850-52, five volumes) and de Vere's (1912-15, ten) are on archive.org in part; not taken for their length. |
| outside-witness row 26, Leo Africanus | filled | `leo-africanus_history-and-description-of-africa-v1_pory-brown1896.txt` (1896) | the-coptic-church-under-the-ottomans, context (needs-ruling) |
| outside-witness row 26, Leo Africanus | filled | `leo-africanus_history-and-description-of-africa-v2_pory-brown1896.txt` (1896) | the-coptic-church-under-the-ottomans, context (needs-ruling) |
| outside-witness row 26, Leo Africanus | filled | `leo-africanus_history-and-description-of-africa-v3_pory-brown1896.txt` (1896) | the-coptic-church-under-the-ottomans, context (needs-ruling) |
| outside-witness row 27, Busbecq: the Turkish Letters and the letters from France | filled | `busbecq_life-and-letters-v1_forster-daniell1881.txt` (1881) | orthodoxy-under-the-ottomans-parish-millet-and-n, context (needs-ruling) |
| outside-witness row 27, Busbecq: the Turkish Letters and the letters from France | filled | `busbecq_life-and-letters-v2_forster-daniell1881.txt` (1881) | the-huguenots, context (needs-ruling) |
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

Ninety-three files for the 63 person rows marked major in
`Build/Ministry/Operations/Audits/2026-11-12_wanted-sources-combined/Wanted_Sources.md` (rows 163-225). The search
record is `Build/Ministry/Operations/Audits/2026-11-15_library-era9/Search_Log.md`. Every file has a printed
imprint year of 1930 or earlier, read on its title page or, for sixteen volumes, on the scan's page image. The
rows not marked major (226-330), the era 9 outside witnesses, the council records and the held eras 8-9 items
are left for the next batches. One want was held already.

| want | state | file(s), with the imprint year | shelf |
|---|---|---|---|
| era 9 row 163, Barton W. Stone: his own Biography | filled | `stone_biography-of-elder-barton-warren-stone_rogers1847.txt` (1847); 146,459 words; eng | the-stone-campbell-restoration-movement, tradition |
| era 9 row 164, Alexander Campbell: a Life (Richardson, vol. 1) | filled | `richardson_memoirs-of-alexander-campbell-v1_1868.txt` (1868); 188,994 words; eng | the-stone-campbell-restoration-movement, context |
| era 9 row 164, Alexander Campbell: a Life (Richardson, vol. 2) | filled | `richardson_memoirs-of-alexander-campbell-v2_1870.txt` (1870); 221,572 words; eng | the-stone-campbell-restoration-movement, context |
| era 9 row 164, Alexander Campbell: one volume of the Christian Baptist | filled | `campbell_christian-baptist-v5_bethany1828.txt` (1828); 155,862 words; eng | the-stone-campbell-restoration-movement, tradition |
| era 9 row 165, Charles G. Finney: Lectures on Revivals of Religion | filled | `finney_lectures-on-revivals-of-religion_6th-ed1835.txt` (1835); 207,129 words; eng | the-second-great-awakening-and-camp-meeting-worl, tradition |
| era 9 row 165, Charles G. Finney: his Memoirs | filled | `finney_memoirs-of-rev-charles-g-finney_1876.txt` (1876); 176,972 words; eng | the-second-great-awakening-and-camp-meeting-worl, tradition (needs-ruling) |
| era 9 row 166, Phoebe Palmer: The Way of Holiness | filled | `palmer_way-of-holiness_1843.txt` (1843); 50,843 words; eng | the-holiness-movement, tradition |
| era 9 row 166, Phoebe Palmer: a Life with her letters | filled | `wheatley_life-and-letters-of-mrs-phoebe-palmer_1876.txt` (1876); 235,522 words; eng | the-holiness-movement, context |
| era 9 row 167, Dwight L. Moody: the Life by his son | filled | `moody-w-r_life-of-dwight-l-moody_1900.txt` (1900); 180,120 words; eng | the-sunday-school-and-bible-institute-movement, context |
| era 9 row 172, William Miller: his own Views of the Prophecies | filled | `miller_views-of-the-prophecies-and-prophetic-chronology_himes1842.txt` (1842); 90,391 words; eng | restorationist-apocalyptic-ferment-and-adventism, tradition |
| era 9 row 172, William Miller: a Life told by a disciple | filled | `bliss_memoirs-of-william-miller_1853.txt` (1853); 178,678 words; eng | restorationist-apocalyptic-ferment-and-adventism, context |
| era 9 row 173, Ellen G. White: Life Sketches | filled | `white_life-sketches-of-ellen-g-white_1915.txt` (1915); 140,745 words; eng | restorationist-apocalyptic-ferment-and-adventism, seventh-day-adventist-church-twentieth-century, tradition |
| era 9 row 215, Washington Gladden: Applied Christianity | filled | `gladden_applied-christianity_9th-ed1897.txt` (1897); 76,263 words; eng | the-social-gospel, tradition |
| era 9 row 216, Charles A. Briggs: his own defence at the trial | filled | `briggs_defence-before-the-presbytery-of-new-york_1893.txt` (1893); 87,020 words; eng | the-mainline-century-liberal-and-neo-orthodox, tradition (needs-ruling) |
| era 9 row 216, Charles A. Briggs: the trial record, part I | filled | `briggs-trial_case-against-professor-briggs-pt1_1892.txt` (1892); 56,636 words; eng | the-mainline-century-liberal-and-neo-orthodox, context (needs-ruling) |
| era 9 row 216, Charles A. Briggs: the trial record, part III | filled | `briggs-trial_case-against-professor-briggs-pt3_1893.txt` (1893); 107,259 words; eng | the-mainline-century-liberal-and-neo-orthodox, context (needs-ruling) |
| era 9 row 217, A. A. Hodge and B. B. Warfield: Inspiration, Presbyterian Review, April 1881 | filled | `presbyterian-review_v2-no6-april-1881-inspiration.txt` (1881); 108,871 words; eng | fundamentalism-1910-1970s, context (needs-ruling) |
| era 9 row 218, David Lipscomb: his own writing (the 1906 census letters were not found) | filled | `lipscomb_queries-and-answers_shepherd1910.txt` (1910); 211,569 words; eng | churches-of-christ-twentieth-century, tradition |
| era 9 row 219, Jerry McAuley: his life and his own account | filled | `offord_jerry-mcauley-his-life-and-work_2nd-ed1885.txt` (1885); 72,189 words; eng | the-rescue-mission-movement, context (needs-ruling) |
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
| era 9 row 180, John Humphrey Noyes: his religious experience, compiled from his writings | filled | `noyes_religious-experience-of-john-humphrey-noyes_gw-noyes1923.txt` (1923); 114,933 words; eng | oneida-community, tradition (needs-ruling) |
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
| era 9 row 179, Edward Irving: his collected writings, vol. 5 | filled | `irving_collected-writings-v5_carlyle1866.txt` (1866); 240,993 words; eng | catholic-apostolic-church-irvingites, tradition (needs-ruling) |
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
| era 9 row 214, Evan Roberts: a Life, in Welsh | filled | `phillips_evan-roberts-ai-waith-cym_1912.txt` (1912); 129,838 words; cym | the-1904-07-revival-family-wales-mukti-india-pyo, context (needs-ruling) |
| era 9 row 222, William Clowes: his Journals | filled | `clowes_journals-of-william-clowes_1844.txt` (1844); 115,023 words; eng | nineteenth-century-methodism, tradition |
| era 9 row 222, Hugh Bourne: a Life | filled | `antliff_life-of-the-venerable-hugh-bourne_1872.txt` (1872); 167,409 words; eng | nineteenth-century-methodism, context |
| era 9 row 193, Abraham Kuyper: a Dutch work of his own | filled | `kuyper_tractaat-van-de-reformatie-der-kerken-nld_1883.txt` (1883); 90,480 words; nld | dutch-neo-calvinism-secession-churches, tradition |
| era 9 row 194, Herman Bavinck: an English print of his own lectures | filled | `bavinck_philosophy-of-revelation_1909.txt` (1909); 110,728 words; eng | dutch-neo-calvinism-secession-churches, tradition (needs-ruling) |
| era 9 row 194, Herman Bavinck: his own summary of doctrine, in Dutch (not the Dogmatiek) | filled | `bavinck_magnalia-dei-nld_1909.txt` (1909); 276,477 words; nld | dutch-neo-calvinism-secession-churches, tradition (needs-ruling) |
| era 9 row 196, C. F. W. Walther: Der Lutheraner, the first year | filled | `walther_der-lutheraner-jg1-1844-1845-deu_st-louis1845.txt` (1844); 148,394 words; deu | confessional-lutheran-revival-emigrations, tradition |
| era 9 row 221, Adolf von Harnack: What Is Christianity?, in English | filled | `harnack_what-is-christianity_saunders1901.txt` (1901); 87,707 words; eng | the-mainline-century-liberal-and-neo-orthodox, tradition |
| era 9 row 221, Adolf von Harnack: Das Wesen des Christentums | filled | `harnack_das-wesen-des-christentums-deu_1900.txt` (1900); 66,516 words; deu | the-mainline-century-liberal-and-neo-orthodox, tradition |
| era 9 row 223, Theodor Fliedner: a Life, in English | filled | `fliedner-life_life-of-pastor-fliedner-of-kaiserswerth_winkworth1867.txt` (1867); 54,506 words; eng | the-reveil-and-inner-mission-awakening, context |
| era 9 row 223, the Fliedners: an English account of Kaiserswerth | filled | `kaiserswerth_institution-of-kaiserswerth-on-the-rhine_1851.txt` (1851); 8,938 words; eng | the-reveil-and-inner-mission-awakening, context |
| era 9 row 223, the Fliedners: Kaiserswerth's own jubilee memoir, in German | filled | `disselhoff_jubilate-denkschrift-kaiserswerth-deu_1886.txt` (1886); 188,677 words; deu | the-reveil-and-inner-mission-awakening, tradition (needs-ruling) |
| era 9 row 224, Hendrik de Cock: two of his first writings | filled | `cock_twee-der-eerste-geschriften-nld_1882.txt` (1882); 29,001 words; nld | dutch-neo-calvinism-secession-churches, tradition |
| era 9 row 225, Paul Petter Waldenstrom: a book of his in English | filled | `waldenstrom_blood-of-jesus_princell1888.txt` (1888); 17,269 words; eng | laestadianism-and-the-nordic-revivals, tradition |
| era 9 row 195, Ignaz von Dollinger: his declarations and letters on the Vatican decrees, in English | filled | `dollinger_declarations-and-letters-on-the-vatican-decrees-1869-1887_1891.txt` (1891); 42,789 words; eng | old-catholic-churches-union-of-utrecht, tradition |
| era 9 row 201, Cyril IV: a church history of Egypt before 1931 | filled | `butcher_story-of-the-church-of-egypt-v2_1897.txt` (1897); 144,216 words; eng | coptic-revival-under-cyril-iv, the-coptic-church-under-the-ottomans, context |
| era 9 row 200, Joseph Audo: the acts of the Vatican council | filled | `collectio-lacensis_t7-acta-et-decreta-concilii-vaticani-lat_1892.txt` (1892); 1,181,347 words; lat | catholic-church-long-nineteenth-century, tradition |
| era 9 row 202, Ioann Veniaminov: his Notes on the Unalaska islands, part 1 | filled | `veniaminov_zapiski-ob-ostrovakh-unalashkinskago-otdela-ch1-rus_1840.txt` (1840); 66,278 words; rus | alaskan-mission-herman-veniaminov, tradition |
| era 9 row 202, Ioann Veniaminov: his Notes on the Unalaska islands, part 2 | filled | `veniaminov_zapiski-ob-ostrovakh-unalashkinskago-otdela-ch2-rus_1840.txt` (1840); 78,182 words; rus | alaskan-mission-herman-veniaminov, tradition |
| era 9 row 202, Ioann Veniaminov: an English account before 1931 | filled | `hale_innocent-of-moscow-apostle-of-kamchatka-and-alaska_1888.txt` (1888); 8,743 words; eng | alaskan-mission-herman-veniaminov, context |
| era 9 row 198, Nikolai of Japan: a Russian account of the Japan mission | filled | `pravoslavie-v-iaponii_pravoslavie-v-iaponii-rus_1889.txt` (1889); 3,933 words; rus | russian-church-synodal-century, japanese-christianity-hidden-emergence-meiji, context |
| era 9 row 185, Hong Xiuquan: the kingdom's own printed books, in translation | filled | `medhurst_pamphlets-issued-by-the-chinese-insurgents-at-nan-king_1853.txt` (1853); 106,466 words; eng | taiping-heavenly-kingdom, tradition |
| era 9 row 185, Hong Xiuquan: an outside account | filled | `callery-yvan_history-of-the-insurrection-in-china_oxenford1854.txt` (1854); 88,299 words; eng | taiping-heavenly-kingdom, context |
| era 9 row 185, Hong Xiuquan: an account that quotes the record of his visions | filled | `lindley_ti-ping-tien-kwoh-v1_1866.txt` (1866); 156,700 words; eng | taiping-heavenly-kingdom, context (needs-ruling) |
| era 9 row 203, Samuel Ajayi Crowther: his journal of 1854 | filled | `crowther_journal-of-an-expedition-up-the-niger-and-tshadda_1855.txt` (1855); 68,238 words; eng | the-missionary-movement-s-native-churches-seramp, tradition |
| era 9 row 203, Samuel Ajayi Crowther: his journal of 1841 | filled | `schon-crowther_journals-of-the-niger-expedition-of-1841_1842.txt` (1842); 98,364 words; eng | the-missionary-movement-s-native-churches-seramp, tradition |
| era 9 row 203, Samuel Ajayi Crowther: a Life | filled | `page_black-bishop-samuel-adjai-crowther_1908.txt` (1908); 146,120 words; eng | the-missionary-movement-s-native-churches-seramp, context (needs-ruling) |
| era 9 row 204, J. Hudson Taylor: a Life (the early years) | filled | `taylor-howard_hudson-taylor-in-early-years_1912.txt` (1912); 206,805 words; eng | the-missionary-movement-s-native-churches-seramp, context (needs-ruling) |
| era 9 row 205, Xi Shengmo (Pastor Hsi): a Life (the early life) | filled | `taylor-howard_one-of-chinas-scholars-pastor-hsi_1909.txt` (1909); 169,725 words; eng | the-missionary-movement-s-native-churches-seramp, context |
| era 9 row 206, Ludwig Ingwer Nommensen: the obituary by J. Warneck | filled | `allgemeine-missions-zeitschrift_jg45-1918-deu_berlin1918.txt` (1918); 281,883 words; deu | indonesian-christianity-the-independent-century, context |
| era 9 row 209, Johann Ludwig Krapf: his Travels | filled | `krapf_travels-researches-and-missionary-labours-in-eastern-africa_1860.txt` (1860); 169,566 words; eng | east-african-christianity-uganda-martyrs, tradition |
| era 9 row 210, Charles Lwanga: a missionary's account of Uganda (it does not name him) | filled | `ashe_chronicles-of-uganda_1895.txt` (1895); 116,463 words; eng | east-african-christianity-uganda-martyrs, tradition |
| era 9 row 211, Tiyo Soga: a Life | filled | `chalmers_tiyo-soga-a-page-of-south-african-mission-work_1877.txt` (1877); 155,925 words; eng | southern-african-mission-churches, context |
| era 9 row 220, James Thomson: his Letters | filled | `thomson_letters-on-the-moral-and-religious-state-of-south-america_1827.txt` (1827); 76,816 words; eng | nineteenth-century-latin-american-catholicism, context |
| era 9 row 186, Antonio Conselheiro: a second witness in English | filled | `cunninghame-graham_brazilian-mystic-antonio-conselheiro_1920.txt` (1920); 68,385 words; eng | canudos-belo-monte, context (needs-ruling) |
| era 9 row 200, Joseph Audo: an English witness | held already | `badger_nestorians-and-their-rituals-v1_1852.txt`, `-v2_1852.txt` | — |
| era 9 row 181, John Nelson Darby: the Letters and the Collected Writings | not found | — | Only reprints of 1964 and 1974. Four smaller books of his own are located (1863-1900). |
| era 9 row 197, Ambrose of Optina: his letters and an early Life | not found | — | About twelve queries, in Cyrillic and in transliteration. |
| era 9 row 199, Mkrtich Khrimian: his writings | located, not vendored | — | Six Armenian printings (1877-1929); the OCR of the four sampled cannot be read. No English account before 1931. |
| era 9 row 207, Kiai Sadrach: Dutch mission reports | not found | — | archive.org only; dbnl.org not yet searched. |
| era 9 rows 212 and 213, Nehemiah Tile and Mangena Mokone | not found | — | Neither is named in the Native Affairs Commission report of 1903-05 or in five 1896 numbers of the Voice of Missions. Sundkler (1948) is out by date. |
| era 9 rows 186 and 187, Os Sertoes (3rd ed., 1905) | held for Mark | — | `004518-completo` on archive.org: clean OCR and a Public Domain Mark, but the Brasiliana USP notice in the file asks for non-commercial use and no republication without leave. |
| era 9 row 208, David Jones and David Griffiths: Ellis, History of Madagascar (1838) | not taken | — | Four scans; no title page prints a year (the preface is dated 10 October 1838). |
| era 9 row 192, Johann Hinrich Wichern: the Denkschrift | located, not vendored | — | Third edition, Hamburg 1889; the black-letter OCR cannot be read. The editions of 1849 were not found. |
| era 9 row 193, Abraham Kuyper: Calvinism, the Stone Lectures | not taken | — | Three scans; none prints a year. A Life before 1931 was not found. |
| era 9 row 194, Herman Bavinck: the Gereformeerde Dogmatiek | not found | — | The one item has no text on the host. |
| era 9 row 195, Ignaz von Dollinger: Friedrich's Life; the Briefe und Erklarungen in German | located, not vendored | — | Both are black letter with OCR that cannot be read. |
| era 9 row 196, C. F. W. Walther: the constitution of 1847 | located, not vendored | — | Printed in Der Lutheraner, the fourth year (`DerLutheraner04`); no separate print found. |
| era 9 row 173, Ellen G. White: Spiritual Gifts | not found before 1931 | — | A facsimile of 1945 and typed transcriptions only. |
| era 9 row 178, John Thomas: Eureka; a Life | not found | — | About eight queries. |
| era 9 row 183, George Muller: the Narrative, parts 1 to 3 | not found | — | Wayland's Life of Trust, which condenses the whole, prints no year and was not taken. |
| era 9 row 185, Hong Xiuquan: Hamberg, The Visions of Hung-Siu-tshuen (1854) | not found | — | Lindley (1866) quotes Hamberg's narrative at length. |
| era 9 row 191, Catherine Booth: Female Ministry (1859) | not found before 1931 | — | A reprint of 1975 only. The Life by Booth-Tucker prints no year and was not taken. |
| era 9 rows 204 and 205, Hudson Taylor, A Retrospect; Pastor Hsi, the full Life | not taken | — | No scan prints a year on its title page. |
| era 9 row 210, Charles Lwanga: a martyr account that names him | not taken | — | Walsh's book has a chapter on him but prints no year. |
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
  history that calls him "Cyril the Reformer". Row 206 (Nommensen) is an obituary inside a 1918 periodical
  volume. Row 210 (Lwanga): Ashe's Chronicles of Uganda does not name him. Row 222 (Bourne) is a Life of 1872.
  Row 223 (the Fliedners): none of the three files is in their own words.
- **Author not named on the title page.** Millennial Dawn, vol. 1 (the host names Russell); the Institution of
  Kaiserswerth, 1851 (the host names Florence Nightingale); the Life of Pastor Fliedner; the Russian pamphlet on
  Japan (the host names Makarov); Spurgeon's Autobiography (compiled by his wife and secretary, unnamed); the
  Memoir of Groves ("by his widow"); the two "Case against Professor Briggs" parts.
- **Later editions.** Finney's Lectures (sixth edition, 1835); Parker's Discourse (third, 1847) and Ten Sermons
  (second, 1861); Gladden (ninth, 1897); Hinton's Knibb (second, 1849); Groves's Memoir (third, 1859); Science
  and Health (161st, 1899, not the text of 1875); Tract 90 (second, 1841); Millennial Dawn (the title page reads
  1886; a library stamp reads 1906); One of China's Scholars (the printing of 1909).
- **Part of a larger work.** Vol. 1 only: Spurgeon's Autobiography, Liddon's Pusey, Coleridge's Keble, the
  Journal of Discourses, Home-Talks, the History of the Church, Lindley. Muller's Narrative is the
  fourth part only. Irving's Collected Writings is vol. 5 only. Butcher is vol. 2 only.
- **Mixed voices.** Stone's Biography holds his own account, the Apology of the Springfield Presbytery and
  Rogers's additions. The Apologia is bound with the Kingsley correspondence. The Journal of Discourses has many
  speakers. The Niger journals of 1842 give Schon first, then Crowther. The Presbyterian Review number holds
  other articles after "Inspiration". The Vatican council volume is about 1.17 million words; Audo is spelled
  "Audu" in it.
- **OCR.** Der Lutheraner (black letter) is fair at best. Veniaminov's Russian is fair, in the old spelling.
  Phillips's Welsh Life has a publisher's list before its title page.
- **Bavinck:** Magnalia Dei is not the Dogmatiek. **Lipscomb:** Queries and Answers (1910) is his own writing,
  not the census letters. **Gurney:** the 1824 title reads "Religious Peculiarities".

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
