# syr fleet graded run 1 (28 October): answer review

## Verdict

**Revise.**

Mar Yausep is readable and mostly faithful. Most answers speak in the world's own images: the Physician, the wound shown to the healer, the house built on the Stone, the one woven Gospel, the covenant kept in town. The honest limits are strong. The answers on a typical day (f5-i), marriage (f5-t), how to join (f4-i) and evidence for rituals (f4-e) say plainly what the record does not hold, and they still give what it does hold.

Five of the 28 answers fail. Three causes account for most of what is wrong:

- **No quote reached a participant.** The voice tried to use a quote 21 times across 13 answers, and the engine removed every attempt. 15 of the 21 removals say "lead-in to a placed quote does not name its speaker". The voice wrote "our own sage" and "our poet", which is how this world's own records name Aphrahat and Ephrem. The admission path never told the voice the naming rule that the net then enforces. The cuts leave dangling words ("He strung Scripture's own names", "That turning of the pearl", "That one archived sentence") in nine answers.
- **The voice falls out of the world under pressure.** f2-e talks about "the voice", "your limits" and "your answers". f6-e says "No record given to me for this turn". f6-p opens "I am a representative of Syriac Christianity". These are the chatbot speaking, not the world.
- **Uncited or weakly grounded claims ship.** The grounding net marked them "withhold" and shipped them anyway. These include the misdescribed Demonstrations (f1-e), "the Peshitta nowhere" (f2-e) and the named later churches (f3-t).

The automatic checks passed all 28 probes. That result does not stand once the answers are read.

## Scope and method

- **Run.** Fleet graded run 1, approved by Mark 2026-10-28. Report `engine/m3/reports/fleet-graded-run-1/syr.json`. Voice: Sonnet 4.5. There was no safety call, no reader call and no self-revision (admission harness path). Package pin `packages/syr/2026-10-28T03-51-22Z` (manifest hash matches `records/worlds/syr.yaml`).
- **Questions.** Read from `canon/sealed_probes/plaintext/<probe_id>.md`, as instructed for this review.
- **Method.** Same as `Build/worlds/lpc/Review-Artifacts/Run3_Access_And_Craft_Review_2026-10-28.md` and the rubric in `Build/worlds/lpc/build/lpc_Probe_Results.md`:
  - P1 means wrong, invented, misleading or damaged. P2 means small and plainly fixable.
  - Each answer is graded on four criteria: Rigor, Accessibility, Craft and Focus.
  - A row with only P2 defects is PASS. A row with any P1 defect is FAIL.
  - Each fix is named at the source: a record, a caution or an engine item.
- **Records.** Every factual claim was checked against the compiled `repository.json`, the world_core horizon and cautions 1-10 in `prompt.txt`, and the `not_for` of every record and quote the answers drew on (about 45 records).
- **What was offered, and why sentences were cut.** I re-ran `engine.m4.evidence.assemble_evidence` and `engine.m4.turn.apply_net` offline on each saved `raw_text`. No model was called. The SDK imports were stubbed. All 28 replays reproduce the shipped `answer_text` exactly. So the offered ground and the removal reasons below are what the run did. One limit: the voice also cites records it read in the system prompt, so "not offered" means not in the turn's ground block.
- **Readability.** `engine.m1.gates.grade_text` on every shipped answer. FK runs 4.2-8.3. FRE runs 58.6-83.8. Only f2-e falls below FRE 60.
- **Quote context.** No quote was placed in any answer, so no shipped quote is out of context. Every quote the voice tried to place is checked in the notes. One attempt was out of context: f5-p applied `syr.quote.warned-before-baptism` to every baptism, which its not_for bars. It was cut.
- **Not compared** with any run dated before 2026-10-27, as instructed. No git command was run, and no other file was edited.

## Results

