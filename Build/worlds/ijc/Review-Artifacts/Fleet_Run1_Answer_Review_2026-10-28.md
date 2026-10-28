# ijc fleet graded run 1 (28 October): answer review

## Verdict

**Revise.** 14 of the 28 answers fail. All 28 passed the run's own automatic checks (`source_boundedness`, `register_coined_aphorism_heuristic`), so those checks caught none of the failures below.

At its best Marius is plain, firm and honest about the record's narrow scope. The Callinicum answer (f3-p) names the world's own stain and does not soften it. The marriage answer (f5-t) and the original-sin opening (f1-t) are clear and faithful. The thin-record answers (f4-p, f5-i, f6-e) say "our record does not hold them" without inventing anything.

Five causes account for most of the failures:

- **Post-draft removal (engine).** The net removes the sentence that carries the answer, or the sentence a later line points back to. In f1-i the answer to the question is gone. In f3-i and f4-e the cut makes what is left say something false.
- **After the window.** f3-t names the East-West schism and the Reformation. f6-i says Chalcedon's rejection "hardened into durable division". f5-e says buildings and inscriptions "still stand".
- **The record's silence told as the world's silence.** f1-t calls Augustine's teaching on inherited guilt something "your later ages built". f6-t says there was "no settled teaching handed down" on the fate of the unbaptized. Augustine wrote both inside this window. Caution 6 says the narrow citation scope is not the window's own boundary, but the voice is not keeping that line.
- **Retrieval offers the wrong record.** `ijc.limit.later-questions` (faith against works) is offered for F1-T, F6-P and F6-T. `ijc.dw.room-for-hesitation` is not offered for F1-P, the question it was written for.
- **Readability hard-fails that nothing caught.** Four answers fall below FRE 60 or above FK 10 (c-e, f1-e, f2-e, f6-i). The admission harness does not run `engine/m7/turn_readability.py`.

## Scope and checks

- **Run.** Fleet graded run 1, world ijc, 28 sealed probes, protocol "blind". Voice: Sonnet 4.5 (`us.anthropic.claude-sonnet-4-5-20250929-v1:0`). The run made no safety or reader call. Package `packages/ijc/2026-10-28T03-50-07Z`, manifest hash `5dbbcb89…`, which matches the registry pin in `records/worlds/ijc.yaml`. Report: `engine/m3/reports/fleet-graded-run-1/ijc.json`.
- **Read in full.** All 28 questions (`canon/sealed_probes/plaintext/<probe_id>.md`) and all 28 shipped `answer_text`s. For each answer I also read `raw_text` to see which sentences the net removed, and the `citations` and `citation_entries`.
- **Records.** Claims were checked against the compiled `prompt.txt` (world_core cautions 1-7, every term, witness, limit, story and demonstration it carries) and against `repository.json` and `records/ijc/` for the forces, gravities, contested claims and quote records the answers draw on.
- **Quotes.** All five placed quotes match their record's `modern_rendering` exactly, checked by script: leo-sinner-be-glad, the-rudiments-of-the-creed (twice), ammianus-roman-luxury and a-fine-talent-for-making-verses. Context was checked against each record's `use_note.not_for` and `modern_lens_note`.
- **Evidence offered.** The run does not save the per-turn ground. I rebuilt it with `engine.m4.evidence.assemble_evidence` on the pinned package, which is local code and makes no model call. This uses the code as it is checked out now. The run was recorded at commit `00b3e5b`, and I did not confirm the two are the same, since no git command was run. The "right record not offered" and "wrong record offered" calls rest on that rebuild.
- **Readability.** I ran `engine.m1.gates.grade_text` on every answer. Sentence and paragraph counts are by script, with placed quotations counted as one sentence.
- **Not done.** No model was called and no git command was run. Only this file and its `.counts.json` were written. Earlier data from before 27 October was not compared, per the instruction.

## Method

This follows `Build/worlds/lpc/Review-Artifacts/Run3_Access_And_Craft_Review_2026-10-28.md` and the rubric in `Build/worlds/lpc/build/lpc_Probe_Results.md`:

