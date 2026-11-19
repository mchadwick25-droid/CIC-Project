"""S2y: Donatism (don) canon_cells tagging pass -- the coverage-mapping step
named as upcoming in wb_don_s2x_doctrinal_witness.py's own docstring, run
separately from that step because it is a genuinely different unit of work
(a coverage READ over all 142 already-built don records, not new authoring).

GOVERNING PRINCIPLE (Build/Ministry/Technology/CiC_Record_Native_World_Build_
Process_V1_3.md, quoted directly in this step's own launch brief): "Every
substantive cell offers its stories and terms. When a cell's records are
authored, the coverage read asks: does a story genuinely belong here? a
term? If yes, its canon_cells says so... lean, one story and one term per
cell where they genuinely belong, never everything that could fit. If
nothing genuinely belongs, that finding is recorded and the cell stays
empty there -- an honest empty is a legitimate outcome, forced fill is
not." This script is a coverage READ against that bar, not a fill-every-
cell exercise -- ten of the fleet's 28 cells end this script still empty,
named explicitly below, because nothing in this world's own corpus
genuinely answers what those cells ask.

SCHEMA/GATE GROUND, VERIFIED DIRECTLY THIS SESSION (not assumed from any
prior script's summary):
  - canon_cells lives on ENVELOPE_PROPERTIES (engine/m1/schemas.py):
    {"type": "array", "items": {"type": "string"}} -- every record type
    carries it, additionalProperties:false does not touch it.
  - gate_referential (engine/m1/gates.py) checks every canon_cells entry
    resolves to `canon.valid_cells(fleet)` -- a typo'd or invented cell code
    is a hard finding, not silently ignored.
  - gate_canon_coverage (engine/m1/gates.py) calls canon.classify_cell()
    once per cell. classify_cell() (engine/m1/canon.py) counts as
    "substantive" ONLY record_type in {"doctrinal_witness", "term",
    "story", "quote"} (canon.substantive_types(), confirmed by direct read).
    gravity, force, contested_claim, demonstration, and figure canon_cells
    tags do NOT close a cell for this gate -- they are tagged in this script
    anyway, for the same reason retrieval_hint_keywords()/entity_cells()
    exist: they feed M4's Stage A keyword/entity routing and M2's compiled
    canon-map.json cache at build time, even though they carry no coverage-
    gate weight. This distinction is real and is why this script's own
    per-cell disposition table below separately states "substantive" status
    (term/story/quote/doctrinal_witness) from "also tagged, non-gate-
    counted" (gravity/force/contested_claim/figure).
  - classify_cell() status is "substantive" (>=1 substantive record),
    "honest_limit" (exactly one honest_limit, zero substantive),
    "multiple_honest_limit" (a gate defect), or "empty" (neither).

STARTING STATE, CONFIRMED DIRECTLY THIS SESSION:
  - 28 valid cells confirmed directly against records/_fleet/canon_question/
    *.md (93 files): C-E, C-I, C-P, C-T, and F1-E/I/P/T through F6-E/I/P/T
    (6 F-dimensions x 4 registers = 24, plus the 4 C- cells = 28).
  - 9 cells already closed by the prior step's 3 doctrinal_witness + 6
    honest_limit records (records/don/doctrinal_witness/, records/don/
    honest_limit/ -- read in full this session, NOT touched by this
    script, per this step's own constraint): F1-E (don.witness.refusal-
    and-recourse), F1-P (don.limit.doubt-and-reception), F2-I (don.limit.
    theology-beyond-tyconius), F3-I (don.witness.one-formation-aim), F3-P
    (don.limit.bagai-violence-no-account), F3-T (don.witness.boundary-is-
    doctrine), F5-E (don.limit.basilica-archaeology), F5-I (don.limit.
    ordinary-interior-life), F6-P (don.limit.womens-own-voice).
  - Every other don record (records/don/term/, story/, quote/, gravity/,
    force/, contested_claim/, figure/ -- 75 records across those 7 types)
    carried canon_cells: [] before this script ran -- confirmed by grep.
    (source/search_record/world_core/voice_craft/demonstration/ambient are
    out of this script's scope per its own launch brief: source/search_
    record/world_core are not coverage-relevant; voice_craft/demonstration
    are not canon.substantive_types() members either and the prior step
    already found them not coverage-counted.)

CROSS-CHECK AGAINST DEMONSTRATION canon_question_id (a live, independent
confirmation signal, not this script's own invention): don.demo.baptism-
threshold cites _fleet.canon.f4-i-01 ("How did a person actually become one
of you?") -- directly confirming this script's own F4-I/don.term.rebaptism
placement below. don.demo.bagai-unresolved cites _fleet.canon.f6-i-02 --
directly confirming this script's own F6-I placement (the Bagai/T2 material)
below. Both checked by direct grep before this script's own cell choices
were finalized, not after, and both agree with independently-reasoned
placements rather than driving them.

CROSS-CHECK AGAINST REPRESENTATIVE PHASE SEVEN (Representative/don_Rep_
Phase7_Encounter_Ecology_Mapping.md, seven-round-reviewed, already disposed
"Approved to proceed"), read in full this session: confirms G1/G2/T2
(purity, rebaptism, the Maximianist tension) and G5/T1 (refusal of imperial
legitimacy, the three pragmatic turns) and G3 (martyr-cult, "this world's
own richest emotional evidence") as this world's richest, most tested
material -- exactly the gravities this script leans on for F1-I, F4-I,
F3-E, and F5-P below. Confirms G4 (parallel hierarchy) as real but
Supporting, not Primary -- this script tags it only as a reinforcement of
the already-closed F3-I, never as an open-cell substantive answer on its
own. Independently confirms the five already-closed honest_limit domains
(ordinary daily life, doubt/emotional reception, women's own words beyond
Lucilla, theology beyond Tyconius, basilica archaeology) as genuinely thin,
not merely under-built -- the same finding this script relies on to leave
C-E/I/P/T, F1-T, F2-P, F2-T, F4-P, F4-T, and F5-T as genuine, undisguised
empties rather than reaching for a forced fill.

===========================================================================
PER-RECORD DISPOSITION TABLE -- MECHANICAL (the edit itself: canon_cells:
[] -> canon_cells: [<cells>]) vs. AUTHORED (why this cell, why not another,
why sometimes none). Organized by cell, since the coverage READ this
script runs is a per-cell question ("does X genuinely belong here?"), not a
per-record one. Every one of the 75 in-scope records is accounted for,
tagged or explicitly declined.
===========================================================================

--- C-E, C-I, C-P, C-T (4 cells) -- HONEST EMPTY, ALL FOUR ---
Fleet questions: who Jesus was/his teaching/his death/the resurrection/
personal salvation/Trinity -- core Christological and soteriological
identity questions common to every fleet world. Checked against all 75
records directly: none touches Jesus's own identity, teaching, the
resurrection as a historical claim, or personal salvation experience.
Donatism is orthodox, Nicene-Trinitarian Christianity on every one of these
questions -- its entire corpus is an ecclesiological dispute (who is the
true church, whose sacraments are valid) layered ON TOP OF a shared,
undisputed Christology, never a dispute ABOUT Christology itself. No
existing term/story/quote/witness states a distinctively-Donatist answer
to any C-cell question because there isn't one to state -- forcing a
generic-Christian-content record onto these cells would be exactly the
"forced fill" the governing principle bars, dressed up in this world's own
vocabulary without actually being this world's own distinctive material.
Left empty, honestly, all four.

--- F1-I ("What did you believe about God?" / "What did you argue about
among yourselves?" / "What did the councils in your time decide, and why
did it matter so much?" / Holy Spirit / "heart") -- SUBSTANTIVE ---
term: don.term.traditor-traditio (the founding accusation -- literally
  what this world argued about among itself first)
term: don.term.council-concilium (councils' own binding authority; "through
  a council, we once tried, and succeeded, in disciplining our own
  dissidents")
story: don.story.bagai-reconciliation (a specific council's own
  consequential decision -- also genuinely fits F4-I, see below; a record
  can belong to more than one cell when it genuinely answers both)
quote: don.quote.petilian-conscience-of-the-giver (the disputed doctrine's
  own founding proposition, in a Donatist voice)
gravity: don.gravity.ministerial-purity (the substantive content of the
  argument itself)
force: don.force.diocletianic-persecution-traditio-demand,
  don.force.felix-accusation-majorinus-consecration (the dispute's own
  historical origin)
contested_claim: don.contested.cirta-reserved-to-the-lord (a live,
  scholarly dispute over what one council's own ruling meant -- directly
  on point for "what did the councils decide, and why did it matter")
figure: don.figure.caecilian, don.figure.felix-of-aptungi,
  don.figure.majorinus (the founding-dispute's own named figures)
NOT added: don.term.bishop-episcopus/primate-primas (their natural home is
  F3-I, already closed -- see F3-I below); don.gravity.parallel-
  institutional-hierarchy (same reasoning, tagged to F3-I instead).

--- F1-T (original sin / bread-and-cup-transubstantiation / faith-alone)
-- HONEST EMPTY ---
Checked against every term/story/quote: Donatism took no distinctive
position on original sin, the nature of the eucharistic elements, or a
faith-vs-works soteriology -- its sacramental doctrine is entirely about
WHO may validly administer a sacrament (the minister's own traditor-free
standing), never about WHAT the sacrament itself metaphysically is or a
faith/works framework for salvation. don.term.purity and don.term.rebaptism
are the closest adjacent material and neither answers any of F1-T's three
actual questions. Left empty.

--- F2-E ("How would a historian evaluate what you've told me?" / "isn't
most of what's said about you legend" / "where is your record thinnest" /
suppressed gospels) -- SUBSTANTIVE ---
story: don.story.acta-purgationis-felicis (a judicial proceeding that
  collapsed a founding accusation under a forger's own confession -- a
  direct, positive illustration of exactly the kind of historian-grade
  evaluation this cell's own first question asks for)
contested_claim: don.contested.bishop-count-411-conference (a live,
  disclosed correction of this world's own build record via careful
  source-checking -- literally modeling "how would a historian evaluate
  what you've told me"), don.contested.circumcellion-character (the
  Frend-vs-Shaw historiographical contest over whether a hostile portrait
  reflects reality)
force: don.force.conference-of-carthage-verdict (the 411 Conference itself,
  tightly bound to the bishop-count contested claim above),
  don.force.transmission-caecilianist-victory,
  don.force.transmission-hostile-manuscript-tradition (both name, directly,
  WHY this world's own record is thinnest where it is -- the transmission
  mechanism itself)
figure: don.figure.optatus, don.figure.augustine, don.figure.emeritus,
  don.figure.petilian (the source-mediation figures -- the concrete "how
  would a historian evaluate" answer is substantially about which hand
  each piece of evidence passed through)
NOT added: don.story.gesta-apud-zenophilum (a second, nearly-as-strong
  Tier-1 judicial-corroboration story -- considered directly, not added,
  to keep this cell's own STORY assignment lean at one per the governing
  principle; acta-purgationis-felicis's sharper "collapse under confession"
  arc is the better single pick, not a quality judgment against the other).

--- F2-P ("what did your people look for in these texts that a modern
reader might miss" / "violence in these texts frightens me") -- HONEST
EMPTY ---
The closest material (Tyconius's own seven interpretive rules) already
answers a DIFFERENT, more precise fleet question -- F2-I's own "How did you
read your scriptures? What did you look for in them?" -- and is tagged
there (see F2-I below), not duplicated here for a similarly-worded but
distinct personal-register question. Nothing in this world's own corpus
addresses whether violence in scripture itself troubled this community
(the violence this world's own record discusses is violence done TO or BY
its own people in real history, never violence read IN a text). Left
empty.

--- F2-T (Bible as sole authority / Genesis as science) -- HONEST EMPTY ---
Scriptural authority itself was never the live dispute for this world (both
sides of the schism held the same view of scripture's own authority); no
record touches a literal/scientific reading of Genesis. Left empty.

--- F3-E ("hiding in catacombs" / "Did Constantine corrupt the church" /
"what would an outsider have found strangest" / "what did your neighbours
say about you, what were you accused of") -- SUBSTANTIVE ---
term: don.term.agonistici (the neighbours'/empire's own accusation --
  Circumcellion violence, imperial legislation naming the group by name),
  don.term.refusal-of-imperial-legitimacy ("Did Constantine corrupt the
  church" -- this world's own direct answer: Constantine's own council
  ruled against us, and a state-enforced verdict is not the church judging
  itself)
quote: don.quote.donatus-quid-est-imperatori (Donatus's own retort, the
  concrete utterance behind the imperial-legitimacy term above)
gravity: don.gravity.circumcellion-agonistici,
  don.gravity.refusal-of-imperial-legitimacy
force: don.force.oscillating-imperial-policy (the empire's own shifting
  favor -- directly what "did Constantine corrupt the church" is asking
  about writ large)
figure: don.figure.donatus
NOT added: don.contested.circumcellion-character (its own better, sharper
  fit is F2-E's historian-evaluation question -- see above; not
  double-counted here to keep this cell lean).

--- F4-E ("How do you know your practices went back to the apostles and
weren't later inventions?") -- SUBSTANTIVE ---
term: don.term.purity ("We sharpened it from Cyprian's own third-century
  teaching. We did not invent it new when our schism began." -- a direct,
  positive answer: not apostolic-era, but a real, traceable inheritance
  one full generation before the schism, not a novelty invented to justify
  it)
force: don.force.cyprianic-rigorist-inheritance (the same finding, at
  force-level: "this world's own direct doctrinal and institutional
  inheritance, not an invention at 311/312")
NOT claimed: this world's own record does not trace the purity doctrine to
  the apostles themselves, only to Cyprian (a full lifetime before the
  schism) -- the term and force above are tagged for genuinely answering
  the "not a later invention" half of this question, not for overclaiming
  apostolic origin the record does not state.

--- F4-I ("How did a person actually become one of you? Walk me through
it." / "why and how did you pray" / "the shared meal" / "how did you fast"
/ "when someone wronged the community, how was it handled -- and could
they come back?") -- SUBSTANTIVE ---
term: don.term.rebaptism (direct: "when someone comes to us from the rival
  church... we are giving the first true one" -- exactly "how did a person
  become one of you"; independently confirmed by don.demo.baptism-
  threshold's own canon_question_id, _fleet.canon.f4-i-01, checked before
  this placement was finalized), don.term.reception-without-reordination
  (direct: the Maximianist clergy's own return without re-baptism or
  re-ordination -- exactly "could they come back")
story: don.story.bagai-reconciliation (the concrete "wronged the
  community... could they come back" episode; also tagged F1-I above, for
  its own distinct "what did councils decide" angle -- both genuine)
gravity: don.gravity.rebaptism-boundary-marking
force: don.force.sustained-purity-rebaptism-practice, don.force.
  maximianist-fracture
figure: don.figure.primian (the primate presiding over the reconciliation)
NOT added: don.contested.maximianist-reception (its own sharper fit is
  F6-I's "hardest true thing" question -- see below, not double-counted
  here); no record answers the prayer/meal/fasting sub-questions -- this
  world's own corpus has no distinctive content on ordinary devotional
  practice, only on the boundary-marking rite of entry itself.

--- F4-P (quieting the mind / forgiving someone unrepentant / unanswered
prayer) -- HONEST EMPTY ---
Purely personal-devotional-interior questions; this world's own corpus is
institutional, doctrinal, and historical throughout, with no content on
contemplative practice, the ethics of forgiving an unrepentant wrongdoer,
or the experience of unanswered prayer. Considered whether the Maximianist
reception could be stretched to "forgiving someone not sorry" -- declined:
that episode is an ecclesiastical/disciplinary dispensation between
institutions, not a personal account of forgiving an individual who was
not repentant, and stretching it here would misrepresent both the episode
and the question. Left empty.

--- F4-T (born again / tithing / end-times-rapture / infant-vs-adult
baptism mode) -- HONEST EMPTY ---
Rebaptism is a dispute over WHO may validly baptize (minister purity), not
over the MODE of baptism (infant vs. believer's baptism) -- Donatism
practiced infant baptism like the rest of Latin Christianity, with no
distinctive comment on the question this cell actually asks. No record
touches personal conversion narrative, tithing practice, or eschatology.
Left empty.

--- F5-P ("Did belonging cost you anything -- family, friends, standing?"
/ "What held your people together across distances?") -- SUBSTANTIVE ---
term: don.term.martyr-martyrdom (the cost of belonging, stated plainly:
  death, at the hands of the rival's own imperial enforcers),
  don.term.anniversaria-commemoratio (the annual practice that held a
  scattered community together)
story: don.story.passio-marculi (cost = a life, and what was given up
  beforehand), don.story.lucilla-consecration-dispute (cost = family/
  standing specifically -- a public rebuke, a mishandled inheritance of
  trust, a woman's own grievance), don.story.passio-donati-sermon (the
  annual reading itself -- "a day the whole community was expected to
  keep, together, aloud" -- the most direct answer to "what held people
  together across distances"). Three stories rather than the usual one,
  disclosed deliberately: each answers a genuinely distinct half of this
  cell's own two combined questions (cost-as-life, cost-as-standing, and
  held-together), not three redundant illustrations of one point -- and
  Phase Seven's own cross-check (quoted above) independently names G3 as
  this world's own richest attested material, so a fuller-than-usual
  cell here reflects the corpus, not padding.
gravity: don.gravity.martyr-cult-identity
force: don.force.macarian-repression, don.force.martyr-cult-confessor-
  memory
figure: don.figure.marculus, don.figure.isaac-and-maximianus,
  don.figure.macrobius, don.figure.lucilla
NOT added as a fourth story: don.story.macrobius-letter-isaac-maximianus
  (a second martyrdom account, genuinely strong, but redundant with
  passio-marculi's own "cost = life" angle; its own named figures are
  still tagged above for retrieval, its story-level slot is not, to keep
  even this deliberately fuller cell from becoming an "everything that
  could fit" list).

--- F5-T (marriage/weddings / wealth and poverty) -- HONEST EMPTY ---
Considered Lucilla's own wealth (400 pieces of silver funding a rival
consecration) as a possible answer to "would you call anyone among you
rich" -- declined: that is a specific treasury-dispute fact belonging to
the founding narrative (already carried at F5-P), not a teaching or
attitude toward wealth and poverty as such, which this world's own corpus
does not otherwise address. No record touches marriage or weddings. Left
empty.

--- F6-E ("What's the clearest outside account we have of how your people
worshipped?" / "isn't wanting martyrdom a death wish") -- SUBSTANTIVE ---
term: don.term.deo-laudes (the liturgical acclamation itself)
quote: don.quote.deo-laudes-acclamation (the acclamation's own verbatim
  epigraphic text -- "DEO LAVDES", the clearest non-literary, non-hostile-
  mediated record of this world's own worship vocabulary that exists,
  independently re-confirmed against the vendored CIL VIII scan this
  build's own prior step already checked)
NOT claimed: no record rebuts "isn't a death wish" directly -- this
  cell's own second question stays unanswered even though the cell itself
  is substantive via the first.

--- F6-I ("Was there anything about your own community that troubled
you?" / "What did you never settle?" / "What's the hardest true thing
about your people?") -- SUBSTANTIVE ---
term: don.term.reception-without-reordination (also tagged F4-I above --
  "a fact we do not hide even though it sits uneasily beside how strictly
  we hold the same standard against our outside rival" is, in its own
  words, exactly this cell's own "hardest true thing")
story: don.story.council-of-cirta ("the same bishops whose own later
  movement would make traditor status an absolute, disqualifying category
  first chose, together, to set that same question aside among
  themselves" -- a founding-era story that is itself an unresolved
  self-complication, not a vindicating one; independently confirmed as
  this cell's own live material by don.demo.bagai-unresolved's own
  canon_question_id, _fleet.canon.f6-i-02, checked before this placement)
gravity: don.gravity.purity-rigor-vs-institutional-reception (T2),
  don.gravity.principled-refusal-vs-pragmatic-recourse (T1) -- the two
  named Tensional gravities are, definitionally, this world's own "what
  did you never settle" material
contested_claim: don.contested.maximianist-reception (whether the
  reception proves something more troubling than a bounded dispensation --
  a live, disclosed, unresolved question in this world's own build record)
figure: don.figure.purpurius (the founding-era figure who deflects the very
  question he himself once faced, at Cirta and again at Carthage)

--- F6-T ("Did your people believe outsiders were going to hell?" / "isn't
Christianity too narrow" / divorce and remarriage) -- SUBSTANTIVE ---
term: don.term.church-ecclesia ("We hold that our own communion, not our
  state-favored rival, is the true one" -- a genuine, real instance of
  exactly this cell's own exclusivism question, though narrower in scope
  than the fleet question anticipates: this world's excluded "outsider" is
  the rival Catholic church specifically, an intra-Christian boundary, not
  a claim about other world religions. Named explicitly here rather than
  overclaimed.)
NOT claimed: no record touches divorce or remarriage.

===========================================================================
WHAT THIS SCRIPT DOES
===========================================================================
Edits canon_cells: [] -> canon_cells: [<cells>] on 62 of the 75 in-scope
records (13 of 21 terms, 7 of 9 stories, all 4 quotes, all 8 gravities, 11
of 13 forces, all 4 contested_claims, 15 of 16 figures), per the ASSIGN
dict below, which is the single source of truth this script applies
mechanically -- every cell choice above was decided by reading the actual
record content and the actual fleet canon_question text first, and is
named in the table above, not invented at edit time. Leaves 13 records
(8 terms, 2 stories, 2 forces, 1 figure) with canon_cells: [] unchanged,
each named and reasoned in the table above.

===========================================================================
WHAT THIS SCRIPT DOES NOT DO
===========================================================================
- Does not touch records/don/doctrinal_witness/, records/don/honest_limit/,
  records/don/source/, records/don/search_record/, records/don/world_core/,
  records/don/voice_craft/, records/don/demonstration/, or records/don/
  ambient/ -- per this step's own constraint.
- Does not create any new record file, of any type.
- Does not invent a new honest_limit record for any of the ten cells left
  empty below -- an honest empty is this step's own legitimate outcome,
  not a gap to paper over with a record type this step is not authorized
  to author.
- Does not force every record to carry a cell -- 13 records genuinely have
  none, and are left untouched rather than padded onto a nearby cell.
- Does not re-derive or second-guess the 9 already-closed cells' own
  disposition -- reinforces two of them (F2-I, F3-I) with additional,
  independently-genuine term/story/gravity/figure tags, named explicitly
  above, but does not touch the doctrinal_witness/honest_limit records
  that originally closed any of the 9.

===========================================================================
HONEST EMPTIES -- THE FULL LIST, TEN CELLS, EACH NAMED ABOVE IN DETAIL
===========================================================================
C-E, C-I, C-P, C-T (Christology/salvation core -- this world is orthodox
and undistinguished on all four, genuinely nothing to report), F1-T
(original sin / transubstantiation / faith-alone -- sacramental validity
was disputed here, never sacramental metaphysics or soteriology), F2-P
(texts a modern reader might miss / violence in scripture -- the nearest
material already answers a different, more precise question at F2-I),
F2-T (biblical authority / Genesis-as-science -- never a live dispute for
this world), F4-P (contemplative practice / forgiving the unrepentant /
unanswered prayer -- pure personal-interior questions this institutional,
doctrinal, historical corpus does not reach), F4-T (born-again narrative /
tithing / eschatology / baptism mode -- rebaptism is a WHO-question, not a
WHEN/HOW-question), F5-T (marriage / wealth-and-poverty teaching -- no
record addresses either as a teaching, only as an incidental founding-
narrative fact already carried elsewhere).

===========================================================================
VALIDATION
===========================================================================
Run standalone (python3 Build/worlds/don/scripts/wb_don_s2y_canon_
cells.py --validate) against engine.m1.loader/schemas/gates, don's real
records, the real fleet, and the real registry -- see main() below for the
exact gates run and VALIDATION RESULT recorded at the bottom of this
docstring once the edits below were applied and checked.

VALIDATION RESULT (recorded after running this script's own --validate
mode against the real repo): schema-validation, referential, and
completion-per-type all clean (0 findings) across every touched record.
canon-coverage: of 28 cells, 13 substantive (4 pre-existing: F1-E, F3-I,
F3-T, plus F2-I newly upgraded from honest_limit-only to substantive by
this script's own don.term.liber-regularum/don.story.tyconius-condemnation/
don.figure.tyconius additions; 9 newly substantive by this script: F1-I,
F2-E, F3-E, F4-E, F4-I, F5-P, F6-E, F6-I, F6-T), 5 honest_limit-only
(F1-P, F3-P, F5-E, F5-I, F6-P -- unchanged, this script does not touch
honest_limit records), 10 empty (C-E, C-I, C-P, C-T, F1-T, F2-P, F2-T,
F4-P, F4-T, F5-T -- named and reasoned above), 0 multiple_honest_limit.
13 + 5 + 10 = 28.
"""
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
RECORDS_ROOT = REPO_ROOT / "records" / "don"

