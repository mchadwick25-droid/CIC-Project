Simulated review — informational only, not an Article 31 substitute.

# lpc change order of 2026-09-30: independent verification

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** claude-sonnet-5-5
- **Reviewer agent:** independent change-order verifier (fresh context, high effort; read nothing of the drafting sessions)
- **Drafter agent:** change-order drafting sessions that authored commits fa36b1b09, d3bec0e96, 3e82396b7, 2de852bf1 and d114068df
- **Round:** 1 (verification of an approved change order; not a revision round)
- **Truncation check, method 1:** row count by line pattern: `grep -cE '^\| \x60[0-9a-f]{8}\x60 \|'` on this file returns 59 (58 findings plus the note on 6516f231), and `tail -n 1` returns the closing line "End of verification.", both run after the last edit.
- **Truncation check, method 2:** set comparison in Python: the 8-hex claim ids extracted from the findings file (59 unique) equal, as a set, the ids in this file's per-finding table (59); no id is missing on either side.
- **Scope:** OG-29; `Build/Ministry/Operations/Audits/lpc_Claims_Verification_Findings_2026-09-30.md` (read in full); commits fa36b1b09, d3bec0e96, 3e82396b7, 2de852bf1, d114068df.
- **Verdict:** every one of the 58 findings is corrected at its cited place, and no Confidence letter, tier, classification or verdict changed. The change order is not complete: old wording survives in 11 live places (P1) and in lesser copies (P2), and 7 corrections cite sources this world has not licensed. Details below.

## Method

1. For each finding I read the new wording at the cited line in the file as committed at d114068df.
2. I checked each cited source line in the vendored file under `cic/texts/`, located by its structural marker: the `div2`/`div3` id and title in the NPNF/ANF XML files, the `<div n=>` section in the Hartel TEI files, and the heading or sermon number in the OCR files. The markers used are recorded in the table notes.
3. I swept every live surface named in the dispatch for each old phrase. The surfaces were `Build/worlds/lpc/*.md`, `Representative/`, `Story-Chunks/`, `Lexicon-Chunks/`, every type under `records/lpc/`, `scripts/*.py`, both indexes, `cic-website/`, `cic-poc/` and `packages/`. The claims registers, `lpc_Decision_Log.md` and `Open_Gaps_Tracking.md` are audit trail and quote old wording by design, so they are excluded.
4. Generators: I ran s21, s22, s24, s25 and s28 in a scratch copy of the tree and compared the output with the committed records field by field. Nothing in the repository was written. As a baseline, I ran the same five scripts at 232f89b9e (before the change order) against the records of that commit. The two comparisons give the same result on all 16 edited records. So the change order added no drift between generator and record. The fields that differ were already different before it: later canon and narration passes rewrote them. Every field that matched before still matches: the-silent-century, womens-own-voice, the Duval and Granfield sources, the world_core `cautions` and `thin_topics`, and the sesterces `claim_guards`. I also regenerated `lpc_Force_Index.md` and `lpc_Story_Index.md` in scratch. Both came out byte-identical to the committed files.
5. Classification guard: `git diff 232f89b9e d114068df` changes no `citation_specificity`, `verification_state`, `evidentiary_weight`, `formation_confidence` or tier field, no Registry Confidence letter, and no Doc_04 classification cell.

## Per-finding table

Status key: **closed**; **closed, cites unlicensed source** (the claim is now true at source, but the new wording leans on a text no Registry row licenses; see P1-A and P1-B); **not closed**; **not applied**.

