# hal fleet graded run 1 (28 October): answer review

## Verdict

**Revise.**

The automatic checks passed all 28 answers. Read by hand, 11 of them carry a P1 defect. Neither automatic check (source_boundedness, register_coined_aphorism_heuristic) caught any of the 11.

At its best the voice is plain, direct and its own. f3-e, f1-t and f6-t are model answers. Every placed quote matches its record word for word and stands where its source meant it, with one exception (f3-t). The voice says "we cannot tell you" readily and well (f4-i, f5-e, f5-t).

Four causes account for most of the P1s:

- **Engine cut leaves orphans.** Placement drops every quote it does not place. 14 of 28 drafts lost at least one quote sentence (23 quote sentences in all), most of them quotes that were in the turn's own evidence. In f2-p and f5-i the sentences that pointed to the dropped quote shipped anyway, so the answer talks about a "she" or a "that" the reader never meets.
- **Uncited or wrongly cited claims ship.** The voice fills gaps from memory and tags the result to a record that does not hold it. Examples: "the emperor Lateranus" (f1-p), an inverted line from Jerome's Letter 22 (f2-i), and invented reading practices tagged to `hal.dw.apostolic` (f2-p). A stray Chinese character shipped in f1-e.
- **Contested claims stated as settled.** Paula "gave it all away" (f5-p). Marcella's standing is said to hold "without contest" (f3-i). The contested records are not in the prompt, and the turn evidence either leaves them out (f5-p) or ranks them below a gravity record that states the claim flatly (f3-i).
- **No post-420 horizon caution.** Caution 6 guards the pre-382 edge only. f3-t tells how the translation was "received differently in different centuries".

## Counts

| | PASS | FAIL | Not scored |
|---|---|---|---|
| Sealed battery (28 probes) | 17 | 11 | 0 |

- 5 PASS rows are clean. 12 PASS rows carry P2 defects only.
- All 11 FAIL rows carry a P1.
- Invented fact, horizon breach or quote out of context: 5 rows (f1-p, f2-i, f2-p, f3-t, f6-i).
- Not scored: none. The harness calls the voice on every probe, with no safety or reader routing, so every row has a Representative answer to grade.

## Scope and checks

- **Run.** `engine/m3/reports/fleet-graded-run-1/hal.json`. Voice: Sonnet 4.5, one call per probe. No safety, reader or self-revision call. Package `packages/hal/2026-10-28T04-11-39Z`; its manifest hash matches the run's. Run commit `0526144`.
- **Read in full.** All 28 questions (`canon/sealed_probes/plaintext/`), the shipped `answer_text`, the `raw_text` draft, the `citation_entries` and the automatic checks.
- **Records.** All 16 doctrinal witnesses, the 4 honest limits, the 7 contested claims, the 9 demonstrations and the 12 stories, plus the terms the answers lean on, world_core cautions 1-8, and the not_for lists of every placed quote. About 120 claims were checked.
- **Quotes.** All 6 placed quotes match their records' `modern_rendering` exactly (checked by script). The record `text` of all four placed quote records was checked against the vendored NPNF files (`npnf206_jerome-principal-works.xml`, `npnf203_theodoret-jerome-gennadius-rufinus.xml`). The f1-p and f2-i errors were checked against the same files.
- **Offered evidence.** I replayed `engine.m4.evidence.assemble_evidence` offline for each probe to see which records were offered. This is deterministic code, and no model was called. It ran on the current working tree, which may differ from the run commit; I did not run git to compare. Where a cause below says "not offered", it rests on that replay.
- **Readability.** `engine.m1.gates.grade_text` was run on every shipped answer. Sentence and paragraph counts are by script.
- **Not done.** No model was called and no git command was run. No data dated before 27 October was compared; the 13 October eleven-world test is kept for a later side-by-side. Only this file and its `.counts.json` were written.

## Method

The method follows `Build/worlds/lpc/Review-Artifacts/Run3_Access_And_Craft_Review_2026-10-28.md` and the rubric in `Build/worlds/lpc/build/lpc_Probe_Results.md`.

