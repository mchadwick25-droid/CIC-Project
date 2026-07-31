#!/usr/bin/env python
"""SH-11: precompute the answer bank (app/answer_bank.py) from the real
Guided-Questions curriculum.

NOT RUN as part of this build - needs a live ANTHROPIC_API_KEY and Mark's
go-ahead to spend real money, same discipline as B-COST's --run mode. Under
MOCK_LLM=true this script runs mechanically end-to-end and writes real files
in the real format, but every "answer" in them is mock_llm.py's placeholder
text - never let a mock-mode run's output reach cic-poc/backend/data/answer_bank/
for real; that flag is exactly why this script prints a loud warning banner
whenever settings.mock_llm is true (see main() below).

  python scripts/build_answer_bank.py --world desert-monasticism --role general
  python scripts/build_answer_bank.py --world desert-monasticism --role general --set general-ordinary-day
  python scripts/build_answer_bank.py --all   # every solo world x every role x every set

Solo (interview-mode) worlds only, per app/answer_bank.py's own scope - Table
mode's bank is the cost model's own "expensive one, ages fastest" and Table
is becoming a paid-tier feature (2026-07-31 Table-mode product-shape
decision) needing its own subscription-gating infrastructure this doesn't
touch.

Cost note: this calls representative_engages() directly per question - the
SAME live code path an ordinary turn takes (same retrieval, same prompt
assembly, same model), which is exactly the point: a precomputed answer
must be indistinguishable in quality from what a live turn would have
produced, or it isn't safe to serve to a future participant as if it were
one. That means this is a SYNCHRONOUS run at standard per-call pricing, not
the Batch API's 50% discount the cost model's build-cost estimate assumed
(Ministry/Technology/Pass3/cost_floor_model.py STEP 5) - Batch requires a
genuinely different call shape (submit + poll) that doesn't reuse
representative_engages() as directly. Left as a real, named follow-up
optimization rather than attempted half-built here; budget roughly 2x the
cost model's own build-cost figures for a first synchronous run.

Chain semantics: a whole SET (all its questions, in order) is precomputed
as one deterministic conversation, not each question independently - each
later question's generation call sees the full accumulated transcript of
the set's own prior (question, precomputed-answer) pairs, exactly mirroring
what a live undeviated walk looks like at that point (see the curriculum
doc: "each set is a walk... a natural next step from the last").
"""

import argparse
import json
import os
import sys
from pathlib import Path

os.environ.setdefault("MOCK_LLM", "true")
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

CURRICULUM_PATH = (
    Path(__file__).resolve().parent.parent.parent.parent
    / "Ministry" / "Features" / "Guided-Questions" / "Design"
    / "CiC_Guided_Questions_Curriculum_V1_0.json"
)

# The solo worlds SH-11 v1 covers - see app/answer_bank.py's module
# docstring. All six exist in app/world_manifest.py; this list is the
# explicit "which ones get a bank" decision, not derived automatically, so
# adding a world here is a deliberate act.
SOLO_WORLDS = [
    "post-apostolic-house-church",
    "syriac-edessa-nisibis",
    "desert-monasticism",
    "hieronymian-ascetic-literary",
    "alexandria-catechetical",
    "imperial-juridical-christianity",
]


def load_curriculum() -> dict:
    return json.loads(CURRICULUM_PATH.read_text(encoding="utf-8"))


