Simulated review — informational only, not an Article 31 substitute.

Reviewer model: claude-opus-5-5
Drafter model: claude-sonnet-5-5
Reviewer agent: Doc_10 round 3 recheck, fresh context, medium effort, targeted; read the round-2 review, OG-69 and the current files, nothing of the fixing session
Drafter agent: the round-2 fix session (Sonnet), commit 0b0cbb6e4, recorded in `Open_Gaps_Tracking.md` OG-69
Round: 3 of 3 for Doc_10, the last round under the cap (`roundcount lpc 10 --check-new` passed before this file was written; 2 earlier review files on record)
Truncation check, method 1: heading count and closing line. `grep -cE '^### R[0-9]+ '` on this file returns 4 residual-item headings, and `tail -n 1` returns "End of review.", both run after the last edit.
Truncation check, method 2: set comparison in Python. The ids in the summary table (N1–N3, R1–R4) equal, as a set, the ids of the verdict table (N1–N3) together with the `###` residual-item sections (R1–R4). The reviewed files were checked the same two ways: each file's byte count on disk equals `git cat-file -s HEAD:<path>` (Doc_10 77,713; Permanent Prompt 22,264; compel demonstration 4,501; world_core 31,436; Correction of the Donatists source record 2,405), and each ends on a complete sentence. The compiled prompt (the package pinned at the time (its compiled prompt), 85,017 bytes, not tracked by git) ends on the last sentence of the road-back demonstration.

# Round-3 recheck of Doc_10, Representative Construction Notes: Datus (`lpc`)

**Scope.** Only N1, N2 and the optional N3 of `Review-Artifacts/Doc10_Round2_Review.md`, against the files as changed by commit `0b0cbb6e4` and the pinned package (`records/worlds/lpc.yaml`: the package pinned at the time). N4 and N5 were optional and are not rechecked.

## Verdict

**No substantial finding; approved to proceed** for Doc_10. N1 clears: no Doc_10 surface, no voice record and nothing in the compiled prompt states the council's year. The demonstration and the Prompt still tell Letter 185 §§25–26 correctly without it. N2 and N3 clear. Four residual items remain (R1–R4). R1 is a one-character fix in the Prompt file and needs no review. R2–R4 sit outside Doc_10, in records, the generator, Doc_02 and the OG-69 entry, and none reaches the compiled prompt. They go to their owners and to the project lead. None of them blocks Doc_10.

## Gates run directly

| Check | Result |
|---|---|
| `roundcount lpc 10 --check-new` | PASS (2 review files on record before this one) |
| `prereview lpc --doc 10` | PASS on all five checks (m2 build 22 gates, 0 failing; bar screen 13 voice-diet fields, 0 over FK 10; cross-world 0 new; holdings). The run rewrote `build/lpc_Prereview_Doc10.txt` (one line) |
| `records lpc` | PASS |
| `regate lpc` | PASS. 274 public fields, 191 new or edited; 150 below FK 8, reported and not failed |
| `gaps lpc` | PASS |
| `claims lpc` | PASS. 113 derived, 113 registered, 1 UNVERIFIED (not a Doc_10 claim, as in round 2) |
| `deployed lpc` | PASS at pin 2026-10-01T15-13-39Z |
| Six-word overlap between any two demonstrations (Python, Representative turns) | None |

## Verdicts on the round-2 findings

| id | verdict | evidence in the current files |
|---|---|---|
| N1 | resolved | See "N1 in detail" below |
| N2 | resolved | Doc_10 l. 152 and l. 446 now name `compiled/prompt.txt` "in the pinned package (its location is the `package` block of `records/worlds/lpc.yaml`)". No timestamped package path remains in Doc_10. l. 241 and l. 332 use the placeholder `packages/lpc/<pin>/`, which names no directory |
| N3 | resolved | Doc_10 §1 l. 39: "the ordinary believer is heard almost only through them (Doc_01 §8 item 3; Doc_02 §6)". This now fits Doc_02 §6's two lay letters. The wording differs from round 2's suggestion but says the same thing |

### N1 in detail