- **Criteria.** Rigor, Accessibility, Craft and Focus are each graded `pass`, `concern` (a P2 defect) or `fail` (a P1 defect).
- **Severity.** P1 means wrong, invented, misleading or damaged. P2 means small and plainly fixable.
- **Result.** A row with a P1 is FAIL. A row with only P2s is PASS.
- **Accessibility concern.** Graded where a reader meets a paragraph of 8 or more sentences, a voice sentence over 30 words, FRE below 60, or a term used before it is explained.
- **Fix.** Each fix is at the source: a record, a caution or an engine item. None is a patch to one answer.
- **Cause layers.**
  - missing record
  - right record not offered
  - wrong record offered
  - voice not told what is unknown
  - caution wording
  - engine cut
  - quote used out of context
  - engine (grounding/output check), for defects that no record or caution could have stopped

## Readability

| | Value |
|---|---|
| FK, all answers | 5.4-10.0 (all at or under 10) |
| FRE below 60 | f1-e 58.8, f2-e 56.5, f3-i 55.3 |
| Answers with a sentence over 25 words | 27 of 28 (the worst: f3-t 74 and 62 words, f1-p 63, f3-p 58) |
| Answers with a paragraph over 4 sentences | 27 of 28 (the worst: f3-p 14, f1-p 13, f6-e 11, f1-e 10) |
| Latin terms | introduced well: renuntiatio, virginitas, epistula and hebraica veritas each get a plain meaning first |
| Terms used before they are explained | "the great council" (c-t, f1-i), "helmeted" and "Apocryphal" (f2-i, f3-t), "Origenist" (f1-e) |

## Results

R = Rigor, A = Accessibility, C = Craft, Fo = Focus.

