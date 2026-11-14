# R4 cap check: John of Beth Aphthonia, post-R3 changes (Mark's cap ruling, 2026-11-14)

## Scope

One targeted check, ordered in Mark's cap ruling, of the changes made after R3 to the profile `john-of-beth-aphthonia` in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch7/`:

1. `john-of-beth-aphthonia.brief.txt`, paragraph 4 ("John bar Aphthonia was a learned man of Edessa..."), as it stands, with the removal of "John of Ephesus names another monastery of Aphthonia, at Charrhae."; the audio script; readability and length.
2. `john-of-beth-aphthonia.card.json`, `uncertain` item beginning "Beth Aphthonia and Kenneshre."
3. `records.json`, entry `john-of-beth-aphthonia`: claims[22], claims[32], claims[33], contested_claims[2].

Nothing else in the profile was reviewed. R1-R3 review and change files in this folder were not read before this verdict. Bar: CLAUDE.md "Trust and source fidelity" and "Accessible and rigorous"; the coordinator's ruling that the profile is one Who as the author of the Life, with identity with the archimandrite John bar Aphthonia held as contested and bar Aphthonia's facts kept apart and given as his.

## Method

- Read each cited passage in context:
  - Brooks, John of Ephesus, `john-ephesus_lives-eastern-saints-po19-mixed-issue_brooks1926.txt` l.10630-10670 (list of consecrations, notes 1-7), and the parallel list at l.14850-14862.
  - Chabot, Michael the Syrian, `michael-the-syrian_chronique-tome2-livres-viii-xi-fra_chabot1901.txt` l.29070-29102, l.14760-14775, l.11843-11858.
  - Hamilton-Brooks, Zachariah, `zachariah-rhetor_chronicle_hamiltonbrooks1899.txt` l.12535-12560 (IX.15), l.10295-10335 (VIII.5).
  - Kugener, `zacharias-scholasticus_vie-de-severe-po2-syr-fra_kugener1903.txt` l.21280-21480 (hymn headings, running heads, hymn texts).
  - Abbeloos-Lamy, Bar Hebraeus, `barhebraeus_chronicon-ecclesiasticum-vol1-lat_abbeloos-lamy1872.txt` l.17295-17312.
- Ran every quoted string through `vq.py` (whitespace and hyphen-break tolerant); for misses, split the string to find the cause.
- Audio: rebuilt the expected script from the brief (`[calmly] ` + paragraphs 1-5 + `[warmly] ` + paragraph 6) and compared byte for byte.
- Readability: `engine.m1.gates.grade_text` on the brief; word count by whitespace split.

## 1. Brief paragraph 4, audio, readability: PASS

