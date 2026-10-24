# Handoff — live-reply claim check, follow-on fixes — 2026-10-24

From session: https://claude.ai/code/session_01FAFtP6dLsmGd6gWztwpwWg · Workstream: the 19 October live-reply claim check (`Build/Ministry/Operations/Audits/2026-10-19_live-reply-claim-check_eleven-worlds.md`) and its follow-ons · Branch: `claude/exciting-bardeen-sr4a1i` · Earlier PRs, merged: https://github.com/mchadwick25-droid/CIC-Project/pull/1094, https://github.com/mchadwick25-droid/CIC-Project/pull/1102 · This PR: opened as a draft from this branch.

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| Every finding of the 19 Oct claim check re-confirmed against `cic/texts/` and fixed (PR 1094) | Separate Opus contexts re-confirmed each finding with verbatim lines. Sonnet drafted the fixes; Opus reviewed them in two rounds. A separate independent recheck thread passed them in two rounds (`2026-10-24_live-reply-record-fixes_Independent-Recheck_Round1.md` and `_Round2.md`). |
| Recheck round 1 fixes B1–B7, and the two Syriac leftovers (PR 1102) | Recheck round 2: PASS. Syriac leftovers reviewed in `2026-10-24_syriac-leftovers_Review_Round1.md`. |
| Desert world-core `formation_logic` rewritten; martyrdom link scoped to Athanasius on Antony | `2026-10-24_desert-core-formation-logic_Review_Round1.md`. |
| Nine House Churches force records: real voices named, unsourced felt states cut, one factual error fixed (this PR) | `2026-10-24_pahc-force-records_Assessment.md`; reviews Round1 (6 blocking, fixed) and Round2 (PASS). |
| Cappadocia: 19 records citing five unvendored sources re-grounded in held texts; Basil's famine homilies recorded as held in extracts; source-record kinds corrected (this PR) | `2026-10-24_cappadocian-unvendored-citers_Assessment.md`; reviews Round1–3; cap reached with two one-sentence findings; project lead's cap ruling (System Hub Decision Log, "Cap ruling: cappadocian unvendored-citers", 2026-10-24); ordered recheck PASS (`…_Cap-Ruling-Recheck.md`). |
| The 330s dating of On the Incarnation (this PR) | No vendored source carries it. `alx.source.athanasius-de-incarnatione` now gives the NPNF editor's own dating and caveat; reviewed in the Cappadocia rounds. |
| Open_Gaps entries in all eleven worlds, append-only | Path check and commentary check pass. |
| Packages rebuilt and repinned, site pages recompiled, `cic/texts/README.md` regenerated, M9 waivers tightened or raised where an existing waiver reason covers the change | `engine.m10.cli records`/`regate` per world, M2 and site staleness, M9 drift test, README check; engine suites 3101 passed, 2 `test_deeper_seam` failures in the parallel run that pass alone (119 passed). |

## 2. Not done

- Engine question, audit item 5: `verdict: withhold` drops a sentence's citation, not the sentence, unless the reason is a quotation reason (`engine/m4/turn.py:368-394`; tested). Whether uncited, ungrounded sentences should ship, and that paragraph-level `inherited_verdicts` are never applied, are open for the project lead. No engine code changed.
- Audit item 6: over 300 records fleet-wide carry `sources: []` while `verified-direct`. Methodology question for the project lead; a waiver needs his approval.
- Desert Life of Antony quote records are `register: emic` and some give Antony as speaker of narrated speech. Fleet-wide question.
- Record bodies still hold build narration the commentary checker does not flag. Whether to strip them is the project lead's call.
- Cappadocia, logged in its Open_Gaps (entry 56): `term.pleonexia` famine framing; `demo.taught-most` Matthew 25 glosses; a source record for the npnf208 Prolegomena homily extracts; `license:` lines on unvendored sources in eight more records; the usury homily is quoted almost whole in npnf208 (Source Registry row 16 understates it).
- PG36/PG37 Greek OCR (De vita sua, Oration 44): ruled "hedge for now" by the project lead. Using it needs someone to check the page images.
- A modern source for the 330s dating would need acquiring by the Library.

## 3. Re-check before you trust it

- The Cappadocian pass reached the three-round cap. Its last two sentences cleared only through the ordered recheck under the cap ruling.
- `test_deeper_seam` and `test_shelf` tests fail intermittently under `pytest -n auto` and pass alone. Not caused by this work, but not root-caused either.
- Many re-grounded loci cite raw line numbers in the vendored files. If a file in `cic/texts/` is re-extracted, those numbers move.
