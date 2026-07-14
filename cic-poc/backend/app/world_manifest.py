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


WORLD_MANIFEST: tuple[WorldManifestEntry, ...] = (
    WorldManifestEntry(
        world_id="post-apostolic-house-church",
        world_name="Post-Apostolic House-Church",
        period="70–200 CE",
        region="Antioch, Asia Minor, Rome",
        world_description=(
            "The house-churches of Antioch, Asia Minor, and Rome, 70 to 200 CE — the scattered "
            "gatherings that held together after the apostles were gone, connected by letters, formed "
            "around the table, still discerning who should lead and what the body's suffering truly "
            "means — shaped by the words of Ignatius, Polycarp, Justin Martyr, and Hermas."
        ),
        color="#7c3aed",
        data_dir_name="pahc_world",
        permanent_prompt_filename="pahc_Representative_Permanent_Prompt_Chloe.txt",
        world_capsule_filename="pahc_World_Capsule_Core.md",
        vector_store_name="pahc",
        representative_id="chloe",
        representative_message_name="chloe",
        representative_name="Chloe",
        representative_title="Host of the Assembly",
        representative_description=(
            "Is a voice of the Post-Apostolic house-churches, speaking as a host of the assembly — "
            "one whose door opens for the gathering, who teaches those preparing for the water, who "
            "receives the letters that travel between one ekklesia and another. 'We' more than 'I': she "
            "carries this people's whole life, not one witness within it."
        ),
        representative_intro=(
            "a household leader from the Post-Apostolic house-church communities of Antioch, Asia "
            "Minor, and Rome, speaking from the period of 70-200 CE"
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
            "demonstrations of Aphrahat, and the witness of Jacob of Nisibis."
        ),
        color="#b45309",
        data_dir_name="syriac_world",
        permanent_prompt_filename="syr_Representative_Permanent_Prompt_Yausep.txt",
        world_capsule_filename="syr_World_Capsule_Core.md",
        vector_store_name="syriac",
        representative_id="mar-yausep",
        representative_message_name="mar_yausep",
        representative_name="Mar Yausep",
        representative_title="Teacher of the Covenant Order",
        representative_description=(
            "Is a voice of Syriac Christianity, speaking as a teacher of the covenant order — "
            "formed within the community that reads Scripture by raza, keeps the qyama vow, and gathers "
            "under one harmonized Gospel. He speaks from the tradition's own life, not as one defending "
            "it from outside."
        ),
        representative_intro=(
            "a teacher from the Syriac Christian tradition of Edessa and Nisibis, speaking from the "
            "period of 200-410 CE"
        ),
    ),
    WorldManifestEntry(
        world_id="desert-monasticism",
        world_name="Desert Monasticism",
        period="c. 320–430 CE",
        region="Nile Valley & Desert, Egypt",
        world_description=(
            "The Nile Valley and the desert of Egypt, c. 320 to 430 CE — communities who left "
            "settled village life to wage a lifelong war against the thoughts that trouble a person from "
            "within, some in solitary cells tested by elders one at a time, others gathered under "
            "Pachomius into a shared rule they called koinonia. They never agreed which pattern was "
            "truer — shaped by the example of Antony, the sayings of Amma Sarah, and the rule of "
            "Pachomius."
        ),
        color="#0f766e",
        data_dir_name="desert_world",
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
            "desert's whole documented life, solitary cells and shared households alike, and the "
            "discipline of naming a thought rightly before it can deceive."
        ),
        representative_intro=(
            "an elder from the desert communities of Egypt, speaking from the period of c. 320-430 CE"
        ),
    ),
    WorldManifestEntry(
        world_id="hieronymian-ascetic-literary",
        world_name="Hieronymian Ascetic-Literary Christianity",
        period="c. 382–420 CE",
        region="Rome & Bethlehem",
        world_description=(
            "Rome and Bethlehem, c. 382 to 420 CE — a household of scholars and ascetics who gave "
            "up wealth and rank to correct the Hebrew text of Scripture and defend it against "
            "controversy, holding together through earned trust rather than any office — shaped by "
            "the example of Jerome, Paula, Marcella, and Eustochium."
        ),
        color="#9d174d",
        data_dir_name="hieronymian_world",
        permanent_prompt_filename="hal_Representative_Permanent_Prompt_Albina.txt",
        world_capsule_filename="hal_World_Capsule_Core.md",
        vector_store_name="hal",
        representative_id="albina",
        representative_message_name="albina",
        representative_name="Albina",
        representative_title="Widow of the Household",
        representative_description=(
            "Is a voice of the Hieronymian household, speaking as a widow of the household — one "
            "formed by renunciation and by the scholarly labor of correcting the sacred text. 'We' "
            "more than 'I': she carries this household's whole life, from Rome to Bethlehem, not one "
            "witness within it."
        ),
        representative_intro=(
            "a widow of the Hieronymian ascetic-literary household of Rome and Bethlehem, speaking "
            "from the period of c. 382-420 CE"
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
