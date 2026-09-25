# Step 0 Review, Round 3 — Lollardy

**Reviewer:** independent adversarial review agent (Opus), 2026-09-25, per `cic-build-cycle` discipline. Targeted recheck against Round 2 findings, not a full re-review. Final round under the three-round cap.
**Document reviewed:** `Step0_Movement_Scope_Confirmation.md`, Revision 3 (commit `1c25a20fc`).
**Checked against:** `Step0_Review_Round2.md`; `Ministry/Features/Atlas-World-Map/Decision-Log.md`; `Ministry/Features/Atlas-World-Map/Design/CiC_World_Atlas_PreStep0_Survey_V0_1.md`; `cic-website/data/world-census.json` at HEAD and at `8673befa`; `cic/corpus-map/lollardy.yaml`; `cic/texts/wyclif_select-english-works-v3_arnold1871.txt`, `wyclif_select-english-works-v1_arnold1869.txt`, `hus_de-ecclesia-the-church_schaff1915.txt`, `foxe_acts-and-monuments-v3_cattley-townsend1837.txt`; the sibling Hussite Step 0.

## Verdict

**CLEARED — approved to proceed**, subject to the four wording-level corrections under Minor, applied directly under `cic-build-cycle`'s cosmetic-revision rule (no fresh review cycle). All five Round 2 substantial findings and the Round 2 process finding are fixed. No new substantial finding. Nothing in the document is now wrong in substance, unsupported, or misleading on any sourcing, scope, or confidence conclusion.

## Round 2 findings — rechecked

**R2-S1 (Decision Log miscitation): FIXED.** §0 and A3 both now cite "2026-08-02 (Pass 3) — ERA 6 FROZEN by Mark; census 202→212; four eras Frozen in one day." Confirmed at `Decision-Log.md` line 4049. The Q4 item ("Q4 — Lollardy person-defined check CLEARED (its floorNote ordered the run)") sits at line 4069 under that entry. Quoted verbatim.

**R2-S2 (A1 quotes not verbatim; attribution overstated): FIXED for both Trinitarian quotes.** Checked against the file directly:
- Line 6397: `Sij)J)e  alle  ]?e  holi  Trinite  is  fadir  of  us  alle` — the document's quote matches, allowing only for the OCR's doubled spaces.
- Lines 21101–21104: `as ]?es ])ree persones of God ben o God and not manye, so alle dedes and werkes of ]pe Trinite mai not be departid from o])ir. For as al ])at ])e Fadir wole, ])e Sone wole, and ])is Goost wole` — matches the file across its line breaks, word for word and glyph for glyph.

The fabricated uniform "J?" is gone. The attribution is now consistent: A1 cites both tracts as "Wycliffite writing that Arnold ascribes to Wyclif." Arnold's headnotes are characterised accurately. The Pater Noster headnote (lines 6331–6345) rests on Bale's catalogue and says "No internal evidence points to Wyclif or any one else." The "þe chirche and hir membris" headnote (lines 20960–20985) argues from Bodl. 788, style, "Caymes castelis," and the Eucharist language ("I see little reason to doubt"). One residual defect in the same paragraph: see M1.

**R2-S3 (stale census `why` quotes): FIXED.** A5 and §4.5 now rest on `relationsSummary` ("Contested influence line to the English Reformation"), verbatim at HEAD line 13035. B4's appeal to the `why` field is narrowed to its trial-record half, which the live `why` supports: "trial records built to convict Lollards ended up preserving some of the fullest surviving statements of what ordinary medieval believers actually thought."

**R2-S4 (out-of-date sourcing): FIXED.** `cic/corpus-map/lollardy.yaml` has exactly eleven `source_file` entries. B1, B4, the Section B conclusion, and §4.2–§4.4 now all state eleven works. They name the four additions correctly (*Fasciculi Zizaniorum*, Foxe Vol. III, Loserth's *De Ecclesia*, Buddensieg's *De Veritate*). They mark Foxe and *Fasciculi* as hostile `role: context` material not yet content-assessed. Foxe's coverage (Thorpe, Sautre, Badby, Brute, Oldcastle) matches the corpus-map locus. The Tier question is now correctly reframed as content depth, not accessibility. §4.4's reference to Mark's 2026-09-25 Latin-as-primary ruling matches the corpus-map notes.

**R2-S5 (Hussite sibling never engaged): FIXED, honestly and without overreach.** B3 now names the Hussite and Bohemian Brethren candidate (V.6) and the direct textual dependence. The Schaff quotation ("Huss appropriated paragraph after paragraph from his predecessor and transferred them often with little verbal change to his own pages") is verbatim against `hus_de-ecclesia-the-church_schaff1915.txt` lines 1514–1516. The 712-line Foxe count is reproduced exactly (`grep -ciwE "hus|huss"` returns 712). The corpus-map note "was not checked for Hus/Bohemian content" is quoted correctly. B5 no longer contradicts the sibling: it limits the one-region claim to this document's own 2026-09-15 batch and concedes that the Hussite candidate is narrower. §4.7 carries the Foxe and *De Ecclesia* cross-assignment forward as a cross-world decision for Mark, and does not decide it. That is the right handling for a Step 0.