| Probe | Result | Severity | Cause layer | Fix |
|---|---|---|---|---|
| c-i-probe-01 | PASS | P2 | engine cut | E1. The Aphrahat "sure thing" sentence was cut, so "He used Scripture's own names" now reads as if Jesus used them, and the answer never says Jesus is God. |
| c-e-probe-01 | PASS | P2 | voice not told what is unknown | R4. The real route by which the faith reached Edessa is unknown (`syr.contested.edessa-origins`, which was offered). The answer gives the legend and the harmony but never says the route is unknown. "Sheol" and "the Apostle" are not introduced. |
| c-p-probe-01 | PASS | - | - | None needed. The one-innocent quote was cut, and the rest stands. Faithful to `syr.dw.physician`. The advisory "aphorism" is the record's own sentence. |
| c-t-probe-01 | PASS | P2 | engine cut; wrong record offered | E1 (three quotes cut; "He strung..." has no antecedent). E3 (Aphrahat's names are cited to `syr.dw.god`, which does not hold them). R5 (`syr.dw.was-jesus-god`'s text "We stood with the great council's faith", spoken by a Persian-side voice, drifts toward its own not_for). |
| f1-i-probe-01 | PASS | P2 | engine cut | A 12-sentence paragraph (A1). Joseph and Moses were dropped from the roll-call when the litany tag was cut (E1). The answer stays faithful to `syr.dw.god` and `syr.dw.suffering`. |
| f1-e-probe-01 | **FAIL** | P1 | missing record; engine | "twenty-three Demonstrations, each one written to refute a rival teacher by name or to correct a wrong turn inside the faith". This is wrong. Most of the Demonstrations are pastoral teaching (faith, love, fasting, prayer, the covenant). It is offered as the evidence the question asks for. The net withheld it (25% grounded) and shipped it. Fix: E2, and R1 (give `syr.term.tahwyata` a plain sentence the voice can say about what the Demonstrations are). The right record `syr.dw.decides` was not in the ground block. The voice used the prompt copy. |
| f1-p-probe-01 | PASS | P2 | right record not offered; engine cut | "The only fatal mistake is hiding the wound" lost its lead-in (E1). The penitence-for-sin material answers a question about doubt. `syr.demo.room-for-doubt` and `syr.dw.doubt` were not offered, and `dw.doubt` says a private crisis of doubt is not recorded (R6). |
| f1-t-probe-01 | PASS | P2 | engine cut | "Our sage taught it with a picture. On faith the whole house is raised" lost the Stone (E1). Otherwise exact to `syr.dw.adam-grace`, and its not_for on original guilt is kept. |
| f2-i-probe-01 | PASS | P2 | engine cut | "That turning of the pearl was how we read" refers to a quote that was cut (E1). |
| f2-e-probe-01 | **FAIL** | P1 | caution wording; engine | Voice-itself: "I honor the question. Let me walk through...", "you named the gap honestly in your limits, then walked past it in your answers", "Some days the voice wanted to give a fuller picture". The voice is grading its own build. Wrong claim: "the Peshitta nowhere". Aphrahat's Old Testament is the Peshitta Old Testament, and the record bars only the Peshitta Gospels as the normative text. Also: markdown headings stripped, leaving a headless fragment ("Any claim about what it felt like..."), the typo "theRecord's", and FRE 58.6. Fix: V1, E2, and R2 (an in-voice answer for "would a scholar believe you"). |
| f2-p-probe-01 | PASS | P2 | engine cut | "A whole chapter's worth of meaning was found in a single pearl" is unexplained, because both pearl sentences were cut (E1). A 10-sentence paragraph (A1). |
| f2-t-probe-01 | PASS | P2 | engine cut | The same orphaned "single pearl" (E1). Otherwise exact to `syr.dw.reading`. |
| f3-i-probe-01 | PASS | - | - | None needed. Office, vow and trusted teacher are held unsettled, as `syr.dw.authority-lived` holds them. The catholicos caution (7) is kept. |
| f3-e-probe-01 | PASS | P2 | wrong record offered; caution wording | The only record offered was `syr.term.catholicos`. The voice answered from the prompt copy of `syr.dw.outsiders-empire`, and that record's text states two disputed points as settled: the flood line (against `syr.story.edessa-flood-201`'s not_for) and Rome's conversion as the cause of the persecution (`syr.story.simeon-martyrdom` calls this partly later framing). Fix: R3 and E4. |
| f3-p-probe-01 | PASS | P2 | right record not offered | `syr.dw.failures` was not offered. It holds the record's own failures and "we did not see our failures as failures" (E4). P2 voice: "I will not invent a process", singular and narrating the refusal. P2 access: a 52-word sentence. |
| f3-t-probe-01 | **FAIL** | P1 | caution wording; engine | Horizon: it names "Syriac Orthodox, Church of the East, Maronite", says the harmony "was eventually replaced", and says the cities "vanished under later occupation". This breaks `syr.dw.one-church`'s not_for ("an answer to which modern church continues this one"). Wrong claim: the Persian church organized "at a synod we did not live to see". The 410 synod closes the window and is inside it (`syr.force.synod-410`, `syr.dw.decides`). The net withheld the church-names sentence and shipped it. Fix: C1, E2 and E5. |
| f4-i-probe-01 | PASS | P2 | missing record | "The one coming to baptism was taught the Gospel... That story was what shaped a believer before the water" is an unattested step in a sequence the record says it cannot give (`syr.limit.ritual-sequence`). Fix: R7. Otherwise a model honest-limit answer. |
| f4-e-probe-01 | PASS | P2 | - | Faithful, and it keeps the flood-line doubt ("we cannot be sure it stood in the first telling"). P2 access: a 44-word sentence and an 8-sentence paragraph. |
| f4-p-probe-01 | PASS | P2 | engine cut | "Our teacher answered that..." now answers no one, because the taunt sentence was cut (E1). It closes on a probing personal question ("Does your own mind race because of something you did...?"), which is therapist cadence. It keeps "not our idiom" from the record. |
| f4-t-probe-01 | PASS | P2 | caution wording | Exact to `syr.dw.born-again-endtimes`. P2: the coined closer "as public as a wedding, and we sang it the same way" implies a wedding custom that `syr.limit.marriage` says is unknown. |
| f5-i-probe-01 | PASS | P2 | - | Strong limits for women, the laity and the enslaved. P2: "Bardaisan's circle at the royal court" (c. 200-214) is given as the milieu of a typical day across the whole window. An 8-sentence paragraph. |
| f5-e-probe-01 | PASS | P2 | engine cut | The chronicle sentence was removed ("placed quote does not match its record"). Now "No foundation of it has been excavated" and "That one archived sentence is our earliest hard trace" point at nothing (E1). The flood line is also called a hard trace with no dispute (R3). |
| f5-p-probe-01 | PASS | P2 | right record not offered; record conflict | "When the persecution came, bishops died first, then the covenant's vowed members" comes from `syr.dw.cost-distance` (the F5-P record, not offered). It is cited to `syr.gravity.persecution-endurance` instead, and it conflicts with `syr.gravity.covenant-life`'s not_for ("the order was a targeted group"). Fix: R8. The warned-before-baptism lead-in ("warned each one") was cut. |
| f5-t-probe-01 | PASS | P2 | - | A model limit, from `syr.limit.marriage`. P2: it cites the two demonstrations as sources, and "We will not borrow customs..." narrates the refusal. |
| f6-i-probe-01 | PASS | P2 | caution wording | Faithful to cautions 4 and 9 and to `syr.dw.unsettled`. P2 voice: "What troubles me now", "unsettles me most". The voice is a people speaking ("we"), never one witness (V1). A 9-sentence paragraph. |
| f6-e-probe-01 | **FAIL** | P1 | voice not told what is unknown; caution wording | "I do not know what you are talking about. No record given to me for this turn says... The ground I have been given includes... Where are you getting this from?" The content is right: no source of this world was taken under torture. But the voice reads out its own machinery and turns on the asker. Fix: R2 (an honest limit for a premise the record does not hold), V1 and E6. |
| f6-p-probe-01 | **FAIL** | P1 | right record not offered; record text | It opens "I am a representative of Syriac Christianity (Edessa/Nisibis), not here to judge you". That is copied from `syr.demo.someone-like-me`'s own text. It then answers as if the asker were joining the covenant ("What it would have cost you, plainly: marriage given up for life"). It does not say how the community regarded people unlike itself, which is what the demo holds. The demo (cell F6-P) was not in the ground block. Fix: R9 and E4. |
| f6-t-probe-01 | PASS | P2 | - | Holds "confidence in the Judge, not a roster", as `syr.dw.death-judgment` does. P2 focus: the second paragraph is Aphrahat's path for believers (`syr.limit.what-must-one-do`), not the fate of outsiders. |

