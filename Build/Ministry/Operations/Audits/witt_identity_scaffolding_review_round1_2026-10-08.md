# Witt identity-and-scaffolding pass: adversarial review, round 1 (2026-10-08)

Scope: branch `records/identity-scaffolding-witt`, commit ea94dc1e, diffed with `git diff origin/main...HEAD`. I compared all 14 edited `records/witt/doctrinal_witness/*.md` files old against new, sentence by sentence: every `text`, and every edited markdown body. I also checked `positions` and `tensions` in those 14 files, and the removal of the `spoken-scaffolding/witt` waiver from `engine/m1/cross_world.py`. I made no model or API call and edited no record.

Mechanical checks, all run on the branch:
- `python -m engine.m10.cli records witt`: PASS.
- `python -m engine.m10.cli regate witt --base origin/main`: PASS. Every note is a base failure, unchanged.
- `python tools/check_live_commentary.py --base origin/main --enforce`: exit 0, 0 hits.
- `python -m engine.m2.site_cli staleness-check`: witt `stale: false`.
- `python -m engine.m9.cli check`: **exit 1 on the branch, exit 0 on origin/main** (run in a clean worktree of c5b195bf). The one problem: "m1:readability/witt: waiver says 194, this run found 188 - the waiver is stale - tighten it". See finding 1.
- Quotations: I checked every quoted fragment in the touched sentences against the vendored files. These were the Augsburg Confession (`cic/texts/melanchthon_augsburg-confession_anon-pg275.txt`), the Small Catechism (`luther_small-catechism_smith1994.txt`), the Large Catechism (`luther_large-catechism_bente-dau1921.txt`) and Luther's works v1 and v2. Results are in finding 9.
- My own sweep of every witness, term, story and figure spoken field in `records/witt/` for `?`, "You ask", "your question", "you wonder", "Walk in", "Listen" and second person. Results are in finding 8.

## Verdict: REVISE

Findings 1-4 are substantial, and each needs only a small fix. The scaffolding work itself is sound. Every question opener is gone. No yes/no was added that the old text did not give. No quoted span was altered or reordered. The world's own imagery survived.

## Findings

### 1. SUBSTANTIAL: the m9 gate fails on the branch, because the witt readability waiver is now stale (`engine/m9/enforce.py`)
The pass cut witt's readability failures from 194 to 188, but did not tighten the waiver. `engine.m9.cli check` therefore exits 1 on the branch and 0 on the base. CLAUDE.md says a stale waiver fails the run. CI will fail.
Fix: in `engine/m9/enforce.py`, change `"m1:readability/witt": Waiver(count=194, ...)` to `count=188`. Rerun `engine.m9.cli check` until it exits 0.

### 2. SUBSTANTIAL: the rewritten Article X sentence inverts who rejects whom (`witt.dw.one-holy-church-forever`)
Old: "We had a real boundary, plainly stated, with the cities who read the Lord's Supper differently than we did -- what our confession calls those who "reject those that teach otherwise.""
New: "We had a real boundary, plainly stated, with the cities who read the Lord's Supper differently than we did. Our confession calls them those who "reject those that teach otherwise.""
Source, Augsburg Confession Art. X, line 324: "... and they reject those that teach otherwise." In the source, "they" is our own churches. The confession does the rejecting. The quoted words are verbatim, but the new sentence makes "them" (the rival cities) the ones who "reject". The old frame was already garbled. The rewrite turns it into a plain, standalone claim that misreads the source. This is a quotation set in a false frame, inside a sentence this pass rewrote. Neither version is listed in `Build/worlds/witt/Open_Gaps_Tracking.md`.
Fix: "Of the Supper, our confession says plainly that we "reject those that teach otherwise."" The quoted span stays verbatim, and the claim now matches line 324.

