# Witt identity-and-scaffolding pass: targeted recheck, round 2 (2026-10-08)

Scope: branch `records/identity-scaffolding-witt` at c9efcb2a, with `git diff origin/main...HEAD` and the fix commits since round 1 (`git diff ea94dc1e HEAD`). This is a targeted recheck, not a fresh review. I rechecked round 1 findings 1-4 (required) and 5-7 (recommended), the text the fixes introduced, and every statement in the new gap entry OG-61 in `Build/worlds/witt/Open_Gaps_Tracking.md`. I made no model or API call and edited no record. This is round 2 of the three-file cap.

Mechanical checks, run on the branch:
- `python -m engine.m9.cli check`: exit 0. The library access gate is clean: every finding is waived, and every waiver is live and current.
- `python -m engine.m10.cli records witt`: PASS.
- `python -m engine.m10.cli regate witt --base origin/main`: PASS. Its two notes are base failures on `witt.voice.craft`, unchanged.
- `python tools/check_live_commentary.py --base origin/main --enforce`: exit 0.
- `python -m engine.m2.site_cli staleness-check`: no world `stale: true`.
- Package pin: `records/worlds/witt.yaml` pins `packages/witt/2026-10-08T14-49-50Z` with `manifest_hash: "sha256:fa31a02a374cd59403f40efbb56865725f462d75f9444fbe4b938403930fbb24"`. `sha256sum` of that `manifest.json` is `fa31a02a374cd59403f40efbb56865725f462d75f9444fbe4b938403930fbb24`. They match, and OG-61 states the same pin and hash.
- Quotes re-read against the vendored files for every sentence the fixes touched: Augsburg Confession Art. II (lines 192-196) and Art. X (lines 320-324), Small Catechism Second Article (lines 198-205).

## Verdict: REVISE

The record fixes are sound. Every round 1 finding on the records is fixed as asked, and no fix adds a claim. One finding is substantial, and it is in the gap file, not a record: OG-61 says every quoted fragment in a touched sentence matches its source, and then lists one that does not. It also misquotes one of the carried defects. Both are one-line fixes to OG-61. A blocking finding needs independent re-confirmation, so the fix needs a round 3 recheck. That is the last file under the cap.

## Round 1 findings, rechecked

### R1-1. Stale readability waiver: FIXED
`engine/m9/enforce.py` now reads `"m1:readability/witt": Waiver(count=188, ...)`. `engine.m9.cli check` now exits 0.

### R1-2. Article X frame: FIXED
New: "Of the Supper, our confession says plainly that we "reject those that teach otherwise."" Source line 324, under "Article X: Of the Lord's Supper": "and they reject those that teach otherwise", where "they" is our own churches. The quoted span is verbatim, and the confession is now the one that rejects. See finding 4 for a small repetition the fix introduced.

### R1-3. Unsupported source pointer in `what-we-have-never-settled`: FIXED
`witt.contested.1543-treatise-later-effect` is gone from the Sources line. The line now names exactly the four contested records and `witt.core.witt` that frontmatter `sources` lists.

### R1-4. No gap entry: FIXED, with errors in the entry
OG-61 is appended and numbered. Its errors are findings 1, 2 and 3 below.

### R1-5. Three openers: FIXED
All three use the round 1 wording:
- `a-narrow-word-plainly-spoken`: "On who is condemned at the end, our confession states the claim plainly, ..."
- `nothing-against-scripture-or-the-church-catholic`: "We hold that our practices are not later inventions, but we do not argue it the way you might expect."
- `born-in-sin-fed-at-the-table`: "What you call transubstantiation is not how we speak of the bread and cup, ..."

### R1-6. Wording and antecedents: FIXED
- `cold-and-careless-among-us`: "Hypocrites among those who taught the faith: that happened among us, and we will not pretend it did not." And "his wife Katharina asked why ...". This is derivable. The record's source `witt.story.household-and-kate-on-prayer` quotes "Kate my wife", and the force locus names "Katharina von Bora's own question". "Our founder answered her plainly" now has its antecedent.
- `a-narrow-word-plainly-spoken`: the dash and colon sentence is now two sentences.
- `true-priests-of-gods-own-making`: "We have no outside account of how our people worshipped, not independently in our own hand." And "... of our worship in that outsider's own words."
- `one-holy-church-forever`: "From our own record, we cannot point you to a church of ours to visit today." This keeps the old claim and no longer doubts that such a church exists.

