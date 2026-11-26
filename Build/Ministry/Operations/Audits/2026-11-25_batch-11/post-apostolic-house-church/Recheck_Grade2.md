# Recheck of the second-grade fixes: The Post-Apostolic House Churches

Checks `Fixes_Grade2.md` against `Grades2/Grades.md` (three findings: missing where/when, "Part of their guilt" bare, the Ending's thread). Cited lines opened in `cic/texts/`. Scratch copy: `/tmp/claude-0/-home-user-CIC-Project/39d92526-11f8-5688-9d05-41b4a8cf62d5/scratchpad/rc2pah/final.txt`.

## Verdict: FIX

Three small changes to the fix pass. With them, the brief counts 672 by `wc -w` and 672 by a Python whitespace split (limit 672). Every old string occurs exactly once.

## Findings

**F1 (BLOCKING, cuts the scene's meaning): restore "ministrae, servers".** Cut 4 sends the ministrae line to the card. The Never cut list names only "the two women tortured to find the truth", so the line is not on it in so many words. But the line still has to stay:
- The slate let the two ministrae stay "for a new job (what the meetings were)". The outline repeats it (line 60: "here only what the meetings were: the dawn hymn, the oath, the meal, the two women").
- Line 18 counts "ministrae" among the glosses the story must carry.
- Without the word, the women tell the listener nothing about the meetings. They are just slaves who were tortured. "Quae ministrae dicebantur" (mirbt 2795–2796) is the one thing that ties them to the gatherings. It is also the only outside word for a serving role, in a story about who led.
- Kit Part 2 (Length): "cut an event before its meaning." Cut 4 keeps the event and cuts its meaning.

Keep the line, but drop "he wrote" (−2). The passive "They were called" follows "dicebantur" and still obeys Do not say ("Not 'the Christians called them'"). Pliny is already named as the witness in the same sentence. Pay for it in the opening's next sentence (−4, see F2).

**F2 (MINOR, the cut that pays for F1).** "He questioned people who said they had once been Christians and had given it up" becomes "He questioned people who said they had stopped being Christians". That is Pliny's own "fuisse quidem, sed desisse" (mirbt 2786–2787), and it saves 5 words where change 8 saved 1. The sentence runs 10 words.

**F3 (BLOCKING, unclear on one hearing, plus a word that reaches past the source): the doubt sentence.**
- *Who "He" is.* In "An informer had named them. He was unsure whether…", "He" is heard as the informer, the nearest man named. Write "Pliny".
- *"Only."* Pliny sets "nomen ipsum, si flagitiis careat" (the name itself, if free of crimes) against "flagitia cohaerentia nomini" (the crimes attached to the name) (mirbt 2774–2775; npnf201 19463–19469). He does not say "only". Drop it (−1). The new sentence is 16 words, with nothing nested.

## Judged as asked

**(a) Pliny's doubt (mirbt 2772–2775).** It is a new claim for the brief, but it is not new to the sheet. The sheet already quotes "the name itself" (nomen ipsum, mirbt 2774–2775) in its §6 table (Source_Sheet line 198, the Ignatius-under-guard row). L7 only adds the full clause as its own row.
- The claim is well held. It is Pliny's own words, contemporary and hostile. "Documented that he says so" is the right rating, and the sheet correctly notes that no law behind it is held.
- It answers the grade directly. Kit Part 1 ("Explain it") asks why an act of punishment happened where the old source gives the reason. Here the source's own reason is that the governor did not know what was being punished.
- It is told as narration, not a barred quote. It does not repeat pliny-the-younger's line ("he did not know what was punished"), which comes from "nescio quid … puniri soleat" (mirbt 2771–2772), a different clause.
- Rewording it from L6 alone ("brought as Christians", "named by an informer") would not say guilty of what. So the doubt stands, worded as in F3.

**(b) The ministrae line.** See F1. It is not the record's force: the force is the torture, and that stays. But the word is the meaning the slate gave this scene, so it stays, paid for by F2.

**(c) Where and when.**
- *When.* "Early in the second century" holds as Widely Accepted. Pliny writes to Trajan (mirbt 2768). Eusebius puts Trajan after Nerva (npnf201 16977). Jerome's Chronicle sets Pliny's entry after Trajan's regnal years x and XI (jerome-chron 42193–42200, 42246–42247; the Ignatius entry stands at XI). Turning a reign into a century is the same step the outline already takes for "near the end of the first century". No year is told.
- *Where.* "A Roman province" holds. Tertullian has "ruler of a province" (anf03 1566–1567), and Jerome has "cum quandam prouinciam regeret" (jerome-chron 42246–42247).
- *Pliny's own Book 10.* As governor, Pliny names Bithynia elsewhere in Book 10, but the Library does not hold Book 10. Only Ep. X 96–97 is held, in mirbt 2766ff. and inside McGiffert's note in npnf201. A search of `cic/texts/` for Plin- within 400 characters of Bithyn-/Pont- finds only modern or early-modern editors' notes: McGiffert, Mansi's editor, Whiston, Harnack, Duchesne and others. None of them is an old text. So under Part 1 (Rigor) the province stays unnamed. This is right for the brief.
- *Follow-up, not this pass.* Vendoring Pliny's Book 10 (Latin, out of copyright) would let the province be told. That is a Library want for the source-research thread. The tree-wide clash with pliny-the-younger ("Bithynia", "around the year 112") is already flagged in the fix pass as out of scope.

**Other changes, checked.**
- Change 3 (the Ending) matches npnf201 31530–31534 and 31549–31553. "A share of" rests on J3 and J4. The thread is now clear: Rome's elders did not keep Asia's day, and the visitors did.
- Change 5 (Ignatius) keeps the Never-cut "prisoner for the name" (anf01 4703).
- Change 6 (Justin) holds. "Brought to the one who presides" is in ch. 65 (1apol-grc 1716–1717), and ch. 67 says "as we said before" (ὡς προέφημεν, 1apol-grc 1768). The presider's address and the standing prayer go to Leave out. They are not force.
- Changes 1, 7 and 9: nothing is lost. The opening's first sentence, which is Never cut, is reworded and not cut.
- No gap-only tell. No AI tell. The heart is untouched.

## Exact replacements

### Brief (the full set, applied in this order to the live brief; this replaces the table in `Fixes_Grade2.md`)

| # | Old | New |
|---|---|---|
| 1 | Under the emperor Trajan, Pliny, a Roman governor, wrote that Christians had spread through his province's cities, villages and countryside. | Early in the second century, Pliny governed a Roman province. He wrote to the emperor that Christians had spread through its cities, villages and countryside. |
| 2 | An informer had named them. Part of their guilt | An informer had named them. Pliny was unsure whether to punish the name Christian itself, or crimes that went with it. Part of their guilt |
| 3 | Those elders kept a different day, yet lived at peace with visitors who kept Asia's day, and sent them the thanksgiving. | Those elders did not keep Asia's day, yet lived at peace with visitors who did, and sent them a share of the thanksgiving. |
| 4 | They were called, he wrote, ministrae, servers. | They were called ministrae, servers. |
| 5 | was brought from Syria as a prisoner, he wrote, for the name of Christ and the hope they all shared. | was brought from Syria as a prisoner, he wrote, for the name of Christ. |
| 6 | Then the one who presides spoke, and all stood to pray. Bread, wine and water were brought, he gave thanks as he was able, | Bread, wine and water were brought to the one who presides. He gave thanks as he was able, |
| 7 | that his church still drew counsel from the letter Rome had sent in the quarrel, written through Clement. | that his church still drew counsel from Rome's letter in the quarrel, written through Clement. |
| 8 | He questioned people who said they had once been Christians and had given it up. | He questioned people who said they had stopped being Christians. |
| 9 | Justin, himself a Christian, wrote | Justin, a Christian, wrote |

Count: +5, +16, +2, −2, −6, −6, −3, −5, −1 = net 0, so 672 stays 672.

### Outline.md (amending `Fixes_Grade2.md`'s outline changes)

**Line 64 (Opening 1).** Apply in place of `Fixes_Grade2.md`'s line-64 items:
- Old: `Under the emperor Trajan, Pliny, a Roman governor, wrote that Christians had spread through his province's cities, villages and countryside (mirbt 2800–2801; npnf201 19511–19512; grade fix pass). He questioned people who said they had once been Christians and had given it up.`
- New: `Early in the second century, Pliny governed a Roman province. He wrote to the emperor that Christians had spread through its cities, villages and countryside (mirbt 2768, 2800–2801; npnf201 19511–19512; Setting; grade fix passes). He questioned people who said they had stopped being Christians (mirbt 2786–2787, "fuisse quidem, sed desisse").`
- Old: `Part of their guilt, or their error, they told him, was this. Quote 1.`
- New: `Pliny was unsure whether to punish the name Christian itself, or crimes that went with it (mirbt 2772–2775; npnf201 19463–19469; Source Sheet L7; grade-2 fix pass). Part of their guilt, or their error, they told him, was this. Quote 1.`
- The ministrae clause (`and he had two slave women, who were called ministrae, servers, tortured to find the truth:`) stays as it is. `Fixes_Grade2.md`'s change to it is withdrawn.

**Line 108 (Ending 1):** as `Fixes_Grade2.md` gives it.

**Lines 30 and 31 (Setting):** as `Fixes_Grade2.md` gives them.

**After line 240 (Cut first), add this in place of `Fixes_Grade2.md`'s block:**

```
Second grade fix pass (2026-11-25, `Fixes_Grade2.md`, `Recheck_Grade2.md`), measured on the live brief:

32. "he wrote" in "They were called, he wrote, ministrae, servers." (mirbt 2795–2796); 2 words: **Leave out**. The word ministrae and its gloss stay (slate: what the meetings were).
33. Ignatius's "and the hope they all shared" (anf01 4703); 6 words: **Leave out**.
34. Justin's "Then the one who presides spoke, and all stood to pray." (1apol-grc 1762–1767), the next sentence becoming "Bread, wine and water were brought to the one who presides. He gave thanks as he was able"; 6 words net: **Leave out**.
35. "the letter Rome had sent in the quarrel" becomes "Rome's letter in the quarrel"; 3 words: **Leave out**.
36. "had once been Christians and had given it up" becomes "had stopped being Christians" (mirbt 2786–2787), and "himself" (Justin); 6 words: **Leave out**.
37. Trajan's name in the opening (by role, Names): **Leave out**.

Items 32–37 make room for the second grade's three fixes (+23), which leave the live brief at 672 (`wc -w`).
```

### Source_Sheet.md

As `Fixes_Grade2.md` gives it (S12, line 42, L7, §6 row). No change.
