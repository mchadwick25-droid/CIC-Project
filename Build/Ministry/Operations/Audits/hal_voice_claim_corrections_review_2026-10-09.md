# Hal voice claim corrections: adversarial review (2026-10-09)

Scope: branch `records/voice-claim-corrections-hal-2026-10-09` at ff8e8c54 (`git diff origin/main...HEAD`, one commit over the merge-base 8d7e0edc). The branch makes Mark's ruled corrections for the Jerome item of "Voice errors found in the record pass staging reading, 9 October": items (7), "learned it as an older man", and (10), "scholars contest it still". It edits `hal.quote.partially-acquired-hebrew` `use_note.means` and `hal.core.hieronymian` `cautions`, tightens the hal readability waiver in `engine/m9/enforce.py`, repins the package and adds OG-18. I edited no record and made no model or API call. This is one review, Opus 5.5.

Mechanical checks, run on the branch:
- `python -m engine.m10.cli records hal`: PASS.
- `python -m engine.m10.cli regate hal --base origin/main`: PASS. 127 notes, every one a base failure, unchanged. Neither changed field appears in the notes. Scored with `engine.m1.gates.grade_text`, the old `cautions` was FK 14.1 / FRE 32.1 and the new one is FK 6.9 / FRE 60.08. That is just over the FRE floor of 60, which matters for the fix in finding 1. FK 6.9 is below the band floor of 8; `engine.m9.cli check` reports it and does not fail it.
- `python -m engine.m9.cli check`: exit 0. The library access gate is clean: every finding is waived, and every waiver is live and current. The `engine/m9/enforce.py` diff is one line: `m1:readability/hal` count 161 → 159. Nothing else in the file changes. Two fewer failures matches the old `cautions` field failing both FK and FRE and the new one failing neither.
- `python -m engine.m2.cli staleness-check`: pass; hal `stale: false`. `python -m engine.m2.cli determinism-check hal`: pass, no differing paths.
- `python -m engine.m2.site_cli staleness-check`: pass. hal (`cic-website/data/worlds/hieronymian-ascetic-literary.json`) is `stale: false`, so the site JSON needs no rebuild. Neither changed field feeds the site compiler.
- `python tools/check_live_commentary.py --base origin/main --enforce`: exit 0. `records`: 0 hits. Only KEEP lines in `engine/m9/enforce.py` and PROTECTED lines in `Open_Gaps_Tracking.md` are listed.
- Package pin: `records/worlds/hal.yaml` pins `packages/hal/2026-10-08T23-42-37Z` with `manifest_hash: "sha256:de206f7d7a97269e1a01b1cb1386b72d653ee197e18fd1aaa626d6180ba09b4e"`. `sha256sum` of that `manifest.json` gives the same value, and OG-18 states the same path and hash. All 228 manifest entries hash correctly against the local package. Its 162 record files match `records/hal/` byte for byte, including both changed records, so the package holds the last record edit. But see finding 2: its `records_commit` is the merge-base, not a commit that holds these records.

## Verdict: REVISE (one targeted fix, then a targeted recheck)

Both ruled items are handled. No record now says or invites "older man", and the etic phrase "contested in modern scholarship" is gone from the field the voice drew item (10) from. The quote text and `modern_rendering` are untouched and agree with the new use note. `hal.contested.hebrew-fluency` is unchanged and still Contested. OG-18 is accurate and append-only. All eight cautions survive the rewrite.

But the rewrite of caution 4 adds a new sentence whose subject reads as Jerome: "He never states his fluency as settled." That is a claim the world's own records contradict, in a voice-diet field compiled into `compiled/prompt.txt` (line 58), on the very topic this branch is correcting. That is finding 1. It is a one-sentence fix. The fix also clears finding 2 when the package is rebuilt.

## Source verification

