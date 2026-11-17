# Fixes R50: Marcion of Pontus

Ruling: Mark, 2026-11-17 ("yes no softening, we are a witness not a judge … for this round 1 but also the should fixes too"). Released text kept as `marcion-of-pontus.r50.brief.txt`.

## Fix-list items

1. **Cut the narrator's verdict after Polycarp's line.**
   - Old: "Irenaeus, who had seen Polycarp in his early youth, tells the story, and it shows how hard the church set itself against this man."
   - New: "Irenaeus, who had seen Polycarp in his early youth, tells the story."
   - Source: M8 (ANF 39882–39884; "whom I also saw in my early youth", ANF 39860).

2. **Do not call one side "the church" while Marcion's churches are in the story; name who answered him.**
   - Old: "The church answered him in book after book, arguing that one God made the world and sent Jesus. Irenaeus defended four Gospels against him, Tertullian wrote five books, and Polycarp, Irenaeus says, turned many back at Rome."
   - New: "Writers who opposed him answered in book after book, arguing that one God made the world and sent Jesus. Justin wrote against him in his lifetime, Irenaeus defended four Gospels against him, and Tertullian wrote five books. Polycarp, Irenaeus says, turned many back at Rome."
   - Source: I3 (Justin's book, quoted by Irenaeus, ANF 44907–44917; Tertullian's five books, T 22509–22512), I4 (Irenaeus, four Gospels, ANF 41120, 41142–41150), I5 (Polycarp, ANF 39871–39874). The remaining uses of "church" are particular ("the church at Rome", "the Roman church", "the churches of the Marcionites"), not one side named as the whole.

3. **Do not end on "…as far away as Persia, and elsewhere"; end on Tertullian's wasps line, credited as his.**
   - Old: "Yet Justin saw people of every nation follow Marcion, who founded churches of his own, the churches of the Marcionites. Tertullian wrote that just as wasps make combs, so these Marcionites make churches. Those churches also claimed martyrs of their own. Two centuries later, Epiphanius still found Marcionites in Rome and Italy, in Egypt, Syria and Cyprus, as far away as Persia, and elsewhere."
   - New (now its own paragraph): "Even in Marcion's lifetime, Justin saw people of every nation follow him, and Marcion founded churches of his own, the churches of the Marcionites. Those churches claimed martyrs of their own. Two centuries later, Epiphanius still found Marcionites in Rome and Italy, in Egypt, Syria and Cyprus, and as far away as Persia. Tertullian had mocked them: "Even wasps make combs; so also these Marcionites make churches.""
   - Source: I1 — Justin, ANF 14945–14946 (in his lifetime, S2); Epiphanius, EPI 7464–7473; Tertullian, T 29323–29330 (opened and confirmed verbatim: "Even wasps make combs; so also these Marcionites make churches."). Martyrs: I2 (EUS 29928–29930). "Mocked" credits the line as Tertullian's scorn, per the fix list; it reports the kind of remark (wasps against churches), not a feeling.

## Across-the-set items

- **No softening / no one-side framing:** item 2 removes the narrator's "the church" for Marcion's opponents. Nothing else needed change.
- **Setting stack:** "In the middle of the second century, in the church at Rome, a shipmaster from Pontus, on the Black Sea, gave money in the warmth of new faith." → "In the middle of the second century, a shipmaster from Pontus, on the Black Sea, gave money to the church at Rome in the warmth of new faith." Source: S2, S5 (T 21331–21332), M2, S3.
- **Witness line varied:** "Everything we know of Marcion comes from the men who wrote against him." → "No word of Marcion's own survives; his story comes to us only from the men who wrote against him." Source: sheet note "No word of Marcion's own is held" (T 22580–22581, 29245–29248).
- **"Yet" opening the impact:** the impact no longer uses "Yet"; the Justin sentence now opens "Even in Marcion's lifetime" (S2: "is even at this day alive", ANF 14943–14944).
- **Uncertainty tags:** one remains ("although his real reasons remain uncertain", on Tertullian's reconstruction, M3 — Inferential-Thin). Within the limit of one; left as released.

## Readability

`python -m engine.m1.profile_readability …/marcion-of-pontus.brief.txt`: 379 words (was 374), grade 8.6 (names out 6.8), reading ease (names out) 74.4, 15.8 words a sentence, longest sentence 28 words — pass.

## Quotations added or changed

- **Changed (paraphrase → direct quotation):** Tertullian, *Against Marcion* IV.5, ANF3 printed English, `cic/texts/anf03_tertullian.xml` lines 29329–29330 (cited span T 29323–29330): "Even wasps make combs; so also these Marcionites make churches." Wording as in Outline (What came of him, item 1) and Source Sheet I1. Latin at OEH 8490 ("Faciunt favos et vespae, faciunt ecclesias et Marcionitae"). Needs a second reading.
- Q1, Q2, Q3 unchanged.
