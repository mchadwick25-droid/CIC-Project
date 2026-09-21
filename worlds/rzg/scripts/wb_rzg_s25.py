"""B-5 (S2.5): Reformed Cities (rzg) gravity + force records.

WHAT THIS SCRIPT DOES. Converts this world's already-built, already-reviewed
Gravity Discovery (Doc_04_Gravity_Discovery.md, Approved to proceed,
Revision 2) and Forces Document (Doc_08_Forces_Document.md, Approved to
proceed, Revision 2) into record-native `gravity` and `force` records under
records/rzg/gravity/ and records/rzg/force/, per the live schema and gate
battery. Follows don's own precedent (wb_don_s25.py, read in full before
this script was written) exactly: gravity and force are separate,
cross-referencing records, never one record covering both.

INPUTS, mapped to OUTPUTS, precisely:
  - Doc_04_Gravity_Discovery.md SS3.1-3.5 (confirmed classification: 3
    Primary - G1 Sovereignty of God/Predestination and Election, G2
    Spiritual Presence and Rejection of Corporeal/Sacrificial Mediation,
    G3 Scripture as Sole and Sufficient Authority; 1 Supporting - G4
    Consistorial Church Discipline, Geneva-scope-qualified; 2 Tensional -
    T1 Council-Led Authority vs. Consistorial Independence, T2 Zwingli's
    Remembrance Reading vs. the Negotiated Consensus) -> 6 gravity
    records. T1/T2's own full text (both poles, both quoted verbatim, both
    tests) was read in full this session and is carried directly, not
    summarized further than Doc_04 itself already states it.
  - Doc_08_Forces_Document.md Section 3 (the Six-Cell Matrix, all 19
    forces, Layers 1-3 each) -> 19 force records, one per named force
    (1A-1/1A-2/1B-1/1B-2/1B-3/2A-1..5/2B-1..6/3A-1/3B-1/3B-2). Read in
    full this session - every description below carries that force's own
    Layer 1 (Historical Event) and Layer 3 (Formation Impact) content;
    Layer 2 (World's Own Experience, several marked [Inhabited] and
    carried verbatim from Doc_05 in Doc_08's own text) supplies this
    record's own first-person manifestations where the force's own
    entry has one.
  - Doc_08 Section 5 (Forces-and-Gravities Synthesis) -> the gravity <->
    force relations below, mirrored exactly from that section's own
    "Connected forces" lists per gravity, never re-derived or force-fit
    (Doc_08's own explicit caution, quoting its own don-precedent lesson:
    "a wording variance gets flagged upstream, not silently converted").
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_ROOT = REPO_ROOT / "records" / "rzg"

WORLD_ID = "the-reformed-cities-zurich-and-geneva"
SCHEMA_VERSION = 2


def _yaml_dump(payload: dict) -> str:
    return yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=100, default_flow_style=False)


def _write(path: Path, payload: dict, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\n" + _yaml_dump(payload) + "---\n" + body.strip() + "\n", encoding="utf-8")


# ------------------------------------------------------------- gravities ---
GRAVITIES: list[dict] = [
    dict(
        slug="sovereignty-of-god-predestination-election", name="Sovereignty of God / Predestination and Election",
        classification="primary",
        description=(
            "God's own free choice, made before the world existed, determines who is saved - not "
            "anything foreseen or earned in the one chosen. We hold this as the ground of a settled "
            "life, not a threat: whoever is joined to Christ by true faith already has, in that faith "
            "itself, the only evidence of election anyone is given. Present in seed form in Zwingli's "
            "own 1527 election exposition, systematized fully in Calvin's Institutes, and carried "
            "forward into the Second Helvetic Confession's own pastoral register and, at Dort's own "
            "international remove, Beza's own sharper systematic form. Confirmed cross-strand Primary: "
            "the core conviction is genuinely attested in both cities' own founding voices, even though "
            "its fullest systematized, later double-predestination form is substantially Calvin/Beza-"
            "concentrated - a divergence we disclose rather than smooth away."
        ),
        manifestations=[
            "our founder's own 1527 exposition working through Romans 8-9",
            "Calvin's Institutes, Books II-III, our own load-bearing doctrinal core",
            "the Second Helvetic Confession's own pastoral answer: look to Christ, not to your own conscience, for proof of election",
            "the Bolsec controversy (1551), where this doctrine was tested as a live pastoral question before the whole Geneva congregation",
        ],
        relations=[
            {"type": "tension-with", "target": "rzg.term.predestination-election"},
        ],
    ),
    dict(
        slug="spiritual-presence-rejection-of-corporeal-sacrificial-mediation",
        name="Spiritual Presence and the Rejection of Corporeal/Sacrificial Mediation", classification="primary",
        description=(
            "We refuse Rome's claim that the Mass repeats Christ's own sacrifice, and we refuse "
            "Wittenberg's claim that Christ's body sits locally in the bread. What we affirm - that "
            "Christ is truly given, by the Spirit, to whoever receives him believing - took both cities "
            "and a 1549 agreement to state together. Zurich's own founding refusal of the Mass (1523) "
            "matured, at Marburg (1529), into a further refusal of corporeal presence specifically "
            "aimed at Wittenberg, not Rome; the Consensus Tigurinus (1549) then supplies this doctrine's "
            "own strand-bridging positive formula, resolving our own internal tension (T2) in text "
            "without settling, in our own words, whether that resolution is genuine synthesis or "
            "diplomatic elasticity."
        ),
        manifestations=[
            "the Sixty-Seven Articles, Art. XVIII: 'the mass is not a sacrifice, but is a remembrance of the sacrifice'",
            "the refusal pressed further at Marburg (1529) against Wittenberg's own corporeal presence",
            "the Consensus Tigurinus's own 9th Head of Agreement (1549), jointly signed by both our cities",
        ],
        relations=[
            {"type": "tension-with", "target": "rzg.term.the-lords-supper-spiritual-presence"},
            {"type": "associated-with", "target": "rzg.contested.sign-and-the-thing-signified"},
        ],
    ),
    dict(
        slug="scripture-sole-authority-disputation-catechesis",
        name="Scripture as Sole and Sufficient Authority, Enacted Through Disputation and Catechesis",
        classification="primary",
        description=(
            "Whatever Scripture will not yield, we have no standing to require; whatever it does "
            "yield, no pope, council, or custom may set aside. This is the strongest cross-strand "
            "conviction in our own record, enacted two different ways by two cities that never "
            "borrowed each other's own method: at Zurich, public Disputation, argued aloud before the "
            "city council until it judged what the text had yielded, binding every priest in its "
            "territory; at Geneva, sustained catechesis, doctrine built up book by book and taught to "
            "the whole population. The Anabaptist schism (1525) tested this same method against a "
            "rival reading from inside our own founding circle - we do not deny they read Scripture; "
            "we deny they read it whole."
        ),
        manifestations=[
            "the First and Second Zurich Disputations (1523), where the Sixty-Seven Articles were argued and ratified",
            "Calvin's Geneva Catechism, taught to the whole population",
            "the Second Helvetic Confession and Heidelberg Catechism, later fixed statements of the same founding conviction",
        ],
        relations=[
            {"type": "tension-with", "target": "rzg.term.sola-scriptura"},
            {"type": "associated-with", "target": "rzg.contested.anabaptist-schism-legitimacy"},
        ],
    ),
    dict(
        slug="consistorial-church-discipline", name="Consistorial Church Discipline", classification="supporting",
        description=(
            "At Geneva, a body of pastors and lay elders, not the civil magistrate, holds our whole "
            "population's ordinary conduct answerable to what we profess. Its own founding act - the "
            "1541 Ecclesiastical Ordinances - built the independence claim into the institution from "
            "the start, a claim the Perrinist crisis tested decades later and substantially resolved "
            "in the Consistory's own favor only by 1555. The general doctrine is Documented, Confidence "
            "A, directly in Calvin's own words; Geneva's own specific weekly operation - the actual "
            "case-by-case discipline the census itself selected this world for - rests on the still-"
            "unacquired 1541 Ordinances, Confidence E. We classify this Supporting, not Primary: real "
            "and formation-central at Geneva, but not cross-strand attested, since Zurich's own council "
            "governed church and city as one body from the start and built no comparable institution."
        ),
        manifestations=[
            "Calvin's Institutes IV.3.8: 'seniors selected from the people to unite with the bishops in pronouncing censures'",
            "the council's own attempt to claim authority over who might come to the Lord's table - and the Consistory's own refusal to yield it",
            "the Perrinist crisis, resolved substantially in the Consistory's own favor by 1555",
        ],
        relations=[
            {"type": "tension-with", "target": "rzg.term.consistory"},
        ],
    ),
    dict(
        slug="council-led-authority-vs-consistorial-independence",
        name="[TENSIONAL] Council-Led Civic Authority (Zurich) vs. Consistorial Independence from Civil Control (Geneva)",
        classification="tensional",
        description=(
            "We have never agreed, between our own two cities, who holds the final word over church "
            "discipline. Zurich's council has governed church and city as one body from our first days "
            "to our last. Geneva's own Consistory fought for, and only by 1555 substantially won, an "
            "independence from that same kind of magistrate's claim. Both poles are founded "
            "independently - Zurich's in 1519, Geneva's own Consistory in 1541 - twenty-two years "
            "apart, by two different founding acts that never had occasion to converge. We have not "
            "found the place where these become one arrangement, and we have not needed to: each city "
            "holds its own legitimate answer to the same underlying question, and this world's own "
            "life never converged on Zurich's own side within our own construction window. The wider "
            "Reformed world's later convergence toward a Geneva-influenced pattern is a fact about our "
            "own descendants, not about Zurich and Geneva as we actually stood."
        ),
        manifestations=[
            "Zurich's council governing church and city as one body, unbroken, 1519 to 1650",
            "Geneva's own Consistory, founded 1541, fighting to stay independent of civil-council control",
            "the Perrinist crisis (resolved 1555), the sharpest, most concentrated test of Geneva's own pole",
        ],
        relations=[
            {"type": "tension-with", "target": "rzg.term.consistory"},
        ],
    ),
    dict(
        slug="zwinglis-remembrance-reading-vs-negotiated-consensus",
        name="[TENSIONAL] Zwingli's Own 'Remembrance' Reading of the Supper vs. the Negotiated Spiritual-Presence Consensus",
        classification="tensional",
        description=(
            "We hold two things together without ever fully reconciling them. Our own founder at "
            "Zurich once called the Supper nothing more than a remembrance and assurance of what "
            "Christ had already done (Sixty-Seven Articles, Art. XVIII, 1523). Our two cities later "
            "signed a fuller word together - the Consensus Tigurinus's own 9th Head of Agreement "
            "(1549) - holding that we do not disjoin the reality from the signs, that Christ is truly "
            "given by the Spirit to whoever receives him believing. Whether the later formula deepens "
            "the earlier one or merely stands beside it in careful language neither city could refuse, "
            "we cannot say with certainty. We carry both, because both are true of our own record, "
            "without needing to decide which one finally speaks for us."
        ),
        manifestations=[
            "the Sixty-Seven Articles, Art. XVIII (1523): 'the mass is not a sacrifice, but is a remembrance'",
            "the Consensus Tigurinus's own 9th Head of Agreement (1549), signed two decades later, by both cities together",
            "the Marburg Colloquy (1529), the doctrinal context that pressed, over twenty years, toward a joint answer",
        ],
        relations=[
            {"type": "tension-with", "target": "rzg.term.the-lords-supper-spiritual-presence"},
            {"type": "tension-with", "target": "rzg.term.memorial-commemoration"},
            {"type": "associated-with", "target": "rzg.contested.zwinglis-remembrance-vs-negotiated-consensus"},
        ],
    ),
]

# ----------------------------------------------------------------- forces ---
# Each entry: matrix_cell (determines kind: 1x/2x/3x -> initiating/ongoing/ending),
# name, description (Layer 1 + Layer 3, third-person historical/analytical register
# matching don's own force.description precedent), manifestations (Layer 2's own
# inhabited first-person lines where the force's own entry carries one).
FORCES: list[dict] = [
    dict(slug="late-medieval-sacramental-clerical-order", cell="1A", name="The late-medieval Latin sacramental and clerical order",
         description=(
             "The late-medieval Western church's own sacramental system - the Mass as a repeated "
             "propitiatory sacrifice, image veneration, a clerical hierarchy claiming sole mediating "
             "authority - was the inherited ecclesial order this world and Lutheran Wittenberg both "
             "contested, read here through the Swiss Confederacy's own decentralized city-state "
             "structure rather than a princely territorial settlement. Documented. This is the deep "
             "external root of G2, the specific system its own Supper doctrine is built in refusal of, "
             "and, at one remove, of G3, the method that licensed testing the inherited order at all."
         ),
         manifestations=["a repeated sacrifice where Christ himself declared his own offering finished, once", "images bowed to where nothing in Scripture licensed it"]),
    dict(slug="augustinian-inheritance-predestination-grace", cell="1A", name="The Augustinian inheritance on predestination and grace",
         description=(
             "Calvin's own Institutes draws explicitly and heavily on Augustine's anti-Pelagian "
             "writings for total depravity, unconditional election, and irresistible grace - Calvin "
             "named Augustine his primary authority next to Scripture itself. A direct theological "
             "line across eleven centuries with no institutional continuity: influence, not identity. "
             "Documented as this world's own inherited theological antecedent. This force grounds G1 "
             "directly, as an inherited theological line rather than a local invention, distinct from "
             "and prior to Zurich's and Geneva's own two local origins."
         ),
         manifestations=["Augustine saw it first against Pelagius, and we see it again now, against a church that has let it grow faint"]),
    dict(slug="zwinglis-1519-preaching-sausage-affair", cell="1B", name="Zwingli's 1519 preaching decision and the 1522 Sausage Affair (Zurich's own origin)",
         description=(
             "Zwingli began continuous, book-by-book scriptural exposition at Zurich's Grossmunster "
             "from 1519, rather than following the fixed lectionary; the 1522 Sausage Affair (a public "
             "Lenten-fast violation Zwingli defended on scriptural grounds) catalyzed open civic "
             "reform, leading to the First Zurich Disputation (1523). Documented. This is the deep "
             "root of G3's own Zurich-strand enactment, and through it, of G1 and G2 as Zwingli's own "
             "1523 and 1527 writings first state them. Also the founding root of T1's own Zurich pole, "
             "and indirectly of the 1525 Anabaptist schism, which breaks from this same circle."
         ),
         manifestations=["Scripture read continuously, book by book, not cut into a fixed year's own lectionary", "whatever the text does not say, the church may not require"]),
    dict(slug="genevas-1526-bern-alliance-1536-break-calvins-arrival", cell="1B", name="Geneva's 1526 Bern alliance, 1536 break from Savoy, and Calvin's arrival (Geneva's own origin)",
         description=(
             "Geneva's 1526 alliance with Bern and Fribourg and its 1536 political break from Savoy "
             "and the Prince-Bishop created the civic opening; Calvin arrived the same year, was "
             "exiled to Strasbourg (1538-1541), and was recalled to consolidate the 1541 Ecclesiastical "
             "Ordinances. Documented, five years after Zwingli's death, with no contact between the "
             "two triggers. This is the deep root of G3's own Geneva-strand enactment, and through "
             "Calvin's own systematic elaboration, of G1's own fullest worked form and G2's own mature "
             "doctrine. Also the direct precondition for the 1541 Ordinances and, through them, of G4 "
             "and T1's own Geneva pole."
         ),
         manifestations=["a church is not rightly ordered by doctrine alone - someone must watch how the doctrine is lived"]),
    dict(slug="1541-ecclesiastical-ordinances-consistory-founding", cell="1B", name="The 1541 Ecclesiastical Ordinances and the founding of the Consistory",
         description=(
             "Calvin's 1541 recall to Geneva produced the Ecclesiastical Ordinances, creating a "
             "Consistory of pastors and lay elders with disciplinary censure authority, structurally "
             "distinct from a body answerable to the civil council alone. Documented as general "
             "doctrine, Confidence A, directly in Calvin's own words; Geneva's own specific 1541 "
             "institutional text remains unvendored, Confidence E. This is the specific institutional "
             "founding act behind G4 and the founding moment of T1's own Geneva pole - an "
             "independence claim built into the institution from its own origin, tested decades on by "
             "the Perrinist crisis rather than invented by it."
         ),
         manifestations=["the magistrate governs bodies and property; he does not sit in judgment on whether a soul may come to the Lord's own table"]),
    dict(slug="marburg-colloquy", cell="2A", name="The Marburg Colloquy (1529)",
         description=(
             "At Marburg (1-4 October 1529), Zwingli and Oecolampadius stood against Luther and "
             "Melanchthon over whether Christ's body is locally or corporeally present in the Supper; "
             "Calvin, then about twenty and a law student, was not present, and Geneva was not yet "
             "reformed. Documented. This is the specific rupture separating G2's own refusal of "
             "Wittenberg from its own earlier, shared refusal of Rome, and the direct trigger, twenty "
             "years on, for the Consensus Tigurinus."
         ),
         manifestations=["the bread is bread, and the body is in heaven", "what happens at this table is remembrance and thanksgiving, not another sacrifice repeated"]),
    dict(slug="wars-of-kappel-zwinglis-death", cell="2A", name="The Wars of Kappel (1529, 1531) and Zwingli's death",
         description=(
             "The First War of Kappel (1529) was resolved without battle; the Second War of Kappel "
             "(1531) killed Zwingli himself, fought between Reformed and Catholic Swiss cantons over "
             "the Confederacy's own decentralized cantonal structure making reform a city-by-city "
             "political decision. Documented. This force removes Zurich's own founding voice from the "
             "ongoing life of the movement he began - the direct precondition for Bullinger's own "
             "forty-four-year pastorate and, through it, the Second Helvetic Confession, a fixed text "
             "written because a founding generation's own oral method needed to outlive its founder."
         ),
         manifestations=["our own pastor was killed in that same fighting", "reform here was never a private conviction sheltered from the world's own violence"]),
    dict(slug="genevas-refugee-inflow-bernese-dependence", cell="2A", name="Geneva's refugee inflow and Bernese dependence",
         description=(
             "Geneva became a print and refugee center over this window, sheltering French Huguenots "
             "and, under Mary I, English Marian exiles, while remaining dependent on Bernese support "
             "in ways that both stressed and internationalized the city. Documented. This is the "
             "direct external pressure G4's own weekly Consistory discipline was specifically built to "
             "address - genuine civic disorder and moral laxity arising in real part from sustained "
             "refugee inflow, not from Geneva's own settled population alone."
         ),
         manifestations=["every new household arriving under threat is one more soul this city's own discipline must answer for"]),
    dict(slug="counter-reformation-sustained-pressure", cell="2A", name="The Counter-Reformation as sustained external pressure",
         description=(
             "Catholic pressure was sustained across the whole window: the Jesuits, founded 1540, "
             "established at Fribourg from 1580, directly facing Reformed Bern and Geneva; the 1590s "
             "Catholic reconquest of the Chablais was fought on Geneva's own doorstep. Documented as "
             "to its own named episodes. (Michael Servetus's 1553 execution is a separate, sharper "
             "episode scoped to a different registered world and not treated here.) This force "
             "sustains the Rome-facing refusal across the entire window without ever converting into "
             "a world-ending event."
         ),
         manifestations=["Rome did not simply lose this ground once and withdraw; it kept pressing at the edge of what we had won"]),
    dict(slug="synod-of-dort-international-dimension", cell="2A", name="The Synod of Dort's international Reformed dimension (1618-19)",
         description=(
             "The Synod of Dort seated an international Reformed delegation, including, per standard "
             "historiography and not yet independently verified against a primary vendored source, "
             "delegates from Geneva and the Swiss Reformed cantons - meaning, if this holds, both our "
             "own confirmed strands were represented in person. Confirmed by the project lead as part "
             "of this world's own transmission; the specifically Dutch domestic controversy remains a "
             "separate world's own future content. This force sharpens rather than closes G1, via "
             "Beza's own doctrinal throughline, at one remove - it transmits forward rather than "
             "closing anything, thirty-two years before the window's own 1650 close."
         ),
         manifestations=["what was decided at Dort was not a new question; it was the same conviction about God's own free election, pressed to its sharpest statement yet"]),
    dict(slug="anabaptist-schism", cell="2B", name="The Anabaptist schism (1525)",
         description=(
             "The first Swiss Brethren baptisms (21 January 1525), at Felix Manz's own house in "
             "Zurich - Conrad Grebel baptizing Georg Blaurock, who then baptized the others present, "
             "including Manz - split this world's own founding community from within, only two years "
             "after the First Zurich Disputation. Grebel and Manz were both formerly of Zwingli's own "
             "reform circle. Documented. This force tests G3's own scriptural method against a rival "
             "reading from inside - a direct continuation of Zwingli's own 1519 origin, not an "
             "unrelated contemporary movement."
         ),
         manifestations=["some among us read the same Scripture and heard the same doctrine - and where we stopped, they went further", "we do not deny they read Scripture; we deny they read it whole"]),
    dict(slug="consensus-tigurinus-force", cell="2B", name="The Consensus Tigurinus (1549)",
         description=(
             "In 1549, Zurich's own ministers and Geneva's own Calvin put their names to a single "
             "jointly-negotiated formula on the Supper neither city had used alone before. Documented, "
             "verified verbatim: 'Wherefore, though we distinguish, as we ought, between the signs and "
             "the things signified, yet we do not disjoin the reality from the signs.' This is the "
             "direct textual bridge across the strand divide our two origins opened - the one document "
             "in this world's entire corpus literally co-authored across the boundary - and the second "
             "pole of T2, resolving that tension in text without settling whether it is genuine "
             "synthesis or diplomatic elasticity."
         ),
         manifestations=["we do not divide the sign from the thing it signifies", "Christ's own promise, received in faith, is truly given here - not carnally, but by the Spirit's own power"]),
    dict(slug="bolsec-controversy", cell="2B", name="The Bolsec controversy (1551)",
         description=(
             "Jerome Bolsec publicly challenged Calvin's own predestination doctrine at Geneva in "
             "1551, a live pastoral and disciplinary crisis over the doctrine's own content. "
             "Documented. This is the direct trigger that tests G1 as a live, contested pastoral "
             "question rather than settled doctrine alone."
         ),
         manifestations=["to question this doctrine publicly is to ask whether the comfort this church offers its own people is true or merely asserted"]),
    dict(slug="perrinist-crisis", cell="2B", name="The Perrinist crisis (resolved 1555)",
         description=(
             "The Perrinist faction inside Geneva contested the Consistory's own independence from "
             "civil-council control; the fight was substantially resolved in Calvin's favor only by "
             "1555. Documented. This is the direct test of the 1541 Ordinances' own founding "
             "independence claim, and the specific episode constituting T1's own Geneva pole in its "
             "sharpest, most concentrated ongoing-internal form."
         ),
         manifestations=["when the council's own men tried to claim that authority for themselves, the Consistory did not yield it", "a discipline answerable to the city's own shifting politics is no discipline at all"]),
    dict(slug="second-helvetic-confession-heidelberg-catechism", cell="2B", name="The Second Helvetic Confession (1566) and the Heidelberg Catechism (1563)",
         description=(
             "Bullinger's Second Helvetic Confession (1566), written decades after Zwingli's death, "
             "and the Heidelberg Catechism (1563, a third, non-Zurich/non-Geneva Reformed voice from "
             "the German wing), together fix this movement's shared confessional core in transmissible "
             "written form. Documented. This is the specific mechanism behind our own Memory "
             "Structures - textual codification by a named successor once a founding generation's own "
             "oral method needed a fixed text to outlive it, matching the same succession-proofing "
             "role Beza's own Tabula praedestinationis (1555) performs for Geneva."
         ),
         manifestations=["a confession is not written to say something new; it is written so that what is already believed can be tested, taught, and handed to the next generation without drift"]),
    dict(slug="transmission-author-gravity-genre-asymmetries", cell="2B", name="Transmission - the Author-Gravity and genre asymmetries within this world's own self-transmission",
         description=(
             "This world's own record transmitted itself through its own tradition's continuing "
             "institutional life, not through a hostile party's own refutation literature. Within that "
             "self-transmission, two distinct asymmetries hold: Calvin's own vendored corpus is "
             "roughly four times Zwingli's by volume; and institutional daily-practice material (the "
             "1541 Ordinances, the Genevan Psalter, Geneva's own consistory registers) remains almost "
             "entirely unvendored for both cities alike. Documented as this world's own central "
             "evidentiary condition. This transmission pattern is the specific mechanism behind G1's "
             "own Confidence/Gravity Cross-Check divergence - the asymmetry is a fact about what "
             "survived to be copied and reprinted, not about which strand held the doctrine more "
             "centrally."
         ),
         manifestations=["our own record does not reflect on its own future survival directly - no surviving voice narrates which of its own texts it expected to outlast it"]),
    dict(slug="no-external-ending-force", cell="3A", name="No external ending force attested within the window",
         description=(
             "No external force closes this world within its own 1519-1650 construction window. The "
             "window's own 1650 close is the census's own administrative continues-cap for a still-"
             "living tradition, not a historical rupture. Documented as an honest finding, not an "
             "inferred absence. This distinguishes this world sharply from this project's own "
             "Donatism precedent, where two external forces jointly close that world's window - here, "
             "the Counter-Reformation's own sustained pressure across the whole window never converts "
             "into a comparable closing event. This world's own gravities continue, unbroken, into "
             "four descendant traditions: the Scottish Kirk, the Huguenots, the Dutch Reformed, and "
             "English Puritanism."
         ),
         manifestations=["what continues is continuation, not survival of a closed thing"]),
    dict(slug="no-internal-fracture", cell="3B", name="No internal fracture closes this world within the window",
         description=(
             "No internal fracture closing this world is attested within the window. The Zurich/"
             "Geneva relationship is confirmed as one world, two strands, not a fracture into two; "
             "T1's own permanent, within-window non-convergence is a held tension, not a rupture. "
             "Documented. This finding is what makes T1 a genuine Tensional gravity rather than a "
             "resolved historical episode - its own permanent non-convergence is itself the finding, "
             "not a gap in this document's own knowledge."
         ),
         manifestations=["we were never one city, and we never pretended to be", "we remain what we always were: one faith, arrived at twice"]),
    dict(slug="selective-reception-four-descendant-traditions", cell="3B", name="Transmission - selective reception by four descendant traditions",
         description=(
             "This world's own gravities transmit, unbroken, into four named descendant traditions: "
             "the Scottish Kirk, the Huguenots, the Dutch Reformed, and English Puritanism. Documented "
             "as this world's own named transmission scope; the specific selective mechanism by which "
             "each descendant tradition received which parts of this world's own doctrine is not "
             "independently traced beyond the Beza/Dort throughline. This is the specific transmission "
             "dimension the Author-Gravity asymmetry prepares: the same volume asymmetry that shapes "
             "what this construction can know about Zwingli versus Calvin is also what shapes which "
             "strand's own systematized doctrine the descendant traditions primarily inherit."
         ),
         manifestations=[]),
]

CELL_TO_KIND = {"1A": "initiating", "1B": "initiating", "2A": "ongoing", "2B": "ongoing", "3A": "ending", "3B": "ending"}

GRAVITY_FORCE_LINKS = {
    "sovereignty-of-god-predestination-election": [
        "augustinian-inheritance-predestination-grace", "bolsec-controversy",
        "second-helvetic-confession-heidelberg-catechism",
        "transmission-author-gravity-genre-asymmetries", "synod-of-dort-international-dimension",
    ],
    "spiritual-presence-rejection-of-corporeal-sacrificial-mediation": [
        "late-medieval-sacramental-clerical-order", "zwinglis-1519-preaching-sausage-affair",
        "marburg-colloquy", "consensus-tigurinus-force",
    ],
    "scripture-sole-authority-disputation-catechesis": [
        "zwinglis-1519-preaching-sausage-affair", "genevas-1526-bern-alliance-1536-break-calvins-arrival",
        "anabaptist-schism", "second-helvetic-confession-heidelberg-catechism",
    ],
    "consistorial-church-discipline": [
        "genevas-1526-bern-alliance-1536-break-calvins-arrival", "1541-ecclesiastical-ordinances-consistory-founding",
        "genevas-refugee-inflow-bernese-dependence", "perrinist-crisis",
    ],
    "council-led-authority-vs-consistorial-independence": [
        "zwinglis-1519-preaching-sausage-affair", "1541-ecclesiastical-ordinances-consistory-founding",
        "perrinist-crisis", "no-internal-fracture",
    ],
    "zwinglis-remembrance-reading-vs-negotiated-consensus": [
        "zwinglis-1519-preaching-sausage-affair", "marburg-colloquy", "consensus-tigurinus-force",
    ],
}


def emit_gravity(g: dict) -> Path:
    rid = f"rzg.gravity.{g['slug']}"
    force_targets = [f"rzg.force.{fs}" for fs in GRAVITY_FORCE_LINKS[g["slug"]]]
    relations = list(g["relations"]) + [{"type": "associated-with", "target": t} for t in force_targets]
    payload = {
        "id": rid, "world_id": WORLD_ID, "record_type": "gravity", "schema_version": SCHEMA_VERSION,
        "status": "draft", "register": "emic", "canon_cells": [],
        "confidence": {
            "citation_specificity": "A", "verification_state": "verified-direct",
            "evidentiary_weight": "load-bearing", "formation_confidence": "Documented",
            "divergence_note": None,
        },
        "sources": [], "relations": relations,
        "name": g["name"], "description": g["description"],
        "manifestations": g["manifestations"], "classification": g["classification"],
    }
    path = OUT_ROOT / "gravity" / f"{rid}.md"
    body = (
        "Built from Doc_04_Gravity_Discovery.md SS3 (Approved to proceed, Revision 2), carrying that "
        "document's own classification and reasoning directly. `relations` mirrors Doc_08 Section 5's "
        "own 'Connected forces' list for this gravity exactly, per that document's own explicit caution "
        "against force-fitting a connection its own words do not support."
    )
    _write(path, payload, body)
    return path


def emit_force(f: dict, *, gravity_targets: list[str]) -> Path:
    rid = f"rzg.force.{f['slug']}"
    payload = {
        "id": rid, "world_id": WORLD_ID, "record_type": "force", "schema_version": SCHEMA_VERSION,
        "status": "draft", "register": "emic", "canon_cells": [],
        "confidence": {
            "citation_specificity": "A", "verification_state": "verified-direct",
            "evidentiary_weight": "load-bearing", "formation_confidence": "Documented",
            "divergence_note": None,
        },
        "sources": [], "relations": [{"type": "associated-with", "target": t} for t in gravity_targets],
        "name": f["name"], "kind": CELL_TO_KIND[f["cell"]],
        "description": f["description"], "manifestations": f["manifestations"],
        "matrix_cell": f["cell"],
    }
    path = OUT_ROOT / "force" / f"{rid}.md"
    body = (
        "Built from Doc_08_Forces_Document.md Section 3 (Approved to proceed, Revision 2), carrying "
        "that force's own Layer 1 (Historical Event) and Layer 3 (Formation Impact) into `description`, "
        "and Layer 2 (World's Own Experience) into `manifestations` where the force's own entry carries "
        "one - several of these are themselves marked [Inhabited] in Doc_08's own text, carried verbatim "
        "from Doc_05, not freshly composed here."
    )
    _write(path, payload, body)
    return path


def main() -> int:
    written = [emit_gravity(g) for g in GRAVITIES]

    force_to_gravities: dict[str, list[str]] = {}
    for gravity_slug, force_slugs in GRAVITY_FORCE_LINKS.items():
        for fs in force_slugs:
            force_to_gravities.setdefault(fs, []).append(f"rzg.gravity.{gravity_slug}")
    force_to_gravities.setdefault("anabaptist-schism", []).append("rzg.contested.anabaptist-schism-legitimacy")
    written += [emit_force(f, gravity_targets=force_to_gravities.get(f["slug"], [])) for f in FORCES]

    assert len(GRAVITIES) == 6, "expected 3 Primary + 1 Supporting + 2 Tensional = 6"
    assert len(FORCES) == 19, "expected all 19 forces from Doc_08's own Force Index"
    force_slugs = [f["slug"] for f in FORCES]
    assert len(force_slugs) == len(set(force_slugs)), "duplicate force slug"

    for p in written:
        print(p.relative_to(REPO_ROOT))
    print(f"\n{len(written)} records written ({len(GRAVITIES)} gravity + {len(FORCES)} force).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
