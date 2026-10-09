# Witt voice claim corrections: adversarial review (2026-10-09)

Scope: branch `records/voice-claim-corrections-witt-2026-10-09` at 05c5a112 (`git diff origin/main...HEAD`, one commit on 8d7e0edc). The branch corrects items (10) and (12) of "Voice errors found in the record pass staging reading, 9 October" (OG-63), rebuilds and repins the `witt` package, adds OG-64 and tightens one engine waiver. I edited no record and made no model or API call. This is one review, Opus 5.5.

Mechanical checks, run on the branch:
- `python -m engine.m10.cli records witt`: PASS.
- `python -m engine.m10.cli regate witt --base origin/main`: PASS. Every note is a base failure, unchanged. Neither changed field appears in the notes.
- `python -m engine.m9.cli check`: exit 0. 1286 report-only observations. The library access gate is clean: every finding is waived, and every waiver is live and current. That includes `m1:readability/witt` at 186, so the count matches exactly. The only Speratus line is report-only: `tellable_as` now scores FK grade 5.8, below the band floor of 8.
- `python -m engine.m2.cli staleness-check`: `witt` not stale, empty diff.
- `python tools/check_live_commentary.py --base origin/main --enforce`: exit 0. Nothing is flagged in the two records, `records/worlds/witt.yaml` or `engine/m9/enforce.py`.
- Package pin: `records/worlds/witt.yaml` pins `packages/witt/2026-10-08T23-42-04Z` with `manifest_hash: "sha256:64f820e2176e2227cccb8149d068a8f7a470d0a785ff1279ffd2a2f67d3f961b"`. `sha256sum` of that `manifest.json` gives the same value, and OG-64 states the same path and hash. The manifest's record hashes for `witt.story.speratus-hymn-under-the-window` (c1036223...) and `witt.core.witt` (4b98e9bf...) equal the edited files on the branch, so the package was built after the last record edit. Its `records_commit` is the merge base 8d7e0edc, because the build ran on the uncommitted edits. The hashes and the staleness check show it holds the edited content.
- Engine diff: `engine/m9/enforce.py` changes one line. That line's `count=188` becomes `count=186`. The deadline, owner and every other waiver are unchanged. This is the mechanical tighten the gate requires, the same kind as the 8 October witt claim-correction PR. OG-64 discloses it.

## Verdict: REVISE (one record field, then a targeted recheck)

Item (10) is closed. No `vendored` and no `this library` is left in the Speratus story's spoken field, and every hedge is still there. Item (12) is not closed. The new visitation note no longer says "we have not read them", but "reached us only by name" makes the same claim in other words, and the library's own term "named" is still in the voice (finding 1). Findings 2 and 3 are wrong statements in OG-64, the audit trail. They are one-line edits.

## Per-item checks

1. **The 1527 date.** It is supported. `witt.source.saxon-visitation-protocols` gives "(1527–28 ff.)". `witt.force.parishes-state-as-reported` and `witt.force.territorial-princely-force` say 1527-28. `witt.limit.record-thinnest` and `witt.demo.record-thinnest` say "starting in 1527". The source record is `named-not-rechecked` at Widely Accepted. "From 1527" claims no more than those records do. OG-64 states the confidence correctly.
2. **The visitation note's new wording.** See finding 1.
3. **`witt.limit.record-thinnest` `statement` and `witt.demo.record-thinnest` `exchange`** ("Those reports exist. We do not hold them." and "those reports exist, and we do not hold them"). These do not voice the library's gap as the church's claim. In this world "hold" is the voice's settled word for what its record holds. `thinness` says "so we hold the program, not a village's own report of itself". The limit goes on: "What we hold instead is our founder's own testimony". The wording says what the record holds. It makes no claim that the church did not read or know its own reports. The drafter's judgment stands.
4. **The Speratus story `tellable_as`.** Every true claim is kept: Wittenberg, the wanderer down from Prussia, "remembered", Speratus's own hymn by title, beneath Luther's window, and "The tradition says it moved him deeply". The three hedges are intact. "We have no word of when it happened" keeps no date. "We do not know who the singer was" keeps no name, and the sentence still leaves the singer separate from Speratus. "We cannot say the scene ever happened at all" keeps no confirmation. "Exactly" is dropped from "when". That is right, because no record gives any date for the scene. Nothing is added. Every sentence is short and plain. Nothing in it reads as generated. The FK 5.8 score is report-only and is not a finding.
5. **The Speratus story `text`.** "What the account does not do" and "The story we can honestly tell" lose nothing true. "The account" points back to "The tradition Bacon's Introduction relates". See finding 2 on how OG-64 describes this field.
6. **Quotes.** The diff touches only `witt.core.witt` and `witt.story.speratus-hymn-under-the-window`. No quote record, quote `text` or `modern_rendering` is changed.
7. **OG-64.** It is appended after OG-63 with 17 added lines and no removed ones. OG-63 is untouched. OG-64 cites OG-63 by subject and date, and states the gates and the waiver change honestly. The "Changed" bullets match the diff word for word. Apart from findings 2 and 3, the "Not changed" paragraph is accurate.
8. **Other spoken fields with build vocabulary.** I scanned every `records/witt` field that `engine/m1/spoken_fields.py` registers, plus `thin_topics.note`. Many `force.description`, `gravity.description` and story `text` fields, and some figure labels, still say "this library". Two participant-label fields still say "vendored": `witt.figure.brussels-martyrs-john-and-henry` `names` ("this library's own vendored text") and `witt.force.absent-inputs-1525-and-1555` `name` ("outside every vendored text"). These are outside items (10) and (12), which name one reply's words and their source fields each. OG-64 is right to leave them for the build thread. See observation (a).

