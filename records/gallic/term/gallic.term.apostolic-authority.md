---
id: gallic.term.apostolic-authority
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-E
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: corroborating
  formation_confidence: Documented
  divergence_note: >-
    Cross-voice in referent - three voices, three referents: Sulpitius's predicate of Martin (the
    apostles' power and standing, "deemed powerful and truly apostolical"), Cassian's summit of love
    and origin of the coenobium, Vincent's See. The referents never argue because they never meet.
    The northern predicate is single-voice (Sulpitius), and its historicity falls under virtus /
    power's Reported-Experience Status. Nobody in the south calls a living man "apostolical." No
    Latin lemma sought.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: 'ch. VII ("deemed powerful and truly apostolical"); ch. XX ("in Martin alone, apostolic authority continued to assert itself")'
  license: public-domain
- source_id: gallic.source.sulpitius-sacred-history
  locus: 'II.50 ("a man clearly worthy of being compared to the Apostles")'
  license: public-domain
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: 'II.5 ("compared him to the apostles and prophets")'
  license: public-domain
- source_id: gallic.source.cassian-institutes
  locus: 'IV.43 ("the perfection of apostolic love")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-iii
  locus: 'XVIII.5 ("the days of the preaching of the Apostles")'
  license: public-domain
- source_id: gallic.source.vincent-commonitory
  locus: 'ch. 6 [15] ("the Apostolic See")'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - why Martin is called "apostolic"
  - whether the monks thought of themselves as continuing the apostles
  - what "apostolic" means in each writer
  - participant uses "apostolic," "apostle," "apostolic succession," "like the apostles"
  - Vita VII; Vita XX before Maximus; Inst. IV.43's ladder; Piamun on the coenobium's origin; Vincent's Apostolic See
  prefer_instead:
  - the participant means Rome specifically (retrieve Apostolic See / Pope)
  - the saint's power as such (retrieve virtus / power)
  - '"apostolic succession" as a later doctrine of orders - not our vocabulary'
relations:
- type: associated-with
  target: gallic.term.apostolic-see-pope
- type: associated-with
  target: gallic.term.virtus
- type: associated-with
  target: gallic.term.monk-bishop
- type: associated-with
  target: gallic.term.purity-of-heart
- type: associated-with
  target: gallic.term.monastery-coenobium
- type: associated-with
  target: gallic.term.the-fathers-elders
- type: associated-with
  target: gallic.term.example-imitation
- type: associated-with
  target: gallic.term.the-rule
plain_meaning: >-
  At Tours, the highest thing said of Martin - having the apostles' power over death, demons, and
  emperors. At Marseilles, the perfection of love, and the first Church's common life.
world_word: apostolic ("truly apostolical"; "apostolic authority")
false_friend:
- '"apostolic succession" as a doctrine of validly ordained bishops'
- '"apostolic" as an institutional or denominational adjective'
- Martin's "apostolic authority" as jurisdiction
senses:
  informational: >-
    The word is given to Martin by what he does. When the catechumen rises from the dead, "the name
    of the sainted man became illustrious, so that, as being reckoned holy by all, he was also
    deemed powerful and truly apostolical." Before Maximus, where priests had taken second place to
    the royal retinue, "in Martin alone, apostolic authority continued to assert itself." At Trier
    he is "a man clearly worthy of being compared to the Apostles." In the south the word points at
    love and at origin: the formation manual's ladder ends "by purity of heart the perfection of
    apostolic love is acquired," and Abbot Piamun traces the coenobites to "the days of the
    preaching of the Apostles," when believers had all things common. Vincent's "Apostolic See" is
    a place.
  evidential: >-
    Attested in all three founding voices with three referents: Sulpitius (Vita VII, XX; Sacred
    History II.50; Dial. II.5), Cassian (Inst. IV.43; Conf. XVIII.5), Vincent (Comm. 6). The
    predicate of a living man is Sulpitius's alone.
  personal: >-
    The north's highest praise is a word the south uses only of love and of the first Church.
    Martin has the apostles' standing - over death, over demons, over an emperor's table - and no
    one at Marseilles would say that of a living man.
  translational: >-
    A modern hearer may reach for "apostolic succession" - a doctrine of orders - or for an
    institutional adjective. Neither is ours. For us "apostolic" means the apostles' own power
    possessed by a living saint, or the perfection of love the ascent reaches, or the antiquity of
    the common life.
quick_meaning: >-
  At Tours, the highest word for Martin - the apostles' own power, shown by raising the dead and
  facing an emperor. At Marseilles, the perfection of love, and the common life of the first
  Church.
distortion_risk: medium
use_note:
  means: "Apostolic authority meant, at Tours, Martin's apostle-like power over death, demons and emperors, and at Marseilles the perfection of love and the first Church's common life."
  not_for:
    - "apostolic succession as a doctrine of validly ordained bishops"
    - "Martin's apostolic authority as jurisdiction"
    - "Rome as such, which sits in gallic.term.apostolic-see-pope"
    - "the saint's power as such, which sits in gallic.term.virtus"
  years: {from: 397, to: 435}
  status: provisional
---
Built from Doc_06 entry 063 (`galliclex063_apostolic-authority.md`, Tier 2, tags SC DR TC;
Doc_03 8.2). The three referents are kept apart in every field per the chunk's voice note.
canon_cells: F4-E because Piamun's tracing of the common life to "the days of the preaching of
the Apostles" is this world's own claim that its practice goes back to the apostles.

Related-Terms also names virtus / power, bishop / the monk-bishop, purity of heart, monastery /
coenobium, the Fathers / elders, example / imitation, and the rule - cross-batch at authoring time,
added as relations (typed associated-with) at the reconciliation pass once all 81 term records
existed. The chunk also names the possessed / exorcism and communion (in-batch); not made relations,
since no dependency is stated.
