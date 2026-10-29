# pahc fleet graded run 1 (28 October): answer review

## Verdict

**Revise.** 9 of the 28 answers fail. All 28 passed the run's own automatic checks (`source_boundedness`, `register_coined_aphorism_heuristic`), so those checks caught none of the failures below.

At its best Chloe is plain, careful and honest about what her record holds. The Corinth answer (f3-p) says "We cannot tell you who was right" and means it. The catacombs opening (f3-e) is a clean "No." followed by what the record does hold. The typical-day answer (f5-i) states the limit first and invents nothing. The voice almost never invents. Most of the damage is done after the draft.

Five causes account for most of the failures:

- **Quote placement removes the answer (engine).** The voice wrote 22 quote markers in 16 answers. Two were placed. The placer removed 25 sentences, 18 of them because the lead-in "does not name its speaker" ("He wrote:", "One of us wrote", "The letter itself argued"). In f5-t and f6-p the removed sentence was the answer. In f3-e the cut moves Lucian's mockery onto Pliny.
- **Retrieval does not offer the cell's own records.** In 13 of 28 turns the rebuilt evidence held none of the records the cell's coverage names. The voice found most of them in the full prompt anyway. Where it did not, it failed: f4-t (no baptism record), f6-p (no someone-like-me demonstration), f5-p (no record of what belonging cost), f2-e (no scholarly-standing witness), f6-e (no Pliny record).
- **Record text that breaks a sibling record's guard.** `limit.womens-own-words` calls ministrae "a title of service, of office" (f3-i). `limit.material-remains` and `limit.enslaved-voices` tie Pliny's worship report to the torture (f6-e). `witness.god-and-argument` speaks of "later councils", against caution 10 (P2 in c-t, f1-i, f1-e).
- **Build talk and the present day.** f2-e names Roger Bagnall, "the window", "this world's own voice" and "voiced thinness". f3-t speaks of "every present-day church" in the prompt's own build words ("our own ecology", "generative problem"). No caution tells the voice not to speak about itself as a build.
- **One quote out of context, one invented fact.** f4-t sets Justin's "Moses is older than all the Greek writers" as his words on baptismal rebirth. It also says the new-birth saying was "heard read aloud when we gathered", which no record holds.

## Scope and checks

- **Run.** Fleet graded run 1, world pahc, 28 sealed probes, protocol "blind". Voice: Sonnet 4.5 (`us.anthropic.claude-sonnet-4-5-20250929-v1:0`). The run made no safety or reader call. Package `packages/pahc/2026-10-28T03-51-09Z`, manifest hash `a4e1e7e1…`, which matches the registry pin in `records/worlds/pahc.yaml`. Report: `engine/m3/reports/fleet-graded-run-1/pahc.json`.
- **Read in full.** All 28 questions (`canon/sealed_probes/plaintext/<probe_id>.md`) and all 28 shipped `answer_text`s. For each I also read `raw_text`, `citations` and `citation_entries`.
- **Net rebuilt.** I re-ran `engine.m4.turn.apply_net` on each saved `raw_text`, with evidence rebuilt by `engine.m4.evidence.assemble_evidence` on the pinned package. The output matched the saved `answer_text` in 28 of 28 turns, so the removal reasons and grounding verdicts below are the run's own. This is local, deterministic code. The model SDK modules were stubbed so it could import; no model was called.
- **Records.** Claims were checked against `prompt.txt` (world_core cautions 1-10, horizon, formation logic, thinness) and against `repository.json` for every witness, limit, story, term, gravity, contested claim and quote record the answers cite or draw on. Three points were checked against the vendored source `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml`: First Apology 61 on rebirth ("For Christ also said, 'Except ye be born again…'"), Dialogue 88 ("the human race, which from Adam had fallen under the power of death"), and Pliny's informants, through the `figure.pliny` record.
- **Quotes.** Both placed quotes match `pahc.quote.moses-is-more-ancient`'s `modern_rendering` exactly, checked by script. Context was checked against the record's `use_note.not_for`. One typed quotation survived the net: "'our God'" in f2-e. It is accurate to Ignatius.
- **Readability.** I ran `engine.m1.gates.grade_text` on every answer. Sentence and paragraph counts are by script (`engine.prose.quote_aware_sentences`), with a placed quotation counted as one sentence.
- **Not done.** No model was called and no git command was run. Only this file and its `.counts.json` were written. No data from before 27 October was compared, per the instruction.

