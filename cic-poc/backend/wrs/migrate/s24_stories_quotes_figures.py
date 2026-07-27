"""S2.4 - Desert story, quote, and figure records (blueprint S2.4).

Stories: mechanical split of data/desert_world/story_chunks/*.md (front
matter + the chunks' own Story Text / Tier Justification / Usage Guidance
sections - note the chunks DO carry Tier Justification, correcting the
Touches-verification's claim that only Doc_09a holds it; the two match,
verified against Doc_09a directly this session).

Quotes: the three whole-carried sayings (the Permanent Prompt's own
whitelist). Quote-fidelity verification PERFORMED at this step (2026-07-27,
web verification against published-translation quotations):
  - Moses ("My sins run out behind me...") - matches the Ward-associated
    rendering verbatim -> translation_used srcDES021, license verbatim.
  - Sarah ("According to nature I am a woman...") - matches Ward's
    rendering (continuation clause a minor variant) -> srcDES021, verbatim.
  - Arsenius - the chunk's rendering ("flee, be silent, be still - these
    are the roots of sinlessness") matches NO published translation
    checked; it is the build's own English of the Latin systematic
    collection's fuge/tace/quiesce -> translation_used HONESTLY UNSET
    (the quote-recording gate fires; that red is a real finding, see the
    S2.4 gate artifact), license paraphrase-only.

Figures: one record per named person any voice-bearing record references
(SS3.6), narratable set from what the record set actually holds. The
narratability gate then runs against the REAL voice material (Permanent
Prompt + Capsule Core) - its firings on figures the prompt names but the
record set cannot narrate (Syncletica, Theodora, Poemen, Sisoes) are the
gate doing its job on day one; disposition in the gate artifact.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(HERE))

from source_rows_from_doc02 import emit_record

CHUNKS = BACKEND / "data" / "desert_world" / "story_chunks"
OUT = BACKEND / "wrs" / "records" / "desert_world"

STORY_META = {
    # rid: (owner_figure_id, attested_occasion, source rows, voice_surface)
    "desertstory001": ("desertfig001",
        "Hearing Matthew 19:21 read in church, not yet twenty and recently orphaned (Vita Antonii ch. 2).",
        ["srcDES001", "srcDES020"],
        "Athanasius records that Antony heard the word as spoken to him in that hour - we tell it with his name on it, as remembered history, not as our own eyewitness."),
    "desertstory002": ("desertfig001",
        "The staged withdrawal: near the village under an older ascetic, the tombs, the outer mountain at Pispir (c. 286) with emergence c. 305, the inner mountain from c. 311-313 (Vita chs. 3-14, 49-50; Doc_01 SS2.1).",
        ["srcDES001", "srcDES020"],
        "Athanasius records the stages; we tell it as a lifelong deepening, not one departure."),
    "desertstory003": ("desertfig002",
        "The founding at Tabennesi c. 320, joined first by his brother John; by his death in 346, nine houses for men and two for women (the Lives, cross-recension outline).",
        ["srcDES002", "srcDES018"],
        "The Lives record it; we tell the broad outline all recensions share and say plainly that their textual history is tangled."),
    "desertstory004": ("desertfig004",
        "A council at Scetis called to judge a brother's fault; Moses, pressed to attend, arriving with the leaking jar (Apophthegmata, Moses, Alphabetical Collection).",
        ["srcDES005", "srcDES021"],
        "The tradition tells of Abba Moses that... - told as community tradition, never as verified single-event history; his story, kept on his name."),
    "desertstory005": ("desertfig005",
        "Prayer for guidance while still tutor at the imperial court, and again after withdrawal to Egypt (Apophthegmata, Arsenius, Alphabetical Collection).",
        ["srcDES005", "srcDES021"],
        "They say of Abba Arsenius that... - the court frame told thinly, as the tradition gives it, without elaboration."),
    "desertstory006": ("desertfig006",
        "Visiting elder monks coming to test or humble her as a woman (Apophthegmata, Sarah, Alphabetical Collection).",
        ["srcDES005", "srcDES021"],
        "The tradition tells that Amma Sarah answered them - a pointed reversal under a hostile frame, flattened neither into equality nor inferiority claims."),
    "desertstory007": ("desertfig001",
        "Solitary enclosure in the tombs (Vita Antonii chs. 8-10) - the tradition's own portrait register, not incident report.",
        ["srcDES001", "srcDES020"],
        "This is how the tradition remembers Antony's own struggle, what it believed total combat could involve - offered as portrait, explicitly marked, never as literal event-claim."),
    "desertstory008": (None,
        "None - explicitly a typical/composite reconstruction (Tier 4); the absence of a specific occasion is this field's honest value.",
        ["srcDES009", "srcDES005", "srcDES007"],
        "In a typical day for someone formed in this tradition... - marked as reconstruction from the outset, assembled from separately attested elements, never one person's recorded day."),
}

QUOTES = [
    {"id": "desertq001", "speaker_or_author": "desertfig004",
     "text_translation": "My sins run out behind me, and I do not see them, and today I am coming to judge the errors of another.",
     "locus": "Apophthegmata Patrum, Moses (Alphabetical Collection)",
     "translation_used": "srcDES021", "license": "verbatim",
     "confidence": {"citation_specificity": "B", "verification_state": "verified-via-authority",
                     "verification_date": "2026-07-27", "evidentiary_weight": "load-bearing",
                     "formation_confidence": "Widely Accepted"},
     "note": "Wording verified 2026-07-27 against published quotations of the Ward rendering (S2.4 quote-fidelity verification)."},
    {"id": "desertq002", "speaker_or_author": "desertfig005",
     "text_original": "fuge, tace, quiesce",
     "text_translation": "Arsenius, flee, be silent, be still - these are the roots of sinlessness.",
     "locus": "Apophthegmata Patrum, Arsenius (Alphabetical Collection); Latin systematic collection for the triplet",
     "license": "paraphrase-only",
     "confidence": {"citation_specificity": "B", "verification_state": "verified-via-authority",
                     "verification_date": "2026-07-27", "evidentiary_weight": "load-bearing",
                     "formation_confidence": "Widely Accepted"},
     "note": "Saying and Latin triplet verified genuine 2026-07-27; the chunk's ENGLISH rendering matches no published translation checked (Ward-associated renderings differ: 'be silent, and dwell in stillness...'). translation_used honestly unset - the build never recorded its translation edition; the quote-recording gate's red on this record is the gate catching exactly that. license paraphrase-only until a published rendering is adopted or this one is verified against an edition (S2.9 candidate)."},
    {"id": "desertq003", "speaker_or_author": "desertfig006",
     "text_translation": "According to nature I am a woman, but not according to my thoughts. It is I who am a man and you who are women.",
     "locus": "Apophthegmata Patrum, Sarah (Alphabetical Collection)",
     "translation_used": "srcDES021", "license": "verbatim",
     "confidence": {"citation_specificity": "B", "verification_state": "verified-via-authority",
                     "verification_date": "2026-07-27", "evidentiary_weight": "load-bearing",
                     "formation_confidence": "Widely Accepted"},
     "note": "First clause verified verbatim against the Ward rendering 2026-07-27; the continuation clause circulates in minor variants - recorded, not smoothed."},
]

FIGURES = [
    ("desertfig001", [("Antony", "in-world"), ("Antony of Egypt (the Great)", "scholarly")], True,
     ["desertstory001", "desertstory002", "desertstory007"],
     "Founding figure; three stories carried (Tier 1 x2, Tier 3 portrait). Literacy/philosophical formation independently contested (Rubenson/Athanasius tension, srcDES003/srcDES013)."),
    ("desertfig002", [("Pachomius", "in-world")], True, ["desertstory003"],
     "Founder of the koinonia; story held at cross-recension outline only (version-priority unresolved, srcDES002)."),
    ("desertfig003", [("John, brother of Pachomius", "scholarly")], False, [],
     "Named within desertstory003's text as first to join; no story of his own in this world's inventory."),
    ("desertfig004", [("Abba Moses", "in-world"), ("Moses (of Scetis)", "scholarly")], True, ["desertstory004"],
     "The one story carried whole for him; live-test history: a first attempt once misattributed this story to 'Macarius' - the Permanent Prompt's named-attribution guard was written around exactly this record (chunk guidance)."),
    ("desertfig005", [("Abba Arsenius", "in-world"), ("Arsenius (the Great)", "scholarly")], True, ["desertstory005"],
     "Court-tutor biographical frame held Inferential/Thin per the chunk; only the call-saying carried."),
    ("desertfig006", [("Amma Sarah", "in-world"), ("Sarah (of the Nile/Scetis tradition)", "scholarly")], True, ["desertstory006"],
     "One of the three named ammas; her answer to the elders is the world's clearest direct amma voice."),
    ("desertfig007", [("Amma Syncletica", "in-world"), ("Syncletica", "scholarly")], False, [],
     "Named in the Permanent Prompt and Capsule Core's honest-limits passages; genuinely attested in the Apophthegmata tradition but NO story/saying record in this world's inventory (Doc_09a selected Sarah's saying only; expansion is Doc_09a's own open item 1)."),
    ("desertfig008", [("Amma Theodora", "in-world"), ("Theodora", "scholarly")], False, [],
     "Same standing as Syncletica: named in voice material's honest-limits passage, no carried record."),
    ("desertfig009", [("Abba Poemen", "in-world"), ("Poemen", "scholarly")], False, [],
     "Named in the Permanent Prompt EXPLICITLY as a name-without-story ('even a name as often repeated as Poemen's') - the prompt's own refusal-to-invent guard."),
    ("desertfig010", [("Abba Sisoes", "in-world"), ("Sisoes", "scholarly")], False, [],
     "Same as Poemen: named as a name-only example in the prompt's anti-fabrication guard."),
    ("desertfig011", [("Athanasius of Alexandria", "scholarly")], False, [],
     "Named as source-author in the Antony stories' own telling ('Athanasius records that...'); an author-figure of this world's record, not a narratable participant figure."),
    ("desertfig012", [("Macarius", "scholarly")], False, [],
     "Named in desertstory004's usage guidance solely as the historical misattribution target of the live-test defect; no story carried; kept as a record so the misattribution class stays queryable."),
]

SENTINELS = {"—", "–", "-"}


def parse_story(path: Path):
    text = path.read_text(encoding="utf-8")
    fm_block = re.search(r"```(.*?)```", text, re.S).group(1)
    fm = {}
    for line in fm_block.strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    def section(name):
        m = re.search(rf"## {name}\s*\n(.*?)(?=\n## |\Z)", text, re.S)
        return m.group(1).strip().strip("-").strip() if m else ""
    return fm, section("Story Text"), section("Tier Justification"), section("Usage Guidance")


def classify_dnrw(clause: str):
    t = clause.strip()
    if t in SENTINELS:
        return None
    low = t.lower()
    if "different world" in low or "cross-apply" in low:
        return "retired-cross-world"
    if "not native to this world" in low or "retrojected" in low:
        return "anachronism-guard"
    return "sense-disambiguation"


def main():
    from wrs.schema.validate import parse_front_matter  # noqa (env check)
    # stories
    for path in sorted(CHUNKS.glob("*.md")):
        rid = path.stem.split("_")[0]
        fm, story_text, tier_just, usage = parse_story(path)
        owner, occasion, src_ids, voice = STORY_META[rid]
        tier = int(re.sub(r"[^\d]", "", fm.get("Tier", "1")) or 1)
        rw = [c.strip() for c in fm.get("Retrieve-When", "").split(";") if c.strip()]
        dnrw = []
        for clause in [c.strip() for c in fm.get("Do-Not-Retrieve-When", "").split(";") if c.strip()]:
            kind = classify_dnrw(clause)
            if kind in ("sense-disambiguation", "anachronism-guard"):
                dnrw.append({"condition_type": kind, "text": clause})
        rec = {
            "id": rid, "world_id": "desert-monasticism", "record_type": "story",
            "schema_version": 1, "jobs": [1, 2, 3], "register": "emic",
            "review_state": "draft", "cache_stability": "static",
            "title": fm.get("Story-Title", ""),
            "narrative_tier": {"tier": tier, "justification": tier_just},
            "text": story_text,
            "attested_occasion": occasion,
            "tellable_as": "scene",
            "voice_surface": voice + " Usage guidance (chunk, verbatim): " + usage,
            "retrieval": {"tier": tier, "retrieve_when": rw,
                           "do_not_retrieve_when": dnrw, "force_llm_vote": False},
            "sources": [{"source_id": s,
                          "author_gravity_note": fm.get("Confidence", "") if i == 0 else
                          ("Source line (chunk): " + fm.get("Source", ""))}
                         for i, s in enumerate(src_ids)],
        }
        if owner:
            rec["owner_figure_id"] = owner
        emit_record(rec,
                    f"Migrated at S2.4 (2026-07-27) from `data/desert_world/story_chunks/{path.name}` "
                    f"(Story Text / Tier Justification / Usage Guidance verbatim from the chunk's own "
                    f"sections; occasion and telling-formula per chunk + Doc_09a). "
                    f"Tier-4 owner gap: see FLAG-003.",
                    OUT / "story" / f"{rid}.md")
    # quotes
    for q in QUOTES:
        note = q.pop("note")
        rec = {"world_id": "desert-monasticism", "record_type": "quote",
               "schema_version": 1, "jobs": [1, 2, 3], "register": "emic",
               "review_state": "draft", **q}
        emit_record(rec, f"S2.4 quote record (2026-07-27). {note}",
                    OUT / "quote" / f"{q['id']}.md")
    # figures
    for fid, names, narratable, story_ids, note in FIGURES:
        rec = {"id": fid, "world_id": "desert-monasticism", "record_type": "figure",
               "schema_version": 1, "jobs": [1, 3], "register": "etic",
               "review_state": "draft",
               "names": [{"name": n, "name_kind": k} for n, k in names],
               "narratable": narratable, "story_ids": story_ids,
               "attribution_note": note}
        emit_record(rec, f"S2.4 figure record (2026-07-27). SS3.6: named in voice-bearing records; narratable set from what the record set actually holds.",
                    OUT / "figure" / f"{fid}.md")
    print(f"wrote 8 story + {len(QUOTES)} quote + {len(FIGURES)} figure records")


if __name__ == "__main__":
    main()
