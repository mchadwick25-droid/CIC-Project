"""S6.2/PAHC - S2.3-equivalent: term authoring (single batch; 13 terms).

Adds the authored fields onto the S2.2 mechanical records. PAHC
firsts, each declared:

- formation_confidence is EXTRACTED, not derived: every chunk carries
  its own '**Confidence:**' block (the full five-level vocabulary in
  the chunks' own words) - extract_confidence() reads the leading
  enum token from the distortion_risk field's verbatim text and
  ASSERTS the extraction against the enum. ONE declared special case:
  pahclex009 (ministrae), whose block splits Documented(the report
  exists)/Inferential-Thin(what it tells about the women's role) -
  the ENTRY's load-bearing content is the role reading, so the
  conservative Inferential-Thin is taken, with the chunk's own split
  riding verbatim in the field it already lives in.
- original_script is EXTRACTED from the Term field's own parens
  (episkopos (GREEK) etc.) - Greek where present; the three Latin
  terms (ministrae, hetaeria, pertinacia) and the English 'Two Ways'
  legitimately have none.
- The STRAND A/B structure gets its authored home: period senses and
  voice surfaces carry the both-patterns honesty in the chunks' own
  shape (one bishop at the center in some households, a governing
  council in others, neither declared wrong) - the strand-plural
  world speaking as its own plurality.
- The 15 confirmed-gloss originals read IN VIEW: GLOSS_MAP below,
  asserted at every run against live CONFIRMED_GLOSSES and live term
  fields. 12 of 15 resolve to term records; the three Sunday
  circumlocutions are B-category Facilitator phrases with no term
  record BY DESIGN. Note 'the water' -> pahclex011: the gloss IS the
  runtime carrier of that surface (its alias was Rule-A-dropped at
  birth, S2.2) - the SS4 design working end-to-end.
- The Two Ways single-source watch item (S2.1b) lands: pahclex007's
  confidence and conceptual note carry the chunk's own
  single-source-not-network-norm cap and the out-of-set Barnabas
  boundary.
- FLAG-023 reader; FLAG-002 EF-verbatim on first edges; symmetric
  mirrored both sides, INVERSE typed pairs; prior_sense honesty with
  UNVERIFIED flags on builder inferences.

Relation map (grounded in the chunks' own EF/body text):
  001 assoc 002 (the G01 pair: fuller argument / counterweight)
  006 presupposes 001 (the council-around-a-bishop needs the bishop)
  006 assoc 002 (the same elders, differently configured)
  008 tension-with 001 (charismatic pathway vs settling office)
  003 assoc 004 (the letter and the table carry unity - G02/G07)
  004 assoc 001 (who presides reaches into who leads)
  004 presupposes 011 (baptism opens the door to the table)
  011 presupposes 007 (teaching first, then the water)
  011 assoc 001 (the bishop's oversight where Strand A holds)
  005 assoc 004 (deacons carry the elements)
  005 assoc 009 (ministrae/diakonoi - the honest unknown)
  010 assoc 004 (agape <-> eucharistia, the chunk's own bridge)
  010 assoc 012 (agape <-> hetaeria, the chunk's own bridge)
  012 assoc 013 (the two Pliny legal terms)
"""
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))

TERM_DIR = BACKEND / "wrs" / "records" / "pahc_world" / "term"
CHUNKS = BACKEND / "data" / "pahc_world" / "lexicon_chunks"

VDATE = "2026-07-31"

# the S2.8 render-parity catch, fixed as a declared S2.3 correction:
# the deployed chunks' Related-Terms lists are the world's own
# reciprocity map, and the first authored graph under-covered them
CH = ("the chunk's own Related-Terms membership (the deployed "
      "reciprocity map - the S2.8 render-parity catch, fixed as a "
      "declared S2.3 correction)")

GLOSS_MAP = {
    "the day named for the sun": None,
    "the Lord's own day": None,
    "the first day of the week": None,
    "the water": "pahclex011",
    "Two Ways": "pahclex007",
    "episkopos": "pahclex001",
    "presbyteros": "pahclex002",
    "ekklesia": "pahclex003",
    "eucharistia": "pahclex004",
    "diakonos": "pahclex005",
    "presbyterion": "pahclex006",
    "prophetes": "pahclex008",
    "ministrae": "pahclex009",
    "agape": "pahclex010",
    "pertinacia": "pahclex013",
}

ENUM = ("Documented", "Widely Accepted", "Dominant Modern Reconstruction",
        "Contested", "Inferential-Thin")


def read_record(path: Path):
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n"), path
    rest = text[4:]
    front, sep, body = rest.partition("\n---\n")
    assert sep, path
    return yaml.safe_load(front), body


