# Cold Review — Doc_02 "Source Ecology" (World #1), Round 2 (Independent, Post-Round-1-Fix)

**Reviewer:** Independent adversarial pass. Round 1's cold review (`doc02_cold_review_round1.md`) and the document's own Section 13 log describing "Round 1 fixes applied" were read for context, but every claim in both was independently re-verified against the live document, the live Registry workbook, and freshly-fetched primary/secondary sources rather than taken on trust. Scope followed the brief: (A) re-verify the Philadelphians 4 / Smyrnaeans 8 fix, (B) check the two new Registry rows and Registry-wide consistency, (C) check the two new confidence tags, (D) a fresh independent pass over claims round 1 did not focus on.

---

## A. The Philadelphians 4 / Smyrnaeans 8 fix

Independently fetched the Roberts-Donaldson/ANF translations of both letters directly from newadvent.org (fathers/0108.htm for *Philadelphians*, fathers/0109.htm for *Smyrnaeans*).

- *Philadelphians* ch. 4 ("Have but one Eucharist, etc."): "Take heed, then, to have but one Eucharist. For there is one flesh of our Lord Jesus Christ, and one cup... one altar; as there is one bishop..." — **matches the document's current attribution exactly.**
- *Smyrnaeans* ch. 8 ("Let nothing be done without the bishop"): "Let that be deemed a proper Eucharist, which is administered either by the bishop, or by one to whom he has entrusted it... It is not lawful without the bishop either to baptize or to celebrate a love-feast..." — **matches the document's current attribution exactly**: bishop-authorization over eucharist, baptism, and love-feast, with no "one eucharist" numerically-emphatic language anywhere in this chapter.

Checked the current Section 4 text line by line: the original sentence now reads "*Philadelphians* 4's 'one eucharist' instruction... and, separately, *Smyrnaeans* 8's own requirement that a valid eucharist be administered only by or with the bishop's authorization," and the correction paragraph now reads "*Smyrnaeans* 8, already cited immediately above for its bishop-authorization requirement over the eucharist, extends the identical requirement to a further practice in the same chapter: 'It is not lawful without the bishop either to baptize or to celebrate a love-feast.'" Both are now accurate. No trace of the reversed attribution survives anywhere in the current document (grep-checked every occurrence of "Smyrnaeans" and "Philadelphians").

Checked Registry row P03 directly: **Licensed For** now reads "...Doc_02 liturgical evidence (Philadelphians 4's 'one eucharist' instruction; Smyrnaeans 8's bishop-authorization requirement over baptism, eucharist, and love-feast)..." and **Notes** states plainly "Doc_02 Sec.4 previously misattributed the 'one eucharist' clause to Smyrnaeans 8 rather than Philadelphians 4 -- fixed after independent verification against two translation traditions. Smyrnaeans 8 itself is licensed for its own distinct bishop-authorization clause, which covers baptism, eucharist, AND love-feast." Both fields are now accurate and consistent with the narrative and with each other.

**Verdict on Task A: RESOLVED.** The fix is genuine, accurate, and applied consistently in both places it needed to be. No residual instance of this error found anywhere in the current document or Registry.

---

## B. The two new Registry rows (S56 Myllykoski, S57 Hartog)

Read both rows directly from the live workbook. S56 (Myllykoski/HULCE, Documented, Priority Flag No) is licensed for the specific "fifteen manuscripts / six alpha / nine beta / stemma" claim in Sec. 1.4. S57 (Hartog 2013, Documented, Priority Flag No) is licensed for the specific "eight manuscripts, stemmatically-filtered" claim, with its Notes explicitly distinguishing it from S44's bundled, debate-level scope. Cross-checked against S44 (the Harrison/Hartog/Holmes/Berding "position-cluster" row) and S45 (Kirsopp Lake / Hermas-Athos manuscript dating): no duplication or conflict — S44 is a different debate (Polycarp unity/two-letter-splice) explicitly reserving individual-scholar claims for their own rows, S45 is an unrelated manuscript (Hermas's Codex Athous/Grigoriou 96, not Polycarp's), and S56/S57 are each scoped to a distinct, narrow, individual claim. No ID collisions (72 total rows, all unique).

`recalc.py` **could not be run or even located** — no file by that name exists anywhere in the working directory (confirmed by direct search), despite the document's Section 13 log citing "`recalc.py` confirms 0 errors post-fix" in an earlier round. This may simply mean the script is ephemeral/not persisted between build sessions, but it means the log's claim about this round's own recalculation could not be verified by rerunning the named tool. In its place, an independent equivalent structural check was performed directly against the workbook:

- Total Source Registry rows: 72 (70 + S56 + S57), no duplicate IDs.
- Priority Review Queue: 45 rows, exactly matching the 45 rows flagged `Yes` in the main sheet — no drift, no orphaned entries (S56/S57 correctly excluded, since both are Flag=No).

