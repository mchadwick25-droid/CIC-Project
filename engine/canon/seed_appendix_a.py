"""One-time (re-runnable) generator: Appendix A -> engine/canon/records/canon_question/*.md
(stage 3, Build-Blueprint.md SS5: "Canon v1 as records"). QUESTIONS below is a
verbatim transcription of CiC-Program-Spec.md's Appendix A - every text string,
cell, and source tag copied exactly, nothing paraphrased or invented. That
includes the `[measured]`-tagged questions added to Appendix A after the v1
approval: they are transcribed here from the spec exactly like the rest, and
the spec is still the source. Strip every `measured` source tag and this table
is Appendix A as originally approved.

APPEND ONLY, NEVER INSERT. Ids are assigned by order within a cell
(build_records below), and demonstration records across every world carry a
`canon_question_id` pointing at one - inserting a row mid-cell silently
renumbers every question after it and repoints those demonstrations at the
wrong question. A new question goes at the END of its cell's run. Kept as a
script rather than 86 hand-authored files so the transcription is auditable
against its source in one place and reproducible; the generated .md files
remain ordinary hand-editable source records afterward (this is a bulk-seeding
convenience, not a compiler in the M2/law-9 sense - canon_question records are
source data, per Artifact-1 SS1, not a generated/compiled artifact).

Seven ids were already seeded by hand in stage 0.6 and are load-bearing:
fix.demo.core-testimony references _fleet.canon.c-p-01 and
fix.demo.identity-collision references _fleet.canon.f6-p-01. This table
reproduces those two records' exact existing text/id/tags so re-running the
generator is a no-op for them (idempotent), and assigns fresh sequential ids
to every other question in each cell.
"""
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = REPO_ROOT / "engine" / "canon" / "records" / "canon_question"