def build_chain(world_id: str, role: dict, curriculum_set: dict) -> list[dict]:
    """Runs one (world, role, set) chain live, question by question, and
    returns the bank entries for every question in it. Each call sees the
    accumulated transcript of this same chain's own prior turns."""
    from langchain_core.messages import HumanMessage

    from app.config import settings
    from app.graph.nodes import representative_engages
    from app.graph.state import ConversationState, WorldContext
    from app.main import load_world_content

    permanent_prompt, world_capsule = load_world_content(world_id)
    state = ConversationState(
        session_id=f"answer-bank-build-{world_id}-{role['id']}-{curriculum_set['id']}",
        world_id=world_id,
        world_ids=[world_id],
        current_world_id=world_id,
        worlds_at_table=[WorldContext(
            world_id=world_id, permanent_prompt=permanent_prompt,
            world_capsule=world_capsule,
        )],
        permanent_prompt=permanent_prompt,
        world_capsule_core=world_capsule,
    )

    entries = []
    for q in sorted(curriculum_set["questions"], key=lambda x: x["order"]):
        state.messages = list(state.messages) + [HumanMessage(content=q["text"])]
        result = representative_engages(state)
        message = result["messages"][0]
        state.messages = list(state.messages) + [message]
        state.turn_count = result.get("turn_count", state.turn_count)

        entries.append({
            "role": role["id"],
            "set_id": curriculum_set["id"],
            "question_order": q["order"],
            "question_text": q["text"],
            "answer_text": message.content,
            "representative_name": message.name,
            "citations": message.additional_kwargs.get("citations") or [],
            "retrieval_audit": message.additional_kwargs.get("retrieval_audit"),
            "glosses_used": message.additional_kwargs.get("glosses_used") or [],
        })
        print(f"    [{'MOCK' if settings.mock_llm else 'LIVE'}] "
              f"{role['id']}/{curriculum_set['id']}#{q['order']} -> "
              f"{len(message.content)} chars")

    return entries


def merge_into_bank_file(world_id: str, new_entries: list[dict]) -> None:
    from app.config import settings

    path = settings.data_base_path / "answer_bank" / f"{world_id}.json"
    path.parent.mkdir(parents=True, exist_ok=True)

    existing = {"entries": []}
    if path.exists():
        existing = json.loads(path.read_text(encoding="utf-8"))

    by_key = {(e["role"], e["set_id"], e["question_order"]): e for e in existing["entries"]}
    for e in new_entries:
        by_key[(e["role"], e["set_id"], e["question_order"])] = e

    existing["entries"] = list(by_key.values())
    path.write_text(json.dumps(existing, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  wrote {len(new_entries)} entries -> {path} ({len(existing['entries'])} total)")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--world", help="a single world_id from SOLO_WORLDS")
    p.add_argument("--role", help="a single role id (general, pastor_teacher, academic_scholar, reevaluation)")
    p.add_argument("--set", dest="set_id", help="a single set id within --role")
    p.add_argument("--all", action="store_true", help="every solo world x every role x every set")
    args = p.parse_args()

    from app.config import settings

    if settings.mock_llm:
        print("=" * 76)
        print("MOCK_LLM=true - every 'answer' below is placeholder text, not a real")
        print("representative response. This is fine for testing this script's own")
        print("mechanics (file format, chain-threading, merge logic). It is NOT fine")
        print("to let output from a run like this reach cic-poc/backend/data/answer_bank/")
        print("for real - that would mean serving mock placeholder text to a real")
        print("participant as if a Representative said it. Set a real")
        print("ANTHROPIC_API_KEY and MOCK_LLM=false for an actual build.")
        print("=" * 76)

    curriculum = load_curriculum()
    worlds = SOLO_WORLDS if (args.all or not args.world) else [args.world]
    if args.world and args.world not in SOLO_WORLDS:
        raise SystemExit(f"{args.world} is not in SOLO_WORLDS - add it there deliberately first")

    for world_id in worlds:
        world_entries = []
        for role in curriculum["roles"]:
            if args.role and role["id"] != args.role:
                continue
            for curriculum_set in role["sets"]:
                if args.set_id and curriculum_set["id"] != args.set_id:
                    continue
                print(f"{world_id} / {role['id']} / {curriculum_set['id']}")
                world_entries.extend(build_chain(world_id, role, curriculum_set))
        if world_entries:
            merge_into_bank_file(world_id, world_entries)


if __name__ == "__main__":
    main()
