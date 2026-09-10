---
id: gallic.term.compunction
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: draft
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: corroborating
  formation_confidence: Documented
  divergence_note: >-
    Weighted to Cassian; the single northern attestation (the angel's word to Martin after the Ithacian
    communion) depends on the translator's word choice for the angel's speech. Eucherius's De Contemptu
    Mundi would bear on this term and remains deliberately unswept. The Latin compunctio is not
    attested in the vendored translation.
sources:
- source_id: gallic.source.cassian-institutes
  locus: 'Institutes IV.43 ("From the fear of the Lord arises salutary compunction. From compunction of heart springs renunciation"); XII.15 ("their compunction for their faults increases day by day in proportion as their purity of soul advances")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-i
  locus: 'Conferences I.19 ("most salutary compunction"); II.11 ("my heart''s compunction increased and I openly burst into sobs and tears"); II.17 ("a healthy compunction")'
  license: public-domain
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: 'Dialogues III.13 ("Justly, O Martin, do you feel compunction ... Renew your virtue, resume your courage") - once, in the translator''s rendering'
  license: public-domain
- source_id: gallic.source.eucherius-de-contemptu-mundi
  locus: 'would bear on this term; deliberately unswept - nothing drawn'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - whether the monks felt guilty, or what compunction is
  - why tears were valued, or whether growing holier meant feeling worse
  - participant uses "compunction," "guilt," "remorse," "conscience," "tears," or "contrition"
  - Serapion's sobs, "From the fear of the Lord arises salutary compunction," Institutes XII.15, or the angel's word to Martin after the Ithacian communion
  do_not_retrieve_when:
  - the public discipline for a fault (retrieve penance / satisfaction)
  - the emotional ascent as a whole (retrieve fear -> hope -> love)
  - modern guilt or shame as pathology
relations:
- type: associated-with
  target: gallic.term.purity-of-heart
- type: associated-with
  target: gallic.term.grace
- type: associated-with
  target: gallic.term.renunciation
- type: associated-with
  target: gallic.term.the-world-secular
- type: associated-with
  target: gallic.term.disclosure-of-thoughts
- type: associated-with
  target: gallic.term.humility
- type: associated-with
  target: gallic.term.lukewarmness
- type: associated-with
  target: gallic.term.thoughts
- type: associated-with
  target: gallic.term.mortification
- type: associated-with
  target: gallic.term.angels
- type: associated-with
  target: gallic.term.beginning-of-a-good-will
- type: associated-with
  target: gallic.term.communion
- type: associated-with
  target: gallic.term.fear-hope-love
- type: associated-with
  target: gallic.term.penance-satisfaction
plain_meaning: >-
  For us compunction is the salutary pricking of heart from which the monastic life springs and by
  which it advances. "From the fear of the Lord arises salutary compunction. From compunction of heart
  springs renunciation." It is the sign of progress, not of failure: "their compunction for their
  faults increases day by day in proportion as their purity of soul advances."
world_word: compunction (compunctio)
false_friend:
- guilt, scrupulosity, or shame as psychological burdens to be relieved
- tears as breakdown
- compunction as a sign that something has gone wrong
senses:
  informational: >-
    Cassian sets it at the root of the ladder and again near its top. At the root: "From the fear of
    the Lord arises salutary compunction. From compunction of heart springs renunciation, i.e. nakedness
    and contempt of all possessions." It is one of the ways God visits the mind - when we have been
    slothful "He chastens us with most salutary compunction" - and what a true discipline produces
    where a false one cannot. The picture is Serapion at the after-supper conference: "first I was
    moved to secret sighs, and then my heart's compunction increased and I openly burst into sobs and
    tears," and the stolen biscuit comes out. Near the top, in the book on pride, the perfect are
    marked by it: they "recognize more and more that they are burdened with sin (for their compunction
    for their faults increases day by day in proportion as their purity of soul advances)." At Tours
    the word is heard once, in heaven's mouth: after Martin grieves at his coerced communion, "an angel
    stood by him and said, 'Justly, O Martin, do you feel compunction ... Renew your virtue, resume
    your courage.'"
  evidential: >-
    Cassian (Institutes IV.43, XII.15; Conferences I.19, II.11, II.17), received; Sulpitius once
    (Dialogues III.13), in the translator's rendering. Eucherius's De Contemptu Mundi is unswept. The
    Latin lemma is not attested.
  personal: >-
    The holier the monk, the more he weeps; the tears are not a symptom of distance from God but of
    nearness. In both our houses compunction is what a healthy heart does, and what a cooled one has
    stopped doing. The south trains us out of wonder and into compunction; and when the pricking is
    right, the remedy is not despair but renewal.
  translational: >-
    'Did the monks live in guilt - was feeling worse a sign something had gone wrong?' - the opposite:
    a salutary pricking that begins the monastic life and deepens as purity grows, sent by God,
    produced by true discipline, and confirmed by an angel as "just" - a weeping monk is a progressing
    monk.
quick_meaning: >-
  The healthy pricking of heart that starts the monastic life and deepens as the monk advances - a
  sign of progress, not of failure.
distortion_risk: medium
---
Built from Doc_06 entry 040 (Tier 2, promoted from Doc_03's Tier 3 on Doc_05 §8's weighting; chunk
galliclex040_compunction.md; Doc_03 4.8). Register emic. Quotations verified at locus by the build's
own Doc_06 pass; not re-read here. Row 25 is cited only as a stated coverage limit, labeled so.

Related-Terms also names fear -> hope -> love, penance / satisfaction and communion - cross-batch at
authoring time, added as relations (typed associated-with) at the reconciliation pass once all 81
term records existed.
