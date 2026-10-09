# Syr voice claim corrections: adversarial review (2026-10-09)

Scope: branch `records/voice-claim-corrections-syr-2026-10-09` at d31744e0 (`git diff origin/main...HEAD`: commits 3593f282 and d31744e0). The branch corrects the records behind item (9) of "Voice errors found in the record pass staging reading, 9 October" (the voice said "Three times Shapur came against Nisibis while Jacob lived, and three times the city held"), repins the package and adds gap entry 25. I edited no record and made no model or API call. This is one review, Opus 5.5.

Mechanical checks, run on the branch:
- `python -m engine.m10.cli records syr`: PASS.
- `python -m engine.m10.cli regate syr --base origin/main`: PASS. Every note is a base failure, unchanged. Neither changed record appears in the notes.
- `python -m engine.m2.cli staleness-check`: exit 0, `"pass": true`; no world stale, `syr` included.
- `python -m engine.m2.cli determinism-check syr`: pass, no differing paths.
- `python tools/check_live_commentary.py --base origin/main --enforce`: exit 0. Only PROTECTED lines in `Open_Gaps_Tracking.md` are listed. Nothing is flagged in the two records or in `records/worlds/syr.yaml`.
- Package pin: `records/worlds/syr.yaml` pins `packages/syr/2026-10-08T23-41-36Z` with `manifest_hash: "sha256:49d5785cbcc8b945053da82b860066a30d1e9986a2a3939a99dce63eed6883d7"`. `sha256sum` of that `manifest.json` gives the same value, and entry 25 states the same path and hash. All 224 manifest entries hash correctly. `records_commit` and `built_by` are 3593f282, the commit of the last record edit; no `records/syr` file changes after it. The package's record files match `records/syr/` byte for byte (`diff -rq` gives no output).
- No quote record is touched. No `modern_rendering` and no quote text changed. `syr.contested.jacob-death-year` keeps `formation_confidence: Contested`.
- Entry 24 is untouched (the diff removes no line from `Open_Gaps_Tracking.md`). Entry 25 is appended, closes item (9) by subject and date, and leaves the other items of the 9 October entry OPEN.

## Verdict: REVISE (one line, targeted recheck only)

The two edits do what was ruled: no record now states a count of sieges or ties the sieges to Jacob's lifetime, and the new `not_for` names the voice's error directly. One new phrase is wrong, though. The rewritten `held_against` line makes the open question "which siege Jacob lived through". That assumes he lived through exactly one siege, which the same record's 350 pole contradicts. It also gives the candidate years a meaning no other record gives them. It is a one-line fix, plus the matching quotation in entry 25 and a rebuild and repin.

## Source verification

- Theodoret, Ecclesiastical History II.26 (`cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml`, chapter at line 11049). The chapter tells one siege: the seventy-day blockade, the Mygdonius dammed and loosed against the wall, Ephrem urging "the divine Jacobus" to mount the wall, and the gnats. It gives no year and no count of sieges. The damming of the river marks it as the 350 siege, so in this tradition Jacob is alive in 350. That point is still held: in the `sources` locus of `syr.contested.jacob-death-year` ("Jacob alive at the 350 siege in this tradition") and in `syr.source.theodoret-historia-ecclesiastica` `attribution_status`. The NPNF editor's note (line 4027-4035) says Theodoret confounds the 350 siege with that of 359, and that per Valesius "Volagesus, and not Jacobus, was bishop of Nisibis in 350". "Resists clean dating" is supported. The old "blends the city's three sieges" was not: the chapter and the note speak of 350 and 359, not of three sieges.
- Chronicle of Edessa (`cic/texts/chronicle-of-edessa_cowper.txt`, line 77): "17. In the year 649, died Mar Jacob, bishop of Nisibis." Year 649 of the Greeks is 337/338 CE. The unchanged `held_against` bullet and the `sources` locus are accurate.
- Chronicon Paschale: not vendored (the record already says "vendored-adjacent"). The 350 bullet is unchanged.
- Candidate years. `syr.story.jacob-deliverance` (`narrative_tier_justification`, `absent_detail`, `use_note.not_for`) and `syr.quote.theodoret-gnats` (`use_note.not_for`) give 338, 346 and 350 as candidate years for the one siege of the deliverance story ("even which siege it belongs to (338, 346, or 350) is unsettled"). The years match. What they are candidates for does not; see finding 1.

## Per-item checks

