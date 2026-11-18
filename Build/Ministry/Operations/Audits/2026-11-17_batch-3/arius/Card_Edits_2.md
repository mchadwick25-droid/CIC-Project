# Card edits 2: Arius

Card writer, 2026-11-18. Started from the census's current `card` for `arius` (`cic-website/data/world-census.json`), and worked against the final `arius.brief.txt`, `Outline.md`, `Source_Sheet.md`, `Second_Reading_Key_3.md` and `Second_Readings_3.md`. Output: `arius.card.json`, overwriting the earlier batch card. No `briefLength` (the census does not accept it). Every other census field is kept word for word and in order, except the three listed below.

## quotationOriginals

One entry for each of the twelve quoted spans in the new brief, in the brief's order. Each new `printed` was re-read at its lines.

| # | Edit | modern | printed, file : lines | secondReading | Evidence |
|---|---|---|---|---|---|
| Q1 | kept unchanged | "We are persecuted because we said: the Son has a beginning, but God has no beginning." | Oehler Epiphanius 45736-45738 | same (existing) | Still the brief's first sentence. |
| Q2 | new | "begotten, not made" | "begotten (γεννηθέντα), not made", npnf214 2411-2412 | same | Second_Readings_3 S3-15. |
| Q3 | new | "of one substance with the Father" | "of one substance (ὁμοούσιον, consubstantialem) with the Father", npnf214 2412-2413 | minor | S3-16; its note on "substance" carried in `uncertain`. |
| Q4 | kept unchanged | "enemies of Christ" | npnf204 19018 | minor (existing) | Brief, paragraph 3. |
| Q5 | kept unchanged | "before he was begotten he was not" | npnf214 2422 | same (existing) | Brief, paragraph 4. |
| Q6 | kept unchanged | "We have not been followers of Arius. For how could we, who are bishops, follow a priest?" | Hussey Socrates 16658-16659 | same (existing) | Brief, paragraph 6. |
| Q7 | new | "substance" | Socrates 2.41, the creed of 360, "the term ousia [substance or essence] ... as it is not contained even in the sacred writings", npnf202 9565-9571 | minor | S3-17; note in `uncertain`. |
| Q8 | new | "like the Father" | "we affirm that the Son is like the Father, in such a manner as the sacred Scriptures declare and teach", npnf202 9573-9574 | same | S3-18. |
| Q9 | new | "groaned, and was astonished to find itself Arian" | "The whole world groaned, and was astonished to find itself Arian.", Jerome, Dialogue against the Luciferians 19, npnf206 32412-32413 | **none held** | No second reading of this span exists in the batch records (it is not in Second_Reading_Key_3.md). The field is left out rather than invented; the census check requires it, so this entry fails until a second reading is held. |
| Q10 | new | "alone unbegotten" | "solum ingenitum", Kauffmann 15310 | same | S3-19; lines corrected from 15310-15311 to 15310 per Second_Readings_3 line corrections; the reader's scope point on solum carried in `uncertain`. |
| Q11 | new | "subject and obedient in all things" | "et filium subditum et oboedientem suo in omnibus deo patri", Kauffmann 15323-15325 | same | S3-20. `uncertain` notes that 15322-15323 use the same words of the Holy Spirit to the Son; the brief's are on 15324, of the Son to the Father. |
| Q12 | new | "the faith and communion that came from Arius" | Toledo III anathema 1, "Omnis ergo, qui fidem et communionem ab Ario venientem ... anathema sit.", Collectio canonum 36900-36904 (OCR kept; line-break hyphens joined) | minor | S3-21; its note on communio and the tense carried in `uncertain`. |

Removed (no longer quoted in the new brief): "I have walked in their footsteps, ..." (the Thalia, npnf204 41472-41479); "as godless men" (npnf203 6026); "of things that were not" (npnf214 2422-2423); "Arian" (npnf204 70062-70064; the brief now has "Arian" only inside Jerome's quotation and unquoted in "called ... Arians").

No original-language companion fields: Q2, Q3, Q7, Q8 and Q9 are rendered from printed English, and Q10-Q12 from the Latin given as `printed`, with no English cited.

## sources.about

Two entries added, because the census check requires each quotation's file to be among the card's sources:
- Jerome, Dialogue against the Luciferians, on the council of Ariminum (359); English translation; `cic/texts/npnf206_jerome-principal-works.xml` (Q9).
- Third Council of Toledo, Acts (589), in Collectio canonum Ecclesiae Hispanae; Latin; 1808; `cic/texts/collectio-canonum-ecclesiae-hispanae-toledo-iii-lat_1808.txt` (Q12).

The Kauffmann file (Q10, Q11), npnf202 (Q7, Q8) and npnf214 (Q2, Q3) were already listed. No existing source entry was changed or removed.

## briefReferences

Replaced the twelve old entries with sixteen plain-text references for what the new brief draws on, each with file and lines: Arius's two letters (Oehler; npnf203 6004-6066; npnf204 57094-57111, 57166-57172); Socrates 1.5 and Robertson (npnf202 2063-2076; npnf204 1673-1676, 1687-1689); Alexander's encyclical (npnf204 18975-19019); survival in opponents' books (I6 lines); the Creed of Nicaea (npnf214 2408-2429); Nicaea, exile and burning (npnf202 2962-2965, 3184-3193, 3363-3386); the recall creed (npnf202 4859-4903); Letter 54 and Robertson's dating (npnf204 70051-70106, 4854-4875); Antioch 341 (Hussey 16658-16659; npnf204 57413-57423); Sulpicius Severus (npnf211 11186-11200); the creed of 360 (npnf202 9565-9574, 9606-9610); Jerome (npnf206 32409-32413); Socrates 4.33 and Jordanes (npnf202 14441-14459; Mierow 1648-1660); Ulfila's creed (Kauffmann 15308-15325); Toledo III (36900-36904). Quotation marks appear only around words the brief itself quotes.

## Clearly wrong

None. No card statement is contradicted by the new brief or a held source.

## Not found

- `legacy.traces[0]`: "The churches later called Arian, which held with him that the Son was not eternal." Still unsupported in those words: no held Homoian text says the Son is not eternal (Source_Sheet N12; Outline, heart, "Inferential-Thin as phrased"). The new brief does not state it, and does not contradict it outright, so it stays in place, as ruled at the earlier card check.
