# cappadocian: fleet graded run 1, answer review (28 October)

## Verdict

**Revise.**

Chilo is mostly faithful and readable. All six placed quotes match their records word for word. The best answers (F3-E, F5-T, F6-P, F5-P) are concrete, honest about their limits and in the world's own voice. But 6 of 28 answers carry a P1 defect. Three causes account for most of them:

- **No record where one was needed.** The fate of those outside the church (F6-T) and an outside record obtained under torture (F6-E) have no record. The voice went silent on a well-documented, contested teaching in F6-T, and broke frame in F6-E.
- **The right record was not offered.** The scrutiny question (F2-E) did not get `cappadocian.dw.where-record-thinnest`. The "what unsettled you" question (F6-I) did not get `cappadocian.limit.whose-voice-we-lack`. In both, the voice built its own answer and went wrong.
- **The engine's quote removal leaves lead-ins behind.** In F4-E a lead-in survived its removed quote and now says the opposite of the answer. Smaller residue appears in F2-T, F1-E and F6-T.

On craft, the main weakness is length and repetition. Paragraphs run long in 27 of 28 answers. The same record sentences ("sung so many times that they came to interpret the singer", "argued hard against the delay without mocking the fear") recur in up to eight answers.

## Scope and checks

- **Run.** Live test "fleet graded run 1", authorized by Mark on 28 October, world cap $3.92. Voice: Sonnet 4.5 (Bedrock, us-east-1). The harness makes the voice call only: there is no safety call, no reader call and no self-revision. The deterministic net (`apply_net`) shapes each reply, quote placement and removal included.
- **Package.** `packages/cappadocian/2026-10-28T03-49-28Z`, manifest `sha256:e14488cd...`. That is the registry's current pin, so the tested package is the live one.
- **Automatic checks not computed.** One call hit a transient API error and was retried. The harness then counted 29 calls for 28 probes and refused to write the report (`cappadocian.stderr.txt`). So there is no `cappadocian.json` and no automatic pass result. This review grades the 28 saved answers in `engine/m3/reports/fleet-graded-run-1/cappadocian.json.answers.jsonl` by hand.
- **Probe order.** Index i maps to the i-th entry of `protocol.battery()`. That is C-I, C-E, C-P, C-T, then F1 to F6 in the order I, E, P, T, the same as `gallic.json` per_probe. Each question was read from `canon/sealed_probes/plaintext/<probe_id>.md`.
- **Quotes, by two methods.** (1) A script matched all six quoted spans in the answers against `modern_rendering` in the package's `quotes.json`, and all six match exactly. (2) Each quote record's `text` was found in its vendored file: `npnf208_basil-letters-select-works.xml` (Letter XVI ant, On the Holy Spirit 27.66, Homily XIII excerpt line 7019), `gregory-nyssa_life-of-macrina_clarke1916.txt` line 128, and `basil_ascetic-works-longer-shorter-rules_clarke1925.txt` line 17072. For each, the not_for and retrieve_when were also read against how the answer used it.
- **Records.** Every factual claim was checked against world_core (horizon, the eight cautions, living_traditions, thin_topics) and against each cited record. Where a cell's own record was not cited, that record was checked too. About 120 claims were checked.
- **Readability.** `engine.m1.gates.grade_text` (local code) was run on each answer. Sentence and paragraph counts are by script, with each placed quote counted as one sentence.
- **Not done.** No model was called and no git command was run. Only this file and its `.counts.json` were written. Safety turns are out of scope: this battery has no safety probe, and none was routed.

## Results

Severity: P1 is wrong, invented, misleading or damaged. P2 is small and plainly fixable. A row with only P2 defects is PASS, with the defects noted. The four criteria are Rigor, Accessibility, Craft and Focus.

Accessibility counts as a concern where a reader meets a paragraph of 8 or more sentences, a sentence of the voice's own over 30 words, FRE under 60, or a term used before it is explained.

