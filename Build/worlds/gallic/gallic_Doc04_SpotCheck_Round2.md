# Doc_04 Spot-Check — Round 2 (bounded)

**Document checked:** `gallic_Doc04_Gravity_Discovery.md`, status "Round 1 review complete; fix round applied (2026-09-09)", 451 lines.
**Checker:** independent, fresh context; no part in drafting Doc_01–Doc_04, in the Round 1 review, or in the Round 1 fix round.
**Date:** 2026-09-09.
**Scope:** bounded verification that the Round 1 fix list (S1–S9, C1–C9; C10 explicitly left unfixed by the reviewer's own instruction) actually landed in the live file, that each fix matches its own stated remedy, and that no fix introduced a new error. **Not** a re-run of Round 1's substantive research.
**Read in full:** `gallic_Doc04_Review_Round1.md`; the whole live Doc_04.
**Primary sources opened directly this pass** (flattened with `<div>` ids preserved, grep-and-context, the same method Round 1 used): `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml`; `cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml`; `cic/texts/salvian_on-the-government-of-god_sanford1930.txt`; plus `gallic_Doc03_Lexicon_Candidates.md` for the S3 and C5 checks. Every ✔ below was checked in the live file or in the vendored source, never taken from the §11 log.

---

## VERDICT

**DOES NOT FULLY CLEAR — three specific defects, all narrow, all single-line.**

**All nine substantial fixes (S1–S9) are physically present in the body of the document, in the right place, and each matches what the Round 1 remedy actually asked for.** I re-verified every touched quotation and locus against the vendored files independently rather than trusting the document's restated claim: the *Vita* X / *Inst.* I.10 / *Inst.* I.1 camel's-hair correction, the Richardson-vs-Gennadius layer at ch. LXXXVI, the Salvian VIII.4 Carthage context, both Salvian page numbers, the two re-verified S8 loci, the three new S9 witnesses, and the six sackcloth loci newly introduced by the S4 fix. **All of them check out.** The Interaction Matrix is still a genuine 10×10 table; I recomputed all 45 pairs for upper/lower-triangle symmetry after the S7 edits and found **zero** mismatches, and the five S7-touched prose lines (G2, G3, G4, G6, G8) now agree with the matrix.

**What is wrong is the build's own named failure mode, once, plus two consequences the fix round did not follow through.** One cosmetic fix is claimed in §11 as applied and is only half-applied. One substantial fix (S4) added three entries to §2.2 without updating the count that §5 states for that same section. One substantial fix (S6) corrected the over-read in §3 and in the forces notation but left the identical over-read standing in the §4 matrix cell, so the document now contradicts itself on that sentence.

**Recommendation:** a micro-fix pass on R1–R3 below, then **self-dispose to Approved to Proceed without a further review round**. Nothing found here touches a classification, a confidence rating, a cross-node status, the Cross-Check layer, or §6's one-world input.

---

## Part A — the assigned fix list, item by item

### S1 — the camel's-hair claim ✔ LANDED CLEAN

The false clause "the Egyptian dress Cassian says Gaul cannot wear" is **gone**. §3, G2 Evidence (L124) now reads that the phrase is "**not**, on inspection, Egyptian-comparative dress evidence," gives Roberts's Matt. iii. 4 footnote, gives *Inst.* I.10's actual list, gives *Inst.* I.1's approving use, and re-grounds the stream: "[M]'s evidence for G2 rests on *Inst.* I.10 and IV.10–11 above, not on this passage."

Independently verified in `npnf211`:
- `ii.ii.xi` (*Vita* X): "Most of them were clothed in garments of camels' hair." with the adjacent footnote "**Cf. St. Matt. iii. 4**" ✔ — exactly as the corrected text says.
- `iv.iii.i.x` (*Inst.* I.10): "the severity of the winter does not allow us to be satisfied with **slippers** or **tunics** or a **single frock**; and the covering of **tiny hoods** or the wearing of a **sheepskin** would afford a subject for derision instead of edifying the spectators" ✔ — Doc_04's five-item list is exact, and camel's hair is not among them.
- `iv.iii.i.i` (*Inst.* I.1): "the same John had his raiment of camel's hair and a girdle of skin about his loins," cited approvingly in the girdle chapter ✔.
- Whole-file grep returns exactly **two** hits for "camel" ✔, matching Round 1's count.

The remedy offered a choice (drop [M], or re-ground on *Inst.* I.10 and IV.10–11); the document took the second, correctly, so [M] rightly stays in G2's stream lists at §2.1, §3 and §8. No new error.

### S2 — G3's Persistence test / the unlabelled Richardson date ✔ LANDED CLEAN

§3, G3 Tests (L148) now reads: "Marseilles (Cassian) attests it; Vincent's Lérins participation is Contested and rests on Heurtley's editorial reading; Faustus's own *De gratia* is post-window (c. 473–475, Doc_01 §2.4) and his Lérins abbacy date ('433–4') is Richardson's endnote (row 42), not Gennadius's own text, which gives no date — so Lérins supplies no in-window attestation here." That is the remedy, essentially verbatim, and it removes the manufactured second in-window southern site.

Verified in `npnf203` at `v.iv.lxxxvii`: the chapter opens with the bracketed endnote "**Faustus, Abbot of Lerins 433–4, bishop of Riez 462, exiled 477–84, died 490.**" and the ancient text that follows reads only "first abbot of the monastery at Lerins, and then made bishop of Riez in Gaul," with no date ✔. The document's layer attribution is correct, and it now quotes Richardson's own form "433–4" rather than the laundered "c. 433."

Registry row 24 (Faustus, *De gratia*, CSEL 21) added as **§10 item 12** ✔, worded as the remedy asked ("the one primary source that could actually settle whether Lérins attests G3 inside the window").

### S3 — §6's discount criterion ✔ LANDED CLEAN

§6 point 2 (L345) now reads: "That comparative distinctiveness, **not Doc_03's [SC] tag (which G1 and G4's own core vocabulary also carries — Doc_03 8.1, 3.3, 7.3 — and so cannot itself be the discriminator)**, is why G5 and G8 are discounted…" This takes both halves of the remedy at once: the tag is dropped as the discriminator and the asymmetry is disclosed.

Verified in Doc_03: entry 3.3 Tags `[SC] [TC] [DR] [RT]`; entry 7.3 Tags `[SC] [TC] [DR] [RT]`; entry 8.1 Tags `[SC] [DR] [TC] [RT] [PV]` ✔. All three carry [SC], as the new sentence asserts.

### S4 — Doc_03 8.5 (sackcloth), 5.5, 1.10 ✔ LANDED — **but see R2**

All three are now in §2.2 with stated reasons (L85 sackcloth, L86 predestination, L87 conversion), and §6 point 3 (L346) now names sackcloth as "a directly-opposed practice-level disagreement of the same shape as G6's … recorded here as confirming the same pattern G6 already establishes, not as a fourth data point." That discharges Doc_03 §10 item 5's instruction and closes the §9.1 gaps.

The new sackcloth entry introduces six loci and two quotations that were not in the Round 1 document, so I checked them all rather than assuming:
- `npnf211` sackcloth divs: `ii.ii.xv` (= *Vita* ch. XIV), `ii.ii.xix` (= *Vita* ch. XVIII), `ii.iii.i` (*Ep.* I), `ii.iii.iii` (*Ep.* III), `ii.iv.ii.v` (*Dial.* II.5), `ii.iv.iii.vi` (*Dial.* III.6) — **all six of Doc_04's cited loci exist and carry sackcloth** ✔, with the one-ahead *Vita* offset applied correctly.
- `iv.iii.i.ii` (*Inst.* I.2): "they utterly disapproved of a robe of sackcloth as being visible to all and conspicuous, and what from this very fact will not only confer no benefit on the soul but rather minister to vanity and pride"; "even if we hear of **some respectable persons who have been dressed in this garb**, a rule for the monasteries is not, therefore, to be passed by us, nor should the ancient decrees of the holy fathers be upset" ✔ — both quotations exact.
- The entry's supporting claim that *Inst.* I.2 states the disapproval "on the same 'unanimous decision of the fathers' ground G4 already organizes" is likewise sound: the same chapter carries "a long standing antiquity and numbers of the holy fathers have passed on by an **unanimous decision**" ✔ (the phrase G4's Evidence already quotes).

