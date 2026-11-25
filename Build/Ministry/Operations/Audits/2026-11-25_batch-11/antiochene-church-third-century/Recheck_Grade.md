# Recheck of the grade fixes: antiochene-church-third-century

**Verdict: FIX** (one wording change in fix 2; three outline lines to bring into line).

Scope: the two applied changes in `Fixes_Grade.md`, the one not applied, against `Outline.md`, `Source_Sheet.md` and `cic/texts/`. Changes applied to a scratch copy outside the repository; the live brief was not edited.

## Fix 1: "around 260" in the first sentence: PASS

- Says no more than its source. S1 (E-Eng 41784-41785; E-Gk 11432-11433): Paul received the episcopate of Antioch when Demetrianus died. S2 (JerChr 44213-44215): Gallienus's seventh year. "Around 260" is the outline's own wording (Setting, line 30; beat 1, line 68), Widely Accepted from S2. Nothing added.
- Fixes the named fault: the first sentence now gives the when.
- One hearing: "The bishops who judged him" has a plain antecedent in the sentence before. Paragraph 3 now opens "Almost all we know of him"; "him" follows "their own bishop ... put him out" at the end of paragraph 2, so it holds.

## Fix 2: the Eusebius of Nicomedia sentences: FIX (one phrase)

- Says no more than its source. "One was Eusebius, bishop of Nicomedia": L6 (Philost 138), Lucian's disciples "especially Eusebius, bishop of Nicomedia", credited in the sentence before to the historian on Arius's side. "Arius had written to him about being driven out": the letter is headed "The Letter of Arius to Eusebius, Bishop of Nicomedia", and it says "He has driven us out of the city as atheists" (`npnf203_theodoret-jerome-gennadius-rufinus.xml` 6003-6026; Ar2, L5). "The name Lucian's pupils gave themselves": Arius, a pupil, calls Eusebius, a pupil, "fellow-Lucianist" (6063-6064; Q2); the same claim the old wording made.
- Fixes the named fault: "one of them" and "that letter" now resolve on one hearing.
- One-hearing fault the fix brings in: "not the historian" comes straight after "A church historian of the next century ... says". The nearest historian the listener has heard is that one (Philostorgius, unnamed), not Eusebius of Caesarea. Name the man meant.

Old:
> One was Eusebius, bishop of Nicomedia, not the historian.

New:
> One was Eusebius, bishop of Nicomedia, not Eusebius of Caesarea.

(Eusebius of Caesarea is already named in paragraph 3; no new name.)

## Fix 3 (not applied): agreed

Checked at Thdt 5757-5768: Alexander gives the act ("withdrew himself from communion with these bishops during a period of many years"), no reason; note 295 is the editor's and gives none either. Adding a why would invent one. Keep the sentence as it is.

## Count and readability

Scratch copy with fixes 1 and 2 as written: 670 words (`wc -w`). With the change above: 671 words, at most 675. `python3 -m engine.m1.profile_readability --report` on the 671-word copy: grade 8.1, reading ease (names out) 74.2, 17.7 words a sentence, pass.

## Outline replacements

1. Openings, item 1 (line 63). Old:
> Then the essence: this was the bishop of Antioch, as the bishops' letter tells it. (C6, C7; E-Gk 11896-11910.)

New:
> Then the essence: this was the bishop of Antioch, as the bishops' letter tells it. The when comes first, in one sentence before the letter's charge: Paul of Samosata became bishop of Antioch around 260 (S1, S2; "around 260" Widely Accepted from S2). (C6, C7; E-Gk 11896-11910.)

2. Beat 1 (line 68). Old:
> 1. **Paul becomes bishop, around 260, and what he taught.** When Demetrianus died, Paul of Samosata became bishop (S1, S2; Documented; "around 260" Widely Accepted from S2).

New:
> 1. **What Paul taught.** When Demetrianus died, Paul of Samosata became bishop (S1, S2; Documented; "around 260" Widely Accepted from S2); the year is told in the opening, not again here.

3. Ending, item 1 (line 113). Old:
> One of them, Arius, now driven out of Alexandria (beat 6 gives the reason, Ar2), wrote to another, Eusebius of Nicomedia, and ended with Q2.

New:
> One was Eusebius, bishop of Nicomedia, not Eusebius of Caesarea. Arius, now driven out of Alexandria (beat 6 gives the reason, Ar2), had written to him about it, and ended that letter with Q2, the name Lucian's pupils gave themselves.