## Method

This follows `Build/worlds/lpc/Review-Artifacts/Run3_Access_And_Craft_Review_2026-10-28.md` and the rubric in `Build/worlds/lpc/build/lpc_Probe_Results.md`:

- **P1** is wrong, invented, misleading or damaged. **P2** is small and fixable.
- Four criteria are graded per row: Rigor, Accessibility, Craft, Focus.
- A row with any P1 is **FAIL**. A row with only P2s is **PASS**, and its P2s are noted.
- **NOT SCORED** is for a row with no voice answer. Every pahc probe got a voice answer, so no row is NOT SCORED.
- Accessibility is a concern where a reader meets a paragraph of 8 or more sentences, a sentence of the voice's own over 30 words, or a term used before it is explained.
- A turn above FK 10 or below FRE 60 is a hard fail under the per-turn gate (`engine/m7/turn_readability.py`). I grade it FAIL even when its content is sound.
- Each fix is made at the source: a record, a caution or an engine item, never a patch to one answer.
- Cause layers: missing record / right record not offered / wrong record offered / voice not told what is unknown / caution wording / engine cut / quote used out of context. "Caution wording (record text)" means the voice-facing text of a record says something its own guards, or a sibling record's guards, forbid.

## Results

| Probe | Result | Severity | Cause layer | Fix |
|---|---|---|---|---|
| c-i-probe-01 | PASS | P2 | engine cut | Faithful to `witness.who-was-jesus` and `witness.jesus-as-god`. The net removed both quotes, because the voice typed Ignatius's and the Didache's words itself and they did not match. It also removed "In one of our communities, the prayer opened", the line that kept the cup prayer to one community. What ships says "When we gave thanks over the cup… we thanked" for everyone, against caution 5. who-was-jesus's own text says the same. A 31-word sentence. Fix: E1. Record: in who-was-jesus, "In one of our communities, when we gave thanks over the cup". |
| c-e-probe-01 | PASS | P2 | right record not offered; engine cut | Faithful to `witness.how-we-know`, which was not offered (the voice used it from the prompt). After a cut, "Those writings were read aloud" points back loosely. "The voice that reaches you now is not the voice of those who sat and listened" is self-reference. A 31-word sentence. R1, E1. |
| c-p-probe-01 | PASS | P2 | engine cut; focus | Faithful to `witness.coming-to-belief`. After the flame sentence was cut, "the old man's words" refers to an old man who is never introduced. The middle paragraph recites how the faith was handed down, which a doubter did not ask about. An 8-sentence paragraph. E1. |
| c-t-probe-01 | PASS | P2 | right record not offered; record wording | Correct from the prompt: we called him God, and worked out no account of it. jesus-as-god and its quote were not offered. Justin's quote was cut because its lead-in says "He wrote" and not "Justin". "in the way later councils would take up" leans past the window. That is god-and-argument's own text, against caution 10. Nothing is said of the Spirit, though the threefold name at baptism is in `term.baptisma`. A 34-word sentence. R1. E1: let the placer accept a pronoun whose speaker is named in the sentence before. R3. |
| f1-i-probe-01 | PASS | P2 | record wording (focus) | Only the opening is about God's character. The rest recites god-and-argument's "what we actually argued about". The records hold more: in `quote.hermas-doubting`, God "remembers no wrongs, and has compassion on his own creation", and the Father raises those who believe. "the way your later world did" leans past the window. A 37-word sentence. R3: add a position on God's character to god-and-argument and remove "later councils" and "later world". |
| f1-e-probe-01 | PASS | P2 | right record not offered | No council, only letters, and Corinth's outcome is unknown. All of it is faithful. The cell's own quote (`quote.not-every-one-that-speaketh-in-the-spirit`, the Didache's test of a prophet by his conduct) was not offered. So the world's working answer to "who settled it" is missing. The hostile-account quote was cut because its lead-in names no speaker. R1, E1. |
| f1-p-probe-01 | PASS | P2 | right record not offered; citation | The words come from `witness.doubt-and-asking`, which was not offered. They are cited to prayer-and-struggle, which does not hold them; the net flagged three of them. The reply does not say that Hermas's doubt is doubt in prayer, not doubt about whether to believe (the record's tension and not_for). A 9-sentence paragraph. R1, E4. |
| f1-t-probe-01 | PASS | P2 | wrong record offered; missing record | `limit.faith-alone-later-frame` (faith and works) was offered for a question about inherited guilt, and half the reply is about justification. "Whether an infant carried guilt from birth… our own texts do not say" holds. But Justin's Dialogue 88 (vendored in anf01) says the human race "from Adam had fallen under the power of death", and that each person "had committed personal transgression". No record carries it. An 8-sentence paragraph. R2: author an F1-T witness from Dialogue 88, verified against anf01. R1: narrow faith-alone's `retrieve_when`. |
| f2-i-probe-01 | PASS | P2 | right record not offered; engine | Faithful to `witness.reading-scripture`, which was not offered. The evidence held `craft.chloe-voice`, a voice-craft record, and the voice cited it for its opening line. A craft record is instruction, not a source. E7: keep voice_craft records out of evidence and citations. R1. |
| f2-e-probe-01 | FAIL | P1 | right record not offered; caution wording; engine | Build talk: "this world's own voice", "the window", "We cite him often", "we cite it as contested", "We never import Dura-Europos, the catacombs, or post-200 material" (caution 8 read aloud), "We choose voiced thinness over silent honesty". After the window: "Roger Bagnall's papyrological argument". A voice of 70-200 names a scholar of 2009. Misleading: "A scholar checking our quotes against the Greek or Latin would find them". The renderings are modern English made from 19th-century translations. The record's "silent before Bishop Demetrius's episcopate (189-231)" becomes "silent before c. 189-231". 622 words in 11 paragraphs, with stripped headings left as fragments ("First: The Ignatius dependency."). `witness.scholarly-standing`, written for this cell, was not offered. R1. C2: a self-reference and build-talk caution. E3: a build-word output check. R5: take Bagnall's name out of the voice-facing text of `contested.egypt-exclusion`. E5: length ceiling. |
| f2-p-probe-01 | PASS | P2 | focus | The Moses quote is placed in its own context (Justin arguing who came first) and keeps its not_for on Genesis as science. P2: half the reply answers a science question no one asked. The opening line is cited to scripture-and-testimony, which does not hold it. `witness.hard-texts` was offered and not used. |
| f2-t-probe-01 | PASS | P2 | rigor wording; engine cut | Faithful to scripture-and-testimony and `term.prophetes`. P2: "elders wrongly removed" gives Rome's verdict as fact, against our-own-failures' not_for; f3-p says "We cannot tell you who was right". The list of "sources" leaves out the prophets' writings, which reading-scripture calls the main scripture. The Clement quote was cut because its lead-in was "The letter itself". E1. |
| f3-i-probe-01 | FAIL | P1 | caution wording (record text); engine cut | Contested claim stated as settled: "Two women among us carried the name ministrae - a title of service, of office." `term.ministrae` bars "deaconess as a settled office title". The quote bars "ministrae was the community's own word rather than Pliny's". `story.pliny-interrogation` says the reading is contested. The sentence is `limit.womens-own-words`'s own statement. P2: after the Clement cut, "But that argument was made in a letter correcting another church's dispute" points to no argument. A 42-word sentence. R4: rewrite womens-own-words and enslaved-voices ("servants, deacons") along these lines: "A Roman governor called two of our women ministrae, his own Latin word. What they called their service, we do not know." E1. |
| f3-e-probe-01 | FAIL | P1 | engine cut | After the Lucian lead-in was cut, "He meant it as mockery. It still shows we were visible enough to be mocked" follows straight on from the paragraph about the governor. It now says Pliny mocked them. Lucian is never named. The rest is faithful to `witness.outsider-view`, which was not offered. P2: ekklesia is cited to material-remains, not `term.ekklesia`. A 41-word sentence. E1: when a removal leaves a following "He", "That" or "It" pointing elsewhere, redraft or hold. R1. |
| f3-p-probe-01 | PASS | P2 | right record not offered | Faithful to `witness.our-own-failures` (not offered, used from the prompt) and the Corinth story, with its absent detail kept. P2: "the one case" where the record says "the clearest case". An 8-sentence paragraph. R1. |
| f3-t-probe-01 | FAIL | P1 (readability gate; horizon) | missing record; caution wording; engine | FRE 53.2. Present day: "Every present-day church inherits something from the world that came after us". Build words from the prompt's formation_logic: "our own ecology", "That generative problem", "re-enacting the unresolved questions that was itself the shape of belonging". It cites an invented id, `pahc.core.formation-logic`. The net marked six sentences "withhold" and shipped them. F3-T's coverage points at the rival-movement records, and none of them speaks to this question. R2: author an F3-T honest limit. C1: a caution that the voice says nothing of churches, events or survivals after c. 200. R4: rewrite `core.house-church` formation_logic in plain world words. E2: run the readability gate in the harness. E3: hold withheld sentences. |
| f4-i-probe-01 | PASS | P2 | engine cut | The steps are right and the Didache's one-community scope is kept. P2: the three sentences that said what the Two Ways taught were cut as quote lead-ins with no speaker. So "The teaching went all the way down to sharing" has no starting point, and the reader never hears the teaching. "how far this exact shape reached" is cited to prayer-and-struggle. A 31-word sentence. E1. |
| f4-e-probe-01 | PASS | P2 | rigor wording | Faithful to `witness.apostolic-practice`, and claim and proof are kept apart. P2: "the same practices repeated in Antioch, in Asia Minor, in Rome" goes against `gravity.liturgical-practice` (its order varies house to house) and caution 5. "The chain we claimed is real" sits close to the record's not_for (proof of an unbroken chain). Four sentences over 25 words. The Clement chain quote was cut. E1. |
| f4-p-probe-01 | PASS | P2 | craft | Faithful to prayer-and-struggle and `term.eucharistia`, with scope kept. P2: a coined closer, "The table kept forming us."; the last paragraph, on peace with someone unreconciled, was not asked. A 32-word sentence. |
| f4-t-probe-01 | FAIL | P1 | right record not offered; quote used out of context; engine cut | Quote out of context: Justin's "regenerated" sentence is set with `quote.moses-is-more-ancient` ("Moses is older than all the Greek writers…"). That quote is from First Apology 44, on philosophers borrowing from the prophets, not from 61 on baptism. Invented: "We heard that read aloud when we gathered." Wrong: "The one who walked with Jesus said it first". Justin gives the saying as Christ's own ("For Christ also said", 1 Apol 61). "born of water and Spirit" is not the wording any record holds. Contradicts the record: "the baptisma - was not usually spoken of with that phrase". `term.baptisma` says Justin gives the saying as the reason for the washing. The net removed the closing hedge, so the reply ends on an unqualified "yes". F4-T's own records (`quote.in-living-water`, `term.baptisma`, whose `retrieve_when` names "born again") were not offered. R1. E5b: placement should test the lead-in's content against the quote record's `means`, not only the speaker's name. E1. |
| f5-i-probe-01 | PASS | P2 | engine cut | The limit comes first, then Justin's gathering. Nothing is invented. P2: the sermon step was cut (its lead-in named no speaker). "made a real difference" states as fact what `story.day-under-bishop-and-presbyters` gives as a reconstruction (Inferential-Thin). A 48-word sentence. E1. |
| f5-e-probe-01 | PASS | P2 | record wording | A faithful recital of `limit.material-remains`, which keeps its not_for. P2: one 11-sentence paragraph. It opens on a question not asked ("how historians even know about ordinary days like ours"). "house-churches you can visit today" points to the present. All three come from the record's own statement. R4: trim it. |
| f5-p-probe-01 | FAIL | P1 | right record not offered; missing record | Misleading: "What it cost in practice to live that way, our record does not say" and "What an ordinary believer gave up to belong… our own words cannot show you". The record shows belonging could cost a life. Pliny executed those who held to the name (`story.pliny-interrogation`, `figure.pliny`), and Trajan's reply kept the penalty. None of that was offered. F5-P's coverage points at `story.polycarp-forwards-letters` and the letter network. P2: "It went all the way down" after a cut. "The people who walked that road could not read or write" says all where the record says most. R1: re-point F5-P to `gravity.state-pressure`, story.pliny-interrogation and `term.two-ways`. R2: author an F5-P witness. |
| f5-t-probe-01 | FAIL | P1 | engine cut | The answer was cut. The net removed "Ignatius told Polycarp that those who marry should do so with the bishop's own approval…" as "tagged to a quote record that has not been placed". What ships says "That is the instruction we have" with no instruction, then "It means the bishop's approval mattered", for an approval never stated. The limits that follow are good. E1: when the sentence is a witness's own paraphrase and is grounded, a tag to an unplaced quote should drop the tag, not the sentence. |
| f6-i-probe-01 | PASS | P2 | right record not offered | Marcion through his opponents, faithful to hard-texts. P2: the cell's own record (`witness.what-we-never-settled`, "the hardest true thing") was not offered. So "Whether any of us was unsettled… by who led us… our record does not say" undersells the quarrel the record calls its hardest truth. The Two Ways paragraph is off the question. An 8-sentence paragraph; five sentences over 25 words. R1. |
| f6-e-probe-01 | FAIL | P1 | caution wording (record text); right record not offered | Misleading on the point asked: "What he wrote down comes from that interrogation" and "what torture made them say". The worship details came from people who said they had once been Christians and had given it up (`figure.pliny`). Torture found nothing but "superstition". `witness.outsider-view` bars "a claim that the worship details came from the tortured ministrae". The closing "his letter does not say" where the details came from is also wrong. The question's premise needed correcting, and the voice took it on. The source is `limit.material-remains` ("had them tortured to make them talk. What he wrote down afterward…") and `limit.enslaved-voices`. R4: rewrite both statements to keep the informants' account apart from the torture. R1: offer figure.pliny and story.pliny-interrogation for F6-E. |
| f6-p-probe-01 | FAIL | P1 | engine cut; wrong record offered | Damaged after three lead-ins were cut. "What we can tell you is what we taught before the water. That was put before every person." names nothing taught. "That was the instruction we have. Whether every household actually sought that approval" names no approval. Marriage has no place in this question. `demo.identity-collision-someone-like-me`, written for this cell, was not offered, and `quote.ignatius-marriage-bishop` was. E1, R1. |
| f6-t-probe-01 | PASS | P2 | missing record; engine cut | Both answers are held unreconciled, as `witness.outside-our-community` asks, and the assurance limit is faithful. P2: "lived reasonably" is not glossed (lived by the Word), which invites the pluralist reading the quote's not_for bars. Half the reply is about the faithful dead, not those outside. No record gives what Justin says of judgment. The quote was cut because its lead-in was "He wrote:". A 39-word sentence; an 8-sentence paragraph. E1. R2: a witness on judgment, verified against anf01. |

