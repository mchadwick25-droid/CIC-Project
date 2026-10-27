# Change order: canon questions in visitors' own words — 2026-10-27

## 1. Name

Five `[measured]` questions are added to existing cells of Appendix A of the Program Spec, written in the words real visitors used. This is an amendment to the approved canon, so it is a named change order, not a quiet edit. No new cells, no hints, no matcher change.

Approved by Mark on 2026-10-27: "Approve the five wordings as written."

## 2. Reasoning

- Six of the ten real visitor questions of 20 to 26 October reached no cell, or the wrong one, although good records exist: how did you start this tradition, on what documents was teaching based, who did Jesus leave in charge, how does one inherit eternal life, if you died today would you go to heaven.
- A cell needs two shared content words with a canon question (`engine/m4/evidence.py`, `_MIN_ASK_MATCH_WORDS`). A record's `retrieve_when` words cannot decide a two-word query alone.
- `cic/corpus-map/RETRIEVAL-HINTS.md` rule 2 forbids a hint written from a failing question, and lines 73 to 79 name this case "a canon gap: add a [measured] question to Appendix A".
- New cells would bring Program Spec line 316 (no cell may be empty in any world) onto twelve worlds, plus sealed probes. Existing cells keep the 28 and the sealed set valid.
- Precedent: seven `[measured]` questions were added earlier (86 to 90 to 93; `engine/m4/reports/retrieval_bench.py`).

## 3. Before and after, verbatim

`engine/canon/seed_appendix_a.py`, each row appended at the end of its cell's run:

| Cell | Id | Text |
|---|---|---|
| F1-T | `_fleet.canon.f1-t-04` | What did your people say a person must do to be saved and to inherit eternal life? |
| F2-I | `_fleet.canon.f2-i-04` | On what documents was your teaching based — which writings did you rely on? |
| F3-I | `_fleet.canon.f3-i-06` | How did your tradition start — who began it, and how did it get going? |
| F3-I | `_fleet.canon.f3-i-07` | Who did Jesus leave in charge, and who is in charge of your people now? |
| F6-T | `_fleet.canon.f6-t-04` | What did your people believe happens when someone has died — do the faithful go to heaven? |

`Build/reference/Redesign-Spec/CiC-Program-Spec.md`, Appendix A: the same five questions appended to the F1 T, F2 I, F3 I (two) and F6 T rows, tagged `[measured]`.

`engine/m1/schemas.py`, canon_question `source` enum:

- Before: `["corpus", "ext", "new"]`
- After: `["corpus", "ext", "new", "measured"]` (the seven earlier `[measured]` records already carried a value the enum did not list)

## 4. Result of the bench rerun (offline, no model call)

`python -m engine.m4.reports.retrieval_bench`, 134 questions, on the pinned packages restored from records.

| | Before | After |
|---|---|---|
| Ground records | 1,226 | 1,258 |
| Cells reached | 159 | 162 |
| Empty grounds | 1 | 1 |
| Quote records surfaced | 205 | 210 |

Gains: desert +10 ground, hal +8, ijc +11, pahc +2, witt +3. Regressions, left visible: gallic 179 to 178 ground; rzg 118 to 117 ground and 15 to 14 quotes. The bench questions are locked and were not edited.

## 5. What this change order does not do

- It adds no cells, so no world takes on a new coverage duty.
- It writes no hint on any record and changes no matcher code.
- No sealed probe was opened, read or copied. Whether a sealed paraphrase overlaps the new wordings is checked through `engine/m3`, not by hand, and has not been done.
- It does not fix the alx "how might I be saved" result (original sin); that is record choice inside F1-T.
- The generator was not left to rewrite the earlier records. Re-running `seed_appendix_a.py` also rewrote eight records whose text had been edited by hand since seeding (for example `c-p-01`, `f6-t-01`); those rewrites were discarded. The script's table has drifted from those eight records and is no longer a faithful transcription of them. That drift is recorded here, not fixed.
- The spec's F6 T row lists two questions while the seed table holds three. Existing drift, not touched.
- A synonym or alias layer in the matcher is the larger option. It needs its own change order and is held until this change shows what is left.

## 6. Related files

`engine/canon/seed_appendix_a.py`; `engine/canon/records/canon_question/_fleet.canon.*.md`; `Build/reference/Redesign-Spec/CiC-Program-Spec.md` (Appendix A); `engine/m1/schemas.py`; `engine/m1/canon.py`; `engine/m4/evidence.py`; `cic/corpus-map/RETRIEVAL-HINTS.md`; `engine/m4/reports/retrieval_bench.py`; format precedent `Build/Ministry/Operations/Audits/jes_Step0_ChangeOrder_2026-09-30.md`.
