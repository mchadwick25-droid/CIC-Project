# Era 4 Who batch 11: round 3 changes (Mark's cap ruling, Fix + one check, 2026-11-15)

Mark's cap ruling: apply every round 3 finding in R3_review.md as worded. That is R3-BB1 and the 11 minor findings (Part A 1, Part B 4, Part C 6). Every old string matched its file exactly once, so no finding needed a located-text application. Folder: `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch11/`. Cards were rewritten with indent 2 and `records.json` with indent 1 (ensure_ascii=False, final newline), the formats they already had. score.py rebuilt the Stephen audio file from the brief.

## Part A

**R3-AM1 (README, bare "Tamayo"):** applied as worded, three lines.
- "Other profiles": "give both Tamayo's view that he was Paulus Alvarus" → "give both Juan Tamayo's view that he was Paulus Alvarus"
- "Corrections": "and Tamayo took for Paulus Alvarus (ALV l.31683-31716)." → "and Juan Tamayo took for Paulus Alvarus (ALV l.31683-31716)."
- "Names and ids": "Tamayo took the two for one (ALV l.31683-31716)." → "Juan Tamayo took the two for one (ALV l.31683-31716)."

## Part B

**R3-BB1 (Stephen, the profile's own 789 + 7 arithmetic):** card applied as worded; records applied with the wording in Mark's cap ruling.
- Card `uncertain` "The year": "seven years before the twenty. The note names no year for the twenty, and seven years after 789 is 796. Georg Graf, in his 1910" → "seven years before the twenty. Georg Graf, in his 1910". The sentence "The note names no year for the twenty, and seven years after 789 is 796. " is dropped.
- Records `contested_claims` "The year of the raid", side 2: "seven years before, and names no year for the twenty; seven years after 789 is 796 (l.53478-53480)" → "seven years before the twenty's passion, and names no year for the twenty (l.53478-53480)"

**R3-BM1 (Stephen, "It ends with" / "He ends by"):** applied as worded.
- Card `uncertain` "His name": "It ends with him singing hymns to the martyrs." → "Near its end, he speaks of singing hymns to the martyrs."
- Brief, last paragraph: "He ends by asking the martyrs to remember their unworthy servant" → "Near the end, he asks the martyrs to remember their unworthy servant". The audio, rebuilt by score.py, keeps "[warmly] " before "Near".
- Card `keyWorks[1]`: "at the end of his account" → "near the end of his account"

**R3-BM2 (Stephen, "He" after "the Poet's feast"):** applied as worded.
- Card `uncertain` "Which Stephen": "He was a monk of the laura who flourished in 790" → "This Stephen was a monk of the laura who flourished in 790"

**R3-BM3 (Stephen records, Acts-side range):** applied as worded.
- Records: "(AASS l.50556-50557, l.50600-50607; Greek l.229190-229198)" → "(AASS l.50556-50557, l.50600-50624; Greek l.229190-229198)"

**R3-BM4 (README, Stephen census bullet, Acts range):** applied as worded.
- README: "The Acts give AM 6288, 788 (l.50556-50557)" → "The Acts give AM 6288, 788 (l.50556-50557, l.50619)"

## Part C

**R3-CM1 (al-Tabari `legacy.traces[2]`):** applied as worded.
- "The historian al-Maqrizi (died 1441, by Evetts) is quoted in Étienne Quatremère's French of 1811 on the caliph Aziz's library." → "The historian al-Maqrizi died in 1441, Evetts says. Étienne Quatremère's French of 1811 quotes al-Maqrizi on the caliph Aziz's library."

**R3-CM1 (Ibn Ishaq `uncertain[6]`):** applied as worded.
- "the Negus said that Jesus, son of Mary, was nothing more than this." → "the Negus said that Jesus, son of Mary, was nothing other than this."

**R3-CM2 (Ibn Ishaq records, revolt claim range):** applied as worded.
- "\"Wir sagen, er ist Gottes Sohn\" (l.9589-9591)" → "\"Wir sagen, er ist Gottes Sohn\" (l.9588-9591)"

**R3-CM3 (Ibn Ishaq records, Faymiyun claim scan mark):** applied as worded.
- "\"Diess ist die Tradition des Wahb Ibn Munabbah, nach dem Berichte der Bewohner von Nadjran\"" → "\"Diess ist die Tradition des Wahb Ibn Munabbah, nach dem Berichte der Bewohner von Nadjran\" (scan \"Ihn\")"

**R3-CM-R1 (README, Ibn Ishaq census sentence):** applied as worded.
- "The story's sources are Simeon, the Book of the Himyarites and Procopius, not him; `relationsSummary` and `voices` cite none." → "\"Kaleb Crosses the Sea\" cites Simeon, the Book of the Himyarites and Procopius as primary sources and Bowersock as reference, and none of them is him; `relationsSummary` and `voices` cite none."

**R3-CM-R2 (README, Stephen Acts range):** applied as worded. It is the same fix as R3-BM4, on the same string, so it was applied once (see R3-BM4).

## The one check

score.py (162.5 wpm):

| id | words | minutes | FK | Flesch |
|---|---|---|---|---|
| al-tabari | 336 | 2:04 | 6.7 | 68.4 |
| eulogius-of-cordoba | 336 | 2:04 | 6.9 | 69.5 |
| ibn-ishaq | 338 | 2:04 | 6.8 | 68.8 |
| ishoyahb-iii | 338 | 2:04 | 7.2 | 65.5 |
| paulus-alvarus | 336 | 2:04 | 7.9 | 63.3 |
| stepanos-of-taron | 336 | 2:04 | 6.7 | 69.1 |
| stephen-of-mar-saba | 338 | 2:04 | 6.2 | 75.8 |
| theodore-abu-qurrah | 338 | 2:04 | 8.2 | 61.7 |

Stephen's brief went from 337 to 338 words (R3-BM1). The README's range sentence, "After round 2 the eight run 336 to 338 words, about 2:04,", still matches all eight scores, so it was not changed. All pass FK ≤ 10 and Flesch ≥ 60.

quotes.py: bad 2, the two known hits (the al-Tabari Evetts quote with a folio mark, and the Ishoyahb card regex artifact).
