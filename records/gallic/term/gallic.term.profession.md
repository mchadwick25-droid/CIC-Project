---
id: gallic.term.profession
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
    Both nodes, two voices: Sulpitius of individuals and oaths, Cassian of the whole way of life. The
    "goal and end" of the profession is Abbot Moses's teaching and received. The Latin professio is
    attested in the volume only in the editor's textual footnote to De Incarnatione, an unread work,
    and not in this sense.
sources:
- source_id: gallic.source.cassian-conferences-part-i
  locus: 'Conferences I.2 ("our profession too has its own goal and end")'
  license: public-domain
- source_id: gallic.source.cassian-institutes
  locus: 'Institutes I.10 ("the humble character of our profession"); IV.33 ("the responsibility of this profession"; "a deserter or lukewarm"); X.3 ("begins to forget the object of his profession")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-iii
  locus: 'Conferences XVIII.7 ("renunciation only as a public profession, i.e., before the face of men")'
  license: public-domain
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: 'Dialogues II.11 ("having professed himself a monk"; "taken the oath of allegiance in the same service")'
  license: public-domain
- source_id: gallic.source.sulpitius-vita-martini
  locus: 'Life of St. Martin ch. II ("the necessary vows"); ch. XXIII (Anatolius "under the profession of a monk")'
  license: public-domain
- source_id: gallic.source.sulpitius-letters
  locus: 'Letter II ("both by vow and virtues")'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - whether monks took vows, or what they promised
  - whether a monk could leave, or what "profession" meant
  - participant uses "vow," "profess," "commitment," "oath," or "deserter"
  - the Sarabaite's public profession, Anatolius's false profession, the soldier who "professed himself a monk," or the "goal and end" of the profession
  do_not_retrieve_when:
  - a "profession of faith" as a creed (retrieve the rule or Catholic)
  - a trade or occupation
  - the later formal rite of monastic vows
relations:
- type: associated-with
  target: gallic.term.monk-solitary
- type: associated-with
  target: gallic.term.soldier-of-christ
- type: associated-with
  target: gallic.term.purity-of-heart
- type: associated-with
  target: gallic.term.junior-novice
- type: associated-with
  target: gallic.term.conversion
- type: associated-with
  target: gallic.term.renunciation
- type: associated-with
  target: gallic.term.lukewarmness
- type: associated-with
  target: gallic.term.goal-and-end
- type: associated-with
  target: gallic.term.accidie
- type: associated-with
  target: gallic.term.perseverance
- type: associated-with
  target: gallic.term.sarabaite
- type: associated-with
  target: gallic.term.the-monks-dress
plain_meaning: >-
  For us the profession is the monastic undertaking as a binding public commitment, with its own "goal
  and end." A soldier makes it when he "professed himself a monk." A false monk assumes it "under the
  profession of a monk." A man "turned out a deserter or lukewarm" has betrayed it.
world_word: profession (professio)
false_friend:
- a career ("the profession")
- the later formal rite of solemn vows with canonical consequences
- profession of faith as a creedal declaration
senses:
  informational: >-
    Cassian makes the word carry the whole life: "Our profession too has its own goal and end, for
    which we undergo all sorts of toils not merely without weariness but actually with delight." Dress
    is chosen for "the humble character of our profession"; the man pulled from his cell by accidie
    "begins to forget the object of his profession"; Pinufius warns the newly received that, admitted
    "without realizing the responsibility of this profession," he might have "turned out a deserter or
    lukewarm." The Sarabaites are the counterfeit, "making their renunciation only as a public
    profession, i.e., before the face of men." At Tours the word attaches to persons and oaths: a
    soldier who "had renounced the military life in the Church, having professed himself a monk";
    Anatolius, who "under the profession of a monk, falsely assumed every appearance of humility and
    innocence"; the boy Martin prevented by his age from "the necessary vows"; the dying bishop who
    "both by vow and virtues" was able and willing to be a martyr.
  evidential: >-
    Cassian (Conferences I.2, XVIII.7; Institutes I.10, IV.33, X.3) and Sulpitius (Dialogues II.11;
    Life chs. II, XXIII; Letter II). The Latin professio in this sense is not attested in the vendored
    volume.
  personal: >-
    A profession among us is public, and we know it can be faked - which is why both our houses tell
    stories of men who wore it falsely. At Tours it is a vow sworn like a soldier's oath; at Marseilles
    it is the undertaking whose goal and end order a whole life. "Deserter" is our word for the monk
    who leaves it.
  translational: >-
    'Did monks take formal vows, like a religious order today?' - not a canonical rite: a public
    undertaking of a whole way of life, with its own goal and end and its own "responsibility," sworn
    at Tours like a soldier's oath and betrayed as a soldier deserts, and capable of being assumed
    falsely "before the face of men."
quick_meaning: >-
  The monk's binding, public undertaking of a whole way of life. Sworn like a soldier's oath, and
  betrayed like a deserter.
distortion_risk: medium
---
Built from Doc_06 entry 019 (Tier 2; chunk galliclex019_profession.md; Doc_03 1.9). Register emic.
Quotations verified at locus by the build's own Doc_06 pass; not re-read here.

Related-Terms also names Sarabaite, perseverance and the monk's dress - cross-batch at authoring
time, added as relations (typed associated-with) at the reconciliation pass once all 81 term records
existed.
