# Recheck: Martin of Tours story (batch 4)

Checked `martin-of-tours.brief.txt` (587 words) against `martin-of-tours.brief.v1.txt` (512) and `martin-of-tours.brief.v2.txt` (678/679), per `Recheck2_Prompt.md`. Length is accepted at about 3:45 (Mark, 2026-11-18).

## 1. Review findings

- Findings 1 and 2 (Trier's plea against killing and the tomb's honor, both late): these only asked for Also told parts to come earlier, so they are superseded. Both are now present: "he begged that their blood not be shed" with Q2 (Trier paragraph), and the tomb sentence (paragraph 3).
- Finding 3 (Life and "model" past the mark): fixed, essence ends at word 126.
- Finding 4 (Gregory sentence, "keep"): the sentence is gone in the trim, so the overstatement is gone too.
- Finding 5 (Milan): fixed, "expelled him from a monastery he had set up at Milan" (Outline line 27; M8, NP11 947–953).
- Finding 6 (catechumen): fixed, "At ten, against their wish, he asked to be taught for baptism." (S6, NP11 710–712).
- Finding 7 (scorn tied to the plain life): fixed, "yet as bishop he kept that plain dress" (M10, NP11 1076–1081; M11, NP11 1119–1121).
- Finding 8 (short Q1): the trim goes back to the short form, which the outline allows (Outline line 39). The review left this to Mark.
- Padding list: done.
- Mark's cloak ruling: the cloak is back between the enlistment and Worms. "At Worms" has no time word, and the dream stays in Sulpicius's voice.

## 2. New wording

A word-level diff of v2 against the current brief shows only the five cuts listed under "Trim to 3:45" in `Revision.md`. Nothing else moved. Each sentence that differs from v1 is held:

- Setting: "In the fourth century" (S3, line 33); "in Roman Gaul, in what is now France" (Outline line 14; S4).
- Q1, short form: "I am Christ's soldier. I am not allowed to fight." This is the outline's rendering (Outline line 39), last two sentences, word for word. The Latin is in `cic/texts/sulpicius-severus_libri-qui-supersunt-chronica-vita-martini-lat_halm1866-csel1.txt`, lines 6334–6337: "Christi ego miles snm [sum]: pugnare mihi non licet."
- Q2: the second sentence of the outline's rendering (Outline line 40), word for word. The Latin is in the same file, lines 5903–5907.
- Tomb: I1 (a–d, line 93), credited to Gregory, "almost two hundred years later" (Outline line 58).
- Birth and enlistment: S2 (line 31), S6 (line 43), M1 (line 51).
- Cloak, dream, baptism: M3, M4, M5 (lines 55–59). "so with his sword" follows "Taking, therefore, his sword" (NP11 777–782). "the cold was killing people" is allowed by the Do not say list (Outline line 108). "still only a catechumen" is reported speech without quotation marks, as the review asked.
- The scorn and the plain dress: M10, M11 (lines 69–71).
- Candes and the funeral: M19, M20 (lines 87–89; Outline line 30). "almost" and "it was said" are kept.

No sentence says more than its source, and every witness is right.

## 3. Kit lines

- Hook: three sentences, the last carrying Q1. Within limit.
- Essence complete at word 126 ("...a model for later lives of saints."), counted by a word split.
- Also told: the cloak at Amiens, the eighty disciples and the monks made bishops, Trier with "their blood not be shed", and the tomb's honor are all present.
- Setting: the century comes in sentence 1 and the place in paragraph 2. It is not stacked.
- Ending: his death at Candes and the funeral. It ends on the person.

## Trim check (Revision.md, "Trim to 3:45")

None of the cuts takes out an item from the outline's Never left out list, the Essence or the Also told list. The chains, the Arian beating and both expulsions, the temples and the resistance, the bishops' scorn, and the executions and the compromise are all still told.

The cuts do remove three things that are in the outline but not on a must-keep list. They are noted here for Mark, not as faults in the brief:

1. The second sentence in the "Right" of the Do not say line on the tomb (Outline line 75) says "Gregory's acts (the great church, the feast, Clovis) come later." None of those acts is told now. The "Wrong" in that line, the tomb's honor left out, does not happen.
2. The outline's Connection (line 43) names the book as a second carrier: Fortunatus put it into verse and Gregory continued it. Only the "model" line is left of that.
3. The full Q1, which the review's finding 8 tied to Mark's approved heart. The outline allows the short form.

## 4. Score

`python -m engine.m1.profile_readability .../martin-of-tours.brief.txt`: 587 words, grade 8.4 (names out 7.8), reading ease with names out 72.1, 18.3 words a sentence, longest sentence 29 words. Pass.

## Verdict: PASS
