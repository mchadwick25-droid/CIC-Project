# Donatist identity-and-scaffolding pass: adversarial review, round 1 (2026-10-06)

Scope: branch `records/identity-scaffolding-don`, commit 08558b91, plus the uncommitted OG-25 entry. Diff checked: `git diff origin/main -- records/don Build/worlds/don/Open_Gaps_Tracking.md`. All 21 changed records were compared old against new, sentence by sentence, on the `text` field. No other frontmatter field changed in any record. No model or API call was made.

Mechanical checks run:
- `tools/check_live_commentary.py --surface records --base origin/main`: 0 hits.
- `engine.m1.gates.grade_text` via `engine/m7/turn_readability.score_turn` on old and new text: all 21 records pass FK <= 10 and FRE >= 60. `don.witness.refusal-and-recourse` moved from FK 10.5 (failing) to 9.3. Several records sit below the FK 8 floor. The floor is reported only and never fails.
- `packages/don/2026-10-06T21-47-09Z` exists.

## Verdict: REVISE

## Findings

### 1. SUBSTANTIAL: claim changed in `don.dw.what-belonging-cost`
Old: "What we cannot give you is the smaller ledger, and it is most of the one you asked about."
New: "What we cannot give you is the smaller ledger, and it is most of the whole cost."
The old sentence said the household ledger was most of what the participant asked about. The new one says household losses were most of the total cost of belonging. That is a quantitative claim no source supports. It also undercuts the paragraph's own point that this ledger went unrecorded.
Fix: "What we cannot give you is the smaller ledger: what belonging cost inside one family or one street." (Every element is drawn from the next three sentences.)

### 2. SUBSTANTIAL: answer dropped from `don.dw.washed-for-the-first-time`, and the first sentence no longer answers the question
Old: "Born again - yes, and we would fight you over the arithmetic. You say again. We say for the first time."
New: "Our baptism was a first one, never a second, and we would fight over the arithmetic. The other side says again. We say for the first time."
The retrieval trigger is "whether we were born again". The old opener answered it directly ("yes"). The new opener drops that answer and never uses the asked-about term, so ruling 1 (answer the question asked, in the kind it was asked) now fails. Shifting "You say again" to "The other side says again" is supported: the record's source locus is "the edicts naming the practice of washing again specifically". That part is acceptable.
Fix: "Yes, we were born again, and we would fight over the arithmetic. The other side says again. We say for the first time."

### 3. SUBSTANTIAL: orphaned references in `don.dw.hypocrites-and-those-who-left`
- P1 opens "It happened among us, and it is in the court record." The first "It" has no antecedent. It leans on the participant's turn (the trigger is a statement that their teachers were hypocrites), so it is dialogue scaffolding in a new form.
  Fix: "Teachers who turned out to be hypocrites were among us, and it is in the court record."
- P3 opens "Our own texts do not argue where God was when it happened to us." The removed question ("Where was God when it happened to us?") carried the topic, suffering. With it gone, "it" now reads back to P2, which is about leaving and being cut off.
  Fix: "Our own texts do not argue where God was when suffering came to us."

### 4. SUBSTANTIAL: second-person stage directions remain
The pass removed "You should know that" from `the-emperor-and-the-church` and listed "notice" as scaffolding. The same forms survive here:
- `don.dw.what-we-argued-among-ourselves` P5: "And note whose conscience our doctrine goes looking for. Not yours." Fix: "And our doctrine goes looking for someone else's conscience, not the believer's."
- `don.dw.written-by-our-opponents` P3: "... with no adversary choosing which words to keep - and note that the copy of it we can actually reach is the worst-damaged text in this whole corpus." Fix: "... with no adversary choosing which words to keep. But the copy of it we can actually reach is the worst-damaged text in this whole corpus."
- `don.dw.not-a-death-wish` P4: "That accusation is real and we cannot dismiss it - but you should know that almost everything specific about their conduct comes from people who needed them to look like a mob, ..." Fix: "... we cannot dismiss it. But almost everything specific about their conduct comes from people who needed them to look like a mob, ..."
- `don.dw.hypocrites-and-those-who-left` P3: "... to readers who were likely to be next - and you should hear it as that, and not as a teaching about suffering that we ever worked out." Fix: "... to readers who were likely to be next. It was never a teaching about suffering that we worked out."

### 5. SUBSTANTIAL: touched quote not verbatim in `don.witness.refusal-and-recourse`
The record has "What has the emperor to do with the church?" The vendored source, `cic/texts/optatus_against-the-donatists.txt` line 1904, reads 'What has the Emperor to do with the Church?' The words match, but the capitals do not. The pass moved this quote, so ruling 3 requires it to be verbatim. The project's own quote record (`don.quote.donatus-quid-est-imperatori`) and `don.dw.the-emperor-and-the-church` already capitalise both words.
Fix: "What has the Emperor to do with the Church?"
The attribution is sound: Donatus of Carthage, speaking to Paul and Macarius. "Our primate put it in one line" is fair to the source. The new opener, "The emperor has no standing to judge us.", is drawn from the record's own tensions field and adds nothing.

