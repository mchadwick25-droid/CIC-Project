# R3 recheck: era 2 batch 6

Scope: round 3, the last allowed. A targeted recheck of the round 2 changes only (`git diff d5c4a35a f2c06ec2` on `era2/batch6/`), against `R2_recheck.md` (N1 to N5) and `R2_changes.md`. Six files changed: the Prosper brief and audio, the Eznik brief and audio, the Mercator card and `records.json`. Unchanged text was not re-reviewed. Each changed sentence was opened at its line in the vendored file, with XML tags stripped, to confirm who is speaking. No drafts were edited, and no paid, model or web calls were made. Line numbers point to files under `cic/texts/`.

## 1. The R2 blocking findings

None were raised in R2.

## 2. The R2 minor findings

| Finding | Status | Check against source |
|---|---|---|
| N1 Prosper, brief l.5: Mommsen's identification hung on the appeal; "writing" dangling | RESOLVED | New text: "After Augustine died, Gibson says, Prosper and a layman named Hilary appealed to Pope Celestine. This Hilary had also written to Augustine. Gibson keeps him apart from Hilary of Arles. Mommsen takes the letter's writer for Hilary of Arles, writing before he became bishop." Gibson: "one Hilary (a layman, not to be confounded with his namesake, the Bishop of Arles), who wrote to him two letters", and later "Prosper and Hilary, who finally took the important step of appealing to Pope Celestine, from whom they succeeded in obtaining a letter addressed to the Gallican Bishops" (npnf211 l.15693–15695, 15750–15753). Mommsen: the two letters to Augustine, "altera ab Hilario episcopo Arelatensi", and "Hilarius cum se laicum dicat, scripsit antequam episcopus Arelatensis factus est" (l.42729–42731, 42748–42749). Mommsen's identification now sits on the letter, not the appeal, and "writing" has a referent. The brief now agrees with card `uncertain` 4 ("the Hilary who wrote with him") and the records `contested_claim` ("the Hilary who wrote to Augustine with him"). This also completes R1 Prosper M6. |
| N2 Prosper, length | RESOLVED | 324 words, about 2:00. Both cut facts stay elsewhere. The Vandal capture of Rome is on card `dates` and in the records claim "His chronicle ran to the Vandal capture of Rome" (npnf203 l.43664–43667). Mommsen on not leaving Gaul is on card `uncertain` 3 and in the records claim and `contested_claim` (l.42785–42793). The remaining "He also kept a chronicle." and "Gennadius adds that…" still read clearly: Gennadius is named twice in the paragraph before. |
| N3 Mercator, card `uncertain` 3: the Louvain reading not established | RESOLVED | New text: "Garnier says copyists wrote 'bishop' for 'letter' in Possidius's list of Augustine's works." Garnier: "Atque hinc emendes id quod notariorum culpa positum est in Possidii indiculo, ad Mercatorem episcopum contra eosdem una. Legendum enim, ad Mercatorem epistola", and "a librariis peccatum est" (PL48 l.523–526, 537). The Louvain claim is gone, so nothing now contradicts l.325–330, where the Louvain printing reads "epistola". The records hold no Possidius claim, so they cannot disagree. Completes R1 Mercator M2(b). |
| N4 Eznik, brief l.9: loose pronoun | RESOLVED | "Eznik was later bishop of Bagrevand." The subject is now named after the Moses of Khoren paragraph. It matches card `knownFor` and `dates` and the records claim "Listed as bishop of Bagrevand…". No other word changed. |
| N5 records.json: witness lines not extended | RESOLVED | (a) Eutyches: "(l.23864-23877)". Perry: Basil "denied that sentence to be his" (l.23866), "Juvenal, of Jerusalem, said:— This sentence, therefore, was altered." (l.23872–23874), "Basil said:— I do not remember and I do. not know if I did say so." (l.23876–23877). The range now covers all three. (b) Liberius: "(npnf202 l.33564-33583)". Sozomen IV.15: "They had formed a compilation, in one document… Liberius… were induced to assent to this document… They partially approved of a confession of faith drawn up by Liberius" (l.33564–33580). The range now covers the compilation. |

## 3. Gates on the changed briefs

| Brief | Words | FK | Flesch | Audio = brief less `[calmly] ` and `[warmly] ` |
|---|---|---|---|---|
| Prosper of Aquitaine | 324 | 8.3 | 60.5 | Yes (one `[calmly]`, one `[warmly]`) |
| Eznik of Kolb | 330 | 8.1 | 64.0 | Yes (one `[calmly]`, one `[warmly]`) |

`grade_text` passes both (FK at most 10, Flesch at least 60). `records.json` and the Mercator card parse as JSON. Card, brief and records agree on every changed point.

## 4. New findings

None. The changed sentences add no wrong attribution and no claim the source does not carry. The cuts leave no dangling reference.

Observation only, not a finding: in the Prosper brief, the unchanged sentence "They won a letter from him to the bishops of Gaul" now comes three sentences after Celestine. The nearest "he" is Hilary of Arles. Gibson's own sentence puts the subject and source beyond doubt ("from whom they succeeded in obtaining a letter"), and the R2 text had the same ambiguity ("Mommsen takes them as one man… They won a letter from him"), so the round 2 change did not create it. If the brief is ever touched again, "They won a letter from Celestine to the bishops of Gaul" (+0 words) would remove it.

## Verdict

N1 to N5 are all resolved and hold against the sources, and there is no new finding: the batch clears review at round 3.

## After round 3

The observation on "They won a letter from him" was taken: the Prosper brief and audio now read "from the pope" ("from Celestine" put the brief under the Flesch floor, at 59.9). No other change was made.