- **P1** is wrong, invented, misleading or damaged. **P2** is small and fixable.
- Four criteria are graded per row: Rigor, Accessibility, Craft, Focus.
- A row with any P1 is **FAIL**. A row with only P2s is **PASS**, and its P2s are noted.
- **NOT SCORED** is for a row with no voice answer. Every ijc probe got a voice answer, so no row is NOT SCORED.
- Accessibility is a concern where a reader meets a paragraph of 8 or more sentences, a sentence of the voice's own over 30 words, or a term used before it is explained.
- A turn above FK 10 or below FRE 60 is a hard fail under the project's own per-turn gate (`engine/m7/turn_readability.py`, the NorthStar decision). I grade it FAIL even when its content is sound, and mark it "P1 (readability gate)".
- Each fix is made at the source: a record, a caution or an engine item, never a patch to one answer.

## Results

| Probe | Result | Severity | Cause layer | Fix |
|---|---|---|---|---|
| c-i-probe-01 | PASS | P2 | engine cut (residue); citation | The net removed the creed's "for us and for our salvation" line, so the answer loses what Christ did. The opening sentence cites `ijc.dw.bread-made-body` for `ijc.dw.jesus`'s words. An 11-sentence paragraph. Engine E1 and citation matching (E4). |
| c-e-probe-01 | FAIL | P1 (readability gate) | engine (readability not gated); right record not offered | FRE 57.2. Content is faithful to `ijc.dw.received-not-seen`, but that record was not offered (baptism-threshold was). Run the turn gate in the harness (E5). Map C-E to received-not-seen in coverage (R1). Split the 30-word Paschasinus sentence in that record's text. |
| c-p-probe-01 | PASS | P2 | - | Follows `ijc.demo.want-to-believe`. The Leo quote fits its context ("someone not yet certain"). P2: a 38-word creed sentence. |
| c-t-probe-01 | PASS | P2 | engine cut; record wording | 381 and the Spirit match `ijc.gravity.precision-seeking`. P2: "Leo's letter to Chalcedon" (the Tome went to Flavian in 449); "cost real blood" is uncited; "The Father is God, the Son is God, the Spirit is God" is uncited. Fix with the `ijc.term.tomus` wording (R5). |
| f1-i-probe-01 | FAIL | P1 | engine cut; wrong record offered | Seven sentences removed, the whole Nicene answer among them. What ships is an inner-life limit for a question about God's nature. The creed is misquoted as "maker of heaven and earth" (325 reads "of all things visible and invisible"). Engine E1. Coverage F1-I to dw.jesus, term.homoousios, quote.nicene-creed and gravity.precision-seeking (R1). |
| f1-e-probe-01 | FAIL | P1 (readability gate) | engine (readability); engine cut (residue) | FK 10.6, FRE 51.9, 296 words. After the cut, "When the assembly was asked" and "that same council" name no council. E5, E1. |
| f1-p-probe-01 | FAIL | P1 | right record not offered | Misleading: it says the record has no one's struggle, then offers a massacre. `ijc.dw.room-for-hesitation` says "There is documented room for hesitation" (Eusebius's letter home from Nicaea) and was not offered. Coverage F1-P and `retrieve_when` on room-for-hesitation (R1). |
| f1-t-probe-01 | FAIL | P1 | caution wording; wrong record offered | "the full Augustinian machinery your later ages built" puts Augustine after the window. He wrote on original sin inside it (to 430). `ijc.limit.later-questions` was offered and dw.original-sin-transmitted was not. Add a not_for to dw.original-sin-transmitted (R3), widen caution 6 (C2) and fix coverage (R1). |
| f2-i-probe-01 | PASS | P2 | - | Faithful to `ijc.dw.how-we-read`. P2: "We did not read it to find ourselves in it" leans on that record's not_for (devotional reading absent rather than thinly recorded). Coined closer. An 8-sentence paragraph. |
| f2-e-probe-01 | FAIL | P1 | caution wording; engine cut | Misleading: "Nearly every voice we cite is Rome's" and "one see's loudest voice and the councils it dominated". This picks Rome against the three-strands rule, and Canon 28 passed over Rome's objection. Build talk: "evidence for the gravity itself", "the 'we' itself, the voice's own premise". The headings were stripped and left fragments. FRE 57.6, 496 words. Caution on self-reference (C3), build-word check (E3), E1, E5. |
| f2-p-probe-01 | PASS | P2 | repetition | Answers what the reader is missing (the creed frame). The quote fits its `modern_lens_note`. P2: the first paragraph repeats f2-i nearly word for word; closer "We read for standing."; a 9-sentence paragraph. E6. |
| f2-t-probe-01 | FAIL | P1 | engine cut; quote lead-in wrong | Damaged: after the Peter sentence was cut, "It was more than a blessing. That claim was real" points at nothing. Wrong: "when Leo sent his letter - his Tome - to Chalcedon". The quote is from the 449 Tome to Flavian. E1. Add the addressee and date to the-rudiments-of-the-creed's use_note and not_for (R5). |
| f3-i-probe-01 | FAIL | P1 | engine cut | Misleading: the Thessalonica sentence was cut, so "The emperor did public penance" now follows the 386 basilica. It is also stated flat, against `ijc.story.emperor-penance`, which keeps the later scene with Sozomen and Theodoret. 592 words, nine paragraphs, a 10-sentence Ammianus quote. E1, and a length ceiling (E5). |
| f3-e-probe-01 | PASS | P2 | - | Correct that the window opens after the persecutions. P2: "office-holders hiding what ordinary believers actually lived" turns the record's silence into intent. "That belongs to the age of persecution" half-endorses the hiding image for an age this world cannot speak to. |
| f3-p-probe-01 | PASS | P2 | - | Callinicum, faithful to the story record, uncorroborated and with no Jewish voice, as its absent_detail says. P2: "The tool he used" is unclear after the cut; a 10-sentence paragraph. |
| f3-t-probe-01 | FAIL | P1 | caution wording; missing record | Horizon: "The East-West schism came six centuries after that. The Reformation came a thousand years later", plus a view of present-day churches and "which books they added to or subtracted". Rewrite caution 7 as a general post-451 rule (C1). Author an F3-T honest limit (R2). Engine horizon check (E2). |
| f4-i-probe-01 | PASS | P2 | repetition | The threshold from `ijc.dw.baptism-threshold`, with an honest limit on the catechumenate. P2: the record recited nearly whole (as in f4-t and f5-p); paragraphs of 8, 5 and 6 sentences. |
| f4-e-probe-01 | FAIL | P1 | engine cut | Wrong after the cut: "Nicaea itself legislates by it ... That is Rome claiming a practice". The Rome line belonged to the removed Julius quote. Damaged: Augustine "dates a new practice" that is never named. E1. |
| f4-p-probe-01 | PASS | P2 | - | A faithful `ijc.limit.inner-life` answer: the vigil, nothing invented. P2: an 8-sentence block. |
| f4-t-probe-01 | PASS | P2 | repetition | Accurate to `ijc.dw.baptism-threshold`. P2: that record's text shipped almost word for word. |
| f5-i-probe-01 | PASS | P2 | repetition | The limit, then giving and the eucharist, all from records. P2: recites `ijc.limit.f5-ordinary-day` whole; the closer restates it. |
| f5-e-probe-01 | FAIL | P1 | missing record; voice not told what is unknown | Invented: "columns and vaults, floors laid in mosaic, and walls that stood high enough to hold a siege", wooden furnishings and hangings, hymns surviving "in manuscripts". Present-day: "some of it still stands", inscriptions "some have". The quote sits next to its not_for (P2). Author an F5-E honest limit (R2). Hold uncited specifics (E4). |
| f5-p-probe-01 | PASS | P2 | engine cut (residue); focus | P2: after the cut, "That day, he says" has no day and no named Leo. Half the answer recites deferred baptism, which is not something given up. E1. |
| f5-t-probe-01 | PASS | P2 | - | Faithful to `ijc.dw.marriage-ranked` and the marriage limit. P2: "where our teachers ranked marriage" appears twice in the last two paragraphs. |
| f6-i-probe-01 | FAIL | P1 | record wording; voice not told what is unknown | Horizon: "hardened into durable division ... the aftermath showed it was not". Misleading: "That unsettled us ... coming apart in our hands", where `ijc.force.chalcedon-failed-consensus` says the community's own reading "is not recoverable". FK 10.4, FRE 51.7. Rewrite that force's description (R4). E5. |
| f6-e-probe-01 | PASS | P2 | focus | `ijc.limit.earlier-windows` verbatim and correct. P2: it opens on martyrdom-seeking, which was not asked; an 8-sentence block. |
| f6-p-probe-01 | FAIL | P1 | record wording (demonstration) | "I am a representative of Imperial and Juridical Christianity - a composite voice of Church and Empire across the window". This is the self-description the prompt excludes, in "I" and in build words. It comes from `ijc.demo.someone-like-me`'s own opening. Limit later-questions was offered. Rewrite the demo (R6), output check (E3), coverage (R1). |
| f6-t-probe-01 | FAIL | P1 | missing record; caution wording; wrong record offered | Misleading: "we have no treatise, no settled teaching handed down, on the eternal fate of the unbaptized" makes the record's silence into the world's. Wrong: "intolerable that any Christian answer for burning a synagogue". The record says intolerable that a bishop fund a synagogue, and worse that anyone answer for the Valentinian house. An 18-sentence paragraph. Author an F6-T limit (R2), C2, R1. |

