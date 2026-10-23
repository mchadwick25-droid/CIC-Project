# Source Readiness Dossier — The Ruthenian Uniate Church — Zamość to the Partitions

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and why it
exists.

**Atlas ID:** VII.28
**Corpus-map slug:** `ruthenian-uniate-18th-century`
**Time window:** 1700-1815
**Region(s):** Ruthenia (Ukraine & Belarus), Austrian Galicia; census `regions`: North Europe
**Dossier author / date:** Claude, Library thread, Era VIII source-research pass, 2026-10-23
**Corpus-map / `cic/texts/` state as of:** branch `library/era-viii-2026-10`, this pass.

## 1. Already assigned

9 works across 8 vendored files in `cic/corpus-map/ruthenian-uniate-18th-century.yaml`.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Apollogia, że Rusi Unitom nie godzi się odstępować od swojego Obrządku ([1772]) | anonymous-uniate | tradition | assigned | whole work | `anonymous-uniate_apollogia-rusi-unitom-obrzadek-pol_1772.txt` |
| Codex Constitutionum Ordinis S. Basilii M. (1791) | basilian-order | tradition | assigned | whole work | `basilian-order_codex-constitutionum-ordinis-s-basilii-lat_1791.txt` |
| Brevis notitia fundationis Theodori Koriathovits, Part I (1799) | basilovits | tradition | needs-ruling | whole work | `basilovits_brevis-notitia-fundationis-koriathovits-pars1-lat_1799.txt` |
| Annales Ecclesiae Ruthenae (history of the Ruthenian Greek Catholic church, with documents) | harasiewicz | context | provisional | the author's index at about file lines 775-860 lists the Synod of Brest documents (775, 784, 798, 842, 860)... | `harasiewicz_annales-ecclesiae-ruthenae-lat_1862.txt` |
| Synodus provincialis Ruthenorum (1720), papal confirmation and Propaganda's decrees | mansi | context | assigned | the approbation by Benedict XIII and the Roman decrees printed with the synod (columns 1439-1441, 1469) | `mansi_sacrorum-conciliorum-collectio-tomus-35-1414-1724-lat_welter-facsimile1902.txt` |
| Synodus provincialis Ruthenorum habita in civitate Zamosciae anno 1720 (acts, decrees, professions of faith, Metropolitan Kiszka's letters) | mansi | tradition | assigned | columns 1437-1538 (from about file line 133890 to Mansi's monitum near line 143600) | `mansi_sacrorum-conciliorum-collectio-tomus-35-1414-1724-lat_welter-facsimile1902.txt` |
| Geschichte der Union der ruthenischen Kirche mit Rom, Vol. 2 (1596-1879) | pelesz | context | provisional | Vorrede at the head; Erstes Capitel (the restored union, 1596) at about file line 1157; Zweites Capitel at ... | `pelesz_geschichte-der-union-bd2-deu_1880.txt` |
| Vetera monumenta Poloniae et Lithuaniae, vol. IV: the documents on the Ruthenian Uniate church and the Basilians | theiner | context | assigned | the documents addressed to the Ruthenian metropolitans and bishops (for example the letter on the restored ... | `theiner_vetera-monumenta-poloniae-lithuaniae-v4-lat_1864.txt` |
| Katechizm albo Krótkie zebranie Nauki Chrześciańskiey (1792), with the bishop's pastoral letter | wazynski | tradition | assigned | whole work | `wazynski_katechizm-albo-krotkie-zebranie-nauki-chrzescianskiey-pol_1792.txt` |

## 2. Cross-link opportunities

| file | locus | why | suggested role / confidence |
|---|---|---|---|
| pelesz_geschichte-der-union-bd2-deu_1880.txt | the eighteenth-century chapters (Catherine II, the partitions; from about file line 28000) | Already in the bucket; the brief says cross-link only. | context / provisional (as placed) |
| harasiewicz_annales-ecclesiae-ruthenae-lat_1862.txt | the chapters through the partitions and the Austrian period | Already in the bucket. Annales prints documents, so it is more than scholarship here. | context / provisional (as placed) |
| theiner_vetera-monumenta-poloniae-lithuaniae-v3-lat_1863.txt | the documents of the 1680s-1690s at the end of the volume | The immediate prelude (vol. IV, vendored above, starts at 1697). | antecedent / provisional |
| susza_saulus-et-paulus-ruthenae-unionis-lat_martynov1864.txt | whole work | Seventeenth-century Uniate apologetic; antecedent to the Zamość generation. | antecedent / provisional |
| guepin_apotre-de-l-union-des-eglises-fra_1897.txt | the chapters on the cult of Josaphat | Josaphat's cult was a Uniate rallying point; only if the build uses his eighteenth-century veneration. | transmission / needs-ruling |
| mogila_orthodox-confession_anon1762.txt | whole work | The Orthodox confession in an English of 1762: the rival church's catechism inside this window. | context / provisional |

The Union of Brest bucket (VI.20) holds the Brest-era polemic (Russkaya istoricheskaya biblioteka t. 4 and 7, Smotrycki, Susza, Golubev on Mohyla, Kimmel's confessions, Theiner vol. III, Harasiewicz, Pelesz). Nothing in this spec duplicates it; Theiner vol. IV continues its vol. III.

## 3. Verified acquisition leads

| title | author | translator | year | url | rights basis | verified by |
|---|---|---|---|---|---|---|
| Benedicti XIV Bullarium (Mechlin edition), Tomus I parts (vols 1-3 of the set on the host) | Benedict XIV | — | 1826 | https://archive.org/details/bullariuminquoco01bene (also 02, 03, 04) | PD by date | djvu downloaded 1.1, 1.2, 1.0, 0.9 MB, OCR 0.84-0.88, 23 October 2026; part 01 carries constitution LXVI 'Episcopis Ruthenis', part 02/03 Demandatam (LXXXVII, 1743, to the Melkites); Allatae sunt (1755) is in a later tome not located among these four. Not vendored for size; a strong lead for this entry and for melkite-greek-catholic-church |
| Brevis notitia fundationis Theodori Koriathovits, Pars IV, Tomus II | Joannicius Basilovits | — | 1804 (host 1799) | https://archive.org/details/brevisnotitiafun02basi | PD by date | djvu downloaded 0.74 MB, OCR 0.80, 23 October 2026; carries the papal bulls and royal decrees for Munkács |
| Bullae et Brevia Summorum Pontificum, Sacrarum Congregationum Decreta nec non ... Poloniae Regum Diplomata, Congregationem Ruthenorum O.S.B.M. concernentia | Ruthenian Basilian congregation | — | 1767 (Pochaiv) | https://archive.org/details/jbc.bj.uj.edu.pl.NDIGSTDR014786 | PD by date; library 'Domena publiczna' | djvu downloaded 0.38 MB, OCR 0.60, 23 October 2026; mixed Latin and Cyrillic, sampled middle garbled; borderline, a cleaner OCR pass would make it vendorable |
| Geschichte des allmäligen Verfalls ..., II. Band, Das XIX. Jahrhundert | Likowski | Tloczynski | 1887 | https://archive.org/details/geschichtedesall02liko | PD by date | djvu downloaded 0.89 MB, OCR 0.91, 23 October 2026; 1796 onward, mostly the Polotsk-to-Galicia entry's window |
| Dzieje Kościoła unickiego na Litwie i Rusi w XVIII i XIX wieku (Polish original, enlarged ed.) | Likowski | — | 1906 | https://archive.org/details/dziejekosciolau00likogoog | PD by date | metadata API, djvu 1.6 MB, 23 October 2026; the original language of the German vendored above |
| Imago vitae monasticae | Basilovits | — | 1802 | https://archive.org/details/imagovitaemonast00basi | PD by date | metadata API, djvu 0.33 MB, 23 October 2026; Basilian spiritual work, not downloaded |
| Iosaphatidos sive de nece B. Iosaphat Kuncewicz | not named in metadata | — | 1748 | https://archive.org/details/rcin.org.pl.WA248_82393_XVIII-2-139_iosaphatidos-five_o_64431 | PD by date; RCIN 'Public Domain' | metadata API, djvu 0.11 MB, 23 October 2026; Latin poem on Josaphat's death, window-era cult; not downloaded |
| Mowa ... Ferdynanda Ciechanowskiego, biskupa chełmskiego | Ferdynand Ciechanowski | — | 1811 | https://archive.org/details/rcin.org.pl.WA248_275482_F-5436_dabrowa-ciechan-mowa_o_239382 | PD by date | metadata API, djvu 0.01 MB, 23 October 2026; Uniate bishop's speech, too small to matter |
| Dzieła Kongregacyi Generalney Obrządku Starożytnego Greckiego Oryentalnego | Orthodox (non-Uniate) general congregation of Pinsk | — | 1791 | https://archive.org/details/jbc.bj.uj.edu.pl.NDIGSTDR028172 | PD by date | metadata API, djvu 0.11 MB, 23 October 2026; the Orthodox side's 1791 constitution in the Commonwealth, a context witness; not downloaded |
| Acta et decreta sacrorum conciliorum recentiorum (Collectio Lacensis), Tomus I | Jesuits of Maria Laach (Schneemann) | — | 1870 | https://archive.org/details/bub_gb_xilqS9mJXmMC | PD by date | djvu downloaded 3.7 MB, 23 October 2026; Latin-rite councils only; the Eastern-rite tome (which would hold Zamość) was not found on the host |
| Vetera monumenta Poloniae et Lithuaniae, vol. IV, 'English' and 'Polish' items | — | modern | — | https://archive.org/details/vetera-monumenta-poloniae-lithuaniae-theiner-vol4-english | not established | search hit, 23 October 2026; modern renderings of unknown origin, not an edition; never to be vendored |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Synodus provincialis Ruthenorum, separate printings (Rome 1724, 1785, Przemyśl 1838) | The synod's own edition | No archive.org item under any title or description search; Mansi 35 is the substitute |
| Summariusz Reguł Świętego Oyca Naszego Bazylego Wielkiego (1751) | Basilian rule in Polish | OCR 0.43, garbled |
| Ecphonemata Liturgii Greckiey (Pochaiv 1784) | Uniate liturgical explanation in Polish | OCR 0.38, garbled, and only 0.05 MB |
| Kulczyński, Specimen Ecclesiae Ruthenicae (1733) | Basilian procurator's history of the Ruthenian church | Not found on the host; his Signum Magnum (1732) is there only as a 0.05 MB OCR |
| Malinowski | Named in the brief | No relevant pre-1930 work found under the name on the host |
| Harasiewicz, Annales (1862) | Named in the brief | Already vendored; cross-link only |
| Pelesz vol. 2 | Named in the brief | Already vendored; cross-link only |

## 5. Open cross-world questions

- Do the Carpathian (Munkács) Greek Catholics belong to this entry, or to a separate Habsburg Hungary entry? (Basilovits is placed needs-ruling.)
- Benedict XIV's Bullarium serves this entry, the Melkite split (Demandatam, 1743) and the Armenian Catholic patriarchate (1742): which world takes the volumes when they are vendored?
- Mansi 35's non-Ruthenian supplements (Constance, Florence, Lateran V) are placed needs-ruling for the late-medieval Latin entry.
- Likowski vol. II (1796 onward) belongs mainly to ruthenian-greek-catholic-polotsk-to-galicia; that world may want it.
- The Orthodox side of the Commonwealth (Pinsk congregation 1791; the Mohyla confession) is thin here; is it this entry's job or the Russian/Orthodox entries'?

## 6. Recommendation (portfolio decision for the project lead; does not block library work)

**Build.** The floor text the census names first, the acts of the Synod of Zamość, is now in hand in full, with the metropolitan's dedication and the professions of faith; with it come the papal documents to 1775 (Theiner IV), the Basilian order's own constitutions from its Pochaiv press, and two short Polish Uniate voices (a plea against rite-switching of about 1772 and a bishop's catechism of 1792). Harasiewicz and Pelesz already cover the partition era in narrative and documents, and Likowski adds the fullest account of the century. The gap is the 1794-96 forced reversions seen from the Uniate side and any Church Slavonic liturgical print: neither has a readable open copy, so the Russian campaign is known here only through later histories. Against its siblings the entry is distinct: Brest (VI.20) ends about 1700 and Polotsk-to-Galicia begins in 1815, and nothing here repeats either bucket.

