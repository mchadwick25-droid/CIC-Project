# Round 3 (final) targeted recheck: `aec` (Antiochene Exegetical Christianity, Chrysostom-centered): Step 0, Doc_01, Doc_02 + Source Registry, records/worlds/aec.yaml

Per the `cic-build-cycle` skill, Round 3 is the final round available under the 3-round cap on substantial revision. Run by an independent Opus subagent (agent id `a94b5afa5c27e4427`, 2026-09-25), checking the Round 2 findings and the Round 2 fix commit (`7dfc5b93`) against the vendored XML and text files, the corpus-map on this branch, `Build/worlds/lpc/`, and the Source Registry Template. Read-only; the agent edited no files.

**Bottom line, in the reviewer's own words: "this round did not clear."** Several Round 2 fixes were claimed but not applied, or applied only in part. Two Round 2 fixes introduced new factual errors. A fresh pass also found a few substantive items Rounds 1 and 2 missed. Most of the residue is mechanical — bringing stale text into line with positions the documents already hold — but at least six findings are substantial under the skill's own definition (a document's scope boundary, sourcing/independence conclusion, dating confidence, or a confidence rating).

**What held up (verified at source this round):** the magister militum quote (now complete, `npnf109` `iii.ii-p9`); the Flavian prolegomena quote (`iii.vi-p2`); the Eutropius quote (`xv.iii-p5`); the Romans 12:20 locus; the Matthew Homily II opening (`iii.v-p2`–`p3`); the canon XIII quote (`npnf214`); the Palladius Olympias quotes and descent (Ch. LVI); the Palladius Sabaniana clause (correctly placed in Ch. XLI, "Holy Women"); the Socrates VI.3 Libanius/Andragathius quote and the corrected fellow-students direction; the Evagrius/Paulinus/three-years account; the `lpc` Doc_04 characterization (eleven rounds, never cleared, Approved to proceed on the project lead's direct instruction, Rounds 5–11 left open); Candidate 4 correctly "Preaching and Catechesis," tested in `lpc` Doc_04 §3, classified in §4; the 2026-09-14 ruling concerning Candidate 5 (Conciliar Authority); the `lpc` Doc_01 §7 quote; the Registry row splits (6/6a, 8/8a, Theodoret's per-work `assigned`/`provisional` split) all matching the corpus-map exactly; and `records/worlds/aec.yaml`'s header removal (YAML valid and complete). **`records/worlds/aec.yaml`: CLEARED.**

---

## Step 0: SUBSTANTIAL REVISION REQUIRED

**M1 (MEDIUM), §3 B3.** Round 2's softening of "Passes B3" was not actually applied — the document still asserted "Passes B3, on the specific ground the Step 0 Conclusion required" two paragraphs after its own hedged framing, a self-contradiction on its own central deliverable.

**M2 (MEDIUM, substantive, new), §2 A5 (and Doc_02 §4).** The *Adversus Judaeos* dating was overstated: the `npnf109` apparatus (`xix.ii-p12`) dates only one homily to September 386 and itself discusses a Paschal-table dating difficulty; Socrates VI.3 (`ii.ix.iv-p2`) separately states Chrysostom composed a book "Against the Jews" while still a reader, i.e. before 386. The claim that "only the editorial apparatus... is present" also missed this vendored mention.

**M3 (MEDIUM, substantive, new), §3 B3.** The Meletian-schism engagement left out its sacramental-validity dimension: Socrates II.44 (`ii.v.xliv-p3`) states the homoousian party refused communion with Meletius's own adherents specifically because of the validity of his own ordination and their own baptism at Arian hands — the ground of `lpc`'s own Candidate 6 (Sacramental/Ordination Validity), not only Candidate 3 (Collegial Communion).

**L1 (LOW, factual error), §1.** "The window opens roughly a generation before John Chrysostom's own birth (c. 349)" is arithmetically false against the window's own 350 start; flagged already at Round 1 and never fixed.

**L2 (LOW), §1.** Ephesus is discussed in A1, mislabeled as A5.

**L3 (LOW), §3.** A quote from `lpc` Doc_04's own Disposition ("It does not assert…") drops its own opening clause ("It is not Frozen, and…"); Candidate 4 described only as "in §4" when it is tested in §3 and classified in §4.

**L4 (LOW, audit trail), §2 A1.** The canon XIII re-transcription was credited to "Round 2 review," but no such finding exists in `Round2_Library_Stage_Review.md`.

## Doc_01: SUBSTANTIAL REVISION REQUIRED

**H1 (HIGH).** Round 2's claimed fix to the §4/§7 self-contradiction was not actually propagated: §4's own "Governing consequence" paragraph, §7 items 2 and 6, and §5's Cell 3B all still deferred the Theodoret strand/inclusion question to Doc_04 after §4 itself declared it closed. The same stale deferral was carried into Doc_02 §7 and §9.

**H2 (HIGH, substantive, new error in the Round 2 fix), §4.** The "one consistent criterion" rested on a false premise for the Letters: they are not uniformly 440s Eutychian-controversy material. The vendored `npnf203` Letters volume (div2 3.10) carries a run of documents from the Nestorian controversy of 430–431 (John of Antioch's own letter to Nestorius, Theodoret's own letters to Nestorius and from Ephesus, the Commissioners of the East's own reports from Chalcedon) — the same subject and date bracket as the Counter-statements, not the 440s material the corpus-map's own note otherwise describes.

**M1 (MEDIUM, substantive, new), §5.** "A jurisdictional and personal dispute, not a doctrinal one" is unsourced and, on Socrates II.44's own text, inaccurate — the split turned specifically on the validity of ordination and baptism, not personality or jurisdiction.

**M2 (MEDIUM), §2.** "The third city… by standard reckoning" was left unqualified, contradicting Step 0's own corrected wording.

**M3 (MEDIUM, citation), §2.** The fellow-students/Diodorus sentence was cited to `ii.ix.iv-p6` (the NPNF endnote) rather than `ii.ix.iv-p2` (Socrates' own body text).

**L1 (LOW).** Diodore stated as Chrysostom's own teacher as settled fact, against §2's own Widely-Accepted/not-independently-verified framing; §6's "consensus… taken for granted" sits badly with §5's own anti-Anomoean correction; the Counter-statements' edge-case status attributed to "subject-matter grounds too" when the subject-matter test itself is passed — the edge case comes from the condemnation and the composition date; the Template's Boundary Check quote joined two separate sentences with an ellipsis and altered the second's own wording.

## Doc_02 + Source Registry: SUBSTANTIAL REVISION REQUIRED

**M1 (MEDIUM, citation).** The corrected Socrates quote ("he limited his attention to the literal sense of scripture…") was cited to `ii.ix.iv-p6` (the endnote) rather than `ii.ix.iv-p2` (Socrates' own body text) — the same locus error as Doc_01 M3, carried into the Round 2 review artifact as well.

**M2 (MEDIUM, substantive, new error from the Round 2 fix), §6.** Olympias was said to be "independently attested, from outside Chrysostom's own circle" by Palladius. This is false: the vendored *Lausiac History* itself states Palladius was "embroiled in the disturbance connected with the blessed John" and traveled to Rome "because of the blessed bishop John" — he is a partisan in the same controversy, not an outside witness. Corroboration by a second author within Chrysostom's own circle, not independent attestation.

**M3 (MEDIUM), §1/§8.** The Round 2 fix to match Doc_01's per-work Theodoret finding was not updated for Doc_01 H2's own Letters split, and still used a date-based ("out-of-boundary by date") rather than subject-based framing in places.

**M4 (MEDIUM, fresh — missed by Rounds 1 and 2).** The Ammianus corpus-map row this branch had been citing since Round 1 as "already carried" did not actually exist on `library-stage/antiochene-exegetical-christianity` — the corpus-map file on this branch held 46 rows, not 47. The row was added, on a different branch (`library-stage/roman-church-gregorian`), by commit `4e1ff183`, not an ancestor of this branch's HEAD. Every "47 rows (corrected from 46)" and "already carried" claim across Step 0, Doc_01, Doc_02, and the Registry was therefore false on this branch as drafted. Per the skill's own rule on logging disagreements between reviews, this also means Round 1's M2 ("47, not 46") did not describe what was actually on this branch at the time.

**M5 (MEDIUM, substantive), Registry row 11a.** Confidence rated D ("tradition/genre-level attribution, no specific text/author named" per the Template) for a specifically named and located work (the Counter-statements, div2 3.6–3.7) — a misuse of the Citation Reliability scale to signal "edge case" rather than what it actually measures. The same conflation understated rows 6a and 8a at C when both are specifically located (B).

**M6 (MEDIUM), Registry row 11b.** The Comparandum Note's "do not read their prior provisional carriage" was wrong — the corpus-map carries the *Eranistes* and Letters at `assigned`, not `provisional`, reintroducing the error Round 1 M5 had already found and fixed elsewhere.

**L1 (LOW), §6.** "The same chapter's own immediate context" for the Sabaniana clause was wrong — it is a separate chapter (XLI, "Holy Women"), fifteen chapters before the Olympias chapter (LVI).

**L2 (LOW), Registry.** Row 11a's canon XIII verification was cited to "Doc_01 §4" when the verification is in Step 0 §2 A1; row 11b's "boundary… deliberately drawn to close (430) before the Eutychian controversy" repeated the same "drawn to avoid" framing Step 0 had already withdrawn for the Nestorian controversy.

**L3 (LOW), Registry.** The Living-document protocol paragraph did not include rows 14–18, which are also Confidence B/C or lower.

**L3 (LOW, audit trail).** Rows 1, 6a, 8a, 11, and 14 credited their own changes to "Round 2 review" findings that do not appear in `Round2_Library_Stage_Review.md` — the row splits actually answer Round 1 M2/M5, not a distinct Round 2 finding.

**Required before any disposition, all documents (not itself a substantive finding).** CLAUDE.md's "Keep the live/canonical surfaces clean" rule applies to `worlds/`. All four documents carry heavy inline correction narration ("corrected this revision (Round N review, … finding)"), the same pattern `lpc` Round 11 treated as a record-state finding requiring the history to move to a companion `Superseded_Claims.md` file, with the live document stating only current claims. Not yet done for `aec` as of this round.

---

## Severity summary and disposition under the 3-round cap

**Mechanical or alignment only** (bring stale text into line with positions the documents already hold; change no claim's substance): Step 0 M1, L1–L4; Doc_01 H1, M2, M3, L1; Doc_02 + Registry M1, M3, M6, L1–L3; the narration cleanup.

**Genuinely substantial** (new substance or a corrected fact, confidence rating, sourcing conclusion, or scope boundary): Doc_01 H2 (the Letters' own subject and boundary); Doc_02 M2 (Palladius's own independence mischaracterized); Step 0 M2 (*Adversus Judaeos* dating; a missed Socrates attestation); Step 0 M3/Doc_01 M1 (the Meletian schism's own ordination/baptism-validity ground); Doc_02 M4 (the Ammianus corpus-map row was not actually on this branch); Registry M5 (a Confidence rating misapplied).

Each finding is narrow and precisely located; none touches Chrysostom's own core evidence, the headline quotations, or the B3 hypothesis as a whole — but each is actually wrong or unsupported, not a "could be stronger" observation. This round does not clear.

**Disposition.** Per the `cic-build-cycle` skill, a fourth review round is not available. This is an unresolved tension for the project lead, not a self-disposed clearance. The mechanical/alignment findings and the six substantial findings above were applied directly in this revision (disclosed as a post-cap correction, not a self-certified clearance, matching the treatment already given to `roman-church-gregorian`'s own Doc_02/Source Registry under the same rule). The narration-cleanup requirement was not attempted in the same pass, given its own scope, and is named as required follow-up work, separate from and in addition to the substantive findings.
