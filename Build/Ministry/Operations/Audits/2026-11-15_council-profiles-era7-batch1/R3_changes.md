# Round 3 changes: era 7 council profiles, batch 1 (2026-11-15)

Round 3 was the last round under the cap. The worker applied its points itself; the Chanforan blocking point went first to Mark, whose cap ruling ("A", 2026-11-15, relayed by the coordinator) ordered it applied as the reviewer worded it, with its two minors and Worms's two minors, then one targeted check of only those strings (`R4_cap-check.md`). The check does not count toward the cap.

## Part A, Diet of Worms

- **A3-M1. Applied.** Records `claims[60]` witness now `pallavicino_istoria-del-concilio-di-trento-parte1-ita_1664.txt l.10137-10178` ("come notorio eretico" is at l.10178). `contested_claims[2]`, Waterworth's side, now `l.1720-1729` (arrival at l.1720 and 1726, "the seventeenth" at l.1729).
- **A3-M2. Applied as worded.** The Aleander absence note adds: "Two 1538 items name him as legate: a letter in Theiner (...l.48761), and ZKG 14's notice of six letters, mostly his, printed by Capasso (...l.24362)." The absence stands; neither item is from Worms.

## Part B, Diet of Augsburg

- **B3-M1. Applied** (before the ruling, as a minor round 3 fix to reader-facing text under Mark's standing cap ruling of 2026-11-14). Entry `record[0].note`: "The Book of Concord's English of the confession was prepared by a joint committee ...", so the committee's work is not read as the whole volume's English (Jacobs translated the Apology).

## Part C, Synod of Chanforan

- **C3-B1. Applied as the reviewer worded it** (Mark's cap ruling). Brief p.8: "Léger wrote in 1669 that the valleys changed nothing at the Reformation, but later went beyond self-defense." (LEG l.23072-23086: their old rule allowed defense "en toute extrémité", kept through the war of Emanuel Philibert; "ils en ayent uzé autrement du depuis".)
- **C3-M1. Applied as worded.** Entry `uncertain[12]` and records contested claim 3: "nothing changed in doctrine or discipline through their talks with the reformers".
- **C3-M2. Applied as worded.** Brief p.2: "in quotations by the historians Alexis Muston and Édouard Montet".
- A note in R3 Part C: `R2_changes.md`'s preface says only Augsburg's audio changed in round 2; Chanforan's changed too, with the worker's brief edit. The audio matches the brief. Recorded here; R2_changes is not edited.

## Brief figures after round 3

| Brief | Words | Spoken | FK | Flesch | Longest |
|---|---|---|---|---|---|
| Diet of Worms 1521 | 399 | 2:30 | 7.12 | 67.17 | 23 |
| Diet of Augsburg 1530 | 400 | 2:30 | 7.91 | 60.26 | 25 |
| Synod of Chanforan 1532 | 400 | 2:30 | 6.99 | 66.50 | 25 |

Audio regenerated with `working/mkaudio.py` and checked equal to the brief plus tags; records re-merged into `era7/records.json`; JSON valid.