- Jerome, Ep. 108 to Eustochium (`cic/texts/npnf206_jerome-principal-works.xml`, div `v.CVIII`), lines 22016-22019: "While I myself beginning as a young man have with much toil and effort / partially acquired the Hebrew tongue and study it now unceas[ingly] lest if I leave it, it also may / leave me". The record's `text` is verbatim, with the page-break split in "unceasingly" joined, as its body says. Jerome says he began as a young man. Nothing in the passage says he began or learned it late.
- `text` and `modern_rendering` are byte-identical to origin/main. Of the record's top-level fields, only `use_note` changed. Within it, only `means` changed. `modern_rendering` ("As for me, I began as a young man and with much toil and effort partially acquired the Hebrew tongue. I study it now without ceasing, in case, if I leave it, it too leaves me.") agrees with the new `means` ("says he began Hebrew as a young man, had only partially acquired it through long toil, and kept studying it lest he lose it"). Each of the three clauses of `means` is in the source sentence, and the note adds nothing else.
- The new `means` is still one sentence, descriptive, not an instruction. The `use-note-shape` gate passes. `not_for` is unchanged and still bars both the full-mastery and the knew-little readings.

## Per-item checks

1. Item (7), "older man". Grep across `records/hal` for "older man", "old age" and "late in life" finds nothing. "in later life" appears only in caution 1 and the `hal.figure.jerome` body, where it is about Jerome curating his letters, not about Hebrew. The staging report tagged the sentence to `hal.quote.partially-acquired-hebrew`, and the voice drew it from no record. OG-18 is right that this was the voice's own error, and right to give the use note the start date so the voice has it.
2. Item (10), "scholars contest it still". The report (`engine/m4/reports/live-turn-report-hal-2026-10-09-record-pass-staging-reading.json`) tags "His critics doubted that claim then, and scholars contest it still." to `hal.core.hieronymian`, verdict `withhold`, as OG-18 says. The old caution 4, "contested in modern scholarship", is the only Hebrew-fluency wording in that record, and it is gone. I scanned for "scholars contest", "modern scholar", "historians" and "seriously contested". The hits in records the voice reads are these:
   - `hal.term.grammaticus` `false_friend` ("seriously contested").
   - `hal.figure.jerome` body ("per Williams").
   - `hal.dw.authority` `tensions` ("modern scholarship divides").
   - `hal.term.exegesis-as-practiced-authority` `divergence_note`.
   - `hal.term.patrocinium` and `hal.term.origenism` `senses`.
   - `hal.contested.paula-jerome-relationship` `held_against`.
   None of these fields is in `engine/m1/spoken_fields.py`, and none is read by `engine/m2/builders.py`, `engine/m4/evidence.py` or `engine/m4/citation_cards.py`. Leaving `grammaticus` and `jerome` as they are is right.
   The one spoken hit is `hal.limit.f5-material-remains` `statement` ("how historians know this world"). It concerns a different topic, the evidence base. It is not the contest and not in the scope of this ruling.
   `hal.gravity.hebraica-veritas` `description` (evidence-head) names "the separate Contested question of Jerome's actual Hebrew fluency". It uses the vocabulary term and no outside-the-world phrasing.
3. Caution 4 register. Naming "the Representative" and "the Facilitator" in `world_core` has precedent (`lpc.core...`). `world_core` is third-person background, per the comment in `engine/m1/gates.py` at line 878. Pointing the dispute to the Facilitator is right under the working rules. "An open question" plus the pointer to `hal.contested.hebrew-fluency`, which carries `formation_confidence: Contested`, does not mislabel the claim. The third sentence is the defect; see finding 1.
4. The other seven cautions, old against new:
   - (1) Every point is kept. Jerome's hand, his later-life curation, the framing of the women's agency, "real, load-bearing, single-sourced" (now "real and load-bearing, and it has one source"), and never treating it as independent corroboration.
   - (2) "Idealize by design" is now "praise by design". The next two sentences keep the point: the ideal is evidence, the scene detail is not.
   - (3) Kept: widely accepted as Jerome's composition, and never the women's voice.
   - (5) Kept.
   - (6) Kept, minus the word "formative". That is a small loss of nuance, not a new or false claim.
   - (7) "Daily-life specifics (schedule, scriptorium, school as institutions)" is now "daily life ... the schedule, the scriptorium, and the school". This loses "as institutions". It agrees with the record's own `thin_topics` entry ("daily schedule, horarium, liturgy hours, scriptorium, school ... reconstruction, not documentation"). It also agrees with `hal.story.day-at-monastery`, which is Inferential-Thin, and with `hal.term.monasterium` `senses.evidential`. So it misleads nothing in this world.
   - (8) Kept: Palladius and Rufinus hostile, Sulpitius admiring, triangulate rather than settle.
   No caution adds a new claim except the sentence in finding 1.
