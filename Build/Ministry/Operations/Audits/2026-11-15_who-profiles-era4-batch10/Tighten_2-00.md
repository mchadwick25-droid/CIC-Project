# Tightening to 2:00: era 4 Who batch 10

After round 1, under Mark's restated length rule (2026-11-15), three fresh Opus agents tightened the seven briefs toward 2:00, about 325 words. This is a change log, not a review round. The worker then took Stephen the Younger from 337 to 328 words and Nikephoros of Constantinople from 362 to 330: in Stephen's, the exile and the coin scene share one sentence, and the two chroniclers' shared charge is told in one sentence; in Nikephoros's, Ignatius's confession and the laying of the body in the Holy Apostles are cut, both kept on the card, and Theophanes the priest is named as a priest and abbot, as the card names him. Round 2 reviews all tightened text in full.

---

## Tighten A: theophanes-the-confessor, stephen-the-younger, nikephoros-of-constantinople

## theophanes-the-confessor: 363 -> 328 words (about 2 minutes). FK 6.78 -> 7.33, Flesch 73.22 -> 70.15
- Cut "the monk and abbot" from the who-line (P5 still has him become a monk; card knownFor keeps abbot).
- Merged Goar's two birth placings into one sentence: "dates his birth to about 751 or 752, or to 744 by Theophanes's own figures" (both are Goar's, THEOPH l.332-337).
- "The Life says that on his wedding night" -> "On his wedding night, the Life says"; dropped "angry" from "Her angry father" (the Life says the father angered the emperor; "angry" was unearned).
- Cut the Nicaea donkey ride ("When the bishops met at Nicaea in 787, he rode there..."). Card `place` keeps "Nicaea, in 787". Merged the monk sentence into the marriage paragraph, subject named "Theophanes".
- Merged "Leo the Armenian later attacked the holy images of Christ, his Mother and the saints. Then he sent for..." into one sentence; "for two years" -> "two years".
- Split the death and dating sentences into their own paragraph (no words cut).
- "His preface says that George" -> "His preface says George".
- No README exception.

