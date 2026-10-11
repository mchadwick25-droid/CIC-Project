# cappadocian — identity-and-scaffolding record pass, adversarial review round 1 (2026-10-06)

Branch `records/identity-scaffolding-cappadocian` (commits a388838d, 4afc2741), diff `git diff origin/main...HEAD`. Reviewer: Opus 5.5. No model or API spend. No records edited.

**Verdict: REVISE.**

**Oblique disagreement: no.** The world's sources are Basil's letters and canonical letters, the Nazianzen orations and the Nyssen treatises. They argue doctrine and give rulings directly. The apophatic reserve (akatalepsia, Basil's reserve on the Spirit) is content the world holds, not an oblique answer shape. The author also says the world is not oblique. Leading with who is right.

## Method

- Compared the old text (`git show origin/main:<path>`) with the new text, paragraph by paragraph and sentence by sentence, for all 21 changed witnesses. Checked every frontmatter field: only `text` changed in each file. Checked each record's `retrieval.retrieve_when` for the kind of question the opener must answer.
- Ran a recursive scan of every spoken field (`text`, `plain_meaning`, `quick_meaning`, `tellable_as`, `modern_contrast`, `absent_detail`, `prior_sense`, `retelling`, `modern_rendering`, nested ones included) in every witness, term and story under `records/cappadocian/`. The scan looked for question marks and for second-person or stage-direction phrases. I also read all 26 witnesses in full, including the five untouched ones.
- Read every markdown body diff for the commentary removals.
- Re-ran the gates: `engine.m10.cli records cappadocian` PASS; `engine.m10.cli regate cappadocian --base origin/main` PASS; `engine.m2.cli determinism-check cappadocian` PASS; `engine.m2.cli staleness-check` shows cappadocian not stale; `engine.m2.site_cli staleness-check` shows no stale world; `tools/check_live_commentary.py --base origin/main --enforce` exit 0; the embedded-quotation baseline test passes with `"cappadocian": 0`; `engine.m9.cli check` exit 0, "clean - every finding is waived, every waiver is live and current", so the cappadocian readability waiver at 274 matches this run.
- Pin: `sha256sum packages/cappadocian/2026-10-06T22-28-44Z/manifest.json` = `5af54bb7…acc5a`. This matches `records/worlds/cappadocian.yaml` `package.manifest_hash`, and `location` matches. The manifest's `records_commit` is the origin/main base (50d39828), the same practice as the don pass.
- (h) Files changed outside `records/cappadocian/` and `Build/`: `cic-website/data/worlds/cappadocian-nicene-pastoral-monastic-tradition.json`, `engine/m9/enforce.py`, `packages/cappadocian/2026-10-06T22-28-44Z/manifest.json` and `records/worlds/cappadocian.yaml`. The last two are the expected package and pin. Of the rest, only the site JSON and `enforce.py` are code or site changes. Confirmed. The site JSON diff changes only `_generated_by` and the two Jesus witness citations (`narrative/questions/0` and `/1`), which match the new texts. The `enforce.py` diff is the one waiver count, 302 → 274.

## Findings

### 1. Substantial — OG-36 says no known-wrong claims are carried, but two edited witnesses carry claims OG-34 records as wrong

OG-36: "Known-wrong claims carried unchanged: none found in this world's gap entries against these records."

That is false. The gap item on record defects found while drafting use notes (slice 6, 2026-10-04) records:
- (3) `cappadocian.dw.stillness-and-the-summons` blends Gregory of Nazianzus's Oration 2 defence of fleeing office with Basil's riverside retreat in Pontus, as if one man wrote both. The edited text still says: "One of them wrote the era's own classic defense of fleeing church office for a quiet retreat by a riverbank - and then served in that office anyway…"
- (9) `cappadocian.dw.macrina-and-its-cost` says her "mother" tried to arrange matches, where the source has "her parents". It also sources "Two of her own brothers became some of our greatest bishops" to `cappadocian.story.forty-sebaste`, which does not support it. The edited text still says "she refused every later match her own mother tried to arrange" and "Two of her own brothers became some of our greatest bishops."

The pre-launch voice-error item (2026-10-04, item 2: Emmelia "arranged matches for her daughter") is the same misreading reaching the voice.

Carrying these unchanged was correct under the brief. The log must say so.

Fix: replace the sentence with: "Known-wrong claims carried unchanged, for the project lead: `stillness-and-the-summons` (the Oration 2 / riverside-retreat blend) and `macrina-and-its-cost` (the 'mother' arranging matches; the two-bishops claim sourced to forty-sebaste). Both are recorded in the gap item on record defects found while drafting use notes (slice 6, 2026-10-04), items 3 and 9; the second is the source of the 'Emmelia arranged matches' voice error in the pre-launch voice-error item (2026-10-04)." Also put both in the report to the project lead.

### 2. Substantial — other inaccurate sentences in OG-36

(a) The entry lists "Now the cost, told exactly" among the second-person stage directions removed. Only "Now" was removed. `macrina-and-its-cost` still says "The cost, told exactly: no see, no pulpit, was ever hers". Fix the record, not the log: "Her authority had a cost. No see, no pulpit, was ever hers; her authority ran through household and community, not office." Or correct the log to say the phrase was kept.

(b) "Long sentences in the touched witnesses were split … no wording was added for that." The splits did add words. Examples: "He said they taught" (a-stranger-weather), "A synod did it, one he said was packed against him" and "He was sent to a province." (authority-and-spread), "Then came full return to communion." and "We do not smooth it" (marriage-ending), "We did not mean … We meant" (who-was-jesus), "We lived through those councils and helped write them." and "So, more distantly, does Protestant dogmatics." (catholic-and-its-rivals), "They did not argue against the seriousness behind it." (baptism-and-new-birth). Fix: "split; only subjects, verbs and connectives needed to make whole sentences were added, no content."

(c) The "Quotes" paragraph says the only quotation marks are the participant's words. It leaves out that the quotation marks around "Personal Lord and Savior" in `was-jesus-god` are new, and so is the capital P. The old text had the phrase unquoted: "Was he our personal Lord and Savior? Not our own phrase." Fix: say the quotation marks were added. Better, restore the old form without quotation marks, to match the source phrasing the record carries in `positions` ("Lord and Savior" was not this world's own phrase). Also see finding 3 on "recompiled at the records commit".

