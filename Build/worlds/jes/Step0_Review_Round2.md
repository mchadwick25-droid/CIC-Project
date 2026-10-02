# Step 0 Review, Round 2 — The Society of Jesus

**Reviewer:** independent adversarial review agent (Opus), 2026-09-25, per `cic-build-cycle` discipline. Targeted recheck, not a full re-review.
**Document reviewed:** `Step0_Movement_Scope_Confirmation.md`, Revision 2 as rewritten by the narration-stripping hygiene pass (commit `4b4ce830`).
**Checked against:** Round 1 findings F1–F10 (read from commit `acd9a888`; see M3 below); the Revision 2 text before the hygiene pass (`a67b1b2e`); the vendored files in `cic/texts/`; the live `cic/corpus-map/the-society-of-jesus.yaml` and `the-tridentine-church.yaml`; `cic-website/data/world-census.json`; `Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md`; Constitution V2.3 Article 4 (`Build/reference/L1-Foundation/CiC_L1_Constitution_V2_2.docx`, internally "Version 2.3").

## Verdict

**Substantial revision needed. This is Round 2 of 3.** Revision 2 fixed Round 1's substantive content findings correctly. That includes the Trent/Chalcedon claim, which is now precise and accurate. The hygiene rewrite also kept every fact, quote, date, and citation it touched. But two binding sourcing items are now false against the live corpus-map and a 2026-09-25 ruling by Mark. The hygiene pass edited this document and the corpus-map in the same commit, yet left the document describing the corpus-map defect it had just fixed. One Round 1 fix (F6) was made in §0 but not in A4, so the document now contradicts itself about Mark's reasons for selecting this world.

Most of S1 is drift from events that came after Revision 2, not a failure of Revision 2's own drafting. A Round 3 should be a bounded resync, not a redraft (see Disposition).

## Findings

### Substantial

**S1. The sourcing record is stale again, and two binding §4 items would now misdirect Doc_02.** Revision 2 was accurate against the 2026-09-24 vendoring pass. After that, the 2026-09-25 acquisition pass (`79b68940`) and the Latin/OCR re-assessment (`cd63bbab`) changed the record under it. The hygiene pass (`4b4ce830`, the same day) did not update the document. The live corpus-map now differs from the document in four ways:

- **Constitutions and Nadal's *Adnotationes* are no longer PRIMARY.** Mark's OCR ruling "a" (2026-09-25, `LIBRARY-DECISION-LOG.md` point 5) says scan quality decides whether a text can be quoted. Under it, both corpus-map notes now read "flagged under Mark's OCR ruling 'a' as garbled. It stays second witness for that reason ... not yet quotable verbatim." The document still says "vendored as PRIMARY content" (B1, and §4 item 1, which is binding on Doc_02). It also presents the Constitutions gap as one of language only ("sourceable only in Latin"). The gap is now about scan quality: the order's governing document is not yet quotable verbatim in any language. The document discloses Nadal's OCR flag but says nothing about the Constitutions' flag. If Doc_02 follows §4 item 1 as written, it will treat a garbled scan as quotable primary text, which is a verbatim-fidelity risk.
- **Faber's own *Memoriale* is now vendored** as `faber_memoriale-lat_1873.txt`, with role tradition, confidence assigned, and a clean scan. B1 and §4 item 2 (binding) still say "Faber is only partly resolved" and treat Boero's biography as the only Faber source. That binding instruction is now obsolete.
- **"Ten works" and "~1.39M words" are out of date.** I confirmed 1,385,753 words for the original ten files, so the figure was right when written. The corpus-map now lists 19 works. The nine additions are the *Memoriale*, the Lainez *Epistolae et Acta* v1, Salmeron *Epistolae* v2 and v3, Nadal *Epistolae* v1 and *Scholia in Constitutiones*, Polanco's *Chronicon* v1, Ribadeneira's *Vita Ignatii* (context, OCR-flagged), and MHSI *Epistolae et Instructiones* v22. The document cites REGISTRY.yaml and the corpus-map as its authorities, and both now contradict it.
- **The coverage window moves.** Lainez (General 1558–65), Salmeron's letters, Nadal's letters and *Scholia*, and Polanco extend the vendored first-generation voice well past 1556. B5, the Tier rationale ("strong for 1521–1556 and thin for 1556–1650"), and §4 item 5 need re-dating, roughly to "thin after c. 1580." The central point still holds: nothing is vendored on Ricci, de Nobili, the *Ratio Studiorum*, or the Jesuit Relations. I grepped `cic/texts/` and found no relation/Thwaites/Ricci/Nobili/Ratio files.

**S2. The Trent role split is now confirmed, but the document still describes it as a live defect.** The live corpus-map assigns the Waterworth canons/decrees as follows:

- `the-society-of-jesus.yaml`: `role: context`, `confidence: assigned`. The note reads "Double-placed to the-tridentine-church (VI.22), where the same text is role tradition instead."
- `the-tridentine-church.yaml`: `role: tradition`, `confidence: assigned`. The note reads "Native/foundational here."

