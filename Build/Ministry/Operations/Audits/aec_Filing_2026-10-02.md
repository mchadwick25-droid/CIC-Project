# aec filing and gate resync, 2026-10-02

Scope: bring PR #624 (Antiochene Exegetical Christianity, code `aec`, Steps 0 to 2 written 2026-09-25 under the V1.8 process) up to the current Library-stage gates of `main`. No change to scholarship, confidence tags or any review outcome. The Round 3 review did not clear the three documents, and the filing records that as it stands. Session: https://claude.ai/code/session_019FXuEebrCDmzYe987sNAxL

## Merge of origin/main

| Conflict | Resolution |
|---|---|
| `Build/worlds/_cross-world/dossiers/antiochene-exegetical-christianity-chrysostom-ce_Source_Readiness_Dossier.md` (the branch added a "Closed" paragraph for Ammianus; main had moved the file and carried the same paragraph as "Resolved") | Main's paragraph kept. |
| `cic/corpus-map/_staging/ammianus-marcellinus_roman-history_yonge1862.yaml` (add/add) | Main's file kept. It carries the `row_id` on every row and already holds the Book XXII row the branch had added by hand. |
| `cic/corpus-map/antiochene-exegetical-christianity-chrysostom-ce.yaml` (generated) | Main's version taken, then regenerated. `python cic/engine/corpus_map_merge.py --check` is valid. |

## Filing

- Documents moved from `worlds/aec/` to `Build/worlds/aec/`: Step 0, Doc_01, Doc_02, `Source_Registry.md`, `Open_Gaps_Tracking.md`. `records/aec/.gitkeep` added. Build state and handoff manifest at `Build/worlds/aec/build/`.
- `worlds/aec/Superseded_Claims.md` moved to `Build/Ministry/Operations/Audits/aec_Superseded_Claims.md`, because it is correction history. The live documents no longer point to it.
- The single combined review file for each of Rounds 1 to 3 is filed as `Step0_Review_Round<n>.md`, `Doc01_Round<n>_Review.md` and `Doc02_Round<n>_Review.md` for n = 1 to 3, identical copies of each round's text. No header field and no Disposition line was added; only paths cited in the texts (`worlds/aec/...`, `worlds/lpc/...`) were repointed to `Build/worlds/...`. No review file says Approved to proceed, because none of the three documents cleared.
- Registry entry `records/worlds/aec.yaml`: `state: building` changed to `state: candidate`. `safety_adjacent` left unset (project lead's field).
- Paths in the documents and the dossier repointed from `worlds/...` and the missing V1.8 process file to `Build/worlds/...` and `Build/reference/method/CiC_Record_Native_World_Build_Process_V2.0.md`.
- Library placement: `palladius_lausiac-history_clarke1918.txt` placed to this world as `context`, `provisional` (staging file `cic/corpus-map/_staging/palladius_lausiac-history.yaml`, row issued with `--assign-ids`), so that Doc_02 section 6's use of it has a Registry row. The bucket now holds 50 rows: the 47 of the branch, the Liturgy of S. John Chrysostom and the Palladius *Dialogue* that arrived on `main`, and this placement.
- Source Registry: rewritten to the 11-column layout with the `Discovery (channel / instrument / date)` column (12 pipes a row); one Confidence letter per row (row 14 split into 14 at B and 14a at A); rows 13, 14a and 21 are A only after the loci were read at source in this filing; row 2 gained the paragraphs that carry the verse it licenses; rows 15 and 16 carry the plain Exclusion Reason `Out-of-Boundary`; rows 19 to 21 added; the dossier section 2 cross-links given a table; corpus figures counted two ways with the locale.
- Doc_02 section 8: holdings dispositions rewritten with Table D (84 files marked "in scope, unread", each deferred with the buckets that assign it).
- Dossier: ISO dates removed from the header and from the "verified by" cell; the Palladius lead and its note restated as vendored.

## History moved out of the live documents

Each of Step 0, Doc_01 and Doc_02 carried a status line that narrated the cap escalation, a pointer to the withdrawn-claims file, and a Document Log table. The log, kept here:

| Date | Event | Artifact | Result |
|---|---|---|---|
| 2026-09-25 | Drafted | none | none |
| 2026-09-25 | Round 1 review | `Review-Artifacts/Round1_Library_Stage_Review.md` | SUBSTANTIAL REVISION REQUIRED |
| 2026-09-25 | Round 1 fix pass | none | none |
| 2026-09-25 | Round 2 review | `Review-Artifacts/Round2_Library_Stage_Review.md` | SUBSTANTIAL REVISION REQUIRED |
| 2026-09-25 | Round 2 fix pass | none | none |
| 2026-09-25 | Round 3 (final) review | `Review-Artifacts/Round3_Library_Stage_Review.md` | SUBSTANTIAL REVISION REQUIRED |
| 2026-09-25 | Round 3 fix pass (post-cap correction) | none | none |
| 2026-09-25 | Narration cleanup, history extracted | `Superseded_Claims.md` | Correction history extracted |

The Disposition sections said, in substance, that the fixes applied through Round 3 were a post-cap correction and not a self-certified clearance, matching the treatment given to `roman-church-gregorian`'s own Doc_02 and Source Registry under the same rule. The live Disposition sections now state the current status in present tense and keep that disclosure.

Other text removed or reworded, all wording only:

- Step 0 section 5 (process findings for the System Hub) kept two findings in present tense and dropped the account of the early draft that treated "World #8 is not yet built" as still true because the Step 0 Conclusion said so (see `aec_Superseded_Claims.md`, entry 1.8).
- Step 0 section 3 (B3) lost the phrase saying an earlier draft assumed the preaching material was thin.
- Doc_02 section 9 item 6 (removed, replaced by the holdings-triage item): "`engine.m9.cli holdings aec` requires an empty `records/aec/` directory to run (section 8), not a later-build-stage prerequisite; run this way, 74 files remain "in scope" per its own broad heuristic, most not individually assessed this session." `records/aec/` now exists with `.gitkeep`.
- Doc_02 section 9 item 10 (removed, replaced by the Lausiac placement item): the account of the Ammianus corpus-map row added by commit `4e1ff183` on the sibling `library-stage/roman-church-gregorian` branch, hand-applied to this branch during Round 3 and re-checked with `corpus_map_merge.py --check`, and of the "47 rows" count. Open_Gaps_Tracking.md entry for Round 3 (2026-09-25) keeps the account.
- "This session" and "this revision" wording replaced by "at this stage".
- Quotations the gate cannot verify were recast as prose without quotation marks: the Step 0 Conclusion passages, the Methodology A5 passage, the `lpc` Doc_04 and Doc_01 passages, corpus-map notes, the NPNF editor's endnote on Diodore's method (the gate does not read endnotes), and the one Template phrase carrying emphasis marks. The Eutropius and Matthew quotations were cut to the text that matches the vendored file. Quotations that verify now carry `cic:<file>:<locus>` addresses.
- Figures: "47 work-rows" became 50; the Matthew word count "roughly 466,000" became 535,125 (`wc -w`, `POSIX`) and 484,393 (tags stripped); "3.34 million" now states `POSIX`, `C.UTF-8` and tag-stripped counts.
- The statement that the Palladius *Dialogue* is not vendored was corrected in Step 0, Doc_01, Doc_02 and the dossier: it is vendored and assigned, and unread.
