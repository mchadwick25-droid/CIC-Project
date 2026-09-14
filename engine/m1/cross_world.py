"""Cross-world consistency checks (the fleet-level counterpart to gates.py).

gates.py asks "is THIS world well-formed?" and every one of its fifteen gates
runs against one world's records in isolation. That is the right shape for
everything it checks, and it is why the whole battery is green on all six
formation worlds while the fleet still holds real, participant-visible
inconsistencies: nothing in it can see two worlds at once, so nothing in it
can notice that five worlds answer a question one way and the sixth answers
it another. This module is that missing view.

The line it polices is the one the 2026-08-26 cross-system consistency audit
drew (world-build-docs/_cross-world/CiC_Cross_System_Consistency_Audit_
2026-08-26.md): a world may differ from its siblings in SUBSTANCE - how many
terms it holds, how rich its quote corpus is, which cells it can only answer
with an honest limit - and may never differ in the SHAPE the pipeline moves
that substance through. Six different historical records are supposed to look
different. Six identical pipelines are not.

Two severities, and the difference matters:

  DEFECT      a contract this file states is broken. Never expected. Any
              defect not named in ACCEPTED_OPEN fails the run.
  OBSERVATION a per-world measurement with no fixed contract (retrieval-hint
              coverage, optional-field adoption). Printed for a human, never
              failed on - the numbers are the point, not a threshold.

ACCEPTED_OPEN is how a KNOWN, DOCUMENTED defect stays visible instead of
being suppressed: each entry names the audit finding that owns it and the
thread the repair belongs to. A defect with no entry is new drift, and new
drift fails. Removing an entry is what "fixed" means here.

    python -m engine.m1.cross_world          # full report, exit 1 on new drift
    python -m engine.m1.cross_world --all    # also print accepted-open detail
"""
import json
import re
import sys

from engine.m1.loader import RECORDS_ROOT, load_world_records
from engine.m1.registry import REPO_ROOT, formation_world_keys, load_registry

CENSUS_PATH = REPO_ROOT / "cic-website" / "data" / "world-census.json"
APP_WORLDS_TS = REPO_ROOT / "cic-poc" / "frontend" / "src" / "data" / "worlds.ts"
SITE_TRADITIONS_DIR = REPO_ROOT / "cic-website" / "traditions"

DEFECT = "defect"
OBSERVATION = "observation"

# Every defect below is keyed <check-id>/<world-or-scope>. An entry here says:
# this one is known, it is written up, and it is somebody's named next step -
# not that it is acceptable. See the audit doc for each finding's evidence.
ACCEPTED_OPEN: dict[str, str] = {
    "census-living-flag/alx": "F-06 - census `living` says false, registry says true; which is correct is Mark's own per-world Living Tradition touchpoint, not a build thread's to settle",
    "census-living-flag/pahc": "F-06 - as alx",
    "census-living-flag/hal": "F-06 - as alx",
    "census-living-flag/ijc": "F-06 - as alx",
    # F-07/F-08 CLOSED 2026-08-28 by Mark's identity ruling ("the registry
    # wins"): the census now derives its representative name/title from
    # records/worlds.yaml (syr's registry entry took the ruled values Mar
    # Yausep / Teacher of the Covenant Order), so these five accepted-open
    # entries are deleted and the checks ENFORCE - identity drift between
    # the Atlas and the room fails the run from here on.
    "census-display-name/alx": "F-09 - alx alone sets display_name to the Atlas's friendly short name; the other five carry the census's formal name",
    "id-type-token/doctrinal_witness": "F-03 - pahc uses `pahc.witness.*` where the other five use `<world>.dw.*`; renaming 17 records re-hashes the package, so it belongs to a pahc build thread",
    "id-type-token/voice_craft": "F-03 - pahc uses `pahc.craft.chloe-voice` where the other five use `<world>.voice.craft`",
    "figure-dates-keys/pahc": "F-04 - pahc keys figure.dates as display/note where the other five use born/died/floruit, and the frontend prints the key verbatim, so pahc participants read 'display:' and 'note:' in the UI",
    "figure-dates-keys/cappadocian": "F-04-analogue - all 15 cappadocian figure records key figure.dates as `display` (one-sentence prose covering contested/multi-clause dating - e.g. Basil's own death 'traditionally placed at January 379 or September 378, though the modern redating literature argues for 377 instead' - that doesn't reduce cleanly to born/died/floruit without losing the contested-date nuance itself). Found 2026-09-01 while wiring the Representative portrait; same disclosed-not-fixed disposition as pahc's own instance, not a mass rewrite improvised under this step - belongs to a cappadocian build thread.",
    "quote-speaker-label/syr": "F-05 - four syr quotes name a `syr.source.*` record as speaker_or_author; the label resolvers only unwrap `figure` ids, so the raw record id reaches both the Level-3 card and the compiled prompt's quote index",
    "ui-field-leak/desert": "F-10 - desert.figure.evagrius names a record id (desert.source.evagrius-praktikos) and a build document (Doc_01) inside figure.dates, and desert.figure.pachomius says 'not independently adjudicated by this build' - all three printed verbatim by the doorway's Level-3 panel",
    "figure-dates-keys/don": "F-04-analogue - all 24 don figure records key figure.dates as `display`, the same pattern and the same reason as figure-dates-keys/cappadocian above: this world's own dating is pervasively contested or multi-clause (two Marcellinuses roughly a century apart, three Felixes, disputed Passio dating with two vendored authorities disagreeing by over two decades) and does not reduce to born/died/floruit without losing the disclosed uncertainty itself. Same disclosed-not-fixed disposition, found compiling the world rather than wiring a portrait - belongs to a don build thread, not a mass rewrite improvised here.",
    "app-world-assets/don": "Record-native compilation, 2026-09-10: Phase C deployment wiring (app/world_manifest.py, WORLD_ASSETS, frontend hand-sync points) was never in scope for the record-native compile (Phase B) this entry covers - it is the next, separate phase per reference/method/CiC_Record_Native_World_Build_Process_V1_3.md SS4, and belongs to whoever picks up Donatism's own go-live work.",
    "app-world-order/don": "Record-native compilation, 2026-09-10: as app-world-assets/don - deployment wiring, out of scope for this compile, deferred to Donatism's own Phase C work.",
    "site-portrait/don": "Record-native compilation, 2026-09-10: as app-world-assets/don - the traditions/donatism.html portrait page is deployment wiring, out of scope for this compile, deferred to Donatism's own Phase C work.",
}


