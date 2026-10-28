# alx fleet graded run 1 (28 October): answer review

## Verdict

**Revise.**

Theon mostly holds. Most answers are plain, serious and in the world's own images: the physician, the school, the water and the table. The voice names the record's gaps without being asked. It never says anything after 400. All nine placed quotations match their records word for word, and none is used against what its source meant.

The automatic checks passed all 28 answers. This review fails 7. Three causes account for most of the gap:

- **The voice fills gaps with invented detail.** Three answers make up facts that no record holds: Origen writing on new birth in John's gospel (f4-t), a teacher's working day (f5-i), and pagan guilds and processions given up at baptism (f5-p). These are the cells with no witness record behind them.
- **Engine cuts leave damage.** In 17 of 28 answers the shipped text is missing sentences from the draft. Eleven are left with an orphan: a sentence that points back to something that is no longer there. The transcript keeps no note of what was cut, or why.
- **Voice against its cautions.** f2-e speaks as the build, not the world ("That is honest service to the participant"). c-e states the contested Clement-to-Origen teaching line as plain fact, against caution 3.

Two turns also fall below the project's hard reading floor (FRE 60), and the harness did not run that gate.

## Counts

| | PASS | FAIL | Not scored |
|---|---|---|---|
| Single-turn probes (28) | 21 | 7 | 0 |

- PASS rows carry P2 defects only, except f3-t, which is clean. 20 rows are P2-only. 7 rows carry a P1.
- Not scored: none. The battery has no safety probe, and every probe got a voice answer.
- Invented fact: 3 rows (f4-t, f5-i, f5-p). Horizon: 0 rows. Quote used out of context at P1: 0 rows.
- Harness result for comparison: 28 of 28 passed `source_boundedness` and `register_coined_aphorism_heuristic` (one advisory on f2-e). Neither check reads invented detail, cut residue, cautions or reading level.

## Scope and checks

- **Run.** Fleet graded run 1, approved by Mark 2026-10-28, cap $8.59, spent $0.62 for this world. Voice: Sonnet 4.5. No safety call, no reader call, no self-revision. Package `packages/alx/2026-10-28T03-49-20Z`, manifest hash `de580ce5...`, which is the current registry pin.
- **Read in full.** All 28 probe questions (`canon/sealed_probes/plaintext/`), each `raw_text` (the draft with tags), each shipped `answer_text`, the citations and the automatic checks. The shipped text is graded, because it is what a participant reads.
- **Cuts.** The draft and shipped text were compared sentence by sentence by script. 17 answers lost at least one sentence. Markdown headings were also stripped (f1-i, f1-t, f2-e); f1-t lost only its heading.
- **Quotes.** All 9 quotations placed in the shipped text match their records' `modern_rendering` exactly, checked by script against `quotes.json`. Each placed quote's lead-in was read against its `use_note.not_for`.
- **Records.** About 120 claims were checked against `prompt.txt`, `repository.json` and `quotes.json`, the world_core cautions 1-5, the four honest limits, and the not_for lists of every cited term, witness, gravity, force, story and quote.
- **Readability.** `engine.m7.turn_readability.report_turns` on all 28 shipped answers: 28 scored, 2 failed (f2-t FRE 57.3, f3-i FRE 57.7). Sentence and paragraph counts are by script, with placed quotations left out of sentence length.
- **Truncation.** Two methods: every `stop_reason` is `end_turn`, and every draft ends on closing punctuation. No truncation.
- **Limits of the evidence.** The m3 harness saves neither the per-turn ground offered to the voice nor a log of what was cut. So for "right record not offered" this review can say only that the record exists and the answer did not use it.
- No model was called. No git command was run. Only this file and its `.counts.json` were written.

## Readability per answer

FK and FRE are for the whole shipped answer. "Longest" is the longest sentence in the voice's own words. "Paragraphs over 4" lists the sentence count of each paragraph over four sentences.

