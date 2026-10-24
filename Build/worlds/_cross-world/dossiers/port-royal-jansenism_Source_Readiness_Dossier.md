# Source Readiness Dossier — Port-Royal Jansenism

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and why it
exists.

**Atlas ID:** VII.9
**Corpus-map slug:** `port-royal-jansenism`
**Time window:** 1640-1710
**Region(s):** France; census `regions`: Mediterranean
**Dossier author / date:** Claude, Library thread, Era VIII source-research pass, 2026-10-23
**Corpus-map / `cic/texts/` state as of:** branch `library/era-viii-2026-10`, this pass.

## 1. Already assigned

6 works across 6 vendored files in `cic/corpus-map/port-royal-jansenism.yaml`.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Lettres de la Mère Marie Angélique Arnauld, tome I (1742) | arnauld-angelique | tradition | assigned | the letters; the editors' Avertissement excluded | `arnauld-angelique_lettres-t1-fra_1742.txt` |
| The Nuns of Port Royal as seen in their own Narratives (1909) | lowndes | context | assigned | the whole book; the quoted extracts from the nuns' narratives are the primary content | `lowndes_nuns-of-port-royal-own-narratives_1909.txt` |
| Les Lettres Provinciales (1656-1657), ed. Stewart | pascal | tradition | assigned | the eighteen letters; Stewart's introduction and notes excluded | `pascal_lettres-provinciales-fra_stewart1920.txt` |
| The Provincial Letters, tr. M'Crie (1856) | pascal | tradition | assigned | the eighteen letters; M'Crie's introduction and notes excluded | `pascal_provincial-letters_mcrie1856.txt` |
| Thoughts, Letters and Minor Works (Harvard Classics vol. 48, 1910) | pascal | tradition | assigned | the Thoughts, Letters and Minor Works; the series editor's introductions excluded | `pascal_thoughts-letters-minor-works_trotter-booth-wight1910.txt` |
| Divers actes, lettres et relations des religieuses de Port-Royal (1724) | port-royal | tradition | assigned | the nuns' Relations, acts and letters; the pieces by Lancelot and other men of the circle as their own witn... | `port-royal_divers-actes-lettres-relations-fra_1724.txt` |

## 2. Cross-link opportunities