# FIRST-PASS coverage ranges, asserted here for Mark's correction, not derived.
# A volume's own dates cannot be read off the file mechanically, and guessing
# them silently would be worse than stating them where they can be argued
# with. Range = the span the volume's contents actually testify to, so a
# history written in the 440s about 305-439 carries the span it covers, not
# its composition date. Overlap with a world's `time_window` is what puts a
# volume in that world's scope.
COVERAGE = {
    "addai": (30, 400), "anf01": (90, 202), "anf02": (100, 215), "anf03": (155, 240),
    "anf04": (155, 254), "anf05": (170, 258), "anf06": (200, 311), "anf07": (90, 380),
    "anf08": (100, 400), "anf09": (150, 254), "aphrahat": (336, 345),
    "chronicle-of-edessa": (130, 540), "ephraim": (306, 373),
    "npnf101": (354, 430), "npnf102": (354, 430), "npnf103": (354, 430), "npnf104": (354, 430),
    "npnf105": (354, 430), "npnf106": (354, 430), "npnf107": (354, 430), "npnf108": (354, 430),
    "npnf109": (349, 407), "npnf110": (349, 407), "npnf111": (349, 407), "npnf112": (349, 407),
    "npnf113": (349, 407), "npnf114": (349, 407),
    "npnf201": (260, 339), "npnf202": (305, 439), "npnf203": (340, 466), "npnf204": (296, 373),
    "npnf205": (335, 395), "npnf206": (347, 420), "npnf207": (313, 390), "npnf208": (330, 379),
    "npnf209": (310, 749), "npnf210": (339, 397), "npnf211": (360, 450), "npnf212": (400, 604),
    "npnf213": (300, 604), "npnf214": (325, 787), "optatus": (320, 400),
    "origen": (185, 254), "palladius": (320, 420),
    # Added 2026-09-09. These eighteen files (fourteen keys) had NO entry, so
    # corpus_tier() fell through to "4 - unclassified" and the generated report
    # rendered them under a Tier 4 heading whose legend reads "no time overlap"
    # - asserting a date judgement that had never been made. Philostorgius is
    # the case that surfaced it: his History covers 300-425 against ijc's
    # 312-451, a 113-year overlap, and it sat at the bottom rank of six worlds'
    # worklists because nobody had ever entered its dates. Same first-pass
    # standard as every row above: asserted for correction, and they RANK
    # rather than exclude.
    "anan-isho": (270, 650),          # Egyptian desert material, compiled by Ananisho c. 7th c.
    "basil": (330, 379),              # Basil of Caesarea
    "eunomius": (335, 393),           # Eunomius of Cyzicus
    "evagrius": (345, 399),           # Evagrius Ponticus
    "gregory-nazianzen": (329, 390),
    "gregory-nyssa": (335, 395),
    "julian": (331, 363),             # the emperor's own letters and apologia
    "lucian": (125, 180),             # Lucian of Samosata
    "macarius": (300, 400),           # Fifty Spiritual Homilies, late 4th c.
    "morison": (330, 379),            # a 1912 study OF Basil - covers his period, not its own
    "nestle1904": (30, 100),          # Greek New Testament
    "pachomius": (292, 348),
    "philostorgius": (300, 425),      # the History's own span, per the file's Quasten note
    "tacitus": (64, 64),              # the vendored locus is Annals 15.44 alone: the persecution of 64
    # Added 2026-09-09, source-library-integration merge. 14 more keys (17
    # vendored files - 2 for the 3 Monceaux tomes sharing one key, - 1 because
    # `optatus_libri-vii-critical_ziwsa1893.txt` shares the pre-existing
    # `optatus` key and needs no new entry) with no COVERAGE entry - the same
    # defect this file's own 2026-09-09 fix above closed for 14 other keys,
    # reopened by this merge if left unfilled. Same first-pass standard:
    # asserted for correction, rank rather than exclude.
    #
    # The Theodosian Code entries need particular care rather than a single
    # "5th century" guess: it is a compilation, issued 438, of constitutions
    # spanning Constantine's accession (312) through Theodosius II - both
    # endpoints load-bearing, not the compilation date alone. Same range for
    # `theodosianus-16` (Mommsen-Meyer, all 16 books, despite its own staging
    # note's "Book 16" title - see the corpus-map commit) and
    # `codex-theodosianus` (Latin Library transcription, same full text), and
    # for `boyd` (a modern study of the same code's ecclesiastical edicts,
    # covering the code's own span rather than its 1905 publication date -
    # the same "study covers its subject's period" logic already applied to
    # `morison` above).
    "theodosianus-16": (312, 437),    # Constantine's accession through Theodosius II; a compilation, not one date
    "codex-theodosianus": (312, 437), # same text, different vendored transcription - see theodosianus-16
    "boyd": (312, 437),               # 1905 study OF the same code's ecclesiastical edicts, not this study's own date
    # Cyprian: his own episcopate and writing career (elected bishop c. 248,
    # martyred 258), not anf05's broader (170, 258) which also covers
    # Hippolytus and Novatian.
    "cyprian": (248, 258),
    # Augustine's own Latin corpus (Goldbacher's CSEL57 letters; Petschenig's
    # CSEL51/53 anti-Donatist treatises) - his own lifespan, same convention
    # already used for the English NPNF101-108 volumes of the same works.
    "augustine": (354, 430), "augustini": (354, 430),
    # Possidius: Augustine's own companion; the Vita narrates Augustine's full
    # life (354-430) and was itself composed shortly after his death, c. 432.
    "possidius": (354, 432),
    # Tyconius: floruit, not attested birth/death. Liber Regularum was written
    # before 383 per Augustine's own reference to it (Doc_01 SS4 of this
    # entry's own build thread leaves his formal communion status open).
    "tyconius": (370, 400),
    # Gregory the Great's own pontificate (590-604) - the Epistolae Selectae
    # are his own correspondence written during it, addressing the surviving
    # African Donatist remnant from Rome. Matches npnf212/213's own treatment
    # of Gregory the Great (upper bound 604).
    "gregory-great": (590, 604),
    # Liber Genealogus: an anonymous North African chronicle whose own
    # regnal/persecution notices read (per Monceaux) as Donatist-affiliated.
    # 303 is the Diocletianic persecution that starts the traditores dispute
    # at the schism's own origin; 427 is the Mommsen-catalogued A recension's
    # own compilation date - the latest point this specific vendored text
    # itself can be dated to.
    "chronica-minora-liber-genealogus": (303, 427),
    # CIL VIII Numidia: a collective epigraphic corpus, "inscriptions from
    # many hands across centuries" per this file's own authors_ruled entry -
    # broad range reflects that collective, multi-century nature honestly
    # rather than picking one date for a corpus that spans many.
    "cil8-supplementum-numidiae": (100, 700),
    # Monceaux (1912/1920/1922): modern secondary scholarship, its three
    # vendored tomes covering the Donatist movement's own historical span
    # (Tome IV, the movement as a whole; Tome V, Optatus and the earliest
    # Donatist writers; Tome VI, Donatist literature "in Augustine's own
    # generation") - not this study's own early-20th-century publication
    # dates. Same "study covers its subject's period" logic as `morison` and
    # `boyd` above.
    "monceaux": (303, 430),
    # Monumenta Vetera ad Donatistarum Historiam Pertinentia (Mabillon, in
    # Migne PL8): dated directly from this file's own staging entry - item 1
    # c. 340 (persecution under Leontius and Ursatius), items 2-3 both 348
    # (the Passio Marculi and the Passio Isaac et Maximiani).
    "monumenta-vetera-donatistarum": (340, 348),
    # PL11's Optatus/Donatism cluster: only the Collatio Carthaginiensis (the
    # 411 Conference of Carthage's own acts) is in scope for this vendored
    # file's assignment - Zeno of Verona's own works, cols 9-751ish, are this
    # same volume's unrelated majority and are explicitly out of scope per
    # this file's own staging note. One year, same convention as `tacitus`.
    "pl11-zeno-optatus-collatio-carthaginiensis": (411, 411),
}
BY_DESIGN = {"webbe", "anf10"}