## stephen-the-younger: 365 -> 337 words (about 2 minutes 5 seconds). FK 7.18 -> 7.25, Flesch 65.60 -> 66.97
- Merged the council and Callistus sentences; "to have Stephen sign the ruling" -> "to have Stephen sign".
- "Back from exile, after the scene with the coin, Stephen was held" -> "After the scene with the coin, Stephen was held" (the prior sentence gives the exile).
- Cut the four death-date placings (Life 28 November, fifty-third year; Theophanes 20 November; Fabricius 766; Migne's editors 767). The brief now gives no day or year, so nothing reads settled; the card's `dates` and `uncertain[2]` keep all four and the Regius variant.
- The "accused of drawing people into the monastic life" side (why he was killed) is kept, now in two sentences: Theophanes the Confessor, a chronicler, says...; "So does Patriarch Nikephoros of Constantinople, in his Short History."
- No README exception.

## nikephoros-of-constantinople: 365 -> 362 words (about 2 minutes 15 seconds). FK 8.16 -> 8.62, Flesch 61.92 -> 61.69
- Moved the exile placings out of the middle of the night scene to after it, compressed: "The Bollandists, editors of saints' Lives, date the exile to 815, or in one note to 814, and Jacques Goar, Theophanes's editor, to 816." All three placings kept.
- Cut "before holding any church office" from the Nicaea sentence (the next paragraph says "while still a layman").
- No other cut. A 2:00 version would lose the Joseph synod and Theodore's break; README exception line added under "Majors and lengths".

## Checks
- Every changed sentence reread against records.json and the vendored lines where wording moved (THEOPH preface l.3731, l.3954-3967, l.4141-4211; PG100 Life of Stephen l.96955-96984; PG100 Oratio l.11733-11775).
- No sentence over 25 words. No new facts. Audio scripts rebuilt and equal their briefs with the two tags. Card briefLength updated (Theophanes, Stephen; Nikephoros unchanged).

---

## Tighten B: nicholas-mystikos, peter-of-sicily

No README exception lines: both land at about 2:05, which I take to be inside "aims at 2:00". Cards' briefLength set to "about 2 minutes 5 seconds". Audio rebuilt by script ([calmly] first paragraph, [warmly] last); the old audio matched the rule before the rebuild. No card text other than briefLength changed. No sentence runs past 24 words.

## nicholas-mystikos: 366 -> 339 words. FK 6.56 -> 7.07, Flesch 72.76 -> 70.19
- Scene: "Guards with swords, bows and shields stood over him, and he slept on straw in the winter cold" -> "Armed guards stood over him in the winter cold, and he slept on straw" (this removes a second triad right after the clothes/bedding/book one; "Hiemis rigorem ... custodum violentiam ... super palea", PG111 l.14403-14408).
- "The chronicle that carries on from Theophanes the Confessor" -> "that continues" (identifier kept).
- "Nicholas writes that he begged Leo" -> "Nicholas begged Leo, he writes,"; "for a single day" -> "even for a day" ("ne unum quidem diem").
- De Boor paragraph rebuilt: "Nicholas wrote all this to win the pope over, says Carl de Boor. De Boor edited the other side's account, the Life of Euthymius, who replaced Nicholas as patriarch." Cut "It was written in 921 or later" (the card's uncertain[0] keeps "no earlier than 921"). The partisan marker "the other side's account" is kept.
- "Leo was handed a treasonous letter" -> "a treasonous letter from Nicholas to a rebel general reached Leo" (DEBOOR l.6041-6058).
- The two 906 sentences merged: "By de Boor's reading of the Life, Nicholas offered to readmit the emperor in 906, then turned him away at Christmas and Epiphany." Cut "and the boat" from "The banquet followed on 1 February 907" (DEBOOR l.6033-6035, l.9246-9248).
- Close: "On his knees before Leo, he had told him ... His deeds, he said, should match the written law" -> "Once, on his knees, he had told Leo that a king is called an unwritten law, whose deeds should match the written law" (Letter 32 l.14028-14029, l.14093-14097).
- Kept: both legates sentences (R1-B5), the Zoe Karbonopsina identifier (R1-M2), "no compelling proof" (R1-M3), "as bridegroom and priest" with "Nicholas says" (the point is contested).

## peter-of-sicily: 365 -> 334 words. FK 7.32 -> 7.16, Flesch 65.48 -> 65.48
- Cut "at the start of his reign" from the Basil sentence. "In Basil's second year" still carries the date, and the card's `dates` keeps it.
- Cut "Basil took the throne in September 867, so" and merged the Gieseler paragraph into the one before: "J. C. L. Gieseler, who edited the History in 1846, dates the embassy to 868. He says that is all we know of Peter for certain." The card's `dates` keeps the accession, 24 September 867.
- Cut "He says he learned this from Paulicians he talked with and from orthodox Christians in the city." The card's uncertain[0] keeps it. The opening scene still has him talking with them, and "hostile polemic" still marks the History.
- Kept: the R1-B6 Rački close, the R1-B7 order sentence, the R1-M6 wheat sentence, R1-M7's sect sentence and Montfaucon's other side.

## Round 2 (the worker asked for 328 or less)
Both cards' briefLength is now "about 2 minutes". The audio was rebuilt. No README exception lines.

### nicholas-mystikos: 339 -> 328. FK 7.13, Flesch 69.03
- "Nicholas writes that the bishops would baptize ..., and Leo swore he had" -> "The bishops, Nicholas writes, would baptize the boy only if Leo sent Zoe away. Leo swore he had."
- "honored as an empress" -> "honored as empress".
- The plea paragraph now follows Nicholas's own account directly, as "He begged Leo ..." (the "he writes" is no longer needed).
- De Boor paragraph: "... says Carl de Boor, who edited the other side's account, the Life of Euthymius. Euthymius replaced Nicholas as patriarch."
- The chronicle sentences moved to just before the 906 paragraph, so the ban leads into the readmission. They were merged into one: "The chronicle that continues Theophanes the Confessor says Nicholas barred Leo from church, and names a priest, Thomas, deposed for blessing the marriage." (PG109 l.33529-33538: "officio depositus"; "ingressu Leoni interdixit").
- "So, de Boor finds, did legates of the eastern patriarchs" -> "did those of the eastern patriarchs".
- "came back" -> "returned".

### peter-of-sicily: 334 -> 326. FK 7.05, Flesch 65.73
- "boast that they would send some of their own" -> "boast of sending some of their own".
- "Peter stayed nine months, and the exchange was made" -> "He stayed nine months, and the exchange came".
- "that the Paulicians curse Mani" -> "that they curse Mani".
- Cut "often in other words" from the Photius sentence. The card's "Whether Peter followed Photius" item keeps it.

---

## Tighten C: michael-keroularios, ilarion-of-kyiv

No exceptions: both now about 2:00. No README line added. briefLength set to "about 2 minutes" on both cards; audio scripts rebuilt and diffed against the briefs.

## michael-keroularios: 363 -> 327 words; FK 6.8 / Flesch 69.6 (before 6.7 / 70.8 per R1)
- Cut "His brother could not bear the parting and died suddenly." and "kept apart from his brother" (P3 now "He was exiled and made a monk."). The brother stays on the card (2 mentions).
- Cut "They handed him a sealed letter, and he found the seal tampered with." In the brief the clue led nowhere. Not on the card. The records claim on letter I still carries it untagged; the worker may want to tag it "(records only)".
- Cut "he adds" (P1, attribution carried by "Psellos writes"), "being" (led away), "own" (his own letters), "once" (spoke too boldly), "that" (Sathas says instead he...).
- Close: "to teach us and to persuade us" -> "to teach and persuade us" (Latin "ut docerent ac nobis persuaderent", WILL l.17813-17815). R1-M14's "or to debate" sentence kept.
- Kept untouched: R1-B8 "the future patriarch", R1-B9 sentences, partisan marker and Sathas's charge line, "hostile sentence", both death versions with "before the court".

## ilarion-of-kyiv: 363 -> 326 words; FK 6.9 / Flesch 66.7
- Cut "Its Laurentian copy, in Old Russian, calls him a Rusin, a man of Rus." It stays on the card, uncertain[4].
- Cut "It prays for Yaroslav and his wife Irina as living, so the foreword places it before her death in 1050." It stays on the card, uncertain[2].
- "Ilarion left a confession of faith in his own name. He signs it..." -> "Ilarion left a confession of faith. He signs it..." (the signature carries "his own name").
- "the foreword notes" -> "the edition's foreword notes": the first mention of the foreword now ties it to the 1844 edition (+2 words).
- Kept untouched: R1-B1 George/1072, the "No source used here gives his birth" caveat (card uncertain[0] still opens on it), R1-M1 Antony wording, R1-M3 both sides of the consecration question, R1-M4 manuscript sentence, Mouravieff's identifier.