| id | status | note |
|---|---|---|
| `f9dafd30` | closed, cites unlicensed source | Doc_04:94 true against ANF05 Ep. LXXI (`iv.iv.lxxi`, l. 38407), LXXV (`iv.iv.lxxv`, l. 40606), LIV (`iv.iv.liv`, l. 35011), Firmilian LXXIV (`iv.iv.lxxiv`), preface l. 56854; NPNF101 Letter LIV (`vii.1.LIV`, l. 29896). Letter XLIII (`vii.1.XLIII`, l. 28126) is true at source but sits in the Donatist cluster, row 213, which licenses only Letter LIII; Doc_04:90 calls it Row 11, which excludes that cluster (P1-A). |
| `0c59cde1` | closed | Doc_02:120 matches Hartel Praefatio, row 194 file ll. 39116–39134 (De duplici martyrio: Diocletian and Maximin, Erasmus suspected; Paschae Computus: a. 243). |
| `40334bfa` | closed, cites unlicensed source | Doc_04:92 awareness/formation split is true (ANF preface l. 56852–56855; Hartel Sententiae ll. 107–109). New sentences checked: "episcopus episcoporum" only of Christ in Guelferbytanus 32 (l. 9557; index l. 14856); En. in Ps. 36 serm. 2 Primianus passage (PL 36–37 file ll. 27920–27990). Cites Letter XLIII (P1-A) and the Psalmus contra partem Donati (P1-B). |
| `7ee09661` | closed | Doc_05:257. |
| `1110900c` | closed | Doc_04:14. |
| `5c06ab34` | closed | Doc_02:57. PL XI Gesta: "29. Possidius episcopus ... dixit" l. 125618, "Recognovi" l. 125624, further speeches ll. 128141, 128457; corpus map entry `role: context` confirmed. |
| `290e910e` | closed | Doc_02:45. |
| `b60536ca` | closed | Doc_03:46 "set himself up" matches ANF l. 56872. The same "nine rounds" overstatement survives elsewhere (P2-1). |
| `4dd89771` | closed | Doc_03:30; third attribution at Weiskotten ll. 1817–1821. |
| `77949f87` | closed | Doc_03:63. |
| `f945a231` | closed | Doc_05:195. |
| `665fd6b0` | closed | Doc_02:109; Doc_01 §2 l. 35 carries the asymmetry. |
| `c403950b` | closed | Doc_05:27; Pontius *Life* 11 (`iv.iii`, l. 28003); Harnack ll. 376–381, 4361. |
| `9e5090d0` | closed | Doc_05:281. |
| `09e32fac` | closed, cites unlicensed source | Doc_05:175 true; Psalmus cited (P1-B). Psalmus text: Petschenig file ll. 1293, 1608–1613; Retractationes (Knoll) ll. 6830–6834. |
| `a187ea83` | closed | Doc_05:151; Ep. LXIX (`iv.iv.lxix`, l. 38062). |
| `1b8bdab8` | closed | Doc_06:61. |
| `12785a57` | closed | Doc_07:186. |
| `bfad9bc9` | closed | Doc_07:128; Ep. IV (`iv.iv.iv`), Ep. XXXV (`iv.iv.xxxv`), Ep. XXXVII (`iv.iv.xxxvii`, "sent you as my substitutes"), Ep. XXXIV, Letter XXI (`vii.1.XXI`). Minor compression on Ep. XXXV (P2-7). |
| `b005b155` | closed | Doc_07:62. The same defect survives at Doc_08:371 and World Profile:392 (P1-D). |
| `5e5e442b` | closed | Doc_07:94. |
| `6c30b049` | closed | Doc_07:128. |
| `d8a49b93` | closed | Doc_08:297, :125; *Life* 9–11 (`iv.iii`, ll. 27939–28003). |
| `31abcdcc` | closed | Doc_08:302; Confessions V.8 (`vi.V.VIII`, l. 8104). The caveat is missing at other copies (P2-3). |
| `ae707134` | closed | Doc_08:264. |
| `53939147` | closed | Doc_08:330. |
| `8903963f` | closed | Doc_09:180. Doc_04 §7 item 6 is CLOSED (l. 212). Stale counts survive in Doc_04 and Doc_06 (P2-2). |
| `82d0c263` | closed | World Profile:554. |
| `be767c0a` | closed, cites unlicensed source | World Profile:128 cites the Psalmus as "Registry row 214"; row 214 licenses the Latin *De Baptismo* only (P1-B). |
| `52aa9b06` | closed | World Profile:242. |
| `c168ca30` | closed | World Profile:188. |
| `0641c050` | closed | World Profile:216. |
| `8c8ff86b` | closed | World Profile:224; Ep. XXXIX names Virtius, Rogatianus, Numidicus (`iv.iv.xxxix`); XXXVII/XXXVIII correctly numbered in the ANF sense (the findings file had cited l. 32247 as XXXVIII; it is XXXVII). |
| `d610f6dd` | closed | lpcstory001:37. |
| `1aba44c7` | closed | lpcstory002:33. |
| `7a0e9082` | closed | lpcstory002:68; Ep. LIX (`iv.iv.lix`, "subjoined the names"). |
| `a5bad882` | closed | lpcstory003:33; *On the Mortality* 17 (`iv.v.vii`, ll. 47066–47092). |
| `85c2781c` | closed | lpcstory005:57. |
| `36bd8e42` | closed | lpcstory006:47; Sermo 309 retells Curubis/Paternus (row 227 file ll. 101262–101300). |
| `2e965f1d` | closed | contested cyprian-death-genre:50–54; generator s26 in step. |
| `3b49ec7e` | closed | lpcstory007:68; Prosper a. 430 ll. 54206–54211. |
| `64c5c68e` | closed | 133-year-silence force, description. |
| `649d0bf6` | closed | same record, manifestations. Morin ll. 1701–1703, 10850 (see P2-8). |
| `cf8ec194` | closed | the-silent-century:35–44. |
| `31bdac99` | closed | the-silent-century:49–50. |
| `fe19b3f1` | closed, cites unlicensed source | conciliar-authority gravity description; cites Letter XLIII (P1-A). |
| `83e3ecd6` | closed | term bishop-of-bishops senses.evidential. |
| `a40a3d7f` | closed | term bishop-of-bishops provenance quotes corrected Doc_06 §2.2. |
| `6ba65352` | closed | lpclex012:59. |
| `f80a4c45` | closed, cites unlicensed source | term plenary-council ll. 32–34, 69–71; Psalmus (P1-B). |
| `59fc6359` | closed, cites unlicensed source | lpclex013:59; Psalmus (P1-B). |
| `77d40657` | closed | grace gravity; Ad Donatum 4 (`div n="4"`, l. 256), Ad Quirinum III.4 heading (l. 3300); the English "All our power is of God; I say, of God" is verbatim ANF (To Donatus, l. 28427); NPNF105 l. 18089. |
| `c7aafc6f` | closed | figure possidius:42. Stale docstring in s24 (P2-5). |
| `98c89607` | closed | the-psalms-on-the-wall absent_detail. |
| `94dc0428` | closed | womens-own-voice. Letters XXV/XXX headings ll. 24531, 25665–25675; Goldbacher l. 3976; Knopf no. 16 §VIII ll. 5771–5783. Doc_09:126 is not reconciled (P1-C). |
| `d730e7a3` | closed | Duval source record and Registry row 60; Type column confirms M rows 63, 82, 107, 108, 129 (M/S), 136, 146 and 97 (S/M). |
| `8fdddf7d` | closed | Granfield source record and Registry row 113; row 186 licence confirmed. |
| `75d73052` | closed | term bishop-of-bishops provenance. Stale docstring in s22 (P2-5). |
| `6516f231` | closed (note) | sesterces claim_guards; Audollent l. 29034 "environ 25.000 francs". |