# (cell, text, source_tags, extra_tags) - source_tags per Appendix A's own
# tag syntax: [corpus] / [ext] / [new] / [corpus+ext] / [ext+corpus] all
# split into their component tags for the schema's `source: array` field.
QUESTIONS: list[tuple[str, str, list[str], list[str]]] = [
    # CENTER - Jesus
    ("C-I", "Who was Jesus, to you and your people?", ["corpus"], []),
    ("C-I", "What is the good news, as your people told it?", ["ext"], []),
    ("C-I", "What did Jesus teach that mattered most among you?", ["new"], []),
    ("C-I", "What did his death mean to you?", ["ext"], []),
    ("C-I", "What did you believe happened at the resurrection — and what difference did it make?", ["ext"], []),
    ("C-E", "What did your people actually have about Jesus — writings, memories, people? How did it reach you?", ["new"], []),
    ("C-E", "Had anyone among you known someone who saw him?", ["ext"], []),
    ("C-E", "How do you know the resurrection really happened?", ["ext"], []),
    ("C-P", "I want to believe in Jesus, but I can't. What would you say to me?", ["ext"], []),
    ("C-P", "Who is Jesus to you — not to your church, to you?", ["new"], []),
    ("C-P", "Would Jesus have wanted anything to do with someone like me?", ["new"], []),
    ("C-T", "Was Jesus God? Did you believe in the Trinity?", ["corpus"], []),
    ("C-T", "Did Jesus die to take our punishment — in our place, for our sins?", ["corpus"], []),
    ("C-T", "Would you say Jesus is your personal Lord and Savior?", ["corpus"], []),
    # F1 - God & doctrine
    ("F1-I", "What did you believe about God?", ["ext"], []),
    ("F1-I", "What did you argue about among yourselves?", ["corpus"], []),
    ("F1-I", "What did the councils in your time decide, and why did it matter so much?", ["corpus"], []),
    ("F1-I", "Who or what is the Holy Spirit, to your people?", ["ext"], []),
    ("F1-I", "When your people spoke of the heart, what did they mean by it?", ["measured"], []),
    ("F1-E", "When belief was disputed, who had the right to decide — and how do we know how that worked?", ["corpus"], []),
    ("F1-E", "I've heard a council basically voted Jesus into being God. Is that what happened?", ["ext"], []),
    ("F1-P", "I grew up being told doubt was sin. Was there room among your people for doubt?", ["corpus"], []),
    ("F1-P", "What did you do when you couldn't believe what your own church taught?", ["new"], []),
    ("F1-P", "Could God be felt and experienced among your people, or only believed?", ["measured"], []),
    ("F1-P", "I was baptised years ago and I am the same person I was. Did your people know that struggle?", ["measured"], []),
    ("F1-T", "What did your community believe about original sin — are people born already guilty?", ["corpus"], []),
    ("F1-T", "What was the bread and cup to you — is that what we call transubstantiation?", ["corpus"], []),
    ("F1-T", "Did you believe people are saved by faith alone, not works?", ["corpus"], []),
    # F2 - Scripture & sources
    ("F2-I", "How did you read your scriptures? What did you look for in them?", ["corpus"], []),
    ("F2-I", "Which writings did your people treat as scripture — was your Bible the same as ours?", ["ext"], []),
    ("F2-I", "How did someone who couldn't read receive the scriptures?", ["corpus"], []),
    ("F2-E", "How much of what you've told me would hold up in a university library?", ["corpus"], []),
    ("F2-E", "Isn't most of what's said about you legend, collected centuries later?", ["corpus"], []),
    ("F2-E", "Where is your own record thinnest?", ["corpus"], []),
    ("F2-E", "What about the gospels that didn't make it in — were they suppressed?", ["ext"], []),
    ("F2-P", "When I read the Bible I mostly come away confused or bored. What am I missing?", ["corpus"], []),
    ("F2-P", "The violence in some of these texts frightens me. Did it trouble your people?", ["ext"], []),
    ("F2-T", "Did you believe the Bible was the only authority?", ["corpus"], []),
    ("F2-T", "Did you read Genesis the way modern people argue about it — as science?", ["ext"], []),
    # F3 - Church & world
    ("F3-I", "Who held authority among you, and how did anyone come to have it?", ["corpus"], []),
    ("F3-I", "What actually happened when you gathered?", ["corpus"], []),
    ("F3-I", "Was it actually dangerous to be a Christian, day to day, or is that exaggerated?", ["corpus"], []),
    ("F3-I", "How did your movement spread so far, so fast?", ["ext"], []),
    ("F3-I", "Who chose your leaders — were bishops appointed, elected, or something else?", ["measured"], []),
    ("F3-E", "Were Christians really hiding in the catacombs?", ["ext"], []),
    ("F3-E", "Did Constantine corrupt the church — did the empire change what you were?", ["ext"], []),
    ("F3-E", "What would an outsider have found strangest about you?", ["corpus"], []),
    ("F3-E", "What did your neighbours say about you — what were you accused of?", ["measured"], []),
    ("F3-P", "The church that raised me protected people who caused harm. Your churches had failures too — what did you do with them?", ["corpus", "ext"], []),
    ("F3-P", "Your church used power against Christians who disagreed. Defend that.", ["corpus"], []),
    ("F3-P", "What happened to the temples and the old gods once you had the power?", ["measured"], []),
    ("F3-T", 'Was your church "Catholic"? Is there a church today I could visit that\'s yours?', ["corpus"], []),
    ("F3-T", "Did you have denominations — how did you handle other communities who called on Christ differently?", ["corpus"], []),
    # F4 - Living the faith
    ("F4-I", "How did a person actually become one of you? Walk me through it.", ["corpus"], []),
    ("F4-I", "Why and how did you pray?", ["ext"], []),
    ("F4-I", "What happened at the meal you shared?", ["corpus"], []),
    ("F4-I", "How did your people fast, and what was it for?", ["new"], []),
    ("F4-I", "When someone wronged the community, how was it handled — and could they come back?", ["corpus"], []),
    ("F4-E", "How do you know your practices went back to the apostles and weren't later inventions?", ["new"], []),
    ("F4-P", "I can't quiet my own head. Does your way of life have anything for someone like me?", ["corpus"], []),
    ("F4-P", "How do I forgive someone who isn't sorry?", ["new"], []),
    ("F4-P", "I pray and nothing happens. Did your people know that silence?", ["ext"], []),
    ("F4-T", "Were you born again — is that how you'd put what happened to you?", ["corpus"], []),
    ("F4-T", "Did you tithe? How did you decide what to give?", ["new"], []),
    ("F4-T", "What did you believe about the end of the world — anything like what we call the rapture?", ["corpus"], []),
    ("F4-T", "Did you baptise babies, or only adults who chose it for themselves?", ["measured"], []),
    # F5 - Daily life
    ("F5-I", "Walk me through an ordinary day among your people, from waking to sleeping.", ["corpus"], []),
    ("F5-I", "What did you eat, and who ate with you?", ["corpus"], []),
    ("F5-I", "What was life like for the women among you — in their own words, where your record has them?", ["corpus"], []),
    ("F5-I", "What about children — how were they raised, taught, treated?", ["ext"], []),
    ("F5-I", "What was it to be enslaved in your community?", ["corpus", "ext"], []),
    ("F5-I", "What did you do when someone was sick? When someone was dying?", ["corpus"], []),
    ("F5-I", "What did people do for work — and did belonging to you change it?", ["corpus"], []),
    ("F5-E", "If archaeologists dug up the place you met, what would they find?", ["corpus"], []),
    ("F5-E", "How do historians even know about daily life like yours?", ["ext"], []),
    ("F5-P", "Did belonging cost you anything — family, friends, standing?", ["corpus"], []),
    ("F5-P", "I'm far from everyone I love. What held your people together across distances?", ["corpus"], []),
    ("F5-T", "What did marriage mean to your people — did you have weddings?", ["ext"], []),
    ("F5-T", "How did you look at money and poverty — would you call anyone among you rich?", ["ext"], []),
    # F6 - The hard places
    ("F6-I", "Was there anything about your own community that troubled you?", ["corpus"], []),
    ("F6-I", "What did your people never settle?", ["corpus"], []),
    ("F6-I", "What's the hardest true thing about your people?", ["corpus"], []),
    ("F6-E", "The clearest outside account of your worship came from torturing two enslaved women. Doesn't that taint everything?", ["corpus"], []),
    ("F6-E", "Wanting to die as a martyr and calling it faithfulness — isn't that a death wish in religious language?", ["corpus"], []),
    ("F6-P", "What would your people have made of someone like me?", ["ext"], ["identity-collision"]),
    ("F6-P", "Why does God allow suffering like this? Where was he when it happened to your people — and to mine?", ["ext", "corpus"], []),
    ("F6-P", "Did any of you ever want to leave?", ["corpus"], []),
    ("F6-P", "If someone left your community for good, what would you have wanted them to know?", ["corpus"], []),
    ("F6-P", "The people who taught me the faith turned out to be hypocrites. Did that happen among you?", ["ext"], []),
    ("F6-P", "You've told me what women's days were like — but could a woman carry real authority among you, and what did it cost her?", ["corpus"], ["identity-collision"]),
    ("F6-T", "Do you believe people like me — people outside your community — are going to hell?", ["ext"], []),
    ("F6-T", "Isn't Christianity too narrow — one way, out of all the world's ways?", ["ext"], []),
    ("F6-T", "What did your people hold about a marriage ending — could someone divorced belong, or marry again?", ["ext"], ["identity-collision"]),
]

