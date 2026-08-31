# Source Registry — Independent Review, Round 1

**Reviewed document:** `cappadocian_Source_Registry.md`, first draft (99 rows), 2026-08-31.
**Reviewer:** independent Opus-tier agent, fresh context, no prior involvement in drafting.
**Method:** read the Registry in full, plus its governing template (`L3B-World-Build-Methodology/Source_Registry_Template.md`), `cappadocian_Doc_02_Source_Ecology.md`, `cappadocian_Doc_01_World_Identification.md`, `cic/texts/README.md`, and `CAPPADOCIAN_BUILD_LEDGER.md` §9.

This file is the review's verbatim output, preserved as the actual review artifact per this project's build-cycle discipline ("review rounds exist as files, not claims"). It is not edited for content after the fact; corrections to what it found are recorded in the Registry's own living-document log and in Round 2/3's own files.

---

I've read all five documents in full and cross-checked the Registry row by row. Here are my findings.

## Headline: the highest-priority check passes clean

**Confidence-A discipline is correct.** There are exactly eight A rows — 16, 19, 25, 40, 47, 53, 61, 62 — covering nine files, and every one is a Mark-supplied file verified in the current session per Ledger §9 and the `cic/texts/README.md` notes. No NPNF/ANF volume is rated A anywhere; every row citing `npnf20x`/`anf0x` is B or lower with an explicit "present since 2026-08-15, not re-verified this session" note. The A-row Verification Notes also match the README's own per-file completeness records in specific detail (68 footnotes for Padelford; 23 for Whiston; 241 for Walford; Loeb |245–|293 for Wright 1913; Letter 36 between 35 and 37; Bishop Araxius and the printer's colophon for the Macrina Vita). I looked hard for a slipped A and did not find one.

**Two other things the brief worried about are also right.** Part F is entirely Native, with an explicit header note stating the rule correctly — the copyright/vendoring-vs-boundary error is not made. And rows 52/53 (the fifth-century church historians) are correctly Native, not Excluded on date, which is the harder version of the same call. Every filename the Registry cites exists under that exact name with the rights and dates claimed.

---

## MUST-FIX

### 1. The document's central self-claim is false: "Every source Doc_02 §§1–6 names has a row below" (lines 9, 192)

Nine named sources have no row.

| Missing | Where Doc_02/Doc_01 names it | Fix |
|---|---|---|
| **The *Philocalia*** | Doc_02 §5 debate (5), §9 Contested list; Doc_01 §2 (the Origen-via-Caesarea-Maritima channel) | Add a row. It is **vendored** — `origen_philocalia_lewis1911.txt`, PD, 2026-08-21 — so it is at least B. It is also the Registry's most interesting untaken boundary case (a compilation by this world's own authors of another world's author), and it currently appears nowhere in the document. |
| **Gregory of Nyssa, *Ad Graecos*** | Doc_02 §1.3, `[CORRECTED]`, explicitly "remains ungrounded and belongs in the manifest's gap list" | Add a named-gap row. Row 33's note mentions it only to say npnf205 excludes it — but the other two exclusions in that same sentence (Life of Macrina, Ecclesiastes homilies) *did* get rows 40 and 44. |
| **Gregory of Nazianzus, Oration 14, *On the Love of the Poor*** | Doc_02 §1.2 (bolded) | Add a row. The Registry gave Orations 2, 4, 5, and 43 their own rows despite all being "within the general corpus," so folding 14 into row 24 is inconsistent — and Oration 14 is the load-bearing text for the poor-institutionalized gravity candidate. |
| **Gregory of Nyssa's homily on Theodore the Recruit** | Doc_02 §3 martyr homilies | Add a row or an explicit coverage note. The word "Theodore" appears nowhere in the Registry (the one hit is "Theodoret"). Row 18 covers Basil's martyr homilies only; row 70 covers *In XL Martyres* II only. |
| **Armenian Christian literature** | Doc_02 §6.6 — ruled out because it "begins after Mashtots' alphabet, c. 405, after this world's own c. 394 close" | Add an **Excluded / Out-of-Boundary** row. This is the cleanest textbook Out-of-Boundary case in the whole world (a straightforward temporal mismatch, explicitly adjudicated in Doc_02) and the Registry has no row for it. |
| **Maraval 1988; Pouchet 1992** | Doc_02 §1.1, named parenthetically as the redating literature | Add rows. This is the scholarship grounding Basil's death year 377 — a claim Doc_02 says "moves a dependent chain, not one isolated date" and carries in §5 debate (3) and §9. It is the most load-bearing uncited scholarship in the document. |
| **Cavallin; Hübner; Zachhuber** | Doc_02 §1.1, named as holding the Ep. 38 reassignment position | Add rows. They appear only as prose inside row 20's Verification Note. Drecoll — named in the same sentence — got row 88. |
| **Rudberg** | Doc_02 §1.1, "manuscript families and growth studied by Rudberg and catalogued in Fedwick's *BBU*" | Add a row. Fedwick, named in the same clause, got row 89. |
| **Morison, *St Basil and His Rule* (1912)** | Not in Doc_02 — but it is one of the ten files Ledger §9 records as supplied and verified this session, is vendored PD, is secondary scholarship whose subject is this world (Native), and carries translated primary excerpts of Basil's Proems to the Longer and Shorter Rules plus Gangra's decrees (README, `morison_...` note) | Add a row at Confidence A. The Registry's own header (line 13) frames "the ten files Mark supplied 2026-08-30/31" as its A-tier set, then rows only nine of them. |

