# Who profiles: round 3 targeted recheck (last round)

Scope: only the lines changed in `review/R3_diff.txt` (r2 to drafts). Bar: `Who_Profile_Pattern.md`, Review checklist. Nothing was edited. No API calls were made.

## Verdict

No BLOCKING findings. Three MINOR findings, plus one note on tooling.

## Findings

**M1. Justin, para 4, MINOR (the caveat was dropped from the brief, but the card keeps it).**
New: "McGiffert also dates the trial after 163, the year Rusticus became prefect of Rome."
- The source (NPNF2-01, Eusebius HE IV.16, n. 1171) says the date "is very difficult to determine," that there are two traditions (Antoninus Pius and Marcus Aurelius), and that the later one "has the most in its favor." If the Acta are right, the death fell "under Rusticus, who, as we know, became prefect of Rome in 163."
- The new sentence is credited to McGiffert, so it does not present the date as settled fact. But it states his conditional dating flatly, and "after 163" is narrower than what he says, which is 163 or later.
- This cut removed the brief's only telling of the two-tradition dispute. The card's "What is uncertain" still carries it ("One tradition dates his death under Antoninus Pius, another under Marcus Aurelius...").
- Suggested wording: "McGiffert dates the trial to 163 or later, when Rusticus was prefect of Rome."

**M2. Eusebius, para 5, MINOR (readability: "There" now points to the wrong place).**
The merge put "He wrote decades later, on the side of Athanasius of Alexandria." between "a council at Tyre in 335" and "There Potamo...". So "There" now follows "Alexandria", and a listener can place the confrontation at Alexandria. Suggested fix: "At Tyre, Potamo..."

**M3. Eusebius, para 5, MINOR (readability: long nested sentence).**
"Eusebius answered that Eustathius held the views of Sabellius, whose name, McGiffert explains, came to stand for treating the Father and the Son as one." The sentence is 26 words, with an attribution nested inside a relative clause. That breaks the ~25-word, nothing-nested rule. The r2 version was two sentences and did not have this problem.

**Note (tooling, not a brief finding).** `drafts/make_cards.py` lines 54–67 still build `marcion-of-sinope` with name "Marcion of Sinope", and its uncertain text is older than the current card. The card JSON is correct. If the card is regenerated from this script, the rename is undone. The script should be brought into line with the card before any rebuild.

## Checks run

1. **Quotations.** No new quotation text was added. The quotes kept in changed lines are unchanged in wording.
   - The Eusebius rewording "read out his own statement of faith" is supported. The Letter of Eusebius (NPNF2-04, ix.ii §1) says "Our own paper, then, which was read in the presence of our most pious Emperor."
   - "One-in-essence" is verbatim (§4).
   - "without inquiry" matches §5.
2. **Changed sentences.**
   - Josephus: "A few held it wholly genuine" matches McGiffert's "This view has at present few supporters" (n. 197). Hase, Keim and Schürer, then Renan and Schaff, then Ewald are all correct against that note. Edersheim was dropped, which is fine because Renan and Schaff are still named. "Origen of Alexandria" is fine.
   - Josephus: cutting the Thecoa episode leaves no dispute untold.
   - Ignatius: the cuts to the Polycarp letter and to Daillé and Pearson leave the authenticity dispute told in place (the long and short forms, Cureton, then Zahn and Lightfoot).
   - Marcion: the cut of Irenaeus's motive and of the Antitheses sentence is fine. "Almost everything... from his opponents" still marks the partisan witnesses. The teaching still rests on Justin, Irenaeus and Tertullian. The Antitheses is still on the card's keyWorks.
   - Clement: cutting "Titus Flavius Clement" and McGiffert's "not out of fear" is fine. No contested point was lost.
   - Eusebius: cutting the beheading and fire line, Pamphilus's library, the Martyrs of Palestine, and "rose in anger" is fine. The Pamphili explanation is still credited to McGiffert.
   - Justin: cutting the Sunday worship passage is fine; the card's keyWorks still has "a Sunday service". For the date sentence, see M1.
3. **Marcion naming.**
   - "Marcion of Pontus" is used at first mention in the Marcion brief (para 1), the Marcion card `name`, and the Valentinus brief (para 2).
   - The source has it: Justin, 1 Apol. 26 ("Marcion, a man of Pontus") and 1 Apol. 58 ("Marcion of Pontus"); Irenaeus I.27.2 ("Marcion of Pontus succeeded him").
   - Sinope is marked as Epiphanius's claim in the brief ("a claim that is his alone", followed by Holl on the one copier). It is also marked on the card: `otherNames` reads "Marcion of Sinope, in Epiphanius of Salamis", and the uncertain line reads "Only Epiphanius... names the city of Sinope". In records.json it is tagged Inferential-Thin.
   - The audio scripts match the briefs once the tags are stripped. The records id is `marcion-of-pontus`.
   - The only leftover "Marcion of Sinope" outside the intended Epiphanius marking is in `make_cards.py` (see the Note).
4. **Word counts.** Two methods were used: `wc -w`, and a regex word count. Time is at 162 words a minute.

| Brief | wc -w | regex | Time |
|---|---|---|---|
| josephus | 401 | 401 | ~2:29 |
| ignatius-of-antioch | 399 | 399 | ~2:28 |
| marcion-of-pontus | 392 | 392 | ~2:25 |
| justin-martyr | 399 | 399 | ~2:28 |
| clement-of-alexandria | 395 | 395 | ~2:26 |
| eusebius-of-caesarea | 403 | 403 | ~2:29 |

   All six are at or under about 405 words. The card `briefLength` values (2:25 to 2:30) fit these counts.

5. **Readability.** `engine/m1/gates.py grade_text` scores:

| Brief | FK | Flesch |
|---|---|---|
| josephus | 7.6 | 68.4 |
| ignatius-of-antioch | 7.6 | 71.2 |
| marcion-of-pontus | 8.2 | 62.5 |
| justin-martyr | 7.3 | 66.5 |
| clement-of-alexandria | 8.3 | 62.8 |
| eusebius-of-caesarea | 8.3 | 62.8 |
| valentinus | 8.5 | 60.8 |

   All pass. The faults found by eye are M2 and M3.
