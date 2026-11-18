# Council profiles, eras 1 and 2: review round 3, targeted recheck (2026-11-14)

**Scope.** Only what changed in the last commit (`HEAD~1..HEAD`) under `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/`, set against `R2_recheck.md` and the author's answer `R2_changes.md`. Changed files: the briefs and audio scripts for Arles 314, Sardica 343, Ariminum and Seleucia 359, Constantinople 381 and Chalcedon 451, and the Nicaea 325 entry. Text that did not change was not reviewed again. This is the third and last review file on each of these documents.

**Method.**
- Read the word diff of every changed file against `HEAD~1`, then read each changed sentence in its paragraph for broken first mentions, dangling references left by cuts, sentence length, AI tells and "not X but Y" contrasts.
- Checked the new Nicaea entry wording against Arius's letter to Eusebius of Nicomedia in Theodoret I.4 (`cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml` l.6030-6046: "We are persecuted, because we say that the Son has a beginning"). Checked "the synod of 382" against the Constantinople `records.json` claims (synodal letter of 382, kept in Theodoret V.9) and "Pulcheria acted with him" against the Chalcedon records claim ("the empress Pulcheria acted with him (Definition of Chalcedon; Hefele)"). Checked "still refusing" against Sulpicius II.43 as cited in R2 (`npnf211` l.11324-11333). No new quotation was added in this round.
- Counted words, ran `engine.m1.gates.grade_text` on each changed brief, split sentences and counted any over 25 words, and compared each audio script byte for byte with its brief plus `[calmly]` at the start and `[warmly]` before the last paragraph. Validated the Nicaea entry as JSON.
- No model calls, no network calls, no paid calls. No draft was edited.

## Gates (changed briefs)

| Council | Words | FK | FRE | Audio = brief | Sentences over 25 words |
|---|---|---|---|---|---|
| council-of-arles-314 | 400 | 7.72 | 60.52 | yes | none |
| council-of-sardica-343 | 398 | 7.72 | 61.04 | yes | none |
| councils-of-ariminum-and-seleucia-359 | 400 | 8.54 | 60.16 | yes | none |
| first-council-of-constantinople-381 | 399 | 7.80 | 62.10 | yes | none |
| council-of-chalcedon-451 | 398 | 7.35 | 63.38 | yes | none |

All five pass. The scores match `R2_changes.md`. The Nicaea entry parses; its brief did not change.

## Round 2 findings

| Finding | Severity (R2) | Status | Evidence |
|---|---|---|---|
| R2-1 | minor | RESOLVED | Para 5: "by the reading of Charles Joseph Hefele, the historian of the councils"; para 7 now "Hefele thinks". Side note R3-2. |
| R2-2 | substantial | RESOLVED | "Charles Joseph Hefele, the historian of the councils, says the empress Pulcheria acted with him." Matches the records' "Who called it" claim. The cut sentences (Marcian in person; Armenia at war) leave nothing dangling: no later sentence relied on either. |
| R2-3 | minor | RESOLVED | "… after the union. It also deposed Flavian …" and "… Zachariah of Mitylene. It was built on a Greek history that ran to 491." No sentence over 25 words. Side note R3-4. |
| R2-4 | minor | RESOLVED | "at Chalcedon, near Constantinople." |
| R2-5 | minor | RESOLVED | "the last twenty bishops still refusing", consistent with Sulpicius's twenty who "had not yielded". |
| R2-6 | minor | RESOLVED | "had handed over the Scriptures in the persecution." The persecution is now named before it is referred to. Side note R3-3. "himself" cut from the Milan sentence loses nothing. |
| R2-7 | minor | RESOLVED | `issue` and `uncertain` name the letter to Eusebius of Nicomedia, kept by Theodoret of Cyrrhus; "persecuted for saying the Son has a beginning" matches `npnf203` l.6045-6046. |
| R2-8 | minor | RESOLVED | "had received him into communion, as he had Marcellus of Ancyra." Marcellus can no longer be heard as a receiver. "Athanasius's Easter letters" and the cut "After this," change no sense. |
| EPH-1 | minor | Left as is; the reason holds | The 43 is credited to the assembly's own signed sentence and the dissenting count is in `contested_claims`. Unchanged; stays minor. |

The one substantial finding of round 2 is resolved.

## New findings

All are minor. None makes a claim unsupported or a quotation inexact, and none blocks.

**R3-1. Minor (Constantinople; first mention).** "chiefly Gregory and the synod of 382." The brief has not said there was a synod in 382, so a listener cannot tell it was the same bishops meeting again the next year. The records support the wording (the synodal letter of 382). Optional fix if words allow: "the bishops' synod of the next year".

**R3-2. Minor (Constantinople; parsing).** "Meletius of Antioch led them at first, by the reading of Charles Joseph Hefele, the historian of the councils, and died while they sat." The 24-word sentence passes the cap, but the long credit sits between the subject and "and died", so a listener could hear Hefele as the one who died. Optional fix: "By the reading of Charles Joseph Hefele, the historian of the councils, Meletius of Antioch led them at first. He died while they sat."

**R3-3. Minor (Arles; antecedent).** "They had asked Constantine for 'judges from Gaul,' which it had spared." "It" points back past "his ordination" to "the persecution" two sentences earlier. Most listeners will follow, but the nearest noun is the wrong one. Optional fix: "which the persecution had spared", if a word can be found.

**R3-4. Minor (Chalcedon; antecedent).** After the split, "It was built on a Greek history that ran to 491. It counts 567 bishops." The second "It" could be heard as the Greek history rather than the chronicle. Harmless to the claim, since the count is the chronicle's; optional fix "The chronicle counts 567 bishops."

No new AI tells, "not X but Y" contrasts, tail lines or over-length sentences were found in the changed text.

## Counts (new findings)

| Council | Blocking | Substantial | Minor |
|---|---|---|---|
| council-of-arles-314 | 0 | 0 | 1 |
| council-of-nicaea-325 | 0 | 0 | 0 |
| council-of-sardica-343 | 0 | 0 | 0 |
| councils-of-ariminum-and-seleucia-359 | 0 | 0 | 0 |
| first-council-of-constantinople-381 | 0 | 0 | 2 |
| council-of-chalcedon-451 | 0 | 0 | 1 |

## Final verdict

| Council | Verdict |
|---|---|
| councils-of-rome-and-carthage-251 | CLEARS (unchanged since R2) |
| council-of-arles-314 | CLEARS (R3-3 optional) |
| council-of-nicaea-325 | CLEARS |
| council-of-sardica-343 | CLEARS |
| councils-of-ariminum-and-seleucia-359 | CLEARS |
| first-council-of-constantinople-381 | CLEARS (R3-1, R3-2 optional) |
| conference-of-carthage-411 | CLEARS (unchanged since R2) |
| council-of-ephesus-431 | CLEARS (unchanged since R2; EPH-1 stays minor) |
| council-of-chalcedon-451 | CLEARS (R3-4 optional) |

All nine clear. This is the third review file on each document, so the cap is reached; the minor items above do not justify another round and may be taken up or left at the author's discretion.
