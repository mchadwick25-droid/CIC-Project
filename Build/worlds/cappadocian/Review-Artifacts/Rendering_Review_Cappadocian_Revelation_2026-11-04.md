# Rendering Review: cappadocian quote records, the "plan of revelation" phrase (1 record)

- **Reviewer:** Opus 5.5 (independent; fresh reader, did not read or render this record before)
- **Date:** 2026-11-04
- **Subject:** one phrase of the `modern_rendering` of `cappadocian.quote.gregory-nyssa-on-becoming-god`, a new defect separate from the rendering covered by the cap ruling of 2026-11-04.

This read is not a further revision round on the defects the project lead's cap ruling of 2026-11-04 covered. It checks one new defect only: the capital R in "the plan of Revelation", whose modern sense can point a reader to the Book of Revelation.

## Method

I read the edition at cic/texts/npnf205_gregory-nyssa-dogmatic-treatises.txt, lines 44319-44337 (Great Catechism, ch. XXV, heading at line 44317). I compared the record's `text` with those lines. I then read the changed phrase against `git diff origin/main -- records/cappadocian`, in the context of the whole rendering. I judged the phrase from the English edition alone. I make no claim about the underlying Greek.

## Results

**1 record: 1 PASS, 0 FAIL.**

| Record id (cappadocian.quote.…) | Edition text at (file, lines) | Text check | Rendering check | Verdict |
|---|---|---|---|---|
| gregory-nyssa-on-becoming-god | cic/texts/npnf205_gregory-nyssa-dogmatic-treatises.txt, lines 44319-44337 | pass | pass: lower-case "the plan of revelation" keeps the edition's sense and adds nothing | PASS |

**What "Revelation" means in the edition.** The edition reads "why are they scandalized at the plan of Revelation when it teaches that God was born among men". The next clause makes "it", the plan of Revelation, the thing that *teaches* the Incarnation. The surrounding argument is about God's presence in all things and his birth in human nature. So "Revelation" names God's revealed teaching, the faith as God has disclosed it. It does not name the Book of Revelation, which plays no part in the chapter and is not what teaches "that God was born among men" here. The capital is the translator's reverent capital, not a book title.

**Does the lower-case wording render it faithfully.** Yes. "The plan of revelation" reads in modern English as the plan God has revealed. The very next sentence of the rendering, "Why are they scandalized when it teaches that God was born among men?", fixes the sense as revealed teaching. The lower case removes the misleading pointer to the Book of Revelation. It adds nothing and drops nothing: "plan" and "revelation" both stay, and no gloss is introduced. "They" in the edition becomes "people" in the rendering; that change sits outside this phrase and outside this read.