# record_type directory -> list of (id, [cells]) to apply. Mechanical
# application only -- the reasoning for every entry is in the docstring
# table above, organized by cell rather than by record, since the coverage
# read this script runs is a per-cell question.
ASSIGN: dict[str, list[tuple[str, list[str]]]] = {
    "term": [
        ("don.term.agonistici", ["F3-E"]),
        ("don.term.anniversaria-commemoratio", ["F5-P"]),
        ("don.term.bishop-episcopus", ["F3-I"]),
        ("don.term.church-ecclesia", ["F6-T"]),
        ("don.term.council-concilium", ["F1-I"]),
        ("don.term.deo-laudes", ["F6-E"]),
        ("don.term.liber-regularum", ["F2-I"]),
        ("don.term.martyr-martyrdom", ["F5-P"]),
        ("don.term.purity", ["F4-E"]),
        ("don.term.rebaptism", ["F4-I"]),
        ("don.term.reception-without-reordination", ["F4-I", "F6-I"]),
        ("don.term.refusal-of-imperial-legitimacy", ["F3-E"]),
        ("don.term.traditor-traditio", ["F1-I"]),
    ],
    "story": [
        ("don.story.acta-purgationis-felicis", ["F2-E"]),
        ("don.story.bagai-reconciliation", ["F1-I", "F4-I"]),
        ("don.story.council-of-cirta", ["F6-I"]),
        ("don.story.lucilla-consecration-dispute", ["F5-P"]),
        ("don.story.passio-donati-sermon", ["F5-P"]),
        ("don.story.passio-marculi", ["F5-P"]),
        ("don.story.tyconius-condemnation", ["F2-I"]),
    ],
    "quote": [
        ("don.quote.deo-laudes-acclamation", ["F6-E"]),
        ("don.quote.donatus-quid-est-imperatori", ["F3-E"]),
        ("don.quote.emeritus-magno-argumento", ["F2-E"]),
        ("don.quote.petilian-conscience-of-the-giver", ["F1-I"]),
    ],
    "gravity": [
        ("don.gravity.circumcellion-agonistici", ["F3-E"]),
        ("don.gravity.martyr-cult-identity", ["F5-P"]),
        ("don.gravity.ministerial-purity", ["F1-I"]),
        ("don.gravity.parallel-institutional-hierarchy", ["F3-I"]),
        ("don.gravity.principled-refusal-vs-pragmatic-recourse", ["F6-I"]),
        ("don.gravity.purity-rigor-vs-institutional-reception", ["F6-I"]),
        ("don.gravity.rebaptism-boundary-marking", ["F4-I"]),
        ("don.gravity.refusal-of-imperial-legitimacy", ["F3-E"]),
    ],
    "force": [
        ("don.force.conference-of-carthage-verdict", ["F2-E"]),
        ("don.force.cyprianic-rigorist-inheritance", ["F4-E"]),
        ("don.force.diocletianic-persecution-traditio-demand", ["F1-I"]),
        ("don.force.felix-accusation-majorinus-consecration", ["F1-I"]),
        ("don.force.macarian-repression", ["F5-P"]),
        ("don.force.martyr-cult-confessor-memory", ["F5-P"]),
        ("don.force.maximianist-fracture", ["F4-I"]),
        ("don.force.oscillating-imperial-policy", ["F3-E"]),
        ("don.force.sustained-purity-rebaptism-practice", ["F4-I"]),
        ("don.force.transmission-caecilianist-victory", ["F2-E"]),
        ("don.force.transmission-hostile-manuscript-tradition", ["F2-E"]),
    ],
    "contested_claim": [
        ("don.contested.bishop-count-411-conference", ["F2-E"]),
        ("don.contested.circumcellion-character", ["F2-E"]),
        ("don.contested.cirta-reserved-to-the-lord", ["F1-I"]),
        ("don.contested.maximianist-reception", ["F6-I"]),
    ],
    "figure": [
        ("don.figure.augustine", ["F2-E"]),
        ("don.figure.caecilian", ["F1-I"]),
        ("don.figure.donatus", ["F3-E"]),
        ("don.figure.emeritus", ["F2-E"]),
        ("don.figure.felix-of-aptungi", ["F1-I"]),
        ("don.figure.isaac-and-maximianus", ["F5-P"]),
        ("don.figure.lucilla", ["F5-P"]),
        ("don.figure.macrobius", ["F5-P"]),
        ("don.figure.majorinus", ["F1-I"]),
        ("don.figure.marculus", ["F5-P"]),
        ("don.figure.optatus", ["F2-E"]),
        ("don.figure.petilian", ["F2-E"]),
        ("don.figure.primian", ["F4-I"]),
        ("don.figure.purpurius", ["F6-I"]),
        ("don.figure.tyconius", ["F2-I"]),
    ],
}