# Geography, added on Mark's ruling 2026-08-26 ("if geography is a defining
# element of the christian tradition, then yes add it"). It is - and it does
# work dates cannot: `pahc` is Greek-speaking Antioch and Asia Minor while
# `syr` is Syriac-speaking Mesopotamia, two different worlds that overlap
# almost entirely in time. Tags are FIRST-PASS, asserted for correction like
# COVERAGE, and they RANK rather than exclude: Mark's standard is that a
# resource may be ranked low and never ignored, so a region mismatch demotes
# a volume in the worklist and never removes it.
REGIONS = {
    "addai": {"syriac-mesopotamia"},
    "anf01": {"rome", "syria", "asia-minor", "gaul"},
    "anf02": {"rome", "syria", "greece", "egypt"},
    "anf03": {"north-africa"},
    "anf04": {"north-africa", "rome", "egypt"},
    "anf05": {"rome", "north-africa"},
    "anf06": {"asia-minor", "egypt", "palestine", "north-africa"},
    "anf07": {"north-africa", "syria", "asia-minor"},
    "anf08": {"syriac-mesopotamia", "rome"},
    "anf09": {"syriac-mesopotamia", "egypt", "palestine"},
    "aphrahat": {"syriac-mesopotamia"},
    "chronicle-of-edessa": {"syriac-mesopotamia"},
    "ephraim": {"syriac-mesopotamia"},
    "npnf101": {"north-africa"}, "npnf102": {"north-africa"}, "npnf103": {"north-africa"},
    "npnf104": {"north-africa"}, "npnf105": {"north-africa"}, "npnf106": {"north-africa"},
    "npnf107": {"north-africa"}, "npnf108": {"north-africa"},
    "npnf109": {"syria", "constantinople"}, "npnf110": {"syria", "constantinople"},
    "npnf111": {"syria", "constantinople"}, "npnf112": {"syria", "constantinople"},
    "npnf113": {"syria", "constantinople"}, "npnf114": {"syria", "constantinople"},
    # Added 2026-09-09 alongside the COVERAGE rows below - a key with coverage
    # but no region lands in tier 3 ("same time, different region"), which
    # understates rather than mislabels, but is still wrong where the region
    # is known.
    "anan-isho": {"egypt"}, "basil": {"asia-minor"},
    "eunomius": {"asia-minor", "constantinople"}, "evagrius": {"egypt"},
    "gregory-nazianzen": {"asia-minor"}, "gregory-nyssa": {"asia-minor"},
    "julian": {"constantinople", "asia-minor", "gaul"},
    "lucian": {"syria", "greece"}, "macarius": {"egypt", "syria"},
    "morison": {"asia-minor"}, "nestle1904": {"ecumenical"},
    "pachomius": {"egypt"},
    # ecumenical for the same reason npnf202 (Socrates/Sozomen) is: a
    # continuous ecclesiastical history of empire-wide councils and imperial
    # religious policy, not a regional witness.
    "philostorgius": {"ecumenical"},
    "tacitus": {"rome"},
    # Added 2026-09-09, source-library-integration merge, alongside the
    # COVERAGE rows above. Imperial law is ecumenical (empire-wide, not
    # regional); everything else here is Donatist-controversy North African
    # material, per this same file's own atlas_ids assignment to `donatism`
    # in the corpus-map staging commit - except `gregory-great`, whose own
    # letters were written from Rome (matching npnf212/npnf213's existing
    # region for the same author), even though their subject is the African
    # remnant.
    "theodosianus-16": {"ecumenical"}, "codex-theodosianus": {"ecumenical"},
    "boyd": {"ecumenical"},
    "cyprian": {"north-africa"}, "augustine": {"north-africa"},
    "augustini": {"north-africa"}, "possidius": {"north-africa"},
    "tyconius": {"north-africa"}, "gregory-great": {"rome"},
    "chronica-minora-liber-genealogus": {"north-africa"},
    "cil8-supplementum-numidiae": {"north-africa"},
    "monceaux": {"north-africa"},
    "monumenta-vetera-donatistarum": {"north-africa"},
    "pl11-zeno-optatus-collatio-carthaginiensis": {"north-africa"},
    "npnf201": {"palestine"},
    "npnf202": {"ecumenical"},
    "npnf203": {"syria", "palestine", "rome", "egypt"},
    "npnf204": {"egypt"},
    "npnf205": {"asia-minor"},
    "npnf206": {"palestine", "rome"},
    "npnf207": {"palestine", "asia-minor", "constantinople"},
    "npnf208": {"asia-minor"},
    "npnf209": {"gaul", "syria"},
    "npnf210": {"italy"},
    "npnf211": {"gaul", "egypt"},
    "npnf212": {"rome"},
    "npnf213": {"rome", "syriac-mesopotamia"},
    "npnf214": {"ecumenical"},
    "optatus": {"north-africa"},
    "origen": {"egypt", "palestine"},
    "palladius": {"egypt", "palestine", "constantinople"},
}

# Read off each world's own registry `place` field, not invented beside it.
WORLD_REGIONS = {
    "alx": {"egypt"},
    "pahc": {"syria", "asia-minor", "rome"},
    "desert": {"egypt", "palestine"},
    "hal": {"palestine", "rome"},
    "syr": {"syriac-mesopotamia"},
    "ijc": {"rome", "constantinople", "italy"},
}


