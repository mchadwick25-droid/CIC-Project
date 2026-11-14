# Council profiles, eras 1 and 2: review round 2, targeted recheck (2026-11-14)

**Scope.** What changed in commit `3b166b44` under `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/`, set against `R1_review.md` and the author's answer `R1_changes.md`. The nine councils are the same as in round 1. Text that did not change was not reviewed again.

**Method.**
- Read the word diff of every brief, entry and `records.json` against `HEAD~1`, then read each changed brief in full for broken first mentions and lost sense.
- Searched the one new quotation in its vendored file with `findq.py` and read it in context. Checked new factual wording against the held lines the records cite: Theodoret I.4 (`npnf203` l.6000-6046), Hamilton and Brooks's introduction (`zachariah-rhetor_chronicle_hamiltonbrooks1899.txt` l.300-318), Badger (`badger_nestorians-and-their-rituals-v1_1852.txt` l.7672-7683), Sulpicius II.43 (`npnf211` l.11318-11339), and the Ephesus count claims in `records.json`. Checked the new tradition id against `cic-website/data/world-census.json`.
- Counted words, ran `engine.m1.gates.grade_text`, counted sentence lengths, and compared each audio script with its brief plus `[calmly]` at the start and `[warmly]` before the last paragraph.
- No model calls, no network calls, no paid calls. No draft was edited.

## Gates

| Council | Words | FK | FRE | Audio = brief | Sentences over 25 words |
|---|---|---|---|---|---|
| councils-of-rome-and-carthage-251 | 398 | 7.35 | 63.78 | yes | none |
| council-of-arles-314 | 399 | 7.75 | 60.21 | yes | none |
| council-of-nicaea-325 | 393 | 7.73 | 60.59 | yes | none |
| council-of-sardica-343 | 400 | 7.74 | 61.01 | yes | none |
| councils-of-ariminum-and-seleucia-359 | 398 | 8.48 | 60.43 | yes | none |
| first-council-of-constantinople-381 | 400 | 7.82 | 62.06 | yes | none |
| conference-of-carthage-411 | 397 | 7.97 | 60.59 | yes | none |
| council-of-ephesus-431 | 399 | 7.64 | 60.53 | yes | none |
| council-of-chalcedon-451 | 399 | 7.35 | 64.09 | yes | two of 27 (R2-3) |

All nine pass: 400 words or fewer, FK 10 or under, FRE 60 or over. The scores match `R1_changes.md`. Each audio script carries only the two tags, in the right places.

## Round 1 findings