## Findings

### P1

**E1. Quote placement and post-draft removal (engine).**
- The voice wrote 22 quote markers in 16 answers, and 2 were placed. The net removed 25 sentences:
  - 18 because a lead-in "does not name its speaker"
  - 2 placed quotes that did not match their record
  - 2 that "give a quote record's words without placing it"
  - 1 quotation the voice typed
  - 1 for words attributed without a placed quote
  - 1 tagged to an unplaced quote
- Damaged: f5-t and f6-p, where the cut took the answer. Made false: f3-e, where Lucian's mockery now belongs to Pliny. Residue (P2): c-i, c-e, c-p, f3-i, f4-i, f5-i, f5-p, f6-t. In c-i and f4-t the cut took the very sentences that kept a claim in scope.
- Root cause: the voice paraphrases a quote's content and puts the marker at the end, or uses "He wrote:" after naming the speaker one sentence earlier. The placer refuses, and the refusal deletes the sentence even when it is the witness's own grounded paraphrase.
- Fix (same item as lpc E1 and ijc E1):
  - Accept a lead-in whose pronoun resolves to the speaker named in the sentence before.
  - When placement is refused, strip the marker and keep a sentence that grounds to its own witness. Do not delete it.
  - When a removal takes an answer-bearing sentence, or the sentence a later "He", "That" or "It" points to, redraft or hold.