Counts: 58 findings. Closed: 51. Closed but citing an unlicensed source: 7. Not closed: 0. Not applied: 0. The note on 6516f231 is closed.

## Findings

### P0

None.

### P1

**P1-A. Letter XLIII is cited as this world's evidence, and as Row 11.**
- Where: Doc_04:90 ("Letters XLIII and LIV (Row 11)"), Doc_04:92 and :94, World Profile:126, the conciliar-authority gravity record (description, l. 79), and `wb_lpc_s25.py` ll. 709 and 714.
- Why it is wrong: Letter XLIII is one of the 11 letters in the Donatist cluster. Row 11 excludes that cluster in terms. Row 213 carries the cluster but licenses Letter LIII only, and the corpus map assigns the cluster to `donatism` with `role: context`.
- The quotation itself is true at source (`vii.1.XLIII`, l. 28126). The claim "recurs in more than one text" still holds on Letter LIV (row 11) alone.
- Fix: cite Letter LIV only, or license Letter XLIII at row 213. The second is a Registry decision.

**P1-B. The *Psalmus contra partem Donati* has no Registry row.**
- Where it is cited: Doc_04:92, Doc_05:175, World Profile:128 (as "Registry row 214"), lpclex013:59, and the plenary-council term record (twice).
- Why it is a gap: the corpus map assigns the Psalmus only to `donatism.yaml`. Row 214 licenses the Latin of *De Baptismo* for cross-checking; the Psalmus shares its printed volume and nothing more.
- What is true: the content is verified (Petschenig ll. 1608–1613; Retractationes ll. 6830–6834).
- Fix: add a Registry row for the Psalmus, or remove it from the wording. That is for the project lead, since it touches cross-world assignment.

