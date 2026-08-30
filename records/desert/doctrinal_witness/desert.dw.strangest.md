---
id: desert.dw.strangest
world_id: desert-monasticism
record_type: doctrinal_witness
schema_version: 2
status: draft
register: emic
canon_cells: [F3-E]
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: corroborating
  formation_confidence: Widely Accepted
  divergence_note: "Widely Accepted, matching desert.gravity.withdrawal's own basis - this witness is a first-person framing of already-established material, not a new claim."
sources:
- source_id: desert.source.athanasius-vita-antonii
  locus: "SS2-3 - giving away a substantial inheritance over two separate church visits, not one; SS12-13 - years inside an abandoned fort with its entrance built up, seen by almost no one"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what an outsider would have found strangest about this world's own practice"
  - "participant asks what total renunciation and physical seclusion actually looked like"
  do_not_retrieve_when: []
relations:
- type: associated-with
  target: desert.quote.three-hundred-acres-to-the-villagers
- type: associated-with
  target: desert.story.antony-call
- type: associated-with
  target: desert.story.antony-withdrawal
text: >-
  An outsider, we think, would have found the giving away strangest of all.
  Not the praying. Not even the fasting. But that a young man with land and
  inheritance enough to live comfortably gave it all away, in two separate
  visits to the church, and never went back for it. And then the disappearing:
  years spent inside an old fort with its entrance walled up, seen by almost
  no one, while people gathered outside anyway, just to be near a wall with
  someone praying behind it. To most people that would look like throwing a
  life away. We understood it as the opposite. Once dying for the faith was no
  longer asked of anyone, it was the only way left to give the whole of a life
  rather than a part of it.
positions:
- "total renunciation of property, given away in two distinct steps rather than a single act"
- "years of near-total physical seclusion, sought rather than avoided"
- "renunciation and seclusion understood, from inside, as total offering rather than as loss"
tensions:
- "what looks from outside like loss reads, from inside, as gain - we do not soften the strangeness; we say plainly what the strangeness itself is evidence of"
---
First-person framing of desert.story.antony-call and desert.story.antony-
withdrawal, both already independently verified; no new claim beyond
what those two records already carry.

Step4, Round 1 review Finding C5: "behind a locked door" and "in a
single afternoon" overclaimed against SS2-3 (two separate church
visits, not one) and S12 ("he built up the entrance completely" - a
sealed entrance, not a locked door). Corrected above to match the
vendored text directly. Finding M9 (tensions field): "this world's own
account" replaced with first-person phrasing, matching the fix already
applied to the other affected doctrinal_witness records.

Step4, Round 2 review Finding S4: the C5 fix above had itself invented
an interval ("within days of each other") the Vita does not state -
S2 dates the first giving ("not six months after the death of his
parents"); S3 opens "And again as he went into the church," with no
interval given, nothing ruling out a longer gap. Removed from `text`,
`positions[0]`, `sources[0].locus`, and this note; the record now
states only what the Vita itself supports - two separate visits, no
stated interval between them.

Step5, Round 1 review Finding S6: this compiled text still opened "An
outsider, I think, would have found..." - a bare narratorial first
person with no quoted figure nearby, against the fleet's own strict
we-voice discipline (fleet-voice/EXEMPLAR-TRANSCRIPT.md v4, restated in
desert.voice.craft's own flavor_notes). Corrected to "An outsider, we
think, would have found..."

BAR SWEEP (2026-08-29, Mark: "much better thats the bar"): text rewritten to the approved sample's level - short sentences, everyday words; every claim, name, quote, hedge, and reviewed constraint kept.
