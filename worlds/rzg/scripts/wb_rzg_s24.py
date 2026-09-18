"""B-4 (S2.4): Reformed Cities (rzg) story + figure + quote records.

WHAT THIS SCRIPT DOES. Converts this world's already-built, already-reviewed
Story Inventory (Doc_09_Story_Inventory.md) and its three deployment-facing
Story-Chunks (Story-Chunks/rzgstoryNNN_*.md, read in full this session) into
record-native `story` records under records/rzg/story/, per the live schema
and gate battery. Also authors `figure` records for every named person this
world's own build treats as load-bearing enough to need a name-bridge (the
three stories' own cast - Zwingli, Hegenwald, Faber, Calvin, Farel, Myconius -
plus Bullinger and Beza, both extensively cited across the term records and
Doc_01's own succession account), and `quote` records for a small, bounded
set of primary lines already independently re-verified, character-exact,
across multiple already-reviewed documents this session (never a fresh
citation this script invents).

Follows don's own precedent (wb_don_s24.py, read in full before this script
was written) exactly in shape, adapted for this world's own genuinely
smaller story roster (3 Tier-1 stories, 0 Tier 2/3/4, per Doc_09 SS3.1 -
this world's own confessional core actively refuses the hagiographic genre,
per Doc_07 SS2C/SS2H, and no Tier 2/3/4 material is built to fill an
absence that is itself evidence the refusal worked).

INPUTS, mapped to OUTPUTS, precisely:
  - Story-Chunks/rzgstory001/002/003_*.md (read in full this session) ->
    3 story records, each carrying that chunk's own Story Text, Formation
    Ecology Connection, Tier Justification, and Usage Guidance sections,
    converted onto text/tellable_as/narrative_tier_justification/
    modern_contrast.
  - The three stories' own named cast, plus Bullinger (Zwingli's own
    successor, Second Helvetic Confession's own author, four-decade
    pastorate per Doc_01) and Beza (Calvin's own successor, named in
    Doc_01/Doc_04's own T1 Confidence/Gravity Cross-Check discussion) ->
    8 figure records. DATES ARE STATED ONLY WHERE THIS SESSION'S OWN
    READING DIRECTLY GROUNDS THEM - Zwingli's death (11 October 1531,
    rzgstory003) and Bullinger's pastorate (1531-1575, Doc_01) are the
    only dates this script asserts; every other figure's own dates are
    left unstated rather than filled from unverified general knowledge,
    per this project's own no-guessing rule.
  - Already-verified quotations already carried, character-exact, across
    multiple already-reviewed documents this session -> 6 quote records
    (the Consensus Tigurinus's own 9th Head of Agreement; the Sixty-Seven
    Articles' own Art. XVIII and its own preface; Zwingli's own reported
    last words at Kappel; Calvin's own Institutes IV.3.8 elder definition;
    the Second Helvetic Confession's own predestination-comfort line).
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_ROOT = REPO_ROOT / "records" / "rzg"

WORLD_ID = "the-reformed-cities-zurich-and-geneva"
SCHEMA_VERSION = 2


def _yaml_dump(payload: dict) -> str:
    return yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=100, default_flow_style=False)


def _write(path: Path, payload: dict, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\n" + _yaml_dump(payload) + "---\n" + body.strip() + "\n", encoding="utf-8")


# --------------------------------------------------------------- stories ---
STORIES: list[dict] = [
    dict(
        slug="first-zurich-disputation",
        tellable_as=(
            "The city council of Zurich did not simply permit the argument that launched our own "
            "Reformation there. It summoned it. On 29 January 1523, six hundred people filled the "
            "Town Hall - priests and laymen from across the canton, and delegates from the bishop of "
            "Constance. Before it began, enemies of the new preaching mocked the whole gathering as a "
            "\"tinker's day,\" saying nothing but tinkers would attend. That mockery is why our own "
            "record of the day survives in such detail: a Zurich schoolmaster named Erhart Hegenwald "
            "sat through the whole disputation and afterward wrote an account specifically to answer "
            "the sneer. \"I was there myself and sat with them,\" he wrote, \"heard and understood and "
            "remembered all that was said there.\" The council did not merely watch. When the "
            "arguments were finished, it found for our own side, and ordered every priest in the "
            "canton to preach the same way. An argument some had already dismissed in advance became "
            "an official act of civic reform."
        ),
        modern_contrast=(
            "A modern reader may picture a staged event, decided before it began - the way we now "
            "assume councils rarely reverse the powerful. We know it differently: the whole point of "
            "Hegenwald's own account is to answer people who mocked the gathering in advance as certain "
            "to fail, and our own council's judgment, reached that day, bound every priest in its "
            "territory from then on."
        ),
        narrative_tier=1,
        narrative_tier_justification=(
            "Direct textual attestation: a named author (Hegenwald) with an identifiable social "
            "location (a Zurich schoolmaster, stating his own eyewitness method), datable with "
            "reasonable confidence, and a historically credible narrative claim. This vendored volume "
            "carries a disclosed internal date inconsistency (29 January stated twice, 23 January "
            "once, in the editor's own prose only) - this record follows the two-source majority and "
            "standard historiography (29 January 1523), naming rather than silently resolving the "
            "inconsistency. A further disclosed complication: lines 1558-1567 of the vendored file are "
            "a page-layout interleaving of Hegenwald's own primary letter into the editor's "
            "introduction; this record's own load-bearing details (the six hundred figure, Faber's "
            "identity, the council's ratification) are independently corroborated in Hegenwald's own "
            "primary preface and mandate, not drawn from the interleaved fragment alone."
        ),
        body=(
            "Built from Story-Chunks/rzgstory001_first-zurich-disputation.md (Approved to proceed, Doc_09 "
            "Round 2). AUTHORED: tellable_as compresses the chunk's own longer Story Text into a single "
            "spoken-register passage in this world's own first-person register; modern_contrast draws on "
            "the chunk's own Usage Guidance and Doc_04's own Disputation-adjacent Distortion Risk framing."
        ),
    ),
    dict(
        slug="calvins-journey-to-zurich",
        tellable_as=(
            "By 1549, a quiet worry had spread among people who respected both our own churches: did "
            "Calvin's own teaching on the Supper actually agree with what Zurich taught? Calvin heard "
            "the worry directly, from people who revered both churches and did not want an appearance "
            "of disagreement to slow their own faith. A letter would not settle it. He went himself, "
            "and asked his own colleague William Farel - \"indefatigable soldier of Christ,\" he called "
            "him - to come too. Farel needed no persuading; he had suggested the visit himself. What "
            "the two of them worked out with Zurich's own pastors became the Consensus Tigurinus. "
            "Calvin's own letter afterward is careful about what it actually is: not a new invention, "
            "but a faithful record of the conference - and not his and Farel's own private business, "
            "but binding on every colleague serving Christ under Geneva's own jurisdiction as well."
        ),
        modern_contrast=(
            "A modern reader might expect two theologians to settle a doctrinal question by letter, or "
            "through delegates. Calvin's own account states plainly that he judged the matter too "
            "important for that: he made the journey himself, in person, with a colleague at his side."
        ),
        narrative_tier=1,
        narrative_tier_justification=(
            "Direct, first-person textual attestation from a named author (Calvin) about his own "
            "actions, addressed to a named audience (the pastors and doctors of the Church of Zurich), "
            "datable to 1549. The one caveat this tier's own definition names for authorial perspective "
            "applies narrowly: Calvin's own characterization of Farel's enthusiasm and the conference's "
            "own friendly tone are his own words about his own colleague and conduct, not an "
            "independently corroborated outside report - the bare facts of the journey and its outcome "
            "are not themselves in question."
        ),
        body=(
            "Built from Story-Chunks/rzgstory002_calvins-journey-to-zurich.md (Approved to proceed, "
            "Doc_09 Round 2). AUTHORED: tellable_as compresses the chunk's own Story Text; "
            "modern_contrast draws on the chunk's own Formation Ecology Connection (a specific human "
            "journey behind an abstract doctrinal convergence)."
        ),
    ),
    dict(
        slug="myconius-account-of-zwinglis-death",
        tellable_as=(
            "Zwingli left Zurich for the front early on 11 October 1531, and was killed that same "
            "afternoon. His close friend Oswald Myconius was in the city that day and later wrote down "
            "what he remembered - warnings that, looking back, seemed to have foretold it; a "
            "disorganized muster, fewer than four thousand five hundred where five thousand had been "
            "summoned; a sudden pain of heart Myconius felt as he watched Zwingli ride out in the rear. "
            "That night the news came back: the fight was sharp and lost, and Zwingli was dead, struck "
            "down three times and rising each time before a fourth blow brought him to his knees. He "
            "was reported to have said, as he fell, \"What evil is there in this? They are able, it is "
            "true, to kill the body but not the soul.\" His body was found by the victors afterward, "
            "given a mock trial, and burned. When his friends searched the field, they found - "
            "Myconius records this as something reported to him, not seen - that his heart had come "
            "through the fire whole and unburned."
        ),
        modern_contrast=(
            "A modern reader may expect a founder's death to be told as pure tragedy, without the "
            "hedges Myconius himself preserves. We keep them because he did: the battlefield details "
            "are secondhand, reported to him, and the heart found whole in the ashes is presented in "
            "his own account as something strange he was told, not something he saw."
        ),
        narrative_tier=1,
        narrative_tier_justification=(
            "Direct textual attestation from a named author (Oswald Myconius) with an identifiable "
            "social location (Zwingli's own close friend, a Reformed pastor in his own right), datable "
            "to the events of 11 October 1531 and written near them. Two disclosed caveats: Myconius "
            "was in Zurich, not on the battlefield, and his own account of the fighting is explicitly "
            "secondhand; the heart-found-whole detail is presented in his own text as reported to him, "
            "not personally observed, and this record preserves that same hedge rather than upgrading "
            "it to unqualified fact. A page-break in the vendored text splits the quotation of Zwingli's "
            "own last words across a running header (\"Zwingli's Death 23\") - the quoted words "
            "themselves are continuous and unaffected."
        ),
        body=(
            "Built from Story-Chunks/rzgstory003_myconius-account-of-zwinglis-death.md (Approved to "
            "proceed, Doc_09 Round 2 - this chunk was itself added at Round 1 review, correcting a "
            "false claim that no vendored source narrated Zwingli's own death). AUTHORED: tellable_as "
            "compresses the chunk's own Story Text; modern_contrast draws on the chunk's own Tier "
            "Justification hedges."
        ),
    ),
]

# --------------------------------------------------------------- figures ---
FIGURES: list[dict] = [
    dict(slug="zwingli", names=[("Huldrych Zwingli", "in-world"), ("Ulrich Zwingli", "scholarly")],
         dates={"died": 1531},
         bridge_line="Our own founder at Zurich, who first preached straight through Matthew rather than follow the fixed calendar of readings.",
         narratable=True),
    dict(slug="bullinger", names=[("Heinrich Bullinger", "in-world")],
         dates={"floruit": "pastorate at Zurich, 1531-1575"},
         bridge_line="Zwingli's own successor at Zurich, whose four-decade pastorate gave our confession its own mature, lasting form.",
         narratable=True),
    dict(slug="calvin", names=[("John Calvin", "in-world"), ("Jean Calvin", "scholarly")], dates={},
         bridge_line="Geneva's own pastor, whose Institutes and Catechism built our doctrine up book by book.",
         narratable=True),
    dict(slug="farel", names=[("William Farel", "in-world")], dates={},
         bridge_line="Calvin's own colleague, who first brought him to Geneva's own ministry and later traveled with him to Zurich to frame the Consensus.",
         narratable=True),
    dict(slug="myconius", names=[("Oswald Myconius", "in-world")], dates={},
         bridge_line="Zwingli's own close friend, who wrote down what he remembered of our founder's own death.",
         narratable=True),
    dict(slug="hegenwald", names=[("Erhart Hegenwald", "in-world")], dates={},
         bridge_line="A Zurich schoolmaster who sat through our own First Disputation and wrote it down to answer those who mocked it in advance.",
         narratable=True),
    dict(slug="faber", names=[("John Faber", "in-world")], dates={},
         bridge_line="The bishop of Constance's own Vicar General, sent as the ablest man to argue the old church's own side at our First Disputation.",
         narratable=False),
    dict(slug="beza", names=[("Theodore Beza", "in-world")], dates={},
         bridge_line="Calvin's own successor at Geneva, who carried our own doctrine of election into its fullest systematic form.",
         narratable=False),
]

# ----------------------------------------------------------------- quotes ---
QUOTES: list[dict] = [
    dict(
        slug="signs-and-things-signified",
        text="Wherefore, though we distinguish, as we ought, between the signs and the things signified, "
             "yet we do not disjoin the reality from the signs.",
        speaker_or_author="the Ministers of the Church of Zurich and John Calvin, Minister of the Church of Geneva",
        modern_rendering="We tell the sign apart from what it points to. But we never pull them apart.",
        source_slug="consensus-tigurinus", locus="9th Head of Agreement, lines 768-770",
        modern_lens_note=(
            "A modern reader may hear careful, almost legal hedging. We hear the specific, hard-won "
            "language both our cities judged they could actually mean, not merely sign."
        ),
    ),
    dict(
        slug="mass-not-a-sacrifice",
        text="That Christ, having sacrificed himself once, is to eternity a certain and valid sacrifice "
             "for the sins of all faithful, wherefrom it follows that the mass is not a sacrifice, but "
             "is a remembrance of the sacrifice and assurance of the salvation which Christ has given us.",
        speaker_or_author="Huldrych Zwingli",
        modern_rendering="Christ offered himself once, for good. So the Mass does not repeat that offering. It remembers it.",
        source_slug="zwingli-sixty-seven-articles", locus="Article XVIII, lines 4565-4569",
        modern_lens_note=(
            "A modern reader may hear a minor liturgical technicality. We hear the single sharpest "
            "doctrine separating us from Rome - what kind of sacrifice Christ's own death actually was."
        ),
    ),
    dict(
        slug="taught-better-from-scripture",
        text="The articles and opinions below, I, Ulrich Zwingli, confess to have preached in the worthy "
             "city of Zurich as based upon the Scriptures which are called inspired by God... and where "
             "I have not now correctly understood said Scriptures I shall allow myself to be taught "
             "better, but only from said Scriptures.",
        speaker_or_author="Huldrych Zwingli",
        modern_rendering="Everything I have preached rests on Scripture. If I have misread it, correct me - but only from Scripture itself.",
        source_slug="zwingli-sixty-seven-articles", locus="preface, lines 4487-4492",
        modern_lens_note=(
            "A modern reader may hear false modesty ahead of a debate already decided. We hear our own "
            "founder's own opening confession, before six hundred witnesses, staking everything on the "
            "text alone."
        ),
    ),
    dict(
        slug="zwinglis-last-words",
        text="What evil is there in this? They are able, it is true, to kill the body but not the soul.",
        speaker_or_author="Huldrych Zwingli, as reported by Oswald Myconius",
        modern_rendering="What is so terrible about this? They can kill my body. They cannot kill my soul.",
        source_slug="zwingli-latin-works-vol1",
        locus="Myconius, 'Original Life of Zwingli' SS12, lines approx. 1592-1593",
        modern_lens_note=(
            "This is reported speech, preserved by a close friend not present at the exact moment, not "
            "an independently witnessed direct quotation - we hold it the same way Myconius himself did."
        ),
    ),
    dict(
        slug="seniors-selected-from-the-people",
        text="seniors selected from the people to unite with the bishops in pronouncing censures and "
             "exercising discipline",
        speaker_or_author="John Calvin",
        modern_rendering="Ordinary people, chosen from among us, join the pastors in judging conduct.",
        source_slug="calvin-institutes-book4", locus="IV.3.8, lines 2831-2832",
        modern_lens_note=(
            "A modern reader may assume church discipline was always a clergy-only affair. Our own "
            "founder's own words say otherwise: laypeople hold real standing in it."
        ),
    ),
    dict(
        slug="christ-the-mirror-of-election",
        text="We reject those who seek out of Christ whether they are chosen... Let... Christ be the "
             "mirror in which we behold [our] predestination.",
        speaker_or_author="Heinrich Bullinger",
        modern_rendering="Do not search for proof of your own election apart from Christ. Look at Christ, and see your own election reflected there.",
        source_slug="second-helvetic-confession", locus="ch. X, lines 667, 684-685",
        modern_lens_note=(
            "A modern reader may hear predestination as an invitation to anxious self-examination. Our "
            "own confession points the anxious soul away from themselves, toward Christ."
        ),
    ),
]


def emit_story(s: dict) -> Path:
    rid = f"rzg.story.{s['slug']}"
    payload = {
        "id": rid, "world_id": WORLD_ID, "record_type": "story", "schema_version": SCHEMA_VERSION,
        "status": "draft", "register": "emic", "canon_cells": [],
        "confidence": {
            "citation_specificity": "A", "verification_state": "verified-direct",
            "evidentiary_weight": "corroborating", "formation_confidence": "Documented",
            "divergence_note": None,
        },
        "sources": STORY_SOURCES[s["slug"]],
        "retrieval": {"tier": 1, "retrieve_when": STORY_RETRIEVE[s["slug"]][0],
                      "do_not_retrieve_when": STORY_RETRIEVE[s["slug"]][1]},
        "relations": STORY_RELATIONS[s["slug"]],
        "narrative_tier": s["narrative_tier"],
        "narrative_tier_justification": s["narrative_tier_justification"],
        "tellable_as": s["tellable_as"],
        "text": s["tellable_as"],
        "modern_contrast": s["modern_contrast"],
    }
    path = OUT_ROOT / "story" / f"{rid}.md"
    _write(path, payload, s["body"])
    return path


def emit_figure(f: dict) -> Path:
    rid = f"rzg.figure.{f['slug']}"
    payload = {
        "id": rid, "world_id": WORLD_ID, "record_type": "figure", "schema_version": SCHEMA_VERSION,
        "status": "draft", "register": "emic", "canon_cells": [],
        "confidence": {
            "citation_specificity": "B", "verification_state": "verified-via-authority",
            "evidentiary_weight": "corroborating", "formation_confidence": "Documented",
            "divergence_note": (
                "This figure's own bridge_line is drawn from already-reviewed construction documents "
                "(Doc_01, the story cast, term Key Sources), not from a fresh primary-source read this "
                "pass - verified-via-authority, not verified-direct, matching this world's own honest "
                "distinction elsewhere between a general doctrine directly checked and a fact carried "
                "forward from an already-cleared document."
            ),
        },
        "sources": [], "relations": [],
        "names": [{"name": n, "tag": tag} for n, tag in f["names"]],
        "dates": f["dates"],
        "narratable": f["narratable"],
        "bridge_line": f["bridge_line"],
    }
    path = OUT_ROOT / "figure" / f"{rid}.md"
    body = (
        f"Built from this world's own already-reviewed construction documents (Doc_01, Doc_09's own "
        f"story cast, Doc_06's own Key Sources). `dates` states only what this compilation pass "
        f"directly verified this session ({f['dates'] or 'nothing dated beyond general attestation'}) - "
        f"never filled from general knowledge the vendored record itself does not supply here."
    )
    _write(path, payload, body)
    return path


def emit_quote(q: dict) -> Path:
    rid = f"rzg.quote.{q['slug']}"
    payload = {
        "id": rid, "world_id": WORLD_ID, "record_type": "quote", "schema_version": SCHEMA_VERSION,
        "status": "draft", "register": "emic", "canon_cells": [],
        "confidence": {
            "citation_specificity": "A", "verification_state": "verified-direct",
            "evidentiary_weight": "load-bearing", "formation_confidence": "Documented",
            "divergence_note": None,
        },
        "sources": [{"source_id": f"rzg.source.{q['source_slug']}", "locus": q["locus"], "license": "public-domain"}],
        "relations": [],
        "text": q["text"],
        "speaker_or_author": q["speaker_or_author"],
        "license": "verbatim",
        "modern_lens_note": q["modern_lens_note"],
        "modern_rendering": q["modern_rendering"],
    }
    path = OUT_ROOT / "quote" / f"{rid}.md"
    body = (
        "Independently re-verified, character-exact, against the vendored file this session, matching "
        "the already-established locus this world's own reviewed documents already cite for this exact "
        "quotation - not a fresh citation this script invents."
    )
    _write(path, payload, body)
    return path


STORY_SOURCES = {
    "first-zurich-disputation": [
        {"source_id": "rzg.source.zwingli-selected-works", "locus": "lines 1513-1654, 1665-1678", "license": "public-domain"},
    ],
    "calvins-journey-to-zurich": [
        {"source_id": "rzg.source.consensus-tigurinus", "locus": "Calvin's prefatory letter, lines 84-146", "license": "public-domain"},
    ],
    "myconius-account-of-zwinglis-death": [
        {"source_id": "rzg.source.zwingli-latin-works-vol1", "locus": "Myconius, 'Original Life of Zwingli' SS12, lines 1550-1613", "license": "public-domain"},
    ],
}

STORY_RELATIONS = {
    "first-zurich-disputation": [
        {"type": "illustrates", "target": "rzg.term.disputation"},
        {"type": "illustrates", "target": "rzg.term.sola-scriptura"},
    ],
    "calvins-journey-to-zurich": [
        {"type": "illustrates", "target": "rzg.term.the-lords-supper-spiritual-presence"},
        {"type": "illustrates", "target": "rzg.term.mutual-consent"},
    ],
    "myconius-account-of-zwinglis-death": [],
}

STORY_RETRIEVE = {
    "first-zurich-disputation": (
        ["participant asks how the Reformation actually began at Zurich, with named people and a specific event",
         "participant asks what a Reformation-era public disputation was actually like"],
        ["participant wants the Sixty-Seven Articles' own doctrinal content itself"]),
    "calvins-journey-to-zurich": (
        ["participant asks how the Zurich/Geneva doctrinal bridge actually came about",
         "participant asks about Farel's own role in this world"],
        ["participant wants the Consensus's own actual doctrinal content"]),
    "myconius-account-of-zwinglis-death": (
        ["participant asks how Zwingli actually died",
         "participant asks what it was like in Zurich on the day of the Second Battle of Kappel"],
        ["participant wants the doctrinal content of what Zwingli taught"]),
}


def main() -> int:
    written = []
    for s in STORIES:
        written.append(emit_story(s))
    for f in FIGURES:
        written.append(emit_figure(f))
    for q in QUOTES:
        written.append(emit_quote(q))

    assert len(STORIES) == 3
    assert len(FIGURES) == 8
    assert len(QUOTES) == 6

    for p in written:
        print(p.relative_to(REPO_ROOT))
    print(f"\n{len(written)} records written ({len(STORIES)} story + {len(FIGURES)} figure + "
          f"{len(QUOTES)} quote).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
