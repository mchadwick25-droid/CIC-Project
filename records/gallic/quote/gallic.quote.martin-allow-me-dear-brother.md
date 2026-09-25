---
id: gallic.quote.martin-allow-me-dear-brother
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: >-
    The wording is Documented as Sulpitius's own text. Like the rest of the deathbed scene, the saying
    rests on the testimony of those present, not on Sulpitius's own witness; carried at Widely Accepted
    strength on that basis, at ordinary narrative register rather than the letter's more overtly
    supernatural claims.
sources:
- source_id: gallic.source.sulpitius-letters
  locus: 'Letter III, To Bassula, His Mother-in-Law (npnf211 div ii.iii.iii, file lines 2470-2473): Martin''s reply to the presbyters asking him to ease his body by turning on his side'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - participant asks about prayer at the point of death, or keeping attention fixed on God through
    physical suffering
  - conversation reaches the interior road held even in the body's last extremity
  prefer_instead:
  - participant wants the fuller deathbed climax, including the devil - retrieve
    gallic.quote.martin-rebukes-the-devil-and-dies, which follows this saying directly
text: >-
  Allow me, dear brother, to fix my looks rather on heaven than on earth, so that my spirit which is
  just about to depart on its own journey may be directed towards the Lord.
speaker_or_author: gallic.figure.martin
license: verbatim
modern_lens_note: >-
  The presbyters offer a small physical mercy - turning him to ease his body - and Martin declines it
  for a reason about direction, not comfort: he wants his eyes, and by extension his attention, fixed
  on heaven rather than earth until the last moment. Bodily ease and spiritual orientation are treated
  as genuinely in tension here, and Martin chooses the second.
relations:
- type: associated-with
  target: gallic.story.death-of-martin-at-condate
- type: associated-with
  target: gallic.figure.martin
- type: associated-with
  target: gallic.gravity.interior-road
modern_rendering: PENDING_OPUS_RENDERING
---
Verified verbatim against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"fix my looks rather on heaven"` returns line 2471. Read in context at lines 2468-2473: "And on being
asked by the presbyters who had then gathered round him, to relieve his body a little by a change of
side, he exclaimed: "Allow me, dear brother, to fix my looks rather on heaven than on earth, so that
my spirit which is just about to depart on its own journey may be directed towards the Lord."" The
quoted reply matches the host record's current wording exactly; verified independently rather than
trusted on that basis. No word was added, dropped, substituted, or reordered; hard line wraps were
joined with single spaces, and the edition's own curly quotation marks are dropped as its own
punctuation, not part of the quoted prose.
