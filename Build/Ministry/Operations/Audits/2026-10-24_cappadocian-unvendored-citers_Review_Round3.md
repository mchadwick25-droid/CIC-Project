# Cappadocia: unvendored-citers re-grounding, adversarial review round 3, 2026-10-24

**Method.** Targeted recheck, final round under the three-round cap. I checked only round 2's N1 and N2, the round 2 follow-ups, the lines commit 0449350b changed (`git diff HEAD~1 HEAD -- records/`), and any new defect in those lines. I opened every cited locus in `cic/texts/` and compared quoted words character by character. No record was edited and no model or API was called.

**Date.** 2026-10-24.

**Reviewer.** Independent Opus context.

**Verdict.** PASS WITH FIXES. N1 and N2 are resolved. Most follow-ups were applied correctly. Two BLOCKING findings remain (R3-1, R3-2). Both are short wording errors with exact replacements below. Neither needs new research. Because this is the final round, an independent re-confirmation of those two replacements is a cap matter for Mark, not a fourth round.

**Gates.** On the committed state: `python -m engine.m10.cli regate cappadocian --base origin/main` PASS. Its readability notes are all pre-existing and unchanged at the base. `python -m pytest engine/m1/tests/test_embedded_quotations.py -q -p no:cacheprovider` 16 passed.

Path key: N207 = `cic/texts/npnf207_cyril-jerusalem-gregory-nazianzen.xml`, N208 = `cic/texts/npnf208_basil-letters-select-works.xml`.

## (a) Round 2 blocking findings

| # | Record | Resolved? | Evidence |
|---|---|---|---|
| N1 | term.philoptochia, senses.translational | Resolved | Now "in the famine Basil, by his word and advice, opened the stores of those who held them and fed the hungry." N207:42005-42007: "For by his word and advice he opened the stores of those who possessed them, and so, according to the Scripture dealt food to the hungry". No quotation marks are used, and the paraphrase adds nothing. |
| N2 | demo.taught-most, sources and body | Resolved | The philoptochia locus is now "the institution". The new basil-letters-general-corpus locus quotes N208:6272-6273 "Do not wait for a famine before / thou openest thy barns" and N208:6297-6298 "for I was an hungred and ye / gave me meat" verbatim. The body's range 6272-6302 covers the barns line (:6272), the Matthew 25 blessing (:6295-6298) and the condemnation (:6300-6303). The body's "No quotation marks" note now rests on Homily VIII being only summarized (N208:6926-6935), which is true. |

## (b) Follow-ups

| Item | Status | Evidence / note |
|---|---|---|
| panegyris-shrine text | Applied correctly | The "this record has not checked that" sentence is gone. "we cannot name more than that" is emic and makes no new claim. |
| source.basil-moral-famine-homilies | Applied correctly | divergence_note, edition and discovery_channel now say extracts of Homilies VI and VII are quoted and Homily VIII summarized. N208:6227 "Homily VI., on Luke xii. 18, is on selfish wealth and greed."; quoted extracts follow to :6310. :6848 "Homily VII., against the rich"; quoted extract from :6855. :6926-6935 Homily VIII "on the Famine and Drought" is summary only, with no quotation of Basil. |
| dw.who-was-jesus | Applied correctly | The unchecked surplus line is gone. See (c). |
| term.pleonexia | Applied correctly | The surplus line is gone and the new source row is added. See (c) and the note below. |
| term.philanthropia not_for | Applied correctly | Now points to cappadocian.term.eikon, which does carry it (eikon lines 46-48: "the poor man at the door bore that image too"; means at line 77-78: "the poor bear that image"). |
| voice.craft | Applied, but see R3-1 | The mapping wording ("whole text, unverified beyond extracts") is accurate. The guard sentence is not. |
| philoptochia evidential and locus | Applied correctly | Both now match N208: extracts of VI and VII quoted, VIII only summarized. |
| philoptochia divergence_note | Not done, see R3-2 | Round 2 named this field. It still says the homilies' wording rests on no checkable text. That now contradicts the record's own evidential and locus. |
| demo.taught-most body note | Applied correctly | See N2. |