## Findings

### P1

**E1. Post-draft removal ships damaged or false answers (engine).**
- Where: f1-i, f2-t, f3-i, f4-e (P1). Residue in c-i, c-t, f1-e, f2-e, f5-p (P2).
- Most removals take a sentence that restates a quote record's words without placing it (the Nicene creed in c-i, c-t and f1-i; Julius in f4-e), or a quote lead-in the placer has already used.
- f4-e shows the worst case. The cut moved "That is Rome claiming..." onto Nicaea's canon, so the shipped answer says something false that no draft said.
- f3-i is the same. "The emperor did public penance" now belongs to 386.
- Fix (engine, same item as lpc E1): when a removal takes out an answer-bearing sentence, or the sentence a later deictic ("That", "he", "that same council") points to, redraft or hold. Do not ship the rest. The "quote words without placing" rule should not fire on a doctrinal witness's own paraphrase of a creed.

**H1. After-window knowledge (caution, record, engine).**
- f3-t names the schism, the Reformation and present-day churches.
- f6-i ships "hardened into durable division". That wording is in `ijc.force.chalcedon-failed-consensus`'s own description.
- f5-e says buildings and inscriptions still stand.
- Fixes:
  - **C1, caution 7.** Today it lists post-451 events "beyond this world's own horizon". Rewrite it as the general rule the lpc ruling uses: the voice knows nothing after 451, and names no later event, division, church or survival.
  - **R4, record.** End the force's description at what 451 shows: resistance at the council itself, and the window closing as the fracture opens. Move "hardens into durable division" out of voice-facing text.
  - **E2, engine.** The horizon check (`window_end` in `apply_net`) passed "six centuries after that" and "a thousand years later". It should catch relative dates and named later events, and block them, not log them.

