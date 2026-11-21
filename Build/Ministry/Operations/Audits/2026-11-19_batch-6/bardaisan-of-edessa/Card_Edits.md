# Card edits: Bardaisan of Edessa

Card writer, batch 6, 2026-11-19. Existing card: `Card.existing.json` (the census `card` object for `bardaisan-of-edessa`; checked identical to the census). Result: `bardaisan-of-edessa.card.json`. Brief: `bardaisan-of-edessa.brief.txt` (674 words, about 4 minutes 30 seconds at 150 words a minute; `briefLength` is not a census card key, so it is not on the card).

Every existing field is kept word for word and in its order, except the two corrections below.

## Clearly wrong

1. **`datesNote`.**
   - Old: "About 155 to about 223, by later Syriac chronicles"
   - New: "About 155 to about 222, by later Syriac chronicles"
   - Evidence: the chronicle that gives the death, Barhebraeus, says he lived 68 years and died in the year 533 (BHE 4220–4221, "Vixit Bardesanea annos 68, et obiit anno 533"). Holl converts 533 to 221/2 (EPI 26426–26427). The 223 is Hort's figure through McGiffert (EU 26586–26588), not the chronicle's. The brief: "He died about 222, in his late sixties." The card's own `uncertain` line already gives Holl's 221 or 222.

2. **`uncertain`, third line.**
   - Old: "McGiffert thinks Ephrem knew Bardaisan only through his followers, and so judged him more harshly."
   - New: "McGiffert thinks Ephrem knew Bardaisan only through his followers, and so judged him more harshly. But Ephrem says he came upon a book of Bardaisan's, and he answers Bardaisan's Domnus by name."
   - Evidence: McGiffert's claim stands at EU 26574–26577 ("knows him only through his followers ... and hence passes a harsher judgment"), so the line is kept as his view. Ephrem's own texts contradict it: *Nisibene Hymn* 51 in Gwynn's English, "I have chanced upon a book of Bardaisan, / And I was troubled for an hour's space; / It tainted my pure ears" (EPH-G, `npnf213_gregory-great-ephraim-syrus-aphrahat.xml` 11200–11202); and Ephrem's discourse "AGAINST THE DISCOURSE WHICH IS CALLED 'OF DOMNUS,' WHICH WAS COMPOSED BY BARDAISAN AGAINST THE PLATONISTS" (EPH-P, `ephraim_prose-refutations_mitchell1912-1921.txt` 1350–1352). Source_Sheet I2 reaches the same finding, and the outline's Do not say list rules the claim out of the brief. The added sentence uses no quotation marks, so the census quotation check is not engaged.

## New

1. **`sources.about`, six entries added**, after the existing four:
   - John Gwynn's introduction to Ephrem (NPNF 2.13, 1898), with Ephrem's lines in English: the curse on "the Seven" (11261–11270), the book he came upon (11200–11202), the hymns of Bardaisan's school (11241–11247).
   - Jerome, *Lives of Illustrious Men* 33, English (`npnf203` 40139–40151) and Latin, PL 23 (`jerome_opera-pl23-…` 53437–53442): the brief's "a Latin scholar, about 170 years on, called it the strongest of his books".
   - Thomas Smith's introductory notice and notes to the *Recognitions* (same file as the dialogue, 6252–6254, 18279–18281): the brief's "a later Christian book reworked its chapters, most editors judge".
   - The *Chronicle of Edessa*, Cowper's English (line 49): the birth, "about 155".
   - Barhebraeus, *Ecclesiastical Chronicle*, Latin (4220–4221): the death, "about 222, in his late sixties".
2. **`briefReferences`, sixteen lines added**, one for each place the brief draws on: six for the dialogue (the opening scene, BLC 67908–67946; Philip and the pupil's record, BLC 68100, 68337–68342, EU 26622–26629, BLC 67855–67857; the harp, ship and sun, BLC 68006–68071; nature, fate and the astrologers, BLC 68249–68463; the laws of countries and the Christians, BLC 68605–68990; the ending, BLC 69023–69031); the *Chronicle of Edessa* and the river Daisan (CHE 49; EU 26584–26589; BLC 67892–67894; EPH-G 11186–11188); Eusebius IV.30 (EU 26633–26656); Epiphanius, *Panarion* 56 (EPI 26328–26330, 26491–26501); Barhebraeus with Holl (BHE 4220–4221; EPI 26426–26427); the *Recognitions* (REC 6252–6254, 18279–18281); Jerome (as above); Ephrem's *Prose Refutations* (EPH-P 428, 1549, 1937); Ephrem in Gwynn (as above); Sozomen III.16 (SOZ 32079–32103); and the census for Edessa's modern country and the Valentinus and Marcion glosses. None has quotation marks.
3. **`quotationOriginals`, three entries added**, one for each quoted span in the brief. The census card had none, so every span is new and has no `secondReading`. Each printed wording was re-read in the file at its lines.

## Awaiting second reading

| Modern span (brief) | Printed (Pratten, ANF 8) | File and lines |
|---|---|---|
| "So we humans are ruled by nature all alike, by fate each in a different way, and by our freedom each as we choose." | "And thus we men are found to be governed by Nature all alike, and by Fate variously, and by our freedom each as he chooses." | `anf08_…` 68441–68443 |
| "Wherever we are, we are all called by the one name of Christ: Christians." | "for, lo! wherever we are, we are all called after the one name of Christ—Christians." | `anf08_…` 68968–68969 |
| "When that new world is set up, all evil turmoil will cease, and every rebellion will end. The foolish will be convinced, and all that is lacking will be filled." | "And at the establishment of that new world all evil commotions shall cease, and all rebellions terminate, and the foolish shall be convinced, and all deficiencies shall be filled up," | `anf08_…` 69026–69029 |

Notes for the second reading:

- The outline gives Q2 as 68966–68969 and Q3 as 69026–69031. The printed words of the spans the brief keeps stand at 68968–68969 and 69026–69029; the lines cited are those.
- All three are rendered from Pratten's English. The Syriac (Cureton) is not held, so no `original` is given.

## Not found

- `legacy.remembered`, "Ephrem attacked Bardaisan as one of the worst of heretics in his Prose Refutations": the *Prose Refutations* set him with Marcion and Valentinus as the party from which Mani's teaching comes, under the heading "Mani, the last of the great heretics" (EPH-P 955–957), and attack him throughout. The words "one of the worst" are not found as such. Kept.