| file | locus | why | suggested role / confidence |
|---|---|---|---|
| npnf105_augustine-anti-pelagian-writings.xml | On grace and free will, On rebuke and grace, On the predestination of the saints, On the gift of perseverance | The Augustine the movement read "harder than the Jesuits"; Arnauld cites Augustine about 97 times in the Fréquente communion scan and the Provinciales about 114 times. | antecedent / assigned once the spec is vendored (the world's own texts argue from it); provisional until then |
| council-of-trent_canons-and-decrees_waterworth1848.txt | Session XIV (penance), Session XIII (eucharist), Session VI (justification) | Arnauld argues from Trent on penance and communion (about 78 hits for "Trente" in the 1644 scan). | antecedent / provisional |
| augustine Latin CSEL files (e.g. augustine_epistulae-*, augustine_retractationes-lat_knoll-csel36.txt) | anti-Pelagian letters and Retractationes | Same Augustinian base, in Latin. | antecedent / provisional |

## 3. Verified acquisition leads

| title | author | translator | year | url | rights basis | verified by |
|---|---|---|---|---|---|---|
| De la fréquente communion (first edition) | Antoine Arnauld | — (French) | 1644 | https://archive.org/details/bub_gb_qJx2IKzu6YMC | PD by date | metadata API and dry run, djvu 2.06 MB, 23 October 2026; verified and downloaded, held back by the lead for size (the nuns' Relations volume took the budget); first to add next |
| Lettres de la Mère Angélique, tome II | Marie-Angélique Arnauld | none | 1742 | https://archive.org/details/taylorinstituti00ahlagoog | PD by date; NOT_IN_COPYRIGHT | metadata API, djvu 1.23 MB, OCR 0.87, 23 October 2026 |
| Lettres de la Mère Angélique, tome III (title page M.DCC.XLIV) | Marie-Angélique Arnauld | none | 1744 | https://archive.org/details/taylorinstituti00nlalgoog | PD by date; NOT_IN_COPYRIGHT | metadata API, djvu 1.06 MB, OCR 0.86, 23 October 2026 |
| Entretiens ou conférences de la Mère Marie-Angélique Arnauld (Bruxelles) | Marie-Angélique Arnauld | none | 1757 (host) | https://archive.org/details/entretiensoucon00pascgoog | PD by date; NOT_IN_COPYRIGHT | metadata API, djvu 0.75 MB, OCR 0.85, 23 October 2026 |
| Mémoires pour servir à la vie de la R. Mère Marie Angélique (her own Relation, with the Avertissement on how it was written) | Angélique Arnauld; collected by Angélique de Saint-Jean | none | 1737 | https://archive.org/details/wotb_6743934 | PD by date | metadata API, djvu 0.84 MB, OCR 0.74 (garbled front matter), 23 October 2026 |
| Mémoires pour servir à l'histoire de Port-Royal et à la vie de la Mère Angélique, tome I (Utrecht; nuns' Relations) | collected Relations | none | 1742 | https://archive.org/details/bub_gb_ggOZRILGvtUC | PD by date; CC PD mark | metadata API, djvu 1.22 MB, OCR 0.84, 23 October 2026 |
| Mémoires pour servir à l'histoire de Port-Royal, tome I (Relations of individual nuns) | collected Relations | none | 1734 | https://archive.org/details/mmoirespourser0102arna | PD by date | metadata API, djvu 0.93 MB, OCR 0.85, 23 October 2026 |
| Mémoires pour servir à l'histoire de Port-Royal, par M. Fontaine, tome I (Cologne) | Nicolas Fontaine | none | year not read; host 1739 | https://archive.org/details/memoirespourser01fontgoog | PD by date; NOT_IN_COPYRIGHT | metadata API, djvu 1.18 MB, OCR 0.90, 23 October 2026 |
| Same, tome II (Cologne, MDCCXXXVIII) | Nicolas Fontaine | none | 1738 | https://archive.org/details/memoirespourser00fontgoog | PD by date; NOT_IN_COPYRIGHT | metadata API, djvu 1.32 MB, OCR 0.91, 23 October 2026 |
| Mémoires pour servir à l'histoire de Port-Royal, par M. du Fossé (Utrecht) | Pierre Thomas du Fossé | none | 1739 | https://archive.org/details/memoirespourser00fossgoog | PD by date; NOT_IN_COPYRIGHT | metadata API, djvu 0.97 MB, OCR 0.84, 23 October 2026 |
| Abrégé de l'histoire de Port-Royal, edited from a manuscript prepared for the press (editor not read in the scan) | Jean Racine | none | 1908 | https://archive.org/details/abrgdelhisto00raciuoft | PD by date; NOT_IN_COPYRIGHT | metadata API, djvu 0.57 MB, OCR 0.87, 23 October 2026 |
| Pensées et Opuscules, ed. Brunschvicg, 6th revised edition (Hachette) | Blaise Pascal | none | 1919 (title page; host says 1912) | https://archive.org/details/pensees-et-opuscules | PD by date; CC PD mark | metadata API, djvu 2.07 MB, OCR 0.80, 23 October 2026 |
| Œuvres de Blaise Pascal (Grands Écrivains), vol. XI | Pascal; series editors not read for this volume | none | host 1925 | https://archive.org/details/uvresdeblaisepas11pasc | PD by date; NOT_IN_COPYRIGHT | metadata API, djvu 0.91 MB, OCR 0.75, 23 October 2026 |
| Œuvres de Blaise Pascal (Grands Écrivains), vol. I | Pascal; ed. Brunschvicg and Boutroux | none | 1908 | https://archive.org/details/oeuvrespublies01pasc | PD by date | metadata API, djvu 0.81 MB, OCR 0.83, 23 October 2026 |
| The Gospels with moral reflections on each verse, vol. I of 3 (Glasgow, Collins; essay by Daniel Wilson) | Pasquier Quesnel | not named | 1830 | https://archive.org/details/gospelswithmoral01ques | PD by date; NOT_IN_COPYRIGHT | metadata API, djvu 1.00 MB, OCR 0.91, 23 October 2026 |
| Select Memoirs of Port Royal, vol. I | Mary Anne Schimmelpenninck | none | 1858 | https://archive.org/details/selectmemoirsofp01schi | PD by date; NOT_IN_COPYRIGHT | metadata API, djvu 0.57 MB, OCR 0.91, 23 October 2026 |
| La Constitution Unigenitus ... et le nouveau catéchisme (La Haye, David du Ry) | Clement XI | none | 1718 | https://archive.org/details/laconstitutionu00goog | PD by date; NOT_IN_COPYRIGHT | metadata API, djvu 0.06 MB, OCR 0.64, 23 October 2026 |
| Les nouvelles et anciennes reliques de Mre Jean du Verger de Hauranne (hostile extracts against Saint-Cyran, addressed to the Paris faculty) | anonymous | none | 1648 | https://archive.org/details/bub_gb_swYu6lv22AgC | PD by date; CC PD mark | metadata API, djvu 0.70 MB, OCR 0.79, 23 October 2026 |
| Augustinus, Louvain 1640 (one of several volume scans) | Cornelius Jansen | none | 1640 | https://archive.org/details/bub_gb_KXEvROSpKdwC | PD by date; CC PD mark | metadata API, djvu 3.35 MB (OCR not measured), 23 October 2026 |
| Essais de morale, tome I | Pierre Nicole | none | 1755 | https://archive.org/details/bub_gb_O2Jpc0rFiYkC | PD by date; CC PD mark | metadata API, djvu 0.58 MB, 23 October 2026 |
| Moral Essays (English) | Pierre Nicole | not named | 1677 | https://archive.org/details/bim_early-english-books-1641-1700_moral-essays-_nicole-pierre_1677 | PD by date | metadata API, djvu 0.45 MB, 23 October 2026 |
| The Perpetuity of the Faith of the Catholic Church on the Eucharist (English) | Nicole and Arnauld | not named | 1834 | https://archive.org/details/perpetuityfaith00nicogoog | PD by date; NOT_IN_COPYRIGHT | metadata API, djvu 0.54 MB, 23 October 2026 |
| The famous Bull Unigenitus, in English, with a short history | Clement XI | not named | 1753 | https://archive.org/details/bim_eighteenth-century_the-famous-bull-unigenit_catholic-church-pope-1_1753 | PD by date | metadata API, djvu 0.04 MB, 23 October 2026 |
| Théologie familière (Spanish translation, Teología familiar) | Saint-Cyran | not named | 1693 | https://archive.org/details/teologia-familiar-junto-con-otros-diversos-pequenos-tratados-de-devocion | PD by date | search hit, 23 October 2026 |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Gutenberg #18269, Pascal's Pensées (Trotter) | Proofread English Pensées | The Gutenberg text reproduces a 1958 Dutton paperback with T. S. Eliot's introduction, so it is a 1931-1963 printing under the brief's rule. It also moves Brunschvicg fragment 514 to the notes and renumbers every fragment after it. The 1910 Harvard Classics scan of the same translation keeps the numbering and was vendored instead. |
| thoughtstrbywftr00pascuoft | Second Toronto scan of Harvard Classics vol. 48 | Duplicate of the vendored scan; the other carries the NOT_IN_COPYRIGHT rights field. |
| Lettres provinciales via ccel (census url) | The census links CCEL | CCEL is blocked from this sandbox; Gutenberg #73959 (M'Crie) supplies the English. |
| Gallica copies of the Relations and the Nécrologe | Fullest French holdings | Gallica is blocked; no workaround tried. |