**S1. Record silence told as world silence (caution and records).**
- f1-t: "the full Augustinian machinery your later ages built". f6-t: "no settled teaching handed down" on the unbaptized.
- Caution 6 already says the narrow citation scope "does not reflect this window's own boundaries". The voice does not carry that distinction into its answers.
- Fixes:
  - **C2.** Add to caution 6: "where our record does not draw on a writer of our years, say our record does not carry it; never place that writer's teaching in a later age or say our age had none."
  - **R3.** Add to `ijc.dw.original-sin-transmitted` the not_for "a claim that Augustine's teaching on inherited guilt is later than this window".
  - **R2.** Author an F6-T honest limit in that narrow form.

**R1. Retrieval offers the wrong record (coverage).**
- F1-P is not offered `ijc.dw.room-for-hesitation`, its own record.
- F1-T, F6-P and F6-T are offered `ijc.limit.later-questions` (faith against works).
- F1-I is offered women's authority, Ammianus and Callinicum for "the character of God".
- C-E and F1-T are not offered their own witnesses. The voice found those only because the full prompt carries them.
- Fix (coverage and retrieve_when): point each cell's coverage at the witness written for it, and narrow later-questions' `retrieve_when` to faith-against-works wording.

**V1. Self-reference and build talk (record, caution, engine).**
- f6-p opens with the excluded self-description, word for word from `ijc.demo.someone-like-me` ("I am a representative of Church and Empire").
- f2-e talks about "the gravity itself" and "the voice's own premise", and argues about its own "we".
- Fixes:
  - **R6.** Rewrite the demo's opening in the we-voice, without the role label.
  - **C3.** Add a world_core caution like lpc caution 15: never explain or defend the "we", and never speak of the voice, the window as a build term, or gravities.
  - **E3.** An output check for "I am a representative", "composite voice", "the gravity" and "the voice's own".

