# Source Readiness Dossier — Quietist Controversy (Molinos, Guyon)

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and why it
exists.

**Atlas ID:** VII.14
**Corpus-map slug:** `quietist-controversy-molinos-guyon`
**Time window:** 1675-1699
**Region(s):** Spain, France; census `regions`: Mediterranean
**Dossier author / date:** Claude, Library thread, Era VIII source-research pass, 2026-10-23
**Corpus-map / `cic/texts/` state as of:** branch `library/era-viii-2026-10`, this pass.

## 1. Already assigned

17 works across 16 vendored files in `cic/corpus-map/quietist-controversy-molinos-guyon.yaml`.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Instruction sur les états d'oraison (1697) | bossuet | context | assigned | the treatise and the appended acts of condemnation | `bossuet_instruction-sur-les-etats-d-oraison-fra_1697.txt` |
| Relation sur le Quiétisme (1698) | bossuet | context | assigned | the whole Relation | `bossuet_relation-sur-le-quietisme-fra_1698.txt` |
| Three Letters concerning the Present State of Italy, letter I (1688) | burnet | context | assigned | the first letter, on Molinos and the Quietists; letters II and III as background on the Inquisition and Ita... | `burnet_three-letters-present-state-of-italy_1688.txt` |
| Coelestis Pastor (1687), errors of Molinos; Cum alias (1699), errors on pure love | denzinger | context | assigned | the paragraphs headed 'Errores Michaelis de Molinos' (Innocent XI) and 'Errores de amore erga Deum purissim... | `denzinger_enchiridion-symbolorum-lat_bannwart1911.txt` |
| Explication des Maximes des Saints (1697), ed. Cherel | fenelon | tradition | assigned | the Avertissement and the articles; Cherel's preface, introduction and notes excluded | `fenelon_explication-maximes-des-saints-fra_cherel1911.txt` |
| Fénelon, Mandement of submission and letter to Innocent XII (1699) | fenelon | tradition | assigned | the Mandement and the letter to the Pope | `innocent-xii_cum-alias-with-fenelon-mandement-lat-fra_1699.txt` |
| Réponses à la Déclaration des trois évêques et à la Summa de M. de Meaux (1698) | fenelon | tradition | assigned | the Réponses; the quoted Declaration paragraphs as the bishops' text | `fenelon_reponses-a-la-declaration-fra_1698.txt` |
| The Maxims of the Saints explained, English translation (1698) | fenelon | tradition | assigned | the Maxims and Fénelon's letter to the Pope; the Issy articles, the bishops' Declaration and the King's let... | `fenelon_maxims-of-the-saints_1698.txt` |
| A Short Method of Prayer and Spiritual Torrents, tr. Marston (1875) | guyon | tradition | assigned | the two treatises; the translator's preface excluded | `guyon_short-method-spiritual-torrents_marston1875.txt` |
| Autobiography (La Vie écrite par elle-même), tr. Allen, vol. I (1897) | guyon | tradition | assigned | the autobiography; Allen's introduction excluded | `guyon_autobiography-v1_allen1897.txt` |
| Autobiography (La Vie écrite par elle-même), tr. Allen, vol. II (1897) | guyon | tradition | assigned | the autobiography | `guyon_autobiography-v2_allen1897.txt` |
| La Vie écrite par elle-même, tome III (1791 edition) | guyon | tradition | assigned | the third part of the Life | `guyon_vie-ecrite-par-elle-meme-t3-fra_1791.txt` |
| Moyen court et très facile de faire oraison; Courte apologie; Les Torrens spirituels (1790 edition) | guyon | tradition | assigned | the three treatises; the editor's general preface and Falconi's letter as their own works | `guyon_opuscules-spirituels-t1-fra_1790.txt` |
| Cum alias (12 March 1699), with the assemblies' procès-verbaux | innocent-xii | context | assigned | the brief in Latin and French, the Systema, the procès-verbaux, the King's Declaration and the Paris Mandement | `innocent-xii_cum-alias-with-fenelon-mandement-lat-fra_1699.txt` |
| The Dark Night, Spiritual Canticle and Living Flame (as the books the Quietists and their opponents argued over) | john-of-the-cross | antecedent | needs-ruling | whole file | `john-of-the-cross_dark-night-canticle-living-flame_lewis1891.txt` |
| Guida spirituale (1675; Venice 1678) | molinos | tradition | assigned | the three books and the Treatise on daily communion; the approbations as their own witnesses | `molinos_guida-spirituale-ita_1678.txt` |
| The Spiritual Guide, English translation (1688) | molinos | tradition | assigned | the Guide and the Treatise of daily communion; the translator's preface excluded | `molinos_spiritual-guide_1688.txt` |