# WHY THERE IS NO THIRD, THEOLOGICAL AXIS HERE, and why one must not be added.
#
# Mark, 2026-08-26: "there has to be a theological center, as the gnostics are
# the same time and place as alexandria but they are not a part of the
# christian tradition." Correct, and the project already enforces it - twice,
# and in the right places, neither of which is corpus scope:
#
#   * At WORLD level: cic-website/data/world-census.json carries `beyondFloor`
#     and the status "Excluded - Doctrinal Floor (C1)". Valentinian/Gnostic
#     Christianities are named there explicitly, beside Marcion, Manichaeism
#     and Homoian-Arian Christianity. All six live worlds are beyondFloor:
#     false. No excluded movement can become a world.
#   * At RECORD level: the `register` field. `emic` is the world's own voice;
#     `etic` is a thing described from outside it.
#
# Corpus scope answers a different question from the floor: scope decides what
# a world may READ, the floor decides what it may CLAIM AS ITS OWN VOICE.
# Collapsing them would be actively wrong - alx has to be able to read
# Irenaeus and Clement on the Gnostics precisely in order to say what it held
# against them.
#
# A naive check ("emic record mentioning a floor-excluded movement") was
# measured before being rejected: it fires on 30 records across four worlds
# and is wrong on essentially all of them. alx.force.gnostic-challenge is
# emic because it is Alexandria's OWN EXPERIENCE of its rivals; syr.dw.god is
# emic because it is this world confessing "against Marcion it held that the
# Maker of this world is the Father of Jesus." Both are the floor working, not
# failing. Whether a record presents an excluded movement's theology AS the
# world's own belief is a judgment about what a sentence asserts, and no
# pattern available here can make it. It belongs to review, not to a gate.
#
# One case is worth a human's eye rather than a check: ijc carries nine emic
# records touching Homoian/Arian material and a `homoian-recentering` entry in
# its voice_craft flavor notes, while the census lists Homoian-Arian
# Christianity as floor-excluded. That is a deliberate editorial choice - the
# defeated side's story, told by the world that defeated it - and its own
# thinness statement already names "the defeated Homoian side's own voice" as
# thin. Deliberate, documented, and closest to the line of anything in the
# fleet.


def corpus_tier(filename: str, world_key: str, world_window: dict, *, named: bool) -> str:
    """Mark's ranking, in one place. Nothing here returns "excluded"."""
    key = corpus_key(filename)
    if key in BY_DESIGN:
        return "by design"
    if named:
        return "1 - named, never opened"
    lo, hi = COVERAGE.get(key, (None, None))
    if lo is None:
        return "4 - unclassified"
    in_time = not (hi < world_window["start"] or lo > world_window["end"])
    regions = REGIONS.get(key, set())
    in_place = bool(regions & (WORLD_REGIONS.get(world_key, set()) | {"ecumenical"})) or "ecumenical" in regions
    if in_time and in_place:
        return "2 - same time and place"
    if in_time:
        return "3 - same time, different region"
    return "4 - outside this window"

# The principal authors each volume carries, from its own title. Used for the
# one signal in this report that is DERIVED rather than asserted: a world that
# already names a figure in its records, and has never opened that figure's
# own vendored works, is reaching them second-hand. That is measurable, and it
# is how Basil surfaced. Date overlap alone is far too blunt - it puts the
# Chronicle of Edessa on Alexandria's list - so it sets the candidate pool
# only, and this narrows it to what a human should look at first.
AUTHORS = {
    "anf01": ["Clement of Rome", "Ignatius", "Polycarp", "Justin", "Irenaeus"],
    "anf02": ["Hermas", "Tatian", "Athenagoras", "Theophilus", "Clement of Alexandria"],
    "anf03": ["Tertullian"], "anf04": ["Tertullian", "Minucius Felix", "Origen"],
    "anf05": ["Hippolytus", "Cyprian", "Novatian"],
    "anf06": ["Gregory Thaumaturgus", "Dionysius", "Julius Africanus", "Methodius", "Arnobius"],
    "anf07": ["Lactantius"], "anf09": ["Origen"],
    "aphrahat": ["Aphrahat"], "ephraim": ["Ephrem", "Ephraim"],
    "npnf101": ["Augustine"], "npnf102": ["Augustine"], "npnf103": ["Augustine"],
    "npnf104": ["Augustine"], "npnf105": ["Augustine"], "npnf106": ["Augustine"],
    "npnf107": ["Augustine"], "npnf108": ["Augustine"],
    "npnf109": ["Chrysostom"], "npnf110": ["Chrysostom"], "npnf111": ["Chrysostom"],
    "npnf112": ["Chrysostom"], "npnf113": ["Chrysostom"], "npnf114": ["Chrysostom"],
    "npnf201": ["Eusebius"], "npnf202": ["Socrates", "Sozomen"],
    "npnf203": ["Theodoret", "Jerome", "Rufinus"], "npnf204": ["Athanasius"],
    "npnf205": ["Gregory of Nyssa"], "npnf206": ["Jerome"],
    "npnf207": ["Cyril of Jerusalem", "Gregory Nazianzen", "Nazianz"],
    "npnf208": ["Basil"], "npnf209": ["Hilary"], "npnf210": ["Ambrose"],
    "npnf211": ["Sulpitius", "Vincent of Lerins", "Cassian"],
    "npnf212": ["Leo"], "npnf213": ["Ephrem", "Aphrahat"], "npnf214": ["Nicaea", "Chalcedon"],
    "optatus": ["Optatus"], "origen": ["Origen"], "palladius": ["Palladius"],
}


def corpus_key(filename: str) -> str:
    return re.split(r"[_.]", filename)[0]


_TEXTS_DIR = REPO_ROOT / "cic" / "texts"
_AUTHORS_BY_FILE = {
    p.name: AUTHORS[corpus_key(p.name)]
    for p in (_TEXTS_DIR.iterdir() if _TEXTS_DIR.is_dir() else [])
    if p.suffix in (".xml", ".txt") and corpus_key(p.name) in AUTHORS
}


# --------------------------------------------------------------------------
# finding plumbing
# --------------------------------------------------------------------------

class Finding:
    __slots__ = ("check", "scope", "severity", "message")

    def __init__(self, check: str, scope: str, severity: str, message: str):
        self.check, self.scope, self.severity, self.message = check, scope, severity, message

    @property
    def key(self) -> str:
        return f"{self.check}/{self.scope}"

    def __repr__(self) -> str:
        return f"{self.severity.upper():11} {self.key:44} {self.message}"


def _defect(check, scope, message) -> Finding:
    return Finding(check, scope, DEFECT, message)


def _observation(check, scope, message) -> Finding:
    return Finding(check, scope, OBSERVATION, message)


# --------------------------------------------------------------------------
# stage 1: the registry against itself
# --------------------------------------------------------------------------

def check_registry_shape(*, registry, worlds, **_) -> list[Finding]:
    """Every formation world's registry entry carries the same key set. A
    world that is simply MISSING a key the others have is the exact shape of
    the desert deep-link defect this audit started from - `census_id: null`
    read as "no Atlas entry" by every consumer, when the Atlas entry existed
    all along."""
    findings = []
    keysets = {w: set(registry[w]) for w in worlds}
    universe = set().union(*keysets.values())
    for w in worlds:
        for missing in sorted(universe - keysets[w]):
            findings.append(_defect("registry-key-set", w, f"registry entry has no {missing!r} key; the other formation worlds do"))
        for key in sorted(universe):
            if key in keysets[w] and registry[w][key] is None:
                findings.append(_defect("registry-null-field", f"{w}.{key}", f"{key} is null; every other consumer reads that as 'this world has none'"))
    return findings


