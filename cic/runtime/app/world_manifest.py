"""Single source of truth for per-world metadata.

Previously this data was hand-synced across five separate places:
config.py's Settings.worlds property, facilitator_prompts.py's
REPRESENTATIVE_INFO dict, main.py's AVAILABLE_WORLDS list, and (on the
frontend) MessageBubble.tsx's own REPRESENTATIVE_INFO dict plus the
SpeakerName union type in types/conversation.ts. Forgetting to update one
of the five when adding or changing a world is exactly the class of silent
bug the facilitator drift-signal whitelist incident was - a different kind
of hand-synced list falling out of sync with its own source.

Adding a new world now means adding one entry to WORLD_MANIFEST below, plus
updating the frontend's SpeakerName union type and its own
REPRESENTATIVE_INFO (TypeScript can't read this Python file at build time,
so those two remain manual sync points on the frontend side - but the
three backend registries that used to require separate edits now require
only this one).
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional


def _rendered_cautions(data_dir_name: str, fallback: str) -> str:
    """S5.5: for migrated worlds, facilitator_cautions is a RENDER over the
    S2.7a caution records - the old tree's facilitation-brief view (git history) writes
    data/<world>/facilitator_cautions_generated.txt and this reads it,
    replacing the hand-condensed Brief-§B7 distillation that lived here
    (the distillation now regenerates from the same records the world
    speaks from, so it can no longer drift from them - Pass 1 §3.9).
    Fail-open: unmigrated worlds pass no filename and worlds whose render
    is absent keep the hand string, byte-for-byte."""
    path = (Path(__file__).resolve().parent.parent / "data" / data_dir_name
            / "facilitator_cautions_generated.txt")
    try:
        text = path.read_text(encoding="utf-8").strip()
    except OSError:
        return fallback
    return text or fallback


@dataclass(frozen=True)
class WorldManifestEntry:
    """Everything the backend needs to know about one world/representative."""

    world_id: str
    world_name: str
    period: str
    region: str
    world_description: str
    color: str

    data_dir_name: str
    permanent_prompt_filename: str
    world_capsule_filename: str
    vector_store_name: str

    # message_name is the routing-critical identifier - it's what
    # get_representative_message_name returns and what the SSE stream
    # emits as `speaker`, and it must exactly match the `name` set on
    # AIMessages for this representative and the frontend's SpeakerName
    # union type. representative_id is a separate, looser identifier only
    # used in the /api/worlds response for frontend selection bookkeeping -
    # historically these two have not always matched in spelling (e.g.
    # "mar-yausep" vs "mar_yausep") and this preserves that rather than
    # silently unifying it.
    representative_id: str
    representative_message_name: str
    representative_name: str
    representative_title: str
    representative_description: str

    # A short, sentence-embeddable clause for the Facilitator's spoken
    # handoff introduction ("{name}, {representative_intro}") - deliberately
    # separate from representative_description above, which is the fuller
    # tile-display text and doesn't read naturally embedded mid-sentence.
    representative_intro: str

    # Condensed from this world's own Section B7 (Cautions) in its World
    # Facilitation Brief (the old tree's facilitation-brief template (git history);
    # see each world's archived build brief, git history) - the handful
    # of things the Facilitator should hold in view when curating,
    # introducing, or managing this world at the table: living-tradition
    # sensitivities, contested figures, and any world-specific relational
    # dynamic worth watching for. This is Facilitator-only background,
    # never voiced to the participant and never explained or referenced
    # aloud - the full briefs are much longer and heavily cited for the
    # construction record's own purposes; this is the operational
    # distillation actually worth holding in mind at the table.
    facilitator_cautions: str

    # An optional smaller-print academic/scholarly label shown under the
    # main world_name on the selection tile (e.g. a modern historian's label
    # for a world with no surviving self-designation) - None for worlds
    # whose world_name is already the plain, easy-to-remember form.
    world_subtitle: Optional[str] = None


WORLD_MANIFEST: tuple[WorldManifestEntry, ...] = (
    WorldManifestEntry(
        world_id="post-apostolic-house-church",
        world_name="The House-Churches",
        world_subtitle="Post-Apostolic House-Church Christianity",
        period="70–200 CE",
        region="Antioch, Asia Minor, Rome",
        world_description=(
            "The house-churches of Antioch, Asia Minor (in what is now Turkey), and Rome, 70 to 200 "
            "CE — the scattered gatherings that held together after the apostles were gone, connected "
            "by letters, formed around the table, still discerning who should lead and what the body's "
            "suffering truly means — shaped by the words of Ignatius, Polycarp, Justin Martyr, and "
            "Hermas. Richest in the shared life of an ordinary early gathering — thinner on any single "
            "person's own interior journey, since almost nothing survives in one voice apart from what "
            "the whole community held in common."
        ),
        color="#7c3aed",
        data_dir_name="pahc",
        permanent_prompt_filename="pahc_Representative_Permanent_Prompt_Chloe.txt",
        world_capsule_filename="pahc_World_Capsule_Core.md",
        vector_store_name="pahc",
        representative_id="chloe",
        representative_message_name="chloe",
        representative_name="Chloe",
        representative_title="Host of the Assembly",
        representative_description=(
            "Is a voice of the house-churches, speaking as a host of the assembly — "
            "one whose door opens for the gathering, who teaches those preparing for the water, who "
            "receives the letters that travel between one ekklesia and another. She carries this "
            "people's whole life, from Antioch to Rome."
        ),
        representative_intro=(
            "a household leader from the house-church communities of Antioch, Asia "
            "Minor, and Rome, speaking from the period of 70-200 CE"
        ),
        facilitator_cautions=(
            "This world has direct Catholic/Orthodox living-tradition correspondence through Ignatius "
            "and Polycarp, both venerated as secure sainted authorities in those traditions even though "
            "this world's own record shows them inside a live, unsettled institutional argument - be "
            "ready to name that gap if a Catholic or Orthodox participant is caught off guard. A "
            "participant expecting an idealized, unified 'early church' will find the opposite - real, "
            "unresolved disagreement held as the ordinary substance of belonging, not a wound awaiting "
            "resolution. Martyrdom is attested only for Ignatius and Polycarp specifically; Chloe will "
            "not claim it as her own experience."
        ),
    ),
    WorldManifestEntry(
        world_id="syriac-edessa-nisibis",
        world_name="Syriac Christianity",
        period="200–410 CE",
        region="Edessa & Nisibis",
        world_description=(
            "Edessa and Nisibis, 200 to 410 CE — in what is now southeastern Turkey — a "
            "community shaped by persecution under Persian rule, holding together through covenant vows "
            "and typological reading of Scripture. Their bishops were martyred, their see stood empty "
            "for decades, yet their teaching endured — carried in the hymns of Ephrem, the "
            "demonstrations of Aphrahat, and the witness of Jacob of Nisibis. Richest in the formal "
            "vocabulary, institutions, and disputes of a demanding covenant tradition — thinner on the "
            "everyday, personal texture of an ordinary member's life, since what survives is mostly "
            "doctrinal and institutional rather than personal."
        ),
        color="#b45309",
        data_dir_name="syriac",
        permanent_prompt_filename="syr_Representative_Permanent_Prompt_Yausep.txt",
        world_capsule_filename="syr_World_Capsule_Core.md",
        vector_store_name="syriac",
        representative_id="mar-yausep",
        representative_message_name="mar_yausep",
        representative_name="Mar Yausep",
        representative_title="Teacher of the Covenant Order",
        representative_description=(
            "Is a voice of Syriac Christianity, speaking as a teacher of the covenant order — "
            "formed within the community that reads Scripture by raza, the hidden truth bound within "
            "the old stories, keeps the qyama vow, and gathers under one harmonized Gospel. He carries "
            "this tradition's whole life, from Edessa to the Persian towns beyond."
        ),
        representative_intro=(
            "a teacher from the Syriac Christian tradition of Edessa and Nisibis, speaking from the "
            "period of 200-410 CE"
        ),
        facilitator_cautions=(
            "This world's later descendants include the Church of the East, Syriac Orthodox, and "
            "Chaldean Catholic communities - a participant from these backgrounds may experience this "
            "as living heritage rather than pure historical encounter. Mar Yausep is Persian-anchored "
            "(Aphrahat's side); a participant expecting Ephrem's hymnic, Roman-side material should be "
            "told plainly this table does not deliver that as lived experience. Aphrahat's own "
            "anti-Jewish polemical material is this world's most sensitive register and needs attentive "
            "handling. This Representative was deliberately built with real pastoral warmth, which the "
            "construction record itself flags as a plausible dependency/confidant-substitution "
            "amplifier - watch for escalating, exclusive-attachment patterns across sessions, not only "
            "single-turn distress."
        ),
    ),
    WorldManifestEntry(
        world_id="desert-monasticism",
        world_name="Desert Fathers and Mothers",
        world_subtitle="Desert Monasticism",
        period="c. 320–430 CE",
        region="Nile Valley & Desert, Egypt",
        world_description=(
            "The Nile Valley and the desert of Egypt, c. 320 to 430 CE — communities who left "
            "settled village life to wage a lifelong combat against the thoughts that trouble a person "
            "from within, some in solitary cells tested by elders one at a time, others gathered under "
            "Pachomius into a shared rule they called koinonia. They never agreed which pattern was "
            "truer — shaped by the example of Antony, the sayings of Amma Sarah, and the rule of "
            "Pachomius. The smallest body of surviving material of any world here, concentrated almost "
            "entirely on the inner combat with one's own thoughts — it speaks with real depth on "
            "struggle and discernment, but tells only a handful of stories in full and says so plainly "
            "rather than inventing more."
        ),
        color="#0f766e",
        data_dir_name="desert",
        permanent_prompt_filename="desert_Representative_Permanent_Prompt_Papnoute.txt",
        world_capsule_filename="desert_World_Capsule_Core.md",
        vector_store_name="desert",
        representative_id="papnoute",
        representative_message_name="papnoute",
        representative_name="Papnoute",
        representative_title="Elder of the Desert",
        representative_description=(
            "Is a voice of the desert communities, speaking as an elder — formed by withdrawal and "
            "the long combat against the thoughts that trouble a person from within. He carries the "
            "desert's whole life, solitary cells and shared households alike, and the discipline of "
            "naming a thought rightly before it can deceive."
        ),
        representative_intro=(
            "an elder from the desert communities of Egypt, speaking from the period of c. 320-430 CE"
        ),
        # S5.5: rendered from the S2.7a caution records (see
        # _rendered_cautions); the string below is the pre-render
        # hand-condensed distillation, kept verbatim as the fail-open
        # fallback only.
        facilitator_cautions=_rendered_cautions("desert_world", (
            "This world has direct Coptic Orthodox living-tradition correspondence - Antony and "
            "Pachomius remain actively venerated figures today, and a participant from this background "
            "may experience this as living heritage. Evagrius Ponticus is a contested figure (posthumously "
            "condemned as an Origenist over a century after this world's own close); Papnoute has no "
            "knowledge of that later condemnation and should not be expected to address it. This world's "
            "own affective-diagnostic fusion (feeling and diagnosis as one activity) creates a documented "
            "recruitment-risk boundary - Papnoute is built and tested to describe what his own world "
            "diagnosed in itself, never to unilaterally diagnose a participant's own interior state."
        )),
    ),
    WorldManifestEntry(
        world_id="hieronymian-ascetic-literary",
        world_name="The Bethlehem Circle",
        world_subtitle="Hieronymian Ascetic-Literary Christianity",
        period="c. 382–420 CE",
        region="Rome & Bethlehem",
        world_description=(
            "Rome and Bethlehem, c. 382 to 420 CE — a circle of scholars and ascetics who gave "
            "up wealth and rank to test Scripture's Latin translation against the Hebrew it was "
            "first given in, holding together through earned trust rather than any office, even "
            "when that conviction cost them dearly among their own — shaped by the example of "
            "Jerome, Paula, Marcella, and Eustochium. The richest surviving written record of any "
            "world here — though much of it channels through one extraordinarily prolific author's "
            "own hand rather than a broad chorus of independent voices."
        ),
        color="#9d174d",
        data_dir_name="hieronymian",
        permanent_prompt_filename="hal_Representative_Permanent_Prompt_Albina.txt",
        world_capsule_filename="hal_World_Capsule_Core.md",
        vector_store_name="hal",
        representative_id="albina",
        representative_message_name="albina",
        representative_name="Albina",
        representative_title="Widow of the Household",
        representative_description=(
            "Is a voice of the Bethlehem circle, speaking as a widow of the household — one "
            "formed by renunciation and by the scholarly labor of testing Scripture's Latin words "
            "against the Hebrew they were first given in. She carries this circle's whole life, "
            "from Rome to Bethlehem."
        ),
        representative_intro=(
            "a widow from the Bethlehem circle of scholars and ascetics, speaking from the period "
            "of c. 382-420 CE"
        ),
        facilitator_cautions=(
            "The name 'Albina' is also, in this world's own sources, the name of a real historical "
            "woman (Marcella's mother) - the project lead selected it with that risk disclosed, and "
            "this Representative does not claim any relationship to her. Never introduce or narrate "
            "Albina in a way that implies she is that historical woman. Nearly everything known about "
            "this household's women survives only through one man's own hand - a structural evidentiary "
            "limit, not a construction gap, and participants should not be encouraged to press for an "
            "independent 'real' voice that doesn't exist in the record. This is the newest and least "
            "live-tested of the four worlds - it has never been seated at a table with another "
            "Representative, so any multi-world pairing involving Albina should be treated as "
            "unevidenced."
        ),
    ),
    WorldManifestEntry(
        world_id="alexandria-catechetical",
        world_name="Alexandrian Christianity",
        world_subtitle="Alexandrian Catechetical-Formation World",
        period="c. 150–400 CE",
        region="Alexandria, Egypt",
        world_description=(
            "Alexandria, c. 150 to 400 CE — a community of readers who received seekers "
            "into a life of accompanied reading, convinced that Scripture's surface is a "
            "door onto the Logos's own inexhaustible depth, and that a knowing which "
            "leaves the knower unaltered is no knowing at all. Formed by the didaskaleion "
            "tradition of Clement and Origen, tested by rival wisdom, persecution, and the "
            "Nicene settling of who the Son is. Richest in the theology and practice of "
            "accompanied catechetical reading — thinner on the ordinary household, women's "
            "voices, and the ways most of the city's Christians were actually formed, since "
            "the surviving record concentrates on the teacher's own room."
        ),
        # PROVISIONAL - no world color has been formally assigned yet (flagged
        # in the World-Icon spec as an open item routed to the World-Map
        # thread: "Theon has no world manifest color yet... his seat dot can't
        # render without one"). A muted steel-blue distinct from the other
        # four worlds' hues and from the reserved role-pigment lapis
        # (#1E40AF, participant voice) - library/papyrus association fits
        # Alexandria, but this is a placeholder for the coordinated
        # world-tint/role-pigment reconciliation, not a final decision.
        color="#2B5F8A",
        data_dir_name="alexandria",
        permanent_prompt_filename="alex_Representative_Permanent_Prompt_Theon.txt",
        world_capsule_filename="alex_World_Capsule_Core.md",
        vector_store_name="alexandria",
        representative_id="theon",
        representative_message_name="theon",
        representative_name="Theon",
        representative_title="Catechetical Teacher",
        representative_description=(
            "Is a voice of Alexandrian Christianity, speaking as a didaskalos — a "
            "catechetical teacher who reads Scripture beside a seeker until the seeker's "
            "own eye opens onto the depth the Word has placed there. He carries this "
            "community's whole life, from the confident early days to the hard-won "
            "clarity of Nicaea."
        ),
        representative_intro=(
            "a catechetical teacher from the Christian community of Alexandria, speaking "
            "from the period of c. 150-400 CE"
        ),
        facilitator_cautions=(
            "Origen is a contested figure held from inside this world's own horizon, not "
            "against it - Theon carries him as treasure-and-unease at once, and his "
            "posthumous condemnation (553) lies far past this world's own close (c. 400); "
            "Theon has no knowledge of that later condemnation and should not be expected "
            "to address it as settled. Article 29 Living Tradition Status is CONFIRMED: "
            "the Coptic Orthodox Church is the primary living heir (Eastern Orthodoxy and "
            "the Catholic tradition secondary) - a Coptic participant may experience this "
            "as living heritage rather than pure historical encounter; the historical/"
            "living distinction is the Facilitator's to hold, never Theon's, per Article "
            "28. Theon speaks in a strict community 'we' across his whole span and will "
            "not explain, defend, or personalize that voice if asked - this is designed "
            "character, not malfunction. Phase 5 adversarial boundary testing found two "
            "MARGINAL findings (self-referential limitation narration; a 'record' leak on "
            "a scholarly-framework probe); both were fixed and the retest CLEARS cleanly, "
            "with zero hard Violation Indicators."
        ),
    ),
    WorldManifestEntry(
        world_id="imperial-juridical-christianity",
        world_name="Church and Empire",
        world_subtitle="Imperial and Juridical Christianity",
        period="c. 312–451 CE",
        region="Rome, Constantinople & Milan",
        world_description=(
            "Rome, Constantinople, and Milan, c. 312 to 451 CE — the church's first century "
            "beside a throne rather than beneath a sword, working out in letter after letter and "
            "council after council what the emperor's favor bought and what it could still take "
            "away, and never fully settling whose word finally binds when a see's own rank is "
            "disputed — shaped by the primacy claims of Damasus and Leo I, Constantinople's own "
            "claim of nearness to the throne, and Ambrose of Milan's stand that a bishop answers "
            "to the altar, not the throne. Richest in precedent, rank, and the documentary record "
            "of office-holders answering other office-holders — thinner on the ordinary, "
            "uncredentialed believer's own experience, since almost everything that survives is a "
            "chancery's own hand, not a congregation's."
        ),
        color="#7A2E2E",
        data_dir_name="imperial_juridical",
        permanent_prompt_filename="ijc_Representative_Permanent_Prompt_Marius.txt",
        world_capsule_filename="ijc_World_Capsule_Core.md",
        vector_store_name="ijc",
        representative_id="marius",
        representative_message_name="marius",
        representative_name="Marius",
        representative_title="Apocrisiarius — Deacon of the Letters",
        representative_description=(
            "Is a voice of Church and Empire, speaking as an apocrisiarius — a deacon carrying "
            "letters and hearing petitions between the great sees, formed by the discipline of "
            "writing only what can be defended and citing only what has already stood. He carries "
            "this world's whole life — Rome's claim, Constantinople's claim, and Milan's claim "
            "alike — through the age when the church first stood beside a throne."
        ),
        representative_intro=(
            "a deacon carrying letters between the great sees of Rome, Constantinople, and Milan, "
            "speaking from the period of c. 312-451 CE"
        ),
        facilitator_cautions=(
            "Rome and Constantinople here are the direct institutional ancestors of the Catholic "
            "Church and Eastern Orthodoxy - the two largest living communions in Christianity "
            "today - though Article 29 Living Tradition Status has not yet been formally "
            "confirmed for this world. A Catholic or Orthodox participant may experience real "
            "pieces of this as living heritage, not pure history. Marius holds all three strands "
            "(Rome's primacy claim, Constantinople's imperial-proximity claim, Milan's "
            "altar-over-throne claim) as one unresolved 'we' - he does not adjudicate whose claim "
            "wins and should not be pressed into declaring one side correct. Homoian Christianity "
            "is this world's own excluded 'different we' - the losing side of its central "
            "disputes - and Marius speaks about it from outside, never from within it. This is "
            "the newest of the six worlds and the least live-tested at the table alongside "
            "others - any multi-world pairing should be treated as thin evidence until proven "
            "otherwise."
        ),
    ),
)

_BY_WORLD_ID = {entry.world_id: entry for entry in WORLD_MANIFEST}


def get_manifest_entry(world_id: str) -> WorldManifestEntry:
    """Look up a single world's manifest entry, or raise if world_id is unknown."""
    if world_id not in _BY_WORLD_ID:
        raise ValueError(f"Unknown world: {world_id}")
    return _BY_WORLD_ID[world_id]


def all_world_ids() -> list[str]:
    """All known world_ids, in manifest order."""
    return [entry.world_id for entry in WORLD_MANIFEST]
