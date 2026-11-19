# Card check: Council of Nicaea (325)

I compared the new entry `council-of-nicaea-325.entry.json` with `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era2/council-of-nicaea-325.entry.json`. I checked every changed or added claim against `Source_Sheet.md` and the cited lines. I re-read all fourteen quotations, ten for the main brief and four for the story, in their files. I checked howItWorked against `Card_How.md` and `Outline_Check.md`.

**Verdict: FIX** (one blocking finding)

## Quotations, main brief

| # | Modern (matches brief) | Printed wording re-read | Result |
|---|---|---|---|
| 1 | "We are persecuted because we said, 'The Son has a beginning, but God has no beginning.'" | PG 82, 70615–70616, "Διωχόμεθα 3 ὅτι εἴ-/παμεν "3" ᾿Αρχὴν ἔχει ὁ Υἱὸς, ὁ δὲ Θεὸς ἄναρχός ἐστι."; English at npnf203 6045–6046 | Verbatim, with the markers left out. "We said" for εἴπαμεν is right |
| 2 | "For I count civil strife in the church of God worse than any war or fierce battle." | Heikel 11167–11168; npnf201 64468–64470 | Verbatim in both |
| 3 | "of one being" | npnf214 2412–2413 | Verbatim |
| 4 | "in the sight of all" | npnf203 6395–6396 | Verbatim |
| 5 | "God of God, Light of Light" | npnf214 2411 | Verbatim |
| 6 | "begotten, not made" | npnf214 2411–2412 | Verbatim |
| 7 | "there was a time when he was not" | npnf214 2418–2421 | Verbatim |
| 8 | "318 fathers ... shall not be set aside" | npnf214 13970–13972 | Verbatim |
| 9 | "pre-eminent" | npnf214 20218–20220 | Verbatim |
| 10 | "the whole world groaned, and was astonished to find itself Arian." | npnf206 32412–32413 | Verbatim |

## Quotations, story (how-nicaea-decided)

| # | Modern (matches brief) | Printed wording re-read | Result |
|---|---|---|---|
| 1 | "those who presided" | npnf201 64501–64502 | Verbatim |
| 2 | "He won some over and shamed others with his words," | Heikel 11238, "μὲν συμπείϑον, τοὺς δὲ “καταδυσωπῶν τῷ λόγῳ,"; npnf201 64512–64513 | Verbatim. The line starts with μὲν; the τοὺς before it ends line 11237, so the card's start agrees with the cited line |
| 3 | "of one being" | npnf204 19659–19660, "One-in-essence" | Verbatim |
| 4 | "It seemed good ... 'This is what the universal Church believes.'" | PG 26, 57165–57169; npnf204 56538–56542 | Verbatim in both. "Universal" for καθολική is explained |

Each modern wording matches its brief exactly.

## howItWorked

Every line agrees with `Card_How.md`, which passed its check, and adds only what the story brief and the sheet support:
- Latin through an interpreter (EUS 64500–64501).
- Each side's points in turn (EUS 64505–64509).
- The two drafting accounts (H7).
- A few would not accept all of it (H11).
- Gifts by rank and the farewell plea for peace (H15–H16).
- Eusebius's claim that unity held, against the later record (H16, I3).
- The opening-speaker split (H4).

Line 6 names Sozomen and Theodoret, which meets the check's minor finding C-1. The S-1 blocking finding against the story outline is met in line 4: "Every member signed, Eusebius says, ... and other records show a few would not accept all of it."

## Constantine's words on the Jews

decided[4] is right and keeps the witness. The synodal letter says only that "all our brethren in the East who formerly followed the custom of the Jews" will keep Easter with Rome and Alexandria (NC 6402–6406). The contempt is in Constantine's own letter: "the detestable company of the Jews" (NC 6446–6447) and "the murderers of our Lord" (NC 6469–6470). The card credits it to him, says it is not in the council's letter, and neither quotes nor voices it. The brief carries none of it. This meets Outline.md's Do not say and Leave out lines.

## Other changed claims

The following are supported:
- issue 0–5 (K1, K2, M1–M3; Theodoret I.4).
- decided 1–5 (H7, M11–M14, the canons at NC).
- knownFor.
- outcome 1–3 and 5 (I1–I4; SOC 3939–3942, 3978–3979; NC 20225–20230; NC 32490–32545).
- datesNote (H14).
- uncertain 2–10 (C6, M6, M11, H4, H6, H11, S3, K1).
- The record notes. Jerome's Dialogue is dated 379 at npnf206 2708, so "about fifty-five years" is fair.
- The sources, and the brief references of both briefs.

Brief lengths: the main brief has 549 words (3 minutes 40 seconds) and the story 237 words (1 minute 30 seconds). Both are right.

## BLOCKING

1. **outcome[4]: "(his introduction also gives 332)" is misleading.** The editor gives 341 and says "we know the exact date" (NC 9305–9313). He mentions 332 only as Ballerini's and Mansi's theory, which he reports Hefele "rejects ... altogether" (NC 9360–9367). The card makes 332 sound like the editor's second date. Exact correction:
   - Replace: `A later council at Antioch, in 341 by its editor's date (his introduction also gives 332), threatened`
   - With: `A later council at Antioch, in 341 by its editor's date (he reports, and Hefele rejects, a theory that its canons came from a synod of 332), threatened`

## Non-blocking

- howItWorked[5] keeps the NPNF wording "Thus believes the Catholic Church". The story renders it "universal" so that it is not heard in the modern denominational sense. `Outline_Check.md` C-2 suggested adding "(the whole church)". This is optional. Nothing in the line is wrong.

## Recheck (2026-11-17)

**Result: PASS**

- **BLOCKING 1 is fixed.** outcome[4] now reads "in 341 by its editor's date (he reports, and Hefele rejects, a theory that its canons came from a synod of 332)". This matches NC 9305–9313 and 9360–9367.
- The JSON parses. No other text changed.
