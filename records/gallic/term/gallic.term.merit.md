---
id: gallic.term.merit
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F1-T
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Cross-voice in referent, not in doctrine: Cassian's "merit" is what effort cannot claim against
    grace (Marseilles); Sulpitius's merita are a saint's standing by which a miracle is asked
    (Tours). The two senses never meet in one text and so never conflict - they must be kept apart,
    not reconciled. Latin meritum is attested only in Heurtley's editorial appendix quoting
    Augustine; Hilary of Arles (row 27) uses merita of Honoratus in a phrase Doc_04 rated
    Inferential/Thin. Pelagius's condemned thesis that grace is given "according to our merits" is
    Augustine's report and is not quoted.
sources:
- source_id: gallic.source.cassian-conferences-part-i
  locus: 'Conferences I.15 ("from no antecedent merits of ours, but by the free grace of His pity He receives us")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-ii
  locus: 'Conferences XIII.12 ("not to refer all the merits of the saints to the Lord in such a way as to ascribe nothing but what is evil and perverse to human nature"); XIII.16 ("in accordance with the desert of each man"); XIII.18 ("not to the merit of our own works but to heavenly grace")'
  license: public-domain
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: 'Dialogues III.2 ("loose, by his pious merits, her tongue"); III.17 ("the sacred merits of this man")'
  license: public-domain
- source_id: gallic.source.gennadius-de-viris-illustribus
  locus: 'ch. LXXXVI (Faustus - "is not its own desert, but the gift of grace")'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - whether the monks thought they "earned" grace or salvation
  - what "merit" meant
  - why a miracle is asked "by his merits"
  - participant uses "merit," "earn," "deserve," "works-righteousness," "reward"
  - Conf. XIII.12's warning about the merits of the saints; Conf. I.15; the dumb girl healed "by his pious merits"
  prefer_instead:
  - the broader doctrine is the question (retrieve grace (of God))
  - the participant means the saint's power as such (retrieve virtus / power)
  - any attempt to source this term from Salvian
  - '"merit" as a later scholastic category (condign / congruous)'
relations:
- type: associated-with
  target: gallic.term.beginning-of-a-good-will
- type: associated-with
  target: gallic.term.co-operation
- type: associated-with
  target: gallic.term.pelagians-as-foil
- type: associated-with
  target: gallic.term.blessing
- type: associated-with
  target: gallic.term.free-will
- type: associated-with
  target: gallic.term.virtus
- type: associated-with
  target: gallic.term.monk-bishop
- type: associated-with
  target: gallic.term.humility
- type: tension-with
  target: gallic.term.grace
plain_meaning: >-
  A word we speak in two rooms. At Marseilles, it is what our effort cannot claim against grace.
  At Tours, it is the saint's standing before God, by which a miracle is asked.
world_word: merit (meritum; "no antecedent merits")
false_friend:
- '"works-righteousness" - earning salvation - as the thing we stood for'
- merit in the later scholastic sense
- a saint's merits as a treasury
senses:
  informational: >-
    At Marseilles our teachers hold the word at both ends. Abbot Moses reminds the monk of the call
    with which "from no antecedent merits of ours, but by the free grace of His pity He receives
    us." Chaeremon ascribes "the main share in our salvation" not to "the merit of our own works but
    to heavenly grace," and refuses "the profane notion of some" who lay down that grace is dispensed
    "in accordance with the desert of each man." Yet the same conference will not let the word go:
    we must not refer "all the merits of the saints" to the Lord so as to leave human nature nothing
    but evil. At Tours merit is what one appeals to - bishops beg Martin to loose a girl's tongue
    "by his pious merits," and Sulpitius hopes Rome may learn "the sacred merits of this man."
  evidential: >-
    Both senses are directly attested: Cassian, Conf. I.15, XIII.12, XIII.16, XIII.18 (Marseilles,
    received); Sulpitius, Dial. III.2 and III.17 (Tours). Faustus's later teaching that the will's
    gain "is not its own desert, but the gift of grace" is known through Gennadius ch. LXXXVI.
    Augustine's treatises are context only and are not quoted for this term.
  personal: >-
    We deny that grace is earned and we ask a miracle by a saint's merits, and we see no
    contradiction, because the two are never said in the same breath. Of every virtue we say
    "Not I"; of Martin we say his merits stand before God.
  translational: >-
    A modern hearer may hear "merit" and think of earning salvation, or of a treasury of the
    saints' merits. We refused the first outright - "no antecedent merits" - and the second is a
    later idea. What we kept was narrower: the saints' merits are real and not to be denied to human
    nature, and grace still goes first.
quick_meaning: >-
  Two rooms, one word. At Marseilles, what our effort cannot claim against grace, which goes first.
  At Tours, the saint's standing by which we ask a miracle.
distortion_risk: high
---
Built from Doc_06 entry 046 (`galliclex046_merit.md`, Tier 2, tags SC TC DR; Doc_03 5.7). The
two referents are kept apart in every field, per the chunk's own voice note. CT tag not applied
(Doc_06 section 3).

Related-Terms also names grace (of God), free will, virtus / power, bishop / the monk-bishop, and
humility - cross-batch at authoring time, added as relations (typed associated-with except as stated
here) at the reconciliation pass once all 81 term records existed. Relation typing: `tension-with`
gallic.term.grace follows the chunk's own "the counter-term of grace (008) in the south's argument"
- what is refused to effort (no antecedent merits) and yet kept for the saints, held against grace
rather than inside it. The chunk also names perseverance (in-batch); not made a relation here, since
the chunk's own Ecological Function states no dependency on it beyond cluster adjacency.