| Probe | Words | FK | FRE | Longest | Sentences over 25 | Paragraphs | Paragraphs over 4 |
|---|---|---|---|---|---|---|---|
| c-i | 252 | 6.8 | 77.2 | 29 | 3 | 3 | 6, 5 |
| c-e | 269 | 8.2 | 66.0 | 40 | 2 | 5 | 5 |
| c-p | 193 | 5.6 | 80.6 | 26 | 1 | 3 | 5 |
| c-t | 281 | 7.8 | 70.3 | 30 | 1 | 5 | 5 |
| f1-i | 199 | 5.3 | 79.9 | 22 | 0 | 4 | 5 |
| f1-e | 208 | 7.1 | 61.0 | 29 | 1 | 3 | 12, 6 |
| f1-p | 276 | 5.8 | 74.9 | 31 | 1 | 4 | 5, 7, 6 |
| f1-t | 278 | 8.6 | 64.0 | 29 | 2 | 3 | 7, 5 |
| f2-i | 310 | 6.8 | 67.9 | 24 | 0 | 6 | 5, 5 |
| f2-e | 844 | 7.5 | 67.4 | 36 | 7 | 11 | 8, 6, 6, 8, 7, 7 |
| f2-p | 380 | 5.5 | 77.7 | 32 | 1 | 6 | 5, 6, 6, 5 |
| f2-t | 206 | 9.5 | **57.3** | 41 | 3 | 4 | none |
| f3-i | 266 | 8.5 | **57.7** | 37 | 1 | 5 | 6, 6 |
| f3-e | 131 | 5.7 | 68.0 | 21 | 0 | 4 | 6, 5 |
| f3-p | 187 | 6.1 | 69.9 | 22 | 0 | 4 | 7, 5 |
| f3-t | 219 | 7.2 | 71.5 | 27 | 1 | 5 | 5 |
| f4-i | 438 | 5.6 | 77.9 | 29 | 2 | 7 | 6, 5, 5, 5, 6 |
| f4-e | 184 | 7.6 | 63.5 | 24 | 0 | 3 | 6, 5 |
| f4-p | 250 | 6.2 | 76.4 | 34 | 2 | 4 | 5, 5 |
| f4-t | 229 | 8.5 | 70.5 | 40 | 4 | 3 | 5 |
| f5-i | 329 | 5.9 | 77.7 | 24 | 0 | 5 | 6, 6, 6 |
| f5-e | 216 | 6.5 | 75.5 | 28 | 1 | 3 | 5, 5 |
| f5-p | 389 | 6.7 | 76.7 | 27 | 3 | 4 | 10, 6 |
| f5-t | 187 | 9.8 | 65.7 | 44 | 4 | 2 | none |
| f6-i | 233 | 7.6 | 67.8 | 35 | 1 | 4 | 5 |
| f6-e | 248 | 7.9 | 66.0 | 32 | 2 | 4 | 7, 7 |
| f6-p | 288 | 5.6 | 80.2 | 33 | 3 | 5 | 6, 5 |
| f6-t | 373 | 7.4 | 70.6 | 32 | 2 | 4 | 7 |

(The probe ids above drop the `-probe-01` suffix.)

**What the numbers say.** 26 of 28 turns clear the reading targets. The two that fail (f2-t, f3-i) do so on long lead-ins and one 37-41-word sentence each. Thirteen answers have a sentence of the voice's own over 30 words. The worst are f5-t (44), f2-t (41), c-e (40) and f4-t (40). 22 turns sit below the FK 8 floor, which is reported only and never fails.

**What they miss.**

- **Paragraph length.** 26 of 28 answers have a paragraph over four sentences. f1-e (12), f5-p (10) and f2-e (8, 8) are walls of text for a reader on a phone.
- **Length.** f2-e runs to 844 words. f4-i (438) and f5-p (389) are also long for one turn.
- **Terms used before they are explained.** "subordinationist" (c-t), "ecology" and "social strata" (f2-e), "Stromateis" (f2-e, f5-t) and "Paedagogus" (f4-i, named but glossed). Elsewhere the voice introduces terms well: "pistis, the soul's first real move toward God", "the oikonomia".

## Craft assessment

The voice has a real character. It is warm without being sweet. It uses concrete images, and it says the hard thing plainly ("At our worst, we did what churches with power do"). Its weaknesses are mechanical: orphans left by engine cuts, demonstration text lifted near word for word, the same record sentences coming back across answers, and long, nested lead-ins to quotes.

**Best writing.**

1. f5-e: "Those are acts, not architecture... What was handed down to us were the lives and the books, not the floor plans." A plain, honest limit that turns straight to what the record does hold.
2. f3-t: "We speak from before the splits that made today's map, and we cannot say." Brief, in idiom, and true to its record.
3. f6-i: "When those two pulled against each other, the structure itself did not tell us which one ought to win." The teacher-bishop tension, held without a verdict.
4. f1-e: "Our best picture of deciding well is Dionysius at Arsinoe... Our harder picture is the same power with an empire behind it." Short sentences that carry a real contrast.

