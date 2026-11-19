# Curation sample review: pilot redo

Reviewer: Opus 5.5, 2026-10-30. Group: PILOT. One file, re-curated by a different Sonnet 5.5 drafter (PR #1333) after the wave 1a group B verdict `needs-redo`. Reviewed fresh against `cic/texts/possidius_vita-augustini_weiskotten1919.txt`.

`check` was run with the `answering_library` code from `origin/main` (the shared checkout's code is older and rejects the `quote` field in `fixes`). Result: PASS, class partial to curated, 98 divisions (92 body, 3 apparatus), coverage 100.0%, 180 of 180 byte ranges exact. Series `caput` and `chapter` read 1 to 31; `letter-lat` and `letter-eng` read 1 to 14; no repeats, backward steps or gaps.

| Stem | Verdict | What was checked | Defects / notes |
|---|---|---|---|
| `possidius_vita-augustini_weiskotten1919` | sampled-ok | All 64 top-level heads read in the file: PRAEFATIO 1485, PREFACE 1518, then CAPUT I to XXXI and CHAPTER I to XXXI alternating from 1563 to 4916, in order with no gap or repeat; margin numbers before `15 CAPUT VIII` (2035), `5 CAPUT XII` (2362) and `15 CAPUT XXI` (3241) are read correctly. The `chapter` rule stops at 4960, so the NOTES' own CHAPTER heads (5076 to 5960) are not taken as body. All 28 letter heads in chapter 30 read (Latin 4177 to 4825, English 4212 to 4863): each language prints 1 to 14 with nothing missing. A scan for any numeral-like line start (`[0-9iIlnoO]{1,2}.`) in 4164 to 4879 finds exactly these 28 lines. No numbered lines elsewhere in the body. Every evidence quote is on its line. Packet sample (12 divisions, lines 10 to 6295) and the three largest (eng-chapter28 3922, eng-chapter31 4916, eng-chapter27 3744) begin at their printed heads. Apparatus: front 11 to 1482 ends at page number 37 before the work's title; notes 5063 to 5999 open at NOTES; index 6000 to 6294 opens at INDEX TO LATIN TEXT. | No defect. Notes below. |

## The section-11 judgment call: confirmed

Neither language prints a clean `11`. The yaml sets Latin `ii.` (4629) and English `n.` (4667) as section 11. The call is sound, for three reasons that do not rest on sequence alone:

- Each language is its own printed instance. Latin `ii.` stands between `10.` (4611) and `12.` (4697); English `n.` stands between `10.` (4645) and `12.` (4735).
- The two are counterparts. "Occurrit autem alia quaestio, quam contemnere non debemus" (4629) is rendered "But another question arises which we ought not to slight" (4667).
- This scan's OCR reads the printed `11` as `n`, `ii` or `II` elsewhere on the same pages: the apparatus line numbers "n quadraginta" (4184), "II nee A" (4247) and "n fuerit A" (4638), each between printed 10 and later numbers.

4629 is line 23 of its Latin page (margin numbers 5, 10, 15, 20, 25 at 4611, 4616, 4621, 4626, 4631), so `ii.` is not a margin number.

## Section-1 fixes: confirmed

Latin 4177 `20 i. Caritati tuae` and English 4212 `i. I thought` both print `i.` for `1.` and are followed by printed `2.` in each language. The `20` at 4177 is the margin line number (5, IO, 15, 20, 25 at 4162, 4167, 4172, 4177, 4182). The two lines are counterparts ("Caritati tuae misso exemplo epistolae" / "the copy which was sent to your Grace"). Before the fix, the letter's first section was folded into the chapter opening.

## Margin-number pattern: confirmed

The optional `^(?:\d{1,2} )?` lets Latin 2 (`10 2.`, 4229), 9 (`20 9.`, 4563) and 10 (`5 10.`, 4611) match. Each leading number is the page's margin line count: 4229 is line 10 of the page starting 4220; 4563 is line 20 of the page starting 4544; 4611 is line 5 of the page starting 4607. The pattern also reads the margin before CAPUT VIII, XII and XXI. Because rule `lines` are hand-listed single lines, the looser pattern cannot pick up stray lines.

## Minor notes (not defects of this curation)

- Facing pages interleave. The edition prints Latin and English on alternating pages, so each division also holds the other language's page tail up to the next head. For example, `lat-caput30/sec1` (4177) holds the end of English chapter 29 (4189 to 4196), and `eng-chapter30/sec1` (4212) holds the end of Latin section 1 (4220 to 4228). The Latin pages' apparatus criticus (for example 4183 to 4187) also sits inside body divisions. Every line stays addressable to its file location, and no number is invented. Separating the languages page by page needs tooling the ledger lists as open (page-head splitting, a per-rule language guard), not a redo.
- Three one-line gap divisions remain as `text/line<N>`: line 10 (OCR title page, "SANCTI AUGDSTINI VITA", 3 words), line 1483 (the printed title "SANCTI AUGUSTINI VITA / SCRIPTA A POSSIDIO EPISCOPO" above the Praefatio, 7 words) and line 6295 ("r", stray OCR after the index, 1 word). Lines 10 and 6295 could sit inside the front and index ranges in a later pass.
- The notes range 5063 to 5999 ends with the bibliography (for example 5995 to 5998). It is still apparatus, under the kind `notes`.

## Tooling observations

- The shared checkout at `/home/user/CIC-Project` runs older `answering_library` code that rejects `fixes[].quote`. Running `curate check` there on a post-#1329 curation fails to load. Sampling needs the `origin/main` code.
- The four fixed lines still raise the look-alike `warn`, as the drafter's report says. It does not affect the result.