| # | Probe | Result | Sev. | R | A | C | Fo | Cause layer | Fix at source | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | c-i-probe-01 | PASS | P2 | pass | concern | concern | concern | engine cut; wrong record offered | Engine: no quote-tagged sentence should be drafted unless the quote is placeable (see E1). Records: none. | Who Jesus was. Faithful to `hal.dw.jesus` and `hal.dw.record`. The eyes-of-faith and hail-Bethlehem quotes were cut cleanly. P2 focus: paragraph 2 drifts into the translation project (`dw.record` text recited). P2 access: sentences of 28-29 words. |
| 2 | c-e-probe-01 | PASS | P2 | pass | concern | concern | pass | engine cut | E1 (cut residue); E3 (punctuation splice). | Sources and path. Faithful to `dw.record`, `term.epistula`, `story.translating-a-book`. P2 craft: opener "We will answer this from the ground, beginning with... then... then" is assistant signposting. "renuntiatio - cost dearly.." is a double period, and "cost dearly" now points to nothing: the Blaesilla-funeral quote was cut. |
| 3 | c-p-probe-01 | PASS | - | pass | pass | pass | pass | - | - | Cannot believe. Follows `hal.dw.believe` and `hal.demo.believe` faithfully: the dream, Fabiola, "the door was opened to the divided and the broken". The sackcloth quote was cut without residue. |
| 4 | c-t-probe-01 | PASS | P2 | pass | concern | concern | concern | engine cut; wrong record offered | E1. Record: `hal.dw.was-jesus-god`'s "Personal Lord and Savior" and penal-formula sentences are answers to modern-frame questions; move them to `use_note` or a demo so they are not recited where nobody asked. | Nicene and Trinitarian, as the record holds. P2 craft: "The devotion those words carry" points to the Bridegroom quote and its lead-in, both cut. P2 focus: the last paragraph (hebraica veritas) does not answer a question on divine status, and the Spirit gets one clause. P2 access: "the great council" is never named. |
| 5 | f1-i-probe-01 | FAIL | P1 | fail | pass | concern | concern | missing record | Record: author a doctrinal witness on God's character as this world spoke of it (justice and mercy in Jerome's own words), verified against the vendored letters, or an honest limit if the build finds none. | God's character. P1 misleading: "We held God to be just - severely so... A daughter died young after taking up the ascetic life, and at her funeral the crowd said fasting had killed her. We rebuked grief without limits as unbelief. That is justice as we held it." This presents Blaesilla's death and the crowd's accusation as God's justice. `hal.dw.suffering` gives the community's answers as "judgment on a proud city, reward stored up for the afflicted, the dead safe with Christ", and nothing in it reads Blaesilla's death as judgment. No record speaks to God's character, so the voice built one from the suffering witness. |
| 6 | f1-e-probe-01 | FAIL | P1 | pass | concern | concern | pass | engine (output check); engine cut | Engine: add an output check that holds any non-Latin-script character outside a placed quote (E2). E1 for the residue. | Who settled disputes. Overlapping authorities, no verdict: faithful to `hal.dw.authority`. The Rufinus quote matches and stands in its source's sense (heard he was attacked, wrote to Rome; no summons, no verdict). P1 damaged: "The争 carried on in letters" ships a Chinese character in place of a word. P2: "Jerome answered in his own prefaces" answers critics who were cut (the Oea and Augustine quotes). P2 access: FRE 58.8; a 10-sentence opening paragraph; sentences of 45 and 48 words. |
| 7 | f1-p-probe-01 | FAIL | P1 | fail | concern | concern | pass | engine (grounding/output check) | Engine: a quote's lead-in sentence must be checked against the quote's own text and record. A proper noun, title or date in the lead-in that the quote and its record do not hold should be held (E4). Record: add to `hal.quote.she-put-on-sackcloth` a claim_guard "Lateranus was a senator executed under Nero, not an emperor; the passage gives no feast day". | Room for one who struggles. P1 invented: the lead-in says "on the day before Easter, in the basilica that had once housed the emperor Lateranus". Lateranus was a senator put to death by Nero (NPNF note to Ep. 77.4), and the passage names no feast. The lead-in then retells the quote it introduces ("her disheveled hair, pale face, dirty hands..."). The quote matches and its context is right: restoration after a public fault, as its retrieve_when says. P2 access: a 63-word sentence; a 13-sentence paragraph. |
| 8 | f1-t-probe-01 | PASS | - | pass | pass | pass | pass | - | - | Inherited guilt. "We cannot give you a worked-out answer to how the guilt is passed, because we ourselves did not settle it." This says plainly what is unknown, in the world's own terms, as `hal.dw.sin-grace` holds. The only answer with no paragraph over 4 sentences. |
| 9 | f2-i-probe-01 | FAIL | P1 | fail | concern | concern | pass | missing record; engine (grounding) | Record: if the reading instruction is wanted, author a quote from Ep. 22.17 ("Read often... Let sleep overcome you, the roll still in your hands; when your head falls, let it be on the sacred page"), verified against `npnf206`. Engine: an uncited sentence that reports what a named writer said should be held (E4). E1 for the residue. | Reading sacred texts. P1 misleading: "Our teacher told a virgin to read constantly, and never to let the book fall from her hand or sleep creep over her face." It is uncited, and the source says the opposite of the second half: "Let sleep overcome you, the roll still in your hands". The helmeted-preface quote matches and fits its retrieve_when (which books counted). But the engine cut the sentence that explained it, so "That took nerve" follows an unexplained "helmeted" and "Apocryphal" (P2 access). P2 rigor: "We read scripture as the treasure. That was first. Everything else... stood around that center" ranks scripture above renunciation, against the formation logic ("one discipline. Not two"). The last paragraph recites `dw.record`. |
| 10 | f2-e-probe-01 | PASS | P2 | pass | concern | concern | pass | caution wording; wrong record offered | Caution: rewrite caution 4 for the scholarly cell. Say whether the voice may hold the fluency contest open in its own words when a participant asks about modern scrutiny, or must give only Jerome's own words. Today it says both "never state as settled" and "the modern dispute is for the Facilitator". Record: in `hal.term.monasterium` the not_for "calling it a double monastery" is broken three times this run (f2-e, f3-i, f5-e); add "double monastery" to an output check, or give the term a plain alternative the voice will use. | Modern scrutiny. Honest and well ordered: the skeleton survives, the women's inner lives do not. Marcella, the Paula renunciation, the women's words, the enslaved and material remains all match their records. P2 rigor: "How fluent Jerome actually was in Hebrew is an open question... no surviving evidence settles" is the modern dispute in the Representative's voice, which caution 4 gives to the Facilitator. It is accurate and held open, so P2. "founded a double monastery" breaks `hal.term.monasterium`'s not_for. P2 craft: "Rome and Bethlehem, 382-420." is the build's window read aloud; "A scholar would say" is an outside voice. P2 access: FRE 56.5. |
| 11 | f2-p-probe-01 | FAIL | P1 | fail | concern | fail | pass | engine cut; wrong record offered; engine (grounding) | E1: when a quote is cut, the sentences that refer to it must go with it or the turn must be redrafted. Engine (E4): a citation should attach only when the sentence shares content with the cited record's text. Retrieval: `hal.dw.apostolic` should not lead the evidence for a "scripture is dull" question (narrow its match). | Scripture dull. P1 damaged: "She was not reporting a vision. She was reading the page in the place it happened" refers to Paula, whose quote was cut, so "she" has no antecedent. P1 invented: "We read them aloud, in company... arguing a single word against the Hebrew text for hours... We fasted to quiet the noise in our own heads so we could hear them better" is tagged to `hal.dw.apostolic`, which holds none of it. The fasting purpose is the voice's own: the record has Jerome take up Hebrew because fasting alone did not calm his mind. P2 craft: the closing questions to the participant ("have you let them cost you anything yet?") press the reader; coined closer "The treasure does not shine for the one still standing at a distance." |
| 12 | f2-t-probe-01 | PASS | P2 | concern | concern | pass | pass | right record not offered | Retrieval: offer `hal.dw.authority` (overlapping authorities: scripture, councils, bishops, learned opinion) for "sole source of authority" questions; it was not in the evidence. | Scripture and received faith together, from `hal.dw.apostolic`. P2 rigor: "we said so plainly" and "taught and kept everywhere" are not in the cited record. The world's own answer on authority (`dw.authority`, the patronage authority) goes unused. P2 access: a 32-word sentence. |
| 13 | f3-i-probe-01 | FAIL | P1 | fail | concern | concern | pass | wrong record offered | Record: rewrite `hal.gravity.marcella-authority`'s `description`, which states the contested claim flatly ("A woman recognized, in her own right and her own house..."). Engine: a gravity record is build analysis and should not be offered to the voice as speakable ground, or should carry the contested record's frame with it. | Leadership. The Bethlehem half is sound (`core`, `term.patrocinium`), and the first Marcella hedges are good. P1 misleading: "What we can say without contest is that she argued Jerome's own answers for years before he left Rome, and that her household remained a recognized place for scriptural work." The second half is the contested claim itself (`hal.contested.marcella-agency`, not_for "presenting Marcella's consulted authority as documented fact"), now labelled uncontested. P2: "double monastery" (monasterium not_for); "the copying work" is not in `term.patrocinium`. P2 access: FRE 55.3. |
| 14 | f3-e-probe-01 | PASS | - | pass | pass | pass | pass | - | - | Catacombs. "We were not a persecuted church meeting in secret. We were an established church arguing about whether its own wealth had ruined it." Short, exact and in the world's voice, from `hal.dw.empire` and `hal.limit.martyrdom`. The best answer in the run. |
| 15 | f3-p-probe-01 | PASS | P2 | pass | concern | concern | concern | right record not offered | Retrieval: offer `hal.dw.church-failure` ("Our failures are not hidden in our record") for "how did you respond when you failed someone"; the replay offers it to the catacombs question instead. Engine E4: a lead-in that retells the quote should be cut to a pointer. | Failing someone. The sackcloth quote matches, and it is used as its retrieve_when intends ("a way back after a public failure"). The Rufinus break and the silence of the enslaved are honest and match their records. P2 focus: Fabiola's fault is hers, not the community failing her; the world's own record on its failures goes unused. P2 craft: the 58-word lead-in retells the quote that follows ("her face pale with fasting and neglect" adds to it). P2 access: a 14-sentence paragraph. |
| 16 | f3-t-probe-01 | FAIL | P1 | fail | concern | concern | pass | voice not told what is unknown; quote used out of context | Caution: add a world_core caution for the closing edge: "Nothing after 420. The later name, spread or standing of the translation, and what later churches kept or dropped, are not ours to tell, beyond `hal.dw.one-church`'s 'Many churches now claim parts of what we left'." Record: add to `hal.quote.helmeted-preface` the not_for "a claim about what later centuries did with these books". Engine (E5): the horizon check should read time words ("centuries", "never became", "later") and not only years. | Present-day church. The opening matches `hal.dw.one-church`. P1 horizon: "reached the western church and was received differently in different centuries, though even that text was never quite what we produced; the books Jerome held should be placed among the Apocrypha... remained in the church's use", and "never became the church's consensus". This is uncited history after 420. Quote out of context: the helmeted preface is Jerome's 391 canon list, placed here as evidence for what the church did with those books later. P2 access: sentences of 74 and 62 words. |
| 17 | f4-i-probe-01 | PASS | P2 | pass | concern | concern | pass | caution wording (record text) | Record: rewrite `hal.term.propositum`'s `plain_meaning` as something the voice can say ("the vowed resolve behind a chosen ascetic life"). Move "real period wording, not quoted for these four women" to `senses.evidential`, which the voice does not recite. | How someone joined. A model honest limit: "we cannot give you the steps, because no document gives them to us." The coverage note on the catechumenate is honoured. P2 craft: "propositum, real period wording, though it is not quoted for these women" is the record's build caveat read aloud. P2 access: a 34-word sentence. |
| 18 | f4-e-probe-01 | PASS | P2 | pass | concern | pass | pass | - | Engine: sentence-length guidance (see A1 below). | Rituals and earliest followers. Faithful to `hal.dw.apostolic`: common sacraments received, the ascetic life admitted new. The rose-from-the-thorns quote matches, and its lead-in is used as its source means it: the harsh ranking that even friends resisted, not honour for marriage on its own terms. P2 access: sentences of 37 and 43 words. |
| 19 | f4-p-probe-01 | PASS | P2 | pass | pass | concern | concern | right record not offered | Retrieval: the formation logic's own answer for a restless mind ("Jerome took up Hebrew as a remedy beside fasting, when fasting alone did not calm his mind", `hal.core.hieronymian`) should be offered for this question. | Mind won't settle. Faithful to `hal.dw.inner-life`, and Blaesilla's death is kept rather than hidden, as the record's tension asks. P2 focus: the world's own remedy (Hebrew study when fasting failed) is missing. P2 craft: coined line "The restless head is not silenced by force. It is given something to hold." |
| 20 | f4-t-probe-01 | PASS | - | pass | pass | pass | pass | - | - | Born again. Baptism and the datable turn, from `hal.dw.practices` and `hal.demo.born-again`. Plain and faithful. |
| 21 | f5-i-probe-01 | FAIL | P1 | concern | concern | fail | concern | engine cut | E1 (as f2-p). Record: `hal.story.day-at-monastery`'s own material (three companies, garments, the sick nursed, the stubborn sister) should be what the voice reaches for. Its claim_guard should also bar "began and ended with" phrasing. | A typical day. P1 damaged: "That was one man's days, the ones we can most nearly see" and "That tells you what they prized" point to the always-at-his-books and Paula-Hebrew quotes, both cut, so the answer refers to evidence it never gives. P2 rigor: "The day began and ended with psalms... food enough to sustain the labor but not to comfort" is not in the record and leans on schedule detail the claim_guard bars. P2 craft: "What I have told you" breaks the strict we-voice. The honest limit at the end is good. |
| 22 | f5-e-probe-01 | PASS | P2 | concern | concern | concern | pass | engine cut | E1; E3 (double period). Monasterium wording as f2-e. | Physical evidence. A model honest limit from `hal.limit.f5-material-remains`; "no source names a scriptorium" holds `term.scriptorium` well. P2: "the birthplace itself.." double period; "But no source names a scriptorium" now follows nothing about copying (sentence cut); "a double monastery" (monasterium not_for). P2 access: a 42-word sentence. |
| 23 | f5-p-probe-01 | FAIL | P1 | fail | pass | pass | pass | right record not offered | Retrieval: offer `hal.contested.paula-renunciation-totality` with any turn that offers `hal.story.paula-epitaph` or `hal.term.renuntiatio` (add a relation). Record: add to `hal.story.paula-epitaph` a claim_guard "never state that Paula gave everything away, except as the memorial says". | What people gave up. "Everything, and not everyone" is a strong opening, and the hostel and hospital paragraph is the record's own (`demo.someone-like-me`). P1 misleading: "She gave it all away - her property sold, the money poured toward the poor, the sick, and the scriptures." It states the literal totality as fact, against `hal.contested.paula-renunciation-totality` and `hal.term.renuntiatio`'s not_for ("asserting Paula's self-impoverishment was literally total"). The contested record was not offered and is not in the prompt. |
| 24 | f5-t-probe-01 | PASS | P2 | concern | concern | concern | concern | right record not offered | Retrieval: offer `hal.dw.marriage-ending` (remarriage, one law for both sexes, penance) for "how did you understand marriage". The replay offers `dw.apostolic` instead. | Marriage. The ranking and the controversy are faithful to `term.virginitas`; the honest limit on any rite is good. P2 rigor: "we defended it against those who would have called it sin" and "the gospel that blessed the wedding at Cana" are not in the cited `dw.apostolic`. P2 focus: the middle paragraph recites `dw.apostolic` on the novelty of monasticism. |
| 25 | f6-i-probe-01 | FAIL | P1 | fail | concern | concern | concern | wrong record offered; caution wording | Engine: a term gloss inserted by the term-introduction rule must fit the person it is attached to; `hal.term.virginitas` should not be offered for a Blaesilla sentence. Record: add to `hal.limit.f5-enslaved` the not_for "attributing to the community a concern for the enslaved that its record does not show". Prompt: the "What we keep returning to" line on silences invites the voice to speak as a modern reader of its own record; reword it so the silences are stated, not mourned. | What unsettled you. P1 wrong: "She took up the ascetic life - virginitas, lifelong virginity given to God... - and she died within months." Blaesilla was a young widow (`story.rome-crisis`, `figure.blaesilla`), so lifelong virginity was not open to her. P1 misleading: "The enslaved and dependent people... trouble us more" gives the circle a modern unease the record does not show. "those whose lives were bound to hers came with her or were left behind" infers what `limit.f5-enslaved`'s not_for bars ("inferring how a mistress's conversion affected those she owned"). The Blaesilla funeral and the weeping are faithful. |
| 26 | f6-e-probe-01 | PASS | P2 | pass | concern | concern | pass | - | Paragraph guidance (A1). | Torture source. A model use of `hal.limit.martyrdom`: the Pliny account "belongs to an earlier age of the church, not to our own". P2 access: an 11-sentence paragraph. P2 craft: stock turn "not coercion, but curation". |
| 27 | f6-p-probe-01 | FAIL | P1 | concern | pass | concern | fail | wrong record offered | Retrieval: `hal.demo.someone-like-me` is keyed to this canon question (`_fleet.canon.f6-p-01`) and should lead the evidence. The replay offers `hal.dw.sin-grace` first and not the demo. | A person like me. P1 focus and misleading: it opens "we will not pretend we held light opinions about the life you are asking us to consider" and answers with sin and Fabiola's penance. It presumes the asker has a fault to repent. The world's own answer (the hostel and hospital "for strangers and the sick, whoever they were"; "Nothing we kept speaks of a test at the door") is never given. P2 craft: "We are the representative of one bounded network" is a role label in place of the we-voice; "We will not weigh you for belonging somewhere we are not" is unclear. |
| 28 | f6-t-probe-01 | PASS | - | pass | pass | pass | pass | - | - | Fate of outsiders. Faithful to `hal.dw.hell` and `hal.demo.hell`: real judgment, universal restoration renounced under pressure, "hope" for every soul, no lists of the lost. Holds the tension without softening. |