This part passes. **However, a real defect was found that a proper recalc should have caught:** the workbook's three derived cross-reference sheets — "By Confidence Level," "By Boundary Status," and "By Author" — were **not regenerated** after S56 and S57 were added. All three sheets still contain exactly 70 source rows and are missing S56 and S57 entirely. This is not a pre-existing, chronic gap: S48 through S55 (the rows added in the earlier five-round history) **do** appear correctly in all three views, confirming these sheets were properly kept in sync through every prior round and that this specific staleness is a new regression introduced by *this* round's fix pass, not an inherited problem. The "By Author" sheet's own stated purpose ("Cross-reference: every row grouped by Author/Voice, so Author Gravity concentration... is visible structurally") is directly undermined by this gap — a builder using that view to check whether any one voice is over-relied-upon would not see Myllykoski or Hartog at all.

**Verdict on Task B: SUBSTANTIAL.** The new rows themselves are well-formed, correctly scoped, and non-duplicative, and the Priority Review Queue is in sync — but the three derived index/view sheets were not regenerated to include them, a genuine, freshly-introduced Registry-consistency defect (not merely a documentation gap, since these sheets are meant to be exhaustive structural indices, not curated summaries).

---

## C. The two new confidence tags (Sections 3, 9)

**Section 9** now reads: *"[Documented that Pliny's letter and Ignatius's own corpus attest state pressure directly; Inferential-Thin on the institutional-silence-as-legal-risk mechanism and on the survivorship-pattern argument, both of which are this document's own inference from absence rather than directly attested.]"* This is accurate and well-scoped: it correctly separates the two directly-attested facts (Pliny, Ignatius) from the two speculative mechanisms the section itself proposes (institutional silence as legal-risk avoidance; survivorship bias), and it uses the document's own vocabulary correctly (Documented / Inferential-Thin, not a manufactured tier). **This part of the fix is complete and sound.**

**Section 3's fix is only partial.** The new tag — *"[Documented that no institutional self-documentation survives; Inferential-Thin as to why — the legal-risk explanation offered in Section 9 below is this document's own inference, not a directly-attested cause.]"* — is itself accurate and well-calibrated, but it is attached only to the "What does not exist" paragraph. Round 1's finding explicitly called out **two** distinct mixed-certainty claims in this section: the flat "no institutional records survive" claim *and* the more interpretive claim in the "What exists" paragraph that the Didache's transition instructions (Did. 15:1) are "read by scholars as evidence of an office structure still actively forming, not yet standardized." That second claim — a specific interpretive/scholarly-reading claim, exactly the kind of thing the document tags everywhere else (e.g., Section 1.1's "read by scholars" language is tagged Contested/Inferential-Thin) — remains untagged. The section is no longer *entirely* without tags, but it still does not match the density/consistency of tagging found in Sections 1, 2, 4, 5, 6, 7, and 10.

**Verdict on Task C: COSMETIC** (Section 9's tag is a clean, complete fix; Section 3's tag is accurate as far as it goes but only half-closes the gap round 1 identified — a residual, low-stakes inconsistency, not a substantive claim problem).

---

## D. Fresh independent pass — claims round 1 did not focus on

Went beyond the requested five and independently checked the following against external sources, deliberately looking for the same species of error as Task A (right source, wrong specific citation/attribution within it):

