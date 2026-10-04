---
id: gallic.term.disclosure-of-thoughts
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-P
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Single-voice (Cassian), and specifically an Egyptian coenobitic practice "we have seen observed
    throughout Egypt"; whether any Gallic house kept it is not documented - what a Gallic junior in the
    420s actually underwent is not written down. Tours has no counterpart in what was read. Cassian's
    own word "confession" in this sense is held apart from later sacramental confession. The Latin
    lemma is not supplied against the text.
sources:
- source_id: gallic.source.cassian-institutes
  locus: 'Institutes IV.9 ("any itching thoughts"; "lay them bare to the senior"; "a thought is from the devil if we are ashamed to disclose it"; "the alphabet, as it were, and first syllables"); IV.37 ("watch his head," i.e. "the first rise of thoughts")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-i
  locus: 'Conferences II.10 ("the scrutiny of the elders"; "a wrong thought is enfeebled at the moment that it is discovered"); II.11 (Serapion; "your confession frees you from this slavery"); II.13 (the unfit elder)'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - whether the monks "went to confession"
  - what a monk told his elder, or how thoughts were judged
  - what the first thing a novice learned was
  - participant uses "confession," "confess," "spiritual direction," "accountability," or "opening the heart"
  - Serapion's biscuit, the shame-test, the alphabet of perfection, or "watch his head"
  prefer_instead:
  - the public penance for a committed fault (retrieve penance / satisfaction)
  - the general doctrine of thoughts' three origins (retrieve thoughts)
  - the regulating virtue itself (retrieve discretion)
  - later sacramental confession of sins to a priest - our practice is of thoughts, to an elder, before sin
relations:
- type: associated-with
  target: gallic.term.the-fathers-elders
- type: associated-with
  target: gallic.term.elder-senior-abbot
- type: associated-with
  target: gallic.term.junior-novice
- type: associated-with
  target: gallic.term.conference
- type: associated-with
  target: gallic.term.obedience
- type: associated-with
  target: gallic.term.humility
- type: associated-with
  target: gallic.term.thoughts
- type: associated-with
  target: gallic.term.compunction
- type: associated-with
  target: gallic.term.the-devil-demons
- type: associated-with
  target: gallic.term.penance-satisfaction
- type: associated-with
  target: gallic.term.illusion
- type: precondition-for
  target: gallic.term.discretion
plain_meaning: >-
  In Cassian's Marseilles, the practice of laying every "itching thought" bare to the senior as soon
  as it arises. It is "the alphabet, as it were, and first syllables in the direction of perfection."
  The elders' rule: "a thought is from the devil if we are ashamed to disclose it." So "a wrong
  thought is enfeebled at the moment that it is discovered."
world_word: disclosure of thoughts (to the senior)
false_friend:
- sacramental confession of sins to a priest, with absolution
- spiritual direction and "accountability" as optional counsel
- therapy
senses:
  informational: >-
    It is the first thing the Egyptians teach. The juniors "are next taught not to conceal by a false
    shame any itching thoughts in their hearts, but, as soon as ever such arise, to lay them bare to
    the senior, and ... to take it on trust that that is good or bad which is considered and pronounced
    so by the examination of the senior." The test is shame: "a thought is from the devil if we are
    ashamed to disclose it to the senior." Pinufius makes it the monk's standing guard - "watch his
    head," the first rise of thoughts - and Moses names it the first proof of humility and gives its
    mechanism: "a wrong thought is enfeebled at the moment that it is discovered." The story that
    carries it is Serapion's: a boy who stole a biscuit a day, hearing an old man speak after supper
    "about ... the dominion of secret thoughts," pulls it from his dress and confesses, and the old man
    answers, "Without any words of mine, your confession frees you from this slavery." The danger on
    the other side is a harsh elder who shames the one who discloses - which is why not every grey
    head is fit to hear.
  evidential: >-
    Cassian only (Institutes IV.9, IV.37; Conferences II.10-13), Egyptian coenobitic practice by his
    own framing. Gallic observance is undocumented; Tours has no counterpart in what was read. The
    editor's cross-reference at IV.9 is editorial.
  personal: >-
    What is disclosed is a thought, not a deed; it is told to an elder, not a priest; and it is told
    before it is acted on, so that it need never be. Our shame is a diagnostic. "Our cunning adversary
    cannot in any way circumvent a young and inexperienced monk" who does this - and "confession" in
    our book is not the sacrament.
  translational: >-
    'So the monks went to confession?' - not as that word came to mean: the disclosure of thoughts,
    before any deed, to an elder whose examination replaced one's own judgment, tested by shame and
    freeing "at the moment that it is discovered" - the first syllable of the monastic alphabet,
    Egypt's practice, prescribed for a Gallic house.
quick_meaning: >-
  Telling every thought to the senior the moment it rises, before any deed. The first lesson of the
  monastic life - and not the later sacrament.
distortion_risk: high
use_note:
  means: "Disclosure of thoughts meant laying every rising thought bare to the senior before any deed, the first lesson of Cassian's monastic life and not the later sacrament."
  not_for:
    - "sacramental confession of sins to a priest with absolution"
    - "therapy or optional spiritual accountability"
    - "public penance for a committed fault, which sits in gallic.term.penance-satisfaction"
    - "a documented Gallic practice, when whether any Gallic house kept it is unrecorded"
  years: {from: 415, to: 426}
  status: reviewed
---
Built from Doc_06 entry 030 (Tier 2; chunk galliclex030_disclosure-of-thoughts.md; Doc_03 3.8).
Register emic. Quotations verified at locus by the build's own Doc_06 pass; not re-read here. The
relation to discretion is typed precondition-for, per Conf. II.10 as the chunk reads it (discretion
"gained only by true humility, i.e. by testing every thought ... against the judgment of the
elders"). The Benedictine/sacramental back-projection (Doc_06 §4(b)) runs directly through this term.
Canon cell F4-P: "enfeebled at the moment that it is discovered" is this world's own answer to
someone struggling with their own mind.

Related-Terms also names the devil / demons, penance / satisfaction and illusion - cross-batch at
authoring time, added as relations (typed associated-with) at the reconciliation pass once all 81
term records existed.
