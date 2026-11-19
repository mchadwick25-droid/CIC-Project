# Polycarp of Smyrna, clean write: round 3 targeted recheck

Reviewer, 2026-11-16. Third and final review under the three-round cap. A targeted recheck: only what changed since round 2, against `R2_recheck.md`. Judged against the updated `Standard_draft.md` and `Writer_Sheet.md`.

**Verdict: PASS.** No blocking findings. Round 2's m1 is fixed; m2 is unchanged and stays minor. Every new or changed sentence traces to the sheet, and every quote matches its final reading.

## 1. Listener read (once through, no going back)

It reads as a story told by someone who knows the record, not a report. It moves in scenes: the cry in Smyrna, the farms and the betrayal, the meal for the police, the stadium, the fire, the bones, then what came after. The voice reports the wonders as the church's own ("says its own people saw", "they say"), which a listener hears plainly.

Where I drifted:
- **"He prayed for two."** A half-beat to supply "hours" from "an hour to pray". It lands; no loss.
- **"the false teachers"** (paragraph 7). The definite article points back to nothing named; I briefly wondered "which ones?" The sense still holds because "false teaching" came one sentence before.
- **"keep the birthday of his martyrdom."** A second-language listener may stop on "birthday" for a death day. The sheet gives the church's reason (Q18: to remember those who have competed and prepare those to come). Not lost, but a moment of puzzle.
- **"shared communion" / "cut off"** (last paragraph). Both are church terms of art. "Cut off" is clear enough from context (Victor against the churches of Asia, Irenaeus reminding him of peace). "Shared communion" is the one term a general listener may not hold, but "and parted in peace" carries its sense beside it.

Flat or childish? No. The score is 6.7 because sentences got shorter, not because the thought got thinner. "He belonged to the generation the apostles taught" and "A letter he wrote to the church at Philippi survives" are plain, adult sentences with real content. The stadium answer and the fire keep their own imagery ("my King, who saved me", "like a ship's sail"). The closing line ("Irenaeus wrote to remind him of that peace") ends on the story's point, not on a summary. Plain and clear, not flattened.

## 2. Trace of new and changed sentences

- **"Irenaeus heard him as a boy, and later wrote that apostles had instructed Polycarp and made him bishop."** S5 ("instructed by apostles"; appointed "by apostles in Asia"), M13, I8. Told as Irenaeus's claim, and "apostles" names no single apostle, which is what D1 asks ("Tell it as Irenaeus's claim; 'John' is a later and narrower claim"). Correct.
- **"Then they demanded Polycarp, the man they called the destroyer of their gods, who taught many not to sacrifice."** M16 (ch. 3 demand), Q12 (ch. 12: "the destroyer of our gods. He teaches many not to sacrifice"). The words are faithful. The charge is spoken in the stadium in chapter 12 and is moved beside the chapter-3 cry; the trace says so openly. "The man they called" is not tied to a moment, it is the same Smyrna crowd, and it explains "atheists" where the listener needs it. A fair narrative placement, not a misstatement. See m3.
- **"Because many wished it ... one gave him away under torture."** Unchanged in substance (M18, M20).
- **Arrest paragraph, split into shorter sentences.** Q4 escape, food and prayer readings; "many were sorry they had come for such a godly old man" matches Q4 (prayer) ("Many were sorry they had come out against such a godly old man"). Correct.
- **"The crowd asked for a lion, but the beast shows were over, so they shouted for him to be burned."** M26. Philip the Asiarch is not named; the refusal is implied by "the beast shows were over". Correct, and it fixes round 2's m1.
- **"The fire could not consume his body, they say, so an executioner killed him with a dagger."** Q16 (dagger): "the fire could not consume his body. They ordered an executioner ... drive in a dagger." Attributed. Dove left out (D3). Correct.
- **"Later they laid his bones in a fitting place, and resolved to gather there each year and 'keep the birthday of his martyrdom.'"** Q18, M34. Quote exact. "Resolved" stays a fair paraphrase (R2).
- **"A letter he wrote to the church at Philippi survives."** M5, N4, I13. Supported. "Irenaeus recommended that letter" is now cut; nothing lost that matters.
- **"It calls its readers back from false teaching to 'the word handed down to us from the beginning.'"** Q21. Quote exact.
- **"Irenaeus pointed to Polycarp as a steadier witness to the truth than the false teachers."** I9 ("a more stedfast witness of truth, than Valentinus, and Marcion, and the rest"), M10. Irenaeus calls them heretics; "the false teachers" is a fair plain gloss, and still attributed to Irenaeus. Correct.
- **"Some forty years later Victor, another bishop of Rome, tried to cut off the churches of Asia over the date of Easter."** I11, I12, M9. "Another bishop of Rome" correctly separates Victor from Anicetus. Correct.
- **"Irenaeus wrote to remind him of that peace."** I11. Correct.
- **Quotes.** "Away with the atheists!" (M16/Q7), "Let the will of God be done" (Q4), the eighty-six years answer (Q8, exact), "keep the birthday of his martyrdom" (Q18), "the word handed down to us from the beginning" (Q21). All match the final readings.

## 3. Prior findings

| R2 | Status | Note |
|---|---|---|
| m1 burning cry | Fixed | The lion request and the end of the beast shows now come before the cry for fire (M26). |
| m2 tradition in opening | Not changed | Still only "the church in Smyrna" plus "the generation the apostles taught". Remains minor: nothing wrong, and where and when are clear. |

## 4. Findings

### Blocking

None.

### Minor

- **m2 (carried).** Which tradition is only implied in the opening. Not an error.
- **m3. Chapter-12 charge placed at chapter 3.** Faithful words, openly traced, the same crowd. Acceptable as told; noted so the move stays visible.
- **m4. "the false teachers" has no named antecedent.** Not wrong (I9), a brief listener snag only.

### The writer's open points

- **Birthday reason.** Leaving out Q18's reason is not an error. A short clause would ease the "birthday" puzzle for a second-language ear; optional, not a finding.
- **"Shared communion."** Accurate to M9 ("they stayed in communion"), and "parted in peace" carries it. Keep.
- **"Cut off."** Accurate to I11 (the sheet's own words). Clear in context. Keep.
- **Length ~2:25.** 365 words at about 150 a minute. The standard says "about two minutes" and "go shorter when the record is thin"; this record is not thin (martyrdom, letter, two bishops of Rome). The extra time buys the third part round 1 asked for. Not a finding.

## 5. Score

`python3 -m engine.m1.profile_readability .../Polycarp_draft.brief.txt`:

> 365 words, grade 6.7 (names out 6.0), reading ease names out 77.7, 14.6 words a sentence, 1.1 joining words per 100, 16% short sentences, longest sentence 23 words - pass (note: grade 6.7 is under 8: the listener read checks it is not flat)

Passes the hard limits (grade ≤ 10, reading ease ≥ 60). The under-8 grade is judged by the listener read in section 1: plain and clear, not flat.