def check_package_pinned(*, registry, worlds, **_) -> list[Finding]:
    """Every world is load-verified against the manifest hash pinned here
    (engine.m4.world_loader refuses on any mismatch). A world missing either
    half of that pin is one the runtime cannot refuse to serve wrong."""
    findings = []
    for w in worlds:
        pkg = registry[w].get("package") or {}
        for field in ("location", "manifest_hash"):
            if not pkg.get(field):
                findings.append(_defect("package-pin", w, f"package.{field} is missing - the world cannot be load-verified"))
        location = pkg.get("location")
        if location and not (REPO_ROOT / location / "manifest.json").is_file():
            findings.append(_defect("package-pin", w, f"package.location {location!r} has no manifest.json on disk"))
    return findings


# --------------------------------------------------------------------------
# stage 2: the registry against the Atlas census (the other surface)
# --------------------------------------------------------------------------

def _census_live_entries() -> dict[str, dict]:
    if not CENSUS_PATH.is_file():
        return {}
    census = json.loads(CENSUS_PATH.read_text(encoding="utf-8"))
    return {m["id"]: m for m in census.get("movements", []) if m.get("status") == "Built & Live"}


def check_census_link(*, registry, worlds, **_) -> list[Finding]:
    """The Atlas deep link is `?worlds=<census entry id>` (cic-website/
    index.html, atlas-v3.html's own `data-aid="${m.id}"`), and the app
    matches it against the registry's census_id (App.tsx's
    findWorldByCensusId). A census_id that does not resolve to a live census
    entry is a deep link that can never match - the participant lands on the
    world list instead of the world they clicked."""
    findings = []
    live = _census_live_entries()
    if not live:
        return [_defect("census-file", "fleet", f"no Built & Live entries readable at {CENSUS_PATH}")]
    for w in worlds:
        cid = registry[w].get("census_id")
        if not cid:
            findings.append(_defect("census-id", w, "census_id is unset - the Atlas deep link for this world can never match, and it falls through to the world list"))
        elif cid not in live:
            findings.append(_defect("census-id", w, f"census_id {cid!r} is not a 'Built & Live' entry in world-census.json"))
    claimed = {registry[w].get("census_id") for w in worlds}
    for cid in sorted(set(live) - claimed):
        findings.append(_defect("census-orphan", cid, "census entry is marked 'Built & Live' but no registry world claims it"))
    return findings


def check_census_agreement(*, registry, worlds, **_) -> list[Finding]:
    """The registry is the ONE world registry (spec principle 4) and the
    census is a second, independently maintained description of the same six
    worlds that a participant reads FIRST. Where they disagree, the
    participant meets one world on the Atlas and a different one when they
    walk through the door."""
    findings = []
    live = _census_live_entries()
    for w in worlds:
        entry = live.get(registry[w].get("census_id") or "")
        if entry is None:
            continue  # already reported by check_census_link
        e = entry.get("entry") or {}
        rep = registry[w].get("representative") or {}
        window = registry[w].get("time_window") or {}

        if entry.get("start") != window.get("start") or entry.get("end") != window.get("end"):
            findings.append(_defect("census-time-window", w, f"census start/end {entry.get('start')}-{entry.get('end')} != registry time_window {window.get('start')}-{window.get('end')}"))
        if bool(entry.get("living")) != bool(registry[w].get("living_tradition_flag")):
            findings.append(_defect("census-living-flag", w, f"census living={entry.get('living')} != registry living_tradition_flag={registry[w].get('living_tradition_flag')}"))
        if e.get("representativeName") and e["representativeName"] != rep.get("name"):
            findings.append(_defect("census-representative-name", w, f"census representativeName {e['representativeName']!r} != registry representative.name {rep.get('name')!r}"))
        if e.get("representativeTitle") and e["representativeTitle"] != rep.get("role_label"):
            findings.append(_defect("census-role-label", w, f"census representativeTitle {e['representativeTitle']!r} != registry representative.role_label {rep.get('role_label')!r}"))
        if entry.get("name") and entry["name"] != registry[w].get("display_name"):
            findings.append(_defect("census-display-name", w, f"census name {entry['name']!r} != registry display_name {registry[w].get('display_name')!r}"))
        # The friendly card name (entry.worldName - what the homepage card
        # and Atlas sheet actually display) was the ONE participant-facing
        # identity field nothing compared (2026-08-28 foundation audit,
        # F-16). Mark's same-day ruling: both name registers live in the
        # registry - card_name friendly, display_name scholarly - and the
        # census derives.
        if e.get("worldName") and registry[w].get("card_name") and e["worldName"] != registry[w]["card_name"]:
            findings.append(_defect("census-world-name", w, f"census entry.worldName {e['worldName']!r} != registry card_name {registry[w]['card_name']!r}"))
    return findings


# --------------------------------------------------------------------------
# stage 3: the records tree, world against world
# --------------------------------------------------------------------------

def check_record_type_directories(*, worlds, **_) -> list[Finding]:
    """Observation, not defect: a world legitimately may hold no records of
    some type, and the compiler emits an empty chunk directory rather than
    failing. Reported because a MISSING directory and an empty one look the
    same downstream, and the difference is usually a build that stopped."""
    findings = []
    dirs = {w: {p.name for p in (RECORDS_ROOT / w).iterdir() if p.is_dir()} for w in worlds}
    universe = set().union(*dirs.values())
    for w in worlds:
        for missing in sorted(universe - dirs[w]):
            findings.append(_observation("record-type-dir", w, f"no {missing}/ directory; every other formation world has one"))
        stray = [p.name for p in (RECORDS_ROOT / w).iterdir() if not p.is_dir()]
        for name in sorted(stray):
            findings.append(_observation("records-stray-file", f"{w}/{name}", "non-record file at the world's records root - the compiler ignores it, but it is not part of the frozen records copy"))
    return findings


def check_id_type_tokens(*, records, worlds, **_) -> list[Finding]:
    """One id shape across the fleet, extended past what gate_id_convention
    already enforces. That gate holds every id to `<world>.<type>.<slug>` and
    bans a canon-cell code in the slug, but it never compares the middle
    segment BETWEEN worlds - so a record_type may be addressed one way in one
    world and another way in the next and still pass, which is exactly what
    happened. The gate's own docstring gives the reason this matters at
    scale: 'At the hundred the spec plans for, it is a corpus nobody can
    write a tool against.'"""
    findings = []
    tokens: dict[str, dict[str, set[str]]] = {}
    for w in worlds:
        for rec in records[w].values():
            parts = rec["id"].split(".")
            if len(parts) != 3:
                continue
            tokens.setdefault(rec["record_type"], {}).setdefault(w, set()).add(parts[1])
    for record_type, by_world in sorted(tokens.items()):
        used = {t for toks in by_world.values() for t in toks}
        if len(used) == 1:
            continue
        counts = {t: sorted(w for w, toks in by_world.items() if t in toks) for t in sorted(used)}
        majority = max(counts, key=lambda t: len(counts[t]))
        for token, holders in sorted(counts.items()):
            if token == majority:
                continue
            findings.append(_defect("id-type-token", record_type, f"{', '.join(holders)} address {record_type} as `<world>.{token}.*` where the rest of the fleet uses `<world>.{majority}.*`"))
    return findings