## Quote-context check

| Quote | Where | Matches record | Used as its source meant |
|---|---|---|---|
| `hal.quote.rufinus-writes-because-rome-is-where-the-news-is` | f1-e | yes | yes: overlapping authorities, no summons, no verdict |
| `hal.quote.she-put-on-sackcloth` | f1-p | yes | yes, but the lead-in invents "the emperor Lateranus" and "the day before Easter" (row 7) |
| `hal.quote.she-put-on-sackcloth` | f3-p | yes | yes: the way back after a public fault |
| `hal.quote.helmeted-preface` | f2-i | yes | yes: which books counted, and a defended translation |
| `hal.quote.helmeted-preface` | f3-t | yes | **no**: placed as evidence of what later centuries did with the books (row 16) |
| `hal.quote.i-gather-the-rose-from-the-thorns` | f4-e | yes | yes: the harsh ranking even friends resisted |

14 of 28 drafts tagged one or more quotes that placement then cut, 23 quote sentences in all. In the replay, most of these quotes were in the turn's own evidence (always-at-his-books alone was cut five times), so the cause is placement, not retrieval. No cut quote shipped. The harm is the sentences left pointing at them (c-e, c-t, f1-e, f2-i, f2-p, f5-e, f5-i).

## Craft

**Best writing.**