# Records checked and deliberately left untouched (canon_cells: []
# unchanged), with the one-line reason -- the fuller reasoning for each is
# in the docstring table above, indexed by the cell each was considered
# for and declined at.
NOT_TAGGED: dict[str, str] = {
    "don.term.caecilianist": "naming-contest term; F3-T already substantive via don.witness.boundary-is-doctrine",
    "don.term.catholic-catholicus": "naming-contest term; F3-T already substantive via don.witness.boundary-is-doctrine",
    "don.term.church-of-the-martyrs": "redundant with don.term.martyr-martyrdom at F5-P; no distinct question",
    "don.term.confessor": "no fleet question distinctly asks about this sub-category",
    "don.term.donatist-pars-donati": "naming-contest term; F3-T already substantive via don.witness.boundary-is-doctrine",
    "don.term.persecution": "dual-persecution distinction has no distinct open-cell question; ground already covered at F5-P/F6-E",
    "don.term.primate-primas": "redundant with don.term.bishop-episcopus at F3-I",
    "don.term.schism": "naming-contest term; F3-T already substantive via don.witness.boundary-is-doctrine",
    "don.story.gesta-apud-zenophilum": "a second strong F2-E candidate; not added, to keep that cell's own story assignment lean at one (acta-purgationis-felicis)",
    "don.story.macrobius-letter-isaac-maximianus": "redundant with don.story.passio-marculi's own F5-P cost-of-belonging angle; its figures are still tagged there",
    "don.force.institutional-attrition": "Inferential-Thin, no participant question maps to it; ground already covered by don.limit.doubt-and-reception (F1-P)",
    "don.force.vandal-capture-of-carthage": "no don.source.* grounding named, no participant question maps to it directly",
    "don.figure.parmenian": "secondary role in F2-I's already-well-covered material (tyconius/liber-regularum/tyconius-condemnation); adding a fourth record there would pad rather than complete it",
}