def write_record(path: Path, front: dict, body: str):
    fy = yaml.safe_dump(front, sort_keys=False, allow_unicode=True,
                        width=100, default_flow_style=False)
    path.write_text(f"---\n{fy}---\n{body}", encoding="utf-8")


def chunk_ef(chunk_glob: str) -> str:
    path = next(CHUNKS.glob(chunk_glob))
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^## Ecological Function\s*\n(.*?)(?=^## |\Z)",
                  text, re.S | re.M)
    assert m, chunk_glob
    return re.sub(r"^-{3,}\s*$", "", m.group(1), flags=re.M).strip()


def ef_note(lead: str, chunk_glob: str) -> str:
    return (lead + " Chunk Ecological Function (verbatim, absorbed per "
            "FLAG-002): " + chunk_ef(chunk_glob))


def extract_confidence(front: dict, rid: str) -> str:
    """The extract-not-derive first: the chunk's own Confidence block
    rides inside distortion_risk verbatim (the S2.2 split); read its
    leading enum token."""
    dr = front.get("distortion_risk", "")
    m = re.search(r"\*\*Confidence:\*\*\s*(.*)", dr, re.S)
    assert m, rid
    block = m.group(1).strip()
    if rid == "pahclex009":
        # declared special case: the block splits Documented(report)/
        # Inferential-Thin(role content); the entry's load-bearing
        # content is the role reading - conservative extraction
        return "Inferential-Thin"
    # prefix-match the enum, longest first: multi-level blocks (004/
    # 010: Documented-for-baseline + Contested-for-the-elaboration;
    # 011: Widely Accepted + a Documented qualifier) lead with the
    # term's own base assessment; the full split stays verbatim in
    # the field this text lives in
    for tok in sorted(ENUM, key=len, reverse=True):
        if block.startswith(tok):
            return tok
    raise AssertionError((rid, block[:60]))


def extract_script(term: str):
    m = re.search(r"\(([^)]*[Ͱ-Ͽ][^)]*)\)", term)
    return m.group(1).strip() if m else None