1. f3-e: "We were not a persecuted church meeting in secret. We were an established church arguing about whether its own wealth had ruined it."
2. f1-t: "We cannot give you a worked-out answer to how the guilt is passed, because we ourselves did not settle it." This states an honest limit in the world's own terms.
3. f5-p: "Everything, and not everyone." Then: "Others belonged to what the giving built, without giving the same way themselves."
4. f4-i: "We will answer you plainly: we cannot give you the steps, because no document gives them to us."

**Worst writing.**

1. f1-e: "The争 carried on in letters".
2. f4-i: "propositum, real period wording, though it is not quoted for these women". The record's caveat is read aloud.
3. f6-p: "We are the representative of one bounded network of households and monasteries".
4. f2-e: "Rome and Bethlehem, 382-420." The build's window is read aloud.

**Repetition across answers (P2).** Record text is recited whole rather than drawn on:

- `hal.dw.record` in c-i, c-e and f2-i.
- `hal.dw.apostolic` in f2-t, f4-e and f5-t.
- The Ciceronian dream in c-p, f1-p, f2-p and f4-p.
- Fabiola's penance in c-p, f1-p, f3-p and f6-p.
- The "detestable monks" funeral in f4-t and f6-i.

These are single-turn probes, so this is not a conversation defect. It shows that a few tier-1 witnesses answer most questions word for word.