def check_record_world_ids(*, records, registry, worlds, **_) -> list[Finding]:
    """The two independent places a record names its own world - the envelope
    `world_id` and the id's own first segment - both have to agree with the
    registry. A record filed under one world declaring another compiles fine
    and is uncitable at turn time."""
    findings = []
    for w in worlds:
        expected = registry[w].get("world_id")
        for rid, rec in sorted(records[w].items()):
            if rec.get("world_id") != expected:
                findings.append(_defect("record-world-id", w, f"{rid} declares world_id {rec.get('world_id')!r}, registry says {expected!r}"))
            if rid.split(".")[0] != w:
                findings.append(_defect("record-id-prefix", w, f"{rid} is not prefixed with its own world_key {w!r}"))
    return findings


def check_figure_dates_keys(*, records, worlds, **_) -> list[Finding]:
    """`figure.dates` is `{"type": "object"}` in the schema - no key
    vocabulary at all - and cic-poc/frontend's FigureBridgeMark prints
    `${key}: ${value}` straight into the Level-3 panel. So the authoring
    convention a world happened to pick IS what a participant reads.

    fleet_vocabulary is a strict-majority threshold (more worlds use a key
    than don't), not "all but one" - that weaker form only worked back when
    pahc was the fleet's sole outlier; the moment a second world (cappadocian,
    keying dates as `display` for its own reasons) legitimately diverges too,
    "all but one" silently flags every conforming world instead, since the
    dominant convention no longer clears an "all but one" bar with two
    outliers standing. A strict majority keeps working regardless of how many
    minority conventions exist alongside it."""
    findings = []
    by_world = {}
    for w in worlds:
        by_world[w] = {k for rec in records[w].values() if rec["record_type"] == "figure" for k in (rec.get("dates") or {})}
    counts: dict[str, int] = {}
    for keys in by_world.values():
        for k in keys:
            counts[k] = counts.get(k, 0) + 1
    fleet_vocabulary = {k for k, n in counts.items() if n > len(worlds) / 2}
    for w in worlds:
        for key in sorted(by_world[w] - fleet_vocabulary):
            findings.append(_defect("figure-dates-keys", w, f"figure.dates uses key {key!r}, which no other world uses; the frontend prints the key verbatim to the participant"))
    return findings


# --------------------------------------------------------------------------
# stage 4: what a participant actually reads
# --------------------------------------------------------------------------

_RECORD_ID = re.compile(r"\b(?:[a-z]{2,8})\.(?:[a-z_]{2,20})\.[a-z0-9][a-z0-9-]{2,}\b")
# Deliberately does NOT match a bare `SS<n>`. This project writes the section
# sign as "SS", so `Vita SS89` is a real primary-source locus - the checkable
# reference a participant is SUPPOSED to be shown - and desert alone uses it in
# 44 of its 192 source loci. An earlier version of this pattern flagged all
# three of desert.figure.antony's dates on that basis and reported six leaks
# where there are three. A build reference has to name a BUILD artifact
# (`Doc_01 SS2.3`, `Artifact-1`, BUILD-LOG) or talk about the build in prose.
_BUILD_REF = re.compile(r"\bDoc_\d|\bArtifact-\d|\bBUILD-LOG\b|\bthis build\b|\b20\d{2}-\d{2}-\d{2}\b", re.IGNORECASE)

# Exactly the fields that reach a participant's screen, via
# engine.m4.citation_cards' label table, engine.m4.name_bridge's figure card
# and engine.m2.builders' compiled quote index. Deliberately narrower than
# "every string on the record", for the same reason gates.gate_no_build_
# attribution scopes itself to build_prompt()'s own field contract:
# commentary fields are a LEGITIMATE home for build language, and scanning
# them would bury the real findings.
_PARTICIPANT_FIELDS = {
    "figure": ["bridge_line"],
    "term": ["world_word"],
    "story": ["tellable_as"],
    "gravity": ["name"],
    "force": ["name"],
    "contested_claim": ["claim"],
}


def check_participant_field_leaks(*, records, worlds, **_) -> list[Finding]:
    findings = []
    for w in worlds:
        hits = []
        for rid, rec in sorted(records[w].items()):
            texts = [(f, rec.get(f)) for f in _PARTICIPANT_FIELDS.get(rec["record_type"], [])]
            if rec["record_type"] == "figure":
                texts += [(f"dates.{k}", v) for k, v in (rec.get("dates") or {}).items()]
            for field, text in texts:
                if not isinstance(text, str):
                    continue
                match = _RECORD_ID.search(text) or _BUILD_REF.search(text)
                if match:
                    hits.append(f"{rid}.{field} ({match.group(0)!r})")
        if hits:
            findings.append(_defect("ui-field-leak", w, f"{len(hits)} participant-facing field(s) carry a record id or build reference: {', '.join(hits[:4])}{' ...' if len(hits) > 4 else ''}"))
    return findings


def check_quote_speaker_labels(*, records, worlds, **_) -> list[Finding]:
    """`speaker_or_author` is authored two ways across the corpus - a figure
    record id, or already-readable prose - and both are legitimate. What is
    not legitimate is a third way that no resolver unwraps: the label
    resolvers (engine.m4.citation_cards._quote_speaker_label for the Level-3
    card, engine.m2.builders._quote_speaker for the compiled prompt's quote
    index) both only look through a `figure` id, so anything else lands on a
    participant's screen as a raw database key."""
    from engine.m2.builders import _quote_speaker
    from engine.m4.citation_cards import _label

    findings = []
    for w in worlds:
        repo = records[w]
        bad = []
        for rid, rec in sorted(repo.items()):
            if rec["record_type"] != "quote":
                continue
            for rendered in (_label(rec, repo), _quote_speaker(rec)):
                if _RECORD_ID.search(rendered or ""):
                    bad.append(rid)
                    break
        if bad:
            findings.append(_defect("quote-speaker-label", w, f"{len(bad)} quote(s) render a raw record id as the speaker a participant reads: {', '.join(bad[:4])}{' ...' if len(bad) > 4 else ''}"))
    return findings


# --------------------------------------------------------------------------
# stage 5: the frontends
# --------------------------------------------------------------------------

def check_app_world_assets(*, worlds, **_) -> list[Finding]:
    """cic-poc/frontend/src/data/worlds.ts holds the one thing about a world
    the registry does not carry (portrait file, accent colour) - and
    useWorlds.toEntry() returns null for a world with no entry there, which
    DROPS it from the world list silently. A world can be built, compiled,
    admitted and served by GET /api/worlds and still never appear."""
    findings = []
    if not APP_WORLDS_TS.is_file():
        return [_defect("app-assets-file", "fleet", f"{APP_WORLDS_TS} not found")]
    text = APP_WORLDS_TS.read_text(encoding="utf-8")
    order_match = re.search(r"WORLD_ORDER\s*=\s*\[([^\]]*)\]", text)
    order = set(re.findall(r"'([^']+)'", order_match.group(1))) if order_match else set()
    assets_match = re.search(r"WORLD_ASSETS[^=]*=\s*\{(.*?)\n\}", text, re.S)
    assets = set(re.findall(r"^\s*(\w+):\s*\{", assets_match.group(1), re.M)) if assets_match else set()
    for w in worlds:
        if w not in assets:
            findings.append(_defect("app-world-assets", w, "no WORLD_ASSETS entry - useWorlds() drops this world from the world list without an error"))
        if w not in order:
            findings.append(_defect("app-world-order", w, "not in WORLD_ORDER - indexOf returns -1, which sorts it ahead of every listed world"))
    for extra in sorted((assets | order) - set(worlds)):
        findings.append(_defect("app-world-unknown", extra, "named in the frontend's world tables but not a formation world in the registry"))
    return findings