Three places in the document still say "neither world currently holds the text as 'native' — a corpus-map defect":

- **B3**
- **the Section B conclusion**
- **§4 item 3**, which is binding and says the split "needs fixing at the corpus-map level before either Doc_02 can rely on" it

All three are now false. The same commit that fixed the corpus-map (`4b4ce830`) also rewrote this paragraph and removed its "not fixed by this revision" clause, which made the error worse. A corrected text should say the split is settled: tradition/native for the Tridentine Church, context/implementing for the Society, both at confidence `assigned`. §4 item 3 should then drop to a disclosure-only cross-reference. It should no longer say anything blocks Doc_02.

B3 also points to "the native/implementing split described elsewhere in this document." No other section describes it any more; the Revision 1 text that did was removed. This is a dangling reference.

### Moderate

**M1. F6 was fixed in §0 but not in A4, so the document contradicts itself.** §0 now says there is no record that Mark chose this world for its desert-monastic/Evagrian echo, and that the echo is "this thread's own reasonable reading." A4 still says, unchanged from Revision 1: "Mark selected this candidate directly, 2026-09-15, per §0 above, specifically for its dual role as Catholic-renewal contrast and desert-monastic-practice echo." That line attributes a motive to the project lead with no record behind it. §0 also still says the echo is "named below as 'Mark's own stated reasoning'," but that phrase no longer appears anywhere below. Both sentences need rewriting. The "Catholic-renewal voice" rationale in §0 and A4 is also stated as fact with no cited record. The document should either cite one or state it as a reading, as it now does for the echo.

**M2. The Devotio Moderna anchor is attributed to the wrong source (B2).** The document says: "Xavier's own Letters record the early companions reading the Imitation of Christ and Ignatius distributing *De Contemptu Mundi*." Neither passage is from Xavier's letters:

- `francis-xavier_life-and-letters-v1_coleridge1872.txt` l. 3505–3509 ("spiritual reading in the Bible and the Imitation of Christ") is Coleridge's own biographical narration.
- l. 4531–4536 is a Coleridge footnote citing Alcazar's *Chrono-Historia*. It says Ignatius gave "each monk at Monte Cassino a copy of the book de Contemptu Mundi, i. e. the Imitation of Christ."

The substance of the anchor is real and vendored. The attribution should read: "Coleridge's *Life and Letters of St. Francis Xavier* (Vol. I) records ..., and a footnote citing Alcazar reports ...". Misattribution is the recurring defect class that CLAUDE.md singles out.

**M3. The narration strip was incomplete, and the document points to a review file that is not on this branch.**

(a) Revision-history narration survives throughout:

- B1's heading: "substantially stronger than Revision 1 describes — this section was stale"
- "narrower than Revision 1's ... framing" and "than Revision 1 described" (B1)
- "than Revision 1 recognized" (Tier)
- "dropped per F8's own finding" (Section A conclusion)
- "on corrected evidence" (A1 heading, Section A and B conclusions)
- "(§2 A3, corrected)", "§3 B3, corrected", "Per §0, corrected", "Per §2 A3, corrected" (§4)
- "a real correction, not disclosure-only" (§4 item 4)

That is roughly a dozen instances of the same kind the hygiene pass set out to remove. `tools/check_live_commentary.py` has no `World-Builds` surface, so no automated check will catch them.

(b) The Status line and §6 point to `Step0_Review_Round1.md`. The hygiene commit justified stripping the narration on the grounds that the record lives in that sibling file. But none of the six `Step0_Review_Round1.md` files exists on this branch, on `main`, or on `origin/main`. They exist only on the unmerged branch `origin/source-research/step0-review-round1` (commit `acd9a888`, not an ancestor of HEAD). As things stand, the audit trail the stripped narration was deferred to cannot be reached from the branch that carries the document. The Round 1 files need merging alongside this one.

### Minor

