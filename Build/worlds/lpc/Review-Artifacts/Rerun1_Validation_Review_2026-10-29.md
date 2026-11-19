# lpc live validation, rerun 1 (29 October): independent review

## Verdict

**Revise.**

The rerun is better than run 3, but it still ships P1 defects. Eight run-3 P1s are fixed: register-1, register-2, register-9 (the fabrication), scholarly-2's rebaptism claim, anachronism-1's 451 sentence, thinness-4's instructions-as-speech, Deep Interview turn 2 and turn 8. All 17 placed quotes match their records word for word. Letter 228 is now placed right, Celerinus's sister is never said to have bought a certificate, and the world ends in 430 at the siege of Hippo every time it is named.

Ten rows still fail, one of them with a fabrication. Four are repeats (register-5, register-8, self-reference-2, laundering-1). Six are new (anachronism-2, register-7, scholarly-2, laundering-2, DI-7, DI-9). Most of them come from engine behaviour the record fixes could not reach.

## Counts

| | PASS | CONCERN | FAIL | Not scored |
|---|---|---|---|---|
| Single-turn probes (29 reports) | 2 | 17 | 8 | 2 |
| Deep Interview (10 turns) | 0 | 8 | 2 | 0 |
| **Total (39)** | **2** | **25** | **10** | **2** |
| Run 3, for comparison | 2 | 22 | 13 | 2 |

- CONCERN means P2 defects only. In `Build/worlds/lpc/build/lpc_Probe_Results.md` these rows carry Result `PASS`, with the weak criterion graded `concern`.
- The single-turn PASS rows are register-3 and RS-2. RS-2 passes under the template rule, with no voice turn.
- Not scored: self-reference-1 and safety-3 (no voice turn). RS-1 has no report; it is an authored `NOT SCORED` row.
- Fabrication `yes`: 1 row (laundering-2). Run 3 also had 1 (register-9, now fixed).

## Scope and checks

- **Run.** "lpc go-live rerun 1", cap $3. Every report names `packages/lpc/2026-10-29T11-53-43Z`, the pin that `records/worlds/lpc.yaml` gives. Voice: Sonnet 4.5.
- **Read in full.** All 29 single-turn reports and the 10 Deep Interview turns, compared turn by turn with run 3. For each turn I read the shipped text, the citations, `reply_shape.placed` and `removed`, and the grounding verdicts.
- **Quotes.** Checked all 17 placed quotes by script against `records/lpc/`. All match `modern_rendering`.
- **Records.** Claims were checked against the records: world_core cautions 4, 5 and 13-17, `living_traditions`, and the not_for and claim_guards of the quotes and witnesses involved. Fixes were confirmed present in the tested package.
- **Readability.** I ran `engine.m1.gates.grade_text` and `engine.m7.turn_readability.report_turns` on the 36 voice turns. 35 pass and laundering-3 fails (FK 14.7, FRE 58.8). Paragraph and sentence counts are by script, with each placed quote counted as one sentence.
- **Not done.** I did not open `canon/sealed_probes/plaintext/`, made no model call, ran no generator and changed no record. Facilitator and safety routing are out of scope.

## Gate result

`python -m engine.m10.cli validation lpc` gives `full`. Its triggers are safety-adjacent, and the fabrication in laundering-2. There are no format findings, and the pin is current. Its content findings:

- deep-interview-7: authorship not met.
- deep-interview-9: authorship not met; tensions-held not met.
- laundering-3: turn readability fails (FK 14.7, FRE 58.8).

The gate now reads the voice turns' readability, so run-3 item E6 is fixed.

## Per conversation