## 2. Cross-link opportunities

| file | locus | why | suggested role / confidence |
|---|---|---|---|
| teresa-of-avila_life_lewis1904.txt, teresa-of-avila_interior-castle_stanbrook1912.txt | the chapters on the prayer of quiet and union | Molinos cites Teresa by name (about 7 hits in the 1678 Guida). Bossuet's Instruction cites her about 30 times and Cherel's Fénelon about 5, so both sides argued from her. | antecedent / provisional (could be assigned once the Guida is vendored) |
| john-of-the-cross_dark-night-canticle-living-flame_lewis1891.txt | whole file | Already in the bucket as needs-ruling. The 1678 Guida does not name John of the Cross: its two "della croce" hits refer to the cross itself. So the vendored set does not yet support the antecedent rule. | keep needs-ruling |
| council-of-trent_canons-and-decrees_waterworth1848.txt | Session XIII (eucharist) | Molinos's Trattato on daily communion quotes the Council of Trent (about 6 hits, from file line about 11600 in the 1678 scan). | antecedent / provisional |
| kempis_imitation-of-christ_benham1886.txt | whole | The common devotional stock of both parties. Nothing in the vendored set quotes it by name: checked by grep only for Teresa, John and de Sales. | open; not proposed |

## 3. Verified acquisition leads

| title | author | translator | year | url | rights basis | verified by |
|---|---|---|---|---|---|---|
| The Spiritual Guide, verbatim reprint of the 1699 edition, with letters from Italy (Glasgow, John Thomson) | Molinos | not named | 1885 | https://archive.org/details/spiritualguidet00moligoog | PD by date; NOT_IN_COPYRIGHT | metadata API, djvu 0.20 MB, OCR 0.90, 23 October 2026 (two-part arrangement, no communion treatise) |
| Guida spirituale (Venice, Hertz) | Molinos | none | 1681 | https://archive.org/details/bub_gb_VvjL_Pa7SCUC | PD by date; CC PD mark | metadata API, djvu 0.37 MB, OCR 0.71, 23 October 2026 |
| Guida spirituale, with the Palermo pastoral letter added (Venice) | Molinos | none | 1683 | https://archive.org/details/bub_gb_kuusvleNV-MC | PD by date; CC PD mark | metadata API, djvu 0.43 MB, OCR 0.73, 23 October 2026 |
| Recueil de diverses pièces concernant le Quiétisme et les Quiétistes (Amsterdam, Wolfgang and Savouret): Protestant preface, French Guide, communion treatise, letters on Molinos | Molinos and others | French translator not named | 1688 | https://archive.org/details/Scansionemar2846MiscellaneaOpal | PD by date; CC0 | metadata API, djvu 0.55 MB, OCR 0.82, 23 October 2026 |
| The Spiritual Guide (second 1688 English issue) | Molinos | not named | 1688 | https://archive.org/details/bim_early-english-books-1641-1700_the-spiritual-guide-_molinos-miguel-de_1688 | PD by date | metadata API, djvu 0.42 MB, OCR 0.62, 23 October 2026 |
| Bullarum ... Taurinensis editio, vols. 19-20 (Innocent XI; Coelestis Pastor and the Molinos process) | Holy See | none | 1857 | https://archive.org/details/bullarumdiplomat19cath | PD by date | metadata API, djvu 4.21 MB, OCR 0.79, 23 October 2026 (too large for one bull; Denzinger used for the propositions) |
| Instruction ... a short and easie method of prayer (English) | Guyon | not named | 1704 | https://archive.org/details/bim_eighteenth-century_a-short-and-easie-method_guyon-jeanne-marie-bouv_1704 | PD by date | metadata API, djvu 0.19 MB, OCR 0.73, 23 October 2026 |
| Letters of Madam Guyon (selections translated and re-arranged by Mrs T. C. Upham) | Guyon | Mrs T. C. Upham | 19th c. (Gutenberg) | https://www.gutenberg.org/ebooks/30083 | PD in USA per Gutenberg | Gutenberg page, 0.14 MB, 23 October 2026 (re-arranged selections, so it does not reproduce the letters as written) |
| Life and religious opinions and experience of Madame de La Mothe Guyon | Thomas C. Upham | none | 1847 | https://archive.org/details/lifereligiousop00uphagoog | PD by date; NOT_IN_COPYRIGHT | metadata API, djvu 1.46 MB, OCR 0.94, 23 October 2026 (Protestant biography; transmission) |
| Spiritual Letters of Archbishop Fénelon: letters to women | Fénelon | not named on probe | 1877 | https://archive.org/details/spiritualletters00fnuoft | PD by date; NOT_IN_COPYRIGHT | metadata API, djvu 0.47 MB, OCR 0.88, 23 October 2026 |
| Breves considerationes in doctrinam Michaelis de Molinos et aliorum Quietistarum | du Vaucel (per earlier lead) | none | 1688 | https://archive.org/details/bub_gb_5z1vusUbJDYC | PD by date; CC PD mark | metadata API, djvu 0.14 MB, OCR 0.68, 23 October 2026 |
| Réponse de M. l'Archevêque de Cambray à la Déclaration (earlier printing, reply only) | Fénelon | none | 1697 | https://archive.org/details/bub_gb_GMsfb8BOzJwC | PD by date; CC PD mark | metadata API, djvu 0.27 MB, OCR 0.79, 23 October 2026 |
| Remarques sur la réponse de M. l'Archevêque de Cambray à la Relation sur le quiétisme | Bossuet | none | 1698 | https://archive.org/details/remarquessurlar00boss | PD by date | metadata API, djvu 0.38 MB, 23 October 2026 |
| Recueil de lettres en prose et en vers sur le livre intitulé Explication des maximes | Bossuet (host attribution) | none | 1699 | https://archive.org/details/recueildelettres00boss | PD by date | metadata API, djvu 0.11 MB, 23 October 2026 |
| Summa doctrinae libri cui titulus Explication des maximes des saints | Bossuet | none | 1697 | https://archive.org/details/bub_gb_MlEaVFCVhfsC | PD by date | search hit, 23 October 2026 |
| The Archbishop of Cambray's dissertation on pure love (English) | Fénelon | not named | 1769 | https://archive.org/details/bim_eighteenth-century_the-archbishop-of-cambra_fnelon-franois-de-sal_1769 | PD by date | metadata API, djvu 0.42 MB, 23 October 2026 |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| explicationdesma00fn (Explication, 1697) | First edition of the Maxims | OCR 0.59, below the floor; Cherel's 1911 critical text vendored instead. |
| bub_gb_A8lMszTNsU0C (Explication, 1697) | Second scan of the first edition | OCR 0.53, below the floor. |
| buladelasantidad00cath (Spanish text of the 1687 bull) | The condemnation in Spanish | The djvu text (0.03 MB) is a Portuguese gazette about Turks and Venice, not the bull: wrong content under the item. |
| Gutenberg #22269, Autobiography of Madame Guyon | Proofread English | A Moody Press abridged text, publication date not given; Allen's full 1897 translation used instead. |
| Gutenberg #24989, A Short Method of Prayer | Proofread English | Marston's translation with the Spiritual Torrents dropped (its own transcriber's note says so); the IA scan of the full 1875 volume used instead. |
| in.ernet.dli.2015.23470, The Maxims of the Saints (1903) | English Maxims | djvu 0.07 MB, fragmentary; the 1698 English used instead. |
| bim_...the-spiritual-guide-_molinos-miguel-de_1699 | 1699 English Guide | djvu 0.13 MB, fragmentary. |