## (c) Claims against the extracts

- **who-was-jesus**, "We were told not to wait for a famine before opening our barns." Supported. N208:6272-6273, "Do not wait for a famine before thou openest thy barns", is addressed to Basil's hearers in the second person. "We were told" is a fair emic rendering. No quotation marks are used.
- **pleonexia**, "They told the rich not to wait for a famine before opening their barns." Supported by the same lines. Homily VI is addressed to the greedy rich ("selfish wealth and greed", N208:6227-6228).
- **philanthropia not_for to eikon.** Correct, as above.

## (d) Findings

| # | Sev. | Record / field | Problem (evidence) | Exact replacement |
|---|---|---|---|---|
| R3-1 | BLOCKING | voice.craft: guard (lines 51-52) | "Our famine preaching reaches us only in long extracts, not whole." This is wrong for the famine sermon. The only famine homily, Homily VIII "on the Famine and Drought", survives in the vendored volume as summary only (N208:6926-6935). The long extracts are from Homilies VI and VII, on greed and against the rich (N208:6227, :6848). The guard also contradicts philoptochia's corrected evidential ("The famine homily itself, Homily VIII, is only summarized there."). As written, it would license the voice to treat famine-sermon wording as held. | `Our famine preaching` / `reaches us only in long extracts, not whole.` → `Our preaching against greed` / `reaches us only in extracts, and our famine sermon only in summary.` |
| R3-2 | BLOCKING | term.philoptochia: confidence.divergence_note (lines 15-19) | It still says "no open-license translation of that specific homily set is vendored anywhere in this project ... any specific wording attributed to those homilies rests on general scholarly knowledge, not a checkable primary text." That is now false. English extracts of Homilies VI and VII are vendored in N208:6227-6310 and :6848 onward. The record's own evidential and locus say so. | Replace from `Basil''s own famine and wealth homilies -- the era''s sharpest, most-quoted lines on this theme --` through `those homilies rests on general scholarly knowledge, not a checkable primary text.'` with: `Basil''s own famine and wealth homilies are a separate case: no open-license translation of the whole` / `set is vendored in this project (Source Registry row 16). The npnf208 Prolegomena quotes long English` / `extracts of Homilies VI and VII (npnf208 xml:6227-6310, 6848 onward) and only summarizes Homily VIII` / `on the famine (6926-6935). Wording within those extracts is checkable; any other wording attributed` / `to these homilies rests on general scholarly knowledge, not a checkable primary text.'` |

## Non-blocking notes (log, do not reopen)

- **pleonexia framing.** plain_meaning opens "During a famine, preachers named this vice directly." The new last sentence is from Homily VI, which the Prolegomena does not place in the famine (only Homily VIII is tied to 368, N208:6926-6927). The new line reads a little oddly after that opening. The opening sentence predates this batch.
- **basil-letters-general-corpus as the citation route.** Its `work` names only the Letters, while its `edition` is the whole vendored npnf208 volume. Citing the Prolegomena's homily extracts through it is accurate as to the file, but a row naming the Prolegomena extracts would be cleaner.
- **demo.taught-most exchange.** "the stranger" and "what is done for the least is done for him" are not in the Homily VI extract (the extract omits the stranger clause, N208:6306-6307 note, and does not quote Matt. 25:40). They are unquoted glosses of the Gospel passage, and these lines did not change in this batch.
- **story.famine-open-barns.** Round 2 asked for it to be re-assessed. Its "no direct quotation from the homilies" stance stays correct, because the famine homily itself is only summarized. No change needed.
- **Open_Gaps logging.** Log this round, R3-1 and R3-2, and the notes above in `Build/worlds/cappadocian/Open_Gaps_Tracking.md`. Rebuild the package after R3-1 and R3-2 are applied.