**Worst writing.**

1. f2-e: "That is honest service to the participant, but it walks close to speaking about a view..." and "We should flag that gap more consistently." This is the build's own audit voice, read aloud to a participant.
2. c-p: a paragraph that opens "It was love for the Holy Word, and for the man who taught him. We cannot make it happen for you either." There is no "it" and no "him": the engine cut the Gregory sentence they point to.
3. f2-i: the answer opens on "That is the center. Everything else follows from it." The sentence that said what the center is was cut.
4. f5-p: "The first ask is what people gave up to belong." Stiff, and it echoes the question back.

**Repetition and lifted text (P2).**

- c-p is `alx.demo.want-to-believe` nearly word for word. f6-t follows `alx.demo.going-to-hell` sentence by sentence. f6-p closes on `alx.demo.someone-like-me`.
- "We refused the two easy exits... At our worst, we did what churches with power do. That, too, is in our record." appears in f3-p, f6-i and f6-e.
- The Clement "Sicilian bee" quote is placed three times (c-e, f2-i, f2-t). "made man that we might be made God" appears in c-i, c-t and f1-t.
- Gregory's "love was kindled" appears in c-p, f1-p, f4-p, f5-i, f5-p and f6-p.
- The last paragraph of c-t and the middle of f1-i are the same four sentences from `alx.dw.god`.

**AI tells.** No hedging filler and no disclaimers. The remaining tells:

- **Coined closers.** "The confusion is the door." (f2-p). "A fountain is not studied. It is drunk from." (f2-p).
- **Assistant-style offers.** "If there is a particular record you are asking about, name it, and we will tell you..." (f6-e).
- **Refusal framing.** "Your question places me where I cannot stand." (f6-p).

## Quote-context check

Every quote placed in the shipped text, read against its source's meaning and its not_for:

| Quote | Where | In context? | Note |
|---|---|---|---|
| alx.quote.clement-bee | c-e | yes | Teaching passed teacher to student. Pantaenus is credited to "a later historian", as the not_for requires. |
| alx.quote.clement-bee | f2-i | stretched (P2) | A praise-epithet for a teacher's wide reading, used as an image of how Scripture forms the reader. The source does not say that. |
| alx.quote.clement-bee | f2-t | yes | A teacher's authority resting on visible wisdom. |
| alx.quote.athanasius-made-god | c-t | yes | Why it mattered that Jesus was God: its own retrieve_when. |
| alx.quote.gregory-spark | f1-p | partly (P2) | "One of our students, Gregory" places at Alexandria a pupil Origen taught at Caesarea. The not_for bars "evidence for the school at Alexandria". |
| alx.quote.clement-instructor | f1-t | yes | The Word as healer of the soul's disorder, under the "doctor's imagery". |
| alx.quote.clement-schoolmaster | f2-e | yes | Cited as a checkable claim. |
| alx.quote.origen-scripture-senses | f2-p | yes | Levels of Scripture, the plain sense kept. |
| alx.quote.athanasius-death-trampled-down | f6-t | source kept; off focus (P2) | The lead-in matches its use_note. But the question is about the fate of outsiders, and the quote is about the resurrection. |

Quotes the voice drafted but the engine cut (no context failure shipped): ecclesiastical-and-apostolical-tradition (c-e, f1-e, f2-t, f4-e), gregory-spark in the voice's own wording (c-p, f4-p, f6-p), dionysius-too-high-for-me-to-grasp (f2-e), athanasius-fountains (f2-p), dionysius-nepos (f3-i), dionysius-plague (f3-e, f5-i), timothy-ordinary-questions (f5-i), couches-and-trenchers-and-bowls (f5-e), clement-possessions (f5-p), origen-punishment-heals (f1-i), clement-instructor (f4-i). In f5-e the draft framed the couches quote correctly ("a word to the wealthy... not a description of where the community met"), as its not_for asks.

The recurring Gregory problem starts in a record. `alx.demo.want-to-believe` itself says "One of our students, Gregory", with no mention of Caesarea. The voice copies that framing into six answers.

## Findings

P1 is blocking: wrong, invented, misleading or damaged. P2 is small and plainly fixable. Each fix is at the source: a record, a caution or an engine item. None is a patch to one answer.

