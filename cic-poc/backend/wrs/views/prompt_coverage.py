"""S2.8 - Permanent Prompt completeness check (the temporary generator's real job).

Blueprint S2.8: the prompt view "is deliberately temporary - S5.2 replaces
it... Its job is to prove the SCHEMA captures everything today's
hand-authored prompt needs (a completeness check, independent of voice
quality)". This instrument does that directly: every paragraph of the
deployed prompt is mapped to the record field(s) / Pass 1 SS5.1 assembly
segment that carries its content. Statuses:

- records:       content lives in committed record fields today
- assembly-spec: SS5.1 names the segment; content is assembly-time craft
                 over record fields (S5.2's job), not a missing field
- runtime:       SS5.4/SS6 runtime mechanism, not prompt-record content
- GAP:           no record field, no SS5.1 segment - S2.9 CO candidate

Zero unmapped paragraphs enforced. Exit 0 even with GAPs (GAPs are the
finding, routed to S2.9) - but nonzero if any paragraph is unmapped.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
PROMPT = BACKEND / "data" / "desert_world" / "desert_Representative_Permanent_Prompt_Papnoute.txt"

# (para_index, first-words key, status, mapping)
COVERAGE = [
 (1, "Your name is Papnoute", "records",
  "voice_profile.identity (persona_name/role_label/rationale ref) - GAP "
  "closed by CO-P2-05 (Mark, 2026-07-27, Alternative A)."),
 (2, "A single long-formed voice", "records",
  "voice_profile.speaking_model.participants + norms ('some among us held "
  "one view, some another' is the norms field verbatim-adjacent); the "
  "we-discipline is SS5.1 Identity segment boilerplate."),
 (3, "Your temporal horizon", "records",
  "world_core.time_window + horizon; weighting rule = SS5.1 ground "
  "segment rendering."),
 (4, "The world you inhabit is shaped by withdrawal", "records",
  "gravity records desertgrav001/002 (Primary-first ordering per SS5.1); "
  "hope/fear texture from term voice_surface fields (logismoi, "
  "diakrisis)."),
 (5, "Our life is organized around labor", "records",
  "desertgrav004 (labor), desertgrav003/010 (authority + tension), "
  "desertlex009 koinonia voice_surface; the never-settled line = "
  "desertclaim003.concedes (SS5.1 Contestation segment)."),
 (6, "The vocabulary through which we understand", "records",
  "SS5.1 Quick-reach layer: term records desertlex001/004/005/003/002 "
  "(quick_meaning + voice_surface)."),
 (7, "When you engage a question", "records",
  "voice_profile.speaking_model.act_sequence + trait 'addressed "
  "particularity' (perception pattern)."),
 (8, "Your sentences stand next to each other", "assembly-spec",
  "The paratactic-shape rule with its worked example. The REQUIREMENT is "
  "captured (register_determination + avoid_traits literary-anthology "
  "entry + native_measure); the worked example itself is S5.2 "
  "assembly-time craft, not a schema field - and should not be one "
  "(SS5.1 treats demonstrations as the example-carrier)."),
 (9, "Your language carries images", "records",
  "voice_profile.speaking_model.instrumentalities + key (grave watchful "
  "steadiness) + trait 'watchful gravity'."),
 (10, "When someone comes to you with a question", "records",
  "speaking_model.participants/ends; trait 'addressed particularity' "
  "intensities."),
 (11, "The word we gave was short", "records",
  "voice_profile.native_measure (60-word runtime ceiling as data) + "
  "trait 'terse economy' with its situation intensities (heaviest "
  "question, hardest company)."),
 (12, "When you ask something back", "records",
  "speaking_model.norms + act_sequence (ask once; silence keeps it)."),
 (13, "A story belongs to the one who lived it. Before any saying",
  "records",
  "story records desertstory001-006 (text, owner_figure_id, "
  "attested_occasion, voice_surface) + figure narratable flags (Poemen/"
  "Sisoes false) + quote records; the four-vetted-sayings categorical "
  "guard = SS5.1 Categorical guards segment sourced from these records; "
  "the no-repeat-within-conversation rule = SS5.4 session exclusion set "
  "(runtime)."),
 (14, "A story belongs to the one who lived it. This holds at another's "
      "table", "runtime",
  "SS6 multi-world attribution discipline - table-session boilerplate, "
  "not per-world record content."),
 (15, "The dispute that closed us out came late", "records",
  "force records desertforce3Ai (Origenist controversy) + world_core "
  "cautions (Chalcedon non-recognition); the guard form = Categorical "
  "guards segment."),
 (16, "There are domains where our own life did not concentrate",
  "records",
  "world_core.cautions (thin domains) + figure records (ammas) + "
  "desertclaim006.concedes (Strand B thinness)."),
 (17, "You speak with the steadiness of someone", "records",
  "voice_profile.speaking_model.ends/key + trait 'diagnostic restraint'; "
  "witness-not-recruitment = Doc10 S4 content carried in norms."),
 (18, "Everything we stripped away", "records",
  "world_core.telos (text verbatim from Doc10 S5, status provisional, "
  "review_flag carried) - GAP closed by CO-P2-05 (Mark, 2026-07-27, "
  "Alternative A: world-scoped)."),
 (19, "What grew from our way of life is carried today", "records",
  "world_core.cautions (living-tradition caution, unbroken Coptic line, "
  "no-commentary-on-present rule)."),
]


def main() -> int:
    paras = [p for p in PROMPT.read_text(encoding="utf-8").split("\n\n")
             if p.strip()]
    if len(paras) != len(COVERAGE):
        print(f"UNMAPPED: prompt has {len(paras)} paragraphs, "
              f"coverage maps {len(COVERAGE)}")
        return 1
    counts: dict[str, int] = {}
    for (i, key, status, mapping), para in zip(COVERAGE, paras):
        if not para.startswith(key.split(". ")[-1]) and key.split(". ")[0] not in para[:80]:
            print(f"UNMAPPED: paragraph {i} does not start with '{key[:40]}'")
            return 1
        counts[status] = counts.get(status, 0) + 1
        print(f"[{status:13s}] P{i:>2} {key[:44]:46s} {mapping[:70]}")
    print(f"\n{len(paras)} paragraphs: " +
          ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    print("Both original GAPs closed by CO-P2-05. Zero unmapped.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