The fix itself is clean. Its **arithmetic consequence was not followed through** — see R2.

### S5 — G3's Author Gravity flag ✔ LANDED CLEAN (one minor residue, R4)

§2.1 G3 (L60) now reads "**single-voice (Cassian) within this world's own Native voices, and node-bound risk**" with the supporting reasons spelled out ✔ — the remedy's wording. §8's G3 row (L373) carries the same flag ✔. §5's roll-up (L336) now names G3 and, to its credit, **discloses the retrofit honestly** rather than papering it over: "not named as single-voice at generation, only as node-bound, and corrected at §2.1 in the fix round following Round 1 review." That is the right way to make this correction.

### S6 — G2's Salvian evidence ⚠ LANDED IN §3, **NOT IN §4** — see R3

The two loci the remedy named are both fixed:
- §3, G2 Evidence (L123): "in context, one item in a three-part list of holy places named in a Carthaginian mockery of visiting ascetics (Sanford pp. 229–30); Egypt remains a byword for holiness in a non-monastic Gallic voice, **but the passage carries no comparative or normative weight and is not evidence of a Gallic *measuring* relationship to Egypt**" ✔.
- §3, G2 forces notation (L136): the "measures holiness by" phrasing is replaced by "Salvian names 'the monasteries of Egypt' among the holy places whose visiting ascetics Carthage mocks (VIII.4) — though this passage carries the reference point, not the measuring relationship, and is weaker evidence than the receptive and comparative modes above" ✔.