**P1-C. Doc_09:126 still says no woman in this world's horizon left a narrative of her own.**
- It also says Perpetua is "the one North African woman who did".
- Why it is wrong: Quartillosa narrates her vision in the first person in the *Passio* of Montanus and Lucius ("quae in hunc modum quod uidit exposuit. Vidi, inquit, filium meum ...", Knopf no. 16 §VIII, ll. 5771–5783, row 231, Native, 259).
- Doc_09 now contradicts the corrected `lpc.limit.womens-own-voice` record and World Profile:620.
- The Story Index row 4 heading is derived from Doc_09 and follows it.

**P1-D. "Inaccessible wherever a non-episcopal voice would have had to carry it."**
- Where: Doc_08:371 and World Profile:392.
- Why it is wrong: this is the defect already closed at Doc_07:62 (b005b155). A deacon (Pontius), two lay confessors (Epistles XX–XXI) and Quartillosa all speak in their own voices.
- Fix: narrow it to the ordinary congregant, as Doc_07:62 now does.

**P1-E. Doc_05:291: "G5 fails Persistence while appearing in both phases, at one locus each."**
- This is the false premise corrected at Doc_04 §3 and §5 (f9dafd30).

**P1-F. "One attested locus in each phase, a century apart."**
- Where: `lpc_Gapped_Formation_Precedent.md`:33.
- This is the same false premise. The document was handed to the build by the project lead, so the project lead decides the wording.

**P1-G. The Representative construction documents carry the old G5 wording.**
- Phase1:96: "one attested locus per phase".
- Phase2:64: "one attested locus per phase" and "formed by, or even aware of".
- Phase3:35: "formed by or aware of".
- Phase7:62 quotes Doc_04's old Formation sentence verbatim ("...formed by, or even aware of..."). That sentence no longer exists in Doc_04, so this is now a stale quotation.
- The Permanent Prompt and the Voice Configuration carry no G5 awareness claim.

### P2

**P2-1. The preface-specific "nine review rounds" survives in several places.**
- Doc_02:17 says rows 12–13 (*On Baptism*, Letter 185) were "re-verified at source across Doc_01's nine review rounds".
- `Doc01_Round1_Review.md` read only the corpus map for Ep. 185. Its method section lists that work under "independent historical verification", not under vendored text. Round 1 did not read the 256 preface at source either.
- So "nine" is at most eight. The same count appears at:
  - Doc_04:34 (the 256 preface; Letters XXXI and CCXIII; Pontius);
  - the pastoral-office-flock-keeping gravity record, l. 17;
  - the sacramental-ordination-validity gravity record, l. 16;
  - `wb_lpc_s25.py` ll. 493, 514 and 813.

**P2-2. Two unresolved-tension counts are stale.**
- Doc_06:170 says "one open"; Doc_04:266 says "open".
- Both point at Doc_04 §7 item 6, which is CLOSED (Doc_04:212; OG-4).
- Docs 05, 07, 08 and 09 now correctly read "none open".

**P2-3. "Textual, not successive" appears without the Confessions V.8 oratory caveat.**
- Where: Doc_07:244; Doc_08:191; World Profile 184, 238, 366 and 768; Rep Phase2:33; `wb_lpc_s25.py` l. 1381.
- Doc_07:176, Doc_08:278 and :302, and World Profile 428 and 652 do carry the caveat.