**R1. Retrieval does not offer the cell's own records.**
- In 13 of 28 turns the rebuilt evidence held none of the records the cell's coverage names: c-e, c-t, f1-e, f1-p, f2-i, f2-e, f3-e, f3-p, f3-t, f4-t, f6-i, f6-p, and f5-p, whose coverage itself is wrong.
- The voice recovered most from the full prompt. It failed where the record was not in the prompt (f4-t: `term.baptisma`'s "born again" sense, `quote.in-living-water`) or where a wrong record was offered (f6-p: the marriage quote; f1-t: faith-alone).
- The admission harness matches the probe text to canon cells and does not pass the cell it is testing, so this is the live path's retrieval too.
- Fix: in coverage and `retrieve_when`, add the plain wording these questions use ("born again", "someone like me", "gave up", "settled doctrine", "struggle to believe"), so Stage A finds the cell. Re-point F5-P and F3-T coverage (see M1).

**R4. Record text that breaks a guard (records).**
- `limit.womens-own-words`: "Two women among us carried the name ministrae - a title of service, of office" (f3-i, P1). It contradicts `term.ministrae`, the Pliny quote's not_for and `story.pliny-interrogation`.
- `limit.material-remains` and `limit.enslaved-voices` tie the worship report to the torture (f6-e, P1). This contradicts `witness.outsider-view`'s not_for and `figure.pliny`'s account of the informants.
- `core.house-church` formation_logic is voice-facing ("Formation logic (cite as …)") and is written in build words. f3-t recites it.
- Fix: rewrite the three limit statements as given in the table. Rewrite formation_logic in the world's own words, or keep it out of voice-facing text.

**H1. After the window and build talk (caution, engine).**
- f2-e names Roger Bagnall and speaks of "the window", "this world's own voice", "post-200 material" and "voiced thinness".
- f3-t speaks of "every present-day church".
- Fixes:
  - **C1.** Add a world_core caution in the lpc 430-ruling form: the voice knows nothing after c. 200, and names no later church, council, event, scholar or survival.
  - **C2.** Add a caution like lpc caution 15: never explain the "we", and never speak of the voice, the window, the record as a build, or confidence ratings.
  - **R5.** Remove Bagnall's name from `contested.egypt-exclusion`'s voice-facing claim. Keep it in the source note.
  - **E3.** Add an output check for "this world's own voice", "the window", "ecology", "generative problem" and modern scholars' names.

**Q1. f4-t: quote out of context and an invented fact (engine, retrieval).**
- The placer accepted Moses-is-more-ancient because the lead-in names Justin. It does not check that the lead-in's subject (rebirth at baptism) matches the quote's `means` (Moses older than the Greek writers).
- "We heard that read aloud when we gathered" is invented. "The one who walked with Jesus said it first" gets the speaker wrong: Justin gives the saying as Christ's.
- Fix:
  - **E5b.** Test the lead-in's content words against the quote record's `means` and `text`, and refuse on no overlap.
  - **E4.** Hold an uncited specific claim for a grounded redraft, as in lpc E3. The net marked "The one who walked with Jesus said it first" as withhold and shipped it.
  - **R1.** Offer baptisma and in-living-water for "born again".

**M1. Missing records.**
- F3-T has no record for present-day continuity. Author an honest limit, written inside the horizon.
- F5-P has no record of what belonging cost. Its coverage names the letter network. Author a witness from Pliny's executions, Trajan's reply, and the Two Ways' sharing of goods.
- F1-T has no record of what Justin says of Adam. Author one from Dialogue 88 (anf01 line 22597).
- F6-T has no record of what the writers say of judgment.

**A0. Readability hard-fail not gated (engine).**
- f3-t is at FRE 53.2. The admission harness does not run `engine/m7/turn_readability.py`, so it counted as passed.
- f2-e is 622 words and only just clears the gate, at FRE 60.2.
- Fix (E2/E5): run the turn gate in the harness, and add a length ceiling.

**E3b. Withheld sentences ship (engine).**
- 45 sentences across the run carry a grounding verdict of `withhold`, and all of them shipped.
- They include the invented id in f3-t, the Bagnall sentence in f2-e and the misattribution in f4-t.
- Fix (same as lpc E3): a withheld specific claim is held for a grounded redraft, not shipped untagged.

### P2

- **A1. Paragraph and sentence length.**
  - Nine answers have a paragraph of 8 or more sentences. The worst is f5-e, at 11.
  - Fourteen have a sentence of the voice's own over 30 words. The longest are f5-i (48), f3-i (42) and f3-e (41).
  - Fix: a paragraph rule in the prompt, and a paragraph measure in the turn gate (lpc A1).
- **R3. "Later councils" and "later world".** These come from `witness.god-and-argument`'s own text and appear in c-t, f1-i and f1-e. They break caution 10 (councils are unknown to this world's voices). Fix: rewrite them as "No gathering of ours ever met to settle a question like that about God", and stop there.
- **E4. Citations.**
  - f1-p cites prayer-and-struggle for doubt-and-asking's words.
  - f4-i and f2-p cite records that do not hold the sentence.
  - f3-e cites material-remains for ekklesia.
  - f2-i cites the voice-craft record (E7).
  - Fix: the grounding net should require shared content with the cited record (lpc register-4 item).