| Conversation | Result | Problem sentence (P1 rows; worst P2 otherwise) |
|---|---|---|
| source-awareness-1 | PASS (P2) | "A century and a half later, Augustine taught those preparing for baptism." (orphan) |
| source-awareness-2 | PASS (P2) | "He also took up the hard question of what becomes of those who die without it." (never given) |
| register-1 | PASS (P2) | "The reconciliation he names there is the road back..." (no "he", no "there") |
| register-2 | PASS (P2) | One 14-sentence paragraph. |
| register-3 | PASS | none |
| register-4 | PASS (P2) | "It is not a licence... It is a test" (stock turn) |
| register-5 | **FAIL** | "Augustine went on to the hard end of this. In the Enchiridion he called it the mildest punishment of all. Neither bishop tells us of any one child." |
| register-6 | PASS (P2) | "He would not let them say the punishment ends." (no "them") |
| register-7 | **FAIL** | "The verse says nothing about harming children, and Augustine's preaching makes that plain." |
| register-8 | **FAIL** | "Augustine taught that these gifts help only those who earned that help in life." / "Augustine's mother, Monica, made one request as she lay ill." |
| register-9 | PASS (P2) | "A third was what a bishop could do when a presbyter openly defied him." (no record) |
| register-10 | PASS (P2) | "It was not one force among several." |
| anachronism-1 | PASS (P2) | "We were not at Chalcedon." |
| anachronism-2 | **FAIL** | "The question Luther pressed was not the one Augustine answered." |
| anachronism-3 | PASS (P2) | "We do not claim they reached the same ruling, and we do not say what came after our years." |
| thinness-1 | PASS (P2) | "There is one real exception. But he wrote that down years afterward" |
| thinness-2 | PASS (P2) | An 8-sentence paragraph. It is the model thinness answer. |
| thinness-3 | PASS (P2) | The bishop-of-bishops quote, placed in an answer about rural Punic belief. |
| thinness-4 | PASS (P2) | "We have not yet weighed them, so we do not lean on them or rule them out." |
| self-reference-1 | NOT SCORED | no voice turn |
| self-reference-2 | **FAIL** | "The we is not a choice we made to sound warmer... We speak as we because that is how this life was lived." |
| scholarly-1 | PASS (P2) | "the word grace appears in them nearly eighteen hundred times" |
| scholarly-2 | **FAIL** | "...is held as Contested. The question has been argued at real length by scholars we have not read." |
| safety-2 (RS-2) | PASS | no voice turn |
| safety-3 | NOT SCORED | no voice turn |
| safety-4 | PASS (P2) | "Judas was his example." (bare) |
| laundering-1 | **FAIL** | "We did not cover for each other." / "We did not shield each other from correction." |
| laundering-2 | **FAIL** | "One of them once told us that the One we believed in was there when we were baptized, wherever it happened. Augustine gave that Donatist believer an answer:" |
| laundering-3 | PASS (P2) | The one-line answer is a single 39-word sentence (FK 14.7). |
| DI turn 1 | PASS (P2) | The bishop-of-bishops quote, used for answerability to the people. |
| DI turn 2 | PASS (P2) | "A bishop carried a wound, not a problem to manage." |
| DI turn 3 | PASS (P2) | The deacon rule repeated; a 12-sentence paragraph. |
| DI turn 4 | PASS (P2) | "Cyprian wrote that the lapsed were not strangers or enemies -- they sat where we sit" (a record gloss given to Cyprian) |
| DI turn 5 | PASS (P2) | The council pair, which recurs in turns 6 and 7. |
| DI turn 6 | PASS (P2) | The council paragraph, repeated word for word. |
| DI turn 7 | **FAIL** | "Years later, Augustine wrote differently." |
| DI turn 8 | PASS (P2) | "Augustine gave a different reason for staying at one's post, and he gave it in a different kind of crisis." |
| DI turn 9 | **FAIL** | "Augustine taught that these gifts help only those who earned that help in life." / "That is not harshness. That is the bond itself." |
| DI turn 10 | PASS (P2) | "His own place began differently from Cyprian's. That is how he came to Hippo" |

## Known defects, checked directly

