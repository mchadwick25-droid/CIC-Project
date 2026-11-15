# R2 recheck: Library eras 1-3 batch, 2026-11-15

What was rechecked. Only the 11 round 1 findings and the two extra changes at the foot of `R1_changes.md`. For each finding, the new wording was looked up in the file header, the REGISTRY.yaml row, the README entry, the queue row, the staging yaml, the merged shelf file and the two wants files. The new line citations were read in the text. All nine edited text files have the rule line at line 11, so file line = OCR line + 12. For all nine, the file size minus the header (through the rule line and one blank line) equals the byte count on the Source line, and the body is byte-identical to HEAD. Nothing else was re-reviewed.

| finding | fixed? | note |
|---|---|---|
| 1 Bekker / Lachmann | partly | Creator line fixed; "CAROLI LACHMANNI" stands at 19757. The REGISTRY.yaml notes and the queue title still read "recognovit Immanuel Bekkerus; Genesius", which R1 asked to change. See new finding A. |
| 2 Lagarde Greek OCR | yes | Header, registry and shelf note say "garbled throughout". |
| 3 Bardy Greek OCR | yes | Header and registry. |
| 4 PG 82 Latin column | yes | Header and registry say "unreadable throughout (read as Greek letters)". |
| 5 Mansi locus | partly | The locus no longer runs to the volume's end. But the new numbers are mis-offset. See new finding B. |
| 6 Mansi host note | yes | Header and registry. |
| 7 Littmann Nr. 11 | yes | Header, registry, README, staging and shelf file. At file 10029-10030 Littmann reports Nielsen (ZDMG 66) reading it as largely pagan and rejects that. OCR "about 10017" = file 10029. Supported. |
| 8 Surius 1875 | yes | Now "the host record gives 1875". |
| 9 Langlois introduction | yes | "INTRODUCTION." stands at file 13585 (OCR 13573); "about 13574" holds. Header, registry and README agree. |
| 10 Lagarde shelf reason | yes | The note now gives the date problem and says the date is not settled. |
| 11 Naironus title | yes | "Banesio" removed from header, registry and queue; no copy remains. |
| extra: "after Schulze" removed | sound | It removes an unchecked claim. |
| extra: Bardy note | sound | 1923 is a year before Loofs 1924. The note no longer claims a disagreement nobody checked. |

## New findings

A. **MINOR.** `cic/texts/REGISTRY.yaml` (theophylact-simocatta row, notes) and `Build/worlds/_cross-world/download-queue-seed.yaml` (title at 25697) still read "recognovit Immanuel Bekkerus; Genesius". This is round 1 finding 1's second sentence, left undone, and `R1_changes.md` does not say so. Add "ex recognitione Caroli Lachmanni" after "Genesius", or name Lachmann in the notes.

B. **MINOR.** Mansi tomus 8. The Jerusalem heading "CONCILIUM * HIEROSOLYMITANUM" is at file line 116792, which is OCR 116780. The header and registry say "A synod of Jerusalem follows from about 116792 and the indices from 118250". Both are file line numbers labelled as OCR (OCR 116780 and 118238). The staging and shelf locus "to about 116790" OCR is file 116802, ten lines past the Jerusalem heading. The Wanted_Sources row "lines 90512-116802" ends at the same wrong place. Use OCR 116780 (file 116792) for the start of Jerusalem and end the acts just before it.

C. **MINOR.** `R1_review.md` was changed after it was committed: line numbers in the rights table and in the Epiphanius, Loofs, Surius, Theodoret, Littmann, Langlois and Bekker paragraphs and in findings 1 and 9. `R1_changes.md` does not record this. A review is lasting audit trail, so corrections to it should be logged as corrections, not made silently in place.

Counts: 0 blocking, 3 minor.