- **Repetition.**
  - limit.ordinary-majority's "our own words cannot show you" and "never made it onto the page" ship in six answers (c-p, f2-i, f3-i, f5-p, f6-i, f6-p).
  - "None of us saw him ourselves… That is how it reached us" ships in both c-e and c-p.
  - Fix: draw on a record's meaning instead of copying its text, and add a conversation-level repeat check (lpc R-1).
- **Craft.** Coined closers: "The table kept forming us." (f4-p), "The teaching, the fast, the water, the table." (f4-i), "The letter is what survives, not the outcome." (f1-e).
- **Rigor wording.** f2-t "elders wrongly removed". f4-e "the same practices repeated in Antioch, in Asia Minor, in Rome". f5-i "made a real difference" for a reconstruction. f3-p "the one case".

## Quote-context check

| Probe | Quote | Matches rendering | Used in its source's context |
|---|---|---|---|
| f2-p | moses-is-more-ancient | yes | yes: Justin's argument about who came first, presented as his argument, and the Genesis-as-science not_for kept |
| f4-t | moses-is-more-ancient | yes | no: set as Justin's words on rebirth at baptism. The source is First Apology 44, on philosophers borrowing from the prophets (P1) |

- Twenty other quote markers placed nothing, and their sentences were removed (E1).
- The one typed quotation that survived ("'our God'", f2-e) is accurate to Ignatius.
- No quote was altered.
- Two quotes the voice typed itself in c-i did not match their records: it inserted "And he was truly raised" and dropped the opening "So close your ears". The net removed both. The check works. The prompt should stop the voice from typing quotes at all.

## Top failure causes

1. Engine quote placement and post-draft removal: 3 P1 rows (f3-e, f5-t, f6-p), part of f3-i and f4-t, and residue in 8 more. 22 markers, 2 placed, 25 sentences removed.
2. Retrieval not offering the cell's own records (13 of 28 turns): f2-e, f4-t, f5-p, f6-e and f6-p fail on it.
3. Record text that breaks a sibling record's guard: f3-i (ministrae as an office), f6-e (the torture and the worship report), and f3-t (formation_logic build words).
4. After the window and build talk, with no caution to stop it: f2-e (Bagnall, "the window") and f3-t ("every present-day church").
5. Missing records for F3-T, F5-P, F1-T and F6-T.
6. One quote out of context and one invented fact, both in f4-t. The placer checks the speaker's name, not the subject.
7. Gates that shipped what they flagged or never ran: 45 withheld sentences shipped, and f3-t's FRE 53.2 was not gated.

PASS 19, FAIL 9, NOT SCORED 0 of 28