AUTH = {
 "pahclex001": dict(
    period_sense=(
        "The one who oversees the community's table and guards its "
        "unity - held in this world as a LIVE QUESTION, not an office: "
        "in some households (Antioch, the Asia Minor cities - Strand A) "
        "one episkopos stands at the center and obedience to him is "
        "felt as the very shape of unity; in others (Rome, Corinth - "
        "Strand B) a council of presbyters governs with nothing felt "
        "missing; and the outside pressure of accusation gives BOTH "
        "arguments real weight without settling either (chunk "
        "Quick/World Meaning)."),
    prior_sense=(
        "The ordinary Greek episkopos - an overseer, inspector, "
        "supervisor of civic or financial matters - a secular "
        "function-word the communities applied to their own oversight "
        "before it hardened into a title; a builder note, UNVERIFIED "
        "against this build's own docs."),
    modern_sense=(
        "'Bishop' as an already-secured office with defined powers, "
        "territorial jurisdiction, and a hierarchy (chunk Modern "
        "Hearing)."),
    conceptual_distance_note=(
        "Reading back a later hierarchy 'flattens a live argument into "
        "an accomplished fact' (chunk World Hearing) - the term's own "
        "contest (secured reality vs argued-for aspiration; network "
        "norm vs regional pattern) is the chunk's CT section, parked "
        "for S2.6. Sharp gap: high grounding criterion."),
    semantic_domain="oversight-office",
    grounding_criterion="high",
    voice_surface=(
        "Among us the word names the one who oversees the table and "
        "speaks for the household - where there is such a one. Some of "
        "our households are tuned to a single episkopos the way "
        "strings are tuned to a harp; others are governed by their "
        "elders together and feel no lack. We hold both in our "
        "letters, and neither side has declared the other wrong."),
    cite="A", weight="load-bearing",
    relations=[
        dict(type="associated-with", target="pahclex002",
             note_ef=("The G01 pair by the chunks' own division of "
                      "labor: episkopos carries the fuller Strand A/B "
                      "institutional argument, presbyteros the "
                      "counterweight council model."),
             chunk="pahclex001_*"),
        dict(type="associated-with", target="pahclex004",
             note=("Who presides at the thanksgiving 'reaches straight "
                   "into the argument about who leads' (pahclex004 "
                   "World Meaning); symmetric mirror on pahclex004.")),
        dict(type="associated-with", target="pahclex011",
             note=("Strand-A oversight of the water ('no one should "
                   "baptize without the bishop' - pahclex011 World "
                   "Meaning); symmetric mirror.")),
        dict(type="tension-with", target="pahclex008",
             note=("The chunks' own shift: the prophet's charismatic, "
                   "itinerant authority 'being joined - and in some "
                   "places replaced - by the more settled offices'; "
                   "'where a bishop now presides, the prophet's place "
                   "at the table is less certain' (pahclex008) - a "
                   "lived tension, not a settled succession; symmetric "
                   "both ways.")),
        dict(type="presupposed-by", target="pahclex006",
             note=("Mirror of pahclex006's presupposes edge: the "
                   "council-around-a-bishop exists only where the "
                   "bishop does.")),
        dict(type="associated-with", target="pahclex003",
             note="The assembly and its oversight - " + CH + "; symmetric mirror."),
        dict(type="associated-with", target="pahclex005",
             note="Ignatius's threefold unit names deacons with bishop and presbyters - " + CH + "; symmetric mirror."),
    ]),
 "pahclex002": dict(
    period_sense=(
        "The elders who carry the community's governance - sometimes "
        "as a council holding full authority (Rome's letter to Corinth "
        "speaks of presbyters removed, never a bishop deposed), "
        "sometimes gathered around a bishop (the Asia Minor pattern); "
        "Polycarp, addressed by Ignatius as bishop, still calls "
        "himself 'one of the presbyters' - the distinction not yet one "
        "he claims in writing (chunk Quick/World Meaning)."),
    prior_sense=(
        "The ordinary Greek presbyteros, 'elder' - seniority of age "
        "carrying communal respect, with the Jewish synagogue's elder "
        "councils as the nearer institutional inheritance; a builder "
        "note, UNVERIFIED against this build's own docs."),
    modern_sense=(
        "Either a purely advisory role under a bishop, or a Protestant "
        "lay-elder model (chunk Modern Hearing)."),
    conceptual_distance_note=(
        "The term's meaning 'is still being shaped, not yet fixed' - "
        "councils that HOLD authority in one city, councils that "
        "SUPPORT a bishop in another (chunk World Hearing). Standard "
        "grounding: a role-shape correction inside the same office "
        "vocabulary."),
    semantic_domain="elder-council",
    grounding_criterion="standard",
    voice_surface=(
        "We call them presbyteroi, and what they do depends on where "
        "we stand. In Rome the presbyters together carry the whole "
        "weight of governance; in Antioch they are gathered around a "
        "bishop like strings tuned to a harp. The same word, two "
        "shapes of trust - and our correspondence holds both without "
        "either declaring the other wrong."),
    cite="A", weight="load-bearing",
    relations=[
        dict(type="associated-with", target="pahclex001",
             note_ef="Symmetric mirror of pahclex001's edge (the G01 pair).",
             chunk="pahclex002_*"),
        dict(type="associated-with", target="pahclex006",
             note=("The same elders differently configured: the "
                   "presbyterion is the Strand-A gathered form of this "
                   "office (pahclex006's own scope note); symmetric "
                   "mirror.")),
        dict(type="associated-with", target="pahclex005",
             note="The threefold unit's third member - " + CH + "; symmetric mirror."),
    ]),
 "pahclex003": dict(
    period_sense=(
        "The community's one self-name: the assembly, the church of "
        "God sojourning in whatever city its members live - no "
        "building, no property, a household door opening on the first "
        "day of the week; the ekklesia in Antioch and Rome and Corinth "
        "one ekklesia not by shared structure but by the letters "
        "traveling between them (chunk Quick/World Meaning)."),
    prior_sense=(
        "The Greek polis's own ekklesia - the summoned assembly of "
        "citizens - and the LXX's use for Israel gathered before God: "
        "a civic word already carrying 'called out and gathered' "
        "before these communities took it as their name; a builder "
        "note, UNVERIFIED against this build's own docs."),
    modern_sense=(
        "'Church' as a building, a denomination, or an institution "
        "with established structures (chunk Modern Hearing)."),
    conceptual_distance_note=(
        "The gathered people themselves - portable, propertyless, "
        "identified by meal and letters rather than location or legal "
        "standing (chunk World Hearing). Sharp gap: high grounding "
        "criterion - the building/institution reading erases exactly "
        "the household-and-letter fabric this world is."),
    semantic_domain="gathered-assembly",
    grounding_criterion="high",
    voice_surface=(
        "When someone asks who we are, we have one name: the "
        "ekklesia - the assembly, called out and gathered. The city "
        "can point to no building of ours. What we have is a door "
        "that opens on the first day of the week, and letters that "
        "carry our name between cities faster than any of us could "
        "walk it."),
    cite="B", weight="load-bearing",
    relations=[
        dict(type="associated-with", target="pahclex004",
             note_ef=("The chunk's own EF: 'the letter and the table "
                      "do the heavy lifting of unity, not a "
                      "hierarchy' - the table half is eucharistia; "
                      "symmetric both ways."),
             chunk="pahclex003_*"),
        dict(type="associated-with", target="pahclex001",
             note="Symmetric mirror of pahclex001's edge (the assembly and its oversight - the deployed reciprocity map)."),
    ]),
 "pahclex004": dict(
    period_sense=(
        "The thanksgiving over bread and cup - the meal that does "
        "'more of our community's ongoing forming than anything else "
        "we do'; its presidency inseparable from the authority "
        "question (Ignatius: no valid eucharist apart from the bishop "
        "- in the households his letters shaped; elsewhere presbyters "
        "give thanks together with nothing felt missing); refusing a "
        "rival's separate table an act of worship and belonging in "
        "one breath (chunk Quick/World Meaning)."),
    prior_sense=(
        "The ordinary Greek eucharistia, 'thanksgiving' - gratitude "
        "itself, the word every letter-writer used for thanking God "
        "or a benefactor, specialized here to THE thanksgiving; a "
        "builder note, UNVERIFIED against this build's own docs."),
    modern_sense=(
        "A uniform ritual with established prayers, or the later "
        "debates about presence and sacrifice (chunk Modern "
        "Hearing)."),
    conceptual_distance_note=(
        "Form varies household to household (the Didache's prayers "
        "carry no institution narrative; Justin's account is fullest "
        "but not thereby most representative - the chunk's own "
        "methodological caution, parked with its CT section for "
        "S2.6); what is constant is the table's centrality to "
        "forming the community. Sharp gap: high grounding "
        "criterion."),
    semantic_domain="thanksgiving-table",
    grounding_criterion="high",
    voice_surface=(
        "Whatever else is decided or left open among us, we gather "
        "to give thanks over bread and cup, and each return to that "
        "table re-makes who we are together. Who may preside is "
        "never a small question - it reaches straight into who "
        "leads. And to hold to our own table against a rival's "
        "separate one is worship and belonging in the same act."),
    cite="A", weight="load-bearing",
    relations=[
        dict(type="associated-with", target="pahclex001",
             note_ef=("The chunk's own EF: G07 anchored, tying "
                      "directly into G01 through who presides."),
             chunk="pahclex004_*"),
        dict(type="associated-with", target="pahclex003",
             note="Symmetric mirror of pahclex003's edge (letter and table)."),
        dict(type="associated-with", target="pahclex005",
             note=("Justin's deacons carry the elements to the absent "
                   "(pahclex005 World Meaning); symmetric mirror.")),
        dict(type="associated-with", target="pahclex010",
             note=("The chunk-attested bridge: agape <-> eucharistia, "
                   "'aware they may name the same thing or two "
                   "things, without forcing an answer' (pahclex010); "
                   "symmetric mirror.")),
        dict(type="presupposes", target="pahclex011",
             note=("'Baptism opens the door to the table' (pahclex011 "
                   "World Meaning) - the threshold ordering, typed as "
                   "the Desert pairing.")),
    ]),
 "pahclex005": dict(
    period_sense=(
        "Those set apart to serve - help carried to widow, orphan, "
        "prisoner, stranger; a calling of its own, not a rung on a "
        "ladder; named as part of Ignatius's three-part unit in Asia "
        "Minor, serving without any such tier-claim in Justin's Rome; "
        "in some communities held by women alongside men (chunk "
        "Quick/World Meaning)."),
    prior_sense=(
        "The ordinary Greek diakonos - the table-servant, the one who "
        "waits and carries - a low ordinary work-word the communities "
        "kept low on purpose: the service IS the office; a builder "
        "note, UNVERIFIED against this build's own docs."),
    modern_sense=(
        "A transitional or assistant role subordinate to priests and "
        "bishops (chunk Modern Hearing)."),
    conceptual_distance_note=(
        "Service as its own thing, not a stepping-stone (chunk World "
        "Hearing); the three-tier framing is regional (Ignatius), the "
        "service itself is not. Standard grounding."),
    semantic_domain="service-office",
    grounding_criterion="standard",
    voice_surface=(
        "The diakonoi among us do work that sits closer to the "
        "household's open door than to the letter-writers' hard "
        "arguments: bread to the widow, help to the prisoner, the "
        "cup carried to whoever could not come. It is not a lower "
        "rank on the way to a higher one. It is its own calling, and "
        "in some of our households women hold it beside men."),
    cite="A", weight="corroborating",
    relations=[
        dict(type="associated-with", target="pahclex004",
             note_ef=("The chunk's own EF: service connected to the "
                      "community's self-understanding as carers for "
                      "the vulnerable - enacted at and from the "
                      "table."),
             chunk="pahclex005_*"),
        dict(type="associated-with", target="pahclex009",
             note=("The honest unknown held as the chunks hold it: "
                   "whether Pliny's ministrae translate the "
                   "communities' own diakonoi 'none of this Pliny "
                   "tells us, and none of it do we know from our own "
                   "words'; symmetric both ways.")),
        dict(type="associated-with", target="pahclex001",
             note="Symmetric mirror of pahclex001's threefold-unit edge."),
        dict(type="associated-with", target="pahclex002",
             note="Symmetric mirror of pahclex002's threefold-unit edge."),
        dict(type="associated-with", target="pahclex008",
             note="Symmetric mirror of pahclex008's Didache-15:1 edge (bishops and deacons appointed together as the prophets' ministry passes to local office)."),
    ]),
 "pahclex006": dict(
    period_sense=(
        "The gathered body of presbyters around a bishop - tuned to "
        "him, Ignatius says, as strings to a harp; supporting without "
        "replacing and without merely obeying. A Strand A pattern: "
        "real and deeply formative where practiced, absent from the "
        "Roman correspondence entirely (chunk Quick/World Meaning)."),
    prior_sense=(
        "The word's nearer inheritance is the Jewish elder-council "
        "(the LXX/NT presbyterion of Jerusalem) - a council-word, not "
        "a place-word; a builder note, UNVERIFIED against this "
        "build's own docs."),
    modern_sense=(
        "A denominational governing body or a physical building "
        "(chunk Modern Hearing)."),
    conceptual_distance_note=(
        "A council, not an institution - and not found everywhere "
        "(chunk World Hearing). The chunk's own confidence carries "
        "the fleet-familiar single-witness honesty: 'maximal "
        "single-witness dependency… no other voice independently "
        "corroborates the term.' Standard grounding."),
    semantic_domain="council-around-bishop",
    grounding_criterion="standard",
    voice_surface=(
        "Where one of our households has a bishop, his elders gather "
        "around him as a presbyterion - tuned together, Ignatius "
        "says, the way strings are tuned to a harp. But this way of "
        "speaking is his, and the households his letters formed. In "
        "Rome the elders govern together, and no such council-around-"
        "a-bishop appears in anything they wrote."),
    cite="A", weight="corroborating",
    relations=[
        dict(type="presupposes", target="pahclex001",
             note_ef=("The chunk's own EF: the form G01 takes 'in "
                      "communities with a single bishop' - the "
                      "council-around exists only where the bishop "
                      "does."),
             chunk="pahclex006_*"),
        dict(type="associated-with", target="pahclex002",
             note="Symmetric mirror of pahclex002's edge (the same elders, differently configured)."),
    ]),
 "pahclex007": dict(
    period_sense=(
        "The catechesis given before the water: a way of life and a "
        "way of death set plainly before the learner - what must be "
        "put away, what taken up, why a double heart cannot be "
        "trusted; handed on household by household, needing no "
        "office; and the choice itself kept being made after baptism, "
        "not settled at it (chunk Quick/World Meaning)."),
    prior_sense=(
        "The two-ways moral-instruction pattern is older than these "
        "communities (the wider Jewish tradition the Barnabas "
        "parallel attests in the broader record) - but the chunk's "
        "own note rules Barnabas OUT of this world's defined source "
        "set, so the prior is carried as a builder note, UNVERIFIED "
        "within this world's own evidence, exactly as the chunk "
        "bounds it."),
    modern_sense=(
        "A binary moral framework or dualistic worldview (chunk "
        "Modern Hearing)."),
    conceptual_distance_note=(
        "A practical catechetical method for ongoing choosing, not a "
        "philosophical dualism (chunk World Hearing). The S2.1b "
        "watch item LANDS here: single-source by the chunk's own "
        "confidence ('the Didache alone attests it… not established "
        "as this world's network-wide catechetical norm') - the "
        "authored fields never generalize it beyond that cap. "
        "Standard grounding."),
    semantic_domain="catechetical-two-ways",
    grounding_criterion="standard",
    voice_surface=(
        "Before anyone comes to the water we set two roads before "
        "them - a way of life and a way of death - and walk them "
        "through what belongs to each. No office issues this "
        "teaching; any of us entrusted to teach can give it, shaped "
        "to the one receiving it. And the choosing does not end at "
        "the water: the way of life is chosen again, day after day. "
        "Whether every household prepares its members so, our own "
        "record does not tell us."),
    cite="A", weight="load-bearing",
    relations=[
        dict(type="presupposed-by", target="pahclex011",
             note_ef=("Mirror of pahclex011's presupposes edge: "
                      "teaching first, then the washing - the "
                      "chunk's own formation-instruction anchor."),
             chunk="pahclex007_*"),
    ]),
 "pahclex008": dict(
    period_sense=(
        "Spirit-prompted speakers still moving between households - "
        "presiding at the thanksgiving if genuine, tested by the "
        "Didache's own rules (asks money for himself: false; does "
        "not practice what he teaches: false; stays past three days: "
        "questions) - while the same handbook instructs appointing "
        "bishops and deacons 'for they too conduct the ministry of "
        "the prophets and teachers': the charismatic office being "
        "joined, and in places replaced, by the settled ones (chunk "
        "Quick/World Meaning)."),
    prior_sense=(
        "The Greek prophetes and the Jewish prophetic inheritance - "
        "the one who speaks for God - carried into an itinerant "
        "office these communities still received and tested; a "
        "builder note, UNVERIFIED against this build's own docs."),
    modern_sense=(
        "A future-predictor, or an office assumed already vanished "
        "by this period (chunk Modern Hearing)."),
    conceptual_distance_note=(
        "Still active, still fed and housed - but 'their place is "
        "being negotiated alongside emerging local offices' (chunk "
        "World Hearing); single-source per the chunk's own "
        "confidence (the Didache's tests, with Hermas Mandate 11 a "
        "topical parallel the chunk declines to promote). Standard "
        "grounding."),
    semantic_domain="itinerant-prophecy",
    grounding_criterion="standard",
    voice_surface=(
        "Prophets still come to our doors - and we test them, as we "
        "were taught: a true prophet does not ask money for "
        "himself, lives what he teaches, and moves on within a few "
        "days. If he is genuine, he may preside at the thanksgiving. "
        "But we have also begun appointing bishops and deacons who "
        "carry that same ministry - and where a bishop now presides, "
        "the prophet's place at the table is less certain than it "
        "was."),
    cite="A", weight="corroborating",
    relations=[
        dict(type="tension-with", target="pahclex001",
             note_ef=("The chunk's own EF: G01 'from a different "
                      "angle - the shift from charismatic, itinerant "
                      "authority to settled, local office'; symmetric "
                      "mirror on pahclex001."),
             chunk="pahclex008_*"),
        dict(type="associated-with", target="pahclex005",
             note="Didache 15:1 appoints bishops AND deacons for they too conduct the ministry of the prophets and teachers - " + CH + "; symmetric mirror."),
    ]),
 "pahclex009": dict(
    period_sense=(
        "A word known from the OUTSIDE: Pliny's own Latin for the "
        "two enslaved women he tortured for information - "
        "servant-women whose service was important enough to "
        "interrogate. What the communities knew from inside - "
        "whether ministrae translates their own diakonoi, whether "
        "the service was office, whether it was everywhere the same "
        "- their own words do not say (chunk Quick/World Meaning)."),
    prior_sense=(
        "Ordinary Latin ministrae - female servants, attendants - "
        "the governor's own vocabulary reaching for what he saw; "
        "the word is his, not the communities' (the chunk's own "
        "framing: 'the word is his, not ours')."),
    modern_sense=(
        "Either an egalitarian early church matching modern ideals, "
        "or women with no leadership roles at all (chunk Modern "
        "Hearing - the double distortion, both directions wrong)."),
    conceptual_distance_note=(
        "Women in recognized service, attested through an "
        "outsider's report extracted under torture - held honestly "
        "at exactly that evidentiary distance ('we hold the "
        "evidence honestly rather than overclaiming', chunk World "
        "Hearing). The chunk's own confidence SPLITS "
        "Documented(report)/Inferential-Thin(role content); the "
        "conservative side governs this record's confidence, "
        "declared in the migrator. Sharp double-sided gap: high "
        "grounding criterion."),
    semantic_domain="outsider-named-women-servants",
    grounding_criterion="high",
    voice_surface=(
        "This word is not ours - it is the governor's, for two "
        "women of ours he tortured to learn what we do. What he "
        "names is real: women hold recognized service among us. "
        "What their service was in their own eyes, our record does "
        "not give us in their own words - and we will not put words "
        "in the mouths of women who were made to speak under "
        "torture."),
    cite="A", weight="load-bearing",
    relations=[
        dict(type="associated-with", target="pahclex005",
             note_ef=("The chunk's own EF: connecting internal "
                      "service structures to the external pressure "
                      "of Pliny's letter, and marking the limit of "
                      "what the communities' own voices tell."),
             chunk="pahclex009_*"),
        dict(type="associated-with", target="pahclex012",
             note="The Pliny cluster - the same letter's legal category beside its named women; " + CH + "; symmetric mirror."),
        dict(type="associated-with", target="pahclex013",
             note="The Pliny cluster - the charge beside the women interrogated under it; " + CH + "; symmetric mirror."),
    ]),
 "pahclex010": dict(
    period_sense=(
        "The meal that goes by love's own name - feeding stranger, "
        "widow, orphan alongside the household; Ignatius names it "
        "under the bishop's oversight ('not permitted without the "
        "bishop to baptize or to hold an agape'); whether his agape "
        "is the eucharistic meal or a separate table, and whether "
        "Pliny's 'ordinary and harmless food' is the same practice, "
        "the evidence does not settle - both held without forcing "
        "an answer (chunk Quick/World Meaning)."),
    prior_sense=(
        "Agape as the communities' own love-word (the LXX/NT "
        "inheritance) applied as a MEAL's label - love made visible "
        "in shared bread; the label's application, not the word, is "
        "what this entry tracks (chunk framing)."),
    modern_sense=(
        "Agape and eucharist assumed either always separate or "
        "always identical (chunk Modern Hearing)."),
    conceptual_distance_note=(
        "The relationship 'is still being worked out, varying from "
        "community to community' (chunk World Hearing) - an "
        "unresolved-identity entry whose whole discipline is not "
        "forcing the identification; the entry's own correction "
        "note (an earlier draft mis-stated the primary anchoring; "
        "fixed against Smyrnaeans 8's Greek) rides the chunk "
        "verbatim. Standard grounding."),
    semantic_domain="love-feast-label",
    grounding_criterion="standard",
    voice_surface=(
        "We share a meal that carries love's own name. What we do "
        "there - the stranger fed beside the household - is love "
        "made visible in bread and cup. Whether the agape Ignatius "
        "sets under the bishop and the harmless meal Pliny's "
        "prisoners described are one table or two, we do not force "
        "our evidence to say."),
    cite="A", weight="corroborating",
    relations=[
        dict(type="associated-with", target="pahclex004",
             note_ef=("The chunk's own EF bridge: agape <-> "
                      "eucharistia within the worship cluster."),
             chunk="pahclex010_*"),
        dict(type="associated-with", target="pahclex012",
             note=("The chunk's own EF bridge: agape <-> hetaeria - "
                   "what the communities called love, outsiders "
                   "assessed as association; symmetric mirror.")),
    ]),
 "pahclex011": dict(
    period_sense=(
        "The water, the threshold: teaching first (the Two Ways), "
        "then fasting, then the washing - running water if you can, "
        "still water if not, pouring three times if neither, in the "
        "threefold name; the flexibility itself the teaching (the "
        "heart is the washing and what precedes it, not the "
        "method); after the water, the table; under Strand-A "
        "letters, under the bishop's oversight (chunk Quick/World "
        "Meaning)."),
    prior_sense=(
        "The ordinary Greek baptisma - dipping, washing - an "
        "everyday water-word made the threshold of a life; a "
        "builder note, UNVERIFIED against this build's own docs."),
    modern_sense=(
        "A uniform practice, or later debates about mode and timing "
        "projected back (chunk Modern Hearing)."),
    conceptual_distance_note=(
        "Genuine variation (running, still, poured) holding one "
        "common pattern: teaching, washing, table (chunk World "
        "Hearing). The Rule-A-dropped alias surface 'the water' is "
        "carried at runtime by this world's own exact A-gloss ('the "
        "water'->'baptism') - the S2.2 drop and the SS4 gloss "
        "design meeting as intended, noted for the record. Standard "
        "grounding."),
    semantic_domain="water-threshold",
    grounding_criterion="standard",
    voice_surface=(
        "We call it the water. Before it, the teaching and the "
        "fast; at it, running water if we have it, still if we do "
        "not, poured three times if we have neither - the washing "
        "matters, not the plumbing. And after the water, the "
        "table: baptism opens that door. Where a bishop presides, "
        "the water comes under his oversight; where none does, it "
        "is no less the water."),
    cite="A", weight="load-bearing",
    relations=[
        dict(type="presupposes", target="pahclex007",
             note_ef=("The chunk's own EF: the threshold 'after "
                      "catechesis and before the table' - teaching "
                      "first."),
             chunk="pahclex011_*"),
        dict(type="presupposed-by", target="pahclex004",
             note="Mirror of pahclex004's presupposes edge (the door to the table)."),
        dict(type="associated-with", target="pahclex001",
             note="Symmetric mirror of pahclex001's edge (Strand-A oversight of the water)."),
    ]),
 "pahclex012": dict(
    period_sense=(
        "What Romans suspected the communities might BE: an illegal "
        "club, a forbidden association - the charge never the whole "
        "of what they faced, and the category itself uncertain in "
        "Roman hands (chunk Quick Meaning + World Hearing; a "
        "thin-format entry by the S2.1a declaration)."),
    prior_sense=(
        "Pliny's own Latin use of the Greek loan hetaeria - the "
        "club, the sodality, the association Roman law watched - "
        "the outsider's legal category IS the prior; nothing "
        "in-community transformed it (the chunk's outside-word "
        "framing)."),
    modern_sense=(
        "Christians persecuted primarily as an illegal organization "
        "(chunk Modern Hearing)."),
    conceptual_distance_note=(
        "The chunk's own Inferential-Thin cap: that hetaeria was "
        "the operative legal category, rather than an assumption "
        "the investigating authority brought, 'is asserted, not "
        "confirmed, by this world's own evidentiary base.' Standard "
        "grounding; the record never firms the category."),
    semantic_domain="outsider-legal-category",
    grounding_criterion="standard",
    voice_surface=(
        "The Romans had a word ready for what we might be: a club, "
        "an association, the kind the law forbids. It was never "
        "the whole of what we faced - and whether it was ever "
        "truly the charge, or only the shelf the governor first "
        "reached for, even the report that gives us the word does "
        "not say."),
    cite="B", weight="corroborating",
    relations=[
        dict(type="associated-with", target="pahclex010",
             note=("Symmetric mirror of pahclex010's edge: what the "
                   "communities called love, outsiders assessed as "
                   "association (the chunk-attested bridge)."),),
        dict(type="associated-with", target="pahclex013",
             note=("The two Pliny legal terms - the category "
                   "suspected (hetaeria) and the conduct punished "
                   "(pertinacia), both thin by their own "
                   "confidence; symmetric both ways.")),
        dict(type="associated-with", target="pahclex009",
             note="Symmetric mirror of pahclex009's Pliny-cluster edge."),
    ]),
 "pahclex013": dict(
    period_sense=(
        "What Pliny found punishable: not the content of belief but "
        "the refusal to recant when given the chance - stubbornness "
        "as the operative ground, while his own report leaves open "
        "whether the name itself or the conduct merited punishment "
        "(chunk Quick Meaning + World Hearing; thin-format entry by "
        "the S2.1a declaration)."),
    prior_sense=(
        "Roman moral vocabulary: pertinacia as the vice of "
        "obstinacy - a Roman's word for a Roman's complaint; the "
        "outsider's charge IS the prior (the chunk's framing)."),
    modern_sense=(
        "Christians persecuted for specific beliefs or practices "
        "(chunk Modern Hearing)."),
    conceptual_distance_note=(
        "The chunk's own Inferential-Thin cap: 'a charge whose own "
        "core question the source that reports it leaves open' - "
        "the record carries the openness, never resolves it. "
        "Standard grounding."),
    semantic_domain="outsider-legal-charge",
    grounding_criterion="standard",
    voice_surface=(
        "What the governor punished, by his own account, was not "
        "what we believe but that we would not stop saying it. "
        "Stubbornness, he called it. Whether the name alone or the "
        "refusal was the crime, his own letter asks and does not "
        "answer - and we cannot answer it for him."),
    cite="B", weight="corroborating",
    relations=[
        dict(type="associated-with", target="pahclex012",
             note="Symmetric mirror of pahclex012's edge (the Pliny legal pair)."),
        dict(type="associated-with", target="pahclex009",
             note="Symmetric mirror of pahclex009's Pliny-cluster edge."),
    ]),
}


