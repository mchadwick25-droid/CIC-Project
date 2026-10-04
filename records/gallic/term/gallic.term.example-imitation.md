---
id: gallic.term.example-imitation
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F2-E
- F2-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    All three founding voices attest the term at both nodes, with a real difference in medium: a master
    seen at Tours and in Cassian's Egypt, fathers read at Lerins. What this record does not assert is the
    historicity of the exemplar's deeds (the eyewitness claims of Sulpitius and Cassian) - that question
    belongs to virtus / power, which carries Reported-Experience Status, and to the story inventory.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: 'Life of St. Martin ch. I ("an example to others"); ch. X ("disciplined after the example of the saintly master"); ch. XXV (Paulinus "the object of our imitation")'
  license: public-domain
- source_id: gallic.source.sulpitius-letters
  locus: 'Letter I (the defence against a skeptic); Letter III ("a different example"; "so numerous plants")'
  license: public-domain
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: 'Dialogues II.4 ("I myself am a witness")'
  license: public-domain
- source_id: gallic.source.cassian-institutes
  locus: 'Institutes Preface (Castor''s life "amply sufficient for an example"; "cannot be taught save by one who has had experience"); IV.40 ("from one or two only"); V.4 (the bee, Antony''s teaching)'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-ii
  locus: 'Conferences XI.4 ("the authority of a teacher")'
  license: public-domain
- source_id: gallic.source.vincent-commonitory
  locus: 'Commonitory ch. 1 [1] ("received from the holy Fathers")'
  license: public-domain
- source_id: gallic.source.gennadius-de-viris-illustribus
  locus: 'ch. LXX (Hilary of Arles''s "Life of Saint Honoratus, his predecessor")'
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - how a monk was actually trained or formed
  - why the Life of Martin or the Conferences were written
  - what authority a teacher had
  - participant uses "example," "role model," "imitate," or "mentor"
  - Martin's disciples, Cassian's "one or two only," or eyewitness claims
  - participant asks whether the miracle stories are "true"
  prefer_instead:
  - a specific exemplar's own deeds (retrieve virtus / power for the northern miracle corpus)
  - the elder-junior relationship's disciplinary mechanics (retrieve disclosure of thoughts, obedience)
  - the historicity of a particular story (the story inventory's territory)
relations:
- type: associated-with
  target: gallic.term.the-fathers-elders
- type: associated-with
  target: gallic.term.virtus
- type: associated-with
  target: gallic.term.monk-bishop
- type: associated-with
  target: gallic.term.elder-senior-abbot
- type: associated-with
  target: gallic.term.junior-novice
- type: associated-with
  target: gallic.term.disciple-master
- type: associated-with
  target: gallic.term.tradition
- type: associated-with
  target: gallic.term.conference
- type: associated-with
  target: gallic.term.obedience
- type: associated-with
  target: gallic.term.humility
- type: associated-with
  target: gallic.term.perfection
- type: associated-with
  target: gallic.term.apostolic-authority
- type: associated-with
  target: gallic.term.blessing
- type: associated-with
  target: gallic.term.commonitory-peregrinus
- type: associated-with
  target: gallic.term.sackcloth-and-ashes
plain_meaning: >-
  How formation passes from one person to another among us. A disciple is made by watching - and,
  later, by reading - a named man whose life is held up as the thing to copy. Our books exist to be
  that example when the man himself is absent.
world_word: example / imitation (exemplum)
false_friend:
- an illustration in an argument
- a role model freely chosen by the individual and admired from a distance
- imitation as derivative or inauthentic
senses:
  informational: >-
    The Life of Martin says why it exists in its first chapter: to "serve in future as an example to
    others." At Marmoutier the example is the whole method of the house - "eighty disciples, who were
    being disciplined after the example of the saintly master" - with no probation, no dean, no rule.
    Dying on ashes, Martin refuses straw: "I have sinned if I leave you a different example." At
    Marseilles the word carries Egypt to Gaul: institutes must come from "one who has had experience,"
    the junior is to imitate "one or two only," and an old man will not relax his fast for guests
    "lest the other's strictness should be relaxed owing to my example. For the authority of a teacher
    will never be strong unless he fixes it in the heart of his hearer by the actual performance of
    his duty." At Lerins the example moves from a face to a page: Vincent collates the writings of the
    holy Fathers, while Hilary of Arles still writes a disciple's Life of his own master, Honoratus.
  evidential: >-
    Attested in all three founding voices: Sulpitius (Life chs. I, X, XXV; Letters I, III; Dialogues
    II.4), Cassian (Institutes Preface, IV.40, V.4; Conferences XI.4), Vincent (Commonitory ch. 1).
    Gennadius corroborates that the disciple's-Life form existed at Lerins, and Hilary of Arles's own
    Latin uses exemplum repeatedly. The whole literature of Tours rests on having seen - "I myself am
    a witness" - and the Life is defended against a skeptic on that ground; whether the deeds seen
    happened as told is not what this record asserts.
  personal: >-
    Among us formation is a matter of who, not what. A monk is formed by a person, seen or read, whose
    life is the standard; the authority of every teaching rests on someone having seen it done; and
    our books are written to stand in for the man when he is gone. An example is a thing one is
    responsible for, not merely a thing one offers - an elder's laxity is his disciples' ruin.
  translational: >-
    'Aren't these Lives just legend, and "imitation" just copying?' - for us the Life was written by a
    man who says he saw, as the thing to be copied in deed and body, and imitation of a named master
    was the method by which every monk and bishop we produced was made; our literature is Lives and
    reported conferences rather than treatises for exactly this reason.
quick_meaning: >-
  Formation by copying a named man, seen or read - the method of every house we have, and the reason
  our books are Lives.
distortion_risk: medium
use_note:
  means: "Example meant formation by copying a named man, seen or read, which is why the books of this world are Lives."
  not_for:
    - "an illustration in an argument"
    - "a role model freely chosen and admired from a distance"
    - "a particular exemplar's deeds, which sit in gallic.term.virtus"
    - "the historicity of any one story, which the story records handle"
  years: {from: 397, to: 434}
  status: provisional
---
Built from Doc_06 entry 003 (Tier 1; chunk galliclex003_example-imitation.md; Doc_03 3.2). Register
emic. Quotations verified at locus by the build's own Doc_06 pass; not re-read here. Doc_06 §2.2
records the exemplar as two hubs, one per node, not one cross-node hub;
this record keeps the two media (seen / read) distinct accordingly. Canon cells: F2-E because the
term's own content (eyewitness Lives written to be examples) is what a participant asking about legend
needs; F2-I because formation by watching a person is this world's own answer to how one received
without reading.

Related-Terms also names Commonitory / Peregrinus - cross-batch at authoring time, added as
relations (typed associated-with) at the reconciliation pass once all 81 term records existed.