**(1) No statement of the year as fact on any voice surface.** A grep for `401` and `404` returned no hit in the compiled prompt, in `records/lpc/demonstration`, in `records/lpc/world_core`, in the Permanent Prompt, in Doc_10, in `lpc_Voice_Configuration_Datus.md`, in `lpc_World_Capsule_Core.md`, or in `Lexicon-Chunks`, `Story-Chunks` and the `lpcctx` chunks. The compiled prompt carries the new demonstration sentence (l. 533) and the new caution 5 (l. 157). The remaining hits in `records/lpc` are the Letter 93 source record (R2) and the Correction of the Donatists source record, which now names both datings. Two other hits are unrelated: line numbers 20392–20404 and an archive.org item id. `Representative/lpc_Rep_Phase5_Boundary_Testing_Round1.md` (l. 162, l. 183) and `lpc_Decision_Log.md` (l. 2082) say "the 401 measure". They are dated audit records of a past test run, not compiled, and are left as history. Doc_02 and Registry row 12 are covered under R3.

**(2) The Letter 185 events, told without the year, hold at source.** The source is NPNF104 `div3 id="v.vi.ix"`, l. 19624–19640. Each point holds:

- "Then our bishops in council agreed to petition the emperors for one narrow thing" matches "it was decreed in our council" (§25).
- The fine falls on the rival clergy, "only in the districts where their people had attacked ours". Source: "only in those districts where the Catholic Church suffered any violence from their clergy, or from the Circumcelliones, or at the hands of any of their people".
- "He was one of the brethren who wanted it kept that narrow" matches "certain of the brethren, of whom I was one".
- "The envoys came back without it" matches "our envoys could not obtain what they had undertaken to ask" (§26).
- "A wider law had already gone out, with fines and exile for the rival bishops" matches "a law had already been published ... a pecuniary fine was ordained, and sentence of exile was pronounced against their bishops or ministers".

Prompt l. 23 tells the same events and holds as well. The only trace of the year at this locus is the editor's endnote 2521 (l. 19631), which the voice no longer uses. The Scope note now reads "a decision of the council to petition the emperors", which is accurate.

On the Craft/Focus bar for the compel demonstration:

- (a) holds. The second turn answers the press in its first sentence.
- (b) holds. The closing sentence is unchanged ("He called the laws a kind of medicine for hearts that words could not soften").
- (c) holds. There is no six-word overlap with any other demonstration (checked in Python).
- (d) holds. The hedge keeps the contested record's two alternatives.
- (e) holds. Letter XCIII's towns are still told as a scene.

The removal leaves the first turn grammatical. "Then our / bishops in council agreed" reads as one sentence.

**(3) The source-record sentence on the two datings.** The record now says: "the NPNF footnote dates it 401; the Code of Canons' note and Hefele-Leclercq date it June 404". Each part was checked at source:

- **NPNF footnote** (l. 19631): "That of Carthage, held June 26 (more correctly, probably June 15th or 16th), 401." Holds.
- **NPNF214** l. 35826–35831, note before Canon XCIII: "The most glorious emperor Honorius Augustus, being consul for the sixth time, on the Calends of July, at Carthage ... Theasius and Euodius received a legation against the Donatists." The year holds: Honorius's sixth consulship is 404. But the English note gives the Calends of July (1 July), not June.
- **Latin edition** (Bruns) l. 12659–12663: "Honorio augusto sextum consule, Kalendas Julias *)". Its apparatus (l. 12687–12688) gives the variant readings XVI, VI and XII Kal. Jul., that is 16, 26 and 20 June.
- **Hefele–Leclercq** l. 4882–4884: "Au mois de juin de l'année 404, le IX^e concile de Carthage ... députa aux empereurs ... deux évêques, Théase et Evode." Holds. At l. 4911–4915 it places Honorius's edict, with fines and exile, before the envoys reached him. That matches Letter 185 §26.

So the year 404 is accurate for both sources. "June" is Hefele's dating and the apparatus readings of the Latin, but not what the English note says. This is a precision point in a record outside Doc_10 (R4). It does not change N1.

**(4) world_core caution 5 is still true.** It reads: "Between them falls the council that Letter 185, section 25, records. These are three different years under different emperors." The council falls between 392 and 412 on either dating. The imperial college differs in each of the three years: Theodosius I in 392; Arcadius and Honorius in 401 or 404; Honorius and Theodosius II in 412. The caution holds without naming the council's year. Caution 4's "early in his time as bishop" also holds on either dating (bishop 395/396–430).

## Summary of findings

