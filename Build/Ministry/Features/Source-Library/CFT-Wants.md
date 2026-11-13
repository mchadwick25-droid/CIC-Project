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
| era 5 row 60 (Norbert of Xanten) | filled | `norbert-xanten_vita-b-and-sermons-in-pl170-lat_migne1894.txt` | canons-regular-victorine-school, tradition |
| era 5 row 66 (Hugh de Payens) | filled | `templars_la-regle-du-temple-fra-lat_curzon1886.txt`; `templars_die-urspruengliche-templerregel-lat-deu_1903.txt` | military-religious-orders-templars-hospitallers, tradition |
| era 5 row 77 (Thomas of Celano) | filled | `thomas-celano_vita-et-miracula-sancti-francisci-lat_d-alencon1906.txt`; `thomas-celano_lives-of-st-francis_howell1908.txt` | the-franciscan-movement, tradition |
| era 5 row 61 (Clare of Assisi) | filled | `clare-assisi_life-of-saint-clare-ascribed-to-thomas-of-celano_robinson1910.txt` | the-franciscan-movement, tradition |
| era 5 row 76 (Brother Leo) | filled | `leo-assisi_scripta-fratris-leonis-lat_lemmens1901.txt`; `speculum-perfectionis_speculum-perfectionis-lat_sabatier1898.txt` | the-franciscan-movement, tradition (needs-ruling); the-franciscan-movement, fraticelli-spiritual-franciscan-rigorists, franciscan-order-era-6, tradition (needs-ruling) |
| era 5 row 78 (Agnes of Prague) | filled | `agnes-prague_some-new-sources-for-the-life-of-blessed-agnes-of-bohemia_seton1915.txt` | the-franciscan-movement, context |
| era 5 row 81 (Gerard de Frachet) | filled | `gerard-de-frachet_vitae-fratrum-lat_reichert1896.txt`; `gerard-de-frachet_lives-of-the-brethren_conway1924.txt` | the-dominican-order, tradition |
| era 5 rows 79 (Jordan of Saxony) and 80 (Diana d'Andalo) | filled | `jordan-saxony_die-briefe-lat-deu_altaner1925.txt` | the-dominican-order, tradition |
| era 5 row 62 (Dominic de Guzman) | filled | `acta-sanctorum_augusti-tomus-1-lat_1750.txt` | the-dominican-order, tradition |
| era 5 row 97 (Humbert of Romans) | filled | `humbert-romans_opera-de-vita-regulari-v1-lat_berthier1888.txt`; `humbert-romans_opera-de-vita-regulari-v2-lat_berthier1889.txt` | the-dominican-order, tradition |
| era 5 row 63 (Thomas Aquinas) | filled | `thomas-aquinas_opera-omnia-t4-summa-theologiae-lat_leonine1888.txt`; `thomas-aquinas_opera-omnia-t5-summa-theologiae-lat_leonine1889.txt`; `thomas-aquinas_opera-omnia-t6-summa-theologiae-lat_leonine1891.txt`; `thomas-aquinas_opera-omnia-t7-summa-theologiae-lat_leonine1892.txt`; `thomas-aquinas_opera-omnia-t8-summa-theologiae-lat_leonine1895.txt`; `thomas-aquinas_opera-omnia-t9-summa-theologiae-lat_leonine1897.txt`; `thomas-aquinas_opera-omnia-t10-summa-theologiae-lat_leonine1899.txt`; `thomas-aquinas_opera-omnia-t11-summa-theologiae-lat_leonine1903.txt`; `thomas-aquinas_opera-omnia-t12-summa-theologiae-lat_leonine1906.txt`; `acta-sanctorum_martii-tomus-1-lat_1735.txt` | the-dominican-order, tradition; the-dominican-order, context |
| era 5 row 64 (Joachim of Fiore) | filled | `joachim-fiore_tractatus-super-quatuor-evangelia-lat_buonaiuti1930.txt`; `acta-sanctorum_maii-tomus-6-lat_1739.txt` | joachimite-current, tradition; joachimite-current, context (needs-ruling) |
| era 5 row 65 (Valdes of Lyon) | filled | `stephen-bourbon_anecdotes-historiques-lat_lecoy-de-la-marche1877.txt` | the-waldensians, context |
| era 5 rows 65 (Valdes of Lyon) and 83 (Rainerius Sacconi) | filled | `doellinger_beitraege-zur-sektengeschichte-des-mittelalters-v2-lat-deu_1890.txt` | the-waldensians, cathars-albigensians, context |
| era 5 row 83 (Rainerius Sacconi) | filled | `martene-durand_thesaurus-novus-anecdotorum-v5-lat_1717.txt` | cathars-albigensians, the-waldensians, context |
| era 5 row 82 (Salimbene de Adam) | filled | `salimbene_from-st-francis-to-dante_coulton1907.txt` | joachimite-current, the-franciscan-movement, tradition |
| era 5 row 74 (Marie d'Oignies) | filled | `acta-sanctorum_junii-tomus-5-lat_palme1867.txt` | the-beguines, context |
| era 5 row 75 (Marguerite Porete) | filled | `porete_marguerite-in-revue-historique-54-fra_langlois1894.txt`; `porete_mirror-of-simple-souls_kirchberger1927.txt` | free-spirit-heresy, the-beguines, context; free-spirit-heresy, the-beguines, tradition |
| era 5 rows 56 (Sava of Serbia) and 92 (Domentijan and Teodosije) | filled | `domentijan_zivot-svetoga-simeuna-i-svetoga-save-chu_danicic1865.txt` | serbian-and-bulgarian-medieval-monasticism, tradition |
| era 5 rows 88 (Anna Komnene) and 89 (Basil the Physician) | filled | `anna-komnene_alexias-grc_reifferscheid1884.txt` | balkan-bogomil-continuation, byzantine-church-after-1054, context |
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
