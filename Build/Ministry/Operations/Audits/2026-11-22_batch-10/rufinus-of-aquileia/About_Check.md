# rufinus-of-aquileia: "What it was about" check

**FIX**

Every cited line was opened in `cic/texts/` (N202, N203, N206). The charges against Origen come from his opponents. Each is credited to the opponent: "a bishop from Cyprus charged that Origen taught ..." (Epiphanius, Letter 51.4-5, N206 10810-10818, 10874-10901), "Jerome said" (Letter 124.2, N206 24685-24693), and "the bishop of Rome wrote" (Anastasius, N203 46160-46166, 46202-46207). None is told as Origen's own teaching. Rufinus's answer is credited as his own statement (N203 45986-45993, 46006-46012). The sides in the 390s dispute (N203 46253-46262) and the edict of Valens (N202 13720-13742) are as cited. Leave out is sound: the origin of souls (N203 46037-46046) is held, and it is left out for room only. All 11 "already explained" items hold.

Count by `wc -w` and a second regex count on a scratch copy with every Room change applied: 674, as the outline says. With the two fixes below it is 675, which is at the approved 675. No cut takes the heart, the quarrel's force, a needed credit or the Sicily scene. Cut 4 drops the Melania link clause. The sibling slate allows one clause there but does not require it, so this is sound.

## Findings

1. **BLOCKING: a date moved onto the wrong event (item 9, Room line "Item 9").** Letter 124 dates from 409 or 410, ten years after the quarrel (N206 heading, about 24600-24650: "The date of the letter is a.d. 409 or 410"). Jerome's answer at the time (Apology I.6, N203 51288-51291) names only "the impious doctrine ... about the Father, the Son and the Holy Spirit". As written, "In the Greek, Jerome said" places the ranking inside the 399 beat. Replacement for the outline line:
   - Item 9: after "Jerome took the preface as aimed at him.", add "In the Greek, Jerome later wrote, Origen ranked the Son below the Father, the Spirit below the Son." and begin the next sentence "He charged ..." (+19)
   - In What it was about, item 9, change "Explain, in Jerome's answer: in the Greek, Jerome said," to "Explain, in Jerome's later letter (409 or 410): in the Greek, Jerome wrote,".
   - In the Room "After" line, change "678 + 71 - 75 = **674**" to "678 + 72 - 75 = **675**". Change "Explanations add 71 words" to "Explanations add 72 words".

2. **MINOR: plain sense of the persecution (item 5).** "For their faith" can make a listener hear a pagan emperor persecuting Christians. In fact Valens, a Christian emperor, moved against "the orthodox" (N202 13720-13722). The fix keeps the count the same. Replacement for the Room line:
   - Item 5: "When the monks there were persecuted, he says, he was jailed and exiled." becomes "When the emperor turned on the monks there for their creed, he says, he was jailed and exiled." (+5)
   - In What it was about, item 5, change the plain sense to "When the emperor turned on the monks there for their creed".
