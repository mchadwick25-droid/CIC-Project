# Source Readiness Dossier — The Church of Utrecht

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and why it
exists.

**Atlas ID:** VII.25
**Corpus-map slug:** `church-of-utrecht`
**Time window:** 1723-1815
**Region(s):** Netherlands; census `regions`: North Europe
**Dossier author / date:** Claude, Library thread, Era VIII source-research pass, 2026-10-23
**Corpus-map / `cic/texts/` state as of:** branch `library/era-viii-2026-10`, this pass.

## 1. Already assigned

5 works across 4 vendored files in `cic/corpus-map/church-of-utrecht.yaml`.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Acta et decreta secundae Synodi Provinciae Ultrajectensis (1763) | church-of-utrecht | tradition | assigned | the convocation, decrees, subscriptions and letter to Clement XIII; the editor's Brevis historia as the chu... | `church-of-utrecht_acta-et-decreta-secundae-synodi-lat_1764.txt` |
| Recueil de divers témoignages (1763): preface, précis and the volume as compiled | church-of-utrecht | tradition | assigned | the Préface sur le schisme, the Précis and the list of writings | `church-of-utrecht_recueil-de-divers-temoignages-fra_1763.txt` |
| Historia Ecclesiae Ultrajectinae (1725) | hoynck-van-papendrecht | context | assigned | the history, the dissertations and the refutation of the appeal; the Monumenta as documents of both parties | `hoynck-van-papendrecht_historia-ecclesiae-ultrajectinae-lat_1725.txt` |
| Meindaerts, pastoral letter presenting the Recueil (1763) | meindaerts | tradition | assigned | the LETTRE PASTORALE at the head of the volume | `church-of-utrecht_recueil-de-divers-temoignages-fra_1763.txt` |
| A History of the So-called Jansenist Church of Holland (1858) | neale | context | assigned | the chapters on the seventeenth and eighteenth centuries and the appendices; the medieval sketch as background | `neale_history-so-called-jansenist-church-of-holland_1858.txt` |

## 2. Cross-link opportunities

| file | locus | why | suggested role / confidence |
|---|---|---|---|
| kempis_founders-of-the-new-devotion_arthur1905.txt, kempis_chronicle-of-mount-st-agnes_arthur1906.txt | whole | Neale's history opens with the Brothers of the Common Life as the earlier glory of the Utrecht church (about 39 hits for "Common Life" and 15 for Kempis in Neale). | antecedent / provisional; only if the lead wants the medieval see as the world's memory |
| council-of-trent_canons-and-decrees_waterworth1848.txt | whole | The 1763 Acta note that the first Utrecht synod (1565) was held to receive Trent. The 1763 synod legislates as a Tridentine church. | antecedent / provisional |
| (this batch) port-royal and Unigenitus texts | Denzinger 'Errores Paschasii Quesnel' | The Unigenitus refusal is the church's defining quarrel. Hoynck's 1725 book refutes the Utrecht priests' appeal against it. | context / provisional (row written) |

## 3. Verified acquisition leads