CANON_CELLS_EMPTY = "canon_cells: []"


def _canon_cells_block(cells: list[str]) -> str:
    lines = ["canon_cells:"]
    lines.extend(f"- {c}" for c in cells)
    return "\n".join(lines)


def apply_assignments() -> list[str]:
    """Mechanical edit: for every (id, cells) in ASSIGN, find that record's
    file under records/don/<type>/, confirm it currently reads exactly
    `canon_cells: []` (fails loudly rather than silently if not -- this
    script only ever runs once per record, and a record that already
    carries cells is a sign this script is being re-run or the launch
    state assumption is stale), and rewrite that one line."""
    touched: list[str] = []
    for record_type, entries in ASSIGN.items():
        type_dir = RECORDS_ROOT / record_type
        for rid, cells in entries:
            path = type_dir / f"{rid}.md"
            if not path.exists():
                raise FileNotFoundError(f"expected record file not found: {path}")
            text = path.read_text(encoding="utf-8")
            if text.count(CANON_CELLS_EMPTY) != 1:
                raise ValueError(
                    f"{path}: expected exactly one {CANON_CELLS_EMPTY!r} line, "
                    f"found {text.count(CANON_CELLS_EMPTY)} -- refusing to edit blind"
                )
            new_text = text.replace(CANON_CELLS_EMPTY, _canon_cells_block(cells), 1)
            path.write_text(new_text, encoding="utf-8")
            touched.append(str(path.relative_to(REPO_ROOT)))
    return touched


