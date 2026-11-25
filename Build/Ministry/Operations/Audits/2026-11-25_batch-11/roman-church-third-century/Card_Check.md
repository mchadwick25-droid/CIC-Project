# Card check: The Roman Church in the Third Century

Checked: `roman-church-third-century.card.json` and `Card_Edits.md`, against `Card.existing.json` (the same as the census entry's fields), the brief, `Outline.md`, `Review.md` and `Fresh_Read.md`, with CLAUDE.md ("Trust and source fidelity"), Kit Part 1, `kinds/tradition.md` and the role.

**Verdict: FIX.** Edits 1 to 10 and the Entry fields stand as written. The fixes below are for check 1 (a modern date, identification or judgment stated as content) and check 6 (something clearly wrong left in). Each one changes only the words named.

## What holds

- **Check 2 (nothing else moved).** A field-by-field diff against `Card.existing.json` finds changes only in `why`, `teaser`, `sourcing`, `voices[1]`, `legacy`, `documentedStories[0].text`, `documentedStories[1].text`, both stories' `sources`/`modernWorks`, and the new `uncertain`, `sources` and `quotationOriginals`. Every one is listed in `Card_Edits.md`. `floorNote`, `relationsSummary`, `people` and every other item are word for word.
- **Edits 1 to 4.** Each is justified. The brief no longer calls Hippolytus learned or a rival bishop (Outline, Do not say; Review B2). "withstood" is at H 13627-13633.
- **Edit 5 (legacy).** R1 and R2 (Ath 28529-28534, 29876-29880), R3 (E 25094-25101) and R4 (Bas 28629-28634) each say what the new sentences say. Re-read.
- **Edit 6.** H 13936 says "whether a slave or free". **Edit 7.** "strengthened and prepared for the spiritual conflict" is word for word at H 41197-41199, and "be found ready" is not in that letter (H 33787 is a different letter).
- **Edit 8.** Brent and Moss moved word for word into `modernWorks`. Each note says what the work covers.
- **Edits 9 and 10.** Every Cut first item marked "for the card" (1-3, 5-16, 18-20, 22-29, 31), Leave out N2, and What came of it 2 and 3 are on the card, in `uncertain`, `legacy` or a `sources` note. I spot-checked the sources notes at their lines: Letter 25 (H 31009-31013), Letter 30 (H 31706-31713), Against Noetus (H 23728-23732), LibCat 66818-66821, Ath De Decretis 26 (28469) and De Sententia Dionysii 13 (29867), and Basil Letter LXX (28591). Hartel 8/49/55 correspond to ANF 2/45/51.
- **Check 3.** The card has no `briefReferences`.
- **Check 4.** There are three `quotationOriginals`, one for each quoted span in the brief. Each `modern` matches the brief word for word. Each `printed` and `englishPrinted` is verbatim at its lines: H 13856-13857; CyL 1129-1133 with H 28856-28860; CyL 6825-6828 with H 33011-33016. Both files are in `sources`. Q1 has no held original, so its English stands alone. Q2 and Q3 carry their Latin. No quote is under six words, so none has `secondReading` and none is "checked at card" (**check 5**: nothing to check). The card names no audit file and uses American spelling.
- **Census run.** I merged the card into a scratch copy of the census, with the brief as `longDescription`, kept outside the repository. `node tools/validate-census.mjs <copy>` gives 629 movements, 736 edges, 0 errors and 4 warnings, all on other entries. As `Card_Edits.md` says, the validator does not check a tradition's `quotationOriginals`, so check 4 above was done by hand.
- **Check 7.** This is a tradition entry with no new census entry, so there is nothing to check.

## FIX

1. **legacy** (Kit Part 1, Explain it: a short text may not name a thing without its plain sense).
   Old: "Athanasius later quoted the letter against the Arians."
   New: "Athanasius later quoted the letter against the Arians, who held that the Son of God was a creature."
   Evidence: Ath 28469 ("that the Word of God is not a work or creature"), the chapter the letter is quoted in.

2. **documentedStories[0].text** (modern identification: the road is an editor's note, H 13805-13806; Outline, Setting and Do not say).
   Old: "to manage the church’s cemetery on the Appian Way, and on Zephyrinus’ death the church elected him."
   New: "to manage the church’s cemetery, and on Zephyrinus’ death he became bishop."
   Evidence: H 13804-13806, "appointed him over the cemetery". H 13816-13819 says only that he "obtained (the position)", and no held line says the church elected him (Outline, Do not say, "the people chose Callistus"). The new wording follows the brief: "When Zephyrinus died, Callistus became bishop".

3. **documentedStories[0].text** (modern identification: "adultery after baptism" comes from Tertullian's unnamed bishop, X2; "senatorial" is not in the held text; Outline, Do not say).
   Old: "he readmitted Christians who had committed adultery after baptism; he recognized as marriages the unions of senatorial women with slaves or free men;"
   New: "he said he forgave all their sins, sins of sensual pleasure among them; he let women of rank count a companion, slave or free, as a husband;"
   Evidence: H 13873-13875 ("indulgence in sensual pleasures, saying that all had their sins forgiven by himself"); H 13934-13938 ("their own dignity ... whether a slave or free ... consider such a companion as a husband"); the brief ("a woman of rank ... take a companion, slave or free, and count him her husband").

4. **documentedStories[0].text** (a modern judgment, told in the narrator's voice; it also says what the brief does not: Zephyrinus took back Natalius before Callistus, and Hippolytus says "slave or free", not "poor").
   Old: "What Hippolytus records as scandal, a later church would recognize as pastoral policy — the first known bishop to say that the church could forgive the gravest sins, and to treat a noblewoman’s union with a poor Christian as a marriage. "
   New: "" (the sentence removed)

5. **documentedStories[0].text** (modern: the list of 354 says Hippolytus was deported to Sardinia in 235. It gives no mines and no death, LibCat 66805-66808).
   Old: "Hippolytus was eventually exiled to the same Sardinian mines under Maximinus and died there;"
   New: "Hippolytus was eventually exiled to Sardinia, in 235;"

6. **documentedStories[0].caveat** (modern identification: "the catacomb that bears his name" is only the editor's note at H 13805-13809; Outline, Do not say).
   Old: " That Callistus was a former slave and administered the catacomb that bears his name is generally accepted."
   New: "" (the sentence removed)

7. **documentedStories[0].sources[1].note** (modern identification: Tertullian does not name the bishop, X2; Outline, Leave out).
   Old: "A second hostile witness to the edict on readmitting adulterers, usually taken to be Callistus’."
   New: "A hostile witness to an edict on readmitting adulterers, by a bishop it does not name."

8. **documentedStories[1].text** (clearly wrong: the held sources contradict it. Eusebius gives Xystus eleven years, E 41758. The list of 354 gives two years eleven months, from 256, LibCat 66908-66911. "Less than a year" rests only on modern reckoning).
   Old: "had been bishop for less than a year, and had spent it repairing the breach"
   New: "had spent his time as bishop repairing the breach"

9. **documentedStories[1].text** (modern identification: Cyprian says only "in the cemetery", H 41184-41186; the road comes from the later finding of Damasus's verse, which is not held).
   Old: "underground burial galleries on the Appian Way where"
   New: "underground burial galleries where"

10. **documentedStories[1].text** (a modern date, and wrong by it: only the editor's note dates Cyprian's death, to September 14, H 27583, 41145-41147, which is more than a month after 6 August).
    Old: " He was himself arrested within the month."
    New: "" (the sentence removed)

11. **voices[5]** (modern date and judgment: the list of 354 runs Dionysius to the consulship of Claudius and Paternus, LibCat 66915-66917, not 268; "the clearest doctrinal statement" is a modern judgment of praise).
    Old: "Dionysius of Rome - bishop 259-268, whose letter against Sabellian and tritheist readings, written into the controversy with his Alexandrian namesake, is the clearest doctrinal statement the Roman see made in this century"
    New: "Dionysius of Rome - bishop from 259, whose letter against Sabellian and tritheist readings, written into the controversy with his Alexandrian namesake, Athanasius later quoted"
    Evidence: LibCat 66915-66916 (Aemilianus and Bassus); R1 and R2.

12. **why** and **legacy** (a modern judgment no old source makes; already listed as not found in `Card_Edits.md`).
    why, old: " Almost by accident, it preserves more about second- and third-century religious movements than any other surviving book." New: "" (removed).
    legacy, old: " In passing, it also keeps more about second- and third-century religious movements than any other surviving book." New: "" (removed).
    The census entry's `why` and `legacy` take the same change (Entry fields).

## Noted, no change

- The outline also sends to the card Stephen's quarrel with Cyprian (Sibling) and Aurelian's ruling at Antioch (Sibling and Links, R6). `Card_Edits.md` does not list either. Both are events shared with sibling stories (Latin Pastoral and Antioch), and the role says "Leave connections to other entries out for now", so they are held for the connections pass. Release should record them so they do not go quiet.
- `modernWorks`: the modern studies used only to find old texts (Source_Sheet, Library sweep: Duchesne, Harnack, Koch, Benson, Poschmann, Bardenhewer) are not on the list, because the sheet does not name which volumes were used. The researcher should name them before release. They are not to be guessed.
- Other claims that cannot be found but are not contradicted stay in place, as the role says. These include "grave sin after baptism", "That is the answer the Western church kept", Lawrence "four days later", "repairing the breach with Carthage", and "Rome venerates both as saints".
- "In the 260s" (legacy) is the outline's dating. The old sources put the letter after 259 and before Dionysius of Alexandria's death, so the dating stands.