## 5. Open cross-world questions

- The Denzinger 1911 rows place Cum occasione and Unigenitus as context for Port-Royal. The same volume is placed provisionally for church-of-utrecht and catholic-church-ancien-regime. Whether one fleet-wide handbook should carry rows for several worlds is a ruling for the lead.
- Quesnel's Réflexions morales and the Unigenitus quarrel run past the census end date (1710) into the Utrecht and appellant years. Should they sit with Port-Royal, with church-of-utrecht, or with a French appellant world the census does not yet have?
- Pascal's Pensées is also a general apologetic. Should the Pensées carry a row for catholic-church-ancien-regime as well as Port-Royal?
- The npnf105 Augustine antecedent row: could be assigned once these files are vendored, since Arnauld and the Provinciales argue from Augustine throughout.

## 6. Recommendation (portfolio decision for the project lead; does not block library work)

**Build.** The world's own voice is deep and varied. It has the nuns' collective and personal Relations under persecution, the abbess's letters, Pascal in French and English, and Arnauld's theology. All of it is in-window or a faithful edition of in-window text, and most of the OCR is clean. There is no floor question: the census already rules that condemnation in an intra-Catholic grace dispute is not floor failure. The weak point is language. The nuns write only in eighteenth-century French with the long s, so PD English for them is limited to Lowndes's 1909 extracts, which a reader must check against the French. Nothing in the sibling worlds overlaps. The quietist controversy shares only the condemnation handbook, and Utrecht inherits the Unigenitus quarrel, not the convent.