| Finding | Severity (R1) | Status | Evidence |
|---|---|---|---|
| ROM-1 | minor | RESOLVED | Split after "near"; no sentence over 25 words. |
| ARL-1 | minor | RESOLVED | "the bishops' letter to Silvester, bishop of Rome, with their canons, and Constantine's letters." |
| ARL-2 | minor | RESOLVED | "led by Marinus, whom Hefele takes as bishop of Arles"; matches the records' "Who presided" claim. |
| ARL-3 | minor | RESOLVED, with a side effect | The sentence now ends at "the Scriptures". The cut also removed "in the persecution", which the next sentences rely on (R2-6). |
| NIC-1 | substantial | RESOLVED in the brief; the entry lags (R2-7) | The Arius quote is verbatim at `npnf203` l.6045-6046 and correctly given as Arius's letter, kept by Theodoret. The council's letter stays as the second witness. Source and claim are added. |
| NIC-2 | minor | Left as is; the reason holds | R1 said no fix was required. The dispute is carried in the entry and records. |
| SAR-1 | minor | RESOLVED | "date it by a consulship that their editors take as 347." |
| SAR-2 | minor | RESOLVED | "went home in 346, by the index to his Easter letters." |
| ARI-1 | substantial | RESOLVED | Brief: "who wrote most of the histories", and "its creeds and a statement by Acacius of Caesarea, which the Nicene writers copied." Entry `uncertain[0]` now calls Philostorgius "a Eunomian historian hostile to both sides". Acacius gets his full name at the first mention, and the later "Acacius led" still reads. |
| ARI-2 | minor | RESOLVED | "they used its name to pass the creed off as that of Nicaea", which matches Socrates (`npnf202` l.8946-8953). |
| ARI-3 | minor | RESOLVED | "Jerome" in the brief, the entry's `people`, `record` and `sources`. |
| ARI-4 | minor | Left as is; the reason holds | The fix was optional. The year rests on the consulate in `datesNote`. |
| ARI-5 | minor | RESOLVED | The marks are gone: "homoousion and homoiousion, the words for one substance and like substance". |
| CON-1 | substantial | RESOLVED | It opens with "stood before the council's bishops and gave up his see". Paragraph 6 ties back: "That was when he gave his farewell and withdrew." The listener now hears one resignation, in the right place. |
| CON-2 | minor | RESOLVED, with a side effect | "by Hefele's reading" is added. That puts Hefele in the brief two paragraphs before he is introduced (R2-1). |
| CON-3 | substantial | RESOLVED | `"verdict": "LISTED"`, no id; this matches the supplement scan. |
| CON-4 | minor | RESOLVED | "the Pneumatomachi, whose name means fighters against the Spirit" has no quotation marks, and the gloss is correct. |
| CON-5 | minor | RESOLVED | "Later, Gregory the Great …" has no date. |
| CON-6 | minor | RESOLVED | "chiefly Gregory and the bishops' letter of the next year." |
| CAR-1 | substantial | RESOLVED | "full" is removed. The text now reads "The record survives in Latin … It breaks off in the third session." The contradiction is gone. |
| CAR-2 | minor | RESOLVED | "the third session" in both places. |
| CAR-3 | minor | RESOLVED | "Emeritus of Caesarea in Mauretania" in the brief, and the scan's name in `people`. The later "at Caesarea" now has its place. |
| EPH-1 | minor | PARTLY; the reason mostly holds | "forty-three by their own signed sentence" credits the count to its source, so the count is no longer Hefele's alone. The records hold the dissenting count, Cyril's council's "a little more than thirty", as a `contested_claim`. The brief gives one side of that count, but with its witness named, so it does not state the number as settled. The cap leaves one spare word. This stays minor and does not block. |
| EPH-2 | minor | RESOLVED | "John of Antioch's assembly left its own documents too." |
| EPH-3 | minor | RESOLVED | The early row now gives Wigram (no corporate action at the time) and Badger ("cut off … by the decree", `badger v1` l.7680-7682). Barhadbeshabba has moved to `the-church-of-the-east-under-persia`. That id is in the census, and the "pious Mar Nestorius" wording is in `po09_barhadbeshabba…` l.9. |
| EPH-4 | minor | RESOLVED | Split at "Candidian, protested." |
| CHA-1 | substantial | RESOLVED, with one long sentence | "a later Syriac chronicle, known as that of Zachariah of Mitylene, built on a Greek history that ran to 491" is supported: "the work of Zachariah ended in 491 … only one of the authorities used by the compiler" (l.310-313). The sentence runs 27 words (R2-3). |
| CHA-2 | minor | RESOLVED, with a side effect | Marcian alone now calls the council, and Pulcheria is credited to Hefele. But Hefele is never introduced in this brief (R2-2). |
| CHA-3 | minor | Left as is; the reason holds | The fix was optional, and the entry quotes Dioscorus. |
| CHA-4 | minor | RESOLVED | Severus, Select Letters VI (part 2 file) is in `sources.writtenLater`. |
| CHA-5 | minor | PARTLY | "Flavian, bishop of Constantinople" is fixed, and the Priscus sentence is split. The "It restored Eutyches …" sentence, which R1 counted at 26 words, now runs 27 (R2-3). |

All six substantial findings are resolved.

## New findings

**R2-1. Minor (Constantinople; broken first mention).** Paragraph 5 says "Meletius of Antioch led them at first, by Hefele's reading". Hefele is first introduced in paragraph 7: "Charles Joseph Hefele, the historian of the councils, thinks …". A listener hears the bare name first. Fix: move the introduction to paragraph 5 ("by the reading of Charles Joseph Hefele, the historian of the councils"), and in paragraph 7 write "Hefele thinks …". The net word count stays the same.

**R2-2. Substantial (Chalcedon; name never introduced; item 8, C4).** "his successor Marcian called a new council, with the empress Pulcheria, Hefele says." This is the only mention of Hefele in the Chalcedon brief. Every other brief introduces him as "Charles Joseph Hefele, the historian of the councils". A listener on this page cannot tell who Hefele is, so the credit that CHA-2 was meant to give does not reach them. The brief is at 399 words, so the fix needs a cut elsewhere. Fix: "with the empress Pulcheria at his side, says Charles Joseph Hefele, the historian of the councils." Find the words by trimming elsewhere, for example "a monk of Constantinople who spoke of one nature in Christ after the union" could shed "after the union" only if the entry carries it. Then rescore.

