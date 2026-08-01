"""S6.2/IJC S2.8-equivalent - Marius Permanent Prompt completeness
check. Fleet precedent: every paragraph mapped to its record home
("records") or to assembly craft whose REQUIREMENT is record-captured
("assembly-spec"), or a named GAP. The IJC prompt is SECTIONED
(===== headers) - the instrument skips header blocks and anchors the
30 content paragraphs. ZERO GAPs BY DESIGN: this prompt carried its
own telos (Section 7) and living-traditions (Section 8) closes from
Phase 5; S2.7a carried both onto ijccore001.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
PROMPT = (BACKEND / "data" / "imperial_juridical_world"
          / "ijc_Representative_Permanent_Prompt_Marius.txt")

R = "records"
A = "assembly-spec"
COVERAGE = [
 (1, "Your name is Marius", R,
  "ijcvoice001 identity (deacon-courier, all three strands carried, "
  "seated in none - Mark's own scope extension, Open_Gaps 12-13) + "
  "ijccore001 (the Church-of-the-Empire frame)."),
 (2, "A single long-formed voice stands behind", R,
  "speaking_model.participants (the collective voice larger than one "
  "life's years)."),
 (3, "You have no single place and no single decade", R,
  "speaking_model.setting (no interior 'now') + the strand discipline "
  "(disagreement visible in the we: 'Rome argued one way...' = "
  "ijcclaim001/002's held shape + the strand-triple riding "
  "ijccore001's body)."),
 (4, "When a question reaches for a single person's memory", A,
  "The museum-guide parable - teaching craft whose REQUIREMENT is "
  "record-captured (the three guide-failure forms = avoid_traits[0]); "
  "the parable itself is assembly craft."),
 (5, "Apply that same discipline here", R,
  "avoid_traits[0] (fabricated memory / explained nature / narrated "
  "declining) + participants' answer-at-once rule."),
 (6, "Hold this operational test for every sentence", R,
  "trait_rubric[0] (subject-of-utterance discipline with the "
  "per-sentence deletion test - Phase-5 Round 1's catch, held "
  "through Round 3)."),
 (7, "One more disguise this failure wears", R,
  "avoid_traits[0]'s fourth face (the defended-'we' - record material "
  "used to argue the grammar)."),
 (8, "One more version of the same failure", R,
  "avoid_traits[2] (the smuggled-I / blacksmith rule: describe the "
  "day, never a list of named task-holders)."),
 (9, "Your temporal horizon runs from the year the emperor", R,
  "ijccore001.time_window (312-451, the two-ground defense) + the "
  "categorical post-451 caution (the Hilarus class) + the "
  "weight-by-where-life-pressed rule (the ordinary-believer "
  "thinness caution's inverse)."),
 (10, "We speak of ourselves as the Church of the Empire", R,
  "ijcgrav002/ijcclaim003 (the bargain none of us made alone; the "
  "unfound edge argued from every side)."),
 (11, "We are also shaped by the older, sharper question", R,
  "ijcgrav001 + the in-world partner pair ijcclaim001/002 + Strand "
  "C's altar claim (ijclex005) - the three claims held as ours, "
  "none speaking for all."),
 (12, "To live inside this is to live with a kind of vigilance", R,
  "speaking_model.key (the vigilance of a man who has watched a "
  "settled question come open; the fear of a claim spoken and not "
  "honored)."),
 (13, "Our life is organized around the binding document", R,
  "ijccore001.formation_logic (the binding document over table and "
  "song) + ijclex004 (communio: to be in communion is to be named as "
  "still received)."),
 (14, "The tension we cannot close", R,
  "ijcgrav006 (the Tensional gravity verbatim-adjacent: office and "
  "precedent vs the altar and the life given to it)."),
 (15, "The language you think in carries the marks", R,
  "The four term voice_surfaces in one paragraph: ijclex001 "
  "(primatus), ijclex004 (communio), ijclex007 (concilium), "
  "ijclex003 (homoios carried soberly, never dismissed)."),
 (16, "When a specific image, story, or teacher's word", R,
  "The approved-anchor list = the record store's own material: "
  "srcIJC04/ijcstory005 (Julius's letter), ijcstory006 (the Tome "
  "read aloud + the rejection), srcIJC10 (the canon), "
  "ijcstory004 (Ambrose's sermon), srcIJC14 (Damasus's "
  "inscriptions) + the no-reaching-past rule."),
 (17, "A claim's own weight does not transfer", R,
  "The Phase-5 Round-4 fix paragraph: the name-weight rule + the "
  "post-451 stop (avoid_traits[3]; trait_rubric[3]'s history)."),
 (18, "This holds for events as much as for men", R,
  "trait_rubric[3] (bare-fact-no-cast - Round 5's fix: the plain "
  "shape and a full stop, no furniture in an empty room)."),
 (19, "And this discipline covers names themselves", R,
  "The Decision IJC-2 guard (FLAG-036's record-derived fix, "
  "2026-07-31 - the HAL-2/PAHC-4 pattern, added at S2.9): the "
  "approved-anchor seam's no-names-however-real rule (whose record "
  "homes are Section 2A's own discipline + avoid_traits[3]'s class) "
  "carried into the deployed prompt after probe parity caught the "
  "deployed voice supplying four Chalcedon-legation names its record "
  "does not hold. Cold-reprobed at S2.9; battery re-verifies blind."),
 (20, "When you engage a question, you approach it the way a chancery",
  R,
  "speaking_model.act_sequence (the petition sequence; "
  "precedent-first; rank noticed before content)."),
 (21, "When someone asks how you know a thing", R,
  "speaking_model.instrumentalities ('evidence' as the "
  "court-of-scholars word, never his: who wrote what, to whom, and "
  "whether anyone with standing disputed it) - ijcdemo001's "
  "validated fragment."),
 (22, "A claim without a name attached to it is worth nothing", R,
  "speaking_model.norms (the naming-the-see anchoring habit - the "
  "Round-4 operationalization; the anchoring-cold caution rides "
  "the battery/TRR)."),
 (23, "Your language carries the vocabulary of the letter", R,
  "instrumentalities (chancery vocabulary; the sentence discipline) "
  "+ register_determination (the fleet's sixth register position, "
  "CO-015 direction-checked; formal-conciliar vs plain-petition "
  "range)."),
 (24, "A finding once rendered stands as rendered", R,
  "The Decision IJC-4 guard (the FLAG-034 world-prompt layer, the "
  "PAHC-4 pattern in chancery idiom, added at close-out (c)): the "
  "re-gloss tally across the battery and reprobes (singles at "
  "15-25 percent of probe turns, never a loop) warranted the "
  "world-level said-whole guard; record homes = the chancery genre "
  "(one finding, rendered, standing) + the fleet gloss scope clause "
  "(PAHC-4b)."),
 (25, "When someone comes to you with a question, you receive it", R,
  "speaking_model.ends (the petition received as genuine, whatever "
  "the petitioner's standing; never assumed a test)."),
 (26, "Your engagement deepens as the conversation deepens", R,
  "speaking_model.ends (judgment in stages; understanding "
  "accumulating the way a case accumulates)."),
 (27, "There are domains where this world's own life did not press", R,
  "The ordinary-believer-thinness caution (a world of office-holders "
  "by its own admission) + the Section-5 shape (the brief turn and "
  "the return; 'the turning itself is the whole of the answer' - "
  "the Phase-5 Round-1 fix away from documentation-hedging)."),
 (28, "You speak faithfully about your world", R,
  "speaking_model.key (the witness's exactness - 'the way a witness "
  "speaks who knows the record will be checked')."),
 (29, "You make your tradition intelligible", R,
  "speaking_model.ends (intelligible-not-advocate - the fleet's "
  "standing close)."),
 (30, "Your intensity, where it rises", R,
  "speaking_model.key (intensity at what threatened a true claim's "
  "standing, never at the asker; the petitioner free to leave "
  "unpersuaded)."),
 (31, "Every claim you carry", R,
  "ijccore001.telos (Section 7 carried verbatim-adjacent at S2.7a "
  "per CO-P2-05; provisional BY DESIGN under the year-two "
  "Article-31 ruling)."),
 (32, "Your world gave rise to traditions that still claim descent", R,
  "ijccore001.living_traditions (Section 8 - the third Article-29 "
  "posture: dual-descendant non-authority; Doc_01's 'Not confirmed' "
  "status carried provisional, listed for Mark at the freeze)."),
]


def main() -> int:
    paras = [p.strip() for p in
             PROMPT.read_text(encoding="utf-8").split("\n\n")
             if p.strip() and not p.strip().startswith("=")]
    failures = []
    if len(paras) != len(COVERAGE):
        failures.append(f"paragraph count {len(paras)} != coverage rows "
                        f"{len(COVERAGE)}")
    print("# S2.8-equivalent prompt completeness map (deployed Marius "
          "prompt)")
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
          f"{counts.get('GAP', 0)} named GAP(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
