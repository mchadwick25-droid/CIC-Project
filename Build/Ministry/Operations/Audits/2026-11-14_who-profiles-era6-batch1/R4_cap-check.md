# R4 cap check: era 6 batch 1

One targeted Opus check of only the strings changed after round 3, under Mark's standing ruling of 2026-11-14 (Decision-Log, "Minor round 3 fixes to reader-facing text get one targeted check without asking Mark"). It does not count toward the cap.

## Era 6 Who batch 1, R4 cap check

**Method.** Fresh reviewer, no earlier round seen beyond R3_changes.md and the R3 fix wordings. Scope: `git diff --word-diff 76546a3e 622eb317` on the batch folder (cards, Tauler brief and audio, README; records.json read only for witness lines). Each changed string was read against its source lines in `cic/texts/`, in context. Checked for: what the source says (hedges, "only/alone", witness, pronouns); writing (AI tells, "X, not Y", colon-reveal, sentence length, American spelling, names placed at first card mention). The Tauler brief was scored with `engine.m1.gates.grade_text`, its words counted, and the audio script compared by script with the brief plus its two cues. No repo file but this one was written. No web, paid or model calls.

**Per string**

1. Grote card, uncertain item 1 (Busch's talk and the plague; Kempis's rule): CLEAR.
   - BUSCH l.15349-15369: Florens asks Grote what harm it would do if he and the copyist clerks pooled their weekly earnings and lived in common; Grote fears the begging friars, then says "In nomine domini incipiatis"; they "communem vitam ... inchoaverunt". "The talk with Florens Radewijns that began the common life" is right. FOUNDERS l.1173-1178 is Arthur citing Busch, so "Busch alone" holds among the held witnesses. Radewijns is placed earlier on the card.
   - BUSCH l.15805-15818: Grote is asked to visit "quendam suum fidelem amicum ... Lambertum Stuerman", touches his pulse and feels the plague poison enter. "His friend" is Grote's ("suum"). "He alone" points back to Busch, the subject of the sentence before. Kempis gives no cause (FOUNDERS l.3886-3889, "smitten by the bolt that must fall upon all men"; CHRON l.3785, "in the time of the pestilence"), so "alone" holds and the item's last sentence still stands.
   - FOUNDERS l.3818-3822: "if any should wish to abide continually together, they should earn their own living by the labour of their hands, and, as far as might be, live in common under the discipline of the Church." "As far as they could" keeps the hedge. The dropped "under the discipline of the Church" is not a hedge.
   - Sentences of 14, 12 and 11 words. No AI tells.
2. Kempis card, place (Bethany): CLEAR.
   - CHRON l.2010-2024: John of Kempen "ended his life happily in a good old age and in obedience in Bethany"; Thomas closed his eyes. "Where his brother John died, his Chronicle says" is right, and the Chronicle does not itself place Bethany near Arnhem.
   - DUTHOIT l.761-763: John "died in 1432 at one of them, the convent of Bethania near Arnheim". "William Duthoit places the convent near Arnhem" credits the right witness. "The convent" clearly means Bethany. Duthoit is placed earlier on the card (dates). "Arnhem" is the modern form, outside a quotation.
3. Julian card, uncertain "When she died": CLEAR.
   - DALGAIRNS (hilton_scale-or-ladder-of-perfection_dalgairns1908.txt) l.2853-2854, 2876-2878: "the close of Mother Juliana's life.*" with the note "* Blomfield, 546. All that is known is that she was alive in 1443, but was a hundred years old." The card's sentence follows it closely; "at a hundred" renders "was a hundred years old". "Of his" points back to Dalgairns, the sentence's only man. "Citing Blomefield" uses the card's spelling of the name, which Dalgairns spells "Blomfield"; the note does cite him. The earlier "says only" is gone. 21 words.
   - The sentence before (DALGAIRNS l.1785-1788, "as she appears to have died in 1443, she must have lived to be a hundred") is unchanged and still fits.
4. Suso card, uncertain "The chapter that accused him": CLEAR.
   - BIHL l.6673-6675 (footnote): Denifle 98 for the general chapter at Bruges 1336; "Preger, Mystik II, 330 [OCR '33tl'] 360 und Seeberg 144 für das Provinzialkap. von Herzogenbusch 1335". "Bihlmeyer adds that" keeps the report his. "Chose" fairly renders "entschieden ... für".
   - LANG l.263: "Preger, Geschichte der deutschen Mystik. II. Leipzig 1881" places "his history of German mysticism". No held line gives Preger's first name, so the bare surname is right.
   - BIHL l.4885-4887: "R. Seeberg, Ein Kampf um jenseitiges Leben, Lebensbild eines mittelalterlichen Frommen (Seuse) ... Dorpat 1889, 148 S." Bihlmeyer's page 144 falls in that 148-page book, not in the 1906 reprint (pp. 188-246). So "in an 1889 life of Suso" names the right book. "His" is Preger's. 23 words, two short insets, under the cap.
5. Tauler brief paragraph 3 and audio: CLEAR.
   - EVANS l.1-9 (title page and content note): Pfeiffer's text "translation with some omissions and additions", vol. I, 1924. "Sermons of Meister Eckhart" no longer claims all of them. "In the 1920s" holds. EVANS l.459, 539: "Tauler (1300-1361)", so "gives 1300" is right. "A fellow Dominican" follows "a Dominican friar of Strasbourg" and reads as Tauler's fellow. 20 words.
   - The audio script equals the brief with "[calmly] " at the start and "[warmly] " at the start of the last (seventh) paragraph, checked by script: equal.
6. README, Card traditions, Eckhart sentence: CLEAR.
   - EVANS l.496-498: "The first known mention of his name is in a list of Professors at the University of Paris : fr. Echardus Tutonicus, licentiatus per Bonifacium, 1302." "The first known mention of him in Evans" keeps "known" and names the witness. It could just be read as "the first place Evans mentions him". The sentence's claim that the 1302 list falls inside the entry is true under either reading, so this is not a finding. If the line is ever touched again, "the first known mention of him, Evans says," would close it.

**Briefs against the gates**

| Brief | Words | FK | Flesch | Gates (FK at most 10, Flesch at least 60, about 405 words) |
|---|---|---|---|---|
| johannes-tauler | 404 | 7.17 | 68.00 | Pass |

The other seven briefs did not change after round 3 and were not rescored.

**Notes outside the changed strings (not counted, non-blocking).** None.

**Verdict: CLEAR.** All six changed strings match their sources, keep their hedges and witnesses, and meet the writing bar. The Tauler brief passes the gates at 404 words, and its audio script matches. No fix is required.