| Sentence | Source | Result |
|---|---|---|
| "John bar Aphthonia was a learned man of Edessa, the Syriac chronicle under Zachariah's name says." | Zach. VIII.5 l.10329-10331: "John the archimandrite, a learned man, ... a native of Edessa, the son of Aphthonia" | Supported |
| "When the monks of Saint Thomas at Seleucia were driven from their house, he settled them at Kenneshre on the Euphrates." | Zach. l.10325-10329 ("the monastery of St. Thomas the Apostle of Seleucia, which in zealous faith had removed and had settled at Kenneshre on the river Euphrates, and there been rebuilt by John the archimandrite"); Michael l.11850-11853 ("Le monastère de Thomas de Séleucie (conduit) par Jean le Rhéteur, bar Aphtonia, parvint ... à Qennésrê, sur l'Euphrate, et s'y fixa"), in a list of the expelled; Brooks note 4 l.10661-10662 ("after it had been expelled from Seleueia at the persecution") | Supported |
| "A hymn heading calls him its first abbot." | Kugener l.21332-21333: "hymnes, qui ont été composées par Jean bar Aphthonia, le premier higoumène de Kennesrê" | Supported |
| (a) "Michael the Syrian calls this house the monastery of Bar Aphthonia." | Michael l.29097-29098: "le saint monastère de Bar Aphtonia, appelé de Qennésrîn" | Supported. "This house" = the Kenneshre house of the previous sentences, which is exactly what Michael names. The sentence reports Michael's name for Kenneshre; it does not assert that the Life's Beith Aphthonia is that house, so the contested identity (paragraph 3) is not told as settled. |
| (b) "John bar Aphthonia sat with the bishops who refused the Council of Chalcedon at debates in Constantinople. He wrote a record of them, which the chronicles mention but do not give." | Zach. IX.15 l.12547-12554 ("many words had been spoken during the no small space of one year and more by the believing bishops who had come thither to the royal city by the king's command ... with whom was the learned John the archimandrite, the son of Aphthonia, (and he wrote a record of the discussions), the king would not banish the Synod of Chalcedon"); Michael l.14769-14771 ("bien des choses furent dites pendant une année et plus, par les évêques fidèles. — L'archimandrite Jean Bar Aphthonia y était, et les mit par écrit") | Supported. "Believing bishops" are the anti-Chalcedonian party (the sentence goes on: the king would not banish Chalcedon). "Sat with" is a fair plain rendering of "with whom was" / "y était". "Debates" for "discussions"/"bien des choses furent dites" is fair. Both chronicles report the record and quote none of it, so "mention but do not give" is exact. |
| (c) "In hymns he wrote that Severus fought with his hand as well as his tongue, shooting arrows of ink and pen." | Kugener l.21405-21409, in the hymn headed "Une autre (hymne) sur le même (Sévère) par Jean (bar Aphthonia)" (l.21398), within the series headed "d'autres hymnes, qui ont été composées par Jean bar Aphthonia" (l.21332) and under Kugener's running head "JEAN BAR APHTHONIA" (l.21300, l.21430): "agitant, outre la langue, aussi la main, [il combattit] en lançant des flèches avec l'encre et la plume" | Supported. The attribution of this hymn rests on the series heading (the parenthesis in the hymn's own heading is Kugener's supply), and the series heading is explicit. "Arrows of ink and pen" is a fair compression of "lançant des flèches avec l'encre et la plume". Nothing added. |

Removed sentence, "John of Ephesus names another monastery of Aphthonia, at Charrhae.": **rightly removed.** In Brooks's list (l.10643-10652) each place is the bishop's see ("when they had set up bishops for the various cities of Syria", l.10652-10653): Dimet "from the monastery of Aphthonia in the city of Laodicea", "Sergius from the monastery of Aphthonia in Charrhae". The parallel list at l.14855-14859 settles it: "another whose name was Sergius in the city of Charrhae, from the monastery of the house of Aphthonia". Charrhae is Sergius's see, not the site of a second monastery. The removed sentence misread the witness.

Ruling compliance: paragraph 4 gives every fact as bar Aphthonia's, by name, with its witness named, and never as the Life's writer's. It does not read across the contested identity.

Voice: plain, concrete, no hedging filler or assistant cadence. Sentences are short and one idea each.

Audio: `audio/john-of-beth-aphthonia.audio.txt` equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, byte for byte (both end in one newline).

Readability: `grade_text` gives FK 5.89 (<= 10) and Flesch 73.57 (>= 60). Length 324 words (<= about 325). PASS.

## 2. Card `uncertain` item "Beth Aphthonia and Kenneshre.": PASS, with one MINOR

"Beth Aphthonia and Kenneshre. That the writer's Beith-Aphthonia is the Kenneshre house rests on Michael the Syrian's name for it, the monastery of Bar Aphtonia called of Qenneshre, and on E. W. Brooks's note on John of Ephesus, who names two bishops from the monastery of Aphthonia, Dimet made metropolitan of Laodicea and Sergius made bishop in Charrhae. The heading of the Life gives no place for Beith-Aphthonia."