**P2-4. Capsule Core:51 still gives the plague's outcome as teaching alone.**
- It reads "The sickness produced a bishop's own plain word to the dying" and "every pressure into something taught".
- This is not false as a statement of the best-attested response, and :47 now names the relief. The project lead decides whether :51 should also soften "every".

**P2-5. Generator docstrings keep old wording.**
- `wb_lpc_s22.py` l. 220: "sole textual ground ... Documented".
- `wb_lpc_s24.py` l. 125: "the sole source for lpcstory007".
- `wb_lpc_s25.py` l. 780: "not confined to one locus the way Candidate 5 is", a sentence removed from Doc_04.
- None of these reaches a committed field that matched before the change order.

**P2-6. Participant-facing wording in two changed fields needs work.**
- World Profile:622 now reads "for the women we name we have none of their own words ... we do not put words in her mouth". The pronoun no longer agrees with its noun, and the single sentence scores FK 21.3.
- The bishop-of-bishops `senses.evidential` field scores FK 13.2 and FRE 45.3, and carries build vocabulary ("re-verified at source", "vendored text"). The other senses of that record were already past the ceiling.
- The changed `description` and `statement` fields all pass: FK 7.3 to 8.6, FRE 60.5 to 70.2, scored with `engine.m1.gates.grade_text`.

**P2-7. Doc_07:128 overstates what the Rogatianus fund paid for.**
- It says Ep. XXXV has the clergy care for "the widows, the sick and strangers, from funds left with the presbyter Rogatianus".
- In the source, the Rogatianus portion pays only for needy strangers.

**P2-8. The Optatus attribution is Morin's report, not his own ascription.**
- Several records say the tractatus is one "Morin gives to Optatus".
- Morin reports that the tractatus is "alibi adscribitur", ascribed to Optatus elsewhere (the Orléans codex, l. 10850), and he judges that ascription not unlikely.

**P2-9. Doc_08:314's heading does not match its body.**
- The heading says "one force is registered with no cross-cell connection".
- The body then names 1B-3 as unconnected too.

## Checks the dispatch named

- **Doc_02:17 (rows 12–13, nine rounds).** Overstated; see P2-1.
- **Doc_08:371.** Not closed; see P1-D.
- **Doc_07:244.** Caveat missing; see P2-3.
- **Doc_09:126.** Not closed; see P1-C.
- **Gapped precedent:33.** Not closed; see P1-F.
- **Capsule Core plague paragraph.** :47 is corrected; :51 is P2-4.
- **Generators s21, s22, s24, s25 and s28.** Dry-run into `dry5` and compared semantically: no new drift (Method 4).
- **"None open" counts in Docs 05, 07, 08 and 09.** Correct. Docs 04 and 06 are stale (P2-2).
- **Scillitan statements in Doc_09:106 and :138.**
  - Guelferbytanus "XXX. De natale sanctorum Scillitanorum" is at l. 8466. It sits inside the 33 Augustine sermons, before the *tractatus novem* at l. 10297, and row 229 licenses those 33.
  - Caillau "SERMO XVI. IN NATALI MARTYRUM SCILLITANORUM" is at l. 58322 (OCR "SKRMO XVt").
  - Both are verified. Row 230 is a finding aid only. Doc_09 does not call it Augustine's, and it should keep not doing so.
  - Sermones CCLXXX–CCLXXXII are at row 227 file ll. 91963, 92185 and 92280. Verified.
- **Public surfaces.** `cic-website/tree/latin-pastoral-congregational-christianity.html` and the census entry carry none of the corrected claims. There is no lpc package and no lpc content in `cic-poc`.

## For the project lead

1. **P1-A and P1-B.** License Letter XLIII (row 213) and the *Psalmus contra partem Donati* (a new Registry row), or strike both from the wording. Licensing a text the corpus map assigns to `donatism` is a cross-world decision.
2. **P1-F.** The Gapped Formation Precedent is the project lead's document.
3. **P1-C, P1-D, P1-E and P1-G.** These are remaining copies of defects the approved change order already covers. They go into approved Docs 05, 08 and 09, the World Profile and the Representative construction documents. The project lead decides whether they fall under the same order or need a named extension of it.

End of verification.
