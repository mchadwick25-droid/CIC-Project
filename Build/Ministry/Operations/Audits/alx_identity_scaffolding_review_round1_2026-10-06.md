# Alexandria identity-and-scaffolding pass: adversarial review, round 1 (2026-10-06)

Scope: branch `records/identity-scaffolding-alx`, one commit ahead of origin/main. Diff checked: `git diff origin/main...HEAD`. All 12 changed witnesses were compared old against new, sentence by sentence, on the `text` field. No other frontmatter field changed. Every in-scope spoken field under `records/alx/` (witness, term, story: `text`, `plain_meaning`, `quick_meaning`, `tellable_as`, `modern_contrast`, `absent_detail`, `prior_sense`, `retelling`, `modern_rendering`) was swept for question forms, second-person address and answer-talk, including untouched files. No model or API call was made.

Mechanical checks run:
- `python -m engine.m10.cli records alx`: PASS (re-run by the reviewer).
- `python tools/check_live_commentary.py --base origin/main` and `--enforce`: exit 0, 0 hits in `records`. See finding 5: the checker does not catch the process notes in these witness bodies.
- `packages/alx/2026-10-06T22-02-26Z/manifest.json` hashes to `sha256:60e7d99c...2d50`, which matches the pin in `records/worlds/alx.yaml`.
- The Origen quote in `alx.dw.apostolic` ('transmitted in orderly succession from the apostles, and remaining in the Churches to the present day') matches `cic/texts/anf04_tertullian4-minucius-felix-commodian-origen1-2.xml` lines 22435-22436 verbatim, capitals included. It was not edited. 'handed down' and 'God the Word' sit in sentences that were only rewrapped.
- The question each cell is asked was read from `canon/sealed_probes/plaintext/` (F1-E: "who settled it"; C-T: Jesus's divine status; C-I: who Jesus was).

## Verdict: REVISE

## Findings

### 1. SUBSTANTIAL: `alx.dw.councils` does not answer the who-question first
New first sentence: "Disputed belief was decided in three ways in our own history."
The record's removed opener was "Who had the right to decide, when belief was disputed?" Its cell probe (F1-E) asks "who settled it". The new first sentence says how many ways, not who. Ruling 1 requires a who-question to get who first. The answer is in the record: positions[0] reads "decision migrated across the window: teacher's argument, bishop's judgment, council's ruling".
Fix: "Who decided disputed belief changed across our own history: first the teachers, then the bishop, and at the end the council. Early on, teachers argued. ..."
In the same record, "Our best picture of deciding well" became "Our best picture of a good decision". The old wording praised a way of deciding, and the next sentence ("It was patient public argument") describes that process. "A good decision" is an outcome, so "It was patient public argument" no longer fits. Restore "Our best picture of deciding well is Dionysius at Arsinoe."

### 2. SUBSTANTIAL: `alx.dw.empire` opener blurs the claim and does not answer the question
Old: "We lived that question inside one lifetime, and our answer is double."
New: "We lived Constantine's empire inside one lifetime. What we saw was double."
- The old sentence meant that one community lived through both sides of the change within living memory. The record body says it directly: "experienced both sides within living memory". The new sentence says "we lived Constantine's empire inside one lifetime", which drops "both sides". It can also be read as the empire lasting one lifetime.
- The removed question was "Did Constantine corrupt the church?" The first sentence does not answer it. The answer comes in the closing lines ("The record does not show a church's purity corrupted").
- Naming Constantine is sourced: the record cites Eusebius, Historia Ecclesiastica, locus "the Constantinian close", and its `use_note.not_for` names Constantine. That part is acceptable.
Fix: "Constantine's empire did not simply corrupt us. We lived both sides of that change inside one lifetime, and what we saw was double. Before 325 ..."

### 3. SUBSTANTIAL: `alx.dw.suffering` opens with a stance, not an answer
New first sentence: "We spoke about suffering from inside it, not from above it."
The removed question was "Why does God allow suffering? Where was he?" The answer the world gives ("three answers we could stand behind") arrives only in the third sentence. The world's own "honest silence" is the third of its answers, not a reason to delay the first. This is not obliqueness in the sources.
Fix: "We gave three answers we could stand behind about why God allows suffering. We gave them from inside suffering, not from above it. Our own years include plagues that emptied streets and persecutions that took our teachers' fathers. First, the teacher's answer: ..." (Drop the later "We gave three answers we could stand behind about why God allows it.")

### 4. SUBSTANTIAL: answer-talk scaffolding left in the identity witness `alx.dw.jesus`
Text: "Between those two sentences lies the whole answer."
"The whole answer" presumes a participant's question and points back to it. That is the same dialogue scaffolding this pass removed elsewhere ("Our answer moves across our own century" was dropped from `alx.dw.was-jesus-god` for this reason). OG-17 left it "for the reviewer", so it is ruled on here: it goes.
Fix: "All we hold about him lies between those two sentences."
The first sentence of the record is sound. "To us Jesus is the Logos - God's own Word, through whom all things were made - come in flesh" leads with who, in the world's own words, and adds nothing unsourced.

### 5. SUBSTANTIAL: process-note commentary left in four live record files this PR edits
The notes are in the markdown body below the frontmatter, not in the spoken `text` field. They are change history and process narration in a canonical surface (`records/`). Under CLAUDE.md, this is corruption to remove, and "any PR that edits a live or canonical file also removes the commentary already in that file." This PR edits all four files:
- `alx.dw.councils`: the "REGISTER TRANSLATION: ..." and "BAR SWEEP: ..." paragraphs.
- `alx.dw.god`: "REGISTER TRANSLATION: ...", "BAR SWEEP: ..." and the "LEXICON LABEL PASS (...) ... Claims unchanged; the label is the whole edit." paragraph.
- `alx.dw.original-sin`: "REGISTER TRANSLATION: ..." and "BAR SWEEP: ...".
- `alx.dw.suffering`: "REGISTER TRANSLATION: ...".
Fix: delete those paragraphs. Keep the one-line record descriptions ("The councils cell, grounded in ..."), since they say what the record is, not how it was edited. Log the removal in the gap entry.
`tools/check_live_commentary.py` reports 0 hits on these lines, so the check passes while the rule is broken. That is a gap in the checker, outside this pass's scope, and it needs its own task. The alx demonstration bodies carry the same kind of history ("REVISED same day (Mark: ...)"). They are not edited by this PR, so this PR does not have to clean them.

### 6. SUBSTANTIAL: OG-17 is inaccurate (`Build/worlds/alx/Open_Gaps_Tracking.md`)
- "the antecedent is now stated in the opening sentence ("when belief was disputed", "about why God allows it")": "when belief was disputed" does not appear anywhere in the new `alx.dw.councils` text. "about why God allows it" is in the third sentence of `alx.dw.suffering`, not the opening.
- "`alx.dw.councils` and `alx.dw.empire`: some sentences were split ...; no clause was added or dropped": the councils opener was reworded, not split. "Deciding well" became "a good decision" (finding 1). In empire, "a church's" was added before "purity".
- "every witness leads with who or what, in the kind asked": not true for councils, empire and suffering (findings 1-3).
- The entry does not mention the process-note commentary in the touched bodies (finding 5).
Fix: after the revisions, restate what moved, including the new openers of councils, empire and suffering with their sources, the `alx.dw.jesus` change, and the body-commentary removal. Leave the status OPEN until round 2. The entry is not yet merged, so editing it in place does not break the append-only rule.
Accurate parts: the list of 12 records matches the diff. OG-17 is the next free number. The known-wrong claims list matches OG-15 items (1), (2), (3) and (5), and each claim is carried unchanged. The quote statement is true. The gate and pin lines check out where re-run.

### 7. NOT SUBSTANTIAL: `alx.dw.was-jesus-god` first sentence (item c)
"From the beginning we worshiped Jesus as the Logos, God's own Word, and we baptized into Father, Son, and Holy Spirit."
It answers the C-T question (divine status and relation to Father and Spirit) at once and in the world's own terms. It was the old second sentence, unchanged, and positions[0] carries it. Nothing was added. Dropping "Our answer moves across our own century" loses no claim: "the precise wording was the work, and the wound, of our last years" still tells the development.

### 8. NOT SUBSTANTIAL: the remaining changed openers hold their claims (item a)
- `alx.dw.church-failure` "Our churches had failures, and our record leaves the wounds visible": the failures are told in the rest of the paragraph, and positions[0] backs it. Nothing added.
- `alx.dw.doubt` "Our teachers left room for doubt": the paragraph holds it ("Doubt aimed at understanding was not treated as sin"), and so do positions[1] and the body.
- `alx.dw.original-sin`: "We did not speak of guilt at birth" moved up intact. "The doctor's imagery outweighs the courtroom's" now stands alone. Nothing changed in meaning.
- `alx.dw.apostolic`, `alx.dw.god`, `alx.dw.one-church`, `alx.dw.record`, `alx.dw.resurrection`: each opener answers the removed question, and the rest is rewrapped only. "We say it plainly and do not smooth it over" keeps the meaning of the dropped second-person line.
- `alx.dw.god` "You do not stare at the sun; you see everything else by it" is a generic "you" inside the world's own image, not a stage direction.
- No orphaned "it/they/this" was found after the removed questions. In suffering, "The community's conduct was its answer" still reads back to the second answer just stated.

### 9. NOT SUBSTANTIAL: untouched terms and stories (item b)
The question forms in `alx.story.john-young-robber` `text` are John's own speech as Clement reports it. They are quoted source speech, not scaffolding. The teller directions in story `modern_contrast` and `absent_detail` ("a telling should say so", "the telling must keep 'the tradition says' audible") and the file and line pointer in `alx.story.didymus-meeting` `absent_detail` ("line ~48652") are written to the builder, not to the participant. They fall outside the dialogue-scaffolding ruling, and OG-17 describes them correctly. No term field carries scaffolding.
Demonstration records are participant/representative exchanges by design, so their questions are not orphaned. OG-17's "No demonstration records were examined" is true. It would be more useful to say they were looked at and carry none.

### 10. NOT SUBSTANTIAL: quotes (item h)
No quote was edited or reordered, so ruling 3 required no re-verification. The reviewer checked the one long quote in a changed paragraph anyway (Origen, above), and it is verbatim.

Oblique disagreement: no. The alx sources answer directly (Origen's rule, Athanasius's one-sentence formula, Dionysius's stated practice). The author recorded the world as not oblique, and this review agrees. Findings 1-3 are openers that need repair, not signs of an oblique world.