### R1-7. Verification disclosures: FIXED in 11 bodies, with gaps
The 11 bodies round 1 listed now end their Sources line with "Cited term, story and force records were not re-read for this record." See finding 3 for two bodies where the sentence names the wrong kinds of record, and one body it missed.

### R1-11. Two long sentences: FIXED, with one new frame problem
Both were split. The `truly-god-and-truly-man` split leaves a bare recitation. See finding 5.

## Findings

### 1. SUBSTANTIAL: OG-61 says every quoted fragment matches, then lists one that does not (`Build/worlds/witt/Open_Gaps_Tracking.md`, OG-61, "Quotes untouched")
Current: "Every quoted fragment in a touched sentence was re-checked against `cic/texts/melanchthon_augsburg-confession_anon-pg275.txt`, the Small and Large Catechisms and Luther's works, and matches."
The pass rewrote the sentence in `witt.dw.a-death-begun-that-a-child-receives` that quotes "until born again through Baptism and the Holy Ghost". It split it into "... names the remedy. It speaks of those brought to eternal death "until born again through Baptism and the Holy Ghost."" Source lines 195-196 read "... even now condemning and bringing eternal death upon those not born again through Baptism and the Holy Ghost." The quoted span does not match. OG-61's own carried-defect paragraph says so. The gap file is the audit trail, and CLAUDE.md treats "quotes verified" as a claim to re-check. A verification claim that the same entry contradicts can't stand in it.
Fix: "Every quoted fragment in a touched sentence was re-checked against `cic/texts/melanchthon_augsburg-confession_anon-pg275.txt`, the Small and Large Catechisms and Luther's works. All match except the carried "until born again" span in `witt.dw.a-death-begun-that-a-child-receives`, item (1) below."

### 2. NOT SUBSTANTIAL, should fix: OG-61 misquotes the `born-in-sin` carry-over (OG-61, "Known-wrong claims carried unchanged", item (1))
Current: "`witt.dw.a-death-begun-that-a-child-receives` and `witt.dw.born-in-sin-fed-at-the-table` say "until born again through Baptism and the Holy Ghost""
`born-in-sin-fed-at-the-table` does not say that. It paraphrases, without quote marks: "bringing death, until a person is born again through baptism and the Spirit." Only `a-death-begun` carries the quoted span. The defect in `born-in-sin` is the same "until" reading, as round 1 finding 9 said, but the entry should not put words in quote marks that the record does not hold.
Fix: "(1) `witt.dw.a-death-begun-that-a-child-receives` quotes "until born again through Baptism and the Holy Ghost", and `witt.dw.born-in-sin-fed-at-the-table` paraphrases the same reading ("until a person is born again through baptism and the Spirit"); the source reads ..." The rest of the item stays.

### 3. NOT SUBSTANTIAL, should fix: the disclosure sentence is missing from one body and names the wrong kinds of record in two; OG-61 overstates it
OG-61 says: "The note that cited term, story and force records were not re-read is kept in each body that cites them."
- `witt.dw.nothing-against-scripture-or-the-church-catholic` cites `witt.term.marriage` (frontmatter `sources`, `verification_state: verified-direct`). The base body said that record was "cited here as corroboration, not re-opened against the vendored file by this record". The pass removed that, and round 1 finding 7 missed it, so no sentence replaced it. The body now has no disclosure, and OG-61's "each body that cites them" is false for this record.
- `witt.dw.what-we-have-never-settled` cites four contested records and `witt.core.witt`, and no term, story or force record. Its new sentence ("Cited term, story and force records were not re-read") does not cover what it cites. The base said the contested records were "none re-opened against the vendored files or the secondary scholarship by this record". Frontmatter `verified-via-authority` still carries the gist, so nothing false remains.
- `witt.dw.the-household-we-can-describe` cites a story and `witt.core.witt`. Its sentence covers the story but not the core record. The base said both were "neither re-opened". This body is `verified-direct`.
- "kept" is also inexact. The pass removed the old disclosures and round 1 fixes added a new, shorter sentence.
Fix:
- In `nothing-against`, append to the Sources paragraph: "Cited term records were not re-read for this record."
- In `never-settled`, change it to "Cited contested-claim and world-core records were not re-read for this record."
- In `household`, change it to "Cited story and world-core records were not re-read for this record."
- In OG-61, change it to "Each body that cites another record without re-reading it now says so in one sentence after its Sources line."
This is body text, not spoken text, so it needs no readability or package check beyond the rebuild a record edit already triggers.

