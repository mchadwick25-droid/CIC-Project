---
id: desert.term.anachoresis
world_id: desert-monasticism
record_type: term
schema_version: 2
status: draft
register: emic
canon_cells: [F4-I, F5-P]
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: null
sources:
- source_id: desert.source.athanasius-vita-antonii
  locus: "SS2-14 (the staged withdrawal), SS46-47 (withdrawal as the daily-martyrdom successor once persecution ended, anchored by desert.search.white-martyrdom-citation), SS49-50 (the inner mountain)"
  license: public-domain
- source_id: desert.source.apophthegmata-patrum
  locus: "passim (the tradition's organizing act)"
- source_id: desert.source.palladius-lausiac-history
  locus: "ch. VII, VIII, XVIII (withdrawal as the ordinary shape of settlement life at Nitria, Kellia, and the wider desert)"
  license: public-domain
- source_id: desert.source.kellia-excavations
  locus: "settlement pattern corroboration"
- source_id: desert.source.nepheros-archive
  locus: "documentary corroboration of settlement embeddedness (Melitian community; representativeness a working assumption, not settled)"
- source_id: desert.source.goehring-ascetics
  locus: "the embeddedness thesis - settlements on marginal-but-not-remote land with real village trade ties; cited jointly with Kellia and Nepheros per this world's standing rule, not alone"
retrieval:
  tier: 1
  retrieve_when:
  - why anyone left ordinary life for the desert
  - what joining this movement cost or required
  - questions about escape, retreat, or running away
  do_not_retrieve_when: []
relations:
- type: associated-with
  target: desert.term.apotage
- type: associated-with
  target: desert.term.xeniteia
- type: associated-with
  target: desert.term.kellion
- type: associated-with
  target: desert.term.hesychia
- type: associated-with
  target: desert.term.cheironaxia
- type: associated-with
  target: desert.term.geron-abba-amma
plain_meaning: "Withdrawal: leaving settled village life for the desert's edge, as the whole work of formation, not a change of address."
world_word: anachoresis
false_friend:
- retreat as escape or opting out
- a vacation or a temporary getaway
senses:
  informational: "The defining act of this world: departing village or town life for marginal or remote land, where distance, solitude, and struggle are themselves the curriculum. Antony's own career shows its shape - a staged deepening from village edge to outer mountain to inner mountain, not one dramatic exit."
  evidential: "Attested across every stream this world has: Athanasius's Life of Antony, the sayings tradition, Palladius, and the excavated settlements at Kellia. The documentary record also qualifies the rhetoric: the settlements sat on marginal land with real village trade ties, so 'flight to the desert' was never a total break."
  personal: "To those who did it, withdrawal was the most demanding form of engagement, not the least - a decision to face, without cushioning, the interior life that settled routine lets a person avoid. It replaced martyrdom as the whole self given at once."
  translational: "'Withdrawal' or 'retreat' in the modern sense - a break to recharge, an escape from responsibility - reverses the meaning. This was permanent, bodily, and itself the point; the desert was the arena, not the exit."
quick_meaning: "Leaving settled life for the desert, as the work of formation itself."
---
Re-derived from Doc_06 SS1.1 (Tier 1; tags AS TC RT DR; anchors gravity
1 per Doc_04). The Goehring embeddedness qualification is in the
evidential sense deliberately - the tension with the world's own
rhetoric is gravity 8's territory and is stated, not smoothed. Related
Terms carried from Doc_06's cleared 24-edge reciprocity graph.

Step3a Review Round 5, Finding S3: the evidential sense's embeddedness
claim paraphrased Goehring's thesis near-verbatim without registering
him, against this world's standing rule that embeddedness claims cite
Kellia + Nepheros + Goehring jointly, never Goehring alone or
unregistered; and the personal sense's martyrdom-successor claim
carried no locus for it. Both fixed by registering the missing sources
above - Nepheros and Goehring alongside the already-present Kellia,
and the Vita SS46-47 locus already anchored by
desert.search.white-martyrdom-citation - rather than by rewording
claims the sources already supported.

Step3a Review Round 6, Finding S3: the evidential sense names Palladius
among the attesting streams ("Athanasius's Life of Antony, the sayings
tradition, Palladius, and the excavated settlements at Kellia"), but
Palladius was not registered in sources[] - the same defect class this
commit's own Round 5 fix addressed for Goehring, unswept to the one
other unregistered name sitting in the same sentence. Registered above
(ch. VII, VIII, XVIII, all attesting withdrawal as settlement life's
ordinary shape).