(d) Coverage gaps removed without logging; see finding 4.

### 3. Substantial — the site JSON names a records commit that is not in the branch's history

`cic-website/data/worlds/cappadocian-nicene-pastoral-monastic-tradition.json` `_generated_by` reads "from records_commit e025d05324204d4075f940efe774eb2192a01701". That commit exists only locally and is not an ancestor of HEAD (`git merge-base --is-ancestor e025d053 HEAD` fails). It is an earlier version of a388838d that was amended away. Its records are identical to a388838d, so the content is right and the staleness check passes. But once the branch is pushed, the provenance line points at a commit that does not exist anywhere. OG-36 says the JSON "was recompiled at the records commit", which is not the case.

Fix: after the round-2 records commit, recompile with `python -m engine.m2.site_cli build cappadocian --records-commit <that commit> --compiler-version cic-m2-site-compiler-2` and commit the JSON on top, without amending.

### 4. Substantial — body notes that recorded unanswered canon variants were removed and not logged

The commentary removal dropped three notes. Each recorded a canon-cell variant this world's witness deliberately leaves unanswered:
- `a-stranger-weather` (F3-E): the "gospels that didn't make it in" variant, "which has no real Cappadocian ground and is left unaddressed here".
- `baptism-and-new-birth` (F4-T): "honestly declining the tithe and end-times variants this world's own registered material does not develop".
- `marriage-ending` (F6-T): "The 'hell for outsiders' variant this cell also carries is honestly left unanswered here".

These are process wording, so taking them out of the record body is right. But they were the only record of known coverage gaps: neither `Open_Gaps_Tracking.md` nor any record mentions tithe, end-times, "hell for outsiders" or "gospels that didn't make it in". CLAUDE.md requires every known gap in the gap tracker. Fix: add to OG-36: "Coverage gaps moved here from record bodies: F3-E 'gospels that didn't make it in', F4-T tithe and end-times, F6-T 'hell for outsiders' are not answered by this world's witnesses; the record has no ground for them."

Everything else the pass removed was process history: cell codes, "this session", hal comparisons, design rationale. Genuine source notes were kept. One vendored-file pointer was dropped: the npnf208 file behind Epistle 188, in `marriage-ending`. The cited source record `cappadocian.source.basil-canonical-letters-to-amphilochius` still carries it, so nothing is lost.

### 5. Substantial — `cappadocian.dw.want-to-believe`: orphaned "the first answer" and a quantifier change

Old: "So if you want to believe and cannot, we would not tell you first to try harder. We would tell you that not grasping God completely was never, for us, the same thing as not knowing him at all".
New: "So the first answer was never to try harder. Not grasping God completely was never, for us, the same thing as not knowing him at all".