| # | Probe ID | Result | Severity | Rigor / Access / Craft / Focus | Cause layer | Fix at the source |
|---|---|---|---|---|---|---|
| 0 | c-i-probe-01 | PASS | P2 | concern / concern / concern / concern | caution wording | Macrina's reasoning about her betrothed is given as hers, with no "through her brother's pen" (caution 3). The resurrection and Macrina paragraph is a tangent. "We confessed him fully what the Father is" is broken grammar. Fix: in `cappadocian.dw.macrina-and-its-cost` and its use_note, keep the pen caveat in the same sentence as the reasoning, so a lifted fragment carries it. |
| 1 | c-e-probe-01 | PASS | P2 | concern / pass / pass / pass | right record not offered | Says "It came to us already given, not gathered by us" and "the heart of it came to us whole". That is the deposit model for everyone, which the record's own not_for bars. Basil's grandmother letter (`cappadocian.quote.macrina-the-elder-taught-me`, canon cell C-E) was not offered. Fix: move "not gathered by us" out of `cappadocian.dw.how-it-reached-us`'s spoken `text` and into its tensions. Make retrieval offer the grandmother quote with this witness. |
| 2 | c-p-probe-01 | PASS | P2 | concern / pass / concern / pass | caution wording | The lead-in "Basil wrote to Eunomius" is wrong. Letter XVI is "Against Eunomius the heretic", not a letter to him. The quote's Contested authorship (the same passage stands in Gregory of Nyssa) is not flagged. The quote fits its context. Coined closers: "Belief grows where the praying is kept"; "The door stayed open" is not in the record. Fix: add to the quote's use_note a not_for "a letter addressed to Eunomius", and a lead-in line that names the shared passage. |
| 3 | c-t-probe-01 | PASS | P2 | pass / concern / concern / pass | engine cut | Faithful: one ousia, three hypostases, Basil's reserve on the Spirit held as contested, 381 writing down the worship. P2 craft: "The council wrote down what the font and the prayer already said" appears twice. "before any council met again in our lifetimes" is unclear (it is the record's own phrase). Three sentences over 25 words. Fix: rewrite that phrase in `cappadocian.dw.confession-not-a-vote`. Engine R-1: drop a sentence repeated inside one reply. |
| 4 | f1-i-probe-01 | PASS | P2 | pass / concern / pass / pass | none (craft) | Accurate on incomprehensibility, epinoia, homoousios and eusebeia, and introduces its terms. P2 access: paragraphs of 6 and 7 sentences; a 38-word sentence. |
| 5 | f1-e-probe-01 | PASS | P2 | pass / concern / concern / pass | engine cut | It answers who settled disputes, and how. P2 craft: "One honest limit touches this directly. So the deposit model..." reads out build labels, and "one bishop's own search" points to a quote that was never placed. "Authority ran through distributed, portable carriers" is world_core's etic formation_logic, spoken aloud. P2 access: FRE 59.4, a 42-word sentence. Fix: engine (remove the lead-in with the quote). Record: the term "deposit model" and "honest limit" must not be in any spoken field. |
| 6 | f1-p-probe-01 | PASS | P2 | pass / concern / concern / pass | none (craft) | The answer is yes, with real ground: delayed baptism, the open door, penance. P2 access: a 10-sentence paragraph. P2 craft: "a method for silencing the head completely" is lifted from the stillness record and makes no sense here. |
| 7 | f1-t-probe-01 | PASS | P2 | concern / concern / pass / pass | caution wording | It holds that the record does not frame inherited guilt. P2 horizon: "came later than our own years, and it was mostly argued in the West" knows a post-394 debate. It is the record's own sentence. Fix: rewrite `cappadocian.dw.not-later-formulas` `text` to "we did not frame it that way" without naming a later Western argument. Note for the build: Gregory of Nyssa's "On Infants' Early Deaths" bears on this cell and is not in the records. |
| 8 | f2-i-probe-01 | PASS | P2 | pass / concern / concern / concern | caution wording | Faithful on sung scripture, low literacy, mysterion and plain reading. P2 focus: ends on "We cannot give you our teachers' answer on the violence in our scriptures", which no one asked. The sentence sits in `cappadocian.dw.psalms-teach-the-singer`'s spoken `text`. Fix: move it from `text` to tensions, so it is said only when violence is asked about. |
| 9 | f2-e-probe-01 | FAIL | P1 | fail / concern / fail / pass | right record not offered | P1 misleading, and voice-itself: "Our record's strongest claims would pass under close examination... most of it would stand, because we have built this record to the same standard a rigorous reader brings." It also says "three places we have already named" and "We have not made those claims". This is build narration in the voice, and it breaks the not_for of `cappadocian.dw.where-record-thinnest` ("a claim that the record would pass unchallenged"). It misses caution 1, the chief limit: three men, one family and one circle, partly a family memorial. The cell's own record was not cited. P2 access: FRE 55.9; "Pneumatomachians", "Eustathians" and "Gangra radicals" are not explained. Fix: retrieval must offer `cappadocian.dw.where-record-thinnest` to scrutiny questions. Engine: an output check for talk about "this record" or "we have built". |
| 10 | f2-p-probe-01 | PASS | P2 | pass / concern / pass / concern | caution wording | Good answer: "reception before analysis", "until the words stood inside you". P2 focus: the unasked violence limit again (same record line as row 8). P2 access: a 6-sentence paragraph. Fix: same as row 8. |
| 11 | f2-t-probe-01 | PASS | P2 | pass / concern / concern / pass | engine cut | Correct: scripture was not the only authority, and the unwritten customs are listed. P2 damaged: "He had used two forms of a familiar prayer side by side. The other gave it through the Son" — the "One gave glory..." sentence was removed, so "The other" has nothing before it. A 40-word sentence. Fix: engine (a removal must not take one half of a pair). |
| 12 | f3-i-probe-01 | PASS | P2 | concern / concern / concern / concern | quote used out of context | The household, reluctant office, brotherhood rule and creed all match `cappadocian.force.gentry-household` and `cappadocian.gravity.renunciation-order`. P2 quote context: the Macrina refusal quote (177 words) is placed to show her authority. Its not_for bars "her authority as head of the Annisa community", and the quote is about her refusal of marriage. P2 rigor: Gangra is given as a fixed "break" with no word on its disputed date (caution 8). The radicals are given as the canons tell it, against `cappadocian.contested.eustathian-radicals`. P2 access: 644 words, four paragraphs of 9 sentences. Fix: engine E5 (test placement against not_for). Records: narrow the quote's retrieve_when, and add a Gangra-date clause to the renunciation-order description. |
| 13 | f3-e-probe-01 | PASS | P2 | concern / concern / pass / pass | engine cut | A plain, correct "No. We did not hide in catacombs." P2 rigor: Eupsychius, executed in 362 inside the window, is dropped (caution 2). It sits in the cited record's text, so "the executions of our grandparents' era had passed" stands alone. "on charges their own brothers called trumped up" turns one case (Gregory of Nyssa) into many. P2 access: an 8-sentence paragraph. Fix: in `cappadocian.dw.authority-and-spread`, pair "the executions had passed" with Eupsychius in the same sentence. |
| 14 | f3-p-probe-01 | PASS | P2 | concern / concern / pass / pass | missing record | An honest answer that matches `cappadocian.dw.power-and-its-discipline`: real penance, no surviving case of a leader held to account. P2 rigor: "They set terms for... theft" has no record behind it, and the sentence is uncited. P2 access: one 16-sentence paragraph; "chorepiscopoi" is not explained. Fix: author Basil's theft canon from the vendored canonical letters, or keep the voice to the canons the records hold. Gloss chorepiscopoi on first use. |
| 15 | f3-t-probe-01 | PASS | P2 | pass / pass / concern / pass | none (living_traditions) | Follows world_core living_traditions closely, as the ruling allows. P2: it adds "the later divisions inside the Reformation" and "sixteen centuries", which go beyond the record's own wording. |
| 16 | f4-i-probe-01 | PASS | P2 | concern / concern / pass / pass | caution wording | Steps match `cappadocian.dw.becoming-one-of-us`. P2 rigor: "You were taught afterward to believe as you had been baptized" puts the teaching after the font. Basil's sequence (`cappadocian.quote.baptize-believe-glorify-in-sequence`) is baptized as taught, then believing as baptized. P2 access: paragraphs of 8 and 11 sentences. Fix: record text should say "taught to believe as you had been baptized" with no "afterward". |
| 17 | f4-e-probe-01 | FAIL | P1 | fail / pass / fail / concern | engine cut | P1 damaged and misleading: "One of our own bishops did trace a line back through named hands. So the deposit was not handed complete to every believer in one unbroken chain." This is the lead-in to `cappadocian.quote.macrina-the-elder-taught-me`, which was removed. Without the quote, a question about apostolic origins reads as if Basil traced a chain back to the apostles. That breaks the quote's own not_for (the chain reaches only to Gregory Thaumaturgus). The "So" then contradicts it. The east quote is used in its own context and matches. P2 craft: the "already given" and "318 fathers" paragraph repeats row 1. Fix: engine (when a quote is removed, the lead-in and its "so" go too, or the turn is redrafted). Record: give `cappadocian.dw.customs-from-the-apostles` a spoken sentence that says the grandmother's chain reaches Thaumaturgus, not the apostles. |
| 18 | f4-p-probe-01 | PASS | P2 | concern / concern / pass / pass | quote used out of context | It keeps the record's limit: "not a technique for quieting an anxious mind." P2 quote context: the lead-in is "fixed hours of prayer, kept whether we felt like it or not. Basil wrote:" but `cappadocian.quote.basil-on-work-and-prayer` is about not using prayer as an excuse to skip work, and every hour suiting prayer. The quote does not say what the lead-in says. P2 access: a 9-sentence paragraph. Fix: the quote's retrieve_when should not match a busy-mind question. Engine E5 lead-in test. |
| 19 | f4-t-probe-01 | FAIL | P1 | fail / concern / concern / pass | caution wording | P1 misleading: it opens "No. That phrase is not ours." The cited record says "We treated baptism as new birth in the plainest sense we had". The new-birth language is scripture's own (John 3), and the answer later says "new birth was what we called it", so it contradicts itself. The voice misread the not_for "the modern evangelical sense of being born again" as a denial of the phrase. P2 access: a 43-word sentence; FK 8.9. Fix: record `cappadocian.dw.baptism-and-new-birth`: open the text with the yes ("Yes, new birth was our word, and the Gospel's"). Add the not_for "a claim that this world did not speak of being born again". |
| 20 | f5-i-probe-01 | PASS | P2 | pass / pass / concern / pass | none (craft) | Faithful to `cappadocian.dw.ordinary-day`, and it says plainly that the day is a reconstruction. The quote is in its own context. P2 craft: "Prayer was set at set hours"; the 153-word quote is a third of the reply. |
| 21 | f5-e-probe-01 | PASS | P2 | concern / pass / concern / pass | caution wording | It holds `cappadocian.limit.no-stones-to-show`. P2 rigor: "Stone, perhaps... Drainage from the infirmary... Coins dropped at the martyr feast's own market" guesses at physical remains. The limit's not_for bars "a description of how either building looked", and the next sentence says "we will not describe what we cannot show". A 48-word sentence. Fix: add to the limit's not_for "guesses at what a dig might turn up". |
| 22 | f5-p-probe-01 | PASS | P2 | concern / concern / pass / pass | none (craft) | Naucratius, the delay sermon (in its own context; matches), and the radicals corrected. All match their records. P2 rigor: "The font asked nothing up front" is unsupported (baptism included a renunciation, and the records do not say it asked nothing). P2 access: a 14-sentence paragraph; "viaticum" in the quote is not explained. |
| 23 | f5-t-probe-01 | PASS | P2 | pass / concern / pass / pass | none | Strong and exact: the canons on leaving a spouse, the unequal custom, second marriage with a year (some said two), and Macrina with the pen caveat. It is honest that the wedding rite itself is not in the record. P2 access: an 8-sentence paragraph; a 36-word sentence. |
| 24 | f6-i-probe-01 | FAIL | P1 | fail / concern / concern / concern | right record not offered | P1 invented: "What unsettled us - what we never quite resolved - was whether the singing already said what the argument defended". No record holds this tension. It gives the community an inner unease the evidence does not show. The cell's own record, `cappadocian.limit.whose-voice-we-lack` ("whose voice you are really hearing"), was not offered. Only its Macrina end appears. P2 rigor: "money-changers and bakers told customers..." is given as fact. The record calls it a preacher's half-joking complaint, and its not_for says not a census. P2 access: one 17-sentence paragraph. Fix: retrieval for "unsettled / troubled you / never settled" should offer the whose-voice limit and `cappadocian.demo.never-settled`. Engine E3: hold an uncited claim about the world's inner life for a grounded redraft. |
| 25 | f6-e-probe-01 | FAIL | P1 | pass / pass / fail / concern | voice not told what is unknown | P1 voice-itself: "I do not have a record that names any source obtained under torture. The ground given for this turn holds only two things... The records I am holding now..." It speaks as a system reading its evidence block, in "I", and ends with an assistant offer ("name it plainly, and I will tell you"). The content after that is accurate (Modestus via Gregory's funeral speech; Eunomius through hostile paraphrase). Fix: author an honest_limit for this cell: no outside record of our worship was taken under torture, and the outside witnesses we have are hostile (Julian), not forced. Engine: an output check that blocks "record", "ground", "this turn" and "I am holding" in voice text. Render the evidence block so its labels are not echoed. |
| 26 | f6-p-probe-01 | PASS | P2 | pass / concern / pass / pass | none (craft) | Faithful to `cappadocian.demo.someone-like-me`: received and fed from the plain table, with the gap between the rule and lived practice stated plainly. P2 craft: the demo's required non-judgment opening ("not here to judge you") is missing. P2 access: a 9-sentence paragraph. |
| 27 | f6-t-probe-01 | FAIL | P1 | fail / pass / fail / fail | missing record | P1 misleading silence: "Our record does not develop that question... The silence there is real". This world's own authors did develop it, and disagreed: Basil taught that punishment is eternal, and Gregory of Nyssa argued for a final restoration of all, a reading that is itself contested. No record holds either, so the voice reports a silence that is in the build, not in the sources. P1 damaged: "That was Gregory of Nyssa's own teaching, not the whole circle's shared doctrine" is left from a removed epektasis sentence (`cappadocian.dw.doubt-and-unfinished-growth`). It now pins theosis on Gregory alone. It was offered `cappadocian.dw.not-later-formulas`, which does not fit. Fix: author a contested_claim on the fate of those outside, holding Basil's eternal punishment and Nyssa's restoration both. Verify each against the vendored NPNF volumes before authoring. Point the cell to it. Correct `cappadocian.dw.marriage-ending`'s stray tension about outsiders. Engine: same lead-in rule as row 17. |

## Readability

| Measure | Result |
|---|---|
| FK grade | 5.1 to 9.4 (all under 10) |
| FRE | 2 answers under 60: F1-E 59.4, F2-E 55.9 |
| Sentences over 25 words (voice's own) | 43 across 28 answers; the longest are 48 (F5-E), 43 (F4-T), 42 (F1-E), 41 (F2-E), 40 (F2-T) |
| Paragraphs over 4 sentences | 27 of 28 answers; 10 answers have a paragraph of 8 to 17 sentences (F1-P, F3-I, F3-E, F3-P, F4-I, F4-P, F5-P, F5-T, F6-I, F6-P) |
| Length | 153 to 644 words; F3-I (644) and F4-P (449) are walls of text for a phone reader |

FK and FRE are not the main barrier. Paragraph length is: F3-P and F6-I are each one unbroken block of 16 and 17 sentences.

## Craft

**Best writing.**

1. F3-E: "No. We did not hide in catacombs... The weather was hostile, but it was not the catacombs." Direct, plain, and the world's own image.
2. F2-P: "It was being stood inside the words, at fixed hours, until the words stood inside you." The record's idea, said once and memorably.
3. F6-P: "The rule survives; the doorkeeper's own thoughts do not. So we know what ought to have happened." This is how a limit should sound.
4. F5-T: "So we held marriage as binding, judged its breaking harshly, and gave second marriages grudgingly." Exact, and true to the canons.

**Worst writing.**

1. F6-E: "The ground given for this turn holds only two things." The chatbot speaking, not the world.
2. F2-E: "most of it would stand, because we have built this record to the same standard a rigorous reader brings." Self-praise in build language.
3. F4-E: "One of our own bishops did trace a line back through named hands. So the deposit was not handed complete..." Residue that contradicts itself.
4. F1-E: "One honest limit touches this directly. So the deposit model..." Build labels spoken aloud.

**Repetition across answers (P2).**

- "sung so many times that they came to interpret the singer": C-E, C-P, F1-E, F2-I, F2-P, F2-T, F4-E, F4-P, F6-I.
- "argued hard against the delay without ever mocking the fear": C-P, F1-P, F4-I, F4-T, F5-P.
- "the 318 fathers... before most of us were born": C-E, F1-E, F3-I, F4-E.
- "the practice itself could teach the one who kept it": F1-P, F1-T, F2-I, F2-P, F6-T.
- "Travelers were fed the same portion the house itself ate": C-I, F5-I.

**AI tells.** Stock "not X but Y" turns ("reception before analysis, not the other way round"). Tidy closers ("Belief grows where the praying is kept"; "We never closed it"). One full assistant turn (F6-E).

## Top failure causes

1. **Missing record.** There is no record on the fate of those outside the church (F6-T), and no honest limit for the torture-obtained source question (F6-E). The voice either reports a false silence or falls back on system talk.
2. **Right record not offered.** The cells' own records, `cappadocian.dw.where-record-thinnest` (F2-E) and `cappadocian.limit.whose-voice-we-lack` (F6-I), were not offered. The voice wrote its own answer: one overconfident, one invented. The records' canon_cells tags do not match the sealed battery's questions for several cells (for example F5-T, F6-E, F6-P, F6-I, F6-T). Retrieval should key on the question, not the cell label.
3. **Engine cut leaves lead-ins.** The net removes a quote or sentence and ships what pointed to it (F4-E P1; F6-T, F2-T, F1-E P2).
4. **Caution and not_for wording misread.** A not_for written as a negative ("the modern evangelical sense of being born again") became a false "No" (F4-T). Spoken record text carries unasked limits (the violence line in F2-I and F2-P) and a post-window reference (F1-T).
5. **Voice not told what is unknown, and no output check for system vocabulary.** "I", "this turn's ground" and "the records I am holding" shipped (F6-E). So did "we have built this record" (F2-E).

Invented-fact, horizon or quote failures among the FAIL rows: 2. F6-I is an invented inner tension. F4-E is a quote lead-in left without its quote, and it misstates that quote's chain. The only horizon item is F1-T's "came later", a P2 from the record's own text. No placed quote failed the verbatim check.

## What would clear this

1. Records:
   - Author a contested_claim on the eternal fate of those outside (F6-T), verified against the vendored texts.
   - Author an honest_limit for an outside record obtained under torture (F6-E).
   - Rewrite `cappadocian.dw.baptism-and-new-birth` to lead with the yes (F4-T).
   - Move the violence line, "not gathered by us", and "came later... in the West" out of spoken `text` and into tensions (F2-I, F2-P, C-E, F1-T).
   - Add the not_for items named in rows 2, 12, 18 and 21.
2. Retrieval: offer each cell's own answer record by question (F2-E, F6-I). Offer the grandmother quote with C-E and F4-E.
3. Engine:
   - A removed quote takes its lead-in and its "so" with it, or the turn is redrafted (F4-E, F6-T, F2-T).
   - Output checks for system and build vocabulary (F6-E, F2-E, F1-E).
   - Hold uncited claims about the world's inner life (F6-I).
   - Test placement against not_for (F3-I, F4-P).
   - A paragraph-length measure, and removal of sentences repeated across or inside a reply.
4. The harness: count a retried transient call as one call, so this world's automatic report is written. Then re-run the six FAIL rows as a named live test.

PASS 22, FAIL 6, NOT SCORED 0 of 28
