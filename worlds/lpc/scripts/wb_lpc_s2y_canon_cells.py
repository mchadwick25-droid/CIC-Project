"""S2y: Latin Pastoral-Congregational Christianity (lpc) canon_cells
tagging pass -- the coverage-mapping step named as not-yet-attempted in
wb_lpc_s28.py's own docstring ("a full canon_cells tagging sweep (don's own
wb_don_s2y_canon_cells.py equivalent) is a separate, later step this script
does not attempt"), run separately because it is a genuinely different unit
of work (a coverage READ over all 67 already-built term/story/quote/figure/
gravity/force/contested_claim records, not new authoring). Follows don's own
precedent script (wb_don_s2y_canon_cells.py, read in full before this script
was written) and rzg's own (wb_rzg_s2y_canon_cells.py) in structure and
schema/gate discipline.

GOVERNING PRINCIPLE (CiC_Record_Native_World_Build_Process_V1.5.md, quoted
directly, carried from don's own script): "Every substantive cell offers its
stories and terms. When a cell's records are authored, the coverage read
asks: does a story genuinely belong here? a term? If yes, its canon_cells
says so... lean, one story and one term per cell where they genuinely
belong, never everything that could fit. If nothing genuinely belongs, that
finding is recorded and the cell stays empty there -- an honest empty is a
legitimate outcome, forced fill is not." This script is a coverage READ
against that bar, not a fill-every-cell exercise.

SCHEMA/GATE GROUND, RE-VERIFIED DIRECTLY THIS SESSION (not assumed from
don's or rzg's own script summaries):
  - canon_cells lives on ENVELOPE_PROPERTIES (engine/m1/schemas.py):
    {"type": "array", "items": {"type": "string"}} -- every record type
    carries it, additionalProperties:false does not touch it.
  - gate_referential (engine/m1/gates.py) checks every canon_cells entry
    resolves to `canon.valid_cells(fleet)` -- a typo'd or invented cell code
    is a hard finding, not silently ignored.
  - classify_cell() (engine/m1/canon.py) counts as "substantive" ONLY
    record_type in {"doctrinal_witness", "term", "story", "quote"}
    (canon.substantive_types()). gravity, force, contested_claim, and
    figure canon_cells tags do NOT close a cell for gate_canon_coverage --
    they are tagged in this script anyway, for the same reason
    retrieval_hint_keywords()/entity_cells() exist: they feed M4's Stage A
    keyword/entity routing and M2's compiled canon-map.json cache at build
    time, even though they carry no coverage-gate weight. Every place below
    where a cell ends this script still "empty" despite carrying a gravity/
    force/contested_claim/figure tag is named explicitly as such, not
    silently presented as closed.
  - classify_cell() status is "substantive" (>=1 substantive record),
    "honest_limit" (exactly one honest_limit, zero substantive), "empty"
    (neither), or "multiple_honest_limit" (a gate defect). Substantive
    always wins even where an honest_limit already sits on the same cell --
    confirmed directly against canon.py's own `if substantive: status =
    "substantive"` branch, checked before this script relied on it to
    knowingly upgrade F6-P below.

STARTING STATE, CONFIRMED DIRECTLY THIS SESSION:
  - 28 valid cells confirmed directly against records/_fleet/canon_question/
    *.md: C-E/I/P/T (4) plus F1-F6 x E/I/P/T (24).
  - 9 cells already closed before this script runs, confirmed by direct
    read of every file in records/lpc/doctrinal_witness/ and records/lpc/
    honest_limit/ (none touched by this script):
      doctrinal_witness (substantive): F3-I (lpc.witness.answerability-as-
        ground), F3-T (lpc.witness.communion-over-separation), F6-I (lpc.
        witness.confessor-claim-vs-regulated-peace)
      honest_limit: F1-E (lpc.limit.411-gesta-unread), F2-E (lpc.limit.the-
        silent-century), F3-P (lpc.limit.the-lapsed-own-account), F5-E
        (lpc.limit.rural-punic-berber-life), F5-I (lpc.limit.ordinary-
        interior-life), F6-P (lpc.limit.womens-own-voice)
  - Every other lpc record (records/lpc/term/, story/, quote/, gravity/,
    force/, contested_claim/, figure/ -- 67 records across those 7 types)
    carried canon_cells: [] before this script ran -- confirmed directly by
    an isolated read-only inventory subagent that read every one of those
    67 files in full and reported canon_cells: [] on every single one, no
    exceptions.

CROSS-CHECK AGAINST DEMONSTRATION canon_question_id (a live, independent
confirmation signal, not this script's own invention), all three of lpc's
demonstration records read directly before this script's own cell choices
were finalized: lpc.demo.road-back-examined cites _fleet.canon.f4-i-05
("when someone wronged the community, how was it handled -- and could they
come back?") -- directly confirming this script's own F4-I/lpc.term.
reconciliation-penitential-discipline placement below. lpc.demo.font-twice-
answered cites _fleet.canon.f6-i-02 -- confirming F6-I's own already-closed
placement and this script's own reinforcement of it (lpc.term.heresy, lpc.
gravity.sacramental-ordination-validity). lpc.demo.compel-three-phase cites
_fleet.canon.f6-p-05 ("the people who taught me the faith turned out to be
hypocrites") -- confirming this script's own F6-P placement of lpc.term.
compel-them-to-come-in and lpc.contested.compel-coercion-development below,
a deliberate upgrade named in full at F6-P's own entry.

CROSS-CHECK AGAINST REPRESENTATIVE PHASE SEVEN (Representative/lpc_Rep_
Phase7_Encounter_Ecology_Mapping.md, "Approved to proceed"), read in full
this session: independently confirms G1 (pastoral-office-flock-keeping),
G2 (penitential-discipline), G3 (collegial-communion-preserved), G6
(sacramental-ordination-validity), and G8 (confessor-authority-vs-episcopal-
peace) as this world's richest, most empirically-tested material (Phase
Five's own probe battery) -- exactly the gravities this script leans on for
F3-I, F4-I, F3-T, F6-I, F1-I below. Independently confirms G5 (conciliar-
authority-theory) as real but the weakest, Inferential-Thin-adjacent
connection in the whole matrix, and G7 (grace-and-human-incapacity) as
Augustine-phase-only and freestanding -- exactly this script's own F1-I and
F1-T placements, not stronger claims than the construction record supports.

===========================================================================
PER-CELL DISPOSITION TABLE -- MECHANICAL (the edit itself: canon_cells: []
-> canon_cells: [<cells>]) vs. AUTHORED (why this cell, why not another, why
sometimes none). Organized by cell, since the coverage READ this script
runs is a per-cell question ("does X genuinely belong here?"), not a
per-record one. Every one of the 67 in-scope records is accounted for,
tagged or explicitly declined. Single-cell-per-record is this script's own
default discipline (matching don's own figure/gravity practice, confirmed
by direct read of wb_don_s2y_canon_cells.py's own ASSIGN dict: every one of
its 15 figures and 8 gravities carries exactly one cell); a record is given
more than one cell only where it genuinely, distinctly answers two
different fleet questions, named as such at each such entry below.
===========================================================================

--- C-I, C-E, C-P, C-T (4 cells) -- HONEST EMPTY, ALL FOUR ---
Fleet questions: who Jesus was/his teaching/his death/the resurrection/
personal salvation/Trinity. Checked against all 67 records directly: this
world's entire corpus is ecclesiological and pastoral -- who holds
authority, how a failed member returns, whether a font outside the church
is valid -- built on top of a shared, undisputed, inherited Christology,
never a dispute about Christology itself (unlike, e.g., don's own world,
whose corpus is likewise ecclesiological but which this project ultimately
closed these same four cells for anyway, in a separate later pass, from
material this build does not yet have an lpc equivalent of -- named here
as a known future step, not attempted by this script). lpc.story.the-
plague-and-the-enemies is the one record that comes closest (Cyprian
preaching directly from Matthew 5:45, love of enemies, in imitation of a
God who gives sun and rain to all) but its own retrieval hints name its
real home as "how we treated outsiders or enemies" and "preaching and
catechesis," not Jesus's own teaching as such -- tagged at F5-I below
instead (see F5-I), not stretched onto C-I to manufacture a Christology
answer this record was never built to carry. Left empty, honestly, all
four -- this script's own governing principle bars forcing a generic-
Christian-content record onto these cells to dress up a fill this world's
corpus does not actually offer as distinctively its own.

--- F1-I ("What did you believe about God?" / "What did you argue about
among yourselves?" / "What did the councils in your time decide, and why
did it matter so much?" / Holy Spirit / "heart") -- SUBSTANTIVE ---
term: lpc.term.bishop-of-bishops (the 256 Council's own egalitarian
  formula -- literally what the councils decided), lpc.term.plenary-
  council (Augustine's own hierarchical counter-formula, overturning
  Cyprian's ruling a century later), lpc.term.the-one-episcopate (the
  doctrinal ground beneath both formulas), lpc.term.heresy (the rebaptism
  dispute itself -- argued at the 256 Council and in Augustine's On
  Baptism; also tagged F6-I below, a genuine dual: this cell answers "what
  did the councils decide," F6-I answers "what did you never settle" --
  the same dispute, two distinct questions)
quote: lpc.quote.bishop-of-bishops (the 256 preface's own full text, the
  single most cross-attested line in the corpus)
gravity: lpc.gravity.conciliar-authority-theory (the egalitarian-vs-
  hierarchical theory of council authority itself, Doc_04's own weakest/
  Inferential-Thin candidate but genuinely on point for this cell's own
  "what did the councils decide" question -- not overclaimed as reaching
  ordinary formation, which Doc_04 explicitly found it does not)
NOT added: lpc.gravity.collegial-communion-preserved and lpc.term.
  communion (their own clearer, more precise home is F3-T, already closed
  by lpc.witness.communion-over-separation and reinforced there below --
  not duplicated here to keep this cell's own conciliar-authority focus
  distinct from F3-T's own communion-despite-disagreement focus);
  lpc.force.organized-carthaginian-church (its own single home is F3-I,
  see below, not duplicated here).

--- F1-E (411-gesta-unread) -- ALREADY HONEST_LIMIT, NOT TOUCHED ---
Pre-existing. This script does not add or remove any record here.

--- F1-P ("room for doubt" / "couldn't believe what your own church
taught" / "same person I was since baptism") -- SUBSTANTIVE ---
story: lpc.story.the-psalms-on-the-wall -- read in full this session:
  Possidius records Augustine's own settled teaching, "that even after
  baptism, exemplary Christians and priests ought not depart this life
  without fitting repentance," and then records Augustine doing exactly
  that himself in his last illness -- penitential psalms copied and hung
  on the wall, wept over "freely and constantly" for days. This is a
  direct, non-stretched answer to this cell's own fourth question ("I was
  baptised years ago and I am the same person I was. Did your people know
  that struggle?"): yes, named plainly, in the one Tier 1, Documented
  account of either anchor figure's own final days. A genuine finding, not
  previously tagged anywhere -- this cell was open before this script ran.
figure: lpc.figure.possidius (the story's own sole eyewitness)
NOT added: this story is also tagged F5-I below (dying/last illness,
  distinct from the post-baptismal-repentance question this cell asks) --
  a genuine dual, not double-counted for the same question.

--- F1-T (original sin / bread-and-cup transubstantiation / faith alone)
-- SUBSTANTIVE ---
term: lpc.term.grace -- Augustine's anti-Pelagian doctrine, argued across
  thirteen works over roughly a decade: no one's own effort is ever
  sufficient; whatever good a person does was given first. Genuinely on
  point for this cell's own "were people saved by faith alone, not works"
  question -- the same monergism/synergism terrain, not a stretch (unlike
  don's own build, whose corpus never took a distinctive position on this
  question at all and left F1-T empty; lpc's corpus does, and this script
  credits that difference rather than copying don's own disposition
  blind).
gravity: lpc.gravity.grace-and-human-incapacity
figure: lpc.figure.augustine (this doctrine's own central figure)
force: lpc.force.manichaeism-and-pelagian-anthropology (the two rival
  systems Augustine had to answer, producing this gravity directly)
NOT added: lpc.contested.grace-pelagius-characterization (its own sharper,
  more precise fit is F2-E's historian-evaluation question -- see F2-E
  below, not double-counted here); original sin and the eucharistic
  elements as such are not addressed by any lpc record -- this cell is
  substantive via the faith/works-adjacent grace material alone, not all
  three of its own sub-questions.

--- F2-I ("How did you read your scriptures?" / "which writings" / "how
did someone who couldn't read receive the scriptures?") -- SUBSTANTIVE ---
term: lpc.term.preaching -- the weekly address to the already-baptized,
  evidenced by ~97 Sermons; the direct mechanism by which an illiterate
  congregation received scriptural exposition without personal reading.
gravity: lpc.gravity.preaching-and-catechesis (the medium itself)
force: lpc.force.inherited-latin-theological-vocabulary (the pre-existing
  vernacular vocabulary that made preaching/catechesis to an illiterate
  congregation possible at all)
NOT added: lpc.term.catechesis (its own clearer homes are F4-I and F4-T,
  see below -- catechesis is pre-baptismal instruction of a person joining,
  a distinct question from this cell's own "how did you read scripture, "
  ongoing, already-baptized reception; not triple-tagged here to avoid
  diluting either cell's own focus).

--- F2-E (the-silent-century) -- ALREADY HONEST_LIMIT, REINFORCED ---
Pre-existing honest_limit (lpc.limit.the-silent-century), not touched.
Reinforced with non-gate-counted tags only (contested_claim and force do
not count toward classify_cell()'s substantive test, confirmed above; this
cell's own status stays honest_limit, not silently upgraded):
contested_claim: lpc.contested.cyprian-death-genre (reliable-eyewitness-
  vs-hagiographic-convention is exactly a "how would a historian evaluate
  what you've told me" question, unresolved because the Acta Proconsularia
  hasn't been read), lpc.contested.de-unitate-recensions (a live textual-
  criticism dispute unresolved because the critical edition hasn't been
  read -- the same "where is your record thinnest" territory), lpc.
  contested.grace-pelagius-characterization (whether the anti-Pelagian
  corpus fairly represents a real opponent, unresolved since no Pelagian
  first-person source survives to check against)
force: lpc.force.transmission-asymmetric-span-133-year-silence, lpc.force.
  transmission-institutionally-dominant-side (both name, directly, WHY
  this world's own record is thinnest where it is -- the same reasoning
  don's own script gives for its own parallel F2-E reinforcement)

--- F2-P (modern reader might miss / violence in scripture) -- HONEST
EMPTY --- No lpc record anywhere reflects on whether scripture's own
violent content troubled this community, or on what a modern reader might
specifically miss reading these same texts. Left empty.

--- F2-T (Bible as sole authority / Genesis as science) -- HONEST EMPTY ---
Scriptural authority itself was never the live dispute for this world (no
record touches a literal/scientific reading of Genesis, and no record
takes a position on whether scripture is the sole authority as opposed to
the episcopate's own binding rulings -- if anything the corpus's own
conciliar material, already tagged at F1-I, cuts the other way). Left
empty.

--- F3-I ("Who held authority among you, and how did anyone come to have
it?" / "What actually happened when you gathered?" / "Was it actually
dangerous..." / "How did your movement spread" / "Who chose your
leaders") -- ALREADY SUBSTANTIVE (lpc.witness.answerability-as-ground),
REINFORCED --- This is the ecology's own hub (Doc_05 SS9.1, quoted
directly in the pre-existing witness record's own retrieval hints), so a
fuller-than-usual reinforcement set here reflects the corpus's own real
density, not padding -- disclosed deliberately, the same discipline don's
own script names for its own fuller F5-P:
term: lpc.term.suffrage (the corporate acclamation putting a man into
  office -- direct answer to "how did anyone come to have" authority),
  lpc.term.the-people (the congregation acting as a body -- electing,
  demanding, refusing to disperse), lpc.term.the-flock (the answerable
  bond itself, this cell's own doctrinal ground)
quote: lpc.quote.ancient-venom-against-my-episcopate (a rival faction's
  own persistent attack on the legitimacy of Cyprian's own election),
  lpc.quote.clamour-and-tears (the same congregational-acclamation pattern
  recurring at Augustine's own ordination, a century and a half later)
story: lpc.story.election-of-cyprian (the concrete case: elected "by the
  judgment of God and the favour of the people," over five presbyters'
  opposition)
gravity: lpc.gravity.pastoral-office-flock-keeping (the hub gravity
  itself)
force: lpc.force.congregational-acclamation-overriding-preference (the
  named pattern, attested for both anchor figures), lpc.force.organized-
  carthaginian-church (the precondition enabling both the office and the
  councils where it was argued over), lpc.force.standing-legal-condition-
  unlicensed-religion (directly on point for "was it actually dangerous")

--- F3-E (catacombs / "did Constantine corrupt the church" / outsider-
strangest / neighbours'-accusations) -- HONEST EMPTY --- Checked directly:
no lpc term/story/quote addresses external pagan perception, a catacombs-
style hidden-worship image, or the Constantinian settlement's own effect on
the church (lpc's Cyprian phase is pre-Constantine and its Augustine phase
engages the church-state question only through the Donatist-schism-and-
coercion material, already tagged F6-T/F6-P below, not through "did
Constantine corrupt the church" as its own distinct claim). lpc.force.
illegal-to-established-shift and lpc.force.standing-legal-condition-
unlicensed-religion are the closest adjacent force-level material, but
neither is a term/story/quote and neither states a position on this cell's
own specific sub-questions (outsider-strangest, neighbours'-accusations,
Constantine) rather than the general legal-danger backdrop already
credited at F3-I above. Left empty rather than stretched.

--- F3-P (the-lapsed-own-account) -- ALREADY HONEST_LIMIT, NOT TOUCHED ---
Pre-existing. This script does not add or remove any record here.

--- F3-T ("Was your church 'Catholic'?" / denominations / handling other
communities) -- ALREADY SUBSTANTIVE (lpc.witness.communion-over-
separation), REINFORCED ---
term: lpc.term.communion (formal standing that survives even the sharpest
  disagreement between bishops -- the same content the pre-existing
  witness record already states, named here at term-level too)
gravity: lpc.gravity.collegial-communion-preserved (the witness record's
  own associated gravity)

--- F4-I ("How did a person actually become one of you?" / "why and how
did you pray" / "the shared meal" / "how did you fast" / "when someone
wronged the community, how was it handled -- and could they come back?")
-- SUBSTANTIVE --- The second hub, matching G2's own Primary/richest-
tested status (Phase Seven SS2):
term: lpc.term.reconciliation-penitential-discipline (direct: the public,
  staged, community-witnessed road back -- independently confirmed by
  lpc.demo.road-back-examined's own canon_question_id, _fleet.canon.
  f4-i-05, checked before this placement was finalized), lpc.term.the-
  lapsed (the founding category the whole apparatus exists to answer),
  lpc.term.catechesis (direct: "how did a person actually become one of
  you" -- pre-baptismal instruction, the creed taught before the water;
  also tagged F4-T below, a genuine dual -- this cell answers "how did you
  become one of us," F4-T answers the distinct baptism-mode question),
  lpc.term.libelli (the Decian certificates, the documentary mechanism
  that created "the lapsed" needing a road back in the first place), lpc.
  term.libellatici-sacrificati (the two-tier distinction in how that road
  was calibrated)
quote: lpc.quote.shepherd-wounded-in-the-flock (De Lapsis SS4, the
  emotional register opening the whole lapsed-crisis argument this cell's
  own last question asks about), lpc.quote.longing-expectation-is-a-
  prayer-for-me (a rare direct answer to this cell's own prayer sub-
  question)
story: lpc.story.celerinus-writes-to-lucian (a concrete "could they come
  back" case -- granting peace to three named women; also tagged F6-I
  below, a genuine dual: this cell answers "could they come back," F6-I
  answers the distinct "who had the standing to grant it" tension)
gravity: lpc.gravity.penitential-discipline
force: lpc.force.decian-persecution-libelli-system (the crisis that
  creates the lapsed and the road back both), lpc.force.recurring-contest-
  failed-member (the persisting question this cell keeps returning to)
figure: lpc.figure.cyprian (the discipline's own architect; single-homed
  here rather than spread across his other roles, per this script's own
  one-cell-per-figure default)
NOT added: lpc.term.certificates-letters-of-peace and lpc.term.confessor
  (their own sharper, single home is F6-I -- see below; the confessor's
  own claim is a competing authority mechanism, not itself an answer to
  "how did a person become one of you," and not duplicated here); no lpc
  record answers this cell's own fasting sub-question.

--- F4-E ("How do you know your practices went back to the apostles and
weren't later inventions?") -- HONEST EMPTY --- lpc.force.inherited-latin-
theological-vocabulary is the closest adjacent material (a vocabulary
that pre-dates this world, enabling preaching/catechesis in the vernacular
the congregation already spoke -- tagged at F2-I instead, see above, since
force alone cannot close this cell under classify_cell() and no lpc term/
story/quote makes an apostolic-lineage-or-invention claim about any
specific practice the way don's own lpc.term.purity does for its own world).
Checked directly: no lpc record traces reconciliation, catechesis, or any
other named practice to the apostles, or explicitly defends it against a
charge of being a later invention. Left empty rather than stretched onto a
force-only, non-gate-counted fill.

--- F4-P (quieting the mind / forgiving someone unrepentant / unanswered
prayer) -- HONEST EMPTY --- Purely personal-devotional-interior questions;
considered whether lpc.demo.road-back-examined's own "a door with no
examination behind it is no door at all" content could answer "how do I
forgive someone who isn't sorry" -- declined: that demonstration (not
gate-counted regardless) argues the opposite case, that reconciliation
properly waits on genuine, examined change, not that an unrepentant party
should be forgiven anyway; stretching it here would misrepresent both the
content and this cell's own question, the same discipline don's own script
applied declining the same stretch for the Maximianist reception. Left
empty.

--- F4-T ("Were you born again" / tithing / rapture-eschatology / "Did you
baptise babies, or only adults who chose it for themselves?") --
SUBSTANTIVE --- term: lpc.term.catechesis (read in full this session: "We
  mean adult instruction, before baptism, of people making a consequential
  change of standing" -- a direct, disclosed-narrower answer to this
  cell's own fourth question specifically, not the born-again/tithing/
  eschatology sub-questions, which no lpc record touches). Also tagged
  F4-I above, a genuine dual (see F4-I's own entry).
NOT claimed: this term does not state that infant baptism was absent or
  forbidden, only that the norm it describes is adult catechumens choosing
  baptism after instruction -- named here rather than overclaimed, the
  same disclosure discipline don's own script used for its own F4-E entry.

--- F5-I (ordinary-interior-life) -- ALREADY HONEST_LIMIT, UPGRADED TO
SUBSTANTIVE, DELIBERATELY --- The pre-existing honest_limit (lpc.limit.
ordinary-interior-life) names a specific, narrower thinness -- the
ordinary believer's own INTERIOR, personal experience -- which is a
genuinely different claim from this cell's own first sub-question ("What
did you do when someone was sick? When someone was dying?") asked at the
level of concrete community action, not personal interiority. Two records
answer that distinct question directly and are added here, upgrading this
cell to substantive under classify_cell()'s own "substantive always wins"
rule (confirmed above) -- a deliberate upgrade, named as such, not a silent
overwrite of the honest_limit's own continuing truth about interior life
specifically:
story: lpc.story.the-plague-and-the-enemies (a severe epidemic; the
  bishop's own preached response; the congregation's own material relief
  extended to persecutors and non-Christians alike -- read in full this
  session, its own retrieval hints name "how we treated outsiders or
  enemies" and "preaching and catechesis" as its real home, not
  Christology, see the C-cells' own entry above), lpc.story.the-psalms-on-
  the-wall (Augustine's own final illness and death; also tagged F1-P
  above, a genuine dual for the distinct post-baptismal-repentance
  question)
figure: lpc.figure.pontius (the plague story's own sole source)
force: lpc.force.plague-of-cyprian, lpc.force.vandal-invasion-siege-of-
  hippo (the historical backdrop of each story respectively)
NOT claimed: the honest_limit's own continuing finding about ordinary,
  non-crisis interior life stands unchanged and is not touched by this
  script -- this upgrade is about concrete crisis-response action, a
  different question the same cell happens to also ask.

--- F5-E (rural-punic-berber-life) -- ALREADY HONEST_LIMIT, NOT TOUCHED ---
Pre-existing. This script does not add or remove any record here.

--- F5-P ("Did belonging cost you anything -- family, friends, standing?"
/ "What held your people together across distances?") -- SUBSTANTIVE ---
story: lpc.story.hundred-thousand-sesterces (material cost and solidarity
  held together across distance -- Carthage's own congregation ransoming
  fellow believers in Numidian towns), lpc.story.numidicus (a wife's own
  death, a man's own body left half-consumed and stoned, ordained
  afterward on the strength of what he endured; also tagged F6-E below,
  a genuine dual -- this cell answers "did belonging cost you," F6-E
  answers the distinct death-wish question)
figure: lpc.figure.numidicus is single-homed at F6-E instead (see below,
  this script's own one-cell-per-figure default; his story itself still
  carries both cells)
force: lpc.force.valerianic-persecution (the persecution that
  martyred Cyprian, confirming the cost named by this cell directly)

--- F5-T (marriage/weddings / wealth and poverty) -- HONEST EMPTY ---
Considered the hundred-thousand-sesterces sum itself as a possible answer
to "would you call anyone among you rich" -- declined: that is a specific
ransom-fundraising fact belonging to F5-P's own cost-and-solidarity
question, not a teaching or attitude toward wealth and poverty as such,
which no lpc record otherwise addresses. No record touches marriage or
weddings. Left empty.

--- F6-I ("Was there anything about your own community that troubled
you?" / "What did you never settle?" / "hardest true thing") -- ALREADY
SUBSTANTIVE (lpc.witness.confessor-claim-vs-regulated-peace), REINFORCED
--- Independently confirmed as this cell's own live material by lpc.demo.
font-twice-answered's own canon_question_id, _fleet.canon.f6-i-02, checked
before these placements were finalized:
term: lpc.term.confessor (the rival authority claim itself), lpc.term.
  certificates-letters-of-peace (its own literal instrument), lpc.term.
  heresy (also tagged F1-I above, a genuine dual -- see F1-I's own entry)
story: lpc.story.celerinus-writes-to-lucian (also tagged F4-I above, a
  genuine dual -- see F4-I's own entry)
gravity: lpc.gravity.confessor-authority-vs-episcopal-peace (the pre-
  existing witness record's own associated gravity), lpc.gravity.
  sacramental-ordination-validity (the font question, "answered twice,
  oppositely, a century apart" -- Doc_07's own description of exactly
  this cell's own "what did you never settle" feeling)
force: lpc.force.augustine-engagement-cyprian-conciliar-acts (the century-
  later reversal mechanism itself), lpc.force.confessors-claim-to-grant-
  peace (the confessor tension's own originating force)
figure: lpc.figure.celerinus, lpc.figure.lucian (the correspondence's own
  two named confessors)

--- F6-E ("clearest outside account of your worship" / "isn't wanting
martyrdom a death wish") -- SUBSTANTIVE --- No lpc record answers this
cell's own first sub-question (no epigraphic or non-literary outside
account of lpc worship exists in this world's corpus, unlike don's own
Deo Laudes precedent) -- named here rather than silently passed over:
story: lpc.story.the-death-of-cyprian (Tier 3/Contested, explicitly a
  genre-shaped tradition-portrait -- Cyprian's own calm, chosen composure
  facing execution), lpc.story.numidicus (also tagged F5-P above, a
  genuine dual -- "he himself had not wanted to survive," the sharpest
  single line in this world's own corpus on this cell's own second
  question)
figure: lpc.figure.numidicus (single-homed here, not also at F5-P, per
  this script's own one-cell-per-figure default -- see F5-P's own entry)

--- F6-P (womens-own-voice) -- ALREADY HONEST_LIMIT, UPGRADED TO
SUBSTANTIVE, DELIBERATELY --- The pre-existing honest_limit names a
specific, narrower absence (no woman's own narrating voice survives in
this world's corpus), which is a genuinely different claim from this
cell's own fifth question ("The people who taught me the faith turned out
to be hypocrites. Did that happen among you?") -- independently confirmed
as this cell's own live material by lpc.demo.compel-three-phase's own
canon_question_id, _fleet.canon.f6-p-05, checked before this placement was
finalized. One record answers that distinct question directly and is
added here, upgrading this cell to substantive under classify_cell()'s own
"substantive always wins" rule -- a deliberate upgrade, named as such, the
same move this script already makes at F5-I, and the same move don's own
script made for its own F2-I:
term: lpc.term.compel-them-to-come-in (Augustine's own three-phase
  reversal on coercion -- reported honestly, all three phases, "not the
  one that is easiest to defend")
contested_claim: lpc.contested.compel-coercion-development (whether that
  reversal is a genuine change of mind or a retrospective self-
  presentation -- a live, disclosed, unresolved question)
NOT claimed: the honest_limit's own continuing finding about a woman's own
  narrating voice stands unchanged and is not touched by this script.

--- F6-T ("Do you believe outsiders are going to hell?" / "isn't
Christianity too narrow" / divorce and remarriage) -- SUBSTANTIVE ---
term: lpc.term.schism (the tearing of the one body -- a separate altar, a
  separate bishop, a separate people in the same town, distinguished from
  mere survivable disagreement). Named explicitly, not overclaimed: this
  world's own excluded "outsider" in this material is another Christian
  communion whose baptism it disputes, an intra-Christian boundary, not a
  claim about other world religions -- the same disclosed-narrower move
  don's own script made for its own church-ecclesia entry at this same
  cell.
force: lpc.force.donatist-schism (the rival communion itself -- dominant
  across much of North African Christian life for most of the century
  between the two phases, appealing to Cyprian's own conciliar rulings for
  its own legitimacy; the concrete referent behind the term above)
NOT claimed: no lpc record touches divorce or remarriage.

===========================================================================
WHAT THIS SCRIPT DOES
===========================================================================
Edits canon_cells: [] -> canon_cells: [<cells>] on 65 of the 67 in-scope
records (all 19 terms, all 7 stories, all 5 quotes, all 7 figures, all 8
gravities, 15 of 17 forces, all 4 contested_claims), per the ASSIGN dict
below, which is the single source of truth this script applies
mechanically -- every cell choice above was decided by reading the actual
record content and the actual fleet canon_question text first, and is named
in the table above, not invented at edit time. Leaves 2 force records
(corpus-outliving-the-world, illegal-to-established-shift) with canon_
cells: [] unchanged, each named and reasoned in DECLINED below. This
script also knowingly upgrades two pre-existing honest_limit-only cells
(F5-I, F6-P) to substantive, each named and reasoned in its own table entry
above, and leaves four pre-existing honest_limit cells (F1-E, F2-E, F3-P,
F5-E) untouched.

===========================================================================
WHAT THIS SCRIPT DOES NOT DO
===========================================================================
- Does not touch records/lpc/doctrinal_witness/, records/lpc/honest_limit/,
  records/lpc/source/, records/lpc/world_core/, records/lpc/voice_craft/,
  records/lpc/demonstration/, or records/lpc/ambient/.
- Does not create any new record file, of any type.
- Does not invent a new honest_limit or doctrinal_witness record for any
  of the ten cells left empty below -- an honest empty is this step's own
  legitimate outcome. (A later, separate closure pass -- the lpc equivalent
  of don's own post-hoc "Answer the Canon" closure commit, or rzg's own
  wb_rzg_s2z_canon_closure.py -- is required before lpc can enter the
  registry with zero canon-coverage findings, since lpc is not in engine/
  m9/enforce.py's own GRANDFATHERED_WORLDS set; that is a distinct, later
  unit of work this script does not attempt.)
- Does not force every record to carry a cell -- 2 force records genuinely
  have none, and are left untouched rather than padded onto a nearby cell.
- Does not re-derive or second-guess the 9 already-closed cells' own
  disposition -- reinforces five of them (F1-T's grace material is new
  substantive content rather than reinforcement of a closed cell, so this
  really means F2-E, F3-I, F3-T, F6-I, and the two upgrades F5-I/F6-P) with
  additional, independently-genuine term/story/quote/gravity/force/figure
  tags, named explicitly above, but does not touch the doctrinal_witness/
  honest_limit records that originally closed any of them.

===========================================================================
HONEST EMPTIES -- THE FULL LIST, TEN CELLS, EACH NAMED ABOVE IN DETAIL
===========================================================================
C-E, C-I, C-P, C-T (Christology/salvation core -- this world is orthodox
and undistinguished on all four, genuinely nothing to report as this
world's own distinctive content), F2-P (a modern reader's own blind spots /
violence in scripture -- no record reflects on either), F2-T (biblical
authority / Genesis-as-science -- never a live dispute for this world),
F3-E (catacombs / Constantine / outsider-strangest / neighbours'-
accusations -- the adjacent legal-status force material already serves
F3-I, and answers none of this cell's own four sub-questions distinctly),
F4-E (apostolic-vs-invented-practice -- the adjacent vocabulary-inheritance
force material cannot close this cell alone under classify_cell(), and no
lpc term/story/quote makes an apostolic-lineage-or-invention claim about
any named practice), F4-P (contemplative practice / forgiving the
unrepentant / unanswered prayer -- pure personal-interior questions this
institutional, doctrinal, historical corpus does not reach), F5-T
(marriage / wealth-and-poverty teaching -- no record addresses either as a
teaching).

DECLINED (force records genuinely left canon_cells: [] unchanged):
lpc.force.corpus-outliving-the-world -- Augustine's own theological legacy
  outliving this world's own close is a legacy/influence claim, not an
  evidentiary-thinness or lived-encounter claim; no fleet cell asks this
  world's own posterity as such, and stretching it onto F2-E's own
  "where is your record thinnest" would misstate what this force actually
  says (thinness of transmission, not richness of later influence, are
  different claims).
lpc.force.illegal-to-established-shift -- Doc_04 itself explicitly
  declined to advance this as its own gravity ("changes the instruments
  available to a bishop, not the thing a bishop is... connects to no
  gravity"); its own background legal-context content is already carried,
  where it genuinely bears on a fleet question, by the persecution and
  conciliar forces tagged at F3-I and F6-I above -- not independently
  re-tagged here to avoid claiming this force answers a question on its
  own that it does not.

===========================================================================
VALIDATION
===========================================================================
Run standalone (python3 worlds/lpc/scripts/wb_lpc_s2y_canon_cells.py
--validate) against engine.m1.loader/schemas/gates, lpc's real records, the
real fleet, and the real registry -- see main() below for the exact gates
run and VALIDATION RESULT recorded at the bottom of this docstring once the
edits below were applied and checked.

VALIDATION RESULT (this script's own --validate run against the real repo,
post-edit): schema-validation, referential, reciprocity, completion-per-
type, narratability, glossary-retrofit-complete, quote-recording, alias-
safety, distribution-health, retrieval-negatives-structured, confidence-
crosscheck, rights, edition-rights-consistency, canonical-address,
readability, voice-craft-prompt-budget, no-build-attribution, voice-
perspective, id-convention, quote-mark-fidelity, and quote-verbatim all
clean (0 findings) across every touched record. canon-coverage: of 28
cells, exactly the disposition this table predicted before the script
ran -- 14 substantive (F1-I, F1-P, F1-T, F2-I, F3-I, F3-T, F4-I, F4-T,
F5-I, F5-P, F6-E, F6-I, F6-P, F6-T), 4 honest_limit (F1-E, F2-E, F3-P,
F5-E), 10 empty/blank-cell findings (C-E, C-I, C-P, C-T, F2-P, F2-T, F3-E,
F4-E, F4-P, F5-T), 0 multiple_honest_limit. 14 + 4 + 10 = 28. The 10
blank-cell findings are gate_canon_coverage findings by construction (an
"empty" cell is a defined gate defect, confirmed above) -- expected and
disclosed, not a script bug: closing them is the separate, later closure
pass this docstring's own WHAT THIS SCRIPT DOES NOT DO section already
names as required before lpc can enter the registry (lpc is not in engine/
m9/enforce.py's own GRANDFATHERED_WORLDS set) and not attempted here.
"""
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
RECORDS_ROOT = REPO_ROOT / "records" / "lpc"