**M1. Missing records.**
- F3-T has no record for present-day continuity.
- F5-E has no record for physical remains. The voice invented the architecture: columns, vaults, mosaic floors, hangings.
- F6-T has no record for the fate of those outside.
- Fix (R2): author three honest limits written inside the horizon. F5-E can use what the record holds: Damasus's verse cut in stone, from `ijc.force.transmission-archival` and Jerome. It should say plainly that the record is texts, not a dig.

**A0. Readability hard-fails not gated (engine).**
- c-e (FRE 57.2), f1-e (FK 10.6 / FRE 51.9), f2-e (FRE 57.6) and f6-i (FK 10.4 / FRE 51.7) fail the per-turn gate.
- The admission run's checks do not include it, so all four count as "passed".
- Fix (E5): run `engine/m7/turn_readability.py` inside the admission harness and count its failures. Add a length ceiling: f3-i is 592 words and f2-e is 496.

### P2

- **A1. Paragraph length.** 15 of 28 answers have a paragraph of 8 or more sentences. The worst are f6-t (18), c-i and f1-p (11), and f3-p, f4-e and f5-p (10). Fix: a paragraph rule in the voice prompt, and a paragraph measure in the turn gate (same as lpc A1).
- **E6. Repetition.** Records shipped nearly verbatim across answers:
  - how-we-read in f2-i, f2-p and f2-t.
  - baptism-threshold in f4-i, f4-t and f5-p.
  - Callinicum in f3-i, f3-p, f6-i and f6-t.
  - Fix: let the voice draw on a record's meaning rather than copying its text whole, and narrow Callinicum's `retrieve_when` so it is not offered for authority, fate-of-outsiders and "unsettled you" questions.
- **E4. Citations and uncited specifics.**
  - c-i cites bread-made-body for dw.jesus's words.
  - f6-p cites ancient-custom for the worked line, which no record holds.
  - Uncited specifics shipped in c-t ("real blood") and f5-e (the invented architecture).
  - Fix: hold a sentence with a specific claim and no grounding tag for a grounded redraft (same as lpc E3).
- **R5. The Tome's addressee.** "Leo's letter to Chalcedon" (c-t, f2-t). Fix: `ijc.term.tomus` and `ijc.quote.the-rudiments-of-the-creed` should say "written in 449 to Flavian of Constantinople, read at Chalcedon in 451".
- **Q-context.** f5-e sets Jerome's notice as evidence for the tomb inscriptions, right against its not_for ("a claim that this notice itself describes the verse inscriptions"). It is a P2 here because the voice states the inscriptions from another record first.
- **Craft.**
  - Coined closers: "We read for standing." (f2-p), "We read it to know what we could not yield." (f2-i).
  - Wordplay on "concealment" (f3-e).
  - f2-e reads as a numbered self-assessment, not the world's voice.

## Quote-context check

| Probe | Quote | Matches rendering | Used in its source's context |
|---|---|---|---|
| c-p | leo-sinner-be-glad | yes | yes: Christmas invitation to one not yet certain |
| f2-p | the-rudiments-of-the-creed | yes | yes: the creed as the frame for reading |
| f2-t | the-rudiments-of-the-creed | yes | partly: the lead-in sends the Tome "to Chalcedon" (P1 with the cut damage) |
| f3-i | ammianus-roman-luxury | yes | yes: labelled as a pagan outsider's verdict on 366 |
| f5-e | a-fine-talent-for-making-verses | yes | borderline: set as evidence for inscriptions, against its not_for (P2) |

No quote was invented or altered. No P1 is a misused quote on its own.

## Top failure causes

1. Engine post-draft removal: 4 P1 rows (f1-i, f2-t, f3-i, f4-e) and residue in 5 more.
2. After-window knowledge, through caution 7's wording, one force record's text and a weak horizon check: f3-t, f6-i, f5-e.
3. The record's silence told as the world's silence, which caution 6 does not reach in practice: f1-t, f6-t, and f2-e in part.
4. Retrieval offering the wrong record or missing the right one: f1-p, f1-i, f1-t, f6-p, f6-t, c-e.
5. Readability hard-fails the harness does not gate: c-e, f1-e, f2-e, f6-i.
6. Self-reference and build talk from a demonstration record and a missing caution: f6-p, f2-e.
7. Missing honest limits for F3-T, F5-E and F6-T.

PASS 14, FAIL 14, NOT SCORED 0 of 28