### 4. NOT SUBSTANTIAL, optional: "plainly" twice in two sentences (`witt.dw.one-holy-church-forever`)
Current: "We had a real boundary, plainly stated, with the cities who read the Lord's Supper differently than we did. Of the Supper, our confession says plainly that we "reject those that teach otherwise.""
The R1-2 fix added the second "plainly". Spoken aloud, it echoes. Fix: "Of the Supper, our confession says that we "reject those that teach otherwise."" The quoted span and its frame are unchanged.

### 5. NOT SUBSTANTIAL, should fix: the `truly-god` split leaves the creed recited as the Representative's own "I" (`witt.dw.truly-god-and-truly-man`)
Old (base): "Every household under our own catechism confessed each week that Jesus is God, in the same words: I believe that Jesus Christ is truly God, ..."
New: "Every household under our own catechism confessed each week that Jesus is God, in the same words. I believe that Jesus Christ is truly God, born of the Father in eternity, and also truly man, born of the Virgin Mary."
Round 1 asked for this split. Without the colon, the second sentence stands alone. Heard aloud, it is the Representative saying "I believe", in a voice that speaks as "we" everywhere else. The words are the Small Catechism's (lines 198-199: "I believe that Jesus Christ is truly God, born of the Father in eternity and also truly man, born of the Virgin Mary"). Nothing is invented, but the frame that marked them as the household's recited words is gone. The record does not put them in quote marks, and it adds a comma after "eternity", so adding quote marks alone would set an altered span inside them.
Fix: "Every household under our own catechism confessed each week that Jesus is God, in the same words. Each one said: I believe that Jesus Christ is truly God, born of the Father in eternity, and also truly man, born of the Virgin Mary." This restores the frame and keeps both sentences short. The world's quote handling is unchanged. The base text did not quote these words either.

### 6. NOT SUBSTANTIAL, optional: two OG-61 wording points
- "Each `text` now opens each paragraph with the answer" is broader than the pass. Some second paragraphs open on a lead-in, not an answer: `cold-and-careless` ("We must be careful here, and honest about the shape of what we actually hold"), `never-settled` ("Here is what we never settled."). None is a question or a stage direction, so `scaffolding_hits` is right to pass them. Fix: "Each `text` now opens on the answer, and no paragraph opens on a question."
- "One review file" will be out of date once this file lands. Fix: name both round files.

## OG-61 statements checked and found accurate
- Closes the 2026-10-06 entry by subject and date (OG-59). The `spoken-scaffolding/witt` waiver is removed from `engine/m1/cross_world.py`. With that waiver gone, `engine.m9.cli check` exits 0. So `check_spoken_scaffolding` finds no hit for witt.
- The 14 records listed are exactly the 14 `records/witt/doctrinal_witness/` files in the diff. The diff touches no term, story or figure record.
- Every quoted opener, and every quoted "Then" opener, matches the first sentence of its paragraph in the current `text`, character for character. This covers all 14 records.
- "The table question now names Katharina, whom the record's own locus names." True. The `witt.force.parishes-state-as-reported` locus names her.
- The Article X reframe is described correctly. The quoted words are unchanged, and the line is 324.
- Source wording in carried item (1), "condemning and bringing eternal death upon those not born again through Baptism and the Holy Ghost", is a verbatim sub-span of lines 195-196. The three build-thread carry-overs ("he rose again", "the very next line", "unanswered" for "unavenged", Large Catechism line 1956) match round 1 finding 9. Item (2), the poor-man "sharpest warning", and the citation of the 2026-10-04 slice-6 entry are correct.
- Commentary-removed list: the base bodies held "Closes F..." codes in all 12 cell-closing records (F1-E through F6-T), plus build-step and grep narration. All are gone, and the listed real limits remain.
- "Mark's focus rulings (decisions 56-58)" uses the same label as the sibling entries for don (OG-25) and cappadocian (OG-36).
- Gates, waiver 194 to 188, package path and hash: as stated. See the mechanical checks above.

## For round 3
Round 3 is the last file under the cap. It should recheck only these:
- finding 1, required
- findings 2, 3 and 5, recommended
- any text those fixes introduce

Findings 3 and 5 edit records. If they are applied, rebuild the package and repin `records/worlds/witt.yaml`, and update the pin and hash in OG-61. Then rerun `engine.m9.cli check`, regate, the records gate, the commentary check and staleness. Keep the edits to the exact wording given above. A new problem found at round 3 would escalate to Mark, not go to a fourth round.
