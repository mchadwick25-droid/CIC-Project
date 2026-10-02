"""B-2 + B-3 (S2.2/S2.3): Reformed Cities (rzg) term records - the full
19-candidate lexicon roster, minus the two reserved-merged slots (17
distinct term records).

WHY ONE SCRIPT, NOT TWO, AND WHY 17 NOT 6. Following don's own precedent
(wb_don_s22_s23.py, read in full before this script was written) exactly:
B-2 ("mechanical lexicon split") and B-3 ("full term authoring") collapse
into one pass because the source material's own shape collapses them. For
the 6 confirmed Tier-1 deployment chunks (Lexicon-Chunks/rzglexNNN_*.md,
covering 8 candidate terms via 2 disclosed merges), the chunk IS most of
the authoring work - converting its own sections onto the live schema plus
confidence blocks and relations is what remains. For the other 11
candidates, Doc_06 explicitly deferred their own deployment-chunk
production ("disclosed future work", Doc_06 SS0/SS5) - but Doc_03's own
candidate roster (SS1) already gives each one a real one-line world-meaning,
tier, strand, tags, and AG-risk flag, cross-checked against Doc_04's and
Doc_06's own later confirmations. Building all 17 as term records now,
rather than leaving 11 as a silent gap, matches don's own reasoning
exactly: "there is no B-2 mechanical source at all... so building them is
pure B-3 authoring from Doc_03's own candidate-list content, done here
rather than left as a silent 14-term gap." rzglex002 (Election) and
rzglex009 (Spiritual Presence) are RESERVED, NOT REUSED per Doc_06 SS1's
own explicit numbering rule - both merged into rzglex001 and rzglex007
respectively - so 19 candidates minus these 2 reserved slots = 17 term
records, not 19.

INPUTS, mapped to OUTPUTS, precisely:
  - Lexicon-Chunks/rzglex001/004/005/007/008/012_*.md (read in full this
    session) -> the 6 rich term records, each carrying that chunk's own
    Quick Meaning, World Meaning, Ecological Function, Distortion Risk,
    and Key Sources sections, converted onto the schema's own fields
    (plain_meaning, senses.{informational,evidential,personal,
    translational}, quick_meaning, distortion_risk, false_friend).
  - Doc_03_Lexicon_Candidate_List.md SS1 (Candidate Roster, 19 candidates
    in 6 clusters) -> the 11 thin term records (Providence, The Sixty-Seven
    Articles, Memorial/Commemoration, Mutual Consent, Excommunication,
    Antistes, Elder, Catechism, Confession, Heads of Agreement,
    Reformation), each built from that candidate's own "One-line
    world-meaning" cell, tier, strand, tags, and AG-risk column - genuinely
    thinner than the 6 chunked terms (no per-term Key Sources research
    pass was run for these 11; citations below are the same ones Doc_03
    itself already names for each candidate, never a fresh citation this
    script invents).
  - Doc_06_Full_Lexicon_Development.md SS1 (Tier Confirmation table) ->
    confirms every term's own final tier and the two merge/promotion
    decisions, cross-checked against Doc_03's own preliminary tiers.

READABILITY: every plain_meaning/quick_meaning field below was checked
against engine.m1.fk.fk_grade before this script was finalized (FK ceiling
10, the same scorer gate_readability uses) - confirmed by the gate run
after this script's own first execution, not assumed in advance.

VOICE: all spoken fields (senses.informational/evidential/personal/
translational, plain_meaning, quick_meaning) are written in this world's
own "we/our" emic register throughout, per gate_voice_perspective's own
scan of exactly these term fields.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[4]
OUT_ROOT = REPO_ROOT / "records" / "rzg"

WORLD_ID = "the-reformed-cities-zurich-and-geneva"
SCHEMA_VERSION = 2


def _yaml_dump(payload: dict) -> str:
    return yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=100, default_flow_style=False)


def _write(path: Path, payload: dict, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\n" + _yaml_dump(payload) + "---\n" + body.strip() + "\n", encoding="utf-8")


# ------------------------------------------------------------- 6 rich terms
RICH_TERMS: list[dict] = [
    dict(
        slug="predestination-election",
        world_word="Predestination and Election",
        tier=1,
        false_friend=[
            "a grim, fatalistic doctrine - the idea that some people are simply doomed no matter what "
            "they do, offered as an excuse for cruelty or indifference toward the 'unchosen'",
        ],
        plain_meaning=(
            "God chose, before the world began and by his own free will alone, who would be saved. "
            "Both Zurich and Geneva held this. Geneva built it into a full system. Zurich stated it "
            "more briefly, as pastoral comfort."
        ),
        informational=(
            "Salvation does not begin with anything in the one who is saved - not our own effort, not "
            "our own foreseen faith, not anything God looked ahead and found worthy in us. It begins, "
            "entirely, in God's own free decision, made before the world existed. We call the decree "
            "itself predestination. We call the persons it names, from their own side, the elect. One "
            "of our own founders at Zurich put the whole order plainly, working through Paul's own "
            "letter to the Romans: God's election, predestination or marking out, calling, beatifies - "
            "each step follows the one before it, and none of them rests on anything we ourselves supply."
        ),
        evidential=(
            "This is not a private opinion argued only by theologians in a study. It is stated as our "
            "own church's confession, meant to comfort rather than to torment. Our own confession at "
            "Zurich says it directly: we reject those who seek out of Christ whether they are chosen, "
            "and instead point the anxious soul back to Christ himself - let Christ be the mirror in "
            "which we behold our own predestination. Geneva took the same conviction further, into a "
            "fuller architecture worked out at the length a whole systematic theology allows. The "
            "difference is not a disagreement between our two cities - it is the same doctrine, held "
            "with the same seriousness, given two different registers by two reforms that never had "
            "the chance to compare notes on how to say it."
        ),
        personal=(
            "We do not hold this as a cold decree to fear. We hold it as the ground under a settled "
            "life - the reason we need not examine our own conscience for proof of standing. Whoever "
            "is joined to Christ by true faith already has, in that very faith, the only evidence of "
            "election anyone is given or needs."
        ),
        translational=(
            "This is not a doctrine of doom but of comfort: since our salvation was never something we "
            "could lose by our own failure, it was never something we earned by our own success either. "
            "Our own confession states this pastoral intent directly. The doctrine's own harder, more "
            "systematized edges are a later, largely Calvin- and Beza-specific development, not the way "
            "either city's founders first stated the conviction."
        ),
        distortion_risk="high",
        quick_meaning=(
            "God has, from eternity and by his own free choice alone, decided who will be saved. Both "
            "Zurich and Geneva held this. Geneva's Calvin worked it into a full system. Zurich's "
            "founders stated it more briefly, and pastorally."
        ),
    ),
    dict(
        slug="disputation",
        world_word="Disputation",
        tier=1,
        false_friend=[
            "a formal academic debate, or a piece of political theater - a staged event whose outcome "
            "was likely settled beforehand, since councils rarely reverse the powerful",
        ],
        plain_meaning=(
            "A Disputation was a public debate held before Zurich's own city council. Our reforming "
            "side defended its case from Scripture. The old church's side answered. This is how Zurich "
            "actually decided to reform - not a private argument, a civic one."
        ),
        informational=(
            "Reform here did not begin with a bishop's decree or a prince's command. It began with a "
            "public test: let the case be argued, before the city's own council and its own citizens, "
            "from Scripture alone, and let whichever side cannot answer from Scripture yield. This is "
            "what happened twice in 1523 - first in January, then again in October - and both times "
            "the council itself judged the outcome and acted on it."
        ),
        evidential=(
            "Our own founder confessed at the first of these that everything he had preached in the "
            "city rested on Scripture, and offered, in his own words, to be taught better himself, but "
            "only from that same Scripture, if he had misunderstood it anywhere. This is not a "
            "formality staged to bless a decision already made elsewhere. The council's own judgment at "
            "these disputations is the actual mechanism by which images were removed, the Mass "
            "eventually abolished, and our reformed order established in law."
        ),
        personal=(
            "We trust an argument tested this way the way another might trust a document sealed and "
            "witnessed. It set the pattern our later confrontations - with the Anabaptists, with the "
            "Catholic cantons - repeatedly returned to as the way a contested question gets settled "
            "among us."
        ),
        translational=(
            "This was not theater dressed around a foregone conclusion. It was the specific civic-"
            "scriptural test we trusted to settle a real question, because the council's own judgment, "
            "reached this way, is what we took reform's own legitimacy to require."
        ),
        distortion_risk="medium",
        quick_meaning=(
            "A public, formal debate before Zurich's own city council. Our reforming side defended "
            "its scriptural case against the old church's defenders. This is how Zurich's reform was "
            "actually decided."
        ),
    ),
    dict(
        slug="sola-scriptura",
        world_word="Sola Scriptura",
        tier=1,
        false_friend=[
            "a slogan about individual Bible-reading, implying each believer simply decides doctrine "
            "for themselves from personal study, without an authoritative church structure at all",
        ],
        plain_meaning=(
            "Scripture alone, not church tradition or a pope's decree, settles what we believe and how "
            "we govern our churches. Zurich tested this in public debate. Geneva built it up through "
            "sustained teaching. Both cities held the same conviction."
        ),
        informational=(
            "Whatever Scripture will not yield, the church has no standing to require. Whatever it "
            "does yield, no pope, council, or inherited custom may set aside. This is not one doctrine "
            "among others in our own teaching - it is the method by which every other doctrine here is "
            "tested and defended. Our own founder at Zurich confessed it plainly at the very outset of "
            "his own public case: everything he preached rested on Scripture, and he offered to be "
            "corrected, but only from that same Scripture."
        ),
        evidential=(
            "Our two cities enacted this one conviction through two different instruments, and the "
            "difference is worth naming rather than smoothing over. At Zurich, it took the shape of "
            "public disputation. At Geneva, it took the shape of sustained, systematic instruction - "
            "doctrine built book upon book, catechism taught to the whole population. Neither city "
            "borrowed the other's own method. Both arrived, independently, at the same governing "
            "principle."
        ),
        personal=(
            "A claim only counts as scripturally grounded, to us, if it can be defended, publicly and "
            "specifically, against the actual text - at Zurich, literally in open disputation; at "
            "Geneva, through sustained catechetical instruction answerable to our own trained pastoral "
            "body."
        ),
        translational=(
            "This is not private interpretation but a public, testable standard. The individual "
            "conscience is bound by Scripture, but the testing of what Scripture teaches was never a "
            "private act in either of our cities."
        ),
        distortion_risk="medium",
        quick_meaning=(
            "Scripture alone, not church tradition or a pope's decree, is the final authority for our "
            "doctrine and our civic order. Zurich enacted this through public debate; Geneva enacted it "
            "through sustained teaching. Both cities hold the same conviction."
        ),
    ),
    dict(
        slug="the-lords-supper-spiritual-presence",
        world_word="The Lord's Supper and Spiritual Presence",
        tier=1,
        false_friend=[
            "a minor liturgical or theological technicality - a dispute over whether communion bread "
            "is 'really' the body of Christ that modern ears, used to treating such questions as "
            "symbolic by default, are likely to find hard to take seriously",
        ],
        plain_meaning=(
            "We refuse two claims about the Lord's Supper. It does not repeat Christ's own sacrifice. "
            "His body does not sit physically inside the bread. What we affirm took two cities and a "
            "1549 agreement to state together: Christ is truly given, by the Spirit, to whoever "
            "receives him believing."
        ),
        informational=(
            "Christ, having sacrificed himself once, is a sacrifice sufficient for eternity - so the "
            "Mass is not a sacrifice, but a remembrance of the sacrifice, and any priest who claims to "
            "offer Christ again has mistaken what was actually accomplished at the cross. We also "
            "refuse that Christ's own body could be chewed by the mouth or located within the bread "
            "and wine."
        ),
        evidential=(
            "What we affirm took longer to state, and our two cities did not begin by saying it the "
            "same way. Zurich's own earlier reading held the Supper chiefly as remembrance of what "
            "Christ had already done. Geneva's own developed doctrine went further: Christ's own body "
            "and blood are truly, though not physically, given to believers, by the Spirit's own power, "
            "received by faith. In 1549, both cities put their names to a single formula neither had "
            "used alone before: though we distinguish, as we ought, between the signs and the things "
            "signified, yet we do not disjoin the reality from the signs."
        ),
        personal=(
            "We held the tension between Zwingli's own earlier, sharper reading and the negotiated "
            "Consensus without ever fully settling, in our own words, how much the later formula "
            "actually changed the earlier one. We carry both, because both are true of our own record."
        ),
        translational=(
            "This is the single sharpest doctrine separating us from both of our own rivals at once - "
            "Rome on one side, Wittenberg on the other - carrying the weight of what kind of God we "
            "believe in: one who does not need a repeated sacrifice, and whose Son's own body is not "
            "confined to a location on a table."
        ),
        distortion_risk="medium",
        quick_meaning=(
            "Our own sharpest boundary marker. No repeated sacrifice. No body confined to bread. "
            "After real internal difference, and a 1549 deal, we hold that Christ is truly given by "
            "the Spirit - not merely remembered, and not physically present."
        ),
    ),
    dict(
        slug="sign-and-the-thing-signified",
        world_word="Sign and the Thing Signified",
        tier=1,
        false_friend=[
            "a precise, almost legalistic form of words - the kind of careful compromise language that "
            "suggests both sides were more interested in signing something than in genuinely agreeing",
        ],
        plain_meaning=(
            "In 1549, Zurich and Geneva agreed on exact words for the Lord's Supper. We distinguish "
            "the bread from the reality it points to. We never disjoin the two. This settled, in "
            "words, what neither city's own earlier statement had settled alone."
        ),
        informational=(
            "We do not say the bread simply is the body, the way Rome and Wittenberg, in their own "
            "different ways, both still say. But we also refuse to say the bread is merely bread, a "
            "picture with nothing behind it. Both our cities' own pastors put their names to the same "
            "careful sentence: though we distinguish, as we ought, between the signs and the things "
            "signified, yet we do not disjoin the reality from the signs. Faith receives, truly, what "
            "the sign points to - the reality itself, given by the Spirit's own power to those who come "
            "believing."
        ),
        evidential=(
            "This sentence did not exist before 1549, in exactly this form, in either city's own prior "
            "confession. It is the specific language the Consensus Tigurinus was negotiated to produce, "
            "and its own two signatories - the Ministers of the Church of Zurich, and John Calvin, "
            "Minister of the Church of Geneva - stood behind it together, each recognizing in the "
            "other's own confession something they could not disown as their own."
        ),
        personal=(
            "Whether this formula is a genuine theological synthesis or a diplomatically elastic form "
            "of words is a live contest we do not settle ourselves. But we did not treat it as empty "
            "diplomacy when we signed it. It was the specific, hard-won language each side judged it "
            "could actually mean, not merely sign."
        ),
        translational=(
            "That very suspicion - that this was more compromise than conviction - is a real, "
            "unresolved question about our own record, not one we can wave away. What we can say is "
            "that neither side treated the words as empty."
        ),
        distortion_risk="high",
        quick_meaning=(
            "The exact words both our cities agreed to in 1549. We distinguish the bread from the "
            "reality it points to, but never separate the two. Whether this was real agreement or "
            "careful diplomacy is a live, unsettled question in our own record."
        ),
    ),
    dict(
        slug="consistory",
        world_word="Consistory",
        tier=1,
        false_friend=[
            "a harsh moral-surveillance body, imagined in vivid institutional detail - a court that "
            "summoned households, inspected private life, and enforced conformity street by street",
        ],
        plain_meaning=(
            "At Geneva, the Consistory is our body of pastors and lay elders. It holds our whole "
            "population's daily conduct to account. Zurich has no equivalent. Its council governs "
            "church and city directly."
        ),
        informational=(
            "Doctrine rightly taught still leaves open whether a professed believer's own daily conduct "
            "answers to what has been professed. At Geneva, someone had to ask that question directly - "
            "not the magistrate, whose office is for the body and its property, but a body of pastors "
            "and lay elders together, seniors selected from our own people to unite with the pastors in "
            "pronouncing censures and exercising discipline."
        ),
        evidential=(
            "This body, established under the 1541 Ecclesiastical Ordinances, is what made our own "
            "church government presbyterian rather than purely clerical: laypeople, not only ordained "
            "ministers, hold real disciplinary standing in it. The council itself tried, at points, to "
            "claim the authority to judge who might come to the Lord's own table - and we did not "
            "yield that judgment, because a discipline answerable to shifting civic politics is no "
            "discipline at all."
        ),
        personal=(
            "We fought for this independence not for our own power's sake, but because we judged a "
            "discipline that bends with the council's own mood is no real discipline. That fight was "
            "substantially won in our own favor only by 1555, a full generation after Calvin's own "
            "1541 recall."
        ),
        translational=(
            "What we cannot yet supply is our own day-to-day operation: the real case-by-case practice, "
            "what a summons before us actually involved. A vivid, specific picture of that daily "
            "operation is not something our own sources can currently support."
        ),
        distortion_risk="high",
        quick_meaning=(
            "Geneva's own body of pastors and lay elders. It holds our whole population's daily "
            "conduct to account. We can state the general doctrine plainly. Our own day-to-day case "
            "history is not yet something our sources can supply."
        ),
    ),
]

# ------------------------------------------------------------ 11 thin terms
# Built from Doc_03 SS1's own candidate roster (one-line world-meaning per
# candidate, tier/strand/tags/AG-risk), per this script's own docstring.
# Genuinely thinner than the 6 rich terms above: no dedicated per-term
# research pass or Key Sources section was run for these 11 at Doc_06 - the
# same citations Doc_03 itself already names are what ground each entry
# below, never a fresh citation this script invents.
THIN_TERMS: list[dict] = [
    dict(
        slug="providence", world_word="Providence", tier=2,
        plain_meaning=(
            "Providence is God's own continuous, active care over everything he made. He is not a "
            "distant first cause who set the world going and stepped back."
        ),
        informational=(
            "We hold that God governs every created thing, moment by moment, not merely at the "
            "beginning. This teaching stands behind our own confidence that nothing happens outside "
            "God's own care - the same ground Predestination and Election name for our own salvation "
            "specifically, applied here to the whole created order."
        ),
        evidential=(
            "Calvin's Institutes, Book I, states this doctrine at length. It is present in Zwingli's "
            "own earlier theology too, though not developed to the same degree in what our own record "
            "preserves."
        ),
        personal="We rest on this the same settled way we rest on our own election: not as a fact we prove, but as a ground we stand on.",
        translational="This is not a claim that God micromanages every detail for a hidden reason we could discover. It is our own confidence that nothing escapes his care.",
        false_friend=["a fatalistic claim that nothing anyone does matters, since God has already fixed every outcome in advance"],
        distortion_risk="medium",
        quick_meaning="God's own continuous, active governing of everything he made - not a distant first cause, but ongoing care.",
    ),
    dict(
        slug="sixty-seven-articles", world_word="The Sixty-Seven Articles", tier=3,
        plain_meaning=(
            "The Sixty-Seven Articles are Zwingli's own founding statement of doctrine. He presented "
            "them at the First Zurich Disputation, in 1523."
        ),
        informational=(
            "This is the specific document our founder defended, article by article, before Zurich's "
            "own city council - the text that made the Disputation something more than an open-ended "
            "conversation. It is a document, distinct from the general practice of holding a "
            "disputation itself."
        ),
        evidential="The Articles' own text survives within the Acts of the First Zurich Disputation, in our own vendored record.",
        personal="We point to this document, not a summary of it, when someone asks what our founder actually claimed at the outset.",
        translational="This is not a creed written by a committee over years. It is one man's own confession, tested in public the same year it was written.",
        false_friend=["a later, polished confession comparable to the Second Helvetic Confession, rather than a first, urgent public statement"],
        distortion_risk="low",
        quick_meaning="Zwingli's own founding doctrinal statement. He presented and defended it at the First Zurich Disputation, in 1523.",
    ),
    dict(
        slug="memorial-commemoration", world_word="Memorial / Commemoration", tier=2,
        plain_meaning=(
            "This is Zwingli's own earlier, sharper teaching. The Lord's Supper chiefly remembers "
            "what Christ already did. It does not, on this reading, communicate his body further."
        ),
        informational=(
            "Our own founder's earliest statement holds the Supper as a remembrance and an assurance of "
            "the salvation Christ has already given - not itself the place where something new is "
            "communicated. The Consensus Tigurinus, agreed decades later, states our doctrine more "
            "fully. Whether that later statement preserves this earlier one or changes it, we do not "
            "settle for good."
        ),
        evidential="Zwingli's own Sixty-Seven Articles, Article XVIII, states this position directly: the Mass 'is not a sacrifice, but is a remembrance of the sacrifice.'",
        personal="We carry both readings - Zwingli's earlier word and the Consensus's fuller one - because both are genuinely ours, and we have not found the place where they become one thing.",
        translational="This is not a rejection of Christ's own real gift to us. It is our own earliest, sharpest way of refusing to say more than we believed the text actually gave us.",
        false_friend=["an empty ceremony with no real content, a merely symbolic gesture we no longer take seriously"],
        distortion_risk="medium",
        quick_meaning="Our founder's earlier reading of the Supper. Chiefly a remembrance of Christ's finished sacrifice. Not, on this reading, a new gift of his body.",
    ),
    dict(
        slug="mutual-consent", world_word="Mutual Consent (the Consensus Tigurinus)", tier=2,
        plain_meaning=(
            "Mutual Consent is our own name for the Consensus Tigurinus. Zurich and Geneva signed it "
            "together in 1549. It settles what we hold about the Lord's Supper."
        ),
        informational=(
            "In 1549, the Ministers of the Church of Zurich and John Calvin, Minister of the Church of "
            "Geneva, published a formal agreement together. This is the single most direct evidence "
            "that our two cities' own confessions are one coherent thing, not two traditions later "
            "grouped together by someone else's classification."
        ),
        evidential="The document survives under its own title, naming both signatories directly.",
        personal="We point to this document itself, not a description of it, whenever someone doubts that our two cities actually agreed rather than merely resembled each other.",
        translational="This was not a vague statement of goodwill between neighbors. It was a negotiated, specific, signed text.",
        false_friend=["a modern ecumenical statement of general Christian unity, rather than a specific negotiated doctrinal agreement"],
        distortion_risk="low",
        quick_meaning="Our own name for the Consensus Tigurinus. Zurich and Geneva signed it together in 1549. It settles what we hold about the Lord's Supper.",
    ),
    dict(
        slug="excommunication", world_word="Excommunication", tier=2,
        plain_meaning=(
            "Excommunication is formal exclusion from the sacraments and from our visible church. It "
            "answers sin that is not repented. It is the Consistory's own most severe tool at Geneva."
        ),
        informational=(
            "The doctrine itself is discussed in Calvin's Institutes in general, universal-church terms. "
            "At Geneva specifically, this authority belongs to the Consistory, not the civil council - "
            "an authority we fought to keep independent during the Perrinist crisis."
        ),
        evidential="Calvin's Institutes, Book IV, states the general doctrine of church discipline this tool serves.",
        personal="We do not treat this lightly, and we do not hand it to the magistrate, because a discipline answerable to shifting politics is no discipline at all to us.",
        translational="This is not a private grudge enforced by a religious court. It is our own church's own most serious answer to the question of whether a professed faith is being lived.",
        false_friend=["a purely spiritual or symbolic gesture with no real consequence for the person excluded"],
        distortion_risk="medium",
        quick_meaning="Formal exclusion from the sacraments, for sin that is not repented. It is the Consistory's own most severe tool at Geneva.",
    ),
    dict(
        slug="antistes", world_word="Antistes", tier=3,
        plain_meaning=(
            "Antistes is Zurich's own senior pastoral title. Bullinger held it after Zwingli died."
        ),
        informational=(
            "This title answers to Zurich's own city council, and it is not interchangeable with "
            "Zwingli's own earlier title, Leutpriester. The office marks the settled, ongoing shape our "
            "senior pastorate took at Zurich once Bullinger succeeded our founder."
        ),
        evidential="Bullinger held this title through his own four-decade pastorate at Zurich, from 1531.",
        personal="We use this word specifically for Zurich's own senior pastor - it is not our word for Geneva's own church government, which the council itself carries directly.",
        translational="This is not simply a fancier word for 'pastor' or 'bishop.' It names a specific office within Zurich's own particular arrangement of church and council.",
        false_friend=["a title equivalent to a Catholic bishop, implying an authority independent of the city council"],
        distortion_risk="low",
        quick_meaning="Zurich's own senior pastoral title. Bullinger held it after Zwingli. It answers to the city council.",
    ),
    dict(
        slug="elder", world_word="Elder (lay elder, Geneva)", tier=2,
        plain_meaning=(
            "An elder at Geneva is a layperson, not an ordained pastor. An elder holds real power in "
            "the Consistory."
        ),
        informational=(
            "Our founder's own vendored words state the general doctrine almost exactly this way: "
            "seniors selected from our own people, to unite with the pastors in pronouncing censures "
            "and exercising discipline. This is what makes our own Geneva church government "
            "presbyterian, not purely clerical."
        ),
        evidential="Calvin's Institutes, Book IV, chapter 3, states this general doctrine directly.",
        personal="We trust our elders because they come from among us, not because they hold ordained office - the discipline they exercise is our own community's, not the clergy's alone.",
        translational="This is not an honorary title for a respected older member. It names a real office, with real disciplinary standing, inside the Consistory itself.",
        false_friend=["an honorary or ceremonial role with no real institutional authority"],
        distortion_risk="medium",
        quick_meaning="A layperson at Geneva, not ordained clergy. An elder holds real power in the Consistory, alongside the pastors.",
    ),
    dict(
        slug="catechism", world_word="Catechism", tier=2,
        plain_meaning=(
            "A catechism is a fixed, memorizable statement of doctrine. We teach it to our whole "
            "population. We hold more than one. They are not all the same voice."
        ),
        informational=(
            "We hold at least three distinct catechetical voices: Calvin's own Geneva Catechism, the "
            "Heidelberg Catechism, and Zwingli's own earlier, less formally catechetical instruction. "
            "This is worth naming as a real plurality, not one uniform genre repeated three times."
        ),
        evidential="Calvin's Geneva Catechism survives in full in our own vendored record; the Heidelberg Catechism survives separately, from the Palatinate.",
        personal="At Geneva especially, this is how understanding is built up in the whole population, not only in trained pastors - article resting on article, taught patiently.",
        translational="This is not a dry list of facts to memorize for its own sake. It is how we hand our own convictions on to those who come after us without letting them drift.",
        false_friend=["a single, uniform genre repeated identically across every Reformed city, rather than several distinct catechetical voices"],
        distortion_risk="low",
        quick_meaning="A fixed statement of doctrine, taught to our whole population. We hold at least three distinct catechetical voices, not one.",
    ),
    dict(
        slug="confession-of-faith", world_word="Confession (of Faith)", tier=2,
        plain_meaning=(
            "A confession is a formal, public statement of our own doctrine. The Second Helvetic "
            "Confession, from Zurich, is our own most mature example."
        ),
        informational=(
            "Bullinger's Second Helvetic Confession, written at Zurich in 1566, is our own most mature "
            "vendored confessional statement, later adopted well beyond Zurich itself. We do not "
            "currently hold a comparable Geneva-side confessional document in our own vendored record."
        ),
        evidential="The Second Helvetic Confession survives in full in our own vendored record.",
        personal="We wrote our confessions not to say something new, but so that what we already believed could survive the generation that first argued it out.",
        translational="This is not a creative theological essay. It is a settled, publicly adopted statement, meant to be taught and handed on without drift.",
        false_friend=["a personal statement of individual belief, rather than a formally adopted, publicly binding church document"],
        distortion_risk="low",
        quick_meaning="A formal, publicly adopted statement of our church's doctrine. The Second Helvetic Confession, from Zurich, is our own most mature example.",
    ),
    dict(
        slug="heads-of-agreement", world_word="Heads of Agreement", tier=3,
        plain_meaning=(
            "Heads of Agreement is the Consensus Tigurinus's own name for its own articles. It has "
            "twenty-six of them."
        ),
        informational=(
            "This is a specific textual feature of the Consensus Tigurinus itself - the document's own "
            "way of organizing its own agreed statements, not a generic phrase for any list of "
            "doctrines."
        ),
        evidential="The Consensus Tigurinus's own text is organized under this heading, including the ninth Head of Agreement (Sign and the Thing Signified).",
        personal="When we cite a specific point of the Consensus, we cite it by its own Head number, the way the document itself is organized.",
        translational="This is not a loose figure of speech. It names the Consensus's own formal, numbered structure.",
        false_friend=["a generic phrase for any list of shared beliefs, rather than the Consensus Tigurinus's own specific numbered structure"],
        distortion_risk="low",
        quick_meaning="The Consensus Tigurinus's own name for its own twenty-six articles. A specific feature of that text, not a generic phrase.",
    ),
    dict(
        slug="reformation", world_word="Reformation", tier=3,
        plain_meaning=(
            "Reformation is our own name for our whole central project. We test every inherited "
            "practice against Scripture. We let go of what will not stand."
        ),
        informational=(
            "This word names the whole of what we have been doing since our founder first preached "
            "at Zurich: testing inherited practice against the text, in public, and reforming what does "
            "not hold. Participants already bring strong modern assumptions to this word, which is "
            "exactly why we name it carefully rather than assume it needs no explanation."
        ),
        evidential="Our own record uses this word to describe its own central project throughout, from the earliest disputations onward.",
        personal="We do not experience this as a single completed event in our own past. It is the ongoing shape of how we test what we have inherited.",
        translational="A modern reader often hears this word and pictures one dramatic break with the past, settled quickly. For us, it names an ongoing discipline of testing, not a single finished event.",
        false_friend=["a single dramatic historical break, cleanly finished at one moment, rather than an ongoing discipline of testing inherited practice"],
        distortion_risk="high",
        quick_meaning="Our own name for our central project. We test every inherited practice against Scripture, in public. We let go of what will not stand.",
    ),
]


def emit_term(t: dict, *, relations: list[dict], sources: list[dict], canon_cells: list[str] | None = None) -> Path:
    rid = f"rzg.term.{t['slug']}"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "term",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": canon_cells or [],
        "confidence": {
            "citation_specificity": "A" if t["tier"] == 1 else "B",
            "verification_state": "verified-direct" if t["tier"] == 1 else "verified-via-authority",
            "evidentiary_weight": "load-bearing" if t["tier"] == 1 else "corroborating",
            "formation_confidence": "Documented",
            "divergence_note": t.get("divergence"),
        },
        "sources": sources,
        "retrieval": {"tier": t["tier"], "retrieve_when": t.get("retrieve_when", []),
                      "do_not_retrieve_when": t.get("do_not_retrieve_when", [])},
        "relations": relations,
        "plain_meaning": t["plain_meaning"],
        "world_word": t["world_word"],
        "false_friend": t["false_friend"],
        "senses": {
            "informational": t["informational"],
            "evidential": t["evidential"],
            "personal": t["personal"],
            "translational": t["translational"],
        },
        "quick_meaning": t["quick_meaning"],
        "distortion_risk": t["distortion_risk"],
    }
    path = OUT_ROOT / "term" / f"{rid}.md"
    _write(path, payload, t.get("body", DEFAULT_BODY.format(slug=t["slug"], tier=t["tier"])))
    return path


DEFAULT_BODY_RICH = """Built from Lexicon-Chunks/rzglex{lexnum}_{slug}.md (Approved to proceed, Doc_06
Revision 2), converting that chunk's own Quick Meaning / World Meaning / Ecological Function /
Distortion Risk / Key Sources sections onto this schema's own fields. AUTHORED, not mechanical: the
mapping of "World Meaning" prose onto senses.informational/evidential/personal is this compilation's
own judgment about which portion of the chunk's own multi-paragraph prose best fits each sense's own
purpose, not a field the chunk itself labels that way.
"""

DEFAULT_BODY = """Built from Doc_03_Lexicon_Candidate_List.md SS1's own candidate roster (one-line
world-meaning, tier, strand, tags, AG-risk), per this world's own disclosed Doc_06 deferral of this
term's deployment-chunk production. Genuinely thinner than the fleet's own Tier-1 chunked terms: no
dedicated per-term Key Sources research pass was run for this candidate at Doc_06 - the citation(s)
below are the ones Doc_03 itself already names, not a fresh citation this compilation invents. Tier
{tier}, per Doc_06 SS1's own confirmed tier table.
"""


def main() -> int:
    written: list[Path] = []

    # -- 6 rich terms, from their own already-built, already-reviewed chunks
    lex_num = {"predestination-election": "001", "disputation": "004", "sola-scriptura": "005",
               "the-lords-supper-spiritual-presence": "007", "sign-and-the-thing-signified": "008",
               "consistory": "012"}
    for t in RICH_TERMS:
        t["body"] = DEFAULT_BODY_RICH.format(lexnum=lex_num[t["slug"]], slug=t["slug"])

    rel = {
        "predestination-election": [
            {"type": "associated-with", "target": "rzg.term.sola-scriptura"},
            {"type": "associated-with", "target": "rzg.term.providence"},
            {"type": "associated-with", "target": "rzg.term.the-lords-supper-spiritual-presence"},
            {"type": "tension-with", "target": "rzg.gravity.sovereignty-of-god-predestination-election"},
        ],
        "disputation": [{"type": "associated-with", "target": "rzg.term.sola-scriptura"},
                        {"type": "associated-with", "target": "rzg.term.sixty-seven-articles"},
                        {"type": "illustrated-by", "target": "rzg.story.first-zurich-disputation"}],
        "sola-scriptura": [
            {"type": "associated-with", "target": "rzg.term.disputation"},
            {"type": "associated-with", "target": "rzg.term.predestination-election"},
            {"type": "associated-with", "target": "rzg.term.the-lords-supper-spiritual-presence"},
            {"type": "associated-with", "target": "rzg.term.catechism"},
            {"type": "associated-with", "target": "rzg.term.consistory"},
            {"type": "illustrated-by", "target": "rzg.story.first-zurich-disputation"},
            {"type": "tension-with", "target": "rzg.gravity.scripture-sole-authority-disputation-catechesis"},
        ],
        "the-lords-supper-spiritual-presence": [
            {"type": "associated-with", "target": "rzg.term.sign-and-the-thing-signified"},
            {"type": "associated-with", "target": "rzg.term.predestination-election"},
            {"type": "associated-with", "target": "rzg.term.sola-scriptura"},
            {"type": "associated-with", "target": "rzg.term.memorial-commemoration"},
            {"type": "illustrated-by", "target": "rzg.story.calvins-journey-to-zurich"},
            {"type": "tension-with", "target": "rzg.gravity.spiritual-presence-rejection-of-corporeal-sacrificial-mediation"},
            {"type": "tension-with", "target": "rzg.gravity.zwinglis-remembrance-reading-vs-negotiated-consensus"},
        ],
        "sign-and-the-thing-signified": [
            {"type": "associated-with", "target": "rzg.term.the-lords-supper-spiritual-presence"},
            {"type": "associated-with", "target": "rzg.term.mutual-consent"},
            {"type": "associated-with", "target": "rzg.term.heads-of-agreement"},
            {"type": "associated-with", "target": "rzg.contested.sign-and-the-thing-signified"},
        ],
        "consistory": [
            {"type": "associated-with", "target": "rzg.term.sola-scriptura"},
            {"type": "associated-with", "target": "rzg.term.excommunication"},
            {"type": "associated-with", "target": "rzg.term.elder"},
            {"type": "tension-with", "target": "rzg.gravity.consistorial-church-discipline"},
            {"type": "tension-with", "target": "rzg.gravity.council-led-authority-vs-consistorial-independence"},
        ],
        "providence": [{"type": "associated-with", "target": "rzg.term.predestination-election"}],
        "sixty-seven-articles": [{"type": "associated-with", "target": "rzg.term.disputation"}],
        "memorial-commemoration": [
            {"type": "associated-with", "target": "rzg.term.the-lords-supper-spiritual-presence"},
            {"type": "tension-with", "target": "rzg.gravity.zwinglis-remembrance-reading-vs-negotiated-consensus"},
            {"type": "associated-with", "target": "rzg.contested.zwinglis-remembrance-vs-negotiated-consensus"},
        ],
        "mutual-consent": [{"type": "associated-with", "target": "rzg.term.sign-and-the-thing-signified"},
                           {"type": "illustrated-by", "target": "rzg.story.calvins-journey-to-zurich"}],
        "excommunication": [{"type": "associated-with", "target": "rzg.term.consistory"}],
        "antistes": [],
        "elder": [{"type": "associated-with", "target": "rzg.term.consistory"}],
        "catechism": [{"type": "associated-with", "target": "rzg.term.sola-scriptura"}],
        "confession-of-faith": [],
        "heads-of-agreement": [{"type": "associated-with", "target": "rzg.term.sign-and-the-thing-signified"}],
        "reformation": [],
    }

    src = {
        "predestination-election": [
            {"source_id": "rzg.source.zwingli-selected-works", "locus": "the 1527 Refutation's own 'On Election' section, lines approx. 9591-9762", "license": "public-domain"},
            {"source_id": "rzg.source.second-helvetic-confession", "locus": "ch. X", "license": "public-domain"},
            {"source_id": "rzg.source.calvin-institutes-books2-3", "locus": "Books II-III", "license": "public-domain"},
        ],
        "disputation": [
            {"source_id": "rzg.source.zwingli-selected-works", "locus": "the Acts of the First and Second Zurich Disputations, lines approx. 4487-4700", "license": "public-domain"},
        ],
        "sola-scriptura": [
            {"source_id": "rzg.source.zwingli-selected-works", "locus": "the Sixty-Seven Articles' own preface, lines 4487-4492", "license": "public-domain"},
            {"source_id": "rzg.source.calvin-geneva-catechism", "locus": "lines approx. 1639-1642", "license": "public-domain"},
        ],
        "the-lords-supper-spiritual-presence": [
            {"source_id": "rzg.source.zwingli-sixty-seven-articles", "locus": "Article XVIII, lines 4565-4569", "license": "public-domain"},
            {"source_id": "rzg.source.calvin-institutes-book4", "locus": "e.g. lines 20735, 20812, 20934, 20943", "license": "public-domain"},
            {"source_id": "rzg.source.consensus-tigurinus", "locus": "9th Head of Agreement, lines 768-770", "license": "public-domain"},
        ],
        "sign-and-the-thing-signified": [
            {"source_id": "rzg.source.consensus-tigurinus", "locus": "9th Head of Agreement, lines 768-770, and the document's own title page", "license": "public-domain"},
        ],
        "consistory": [
            {"source_id": "rzg.source.calvin-institutes-book4", "locus": "lines 10503-10504 and IV.3.8 (lines 2831-2832)", "license": "public-domain"},
        ],
        "providence": [{"source_id": "rzg.source.calvin-institutes-book1", "locus": "Book I", "license": "public-domain"}],
        "sixty-seven-articles": [{"source_id": "rzg.source.zwingli-sixty-seven-articles", "locus": "whole text", "license": "public-domain"}],
        "memorial-commemoration": [{"source_id": "rzg.source.zwingli-sixty-seven-articles", "locus": "Article XVIII", "license": "public-domain"}],
        "mutual-consent": [{"source_id": "rzg.source.consensus-tigurinus", "locus": "title page and whole document", "license": "public-domain"}],
        "excommunication": [{"source_id": "rzg.source.calvin-institutes-book4", "locus": "Book IV, general discipline doctrine", "license": "public-domain"}],
        "antistes": [{"source_id": "rzg.source.second-helvetic-confession", "locus": "per Doc_01 SS1's own office naming", "license": "public-domain"}],
        "elder": [{"source_id": "rzg.source.calvin-institutes-book4", "locus": "IV.3.8, lines 2831-2832", "license": "public-domain"}],
        "catechism": [
            {"source_id": "rzg.source.calvin-geneva-catechism", "locus": "whole work", "license": "public-domain"},
            {"source_id": "rzg.source.heidelberg-catechism", "locus": "whole work", "license": "public-domain"},
        ],
        "confession-of-faith": [{"source_id": "rzg.source.second-helvetic-confession", "locus": "whole work", "license": "public-domain"}],
        "heads-of-agreement": [{"source_id": "rzg.source.consensus-tigurinus", "locus": "the document's own structure", "license": "public-domain"}],
        "reformation": [{"source_id": "rzg.source.zwingli-selected-works", "locus": "throughout, per Doc_01's own usage", "license": "public-domain"}],
    }

    retrieve = {
        "predestination-election": (
            ["participant uses \"predestination,\" \"election,\" or \"the elect\"",
             "participant asks why salvation doesn't depend on their own effort or worthiness",
             "participant asks whether Zurich and Geneva taught the same thing about God's own choice"],
            ["participant asks generally about God's own providence over ordinary events without reference to salvation specifically"]),
        "disputation": (
            ["participant uses \"disputation\" or asks how Zurich's reform was actually decided",
             "participant asks why a city council, not a bishop or pope, settled a doctrinal question"],
            ["participant is asking about Geneva's own reform process, which did not proceed by this mechanism"]),
        "sola-scriptura": (
            ["participant asks why this world rejected the Pope's or a council's own authority",
             "participant asks what actually settled a doctrinal dispute here"],
            ["participant is asking specifically about the Zurich Disputation as an event"]),
        "the-lords-supper-spiritual-presence": (
            ["participant asks how this world understood communion",
             "participant uses \"spiritual presence,\" \"remembrance,\" or asks whether Christ is really present in the bread and wine"],
            ["participant is asking specifically about the Consensus Tigurinus's own formal technical language"]),
        "sign-and-the-thing-signified": (
            ["participant asks about the exact 1549 Consensus Tigurinus language",
             "participant asks whether the Zurich/Geneva agreement was a real breakthrough or a diplomatic fudge"],
            ["participant is asking generally about the Supper doctrine without reference to this specific formula"]),
        "consistory": (
            ["participant asks about Geneva's own church discipline",
             "participant uses \"Consistory\" or \"lay elders\""],
            ["participant is asking about Zurich's own church government, which ran through the city council directly"]),
    }

    thin_slugs = {t["slug"] for t in THIN_TERMS}
    for t in THIN_TERMS:
        t.setdefault("divergence", (
            "Built from Doc_03's own candidate-roster entry, not from a dedicated per-term research "
            "pass at Doc_06 - this world's own disclosed deferral (Doc_06 SS0) for the eleven "
            "non-Tier-1 candidates. The underlying doctrine is Documented in the cited source, but "
            "this specific record's own citation was not independently re-verified against the "
            "vendored file this pass, hence verified-via-authority rather than verified-direct."
        ))

    for t in RICH_TERMS + THIN_TERMS:
        rw, dnrw = retrieve.get(t["slug"], ([f"participant asks about {t['world_word'].lower()}"], []))
        t["retrieve_when"] = rw
        t["do_not_retrieve_when"] = dnrw
        written.append(emit_term(t, relations=rel.get(t["slug"], []), sources=src.get(t["slug"], [])))

    all_slugs = [t["slug"] for t in RICH_TERMS + THIN_TERMS]
    assert len(all_slugs) == len(set(all_slugs)), "duplicate slug"
    assert len(RICH_TERMS) == 6 and len(THIN_TERMS) == 11, "expected 6 rich + 11 thin = 17 term records"

    for p in written:
        print(p.relative_to(REPO_ROOT))
    print(f"\n{len(written)} term records written (6 rich, from built chunks; 11 thin, from Doc_03's own "
          f"candidate roster). rzglex002/009 correctly not emitted as independent records - merged into "
          f"rzg.term.predestination-election / rzg.term.the-lords-supper-spiritual-presence.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
