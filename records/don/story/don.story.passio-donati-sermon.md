---
id: don.story.passio-donati-sermon
world_id: donatism
record_type: story
schema_version: 2
status: draft
register: emic
canon_cells:
- F3-I
- F6-E
confidence:
  citation_specificity: B
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Contested
  divergence_note: 'Contested for the general portrait and for the twelfth-of-March commemorative practice;
    Inferential-Thin for the sermon''s own authorship and precise date, which two vendored authorities
    resolve differently and neither of which is adopted here. Mabillon''s editorial heading dates the persecution
    circa 340 and names no author; Monceaux dates the events to 12 March 317 with composition circa 320,
    argues the preacher was an eyewitness and the Donatist bishop of Carthage, and floats - without asserting
    - that this could have been Donatus himself. Never cite a settled date or author for this text. The
    text survives only in raw, uncorrected Latin OCR and no established published English translation was
    consulted; the two short phrases rendered here were checked against the underlying Latin and are close
    literal renderings, not certified translation.'
sources:
- source_id: don.source.passio-donati-sermon
  locus: cic/texts/monumenta-vetera-donatistarum_migne-pl8.txt, lines 88-664 (the sermon entire)
  license: public-domain
- source_id: don.source.monceaux-histoire-litteraire-tome5
  locus: the dedicated chapter treatment - the 12 March 317 dating, the eyewitness finding, and the authorship
    hypothesis
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - participant asks how we commemorate our own dead, or what we do on an anniversary
  - participant asks what being formed by martyrdom felt like from the inside rather than as a description
    from outside
  - participant asks whether we keep practices the rival communion does not
  do_not_retrieve_when:
  - participant wants a neutral dated narrative of who did what to whom (don.story.acta-purgationis-felicis
    or don.story.council-of-cirta serve that better)
  - participant needs a text with a securely named, undisputed author
relations:
- type: associated-with
  target: don.figure.caecilian
- type: associated-with
  target: don.figure.donatus
narrative_tier: 3
narrative_tier_justification: 'Tier 3, and the tier was argued rather than assumed. Tier 1 is ruled out
  because it requires a named author with an identifiable social location and a date held with reasonable
  confidence, and this sermon has none of the three: the two vendored authorities disagree by roughly two
  decades on the date and do not agree on the author at all. Tier 2 is ruled out on its own definition
  - it requires transmission in collected form with an identifiable collection history, and this is a single
  sermon, not an anthology, however often it was read aloud. Tier 3 fits exactly: material attributed to
  specific figures and a specific moment, resting on commemorative tradition rather than on direct documentation,
  and bearing a formation ideal that is itself the evidence. The annual repetition is the point. Whatever
  the sermon''s authorship and date, its own text attests that it was preached at a solemn and yearly commemoration,
  and that repetition - not the verifiability of each detail inside it - is what this story actually shows.'
tellable_as: Every twelfth of March we read aloud the account of a day soldiers took a basilica at Carthage
  in the name of unity, and killed people at prayer inside it.
text: >-
  Every year, on the twelfth of March - the fourth of the Ides of March,
  in the sermon's own reckoning - we gather to remember what was done at
  Carthage in the name of unity.

  The account we read is not softened. Imperial agents came under orders
  to enforce a single church: Leontius, a count, and Ursatius, a duke,
  with the bishop Caecilian and a tribune named Marcellinus standing
  behind them. Soldiers seized a basilica. What had been a house of
  prayer became, in the sermon's own bitter phrase, a place of feasting
  and licence. A boy, a catechumen not yet baptized, lay dying inside it
  and begged those around him - help me, a catechumen. Whether he
  received what he asked is not what the sermon lingers over. That he
  asked it, in that place, at that hour, is.

  A bishop named Honoratus of Sicilibba felt a tribune's sword graze his
  throat and lived. Others did not. The sermon says they were killed
  inside the basilica itself, not by the sword but with clubs, while they
  knelt at prayer with their eyes closed, trusting the ground they stood
  on. Every age, every sex, the account insists. They were buried where
  they fell, within the building's own walls, because there was nowhere
  else and no one to stop it. A bishop arriving from Advocata to see what
  was happening was killed before he could so much as drink the water
  offered him - the sermon calls this, with open irony, the hospitality
  Carthage gave him, and says he paid for it with his own blood.

  This is what is read aloud to us every twelfth of March: to a
  congregation that was not there and cannot check every particular, and
  reads it anyway, because the day itself is how we have chosen to keep
  faith with what we believe was done to our own.
absent_detail: The preacher does not name himself and the sermon does not date itself in a way two competent
  editors can agree on. Nothing survives from the other side of that day - no account by the soldiers,
  the count, the duke, or the bishop the sermon holds responsible - and no independent record of the deaths
  it narrates.
modern_contrast: >-
  A modern reader might expect a persecution account this specific to
  come from an inquest or a contemporary report. This one is a sermon,
  preached at an anniversary, written to be read aloud again the
  following year and the year after that. Its purpose was never to
  establish what happened for a stranger; it was to make the same
  conviction happen again in the hearing of people who already held it.
  That is a different kind of evidence, and a real one - but it is not
  the kind a modern reader reaches for first.
---
Compiled from World-Builds/Donatism/Story-Chunks/donstory001_passio-
donati-sermon.md (Doc_09 story index row donstory001, Tier 3), whose
polished narrative text is carried forward rather than re-derived.

TWO AUTHORITIES DISAGREE AND NEITHER IS ADOPTED - don.core.donatism's
own cautions item 5. Mabillon: persecution circa 340, no author named.
Monceaux: 12 March 317, composition circa 320, an eyewitness Donatist
bishop of Carthage as preacher, possibly Donatus, with Monceaux himself
hesitating on literary grounds because the sermon's tone does not
obviously match the haughty eloquence Optatus attributes to Donatus
later. The relation to don.figure.donatus above records that hypothesis
as a hypothesis; it must never be narrated as this text's settled
authorship.

THE DATE INSIDE THE STORY WAS ITSELF A CORRECTED ERROR. Doc_09's Round 1
review found the chunk's first draft had converted "a.d. IV Idus
Martias" as the fourth of March; the ordinary Roman convention gives
the twelfth, which Doc_02 and the Registry already carried correctly.
The corrected date is the one used here.

HOMONYM, FOUND AT THIS STEP AND NOT PREVIOUSLY FLAGGED ANYWHERE IN THIS
WORLD'S DOCUMENTS: the tribune Marcellinus named in this sermon is not
Flavius Marcellinus, the imperial tribune and notary who presided at the
411 Conference roughly a century later. Both are tribunes named
Marcellinus standing beside imperial coercion of this communion, which
is exactly the shape of confusion don.core.donatism's cautions item 7
already warns about for the two Maximians and the two Optatuses. See
don.figure.marcellinus, which carries the distinction.