## 5. Open cross-world questions

- Denzinger serves at least four census worlds from one file. Should it be vendored once with rows for each world (as specced), or held as a fleet reference outside any one world?
- Fénelon's submission and the bishops' procès-verbaux of 1699 are a Gallican procedure. The provisional catholic-church-ancien-regime row on the Cum alias dossier is named, not decided.
- Guyon's Protestant afterlife (Marston's preface, Upham, the Gutenberg Letters) belongs to reception. Does it sit as transmission here, or with a later Protestant holiness world (the census cites Ward's Experimental Theology in America)?
- Teresa of Avila as antecedent: the vendored Guida names her, so the rule could make the row assigned. Named, not ruled.
- John of the Cross stays needs-ruling: none of the specced own-voice texts names him.

## 6. Recommendation (portfolio decision for the project lead; does not block library work)

**Build.** Both centres of the controversy speak in their own words: Molinos in Italian and in English of 1688, Guyon at length in French and full English, and Fénelon in the Maxims, his Réponses and his submission. The prosecution side is present as the census asks, through Bossuet's Relation and Instruction, the 1699 dossier and the condemned-proposition lists. They are framed as hostile sources. There is no floor question; this is an intra-Catholic spirituality dispute. The gaps: tomes I and II of Guyon's French Life (this edition) were not found, and the Inquisition process records are not on the reachable hosts. The census's "Real texts and trial records" therefore holds for the texts and only partly for the trial. The world is distinct from Port-Royal. The two share only the condemnation handbook and the Gallican setting.