Verified in `salvian_…_sanford1930.txt` (lines 10248–10262): the sentence sits inside "within the cities of Africa, and especially within the walls of Carthage, a people as unhappy as they were unfaithful could scarcely look without reviling and curses at a man pale and in monkish garb… he met with contumely, sacrilege and curses" ✔. The document's new characterization is exactly right.

The remedy's second half ("either drop [Sv] from G2's stream list **or** state explicitly that the Salvian witness carries the reference point but not the measuring relationship") is satisfied by the second option, so [Sv] correctly remains in G2's lists.

**But the §4 matrix cell was not touched** — R3 below.

### S7 — Interaction-line / matrix mismatches ✔ LANDED CLEAN for all five candidates (one residue, R5)

I parsed the §4 table programmatically and checked **all 45 pairs** for symmetry: **zero mismatches**, no empty rows, every pair coded. The matrix was not disturbed by the fix round.

Prose-vs-matrix, for the five candidates S7 touched:

| Candidate | Matrix row | §3 Interaction line now says | Match |
|---|---|---|---|
| **G2** | R: G1 G4 G5 G7 G8 G10(thin) · S: G3 G9 · C: G6 | "reinforcing with G1, G4, G5, G7, G8, G10 (thin); reshaping with G3, G9; competing with G6" | ✔ exact, all 9 pairs, omitted G1/G10 now present |
| **G3** | S: G1 G2 G9 · R: G4 G5 G7 G8 · —: G6 G10 | "reinforcing with G4, G5, G7, G8; reshaping with G1, G2, G9; no demonstrated relationship with G6, G10" | ✔ exact — the G2 miscoding is corrected to reshaping and both "—" cells disclosed |
| **G4** | R: G1 G2 G3 G7 G8(thin) G9(S)/C(N) G10(thin) · S: G5 G6 | "reinforcing with G1, G2, G3, G7; reshaping with G6 and (heard→read) G5; reinforcing in the south and competing in the north with G9" | ✔ the G5 double-coding is gone (G5 now under reshaping only) |
| **G6** | S: G1 G4 G9 · C: G2 G7 · R: G5 G8 G10(thin) · —: G3 | "competing with G2 (south) and G7; reinforcing with G5, G8, G10 (thin); reshaping with G1, G4, G9; no demonstrated relationship with G3" | ✔ exact, all 9, its one "—" cell disclosed |
| **G8** | R: all nine | "reinforcing with G1, G2, G3, G4, G5, G6, G7, G8, G9, G10 — uniformly reinforcing, the whole row" | ✔ exact, omitted G4 now present |

Every candidate S7 named is now correct. Four of the five lines are complete across all nine pairs.

### S8 — Discipline 2 and the G9 citation ✔ LANDED CLEAN (one minor residue, R6)

