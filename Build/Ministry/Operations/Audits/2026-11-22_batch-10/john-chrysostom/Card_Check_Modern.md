# John Chrysostom: card check, modern pass

Checked: `john-chrysostom.card.json` against `Card.pass3.json`, the edit list `Card_Edits.md` "Fourth pass: no modern opinion (2026-11-23)", and `john-chrysostom.brief.txt` as it now stands. Every cited line was opened.

## Verdict: FIX

## What holds

- Nothing moved outside the edit list (diff of the two cards: only the four `uncertain` items and edits 5-9 in `briefReferences`).
- Edits 2 and 4: true at their lines. Freese's note, "The synod (403) ... See Hefele" (Photius 3862-3864). Moore's table, "403. The Synod of The Oak" and "407 (June). Removal to Pityus" (Palladius 678, 706). No year in the march (Palladius 6392-6432). Moore: "anonymous ... generally attributed to Palladius, Bishop of Helen-opolis" (730-731), "nothing except the title to suggest" (754-756), Bigot (900-903). Moore adopts the attribution himself, following Butler (861-893, 905-911).
- Edits 5-9: each matches the brief ("condemned"; no year on the Oak; "He died on the way in 407"; no tradition named; no place on the sermon). Socrates VI.21: 18609-18612. No remaining `briefReferences` entry names wording the brief no longer has.
- `quotationOriginals`: one span, "Glory to God for all things.", printed "Glory to God for all things;" (Palladius 6498-6499). No dropped span. All cited files are in `sources`. No audit named. American spelling.

## Fixes

1. **uncertain[9], the Antiochene item: wrong modern source.** `npnf110` 730-732 is not the Oxford preface. That preface ends at line 596, signed "C. Marriott". Lines 730-732 come from the "Introductory Essay ... By M. B. Riddle, D.D." (598-609). `Card_Edits.md` edit 1 has the same error.
   - Old: "The Oxford editor of the Homilies on Matthew, in his preface, says Diodore 'is reckoned the leader of the so-called Antiochian school of exegetes.'"
   - New: "M. B. Riddle, in his introductory essay to the Homilies on Matthew, says Diodore 'is reckoned the leader of the so-called Antiochian school of exegetes.'"

2. **uncertain[11], the Matthew item: the modern source is not named.** The preface is signed "C. Marriott" (`npnf110` 592).
   - Old: "The Oxford editor of the Homilies on Matthew, in his preface, judges that they were"
   - New: "C. Marriott, the Oxford editor of the Homilies on Matthew, judges in his preface that they were"

3. **The Palladius attribution is still stated as fact in four fields.** These contradict uncertain[12], which marks the identity of the Dialogue's writer with Palladius of Helenopolis as Moore's modern attribution (Palladius 730-756, 895-903). They also contradict the outline's Do not say line from `Fresh_Read_Modern.md` BLOCKING 1. Old sources name only "bishop Palladius" as the writer (Photius, Codex XCVI, 9984-9986), and the brief says only "Palladius, who wrote John's life and took his side".
   - legacy.traces[1]. Old: "Palladius of Helenopolis, a bishop who stood by him, wrote a dialogue on his life and fall, and tells the journey into exile." New: "Palladius, a bishop who took his side, wrote a dialogue on his life and fall, and tells the journey into exile."
   - legacy.remembered[0]. Old: "Honored by Palladius of Helenopolis, who defends him throughout his dialogue," New: "Honored by Palladius, who defends him throughout his dialogue,"
   - uncertain[2]. Old: "Palladius of Helenopolis, who knew him, says he drank no wine," New: "Palladius says he drank no wine," ("who knew him" rests on the same identification; the wine and stomach lines are Palladius 6627-6630.)
   - uncertain[3]. Old: "Palladius of Helenopolis says the soldiers lodged him" New: "Palladius says the soldiers lodged him"

4. **keyWorks[1]: an unmarked modern date.** "387" comes from the Benedictine preface to the Statues (Montfaucon, after Tillemont), printed in `npnf109` 22378-22420, and from Schaff's Prolegomena, "They were preached during Lent 387" (1264). That preface records Baronius, Petavius and Valesius for 388, and says that Sozomen's and Theodoret's account puts the riot after the war against Maximus (22378-22392).
   - keyWorks[1].about. Old: "twenty-one sermons from the weeks of fear in Antioch in 387" New: "twenty-one sermons from the weeks of fear in Antioch"
   - uncertain, new item at the end: "The year of the Homilies on the Statues is a modern date. The Benedictine editors, following Tillemont, date the riot and the sermons to 387, and Schaff gives Lent 387. Baronius, Petavius and Valesius put them in 388, and the old historians Sozomen and Theodoret tell the riot as after the war against Maximus. These are modern judgments."

5. **briefReferences: the brief's "who wrote John's life" has no reference.** Add after the hospital entry, so it reads: "Photius, Library, Codex 96, tr. Freese: George of Alexandria drawing on bishop Palladius, who wrote a life of Chrysostom in the form of a dialogue." Evidence: Photius 9959-9986. The file is already in `sources.about`.

Claims not found: none new.