### P1

**I1. f4-t: an invented attribution (missing record).**
- Text: "Our teacher Origen, writing on John's gospel, spoke of being born again from above through water and Spirit." No record holds this. `alx.term.photismos` gives new birth to Clement ("Clement named the washing by its light: baptism as new birth and new sight"). Also not in any record: "the Paschal night... we called it illumination".
- Fails against: Rigor; source fidelity.
- Fix (record): in `alx.term.photismos`, name Clement's own locus for new birth in the translational sense. Add the not_for "attributing new-birth language to Origen's Commentary on John". If the build wants Pascha as the baptismal night, author it from a vendored source; if not, add an absent_detail.
- Fix (engine): an uncited sentence that names an author and a work should be held for a grounded redraft, not shipped.

**I2. f5-i: an invented working day, and a false limit (missing record; right record not offered).**
- Text: "The teacher rose early... The day was spent in the text - reading it aloud, questioning it, turning it over." No record gives a teacher's day. `alx.story.gregory-formation`'s absent_detail says Gregory gives no daily logistics. The answer then says "we will not invent a typical day".
- It also says "What we cannot give you is... the daybreak and the meal". But the world's own thinness note says the record is "strong on teaching for daily life in the city, through the Paedagogus, books II and III". So the voice calls unknown what the record holds, and invents what it does not.
- Gregory, taught at Caesarea, is given as an Alexandrian day (against the story's not_for). The plague sentence was cut, leaving "That tells you something true about their days... love made visible" with nothing to point to.
- Fails against: Rigor; Focus.
- Fix (record): author an F5-I witness from Paedagogus II-III (meals, sleep, dress, the household's order), with a not_for on the teacher's and catechumen's routine. Add an absent_detail for the school's daily timetable.

**I3. f5-p: invented social detail under real citations (missing record).**
- Text: "you gave up what the old worship had woven through everything: the guilds, the processions, some of the meals, and some of the friends [[alx.gravity.soul-transformation]]". No record mentions guilds or processions. "you could not belong to us and still belong to the old gods" is cited to `alx.force.apostolic-tradition`, which does not say it. "The strict party said they had given up too little when it was easy" invents a reason that `alx.dw.church-failure` does not give.
- Fails against: Rigor; source fidelity.
- Fix (record): F5-P has no witness record. Author one: Clement's Paedagogus on what a believer gave up (banquets, shows, luxury) and `alx.story.leonides-martyrdom` (its retrieve_when is "the cost of belonging"), with an absent_detail for what ordinary believers gave up.
- Fix (engine): a citation should attach only where the sentence shares content with the cited record's text (same as lpc E3/register-4).

**C1. c-e: a contested succession stated as fact (caution wording).**
- Text: "Clement learned from him, and from others before him... Origen learned from Clement. The line ran teacher to student". `alx.force.transmission-ongoing` says this line "rests almost entirely on Eusebius, and it is contested". Caution 3 asks for lower confidence on succession claims that rest on Eusebius alone.
- Fails against: never present a disputed claim as settled.
- Fix (caution): caution 3 names "church institutions or succession" in general. Make it concrete: "the Pantaenus-Clement-Origen teacher line is remembered through Eusebius; say 'we remember' or 'Eusebius tells', never state it as plain fact". Add the same not_for to `alx.term.didaskalos`, which c-e cited.

**V1. f2-e: the build's voice, not the world's (caution wording; engine cut).**
- Text: "That is honest service to the participant, but it walks close to speaking about a view rather than from inside one we actually held." "we should say so more often than we do". "We should flag that gap more consistently." "did the whole ecology, across all its social strata, hold these convictions". The voice talks about the participant, about its own past answers, and about how it should behave. That is the build's audit language. It does not belong to a witness of the world.
- The vocabulary comes from world_core caution 1 ("Stratum bias", "the whole ecology") and the gravity texts, which the voice reads.
- Engine cuts left "The texts are real." and "That is true at the sacramental level." with nothing before them.
- Fails against: voice-itself; Accessibility (844 words, two paragraphs of 8 sentences, "ecology", "social strata").
- Fix (caution): rewrite caution 1 in words the voice can say: "Everything that survives was written by people who could read Greek. When we say 'we', we mean them first. Whether the villages held the same, we cannot show." Keep "ecology" and "stratum" out of text the voice reads.
- Fix (engine): an output check for build terms in voice turns ("the participant", "ecology", "strata", "flag", "gravity"), alongside `gate_no_build_attribution`.

**A1. f2-t and f3-i: below the reading floor (engine).**
- f2-t: FRE 57.3. Its worst sentence is 41 words: the lead-in to the bee quote plus the quote's clauses.
- f3-i: FRE 57.7. Its worst sentence is 37 words ("He traveled to the villages, sat down with the presbyters, the teachers, and any of the brethren who wished to come, and argued it through for three days...").
- Fails against: the NorthStar per-turn hard fail (FRE 60).
- In f2-t the engine also cut the Origen sentence, which was the answer's main evidence that Scripture stood inside the rule of faith. In f3-i it cut the Nepos quote, leaving "loved the man" with no man named.
- Fix (engine): the m3 admission harness should run `engine.m7.turn_readability` on each shipped answer and fail the probe on a hard fail. Today `overall_pass` is true with two turns under the floor.

### P2

- **E1. Cut residue (engine).** Orphans left by removed sentences: c-p ("It was love for the Holy Word..."), f1-e ("That rule set the bounds"), f2-i (opens "That is the center."), f2-e, f2-p ("A fountain is not studied"), f3-e ("That was courage in the open"), f3-i ("loved the man"), f4-p ("Gregory, left an account of how his own teacher met him." and then nothing), f5-e ("But that is a word to the wealthy"), f5-i, f6-p ("The kindling was not forced"). Fix: when a removal takes out the sentence a later sentence depends on, redraft or remove the dependant too (the same as lpc E1). The harness should also save what it removed and why.
- **E2. Draft quotes in the voice's own wording (engine and prompt).** In nine answers the voice wrote its own version of a quote in single quotation marks next to the tag, and the whole sentence was dropped. In several answers it was the strongest evidence. Fix: tell the voice to place the tag alone and never retype quote words. The demonstrations teach the opposite: `alx.demo.want-to-believe` and `alx.demo.going-to-hell` carry inline quotes in their own wording. Rewrite them to place the quote record.
- **R1. Gregory relocated to Alexandria (record).** c-p, f1-p, f4-p, f5-i, f5-p and f6-p. Fix: in `alx.demo.want-to-believe` change "One of our students, Gregory" to words that keep Caesarea, for example "Gregory, who studied under Origen after he left us for Caesarea". Do the same in any other text that calls him "ours".
- **W1. Weak citations (engine).** `alx.limit.faith-alone-later-frame` is cited for guilt at birth (f1-t) and for apokatastasis (f6-t). Neither is in it. `alx.dw.original-sin` is cited for "God is not mocked" (f6-t), which is from a demonstration. `alx.dw.apostolic` is cited for "wanting to believe... was not failure" (c-p). `alx.term.katechesis` is cited for "built the whole method on questions" (f1-p). `alx.dw.councils` is cited for "the teachers named their line plainly" (c-e). Fix: the same as I3: a citation needs shared content.
- **f4-i (missing record).** "They were accepted as a hearer - someone listening at the edge... That stage could last a long time" and "All through this, their life was watched." No record holds the stages. They are true to Origen, Against Celsus III.51 (private instruction and testing before admission), which is vendored. Fix: author a witness or term record for the catechumenate's stages from Contra Celsum III.51, verified against the vendored ANF text.
- **f5-t (right record not offered).** It says the record does not show "whether a bishop or a presbyter presided". `alx.quote.timothy-ordinary-questions` holds Question XI: a clergyman called to celebrate a marriage and "perform the offering" (380s). Fix: add "how marriage was marked" to that quote's retrieve_when. Also: a 44-word sentence.
- **f3-e (rigor).** "Our meeting places were known." is uncited. It sits against `alx.limit.material-remains`, which says the writings tell of souls and books, not rooms.
- **f6-p (voice).** It answers in "I" ("I cannot answer that. I do not know you.") eight times, against the strict we-voice in "Who we are". It recasts the question as a request for a verdict. "a matter between them and their teacher, not a verdict announced to the room" is uncited.
- **f6-i (rigor).** "not that some gave way under persecution - we expected that" softens what `alx.dw.church-failure` calls a bitter fight.
- **f2-p (caution 1).** "We sat them down with someone who had walked the road ahead" makes the school's teacher the way every reader met Scripture. `alx.gravity.scripture-formative` bars "asserting that it shaped the non-literate rural majority".
- **f1-e and f3-i (record).** `alx.dw.councils` ends "It loved the man, and it honored the truth more." It never names Nepos, so the voice ships "the man" with no one named. Fix: name Nepos in the witness text.
- **c-t (access).** "subordinationist" is used without explanation.
- **c-i (focus).** The last paragraph moves from Jesus to the soul (psyche).
- **f6-e (focus, craft).** After a sound "we do not know of such a record", half the answer repeats f3-p and f6-i on church failure, then closes on an assistant-style offer.
- **Demo lift and repetition (engine).** See Craft. Fix: a check against near-verbatim reuse of demonstration text, so that a demonstration teaches the style and is not recited.

## Part Eight-style summary by cell

| Cells | Result | Basis |
|---|---|---|
| C (Jesus) | 3 of 4 pass | c-e fails on the contested succession (C1). |
| F1 (God, doctrine, doubt, guilt) | 4 of 4 pass | Citation and residue P2s only. |
| F2 (Scripture) | 2 of 4 pass | f2-e voice (V1); f2-t reading floor (A1). |
| F3 (authority, church, failure) | 3 of 4 pass | f3-i reading floor (A1). |
| F4 (joining, ritual, rebirth) | 3 of 4 pass | f4-t invented attribution (I1). |
| F5 (daily life, place, cost, marriage) | 2 of 4 pass | f5-i (I2) and f5-p (I3), both in cells with no witness record. |
| F6 (unsettling, sources, the asker, the outsider) | 4 of 4 pass | P2s on focus, voice and repetition. |

## The 28 answers

Criteria: R = Rigor, A = Accessibility, C = Craft, F = Focus. Each is graded pass, concern (P2) or fail (P1).

| Probe ID | Result | Severity | R / A / C / F | Cause layer | Fix at the source |
|---|---|---|---|---|---|
| c-i-probe-01 | PASS | P2 | pass / pass / pass / concern | none (voice drift) | None needed at record level. P2: the soul paragraph strays from the question. |
| c-e-probe-01 | FAIL | P1 | fail / concern / pass / pass | caution wording | Caution 3: state the Pantaenus-Clement-Origen line as remembered through Eusebius. Add the same not_for to alx.term.didaskalos (C1). Citation fix (W1). |
| c-p-probe-01 | PASS | P2 | concern / pass / concern / pass | engine cut | E1 (the cut leaves "It was love..." orphaned). E2/R1: rewrite alx.demo.want-to-believe to place the quote record and keep Caesarea. |
| c-t-probe-01 | PASS | P2 | pass / concern / pass / pass | none (voice) | P2 access: gloss "subordinationist". |
| f1-i-probe-01 | PASS | P2 | pass / pass / concern / pass | engine cut | E1/E2 (Origen paraphrase cut). Craft: recites alx.dw.god word for word, the same as c-t. |
| f1-e-probe-01 | PASS | P2 | pass / concern / concern / pass | engine cut | E1 ("That rule" orphan). Name Nepos in alx.dw.councils. Paragraph of 12 sentences. |
| f1-p-probe-01 | PASS | P2 | concern / pass / pass / pass | quote used out of context | R1 (Gregory as "one of our students"). W1 (katechesis cited for a dw.doubt claim). |
| f1-t-probe-01 | PASS | P2 | concern / pass / pass / pass | wrong record offered | W1: faith-alone limit cited for guilt at birth. The right record (alx.dw.original-sin) was cited elsewhere in the turn. |
| f2-i-probe-01 | PASS | P2 | pass / pass / concern / pass | engine cut | E1: the opening thesis was cut, leaving "That is the center." The bee quote is stretched to Scripture reading. |
| f2-e-probe-01 | FAIL | P1 | concern / fail / fail / pass | caution wording | V1: rewrite caution 1 in sayable words, keep build terms out of voice-read text, add a build-term output check. E1 residue. |
| f2-p-probe-01 | PASS | P2 | concern / pass / concern / pass | engine cut | E1 ("A fountain" orphan). Caution 1 (the teacher made universal). Coined closer. |
| f2-t-probe-01 | FAIL | P1 | pass / fail / pass / concern | engine (gate not run; cut) | A1: run the per-turn readability gate in the m3 harness. E2: the Origen rule-of-faith quote, the answer's key evidence, was cut. |
| f3-i-probe-01 | FAIL | P1 | pass / fail / concern / pass | engine (gate not run; cut) | A1: per-turn gate in the harness. E1/E2 (Nepos quote cut, "the man" unnamed). |
| f3-e-probe-01 | PASS | P2 | concern / pass / concern / pass | engine cut | E1 ("courage in the open" orphan). "Our meeting places were known" is uncited, against alx.limit.material-remains. |
| f3-p-probe-01 | PASS | P2 | pass / pass / concern / pass | none (repetition) | Craft: recites alx.dw.church-failure. Stock lines recur in f6-i and f6-e (repetition check). |
| f3-t-probe-01 | PASS | none | pass / pass / pass / pass | none | None. |
| f4-i-probe-01 | PASS | P2 | concern / concern / pass / pass | missing record | Author a catechumenate-stages record from Contra Celsum III.51 (the "hearer" stage). 438 words. |
| f4-e-probe-01 | PASS | P2 | pass / pass / concern / pass | engine cut | E2 (Origen quote paraphrase cut). Near-verbatim recital of alx.dw.apostolic. |
| f4-p-probe-01 | PASS | P2 | pass / pass / concern / pass | engine cut | E1: Gregory is announced, then the sentence is cut. R1. |
| f4-t-probe-01 | FAIL | P1 | fail / concern / pass / pass | missing record | I1: in alx.term.photismos, name Clement's locus for new birth. Add the not_for on Origen's Commentary on John. Settle or limit Paschal-night baptism. Engine: hold uncited author-and-work attributions. |
| f5-i-probe-01 | FAIL | P1 | fail / pass / concern / fail | missing record; right record not offered | I2: author an F5-I witness from Paedagogus II-III, and an absent_detail for the school's timetable. R1 (Gregory). E1 residue. |
| f5-e-probe-01 | PASS | P2 | pass / pass / concern / pass | engine cut | E1 ("a word to the wealthy" orphan). The answer holds its limit well. |
| f5-p-probe-01 | FAIL | P1 | fail / concern / concern / pass | missing record | I3: author an F5-P witness (Paedagogus on what was given up; leonides-martyrdom), with an absent_detail. Engine: citations need shared content (W1). R1. |
| f5-t-probe-01 | PASS | P2 | concern / concern / pass / pass | right record not offered | Add "how marriage was marked" to alx.quote.timothy-ordinary-questions' retrieve_when (Question XI). A 44-word sentence. |
| f6-i-probe-01 | PASS | P2 | concern / pass / concern / pass | none (voice) | "we expected that" softens the record. Stock closing lines repeat (repetition check). |
| f6-e-probe-01 | PASS | P2 | pass / pass / concern / concern | none (voice) | Focus filler from church-failure. Assistant-style closing offer. |
| f6-p-probe-01 | PASS | P2 | concern / pass / concern / concern | engine cut | E1 ("The kindling" orphan). The "I" voice against the strict we-voice. Uncited "between them and their teacher". |
| f6-t-probe-01 | PASS | P2 | concern / pass / concern / concern | wrong record offered | W1 (faith-alone limit cited for apokatastasis, which belongs to alx.term.apokatastasis). The resurrection quote is off focus. The answer is lifted from alx.demo.going-to-hell. |

## Top failure causes

1. **Missing record: no witness behind the cell, so the voice invents.** f4-t, f5-i and f5-p (all P1), and f4-i (P2). F2-I/P/T, F3-I, F4-I/P/T, F5-P, F6-I/E/T and C-P have no doctrinal witness. F5-I's only limit covers women's words. Author witnesses or limits for F4-T, F5-I and F5-P first.
2. **Engine cut damage.** 17 answers lost sentences and 11 kept an orphan. Two lost their main evidence (f2-t, f3-i). The harness saves no removal log. The cut itself is right to drop voice-typed quote text. What is missing is the follow-up: redraft or remove what depended on it.
3. **Caution wording.** Caution 1's build vocabulary reaches the voice (f2-e). Caution 3 is too general to stop a contested succession being stated as fact (c-e).
4. **Engine gate not run.** The admission harness passes turns under FRE 60 (f2-t, f3-i). Its two checks cannot see invented detail, residue or cautions, which is why it passed 28 of 28.
5. **Record wording that teaches the wrong habit.** Demonstrations carry inline, self-worded quotes and call Gregory "one of our students". The witness text says "the man" without naming Nepos. Citations attach to records that do not hold the sentence.

PASS 21, FAIL 7, NOT SCORED 0 of 28
