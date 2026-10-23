Cap-ruling recheck, pahc force descriptions, 2026-10-13, ordered by the project lead at the review cap; independent Opus reviewer

Verdict: PASS (0 BLOCKING, 6 NON-BLOCKING)

Scope: the `description` field only of `records/pahc/force/pahc.force.apostolic-testimony-inheritance.md` and `records/pahc/force/pahc.force.contemporary-rival-movements.md`. Old text is `origin/main`; new text is the file at HEAD (5a49a91; the working tree is clean for `records/pahc`). The standard: the rewrite may only fix the checked factual errors (Trallians 2, Magnesians 13, Eusebius HE V.16.10, removal of "this build" and "Strand A members") and pass the readability gate. It must keep every hedge, confidence qualifier, limit and attribution, and add no claim beyond the cited sources.

How the text was checked:
- **Sentence by sentence.** Each old clause was matched to its new form.
- **Sources, by grep in the vendored files.** `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml`: 1 Clement 42 (l.1849, "Christ therefore was sent forth by God, and the apostles by Christ"); 1 Clement 44 (l.1942-1944, "ye have removed some men of excellent behaviour from the ministry"); Magnesians 13 (l.6174-6180, "Be ye subject to the bishop ... as ... the apostles to Christ"); Trallians 2 (l.6314, "be subject to the presbytery, as to the apostle of Jesus Christ"). Also `Build/worlds/pahc/CiC_W1_Doc01_World_Identification_FINAL.md` l.86-88 and `Build/worlds/pahc/CiC_W1_Doc08_Forces_Document.md` l.127, the approved upstream text of Force 2A-2.
- **YAML.** Both front matters parse with `yaml.safe_load`.
- **Readability.** `engine.m1.gates.grade_text`: apostolic-testimony-inheritance FK 7.66 / FRE 60.11; contemporary-rival-movements FK 7.12 / FRE 60.33. Both pass FK <= 10 and FRE >= 60.
- **Live surface.** `tools/check_live_commentary.py --surface records` flags neither file. "this build" and "Strand A" no longer appear in either description.

## Round-3 blocking items

1. 1 Clement rebukes the Corinthians, not the presbyters. **Fixed.** New: "1 Clement uses an explicit chain to rebuke the Corinthians who put out their presbyters." This matches anf01 l.1942-1944.
2. "legitimate" kept, not "right". **Fixed.** "legitimate teaching and practice" and "the test of what was legitimate" are both restored.
3. "temporal" scope kept. **Fixed.** "This world's defining assumption about time stands on it."
4. "mature concern", not "settled". **Fixed.** "By 177 CE it was already a mature concern."
5. "precarity" not strengthened to "threat". **Fixed.** "the state's legal risk". This is the round-3 suggested wording. "Risk" keeps the sense of an insecure position, not an active act by the state.
6. "one-bishop" label replaced. **Fixed.** "members in Antioch and Asia Minor above all". The text no longer states as fact that these churches had one bishop, which Doc_01 l.88 holds contested.

Round-3 non-blocking item 10 (the lesson standing as a bare sentence) is also fixed: "In that reading, holding any boundary ...".

## Findings

1. **apostolic-testimony-inheritance: "sent" in 1 Clement 42 (carried from round 3, item 7).**
   - Old: `Christ from God, the apostles from Christ`
   - New: `Christ came from God. The apostles came from Christ.`
   - Source: anf01 l.1849, "Christ therefore was sent forth by God, and the apostles by Christ."
   - NON-BLOCKING. "Came from God" can read as a claim about Christ's origin, not his sending. The old text was elliptical, so this is not a new error.

2. **apostolic-testimony-inheritance: "exactly" dropped (carried from round 3, item 8).**
   - Old: `argued over exactly what standing on it required`
   - New: `Churches still argued over what standing on it required.`
   - NON-BLOCKING. The old text limited the dispute to the details. Restoring "exactly" drops FRE to 59.64, which fails the gate, so this is a real trade-off and not an oversight.

