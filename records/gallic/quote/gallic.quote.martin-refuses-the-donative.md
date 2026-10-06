---
id: gallic.quote.martin-refuses-the-donative
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F5-I
- F5-P
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: >-
    The wording is Widely Accepted as Sulpitius's own text (Vita ch. IV, read at its own locus for
    this record) - one named ancient witness, close to Martin but not present at the scene, rather
    than Documented by independent corroboration. The narrated event (the donative, the exact words
    exchanged) carries the same Widely Accepted strength the host record's own narrative_tier_justification
    gives it; this record carries the words as Sulpitius reports them, not an independent finding that
    the exchange happened exactly so.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: "Life of St. Martin ch. IV (npnf211 div ii.ii.v, file lines 827-842): the donative at the city of the Vaugiones and Martin's request for discharge"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks for Martin's own words at the moment he left the army"
  - "participant asks what 'soldier of Christ' meant, in the phrase's own first occurrence"
  - "Representative needs the exact wording of the discharge request, not a paraphrase of it"
  prefer_instead:
  - "participant wants the whole scene told as a story, with its outcome - retrieve gallic.story.discharge-before-caesar, which this record is drawn from"
  - "participant wants Martin's second speech, offering to stand unarmed - retrieve gallic.quote.martin-offers-to-stand-unarmed"
text: >-
  In the meantime, as the barbarians were rushing within the two divisions of Gaul, Julian Cæsar,
  bringing an army together at the city of the Vaugiones, began to distribute a donative to the
  soldiers. As was the custom in such a case, they were called forward, one by one, until it came to
  the turn of Martin. Then, indeed, judging it a suitable opportunity for seeking his discharge—for
  he did not think it would be proper for him, if he were not to continue in the service, to receive
  a donative—he said to Cæsar, "Hitherto I have served you as a soldier: allow me now to become a
  soldier to God: let the man who is to serve thee receive thy donative: I am the soldier of Christ:
  it is not lawful for me to fight."
speaker_or_author: "Sulpitius Severus, narrating, with Martin's own reply to Cæsar quoted directly"
license: verbatim
modern_lens_note: >-
  A modern reader may expect a refusal of the donative to be framed as a matter of conscience about
  money. It isn't. Martin's own sentence turns on service, not pay: he has "served" as a soldier and
  now asks to "become a soldier to God" - the donative is refused only because it belongs to the old
  service, not because taking it would be wrong in itself. The four short clauses build to the same
  point four times: this is a change of master, stated as plainly as Sulpitius could report it.
modern_rendering: >-
  Meanwhile the barbarians were pouring into the two parts of Gaul. Julian Caesar gathered an army at
  the city of the Vaugiones and began to hand out a bonus payment to the soldiers. As was the custom,
  they were called forward one by one, until it came to Martin's turn. Then he judged it a good moment
  to ask for his discharge. He did not think it right to take the payment if he was not going to stay
  in the service. So he said to Caesar: "Up to now I have served you as a soldier. Now let me become a
  soldier for God. Let the man who is going to serve you take your payment. I am the soldier of
  Christ. I am not permitted to fight."
relations:
- type: associated-with
  target: gallic.story.discharge-before-caesar
- type: associated-with
  target: gallic.figure.martin
- type: associated-with
  target: gallic.figure.sulpitius
- type: associated-with
  target: gallic.quote.martin-offers-to-stand-unarmed
- type: associated-with
  target: gallic.force.army-and-rank-before
- type: associated-with
  target: gallic.gravity.soldier-of-christ
use_note:
  means: "Sulpitius narrates Martin refusing Julian's donative and asking discharge with the words 'I am the soldier of Christ: it is not lawful for me to fight.'"
  not_for:
    - "a refusal of pay on grounds of money, when the passage turns on a change of service"
    - "the offer to stand unarmed and the enemy's surrender, which sit in gallic.quote.martin-offers-to-stand-unarmed"
    - "a verbatim record of the exchange rather than Sulpitius's report of it"
    - "a rule binding every Christian soldier of the time"
  years: {from: 397, to: 397}
  status: reviewed
---
Verified against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n "began to
distribute a donative"` returns one hit, line 834. The chapter div is `<div3 title="Chapter IV. Martin
retires from Military Service." ... id="ii.ii.v">` (line 819). Read lines 827-842 directly: the quoted
span runs from "In the meantime, as the barbarians were rushing..." through "...it is not lawful for
me to fight." - one continuous paragraph in the source, no material skipped.

Normalization: the source hard-wraps prose at fixed widths; line breaks were joined with single
spaces. The source marks Martin's reply with a dash before an opening curly quotation mark and gives
no closing mark until the paragraph's own next full stop; this is rendered here as a normal,
properly-paired quotation, the edition's own punctuation for the same reason the model record for
this world drops curly marks around speech - the words, not the printer's marks, are what is quoted.
No word was added, dropped, substituted, or reordered. "Cæsar" is kept as the source spells it,
including in Sulpitius's own narration (the host record's own prose uses "Caesar" as its narrative
voice's spelling choice, not a claim about the source's own orthography).

speaker_or_author names both the narrator and the quoted speaker because the text field carries
Sulpitius's own narration together with Martin's directly quoted reply, not the reply alone; the two
are not separated because they form one continuous sentence in the source and separating them would
require inventing a narrator's frame sentence that Sulpitius does not supply at this exact point.