**R2-P1 (Round 1 record missing): FIXED.** `Step0_Review_Round1.md` is present in this folder (merged via `084e4bd20`).

**Round 2 minors:** the HathiTrust overclaim, the XML boilerplate, the "real correction" framing in §0, B1's past tense, the garbled B5, the unsourced A1 quote (now census `floorNote` plus Survey line 627 ff., both confirmed), the Arnold "spurious and doubtful writings" conflation (now kept separate from modern scholarship), the "unrelated story note" wording, and the uncited Tier are all fixed. Most process narration is gone. The residue is listed under M4.

## New findings

### Substantial

None.

### Minor, but actually wrong (wording-level; apply directly, no fresh review cycle)

**M1. A1's Ascension/Pentecost quote is normalised, while the paragraph says every quotation is byte-exact.** A1 now says "the quotations below reproduce it exactly as it appears, artifacts included." The third quotation in the second bullet, "Aftir þat Crist was stied in to hevene, aboute ten daies … he sente," does not do that. The file (lines 21104–21105) reads `Aftir  ]?at  Crist  was  stied  in  to  hevene,  aboute  ten  dales, … he  sente`: the thorn is rendered as `]?`, and "daies" is OCR'd as "dales." Round 2 accepted this reading as correct. That was right as a reading, but the paragraph now mixes a normalised quote with byte-exact ones, which R2-S2 said not to do. Fix: quote it as `Aftir ]?at Crist was stied in to hevene, aboute ten dales` (the same OCR convention), or label it explicitly as a normalised reading. The meaning is unchanged either way.

**M2. B4 says the census "itself names" Hudson's *Two Wycliffite Texts*. B1 correctly says it is not a census source.** B4 reads: "the two trial-record sources the census itself names (Tanner, the Thorpe *Two Wycliffite Texts*)." I checked the census at `8673befa` and at HEAD. Tanner is a census source. *Two Wycliffite Texts* appears nowhere in either version, not even under the Thorpe story added since (whose sources are Lahey/Wyclif Society, Hudson's *Selections*, *EWS*, Tanner, Hudson/McSheffrey, and the Cambridge chapter). Fix: "the two trial-record sources named in §3 B1 (Tanner, the Thorpe *Two Wycliffite Texts*)." The sourcing conclusion (both borrow-only) is unaffected.

**M3. §4.3 states the authorship of Arnold Vols. I–II more flatly than B2 does.** B2 says "modern scholarship generally treats this cycle … as Wycliffite (collective) rather than Wyclif's own." §4.3 says flatly that they "are collective/Wycliffite preaching material, not Wyclif's own personal writing." The authorship of the *English Wycliffite Sermons* cycle is a genuinely argued question. Per CLAUDE.md, a contested claim should not be stated as settled. Fix: align §4.3 with B2 ("generally treated by modern scholarship as collective/Wycliffite …").

**M4. Small residues.** (a) A1's list of thorn variants ("as `]?`, `])`, or `]p`") is not exhaustive. The first quote itself shows `j)J)`, and the passage also has `]>`, `))`, `}>`. Add "among others." (b) Some process narration is still in the text: §4.3's heading "Sourcing correctly scoped" and its "no longer an open acquisition item"; B1's heading "a real correction to the census's own prior record." Neutral headings would do.

## Out-of-scope observation (for the Hussite thread, not this document)

The Hussite Step 0 (line 78) calls Lollardy's shelf "eight Wyclif-authored works filed `role: tradition`." This document, correctly, treats Arnold Vols. I–II and much of Matthew as Wycliffite (collective) with contested ascription. The two sibling documents therefore state the same underlying fact differently, which `cic-build-cycle`'s cross-document consistency rule asks to reconcile. The fix belongs in the Hussite document. It is logged here so it does not go quiet.

## Confirmed accurate

- Article 4 quotations unchanged from the Round 1-verified text.
- Census `floorNote` (A1, A3) and `relationsSummary` (A5, §4.5) verbatim at HEAD (lines 13034–13035).
- Pre-Step0 Survey V.5 floor note: "no plain-reading creedal question (eucharistic and ecclesiological dissent, not trinitarian)" at lines 627–633, as cited.
- Arnold Vol. I "spurious and doubtful writings": verbatim substring, now correctly limited to Shirley's catalogue.
- Eleven vendored works; Foxe's 712 Hus lines; the Schaff quotation; the corpus-map notes quoted in B3.
- Escalation check: the Foxe and *De Ecclesia* cross-assignment is a cross-world decision, but this document only names it and carries it forward to Mark. It does not decide it, so it does not trigger escalation of this document's own disposition. The question itself stays open as a Library-thread item for Mark (§4.7).

## Disposition

Round 3, the final round under the cap. No substantial finding remains. M1–M4 are wording, attribution-phrasing, and transcription-convention fixes that change no claim's substance, confidence rating, sourcing conclusion, or scope boundary. Under `cic-build-cycle`'s Revision decision rule, they are applied directly and noted, without another review cycle.

**CLEARED — approved to proceed**, once M1–M4 are applied and noted. M1 should be applied before the document is cited anywhere, because it concerns a string inside quotation marks. The cross-world corpus-map question (§4.7) remains open for Mark as a separate item. It is not a condition of this disposition.
