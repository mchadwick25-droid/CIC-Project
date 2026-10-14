Review round 3, pahc record audit fixes, 2026-10-13, reviewer: independent Opus subagent

Verdict: FAIL (6 BLOCKING, 6 NON-BLOCKING)

Scope: targeted recheck of the uncommitted working-tree diff against HEAD (`git diff -- records/pahc Build/worlds/pahc`): 7 files. The diff covers (1) the `description` of `pahc.force.apostolic-testimony-inheritance`, (2) the `description`, `manifestations[2]` and `sources` loci of `pahc.force.contemporary-rival-movements`, (3) the `work` fields of `pahc.source.tertullian-adversus-marcionem` and `pahc.source.anti-montanist-fragments`, (4) the loci of `pahc.quote.jesus-christ-our-god` and `pahc.quote.appointed-to-be-read`, and (5) the OG-27 and OG-28 text. The standard is the coordinating session's ruling for (1) and (2): a build record may be rewritten only when that is the only way to fix a checked factual error, keeping every hedge, confidence qualifier, limit and attribution, and adding no new claim. This is the third review on this pass, the cap set in CLAUDE.md ("Scaling the build").

How the edits were checked:
- **Sentence by sentence.** Each old description was set beside the new one, and every clause was matched.
- **YAML.** All 6 touched record files parse with `yaml.safe_load`.
- **Readability.** `engine.m1.gates.grade_text`: apostolic-testimony-inheritance FK 7.5 / FRE 61.1; contemporary-rival-movements FK 7.2 / FRE 60.0. Both pass, the second by 0.01.
- **Live surface.** `tools/check_live_commentary.py --surface records` flags none of the 6 files. "this build" and "Strand A" no longer appear in either force record.
- **Facts.** Each was checked by grep against the vendored files:
  - anf01: Ignatius, Trallians 2 (l.6314) and ch. VII (div at l.6505); Magnesians 13 (l.6174-6180); 1 Clement 42 (l.1849) and 44 (l.1942).
  - npnf201: Eusebius, Church History V.16.10 (l.29721-29724).
  - anf03: Tertullian, Adversus Marcionem I.19 (l.23716-23724).
  - npnf204: Athanasius, Festal Letter XXXIX §7 (l.68817).
  - Build/worlds/pahc/CiC_W1_Doc01_World_Identification_FINAL.md l.86-88, for what Strand A means.

## Findings

1. **pahc.force.apostolic-testimony-inheritance, description: who 1 Clement corrects.**
   - Old: `1 Clement grounds correction of Corinth's deposed presbyters in an explicit chain`
   - New: `1 Clement uses an explicit chain to correct Corinth's deposed presbyters.`
   - Source: anf01 l.1942 (1 Clem. 44): "we are of opinion that those appointed by them ... cannot be justly dismissed ... ye have removed some men of excellent behaviour from the ministry". Clement rebukes the Corinthians who deposed the presbyters. He does not correct the presbyters.
   - BLOCKING. The old wording was loose. The new wording names the wrong party, which is a new factual error.
   - Suggested fix: "1 Clement uses an explicit chain to rebuke the Corinthians who put out their presbyters."

2. **pahc.force.apostolic-testimony-inheritance, description: "legitimate" became "right".**
   - Old: `legitimate teaching and practice must trace to apostolic testimony` and `if apostolic testimony were not already the measure of legitimacy`
   - New: `right teaching and practice must trace back to what the apostles testified` and `The apostles' testimony was already the test of what was right.`
   - Problem: the force is about legitimacy, meaning whose teaching carries authority. That is what ties it to authority consolidation in the next sentence. "Right" makes it a claim about correctness. The central claim of the force changes in two places.
   - BLOCKING. The ruling allows no changed claim.
   - Suggested fix: "legitimate teaching and practice" and "already the test of what was legitimate".

3. **pahc.force.apostolic-testimony-inheritance, description: "temporal" dropped.**
   - Old: `It is the ground this world's own defining temporal assumption stands on`
   - New: `This world's defining assumption stands on it.`
   - Problem: the old text named the world's defining assumption about time. The new text calls it the world's defining assumption without qualification, which is a broader claim. The scoping qualifier is lost.
   - BLOCKING.
   - Suggested fix: "This world's defining assumption about time stands on it."

4. **pahc.force.contemporary-rival-movements, description: "mature" became "settled".**
   - Old: `already a mature concern by 177 CE`
   - New: `By 177 CE it was already a settled concern.`
   - Problem: "settled" reads as resolved or fixed. That contradicts the same field ("A member did not feel this as a boundary already secured") and the record's Contested dating. "Mature" meant well developed.
   - BLOCKING.
   - Suggested fix: "By 177 CE it was already a mature concern."

5. **pahc.force.contemporary-rival-movements, description: "precarity" became "threat".**
   - Old: `combined with state legal precarity`
   - New: `This pressure is read together with the state's legal threat.`
   - Problem: precarity is an insecure, at-risk legal position. "Threat" is a stronger, active claim about what the state did. The world's own documents use the term "state legal precarity" for this domain (CiC_W1_Representative_Engagement_Architecture.md l.31).
   - BLOCKING.
   - Suggested fix: "This pressure is read together with the state's legal risk." ("the state's legal precarity" keeps the term but drops FRE to 58.6.)