def verify_gloss_map():
    from app.prompts.confirmed_glosses import CONFIRMED_GLOSSES
    live = {g.original for g in
            CONFIRMED_GLOSSES["post-apostolic-house-church"]}
    assert live == set(GLOSS_MAP), (live ^ set(GLOSS_MAP))
    for original, rid in GLOSS_MAP.items():
        if rid is None:
            continue
        front, _ = read_record(TERM_DIR / f"{rid}.md")
        key = original.lower()
        hay = (front["term"] + " " + front.get("quick_meaning", "")
               + " " + " ".join(front.get("aliases") or [])).lower()
        assert key in hay or key == "the water", (original, rid)
    n = sum(1 for v in GLOSS_MAP.values() if v)
    print(f"gloss map verified in view: {n}/15 resolve to term records; "
          f"3 Sunday circumlocutions (no term record by design); "
          f"'the water' -> pahclex011 via the exact A-gloss (its alias "
          f"Rule-A-dropped at birth - the SS4 carrier)")


def main():
    verify_gloss_map()
    n = 0
    for rid, data in AUTH.items():
        path = TERM_DIR / f"{rid}.md"
        front, body = read_record(path)
        fc = extract_confidence(front, rid)
        script = extract_script(front.get("term", ""))
        for key in ("period_sense", "prior_sense", "modern_sense",
                    "conceptual_distance_note", "semantic_domain",
                    "grounding_criterion", "voice_surface"):
            front[key] = data[key]
        if script:
            front["original_script"] = script
        front["confidence"] = {
            "citation_specificity": data["cite"],
            "verification_state": "verified-via-authority",
            "verification_date": VDATE,
            "evidentiary_weight": data["weight"],
            "formation_confidence": fc,
        }
        rels = []
        for r in data["relations"]:
            note = r.get("note", "")
            if "note_ef" in r:
                note = ef_note(r["note_ef"], r["chunk"])
            rels.append({"type": r["type"], "target_id": r["target"],
                         "note": note})
        front["field_relations"] = rels
        write_record(path, front, body)
        n += 1
    print(f"authored {n} term records (formation_confidence EXTRACTED "
          f"from the chunks' own Confidence blocks; original_script "
          f"extracted from Term parens)")


if __name__ == "__main__":
    main()
