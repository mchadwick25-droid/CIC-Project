# CO-LPC-3 spoken-field corrections: recheck, round 3

- **Reviewer:** Claude Opus 5.5 (claude-opus-5-5), the whole pass. No other model was used at any point.
- **Date:** 2026-10-24.
- **Authority:** "Cap ruling: lpc CO-LPC-3, a third recheck of one line and ten leftovers" (System Hub Decision Log).
- **Scope:** the uncommitted diff on top of `c65300c1` in `Build/worlds/lpc` and `records/lpc` (26 files, 51 insertions, 48 deletions). It is checked against R2-1 to R2-11 in `CO-LPC-3_Spoken_Corrections_Recheck_Round2.md`. This is a targeted recheck, not a full re-review.
- No repo file was changed except this one.

Abbreviations: ANF05 = `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml`; NPNF101 = `cic/texts/npnf101_augustine-confessions-letters.xml`; NPNF102 = `cic/texts/npnf102_augustine-city-of-god-christian-doctrine.xml`; NPNF104 = `cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml`; MORIN = `cic/texts/augustine_sermones-guelferbytani-lat_morin1917.txt`.

## Method

- I read every changed segment as a word diff.
- I read the cited source lines in `cic/texts/` myself.
- I swept `Build/worlds/lpc` and `records/lpc` for every corrected wording. Review artifacts, logs and the gaps ledger were left out.
- I ran `regate lpc`, `records lpc` and `claims lpc`.
- I graded the changed world_core and gravity fields with `engine.m1.gates.grade_text`.

## 1. The R2 findings

| R2 finding | Status | Check |
|---|---|---|
| R2-1 · P1 · Capsule :19 "it held" | **Fixed as proposed** | Now reads "tested it, and your own bishops kept it." True at source. Firmilian's charge against Stephen stands at ANF05:40044–40054: the African envoys were not received "even to the speech of an ordinary conference", and "not only peace and communion, but also a shelter and entertainment, were denied to them". See also ANF05:40019–40022 ("you cut yourself off from so many flocks"). The new sentence claims only what this world's own bishops did. Cyprian did not break with Stephen, and Augustine did not put Cyprian outside. |
| R2-2 · P2 · Doc_02 :49 | **Fixed as proposed** | The controversies list now glosses "the three controversies he engaged", and the Cyprian clause is set off as an aside. It reads correctly. |
| R2-3 · P2 · Doc_04 :160 | **Fixed as proposed** | The cell text is word for word as proposed. |
| R2-4 · P2 · "a boundary that disagreement does not breach" | **Fixed as proposed at all four sites** | world_core `formation_logic` :128, `wb_lpc_s21.py` :4098, Doc_07 :162 and Rep Phase 7 :44 (which quotes Doc_07, and still matches it). The generator string matches the record. `formation_logic` FK 8.2 / FRE 60.7. |
| R2-5 · P2 · Caution 2 (N-9) | **Applied** | In the record (:275–276) and in `wb_lpc_s21.py` :4232, with matching text. Caution 2 paragraph FK 8.7 / FRE 62.5. For how the rule works, see section 3. One P2 is new: R3-1. |
| R2-6 · P2 · "weekly", "to the baptized", "bury" | **Fixed at every listed site** | World Profile :172, :176, :200; Doc_05 :167, :263, :352; Doc_07 :46; `lpclex001` :35; `lpclex008` :12, :39; `lpclex009` :18; `Lexicon_Deployment_Index.md` :21; Rep Phase 2 :16; Rep Phase 4 :37, :58. Each is as proposed. None of "weekly", "every week" or "will bury" remains in the world's deliverables. The only hit is the cost ledger's "weekly allowance". |
| R2-7 · P2 · communion "survives sharp disagreement" | **Fixed as proposed** | Doc_03 :54, Doc_05 :114, Rep Phase 3 :35. Each now says "Cyprian held [it] should survive". |
| R2-8 · P2 · Doc_06 :75 certificates | **Fixed as proposed** | The sentence now opens "A confessor's letter for a lapsed person, which asks for peace or says it is granted". It matches Ep. XVI's two forms, as round 2 checked. |
| R2-9 · P2 · "silence in its own record" | **Fixed as proposed** | Doc_08 :23, Doc_09 :23, Doc_01 :173. World Profile :26 now says "pastoral voice". |
| R2-10 · P2 · apostolic-succession `prefer_instead` | **Fixed as proposed** | Record :48. This is the same wording as `lpc.term.the-one-episcopate` :59 and `lpc.limit.apostolic-origin-undefended` :45. No current generator emits this line. |
| R2-11 · P2 · World Profile :544 "characteristically" | **Fixed as proposed** | Now reads "sometimes over his own reluctance". It matches `lpclex011` :25. |

