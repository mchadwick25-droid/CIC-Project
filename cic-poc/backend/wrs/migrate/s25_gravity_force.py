"""S2.5 - Desert gravity + force records incl. Layer 4 (blueprint S2.5).

Gravities: Doc_04's ten candidates as records - six-test verdicts as fields
(test_1..test_6 keyed to Doc_04's own test names Repetition / Dependency /
Formation / Explanatory / Persistence / Interaction, carried inside each
verdict string; renaming the schema keys to the real names is an S2.9 CO
candidate, anticipated at S1.5 review), classification per Doc_04 SS6
(Primary: 1,2,3,4,5,7; Supporting: 6,9; Tensional: 8,10 - NO not-advanced
candidates exist in this world: all ten were tested and classified),
confidence_crosscheck per SS3, and a reciprocity-complete interaction[] set
from SS2's Interaction column + SS6 (mirrors added for symmetric types are
marked "(mirror)" in their notes).

Forces: Doc_08's twelve entries (1A-i, 1B-i/ii/iii, 2A-i/ii, 2B-i/ii,
3A-i/ii, 3B-i/ii), three layers condensed-verbatim with citations, plus
the NEW Layer 4 (Pass 1 SS3.5: elaboration or explicit stasis - Archer's
cycle as documentation shape only). Layer 4 is this step's scholarship;
stasis: true is used as a real answer where the world's own record shows
persistence-without-change (2A-i, 2A-ii, 2B-i, 3A-ii) - checked as
considered, not defaulted.

connections[] carries FORCE<->FORCE cross-cell links only (each mirrored so
the linkage-reciprocity gate holds); force->gravity tracing lives verbatim
in layer_formation_impact per Doc_08's own text - a gravity record cannot
carry a typed back-edge to a force (interaction[] is enum-typed
gravity-to-gravity), so putting the trace in connections[] would either
break reciprocity or bend the enum. The Forces-and-Gravities synthesis
table remains renderable as a view from the Layer-3 texts (S3.9 discipline).

Also updates world_core.gravities -> all ten gravity ids (closing the
staged completion violation ledgered since S2.3).
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(HERE))

import yaml
from source_rows_from_doc02 import emit_record

OUT = BACKEND / "wrs" / "records" / "desert_world"

COMMON_G = {"world_id": "desert-monasticism", "record_type": "gravity",
            "schema_version": 1, "jobs": [5], "register": "etic",
            "review_state": "draft",
            "sources": [{"source_id": "srcDES001"}, {"source_id": "srcDES002"},
                         {"source_id": "srcDES005"}]}

def T(rep, dep, form, expl, pers, inter):
    return {"test_1": {"verdict": rep, "note": "Repetition"},
            "test_2": {"verdict": dep, "note": "Dependency"},
            "test_3": {"verdict": form, "note": "Formation"},
            "test_4": {"verdict": expl, "note": "Explanatory"},
            "test_5": {"verdict": pers, "note": "Persistence"},
            "test_6": {"verdict": inter, "note": "Interaction"}}

GRAVITIES = [
 dict(id="desertgrav001", name="Withdrawal (anachoresis)", classification="Primary",
      six_tests=T("Strong - every evidence stream (Doc_02 SS1.1-1.2, 1.5, 2.1-2.2, 5.1-5.2)",
                  "High - geography, strand differentiation, source scarcity all downstream",
                  "Direct - defines entry into this world",
                  "Strong - explains siting, three-strand divergence, thin liturgical-text record",
                  "Strong - attested across Lower and Upper Egypt, all three strands",
                  "Reinforces manual labor (4) and elder authority (3); in tension with candidate 8"),
      confidence_crosscheck="Rests on Documented/Widely Accepted confidence across multiple independent evidence types (Doc_04 SS3); the Rubenson/Antony-literacy tension qualifies how any single figure's formation is narrated, not this gravity's cross-strand attestation.",
      interaction=[
        {"type": "reinforcing", "target_id": "desertgrav004", "note": "Doc_04 SS2: withdrawal reinforces manual labor; mutual (labor sustains withdrawal)."},
        {"type": "reinforcing", "target_id": "desertgrav003", "note": "Doc_04 SS2: withdrawal reinforces elder authority (which mediates it)."},
        {"type": "competing", "target_id": "desertgrav008", "note": "Doc_04 SS2/SS6: withdrawal's rhetoric of separation vs. documented embeddedness."}]),
 dict(id="desertgrav002", name="Spiritual combat against demonic thoughts (general form)", classification="Primary",
      six_tests=T("Strong - Athanasius, Apophthegmata, Evagrius independently attest the theme",
                  "High - shapes teaching content and genre",
                  "Direct",
                  "Strong - explains the terse-saying genre as combat-technique",
                  "Strong - present in all three strands, most elaborated in C",
                  "Reinforces diakrisis (5) and elder authority (3); generates candidate 9 as its systematized form"),
      confidence_crosscheck="Widely Accepted (Doc_02 SS1.1, SS1.5) - clear per Doc_04 SS3.",
      interaction=[
        {"type": "reinforcing", "target_id": "desertgrav005", "note": "Doc_04 SS2: combat reinforces diakrisis (mutual: discernment governs the combat)."},
        {"type": "reinforcing", "target_id": "desertgrav003", "note": "Doc_04 SS2: combat reinforces elder authority (thoughts disclosed to the elder)."},
        {"type": "reshaping", "target_id": "desertgrav009", "note": "Doc_04 SS2: generates candidate 9 as its Strand-C systematized form ('extends candidate 2')."}]),
 dict(id="desertgrav003", name="Elder-mediated oral authority", classification="Primary",
      six_tests=T("Strong - the Apophthegmata's entire structure",
                  "High - teaching transmission and formation logic depend on it",
                  "Direct",
                  "Strong - explains absence of a general systematic treatise tradition outside Evagrius",
                  "Strong in A/C; present but structurally secondary in B",
                  "Reinforces diakrisis (5); stands in the candidate-10 tension against candidate 6's office structure"),
      confidence_crosscheck="Documented/Widely Accepted across independent evidence types (Doc_04 SS3); Rubenson qualification as for gravity 1.",
      interaction=[
        {"type": "reinforcing", "target_id": "desertgrav005", "note": "Doc_04 SS2: mutual - discernment is what an elder is recognized as possessing."},
        {"type": "reinforcing", "target_id": "desertgrav001", "note": "(mirror of gravity 1's stated reinforcement - Doc_04 SS2 row 1)."},
        {"type": "reinforcing", "target_id": "desertgrav002", "note": "(mirror of gravity 2's stated reinforcement - Doc_04 SS2 row 2)."},
        {"type": "competing", "target_id": "desertgrav010", "note": "Gravity 10 IS the named tension this pole participates in (Doc_04 SS2 row 10: 'its Interaction is with those two candidates specifically')."}]),
 dict(id="desertgrav004", name="Manual labor as ascetic discipline (cheironaxia)", classification="Primary",
      six_tests=T("Strong - textual AND papyrological AND archaeological",
                  "High - material sustainability, almsgiving, discipline against idleness",
                  "Direct - discipline itself, not merely economic necessity",
                  "Strong - explains candidate 8's economic-embeddedness evidence directly",
                  "Strong - cross-strand",
                  "Reinforces withdrawal (1) and candidate 8; some tension with a purely contemplative reading of candidate 9"),
      confidence_crosscheck="Documented/Widely Accepted, three converging evidence streams (Doc_04 SS3; Doc_02 SS9).",
      interaction=[
        {"type": "reinforcing", "target_id": "desertgrav001", "note": "Doc_04 SS2: labor sustains withdrawal (mutual)."},
        {"type": "reinforcing", "target_id": "desertgrav008", "note": "Doc_04 SS2: labor reinforces candidate 8 (it IS the embeddedness mechanism)."},
        {"type": "competing", "target_id": "desertgrav009", "note": "Doc_04 SS2: some tension with a purely contemplative reading of candidate 9."}]),
 dict(id="desertgrav005", name="Diakrisis (discernment as master virtue)", classification="Primary",
      six_tests=T("Strong - recurs across named elders regardless of settlement",
                  "High - moderates and governs how other disciplines are practiced",
                  "Direct",
                  "Strong - explains the situational, non-systematic character of most surviving teaching",
                  "Strong - cross-strand",
                  "Reinforces elder authority (3); moderates candidate 2/9's ascetic intensity against excess"),
      confidence_crosscheck="Documented/Widely Accepted (Doc_04 SS3). Note Doc_04's own correction: the 'mother of all virtues' Cassian attribution was removed at its Round 1 review - not carried here either.",
      interaction=[
        {"type": "reinforcing", "target_id": "desertgrav003", "note": "Doc_04 SS2: mutual with elder authority."},
        {"type": "reinforcing", "target_id": "desertgrav002", "note": "(mirror of gravity 2's stated reinforcement.)"},
        {"type": "reinforcing", "target_id": "desertgrav007", "note": "(mirror of gravity 7's stated reinforcement of diakrisis - Doc_04 SS2 row 7.)"},
        {"type": "reshaping", "target_id": "desertgrav002", "note": "Doc_04 SS2: moderates candidate 2's (and its systematized form 9's) ascetic intensity against excess - a governing relation distinct from the mutual reinforcement above."}]),
 dict(id="desertgrav006", name="Koinonia / communal rule", classification="Supporting",
      six_tests=T("Strong WITHIN the Pachomian corpus, not attested outside it",
                  "High FOR STRAND B - organizes its entire social structure",
                  "Direct, Strand-B-specific",
                  "Explains Strand B's institutional distinctiveness from A/C",
                  "FAILS cross-strand persistence - no equivalent in A or C",
                  "Stands in the candidate-10 tension against candidate 3's person-based authority model"),
      confidence_crosscheck="Confidence is NOT the limiting factor (Widely Accepted, Doc_02 SS1.2); Persistence is (Doc_04 SS3/SS5).",
      interaction=[
        {"type": "competing", "target_id": "desertgrav010", "note": "Gravity 10 IS the named tension this pole participates in (Doc_04 SS2 row 10)."}]),
 dict(id="desertgrav007", name="Practically applied, non-systematized scriptural engagement", classification="Primary",
      six_tests=T("Moderate-strong - Apophthegmata idiom + documented contrast with World #2",
                  "Moderate - feeds diakrisis and elder-teaching content",
                  "Direct",
                  "Strong - explains the applied hermeneutic and difference from World #2's exegetical logic",
                  "Cross-strand, though evidence thinner for Strand B",
                  "Reinforces diakrisis (5)"),
      confidence_crosscheck="Widely Accepted with the compiler-mediation caveat standing (Doc_04 SS3); flagged at Doc_04 SS6 (Finding NEW-3) as the SOFTEST of the six Primary classifications - Doc_05 should treat it as the one most likely to warrant revisiting. Carried here verbatim, not smoothed.",
      interaction=[
        {"type": "reinforcing", "target_id": "desertgrav005", "note": "Doc_04 SS2: reinforces diakrisis."}]),
 dict(id="desertgrav008", name="Ongoing economic and social embeddedness in village life", classification="Tensional",
      six_tests=T("Moderate - two evidence types of uneven confidence; a corrective reading against the dominant narrative",
                  "Moderate",
                  "Indirect - shapes practice more than professed ideal",
                  "Strong - explains a real documented gap between rhetoric and practiced reality",
                  "Cross-strand as a corrective pattern; direct evidence concentrated in Lower Egypt",
                  "Stands in genuine tension with candidate 1's own rhetoric - exactly what qualifies it as Tensional"),
      confidence_crosscheck="Doc_04 SS3 (corrected): Kellia alone is Documented; Nepheros is UNRATED in Doc_02 and Melitian-caveated; the generalizing claim stays Contested/Inferential. The weaker evidential picture REINFORCES the Tensional classification.",
      interaction=[
        {"type": "competing", "target_id": "desertgrav001", "note": "Doc_04 SS2/SS6: the standing tension with withdrawal's rhetoric (Goehring)."},
        {"type": "reinforcing", "target_id": "desertgrav004", "note": "(mirror of gravity 4's stated reinforcement - labor is the embeddedness mechanism.)"}]),
 dict(id="desertgrav009", name="Evagrian systematized interior psychology", classification="Supporting",
      six_tests=T("Concentrated in one author (flagged at generation)",
                  "High WITHIN its own systematic scope (praktike -> apatheia -> theoria)",
                  "Direct, but for a narrower population (Strand C, largely its educated participants)",
                  "Strong FOR STRAND C; does not explain A or B's own formation logic as directly",
                  "FAILS cross-strand persistence - no comparable systematization in A or B",
                  "Extends candidate 2 (genuine candidate-to-candidate relationship)"),
      confidence_crosscheck="Doc_04 SS3 (corrected per its Round 1 Finding 2): Widely Accepted confidence MEETS the Primary floor - what disqualifies is the Persistence-test failure, not confidence; single-author concentration is an Author-Gravity axis, distinct from evidential confidence, and the two are not conflated. Its later transmission history (399-400; 553) is Doc_08 material, not classification grounds (SS4 correction).",
      interaction=[
        {"type": "reshaping", "target_id": "desertgrav002", "note": "Extends/systematizes candidate 2 (back-direction of gravity 2's 'generates' edge)."},
        {"type": "competing", "target_id": "desertgrav004", "note": "(mirror of gravity 4's stated tension with a purely contemplative reading.)"}]),
 dict(id="desertgrav010", name="Person-based (elder) vs. office-based (Rule) authority", classification="Tensional",
      six_tests=T("Recurs specifically at the Strand A/C-B boundary",
                  "High where it applies - governs succession, discipline, community stability",
                  "Direct - markedly different participant experience",
                  "Strong - explains why Strand B required a written Rule at all",
                  "Persists, unresolved, across the whole c. 320s-c. 430 span",
                  "IS the named tension between candidates 3 and 6 - by construction its Interaction is with those two"),
      confidence_crosscheck="Widely Accepted for both constituent bodies of evidence (Doc_04 SS3); Tensional follows from its nature as an opposition between two other gravities - the Framework's own definition - not from evidential weakness. Generated and tested as a full candidate (Doc_04 Round 1 Finding 4), not asserted at classification.",
      interaction=[
        {"type": "competing", "target_id": "desertgrav003", "note": "The elder pole (Doc_04 SS2 row 10; symmetric)."},
        {"type": "competing", "target_id": "desertgrav006", "note": "The office pole (Doc_04 SS2 row 10; symmetric)."}]),
]

COMMON_F = {"world_id": "desert-monasticism", "record_type": "force",
            "schema_version": 1, "jobs": [1, 5], "register": "etic",
            "review_state": "draft",
            "sources": [{"source_id": "srcDES001"}, {"source_id": "srcDES002"},
                         {"source_id": "srcDES010"}]}

FORCES = [
 dict(id="desertforce1Ai", name="End of systematic persecution; martyrdom closed as a path (Force 1A-i)",
      six_cell_position="1A - Initiating / External",
      layer_historical_event="Diocletianic persecution (303-311/313) the last systematic one; Constantine's toleration (313) removed the conditions under which martyrdom was structurally available. Confidence: Documented (Doc_08 1A-i L1).",
      layer_worlds_own_experience="Not 'relief': the tradition frames withdrawal and interior combat in martyrdom's own idiom - the ascetic as new martyr contending against demons rather than magistrates ('white martyrdom' reading, carried under Reported-Experience Status; its missing anchor citation is Doc_01 SS11 item 7, still open - Doc_08 1A-i L2).",
      layer_formation_impact="The single most consequential force in the ecology: directly generates gravity 1 (withdrawal) as reinvented total offering and gravity 2 (combat) as reinvented total struggle; without it the founding problem does not exist (Doc_08 1A-i L3).",
      layer4={"elaboration": "The world's own conditions permanently reorganized around desert formation as the standing successor to martyrdom: total self-offering ceased to be an event the state supplied and became a discipline the world itself institutionalized - settlement geography, teaching genre, and authority patterns all reshaped downstream (S2.5 Layer-4 authoring from Doc_08 1A-i L3 + Doc_04 SS4)."},
      connections=[]),
 dict(id="desertforce1Bi", name="Pre-existing village-level ascetic culture (Force 1B-i)",
      six_cell_position="1B - Initiating / Internal",
      layer_historical_event="The Vita records Antony modeling himself on an older ascetic already practicing nearby. Confidence: Contested (incident-level Vita reliability; Doc_08 1B-i L1).",
      layer_worlds_own_experience="The tradition's own memory preserves an anonymous predecessor - the world understood its practice as intensification of an existing, humbler culture, not novel departure (Doc_08 1B-i L2).",
      layer_formation_impact="Qualifies gravity 1: withdrawal drawn from an inherited substrate; explains the thinness on named forerunners (Doc_08 1B-i L3).",
      layer4={"elaboration": "The substrate itself changed condition: from unnamed village practice to the visible base of a named, imitable movement - retrospectively significant only once Antony's career made it so (S2.5 authoring from Doc_08 1B-i L3)."},
      connections=[]),
 dict(id="desertforce1Bii", name="Inherited literal-address scriptural formation logic (Force 1B-ii)",
      six_cell_position="1B - Initiating / Internal",
      layer_historical_event="Antony's conversion centers on Matthew 19:21 heard as direct personal address. Confidence: Contested (same incident-level basis; Doc_08 1B-ii L1).",
      layer_worlds_own_experience="The single-verse-as-immediate-command mode recurs as a structural feature of the world's scriptural engagement generally - an inherited interpretive posture, not one man's idiosyncrasy (Doc_08 1B-ii L2).",
      layer_formation_impact="Directly generates gravity 7 (practical scriptural engagement - the flagged softest Primary; Doc_08 1B-ii L3).",
      layer4={"elaboration": "The inherited posture became the world's standing hermeneutic: scripture and lived practice fused into substantially one activity, and no systematic exegetical tradition formed where the posture made one unnecessary (S2.5 authoring from Doc_08 1B-ii L3 + Doc_05 SS8.6 as cited there)."},
      connections=[]),
 dict(id="desertforce1Biii", name="The formation-at-scale problem - Pachomius's cenobitic innovation (Force 1B-iii)",
      six_cell_position="1B - Initiating / Internal",
      layer_historical_event="Tabennesi founded c. 320: written Rule, common property, formal offices. Confidence: Widely Accepted (Doc_08 1B-iii L1).",
      layer_worlds_own_experience="An internally-felt problem: how does total formation extend beyond one extraordinary solitary to the many, without dilution; the Lives present the koinonia as continuous with the same total-commitment logic (Doc_08 1B-iii L2).",
      layer_formation_impact="Directly generates gravity 6 (koinonia). Cross-cell: this force is the ORIGIN of Cell 2B-i's ongoing authority tension - the office model coexists with and contests the elder model for the rest of the span (Doc_08 1B-iii L3).",
      layer4={"elaboration": "A second kind of authority came into being and stayed: after c. 320 the world permanently contains two coexisting models of legitimate spiritual authority - the changed condition gravity 10 names (S2.5 authoring from Doc_08 1B-iii L3)."},
      connections=[
        {"type": "origin-of", "target_id": "desertforce2Bi", "note": "Doc_08 1B-iii L3 / 2B-i L3 (Finding S1's own correction): the ongoing tension is this force's direct, traceable consequence."}]),
 dict(id="desertforce2Ai", name="Ongoing economic/administrative embeddedness (Force 2A-i)",
      six_cell_position="2A - Ongoing / External",
      layer_historical_event="Nepheros archive documents ordinary monastic business with the surrounding world; Kellia's commercial infrastructure corroborates. Confidence: Documented for Kellia; Nepheros UNRATED in Doc_02 and Melitian-caveated (Doc_08 2A-i L1).",
      layer_worlds_own_experience="The least confidently documentable Layer 2: the world's own literary self-presentation emphasizes total withdrawal and does not dwell on the entanglement the documents show. Named Tension carried at full strength (Goehring); built substantially from source-critical reasoning because direct from-within testimony does not exist - the world did not thematize this tension in its own preserved voice (Doc_08 2A-i L2, Finding C4's honest register).",
      layer_formation_impact="Generates gravity 4 (labor as concurrent discipline) and gravity 8 (embeddedness, Tensional - precisely because L2 is thin relative to L1/L3; Doc_08 2A-i L3).",
      layer4={"stasis": True, "elaboration": "Stasis, considered and meant: the tension between rhetoric and practiced economy persisted unchanged and unthematized across the whole span - the world's own self-understanding never absorbed what its documentary record shows; nothing in its own conditions reorganized in response (S2.5 authoring from Doc_08 2A-i L2/L3; Doc_04 SS4: 'holds steady rather than intensifying or fracturing')."},
      connections=[]),
 dict(id="desertforce2Aii", name="The Melitian schism as rival ascetic movement in the same space (Force 2A-ii)",
      six_cell_position="2A - Ongoing / External",
      layer_historical_event="Melitian ascetic communities documented in the same period and region, with their own archive and forms. Confidence: Documented for existence/contemporaneity; Inferential / Thin for organizational distinguishability in daily life (Doc_08 2A-ii L1).",
      layer_worlds_own_experience="The Nicene-communion sources are essentially silent about Melitians as a live rival - a silence read as potentially informative (Athanasius's role as the schism's chief adversary), per Doc_02 SS6's structural-absence reasoning (Doc_08 2A-ii L2).",
      layer_formation_impact="Formation impact NOT confidently traceable beyond gravity 8's evidential complications; the fourth-pattern question remains a genuine limit, named rather than papered over (Doc_08 2A-ii L3).",
      layer4={"stasis": True, "elaboration": "Stasis: no documented condition change within the window - the rival presence persisted, the literary silence persisted, and whether the two practices even differed organizationally remains the open item (S2.5 authoring from Doc_08 2A-ii; the silence itself is the enduring condition)."},
      connections=[]),
 dict(id="desertforce2Bi", name="The unresolved person-vs-office authority tension (Force 2B-i)",
      six_cell_position="2B - Ongoing / Internal (Transmission dimension)",
      layer_historical_event="Rule-and-offices coexist historically with the Apophthegmata's elder-disciple structure, same decades and region. Confidence: Widely Accepted (Doc_08 2B-i L1).",
      layer_worlds_own_experience="Lived as two genuinely different registers of submitting to legitimate authority - personal obedience to a specific elder vs. obedience to an office regardless of holder; even Pachomius is remembered in elder-vocabulary - two only-partially-reconciled registers, not opposed doctrines (Doc_08 2B-i L2).",
      layer_formation_impact="Gravity 10 in its full forces form. Cross-cell: the ongoing expression of Force 1B-iii, so the central ongoing internal tension is a direct consequence of the world's own initiating forces (Doc_08 2B-i L3).",
      layer4={"stasis": True, "elaboration": "Stasis as the load-bearing finding: the tension never resolved and - decisively - never produced an internal adjudication mechanism. That ABSENCE of elaboration is itself the structural vulnerability Doc_08's closing synthesis identifies: no internal body existed that could have contained the Origenist dispute before external authority acted (S2.5 authoring from Doc_08 2B-i L2 + 3B-i L3)."},
      connections=[
        {"type": "originates-from", "target_id": "desertforce1Biii", "note": "(mirror of 1B-iii's origin-of edge; Doc_08 Finding S1 correction.)"},
        {"type": "read-for-closing-as", "target_id": "desertforce3Bi", "note": "Same historical substrate, read at 3B-i for its bearing on the world's closing (Doc_08 3B-i L1)."}]),
 dict(id="desertforce2Bii", name="Strand C's intellectual intensification culminating in Evagrius (Force 2B-ii)",
      six_cell_position="2B - Ongoing / Internal (Transmission dimension)",
      layer_historical_event="Evagrius, uniquely educated relative to the world's norm, produced the praktike->apatheia->theoria scheme and eight-fold logismoi taxonomy at Kellia. Confidence: Widely Accepted (Doc_08 2B-ii L1).",
      layer_worlds_own_experience="Within Strand C the systematization functioned as intensification of an already-present diagnostic practice, organizing rather than replacing existing vocabulary (Doc_08 2B-ii L2).",
      layer_formation_impact="Generates gravity 9 (Supporting, strand-bound). Transmission Specificity: single author, Kellia-concentrated, Greek-literate sub-population - a selection effect named explicitly; the narrowness that made it formative also made it structurally narrow in the way Cell 3A shows consequential (Doc_08 2B-ii L3).",
      layer4={"elaboration": "Strand C's conditions changed: where diagnostic practice had been informal, a systematized curriculum now existed - and with it a legible, isolable intellectual sub-population, the changed condition 3A-i's external action would later exploit (S2.5 authoring from Doc_08 2B-ii L3 + 3A-i L3)."},
      connections=[
        {"type": "narrowness-exploited-by", "target_id": "desertforce3Ai", "note": "Doc_08 3A-i L3: the external force's severity is directly explained by this force's own internal finding - 'the clearest cross-cell case in this document' (SS2 synthesis)."},
        {"type": "transmission-sequel-in", "target_id": "desertforce3Bii", "note": "Doc_08 3B-ii L3: Evagrius's post-553 pseudonymous survival named there as the furthest downstream instance of the same transmission-vulnerability pattern."}]),
 dict(id="desertforce3Ai", name="Episcopal/conciliar intervention in the First Origenist Controversy, 399-400 (Force 3A-i)",
      six_cell_position="3A - Ending/Transforming / External",
      layer_historical_event="Theophilus's 399 Festal Letter, the 400 Alexandria synod condemning Origen and his monastic followers, and the Tall Brothers' expulsion. Confidence: Documented for the synod and expulsion; Contested for Theophilus's motives (Named Tension carried; Doc_08 3A-i L1).",
      layer_worlds_own_experience="No first-person account of the rupture survives; Evagrius died January 399, before it fully broke. Reported-Experience Status: the expulsion is well-documented as event; the interior experience of watching it is not attested and is not invented (Doc_08 3A-i L2).",
      layer_formation_impact="The historically decisive fracture for gravity 9. Cross-cell: severity explained by 2B-ii's narrowness - a broadly attested gravity could not have been excised by one conciliar action; the consequence the classification's own reasoning predicts, not 'decisive corroboration' of it (Doc_08 3A-i L3).",
      layer4={"elaboration": "After 400 the world's conditions no longer include a systematizing school: Strand C's intellectual leadership scattered, the Kellia Origenist circle dispersed, and gravity 9 lost its carrier population within the world's own span (S2.5 authoring from Doc_08 3A-i L1/L3)."},
      connections=[
        {"type": "exploits-narrowness-of", "target_id": "desertforce2Bii", "note": "(mirror; Doc_08 3A-i L3.)"},
        {"type": "conjunctural-with", "target_id": "desertforce3Bi", "note": "Doc_08 3B-i L3: proximate external trigger paired with the internal structural vulnerability - neither alone explains the outcome."}]),
 dict(id="desertforce3Aii", name="Longer imperial-ecclesiastical centralization trend (Force 3A-ii)",
      six_cell_position="3A - Ending/Transforming / External",
      layer_historical_event="The broader 4th-5th c. trajectory of conciliar/episcopal authority over monastic doctrine, continuing past c. 430 toward Chalcedon. Confidence: Widely Accepted as general trend; the specific chain to Shenoute's later model Inferential / Thin (Doc_08 3A-ii L1).",
      layer_worlds_own_experience="Not directly attested within the closing boundary; no Layer 2 account constructed for a pattern participants could not have recognized as completed (Doc_08 3A-ii L2).",
      layer_formation_impact="Context for Cell 3B's synthesis, not a directly traceable impact on any specific gravity within this evidence base (Doc_08 3A-ii L3).",
      layer4={"stasis": True, "elaboration": "Stasis within the world's own window: the trend acts past the boundary; no in-window condition change is traceable to it - recorded as context, exactly as Doc_08 scopes it (S2.5 authoring)."},
      connections=[
        {"type": "context-for", "target_id": "desertforce3Bi", "note": "Doc_08 3A-ii L3: named as context for 3B's internal-versus-external synthesis."}]),
 dict(id="desertforce3Bi", name="The authority tension as standing internal vulnerability at the close (Force 3B-i)",
      six_cell_position="3B - Ending/Transforming / Internal (Transmission dimension)",
      layer_historical_event="No single dateable event - the 2B-i substrate read for its bearing on the closing. Confidence: Widely Accepted (Doc_08 3B-i L1).",
      layer_worlds_own_experience="Never resolved within the span; no evidence of participants experiencing approaching crisis - ongoing unresolved coexistence, with no manufactured anticipation (Doc_08 3B-i L2).",
      layer_formation_impact="The conjunctural synthesis answering Doc_07 SS10's reserved question: internal structural vulnerability (no internal adjudication mechanism ever developed) combined with the external trigger that exploited it - neither alone sufficient; their interaction explains the outcome. Offered as the document's own reasoned synthesis, not attested fact (Doc_08 3B-i L3 + SS2).",
      layer4={"elaboration": "The terminal condition change: the world's distinct form closes conjuncturally - its never-elaborated authority structure (2B-i's stasis) met an external action it had no mechanism to contain, and the ecology's characteristic shape ended/transformed rather than adapting (S2.5 authoring from Doc_08 3B-i L3; flagged there for Validation-Layer testing as interpretation)."},
      connections=[
        {"type": "read-for-closing-as", "target_id": "desertforce2Bi", "note": "(mirror; same substrate, closing register.)"},
        {"type": "conjunctural-with", "target_id": "desertforce3Ai", "note": "(mirror; Doc_08 3B-i L3.)"},
        {"type": "context-from", "target_id": "desertforce3Aii", "note": "(mirror of 3A-ii's context-for edge.)"}]),
 dict(id="desertforce3Bii", name="Transmission shift: live elder word to compiled anthology (Force 3B-ii)",
      six_cell_position="3B - Ending/Transforming / Internal (Transmission dimension)",
      layer_historical_event="Apophthegmata compiled 5th-6th c., after the closing boundary, by anonymous editors; Palladius (c. 419-420) and Cassian (through the 420s, with the apatheia->puritas cordis substitution) already treat the material as completed teaching. Confidence: Documented for chronology; Inferential / Thin for the compilers' selection criteria (Doc_08 3B-ii L1).",
      layer_worlds_own_experience="Participants could not experience their own material's later compilation - a force acting on the legacy. From within: the apophthegma form's occasion-bound character meant the world's own teaching practice did not generate an archive; preservation depended on actors outside itself (Doc_08 3B-ii L2).",
      layer_formation_impact="Transmission Specificity in full: what (occasion-bound sayings, named attributions), by whom (anonymous post-boundary compilers), with what selection effects (the ammas' material thin - a compiler-context effect named without claiming certainty); the same non-institutional teaching logic that made the world distinctive made its preservation wholly external. The 553 Evagrius sequel is the furthest downstream instance, named as outside the c. 430 bound (Doc_08 3B-ii L3).",
      layer4={"elaboration": "The teaching's mode of existence changed at and past the boundary: from live, occasion-bound, elder-mediated word to written, general-purpose anthology mediated by unknown selectors - a legacy-condition change the world's own logic neither anticipated nor provided for (S2.5 authoring from Doc_08 3B-ii L2/L3)."},
      connections=[
        {"type": "transmission-sequel-of", "target_id": "desertforce2Bii", "note": "(mirror of 2B-ii's edge; the Evagrius pseudonymous-survival sequel.)"}]),
]


def main():
    for g in GRAVITIES:
        emit_record({**COMMON_G, **g},
                    "S2.5 gravity record (2026-07-27) from Doc_04 (six-test table SS2, "
                    "Cross-Check SS3, classification SS6 - all read in full). Test keys "
                    "test_1..test_6 = Repetition/Dependency/Formation/Explanatory/"
                    "Persistence/Interaction (S2.9 CO candidate to rename keys). No "
                    "not-advanced candidates exist for this world: all ten classified.",
                    OUT / "gravity" / f"{g['id']}.md")
    for f in FORCES:
        emit_record({**COMMON_F, **f},
                    "S2.5 force record (2026-07-27) from Doc_08 (three layers "
                    "condensed-verbatim with citations; Layer 4 is THIS step's new "
                    "authoring - elaboration or considered stasis). connections[] = "
                    "force<->force cross-cell links only, mirrored; force->gravity "
                    "tracing lives verbatim in layer_formation_impact (see script "
                    "docstring for why).",
                    OUT / "force" / f"{f['id']}.md")
    # world_core.gravities -> all ten (closes the staged completion violation)
    wc_path = OUT / "world_core" / "desertcore001.md"
    parts = wc_path.read_text(encoding="utf-8").split("\n---", 2)
    rec = yaml.safe_load(parts[0][3:])
    rec["gravities"] = [g["id"] for g in GRAVITIES]
    body = parts[2].strip() if len(parts) > 2 else ""
    body = body.replace("gravities[] deliberately empty until S2.5 authors the gravity records; ",
                         "gravities[] populated at S2.5 (all ten Doc_04 candidates); ")
    emit_record(rec, body, wc_path)
    print(f"wrote {len(GRAVITIES)} gravity + {len(FORCES)} force records; world_core.gravities populated")


if __name__ == "__main__":
    main()
