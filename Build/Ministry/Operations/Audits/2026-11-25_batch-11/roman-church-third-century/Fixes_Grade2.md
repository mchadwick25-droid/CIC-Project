# Fixes from the second batch grade: roman-church-third-century

Source of the findings: `Grades2/Held_Findings.json` (roman-church-third-century, two "missing why" bare statements, weight 2, decided by both readers), under Mark's ruling "make fixes" (Decision-Log, "Batch 11: second-grade fixes"). `Grades2/listener.md` gives this story 0 blocking; its drift note (the marriage rule) is not a finding in this pass. Only the two fixes below were asked. The brief, outline and sheet are not edited here; these are the exact replacements to apply.

Count: the live brief is 675 words (`wc -w`), the cap. With every change below applied to a scratch copy it is **675** (`wc -w`). `python3 -m engine.m1.profile_readability --report` on that copy: 673 by its count, grade 8.3 (names out 7.3), reading ease 75.7, 18.7 words a sentence, longest sentence 35 words, pass (live brief: 673, grade 8.5, 75.3, 19.2, longest 36, pass).

Abbreviations as in `Source_Sheet.md`: E = `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` (McGiffert, 1890); H = `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` (ANF 5, Wallis, 1886); CyL = `cic/texts/cyprian_epistulae-lat_hartel1871-csel3-tei.txt` (Hartel, CSEL 3.2, 1871). Every line below was re-read in its file.

## What the sources hold

**1. Why did Natalius give in?** The held source gives a reason, in its own writer's voice. The Little Labyrinth, an anonymous writer "in our own day" (E 32223-32224; sheet Z2), quoted by Eusebius, Church History 5.28. Contemporary; Documented as the writer's account; the scourging is his wonder and stays in his voice (sheet Z3; outline "Angels scourged Natalius, as fact" row).
- E 32252-32256: "When he had thus connected himself with them, he was warned oftentimes by the Lord through visions. For the compassionate God and our Lord Jesus Christ was not willing that a witness of his own sufferings, being cast out of the Church, should perish."
- E 32258-32262: "But as he paid little regard to the visions, because he was ensnared by the first position among them and by that shameful covetousness which destroys a great many, he was scourged by holy angels, and punished severely through the entire night."
- E 32267-32268: "Thereupon having risen in the morning, he put on sackcloth and covered himself with ashes".
The Greek of Book V is not held (sheet line 9); McGiffert's English, printed 1890, stands behind it. The brief tells it in the narrator's words, credited to "a writer of his day". "Ignored" renders "paid little regard"; "whipped" renders "scourged". The sentence follows the source's own order: visions, ignored, the night's scourging, then the morning's penance.

**2. Why did the confessors come back?** The held sources give a reason, in Cornelius's voice and in the confessors' own words as Cornelius reports them. Own words; Cornelius hostile to Novatian; Documented as their account.
- Cornelius to Cyprian (Hartel Ep. 49.1; ANF Ep. 45.1). CyL 6750 with 6776: "circumuentos se esse / adfirmarunt" (they affirmed that they had been deceived); ANF's English, H 32980-32981: "they affirmed that they had been deceived". An original in a clean held print; English printed before 1931 agrees.
- The same letter, the confessors' own words (Hartel 49.2). CyL 6831-6832: "nos errorem nostrum confitemur. inposturam passi sumus. circumuenti sumus perfidia et loquacitate captiosa." H 33018-33019: "We confess our error; we have suffered imposture; we were deceived by captious perfidy and loquacity."
- The same letter's opening (Hartel 49.1). CyL 6731-6735: "cum cognito suo errore et intellecta hominis maligni ... astutia uenenata ad ecclesiam unde exierant ... uenerunt"; H 32960-32963: "acknowledging their error, and perceiving the poisoned cunning of the malignant man ... came back".
- Cornelius to Fabius, in Eusebius 6.43.6. E 38451-38458: "these men found him out and detected his craft and duplicity, his perjuries and falsehoods, his unsociability and cruel friendship. And they returned to the holy church ... And this they did with lamentations and repentance, because through the persuasions of the crafty and malicious beast they had left the church for the time." Later (Eusebius, about 75 years) quoting Cornelius's own words.
The brief says only what the confessors themselves said: they had been deceived. Who deceived them is clear from the sentence ("sided with Novatian") and is Cornelius's charge, so it is not added as narration.

## Brief changes

| # | Old | New | Words |
|---|-----|-----|-------|
| 1 | "make him their paid bishop. Then he put on sackcloth" | "make him their paid bishop. A writer of his day says he ignored warning visions, so holy angels whipped him all night. Then he put on sackcloth" | +17 |
| 2 | "That year, too, the confessors who had sided with Novatian came back." | "That year, the confessors who had sided with Novatian came back, saying they had been deceived." | +5, −1 ("too"; counted under Cuts, item g) |

New sentences: 17 words (fix 1); 16 words (fix 2). Both under 25, each one thought, in time order.

## Cuts and where each goes

The fixes add 22 words. 22 come out. None is from the heart, the record's force, a Never-cut line (`Outline.md` line 250), a credit, a quote, or an explanation Part 1 requires.

