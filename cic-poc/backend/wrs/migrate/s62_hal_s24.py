"""S6.2/HAL - S2.4-equivalent: stories + figures. NO quote record, declared.

12 story chunks (data/hieronymian_world/story_chunks/) -> story records;
9 figure records. Mechanical where the chunk carries the content (Story
Text, Tier Justification, Usage Guidance, retrieval front matter -
verbatim); authored-in-script where Desert/ALX/SYR S2.4 authored
(attested_occasion, tellable_as, owner assignment, the voice_surface
telling-frame).

HAL STORY FORMAT, DECLARED: bare key:value front matter at the top of
the file (no fence, no '## Retrieval Front-Matter' header), separated
from the sections by the first '---' line. Parsed accordingly.

TIER NOTE, DECLARED: SIX Tier 1 stories (01/02/03/03a/04/05 - the
mirror image of Syriac's zero; this world's epistolary evidence base
is narrative-historical to a degree none of the first three worlds
matched), four Tier 3, two Tier 4 composites. Two stories (03/03a) are
the rare TWO-SIDED cases - both parties' own texts survive
independently (Jerome+Augustine; Jerome+Rufinus).

QUOTE FINDING, DECLARED: one candidate verbatim quotation exists in
the deployed corpus - the dream-rebuke inside hal_story08's own Story
Text ('You lie. You are a Ciceronian, not a Christian...', Ep. 22.30).
It rides the story record VERBATIM (nothing lost), but NO separate
quote record is emitted: the build docs supply no vetted
translation/verification apparatus for it (the Desert sayings had
vetting; ALX's De inc. 54 formula had Doc-level verification), and the
chunk's own confidence line marks the dream 'Inferential/Thin (the
dream as reported event)'. Promoting it to a vetted quote record
without that apparatus would overclaim - candidate for the pre-freeze
re-sweep if the apparatus arrives.

OWNER ASSIGNMENTS (CO-P2-06 + the chunks' own tier language):
- hal_story10 (fully communal pattern, no individual subject) -> the
  household itself (halfig009), the standing composite convention.
- hal_story11 -> halfig001 (Jerome), NOT the community: the chunk's
  own Tier Justification rules it - 'composite in method, but not in
  subject... performed by exactly one person throughout the
  household's whole span.' Recorded as a documented judgment, not an
  exception taken silently.
- hal_story04 (the attack on the household itself; the scholar's own
  account 'strikingly vague', no individual subject) -> halfig009.
- hal_story09 (the household's own literary output) -> halfig001 as
  their author - the story is about his writing of them.

NO figure records for Malchus/Hilarion, DECLARED: literary characters
of hal_story09's romances - the chunk's own Usage Guidance forbids
treating them as evidence of specific historical individuals' events;
a figure record would be exactly that promotion.

FEC HANDLING: same as ALX/SYR - Formation Ecology Connection parked
VERBATIM in each story record's body under the named delimiter; the
S2.5-equivalent converts the parkings into typed gravity_links
(CO-P2-04 shape). The two composites' Source Identification tables and
Absent Story Notes park verbatim likewise.

GLOSS NOTE: hal_story01's Story Text is the textual home of the
B-category confirmed gloss ('the month named for the harvest' ->
August) - the circumlocution the S2.3 GLOSS_MAP records as having no
term record by design.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(HERE))

from source_rows_from_doc02 import emit_record

CHUNKS = BACKEND / "data" / "hieronymian_world" / "story_chunks"
OUT = BACKEND / "wrs" / "records" / "hieronymian_world"
WID = "hieronymian-ascetic-literary"

FEC_DELIM = ("[Formation Ecology Connection - parked at the S2.4-equivalent; "
             "becomes typed gravity_links (CO-P2-04 shape) when the "
             "S2.5-equivalent authors the gravity records]")

SOURCE_KEYS = [
    ("Epistula 108", "srcHAL001"),
    ("Epistula 112", "srcHAL009"),
    ("Epistula 127", "srcHAL001"),
    ("Epistula 22", "srcHAL001"),
    ("Multiple letters", "srcHAL001"),
    ("Riparius", "srcHAL001"),
    ("adversus Rufinum", "srcHAL005"),
    ("contra Hieronymum", "srcHAL007"),
    ("Vita Malchi", "srcHAL004"),
]

# The composites' Source Identification tables map elements to rowed
# material explicitly; the monastic-template element of story10 rides
# the locus (Doc_01 SS6 / Doc_08 analogy - no row exists or is owed;
# the table itself parks verbatim in the record body).
COMPOSITE_SOURCES = {
    "halstory10": ["srcHAL001", "srcHAL023"],
    "halstory11": ["srcHAL023", "srcHAL003"],
}

STORY = {
 "halstory01": dict(owner="halfig002", tellable_as="scene",
  occasion=("The 385 departure from Rome and the journey through Cyprus, "
            "Antioch, Egypt (Nitria - where Paula wished, and was refused, "
            "to stay), and Palestine to Bethlehem - as Jerome records it in "
            "Ep. 108, the epitaph letter written to Eustochium near the "
            "time of Paula's 404 death; named author, datable, credible in "
            "broad outline, but authored by an interested party and "
            "single-sourced (the chunk's own Tier Justification)."),
  frame=("We tell the journey as the scholar set it down for Paula's own "
         "daughter after her death - he leaving first, in the month named "
         "for the harvest, she following within the month; Cyprus, "
         "Antioch, the monks of Nitria who nearly kept her, and the road "
         "that ended by the cave at Bethlehem. One pen holds the memory, "
         "and we say whose.")),
 "halstory02": dict(owner="halfig001", tellable_as="scene",
  occasion=("Rome, 384-385: Blaesilla's death after fasting that broke "
            "her health, the city's blame laid at the scholar's door, "
            "Damasus's death removing his protection, and the departure "
            "that same year - the documented sequence attested across "
            "multiple of Jerome's own letters; the full causal framing is "
            "his own, and any formal proceeding is Inferential/Thin at "
            "best (the chunk's own confidence split)."),
  frame=("We tell what the record holds: a young woman of our first "
         "circle dead of the severity she took up, a city that blamed "
         "her teacher, a protector's death, and a leaving. That the one "
         "drove the other is the scholar's own telling; no trial or "
         "synod is in the record, and we add none.")),
 "halstory03": dict(owner="halfig001", tellable_as="scene",
  occasion=("Oea: a bishop reads the corrected text of Jonah - 'ivy' "
            "where the congregation had always heard 'gourd' - and the "
            "disturbance reaches Augustine in Africa, who presses the "
            "concern by letter more than once (Ep. 112 = Augustine's Ep. "
            "75); the rare two-sided case - both parties independently "
            "attested in their own surviving letters."),
  frame=("We tell the gourd and the ivy as both sides kept it - the "
         "congregation's anger at a changed word, and the African "
         "bishop's letters pressing the question. Neither voice is ours "
         "to silence: this quarrel survives in two hands, and we tell "
         "it two-handed.")),
 "halstory03a": dict(owner="halfig001", tellable_as="scene",
  occasion=("The rupture with Rufinus, 401-403: the friend who had "
            "labored over the same Greek texts becomes the fiercest "
            "opponent as the church turns against Origen's teachings - "
            "both Apologiae survive (Rufinus 401; Jerome 401-403, "
            "addressed to Pammachius and Marcella); occurrence "
            "Documented, but the relative weight of doctrine versus "
            "broken friendship is genuinely contested and this story "
            "does not resolve it (the chunk's own rule)."),
  frame=("We tell the rupture as both men's own books keep it - the "
         "shared labor, the renunciation we made urgently and in "
         "public, the friend who would not make it as fully or as "
         "fast, and the harsh words that followed. Whether doctrine or "
         "the friendship's breaking weighed more, we do not decide; "
         "our record holds both and we hold it as it stands.")),
 "halstory04": dict(owner="halfig009", tellable_as="scene",
  occasion=("416: the Pelagian dispute arrives at the Bethlehem "
            "monastery as a mob - buildings burned, at least one of the "
            "household dead; Jerome's own account (the letter to "
            "Riparius) is 'strikingly vague on the particulars', and "
            "the household has never filled the silence in (occurrence "
            "Documented; details Inferential/Thin - the chunk's own "
            "split)."),
  frame=("We tell the attack in the same spare way our own record "
         "does: a dispute that had lived in letters came to our door "
         "as fire, and at least one of us died. How many came, what "
         "burned, who was lost - the one who wrote of it did not say, "
         "and we do not invent what he withheld.")),
 "halstory05": dict(owner="halfig003", tellable_as="scene",
  occasion=("Rome, 410: Alaric's soldiers in the house of Marcella, "
            "demanding treasure given away years before; her death soon "
            "after from the injuries or deprivation - Jerome's Ep. 127 "
            "to Principia, written two years after the event; "
            "single-source, no independent corroboration, and the "
            "reported irony follows the epitaph genre's conventions "
            "(the chunk's own genre caution)."),
  frame=("We tell how the Rome half of us ended: soldiers searching a "
         "house already emptied for the poor, and the widow who had "
         "emptied it dying of what followed. The irony is the "
         "epitaph's own - real, but shaped by a mourner's genre, and "
         "we carry it as such.")),
 "halstory06": dict(owner="halfig002", tellable_as="scene",
  occasion=("The Epitaphium Sanctae Paulae (Ep. 108) as formation "
            "portrait: senatorial birth, wealth given until the "
            "household could not say where it had gone, and still - "
            "from the same emptied purse - a monastery, a convent, a "
            "house of welcome raised; the bare death date (26 January "
            "404) Tier-1-adjacent, the narrative texture "
            "genre-idealized and not historical reporting of scenes "
            "(the chunk's own Tier Justification)."),
  frame=("This is how we remember Paula - not merely what happened to "
         "her but what her life was held up to show. That she gave "
         "until nothing could be found, and that she still built - we "
         "tell both together, as our record does, without deciding "
         "which was truer. It is an epitaph's portrait, and we say "
         "so.")),
 "halstory07": dict(owner="halfig003", tellable_as="scene",
  occasion=("Marcella's standing as the household remembers it (Ep. "
            "127, written after her death, for the scholar's own "
            "partly self-vindicating purposes): clergy bringing their "
            "hardest scriptural questions to her own house on her own "
            "authority once the scholar had left Rome - THE single "
            "most Author-Gravity-constrained story in this repository "
            "(single-source, Contested, post-mortem; the chunk's own "
            "words), and the evidentiary core of the ecology's one "
            "Tensional gravity."),
  frame=("We tell of the widow the clergy consulted carefully, for "
         "the memory comes to us in one voice, written after her "
         "death, by the very man whose answers she had once disputed "
         "- to learn, he says, not to win. Her standing was real and "
         "her wealth her own; how often the clergy came, no record "
         "but his remains to say. We never tell it as rivalry: the "
         "trust was of one kind, differently held.")),
 "halstory08": dict(owner="halfig001", tellable_as="scene",
  occasion=("The Ciceronian dream (Ep. 22, to Eustochium): dragged "
            "before a judge, 'You lie. You are a Ciceronian, not a "
            "Christian' - the scholar's own reported dream, told of "
            "himself inside an exhortatory letter; the tension it "
            "dramatizes Widely Accepted as lived reality, the dream "
            "as literal event Inferential/Thin and genre-shaped (the "
            "dream-vision was a recognized rhetorical device - the "
            "chunk's own confidence split)."),
  frame=("We tell the dream as he told it of himself: the tribunal, "
         "the sentence - a Ciceronian, not a Christian - and the "
         "waking that set the loved books aside for a season. Whether "
         "the night itself happened so, we hold as he framed it, a "
         "story told to form; that the tension was real and lifelong, "
         "his own pages prove either way.")),
 "halstory09": dict(owner="halfig001", tellable_as="background-fact",
  occasion=("The Vita Malchi and Vita Hilarionis as the household's "
            "own literary production: desert romances answering the "
            "Egyptian stories encountered on the founding journey - "
            "explicit hagiographic-romance genre, the clearest Tier 3 "
            "case in the repository, and structurally about named "
            "individuals, which is exactly why they cannot border "
            "Tier 4 (the chunk's own Tier Justification)."),
  frame=("Our scholar wrote desert tales of his own - the captive "
         "monk who kept his vows, the hermit who went to find what "
         "remained when all else was stripped away. We tell them as "
         "what they are: our own answer to Egypt's stories, models "
         "of what we believed formation could become - not "
         "chronicles of two men's lives.")),
 "halstory10": dict(owner="halfig009", tellable_as="scene",
  occasion=("Tier-4 composite: the typical shape of a day at the "
            "Bethlehem double monastery, assembled ONLY from attested "
            "elements (communal discipline per Ep. 108; Hebrew study "
            "under paid non-Christian teachers per the prefaces; the "
            "Bethlehem-Rome correspondence; manual labor by monastic-"
            "template analogy, declared as analogy) - no single "
            "source narrates a specific day, no individual is its "
            "subject (the chunk's own Source Identification table, "
            "parked verbatim in this record's body)."),
  frame=("This is no remembered day but the shape our days took - "
         "prayer and the correction of a Hebrew word held as one "
         "discipline worked from different ends. We say plainly that "
         "it is a pattern assembled from what is attested; and if "
         "you ask for the hours and the psalms, we will tell you "
         "honestly that no record of ours kept them.")),
 "halstory11": dict(owner="halfig001", tellable_as="scene",
  occasion=("Tier-4 composite of the translation process's typical "
            "shape - consultation with a Hebrew teacher, rendering "
            "against Greek and Hebrew both, the defensive preface "
            "and its dedication - reconstructed from independently "
            "attested stages (the prefaces; the documented "
            "dedication pattern of the Bethlehem commentaries); "
            "'composite in method, but not in subject' - on this "
            "world's own evidence the work was performed by exactly "
            "one person, which is why this record is owned by the "
            "scholar's figure and not the community (the chunk's own "
            "Tier Justification, quoted; the CO-P2-06 call "
            "documented in the S2.4 checkpoint)."),
  frame=("This is how the work went, book by book - not one "
         "remembered afternoon but the pattern of a working life: "
         "the teacher consulted, the word weighed against two "
         "tongues, and at the end a preface to defend the choices "
         "and a dedication to the one whose asking had begun it. "
         "One man's own singular practice, reconstructed from its "
         "attested stages - and never told as a single attested "
         "day. Of how fluent the Hebrew finally was, we claim no "
         "more than our record can carry.")),
}

FIGURES = [
 dict(id="halfig001",
      names=[{"name": "the scholar among us (as this household's chunks "
                      "speak of him)", "name_kind": "in-world"},
             {"name": "Jerome of Stridon (Hieronymus)", "name_kind": "scholarly"}],
      narratable=True,
      story_ids=["halstory01", "halstory02", "halstory03", "halstory03a",
                 "halstory08", "halstory09", "halstory11"],
      attribution_note=(
          "The world's Author-Gravity center in the strongest form any "
          "world in this fleet has: nearly the entire narrative record "
          "survives in his voice alone (Doc_02's Author Gravity "
          "Assessment), so even stories about OTHERS (Paula's journey, "
          "Marcella's standing and death) are his tellings - each such "
          "record names the pen. His Hebrew fluency is Contested "
          "(hallex12's split); his own two-sided stories (03/03a) are "
          "the rare exceptions where an opponent's text survives "
          "independently.")),
 dict(id="halfig002",
      names=[{"name": "Paula", "name_kind": "in-world"},
             {"name": "Paula of Rome (347-404)", "name_kind": "scholarly"}],
      narratable=True, story_ids=["halstory01", "halstory06"],
      attribution_note=(
          "Founder-patron of the Bethlehem pole; known almost entirely "
          "through Jerome's Ep. 108 epitaph - a commemorative genre "
          "whose idealizing conventions halstory06 carries explicitly; "
          "her death date (26 January 404) is the record's "
          "Tier-1-adjacent fixed point.")),
 dict(id="halfig003",
      names=[{"name": "Marcella", "name_kind": "in-world"},
             {"name": "Marcella of Rome (d. 410/411)", "name_kind": "scholarly"}],
      narratable=True, story_ids=["halstory05", "halstory07"],
      attribution_note=(
          "The Rome pole's own center and the ecology's Tensional-"
          "gravity figure - and the single most Author-Gravity-"
          "constrained figure in the repository: everything rests on "
          "Jerome's post-mortem Ep. 127 (single-voice; srcHAL001's "
          "Marcella-correspondence-list caveat and srcHAL012's "
          "unverified Ep. 24/127 pairing flag both bear here). Her "
          "standing is told ONLY with that frame attached "
          "(halstory07's own rule).")),
 dict(id="halfig004",
      names=[{"name": "Eustochium", "name_kind": "in-world"},
             {"name": "Julia Eustochium (c. 368-418/419/420)", "name_kind": "scholarly"}],
      narratable=True, story_ids=["halstory01"],
      attribution_note=(
          "Paula's daughter, the virginitas category's own person "
          "(hallex04), addressee of the record's most famous letters "
          "(Epp. 22, 108) - but no surviving story in this inventory "
          "CENTERS her; she is narratable within the journey record "
          "only. Her death year (418/419/420, Contested clustering) "
          "is halcore001's institutional-continuity terminus, carried "
          "with no order asserted.")),
 dict(id="halfig005",
      names=[{"name": "Blaesilla", "name_kind": "in-world"},
             {"name": "Blaesilla of Rome (d. 384)", "name_kind": "scholarly"}],
      narratable=True, story_ids=["halstory02"],
      attribution_note=(
          "Paula's elder daughter, whose death after severe fasting is "
          "the Rome crisis's pivot - known through Jerome's own "
          "letters, i.e., through the pen of the very teacher the city "
          "blamed; halstory02 carries that frame.")),
 dict(id="halfig006",
      names=[{"name": "Augustine, the bishop in Africa", "name_kind": "in-world"},
             {"name": "Augustine of Hippo", "name_kind": "scholarly"}],
      narratable=True, story_ids=["halstory03"],
      attribution_note=(
          "A cross-tradition figure, NOT this world's own voice (the "
          "syrfig008/Basil precedent) - but unlike Basil's legend-only "
          "appearance, his own letters survive independently "
          "(srcHAL009), making halstory03 one of the record's two "
          "genuinely two-sided stories; narratable only within that "
          "correspondence frame. The cross-build boundary rides "
          "srcHAL009's license: his own world is not built here.")),
 dict(id="halfig007",
      names=[{"name": "Rufinus, the friend who became an opponent", "name_kind": "in-world"},
             {"name": "Rufinus of Aquileia", "name_kind": "scholarly"}],
      narratable=True, story_ids=["halstory03a"],
      attribution_note=(
          "The other two-sided case: his Apologia contra Hieronymum "
          "(srcHAL007) survives in his own voice, so the rupture is "
          "never told from one side only; narratable only within "
          "halstory03a's both-perspectives-nameable frame (the "
          "chunk's own rule: the doctrine-vs-friendship weight is "
          "not resolved).")),
 dict(id="halfig008",
      names=[{"name": "Fabiola", "name_kind": "in-world"},
             {"name": "Fabiola of Rome (d. 399/400)", "name_kind": "scholarly"}],
      narratable=False, story_ids=[],
      accepted_refusal_note=(
          "Load-bearing in the lexicon (hallex14 - the nosocomium she "
          "founded, Ep. 77) but NO narratable scene survives in this "
          "story inventory: asked for a Fabiola story, the voice "
          "declines honestly - her founding is kept, her days are not "
          "(the Aphrahat/syrfig002 precedent). The Ep. 77.6 Perseus "
          "verification is the pre-freeze re-sweep's editions-class "
          "item.")),
 dict(id="halfig009",
      names=[{"name": "the household itself - Rome and Bethlehem as one "
                      "project", "name_kind": "in-world"},
             {"name": "the Hieronymian ascetic-literary circle", "name_kind": "scholarly"}],
      narratable=True, story_ids=["halstory04", "halstory10"],
      attribution_note=(
          "Composite/communal owner per CO-P2-06's standing "
          "convention: the pattern-day composite (halstory10, no "
          "individual subject) and the 416 attack (halstory04 - "
          "suffered by the household as such, its particulars left "
          "vague by the record's own restraint). halstory11 is NOT "
          "here despite being Tier-4: its chunk rules it 'composite "
          "in method, but not in subject' - see halfig001.")),
]


def parse_chunk(path: Path):
    text = path.read_text(encoding="utf-8")
    head, sep, rest = text.partition("\n---\n")
    assert sep, path.name
    fm, current = {}, None
    for line in head.splitlines():
        m = re.match(r"^([A-Za-z-]+):\s*(.*)$", line)
        if m:
            current = m.group(1)
            fm[current] = m.group(2).strip()
        elif current and line.strip():
            fm[current] += " " + line.strip()
    secs = {}
    for m in re.finditer(r"^## (.+?)\s*\n(.*?)(?=^## |\Z)", rest, re.S | re.M):
        secs[m.group(1).strip()] = re.sub(
            r"^-{3,}\s*$", "", m.group(2), flags=re.M).strip()
    return fm, secs


def sources_for(rid: str, source_line: str):
    if rid in COMPOSITE_SOURCES:
        locus = ("Composite - elements per the chunk's own Source "
                 "Identification table (parked verbatim in this record's "
                 "body; the monastic-template element of halstory10 is "
                 "declared analogy, Doc_01 SS6/Doc_08, no row owed): "
                 + source_line)
        return [{"source_id": sid, "locus": locus}
                for sid in COMPOSITE_SOURCES[rid]]
    out, seen = [], set()
    for key, sid in SOURCE_KEYS:
        if key.lower() in source_line.lower() and sid not in seen:
            seen.add(sid)
            out.append({"source_id": sid, "locus": source_line})
    return out or [{"source_id": "srcHAL-UNRESOLVED", "locus": source_line}]


def main():
    for path in sorted(CHUNKS.glob("*.md")):
        fm, secs = parse_chunk(path)
        rid = "hal" + path.stem.split("_")[1]      # hal_story03a_x -> halstory03a
        meta = STORY[rid]
        tier = int(re.sub(r"[^\d]", "", fm.get("Tier", "1")) or 1)
        retrieve_when = [c.strip() for c in
                         fm.get("Retrieve-When", "").split(";") if c.strip()]
        dnrw = [{"condition_type": "sense-disambiguation", "text": c.strip()}
                for c in fm.get("Do-Not-Retrieve-When", "").split(";")
                if c.strip()]
        rec = {
            "id": rid, "world_id": WID, "record_type": "story",
            "schema_version": 1, "jobs": [1, 2, 3], "register": "emic",
            "review_state": "draft", "cache_stability": "static",
            "title": fm.get("Story-Title", ""),
            "narrative_tier": {"tier": tier,
                               "justification": secs.get("Tier Justification", "")},
            "text": secs.get("Story Text", ""),
            "attested_occasion": meta["occasion"],
            "tellable_as": meta["tellable_as"],
            "owner_figure_id": meta["owner"],
            "voice_surface": (meta["frame"] + " Usage guidance (chunk, "
                              "verbatim): " + secs.get("Usage Guidance", "")),
            "confidence_line": fm.get("Confidence", ""),
            "retrieval": {"tier": tier, "retrieve_when": retrieve_when,
                          "do_not_retrieve_when": dnrw,
                          "force_llm_vote": False},
            "sources": sources_for(rid, fm.get("Source", "")),
        }
        body = (f"Migrated at the S6.2/HAL S2.4-equivalent (2026-07-31) from "
                f"`data/hieronymian_world/story_chunks/{path.name}` (mapping "
                f"in `wrs/migrate/s62_hal_s24.py`; Story Text / Tier "
                f"Justification / Usage Guidance / Confidence line verbatim; "
                f"occasion/owner/frame authored per Desert-ALX-SYR S2.4 "
                f"conventions).")
        fec = secs.get("Formation Ecology Connection", "")
        if fec:
            body += "\n\n" + FEC_DELIM + " " + fec
        if secs.get("Source Identification"):
            body += ("\n\n[Source Identification - the composite's own "
                     "element-to-source table, parked verbatim (CO-P2-06 "
                     "composite convention)] " + secs["Source Identification"])
        if secs.get("Absent Story Note"):
            body += ("\n\n[Absent Story Note - the chunk's own "
                     "honest-brevity rule, parked verbatim] "
                     + secs["Absent Story Note"])
        (OUT / "story").mkdir(exist_ok=True)
        emit_record(rec, body, OUT / "story" / f"{rid}.md")
    for fig in FIGURES:
        rec = {"id": fig["id"], "world_id": WID, "record_type": "figure",
               "schema_version": 1, "jobs": [1, 3], "register": "etic",
               "review_state": "draft", "names": fig["names"],
               "narratable": fig["narratable"], "story_ids": fig["story_ids"]}
        for k in ("accepted_refusal_note", "attribution_note"):
            if fig.get(k):
                rec[k] = fig[k]
        (OUT / "figure").mkdir(exist_ok=True)
        emit_record(rec, "Authored at the S6.2/HAL S2.4-equivalent "
                    "(2026-07-31); see wrs/migrate/s62_hal_s24.py.",
                    OUT / "figure" / f"{fig['id']}.md")
    print(f"wrote {len(STORY)} stories + {len(FIGURES)} figures + 0 quotes "
          f"(the candidate Ep. 22.30 dream-rebuke declared, riding "
          f"halstory08 verbatim - no vetting apparatus in the build docs)")


if __name__ == "__main__":
    main()