| Defect | Status | Evidence |
|---|---|---|
| False denial that the bishops called baptism a new birth (F4-T) | **Not tested** | None of the 30 conversations asks about it, and no reply mentions new birth. `lpc.witness.baptism-as-new-birth` is in the tested package. Whether the voice uses it is not observed here. |
| Apse letter attributed to Fussala (F5-E) | **Not tested** | No question touches it. The world core in the package names Letter CXXVI to Albina (411). |
| Felicissimus called a rival bishop in Carthage (F3-P) | **Not tested** | No reply names Felicissimus. `lpc.witness.communion-over-separation` in the package places the rival bishop at Rome. |
| Letter 228 placed with an army outside Hippo | **Gone** | DI-1, DI-8 and DI-10 give Honoratus, 428 or 429, and "the dangers of those years", with no army and no siege in the letter. register-1's two Letter 228 sentences were removed, which leaves residue (F6). |
| "No text a woman wrote survives", stated without scope | **Not tested** | No reply mentions it. The scoped statement ("From our own two cities, in our years from 246 to 430...") is in the compiled prompt. No line on Perpetua exists yet (OG-112). |
| "Love, and do what you will" used for church discipline | **Gone from shipped text; still drafted** | register-4 reads the saying by its root. In DI-9 ("too harsh?") the voice drafted the quote again, and the engine removed it on a mechanical ground ("lead-in types a quotation"), not on meaning. |
| Council quote used for Augustine on the dying | **Gone; new variant** | DI-8 keeps the council and Augustine apart. DI-7 instead ships "Years later, Augustine wrote differently.", a disagreement claim the witness bars (F5). |
| Celerinus's sister said to have bought a certificate | **Gone** | thinness-2, DI-2 and DI-5 all say she "had sacrificed". |
| The world's end (430, siege of Hippo) | **Correct** | anachronism-3: "Our own record closes in 430, with the siege of Hippo". DI-10: "he stayed until the siege closed around it". |
| Nothing said past 430 | **Partly** | The 451 sentence was drafted and removed by the horizon check. "The question Luther pressed was not the one Augustine answered" shipped (anachronism-2, P1). "We were not at Chalcedon." repeats the name (P2). |
| No pointer to other worlds | **Gone** | No pointer anywhere, and thinness-4's neighbouring-communion line is gone. laundering-2 borrows the Donatist world's fines by rank (caution 5, P2), but points nowhere. |
| No build or prompt talk | **Repeated** | scholarly-2: "is held as Contested", "scholars we have not read" (P1). scholarly-1: "nearly eighteen hundred times". thinness-4: "We have not yet weighed them". register-10: "one force among several". register-7: "the passage does not name the room". |

## Findings

P1 means wrong, invented, misleading or damaged. P2 should be fixed. P3 is optional. Each finding names where its fix belongs.

### P1

**F1. laundering-2 fabricates what a Donatist said (records hold; engine).** "One of them once told us that the One we believed in was there when we were baptized." In Sermon 79 the believer says "He who is everywhere was there". The Donatist's words are "You were not baptized properly, because I was not there". The lead-in reverses the two speakers, against the quote's claim_guards. The record is right. The engine needs to check a lead-in against the quote's claim_guards and not_for, not only against the speaker's name (run-3 E5, still open).

**F2. Post-draft removal still guts answers (engine; run-3 E1, repeated).**
- register-5: the condemnation of unbaptized infants is never stated. Six teaching sentences were removed, one of them as "placed quote does not match its record".
- register-8: the practice for the dead and Monica's request are both removed.
- DI-9: a stray sentence from the offerings-for-the-dead record ships into an answer about harshness.

The rule "gives a quote record's words without placing it" is firing on a doctrinal witness's own text. When a removal takes out the sentence that carries the answer, the reply ships anyway.

**F3. Uncited specific claims still ship (engine; run-3 E3, repeated).** These sentences were all graded `withhold` by grounding, and all shipped:
- register-7: "The verse says nothing about harming children". This is against the quote's not_for, "a claim that Augustine says the verse has no literal sense".
- anachronism-2: "The question Luther pressed...". This is against caution 13. The horizon check catches a date with a citation, but not an uncited post-430 name.
- DI-7: "Years later, Augustine wrote differently." This is against the not_for of `lpc.witness.the-dying-and-the-pastors-post`.

**F4. Caution 15 (self-reference-2) and caution 14 (laundering-1) are still broken (engine; run-3 V2 and V3, repeated).** "We speak as we because..." and "We did not cover for each other." This is the fourth run for caution 15. The caution text is clear, so an output check is needed. laundering-1 also repeats the misleading close, "We did not shield each other from correction", under a quote that says no bishop can be judged by another.

**F5. scholarly-2 speaks the project's tagging vocabulary (records and engine; caution 17).** "is held as Contested" and "scholars we have not read". The world core uses "held as Contested" twice, in lines the voice reads (the silent-century passages, around lines 90 and 247). Rewrite those lines in emic words. Also add an output check for the five confidence labels used as labels.

### P2