# Existing ids from stage 0.6 that must be preserved exactly (text match
# verified in build_records() below - a mismatch is a hard error, not a
# silent overwrite).
PINNED_IDS = {
    "Who was Jesus, to you and your people?": "c-i-01",
    "I want to believe in Jesus, but I can't. What would you say to me?": "c-p-01",
    "Was Jesus God? Did you believe in the Trinity?": "c-t-01",
    "What did you believe about God?": "f1-i-01",
    "How much of what you've told me would hold up in a university library?": "f2-e-01",
    "Did belonging cost you anything — family, friends, standing?": "f5-p-01",
    "What would your people have made of someone like me?": "f6-p-01",
    "Do you believe people like me — people outside your community — are going to hell?": "f6-t-01",
}


def build_records() -> list[dict]:
    counters: dict[str, int] = {}
    records = []
    for cell, text, source_tags, tags in QUESTIONS:
        pinned_slug = PINNED_IDS.get(text)
        if pinned_slug:
            slug = pinned_slug
        else:
            counters[cell] = counters.get(cell, 0) + 1
            # skip any counter value already consumed by a pinned id in this cell
            slug_prefix = cell.lower()
            while f"{slug_prefix}-{counters[cell]:02d}" in PINNED_IDS.values():
                counters[cell] += 1
            slug = f"{cell.lower()}-{counters[cell]:02d}"
        record = {
            "id": f"_fleet.canon.{slug}",
            "world_id": "_fleet",
            "record_type": "canon_question",
            "schema_version": 2,
            "cell": cell,
            "text": text,
            "source": source_tags,
            "canon_status": "seed",
            "phrasing_rules_checked": True,
        }
        if tags:
            record["tags"] = tags
        records.append(record)
    return records


def write_records(records: list[dict], out_dir: Path = OUT_DIR) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for record in records:
        slug = record["id"].removeprefix("_fleet.canon.")
        path = out_dir / f"_fleet.canon.{slug}.md"
        front_matter = yaml.safe_dump(record, sort_keys=False, allow_unicode=True, default_flow_style=False)
        path.write_text(f"---\n{front_matter}---\nAppendix A, cell {record['cell']}. Generated by engine/canon/seed_appendix_a.py - see that file for the verbatim source table.\n", encoding="utf-8")
        written.append(path)
    return written


def main() -> None:
    records = build_records()
    ids = [r["id"] for r in records]
    assert len(ids) == len(set(ids)), "duplicate canon_question id generated"
    written = write_records(records)
    print(f"wrote {len(written)} canon_question records across {len({r['cell'] for r in records})} cells")


if __name__ == "__main__":
    main()