**AI tells.** No disclaimers or hedging filler. The remaining tells:

- **Signposting.** "beginning with the writings themselves, then the transmission, then..." (c-e).
- **Stock turns.** "not coercion, but curation" (f6-e).
- **Coined closers.** "The treasure does not shine for the one still standing at a distance" (f2-p); "It is given something to hold" (f4-p); "The honesty is not a failure. It is what we have." (f2-e).

## Findings

### P1

- **E1. Engine cut leaves orphans (engine).** Rows: f2-p, f5-i (P1); c-e, c-t, f1-e, f2-i, f5-e (P2). Placement removes each quote-tagged sentence it cannot place, and keeps the sentences that point to it. Fix: when a quote sentence is cut, cut or redraft any following sentence that refers back to it ("she", "that", "those words", "But"). Better still, offer the voice only quotes it can place, so it does not draft around quotes that will be cut.
- **E2. No output check for damaged text (engine).** Row: f1-e. A CJK character shipped inside a voice sentence. Fix: hold any character outside the Latin script and its punctuation unless it is inside a placed quote.
- **E4. Lead-ins and uncited specifics ship unchecked (engine).** Rows: f1-p ("the emperor Lateranus", "the day before Easter"), f2-i (inverted Ep. 22), f2-p (practices tagged to `dw.apostolic`). Fix: test a quote's lead-in against the quote and its record; hold an uncited sentence that reports what a named writer said; attach a citation only where the sentence shares content with the record's text.
- **R1. Contested claims stated as settled (retrieval and records).** Rows: f5-p (Paula's totality), f3-i (Marcella "without contest"). Fix: relate `hal.contested.paula-renunciation-totality` to `story.paula-epitaph` and `term.renuntiatio` so it travels with them; add a claim_guard to `story.paula-epitaph`; rewrite `hal.gravity.marcella-authority`'s description, and stop offering gravity records as speakable ground.
- **C1. No closing-edge horizon caution (caution).** Row: f3-t. Caution 6 covers only the pre-382 edge. Fix: add a post-420 caution (row 16 has the wording). The engine horizon check should also read "centuries", "later" and "never became", not only year numbers (E5).
- **R2. Wrong record or term attached (retrieval and engine).** Rows: f6-i (virginitas glossed onto the widow Blaesilla), f6-p (`dw.sin-grace` offered over the demo keyed to the question), f1-i (no record on God's character, so the suffering witness is bent to fit).

### P2

- **A1. Paragraph and sentence length.** 27 of 28 answers have a paragraph over four sentences, and 27 of 28 have a sentence over 25 words. FK passes everywhere; FRE is under 60 in three answers. Fix: as lpc A1, give the voice prompt a paragraph rule, and give `engine/m7/turn_readability.py` a paragraph measure.
- **Monasterium not_for.** "double monastery" in f2-e, f3-i and f5-e. Fix at `hal.term.monasterium`: an output check, or a plain alternative wording.
- **Record text read aloud.** f4-i (`term.propositum`'s plain_meaning carries a build caveat); c-t (`dw.was-jesus-god`'s modern-frame sentences recited unasked).
- **Retrieval misses.** f2-t (`dw.authority`), f3-p (`dw.church-failure`), f4-p (the Hebrew-as-remedy formation line), f5-t (`dw.marriage-ending`).
- **Caution 4 for the scholarly cell.** f2-e. Clarify what the voice may say about the fluency contest.
- **E3. Punctuation splice.** Double periods in c-e and f5-e.
- **We-voice.** f5-i ("What I have told you"), f6-p ("We are the representative").

## Top failure causes

1. **Engine cut** (E1): orphaned references after quote removal. 2 P1 rows, plus P2 residue in 5 other rows.
2. **Engine grounding and output checks** (E2, E4): invented lead-ins, uncited specifics, a citation that does not hold its sentence, and a garbled character. 4 P1 rows (f1-e, f1-p, f2-i, f2-p).
3. **Right record not offered, or wrong record offered** (R1, R2): contested and question-keyed records missing from the evidence. 4 P1 rows (f3-i, f5-p, f6-i, f6-p).
4. **Voice not told what is unknown** (C1): no post-420 caution. 1 P1 row (f3-t).
5. **Missing record**: no witness on God's character (f1-i), and no record for Jerome's reading instruction (f2-i).

## What would clear this

1. **Engine.**
   - E1: cut or redraft the references left by a removed quote.
   - E2: an output check for non-Latin script.
   - E4: lead-in, uncited-specific and citation-content checks.
   - E5: horizon words, not only years.
   - The paragraph measure (A1).
2. **Records and cautions.**
   - The post-420 caution (C1).
   - The paula-renunciation relation and claim_guard (R1).
   - The marcella-authority gravity description (R1).
   - The f5-enslaved not_for (row 25).
   - The sackcloth claim_guard (row 7).
   - The helmeted-preface not_for (row 16).
   - propositum's plain_meaning (row 17).
   - A decision on a God's-character witness or honest limit (row 5).
3. **Retrieval.**
   - Lead with `hal.demo.someone-like-me` for f6-p.
   - Offer `dw.church-failure`, `dw.marriage-ending`, `dw.authority` and the contested records where rows 12, 15, 23 and 24 name them.
4. **Re-run.** After the fixes, re-run the 11 FAIL rows as a named live test with a cap.

PASS 17, FAIL 11, NOT SCORED 0 of 28
