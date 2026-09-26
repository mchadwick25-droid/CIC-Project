"""S2y: Reformed Cities (rzg) canon_cells tagging pass -- the coverage-
mapping step named as upcoming in wb_rzg_s2x_doctrinal_witness.py's own
docstring, run separately because it is a genuinely different unit of work
(a coverage READ over the 61 records not touched by S2x, not new authoring).
Follows don's own precedent script (wb_don_s2y_canon_cells.py, read in full
before this script was written) in structure and schema/gate discipline.

GOVERNING PRINCIPLE, carried directly from don's own script: "lean, one
story and one term per cell where they genuinely belong, never everything
that could fit. If nothing genuinely belongs, that finding is recorded and
the cell stays empty there." This script is a coverage READ against that
bar, not a fill-every-cell exercise.

SCHEMA/GATE GROUND (re-verified directly this session, engine/m1/canon.py,
engine/m1/gates.py): classify_cell() counts as "substantive" ONLY
record_type in {doctrinal_witness, term, story, quote}. gravity, force,
contested_claim, and figure canon_cells tags do NOT close a cell for
gate_canon_coverage -- they are tagged in this script anyway, for the same
retrieval/keyword-routing reason don's own script gives, and every place
below where a cell stays "empty" despite carrying a gravity/force/
contested_claim/figure tag is disclosed as such, not left ambiguous.

STARTING STATE, CONFIRMED DIRECTLY: S2x closed 10 of 28 cells -- 3
substantive via doctrinal_witness (F3-I one-conviction-two-enactments,
F3-T triple-refusal, F1-T one-supper-two-poles) and 7 via honest_limit
(F5-I, F2-E, F1-E, F4-I, F6-P, F1-P, F5-E). The other 61 rzg records (17
term, 3 story, 6 figure, 6 quote, 6 gravity, 19 force, 3 contested_claim)
all carried canon_cells: [] before this script ran -- confirmed by grep,
one match each, no record already mid-tagged. source/world_core/voice_
craft/demonstration/ambient/doctrinal_witness/honest_limit are out of this
script's own scope, matching don's identical exclusion list.

A GENUINE, DISCLOSED DIFFERENCE FROM DON'S OWN WORLD, CHECKED DIRECTLY, NOT
ASSUMED BY ANALOGY: rzg's own 17-term lexicon was built lean from the start
(Doc_03's own candidate roster, non-redundant by design -- confirmed
directly against every term's own plain_meaning before any cell was
chosen), unlike don's 21 terms, eight of which were naming-contest
synonyms don's own script correctly left untagged. Every one of rzg's 17
terms and all 6 quotes and all 8 figures turned out to answer a genuine,
distinct fleet question on direct inspection -- 0 terms/quotes/figures left
untagged here, against don's 8/21 terms and 1/16 figures left untagged.
This is reported as a checked finding about this world's own tighter build,
not a relaxed standard: every placement below states the specific fleet
question and the specific record content that answers it, the same
discipline don's own script applies throughout. Forces are the one type
where rzg, like don, leaves a real minority untagged (6 of 19) -- named
below, each a genuine meta/transmission/structural finding with no direct
participant-facing question, not a participant answer this script missed.

CROSS-CHECK AGAINST DEMONSTRATION canon_question_id, checked before any
cell choice below was finalized: rzg.demo.consensus-contest cites
_fleet.canon.f2-e-01 ("How would a historian evaluate what you've told
me?") -- independently confirms F2-E is a live, real cell for this world,
though (per the substantive-only rule above) no term/story/quote closes it
substantively; rzg.demo.predestination-and-dread cites _fleet.canon.f1-t-03
-- directly inside F1-T, already substantive via S2x, confirming rather
than driving that placement. rzg.demo.why-we cites _fleet.canon.c-t-03 but
is a fleet-wide subject-of-utterance/voice probe, not this world's own
distinctive Christological content -- checked and NOT treated as evidence
that C-T needs a doctrinal answer beyond what rzg.quote.christ-the-mirror-
of-election already substantively supplies below.

===========================================================================
PER-CELL DISPOSITION -- ALL 18 CELLS OPEN AFTER S2X
===========================================================================

--- C-E, C-I (2 cells) -- HONEST EMPTY ---
Checked against all 61 records: no term/story/quote states a distinctive
rzg answer to what this world's people had about Jesus historically, who
he was, what he taught, or what his death/resurrection meant. This world's
whole corpus is a dispute over predestination, the Supper, scriptural
authority, and church discipline, layered on a shared, undisputed
Christology -- exactly the structural reason don's own script leaves its
own C-cells empty, independently confirmed true here too rather than
assumed by analogy.

--- C-P, C-T (2 cells) -- SUBSTANTIVE ---
quote: rzg.quote.christ-the-mirror-of-election -- "Do not search for proof
  of your own election apart from Christ. Look at Christ, and see your own
  election reflected there." This is this world's own distinctive,
  first-person-relevant answer to "who is Jesus to you, not to your
  church" (C-P) and to a functional equivalent of "personal Lord and
  Savior" (C-T): not the American-revivalist phrasing, but this world's
  own idiom for exactly that relationship -- assurance is found by looking
  to Christ, not by searching oneself. Genuinely fits both cells' own
  distinct registers (personal/P and theological-challenge/T) without
  restating the same content twice for two unrelated questions.
NOT claimed: neither Trinity nor penal substitution (C-T's other two
  sub-questions) is answered by any record; the cell is substantive via
  this one genuine sub-question, not padded to look complete on all three.

--- F1-I ("What did you believe about God?" / "argued about among
yourselves" / councils / Holy Spirit / "heart") -- SUBSTANTIVE ---
term: rzg.term.predestination-election, rzg.term.providence -- both direct,
  first-order statements of what this world believed about God.
gravity: rzg.gravity.sovereignty-of-god-predestination-election.
force: rzg.force.augustinian-inheritance-predestination-grace (the
  doctrine's own intellectual lineage), rzg.force.bolsec-controversy (a
  real internal argument over exactly this doctrine -- "argued about among
  yourselves," not a stretch: Bolsec was one of ours, publicly challenging
  Calvin's own teaching at Geneva), rzg.force.second-helvetic-confession-
  heidelberg-catechism (the doctrine's own later, fuller written fixing).
figure: rzg.figure.beza (carried the doctrine into its fullest systematic
  form).
NOT added: "councils in your time decided" and "Holy Spirit"/"heart" stay
  unanswered within this cell -- the Disputation/council material is
  tagged at F2-I/F3-I instead (see below), where it fits more precisely,
  not duplicated here to pad this cell's own sub-question count.

--- F1-P, F1-E, F5-I, F5-E, F2-E, F6-P (6 cells) -- HONEST_LIMIT, S2X, NOT
REINFORCED --- Checked each directly for a genuine, non-contradicting
substantive reinforcement (don's own precedent for F2-I/F3-I). None found:
F1-E/F5-I/F5-E's own honest_limit records state a specific missing GENRE
(narrative, daily-practice, material-description) that no existing term/
story/quote actually supplies without contradicting the limit's own claim;
F2-E has no term/story/quote at all (see F2-E's own empty-classification
note below); F6-P has no second attested woman's-own-words case beyond
what the honest_limit itself already names. F1-P is reinforced only at a
different, non-overlapping register (C-P/C-T's own doctrinal-prescription
content, not F1-P's own actual-felt-experience question) -- see C-P/C-T
above; not tagged to F1-P itself, since doing so would misrepresent the
mirror quote as answering whether comfort was actually FELT, which it does
not claim.

--- F4-I ("could they come back" etc.) -- UPGRADED FROM HONEST_LIMIT-ONLY
TO SUBSTANTIVE --- rzg.limit.consistory-case-narrative (S2x) states this
world cannot supply a specific NAMED CASE from Geneva's own unvendored
consistory registers. That is a different, narrower claim than "this world
has no general doctrine of how wrongdoing was handled" -- Doc_07 SS2E's
own general-doctrine/specific-case-law split, restated at the record
level: quote: rzg.quote.seniors-selected-from-the-people (Calvin's own
Institutes IV.3.8, directly on point: "seniors selected from the people to
unite with the bishops in pronouncing censures and exercising discipline")
supplies the GENERAL doctrine genuinely, without contradicting the
honest_limit's own narrower claim that no specific case survives. term:
rzg.term.consistory, rzg.term.excommunication (the concrete disciplinary
tool). gravity: rzg.gravity.consistorial-church-discipline. force: rzg.
force.1541-ecclesiastical-ordinances-consistory-founding, rzg.force.
perrinist-crisis. This cell now carries both an honest_limit (untouched,
still true and still valuable -- no specific case exists) and substantive
records (the general doctrine genuinely exists) side by side, the same
honest outcome Doc_07 SS2E's own split describes.

--- F2-I ("How did you read your scriptures?" / "which writings... as
scripture" / "how did the illiterate receive scripture") -- SUBSTANTIVE ---
term: rzg.term.sola-scriptura (the reading-authority conviction itself),
  rzg.term.catechism (direct answer to the illiteracy sub-question: fixed,
  memorizable, taught to the whole population), rzg.term.sixty-seven-
  articles, rzg.term.disputation (the founding document and its own public-
  argument method).
story: rzg.story.first-zurich-disputation (also genuinely fits F3-I, see
  below -- a real dual fit, not padding: the same event is both how this
  world read/argued scripture AND how its council exercised authority).
quote: rzg.quote.taught-better-from-scripture (Zwingli's own confession,
  "where I have not now correctly understood said Scriptures I shall allow
  myself to be taught better, but only from said Scriptures" -- a direct,
  first-person statement of this world's own reading discipline).
gravity: rzg.gravity.scripture-sole-authority-disputation-catechesis.
force: rzg.force.zwinglis-1519-preaching-sausage-affair (the reading
  METHOD's own origin -- continuous exposition rather than the fixed
  lectionary).
figure: rzg.figure.zwingli, rzg.figure.calvin, rzg.figure.faber (the
  Disputation's own opposing voice).

--- F2-P ("what a modern reader might miss" / "violence in scripture")
-- HONEST EMPTY --- No record addresses whether scripture's own violent
content troubled this world (the violence this world's own record
discusses is violence done to or by real people in real history, never
violence read in a text); the "what a modern reader might miss" material
already lives at the more precise F2-I. Left empty, matching don's own
identical structural finding for its own F2-P.

--- F2-T ("Did you believe the Bible was the only authority?" / "Genesis
as science") -- SUBSTANTIVE ---
term: rzg.term.sola-scriptura (dual-tagged with F2-I -- its own content
  answers both "how did you read scripture" and "was it your only
  authority" at once: "Scripture alone, not church tradition or a pope's
  decree, settles what we believe"), rzg.term.confession-of-faith (states
  the confession's own SUBORDINATE relationship to scripture directly:
  "we wrote our confessions not to say something new, but so that what we
  already believed could survive" -- confessions preserve, they do not
  originate, authority).
NOT claimed: no record touches Genesis or a literal/scientific reading;
  the cell is substantive via the authority sub-question alone.

--- F3-E ("catacombs" / "did Constantine corrupt the church" / "what would
an outsider find strangest" / "neighbours' accusations") -- EMPTY (force
tagged, non-gate-counted) --- No term/story/quote answers any of these four
sub-questions distinctively for this world -- checked directly, not
assumed. force: rzg.force.counter-reformation-sustained-pressure (the
closest real content -- sustained Catholic pressure across the whole
window) tagged for retrieval value only; it does not close this cell at
the gate level, and this record discloses that plainly rather than
implying otherwise.

--- F3-I ("Who held authority among you, and how did anyone come to have
it?") -- SUBSTANTIVE, S2X + REINFORCED --- Already substantive via S2x's
rzg.witness.one-conviction-two-enactments. Reinforced with genuinely
distinct, previously-untagged material naming the actual office-holders
and institutions: term: rzg.term.antistes (Zurich's own senior pastoral
title), rzg.term.elder (Geneva's own lay Consistory authority), rzg.term.
consistory (dual-tagged with F4-I -- the institution itself IS both "who
holds authority" and "how wrongdoing is handled"). story: rzg.story.first-
zurich-disputation (dual-tagged with F2-I, see above). gravity: rzg.
gravity.consistorial-church-discipline, rzg.gravity.council-led-authority-
vs-consistorial-independence (dual-tagged with F6-I, see below). force:
rzg.force.1541-ecclesiastical-ordinances-consistory-founding. figure: rzg.
figure.bullinger (held the Antistes title after Zwingli's death -- a
concrete instance of the term above, not a redundant second mention).

--- F3-P ("Did your churches ever fail to hold their own people
accountable... and if so, what happened?" / "used power against Christians
who disagreed, defend that" / "temples and old gods") -- EMPTY at the
substantive level (contested_claim + force tagged, non-gate-counted) ---
The one record that genuinely and directly answers "defend that" --
rzg.contested.anabaptist-schism-legitimacy, whose own held_against/
concedes fields state plainly that this world's council "moved to suppress
the Anabaptist movement by civil force in the years that followed the 1525
baptisms" -- is a contested_claim, not a substantive type. No term/story/
quote states this content independently. This cell's own closest
substantive-adjacent content (rzg.witness.triple-refusal's own tensions[]
field, S2x) is deliberately NOT re-tagged here, per this step's own
constraint against touching S2x's doctrinal_witness/honest_limit output
(matching don's own identical constraint) -- named here explicitly as a
real, checked, disclosed gap rather than silently left unexplained.
force: rzg.force.anabaptist-schism tagged for retrieval value.
"Temples and old gods" sub-question: not claimed; the closest material
(the material-culture subtraction) already lives at the S2x honest_limit/
ambient records, not duplicated here.

--- F4-E ("How do you know your practices went back to the apostles and
weren't later inventions?") -- SUBSTANTIVE --- term: rzg.term.reformation
-- a genuine, if inverted, direct answer: this world does not claim
unbroken apostolic continuity; it claims scriptural testing as a different
and, in its own eyes, stronger warrant ("We test every inherited practice
against Scripture. We let go of what will not stand.") -- exactly the
kind of scriptural-warrant-over-mere-continuity answer Construction Notes
already documents as this world's own Representative's own diagnostic
habit ("notices whether a practice or claim can point to scriptural
warrant").

--- F4-P (quieting the mind / forgiving the unrepentant / unanswered
prayer) -- HONEST EMPTY --- Purely personal-devotional-interior questions;
this world's corpus is institutional, doctrinal, and historical throughout
(Doc_07 SS5's own genre-asymmetry finding, independently confirmed again
here), with no content on contemplative practice or an individual's own
unanswered prayer. Left empty, matching don's own identical finding.

--- F4-T (born again / tithing / end-times / infant-vs-adult baptism)
-- EMPTY at the substantive level (force + contested_claim tagged,
non-gate-counted) --- "Did you baptise babies, or only adults who chose it
for themselves?" is directly on point for the Anabaptist material, but no
dedicated term/story/quote exists for infant baptism as such in this
world's own 17-term lexicon (confirmed directly -- the roster has no
baptism-mode term at all, since the mode was never itself contested
between Zurich and Geneva, only rejected as a further step by the
Anabaptists). force: rzg.force.anabaptist-schism tagged for retrieval.
Born-again narrative, tithing, and eschatology: not claimed, no record
touches any of the three.

--- F5-P ("Did belonging cost you anything?" / "What held your people
together across distances?") -- SUBSTANTIVE --- story: rzg.story.calvins-
journey-to-zurich (two cities, two languages, held together by a shared
conviction strong enough to travel and sign one page -- the distances
question, directly), rzg.story.myconius-account-of-zwinglis-death (cost =
a life, in battle, defending the reform -- the cost question, directly).
quote: rzg.quote.zwinglis-last-words ("They are able, it is true, to kill
the body but not the soul" -- the cost, in his own reported words).
force: rzg.force.wars-of-kappel-zwinglis-death. figure: rzg.figure.farel
(the journey), rzg.figure.myconius (the death account).

--- F5-T (marriage/weddings / wealth and poverty) -- HONEST EMPTY --- No
record addresses marriage, weddings, or a teaching on wealth and poverty
as such (Zwingli's and Calvin's own marriages are biographical facts never
built into a record). Left empty, matching don's own identical finding.

--- F6-E ("clearest outside account of how you worshipped" / "wanting to
die as a martyr, a death wish?") -- HONEST EMPTY --- Genuinely different
from don's own F6-E (which closed via epigraphy and a hostile-source
Deo-laudes acclamation): this world built no comparable outside-observer
worship account, and Zwingli's own death at Kappel was a death in battle
as a field chaplain, not a sought martyrdom the "death wish" framing
could even engage -- this world's own record already states it has no
hagiography or martyr-cult at all (S2x honest_limit, F2-E). Left empty,
a real and disclosed difference from don, not an oversight.

--- F6-I ("troubled you" / "never settled" / "hardest true thing")
-- EMPTY at the substantive level (gravity tagged, non-gate-counted) ---
T1 and T2 are, definitionally, this world's own "never settled" material,
and are tagged here: gravity: rzg.gravity.council-led-authority-vs-
consistorial-independence, rzg.gravity.zwinglis-remembrance-reading-vs-
negotiated-consensus (both dual-tagged with F1-T/F3-I above). But no
term/story/quote independently states either tension AS an unsettled
question outside of the already-built (and, per this step's own
constraint, untouched) rzg.witness records -- checked directly: rzg.term.
sign-and-the-thing-signified and rzg.term.mutual-consent both frame the CT
formula as having SETTLED the Supper question, the opposite of what F6-I
asks, and would misrepresent their own content if tagged here. A genuine,
checked difference from don's own F6-I (substantive there via don.term.
reception-without-reordination and don.story.council-of-cirta, records
whose own content states a self-complication directly, in first-person
term/story form -- no analogous term/story exists in rzg's own lexicon).
Disclosed as a real finding, not a shortfall this script papers over.

--- F6-T ("outsiders going to hell" / "too narrow" / divorce and
remarriage) -- HONEST EMPTY --- No term/story/quote in rzg's own 17-term
lexicon addresses ecclesial exclusivism, salvation's scope, or divorce/
remarriage (unlike don, whose don.term.church-ecclesia closes this cell
directly -- rzg's own lexicon has no equivalent "true church" naming
term). rzg.witness.triple-refusal's own content is the closest match but
is S2x output, not re-tagged here per this step's own constraint. Left
empty, a genuine, checked, disclosed difference from don.

===========================================================================
WHAT THIS SCRIPT DOES
===========================================================================
Edits canon_cells: [] -> canon_cells: [<cells>] on 54 of the 61 in-scope
records (17 of 17 terms, 3 of 3 stories, 6 of 6 quotes, 6 of 6 gravities,
13 of 19 forces, 3 of 3 contested_claims, 8 of 8 figures), per the ASSIGN
dict below. Leaves 6 records (all forces) with canon_cells: [] unchanged,
each named and reasoned in NOT_TAGGED below.

===========================================================================
WHAT THIS SCRIPT DOES NOT DO
===========================================================================
- Does not touch records/rzg/doctrinal_witness/, records/rzg/honest_limit/,
  records/rzg/source/, records/rzg/world_core/, records/rzg/voice_craft/,
  records/rzg/demonstration/, or records/rzg/ambient/.
- Does not create any new record file, of any type.
- Does not invent a new honest_limit for any of the 11 cells left
  genuinely empty below.
- Does not force every record onto a cell -- 6 forces genuinely have none.

===========================================================================
VALIDATION
===========================================================================
Run standalone (python3 Build/worlds/rzg/scripts/wb_rzg_s2y_canon_cells.py
--validate) against engine.m1.loader/canon/gates, rzg's real records, the
real fleet, and the real registry. VALIDATION RESULT recorded after
running: schema-validation, referential, and completion-per-type all clean
across every touched record. canon-coverage: of 28 cells, 11 substantive
(3 pre-existing from S2x: F3-I, F3-T, F1-T; F4-I newly upgraded from
honest_limit-only; 7 newly substantive: C-P/C-T counted together as one
finding above but as two distinct cells, F1-I, F2-I, F2-T, F5-P), 6
honest_limit-only (F5-I, F2-E, F1-E, F6-P, F1-P, F5-E -- unchanged), 11
empty (C-E, C-I, F2-P, F3-E, F3-P, F4-P, F4-T, F5-T, F6-E, F6-I, F6-T --
each named and reasoned above), 0 multiple_honest_limit. 11 + 6 + 11 = 28.
"""
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
RECORDS_ROOT = REPO_ROOT / "records" / "rzg"

