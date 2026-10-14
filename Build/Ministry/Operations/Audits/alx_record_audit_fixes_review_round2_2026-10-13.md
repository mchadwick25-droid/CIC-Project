Review round 2 (targeted recheck), alx record audit fixes, 2026-10-13, reviewer: independent Opus subagent

Verdict: PASS (no blocking findings; no non-blocking findings)

Scope: commit 910638a (HEAD), 10 files under records/alx. Only the ten round-1 findings were rechecked against the new text (`git show HEAD -- records/`). Nothing else was re-reviewed. Every touched field was re-graded with `engine.m1.gates.grade_text`; all pass FK <= 10 and FRE >= 60. The lowest FRE is 63.76 (alx.term.baptism personal) and the highest FK is 7.97 (the same field).

## Findings

None.

## Round-1 findings rechecked

1. **alx.demo.marriage-ending, representative turn (was BLOCKING): cleared.**
   - New: `That book has come down in a form we cannot quote to you in your tongue. So the full answer on marrying again we cannot give you from that book.`
   - Checked against: Stromateis III, which anf02 leaves in Latin (alx.limit.marriage `why_sources_cannot_answer`); Stromateis II.23, anf02 l.34983 ("it regards as fornication, the marriage of those separated while the other is alive"); Origen, Commentary on Matthew XIV, anf09 l.37713-37721 ("some even of the rulers of the church have permitted a woman to marry, even when her husband was living ... not indeed altogether without reason").
   - The sentence is true. Its scope is "that book", which is Stromateis III, and Stromateis III cannot be quoted in English from the vendored edition. It no longer makes the round-1 absence claim ("we cannot answer"). It does not say the world has nothing else on remarriage, so it stays inside alx.limit.marriage `not_for` ("presenting the gap as absence of any Alexandrian teaching on marriage"). "The full answer" also implies that a partial answer exists elsewhere, which is accurate.
   - The closing "The finer grain we must leave in the sources rather than guess at" stays honest. The English material that exists does not agree with itself. Clement II.23 is strict, and Origen reports church leaders who allowed remarriage while the first husband lived, which he calls contrary to Scripture but "not altogether without reason". Leaving the grain in the sources does not hide a settled answer.
   - Turn: FK 5.8, FRE 80.8. The record's sources (limit and Stromateis III) still match what the turn says. No locus change is needed.
   - Not a finding: the turn still does not use II.23, which the world could voice in English. That is a "could be stronger" point, not a defect. If Mark wants the turn to answer the remarriage question, the round-1 full text is still available (it needs `II.23` added to the clement-stromateis locus). Ideally a fuller answer would also carry Origen's report of the divided practice.

2. **alx.dw.church-failure, text: landed as proposed.** "Where the restoring side won, we refused the two easy exits: ..." The qualifier is restored, so "At our worst" pairs again. No hedge was lost. FK 7.1, FRE 65.8.
3. **alx.demo.who-was-jesus, representative turn: landed as proposed.** "By that we meant that his own life is opened to us and shared." The unsourced denial is gone, and the turn now agrees with alx.term.theosis. FK 6.0, FRE 86.9.
4. **alx.term.baptism, senses.personal: landed as proposed.** The new text carries Paedagogus I.6's own qualifier (nothing lacking to faith; its end reserved till the resurrection). The self-contradiction is gone. FK 8.0, FRE 63.8.
5. **alx.term.arete, quick_meaning: landed as proposed.** "with training and will playing a part" now matches plain_meaning, `senses.personal` ("had their part, but they were not the whole") and the false_friend. FK 4.2, FRE 89.9.
6. **alx.term.thanatos, plain_meaning: landed as proposed.** "where that loss leads" agrees with quick_meaning and De Inc. 4-6. FK 3.7, FRE 92.9.
7. **alx.demo.women-own-words, representative turn: landed as proposed.** "kept from martyrdom by his mother" matches HE VI.2, and the invented arena is gone. FK 5.4, FRE 77.6.
8. **alx.demo.want-to-believe, representative turn: landed as proposed.** "Gregory, said that while he studied under a teacher, 'like some spark ... love was kindled.'" The ambiguous "it began" is gone. The follow-on "It was love for the Word, and for the man who taught him" is unchanged. FK 5.6, FRE 82.5. A YAML folding note: the edited line is longer than the lines around it in the `>-` block. That does not change the folded string.
9. **alx.demo.going-to-hell, representative turn: landed as proposed.** "what we did mattered". The tense is consistent now. "God is not mocked" stays present, which is correct for who God is. FK 7.6, FRE 70.4.
10. **alx.term.anastasis, senses.personal: landed as proposed.** "already lived in the resurrection at work in them". The stray "now" is gone and "more than a hope for later" is kept. FK 5.3, FRE 79.1.

The pre-existing items listed in round 1 as "observed but not introduced" (stale `use_note.means` on the fixed terms, `hamartia` world_word, build-record source gaps) were outside this recheck and stay open as round 1 recorded them.