## Findings

### 1. SUBSTANTIAL: the visitation note still voices the library's gap as the church's own
Field: `witt.core.witt` `thin_topics` (visitation topic) `note`. This note reaches the voice every time a visitation keyword is hit. `engine/m4/evidence.py` adds it to the turn's evidence as "THIN GROUND (do not claim past it)", and the 9 October reply took its wording from there.
Current: "The Saxon church inspected its own parishes from 1527 and wrote down what it found. Those reports reached us only by name; none is in our hands."
Why it is wrong: the church in the first sentence is the "us" in the second. A church that wrote these reports itself now says they "reached us only by name". That tells the participant the church knew its own reports only by their titles. This is the claim item (12) ruled false, "we have not read them", in other words. "By name" is also the library's own term: the source record is a "Named absence only". The world's `thinness` uses the same pattern ("reached us only by reference, not in hand"). OG-64 cites it as the model, but that field is not the authority on this point. See observation (b).
Fix: use the wording the world already uses in `witt.limit.record-thinnest` and `witt.demo.record-thinnest`. "Hold" names what the record holds, not what the church knew.
"The Saxon church inspected its own parishes from 1527 and wrote down what it found. Those reports exist, but we do not hold them. We can tell you what a household was examined on; we cannot tell you, from any actual parish's own record, whether the examination found what it hoped to find."
Then rewrite OG-64's first bullet to quote the new wording. Replace the `thinness` justification with the `record-thinnest` one. Rebuild and repin. Confirm the readability waiver count again. `thin_topics.note` is not graded, so 186 should not change.

### 2. NOT SUBSTANTIAL: OG-64 calls the story's `text` speakable
Current (OG-64, third "Changed" bullet): "Both are speakable and carried the same build vocabulary."
`engine/m1/spoken_fields.py` registers story `text` as "source wording, never voiced or shown; kept on this role so the gates still scan it". `engine/m4/evidence.py` `_head_text()` refuses to fall back to it "which is never voiced". `engine/m2/builders.py` `_chunk_text()` compiles only `tellable_as` for a story. The edit is harmless, but the stated reason for it is wrong.
Fix: "Neither is voiced (story `text` is never voiced or shown, per `engine/m1/spoken_fields.py`), but the gates scan the field, and it carried the same build vocabulary."

### 3. NOT SUBSTANTIAL: OG-64's "Not changed" paragraph says what is spoken too broadly
Current: "Build vocabulary stays in fields the compiler does not speak (... record bodies), by `engine/m1/spoken_fields.py`."
`thin_topics.note`, the field this entry corrects, is spoken (finding 1). But it is not in `spoken_fields.py`. So that file is not the full list of what reaches the voice, and the sentence implies it is.
Fix: add after that sentence: "`thin_topics.note` also reaches the voice, through the THIN GROUND line in `engine/m4/evidence.py`, though `spoken_fields.py` does not register it." See observation (c).

## Observations (not findings; for tracking, not for this branch)

(a) OG-64's list of speakable fields left for the build thread could name the two "vendored" participant labels in per-item check 8. They are item (10)'s exact word, on a participant-facing surface.

(b) `witt.core.witt` `thinness` ("the Saxon visitation itself was made and exists, but it reached us only by reference, not in hand") is spoken and has the same weakness as finding 1. It was not the source of the 9 October reply, so it is outside item (12). It should be logged as an open item for the build thread, not left unrecorded.

(c) `thin_topics.note` reaches every turn whose keywords match. It is not in `SPOKEN_FIELDS` or in the field lists `gate_no_build_attribution` and `gate_perspective_leak` scan. No gate reads it for readability, build vocabulary or perspective leak, and that gap is how item (12)'s wording got through. This is an engine-level gap across the fleet. It needs its own gap entry or `ACCEPTED_OPEN` registration by the engine thread, not a fix on this branch.

Finding 1 blocks closure of item (12). It is one record field and a rebuild, and the next round needs only a targeted recheck of that field and OG-64. Findings 2 and 3 are corrections to OG-64. It has not merged yet, so they can be made in place.
