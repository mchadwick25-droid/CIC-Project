# Fresh check: Hippolytus of Rome

Targeted check of the fixes in `Fixes_Fresh.md` against `Outline.md` (lines 35, 36, 59, 155, 201) and the cited files in `cic/texts/`. Nothing else was rechecked.

## 1. New or changed outline lines hold at their sources: PASS

- **Easter clause** (Words row line 35, beat 5 line 59): "a day over which Christians differed, some keeping the moon's fourteenth day".
  - EUS 31136-31140 (V.23.1): "the parishes of all Asia, as from an older tradition, held that the fourteenth day of the moon ... should be observed as the feast of the Saviour's passover"; EUS 31217-31222: "it was not the custom of the churches in the rest of the world to end it at this time". Holds: some kept the fourteenth day, others did not.
  - RG 17504-17509 (VIII.18): "συνιστάνουσι δεῖν τὸ πάσχα τῇ τεσσαρεσκαιδεκάτῃ τοῦ πρώτου μηνὸς φυλάσσειν ... ἐν ᾗ ἂν ἡμέρᾳ ἐμπέσῃ" (OCR "τεσσαρεῦκαι-δεχάτῃ", "ἐν ἡ"); my rendering: "they insist that the Passover must be kept on the fourteenth of the first month, according to the law's ordinance, on whatever day it falls". HIP 13066-13075 agrees. Holds for his own day.
  - "Moon's" is Eusebius's word, not Hippolytus's ("of the first month"); the clause credits no one, so it is fair. "Christians" covers both witnesses (Eusebius's churches; Hippolytus's party, which he counts as heretics); it does not say the dispute was settled or that his table was made for it. The outline marks it "never as the reason he made it". Adds nothing.
  - Confidence **Documented**: right (an old witness's report and his own words).
- **Novatus** (Words row line 36; Do not say line 155): "the split that Novatian's party made from the church at Rome in 251".
  - LP 66825-66826: "supervenit Novatus ex Africa et separavit de ecclesia Novatianum"; LP 66891-66893 (under Cornelius, "Decio [III] ... usque Gallo et Volusiano"): "Novatus extra ecclesiam ordinavit Novatianum in urbe Roma". Rome's list makes the split of Novatus and the split of Novatian's party one event, in Cornelius's time, from 251. So the gloss holds without saying whom Damasus meant.
  - LP 66806-66807: the exile "Severo et Quintiano cons. [235]". 235 to 251: sixteen years, arithmetic on the list's dates.
  - LP 109159-109160 (Damasus): "presbyter in scisma semper mansisse Novati". "Novatus" stays in his mouth.
  - Confidence: the gloss is **Documented** (the list); Damasus's claim stays Contested, as hearsay. Right.

## 2. Cut first 12: PASS

- Noetus's question is not in the heart (line 7), the Also told list (line 8) or the Never cut list (line 202). Cut first 6's "keeping his question" is overridden by 12 itself, stated.
- The opening keeps Noetus's teaching and the expulsion, so the question he raised still stands before the essence. Who (Noetus, then Hippolytus) and where (Smyrna; Rome) come in the first sentences; when ("the early 200s") comes in the third sentence, as before the cut. The cut does not change that. The barred Modalist Monarchianism quote is now not even narrated, which is safer.

## 3. Exact brief changes: PASS

For `hippolytus-of-rome.brief.txt`, apply word for word:

**a. Opening (Cut first 12; minus 11 words)**
- Old: "Twice the elders, the church's priests, called him before the church, where he asked what harm he was doing by glorifying Christ, and they put him out."
- New: "Twice the elders, the church's priests, called him before the church, and they put him out."

**b. Easter table (beat 5; plus 11 words)** — split in two, as `Fixes_Fresh.md` invites, so no new sentence runs past 28 words:
- Old: "He drew up a table, on a cycle of sixteen years, for finding the day of Easter, and Jerome says it gave Eusebius the occasion for his own nineteen-year cycle."
- New: "He drew up a table, on a cycle of sixteen years, for finding the day of Easter, a day over which Christians differed, some keeping the moon's fourteenth day. Jerome says it gave Eusebius the occasion for his own nineteen-year cycle."

**c. Novatus (fresh read's wording; minus 1 word)**
- Old: "Novatus is his name for Novatian, whose party split from the church at Rome in 251, sixteen years after the exile, refusing to take back those who had given way in persecution."
- New: "This was the split that Novatian's party made from the church at Rome in 251, sixteen years after the exile, refusing to take back those who had given way in persecution."

**Count after a-c** (applied to a scratch copy, brief untouched): `wc` 674 (from 675); `python -m engine.m1.profile_readability`: 672 words, grade 8.7 (names out 7.3), reading ease names out 77.6, 19.8 words a sentence, longest 35 (an existing sentence, not one changed here) — pass. At or under 675.