3. **apostolic-testimony-inheritance: causal strength (carried from round 3, item 9).**
   - Old: `its fading would not have generated the urgency behind authority consolidation`
   - New: `That is why its fading drove the push to gather authority.`
   - NON-BLOCKING. The old text said the fading gave urgency to consolidation. The new text makes it drive the push itself, a slightly stronger causal claim. It also no longer echoes the gravity's own name ("authority consolidation").

4. **contemporary-rival-movements: "specifically" became "above all".**
   - Old: `a single formative lesson for Strand A members specifically`
   - New: `The lesson is for members in Antioch and Asia Minor above all.`
   - Source: Doc_08 l.127 has "for Strand A members specifically" and calls G05 "Strand A only".
   - NON-BLOCKING. "Above all" can imply that the lesson also applies elsewhere, but less. "Specifically" reads as "in particular", so the gap is small. "Asia Minor specifically" drops FRE to 59.24, which fails the gate.

5. **contemporary-rival-movements: "since" link dropped.**
   - Old: `disclosed as this build's own interpretive extension, since the gravity-level Interaction Matrix records no demonstrated relationship`
   - New: `This reading is disclosed as an interpretive extension. The gravity-level Interaction Matrix records no shown link ...`
   - NON-BLOCKING. The reason is now implied by the adjacent sentences, not stated. The caveat and the Matrix limit are both kept. As round 3 noted (item 11), no one now owns the reading. That follows from removing the process phrase.

6. **contemporary-rival-movements: Ignatius and the later rivals (already in the old text, not introduced by this rewrite).**
   - Old and new both say Ignatius's anti-docetic argument exists "because these rivals existed and pressed close". "These rivals" are Marcion (c. 144), Valentinus (Rome c. 136) and Montanism (c. 157-172). On the dating that Doc_01 follows (c. 107-115), Ignatius wrote before all three.
   - Source: the sentence is carried verbatim from the approved Doc_08 l.127. Doc_08 l.258 widens it to "proto-docetic teaching".
   - NON-BLOCKING and out of scope here. The rewrite did not change the claim. It belongs upstream, in Doc_08 and the world's `Open_Gaps_Tracking.md`, not in this description.

## Other checks (no finding)

- **Trallians 2.** "be subject to the presbytery 'as to the apostle of Jesus Christ'" matches anf01 l.6314 word for word. The old misreading (submission "owed to the apostle Jesus Christ himself") is corrected.
- **Magnesians 13.** "subject to the bishop as the apostles were subject to Christ" is a fair short form of anf01 l.6174-6180. It leaves out "and to one another" and "and to the Father, and to the Spirit", but adds nothing.
- **Hedges kept in apostolic-testimony-inheritance:** "inherited ... did not invent"; "not against a closed canon"; the 70 CE floor; "not one tradition among several to adapt freely"; "Churches still argued"; "not a neutral fact"; "not mainly an urgency about the world ending soon" ("primarily" became "mainly").
- **Hedges kept in contemporary-rival-movements:** "traditional break ... usually dated c. 144" ("conventionally" became "usually"); Moll's reading as "suggests ... may"; "c." on every date; "That split is on record"; "Archaeology backs up"; "disputed, between c. 157 and c. 172"; "not ... already defeated"; "Sometimes they drew"; "not ... a boundary already secured"; "is read together with", "are read as pointing to", "In that reading"; "disclosed as an interpretive extension"; the Interaction Matrix limit.
- **Small word changes checked as neutral:** "community" became "church"; "contemporary" became "living at the same time"; "actively argued" became "argued"; "at all" was dropped twice; "demonstrated" became "shown". None adds or removes a claim.
- **The Eusebius HE V.16.10 fix** is in `manifestations[2]`, outside this scope. The description makes no claim about the synods.