def check_site_portraits(*, registry, worlds, **_) -> list[Finding]:
    """Each world's own cic-website/traditions/<census_id>.html page carries its
    Representative's portrait directly - the site's entry pattern since the V2
    homepage replaced the old carousel (which kept one shared PORTRAIT_FILES
    lookup in index.html; this checks the same concern against where that
    content actually lives now). A world with no tradition page, or whose
    portrait file is missing on disk, renders a broken image on the public
    site."""
    findings = []
    for w in worlds:
        cid = registry[w].get("census_id")
        if not cid:
            continue
        page = SITE_TRADITIONS_DIR / f"{cid}.html"
        if not page.is_file():
            findings.append(_defect("site-portrait", w, f"census_id {cid!r} has no cic-website/traditions/{cid}.html - the site has no page to carry this world's portrait"))
            continue
        text = page.read_text(encoding="utf-8")
        img_match = re.search(r'<img\s+src="([^"]+)"', text)
        if not img_match:
            findings.append(_defect("site-portrait", w, f"traditions/{cid}.html has no portrait <img>"))
            continue
        img_path = (page.parent / img_match.group(1)).resolve()
        if not img_path.is_file():
            findings.append(_defect("site-portrait", w, f"traditions/{cid}.html's portrait image {img_match.group(1)!r} does not exist on disk"))
    return findings


# --------------------------------------------------------------------------
# observations: measured, never thresholded
# --------------------------------------------------------------------------

def observe_retrieval_hints(*, records, worlds, **_) -> list[Finding]:
    """`retrieval.retrieve_when` is the one retrieval field the live turn
    loop actually reads (engine.m1.canon.retrieval_hint_keywords widens
    Stage A's cell match with it). A world whose builders wrote few hints
    gets less of that widening - a build-effort difference that reads, at
    turn time, exactly like a thinner world."""
    findings = []
    for w in worlds:
        with_block = [r for r in records[w].values() if r.get("retrieval")]
        hinted = [r for r in with_block if (r.get("retrieval") or {}).get("retrieve_when")]
        pct = round(100 * len(hinted) / len(with_block)) if with_block else 0
        phrases = len({p for r in with_block for p in ((r.get("retrieval") or {}).get("retrieve_when") or [])})
        findings.append(_observation("retrieval-hint-coverage", w, f"{len(hinted)}/{len(with_block)} retrieval-bearing records carry retrieve_when ({pct}%), {phrases} distinct hint phrases"))
    return findings


def observe_unread_retrieval_config(*, records, worlds, **_) -> list[Finding]:
    """`retrieval.tier` and `retrieval.do_not_retrieve_when` are authored by
    every world and read by no runtime path (tier reaches only
    gate_distribution_health; do_not_retrieve_when appears at runtime only in
    evidence._FALLBACK_EXCLUDED_KEYS, which excludes it from being SEARCHED,
    not from being enforced). The per-world spread is recorded here so the
    day either one is wired, the drift is already known."""
    findings = []
    for w in worlds:
        tiers = [(r.get("retrieval") or {}).get("tier") for r in records[w].values() if (r.get("retrieval") or {}).get("tier")]
        excl = sum(1 for r in records[w].values() if (r.get("retrieval") or {}).get("do_not_retrieve_when"))
        spread = {t: tiers.count(t) for t in (1, 2, 3)}
        findings.append(_observation("unread-retrieval-config", w, f"tier spread {spread} (read by no runtime path), {excl} records carry do_not_retrieve_when (enforced nowhere)"))
    return findings


def observe_optional_field_adoption(*, records, worlds, **_) -> list[Finding]:
    """Fields the schema allows and no gate requires. Uneven adoption is not
    a defect on its own - it is the leading indicator of one, because it is
    where the next field to be wired will find the fleet already uneven."""
    watched = [("source", "external_ids"), ("contested_claim", "divergence_partners"), ("demonstration", "tags"), ("term", "prior_sense")]
    findings = []
    for w in worlds:
        parts = []
        for record_type, field in watched:
            pool = [r for r in records[w].values() if r["record_type"] == record_type]
            filled = sum(1 for r in pool if r.get(field) not in (None, "", [], {}))
            parts.append(f"{record_type}.{field} {filled}/{len(pool)}")
        findings.append(_observation("optional-field-adoption", w, "; ".join(parts)))
    return findings


def observe_source_licensing(*, records, worlds, **_) -> list[Finding]:
    findings = []
    for w in worlds:
        refs = [s for r in records[w].values() for s in (r.get("sources") or [])]
        licensed = sum(1 for s in refs if s.get("license"))
        findings.append(_observation("source-ref-license", w, f"{licensed}/{len(refs)} sources[] entries carry a license field"))
    return findings


def observe_uncompiled_required_fields(*, records, worlds, **_) -> list[Finding]:
    """Fields the gate battery REQUIRES on every record and the compiler
    never emits. `doctrinal_witness.positions`/`tensions` are the costly
    pair (F-23): `tensions` is where a witness names its own limit - "this
    world left little in its own voice arguing who Christ was" - and
    build_prompt emits only `text`, so the voice is handed the world's
    oblique answer and never the sentence saying it is oblique.

    Reported per world rather than once, because the number is what makes
    the case: a field authored on every record in every world and read
    nowhere is not an oversight anyone will notice from inside one world.
    """
    watched = [("doctrinal_witness", "positions"), ("doctrinal_witness", "tensions")]
    findings = []
    for w in worlds:
        parts = []
        for record_type, field in watched:
            pool = [r for r in records[w].values() if r["record_type"] == record_type]
            filled = sum(1 for r in pool if r.get(field) not in (None, "", [], {}))
            parts.append(f"{record_type}.{field} {filled}/{len(pool)} authored")
        findings.append(_observation("uncompiled-required-field", w, "; ".join(parts) + " - gate-required, compiled into no prompt (F-23)"))
    return findings