- Michael's name: l.29097-29098, as above. Supported.
- Brooks's note 4 (l.10661-10662) is on the Dimet line and identifies that "monastery of Aphthonia" as the one John son of Aphthonia set up at Kenneshre. Supported.
- Dimet made metropolitan of Laodicea (l.10642-10644; l.14855-14856 "he made metropolitan in the city of Laodicea ... Dimet from the holy convent of Aphthonia"); Sergius made bishop in Charrhae (l.10650-10651; l.14858-14859). Supported, and it now reads Charrhae correctly as Sergius's see.
- The item holds the tie as resting on later names and a modern note, and says the Life's heading gives no place. The contested point is not told as settled.

**MINOR 1 (participant text, spelling).** In one sentence the item gives the place as "Kenneshre" and then "Qenneshre", and the house as "Bar Aphtonia" where the rest of the card and the brief say "Aphthonia". "Qenneshre" is neither the card's own spelling nor Michael's ("Qennésrîn"). A reader may take two spellings for two places. Fix: replace "the monastery of Bar Aphtonia called of Qenneshre," with "the monastery of Bar Aphthonia, called of Kenneshre," (the brief's spelling, as claims[32] already allows for the brief).

## 3. records.json

### claims[33] (Brooks's note / Charrhae): PASS, with one MINOR

The reading is right: the note is to the Dimet line; each city in the list is a see; Charrhae is Sergius's see; one monastery of Aphthonia, not two. Locators l.10639-10651 and note 4 at l.10661-10663 hold what they are cited for. Confidence "Dominant Modern Reconstruction" fits Brooks's identification.

**MINOR 2 (quote not verbatim).** The quoted note ends "expelled from Seleucia", but the source line reads "expelled from Seleueia" (OCR; l.10662), and `vq.py` does not find the quotation as given. The claim already marks one OCR form ("eity [OCR]"); this one was silently corrected. Fix: "...after it had been expelled from Seleueia [OCR Seleucia]". Optional strengthening, not a finding: cite the parallel list, l.14858-14859, "Sergius in the city of Charrhae, from the monastery of the house of Aphthonia", which states the see outright.

### claims[22] (the record of the debates): PASS, with one MINOR

Both witnesses say what the claim says, and the brief and keyWorks entry rest on them fairly. The Zachariah locator l.12547-12554 is right. The ellipsis covers only "as recorded above,".

**MINOR 3 (locator).** The Michael line is cited as l.14768-14770, but l.14768 is blank and the quotation runs l.14770-14771 ("— L'archimandrite Jean Bar Aphthonia y était, et les / mit par écrit."). Fix: "l.14769-14771" (to include "bien des choses furent dites pendant une année et plus, par les évêques fidèles"). Observation, not counted: the Zachariah quotation has "king's" with a straight apostrophe; the source has "king’s". Typographic only.

### claims[32] (Michael's name for the house): PASS

"le saint monastère de Bar Aphtonia, appelé de Qennésrîn" is at l.29097-29098, with the hyphen break "ap- / pelé" correctly noted. The note on the brief's spelling is accurate.

### contested_claims[2] ("Whether Beith-Aphthonia is the Kenneshre house"): PASS

Michael l.29097-29098, Brooks l.10661, Bar Hebraeus l.17306-17307 ("in monasterio Aphtonii seu Kenserinensi", verbatim) hold what they are cited for. The opposing side (the Life's heading gives no place; the tie rests on later names and Brooks's note) is stated fairly. The Charrhae line l.10650-10651 is correctly read as Sergius's see, not a second monastery.

## Verdict

NOT CLEAR

Nothing is BLOCKING. Brief paragraph 4 is supported in every sentence, keeps bar Aphthonia's facts as his, and the Charrhae sentence was rightly removed. Audio matches; readability FK 5.89, Flesch 73.57, 324 words. Three MINOR findings remain, each with exact fix text above: MINOR 1, card spelling "Bar Aphtonia ... Qenneshre" -> "Bar Aphthonia, called of Kenneshre"; MINOR 2, claims[33] silently corrects OCR "Seleueia"; MINOR 3, claims[22] Michael locator l.14768-14770 -> l.14769-14771.