## 2. The drafter's extra sweep edits

Each edit below is correct and adds no claim.

- **"Weekly" leftovers outside the R2 list.** Doc_02 :41 and Doc_03 :36 change "undocumented weekly pastoral routine" to "regular". Doc_03 :36 quotes Doc_02 :41, and the two still match. Doc_03 :26 changes "weekly preaching" to "regular". Doc_05 :329 now reads "competes with G4 again and again". The `wb_lpc_s2y_canon_cells.py` :206 docstring now reads "the regular address to the gathered church", which matches `lpc.term.preaching` :49–50. Each edit removes the unattested frequency and asserts nothing new.
- **"Kept it" variants.** World Profile :82 now reads "this world's own bishops kept it against all of them". The gravity record `lpc.gravity.collegial-communion-preserved` :85–86 now reads "This world's own bishops kept it each time", and its generator `wb_lpc_s25.py` :578 matches. Both narrow the old "it holds" / "It held" in the same way as R2-1, so they fix the same overstatement rather than add a claim. Gravity description FK 7.0 / FRE 65.4.
- **Silence wording.** Capsule :79 changes "congregational voice" to "pastoral voice". This aligns it with the Prompt :21, Doc_02 §7 and the R2-9 sites.
- **Claims Register.** The two rows were re-keyed to the new claim text (see section 4).

## 3. The new Caution 2 clause

"Never describe the church's history of those years from this world's own collection, except as Augustine's own later view, given as his and dated to when he wrote it."

- **Is it a clear rule?** Yes. It allows one thing and says how it must be framed: as his view, and placed in time. The sentence after it keeps Augustine's own account of 386–391 as this world's own. The sentence after that keeps Optatus, the canons and imperial law out. These do not conflict.
- **Is it true to the records?** Yes. The ban still rests on the Contested silence (Doc_02 §7 :122; Doc_01 §5 :112–116; OG-54). The exception reaches only Augustine's own writing, which is in this world's collection.
- **Is it consistent with the Constantine witness?** Partly. `lpc.witness.constantine-did-not-corrupt` gives Augustine's view as his: "Augustine answered him directly", "In City of God our bishop adds". So the first condition holds. The second does not. The witness names Answer to Petilian and City of God but dates neither. `lpc.source.augustine-answer-to-petilian` carries no date at all. Only the body of `lpc.source.augustine-city-of-god` dates its work (413–427). A Representative that obeys "dated to when he wrote it" with this witness must either date it loosely ("in his years as bishop", which follows from world_core) or supply a year the records do not hold. That is R3-1.

## 4. The two UNVERIFIED Claims Register rows

Both ids are derived correctly: `claims lpc` matches them, with 98 claims derived and 98 registered. Neither claim can be decided by a string search, so both rows are JUDGEMENT. I checked each at source as follows.

- **89da2f0e (Doc_08 :23).** Doc_01 §5 (:112–116) rates the silence **Contested**, scoped to "what this build has assessed". Doc_02 §7 (:122) names it a silence "in this world's own pastoral voice" for about 133 years, also Contested. MORIN :10297 heads the nine tractatus "SS. OPTATI MILEVITANI", and :10849–10850 titles one a sermon of Optatus for the Holy Innocents. OG-54 (`Open_Gaps_Tracking.md` :1763) logs them as unassessed. The Doc_08 sentence carries the "that this build has assessed" scope, and "pastoral voice" now matches Doc_02. So it holds, at Contested.
- **2bcbf0ef (world_core Caution 2).** This is an instruction, not a claim about the record. Its ground is the same Contested silence. Its permitted span is Confessions IX.vi.14 at NPNF101:13729–13733 ("deeply moved by the voices of Thy sweet-speaking Church"). Its exception covers the Constantine witness. Answer to Petilian II §§202–205 is at NPNF104:17610–17726: "commit no sin if they make a right use of that friendship" (:17670 region) and §204 "What have you to do with the kings of this world". City of God V.25 is at NPNF102:11099–11122. Both works were written well after 391: Petilian in 400–402 (NPNF104:10278–10279 and :10733) and City of God from 413 (NPNF102:864–865). So the exception is true to source. The missing date in the witness is R3-1. It is not a defect in this row.

### Claims rows

