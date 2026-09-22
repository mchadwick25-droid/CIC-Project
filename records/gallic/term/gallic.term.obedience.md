---
id: gallic.term.obedience
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F2-P
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: corroborating
  formation_confidence: Documented
  divergence_note: >-
    Weighted to Cassian: the ranking ("before all virtues") and the exempla are Egypt's; whether any
    Gallic house tested juniors by contrary orders is not documented. Sulpitius shows the disposition in
    Martin's presence without the word or any command. The Patermucius story must be rendered as the
    world held it - "the deed of Abraham" - with the analyst's judgment kept outside the voice. The
    Latin lemma is not supplied against the text.
sources:
- source_id: gallic.source.cassian-institutes
  locus: 'Institutes IV.8 ("to teach him first to conquer his own wishes"; "contrary to his liking"); IV.10; IV.12 ("even before all virtues"); IV.23-26 (Abbot John, "the grace of prophecy," the dry stick "for a whole year," "this cruse of oil"); IV.27-28 (Patermucius, "into the river," "the deed of Abraham"); IV.29 (the count''s son, ten baskets, "the true nobility"); IV.30 ("holds the first place"); II.3 (presiding after obedience)'
  license: public-domain
- source_id: gallic.source.sulpitius-vita-martini
  locus: 'Life of St. Martin ch. XXV ("the authority he unconsciously exerted, that I deemed it unlawful to do anything but acquiesce")'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - what a monk had to obey, or whether obedience was absolute
  - why elders gave absurd commands, or whether the Patermucius story is abuse
  - participant uses "obedience," "obey," "authority," "submission," or "blind obedience"
  - John watering the dry stick, the cruse of oil, the boy at the river, the count's son with his baskets, or Sulpitius at Martin's table
  prefer_instead:
  - whom one obeys as an office (retrieve elder / senior / abbot)
  - obedience to bishops or councils (retrieve bishop / the monk-bishop, council / synod)
  - free will in the grace argument as such (retrieve free will)
relations:
- type: associated-with
  target: gallic.term.example-imitation
- type: associated-with
  target: gallic.term.customs-of-the-monasteries
- type: associated-with
  target: gallic.term.free-will
- type: associated-with
  target: gallic.term.cell
- type: associated-with
  target: gallic.term.elder-senior-abbot
- type: associated-with
  target: gallic.term.junior-novice
- type: associated-with
  target: gallic.term.disciple-master
- type: associated-with
  target: gallic.term.discretion
- type: associated-with
  target: gallic.term.disclosure-of-thoughts
- type: associated-with
  target: gallic.term.grace-as-charism
- type: associated-with
  target: gallic.term.penance-satisfaction
- type: precondition-for
  target: gallic.term.humility
plain_meaning: >-
  For us obedience is the virtue the Egyptians "put not merely before manual labour and reading and
  silence and quietness in the cell, but even before all virtues." It is proved by absurd and terrible
  commands - a dry stick watered for a year, a son carried to the river - and it is the first thing a
  junior learns, "to conquer his own wishes." At Tours it is what Sulpitius feels before Martin:
  "unlawful to do anything but acquiesce."
world_word: obedience
false_friend:
- blind obedience as the suppression of conscience
- the dry stick and the river as abuse or cult control
- institutional discipline enforced by rule
senses:
  informational: >-
    The Egyptians "endeavour with the utmost earnestness and zeal to attain the virtue of obedience,
    which they put ... even before all virtues." It begins on the first day: the dean will "teach him
    first to conquer his own wishes; and ... he will of set purpose contrive to give him such orders as
    he knows to be contrary to his liking." Then the stories. Abbot John, told to water a dry stick
    twice a day, "had continued for a whole year"; told to throw the only cruse of oil in the desert
    out of the window, he "threw it out of window and cast it down to the ground and broke it in
    pieces without any thought or consideration." Patermucius, told to throw his little boy into the
    river, "as if this had been commanded him by the Lord, at once snatched him up and carried him in
    his arms to the river's bank," and it was revealed to the Abbot "that he had done the deed of
    Abraham." A count's son hawks ten baskets through the streets, "gaining through the grace of
    obedience that humility of Christ which is the true nobility." At Tours the word is scarcely used
    and the thing is felt: Sulpitius, given the place of honour at Martin's table, "felt so overcome
    by the authority he unconsciously exerted, that I deemed it unlawful to do anything but
    acquiesce."
  evidential: >-
    Cassian (Institutes II.3, IV.8-30), Egyptian practice by his framing; Sulpitius (Life ch. XXV) for
    the disposition at Tours. No one at Marmoutier is given contrary orders in what was read. Gallic
    testing of juniors by contrary orders is undocumented.
  personal: >-
    Obedience is how our will is broken to the elders' judgment, and its reward is grace: John "was
    exalted even to the grace of prophecy for his admirable obedience." An absurd command is a kindness
    among us, and the man who wants to command has already failed - no one may preside "before he has
    ... learnt by obedience what he ought to enjoin."
  translational: >-
    'Isn't the story of the father carrying his child to the river simply abuse - blind obedience
    enforced by a cult?' - we read it as "the deed of Abraham," and the point of orders "contrary to
    his liking" was the conquest of one's own wishes, whose reward was grace; at Tours no command was
    given at all, and disobedience still felt "unlawful" before an authority "unconsciously exerted."
quick_meaning: >-
  The first of all virtues, learned by orders "contrary to his liking" - the conquest of one's own
  wishes, rewarded with grace. At Tours, an authority felt without any command.
distortion_risk: high
---
Built from Doc_06 entry 031 (Tier 2; chunk galliclex031_obedience.md; Doc_03 3.9). Register emic.
Quotations verified at locus by the build's own Doc_06 pass; not re-read here. The relation to
humility is typed precondition-for, per Inst. IV.29 ("through the grace of obedience that humility of
Christ"). Canon cell F2-P: the Patermucius story is exactly the kind of text a participant finds
frightening, and this record's "the deed of Abraham" reading is this world's own answer to whether it
troubled us.

Related-Terms also names grace as charism - cross-batch at authoring time, added as relations (typed
associated-with) at the reconciliation pass once all 81 term records existed.