### 6. SUBSTANTIAL: OG-25 is inaccurate (`Build/worlds/don/Open_Gaps_Tracking.md`)
- "No claim, figure, name or detail was added or dropped" is false, given findings 1 and 2. The same entry also lists new identity content in the Jesus witness ("Son of the Father, one God with the Spirit, truly died and rose").
- "the wording matches, and the lower case is as the record had it" records a known deviation from the source as a pass (finding 5).
- "Status: CLOSED for the pass" self-certifies closure before this review came back. Under CLAUDE.md, a blocking finding cannot be dismissed by self-certification.
Fix: after the revisions, restate what moved, including the restored "yes" and the corrected ledger sentence. Record the capitalisation fix, and leave status OPEN until a round-2 recheck clears it. The entry is not yet committed, so editing it in place does not breach the append-only rule.
Accurate parts: the list of 21 records matches the diff. The story question forms (`don.story.gesta-apud-zenophilum`, `don.story.council-of-cirta`) are indeed transcript speech or reported questions, not scaffolding. No term record carries scaffolding (sweep confirmed). The package pin exists.

### 7. NOT SUBSTANTIAL: `don.dw.who-jesus-was-among-us` first sentence (item c)
"Christ, to us, was the Christ of the creed we shared with our opponents: the Son of the Father, one God with the Spirit, who truly died and rose."
It leads with who he was to this world, in the world's own framing, which is that the confession was shared. The creed content is covered by the record's `don.core.donatism` source ("standard North African Latin Trinitarian and Christological orthodoxy") and its first position. "Died and rose" is supported by the record's own text: "His death meant...", and in P4, "he stood, he was condemned, he was raised". Three small points:
- "Truly" is emphasis that no source carries.
- "The Son of the Father, one God with the Spirit" can be read as the Son being one God with the Spirit only.
- The sentence runs to 28 words, past the ~25-word line.
Suggested: "Christ, to us, was the Christ of the creed we shared with our opponents. He was the Son, one God with the Father and the Spirit, who died and was raised."
Also, the record's `use_note.not_for` sends creed claims to `the-creed-we-shared`, yet this text now states the creed. Flag only: frontmatter was outside this pass's scope.

### 8. NOT SUBSTANTIAL: `don.dw.the-creed-we-shared` and `don.dw.the-books-they-came-for` read naturally (item d)
Neither has an orphaned "the second", "your third" or "it/them" pointing at a removed question. In `the-books`, "They reached us" refers to the books named at the close of P1, and "him" in P3 refers to Christ in P1. In `the-creed`, P2 opens "Whether he died..." and the only antecedent is "Son" in P1. Suggested: "Whether Christ died to take our punishment...".

### 9. NOT SUBSTANTIAL: weak antecedent in `don.dw.two-churches-in-one-town`
P2: "A man came to hold it by both together: the people and the bishops." "It" points back four sentences to "authority".
Suggested: "A man came to hold that authority through the people and the bishops together."

### 10. NOT SUBSTANTIAL: question echo in `don.dw.walking-to-one-font`
P4: "Whether Christ would want anything to do with someone like you, at least, we can answer from our own doctrine, ..." This is not a stage direction, but the "at least" clause strains the syntax.
Suggested: "One thing we can answer from our own doctrine, because we thought it through to the bottom: whether Christ would want anything to do with someone like you."

### 11. NOT SUBSTANTIAL: in-world rhetoric, not scaffolding
`don.dw.the-test-we-took-from-the-text` P4: "Look at which of the two doors the soldiers are standing outside, and you have your answer." This is the world's own argument (the hated church is the true one). It does not manage the dialogue. Keep it.
`don.dw.becoming-one-of-us` "So: yes, you could come back." answers the question in its kind. Keep it.

### 12. NOT SUBSTANTIAL for this pass: the "heretics" sentence was carried unchanged (item e)
"Nobody in Africa called the other side heretics, because nobody could." (`who-jesus-was-among-us`), and "heretics on none" (`the-creed-we-shared`).
Carrying these is the right call for this pass. Ruling 3 forbids changing claims in a scaffolding pass. The defect is registered (OG-23 item 12, OPEN), and OG-25 names it explicitly. So the pass does not fail on it.
It is still a known-false sentence in two Tier-1 `ready` records. In `who-jesus` it now sits right after the new identity sentence, on the most-asked question. The build thread should take OG-23 item 12 next, ahead of other OG-23 items.

## Item (g): quote re-verification
Line 1904 of `cic/texts/optatus_against-the-donatists.txt`: 'What has the Emperor to do with the Church?' The words match. The capitals do not (finding 5).

## Oblique disagreement: no
The Donatist world is not oblique. Its own voice survives directly in the 411 Gesta, the passiones, the Sermo de passione, the Macrobius letter and Tyconius. The shared creed is a Widely Accepted finding the world can state outright. Leading with who is correct.
