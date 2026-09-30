Simulated review — informational only, not an Article 31 substitute.

# The 133-year silence claim: independent verification of the correction in commit 15f6903ed (lpc)

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** independent-verifier subagent, fresh context, launched from session_01EgyL7xtErqj72CaFiEUx4q (wrote none of the text under review)
- **Drafter agent:** the lpc build-thread worker, commit 15f6903ed "lpc do-first 3b" (trailer "Claude Sonnet 5.5")
- **Round:** 35 (a verification of a correction that changed a claim, against Round 34's finding; not a new revision round)
- **Truncation check, method 1:** hash and tail comparison. For all 11 files changed in 15f6903ed, `git hash-object <path>` equals `git rev-parse 15f6903ed:<path>`, so the working tree is the committed text. Each file's last 50 bytes end on a complete sentence or on the `if __name__ == "__main__": main()` block. The later commit 15b3189b9 touches none of these files.
- **Truncation check, method 2:** structural parse. Both scripts (`wb_lpc_s25.py`, `wb_lpc_s28.py`) compile with `py_compile`. All four changed records parse as YAML front matter and have a body after the closing `---`. The Registry parses to exactly 272 numbered rows (1 to 272, no gap, no duplicate), each with 11 cells. Doc_02 has ten `## ` headings ending at `## 10. Disposition`. Doc_05, Doc_08 and Rep Phase 3 each end at `## Disposition`.
- **Date:** 2026-09-30
- **Scope:** `git show 15f6903ed`, then a sweep of every live lpc file for other copies of the claim.
- **Severity vocabulary:** P0 blocks, P1 must be fixed but does not disqualify, P2 polish.

## Verdict

**Not ready.** The restated claim is true for what it names, and every date, line and row it cites checks out at source. But it overreaches a second time. It leaves out two Native rows, 231 and 232. These hold two North African martyr acts written inside the gap by Cyprian's own church. One of them is a letter from its imprisoned clergy to the congregation, and it names Cyprian as the teacher of the faith they hold. The claim is rated Documented and described as "checkable against the Registry rows", so leaving these rows out is exactly the failure this correction was meant to fix. Whether these acts break the "silence of the congregational voice" is a world-level question for the project lead.

## Findings

### P0

**P0-1. Rows 231 and 232 are dated inside the gap, Native, and not named anywhere.** Rows 231 (Knopf–Krueger 1929, nos. 13, 15, 16) and 232 (Gebhardt 1902, nos. XI, XIII, XIV) carry the *Passio* of Marianus and Jacobus and the *Passio* of Montanus and Lucius. Both were added on 2026-09-29 in the same batch as rows 264 and 265. The checks below use the Knopf file, located by its section headings:

- **Marianus and Jacobus.** This is no. 15, from the heading `15. Martyrium des Marianus und Jakobus.` at line 5166 to the next heading at 5629. At line 5365, Cyprian appears in a vision seated beside the judge (`Cyprianus apparuit`). So the text postdates Cyprian's death.
- **Montanus and Lucius.** This is no. 16, from the heading at line 5629 to `17. Martyrium des. Fruktuosus.` at 6248.
  - It opens as a letter to the church: `Et nobis est apud uos certamen, dilectissimi fratres` (5632).
  - It exhorts the congregation to `concordiam, pacem, unanimitatem` (5865), then says `Haec omnes de carcere simul scripserant` (5871).
  - The brethren gather `pro religione et fide, quam Cypriano docente didicerant` (5918).
  - A vision comes `Cum adhuc ... episcopus noster solus passus fuisset`, and in it the writer asks Cyprian himself about his suffering (6135–6136).
  - Montanus's last address commends the presbyter Lucianus, `sacerdotio destinauit` (6203).

This is a pastoral and congregational voice from within this world's boundary, written after 258, and explicitly continuous with Cyprian's. It is not a bishop's voice. Doc_02 §7 argues that "the binding stands" only on the ground that "conciliar canons and documents of the Donatist dispute are not that". That argument does not reach these acts.

The omission affects every copy of the claim:

- Doc_02 §7 (line 119)
- Doc_05 §0.3 (line 27)
- Doc_08 lines 23 and 264 (264 carries the Documented rating)
- the force record's `divergence_note`, `description` and `manifestations`
- the limit record's `why_sources_cannot_answer`
- the world core, caution 2 (around line 268)
- `wb_lpc_s25.py` lines 1540–1582 and `wb_lpc_s28.py` line 883

The fix has two parts:

- **Needs the project lead:** do these acts leave the Doc_01 §5 binding standing, or do they partly break the silence? Neither the correction nor this review should settle that.
- **Mechanical, either way:** name rows 231 and 232 among the texts dated inside the gap. Both rows are "Not currently drawn on for a specific claim", so "this world draws on none of them" still holds.

### P1

**P1-1. Pontius's *Life* and the *Acta Proconsularia* are also dated inside the gap and not named.** The *Life* (rows 7, 40, 194, 205) narrates the martyrdom, so it was written after September 258. The anf05 text, `div2 id="iv.iii"`, looks back on it ("independently of his martyrdom"). Unlike every text the correction names, row 7 is drawn on: its Licensed-For cell covers Cyprian's election and the Curubis exile. Those are claims about the years before the gap, so the silence is not filled. But a claim graded Documented has to name these texts. The *Acta Proconsularia* (rows 41, 194, 231, 232) is a record of 258, at the gap's very edge. It should be named or explicitly set aside.

**P1-2. The world-core generator still carries the old false claim.** Commit 15f6903ed fixed `wb_lpc_s25.py` and `wb_lpc_s28.py` but not `wb_lpc_s21.py`:

- **Lines 4390–4393:** "THE CENTURY GAP (258-391) IS DONATISM'S OWN TERRITORY, NOT THIS WORLD'S ... this world's own vendored corpus, which holds nothing dated inside it". This is **false**. Re-running s21 would put it back into the world core.
- **s21 lines 4489–4490, and world core lines 409–410:** "richly attested elsewhere only through sources that are Donatism's own territory". This is **false**. Rows 26, 59, 202, 44, 88, 231 and 232 are all Native, all date inside the interval, and none is on the Donatism shelf.

There is also a wider mismatch. The world core's plain-language cautions and the force record's `description` are produced by no script: a search of every `.py` file finds their text only in the records. s21 and s25 would regenerate the older etic text (s25 would even use the older name, "Asymmetrically Attested"). The live records cannot be rebuilt from their generators.

**P1-3. The force record's spoken text and its Documented rating.** Line 37 of `lpc.force.transmission-asymmetric-span-133-year-silence.md` gives two exception groups, "canons from Carthage councils, and early writings of Augustine". It leaves out Doc_02's third group, the Theodosian Code constitutions in rows 44 and 88, along with the rows under P0-1 and P1-1. Lines 58–59 say the record of those years "belongs to another community, not to us". But Optatus (rows 27, 64 and 264) is Native in this Registry and wrote for the Catholic side, and so did rows 231 and 232. The text goes on to say "This is a fact about our record, and it can be checked against our sources". Until the list is complete, that check fails, so the Documented rating is not yet earned. The rating itself is the right level for a claim about the record once the claim is true.

**P1-4. Other live copies that are now false against the Registry.** Their final wording depends on the lead's answer to P0-1:

- **Doc_09 §7 item 1 (line 120) and line 23:** "There is no story from inside the 133-year silence, and there cannot be", and "none comes from the interval, and none can". Rows 231 and 232 hold dated stories from 259. The same claim appears in `Doc09_Claims_Register.md` rows `6be1f5c6` and `6db40b49` (both still UNVERIFIED) and in `lpc_Story_Index.md` line 93.
- **`lpc_Gapped_Formation_Precedent.md` line 21:** "no surviving voice native to this world's own boundary for the interval". This is **false**. Optatus (rows 27, 64 and 264) and rows 231 and 232 are Native.

**P1-5. World core caution 2 forbids more than the record does.** Its first sentence was kept by the correction: "Never describe what happened in those years from this world's own collection". But Doc_02 §8 lists Augustine's conversion (386) and baptism (387) in this world's Documented core sequence. Row 22 is licensed for "Augustine's own nine years as a Manichaean auditor before conversion", and those years fall inside 258–391. The instruction should be limited to a pastoral or congregational voice in the gap, which is Doc_02's actual scope. As it stands, it would forbid the Representative's own pre-ordination history.

### P2

- **The Optatus dates are not "per the vendored file headers" as written.** The row-27 file (`optatus_against-the-donatists.txt` line 5) and the Ziwsa scan (line 6) both read "c. 366-393 CE". Only the two TEI headers (rows 264 and 265, line 2) read "fl. 366-385". Ziwsa's own preface (scan line 309) gives "intra annos 375 — 385". Every one of these ranges falls at least partly inside the gap, so the substance holds, but the attribution should name which headers say what.
- **Doc_02's gloss of rows 26, 59 and 202 is narrower than their cells.** Doc_02 says they are "licensed for the council of 419 and the Apiarius affair". The cells for rows 26 and 202 actually read "institutional skeleton of this world's own conciliar life", and row 59 is licensed for row 26's Apiarius claim. The substance holds: no record and none of Docs 03–09 cites a Gratus or Genethlius canon (searched for "Genethlius", "Gratus" and "Code of Canons").
- **Doc_02's "licensed for their own claims and not for the gap".** This is imprecise for row 22 (see P1-5). Better: "not for a pastoral or congregational voice in the gap".
- **A half-old paraphrase: "richly attested — through sources that are Donatism's own territory (World #4), not this world's".** It appears in Doc_02 §7's first sentence, Doc_08 line 279, Doc_09 line 23, Rep Phase 2 line 31, and World Profile lines 26 and 652. It drops Doc_01 §5's "overwhelmingly", and Doc_02 §7's own list of Native gap texts now contradicts it. Restore "overwhelmingly" (s21 line 4275 already says "almost entirely").
- **World core caution 2 is looser than Doc_02.** It says "holds no bishop's pastoral voice", dropping "ordinary" and "congregational". Optatus was a bishop, and his Native work has pastoral passages, so the loose phrase is easier to refute than Doc_02's. Align it with Doc_02's wording.
- **The Theodosian Code locus is normalized.** The file prints `XVI,  2,  4  (321  lul.  3).` with doubled spaces (line 83906), but Doc_02 prints it with single spaces. The content is right.
- **The force record's voice.** It mixes "this world" and "Augustine ..." with "we/our". The sentence "(That sentence reports how the world understood itself. It is not a judgment of historical accuracy.)" reads as a disclaimer inside spoken text. Otherwise the sentences are short and plain.
- **A lead for the Library.** The Knopf file header lists further African acts inside the gap: nos. 19–22 and 29, the acts of Maximilian, Marcellus, Cassian, Felix and Crispina. Row 231 says these "are not assessed here and have no row". They sit outside the Registry, so they do not bear on the claim, but they belong to this world's window.
- **Outside this correction; flagged, not touched.** The lpc entry's `why` field in `cic-website/data/world-census.json` says Augustine "preached to the same Hippo congregation", yet Cyprian's see was Carthage. Separately, the Registry's status line carries process narration ("This file has been edited after that recheck; no review artifact covers those edits"), which is commentary in a canonical file.

## What was verified at source (by structural marker)

- **Optatus.** Rows 27, 64 and 264 are all Native. The header dates are as given under P2.
- **Row 265.** It is Excluded, with the reason Named Comparandum. The appendix's first document sits in TEI `div n="1"`, where lines 129–130 give the consular formula `Constantino Maximo Augusto et Constantino iuniore nobilissimo caesare consulibus ... Thamugadiensi`. The last document sits in `div n="10"`, which ends with `data Non. Februar. Serdica.` at line 1648. Doc_02's description is accurate.
- **Row 26.** In `npnf214`, `xv.iv.ii-p12` reads "Carthage (under Gratus)—345–348" and `-p13` reads "(under Genethlius)—387 or 390". Both sit inside the Introductory Note, `div3 xv.iv.ii`, of the Code of Canons (`div2 xv.iv`). In Canon II (`div4 xv.iv.iv.iii`), `xv.iv.iv.iii-p8` names Genethlius.
- **Row 202.** In Bruns, `CONCILIUM CARTHAGINENSE PRIMUM` / `TEMPORE JULII L PAPAE ?)` (as the OCR prints it) is at lines 7854–7855, and Gratus follows at 7858.
- **Rows 44 and 88.** Mommsen–Meyer has `XVI,  2,  4  (321  lul.  3).` at line 83906. The Latin Library file holds constitutions of Constantine (line 43 onward).
- **Rows 11, 22 and 25.** Letter I is dated a.d. 386 (`npnf101`, `vii.1.I-p2`). *De Moribus Ecclesiae Catholicae* is dated a.d. 388 (`npnf104`, `iv.iv.ii-p3`). The *Soliloquies* were "written ... shortly after his conversion (387)" (`npnf107`, `ii-p8`), and row 25's title lists the *Soliloquies*.
- **Row 227.** `CLASSIS  V.` is at line 117124, `SERXffONES  DUBII.` at 117125, and `CLASSIS  IV.  DE  DirERSIS.` at 106615, as the row states.
- **Row counts.** The Registry has 272 rows. Ten are Excluded: 28, 29, 98, 128, 204, 245–248 and 265. `records/lpc/source` holds 208 files, and their `lpc_source_registry_row` values are exactly rows 1–213 minus 28, 29, 98, 128 and 204. That leaves 54 rows above 213 without records (59 minus 5 Excluded). World core line 436 is correct.
- **The Letter LIII list.** In `npnf101` (`vii.1.LIII`, a.d. 400), the list runs forward from Linus to Siricius, "whose successor is the present Bishop Anastasius". The corrected witness text matches, and its quotation is verbatim.
- **Rep Phase 3 line 80.** The quoted phrase "Out-of-Boundary for this world by prior ruling" is present in row 204.

## Sweep: remaining copies of the old or half-old claim

| Location | Text | Status |
|---|---|---|
| `scripts/wb_lpc_s21.py` 4390–4393 | "DONATISM'S OWN TERRITORY ... holds nothing dated inside it" | **False**: the old claim (P1-2) |
| `scripts/wb_lpc_s21.py` 4489–4490; world core 409–410 | "richly attested elsewhere only through sources that are Donatism's own territory" | **False** ("only") (P1-2) |
| `lpc_Gapped_Formation_Precedent.md` 21 | "no surviving voice native to this world's own boundary for the interval" | **False** (P1-4) |
| `Doc_09_Story_Inventory.md` 23, 120; `Doc09_Claims_Register.md` `6be1f5c6`, `6db40b49`; `lpc_Story_Index.md` 93 | "no story from inside ... and there cannot be" | **False** against rows 231 and 232 (P1-4) |
| Doc_02 §7, Doc_05 27, Doc_08 23 and 264, force record, limit record, world core ~268, s25 1540–1582, s28 883 | "no ... bishop's ordinary pastoral or congregational voice ... texts dated inside include ..." | True as far as it goes, but **incomplete** (P0-1, P1-1, P1-3) |
| Doc_02 §7 first sentence, Doc_08 279, Doc_09 23, Rep Phase 2 31, World Profile 26 and 652 | "richly attested — through sources that are Donatism's own territory" | **Half-true paraphrase**: needs "overwhelmingly" (P2) |
| Permanent Prompt line 21, `lpc_World_Capsule_Core.md` 79, limit `statement`, World Profile 26 and 428, Rep Phase 1 82, Rep Phase 2 31 | "your own congregational voice falls silent" | **Depends on the lead's P0-1 decision**. Rows 231 and 232 hold a congregational letter from 259 |
| World Profile 26 and 652, Doc_09 120 | "row 27 ... Native ... writing inside the interval" | **True**, but incomplete: rows 231 and 232 are the stronger case |
| Doc_05 251 | "no attested institutional chain ... across its own 133-year gap" | **True** as checked |
| `cic-website`, `cic-poc/frontend`, `packages/` | none found | No lpc copy of the claim. `world-census.json` says only "Donatism contests its interval" |

## For the project lead

1. **P0-1: do the martyr acts of 259 break the silence?** Rows 231 and 232 hold the *Passio* of Montanus and Lucius and the *Passio* of Marianus and Jacobus. The first is a clergy letter to Cyprian's congregation written inside the gap, which names Cyprian as the teacher of its faith. Does it leave Doc_01 §5's "silence of a voice continuous with Cyprian's ordinary-pastoral mode" standing? This is a world-level decision. Its answer sets the wording of Doc_02 §7, Doc_08 3B-2 (Documented), Doc_09 §7 item 1, the Permanent Prompt line 21, the Capsule and the limit record.
2. **Rebuilding records from generators.** Should the plain-language rewrites of the world core cautions and the force description be carried back into s21 and s25, so that the records can be rebuilt from their generators (P1-2)?
