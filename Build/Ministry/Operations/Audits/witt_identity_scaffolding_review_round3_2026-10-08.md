# Witt identity-and-scaffolding pass: targeted recheck, round 3 (2026-10-08)

Scope: branch `records/identity-scaffolding-witt` at c274454f. I read `git diff origin/main...HEAD` and the round 2 fix commits (`git diff c9efcb2a HEAD`). This is a targeted recheck of round 2 finding 1 (required), findings 2, 3 and 5 (recommended), optional findings 4 and 6, and any text those fixes introduced. I made no model or API call and edited no record. This is round 3, the last file under the three-file cap. There is no round 4.

Mechanical checks, run on the branch:
- `python -m engine.m9.cli check`: exit 0. The library access gate is clean: every finding is waived, and every waiver is live and current. The readability waiver at 188 is still exact.
- `python -m engine.m10.cli records witt`: PASS.
- `python -m engine.m10.cli regate witt --base origin/main`: PASS. Its four notes are base failures, unchanged: three on `witt.voice.craft`, and one on `witt.term.we-are-all-priests` `quick_meaning`. The branch touches no term record.
- `python tools/check_live_commentary.py --base origin/main --enforce`: exit 0.
- `python -m engine.m2.site_cli staleness-check`: no world `stale: true`.
- Package pin: `records/worlds/witt.yaml` pins `packages/witt/2026-10-08T15-21-34Z` with `manifest_hash: "sha256:788a5fa5a9bdab9b3f91d70287479714ecbd7ae70e49b4b65e96a740277ad49d"`. `sha256sum` of that `manifest.json` is `788a5fa5a9bdab9b3f91d70287479714ecbd7ae70e49b4b65e96a740277ad49d`. They match, and OG-61 states the same path and hash. `packages/witt/2026-10-08T14-49-50Z` is gone, from disk and from the tree at HEAD. The package's `records/` matches `records/witt/` exactly (`diff -r`), so it was built after the last record edit. Its compiled chunks carry the new `truly-god` and `one-holy` sentences.

## Verdict: APPROVED TO PROCEED

Required finding 1 is fixed, and OG-61's verification claim is now true. Findings 2, 4 and 5 are fixed as asked. Finding 6 is fixed in substance. Finding 3 is fixed in the three records. Its OG-61 sentence is still not quite true for one body: see the new item below. That item is not substantial under round 2's own grading of finding 3, and nothing false stands in any record. Because there is no round 4, it goes to Mark rather than to another revision round.

## Round 2 findings, rechecked

### 1. OG-61 "Quotes untouched" claim: FIXED
New: "... and matches, with one exception: "until born again through Baptism and the Holy Ghost" in `witt.dw.a-death-begun-that-a-child-receives`, carried unchanged (below)." The wording differs from the round 2 text but says the same thing. The exception is real: the record says "until born again through Baptism and the Holy Ghost.", and the source (lines 195-196) reads "upon those not born again ...". No other record holds the quoted span. The claim and the carried-defect item now agree.

### 2. Misquoted carry-over: FIXED
New: "`witt.dw.born-in-sin-fed-at-the-table` paraphrases it as "until a person is born again through baptism and the Spirit"". The record's `text` holds that span word for word, without quote marks. The source wording in the same item is unchanged and verbatim.

### 3. Disclosure sentences: FIXED in the records; OG-61 sentence still overstates (see new item)
- `nothing-against-scripture-or-the-church-catholic`: "Cited term records were not re-read for this record." is appended. It covers `witt.term.marriage`.
- `what-we-have-never-settled`: "Cited contested-claim and world-core records were not re-read for this record." It covers what the record cites.
- `the-household-we-can-describe`: "Cited story and world-core records were not re-read for this record." It covers what the record cites.
- OG-61 now says: "Each body that cites term, story, force, contested-claim or world-core records carries the note that those records were not re-read for this record." This is not the round 2 wording, and it is false for one body. See the new item.

### 4. "plainly" twice: FIXED
New: "Of the Supper, our confession says that we "reject those that teach otherwise."" The quoted span and its frame are unchanged.

### 5. Creed recited as "I": FIXED
New: "Every household under our own catechism confessed each week that Jesus is God, in the same words. Each one said: I believe that Jesus Christ is truly God, born of the Father in eternity, and also truly man, born of the Virgin Mary." This is the exact wording asked for. The frame is back: the words are the household's recitation, not the Representative's own "I". They match the Small Catechism, lines 198-199, apart from the comma after "eternity" already noted in round 2. The new sentence is 24 words. The readability gate and waiver still pass.

### 6. OG-61 wording: FIXED in substance
- New: "Each `text` now opens with the answer where it opened on a question, and scripted mid-text questions are statements." This is narrower than the old claim and true of the pass.
- The entry now names all three round files, including this one.

## New item, for Mark (not substantial, not blocking)

### OG-61 says every body citing a story record carries the note; `a-confession-answered-not-a-vote` does not
`witt.dw.a-confession-answered-not-a-vote` cites `witt.story.diet-of-augsburg-1530` (frontmatter `sources`, `verification_state: verified-direct`). Its body has no not-re-read sentence. The base body said the record was "Built entirely from already-verified material", leaning on that story's own verification. The pass removed that. Round 1 finding 7 and round 2 finding 3 both missed this body. So OG-61's new sentence, "Each body that cites term, story, force, contested-claim or world-core records carries the note", is false for this one record.

Nothing false stands in the record. Round 1 re-checked the cited story material and it held (round 1 finding 9). This is the same class as round 2 finding 3, which was graded not substantial. It is reported to Mark, not to a fourth round. Two one-line options:
- (a) Recommended. Append to the record's Sources paragraph: "Cited story and source records were not re-read for this record." Then rebuild the package, repin, and update OG-61's pin and hash. This is body text, so it needs no readability check.
- (b) Leave the record. Change OG-61 to: "Each body that cites term, story, force, contested-claim or world-core records carries the note that those records were not re-read for this record, except `witt.dw.a-confession-answered-not-a-vote`, whose cited story was re-checked at review (round 1)." No rebuild is needed.

## Not flagged
Several bodies say "Cited term, story and force records" where they cite only term records (for example `scripture-judges-every-other-voice`, `born-in-sin-fed-at-the-table`, `truly-god-and-truly-man`). The sentence names more kinds than the body cites, but it does cover what it cites. Nothing false results.
