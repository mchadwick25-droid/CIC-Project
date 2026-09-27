# Step 0 Review, Round 3 — The Tridentine Church

**Reviewer:** independent adversarial review agent (Opus), 2026-09-25, per `cic-build-cycle` discipline. Targeted recheck, not a full re-review. **This is Round 3 of the 3-round cap.**
**Document reviewed:** `Step0_Movement_Scope_Confirmation.md`, Revision 3 (commit `1c25a20fc`). Compared against the Round 2 findings (`Step0_Review_Round2.md`).
**Scope of this recheck:** (1) whether each Round 2 finding was actually fixed; (2) whether the resynced sourcing matches `cic/corpus-map/the-tridentine-church.yaml` and the vendored files in `cic/texts/`; (3) the Barlow *Brutum Fulmen* language description, checked against the file itself; (4) the Pole rights statement, re-queried against archive.org; (5) every quote re-verified by direct grep of the vendored files.

## Verdict

**ESCALATE: one substantial finding, one moderate, six minor.** Revision 3 fixed every Round 2 finding: the sourcing resync, the settled Trent role-split, the IJC restoration, the narration strip, the reachable Round 1 file, and all five minors. The Pole rights re-check is stated honestly.

The substantial finding is new. Revision 3 added five Bellarmine works to B1. One of them is not Bellarmine's work. `bellarmine_notes-of-the-church_1688.txt` is the 1687–88 Church of England tract series that *examines and refutes* Bellarmine's fifteen Notes of the Church. It is hostile Protestant polemic. B1 calls it "Bellarmine's own direct English-language answer to Protestant ecclesiology." That is a misattribution, and the corpus-map holds it as role: tradition. This is the defect class the project treats as most serious for source fidelity. It is actually wrong, not a "could be stronger" point.

The cap allows no fourth round, so this goes to Mark. The fix is mechanical (see Disposition), and the document's Tier conclusion does not depend on the misattributed file.

## Findings

### Substantial

**S1. The 1688 *Notes of the Church* file is an Anglican refutation of Bellarmine, not Bellarmine's own voice.** B1 lists it as "*The Notes of the Church* (1688, Bellarmine's own direct English-language answer to Protestant ecclesiology)", role: tradition. The corpus-map row, the staging file, and the vendored file's own provenance header say the same thing. A direct read of `cic/texts/bellarmine_notes-of-the-church_1688.txt` shows otherwise:

- Line 2409 onward: "A BRIEF DISCOURSE [concerning the Notes of the] CHURCH With some REFLECTIONS on Cardinal BELLARMIN's Notes," "LICENSED, April 6. 1687."
- The tracts are headed one per Note, each with "EXAMINED": "The Second Note of the Church EXAMINED" (c. line 3973), then the Fourth, Fifth, Seventh, Eighth, Ninth, and Tenth (c. lines 5873, 6804, 8834, 10786, 12357, 13604). This is the London 1687–88 collection *The Notes of the Church, as laid down by Cardinal Bellarmin, examined and confuted*, written by Church of England divines.
- Line 4865 onward: "IMPRIMATUR … GUIL. NEEDHAM" (an Anglican licenser), then "thoſe of the Reformed Religion muſt acknowledg themſelves obliged to them, for ſo frankly quitting thoſe Characters which are eſſential to every true Church."
- Line 18082: "whereas we Proteſtants al[low]…". Line 5900: "the Romaniſts." Also present are "The Church of England not…" (line 903) and "Vindication of the Ordinations of the Church of England" (line 2207, in the bookseller's list).

Bellarmine is quoted and answered inside these tracts. He is not their author. As mapped, the file is recorded as this world's own composed voice when it is an outside opponent's polemic. It is the same kind of source as Barlow's commentary (context) and Sarpi (context).

Why this is substantial: B1 makes a false authorship claim about a named source, and Revision 3 introduced it. Doc_02 would inherit it through §4 item 1's instruction to "cite these directly." It does **not** change the Tier or the B2 ecology. Neither rests on Bellarmine: the personal/pastoral voice is argued from Pole, Borromeo, and the liturgical books. It also does not change the "fourteen mapped files" count. The other four Bellarmine files are consistent with genuine translations of his own devotional works. *The Mind's Ascent* and Hall's *Soul's Ascension* are organized by "steps," as the originals are. The Dalton and Foxton files match their headers. Only the 1688 file is wrong.

### Moderate

**M1. §5's first Library item is stale in the same commit that fixed it.** §5 says the Barlow tradition row "states both embedded bulls are 'printed in English and Latin parallel columns'" and "needs correcting." Commit `1c25a20fc`, which wrote Revision 3, also corrected that row. The corpus-map now says *Regnans in Excelsis* is in "genuine English/Latin parallel columns" and the Paul III bull is "in Latin only (… no parallel English rendering, only a brief English index-line summary)." The substance of §5 matches the file and the corpus-map. Only its "needs correcting" status is out of date. §5 should report the row as corrected. This is the same kind of staleness as Round 2's M1.

### Minor

- **m1. Corpus-map locus line range (Library-level).** The Barlow tradition row puts the Paul III bull "with an English index-line summary … c. lines 28695–28710." The bull's Latin text does start at line 28698 ("Paulus Epiſcopus, Seruus Servorum Dei."). But the only English line naming it is the table-of-contents entry at **lines 30435–30436** ("The Damnation and Excommunication of Henry the Eighth by Pope Paul the Third, Decemb. 17. Anno 1538"). The locus should give that line range separately.
- **m2. The Barlow file header is still wrong (Library-level).** `barlow_brutum-fulmen_1681.txt` lines 4–6 and 17–18 still say the file "prints, in English and Latin" both bulls, and they describe "the bull text itself (English and Latin parallel columns)." The corpus-map note now says "the header is wrong on this point." Leaving a known-wrong claim in a canonical file header is the kind of problem the Library's own hygiene rules exist to catch.
- **m3. §5 under-lists the stale dossier material.** §5 flags the dossier's Pole row (line 68). The Borromeo row (line 69) and the dossier's §5 note on VI.12 ("neither candidate can claim him as a 'native voice' source"; "Recommend this world treat Borromeo only as a named figure … not attempt his own voice") are equally stale. The vendored Latin *Acta* and the original-language ruling contradict both. §5 should name them alongside Pole.
- **m4. "A positive rights check" slightly overstates what was found.** I re-queried the archive.org metadata myself today. It returns `possible-copyright-status`, `licenseurl`, `rights`, and `access-restricted-item` all null, and `date` 1560. That matches B1 exactly. But the absence of tags is not a positive rights finding. PD-by-date (1560) is what carries the rights conclusion, and B1 says so. Suggested wording: "a metadata check on this specific item, which found no restriction; PD-by-date carries the rights conclusion." Separating it from the pending EEBO-wide re-check is done honestly. No written record of that wider re-check exists yet in `Build/worlds/_cross-world/` or `Ministry/`, and B1 correctly says Doc_02 should cite it "once it exists."
- **m5. Residual process narration.** The heavy Revision-history narration is gone. A few change-tense phrases remain: "A further ten files are now mapped," "This world's corpus-map now carries," "is now fixed and no longer an open item," and "Duplicate REGISTRY.yaml entries … were already fixed separately" (§5). None of them misstates a fact.
- **m6. One unsourced addition.** B1: "Pole's correspondence also survives in Italian and English, not only in Latin." This is widely accepted and no vendored file or dossier line contradicts it. But it is uncited, and it sits next to a dossier line that says the opposite. Doc_02 should source it, or fold it into the dossier correction.

## Round 2 findings: status

| R2 | Status | Note |
|---|---|---|
| S1 Stale sourcing | **Fixed**, apart from the Bellarmine misattribution (new S1) | Pole as second witness, Breviary as 1 of 4 volumes, Borromeo Latin *Acta* as tradition/primary, Pius V letters, and the file count all match the corpus-map and the file headers. The corpus-map has 15 rows over 14 distinct files, because Barlow is split into two rows. "Fourteen mapped files" is correct. |
| M1 Corpus-map native split | **Fixed** | B3 and §4 item 4 state it as settled. The corpus-map Waterworth row is role: tradition, confidence: assigned, "this world's own defining conciliar voice," and double-placed as context to the Society of Jesus. |
| M2 IJC distortion | **Fixed** | B2 now says IJC "is not a precedent for a voice-thin world at all" and gives the reason. Round 1 M4's point is restored. |
| M3 Narration | **Fixed in substance** | Residue noted at m5. |
| M4 Round 1 file unreachable | **Fixed** | `Step0_Review_Round1.md` is in this directory. |
| M5 §5 Library list | **Fixed at the time, now partly stale** | See M1 and m3. |
| m1 A1 garble | Fixed | |
| m2 "in Session III" scoping | Fixed | Both body-text Nicaea references are now named. |
| m3 Window direction | Fixed | §1 (window looser than the Council's dates) and §4 item 7 (scope narrower than the window) are now consistent. |
| m4 Pole rights wording | Fixed | Slight overstatement at m4 above. |
| m5 Barlow split named | Fixed | |

## Confirmed accurate

- **Trent quotes, by grep of `council-of-trent_canons-and-decrees_waterworth1848.txt`:**
  - Session III heading at c. line 12303.
  - "the Symbol of faith which the holy Roman Church makes use of" at lines 12339–12340.
  - "Concil. Nicnen." footnote at line 12356.
  - "proceedeth from the Father / and the Son" at lines 12368–12369.
  - "the age of the Council of Nicaea" at line 15232 (OCR "Nicsea"; the document's normalization is fair).
  - "the second Synod of Nicaea" at lines 21977–21978 (OCR "Nicsea").
  - "Chalcedon" occurs once in the decrees, at line 19846, as a disciplinary citation. The other two occurrences (lines 2820 and 11383) are in the essay.
  - "composed by / Cardinal Pole" at lines 3663–3664.
- **Barlow, checked by reading the file:**
  - *Regnans in Excelsis* is in genuine parallel columns. English "…E that reigneth on high" at c. line 2272; Latin "…Egnans in Excelſis" at c. line 2305.
  - The Paul III bull begins at line 28698 in Latin, and I found no English rendering of it. The only English references are the table-of-contents line (30435) and Barlow's own commentary (e.g. lines 23185 and 23273).
  - The document (via §5) and the current corpus-map row now **agree**: Pius V is bilingual, and Paul III is Latin only with an English index line.
- **File headers and corpus-map rows match B1** for:
  - Pole (Wythers 1560, archive.org identifier, flagged under OCR ruling "a" as second witness);
  - Borromeo (1599 Latin printing, clean scan);
  - the Breviary (Bute 1908, "one of 4 seasonal volumes," Leo XIII revision);
  - the Missal (England 1843, whole volume);
  - Pius V (*Apostolicarum … Epistolarum Libri Quinque*, 1640, Latin);
  - Bellarmine: Dalton (19th c.), Foxton 1722 with the Addison essay, 1925, and Hall 1703.
- **Pole rights, re-queried by me** via `archive.org/metadata/bim_early-english-books-1475-1640_the-seditious-oration_pole-reginald_1560`: all four rights/access fields are null and the date is 1560, exactly as B1 reports.
- **Original-language and OCR rulings:** both are logged in `Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md`. The Pole file is named there as a second-witness file.

## Disposition

**ESCALATE to Mark.** Under the cap, Round 3 found a substantial problem (S1), so no fourth revision round opens.

The escalation is narrow. Every Round 2 finding is genuinely fixed. S1 is a misattributed source that Revision 3 imported from the Library. It is not a contested argument, and it does not touch the Tier 1 conclusion or any §4 obligation's substance. For Mark's decision, the proposed fix is a named change order, not a revision round:

1. **Library (corpus-map / staging / file header / REGISTRY / README):**
   - Re-attribute `bellarmine_notes-of-the-church_1688.txt` to its actual Church of England authors, or to the collection.
   - Reclassify it as role: context (an outside opponent's testimony, like Barlow's commentary), and consider whether to rename the file.
   - Correct the header claims in both the Bellarmine and Barlow files (m2).
   - Fix the Barlow locus line range (m1).
2. **This document:**
   - Delete or recast the Bellarmine *Notes* clause in B1 so the file is described as an Anglican refutation (context).
   - Update §5 to report the Barlow row as corrected, and add the stale dossier Borromeo/VI.12 lines (M1, m3).
   - Optionally take m4–m6.
3. **Dossier:** correct lines 68–69 and the §5 VI.12 note.

After the change order, an independent spot-confirmation of items 1 and 2 would be enough. That is a check of the named lines only, not a review round. Also check the Society of Jesus sibling Step 0 and any other world's corpus-map for this same file before relying on it anywhere.