| Item | Old | New | Words | Goes to |
|------|-----|-----|-------|---------|
| a | "Zephyrinus's right hand was Callistus, who had been a slave and, Hippolytus says, was sent to the mines for disturbing a synagogue." | "Zephyrinus's right hand was Callistus, who had been a slave." | −12 | **Leave out** (`hippolytus-of-rome` tells the synagogue and the mines; the slate tells Callistus's side, not Hippolytus's charges again; `Outline.md` line 186 allows "who had been a slave" alone) |
| b | "whom a Christian woman of rank might marry" | "whom a woman of rank might marry" | −1 | **Leave out** (wording) |
| c | "out of the church's fellowship." | "out of the church." | −1 | **Leave out** (wording; the plain sense of being cut off stays) |
| d | "Some years after Callistus's time, as a historian of the next century tells it," | "Some years after Callistus, as a later historian tells it," | −4 | **Leave out** (wording; the credit and its later witness kind stay) |
| e | "from terror or the fear of men" | "from terror or fear of men" | −1 | **Leave out** (wording) |
| f | "Novatian, an elder of Rome, held" | "Novatian, an elder, held" | −2 | **Leave out** (Rome is the story's setting throughout) |
| g | "That year, too," | "That year," | −1 | **Leave out** ("that year" stays, as beat 7 requires) |

Net: +22 − 22 = 0. 675 stays 675.

Considered and not taken: "to Carthage's clergy" (Cut first 15 keeps it); "and set Fabian on the bishop's seat" (the outline's own wording when the dove is cut, line 165); "set up against the first" (explains the second bishop); "the church's shared bread and cup" (explains communion).

## Outline and sheet lines to change

`Source_Sheet.md`:
- Line 45 (Z3). Old: `| Z3 | Warned in visions, then (the writer says) scourged by holy angels all night | E 32252-32262 |` ... `"he was scourged by holy angels, and punished severely through the entire night." |`
  New: `| Z3 | Warned in visions; he paid them little regard; then (the writer says) scourged by holy angels all night | E 32252-32262 |` ... `"he was scourged by holy angels, and punished severely through the entire night." ; "But as he paid little regard to the visions, because he was ensnared by the first position among them and by that shameful covetousness which destroys a great many" (32258-32261) |` (the other cells unchanged).
- New row after line 115 (N7):
  `| N7a | Why the confessors came back: they said they had been deceived; Cornelius says they found Novatian out | CyL 6750, 6776; CyL 6731-6735, 6831-6832; H 32960-32963, 32980-32981, 33018-33019; E 38451-38458 | own words (Cornelius to Cyprian; the confessors through Cornelius); later (Eusebius quoting Cornelius to Fabius) | Documented as their account (Cornelius hostile to Novatian) | "circumuentos se esse / adfirmarunt" ; "nos errorem nostrum confitemur. inposturam passi sumus. circumuenti sumus perfidia et loquacitate captiosa." ; H: "they affirmed that they had been deceived" ; E: "these men found him out and detected his craft and duplicity ... And they returned to the holy church" |`

`Outline.md`:
- Line 120 (Ending 1). Old: "The confessors who had sided with Novatian came to the elders and five bishops and asked that what they had done be forgotten (N7)." New: "The confessors who had sided with Novatian came back, saying they had been deceived (N7a), came to the elders and five bishops and asked that what they had done be forgotten (N7)."
- Line 237 (Cut first 24). Old: "keeping that he had been a slave and, Hippolytus says, was sent to the mines for disturbing a synagogue, about 8 words: **for the card**." New: "keeping that he had been a slave, about 8 words: **for the card**. The synagogue and the mines, about 12 words more, are **Leave out** (second-grade fix; `hippolytus-of-rome` tells them)."
- Line 240 (Cut first 27). Old: "27. Natalius warned in visions and beaten all night by holy angels, the writer's credit, and his welts (Opening, Z3), keeping the sackcloth and ashes, the bishop's feet, clergy and people, and "scarcely taken back", about 24 words: **for the card**." New: "27. Natalius's welts (Opening, Z4), keeping the sackcloth and ashes, the bishop's feet, clergy and people, and "scarcely taken back", about 7 words: **for the card**. The visions he ignored and the angels' scourging, with the writer's credit, stay in the brief (second-grade fix, Z3)."
- After line 248 (Cut first 32), a new item: "33. Second-grade fix pass (2026-11-25), after the two reasons add 22 words: "Christian" before "woman of rank" (essence); "'s fellowship" after "the church" (beat 2); "Callistus's time" becomes "Callistus" and "a historian of the next century" becomes "a later historian" (beat 5); "the" before "fear of men" (beat 6); "of Rome" after "Novatian, an elder" and "too" after "That year" (beat 7, Ending), about 10 words: **Leave out**."

## Totals

Applied: 2, both with content from held sources (Z3 already on the sheet, extended; N7a new). Cuts: 7 edits, 22 words, all Leave out. Not applied: none. Nothing reaches past the sources.