### 3. SUBSTANTIAL: a source pointer added to a body that the record does not cite (`witt.dw.what-we-have-never-settled`)
New body: "Sources: witt.contested.household-catechism-reception, witt.contested.justification-accounted-and-made, witt.contested.two-governments-historical-scope, witt.contested.theses-door-posting, witt.contested.1543-treatise-later-effect, and witt.core.witt's thinness and cautions fields."
The frontmatter `sources` lists four contested records and `witt.core.witt`. It does not list `witt.contested.1543-treatise-later-effect`. The old body named "four already-built contested_claim records" and never named that one. `use_note.not_for` also says "any of the four contested questions". So the new line adds a source that the record does not rest on. That record covers the treatise's reception in the 18th to 20th centuries, after the window closes. Its use-note status is still undecided, per "Record defects found while drafting and reviewing use notes (slice 6), 2026-10-04", item 11. The pass rule was "nothing added".
Fix: remove "witt.contested.1543-treatise-later-effect, " from the Sources line. ("cautions" is fine. The old body named `.cautions`.)

### 4. SUBSTANTIAL: no Open_Gaps entry records the pass or the closed waiver (`Build/worlds/witt/Open_Gaps_Tracking.md`)
The branch does not touch `Open_Gaps_Tracking.md`. The entry "Spoken text opens on a question or carries a stage direction, 2026-10-06" says the record pass removes the `spoken-scaffolding/witt` waiver. Nothing records that the pass ran, which records moved, what body commentary was removed, or that the readability count went from 194 to 188. CLAUDE.md requires every review outcome and closure to be in the world's gap file. The gallic pass logged the same work in its OG-26 entry.
Fix: append a new numbered entry, the 2026-10-08 witt identity-and-scaffolding record pass. It should list:
- the 14 records
- the waiver removed
- the readability waiver tightened to 188 (finding 1)
- what moved in each `text`, one line per record
- the body commentary removed
- carried, unfixed: the two known defects (see "Known carry-overs" below), the Article X frame (finding 2) if it is not fixed here, and the leftover items in finding 8.

### 5. NOT SUBSTANTIAL, should fix: three openers that hide or blur the answer
- `witt.dw.a-narrow-word-plainly-spoken`. Old: "Did we believe outsiders were going to hell? Our confession states the claim plainly ..." New: "On the judgment, our confession states the claim plainly ..." The question carried the subject, outsiders and hell. Now no sentence names it, so a retrieved turn reads as off-topic for its first `retrieve_when` line. No yes/no is needed, and the old text gave none. Fix: "On who is condemned at the end, our confession states the claim plainly, and we will not soften it for you."
- `witt.dw.nothing-against-scripture-or-the-church-catholic`. New: "We do not argue that our practices go back to the apostles the way you might expect." Heard aloud, "We do not argue that our practices go back to the apostles" sounds like a denial of the continuity claim this record makes (`positions[0]`). Only the tail rescues it. Fix: "We hold that our practices are not later inventions, but we do not argue it the way you might expect." This adds nothing. The old question ("How do we know our practices went back to the apostles ...") already carried that claim.
- `witt.dw.born-in-sin-fed-at-the-table`. New: "The bread and cup are not what you call transubstantiation, and we are careful about the difference." This is a category slip, because bread is not a doctrine. It also leads with what the bread is not, not with what it was to us. Fix: "What you call transubstantiation is not how we speak of the bread and cup, and we are careful about the difference."

### 6. NOT SUBSTANTIAL, should fix: wording and antecedents
- `witt.dw.cold-and-careless-among-us`. New: "We will not pretend that the people who taught the faith were never hypocrites among us." This double negative is hard to parse when heard. Fix: "Hypocrites among those who taught the faith: that happened among us, and we will not pretend it did not." The same record has "At our founder's own table, someone asked ... Our founder answered her plainly". "Her" has no antecedent. The old text had the same gap ("a question asked once ... answered her"). The new "someone" makes the mismatch plain to hear. The record's own source locus names her ("Katharina von Bora's own question about coldness in prayer"). Fix: "At our founder's own table, his wife Katharina asked why ...".
- `witt.dw.a-narrow-word-plainly-spoken`. New: "By our own account, Christianity was narrow in the sense you mean -- one way, out of every way people follow: we did not hold that many paths led to the same place." That is a dash, then a colon, in one 33-word sentence. Fix: "By our own account, Christianity was narrow in the sense you mean. We did not hold that many paths led to the same place." Dropping "too" from the old "too narrow ... yes" is acceptable. "In the sense you mean" already qualified it.
- `witt.dw.true-priests-of-gods-own-making`. New: "We must be honest about the clearest outside account we have of how our people worshipped: we do not have one ..." This names "the clearest account we have" and then says we have none. Fix: "We have no outside account of how our people worshipped, not independently in our own hand." The same record also changed "We cannot give you an outsider's own account of our worship the way this question actually asks for one" to "... of our worship." This hardens the claim slightly, because the sentence before it says Rome's reply comes closest at one remove. Fix: "... of our worship in that outsider's own words."
- `witt.dw.one-holy-church-forever`. Old: "A church today you could visit that's ours -- we cannot answer that from our own record". New: "We cannot say, from our own record, whether a church of ours exists today that you could visit." The new wording doubts that any such church exists. The old only declined to point to one. That widens the conflict with the deployed Living Traditions paragraph, which says a confessional family still teaches today. The conflict is already tracked in "Round 4 targeted recheck ... 2026-09-28", item 4. Fix, keeping the old claim: "From our own record, we cannot point you to a church of ours to visit today."