1. `syr.contested.jacob-death-year` `held_against[2]`. The count of three is gone, and nothing true is lost with it (above). See finding 1 for the new clause.
2. `syr.contested.jacob-death-year` `use_note.not_for`. Dropping "blended" is right, since the record no longer holds a blending claim. The added "a claim that all of the city's sieges fell in Jacob's lifetime" names the voice's error. It stays correct under both poles: it forbids the settled claim, not the 350 pole.
3. `syr.figure.jacob-of-nisibis` `dates.floruit`. "The city's remembered intercessor in the Persian siege tradition (which siege is open)" matches the story record and the `concedes` of the contested record ("the city's remembered intercessor"). It adds no claim. This field reaches the turn through `compiled/figures.json`, so the plural that invited a span of sieges was the right one to remove.
4. `syr.figure.jacob-of-nisibis` `dates.died`, left alone: "the Martyrologium Hieronymianum implies 338 (the first siege), the Chronicon Paschale has him defending Nisibis in 350". I judge that it does not invite the error. It gives no count and does not say Jacob lived through more than one siege. On the 338 pole it ties his death to the first siege only, which cuts against "three times while Jacob lived". The 350 clause is one pole, held open in the same sentence. No change is needed for this item. The Martyrologium is unvendored, so the parenthesis cannot be checked against a vendored text. That was so before this branch and is out of its scope.
5. Grep of `records/syr`, `canon/` and the compiled package (`prompt.txt`, `figures.json`, `repository.json`, `capsule.md`) for "sieges", "first siege", "three times" and "three sieges". The other hits do not tie the sieges to Jacob's lifetime or give a count: `syr.core.syriac` ("the Nisibis sieges", civic memory), `syr.source.kayaalp-nisibis-cathedral` (the baptistery is contemporary "with Jacob of Nisibis and the sieges"), `syr.source.ephrem-nisibene-hymns` (body), `syr.story.jacob-deliverance` (`retrieve_when`, tier justification), and `syr.contested.jacob-death-year` `claim` (the contested claim itself). `canon/` has no hit.
6. Entry 25. The "Changed" bullets match the diff word for word. The pin and hash are correct. "No record gives the number of sieges or ties them to his lifetime" is true after the branch. The "Not changed" reasoning on `dates.died` is sound (item 4). The gates it names were run and pass. It cites `determinism-check`, not `staleness-check`; both pass, so nothing it states is wrong.

## Findings

### 1. SUBSTANTIAL: the new `held_against` line misframes the open question
Old (`syr.contested.jacob-death-year` `held_against[2]`, this branch): "the siege's own hagiographic tradition (Theodoret) resists clean dating, and which siege Jacob lived through is itself open (338, 346 and 350 are candidate years), so neither pole can be waved through on narrative grounds alone"
"Which siege Jacob lived through" assumes he lived through one siege. The record's own 350 pole, two bullets up, has him bishop from c. 309 and alive in 350, which means he lived through every siege from 338 to 350. The line is wrong under that pole, and it gives the candidate years a meaning no other record gives them. In `syr.story.jacob-deliverance` and `syr.quote.theodoret-gnats` they are candidates for which siege the deliverance story belongs to, not for Jacob's lifetime. A record that is meant to hold the death year open should not frame his lifetime as a choice of one siege.
Fix: "the siege's own hagiographic tradition (Theodoret) resists clean dating, and even which siege its story belongs to is open (338, 346 and 350 are candidate years), so neither pole can be waved through on narrative grounds alone". This uses the story record's own framing and adds no claim. Make the same change in the first "Changed" bullet of entry 25, which quotes the line. Then rebuild the package and repin `records/worlds/syr.yaml` (default actions). A targeted recheck of this one line is enough; no other item needs another round.

## Recheck (finding 1 only, 2026-10-09)

Scope: commit 156d4d4b plus the working-tree repin, entry 25 Gates line and site JSON. Opus 5.5, targeted recheck.
- `syr.contested.jacob-death-year` `held_against[2]` now reads "the siege's own hagiographic tradition (Theodoret) resists clean dating, and even which siege its story belongs to is open (338, 346 and 350 are candidate years), so neither pole can be waved through on narrative grounds alone". This is the fix as asked. No other record text changed, and no record still says "Jacob lived through".
- Entry 25's first "Changed" bullet quotes the same words up to "candidate years)", the same span it quoted before.
- `records/worlds/syr.yaml` pins `packages/syr/2026-10-09T00-09-50Z` with `sha256:77c3d16828529203709145b8fdc165eeec41a6e005f0b89fcb2ef33c7c983497`. `sha256sum` of that `manifest.json` gives the same value, and entry 25 states the same path and hash. All 224 manifest entries hash correctly. `records_commit` is 156d4d4b, the last `records/syr` commit. The package records match `records/syr/` byte for byte.
- `python -m engine.m2.site_cli staleness-check`: `"pass": true`, no world stale. `python -m engine.m10.cli records syr`: PASS.

Verdict: APPROVED TO PROCEED. Finding 1 is resolved and nothing new was found.
