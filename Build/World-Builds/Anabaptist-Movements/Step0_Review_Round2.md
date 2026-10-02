# Step 0 Review, Round 2 — The Anabaptist Movements

**Reviewer:** independent adversarial review agent (Opus), 2026-09-25, per `cic-build-cycle` discipline. Targeted recheck, not a full re-review.
**Document reviewed:** `Step0_Movement_Scope_Confirmation.md` at "Revision 2", as it stands at HEAD after the narration-stripping hygiene pass (commit `4b4ce830`).
**Checked against:** Round 1 findings F1–F11 (`Step0_Review_Round1.md`, commit `acd9a888`); the Revision 1 → Revision 2 diff (`a67b1b2e`); the hygiene diff (`4b4ce830`); the vendored files in `cic/texts/`; `cic/corpus-map/the-anabaptist-movements.yaml`; `Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md`; `cic-website/data/world-census.json`; `Build/worlds/latap/Step0_Movement_Scope_Confirmation.md`.

## Verdict

**Substantial revision needed, but targeted.** The core Round 1 repairs are real, not cosmetic. Every quote in the document was grepped against its vendored file and is present verbatim; the only differences are OCR noise. The "as through a channel" misattribution is gone. The Christology now reaches Dirk Philips and rests on his and Menno's own words. The Donatism dating agrees with itself throughout. The floor is argued from affirming confessions, not from absence.

The hygiene pass did not drop, soften, or change any fact, quote, date, or citation. I checked every changed line in the diff.