"The first answer" now has no antecedent, because the participant's situation it answered was removed. And the world's counsel ("we would not tell you first") has become an absolute claim about the past ("was never").

Fix: "For someone who wants to believe and cannot, our first word would not be to try harder. Not grasping God completely was never, for us, the same thing as not knowing him at all - both were held together, one not waiting to defeat the other."

### 6. Substantial — `cappadocian.dw.psalms-teach-the-singer`: counsel turned into a new claim about the past

Old: "If you come away from scripture confused or bored, we would not tell you to try harder at reading it. We would tell you what actually worked for most of us: reception before analysis."
New: "Trying harder at reading was not what worked for most of us: reception came before analysis."

The new sentence claims that most of this world tried harder at reading and it did not work. The record never said that, and `cappadocian.dw.reading-scripture` says most of them "could not read at all". The counsel to the confused reader, which was the answer, is gone.

Fix: "For someone confused or bored by scripture, we would not counsel trying harder at reading. What worked for most of us was reception before analysis."

### 7. Substantial — `cappadocian.dw.customs-from-the-apostles`: the new opener strengthens the claim

New opener: "We knew our unwritten practices went back to the apostles by how widely they were kept, not by a documentary chain."

The old text said the practice's universality "was itself the evidence we trusted". "We knew" turns trusted evidence into knowledge. "How widely" weakens "kept everywhere, by every church", and the "impersonal transmission" leg in `positions` drops out of the opener.

Fix, from `positions` ("kept everywhere as apostolic"; "universality and impersonal transmission, not a documentary chain"): "We held our unwritten practices to be apostolic because every church kept them, everywhere, not because of a documentary chain."

### 8. Substantial — `cappadocian.dw.where-record-thinnest`: the opener adds a new description of the record

New: "Our own record is thinnest where it rests on one voice alone, and a rule we hold ourselves to says such a claim must say so."
Old: "Where is our own record thinnest? We will tell you plainly, because a rule we hold ourselves to says a claim resting on one voice alone must say so."

In the old text, the one-voice rule was the reason for disclosing. It was not the answer to where the record is thin. The places the text then lists are mostly missing voices: no women's text, the countryside never speaking, opponents surviving only in hostile accounts. "Rests on one voice alone" is a new description that does not fit them. "Such a claim" also has no clear antecedent.

Fix, from the text's own next sentences: "Our own record is thinnest beyond one family and one circle of friends. Almost everything you have from us comes from them: three men, one household, one circle of students who met at school together. A rule we hold ourselves to says a claim resting on one voice alone must say so."

### 9. Substantial — `cappadocian.dw.ordinary-day`: the opener does not answer the question

`retrieve_when`: "participant asks what an ordinary day looked like among this world's people". New first sentence: "Our record lets us reconstruct a whole day in one of our own brotherhoods." That says what the record allows, not what a day looked like. The day starts in sentence three. OG-36 defends the opener as a disclosure. The disclosure is right to keep, but the ruling puts the answer first.

Fix: "An ordinary day in one of our own brotherhoods began before first light, when the house rose for fixed psalms. No single brother left us a diary of one ordinary day, so this is reconstruction, not one person's own account. Prayer was set at set hours so devotion would not wait on mood. …" (the rest unchanged).

### 10. Substantial — `cappadocian.dw.power-and-its-discipline`: the opener answers neither question

`retrieve_when`: (1) "whether this world's church protected people who caused harm"; (2) "asks this world to defend using power against Christians who disagreed". New first sentence: "The empire that had pressed a different creed on us finally backed our own instead." That is background. The answer to question 1 comes in sentence 8 ("we built real, working machinery, not a cover-up"), and the answer to question 2 in sentence 4 ("We will not pretend that was simply justice arriving"). The pass reordered `baptism-and-new-birth`, `catholic-and-its-rivals` and `customs-from-the-apostles` for exactly this reason; this witness needs the same.

Fix: move the wrongdoing sentences first, then the power history, with no wording change: "On wrongdoing inside our own communities, we built real, working machinery, not a cover-up. Our own canonical letters graded penance by the offense, set terms of exclusion, and set the path back into communion. We cannot show you our own record handling a specific kind of institutional cover-up. What we can show you is a real, if incomplete, disciplinary practice, honestly disclosed as incomplete. The empire that had pressed a different creed on us finally backed our own instead. …" (the rest unchanged).

### 11. Not substantial — `cappadocian.dw.authority-and-spread`: the founding legend's hedge now covers less

