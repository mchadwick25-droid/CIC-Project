# Gallic identity-and-scaffolding pass: adversarial review, round 2 (2026-10-07)

Scope: a targeted recheck of round 1 (`gallic_identity_scaffolding_review_round1_2026-10-07.md`) against fix commit 2ea37d6f, on branch `records/identity-scaffolding-gallic`. Only the round 1 findings and the paragraphs the fix touched were checked. Bodies and frontmatter were compared with `origin/main`. No model or API call was made, and no record was edited.

Mechanical checks, run on the branch:
- `engine.m10.cli records gallic`: PASS.
- `engine.m10.cli regate gallic --base origin/main`: PASS. The only notes are base failures, unchanged.
- `engine.m2.site_cli staleness-check`: gallic `stale: false`, and no world is stale.
- `tools/check_live_commentary.py --base origin/main --enforce`: exit 0.
- Pin: `records/worlds/gallic.yaml` names `packages/gallic/2026-10-07T00-52-09Z`, with `manifest_hash` `sha256:57e2e0a9...6c715c`. That matches the sha256 of the package's `manifest.json`. The earlier package of this pass, `2026-10-07T00-25-25Z`, is gone, as OG-26 says.

## Verdict: REVISE

The record fixes are all correct. One required item is still open: OG-26 has two false statements, and the round 1 bar was an accurate log, sentence by sentence. The fix is to the log only. No record changes, and no rebuild or repin is needed.

## Findings

### 1. SUBSTANTIAL: two OG-26 statements are still inaccurate (`Build/worlds/gallic/Open_Gaps_Tracking.md`, OG-26)
- **"the 'for this record' wording in the loci headings of the three witnesses that had it."** On `origin/main`, all four witness bodies had "for this record" in their loci heading. That includes `laughed-at-and-reported` ("Loci read at their own lines for this record: Ep. II ..."). The fix restored it in all four.
  - Fix: "in the loci headings of all four witnesses".
- **"Removed from the bodies without restoring: ... the 'Reception/Node discipline held' paragraph."** This is wrong. Most of that paragraph is still in `the-christ-who-bears-the-wounds`, reworded:
  - "The hours, the guest as Christ and the grace sentences are named in the text as what Cassian handed on from Egypt or the fathers."
  - "The contested Conference XIII is used only for two sentences neither side of its argument disputes ..."

  The second of these is a contested-claim note. The log says it is gone, and the "Kept as genuine source notes" list does not name it. So a reader of the log would think a contested note had been deleted. What actually went: the two "discipline held" labels, the node sentence (Tours and Marseilles given by place, and no house knowing of the other), "and tensions[4] names the contest rather than resolving it", and "Reciprocal associated-with declared".
  - Fix: state exactly that, and add the reception and Conference XIII notes to the "Kept" list.

### 2. NOT SUBSTANTIAL: OG-26 wording, "loci notes"
"Left for the build thread" says "for this record" appears in "the loci notes of three witnesses". These strings are in `confidence.divergence_note` of `laughed-at-and-reported`, `one-person-two-substances` and `the-christ-who-bears-the-wounds`, not in loci. They are genuine verification apparatus, not a defect. Suggested wording: "'for this record' appears in the `divergence_note` of three witnesses (verification apparatus; stays)". You can fix this with finding 1 at no extra cost.

### 3. NOT SUBSTANTIAL: one more verification disclosure dropped and not logged (`gallic.dw.christ-in-the-beggar-and-the-guest` body)
On `origin/main`: "The cloak material is cited through gallic.story.the-cloak-at-amiens, verified at Doc_09." It now ends at "...the-cloak-at-amiens." This is the same kind of change as round 1 finding 6. No claim is added, but the record no longer says that the cloak locus was not re-read for this record. Its sibling in `the-christ-who-bears-the-wounds` now does say so. Optional, for consistency: "...cited through gallic.story.the-cloak-at-amiens and was not re-read for this record." If you take it, rebuild and repin. If not, name the deletion in OG-26's removed list.

## Round 1 items confirmed fixed
- **Finding 1** (`one-person-two-substances`): "We held there was no other way to speak of the Trinity." The subject is restored, and the sentence has no new claim and no orphaned pronoun.
- **Finding 2** (`laughed-at-and-reported`): "What an outsider found strangest, we can only tell from what was laughed at." The limit is restored, and "only" has its contrast again.
- **Finding 3**: both contested notes are restored, word for word as specified:
  - the Vincent note in `one-person-two-substances`, pointing to `gallic.contested.massilian-label` and `gallic.contested.who-holds-antiquity`;
  - the `election-as-capture` note in `laughed-at-and-reported`.
- **Finding 4**, apart from item 1 above, is fixed:
  - The record list matches the diff. That covers the four witnesses' `text` and bodies, plus the term's `quick_meaning`, its body, and one `divergence_note` sentence.
  - The false "Doc_01/Doc_06" claim is gone. The frontmatter strings are named correctly: "Tier 3", "Tier-3-shaped wonders", and "the approved prompt's own thin-domains paragraph".
  - The restored notes are logged.
  - The demo-record count is corrected (eight of nine). `power-against-dissent` is noted, and both second-person demo replies are named.
  - The known-wrong-claims line is accurate. The `progress-vs-alteration` misquote now cites Comm. 23, file line 13802.
  - "What moved" matches the final wording, including the old wounds text ("Who was Jesus to us? At Tours the answer is a story ... The Lord we knew was the crucified one").
- **Finding 5**: the term's `plain_meaning` is byte-identical to `origin/main`.
- **Finding 6**: three disclosures are restored:
  - "were not re-read for this record" in `the-christ-who-bears-the-wounds`;
  - "were not confirmed at a single line for this record" in `laughed-at-and-reported`;
  - the "for this record" heading in all four witnesses.
- **Finding 7**: "We never said that he died to take our punishment in our place." Same claim as before, now clear.
- **New sentences**:
  - "Yes, he would have." answers the would-he question in its own kind and adds nothing to the old "So, yes."
  - "At Tours this comes to us as a story." only fixes the weak "it" and adds no claim.
- **Touched paragraphs**: no new claim, orphaned pronoun, scaffolding or commentary was found in any of them.

## For round 3
Recheck OG-26 only, against finding 1 (and finding 3 if it is taken). This is the third review file on this pass. If round 3 does not clear, the cap applies.