- **m1.** A1 quotes the corpus-map as saying Trent is `context` "precisely because 'it is not the Society's own composed voice.'" The corpus-map reads "since this is not the Society's own composed voice," in both the pre-hygiene and live versions. The quote is not verbatim.
- **m2.** B2 quotes the census as "founder-corpus gravity needs standard discipline... not a straightforward strength to claim." Those are two different census fields: `sourcing` ("...founder-corpus gravity needs standard discipline") and `statusDescription` ("...a discipline for any account of it to apply, not a straightforward strength to claim"). The ellipsis presents them as one passage. The document should quote each field separately.
- **m3.** This is a new observation, outside Round 1's scope. §0 is headed "relationship to the existing Step 0 record," but it does not mention that the census already carries `statusWord` "Researched — strong candidate" and a Tier 1 `statusDescription`. Round 1 flagged the same omission in the Hussite and Devotio Moderna documents. It does not change the result here, since the Tier 1 conclusion matches.
- **m4.** This is outside the document and should be flagged to the owning thread, not fixed here:
  - The dossier is still dated 2026-09-24, and its §3 still says "nothing is vendored."
  - Two live corpus-map notes (Nadal's *Adnotationes* and the Constitutions) now contain "Correction (2026-09-25): this note previously called..." narration, which is commentary inside a canonical surface.
  - The vendored file headers for both still read "this file is PRIMARY content," which contradicts the corpus-map.

## Confirmed accurate

- **F3 (Trent/Chalcedon) is correctly and precisely fixed.** I checked it myself in `council-of-trent_canons-and-decrees_waterworth1848.txt`:
  - Session III ("SESSION THE THIRD," l. 12301ff.) recites the full Niceno-Constantinopolitan Creed.
  - The recital is introduced as "the Symbol of faith which the holy Roman Church makes use of" (l. 12339–12340, verbatim across the line break).
  - Its only reference to Nicaea is the footnote "Concil. Nicnen." (l. 12366, OCR for *Nicaen.*).
  - No other Nicaea reference occurs anywhere in the decrees (l. 12200–29700).
  - "Chalcedon" occurs three times in the file. Two are in Waterworth's historical essay (l. 2820, 11383). The only occurrence in the decrees is at l. 19846, Session XXIII, Decree on Reformation, ch. XVI: "adhering to the traces of the sixth canon of the Council of Chalcedon, ordains that no one shall for the future be ordained without being attached to that church." This is disciplinary, not doctrinal.
  - The document states this exactly and does not claim a reaffirmation by name anywhere. The "almost clause for clause" match with Article 4 also holds against the recited text.
- **F2 (Chinese/Malabar Rites) is correctly fixed.** The document places the following inside the 1540–1650 window, and all of it is historically accurate:
  - Ricci (from the 1580s)
  - de Nobili at Madurai (1606)
  - Gregory XV's 1623 ruling (*Romanae Sedis Antistes*)
  - the Jiading conference (1627–28)
  - Propaganda's 1645 decree on Morales's questions

  The erroneous "1774" is gone. It correctly gives 1744 for Benedict XIV's Malabar condemnation and 1773 for the suppression. The document does not mention the 1704 and 1742 Chinese-rites rulings, which is acceptable because it never claims to list them all. Recasting the issue as a scope boundary for Doc_01 (§4 item 4) is right.
- **F4 (global claims narrowed or conditioned), F5 (Formula of the Institute, not Trent, is the charter; 1540/1550 and 1545–63 dates correct), F7 (Devotio Moderna cross-reference present, subject to M2), F8 (both superlatives dropped), F9 (positive floor evidence) and F10 (word counts) are all addressed.** For F9, the Autobiography's Manresa Trinity passage (l. 825–841) and the Exercises' Incarnation contemplation (Mullan l. 2225ff., "the Second Person shall become man") both exist as described. The Trinity passage bears more naturally on commitments 1 and 5 than on 2, but the claim is fair.
- **The hygiene rewrite preserved fidelity.** A line-by-line diff of `a67b1b2e` against `4b4ce830` shows no quote, date, citation, figure, or substantive claim dropped, softened, or distorted. The only content-level changes are these:
  - It removes Revision 1's erroneous "1704/1742/1774" narration (correctly) and adds one new, accurate framing sentence ("Its later, better-known condemnations do come well after 1650").
  - It removes "flagged here, not fixed by this revision" from B3 (see S2).
  - It removes the §6 finding recap (see M3b).
- **Article 4's five commitments** in the header are verbatim against the Constitution V2.3 text.
- The census's Atlas VI.11 entry, the 1540–1650 window, "Pre-Survey Candidate" status, the China/Japan/India/Brazil/Canada reach, and the Jesuit Relations listing all match the census.
- The Ganss 1970/1996 copyright status and Nadal's severe-OCR header flag match the vendored file headers and the dossier.

## Disposition

Per `cic-build-cycle`, S1 and S2 each make a binding §4 obligation false. Item 1 would lead Doc_02 to quote a garbled scan as primary text. Item 2 withholds a primary Faber source that is now available. Item 3 blocks Doc_02 on a corpus-map fix that has already been made. These are substantial findings, not requests to make the document "stronger."

A Round 3 revision should be bounded to four tasks:

1. Resync B1, B2, B5, the Tier section, and §4 items 1, 2, 3 and 5 to the live corpus-map and Mark's 2026-09-25 ruling. That means 19 works, Constitutions and Nadal as second witness because of OCR quality, the *Memoriale* vendored, the Trent split confirmed, and the coverage window re-dated.
2. Rewrite A4 and the §0 pointer (M1).
3. Correct the Coleridge/Alcazar attribution (M2).
4. Finish the narration strip, fix the two quotes (m1, m2), and merge the Round 1 review files so the document's pointer resolves (M3).

Round 3 would be the last round. If it does not clear, this becomes an escalation under the three-round cap, not a fourth round. The corpus-map and file-header drift in m4 belongs to the Library thread's owner and is flagged, not touched, here.