## Findings and fixes

### P1

**E1/E5. No quote was placed in any of the 28 answers (engine).** This is the most important finding for the world's distinctiveness.
- 15 of the 21 removals give "lead-in to a placed quote does not name its speaker". The rest give "tagged to a quote record that has not been placed", "gives a quote record's words without placing it" and "placed quote does not match its record".
- The cause is a parity gap. `engine/m4/turn_prep.py` tells a live voice to name the speaker before a quote (QUOTE_SPEAKER_LINE and QUOTE_OFFERS_LINE). `engine/m3/generation.py` `LiveModelAnswerer` builds its message from `render_evidence_block` alone, so the voice is never told the rule, and `apply_net` then enforces it. The world's own idiom ("the sage", "our poet", "our teacher") makes this fail every time.
- `syr.figure.aphrahat` lists "the Persian sage" as its in-world name. The voice wrote "our own sage", which the net does not match.
- Fix (engine): give the admission answerer the same turn_prep directives a live turn gets, so the graded draft is a production draft. Let speaker matching accept a figure's listed in-world names. Then re-run.
- Until then, this run does not measure quote use at all. In nine answers, a removal leaves a sentence that points at nothing (c-i, c-t, f1-p, f1-t, f2-i, f2-p, f2-t, f4-p, f5-e).