5. `hal.contested.hebrew-fluency`: `git diff` is empty. It is still `register: etic`, `formation_confidence: Contested`.
6. OG-18. 22 lines added, 0 removed, after OG-17's "Status: OPEN." OG-17 is untouched. The entry closes items (7) and (10) by subject and date ("Voice errors found in the record pass staging reading, 9 October"). It says item (8) is not closed, and why. Its quotes of the old and new text match the diff. Its gate lines match what I re-ran. It says plainly that the waiver went stale and was tightened, and why. Its statement that "No other record states the contest to the Representative" holds for spoken fields (item 2 above).

## Findings

### 1. SUBSTANTIAL: the new caution 4 says, read as written, that Jerome "never states his fluency as settled"
New (`hal.core.hieronymian` `cautions`, caution 4): "The Representative gives only his own words: he began as a young man and partly acquired it. He never states his fluency as settled."
The only male antecedent is Jerome ("his own words", "he began"). The Representative's persona is a woman, and the voice speaks as "we" (`hal.voice.craft` `identity`). So "He never states his fluency as settled" reads as a claim about Jerome. It is meant as an instruction to the Representative.
As a claim about Jerome, it is unsupported and contrary to the world's own records:
- `hal.contested.hebrew-fluency` contests "the DEGREE of unaided fluency, against his own maximal telling".
- `hal.figure.jerome` says his self-presentation is embellished at the Hebrew formation.
- The old caution 4 itself warned against repeating "his own retrospective account" as settled fact.
This field is voice-diet and is compiled into `compiled/prompt.txt`. A voice that just turned "contested in modern scholarship" into "scholars contest it still" can turn this into "Jerome never claimed to be fluent". That would be a new error on the same topic.
Fix: replace "He never states his fluency as settled." with "Never state his fluency as settled." This is the imperative form cautions 1 and 3 already use ("Never treat...", "Never cite..."), and it keeps the point without a new claim. Scored with `grade_text`, the field stays inside the band: FK 6.9, FRE 60.24. The FRE floor is 60, so recheck the score after any other rewording. "The Representative never states..." falls to FRE 58.2 and fails the regate. Then rebuild the package, repin, and update OG-18's quoted caution text, pin and hash. The waiver count stays at 159.

### 2. NOT SUBSTANTIAL: the package's `records_commit` names a commit that does not hold the packaged records
`packages/hal/2026-10-08T23-42-37Z/manifest.json` has `records_commit` and `built_by` 8d7e0edc, the merge-base. That commit holds the old `cautions` and `use_note`, while the package holds the new ones (byte-for-byte match above). The package was built from the working tree before the record edits were committed. The precedent stamps the commit that holds the edits: hal's previous package `2026-10-08T05-12-13Z` stamps 4dc42835, the hal record commit, and witt's `2026-10-08T19-54-22Z` stamps its record-fix commit. The content is correct, and the staleness and determinism checks pass. Only the provenance stamp is wrong.
Fix: when rebuilding for finding 1, commit the record edit first, then build, so `records_commit` names that commit.

### Observation (not a finding, outside this branch)
`hal.quote.partially-acquired-hebrew` and one other record cite this passage as Ep. 108 "sec. 27", and the citation card shows that label. The standard numbering, from memory, puts the Hebrew passage at §26. The vendored NPNF text has no section numbers, so I could not check this here. The branch does not touch the locus. If the build thread can reach a section-numbered edition, it should confirm the locus there.

Finding 1 blocks the branch until it is fixed. It is one sentence, and the recheck needs only the changed sentence, its readability score and the rebuilt pin. Finding 2 is cleared by the same rebuild.