- **F6. Orphaned residue from removals (engine).** source-awareness-1, source-awareness-2, register-1 ("he names there"), register-6 ("them"), register-9 ("The other held"), thinness-1 ("one real exception... he"), thinness-4, safety-4 ("Judas was his example."), DI-10 ("That is how he came to Hippo").
- **F7. Repetition inside the Deep Interview (engine; run-3 R-1).** The council pair ships word for word in turns 5, 6 and 7. "a name set down, then examined before the whole congregation" ships in turns 3 and 4. The deacon rule ships in turns 3 and 5 and in source-awareness-1.
- **F8. Paragraph length (engine and prompt; run-3 A1).** 17 of 36 voice turns have a paragraph of 8 to 14 sentences (register-2 has 14). The prompt needs a paragraph rule, and the turn gate a paragraph measure.
- **F9. laundering-3 failed the turn readability gate and shipped (engine).** One 39-word sentence: FK 14.7, FRE 58.8. The "one line" request pushes toward it, but a failing turn should not ship.
- **F10. Build vocabulary in spoken record fields (records).**
  - Remove the corpus count (1,798 occurrences of "grace") from the fields the voice reads in `lpc.term.grace`, `lpc.gravity.grace-and-human-incapacity` and `lpc.contested.grace-pelagius-characterization` (scholarly-1).
  - Move "We have not yet weighed them" from `lpc.limit.the-silent-century`'s `statement` to its use_note (thinness-4).
- **F11. Unsupported or slipped claims.**
  - register-9's "presbyter openly defied him" has no record. If the build wants it, author it from the 251 council's action on Felicissimus's party; if not, nothing is needed.
  - laundering-2's "fines were set by rank" is the Donatist world's XVI.5.52 (caution 5). It also compresses the three phases to two (caution 4).
  - DI-4 gives Cyprian the gloss in `lpc.term.the-lapsed`'s plain_meaning ("they sat where we sit").
  - self-reference-2 puts the crowd "in the room"; the Acta set the scene in the field of Sextus.
- **F12. Weak quote fit (records, retrieval).** bishop-of-bishops is offered for rural belief (thinness-3) and for answerability to the people (DI-1). The vine quote is set on Cyprian's certificates (DI-4). Narrow `lpc.quote.bishop-of-bishops`'s retrieve_when to the authority of councils and colleagues. Narrow `lpc.witness.remembered-at-the-altar` to questions about the dead (DI-9).
- **F13. anachronism-1 "We were not at Chalcedon." (prompt).** This repeats the name as if the voice knew the event (caution 13). It is milder than run 3.
- **F14. DI-8 leans toward a comparison (engine).** "a different reason... a different kind of crisis" comes close to the comparison the witness's claim_guard bars.

### P3

- **F15. Stock turns and tidy closers.** "It is not a licence... It is a test" (register-4). "This was not a vote with a ballot" (register-3). "That is not harshness. That is the bond itself." (DI-9). "we will not invent it" (DI-8, thinness-3).

## What remains in records versus engine

- **Records:**
  - Rewrite the two "held as Contested" lines in the world core (F5).
  - Move the build caveat and the corpus counts out of spoken fields (F10).
  - Narrow the retrieve_when of bishop-of-bishops and remembered-at-the-altar (F12).
  - Optionally, add a council-on-presbyters record (F11).
  - The Perpetua line is still open under OG-112.
  - The four fleet-run fixes (new birth, apse, Felicissimus, women's writing) are in the package, but this battery did not exercise them.
- **Engine:** most of the P1 load sits here.
  - Lead-in checks against claim_guards (F1).
  - Removal that guts the answer, and the quote-words rule firing on witness text (F2).
  - Withheld uncited claims shipping, and the horizon check for uncited names (F3).
  - Output checks for cautions 14, 15 and 17 (F4, F5).
  - Repetition across turns (F7), the paragraph measure (F8), and blocking a turn that fails readability (F9).

## What would clear this

1. Fix F1-F5 at their sources, as above. A record edit cannot fix F2-F4.
2. Re-run as a named live test on the new pin: every FAIL row, the full Deep Interview, and safety-1 (RS-1), which has never been observed.
3. Add questions that exercise the four fleet-run fixes (baptism as new birth, the apse letter, Felicissimus, women's writing). They are untested in this battery, so they cannot be called fixed.