### 7. NOT SUBSTANTIAL: verification disclosures removed from bodies
Several bodies said that cited term, story or force records were "verified-via-authority ... not re-opened against the vendored files by this record". The new bodies drop this:
- `a-death-begun` (`witt.term.baptism`)
- `born-in-sin` (three terms, including the "monstrous word" source)
- `how-the-promise` (two terms)
- `one-holy-church` (the force)
- `household` (story, core)
- `poor-man` (`witt.term.marriage`)
- `true-priests` (story, term)
- `truly-god` (`christ-alone`, `justification`)
- `cold-and-careless`, `scripture-judges`, `never-settled` (whole record)

Three of these records are `verified-via-authority` in frontmatter, which keeps the disclosure. The others are `verified-direct`. For those, the body was the only place that said some cited material had not been re-read. I re-checked that material myself, and it holds (finding 9), so nothing false is left. This matches gallic round 1 finding 6. Fix (recommended): after each Sources line, add "Cited term and story records were not re-read for this record."

### 8. NOT SUBSTANTIAL: leftover scaffolding sweep (item 4, item 6)
- No `?` remains in any witness `text`, `positions` or `tensions`. "You ask", "your question", "you wonder" and "Walk in" are gone from every in-scope field. "Listen" appears once, in `witt.term.christ-alone` `plain_meaning` ("We do not listen to saints or scholars"). That is content, not a direction. "But listen to what the same confession says" was correctly removed from `truly-god-and-truly-man`.
- Questions left in story `text` are all quoted or reported source speech, so they stay:
  - Cajetan's three questions in `augsburg-before-cajetan`
  - Katharina's question in `household-and-kate-on-prayer`
  - Luther's prayers in `prayer-for-rain-1532`
  - "have you not grievously failed?" and "why should you not be able to repeat ..." in `return-and-the-eight-sermons`
- `positions` and `tensions` hold no question forms. Their second person ("we cannot tell you whether ...", "'rapture,' in the shape you mean it") states a limit. It does not direct the participant.
- The second person left in the witnesses ("the way you may be picturing", "we will not soften it for you", "We can show you", "You have likely heard ...") is address, not stage direction. Acceptable.
- One borderline case: in `witt.dw.the-poor-man-at-the-door`, "A poor man may come to your door ... If you treat him with contempt ...". This is the Large Catechism's own "you" (line 1946: "When the poor man comes to you ..."), in paraphrase, and it was in the base. Spoken to a participant, it can sound like an accusation. Optional: "Our own book warns the household: when a poor man comes to your door ...".
- `witt.dw.scripture-judges-every-other-voice`. Old: "If we are all priests, he asked, why should we not test and judge ...?" New: "If we are all priests, he said, then we may test and judge ...". This was Luther's own rhetorical question, reported (Christian Nobility, via `witt.term.scripture-against-tradition`). It was not scripted scaffolding. The claim is unchanged, but the world's own argument lost its shape. Optional: restore the question. It sits mid-paragraph, not first, so the scaffolding check is not affected.