**Root cause worth naming to the drafting thread:** Part F was built from Doc_02 §5's scholarship list alone. Every one of §5's twenty-four names has a row; every scholar named *elsewhere* in Doc_02 (all in §1.1) is missing. That is a mechanical, findable pattern, not four independent slips.

**Also under-covered (lower severity but same class):** Basil's canonical letters *as a body* (Epp. 188/199/217) have no row — Part C's parenthetical points at "row 6/5," but row 6 is only canon 21 and row 5 is the undifferentiated letter corpus, while Doc_02 §2 treats the canonical letters as a distinct, heavily-used source ("the single best window this world offers on ordinary village sin"). Doc_02 §2's baptismal exhortations (Basil's protreptic; Nazianzen's oration on baptism) and Basil's Neocaesarean antiphonal-psalmody letter get neither a row nor a coverage note. And Gangra **canon 3**, named at Doc_02 §6.3 as against-the-grain evidence on the enslaved, is missing from row 50's Licensed For (which lists only canons 13 and 17).

### 2. Broken cross-references — six of them

- **Row 13**, Licensed For: "row 30's cross-reference (Eunomius' own Apology...)". Row 30 is Nazianzen's funeral orations on Caesarius/Gorgonia/the elder Gregory. Eunomius' Apology is **row 47**.
- **Row 14**, Licensed For: "completed by Gregory of Nyssa's *On the Making of Man* (row 22)". Row 22 is Basil's Ep. 8/Evagrius. Correct target is **row 39** — which itself correctly back-references row 14, so the error is one-directional.
- **Row 92**, Source: "'On Not Three People' (in Coakley, ed., row 96)". Row 96 is Brian Daley. Coakley's edited volume is **row 99**.
- **Row 75**, Verification Note: "see rows 84–101". **Rows 100 and 101 do not exist** — the Registry ends at 99. The intended range is 76–99.
- **Row 69**, Verification Note: bishops "independently well attested via the church historians (row 52) and secondary literature (row 84 onward)". Row 84 is Holman, *The Hungry Are Dying* — the poverty homilies, not the 381 communion law. Van Dam (row 82) is the plausible target.
- **Rows 83 and 84**, Licensed For: both cite **"Doc_01 §9."** Doc_01 has no §9 — it ends at §5. The content cited (the Sterk-line monk-bishop synthesis and the Holman-line civic reading, both under "Dominant Modern Reconstruction") is **Doc_02 §9**.

### 3. Row 52 misattributes a claim Doc_02 assigns to Oration 43

Row 52's Licensed For includes "Basil's funeral crowd claim (§8, pending confirmation)." Doc_02 §8 and §6.8 both attribute this to **Oration 43** ("Or. 43's claim of a city-wide mourning including Jews and pagans" / "per Oration 43's account of Basil's funeral crowd"), not to Socrates/Sozomen/Theodoret. Row 26 (Oration 43) already carries "Basil's death and funeral." Remove it from row 52.

### 4. Row 71 reintroduces the Eupsychius-homily defect the Ledger records as already caught

Row 71's **Source** field reads: "Basil and Gregory of Nyssa, homilies on Eupsychius' feast (7 September, Caesarea) — feast attested, no homily itself survives."

Two problems. "No homily itself survives" implies a homily existed and was lost; Doc_02 §3 is explicit that "**no *In Eupsychium* is attested**" — no evidence one ever existed. And Doc_02 attributes no such homily to Basil *or* Gregory of Nyssa; naming two authors for a text nobody claims existed is a fresh invention. The row's own Verification Note gets this right, so only the Source field is wrong — but Ledger §7 records exactly this error ("a claimed homily on Eupsychius of Caesarea that isn't actually attested, only his feast is") as "the closest thing to a fabricated source this build has produced," already found and fixed once. It should not go back in as a row title. Rewrite the Source field as "Eupsychius of Caesarea's feast (7 September), attested via Basil's letters — no homily attested."