- Discipline 2 (L19) no longer claims unqualified completeness: it now reads "…**except the two loci marked 'not re-read this pass' at G8 and G9 (§3), carried forward from Doc_03 and now both re-verified in the Round 1 fix round**" ✔.
- G8 (L243): "*Conf.* XIII.14 (`iv.v.iv.xiv`, re-verified this fix round)". **I re-verified it myself:** `iv.v.iv.xiv` = Chapter XIV, "the Divine righteousness provided for in the case of Job His well tried athlete, when the devil had challenged him to single combat" ✔.
- G9 (L263): now "ch. 28 [71–72] (`iii.xxix`, re-verified this fix round; **the passage occurs once in the volume, not also at ch. 10 as Doc_03 7.7's citation had it**)". **I re-verified it myself:** `iii.xxix` opens "Chapter XXVIII… [71.]" and the sentence "be he holy and learned, be he a bishop, be he a Confessor, be he a martyr, let that be regarded as a **private fancy of his own**" occurs **exactly once** in the whole 4 MB file, there ✔. The wrong "ch. 10 [28]" half is removed, and the bracketed section number [71–72] is right.

### S9 — unceasing prayer / the canonical office ✔ LANDED CLEAN

§2.2 (L77) is fully rewritten. It now states the recurrence already in hand, and then does what the remedy asked: names **specifically** what the unread books would have to show — "what would change the outcome is whether those books show the office organizing *other* practices (dependency) or merely regulating time within a formation program G7 already covers." It also gives a partial test result ("Repetition and Persistence would likely pass on this alone") rather than deferring silently. §10 item 8 remains consistent with it.

All three newly quoted witnesses verified:
- `iv.iv.i` (*Conf.* Pref. I): "from the system of the canonical prayers, let our discourse mount to that **continuance in unceasing prayer**, which the Apostle enjoins" ✔ — exact, and the phrase occurs once in the file.
- `v.iv.lxiii` (Gennadius ch. LXII, **ancient text**, not Richardson's endnote): "On the canon of prayers, and the Usage in the saying of Psalms, (for these in the Egyptian monasteries, are said day and night), three books"; and among the Conferences "On the nature of prayer, On the duration of prayer" ✔ — both exact, and the layer is correctly ancient.
- `ii.ii.xi` (*Vita* X): "the elders spent their time in prayer. Rarely did any one of them go beyond the cell, unless when they assembled at the place of prayer" ✔.

### C1–C9

| | Status |
|---|---|
| **C1** G5 stream list | ✔ reconciled — §2.1 (L62) "S, C, V, **L**, F", §3 (L186) "S, C, V, L(by existence), F", §8 (L375) "S, C, V, L, F" |
| **C1** G6 stream list | ✗ **half-applied — see R1** |
| **C2** Castor's see | ✔ L103 "(Gibson's fn., **editorial**: bishop of Apta Julia in Gallia Narbonensis)". Verified: that footnote is at `iv.ii`, embedded in the *Inst.* Preface div, exactly as cited |
| **C3** Salvian pages | ✔ both. VII.12 → **p. 204** (L283); VIII.4 → **p. 230** (L123). Verified against the file's own running heads: "204 THE SEVENTH BOOK" immediately precedes VII.12, "230 THE EIGHTH BOOK" immediately precedes the VIII.4 sentence |
| **C4** §10 item 11 | ✔ L413 now opens "every Tier-1 (est.) term maps to **a classified gravity** here" — self-contradiction gone, mapping unchanged |
| **C5** misattribution | ✔ L173 now "Doc_03 **entry 7.3**". Verified: the phrase "the strongest lexical link found between Vincent's doctrinal method and Cassian's monastic method, and between both and Martin" is at Doc_03 L557, inside entry 7.3 (heading L552) |
| **C6** "decisive" | ✔ the word survives nowhere in the document body — only inside the §11 log entry describing its removal |
| **C7** Eucherius's addressee | ✔ L122 "a letter addressed to **Hilary of Arles** (then at Lérins, per Registry row 26 and Doc_02's naming)" |
| **C8** name-order inference | ✔ L121 "**Eucherius by inference from name-order** and from Pref. II's identification of the first brother as one 'presiding as he does over a large monastery,' **not stated by name at this clause**" |
| **C9** row 6 | ✔ L396 adds row 6 (*Sacred History*) to §9's Verification-Note extensions, and flags it as a duplicate of Doc_03 §10 item 6 |

### C10 — correctly left alone ✔

C10 ("Widely Accepted" used as a source-count rating) was **not** applied, as the Round 1 reviewer's own text directed ("noted for consistency rather than charged against Doc_04"; "no effect on any Primary classification"). I confirmed the three ratings the reviewer named are untouched — G2's northern mode (L130), G6's "Martin's fame" (L211), G9's Celestine episode (L269) — and that **§11 L450 states plainly that it was not changed and why** ✔. This is correct behaviour, not a missing fix.