### 9. NOT SUBSTANTIAL: quotations (item 2)
No quoted span was altered or reordered. All were rewrapped only. Checked against the vendored files:
- "born with sin": AC line 193. Verbatim.
- "tithes": AC line 1354. It is the only hit in the file, so "names "tithes" exactly once" holds.
- "reject those that teach otherwise": AC line 324. The words are verbatim; the frame is wrong (finding 2).
- "my Lord" / "our Lord": Small Catechism lines 189 and 199.
- Unquoted paraphrases that match their sources: "monstrous word for a monstrous idea" (v2 7104-7105), "forgotten in the dust under the bench" (v1 269), "I did nothing; the Word did it all" (v2 14931), "most common and noblest estate ... humble themselves" (LC 1713-1715), "take our own reason captive" (v2 7186), the Article XXIII marriage lines (AC 730, 733), and Article XVII (AC 435-446).
- Base carry-overs, untouched by this pass and unquoted, for the build thread:
  - `how-the-promise-reached-us` recites "on the third day he rose again", but the source has "rose again" with no "he".
  - `truly-god-and-truly-man` says "I am his very own" comes "in the very next line" after "He is my Lord!", but it is three lines later.
  - `the-poor-man-at-the-door` says the cry "will not go unanswered", but the source says "unavenged" (line 1956). This is a softening.
  - `born-in-sin-fed-at-the-table` paraphrases Art. II with the same "until ... born again" as the known `a-death-begun` defect.

### 10. NOT SUBSTANTIAL: body commentary removed (item 3)
The following are all correctly gone: the matrix-cell codes ("Closes F1-E ...", "C-T", "F6-I"), the B-step history, "Reciprocal associated-with declared", the grep narration, and "no relations[] declared accordingly". These real caveats and pointers were kept:
- the tithing limit
- the divorce decline
- the Marburg and post-1580 limits
- the parishes-force bar on citing it as evidence of ignorance
- the one-locus poverty caveat
- the one-remove Confutation note
- the Article XXIII paraphrase note, with its line numbers
- the pre-1517 council boundary
- the 1525/1543 existence-only limit
- source file and line pointers in every body that had them

The `household` body drops "Inferential-Thin" but keeps "Tier 4". Frontmatter `formation_confidence: Inferential-Thin` still holds the tag. `truly-god-and-truly-man` adds a cross-reference to `witt.dw.how-the-promise-reached-us`. It is accurate (that record's own body names `truly-god`). It drops the C-P distinction from `witt.term.christ-alone`. Both are acceptable.

### 11. NOT SUBSTANTIAL: voice and readability (items 5 and 7)
The world's own imagery survived intact:
- the Word "forgotten in the dust under the bench"
- the donkey intoning the lessons
- "ice-cold and negligent"
- the old self drowned daily
- "a monstrous word for a monstrous idea"
- good works following "the way fruit follows a living tree"
- "beware, as of the devil himself"
- "true priests of God's own making"

Splitting long sentences mostly helped (`a-confession`, `nothing-against`, `household`, `never-settled`). The texts still lean on honesty-announcements ("We must be honest", "we will not pretend", "we do not pretend"). This tic was in the base and was not made worse. Several sentences still run past about 25 words. Most were untouched. Two this pass created or lengthened are worth splitting:
- the `truly-god` opener (40 words): split after "in the same words".
- the `a-death-begun` "born with sin" sentence (45 words).

## Known carry-overs, confirmed present in the base and not counted against this pass
- `witt.dw.a-death-begun-that-a-child-receives` quotes "until born again through Baptism and the Holy Ghost". The source, AC lines 195-196, reads "... bringing eternal death upon those not born again through Baptism and the Holy Ghost". The quoted span is identical in origin/main and on the branch. It is listed in `Build/worlds/witt/Open_Gaps_Tracking.md` under "Record defects found while drafting and reviewing use notes (slice 6), 2026-10-04", item (2).
- `witt.dw.the-poor-man-at-the-door` says "the sharpest warning this household book gives anywhere", in `text` and `positions[2]`. Its own `tensions[1]` and `use_note.not_for` say only one locus was searched. The wording is identical in the base. It is listed in the same 2026-10-04 entry, item (3). The related `witt.quote.the-poor-man-who-comes-to-you` claim is item (4).
- That same entry also covers two items these bodies still carry, unchanged in substance: item (5), `true-priests` naming the Confutation record, and item (6), `a-confession` saying it is built on the Confutation and Apology records.

## For round 2
Recheck findings 1-4 (required) and 5-6 (recommended) only. After the edits, rerun `engine.m9.cli check`, regate, the records gate and the commentary check.
