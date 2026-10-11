# rzg — identity-and-scaffolding record pass, adversarial review round 1 (2026-10-08)

Branch `records/identity-scaffolding-rzg` (PR #828; commits d4e910b0, 0991302c, 537db614, fe21a17f), diff `git diff origin/main...HEAD -- records/rzg engine Build/worlds/rzg records/worlds packages`. Reviewer: Opus 5.5. Full review. No model or API spend. No records edited.

**Verdict: REVISE** (one substantial finding, a one-record fix).

## Method

- Compared old and new `text` (`git show origin/main:<path>`, word diff) for all 10 changed records, sentence by sentence. Only `text` and the markdown body changed in each file; sources, positions, tensions, confidence, retrieval and use notes are untouched.
- Read each record's `retrieval.retrieve_when` and `use_note.means` to check the opener answers the kind of question asked.
- Scanned every spoken field (`text`, `plain_meaning`, `quick_meaning`, `tellable_as`, `modern_contrast`, `absent_detail`, `prior_sense`, `retelling`, `modern_rendering`, nested included) in every rzg witness, term, story and quote for "?", "you ask", "your (second) question", "you wonder", "you asked", "walk in", "imagine", "picture", "start with", "you might", "consider". Remaining hits: Zwingli's reported last words (`not-a-death-he-sought`, `myconius-account-of-zwinglis-death`, `zwinglis-last-words`), which are reported speech and must stay; "A modern reader may picture" in `first-zurich-disputation.modern_contrast`, which is not a direction; and one embedded question in `a-narrow-true-church` (finding 2).
- Quotes: the Second Helvetic Confession lines (ch. X, lines 667, 684-685 of `cic/texts/schaff_second-helvetic-confession-heidelberg-catechism_1919.txt`) appear only in unchanged context lines of the diff; the quoted sentences in `a-quieted-mind` and `one-thing-not-in-dispute` are byte-identical to main. Zwingli's last words in `not-a-death-he-sought` match `rzg.quote.zwinglis-last-words` and were not touched.
- Bodies: read all 10 new bodies in full against main.
- Gates re-run: `engine.m10.cli records rzg` PASS; `engine.m9.cli check` "clean - every finding is waived, every waiver is live and current", so the rzg readability waiver at 131 matches this run; `tools/check_live_commentary.py --base origin/main --enforce` exit 0 (records: 0 hits).
- Pin: `sha256sum packages/rzg/2026-10-08T06-20-21Z/manifest.json` = `aed8c87c…f52a79`, matching `records/worlds/rzg.yaml` `package.manifest_hash`; `location` matches. Manifest `records_commit` is d4e910b0, the records commit on this branch.
- Waiver: `spoken-scaffolding/rzg` removed from `engine/m1/cross_world.py`; the m9 readability waiver 134 → 131 is the only other engine change.

## Findings

### 1. SUBSTANTIAL — `rzg.witness.a-narrow-true-church` opens on the participant's charge, not on the answer

New opener: "The charge is that we were too narrow, one way among every way people have ever reached for God. We will not answer that more gently than it deserves."

The old question ("Too-narrow, one way among every way people have ever reached for God?") has become a declarative echo of it. The first sentence restates the challenge; the second states a stance. The answer itself ("We held the alternatives we refused to be wrong, not merely different") only arrives in sentence three. That is the same scaffolding the pass exists to remove: the participant hears their own charge read back before the world answers. `retrieve_when` (a direct challenge as too narrow) and `use_note.means` ("We held the Roman, Wittenberg, and Anabaptist positions we refused to be wrong by Scripture's test, not merely different") both point to the answer sentence as the opener.

Fix (reorder the record's own sentences; nothing added or dropped): replace the first three sentences of `text` with

"We held the alternatives we refused to be wrong, not merely different. The charge is that this made us too narrow, one way among every way people have ever reached for God. We will not answer it more gently than it deserves."

The rest of `text` ("Rome''s own repeated sacrifice and its images: refused. ...") follows unchanged. Update the opener quoted for this record in the gap entry (Identity-and-scaffolding record pass, 2026-10-08) to match.

### 2. Not substantial — embedded question left in the same record

`a-narrow-true-church` still has "Each time, the same test: does this reading hold against Scripture?" It states the content of the test, not a question put to the participant, so it is not scaffolding. But the pass removed the identical construction from `calvins-journey-to-zurich` ("a quiet worry ...: did Calvin's own teaching ... agree ...?"). For consistency, while the record is open for finding 1: "Each time, the test was the same: whether this reading held against Scripture."

### 3. Not substantial — the other nine openers are faithful

- `a-quieted-mind`, `not-a-death-he-sought`, `one-supper-two-poles`, `what-a-stranger-would-notice`, `what-we-have-of-christ`, `why-the-children-too`: each opener is the record's own former first answer with the question folded in. No claim added; "so it was no death wish dressed up as faithfulness" states only what the text already concludes ("not a longing for the risk").
- `one-thing-not-in-dispute` (identity witness): "To us Jesus is what the whole church says he is" opens with who, and says no more than the old "we say what the whole church says". The tense moves from "was" to "is"; this matches `use_note.means` ("We share the church's inherited teaching") and changes no claim. It adds no creedal content, which matters given the voice-error entry (Voice errors found in the staging reading of the voice hand-off, 2026-10-07), item 2.
- `what-we-have-not-agreed`: the splits and the joints "The first is" / "The second is" keep every claim in order. "We have never agreed it between our own two cities" is idiomatic British usage; "agreed on it" would read more easily for a non-native speaker. Optional.
- `why-the-children-too`: "It is not a smaller church" correctly takes the whole believing city as its subject.

### 4. Not substantial — the Calvin story edit does not change the claim

Old: "a quiet worry had spread ...: did Calvin's own teaching on the Supper actually agree with what Zurich taught?" New: "...: that Calvin's own teaching on the Supper might not agree with what Zurich taught." A worry over whether two teachings agree is a worry that they might not. The worry stays with "people who respected both our own churches". Dropping "actually" loses only emphasis; the next sentence ("an appearance of disagreement") carries the same contrast. The edit neither fixes nor worsens the known defect (the worry given to Calvin, "a letter would not settle it", against Calvin's "we agree in judgment"). That defect is correctly carried unchanged and flagged.

### 5. Not substantial — bodies

All source and line pointers and record cross-references are kept (`triple-refusal`, `anabaptist-schism-legitimacy`, `christ-the-mirror-of-election` with its locus, the Myconius loci, Doc_04 §3.5 / Doc_07 §2D/§2I, `signs-and-things-signified`, Doc_07 §2G with its Inferential-Thin caveat, the T1/T2 gravities, `sola-scriptura` lines 4487-4492, the Story-Chunk source pointer). Removed material is process: cell codes, "Closes ...", "already-cleared", "after this script runs", "Approved to proceed", don comparisons. The removed sentence in `one-supper-two-poles` about T2's existing gravity and contested-claim records named no record and recorded no gap. The coverage notes ("... are not claimed") stay in the bodies, so nothing is lost; no record body still carries commentary.

### 6. Not substantial — gap entry (Identity-and-scaffolding record pass, 2026-10-08)

Checked against the files: every quoted opener is exact (line folds read as spaces). Cross-references use subject + date. Both known-wrong claims touching edited records are flagged for Mark: the nine-defects entry (2026-10-04) item 7 for the Calvin story, and the two-defects entry (2026-10-04) item (a) for the Article XVIII line span in `one-supper-two-poles`. No other item in those entries touches an edited record. The gates, waiver removal, waiver count and package pin it reports are what this review found. It says the story change was a mid-text scripted question, which correctly explains why the count is 10 against the 9 the checker found.

Two optional additions, neither required: (a) the third note in the two-defects entry (the Consensus Tigurinus source dated "1549/1554" while witnesses say 1549) also touches `one-supper-two-poles` and `what-we-have-not-agreed`; it is an open question, not a known-wrong claim, but could be named. (b) After finding 1 is fixed, the entry's opener quote for `a-narrow-true-church` must be updated (see finding 1).

## Round 2

A targeted recheck: finding 1 (and finding 2 if taken), the matching gap-entry quote, the rebuilt package pin and manifest hash, and the m9 readability count after the reorder.
