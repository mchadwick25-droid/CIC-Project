# Source Readiness Dossier — Colonial Latin American Devotional Catholicism

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and why it
exists.

**Atlas ID:** VII.17
**Corpus-map slug:** `colonial-latin-american-devotional-catholicism`
**Time window:** c. 1600-1810
**Region(s):** New Spain, Peru; census `regions`: Latin America, Mediterranean
**Dossier author / date:** Claude, Library thread, Era VIII source-research pass, 2026-10-23
**Corpus-map / `cic/texts/` state as of:** branch `library/era-viii-2026-10`, this pass.

## 1. Already assigned

15 works across 14 vendored files in `cic/corpus-map/colonial-latin-american-devotional-catholicism.yaml`.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| The Natural and Moral History of the Indies, Vol. II: the Moral History (Books V to VII), in Grimston's 1604 English | acosta | antecedent | provisional | the Fift Booke, file line 986 onward | `acosta_natural-and-moral-history-of-the-indies-v2_grimston-markham1880.txt` |
| Aprobacion and life of Sor Juana (Fama y obras posthumas, 1700) | calleja-diego | tradition | provisional | Calleja's approbation in the front matter | `juana-ines-de-la-cruz_fama-y-obras-posthumas-spa_castorena1700.txt` |
| The Life of Saint Rose of Lima (Faber's series, 1847; American edition 1855) | faber-fw | transmission | assigned | whole text | `faber-fw_life-of-saint-rose-of-lima_1855.txt` |
| La Estrella del Norte de México (1688) | florencia | tradition | assigned | the author's prologue and chapters; de la Rosa's prologue of 1895 excluded | `florencia_estrella-del-norte-de-mexico-spa_rosa1895.txt` |
| The English-American, or A New Survey of the West Indies (1648) | gage | context | assigned | the chapters on Mexico City and on Guatemala's Indian towns, their feasts, images and confraternities | `gage_english-american-new-survey-of-the-west-indias_1648.txt` |
| Vita mirabilis et mors pretiosa Rosae de S. Maria Limensis (1664) | hansen | tradition | provisional | whole text | `hansen_vita-mirabilis-et-mors-pretiosa-rosae-de-s-maria-lat_1664.txt` |
| Respuesta a Sor Filotea de la Cruz; Exercicios devotos for the novena of the Incarnation; Ofrecimientos of the Rosary of the Sorrows; poems (Fama y obras posthumas, 1700) | juana-ines-de-la-cruz | tradition | assigned | her own prose and verse; the eulogies by others excluded | `juana-ines-de-la-cruz_fama-y-obras-posthumas-spa_castorena1700.txt` |
| Historia de los indios de la Nueva Espana (written 1536-1541) | motolinia | antecedent | provisional | whole text | `motolinia_historia-de-los-indios-de-la-nueva-espana-spa_sanchez-garcia1914.txt` |
| Life and Apostolic Labors of Junípero Serra, English of 1913 | palou | tradition | assigned | the translated chapters; James's introduction and notes excluded | `palou_life-and-apostolic-labors-of-junipero-serra_williams1913.txt` |
| Relación histórica de la vida de Fray Junípero Serra (1787) | palou | tradition | assigned | whole text | `palou_relacion-historica-vida-junipero-serra-spa_1787.txt` |
| Promptuario manual mexicano (1759): the platicas, Lenten sermons and Guadalupe sermon | paredes | tradition | assigned | whole text; the Spanish preliminaries as their own witness | `paredes_promptuario-manual-mexicano-nci-spa_1759.txt` |
| Itinerario para parochos de indios (1668) | pena-montenegro | tradition | assigned | whole text; especially the treatises on idolatry, marriage and the sacraments | `pena-montenegro_itinerario-para-parochos-de-indios-spa_1668.txt` |
| The Book of the Foundations, the chapter on her brother Lorenzo's return from the Indies | teresa-of-avila | context | needs-ruling | contents entry at line 13901 and the text at line 13989 (Lorenzo de Cepeda, back from the Indies after thir... | `teresa-of-avila_book-of-foundations_lewis1913.txt` |
| Compendio de la prodigiosa vida de Fray Juan Macías (1689) | toro | tradition | provisional | the chapters of the Life | `toro_compendio-vida-juan-macias-spa_1689.txt` |
| Sumario y memorial ajustado de las probanzas, cause of Toribio de Mogrovejo (Lima, 1662) | villagomez | tradition | assigned | the articles and the witnesses' depositions | `villagomez_sumario-probanzas-canonizacion-toribio-mogrovejo-spa_lima1662.txt` |

## 2. Cross-link opportunities

| file | locus | why | suggested role / confidence |
|---|---|---|---|
| acosta_natural-and-moral-history-of-the-indies-v2_grimston-markham1880.txt | the Moral History, Books V-VII | Already in the bucket as antecedent/provisional; Acosta's account of Andean and Mexican religion is what Peña Montenegro's Itinerario argues from on idolatry. | antecedent / provisional (unchanged) |
| motolinia_historia-de-los-indios-de-la-nueva-espana-spa_sanchez-garcia1914.txt | whole text | Already in the bucket; the founding Franciscan narrative of New Spain that Florencia and Palóu's college looked back on. | antecedent / provisional (unchanged) |
| teresa-of-avila_book-of-foundations_lewis1913.txt | the Lorenzo de Cepeda chapter | Already in the bucket as needs-ruling; nothing found to change that. | context / needs-ruling (unchanged) |

No other vendored file carries New Spain or Peru devotional matter of weight; a grep for Guadalupe across cic/texts hit only Spanish and Philippine contexts.

## 3. Verified acquisition leads

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| Coronica moralizada del Orden de San Augustin en el Peru (Barcelona) | Antonio de la Calancha | none | 1638 | https://archive.org/details/A050111 | PD by date; Public Domain Mark | metadata API, djvu 5.46 MB, OCR 0.80, 23 October 2026. Held back for size; the strongest next addition (Copacabana shrine, Augustinian Peru, own voice of the colonial church). |
| Obras selectas de la célebre monja de Méjico, Sor Juana Inés de la Cruz (Quito) | Juana Inés de la Cruz; ed. Juan León Mera | none | 1873 | https://www.gutenberg.org/ebooks/74087 | PD in the USA per Gutenberg | Gutenberg page and text, 0.53 MB, 23 October 2026. Mostly secular verse with some religious romances and a long nineteenth-century biography; the 1700 Fama is the better witness. |
| Vida admirable del bienaventurado Fray Martín de Porres (Lima, Huerta) | José Manuel Valdés | none | 1863 (host; written about 1840, documents of 1835-1839 inside) | https://archive.org/details/vidaadmirabledel0000vald | PD by date | metadata API, djvu 0.51 MB, OCR 0.90, 23 October 2026. A transmission witness: a Life of Porres by an Afro-Peruvian physician of the republic; outside the window. |
| Historical Memoirs of New California, vol. 1 | Francisco Palóu; ed. and trans. Herbert E. Bolton | Bolton | 1926 | https://archive.org/details/historicalmemoir0001fray | PD by date (1926) | metadata API, djvu 0.58 MB, OCR 0.90, 23 October 2026. Internet Archive's own scan of a library copy, volume 1 of 4; a fuller Palóu (the Noticias) if the California strand grows. |
| Vida admirable, y muerte preciosa de Soror Rosa de Santa Maria (Valencia, Spanish abridgement of Hansen) | Hansen, abridged by order of Rocabertí | none | 1665 (host) | https://archive.org/details/vidaadmirableymu00hans_0 | PD by date | metadata API, djvu 0.21 MB, OCR 0.88, 23 October 2026. Duplicates the Latin Life. |
| A Voyage to South-America, vol. I | Jorge Juan and Antonio de Ulloa | not checked | 1758 | https://archive.org/details/avoyagetosoutha00ullogoog | PD by date; NOT_IN_COPYRIGHT | metadata API, djvu 1.20 MB, OCR 0.88, 23 October 2026. A second outside witness (Quito and Lima festivals, 1730s-1740s); Gage chosen first. |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Huei tlamahuiçoltica (Lasso de la Vega, 1649), hueitlamahuiolti00lass | The Nican Mopohua, named by the census | Djvu 0.08 MB for the whole book: garbled, as reported. The 1998 Sousa-Poole-Lockhart edition (storyofguadalupe00lisa) is in copyright. 'NicanMopohua' on the host is an undated private upload with no text file. |
| Recapitulación de las ordenanzas de la archicofradía de la Vera Cruz (1759), recapitulacionoe00arch | Confraternity rules, which the census asks for | OCR 0.63 on a 0.14 MB file: borderline and short; not vendored. A lead if confraternity rules become a priority. |
| Sermón en la profesión de Soror Joachina Josepha (1710), sermonenlaprofes00arme | Convent sermon | OCR 0.54, garbled. |
| Piedra fundamental de la mystica Sion (1727), piedrafundamenta00lpez | Convent foundation sermon | 0.10 MB; too slight to carry weight. |
| Lima and Mexico 'Carta de hermandad' confraternity sheets (cartadehermandad14cofr, cartadondecontod00cofr, paramayorgloriay00cofr, paramayorgloriay01cofr, cartadehermandad00cofr) | Confraternity membership certificates of the 1770s-1800s | Single printed sheets; djvu 0.00-0.01 MB, no usable text. |
| Earlier lead A024187 described as Toro's Life of Martín de Porres | A seventeenth-century Life of Porres | The body text shows it is Toro's Life of Juan Macías, not Porres; vendored under its true subject. No seventeenth-century public-domain Life of Porres was found; the Porres process testimony of the 1660s exists only in archives and modern editions. |
| Úrsula de Jesús, The Souls of Purgatory | Named by the census: an enslaved, then freed, woman's spiritual diary | Only the 2004 van Deusen edition exists; in copyright. No public-domain print found. |
| Madre María de San José's autobiography | Named by the census | Only the modern Myers and Powell edition; in copyright. |
| Respuesta a Sor Filotea in English | The census cites Arenal and Powell | 1994 translation, in copyright; no public-domain English found. |

## 5. Open cross-world questions

- The California missions (Palóu) are placed here because the census says so; whether they also belong to `nineteenth-century-latin-american-catholicism` (VIII.48) for the mission secularisation after 1810 is unnamed in this pass.
- Toribio de Mogrovejo's canonization process (1662) testifies about a sixteenth-century archbishop; whether Era VI's mission-born-christianities world (VI.13, 'Americas') should share it is a question for the lead.
- The F. W. Faber Life of Rose (1855) is placed as transmission; its source is not named in the pages read.

## 6. Recommendation (portfolio decision for the project lead; does not block library work)

**Build.** The public domain gives this world real inside depth in Spanish, Latin and Nahuatl: a professed nun's own reply and devotional exercises (Sor Juana), canonization testimony from Lima witnesses (Villagómez), the Guadalupe cult in its own advocate's history (Florencia), Sunday preaching to Nahua parishioners (Paredes), the bishop's manual for Indian parishes (Peña Montenegro), and the Franciscan California record (Palóu, with English). Gage gives the hostile outside view. The gaps the census itself names are real and modern-only: Úrsula de Jesús, María de San José, and the confraternity books, so the voices of enslaved and indigenous devotees reach the corpus only through clergy and process clerks. English is thin: only Palóu, Gage and a nineteenth-century Rose life; the core own-voice texts are Spanish and Nahuatl, which raises the rendering burden. Calancha (5.5 MB, clean) is the first thing to add if the lead wants the Peruvian Augustinian strand.

