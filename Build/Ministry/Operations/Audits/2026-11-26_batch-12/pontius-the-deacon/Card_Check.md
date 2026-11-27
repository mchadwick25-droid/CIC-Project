# Card check: Pontius the Deacon

Batch 12, 2026-11-27. The card checker did not write the card. Read: `CLAUDE.md` (Trust and source fidelity), Brief Kit Part 1 and the bar, `kinds/person.md`, the card role and this batch's header, the era 1 header's four sections, Stage Two Kit sections 1 to 3, then the final brief, `Outline.md`, `Review.md`, `Fresh_Read.md`, `pontius-the-deacon.card.json`, `Card_Edits.md` and `Card.existing.json`. There is no entry file (the entry exists). Every timeline line and headline, every `quotationOriginals` printed and original text, and the lines behind `legacy`, `uncertain`, `keyWorks`, `datesNote` and `shortDescription` were re-read in their files.

## Verdict: FIX

Four changes, below. Everything else passes.

## FIX

1. **timeline, period "257, the first day at Curubis", third line, `text`.** The judge's face was calm; it was his mind that seemed moved (VE 28078–28079, "I perceived from the calmness of his countenance that the judge's mind was moved"; VL 41034–41035, "sensi tamen de uultus sereuitate iudicis mentem quasi iusta petitione commotam"). The card moves the detail from the mind to the face.
   - Old: "Cyprian begs a delay of one day to put his affairs in order. The judge's face seems moved, and the young man signals, twisting his fingers one behind the other, that the delay is granted until the next day."
   - New: "Cyprian begs a delay of one day to put his affairs in order. From the judge's calm face, he senses that the request has moved him, and the young man signals, twisting his fingers one behind the other, that the delay is granted until the next day."

2. **timeline, period "257 to 258", fifth line (the messenger), `text`, `reference` and a new `note`.** The Latin reads "de Xisto ... ab urbe nuntius uenerat" (VL 41142–41143): a messenger had come from the city about Xistus. "From Xistus" is the English translation's reading (VE 28137–28138). The outline keeps both ("from (or about) its bishop", Beat 4); the card states one as fact.
   - Old text: "A messenger comes to Cyprian from the bishop of Rome, whom Pontius calls a most blessed martyr."
   - New text: "A messenger comes to Cyprian from Rome with word about its bishop, whom Pontius calls a most blessed martyr."
   - Old reference: "Pontius, Life and Passion of Cyprian 14, cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml lines 28137-28139"
   - New reference: "Pontius, Life and Passion of Cyprian 14, cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml lines 28137-28139; cic/texts/cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt lines 41142-41143"
   - New note: "The Latin says the messenger came about the bishop; the English translation says from him."

3. **timeline, period "September 258", sixth line (the trial), `text`.** "He is the man" is unclear read once. The Latin is "interrogatur de suo nomine: se esse respondit. et hactenus uerba" (VL 41310), the outline's rendering "He answered that he was. That was all that was said" (outline Quotes).
   - Old: "Brought before the governor and asked his name, Cyprian answers only that he is the man, Pontius writes, and nothing more is said."
   - New: "Brought before the governor and asked his name, Cyprian answers that he is Cyprian, Pontius writes. That was all that was said."

4. **timeline, the period `when` "September 258".** Its first two lines (the friends' offers, VE 28142–28149; Letter 81, EP 17370–17384) have no September date in any old source; only the arrest (KNOPF 4857), the last night and the death are fixed to September. The period date puts them there.
   - Old: "September 258"
   - New: "258, to 14 September"

## The checks

1. **Edits and fields against their evidence.** Each field in `Card_Edits.md` stands on its cited lines, with the four exceptions above. Every Cut first item marked Card is on the card. The Leave out items marked card are on it, or sit in `modernWorks` where they are a modern view (Harnack on the dream, the debates over the kind of book, the eyewitness, the court record and the style). Dessau's identification, Coxe's and Richardson's notes on his death, the count of 23 manuscripts and the list's year 359 are rightly left off under "Modern works on the cards". Review B1 to B4 and Fresh read MINOR 2 are held on the card (the vision's day, `uncertain` 5; the letter's order and reason, `uncertain` 9 and the timeline; "where his faith began"; no list of works). The card states no modern opinion, date or identification as content. "About 392" is worked from Jerome's own "fourteenth year of Theodosius" (JE 38785) and the held note on his accession (JE 15402–15403), as the dates rule allows. Each `modernWorks` note says what the work covers, never what it argues. Cut first 12, 24, 29 and 30 are marked Leave out (from the story). The card carries them as held details (VE 28074–28084, 28142–28145), which is right, though `Card_Edits.md` says that 29 "goes to the card".
2. **Kept fields.** `otherNames`, `knownFor` and `role` match the starting card word for word. The kept `sources` entries are word for word. Every other field is listed as changed or new.
3. **briefReferences.** All twelve name something the brief tells. The removed lines (the Cheltenham list, "the oldest Christian biography", baptism, the councils, the census tradition) are gone.
4. **Census rules.** The keys are as in the polycarp model, with no `briefLength`. There are six `quotationOriginals`, one for each of the brief's six quoted spans and none for a dropped one. Each `printed` is verbatim: VE 28057, 28071–28074 (with the page-break tag dropped), 27673–27677, 27707, 28297–28303; JE 40834. Each `original` stands at its lines (VL 41015, 40267–40270, 40331, 41405–41410; HAR 1309–1313; JL 57621–57622), the scan's joins and line numbers aside. Each cited file is in `sources`. The only quoted span in the card's prose is "a notable volume", at JE 40834. No audit file is named, and the spelling is American outside the printed wording. The three long quotes carry no `secondReading`.
5. **"checked at card".**
   - "a willing exile": *exulem uoluntarium* (VL 41015); Wallis's "a voluntary exile" (VE 28057). Right.
   - "these things I pass over": *illa praetereo* (VL 40331), the same words as VE 27707. Right.
   - "a notable volume": *egregium volumen* (JL 57621–57622), the same words as JE 40834. Right.
6. **Not found, and clearly wrong.** `Card_Edits.md` lists no claims as not found, and none was found missing. Nothing clearly wrong is left in once FIX 1 to 4 are applied.
7. **Census entry.** No new entry, and no `atlasId` to check. The Entry fields stand on their evidence: `modernWorks`; `dates` "257-258" (KNOPF 4823–4836, 4857); `regions` without Asia Minor (outline Setting); the teaser kept.

Readability, run by the checker on a plain file of the card's running text (outside the repository): 2143 words, grade 6.8 (names out 5.9), reading ease names out 78.7, 14.8 words a sentence, longest sentence 35 words. Pass, with grade under 8 noted. The card is not flat: the world's own wording survives in the lines.