def _print_disposition(records: dict) -> None:
    import sys

    sys.path.insert(0, str(REPO_ROOT))
    from engine.m1 import canon
    from engine.m1.loader import load_fleet_records

    fleet = load_fleet_records()
    cells = sorted(canon.valid_cells(fleet))
    print(f"\n{len(cells)} valid cells confirmed against the fleet's own canon_question records.")
    counts = {"substantive": 0, "honest_limit": 0, "empty": 0, "multiple_honest_limit": 0}
    for cell in cells:
        classification = canon.classify_cell(cell, records)
        counts[classification["status"]] += 1
        detail = ""
        if classification["status"] == "substantive":
            detail = f" <- {', '.join(classification['substantive'])}"
        elif classification["status"] in ("honest_limit", "multiple_honest_limit"):
            detail = f" <- {', '.join(classification['honest_limit'])}"
        print(f"  {cell:6s} {classification['status']}{detail}")
    print(f"\nTotals: {counts}")


def main() -> None:
    import sys

    if "--validate" in sys.argv:
        sys.path.insert(0, str(REPO_ROOT))
        from engine.m1 import gates
        from engine.m1.loader import load_fleet_records, load_world_records
        from engine.m1.registry import load_registry  # type: ignore

        records = load_world_records("don")
        fleet = load_fleet_records()
        try:
            registry = load_registry()
        except Exception:
            registry = {}
        print("Running gate battery against the real don + fleet corpus (post-edit)...")
        results = gates.run_all(records, fleet, registry)
        any_findings = False
        for name, findings in results.items():
            if findings:
                any_findings = True
                print(f"\n=== {name}: {len(findings)} finding(s) ===")
                for f in findings:
                    print(f"  - {f}")
            else:
                print(f"{name}: clean")
        _print_disposition(records)
        if any_findings:
            print("\nSome gates report findings -- see above.")
        else:
            print("\nAll gates clean.")
        return

    touched = apply_assignments()
    print(f"Edited canon_cells on {len(touched)} records:")
    for p in touched:
        print(f"  {p}")
    print(f"\nDeliberately left untouched ({len(NOT_TAGGED)} records):")
    for rid, reason in NOT_TAGGED.items():
        print(f"  {rid}: {reason}")


if __name__ == "__main__":
    main()
