# Card check: ignatius-of-antioch (person, a full new card)

Checker: did not write the card. Read: `CLAUDE.md` (Trust and source fidelity), Brief Kit Part 1, `kinds/person.md`, the role, the era-1 card header's four sections, Stage Two Kit sections 1 to 3, the brief, `Outline.md`, `Review.md`, `Fresh_Read.md`, `ignatius-of-antioch.card.json`, `Card_Edits.md`, `Card.existing.json`. No entry file (the person has a census entry). Every timeline line and headline, every quotation and every card text was re-read against its cited file and lines, with the XML tags stripped.

## Verdict: FIX

Eight changes, below. Everything else passes.

## What passes

- **Quotations (item 4).** Three `quotationOriginals`, one for each of the brief's three quoted spans; the old "the blessed Ignatius" and "report says" entries are rightly dropped. Each `modern` matches the brief word for word. Each `printed` is verbatim: Q1 at ANF 7083-7090 (notes stripped), Q2 at ANF 6671-6676, Q3 at EUS 20069-20071. Q3's `original` is the Horologion scan exactly as it reads (HOR 15547-15552). Greek checked by hand: Σῖτός εἰμι τοῦ Θεοῦ, καὶ δι᾽ ὀδόντων θηρίων ἀλήθομαι, ἵνα καθαρὸς ἄρτος εὑρεθῶ; ἀλήθομαι is first person present passive, "I am ground", and the modern rendering keeps every clause and adds nothing. Another held print confirms the reading (McGiffert's English, EUS 20069-20071; the longer form, ANF 7059-7061; the Syriac note, ANF 9390), so carrying the Greek holds. No quotation is under six words, so none is "checked at card" (item 5). No `secondReading` given.
- **Keys and files.** Only allowed card keys (`tools/validate-census.mjs` CARD_KEYS, PERIOD_KEYS, TIMELINE_LINE_KEYS). Every cited file is in `sources`. Quotation marks in card prose surround only a source's own words (ANF 3487, EUS 20068, EUS 19742, ANF 6675, ANF 9390, ANF 7040-7042). No audit file, review or ruling named. American spelling.
- **Kept fields (item 2).** `otherNames`, `placeNote`, `role`, `keyWorks[0]`, `keyWorks[2]`, `legacy.remembered[0-2]` and `sources.ownWords` are word for word from the starting card, and each is held at the lines `Card_Edits.md` gives.
- **Changed and new fields (item 1).** `knownFor`, `shortDescription`, `datesNote`, `keyWorks[1]`, `legacy`, `briefSources`, `sources.about` and the dropped `briefReferences` are justified as listed. Coxe's "first use", the year 107, Harnack's Hadrian and McGiffert's verdicts are gone from the card text. Every item the outline's Card section, What came of it, Cut first (3 and 8) and the fresh read ("writing at Lyon in Gaul") send to the card is on it. The `modernWorks` notes say what each work covers, not what it argues (EUS-ed 19906-19927).
- **briefReferences (item 3).** All nineteen name things the brief now tells.
- **Not found (item 6).** None listed, and none found.
- **Entry fields.** The `teaser` and `dates` changes hold (Outline, Do not say; CHRON 42193-42202).
- **Readability.** `python -m engine.m1.profile_readability` on a plain file of the card's running text, kept outside the repository: "1762 words, grade 7.9 (names out 6.5), reading ease names out 77.2, 16.2 words a sentence, 0.3 joining words per 100, 26% short sentences, longest sentence 44 words - pass".

## FIX

1. **`timeline[3].lines[5].text`** (an assumption added: nothing held says the letter to Polycarp was the last he wrote; SS E7 and Outline beat 6 say only that it is the last stage his letters tell).
   - Old: "He writes that he must suddenly sail from Troas to Neapolis, so he cannot write to every church. These are the last words of his that survive."
   - New: "He writes that he must suddenly sail from Troas to Neapolis, so he cannot write to every church. It is the last stage of his road that his letters tell."

2. **`timeline[1].lines[4].text`** (detail spread onto the wrong case: Trallians 1, ANF 6279-6282, names only Polybius; others came with Onesimus and Damas, ANF 4707-4711, 5674-5677).
   - Old: "Onesimus, bishop of Ephesus, Damas, bishop of Magnesia, and Polybius, bishop of Tralles, come to him at Smyrna with others of their churches."
   - New: "Onesimus, bishop of Ephesus, Damas, bishop of Magnesia, and Polybius, bishop of Tralles, come to him at Smyrna, the first two with others of their churches."

3. **`timeline[2].lines[0].text`** (a church word not glossed where first met on the card; each line stands alone).
   - Old: "To Ephesus he writes that its elders are fitted to the bishop as strings to a harp, and urges the church to sing with one voice."
   - New: "To Ephesus he writes that its elders, the council who led a church with its bishop, are fitted to him as strings to a harp, and urges the church to sing with one voice."

4. **`timeline[4].lines[4].note`** (detail added: Jerome says he heard the lions roaring when condemned, not "in the arena", NPNF3 39826-39829).
   - Old: "Written much later; Jerome also has him hear the lions roar and speak the wheat line in the arena."
   - New: "Written much later; Jerome also has him speak the wheat line as he heard the lions roaring."

5. **`timeline[5].when`** (the period's date resolves what the sheet says not to resolve, SS D5: Polycarp's chapter 13, which this period opens with, asks for news of Ignatius and those with him).
   - Old: "After his death"
   - New: "Later"

6. **`quotationOriginals[1].uncertain`** (detail moved: the translators' note at ANF 6677-6678 follows "Do I therefore die in vain?" and covers that clause and the next, "Am I not then guilty of falsehood", which lies outside the quote).
   - Old: "The translators also note that some read the last two clauses as statements rather than questions (lines 6677-6678)."
   - New: "The translators also note that some read the last question, and the clause after it, as statements rather than questions (lines 6677-6678)."

7. **`uncertain[2]`** (an interval worked out from a Contested date for Ignatius, as Review B4 struck for Irenaeus; the outline gives 250 to 330 years, Who tells it).
   - Old: "Theodoret, writing more than three centuries later, says Peter himself made him bishop."
   - New: "Theodoret, writing much later, says Peter himself made him bishop."

8. **`uncertain[5]`** (a modern work named outside `modernWorks`; the ANF entry's `note` there already covers "the long dispute over them").
   - Old: "Which form is his, and whether the seven are his at all, was argued among modern editors for centuries; the editors of the Ante-Nicene Fathers and Arthur McGiffert, who translated Eusebius, set out that dispute."
   - New: "Which form is his, and whether the seven are his at all, was argued among modern editors for centuries."
