# Schema change order: an optional long telling on the story record

Named schema change order. `engine/m1/schemas.py` sets `additionalProperties: false`, so a story record cannot carry a new field until this order lands. It follows `Schema_Change_Order_Story_Fields.md` (short and medium tellings) and rests on Decision-Log 51 and 53.

Mark's words, 2026-11-01, relayed by the coordination thread: "on the card i would like the full long story in modern english that we can record (2 - 4 minutes)." Length: a target of 2 to 4 minutes, never padded; a thin story stays shorter (entry 53).

## What changes

One optional field on the `story` record type, beside `telling_short` and `telling_medium`:

| Field | Type | Meaning |
|---|---|---|
| `telling_long` | string | The long telling in modern English, faithful to the record and the source passage the record cites, shown on the story's card page and read aloud. Every event of `events` kept; nothing added. |

Existing records validate unchanged without it. The length rule for short and medium stays "the voice picks, code checks" (Settled row 18). The long telling is never placed in an answer.

## Word range

The approved audition pace for the recorded voice is about 134 to 147 words a minute (Front-End Decision Log, 2026-09-29). Mark chose a 1.15 times speed-up, which gives about 154 to 169. At those rates 2 minutes is 308 to 338 words and 4 minutes is 616 to 676, so a telling that runs 2 to 4 minutes at both rates is 340 to 615 words. The gate treats 615 as a ceiling with no tolerance and has no floor. The pace is the one the Front-End Decision Log set for the recorded house-church voice; lpc has no recorded voice of its own yet, and the range is revisited when it does.

## What goes with it

1. Spoken-field registry (`engine/m1/spoken_fields.py`): `telling_long` is an `evidence-head` field and appears in the attribution, perspective and participant field lists beside the other tellings, so the readability gate (B2) and the leak scans cover it. Like `telling_short` and `telling_medium`, being an `evidence-head` field also puts its words into the retrieval text, the absence rule's spoken text and the grounding net's text for a story: the long telling is the record's reviewed text, so a sentence that rests on it is grounded, and a record that carries one changes `compiled/retrieval.json` when it is added. It is still never placed in an answer: story placement lists its fields by hand and leaves it out.
2. Gates, folded into the existing `narratability` gate (`engine/m1/gates.py`), run only on a record that has the field: at most 615 words; every name and number also appears in the record (`text`, `telling`, `heart`, `events`) or in the vendored passage at the lines its sources cite, with the editor's notes and markup removed; a cited span that does not resolve to lines of a vendored text is itself a finding. That every event is kept, that nothing is added past the record and its cited passage, and that no absence is stated unprompted (Settled row 13) is confirmed by the second Opus review and Mark's reading, not by the gate.
3. Card data (`engine/m4/citation_cards.py`): a story card also carries `telling_long`. No display change in this order.

## What it does not do

- No record is written by this order. The seven lpc long tellings are written under their own authoring step: Opus writes in plan, a second Opus pass reviews against the full record and the cited passage, and Mark reads a sample.
- No recording and no paid step; both are a later, separate decision.
- No gate is retired and no other world is touched.

## Done when

The schema, the registry and the gate accept the field; a story without it validates unchanged; a long telling over 615 words is a finding and one under 340 is not; the card carries it. Tests cover each.
