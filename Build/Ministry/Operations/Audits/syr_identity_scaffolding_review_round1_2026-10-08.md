# syr — identity-and-scaffolding record pass, adversarial review round 1 (2026-10-08)

Branch `records/identity-scaffolding-syr` (PR #829), five commits ahead of origin/main (6d430d73 … 1babcf5c). Diff checked: `git diff origin/main...HEAD -- records/syr engine Build/worlds/syr records/worlds cic-website`. Reviewer: Opus 5.5. No model or API spend. No records edited.

**Verdict: CLEARED.** No substantial findings. Five findings below are not substantial; finding 1 asks for one line of tracking.

## Method

- Parsed the frontmatter of every changed record at origin/main and at HEAD and compared every field. Only `text` changed in each record, plus `positions[1]` in `syr.dw.doubt`. Sources, tensions, confidence, relations and use notes did not move.
- Compared the old and new `text` sentence by sentence for all changed witnesses (18 files, not 17; see finding 2).
- Compared every old and new markdown body for dropped source pointers and caveats.
- Ran `spoken_scaffolding.scaffolding_hits` over all of `records/syr`: no hits. Then scanned every spoken field of every syr witness, term, story, figure and honest limit for "?", "you"/"your", imperative openers, "You ask", "Asked …" and "your question", and read each hit in context.
- Quotes: no sentence inside quotation marks was edited. The quote-marked strings in touched sentences are "born again" (the participant's phrase) and 'deception' (in an unchanged sentence). The Adam sentence in `adam-grace` is unchanged; only the question before it was removed. Nothing to re-verify against `cic/texts/`.
- Pin: `sha256sum packages/syr/2026-10-08T06-51-34Z/manifest.json` = `bde50bf6…b37e2`, matching `records/worlds/syr.yaml`; `location` matches. The manifest's `records_commit` is 6d430d73, and no record changed after it.
- Site JSON: compiled from 70d4c80b (same records). The only content changes are the two cited witness texts (`authority-lived`, `doubt`), now matching the records.
- Waivers: `spoken-scaffolding/syr` removed from `engine/m1/cross_world.py`; `m1:voice-perspective/syr` removed from `engine/m9/enforce.py`. Nothing else changed in either file.
- `python3 tools/check_live_commentary.py --base origin/main --enforce`: exit 0.

## Record by record

| Record | Change | Fidelity |
|---|---|---|
| adam-grace | Opening question dropped; "Are people saved by faith alone? The sage answers with a picture." becomes "The sage taught faith with a picture." | Faithful. The record never says yes or no to "faith alone"; the new line claims neither. The picture's own answer (faith first, never left bare) is intact. |
| apostolic | "How did we know …? Our own answer was a story." merged into one statement | Faithful. |
| authority-lived | Opener and mid-text question turned to statements | Faithful; every path (bishop, vow, trust over time) is kept. |
| born-again-endtimes | "Were we born again …? We would recognize the words at once." becomes "We would recognize the words "born again" at once."; "Did we believe in something like the rapture? No." becomes "We did not believe in anything like the rapture." | Faithful. The no is the record's own. The Dem VI locus is carried unchanged and flagged. |
| corpus-and-its-edges | Opener and "Where is the record thinnest? Where it always is." become statements | Faithful. |
| cost-distance | "Did belonging cost anything? On the Persian side … it could cost everything." becomes one statement | Faithful; "could" is kept. |
| death-judgment | The outsider's two questions dropped; the closing now reads "As for the outsider's complaint that one way is too narrow, …" | No claim lost. The "everyone else goes to hell" question is still answered by "We drew far less of the modern map of who exactly burns than people assume." No yes or no is added. The "no judgment on the asker" caveat stays in `use_note.not_for`. |
| decides | "Who had the right to decide …? Our honest answer: it was still being worked out" becomes one statement | Faithful. |
| doubt | Opening question dropped; `positions[1]` "(why doesn't God stop this?)" becomes ", why God does not stop this" | Faithful. The debater's taunt is reported speech and stays. |
| failures | "Did we have failures?" becomes "We had failures."; "What did we do with our failures? Mostly, we did not see them as failures." becomes "Mostly, we did not see our failures as failures." | Valid: the record's next sentence, "Our own record shows some, and we will not hide them," is the yes. |
| god | Mid-text question becomes "Among ourselves we argued about exactly these things: …" | Faithful. |
| one-church | "Did we have denominations? Not as the word is now meant." and "How did the church handle them?" become statements | Faithful. |
| outsiders-empire | "Were these Christians hiding in catacombs? No - …" becomes "We were not hiding in catacombs - …"; "Did the empire change what the church was? Here the question turns strange and sharp." becomes "Here the story turns strange and sharp." | Faithful; see finding 4. |
| reading | "Did we read Genesis …? No. Not because …" becomes "We did not read Genesis … as science. That was not because …" | Faithful. |
| remains | Both questions become statements; the four "From …" fragments become four "They know …" sentences | Faithful. Only "at all" is lost, which carries no claim. |
| suffering | Opening question dropped; the closing sentence "That is where our God was: with the persecuted, as he was with his Son." moved to the front as "God was with the persecuted, as he was with his Son."; "We asked that question with blood in our mouths, and we left our answer." becomes "We gave that answer with blood in our mouths." | No claim dropped and none added. See finding 3 for a small shift. |
| unsettled | Both questions become statements ("Perhaps the hardest true thing about us is this: …") | Faithful; "Perhaps" is kept. "after our own time" is carried unchanged and flagged. |
| was-jesus-god | "Was Jesus God? We said yes, in our own way of speaking." becomes "Jesus is God, we said, in our own way of speaking." | Faithful. The identity witness opens with who. The yes is the record's own. |

Bodies: matrix-cell codes, "verified" narration and register boilerplate are gone. Every source and locus pointer and every caveat is kept: Dem XXII.1-2, VII.1, I, X, XVII.2, XXI.22; Sozomen II.9; the flood entry wording and the 201/202 era note; thin eucharistic detail; leaders' costs overrepresented; the Kayaalp bound; Doc_02 SS7 one-sidedness; the Beck authenticity caveat; no private-doubt account. Two bodies gain a short accurate caveat: `born-again-endtimes` (the Dem VI / Dem VII.20 locus is unsettled, matching the flagged defect) and `unsettled` (the synod-date mismatch with `decides`). Both state known record issues, not new claims.

Gap entry 23 quotes each new opener exactly as it stands in the records (checked string by string). It cites the record-defects entry and the voice-errors entry by subject and date. Its item numbers are items inside those cited entries, not bare entry numbers.

## Findings

### 1. Not substantial (outside this pass's types) — three honest limits open with "You ask", and a fourth opens with a second-person direction

The pass covers witness, term and story text. Honest-limit `statement` is not one of those types, and the checker does not scan it. But it is voice-diet text, and it carries the same defect class the pass removes:

- `syr.limit.f5-enslaved`: "You ask what it was to be enslaved among us."
- `syr.limit.f5-women-own-words`: "You ask what the women among us said of their own lives."
- `syr.limit.marriage`: "You ask what marriage meant to our people - our weddings, our homes."
- `syr.limit.ritual-sequence`: "We cannot walk you through our services step by step." (This one is milder: it states the absence first.)

None of these is recorded in `Build/worlds/syr/Open_Gaps_Tracking.md`. Action: add one line to entry 23, or open a new entry, naming these four records as open for a later honest-limit pass. No edit to them is required in this pull request.

### 2. Not substantial — record count in entry 23

The diff and entry 23's own list both name 18 records. Entry 23 says "Commentary removed from the markdown body of the 17 edited records". The brief also said 17. Change "17" to "18".

### 3. Not substantial — `suffering` second sentence shifts from question to answer

Old: "We asked that question with blood in our mouths, and we left our answer." New: "We gave that answer with blood in our mouths." The old line said the question was asked in suffering and an answer was left behind. The new line says the answer was given in suffering. Both are true of the record, and the roll-call that follows is the answer in either form. The reorder itself is clean: the closing sentence moved to the front, it is not repeated, and nothing after it changed. No fix needed.

### 4. Not substantial — `outsiders-empire` loses its signpost

"Here the story turns strange and sharp" no longer names what turns: whether the empire changed the church. The content that answers it (Constantine's conversion brought suspicion on the Persian church) is intact. An optional fix in the record's own words: "Here the empire's story turns strange and sharp." Not required.

### 5. Not substantial — participial "Asked …" scripting is left in three witnesses

These are not question forms and not second-person. They do still script a participant's question inside the text:

- `syr.dw.was-jesus-god`: "Asked about the Trinity, we answer from our font."
- `syr.dw.reading`: "Asked whether the Bible was the only authority, we would have found the question strange."
- `syr.dw.gospel-harmony` (not edited): "Asked how we knew the resurrection really happened, we answered …"

The voice-errors entry (staging reading, 2026-10-07) records the voice pasting a record's own scripted question. These three are a milder form of that. Leave them for this pass. Note them for whoever next touches these records.

## Not findings

- The `senses.translational` fields in `syr.term.catholicos`, `ewangeliyon-da-mhallete`, `qyama`, `raza-shrara` and `anti-jewish-polemic` open with a quoted modern question. `senses` is not a spoken field in `engine/m1/spoken_fields.py`, so it is out of scope.
- Questions in reported speech stay, as they should: the debater's taunt in `doubt`, and the famine exchange in `syr.story.ephrem-famine-death`. The Abgar letter's "you" in `syr.story.abgar-addai-legend` is also reported speech.
- Generic "you" ("marked you out" in `cost-distance`, "forbidden to shame you" in `penitence-prayer`, "your own name" in `syr.term.ihidaya`) is not a stage direction.
