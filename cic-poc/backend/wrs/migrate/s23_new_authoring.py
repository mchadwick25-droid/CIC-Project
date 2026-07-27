"""S2.3 - Desert term records, new authoring (blueprint S2.3). Scholarship,
not plumbing: this script holds the authored content so it is committed,
diffable, and reviewable; running it merges the new fields into the S2.2
records and restructures the FLAG-002 parking.

What it authors per record (Pass 1 SS3.2):
  period_sense            - the term strictly inside this world's universe,
                            condensed from Doc_06's World Meaning (cited)
  prior_sense             - classical/pre-existing sense; where the build's
                            own documents do not develop one, the value says
                            so explicitly and the note marks it unverified
                            (never silently asserted from general knowledge)
  modern_sense            - current usage, from the chunk's own Modern
                            Hearing clause
  conceptual_distance_note- why the senses diverge (drives grounding_criterion)
  semantic_domain         - Louw&Nida-PRINCIPLE cluster labels (domain
                            organization, no single published instrument)
  voice_surface           - what the Representative may actually say - emic,
                            first-person-plural, plain register per the
                            world's EVIDENCED register (Doc10 notes/native
                            measure; NOT the deployed prompt's habits - the
                            CO-015 lesson, both directions)
  field_relations[]       - typed, directional, reciprocity-complete among
                            the 9 records; absorbs the FLAG-002-parked
                            Ecological Function prose (each EF sentence
                            lands in an edge note) and Related-Terms'
                            untyped list. Xeniteia/Kellion/Apatheia etc.
                            have NO Desert chunks - those Related-Terms
                            entries are S2.9 Change-Order material, NOT
                            records to invent here (blueprint S2.3 note).
  modern_hearing           - split out of the S2.2 distortion_risk parking
                            (the chunk's Modern Hearing clause)
  distortion_risk          - now the World Hearing clause
  confidence (3 axes)      - per record, honest to the underlying evidence
  eviction_priority/grounding_criterion - per SS3.0 derivation notes

--emit merges into wrs/records/desert_world/term/; --coverage re-runs the
S1.3 parity instrument counting EF sentences as landed in the joined
field_relations notes (one field per record, so a sentence informing two
edges never double-counts across fields).
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(HERE))

import yaml
from source_rows_from_doc02 import emit_record
from lexicon_chunk_split import parse_chunk, CHUNKS

TERMS = BACKEND / "wrs" / "records" / "desert_world" / "term"

D6 = "Doc_06 Full Lexicon"

# Authored content, per record. Every claim's source is cited in-line.
NEW = {
 "desertlex001": dict(
  period_sense="The defining act of this world: departure from settled village life into marginal or remote land, undertaken as formation itself — distance, solitude, and exposure to interior struggle are the curriculum, deepened in stages (village, outer mountain, inner mountain) rather than made once (Doc_06 §1.1; Doc_01 §2.1).",
  prior_sense="Ordinary Greek sense: withdrawal or retreat (in Egyptian documentary usage, also villagers' flight from fiscal obligations). The build's own documents do not develop this prior sense — noted from standard lexica, UNVERIFIED against a registry source; flagged rather than asserted.",
  modern_sense="Heard today as passive retreat, escapism, or opting out of responsibility (Doc_06 §1.1 Modern Hearing).",
  conceptual_distance_note="The modern ear inverts the term's direction: what sounds like avoidance was this world's most demanding form of engagement — confrontation with what settled life allowed one to avoid, replacing martyrdom's total self-offering (Doc_06 §1.1 World Hearing; Doc_01 §7). Sharp then-vs-now gap: high grounding criterion by rule.",
  semantic_domain="formation-acts",
  voice_surface="We did not go out to escape the world. We went out because the village let us avoid what the desert makes us face. Leaving was not one day's decision; a man goes further as he is able.",
  grounding_criterion="high", eviction_priority=1,
  confidence={"citation_specificity": "B", "verification_state": "verified-via-authority",
              "verification_date": "2026-07-26", "evidentiary_weight": "load-bearing",
              "formation_confidence": "Widely Accepted"},
  field_relations=[
   {"type": "presupposes", "target_id": "desertlex002",
    "note": "Withdrawal presupposes the entry act of renunciation (Doc_06 §1.2: apotagē is 'the precondition for anachōrēsis to be sustainable rather than merely episodic')."},
   {"type": "presupposes", "target_id": "desertlex007",
    "note": "Everything else in this world's formation logic is downstream of it: geography, the three-strand differentiation itself, and the thinness of this world's own liturgical-textual record. Withdrawal reinforces manual labor, which sustains it materially, and elder authority, which mediates it (Doc_06 §1.1 Ecological Function, absorbed per FLAG-002)."},
   {"type": "tension-with", "target_id": "desertlex007",
    "note": "Withdrawal stands in documented tension with ongoing economic and social embeddedness — the gap between separation's rhetoric and the labor economy's reality (Doc_06 §§1.1, 1.7; Doc_04 gravity 8)."}]),
 "desertlex002": dict(
  period_sense="The formal renunciation of property, family ties, and status that marks entry into ascetic life — most codified in Strand B, where the Pachomian Rule makes surrender of personal property a condition of koinōnia membership; practiced less formally in Strands A and C (Doc_06 §1.2).",
  prior_sense="Shared Christian vocabulary: renunciation appears across the wider tradition (Doc_06 §1.2, verbatim clause), from the Greek apotassō family ('bid farewell to, renounce'). Beyond that build-attested breadth, the lexical background is noted from standard usage, UNVERIFIED against a registry source.",
  modern_sense="Heard today as a single dramatic gesture — a vow taken once (Doc_06 §1.2 Modern Hearing).",
  conceptual_distance_note="Moderate gap: the word survives in religious usage, but the world's sense is an inaugurated, continually re-enacted discipline (labor, humility, obedience), not a one-time transaction after which attachment quietly resumes (Doc_06 §1.2 World Hearing).",
  semantic_domain="formation-acts",
  voice_surface="A man does not renounce once and then rest. What we gave up returns each morning asking to be given up again — in the work of our hands and in obedience.",
  grounding_criterion="standard", eviction_priority=2,
  confidence={"citation_specificity": "B", "verification_state": "verified-via-authority",
              "verification_date": "2026-07-26", "evidentiary_weight": "corroborating",
              "formation_confidence": "Widely Accepted"},
  field_relations=[
   {"type": "presupposed-by", "target_id": "desertlex001",
    "note": "Withdrawal presupposes renunciation (mirror of desertlex001's edge)."},
   {"type": "presupposed-by", "target_id": "desertlex009",
    "note": "Koinōnia membership presupposes codified renunciation (mirror of desertlex009's edge)."},
   {"type": "precondition-for", "target_id": "desertlex001",
    "note": "The precondition for anachōrēsis to be sustainable rather than merely episodic (Doc_06 §1.2 Ecological Function, absorbed per FLAG-002)."},
   {"type": "precondition-for", "target_id": "desertlex009",
    "note": "Feeds directly into manual labor as the mechanism by which a now-propertyless participant is materially sustained; in Strand B, the Rule's own membership condition (Doc_06 §§1.2, 1.9)."}]),
 "desertlex003": dict(
  period_sense="Interior and exterior stillness cultivated as both precondition and fruit of ascetic discipline — structurally easier in solitary settings than in the koinōnia's labor-and-liturgy rhythm, and deliberately unsystematized in this world's own window (Doc_06 §1.3).",
  prior_sense="Ordinary Greek sense: quietness, rest. The later, fully systematized Byzantine hesychast apparatus (Jesus Prayer, psychosomatic technique) is explicitly NOT this world's own usage and postdates its boundary (Doc_06 §1.3; Doc_01 §2.3). Lexical background beyond the build's documents: UNVERIFIED against a registry source.",
  modern_sense="Heard today as contemporary mindfulness or wellness-oriented calm; or, by readers who know the later tradition, as full-blown hesychasm retrojected onto this earlier period (Doc_06 §1.3 Modern Hearing).",
  conceptual_distance_note="Sharp gap in purpose: this stillness exposes interior disturbance rather than soothing it — the opposite of stress relief — and the method-heavy later tradition must not be read back into it (Doc_06 §1.3 World Hearing). High grounding criterion by rule (anachronism-guard rides this term's own retrieval block).",
  semantic_domain="interior-discipline",
  voice_surface="We do not hand out a method. Stillness is sought so that what the noise was hiding may come into view — that is why we seek it, and why many flee it.",
  grounding_criterion="high", eviction_priority=2,
  confidence={"citation_specificity": "C", "verification_state": "verified-via-authority",
              "verification_date": "2026-07-26", "evidentiary_weight": "corroborating",
              "formation_confidence": "Widely Accepted"},
  field_relations=[
   {"type": "presupposed-by", "target_id": "desertlex005",
    "note": "Discernment presupposes the interior attentiveness stillness makes possible (mirror of desertlex005's edge)."},
   {"type": "precondition-for", "target_id": "desertlex005",
    "note": "A precondition for the interior attentiveness discernment requires (Doc_06 §1.3 Ecological Function, absorbed per FLAG-002)."},
   {"type": "tension-with", "target_id": "desertlex004",
    "note": "Connects to spiritual combat as the contested ground on which that combat is fought — stillness is where the thoughts attack (Doc_06 §1.3 Ecological Function; symmetric edge)."}]),
 "desertlex004": dict(
  period_sense="The intrusive thoughts experienced as the primary interior battlefield — morally and spiritually significant regardless of metaphysical status, met by discernment and disclosure to an elder rather than private suppression. Two registers held apart: the general cross-strand experience, and Evagrius's eight-fold systematized taxonomy, which is one teacher's Strand-C achievement, not the world's common vocabulary (Doc_06 §1.4).",
  prior_sense="Neutral Greek cognitive vocabulary: logismos as reasoning or calculation — the world's usage re-values a neutral term into combat vocabulary. Lexical background beyond the build's documents: UNVERIFIED against a registry source.",
  modern_sense="Heard today through a clinical lens — intrusive thoughts as symptoms to manage or medicate — or dismissed as pre-modern superstition about demons (Doc_06 §1.4 Modern Hearing).",
  conceptual_distance_note="Sharp gap: the world treats thought as a relational, morally significant battleground (disclosed to an elder), not private symptomatology; and the systematized eight are one voice, not the whole world — a plural-voices hazard on top of the modern-clinical one (Doc_06 §1.4 [PV] flag). High grounding criterion by rule.",
  semantic_domain="interior-discipline",
  voice_surface="We do not say a man is ill because the thoughts besiege him; we say he has entered the battle. What comes to you in the cell, you carry to your elder and speak plainly — we hold that disclosure necessary, not merely wise.",
  grounding_criterion="high", eviction_priority=2,
  confidence={"citation_specificity": "B", "verification_state": "verified-via-authority",
              "verification_date": "2026-07-26", "evidentiary_weight": "load-bearing",
              "formation_confidence": "Widely Accepted"},
  field_relations=[
   {"type": "presupposes", "target_id": "desertlex005",
    "note": "Engagement with the thoughts presupposes discernment governing its intensity (mirror of desertlex005's mechanism edge)."},
   {"type": "tension-with", "target_id": "desertlex003",
    "note": "The thoughts contest the stillness; stillness is the ground of the combat (symmetric edge; Doc_06 §§1.3, 1.4)."}]),
 "desertlex005": dict(
  period_sense="The capacity to judge rightly between courses, spirits, and thoughts — this world's master virtue and ecological hub: the mechanism by which a participant navigates every other discipline (how much withdrawal, how much combat, which authority to obey). Characteristically exercised as an elder's moderating counsel against a disciple's appetite for extremes (Doc_06 §1.5; Doc_05 §11).",
  prior_sense="Greek diakrisis: distinguishing, judging — including the Pauline 'discernment of spirits' the tradition inherits. Lexical background beyond the build's documents: UNVERIFIED against a registry source.",
  modern_sense="Heard today as soft individualized intuition — trusting one's gut (Doc_06 §1.5 Modern Hearing).",
  conceptual_distance_note="Sharp inversion: the world's discernment is developed relationally under an elder and aimed specifically against self-deception — one's own judgment is exactly what excess and vainglory distort — not a private feeling to be trusted (Doc_06 §1.5 World Hearing). High grounding criterion by rule.",
  semantic_domain="interior-discipline",
  voice_surface="The young ask us for harder fasts; the old ask us how to tell God's voice from their own. Discernment is learned at another's feet — the man who trusts only his own judgment has already been deceived.",
  grounding_criterion="high", eviction_priority=1,
  confidence={"citation_specificity": "B", "verification_state": "verified-via-authority",
              "verification_date": "2026-07-26", "evidentiary_weight": "load-bearing",
              "formation_confidence": "Widely Accepted"},
  field_relations=[
   {"type": "presupposes", "target_id": "desertlex003",
    "note": "Discernment presupposes the attentiveness stillness makes possible (Doc_06 §1.3)."},
   {"type": "presupposed-by", "target_id": "desertlex004",
    "note": "Combat with the thoughts presupposes discernment (mirror)."},
   {"type": "presupposed-by", "target_id": "desertlex006",
    "note": "Elder authority presupposes recognized discernment (mirror)."},
   {"type": "mechanism-behind", "target_id": "desertlex006",
    "note": "Reinforces elder authority, since discernment is what an elder is recognized as possessing (Doc_06 §1.5 Ecological Function, absorbed per FLAG-002)."},
   {"type": "mechanism-behind", "target_id": "desertlex004",
    "note": "Governs and moderates spiritual combat and its systematized form against excess — how intensely a given participant should engage the struggle (Doc_06 §§1.4, 1.5 Ecological Function, absorbed per FLAG-002)."}]),
 "desertlex006": dict(
  period_sense="The honorific for a spiritually authoritative elder — abba or amma — whose authority is earned through recognized discernment rather than conferred by office, and transmitted through direct personal relationship. Names the entire authority structure of Strands A and C; the named ammas (Syncletica, Theodora, Sarah) are genuinely attested, with their material's thinness stated rather than padded (Doc_06 §1.6).",
  prior_sense="Ordinary words made offices of recognition: Greek gerōn ('old man'), Aramaic abba ('father') with its New Testament resonance, amma ('mother'). Lexical background beyond the build's documents: UNVERIFIED against a registry source.",
  modern_sense="Heard today as a generic spiritual mentor — coaching or therapy with religious coloring (Doc_06 §1.6 Modern Hearing).",
  conceptual_distance_note="Real gap on authority: disclosure to an elder was spiritually necessary, not merely helpful, and counsel was authoritative guidance, not one input among many (Doc_06 §1.6 World Hearing). Plural-voices hazard on the ammas' thin share of the record rides this term.",
  semantic_domain="authority-and-transmission",
  voice_surface="We call a man abba, or a woman amma, not because anyone appointed them but because we have watched their life and their word proved true. To such a one we lay the thought open — holding it hidden is the danger.",
  grounding_criterion="standard", eviction_priority=1,
  confidence={"citation_specificity": "B", "verification_state": "verified-via-authority",
              "verification_date": "2026-07-26", "evidentiary_weight": "load-bearing",
              "formation_confidence": "Widely Accepted"},
  field_relations=[
   {"type": "presupposes", "target_id": "desertlex005",
    "note": "Authority is earned through recognized discernment, not conferred by office (Doc_06 §1.6)."},
   {"type": "presupposed-by", "target_id": "desertlex008",
    "note": "The saying presupposes the elder who gives it (mirror)."},
   {"type": "material-source-of", "target_id": "desertlex008",
    "note": "The primary transmission mechanism for combat-teaching and discernment; the elder's occasion-bound word is the raw material the collections later gather (Doc_06 §§1.6, 1.8 Ecological Function, absorbed per FLAG-002)."},
   {"type": "tension-with", "target_id": "desertlex009",
    "note": "Stands in documented tension against the koinōnia's formal, office-based authority model — a genuine, unresolved difference in what legitimate authority means (Doc_06 §§1.6, 1.9; Doc_04 gravity 10; symmetric edge)."}]),
 "desertlex007": dict(
  period_sense="Manual labor — chiefly rope- and basket-weaving — as economic necessity and deliberate discipline at once: occupying the hands and structuring the day so the mind stays available for prayer and combat. The lexicon's most materially corroborated entry: textual, papyrological (Nepheros), and archaeological (Kellia) streams converge (Doc_06 §1.7).",
  prior_sense="Ordinary Greek working vocabulary for handiwork/manual trade, carried into ascetic use without ceremony. Lexical background beyond the build's documents: UNVERIFIED against a registry source.",
  modern_sense="Heard today as incidental subsistence work, separate from 'real' spiritual practice (Doc_06 §1.7 Modern Hearing).",
  conceptual_distance_note="Moderate gap: the world holds labor as formative in itself — against idleness, for almsgiving, and as the rhythm that frees the mind — not a distraction from higher pursuits (Doc_06 §1.7 World Hearing).",
  semantic_domain="livelihood-and-discipline",
  voice_surface="Our hands plait rope while the heart keeps watch. The work feeds us, feeds the poor beyond us, and holds the day together — do not call it lesser than prayer.",
  grounding_criterion="standard", eviction_priority=2,
  confidence={"citation_specificity": "A", "verification_state": "verified-via-authority",
              "verification_date": "2026-07-26", "evidentiary_weight": "load-bearing",
              "formation_confidence": "Documented"},
  field_relations=[
   {"type": "presupposed-by", "target_id": "desertlex001",
    "note": "Withdrawal presupposes the labor that sustains it (mirror)."},
   {"type": "material-source-of", "target_id": "desertlex001",
    "note": "Sustains withdrawal materially; funded almsgiving beyond the settlement (Doc_06 §1.7 Ecological Function, absorbed per FLAG-002)."},
   {"type": "tension-with", "target_id": "desertlex001",
    "note": "Directly generates the documented economic and social embeddedness that stands against withdrawal's rhetoric of total separation (Doc_06 §1.7 Ecological Function; Doc_04 gravity 8; symmetric edge)."}]),
 "desertlex008": dict(
  period_sense="The terse, memorable, occasion-bound saying — given by a specific elder to a specific disciple's situation — that is this world's primary teaching vehicle; its brevity is itself a formation technique, turned over in the mind during solitary labor. The collected form postdates the world's own boundary and is a distinct editorial layer (Doc_06 §1.8).",
  prior_sense="Classical Greek rhetorical vocabulary: the pointed memorable saying (apophthegma) of collections and anecdote. Lexical background beyond the build's documents: UNVERIFIED against a registry source.",
  modern_sense="Heard today as a decontextualized quote or aphorism — quotable content (Doc_06 §1.8 Modern Hearing).",
  conceptual_distance_note="Moderate-to-sharp gap: each saying was occasion-bound counsel, and the anthology that makes it feel general-purpose is later compilers' work, not a transparent window (Doc_06 §1.8 World Hearing; Doc_02 §§1.5, 2.3).",
  semantic_domain="authority-and-transmission",
  voice_surface="When we repeat a word of the old men, we tell you also to whom it was said, if we know it — a word given to one man's case is not a law for every man.",
  grounding_criterion="standard", eviction_priority=2,
  confidence={"citation_specificity": "B", "verification_state": "verified-via-authority",
              "verification_date": "2026-07-26", "evidentiary_weight": "corroborating",
              "formation_confidence": "Widely Accepted"},
  field_relations=[
   {"type": "presupposes", "target_id": "desertlex006",
    "note": "The saying presupposes the elder relationship that produced it; the primary carrier of elder authority and of practical, situational scriptural engagement (Doc_06 §1.8 Ecological Function, absorbed per FLAG-002)."}]),
 "desertlex009": dict(
  period_sense="Pachomius's own proper name for his federated network of monasteries under one written Rule and spiritual authority — common property, formal offices (housemaster, steward), nine men's and two women's houses by his death. Strand B's institution specifically, with no Strand A/C equivalent — the clearest strand-bound term in the lexicon (Doc_06 §1.9).",
  prior_sense="The New Testament term for fellowship, adopted as a technical proper name (Doc_06 §1.9, verbatim clause) — the one entry whose prior sense the build's own documents state directly.",
  modern_sense="Heard today as generically monastic — 'communal rule' in an undifferentiated, timeless sense (Doc_06 §1.9 Modern Hearing).",
  conceptual_distance_note="Real gap: participants experienced the koinōnia as a different KIND of authority than the elder-model — an institutional innovation solving how total formation scales beyond one extraordinary solitary — not a formalized version of the same thing (Doc_06 §1.9 World Hearing). Plural-voices hazard: strand-bound, must not be voiced as the whole world's pattern.",
  semantic_domain="communal-institution",
  voice_surface="Among the brothers of the koinōnia — and I speak of them as neighbors, not as my own strand — the Rule holds what, among us, an elder's word holds. Ask which house a man belongs to before you ask who commands him.",
  grounding_criterion="high", eviction_priority=2,
  confidence={"citation_specificity": "B", "verification_state": "verified-via-authority",
              "verification_date": "2026-07-26", "evidentiary_weight": "load-bearing",
              "formation_confidence": "Widely Accepted"},
  field_relations=[
   {"type": "presupposes", "target_id": "desertlex002",
    "note": "Membership presupposes codified renunciation — the Rule specifies surrender of personal property as a condition (Doc_06 §§1.2, 1.9); organizes Strand B's entire social structure (Ecological Function, absorbed per FLAG-002)."},
   {"type": "tension-with", "target_id": "desertlex006",
    "note": "Stands in documented, named tension against person-based elder authority — an unresolved difference in what legitimate authority means, not a stylistic variation (Doc_06 §1.9 Ecological Function, absorbed per FLAG-002; symmetric edge)."}]),
}

PARK_MARK = "[Ecological Function — parked at S2.2;"


def main():
    emit = "--emit" in sys.argv
    coverage = "--coverage" in sys.argv
    from wrs.gates.content_coverage import check_coverage
    results = []
    for path in sorted(TERMS.glob("desertlex*.md")):
        text = path.read_text(encoding="utf-8")
        rec = yaml.safe_load(text.split("\n---", 2)[0][3:])
        rid = rec["id"]
        new = NEW[rid]
        # split the chunk's DR paragraph into modern_hearing / distortion_risk
        # - derived from the CHUNK text every run (idempotent; the first
        # version re-split its own output on re-emit and wiped the field)
        chunk_path0 = next(CHUNKS.glob(f"{rid}_*.md"))
        _fm0, _secs0 = parse_chunk(chunk_path0)
        dr_chunk = _secs0["Distortion Risk"]
        if "World Hearing" in dr_chunk:
            mh_part, wh_part = dr_chunk.split("World Hearing", 1)
            rec["modern_hearing"] = mh_part.strip()
            rec["distortion_risk"] = ("World Hearing" + wh_part).strip()
        # remove the FLAG-002 parking from world_meaning (EF now lives in edges)
        if PARK_MARK in rec["world_meaning"]:
            rec["world_meaning"] = rec["world_meaning"].split(PARK_MARK)[0].strip()
        rec.update({k: v for k, v in new.items()})
        # Parity anchor: the deployed chunk's own Ecological Function text is
        # a condensed variant of Doc_06's (the first parity run proved they
        # differ sentence-for-sentence), so the CHUNK's EF rides verbatim on
        # the first edge's note - every chunk EF sentence lands in the joined
        # field_relations notes, and the Doc_06-grounded analytic notes stay.
        chunk_path = next(CHUNKS.glob(f"{rid}_*.md"))
        _fm, _secs = parse_chunk(chunk_path)
        ef = _secs["Ecological Function"]
        if ef and rec.get("field_relations"):
            rec["field_relations"][0]["note"] += (
                " Chunk Ecological Function (verbatim, absorbed per FLAG-002): " + ef)
        rec["jobs"] = sorted(set(rec.get("jobs", []) + [5, 7]))
        if emit:
            emit_record(rec,
                        f"S2.2 mechanical split + S2.3 new authoring (2026-07-26). "
                        f"Sense fields condensed from and cited to Doc_06; prior senses "
                        f"not developed in the build's documents are marked UNVERIFIED "
                        f"in-line. EF parking (FLAG-002) restructured into typed "
                        f"field_relations; Related-Terms entries with no Desert chunk "
                        f"(Xeniteia, Kellion, Apatheia, Theōria, Nēpsis, Penthos, "
                        f"Synaxis, Antirrhēsis) are S2.9 Change-Order material, not "
                        f"records invented here.",
                        path)
        if coverage:
            fm, secs = parse_chunk(CHUNKS / f"{rid}_{path.stem}.md") if False else (None, None)
    if emit:
        print(f"updated {len(NEW)} term records with S2.3 authoring")
    if coverage:
        # re-run parity: chunk body vs post-S2.3 fields (EF -> joined edge notes)
        bad = 0
        for cpath in sorted(CHUNKS.glob("*.md")):
            rid = cpath.stem.split("_")[0]
            rpath = TERMS / f"{rid}.md"
            rec = yaml.safe_load(rpath.read_text(encoding="utf-8").split("\n---", 2)[0][3:])
            fm, secs = parse_chunk(cpath)
            fields = {
                "quick_meaning": rec["quick_meaning"],
                "world_meaning": rec["world_meaning"],
                "modern_hearing": rec.get("modern_hearing", ""),
                "distortion_risk": rec["distortion_risk"],
                "field_relations_notes": " ".join(
                    e.get("note", "") for e in rec.get("field_relations", [])),
            }
            for i, s in enumerate(rec.get("sources", [])):
                fields[f"sources[{i}]"] = s.get("author_gravity_note", "")
            chunk_body = "\n".join(secs[n] for n in
                                    ("Quick Meaning", "World Meaning", "Ecological Function",
                                     "Distortion Risk", "Key Sources"))
            r = check_coverage(chunk_body, fields, [])
            status = "PASS" if not r["missing"] and not r["duplicated"] else "FAIL"
            if status == "FAIL":
                bad += 1
            print(f"  {rid}: {r['covered']}/{r['total']} covered, "
                  f"missing={len(r['missing'])}, duplicated={len(r['duplicated'])} -> {status}")
            for m in r["missing"][:4]:
                print(f"      MISSING: {m[:120]}")
        sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