**E2. Withheld claims ship (engine).** The net marked these sentences `withhold`, then shipped them with the citation stripped:
- f1-e: "twenty-three Demonstrations, each one written to refute a rival teacher by name". This is wrong.
- f2-e: "the Peshitta nowhere". This is wrong.
- f3-t: the named later churches. This is horizon.
- Fix: a `withhold` on a specific claim (proper noun, number) holds the sentence for a grounded redraft or removes it. It does not ship the words without the tag.
- The `window_end` check removes only sentences that name a later date or event the records do not name. Church names with no year pass it. It should also test names against the world's not_for and horizon terms.

**V1. The voice reads out its own machinery (caution and engine).**
- f2-e: "the voice", "your limits... your answers", "I honor the question. Let me walk through".
- f6-e: "No record given to me for this turn", "The ground I have been given", "the sources listed here".
- f6-p: "I am a representative of...".
- Fix (prompt and caution): the "Below this line" block in `prompt.txt` speaks of "the ground given with each turn". Add a standing line that the voice never names its records, its ground, its turn, its limits or itself as a voice or representative.
- Fix (engine, E6): an output check for "given to me", "this turn", "the voice", "my/your limits", "I am a representative", "Let me walk through", and markdown headings.

**C1. f3-t: present-day churches and post-410 history (caution).**
- `syr.core.syriac`'s cautions carry no rule for after 410. Only caution 7, which covers catholicos and the School of Nisibis, touches later history.
- Fix: add a horizon caution in the voice's own words. The voice knows nothing after 410. To "which church continues you", it says what it was and that it cannot speak of later churches. It names none.
- Correct the record of when the voice's years end. The 410 synod is the close of "our years", and inside them. This answer said "a synod we did not live to see", which contradicts `syr.dw.decides` and `syr.dw.unsettled`.
- Make sure `syr.dw.one-church` (with its not_for) is retrieved for this cell (F3-T). It was not offered. The voice found it in the prompt.

**R1. f1-e: what the Demonstrations are (record).**
- `syr.term.tahwyata` holds the fact ("twenty-three reasoned teaching letters, composed in dated phases between 336 and 345"), but it was not offered for F1-E.
- Fix: offer it for "what evidence" questions on authority. Add a not_for: "a claim that each Demonstration refutes a named rival".

**R2. f2-e and f6-e: no in-voice answer for outside-scrutiny and false-premise questions (record).**
- Author an honest limit for each.
- Scrutiny: what can be checked (self-dated letters, ancient copies, the archive line) and what cannot (the laity, women, the Jewish side, 373-410), in the "we" voice. Base it on `syr.dw.corpus-and-its-edges`, which already says most of it. It was offered for f2-e, and the voice went meta anyway.
- False premise: "No account of our worship was taken from us under torture. What we have is our own letters and hymns, a city chronicle, and later church histories."

**R9. f6-p: `syr.demo.someone-like-me` (record and retrieval).**
- Its own representative text opens with "I am a representative of Edessa and Nisibis, not here to judge you". The voice copied that line.
- Fix: rewrite the opening in the world's own voice.
- Retrieval: the F6-P demonstration was not in the ground block. The ground block carried the covenant and the what-must-one-do limit instead. Check why the F6-P demonstration is not reaching its own cell (E4).

### P2

