# cappadocian — identity-and-scaffolding record pass, adversarial review round 2 (2026-10-06)

Branch `records/identity-scaffolding-cappadocian`. Fix commits 49c37dd3 (records, OG-36) and e616293d (site JSON). Round 1: `cappadocian_identity_scaffolding_review_round1_2026-10-06.md`. Reviewer: Opus 5.5. This is a targeted recheck of the round 1 findings only. No model or API spend. No records edited.

**Verdict: CLEARED.**

## Method

- Read the new `text` of the 10 records touched in 49c37dd3 against the round 1 text and against `origin/main`: authority-and-spread, customs-from-the-apostles, macrina-and-its-cost, ordinary-day, power-and-its-discipline, psalms-teach-the-singer, want-to-believe, was-jesus-god, where-record-thinnest and who-was-jesus. Only `text` changed in each.
- Scanned the spoken `text` of all 21 edited witnesses for quotation marks, question marks and second-person phrases.
- Read OG-36 in `Build/worlds/cappadocian/Open_Gaps_Tracking.md` sentence by sentence and checked each claim against the records, the diffs and the gate runs.
- Re-ran these gates: `engine.m10.cli records cappadocian` PASS; `regate cappadocian --base origin/main` PASS (the one note is a pre-existing voice_craft FRE failure, unchanged from the base); `engine.m9.cli check` clean; `tools/check_live_commentary.py --base origin/main --enforce` exit 0; `engine.m2.cli staleness-check` and `engine.m2.site_cli staleness-check` both show cappadocian `stale: false`.

## Round 1 substantial findings

1. **Known-wrong claims in OG-36: fixed.** OG-36 names `stillness-and-the-summons`, with the Oration 2 / riverside-retreat blend. It names `macrina-and-its-cost`, with "own mother" and the two-bishops claim sourced to forty-sebaste. It cites OG-34 items 3 and 9 and OG-35 item 2. Both claims are still in the records unchanged ("her own mother tried to arrange"; "Two of her own brothers became some of our greatest bishops"; "riverbank"). The log says so correctly.
2. **OG-36 inaccuracies: fixed.**
   - (a) The macrina record now reads "Her authority had a cost. No see, no pulpit, was ever hers". The orphaned "The cost, told exactly" is gone, and OG-36 describes the new wording.
   - (b) The splitting sentence now says only subjects, verbs and connectives were added, and it lists the examples.
   - (c) `was-jesus-god` now reads "As for a personal Lord and Savior, that was not our own phrase". There are no quotation marks, as in the old text. This is not a question form, and the claim is unchanged. OG-36 says that "voted" in `confession-not-a-vote` is the only quoted string in edited text. The scan confirms this.
3. **Site JSON provenance: fixed.** `_generated_by` now names records_commit 49c37dd3. `git merge-base --is-ancestor` confirms it is an ancestor of HEAD. e616293d changes only that provenance string. Site staleness: not stale.
4. **Unlogged canon coverage gaps: fixed.** OG-36 now records the three items: F3-E "gospels that didn't make it in", F4-T tithe and end-times, and F6-T "hell for outsiders". It says the removed body notes were the only place they were recorded.
5. **`want-to-believe`: fixed.** The new text reads "For someone who wants to believe and cannot, our first word would not be to try harder." No antecedent is now missing, and it is the world's counsel again, not an absolute claim about the past.
6. **`psalms-teach-the-singer`: fixed.** The new text reads "For someone confused or bored by scripture, we would not counsel trying harder at reading. What worked for most of us was reception before analysis." The new claim about the past is gone.
7. **`customs-from-the-apostles`: fixed.** The new text reads "We held our unwritten practices to be apostolic because every church kept them, everywhere, not because of a documentary chain." This matches `positions`. "We knew" and "how widely" are gone. The rest of the text is unchanged; only the line wrapping moved.
8. **`where-record-thinnest`: fixed.** It now opens "Our own record is thinnest beyond one family and one circle of friends", and the text's own list follows. The one-voice rule stands as its own sentence. "Such a claim" is gone. The optional finding 14 rewording was also applied ("This record would not survive… It shows…"). It keeps the answer to the university-library question.
9. **`ordinary-day`: fixed.** The first sentence now answers the question ("An ordinary day… began before first light, when the house rose for fixed psalms."). The reconstruction disclosure is second. The rest is unchanged.
10. **`power-and-its-discipline`: fixed.** The six wrongdoing sentences moved to the front word for word. The power history follows unchanged and now ends at "do not have." Nothing is dropped or duplicated, and no sentence lost its antecedent.

Non-blocking items applied in the same commit: 11 (authority-and-spread: "so the story runs" now covers the seventeen-still-pagan clause) and 12 (who-was-jesus: "We did not mean equal to God; the gap between maker and creature never closed."). Both read correctly. Neither changes a claim.

## OG-36 and pin

- Every OG-36 sentence checked is accurate. That covers the list of records changed, what moved, the splitting, the identity witness, the other wording changes, the quotes, the oblique note, the known-wrong claims, the coverage gaps, the commentary removed, the build-thread items (poorhouse-famine-month, holy-spirit-honored), the nine `cappadocian.demo.*` records, the gates and the package. On the gates line: m9 is still clean at the 274 waiver, and both staleness checks are clean.
- Pin: `sha256sum packages/cappadocian/2026-10-06T23-00-29Z/manifest.json` = `2b06e1fc…f2a0ce`. This matches `records/worlds/cappadocian.yaml` `package.manifest_hash`, and `location` matches. The manifest `records_commit` is 412d4244, the parent of the records commit. That is the same practice as round 1.
- The site JSON records_commit (49c37dd3) is an ancestor of HEAD.

## New findings

None. No new claim, orphan, leftover scaffolding or commentary in the touched paragraphs. The remaining second-person uses in edited texts are disclosures ("We cannot show you", "reaches you through"), generic or scriptural "you", or the participant's quoted word. Round 1 passed all of these.