Two things still fall below the bar. First, the sourcing record is again out of date. The same-day 2026-09-25 vendoring pass (#589, merged before Revision 2's #587) makes several statements in B1, A1, B2 and §4 false. One of them sits under a binding Tier condition. Second, the fix for F9 introduced a new mis-citation: Lactantius's complications are called "Christological", and they are not.

There are also two process defects. The Round 1 review the document points to does not exist on this branch or on `main`. And the narration strip is incomplete. The headline conclusions (clears Section A; Tier 1, provisional) still look like they will survive.

## Findings

### High severity

**R2-1. The sourcing record is out of date against the 2026-09-25 vendoring pass, and it now states things about the corpus that are false (§2 A1, §3 B1, B2, Tier conclusion, §4 items 2 and 6).** The pass (`79b68940` / #589) vendored and assigned three new works to this world, as `cic/corpus-map/the-anabaptist-movements.yaml` records. The document still describes the corpus as it stood on 2026-09-24.
- §3 B1: "Hubmaier's and Marpeck's own primary voices have no confirmed PD English translation anywhere." This is false for Hubmaier. `vedder_balthasar-hubmaier_1905.txt` is vendored. Its Appendix (pp. 273–322) is a complete English translation of Hubmaier's 1527 *On the Sword*. The file header and the corpus-map both say so, and the corpus-map says it "reopens the Hubmaier sourcing gap partially."
- §2 A1: "Grebel, Manz, and Hubmaier have no vendored writings at all." This is false for Hubmaier, for the same reason.
- §3 B1 and §4 item 6: the Ausbund hymnal and "the Dordrecht Confession's own separate publication history" are "neither assessed nor formally closed." Both are now vendored and assigned: `ausbund_lancaster1846-deu.txt` and `dordrecht-confession_ministers-manual_elkhart1890.txt` (the standalone 1890 Elkhart edition).
- §3 B2 and §4 item 2 describe the Hutterite *Geschicht-Buch* as "German, not yet content-assessed." Its status has changed. Under Mark's 2026-09-25 library ruling and OCR ruling "a", it is a garbled scan held to second-witness status. The Ausbund has the same status. Language is no longer the reason. The document's "unsourced in English" framing of Hubmaier and Marpeck (B2) also rests on the retired English-only rule.
- §3 B1: "Anabaptist sourcing... runs second-largest" by raw volume. This is no longer true. I summed `wc -w` over each world's corpus-map `source_file` list for the six worlds the Round 1 comparison used. The totals are Lollardy ~4.95M, Society of Jesus ~3.37M, Tridentine ~2.91M, Anabaptist ~2.66M, Reformed Cities ~2.30M and Wittenberg ~0.96M, so Anabaptist is now fourth. The defensible claim ("not thinnest by volume; thin in named-theologian range") still holds. The ranking does not.
- Tier conclusion, binding item 2 ("Hubmaier/Marpeck's still-effectively-unsourced voice") and §4 item 2 therefore overstate a gap that is now partly closed.

**Fix:** Rebuild B1 against the current corpus-map, with eight works. Restate the Hubmaier gap as partly closed: *On the Sword* in full, plus the *Martyrs Mirror* material. Marpeck and Grebel stay closed, per the dossier's §4. Reclassify the Ausbund and the Hutterite chronicle as vendored second witnesses under OCR ruling "a". Move the standalone Dordrecht edition out of the "unassessed" list. Leave only the Täuferakten and Harder open in §4 item 6. Drop or recompute "second-largest". Rescope Tier item 2 and §4 item 2 to match. This is F6's defect class again, so date-stamp the sourcing claim against the corpus-map revision it was checked against.

**R2-2. The audit trail the document points to is missing from the tree (Status line; §6).** The hygiene pass removed the in-document recap of F1–F11. It replaced the recap with "(See `Step0_Review_Round1.md` for the full finding list)" because that record "belongs in the sibling Step0_Review_Round1.md file." That file is not on this branch (`library-thread/step0-revision2-hygiene`) or on `origin/main`. `git ls-tree` finds no `Step0_Review_*` file under `World-Builds/` for any of the six worlds. The only copy is commit `acd9a888`, on the unmerged remote branch `source-research/step0-review-round1`. As things stand, no merged surface records that Round 1 happened or what it found. This is not a content defect in the document. It is a real gap in the permanent review trail, and it affects all six Step 0 documents, not only this one.

**Fix:** Bring the six `Step0_Review_Round1.md` files from `acd9a888` into this branch, beside this Round 2 file, so that every pointer resolves.

### Medium severity

**R2-3. The F9 fix introduced a new mis-citation: "Lactantius's own positive Christological complications" (§2 A1, last paragraph of the Christology discussion).** The Latin Apologists' Step 0 (`Build/worlds/latap/Step0_Movement_Scope_Confirmation.md`, the Lactantius paragraph and the Resolution) records Lactantius's complications as **pneumatological** and **eschatological**, not Christological. The pneumatological one is Jerome's *Ep.* 84.7 charge that he "altogether denies the subsistence of the Holy Spirit," which bears on commitment (5). The eschatological one is the chiliasm of *Institutes* VII. Round 1's F9 said only "Lactantius's own positive complications." Revision 2 added "Christological" without support. The precedent still fits as a *kind*: positive, argued teaching rather than silence. It does not fit as the same *commitment*.

**Fix:** Change the phrase to "Lactantius's own positive pneumatological and eschatological complications." Say explicitly that the precedent is about the *kind* of complication (argued teaching, not absence), not about the same commitment.

**R2-4. The Herman quotation is cut at a point that hides the martyr's own affirmation of the doctrine, and the scope heading understates the reach (§2 A1, heading and paragraph 2).** The document ends Herman's reply at "cannot be found in his writings." In the vendored *Martyrs Mirror* the sentence goes on: "...cannot be found in his writings; but he shows with many Scriptures, that the Word became flesh (as John writes in his first chapter), and not the seed of Mary." Herman rejects the sieve/spout *image*, but he affirms the *doctrine*: Christ's flesh is not "the seed of Mary." So the complication also reaches the *Martyrs Mirror*, which is the third of the three named-author pillars (dossier §5: Swiss/martyrological, Dutch/Menno, Dutch/Philips). It also reaches the Dordrecht text reproduced there. The heading "reaching two of its three named-author pillars" is therefore short by one. This is the same kind of scope error as F4.

**Fix:** Quote Herman's reply through "and not the seed of Mary." Retitle A1 to say the complication reaches all three Dutch-register pillars: Menno, Dirk, and the *Martyrs Mirror*'s own testimony. Carry the same scope into the Section A conclusion and §4 item 1.

**R2-5. F10 is only half fixed: Hubmaier is still grouped with the Swiss wing and with its non-resistance (§2 A1, §3 B2).** Revision 2 deleted Revision 1's "Swiss Brethren wing (Grebel, Manz, Hubmaier)" sentence. But A1 still groups "Grebel, Manz, and Hubmaier" as "the Swiss wing." B2 still calls Hubmaier and Marpeck "the two Swiss/South German theologians." F10's substance is not addressed anywhere. Hubmaier's base was Nikolsburg, in Moravia, and his *On the Sword* (1527) rejects Schleitheim's non-resistance. §1's "(predominantly) pacifism" and §4 item 4's three-region coherence question both depend on this. Round 1 flagged it as unverified general knowledge. It can now be checked directly: *On the Sword* is vendored in full (Vedder Appendix, addressed to lords of Moravia), and "Nikolsburg" appears 72 times in the Vedder file.

**Fix:** Place Hubmaier in Moravia. Disclose that his own vendored treatise dissents from Schleitheim on the sword. Name that dissent as part of §4 item 4's coherence question.

**R2-6. The affirmative floor evidence is from the Dutch wing only, and the Swiss and Moravian wings still rest on the absence test the document itself calls empty (§2 A1, Section A conclusion).** All three affirming texts are Dutch: Dordrecht 1632, the Waterlander Confession (Ries and Gerrits, 1580), and Dirk's *Enchiridion*. A1 rightly says an absence test "would be empty for the Swiss wing." It then grounds the floor affirmatively "instead" in Dutch texts, and does not say that this leaves the Swiss and Moravian wings resting on "no source checked... denies the Trinity," which is an absence claim. The floor verdict holds for the three-region "movement" only if §4 item 4's still-open coherence argument succeeds. The document does not connect those two points. Candidate affirmative leads already in the corpus, none of them checked here:
- McGlothlin pp. 13–18: an editorial summary of Riedemann's Hutterite *Rechenschaft* (c. 1545). It says the work expounds "the twelve articles" and gives a Trinitarian baptismal formula. This is McGlothlin's summary, not Riedemann's own text, and must be disclosed as secondary.
- Hubmaier's material in Vedder.

**Fix:** State plainly that the affirmative floor evidence is Dutch-wing only. Link the Swiss and Moravian floor question to §4 item 4. Name the leads above for Doc_02 without treating them as settled.

**R2-7. The narration strip is incomplete, despite the hygiene commit saying it rewrote "every such paragraph."** The following process narration remains in this document, all in `World-Builds/`, which CLAUDE.md lists as a canonical surface:
- A1, paragraph 2: the bold lead "— and this revision corrects both the quotation used to characterize it and its scope"; "Revision 1 attributed to Menno the phrase..."; and "repeating it as though it were his own words would have been exactly the kind of quote-verification failure CLAUDE.md's source-fidelity section treats as a recurring, serious defect."
- The B1 heading: "— corrected against the census and brought current".
- B1: "not four as Revision 1 listed"; "omitted entirely from Revision 1"; "corrected in framing"; "'effectively unsourceable' overstated a clean zero"; "The 'no figure word-extracted from vendored XML' caveat from Revision 1 is stale..."
- The Section A conclusion: "now grounded in their own actual words rather than an inherited, unverified quotation".
- The Tier heading paragraph: "now reaching both Menno and Dirk".
- §4 item 1: "scope corrected" and "rather than an inherited, unverified quotation".
- §4 item 5: "scope expanded" and "New in this revision:".
- §5: a paragraph still labelled "**Correction (Revision 2):**", unchanged from the pre-hygiene text, and "at Revision 1".

§5 ("Process findings for System Hub") is arguably a designated process section. Even so, its "Correction (Revision 2)" label is exactly the pattern the hygiene commit said it removed.

**Fix:** Restate each of these as a present-tense fact. The content itself is sound, and the Menno misattribution is worth keeping as a present-tense source-fidelity note ("this phrase is an opponent's caricature, not Menno's wording"). The revision history belongs in the review files (see R2-2).

**R2-8. The root cause of F3 is still uncorrected upstream.** `Build/worlds/_cross-world/dossiers/the-anabaptist-movements_Source_Readiness_Dossier.md` §5, "Trinity/Christology" paragraph, still attributes "as through a channel" to Menno. It still gives Minucius Felix as the precedent, and its §4 still lists Vedder as "closed," which the corpus-map now contradicts. Doc_01 and Doc_02 will read that dossier. This is outside this document and outside this thread (per the default-actions table: flag it, don't touch it). It is recorded here so the root cause is not left in place while only the symptom is fixed.

**Fix:** The owning source-research thread should correct the dossier's §5 and §4 entries.

### Low severity

**R2-9.** "Rejecting his opponents' Christology outright as one of several 'abominable errors'" (A1) is a loose paraphrase. Menno's *Reply to Gellius Faber* says that "weighty and intolerable improprieties and abominable errors result from their confession." The errors are consequences he draws from the confession ("First, A divided Christ..."). He does not call the confession itself one error among several. Rephrase it to follow his own construction.

**R2-10.** The cross-references introduced by the hygiene pass point the wrong way. §0 says the ~1,100-year gap is stated "as §3 B3 states." B4 cites "the gap is roughly 1,100 years, per §3 B3." B3 says only "over a millennium's separation." The 1,100-year figure is in §0. The meaning is consistent; only the pointers are wrong.

**R2-11.** Minor citation looseness, some of it older than this round:
- The Waterlander quotation is cited as "Article II–III," but both quoted sentences are in Article II.
- The VI.14 name is given in quotation marks as "Anti-Trinitarian currents — Servetus, Polish Brethren." The census name is "Anti-Trinitarian Currents (Servetus; Polish Brethren/Socinians; Transylvanian Unitarians)." Either quote it exactly or drop the quotation marks.
- The census phrase "RICH in ordinary inside voice" is quoted without the census's own qualification in the same record: "read with care for genre... Its court testimonies are coerced, not plain inside voice."

## Confirmed accurate

- **All quotations verified verbatim** against the vendored files, with whitespace and hyphenation normalized. Where there are differences, they are OCR noise only ("up- roarious", "tous", "suftering", "for-neither", "incom- prehensible", "In sacred"). None of the wording is altered.
  - Menno's anti-Donatist sentence (`menno-simons_complete-works_funk1871.txt`).
  - Dirk's "liken us to the Donatists... A great injustice is done to us" (`dirk-philips_enchiridion_kolb1910.txt`).
  - Dordrecht Article I and the Article IV "conceived in the virgin Mary." Both are confirmed inside the *Martyrs Mirror*'s "Third Confession Drawn up at Dort... 21st of April, 1632," not in the two Amsterdam confessions reproduced beside it.
  - Waterlander Articles II and VIII (McGlothlin; Ries and Gerrits, 1580).
  - Dirk's Trinitarian sentence, with the elision checked.
  - The friar Cornelis's "sieve... spout" line and Herman's reply (see R2-4 on the truncation).
  - Menno's "truly God and man... in Mary, the pure virgin... planted in her... fed and nourished in her virgin body." This is confirmed to sit inside *Reply to Gellius Faber*, just after "THE CONFESSION OF THE LEARNED CONCERNING CHRIST," with the elisions checked and fair.
  - "the man of Mary's flesh" (7 occurrences, used as the opponents' position).
  - Dirk's "impossible for the flesh of Christ to be formed by Mary," inside his Incarnation section.
- **"As through a channel" does not appear anywhere in the Menno file.** F3's premise is independently re-confirmed.
- **F1 fixed.** Donatism is c. 311–439 CE per the census, against 1525. "Roughly 1,100 years" and "over a millennium" are consistent in §0, B3 and B4. No "two centuries" remains.
- **F2 fixed.** The echo is framed honestly as the document's own outside observation. The movement's own repudiation is quoted and carried into §4 item 5.
- **F4 fixed**, apart from the further scope point in R2-4.
- **F5 fixed in method**: the floor is argued from affirming confessions, with R2-6's Dutch-only caveat.
- **F6 fixed as of 2026-09-24.** The counts match `wc -w`: Menno 531,221; *Martyrs Mirror* 1,187,986; Dirk 207,849; Hutterite 351,933, for a total of ≈2.28M, which "roughly 2.3M" rounds correctly. The Hutterite chronicle is included. The XML caveat is withdrawn. R2-1 covers what has changed since.
- **F7's census quotations are exact**, apart from R2-11.
- **F8 fixed.**
- **F11 fixed.**
- **The *Martyrs Mirror*'s Hubmaier material exists as described**: "BALTHASAR HUBMOR, AND HIS WIFE" and the note on his complaint against Zwingli.
- **The hygiene pass preserved meaning.** I compared every changed line of `4b4ce830` for this file. Each rewrite keeps the same facts, quotes, dates and citations. The only content removed was the Status and §6 recap of Round 1, and that loss is only a problem because of R2-2.

## Disposition

Per `cic-build-cycle`, R2-1, R2-3, R2-4 and R2-6 are statements that are wrong, unsupported, or incomplete in a way that misleads. They are not polish, and they meet the bar for a further revision. R2-2 is a process defect to fix alongside that revision, and it affects all six Step 0 documents. R2-7 is canonical-surface hygiene. R2-8 is flagged to its owning thread and should not be fixed here. R2-9 to R2-11 are low.

None of this reopens the headline conclusions. Every fix is precise and local, and Round 3 should be a narrow recheck of exactly these items. **This is Round 2 of the three-round cap.** If Round 3 does not clear, the pipeline has reached an unresolved tension it cannot close by itself, and the document escalates rather than going to a fourth round.