| id | severity | where | subject |
|---|---|---|---|
| N1 | resolved | compel demonstration; Prompt l. 23; world_core caution 5; compiled prompt | council year removed from every voice surface; events still correct |
| N2 | resolved | Doc_10 l. 152, l. 446 | pin-independent package citation |
| N3 | resolved | Doc_10 §1 l. 39 | "almost only through them" |
| R1 | new, mechanical | Prompt l. 23 | stray comma left by the N1 edit |
| R2 | new, owner's file (not Doc_10) | Letter 93 source record l. 42; `wb_lpc_s21.py` l. 665–668, l. 2100 | "the 401 council" still stated as fact; generator out of step with the edited record |
| R3 | new, for the project lead (not Doc_10) | Doc_02 §1 l. 17, §8 l. 124; OG-69 | OG-69 misplaces and understates Doc_02's use of 401 |
| R4 | new, optional (not Doc_10) | Correction of the Donatists source record l. 18; OG-69 | "June" is not what the Code of Canons' English note says |

## Residual items

### R1 Prompt l. 23: stray comma

The N1 edit left "Then our bishops in council, agreed to ask the emperors for one narrow measure." The comma splits subject from verb. The Prompt file is not compiled into `prompt.txt`, so nothing deployed carries it. **Fix:** "Then our bishops in council agreed to ask the emperors for one narrow measure." This is mechanical and needs no review.

### R2 The Letter 93 source record and the generator still state 401 as fact

`records/lpc/source/lpc.source.augustine-letter-93-to-vincentius.md` l. 42 reads "a real but narrow solicitation of legal protection, argued but not granted, at the 401 council row 12 records". Round 2 named this record for the same change, and it was not edited. The generator `Build/worlds/lpc/scripts/wb_lpc_s21.py` still carries the old text in two places. At l. 2100 it has the same Letter 93 sentence. At l. 665–668 it has the Correction of the Donatists divergence note, with "the 401 council" in its second clause, although the record itself (l. 18) was edited. A rerun of the generator would put the year back into that record. Neither record is compiled, so this is not a Doc_10 defect.

**Fix, for the record owner, in one change:**
- Letter 93 record l. 42 and generator l. 2100: replace "at the 401 council row 12 records" with "at the council Letter 185 section 25 narrates (row 12)".
- Generator l. 668–669: replace "the 401 council," with the record's current l. 18 text, "the council Letter 185 section 25 narrates (...)", in whatever final wording R4 settles on, so that generator and record agree.

### R3 OG-69's account of Doc_02 is inaccurate

OG-69 says "Doc_02 section 7 and Registry row 12 already attribute 401 to NPNF's footnote and do not assert it, so they stand." Registry row 12 does attribute it. Doc_02 §7 (l. 118–121) does not mention 401 at all. The uses are elsewhere:

- **§1, l. 17.** One use is attributed ("at a council NPNF's own editorial footnote dates 401"). Two are not: "after the 401 council that follows it in this sequence" and "not a contemporaneous 401 text".
- **§8 Confidence Map, l. 124.** "The 401 African council" is listed in "the core dated sequence" under **Documented / Widely Accepted**.

A council did meet at Carthage in 401, so the phrase is not false on its own. But in §1's sequence it is the petition council, and §8 rates it Documented while two of the world's own sources date that petition to 404.

Doc_02 has been approved to proceed, so any correction is a change order and the project lead's decision. This review does not make it. OG-69 already logs that decision as open. That entry should be corrected by a new appended entry, because entries are append-only. The new entry should name §1 l. 17 and §8 l. 124 in place of "section 7". It should also record that §8 currently rates the year Documented, which bears on the Contested question OG-69 raises.

### R4 "June 404" and the Code of Canons' note

As shown under N1 (3), the English note before Canon XCIII dates the council "on the Calends of July" in Honorius's sixth consulship. That gives the year 404 and the day 1 July. June comes from Hefele–Leclercq and from the variant readings in the Latin edition's apparatus. The record sentence and OG-69 both say the Code of Canons' note dates it to June 404. That is imprecise on the month and accurate on the year. **Optional wording**, record l. 18: "(the NPNF footnote dates it 401; the Code of Canons' note dates it to Honorius's sixth consulship, 404, and Hefele-Leclercq to June 404)". Apply the same wording to generator l. 668.

## Round record

This is round 3 of 3 for Doc_10, the last round under the cap. Round 3 checked only N1, N2 and N3, against the round-2 file. All three are resolved. The four residual items are one mechanical fix (R1) and three items outside Doc_10 (R2–R4) for their owners and the project lead. None is a substantial finding against Doc_10. Doc_10 is approved to proceed. That approval does not close anything: Phase Five boundary testing on the pinned package and full-system review remain open.

End of review.