---

## Part B — findings

### R1. C1's G6 stream reconciliation is claimed as applied and is only half-applied — the build's named failure mode

§11 L449 states: "G5/**G6** stream lists reconciled across §2.1/§3/§8 (C1)."

The G5 half is done. The G6 half is not:

| Locus | G6 streams now read |
|---|---|
| §2.1, L63 | S, Gn, **L**, E, AA |
| §3 Repetition, L207 | "passes across streams (S, Gn, E, AA)" — **no L** |
| §8 Index, L376 | S, Gn, E, AA — **no L** |

[L] was added in §2.1 only. §2.1 was the outlier before the fix ("S, Gn, AP/AA") and it is still the outlier after it, just differently. This matters slightly more than a bookkeeping slip, because Round 1's own reason for wanting [L] there was substantive: G6's Eucherius *De Laude Eremi* §27 passage is what produces the "internal southern split" finding that the Tensional classification rests on (§3 L205, L209; §8 L376's "S internally split (Cassian vs Eucherius)"). The [L] stream is doing load-bearing work in G6's Evidence and its Persistence result while being absent from two of the three places G6's streams are listed.

**Fix:** add **L** to G6's Repetition line at §3 L207 and to G6's Streams cell at §8 L376.

### R2. The S4 fix added three entries to §2.2 and did not update the count §5 states for it — a new internal inconsistency

§2.2 now contains **17** bulleted non-advancements (I counted them mechanically). §5 L326 still reads:

> "- **Considered, not advanced (14):** §2.2."

Fourteen was correct before the fix round — Round 1's S4 and S9 both refer to "the fourteen 'considered and not advanced' items." The S4 fix added sackcloth (8.5), predestination (5.5) and conversion (1.10), making seventeen, and §5's roll-up was not updated. §5 is the classification summary a downstream document reads instead of §2.2, so the wrong number is in the more-consulted place.

**Fix:** change "(14)" to "(17)" at L326. (The document uses the count only there; "fourteen" appears nowhere else.)

### R3. S6's correction was applied in §3 and left standing in §4 — the document now contradicts itself on the Salvian sentence

§3, G2 Evidence (L123), after the fix:
> "…the passage carries no comparative or normative weight and **is not evidence of a Gallic *measuring* relationship to Egypt**."

§4, the G2×G10 matrix cell (L306), untouched:
> "**R (thin)** — Salvian **measures holiness by** 'the monasteries of Egypt' inside the judgment argument (VIII.4)"

That is the exact formulation Round 1 singled out as indefensible ("'Egypt as the byword for holiness' is a defensible reading of the phrase; '**measures** holiness by the monasteries of Egypt' (forces notation) is not"), and S6's finding-text explicitly noted that the passage "reappears in the G2×G10 matrix cell." The stated remedy named the forces notation, so the fix round can claim technical compliance — but the result is that one gravity's Evidence line and its own matrix cell now assert opposite things about the same sentence, on the sole evidentiary basis for a "thin" reinforcement cell.

**Fix:** reword the G2×G10 cell to match §3, e.g. "**R (thin)** — Egypt remains a byword for holiness in Salvian's judgment argument (VIII.4); the passage carries the reference point, not a measuring relationship." No code change is needed — R (thin) still holds on the weaker reading, and the matrix stays symmetric.

### Minor residues (noted, not charged — none is a failed fix)

**R4. Discipline 5 (§0, L25) was not updated for G3's new flag.** It still reads "Two candidates (G6, G7) carry a single-voice flag from the outset." That sentence is *literally* still true — G3's flag was retrofitted, not set at generation, and §5 discloses exactly that — but a reader of §0 alone will not learn that three candidates now carry a single-voice flag in §2.1. A half-clause would close it.

**R5. S7's general disclosure principle was applied only to the candidates the reviewer named by example.** S7's third bullet asked that "each candidate's line should surface its own" non-interacting cells. G3 and G6 were named and are fixed; **G1 (L106), G5 (L186) and G9 (L265) each still have one undisclosed "—" cell (G10 in all three cases)**, and G4's line (L167) still omits its two "R (thin)" pairs (G8, G10). None of these was in the enumerated remedy and none pre-dates it — they are Round 1 leftovers the fix round had no instruction to touch — so this is an observation about completeness, not a fix that failed.

**R6. Discipline 2 (L19) quotes a marker string that no longer exists in §3.** It refers to "the two loci **marked 'not re-read this pass'** at G8 and G9 (§3)," but both now read "re-verified this fix round" instead. The sentence is self-explaining and substantively accurate; the quoted marker is simply stale.

---

## Part C — sanity check on the §11 "Round 1 fix round" log

The log entry (L439–451) is unusually accurate for this build. Nine substantial fixes are described and nine are genuinely in the body, each doing what the entry says it does. The C10 non-fix is disclosed with its reason rather than quietly skipped. §5's roll-up voluntarily discloses that G3's flag was corrected after the fact rather than caught at generation — a disclosure the fix round was not required to make.

Two claims in the log do not survive checking:

1. **L449, "G5/G6 stream lists reconciled across §2.1/§3/§8 (C1)"** — the G6 half is not reconciled (R1).
2. **L439, "Each fix below was grep-verified against the live file before being logged here"** — a grep of "S, Gn" would have surfaced R1 immediately, and the §5 count (R2) is a two-second check. The verification claim is broader than what was actually verified.

Neither is a fabricated fix: nothing is claimed as present that is wholly absent, which is the sharper version of this build's recurring failure and did **not** recur here. What recurred is the milder version — a two-part fix logged as complete when one part landed.

**Disposition claim at L451** ("all 9 substantial and 9 of 10 cosmetic findings fixed and self-verified") is accurate for S1–S9 and for C2–C9, and overstated for C1.

---

## SUMMARY

| | Result |
|---|---|
| Substantial fixes (S1–S9) present in the body | **9 of 9** |
| Substantial fixes matching their own stated remedy | **9 of 9** |
| Substantial fixes introducing a new error | **1** (S4 → R2); **1** leaving a self-contradiction (S6 → R3) |
| Cosmetic fixes (C1–C9) fully applied | **8 of 9** (C1's G6 half not applied — R1) |
| C10 correctly left unfixed and logged as such | ✔ |
| Quotations/loci re-verified against vendored sources this pass | 17 (all touched by S1, S2, S4, S6, S8, S9, C2, C3, C5) |
| Re-verified quotations found wrong | **0** |
| Matrix pairs re-checked for symmetry | **45 — zero mismatches** |
| Classifications, confidences, or cross-node statuses disturbed | **0** |

**Single most important finding: R1** — the one place §11 claims a fix that is only half in the document, and it is the same "reconciled across §2.1/§3/§8" sentence that names both G5 and G6.

**Runner-up: R3** — S6's over-read was corrected in two of the three places it lives, leaving §3 and §4 asserting opposite things about the Salvian VIII.4 sentence.

**All three defects are single-line edits and none reopens anything.** After R1–R3, this document is in materially better evidentiary shape than it was at Round 1 — which was already the cleanest evidentiary layer this build has produced.

---

## DOCUMENT LOG

- **Checker:** independent, fresh context; no drafting involvement in Doc_01–Doc_04, no part in the Round 1 review or the Round 1 fix round.
- **Scope:** bounded spot-check of the enumerated Round 1 fix list (S1–S9, C1–C9), confirmation that C10 was correctly left alone and logged, an independent re-verification against the vendored primary sources of every quotation and locus the fixes touched, a full 45-pair re-check of the Interaction Matrix after the S7 edits, a prose-vs-matrix check on all ten Interaction lines, and a disturbance sweep for new internal inconsistencies.
- **Method:** every claim marked ✔ was checked in the live file or by grep-and-context against `npnf211`, `npnf203`, `salvian_…_sanford1930.txt`, or `gallic_Doc03_Lexicon_Candidates.md`. The document's own restatement of a source was never accepted as the check. Matrix symmetry was verified by parsing the table programmatically, not by eye.
- **Not done:** no re-run of Round 1's substantive research; no re-assessment of any classification, confidence rating, test result, or §6 argument; no reading of unvendored sources; no live research; no check of the Latin files (rows 26–27), which no fix touched.
- **Disposition: MICRO-FIX PASS on R1–R3, then self-dispose to Approved to Proceed.** No further review round is warranted — R1–R3 are three single-line edits, R4–R6 are optional, and nothing found here touches the classification layer that Doc_05, Doc_06 and Doc_08 consume.