- **E4. Right record not offered (retrieval).**
  - f3-e: only `syr.term.catholicos`; it needed `syr.dw.outsiders-empire`.
  - f3-p: needed `syr.dw.failures`.
  - f5-p: needed `syr.dw.cost-distance`.
  - f1-p: needed `syr.demo.room-for-doubt` or `syr.dw.doubt`.
  - f6-p: needed `syr.demo.someone-like-me`.
  - f1-e: needed `syr.dw.decides`.
  - f3-t: needed `syr.dw.one-church`.
  - Each is the cell's own record. The voice often found the text in the prompt anyway, but it then answered without the record's not_for in the ground block. Fix: offer a cell's own records first for a canon-cell probe.
- **E3. Citations attach to the wrong record.** c-t cites `syr.dw.god` for Aphrahat's names. f5-p cites `syr.gravity.persecution-endurance` for a `cost-distance` sentence. Same fix as the lpc grounding-net item: require shared content with the cited record's text.
- **R3. Disputed points stated as settled in record text.** `syr.dw.outsiders-empire`, `syr.dw.remains` and `syr.dw.corpus-and-its-edges` state the 201 flood line as fact ("a church building stood"). `syr.story.edessa-flood-201` bars "a claim that the church-destruction line is certainly original". `syr.dw.outsiders-empire` also states Rome's conversion as the cause of the persecution, which `syr.story.simeon-martyrdom` calls partly later framing. Fix: write "the city chronicle records" into those texts, as `syr.dw.corpus-and-its-edges` already does in its next clause.
- **R4. c-e: the route of arrival.** Give `syr.contested.edessa-origins` a plain voice line: "By what road the faith first reached our city, no one knows."
- **R5. `syr.dw.was-jesus-god`'s text.** "We stood with the great council's faith" should carry its own position's qualifier, that the Roman-side church stood within it, so that a Persian-side voice does not claim formal reception (its own not_for).
- **R6. f1-p: doubt.** Add `syr.dw.doubt` and `syr.demo.room-for-doubt` to F1-P retrieval. The answer should say a private crisis of doubt is not written about, as `dw.doubt` does.
- **R7. f4-i: what came before baptism.** Add an absent_detail to `syr.limit.ritual-sequence`: what a candidate was taught before the font is not recorded. Offer `syr.quote.warned-before-baptism` here, since it is the one text on what was asked of a person before baptism.
- **R8. Record conflict.** `syr.dw.cost-distance` says the persecution "fell hardest on clergy and on members of the covenant. Bishops died first". `syr.gravity.covenant-life` bars "a claim that the order was a targeted group in the persecution". Decide which holds and align the two. Escalate if the evidence is unclear.
- **A1. Paragraph length.** Paragraphs over four sentences appear in 27 of 28 answers. The worst are 12 (f1-i), 10 (f2-p) and 9 (f1-e twice, f2-t, f6-i). The same fix as lpc A1 applies (prompt rule plus a paragraph measure in `engine/m7/turn_readability.py`).
- **Voice slips.** "me" (f6-i), "I will not invent" (f3-p), therapist closer (f4-p), coined wedding closer (f4-t), narrating the refusal (f3-p, f5-t). These are covered by V1 and the output check.

## Top failure causes

1. Engine cut: every quote was removed, because the admission path omits the speaker-naming directive and the world's own epithets fail the net (E1/E5). This touches 13 answers and leaves dangling words in nine.
2. The voice breaks out of the world into system or assistant language (V1). Three FAILs: f2-e, f6-e, f6-p.
3. Withheld specific claims ship unchecked, and the horizon check misses names with no date (E2). Three FAILs: f1-e, f2-e, f3-t.
4. Right record not offered for the cell's own question (E4). Seven answers.
5. Caution wording: no post-410 or present-day-church caution (C1), and record texts state disputed points as settled (R3).

## Counts

- Single-turn answers graded: 28. There are no Facilitator turns in this harness: no safety or reader call was made.
- P1 findings: 8, in 5 rows (f1-e 1, f2-e 2, f3-t 2, f6-e 1, f6-p 2).
- P2 findings: 35, across 24 rows (23 PASS rows and f2-e).
- Rows with an invented or wrong fact, a horizon breach or a misused quote: 3 (f1-e, f2-e, f3-t). No quote was shipped, so none is misused.

PASS 23, FAIL 5, NOT SCORED 0 of 28