**R2-3. Minor (Chalcedon; length).** Two sentences run 27 words:
- "It restored Eutyches, a monk of Constantinople who spoke of one nature in Christ after the union, and deposed Flavian, bishop of Constantinople, who had condemned him." Fix: end it after "the union", then "It deposed Flavian, bishop of Constantinople, who had condemned him."
- "The losing side tells its story in a later Syriac chronicle, known as that of Zachariah of Mitylene, built on a Greek history that ran to 491." Fix: end it after "Mitylene", then "It was built on a Greek history that ran to 491."

**R2-4. Minor (Chalcedon; place).** The cut of "near Constantinople" leaves Chalcedon with no place at its first mention. A listener may not know where it is. Fix: put it back if the words allow ("at Chalcedon, across the water from Constantinople", only if a held line gives it, or "near Constantinople" as before).

**R2-5. Minor (Ariminum; lost sense).** "the prefect Taurus pleaded with tears before the last twenty bishops." With "still holding out" cut, "the last twenty" no longer says what they were the last of. Sulpicius has the party "diminished down to twenty" who "had not yielded" (`npnf211` l.11324-11333). Fix: "the last twenty bishops who held out".

**R2-6. Minor (Arles; broken first mention).** The ARL-3 cut removed "in the persecution". The next sentence still says "judges from Gaul, which the persecution had spared", which now refers back to a persecution the brief has not named. Fix: "had handed over the Scriptures in the persecution." That is three words and 23 in all.

**R2-7. Minor (Nicaea entry; consistency).** The entry's `issue` still says "Arius's own letters survive only in books by his opponents (synodal letter, npnf214)". `uncertain` still says "Arius's teaching reaches us through the council's letter and his opponents. His own letters survive only in books by his foes." Neither is false, since Theodoret was a foe. But neither names the letter the brief now quotes. Fix: in both, name the letter to Eusebius of Nicomedia, kept by Theodoret I.4, as the place his teaching survives in his own words. A side note, with no fix required: the new claim is tagged `witness_kind: participant`. The letter predates the council and is the condemned party's own statement, not an account of the meeting. The pattern's four kinds have no closer fit, so the tag is acceptable.

**R2-8. Minor (Sardica; ambiguity).** "Julius, bishop of Rome, had received him into communion, and Marcellus of Ancyra." With "too" dropped, a listener can hear Marcellus as a second person who received Athanasius. Fix: "had received him, and Marcellus of Ancyra, into communion." The word count is unchanged.

No new quotation other than Arius's, and no new AI tells, "not X but Y" contrasts or tail lines were found in the changed text. None of the cuts listed in `R1_changes.md` left a name used later without introduction, or a witness unnamed, apart from R2-1, R2-2 and R2-6.

## Counts (new findings)

| Council | Blocking | Substantial | Minor |
|---|---|---|---|
| councils-of-rome-and-carthage-251 | 0 | 0 | 0 |
| council-of-arles-314 | 0 | 0 | 1 |
| council-of-nicaea-325 | 0 | 0 | 1 |
| council-of-sardica-343 | 0 | 0 | 1 |
| councils-of-ariminum-and-seleucia-359 | 0 | 0 | 1 |
| first-council-of-constantinople-381 | 0 | 0 | 1 |
| conference-of-carthage-411 | 0 | 0 | 0 |
| council-of-ephesus-431 | 0 | 0 | 0 (EPH-1 stays minor) |
| council-of-chalcedon-451 | 0 | 1 | 2 |

## Verdict

| Council | Verdict |
|---|---|
| councils-of-rome-and-carthage-251 | CLEARS |
| council-of-arles-314 | CLEARS (R2-6 recommended) |
| council-of-nicaea-325 | CLEARS (R2-7 recommended) |
| council-of-sardica-343 | CLEARS (R2-8 recommended) |
| councils-of-ariminum-and-seleucia-359 | CLEARS (R2-5 recommended) |
| first-council-of-constantinople-381 | CLEARS (R2-1 recommended) |
| conference-of-carthage-411 | CLEARS |
| council-of-ephesus-431 | CLEARS |
| council-of-chalcedon-451 | NEEDS FIXES (R2-2; R2-3 and R2-4 with it) |

This is the second review file on each of these documents. A Chalcedon fix limited to R2-2 to R2-4 needs only a recheck of those lines, plus a rescore and a regenerated audio script.