The old text was one sentence, inside "the story we told ourselves credited one missionary … and left it, by the time he died, with only seventeen who still held the old gods". The new third sentence, "By the time he died, it had only seventeen who still held the old gods.", stands outside "so the story runs". The frame sentence and the tensions field still mark the passage as Tier 3 legend, so this is not a claim change. But the record's own body warns against the "seventeen/seventeen" reading as a census. Recommended: "By the time he died, so the story runs, only seventeen still held the old gods."

### 12. Not substantial — `cappadocian.dw.who-was-jesus` (identity witness): the opener passes; one split is ambiguous

The opener, "Jesus was the Son, one being with the Father, and the ground everything else in our life stood on.", passes check (c). It says who first, in the world's own words ("the Son", "one being"). "One being" moved up from the old "We confessed him fully what the Father is, one being, not merely like the Father" and was removed there. It is sourced by `cappadocian.term.homoousios`, and nothing unsourced was added. No known-wrong claim is recorded against this witness.

The split "We did not mean equal to God, the gap between maker and creature never closing." can be misread as denying that the gap never closes, the opposite of the `positions` line. Recommended: "We did not mean equal to God; the gap between maker and creature never closed. We meant truly made like him, endlessly, by grace."

### 13. Not substantial — `cappadocian.dw.was-jesus-god`: "the question was never open" is sourced

"Jesus was God: we confessed the Son as fully what the Father is, and for us the question was never open." Two old sentences support this: "We would find the question strange only in being asked as open" and "we spent two generations defending, not deciding, its answer". "Fully what the Father is" is moved from the same text. The sentence states what the old opener implied and adds no new content. The opener answers the did-question directly.

### 14. Not substantial — second-person framing left in place (consistency, not ruled scaffolding)

- `where-record-thinnest` (edited): "We would not tell you this record would survive unchallenged in a university library. We would tell you exactly where a serious reader should press hardest." This is the answer to the university-library question, but it has the same "we would not tell you / we would tell you" shape the pass removed from `psalms-teach-the-singer` and `want-to-believe`. Optional: "This record would not survive unchallenged in a university library. It shows exactly where a serious reader should press hardest."
- `holy-spirit-honored` (untouched): "What we can tell you is how it ended:". Optional: "It ended this way:".
- `becoming-one-of-us` (untouched): "You were signed into the Name… taught to believe as you had been baptized… And if you wronged the community". This is a generic narrative "you", not a stage direction. Leave it.
- `not-later-formulas`: "The question of original sin, whether people are born already guilty, is not one our own record answers in those terms." It names the topic as the subject of an answering sentence and is not a question form. Acceptable. Optional: "Our own record does not answer whether people are born already guilty; original sin in those terms is a later, largely Western argument."

### 15. Not substantial — build narration in an untouched story's spoken `text`

`cappadocian.story.poorhouse-famine-month` `text`: "This is deliberately not the famine of 368/9 … This is a different, later month, unattested in its own right, imagined only because…". This is the author's voice in a spoken field. It is not dialogue scaffolding, and the file is outside this pass's edits, so OG-36's "No term or story record carried scaffolding" stands under the ruling. Recommended: add it to OG-36 for the world's build thread (the batched build-narration pass).

## Checks with no finding

- (a) Apart from the findings above, every other changed paragraph keeps its claims. That covers a-stranger-weather (the "Perhaps" hedge kept), baptism-and-new-birth (reorder only), catholic-and-its-rivals (reorder; the today's-church answer kept in the traditions sentence), confession-not-a-vote, doubt-and-unfinished-growth, how-it-reached-us, macrina-and-its-cost, marriage-ending ("Yes" became the permission it answered; "genuinely ended" kept; penance and return kept), not-later-formulas, stillness-and-the-summons, unwritten-carries-too ("No" became "Scripture was not our only authority"; "why" still has its antecedent) and wealth-answerable-to-the-poor.
- (d) Orphans: only finding 5 ("the first answer") and finding 8 ("such a claim"). The others checked are bound: "Perhaps an outsider would have found this strangest" points forward to the next sentence; "exactly that feeling" in doubt-and-unfinished-growth and "the reaching" in stillness-and-the-summons both have antecedents.
- Quotes: no `quote` record or vendored source quotation was touched. No re-verification against `cic/texts/` was needed.
- (g) The waiver tightened to 274 matches the m9 run; see Method. Baseline test, pin and site recompile: see Method and finding 3.

## For round 2

Targeted recheck only: findings 1–10, the OG-36 rewrite, and a fresh site JSON compiled at a reachable records commit. Findings 11–15 are recommended and do not block.