Related: row 64's Verification Note asserts that Julian's specific measures against Caesarea are "attested via Basil's letters (row 5) and the church historians (row 52)." Neither Doc_01 §4 nor Doc_02 §2/§1.6 states that transmission route; Doc_01 §5 calls the correction "Documented" without naming a source. Either ground the route in a source document or state the attestation as unspecified.

### 5. Row 54: wrong Exclusion Reason

Row 54 (the Homoian establishment's imperial acts) is marked **Out-of-Boundary** — but the template defines that as "a straightforward temporal or geographic mismatch," and the Homoian church of Cappadocia is neither temporally nor geographically mismatched. It is a *confessional* boundary. The row's own Comparandum Note supplies textbook Named Comparandum content: "an easy source to reach for as though it were 'this world, just the losing side.'" The Registry's own practice confirms the convention — row 3, genuinely Out-of-Boundary, correctly carries "—" in that column. **Change to Named Comparandum.** (Its Verification Note also contains no verification, only the boundary argument; the template requires both Exclusion Reasons to record what was checked.)

### 6. Row 22: Boundary Status used as an authorship gate, inconsistently with row 20

Row 22 (Basil's Ep. 8 / Evagrius) is Excluded because the *attribution* is unsettled — the row says so outright, and even concedes that "Evagrius' own Cappadocian-period text, were this genuinely his, would in fact be Native." The template is explicit that Boundary Status is assessed "by what the source speaks *for* — its own subject, tradition, or evidentiary target," never by confidence in a claim about it. Row 20 (Ep. 38) has the identical problem — contested authorship between Basil and Nyssa — and is correctly kept **Native** with the caution in the Verification Note. Ep. 8 should be handled the same way: Native, low Confidence, attribution caution in the note.

Separately, row 22's **Comparandum Note field holds a to-do item** ("a future pass, once the attribution is settled, should either fold this into…"), not the required content, which the template defines as "the specific claim, image, or reading this source must not be mistaken for." The actual comparandum statement ("do not cite it as Basil's own voice") sits in the Verification Note instead. The two fields need swapping regardless of how the Native/Excluded question is resolved.

### 7. Systematic miscalibration of the D and E tiers

The Registry's own header (line 11) states the rule correctly — A–E "rates how independently *this specific citation* has been checked," not how confident the claim is — and then the rows do not follow it. Two distinct drifts:

**E is being used to mean "not acquired."** The template defines E as "**No traceable source.** Not a resting tier — remove or re-ground to at least D." But rows 17 (Small Asketikon, Rufinus' Latin 397 and the Syriac version), 23 (Epp. 361–364), 32 (Epp. 48–50 and 58), 58 (the Thaumaturgan creed, locus named inside row 43), and 67 (the Nicaea subscription lists) all name a specific work or locus. By the template's own table that is **B** ("Specific work/locus named, not independently re-checked this session"). Row 65 (Libanius, no specific text) is **C**. This matters practically: E carries a mandate to "remove or re-ground," which would put five perfectly well-identified sources on a removal track for a reason — acquisition status — that belongs in the Verification Note. Row 17's note visibly wrestles with this ("Per the template, E is 'not a resting tier'"), which is the tell.

**D is being used to mean "the attribution is shaky."** Row 11 (Basil–Libanius, Epp. 335–359, located "within npnf208") is the clearest case: exact letter numbers in a vendored file is B by definition; D is "tradition/genre-level attribution, no specific text/author named." Same for rows 22 (Ep. 8, within npnf208), 57 (Address to Origen, within anf06), 21 (the Liturgy of St Basil), 49 (Eunomius' confession of 383), 63 (CTh 13.3.5), and 69 (CTh 16.1.3, 30 July 381). The genuine attribution doubt in each of these is an Article 17 question and already recorded in the Verification Notes, which is where it belongs. Only row 74 (regional road-and-frontier context) is a defensible D.

Recommend one pass re-scoring the whole Confidence column against the template's literal tier definitions, with acquisition status and attribution doubt moved to (or left in) the Verification Note.

### 8. Schema violations

- **Row 23** is Native with Licensed For = "Not currently licensed for any specific downstream claim in Doc_02." The template: "A Native source with nothing named here is not yet usable downstream," and builder step 3, "A source without one is not finished being processed." The row explicitly declares itself unprocessed while claiming Native status. Name a target (the obvious one: Doc_02 §1.1's own attribution-discipline claim, which is what the Apollinaris correspondence is actually cited *for*).
- **Row 46 has no Type** ("—"). Type is a required field with a closed vocabulary. The row's own content — a biographical fact resting on the general historical record — argues for S.
- **Row 63's Licensed For** ("Distinguished from row 62 per Doc_02 §2's own correction") is a citation-hygiene note, not "the specific gravity, force, lexicon term, or Representative trait this source justifies." The real target is Julian's school legislation as external-force evidence (Doc_01 §4 / Doc_02 §2).
- **Part F's table drops the Exclusion Reason and Comparandum Note columns entirely.** All Part F rows are Native so nothing is semantically lost, but it diverges from the schema the document declares at line 19 and from every other Part's table shape. Either restore the columns as blanks or state the omission in Part F's header note.

---

## WORTH NOTING

- **Part A is not "carried here verbatim"** (line 23). The four classifications are carried faithfully — I checked each against Doc_01 §2 — but the text is paraphrased and materially augmented (row 2 adds the ascetic-tour argument; row 4 adds the vendored `evagrius_praktikos_dysinger.txt` filename; row 1 moves "own" from Athanasius to Alexandria). Say "carried forward" rather than "verbatim."
- **Row 20 slightly overstates lex001.** It says citing "under whichever author's name the scholarship majority currently favors, flagged as contested either way" is "already the discipline `cappadocianlex001` follows." The file actually says only "transmitted under both Basil's and his brother's names — attribution contested, carried"; it names no author preference and does not cite Ep. 38 by number.
- **Row 9 silently diverges from Doc_02.** Doc_02 §8 calls the Basil/Eustathius rupture "the hinge of §5 debate (10)"; row 9 licenses it to debate (4) and moves debate (10) to row 12. The Registry's call is probably the better one — debate (4) *is* the Eustathius-debt debate — but it corrects Doc_02 without saying so, and the Registry's stated posture is that it introduces nothing new.
- **"The Eunomian-contest gravity candidate"** (rows 13, 34, 47, 48, 49) is not on Doc_01 §2's candidate list. It is traceable to Doc_01 §1's "recurring gravitational questions," where it sits as a sub-question of the Trinitarian confession — worth relabeling so Doc_04 isn't handed a candidate Doc_01 never nominated.
- **Rows 9 and 50 cite "Doc_01 §3.1" and "§3.2."** Doc_01 §3's two fracture lines are numbered list items, not numbered subsections. Cosmetic, but it looks like a real locus.
- **Type S for rows 52, 53, 66** stretches the template's "S — Modern scholarship." Doc_02 §1.6 does class the church historians as secondary narrative sources, so following it is defensible — but row 66 (Jerome's *DVI*, 392) is argued in its own note to be **in-window** for a world closing c. 394, which by the template's Type definitions makes it P.
- **Rows 1 and 3 at Confidence B** are corpus- and category-level ("Athanasius' corpus"; "later Basilian monastic codifications and Byzantine Cappadocia"). C or D by the letter. Row 1 also declines to name `npnf204_athanasius-select-works-letters.xml`, which is vendored and is precisely what makes that comparandum an easy reach; naming it would strengthen the warning.
- **DelCogliano & Radde-Gallwitz 2011 and Pharr 1952** are named specific works in Doc_02 §1.1 and §2 that appear only inside Verification Notes. Not rowing them is safer than wrongly Excluding them, but it is inconsistent with the completeness claim.

---

## Recommendation

**A revision round is needed.** The A-tier discipline — the thing most likely to be quietly wrong — is genuinely clean, and the Part F boundary reasoning is correct where the brief expected an error. But the document makes a specific completeness claim about itself twice, and that claim is false in nine places, with a mechanical root cause (Part F built from §5 only). On top of that there are six broken cross-references, one misattribution, one reintroduced fabrication-adjacent error the ledger already recorded as caught, two Boundary/Exclusion-Reason errors, four schema violations, and a systematic D/E miscalibration affecting roughly a dozen rows. None of these is fatal to the design, and most are mechanical to fix, but they are more than a spot-check's worth.

---

*Note on row numbers: this review's row numbers refer to the first-draft numbering (99 rows, before the Round-2 revision's renumbering to 112 rows and the Round-3 revision's further renumbering to 116 rows). See `cappadocian_Source_Registry_Review_Round2.md` and `_Round3.md` for the current numbering.*