| Claim (Section) | Check | Result |
|---|---|---|
| Raymond E. Brown is "primarily a Johannine specialist" whose *Churches the Apostles Left Behind* touches Ignatius/Clement "at the margins" (Sec. 2) | Independently confirmed via biography: Brown's entire scholarly identity centers on the Gospel/Epistles of John and the hypothesized Johannine community | Accurate |
| Peter Lampe's *From Paul to Valentinus* is "unchallenged as the reference monograph on Roman house-church topography" (Sec. 2) | Confirmed: Lampe's career centers on social history of Roman Christianity; this monograph remains the standard reference | Accurate |
| Aaron Milavec's "current professional identity has shifted to gender studies" (Sec. 2) | Independently confirmed: Milavec is emeritus faculty in Gender Studies at the University of Roehampton (Catherine of Siena Virtual College), post-dating his Didache commentaries | Accurate |
| Timothy D. Barnes's Ignatius contribution "is a single 2008 article" (Sec. 2) | Confirmed: Barnes, "The Date of Ignatius," *Expository Times* 120.3 (2008), arguing for a 140s redating via the Ptolemaeus-dependency argument — one article, not a sustained Ignatian research program | Accurate |
| Kristina Sessa's argument that every site conventionally called *domus ecclesiae* except Dura-Europos postdates Constantine (Sec. 5) | Confirmed directly against Sessa's own published argument (JTS / recent Journal of Roman Archaeology treatment): Dura-Europos is explicitly the sole pre-Constantinian exception in her analysis | Accurate |
| Dura-Europos dated "c. 232–256 CE" (Sec. 5) | Confirmed: renovation dated by inscription to 232/233 CE; city (and the building's use) ends with the Sassanian siege in 256/257 CE | Accurate |
| Suetonius, *Life of Nero* 16.2, "no explicit fire connection stated" (Sec. 6) | Confirmed: the passage ("Punishment was inflicted on the Christians, a class of men given to a new and mischievous superstition") sits in a list of Nero's public-order measures, with the 64 CE fire link supplied only by scholarly inference from context, not the text | Accurate |
| Keith Hopkins's ~2% literacy-sufficient-to-author-texts estimate (Sec. 7) | Confirmed: Hopkins estimated sophisticated/fluent literacy at under 2% of the (male) population, consistent with the document's figure and framing | Accurate |
| Alexamenos graffito "c. 200 CE, borderline at best" (Sec. 5) | Confirmed: mainstream dating range runs late 1st–late 3rd century, with "around 200 CE" the most-favored specific estimate — the document's "borderline" hedge is a fair characterization | Accurate |
| Éric Rebillard's argument that burial was organized by family, not ecclesial identity, in this period (Sec. 5) | Confirmed against Rebillard's own published work (*Care of the Dead in Late Antiquity*, *Christians and their Many Identities*): family/next-of-kin, not the institutional church, governed burial practice, with no consistent Christian/non-Christian separation in cemetery epigraphy this early | Accurate |
| The Pseudo-Ignatian long recension (not the authentic middle-recension letters) is the actual source of "deaconess" references sometimes wrongly attributed to Ignatius (Sec. 7) | Confirmed: the six spurious long-recension letters (4th/5th-century interpolations) are where such material appears; the seven authentic middle-recension letters do not contain it | Accurate |
| Codex Alexandrinus loses 1 Clement from 57:7 through the end of ch. 63, supplied by Codex Hierosolymitanus (Sec. 1.2) | Confirmed: Alexandrinus is missing exactly this span (a lost leaf, mid-prayer), and the 1056 CE Bryennios manuscript is the source that supplies the missing text | Accurate |

**No new instance of the Philadelphians/Smyrnaeans species of error (correct source, wrong specific citation within it) was found anywhere in this sample.** Every claim independently checked in this pass held up, including several that involve exactly the kind of fine-grained, easy-to-swap attribution (which specific chapter, which specific manuscript, which specific recension) that let the original error survive five prior rounds. This is a reasonably broad and adversarially-targeted sample (twelve claims across Sections 1, 2, 5, 6, and 7, deliberately weighted toward citation-swap risk) and it did not reproduce the error class the brief was concerned about — a meaningful negative result, though it cannot rule out an error existing outside this sample.

**Verdict on Task D: no issues found.**

---

## Summary of findings

| # | Finding | Severity |
|---|---|---|
| 1 | Philadelphians 4 / Smyrnaeans 8 attribution: fully and correctly fixed, in both the narrative and Registry P03 | RESOLVED (no defect) |
| 2 | S56 (Myllykoski) and S57 (Hartog) rows: well-formed, correctly scoped, non-duplicative with S44/S45; Priority Review Queue in sync | RESOLVED (no defect) |
| 3 | The three derived Registry view sheets ("By Confidence Level," "By Boundary Status," "By Author") were not regenerated and are missing S56/S57 entirely — a newly-introduced regression, since S48–S55 are correctly present in all three | SUBSTANTIAL |
| 4 | `recalc.py`, cited in the document's own log as the verification mechanism, does not exist anywhere in the working directory and could not be run to independently confirm "0 errors" this round | SUBSTANTIAL (process gap — the specific claim in the log is unverifiable by the means it names, even though an equivalent manual check was substituted) |
| 5 | Section 9's new confidence tag is accurate and complete | RESOLVED (no defect) |
| 6 | Section 3's new confidence tag covers only the "What does not exist" paragraph; the "What exists" paragraph's interpretive claim about Didache 15:1 (office structure "still actively forming") remains untagged, unlike equivalent interpretive claims tagged elsewhere in the document | COSMETIC |
| 7 | Fresh, adversarially-targeted spot-check of twelve claims in Sections 1, 2, 5, 6, and 7 (scholar-expertise attributions, material-evidence claims, outside-witness claims, manuscript-lacuna claims) — all confirmed accurate; no new instance of the misattributed-citation error class found | No issues found |

---

## Overall verdict: SUBSTANTIAL REVISION REQUIRED

Narrow in scope. The specific defect this reopening exists to fix — the Philadelphians 4 / Smyrnaeans 8 misattribution — is now genuinely and consistently corrected everywhere it appears, and the two new Registry rows are sound. But this round's own fix pass introduced a fresh, verifiable regression: three of the Registry's own cross-reference/index sheets, which had been correctly kept in sync through every prior round, were not updated for the two new rows, and the log's cited verification tool (`recalc.py`) is not present to independently confirm otherwise. This is mechanically simple to fix (regenerate the three view sheets, or add S56/S57 to them directly, and confirm the recalculation script itself is either restored to the working directory or its check reproduced and documented) but it is a genuine structural-consistency defect in the Registry, not a wording issue — the same species of "the fix touched one place but not its downstream copy" problem this document's history has repeatedly had to catch (P03's Licensed For vs. Notes in round 1 of this reopening; the Priority Queue drift in round 2 of the original five-round history). The one cosmetic item (Section 3's partial tag fix) is low-stakes and can be closed at the same time without a further review cycle.