def observe_second_hand_sources(*, records, worlds, **_) -> list[Finding]:
    """Mark's standard, 2026-08-26: every world should reach every available
    resource - they can be ranked, but never ignored.

    The runtime cannot deliver that by ranking. engine/m4 never opens a file
    under cic/texts/; retrieval runs over the world's own compiled records
    alone, so a volume with no source record in a world is invisible at turn
    time however it is ranked. "Not ignored" therefore has to mean a source
    record exists, even a low-ranked one.

    Reported here is the sharpest DERIVED slice of that, not the blunt one:
    volumes whose principal author this world already NAMES in its records
    while never opening that author's own vendored works. Date overlap alone
    is far too coarse to act on - it puts the Chronicle of Edessa on
    Alexandria's list - so it sets the candidate pool and this narrows it.
    A world naming Basil and reaching him only through Palladius is sourcing
    him second-hand, and that is measurable rather than asserted.
    """
    findings = []
    for w in worlds:
        blob = " ".join(
            str(v) for r in records[w].values() for k, v in r.items()
            if k != "_body" and isinstance(v, str)
        )
        opened = {p for r in records[w].values() for p in re.findall(r"cic/texts/([\w.-]+)", str(r.get("edition") or ""))}
        # Word-boundary, never a bare substring. Measured, not theoretical:
        # a plain `"Basil" in blob` matched "Basilidean" (the Gnostic school)
        # four times in alx against two real Basil mentions, and `"Leo"`
        # matched "Leonides" - Origen's father - four times out of four,
        # putting Leo the Great on Alexandria's worklist on the strength of a
        # martyr who died 150 years before he was born.
        second_hand = []
        for filename, authors in ((f, a) for f, a in _AUTHORS_BY_FILE.items() if f not in opened):
            if any(re.search(rf"\b{re.escape(author)}\b", blob) for author in authors):
                second_hand.append(filename)
        findings.append(_observation(
            "second-hand-source", w,
            f"{len(second_hand)} vendored volume(s) whose author this world names but never opens: "
            + (", ".join(sorted(second_hand)) or "none")))
    return findings


def observe_corpus_map(*, registry, worlds, **_) -> list[Finding]:
    """Progress against Mark's standard - *"each world built and representing
    the sources of the christian tradition"* - read from the corpus map, not
    inferred here.

    This replaced `observe_corpus_review` on 2026-08-26. That observer read a
    per-world `corpus_review` record, and when Mark ruled the assignment work
    stays OUT of the built worlds (*"lets keep this separate from the built
    worlds with clear buckets that align"*) the record type went with it - so
    the observer reported "no corpus_review record" six times, forever, about
    a thing deliberately removed. Six lines of standing noise is how a standing
    check stops being read, so it is repointed at the structure that now
    exists rather than deleted: the question it asks is still the right one.

    The join is `registry[world].census_id -> cic/corpus-map/<id>.yaml`, and it
    needs no lookup table because the filename IS the census id. Demonstrating
    that the alignment holds from inside the fleet check is half the reason
    this stays: if the buckets ever stop lining up, this is where it shows.

    Entries belonging to no built world are counted separately and NOT as a
    gap. Basil waiting in `cappadocian-nicene-pastoral-monastic-tradition` is
    material correctly placed for a world that does not exist yet - the exact
    thing F-25 was misreading as six worlds failing to read him.
    """
    findings = []
    try:
        sys.path.insert(0, str(REPO_ROOT / "cic" / "engine"))
        from corpus_map import load as load_corpus_map
        docs = load_corpus_map()
    except Exception as exc:                      # noqa: BLE001 - never fail the fleet run on it
        return [_observation("corpus-map", "fleet", f"corpus map unreadable ({exc.__class__.__name__}); assignment has not started")]

    if not docs:
        return [_observation("corpus-map", "fleet", "no corpus map yet - the assignment thread has not started "
                                                    "(see BRIEF-corpus-assignment-thread.md)")]

    for w in worlds:
        cid = registry[w].get("census_id")
        doc = docs.get(cid or "")
        if doc is None:
            findings.append(_observation("corpus-map", w, f"no corpus-map file for census id {cid!r}"))
            continue
        works = [x for x in (doc.get("works") or []) if isinstance(x, dict)]
        by_role: dict[str, int] = {}
        for entry in works:
            by_role[entry.get("role", "?")] = by_role.get(entry.get("role", "?"), 0) + 1
        unsettled = sum(1 for x in works if x.get("confidence") != "assigned")
        findings.append(_observation(
            "corpus-map", w,
            f"{len(works)} work(s) assigned"
            + (f" ({', '.join(f'{k} {v}' for k, v in sorted(by_role.items()))})" if by_role else "")
            + (f", {unsettled} not yet `assigned`" if unsettled else "")))

    held = sorted(set(docs) - {registry[w].get("census_id") for w in worlds})
    findings.append(_observation(
        "corpus-map", "fleet",
        f"{len(held)} Atlas entry(ies) holding material for worlds not yet built: "
        + (", ".join(held) or "none")))
    return findings

CHECKS = [
    check_registry_shape,
    check_package_pinned,
    check_census_link,
    check_census_agreement,
    check_record_type_directories,
    check_id_type_tokens,
    check_record_world_ids,
    check_figure_dates_keys,
    check_participant_field_leaks,
    check_quote_speaker_labels,
    check_app_world_assets,
    check_site_portraits,
    observe_retrieval_hints,
    observe_unread_retrieval_config,
    observe_optional_field_adoption,
    observe_source_licensing,
    observe_uncompiled_required_fields,
    observe_second_hand_sources,
    observe_corpus_map,
]


def run_all() -> list[Finding]:
    registry = load_registry()
    worlds = formation_world_keys(registry)
    records = {w: load_world_records(w) for w in worlds}
    context = {"registry": registry, "worlds": worlds, "records": records}
    findings: list[Finding] = []
    for check in CHECKS:
        findings.extend(check(**context))
    return findings


def new_defects(findings: list[Finding]) -> list[Finding]:
    """The whole point of the exit code: a defect nobody has written up."""
    return [f for f in findings if f.severity == DEFECT and f.key not in ACCEPTED_OPEN]


def main(argv: list[str] | None = None) -> int:
    show_all = "--all" in (argv if argv is not None else sys.argv[1:])
    findings = run_all()
    new = new_defects(findings)
    accepted = [f for f in findings if f.severity == DEFECT and f.key in ACCEPTED_OPEN]
    observations = [f for f in findings if f.severity == OBSERVATION]

    print(f"cross-world consistency: {len(new)} new defect(s), {len(accepted)} accepted-open, {len(observations)} observation(s)\n")
    if new:
        print("NEW DEFECTS - not in ACCEPTED_OPEN. A world drifted from the fleet")
        print("and nothing has been written up about it yet.\n")
        for f in new:
            print(f"  {f.key:46} {f.message}")
        print()
    if accepted and show_all:
        print("ACCEPTED-OPEN - known, documented, owned by a named next step.\n")
        for f in accepted:
            print(f"  {f.key:46} {f.message}")
            print(f"  {'':46} -> {ACCEPTED_OPEN[f.key]}")
        print()
    for f in observations:
        print(f"  observation  {f.key:44} {f.message}")
    return 1 if new else 0


if __name__ == "__main__":
    sys.exit(main())