6. **pahc.force.contemporary-rival-movements, description: "Strand A members" became "the one-bishop churches".**
   - Old: `a single formative lesson for Strand A members specifically`
   - New: `The lesson is for the members of the one-bishop churches in particular.`
   - Source: Doc_01 l.88 defines Strand A as "Antioch/Asia Minor (episcopal-consolidating)". It says the monepiscopal push there was "genuinely contested or aspirational even within this strand, not simply a description of settled fact". l.86 calls the two-strand framing itself provisional.
   - Problem: "one-bishop churches" states as fact that these churches had a single bishop, which Doc_01 holds contested. Removing the process label is right, but the new label adds a claim.
   - BLOCKING.
   - Suggested fix: "The lesson is for members in Antioch and Asia Minor above all."

7. **pahc.force.apostolic-testimony-inheritance, description: "sent" in 1 Clement 42.**
   - New: `Christ came from God. The apostles came from Christ.`
   - Source: anf01 l.1849: "Christ therefore was sent forth by God, and the apostles by Christ."
   - Problem: the chain is one of sending. "Came from God" can read as a statement about Christ's origin. The old text ("Christ from God") was elliptical, so this is not a new error.
   - NON-BLOCKING. Suggested: "God sent Christ. Christ sent the apostles." Regrade if used.

8. **pahc.force.apostolic-testimony-inheritance, description: "exactly" dropped.**
   - Old: `argued over exactly what standing on it required`
   - New: `Churches still argued over what standing on it required.`
   - NON-BLOCKING. The old text limited the argument to the details. Restoring "exactly" costs little.

9. **pahc.force.apostolic-testimony-inheritance, description: "urgency behind" dropped.**
   - Old: `its fading would not have generated the urgency behind authority consolidation`
   - New: `That is why its fading drove the push to gather authority.`
   - NON-BLOCKING. The old text said the fading gave urgency to consolidation. The new text makes the fading drive the push itself, which is a slightly stronger causal claim. Suggested: "That is why its fading gave urgency to the push to gather authority." Regrade if used.

10. **pahc.force.contemporary-rival-movements, description: the lesson now stands as a bare sentence.**
    - New: `Holding any boundary, doctrinal or legal, was rehearsed as one unbroken kind of refusal.`
    - Problem: in the old text this clause sat inside "is read ... as converging on a single formative lesson ... that". It now stands alone as a statement of fact. The frame survives in the sentences before and after it ("are read as pointing to"; "This reading is disclosed as an interpretive extension"), so the hedge is still there.
    - NON-BLOCKING. Suggested: "In that reading, holding any boundary ...". Regrade if used, because the field has no FRE margin.

11. **pahc.force.contemporary-rival-movements, description: ownership of the extension.**
    - Old: `disclosed as this build's own interpretive extension`
    - New: `This reading is disclosed as an interpretive extension.`
    - NON-BLOCKING. The live-surface check requires the process phrase to go. The caveat that this is interpretation, not finding, is kept. Nobody now owns the reading, which is acceptable for a build record.

12. **Build/worlds/pahc/Open_Gaps_Tracking.md, OG-27.**
    - The entry for `apostolic-testimony-inheritance` says "All hedges and claims otherwise kept". Findings 1-3 show that is not yet true. The `contemporary-rival-movements` entry likewise does not record findings 4-6.
    - NON-BLOCKING in itself. Otherwise OG-27 and OG-28 match the diff exactly: the new OG-27 bullets, the citation-loci paragraph, the "Not changed" line, OG-28 items 1-2 rewritten, the old item 9 removed, and new items 9-10. The OG-27 text must be brought into line with whatever is finally committed.

## Verified correct (no finding)

- **Trallians 2.** anf01 l.6314: "be subject to the presbytery, as to the apostle of Jesus Christ". The new description and `manifestations[1]` match.
- **Magnesians 13.** anf01 l.6174-6180, short recension: "Be ye subject to the bishop, and to one another, as Jesus Christ to the Father, according to the flesh, and the apostles to Christ". The new sentence is a fair short form.
- **Eusebius V.16.10.** npnf201 l.29721-29724: "the faithful in Asia met often in many places throughout Asia to consider this matter, and examined the novel utterances and pronounced them profane, and rejected the heresy". It supports `manifestations[2]` ("examined and rejected by gatherings of the faithful across Asia"), the anti-Montanist `locus`, and the `work` field.
- **Tertullian, Adversus Marcionem I.19.** anf03 l.23718-23724: "a heretic of the Antonine period ... from Tiberius to Antoninus Pius, there are about 115 years and 6-1/2 months". No c. 144 date appears in the chapter. The `locus` and the `work` field are correct, and the Moll caveat is kept.
- **pahc.quote.jesus-christ-our-god.** The passage "Be on your guard, therefore, against such persons" is Trallians ch. VII (div v.iv.vii, anf01 l.6505). The `locus` and `speaker_or_author` are correct.
- **pahc.quote.appointed-to-be-read.** "7. But for greater exactness I add this also" is at npnf204 l.68817. The `locus` is correct.
- **Unchanged parts of contemporary-rival-movements.** Every other hedge in the description is kept: Moll's alternative, "disputed" for the Montanist start date, "on record" for the Valentinian split, and the Interaction Matrix limit. `sources[1].locus` changed quoting style only; its value is the same.

## Note on the cap

This is the third review on these records in this pass. Under CLAUDE.md, a document that does not clear review in three rounds is an unresolved tension and goes to Mark; it does not get a fourth round. The six blocking items are narrow word-level substitutions, and each has a tested fix:
- With fixes 1-3 applied, apostolic-testimony-inheritance grades FK 7.7 / FRE 60.1.
- With fixes 4-6 applied, contemporary-rival-movements grades FK 7.1 / FRE 60.2.

Whether to apply them under a cap ruling, or to revert both descriptions and leave the errors registered in OG-28, is Mark's decision.
