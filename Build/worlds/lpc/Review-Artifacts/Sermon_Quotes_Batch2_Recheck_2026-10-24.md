# lpc sermon batch 2: round-2 targeted recheck

- Branch: `claude/lpc-sermon-batch2-2026-10-24` at `99992cda`, diffed against `667ee9c7` (the round-1 head).
- Reviewer model: Opus 5.5 (`claude-opus-5-5`).
- Scope: only what changed, against the round-1 findings. No repo file was modified. The gates ran in a detached scratch worktree, which was removed afterwards.

## Gates

- `python -m engine.m10.cli records lpc`: PASS.
- `python -m engine.m10.cli regate lpc`: PASS. The only notes are base failures this branch did not touch.
- `engine/m4/tests/test_quote_speaker_offered.py`: 17 passed.
- `tools/check_paths.py --baseline tools/check_paths_baseline.txt`: 0 new. The one baseline line added covers the round-1 review copy's mention of `packages/lpc`, which does not exist in the tree. That is an audit-trail file, so the entry is acceptable.

## B. Vandal-date correction

| Finding | Fix on branch | Checked at source | Status |
|---|---|---|---|
| B-1 (P0) | Fallback applied identically in the force record `description`, `wb_lpc_s25.py` F3A1 and Doc_08 Force 3A-1 Layer 1: "crossed from Spain into Africa in the late 420s; the chronicles disagree on the year, and Prosper's enters the crossing under 427". "In 430 they besieged Hippo" and "third month of the siege (Possidius, Vita XXIX)" are unchanged. | `git grep` for "one chronicle" and "chronicle we hold" over `Build/worlds/lpc`, `records/lpc` and `canon` returns nothing outside Open_Gaps (OG-66 is append-only) and review artifacts. `git grep \b429\b` over the same paths finds only unrelated uses (the anti-Pelagian corpus dates, c. 412-429, and the NPNF letters range). No other site states a crossing year. "The chronicles disagree" is true: Prosper 427, Hydatius 429, Gallic 452 later (see OG-67 below). | Resolved |
| B-2 (P1) | Doc_01 line 27: "crossing from Spain in the late 420s, besieging Hippo in 430 as Augustine lay dying". | Matches the fallback wording proposed in round 1. | Resolved |
| B-3 (note) | None needed. | `packages/lpc` does not exist in the tree, so there is no package to rebuild. | Closed |

## A. Sermon quote records

All changes are in the records and in `wb_lpc_s24.py`. The two agree string for string.

| Finding | Applied as proposed | True at source | Status |
|---|---|---|---|
| G2-1 (P1) | Yes. Lens note: "God's will is done 'in you' whether you will it or not; it is done 'by you' when you do it as well." Claim guard: "'by you' is God's will done by you as well". | PL 38 26340-26341: *Fiet enim voluntas Dei in te, etsi non fit a te*. Now consistent with *sed fiat et a te* and NPNF 10700. | Resolved |
| P1-1 (P2) | Yes. Guard: "The modern rendering uses 'received' (accepistis)". | The `text` says "learnt" and the rendering says "received". | Resolved |
| P1-2 (P2) | Yes. "He explains the order". | — | Resolved |
| P1-3 (P2) | Yes, in the body. | PL 38 line 27711: *reddituri estis, non Oratidnem. sed Symbolum.* The record writes *Orationem*. That corrects an OCR slip in a cited phrase, not a quote field, so it is acceptable. | Resolved |
| P2-1 (P2) | Yes. "participant asks how a believer was told to keep up faith day by day". | — | Resolved |
| P2-2 (P2) | Yes. | — | Resolved |
| P3-1 (P2) | Yes. "the passage does not say how often hymns were sung." | — | Resolved |
| G1-1 (P2) | Yes. "since no one comes to Christ unless it is given him by the Father." | Matches the verse in the passage. | Resolved |
| G2-2 (P2) | Yes. "from Fiet enim voluntas Dei in te". | PL 38 line 26340 ends with *Fiet*, and 26341 continues *enim voluntas Dei in te, etsi non fit a te*. The guard's range 26340-26351 starts on the right line. | Resolved |
| G3-1 (P2) | Yes. "literally 'love Himself from you', rendered 'through you'". | — | Resolved |
| G3-2 (P2) | Yes. "the sermon is on John v. 31 and Galatians v. 16-17 (the flesh against the Spirit)." | Matches the NPNF 78 heading. | Resolved |

## OG-67

- **Hydatius**, lines 1641-1645: entry 90, year V, Mommsen's margin 429. The text reads *Gaisericus rex de Baeticae provinciae litore cum Vandalis omnibus eorumque familiis mense Maio ad Mauritaniam et Africam relictis transit Hispaniis*. Accurate.
- **Gallic Chronicle of 452**, Prosper file lines 71067-71071: entry 108, *Vandali in Africam transfretantes*, sits under year VIII (entry 106). That follows 104 at margin 429 and comes before 109, VIIII, at margin 432. "Under a later year" is accurate.
- **Weiskotten**: 5364 and 5845 are notes and give 428. Line 465 also gives 428, but it is in the Introduction. See N-2.
- It names both untrue OG-66 statements and the missed Doc_01 line. It gives the reason for not citing 429 now and the open Library request. OG-66 is untouched.

## NEEDS-RULING entry

- It is placed under "Placement questions" in the file's existing format: bold title · author slug · file token · atlas id, then a `>` note.
- It is accurate. The staging file for this volume has no Hydatius row, and Hydatius has no slug in `cic/texts/AUTHORS.md` or `cic/corpus-map/AUTHOR-IDS.yaml`. The Hydatius entry and lines are correct.
- It asks only for placement. The proposed role and slug serve that request.

## Regressions

- No `modern_rendering` line changed in any record or in `wb_lpc_s24.py`.
- Only the intended records changed: the 6 quote records and the force record. No `text` field changed.

## New findings

- **N-1 (P2).** In the force record `description` (and `wb_lpc_s25.py`; Doc_08 Layer 1 carries the same pattern), the fix names Prosper and says "the chronicles disagree". The text then goes on: "a date a near-contemporary Gallic chronicler independently records ... The same chronicle records the Vandal capture of Carthage under 439". With several chronicles now in play, "a Gallic chronicler" reads as a second writer. If "the same chronicle" is read as the Gallic Chronicle of 452, it is false: that chronicle enters Carthage under year XXI (Prosper file line 71219). Prosper's chronicle does carry Carthage under 439. Proposed: `... and he died on 28 August 430 -- a date Prosper, a near-contemporary chronicler in Gaul, independently records. This is documented. Prosper also records the Vandal capture of Carthage under 439, ...`. Doc_08 needs the matching change. Not blocking.
- **N-2 (P2).** OG-67 says "Weiskotten's notes to Possidius give 428 (... lines 465, 5364 and 5845)". Line 465 is in Weiskotten's Introduction, not the notes. Because the file is append-only, correct it in the next entry that touches this item: "Weiskotten's introduction (line 465) and notes (lines 5364, 5845)". Not blocking.

## Counts

- Prior findings: 13 (1 P0, 2 P1, 10 P2). Resolved: 13 of 13. B-3 note closed.
- New findings: 0 P0, 0 P1, 2 P2 (N-1, N-2).
- Gates: records PASS; regate PASS; quote test 17 passed; check_paths 0 new.

VERDICT: Approved to proceed