# record_type directory -> list of (id, [cells]) to apply. Mechanical
# application only -- the reasoning for every entry is in the docstring
# table above, organized by cell rather than by record, since the coverage
# read this script runs is a per-cell question.
ASSIGN: dict[str, list[tuple[str, list[str]]]] = {
    "term": [
        ("lpc.term.bishop-of-bishops", ["F1-I"]),
        ("lpc.term.catechesis", ["F4-I", "F4-T"]),
        ("lpc.term.certificates-letters-of-peace", ["F6-I"]),
        ("lpc.term.communion", ["F3-T"]),
        ("lpc.term.compel-them-to-come-in", ["F6-P"]),
        ("lpc.term.confessor", ["F6-I"]),
        ("lpc.term.grace", ["F1-T"]),
        ("lpc.term.heresy", ["F1-I", "F6-I"]),
        ("lpc.term.libellatici-sacrificati", ["F4-I"]),
        ("lpc.term.libelli", ["F4-I"]),
        ("lpc.term.plenary-council", ["F1-I"]),
        ("lpc.term.preaching", ["F2-I"]),
        ("lpc.term.reconciliation-penitential-discipline", ["F4-I"]),
        ("lpc.term.schism", ["F6-T"]),
        ("lpc.term.suffrage", ["F3-I"]),
        ("lpc.term.the-flock", ["F3-I"]),
        ("lpc.term.the-lapsed", ["F4-I"]),
        ("lpc.term.the-one-episcopate", ["F1-I"]),
        ("lpc.term.the-people", ["F3-I"]),
    ],
    "story": [
        ("lpc.story.celerinus-writes-to-lucian", ["F4-I", "F6-I"]),
        ("lpc.story.election-of-cyprian", ["F3-I"]),
        ("lpc.story.hundred-thousand-sesterces", ["F5-P"]),
        ("lpc.story.numidicus", ["F5-P", "F6-E"]),
        ("lpc.story.the-death-of-cyprian", ["F6-E"]),
        ("lpc.story.the-plague-and-the-enemies", ["F5-I"]),
        ("lpc.story.the-psalms-on-the-wall", ["F5-I", "F1-P"]),
    ],
    "quote": [
        ("lpc.quote.ancient-venom-against-my-episcopate", ["F3-I"]),
        ("lpc.quote.bishop-of-bishops", ["F1-I"]),
        ("lpc.quote.clamour-and-tears", ["F3-I"]),
        ("lpc.quote.longing-expectation-is-a-prayer-for-me", ["F4-I"]),
        ("lpc.quote.shepherd-wounded-in-the-flock", ["F4-I"]),
    ],
    "gravity": [
        ("lpc.gravity.collegial-communion-preserved", ["F3-T"]),
        ("lpc.gravity.conciliar-authority-theory", ["F1-I"]),
        ("lpc.gravity.confessor-authority-vs-episcopal-peace", ["F6-I"]),
        ("lpc.gravity.grace-and-human-incapacity", ["F1-T"]),
        ("lpc.gravity.pastoral-office-flock-keeping", ["F3-I"]),
        ("lpc.gravity.penitential-discipline", ["F4-I"]),
        ("lpc.gravity.preaching-and-catechesis", ["F2-I"]),
        ("lpc.gravity.sacramental-ordination-validity", ["F6-I"]),
    ],
    "force": [
        ("lpc.force.augustine-engagement-cyprian-conciliar-acts", ["F6-I"]),
        ("lpc.force.confessors-claim-to-grant-peace", ["F6-I"]),
        ("lpc.force.congregational-acclamation-overriding-preference", ["F3-I"]),
        ("lpc.force.decian-persecution-libelli-system", ["F4-I"]),
        ("lpc.force.donatist-schism", ["F6-T"]),
        ("lpc.force.inherited-latin-theological-vocabulary", ["F2-I"]),
        ("lpc.force.manichaeism-and-pelagian-anthropology", ["F1-T"]),
        ("lpc.force.organized-carthaginian-church", ["F3-I"]),
        ("lpc.force.plague-of-cyprian", ["F5-I"]),
        ("lpc.force.recurring-contest-failed-member", ["F4-I"]),
        ("lpc.force.standing-legal-condition-unlicensed-religion", ["F3-I"]),
        ("lpc.force.transmission-asymmetric-span-133-year-silence", ["F2-E"]),
        ("lpc.force.transmission-institutionally-dominant-side", ["F2-E"]),
        ("lpc.force.valerianic-persecution", ["F5-P"]),
        ("lpc.force.vandal-invasion-siege-of-hippo", ["F5-I"]),
    ],
    "contested_claim": [
        ("lpc.contested.compel-coercion-development", ["F6-P"]),
        ("lpc.contested.cyprian-death-genre", ["F2-E"]),
        ("lpc.contested.de-unitate-recensions", ["F2-E"]),
        ("lpc.contested.grace-pelagius-characterization", ["F2-E"]),
    ],
    "figure": [
        ("lpc.figure.augustine", ["F1-T"]),
        ("lpc.figure.celerinus", ["F6-I"]),
        ("lpc.figure.cyprian", ["F4-I"]),
        ("lpc.figure.lucian", ["F6-I"]),
        ("lpc.figure.numidicus", ["F6-E"]),
        ("lpc.figure.pontius", ["F5-I"]),
        ("lpc.figure.possidius", ["F1-P"]),
    ],
}

# Records checked and deliberately left untouched (canon_cells: []
# unchanged), with the one-line reason -- the fuller reasoning for each is
# in the docstring's own DECLINED section above.
NOT_TAGGED: dict[str, str] = {
    "lpc.force.corpus-outliving-the-world": "legacy/influence claim, not evidentiary-thinness or lived-encounter; no fleet cell asks this world's own posterity",
    "lpc.force.illegal-to-established-shift": "Doc_04 itself declined to advance this as its own gravity; its background legal content is already carried by the persecution/conciliar forces tagged at F3-I and F6-I",
}

CANON_CELLS_EMPTY = "canon_cells: []"


def _canon_cells_block(cells: list[str]) -> str:
    lines = ["canon_cells:"]
    lines.extend(f"- {c}" for c in cells)
    return "\n".join(lines)


def apply_assignments() -> list[str]:
    """Mechanical edit: for every (id, cells) in ASSIGN, find that record's
    file under records/lpc/<type>/, confirm it currently reads exactly
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

        records = load_world_records("lpc")
        fleet = load_fleet_records()
        try:
            registry = load_registry()
        except Exception:
            registry = {}
        print("Running gate battery against the real lpc + fleet corpus (post-edit)...")
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