# record_type directory -> list of (id, [cells]) to apply. Mechanical
# application only -- the reasoning for every entry is in the docstring
# table above, organized by cell, since the coverage read this script runs
# is a per-cell question.
ASSIGN: dict[str, list[tuple[str, list[str]]]] = {
    "term": [
        ("rzg.term.antistes", ["F3-I"]),
        ("rzg.term.catechism", ["F2-I"]),
        ("rzg.term.confession-of-faith", ["F2-T"]),
        ("rzg.term.consistory", ["F3-I", "F4-I"]),
        ("rzg.term.disputation", ["F2-I"]),
        ("rzg.term.elder", ["F3-I"]),
        ("rzg.term.excommunication", ["F4-I"]),
        ("rzg.term.heads-of-agreement", ["F1-T"]),
        ("rzg.term.memorial-commemoration", ["F1-T"]),
        ("rzg.term.mutual-consent", ["F1-T"]),
        ("rzg.term.predestination-election", ["F1-I"]),
        ("rzg.term.providence", ["F1-I"]),
        ("rzg.term.reformation", ["F4-E"]),
        ("rzg.term.sign-and-the-thing-signified", ["F1-T"]),
        ("rzg.term.sixty-seven-articles", ["F2-I"]),
        ("rzg.term.sola-scriptura", ["F2-I", "F2-T"]),
        ("rzg.term.the-lords-supper-spiritual-presence", ["F1-T"]),
    ],
    "story": [
        ("rzg.story.calvins-journey-to-zurich", ["F5-P"]),
        ("rzg.story.first-zurich-disputation", ["F2-I", "F3-I"]),
        ("rzg.story.myconius-account-of-zwinglis-death", ["F5-P"]),
    ],
    "quote": [
        ("rzg.quote.christ-the-mirror-of-election", ["C-P", "C-T"]),
        ("rzg.quote.mass-not-a-sacrifice", ["F1-T"]),
        ("rzg.quote.seniors-selected-from-the-people", ["F4-I"]),
        ("rzg.quote.signs-and-things-signified", ["F1-T"]),
        ("rzg.quote.taught-better-from-scripture", ["F2-I"]),
        ("rzg.quote.zwinglis-last-words", ["F5-P"]),
    ],
    "gravity": [
        ("rzg.gravity.consistorial-church-discipline", ["F3-I", "F4-I"]),
        ("rzg.gravity.council-led-authority-vs-consistorial-independence", ["F3-I", "F6-I"]),
        ("rzg.gravity.scripture-sole-authority-disputation-catechesis", ["F2-I"]),
        ("rzg.gravity.sovereignty-of-god-predestination-election", ["F1-I"]),
        ("rzg.gravity.spiritual-presence-rejection-of-corporeal-sacrificial-mediation", ["F1-T"]),
        ("rzg.gravity.zwinglis-remembrance-reading-vs-negotiated-consensus", ["F1-T", "F6-I"]),
    ],
    "force": [
        ("rzg.force.1541-ecclesiastical-ordinances-consistory-founding", ["F3-I", "F4-I"]),
        ("rzg.force.anabaptist-schism", ["F3-P", "F4-T"]),
        ("rzg.force.augustinian-inheritance-predestination-grace", ["F1-I"]),
        ("rzg.force.bolsec-controversy", ["F1-I"]),
        ("rzg.force.consensus-tigurinus-force", ["F1-T"]),
        ("rzg.force.counter-reformation-sustained-pressure", ["F3-E"]),
        ("rzg.force.late-medieval-sacramental-clerical-order", ["F1-T"]),
        ("rzg.force.marburg-colloquy", ["F1-T"]),
        ("rzg.force.perrinist-crisis", ["F4-I", "F6-I"]),
        ("rzg.force.second-helvetic-confession-heidelberg-catechism", ["F1-I"]),
        ("rzg.force.transmission-author-gravity-genre-asymmetries", ["F2-E"]),
        ("rzg.force.wars-of-kappel-zwinglis-death", ["F5-P"]),
        ("rzg.force.zwinglis-1519-preaching-sausage-affair", ["F2-I"]),
    ],
    "contested_claim": [
        ("rzg.contested.anabaptist-schism-legitimacy", ["F3-P"]),
        ("rzg.contested.sign-and-the-thing-signified", ["F1-T"]),
        ("rzg.contested.zwinglis-remembrance-vs-negotiated-consensus", ["F1-T"]),
    ],
    "figure": [
        ("rzg.figure.beza", ["F1-I"]),
        ("rzg.figure.bullinger", ["F3-I"]),
        ("rzg.figure.calvin", ["F2-I"]),
        ("rzg.figure.faber", ["F2-I"]),
        ("rzg.figure.farel", ["F5-P"]),
        ("rzg.figure.hegenwald", ["F2-E"]),
        ("rzg.figure.myconius", ["F5-P"]),
        ("rzg.figure.zwingli", ["F2-I"]),
    ],
}

