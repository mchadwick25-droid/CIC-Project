---
id: desert.term.nepsis
world_id: desert-monasticism
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells: [F4-P]
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: corroborating
  formation_confidence: Widely Accepted
  divergence_note: null
sources:
- source_id: desert.source.apophthegmata-patrum
  locus: "scattered sayings"
- source_id: desert.source.evagrius-praktikos
  locus: "Praktikos ch. 6 - the charter clause for this term: whether the thoughts disturb the soul is not up to us, but whether they linger, and whether they arouse passions, is (desert.quote.the-eight-generic-thoughts). Ch. 64 adds that the signs are read through the thoughts by day and through dreams at night"
  license: cc-by-4.0
- source_id: desert.source.cassian-conferences
  locus: Conf. XXIV ch. VI, Abraham on guarding the thoughts (the arch drawn from its centre)
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - questions about attention, vigilance, or catching thoughts early
claim_guards:
- do not equate with modern mindfulness practice - the systematized neptic tradition belongs to a much later world and must not be retrojected
relations:
- type: associated-with
  target: desert.quote.the-nous-beholds-its-own-radiance
- type: associated-with
  target: desert.term.diakrisis
- type: associated-with
  target: desert.term.logismoi
- type: associated-with
  target: desert.term.hesychia
plain_meaning: "Watchfulness: standing guard over your own inner movements, so a thought is caught early, while it is still small."
world_word: nepsis
false_friend:
- generic mindfulness
senses:
  informational: "The ongoing act of watching the mind - distinct from discernment, which judges what the watching finds. Rooted in shared Christian vocabulary (Peter's call to be sober and watch), most systematically developed at Kellia; as with stillness, the later Byzantine neptic tradition's full apparatus is not this world's."
  evidential: "Attested in the sayings and in Evagrius's corpus; the systematized register is, like the rest of his scheme, concentrated in that one author."
  personal: "The point was to meet a thought at the door rather than after it had moved in - vigilance as a kindness to yourself, because everything is easier early."
  translational: "Not mindfulness as a calm-inducing practice: the watching here is a sentry's, oriented to a real adversary, and what it feeds is discernment, not relaxation."
quick_meaning: "Watching your own thoughts like a sentry - so you catch them early."
distortion_risk: high
---
Re-derived from Doc_06 SS2.5 (Tier 2; tags AS TC DR PV). Feeds
diakrisis directly (Doc_06's own ecological-function line); shares
hesychia's anti-retrojection fence.

The informational sense refers to Peter's call to be sober and watch
without quoting it verbatim, since no vendored English matches the
traditional wording exactly; a future pass may quote WEB verbatim and
register it if the exact wording becomes load-bearing. The
informational sense names Kellia directly rather than this build's own
lettered taxonomy, and the do_not_retrieve_when fence states its
substantive reason plainly, matching hesychia's parallel fence.