| id | status | confidence | source | check | file | claim |
|---|---|---|---|---|---|---|
| 89da2f0e | JUDGEMENT | Contested | Build/worlds/lpc/Doc_01_World_Identification_Boundaries_Orientation.md; Build/worlds/lpc/Doc_02_Source_Ecology.md; cic/texts/augustine_sermones-guelferbytani-lat_morin1917.txt; Build/worlds/lpc/Open_Gaps_Tracking.md | Same scope and Contested rating as Doc_01 section 5 (lines 112-116). The wording "pastoral voice" matches Doc_02 section 7 (line 122). The claim is scoped to what this build has assessed. The nine Morin 1917 tractatus headed as by Optatus and others (line 10297; Optatus sermon title at lines 10849-10850) are unassessed (OG-54). Not decidable by search. | Doc_08_Forces_Document.md | Structural fact governing every cell below: this world is two attested phases separated by a 133-year silence in its own pastoral voice. No surviving voice continuous with Cyprian's ordinary-pastoral mode, from within this world's boundary, that this build has assessed dates from within that interval. |
| 2bcbf0ef | JUDGEMENT | Contested | Build/worlds/lpc/Doc_02_Source_Ecology.md; Build/worlds/lpc/Doc_01_World_Identification_Boundaries_Orientation.md; cic/texts/npnf101_augustine-confessions-letters.xml; cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml; cic/texts/npnf102_augustine-city-of-god-christian-doctrine.xml; records/lpc/doctrinal_witness/lpc.witness.constantine-did-not-corrupt.md | A binding instruction, not a claim about the record. It rests on Doc_02 section 7 (line 122): no assessed pastoral voice for 258-391, Contested because the nine Morin 1917 tractatus are unassessed (OG-54). The permitted account of 386-391 is Confessions IX.vi.14 (npnf101 lines 13729-13733). The exception covers Augustine's own later writing on those years. The Constantine witness rests on Answer to Petilian II 202-205 (npnf104 lines 17610-17726), written 400-402 (npnf104 lines 10278-10279, 10733), and City of God V.25 (npnf102 lines 11099-11122), begun 413 (npnf102 lines 864-865). Both postdate 391. | lpc.core.latin-pastoral-congregational-christianity.md | Never describe the church's history of those years from this world's own collection, except as Augustine's own later view, given as his and dated to when he wrote it. |

In the working tree, these two ids are wrapped in backticks, unlike every other row. The command accepts them, but they should be written plain like the rest.

## 5. Gates

- `python -m engine.m10.cli regate lpc`: **PASS**. 162 public-facing fields were checked, 94 of them new or edited. There is no regression. Every failure listed was already failing at base and is unchanged.
- `python -m engine.m10.cli records lpc`: **PASS**.
- `python -m engine.m10.cli claims lpc`: **PASS**. 98 claims are derived and 98 registered, 2 of them UNVERIFIED.

## New findings

**R3-1 · P2 · The new Caution 2 requires a date that the Constantine witness does not carry.**
- The rule: "…except as Augustine's own later view, given as his and dated to when he wrote it" (world_core :275–276).
- The record it governs, `lpc.witness.constantine-did-not-corrupt`, names both works in `text`, `positions` and `tensions` but dates neither. `lpc.source.augustine-answer-to-petilian` has no date.
- Why this is P2, not P1: the Representative can still obey the rule with relative dating that the records support ("as bishop", "in his later years"). Nothing in it is false or contested. The risk is that a model, told to date the view, reaches for a year the world does not hold.
- Proposed, in the witness record and its generator:
  - In `text`, replace "Augustine answered him directly." with "Augustine answered him directly, around the year 401."
  - In `text`, replace "In City of God our bishop adds a second point." with "In City of God, begun in 413, our bishop adds a second point."
  - In `sources[0].locus`, add "written 400-402 (npnf104 lines 10278-10279, 10733)".
- Both dates are at source, as cited in section 4.

### Advisory (not counted)

- **Construction-prose leftovers the R2 list did not name.** None of these is voice material. They could be swept with the next touch of each file.
  - Doc_05 :407 has "communion as a structural status that survives disagreement".
  - The `wb_lpc_s2y_canon_cells.py` docstring has "already-baptized reception" at :216 and "formal standing that survives even the sharpest disagreement" at :311.
- **City of God's date.** `lpc.source.augustine-city-of-god` gives 413–427. The NPNF editor gives 413–426 (NPNF102:555, 864–865). This is pre-existing and out of scope.
- **The `wb_lpc_s2z_canon_closure.py` :541 drift** ("Each bishop holds the whole of it, not a share") is still open from round 2.
- **The Claims Register ids** should be written without backticks (section 4).

## Counts

- **R2 findings: 11.**
  - Fixed as proposed: 11. That is 1 P1 (R2-1) and 10 P2s (R2-2 to R2-11).
  - Not fixed: 0.
- **Extra sweep edits checked:** 9 sites in 4 groups ("weekly" leftovers, "kept it" variants, silence wording, Claims Register re-key). All are correct, and none adds a claim.
- **New findings: P0 0, P1 0, P2 1 (R3-1).**
- **Claims rows completed:** 2. Both are JUDGEMENT at Contested.
- **Gates:** regate, records and claims all PASS.

VERDICT: Approved to proceed