# Records checked and deliberately left untouched (canon_cells: []
# unchanged), with the one-line reason -- the fuller reasoning for each is
# in the docstring's own per-cell table where relevant.
NOT_TAGGED: dict[str, str] = {
    "rzg.force.genevas-1526-bern-alliance-1536-break-calvins-arrival": "background causal/origin history; no direct participant-facing fleet question maps to it distinctly from what zwinglis-1519-preaching-sausage-affair already carries",
    "rzg.force.genevas-refugee-inflow-bernese-dependence": "background socio-political context feeding G4's own external pressure; no participant question maps to it directly without stretching F5-P beyond what it actually states",
    "rzg.force.no-external-ending-force": "a meta/structural finding about the construction window itself, not a participant-facing answer",
    "rzg.force.no-internal-fracture": "a meta/structural finding (confirms one world, two strands), not a participant-facing answer",
    "rzg.force.selective-reception-four-descendant-traditions": "a fleet-transmission/scope finding, not a participant-facing answer",
    "rzg.force.synod-of-dort-international-dimension": "a fleet-transmission/scope finding, not a participant-facing answer",
}

CANON_CELLS_EMPTY = "canon_cells: []"


def _canon_cells_block(cells: list[str]) -> str:
    lines = ["canon_cells:"]
    lines.extend(f"- {c}" for c in cells)
    return "\n".join(lines)


def apply_assignments() -> list[str]:
    """Mechanical edit: for every (id, cells) in ASSIGN, find that record's
    file under records/rzg/<type>/, confirm it currently reads exactly
    `canon_cells: []` (fails loudly rather than silently if not), and
    rewrite that one line."""
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

        records = load_world_records("rzg")
        fleet = load_fleet_records()
        try:
            registry = load_registry()
        except Exception:
            registry = {}
        print("Running gate battery against the real rzg + fleet corpus (post-edit)...")
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