| title | author | translator | year | url | rights basis | verified by |
|---|---|---|---|---|---|---|
| Batavia sacra, parts (3 scans) | Hugo Franciscus van Heussen | none | 1715 | https://archive.org/details/bataviasacra00heusgoog | PD by date; NOT_IN_COPYRIGHT | metadata API, djvu 1.83 MB, OCR 0.82, 23 October 2026 (vol. 02: 1.50 MB, OCR 0.80; vol. 01 download reset, 0.71 MB on probe) |
| Historia episcopatuum Foederati Belgii, utpote metropolitani Ultrajectini | Hugo Franciscus van Heussen (host attribution) | none | 1719 | https://archive.org/details/bub_gb_riLRLUFCpEkC | PD by date; CC PD mark | metadata API, djvu 4.20 MB, OCR 0.77, 23 October 2026 |
| A History of the So-called Jansenist Church of Holland (other scans) | J. M. Neale | none | 1858 | https://archive.org/details/historyofsocalle00neal | PD by date | metadata API, djvu 0.87 MB, OCR 0.83, 23 October 2026 (also 10026523bsb, OCR 0.84) |
| Acta et decreta secundae Synodi (other copies) | Provincial Synod of Utrecht | none | 1764 | https://archive.org/details/bub_gb_ELPq5NuOK5YC | PD by date; CC PD mark | metadata API, djvu 0.60 MB, OCR 0.62, 23 October 2026 (bub_gb_dAv5FktMbW0C: 0.31 MB, body garbled) |
| Nouvelles ecclésiastiques, 1735 volume (the appellant periodical, with Dutch church news) | anonymous | none | 1735 | https://archive.org/details/nouvellesecclesi01unse | PD by date | metadata API, djvu 5.85 MB, 23 October 2026 (French appellant voice; size) |
| Inventaris van de archieven bij het Metropolitaan Kapittel van Utrecht | J. Bruggeman | none | 1928 | https://archive.org/details/inventarisvandea00brug | PD by date | metadata API, djvu 1.08 MB, 23 October 2026 (archive inventory; finding aid, not text) |
| Vie de messire Antoine Arnauld | Gabriel Du Pac de Bellegarde | none | 1782 | https://archive.org/details/bub_gb_ExAVAAAAQAAJ | PD by date | search hit, 23 October 2026 (Bellegarde was the Utrecht church's agent, but this is a Port-Royal life) |
| Domestic correspondence of Dominique-Marie Varlet, Bishop of Babylon, 1678-1742 | Varlet | — | 1986 | https://archive.org/details/domesticcorrespo0000varl | in copyright (1986) | search hit, 23 October 2026 (not a download) |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Epistola encyclica illustrissimi archiepiscopi Ultrajectensis nomine cleri Batavi (1767), bub_gb_zZGAXBjKQCQC | The archbishop's encyclical in the church's own voice | djvu text is 0.01 MB (title leaves only); nothing to vendor. |
| historyofsocalle0000revj / historyofsocalle0000neal | Neale reprints | Host date 1970: modern reprints, not checked further. |
| Varlet's Apologies (1724-1727), Steenoven's letters, the chapter's election acts | The census's own named events | Not found on archive.org by title, creator or subject search. Gallica, which holds them, is blocked. |
| Dutch-language sources before 1930 on the Clerezy | The church's own language | Searches for clerezie, oud-bisschoppelijke, jansenisten, kapittel found only the 1928 inventory. Dutch primary texts of the church were not found on the reachable hosts. |
| Mason (from the brief) | Named as a lead | No separate Mason title found. The brief's "Mason" may be Neale's middle name (John Mason Neale): named, not assumed. |

## 5. Open cross-world questions

- The Unigenitus quarrel, Quesnel and the French appellants feed Utrecht directly. Should Unigenitus material live here, with Port-Royal (census end 1710), or with catholic-church-ancien-regime?
- The Recueil's testimonies come from the wider church, many probably French appellants. The provisional ancien-régime row needs piece-by-piece checking.
- The census says this church "continuesAs" the Old Catholic Union of Utrecht. The 1870s Old Catholic material on archive.org (Bonn synod 1874, Cologne congress 1872) is out of window. It belongs to that later world, not this one.
- Van Heussen's Batavia sacra (1715) argues the succession from Willibrord that the 1723 chapter relied on. Antecedent, or the world's own pre-history? Named, not ruled.

## 6. Recommendation (portfolio decision for the project lead; does not block library work)

**Build, thinly; or hold as Atlas only until a Dutch source pass.** The church speaks for itself in two substantial in-window texts: its 1763 provincial council in Latin and its 1763 apologetic dossier in French, with Archbishop Meindaerts's pastoral letter. A hostile contemporary witness with documents (Hoynck, 1725) and a sympathetic English narrative (Neale, 1858) round out the set. That is enough for a Representative to state the chapter's claim and its Catholic self-understanding. It is not enough to give a lived voice: no letters, sermons, liturgy or Dutch-language texts were found. There is no floor question, since the church kept the Catholic faith in everything but communion with Rome. Its uniqueness against Port-Royal is real: chapter rights, episcopal succession and a church surviving in a Protestant republic, not the convent and grace. A Dutch-language search, for example of Delpher or the Utrecht archives (neither tried in this pass, and neither on the reachable list), would decide between Build and Atlas only.

