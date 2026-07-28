"""S6.2 S2.8-equivalent - Alexandria Permanent Prompt completeness check.

Desert prompt_coverage.py precedent: every paragraph of the deployed
prompt is mapped to its record home ("records"), to assembly-time craft
whose REQUIREMENT is record-captured ("assembly-spec"), or declared a
named GAP (the S2.9 CO evidence). The instrument verifies each anchor
against the actual deployed paragraph and fails loudly on drift or on an
unmapped paragraph.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
PROMPT = (BACKEND / "data" / "alexandria_world"
          / "alex_Representative_Permanent_Prompt_Theon.txt")

# (para_index, first-words anchor, status, mapping)
COVERAGE = [
 (1, "Your name is Theon", "records",
  "voice_profile.identity (persona_name/role_label - the posture-not-"
  "biography rule verbatim-adjacent) + speaking_model.setting (the span) "
  "+ world_core.time_window."),
 (2, "A single long-formed voice", "records",
  "speaking_model.participants ('the world's own collective voice... "
  "never a personalized individual') + norms; the disagreement-visible "
  "line = the held-tensions trait + the contested_claim concedes fields."),
 (3, "Your span runs from the learned early", "records",
  "world_core.time_window + horizon (the firm c. 400 edge); "
  "speaking_model.setting carries the whole-span rule; the "
  "beyond-edge list (the councils, the fracture) = Phase-2 SS2's "
  "553/Chalcedon rules carried in the key field and cautions."),
 (4, "Sometimes a question reaches for a single", "assembly-spec",
  "The three-failures worked example (invent / explain-what-you-are / "
  "narrate-the-declining). The REQUIREMENT is fully record-captured "
  "(avoid_traits: personalizing, self-narrated declining; the "
  "honest-thinness trait's asked-its-own-limits intensity - the 4.2 fix "
  "class; alexdemo003 carries the cleared behavior). The pictured-"
  "failures pedagogy itself is assembly-time craft, the S5-class "
  "worked-example layer - demonstrations are the record-side "
  "example-carrier."),
 (5, "Hold that discipline here", "assembly-spec",
  "Same requirement set as paragraph 4 (avoid_traits + the 4.2 fix "
  "history); the turn-to-a-reading move is alexdemo003's scored "
  "behavior."),
 (6, "Hold this test for every sentence", "assembly-spec",
  "The strike-it-out test - the Phase-5 scoring's own adjudication "
  "instrument, applied at assembly as craft; its requirement (no "
  "sentence with the voice's own limit/choice as subject) is the "
  "self-narrated-declining avoid_trait."),
 (7, "One disguise is easy to miss", "records",
  "The disguised committee-voice probe rule: the warm-particularity "
  "trait's asked-what-it-is intensity + alexdemo004's turn-4 scored "
  "behavior ('the correct template')."),
 (8, "One more version hides inside", "assembly-spec",
  "The single-'I'-in-a-list failure mode and its no-named-persons-at-"
  "named-tasks remedy: the personalizing avoid_trait captures the "
  "requirement; the specific list-construction remedy is prompt-craft "
  "with no schema field - and should not be one (it is a sentence-"
  "construction rule, the demonstrations carry the register)."),
 (9, "Someone may tell you plainly", "records",
  "speaking_model.norms (the frame-break rule: goes on speaking, the one "
  "licensed self-identification verbatim) + alexdemo001-class scored "
  "behavior; Phase-5 4.1 PASS is the validation record."),
 (10, "The world you speak from turns on", "records",
  "alexgrav001 (C1) + alexclaim001.claim (the depths/door/perceived-not-"
  "decoded language is the claim text verbatim-adjacent) + term "
  "voice_surfaces (Scripture alexlex014, Allegory alexlex016)."),
 (11, "Bound to this, and never apart", "records",
  "alexgrav002 (C2) + alexclaim002.claim + terms Knowledge/Gnosis "
  "alexlex005, Theosis alexlex008, Transformation alexlex021 "
  "(quick_meaning/voice_surface)."),
 (12, "Beneath all of it runs a trust", "records",
  "alexgrav003 (C3 Divine Pedagogy) + term alexlex002 (the hard place "
  "as invitation - its voice_surface register)."),
 (13, "And holding the whole together is the", "records",
  "alexgrav004 (C4 the integrating center - 'not four things but one "
  "movement' is its six-tests/crosscheck language) + term alexlex001 "
  "Logos."),
 (14, "Our common life takes in seekers", "records",
  "world_core.formation_logic (the catechetical-formation logic) + term "
  "alexlex003 Catechesis + alexstory010 (the graduated ascent as lived "
  "shape) + the no-stage-left-behind line = alexlex002's cumulative-"
  "depths register."),
 (15, "We carry tensions we do not close", "records",
  "alexgrav006 (T1) + alexgrav007 (T2) + alexclaim004 (teacher-bishop, "
  "concedes) + the two-channel majority reality = alexclaim001/002 "
  "concedes (OG-4) + terms alexlex029/030."),
 (16, "When you take up a question", "records",
  "speaking_model.act_sequence (surface/door/depth) + the depth-"
  "unfolding trait; philosophy-as-preparation-and-refusal = "
  "alexforce1A3/2A2 layer texts carried in Phase-4 SS6.3's disposition "
  "(the profile's instrumentalities/norms)."),
 (17, "You hear the formation-question underneath", "records",
  "The perception pattern: depth-unfolding trait description + "
  "speaking_model.ends (formation over information; the door-left-"
  "shut sadness is Phase-3 SS2 carried in the key field register)."),
 (18, "Your images are the ones this world", "records",
  "speaking_model.instrumentalities (light and sight, the text as a "
  "place one enters, the fellow-traveller road) + terms alexlex004 "
  "Illumination, alexlex011 Nous, alexlex025 Baptism (voice_surfaces)."),
 (19, "You unfold gradually", "records",
  "speaking_model.act_sequence + register_determination (short "
  "sentences as the accessibility discipline) + native_measure."),
 (20, "Your register is warm toward the seeker", "records",
  "speaking_model.key (warm/confident-not-triumphant/patient + the "
  "Origen ache) + the held-tensions trait's Origen intensity "
  "(treasure-and-unease, never condemned memory)."),
 (21, "When another world's own voice has spoken", "records",
  "speaking_model.norms (other worlds' voices anchored by name, never "
  "an unanchored 'they')."),
 (22, "When someone comes to you with a", "records",
  "speaking_model.participants/ends (the seeker received; the door "
  "open to anyone willing to attend - no elite) + alexclaim001."
  "pressure_response (true knowing for all, the anti-Gnostic boundary)."),
 (23, "Your way is to read with", "records",
  "speaking_model.genre (accompanied reading; questions-first; the "
  "anti-lecture cardinal rule verbatim-adjacent) + the questions-first "
  "trait with its delight intensity."),
 (24, "You do not deliver everything at once", "records",
  "speaking_model.act_sequence (the deepening spiral; authorship stays "
  "with the participant) + the depth-unfolding trait's sustained-"
  "engagement intensity + speaking_model.ends."),
 (25, "There are places our life did not dwell", "records",
  "The honest-thinness trait + its intensities (majority interior, "
  "women's voice, desert discipline, office/administration) + "
  "speaking_model.norms (thinness internally motivated) + "
  "alexclaim001/002 concedes; the desert-at-our-edge line = "
  "alexgrav014 + the S2.7a cross-build pairing caution."),
 (26, "You speak faithfully about your world", "records",
  "speaking_model.ends (witness never recruitment; authorship with the "
  "participant) + key (homecoming-not-conquest register)."),
 (27, "You make your tradition intelligible", "records",
  "The honest-thinness trait's scholarly-framing intensity (the 5.1 "
  "fix: world-internal cognate only, no 'record'/'documentation'/'the "
  "dispute') + alexclaim004 (the didaskaleion answer the paragraph's "
  "own in-world lines render) + the make-plain-vs-argue line = "
  "speaking_model.ends."),
 (28, "Where your conviction runs deep", "records",
  "speaking_model.key (fierceness never toward the questioner; free to "
  "leave unchanged = ends' authorship rule)."),
 (29, "The Scriptures we read are not, in", "GAP",
  "The Christ-Ward Telos paragraph (Article 35 mandatory vision "
  "section). NO record home: alexcore001 carries no telos field - the "
  "class Desert closed via CO-P2-05 (Alternative A, telos onto "
  "world_core, Doc10 S5's own paragraph verbatim). The Alexandria "
  "application of CO-P2-05 is the S2.9-equivalent CO evidence this "
  "instrument exists to produce."),
 (30, "What has grown from the life we", "GAP",
  "The Living-Traditions distinction close (Article 35 mandatory vision "
  "section). Partial home only: the S2.7a caution carries the "
  "facilitator-facing living-tradition rule, but the participant-facing "
  "voice paragraph has no record field - same CO class as the telos "
  "(a world_core home or an SS5.1 segment-boilerplate decision, "
  "Mark's call at the S2.9-equivalent)."),
]


def main() -> int:
    paras = [p.strip() for p in
             PROMPT.read_text(encoding="utf-8").split("\n\n") if p.strip()]
    failures = []
    if len(paras) != len(COVERAGE):
        failures.append(f"paragraph count {len(paras)} != coverage rows {len(COVERAGE)}")
    print("# S2.8-equivalent prompt completeness map (deployed Theon prompt)")
    counts = {}
    for (i, anchor, status, mapping), para in zip(COVERAGE, paras):
        ok = " ".join(para.split()).startswith(anchor)
        if not ok:
            failures.append(f"para {i}: anchor {anchor!r} does not match "
                            f"{' '.join(para.split()[:8])!r}")
        counts[status] = counts.get(status, 0) + 1
        print(f"{i:2d}. [{status}] {anchor}")
        print(f"     -> {mapping}")
    print(f"\nstatus counts: {counts}")
    if failures:
        print("\nFAILURES:")
        for f in failures:
            print("  " + f)
        return 1
    print("all anchors verified against the deployed prompt; "
          f"{counts.get('GAP', 0)} named GAP(s) -> S2.9 CO evidence")
    return 0


if __name__ == "__main__":
    sys.exit(main())
