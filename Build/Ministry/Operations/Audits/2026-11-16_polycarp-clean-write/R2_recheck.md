# Polycarp of Smyrna, clean write: round 2 targeted recheck

Reviewer, 2026-11-16. A targeted recheck: only what changed since round 1, against `R1_review.md`. Judged against `Standard_draft.md` and `Writer_Sheet.md`.

**Verdict: PASS.** B1 is fixed. Every new or changed sentence traces to the sheet, and every quote matches its final reading. Two minor findings remain. Neither is wrong or misleading enough to need another round.

## 1. Round 1 findings

| R1 | Status | Note |
|---|---|---|
| B1 third part missing | Fixed | Closing movement now carries I18/Q21 (the letter and what he defended), I13 and I9 (Irenaeus's use of him against Valentinus and Marcion), and I11 (the peace with Anicetus used to restrain Victor). The Rome visit now has its consequence. Ignatius (I7) and I2 are left out on purpose and listed as such in the trace; that is a choice, not a gap. |
| M1 betrayal | Fixed | Two farms, two slaves seized, one gave him away under torture, "of his household" (M20). |
| M2 "anniversary" | Fixed | Quotes Q18: "keep the birthday of his martyrdom". |
| M3 pyre causation | Partly fixed | See m1 below. |
| M4 wonder's witness | Fixed | "says its own people saw" (Q15). |
| M5 "atheists" | Fixed in substance | "destroyer of their gods" now gives the reason, though two paragraphs after the cry. The reversal (Q7) is still dropped; that is a choice, not an error. |
| M6 "friends" | Fixed | "Because many wished it" (M18). |
| M7 when | Fixed | "the generation the apostles taught". |
| M8 Friday | Fixed | Cut. |

## 2. Trace of new and changed sentences

- **"He belonged to the generation the apostles taught, for Irenaeus ... wrote that apostles had instructed him."** S5, Q26. The claim is grounded in, and attributed to, Irenaeus in the same sentence. No overreach.
- **"calling him the destroyer of their gods"** Q12 final reading "the destroyer of our gods" (ANF M26 has "overthrower"; the final reading's word is kept, as R1 §4.3 asked). Correct.
- **"its own people saw the flames curve around him like a ship's sail, unable to consume his body, until an executioner killed him with a dagger."** Q15, Q16. Correct; dove left out (D3).
- **"resolved to gather there each year"** Q18 reads "the Lord will let us gather". "Resolved" is a fair paraphrase of the stated intent. No finding.
- **"We still have a letter he wrote to the church at Philippi"** M5, I13. The letter survives and the Library holds it (ANF; parts only in Latin, D9, on the card). Supported.
- **"calling its readers back from false teaching to 'the word handed down to us from the beginning.'"** Q21 final reading: "leave behind the empty talk of many people and their false teaching. Let us return to the word handed down to us from the beginning." Quote exact; paraphrase fair.
- **"Irenaeus recommended that letter, and held up Polycarp against Valentinus and Marcion as the steadier witness to the truth."** I13, I9 ("a more stedfast witness of truth, than Valentinus, and Marcion"). "Steadier" is a faithful modern word for "more stedfast". Correct.
- **"He and its bishop, Anicetus, could not agree about keeping Easter, yet they shared communion and parted in peace."** M9. The disputed Eucharist detail (Q29) is still left out. Correct.
- **"Some forty years later Victor, bishop of Rome, tried to cut off the churches of Asia over the date of Easter, and Irenaeus wrote to remind him of that peace."** I11: Victor "tried to cut off the churches of Asia over the Easter date"; Irenaeus "admonishes Victor that he should not cut off whole churches", citing Polycarp and Anicetus. "Remind him of that peace" is what the record says Irenaeus did. The interval: M9 gives Irenaeus's letter as "about 40 years later" than the visit it reports, derived from Victor's accession (Commodus's 10th year); the trace's uncertainty note says neither year is exact. "Some forty years" is counted from the Rome visit, as the sheet counts it, and "some" carries the approximation. Supported.
- **Quotes.** "Away with the atheists!" (Q7/M16), "Let the will of God be done" (Q4), the eighty-six years answer (Q8, exact), "keep the birthday of his martyrdom" (Q18), "the word handed down to us from the beginning" (Q21). All match the final readings.

## 3. Findings

### Blocking

None.

### Minor

- **m1. The burning cry (paragraph 4).** "The crowd, calling him the destroyer of their gods, shouted for him to be burned" still skips the step R1 M3 named: they asked Philip for a lion, he refused because the beast shows were over, and so they cried for fire (M26). As written, the charge alone seems to bring the cry for burning. A short clause fixes it ("...asked for a lion, and when that was refused, shouted for him to be burned").
- **m2. Tradition in the opening (paragraph 1).** The standard asks the opening for when, where and which tradition. Where is clear (Smyrna, the Roman province of Asia). When is carried by "the generation the apostles taught", which is the best the sheet supports without leaning on Eusebius's later and contested dating (S11, D2). Which tradition is only implied by "the church in Smyrna". S3 gives the census name the writer may use. This is a light touch, not an error: a phrase placing him among the churches the apostles founded in Asia would do it without the census label.

## 4. Score

`python3 -m engine.m1.profile_readability .../Polycarp_draft.brief.txt`:

> 341 words, grade 8.3 (names out 7.5), reading ease names out 73.6, 17.9 words a sentence, 1.5 joining words per 100, 11% short sentences - pass

Passes. At about 150 words a minute it runs about 2 minutes 16 seconds, close to the two-minute guide. Grade with names out stays just under 8 and is no concern for content this clear.
