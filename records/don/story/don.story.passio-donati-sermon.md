---
id: don.story.passio-donati-sermon
world_id: don
record_type: story
schema_version: 2
status: draft
register: emic
canon_cells: []
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Contested
  divergence_note: Formation_confidence held at Contested, not Documented, because the sermon's own authorship
    and precise date are reported from two disagreeing vendored authorities (Mabillon, c. 340, no author;
    Monceaux, 317/320, possibly Donatus the Great) that this record does not resolve between (Story-Chunks/donstory001,
    Tier Justification; Doc_02 SS4, SS8).
sources:
- source_id: don.source.passio-donati-sermon
  locus: the whole sermon; cic/texts/monumenta-vetera-donatistarum_migne-pl8.txt, lines 88-664
  license: public-domain
- source_id: don.source.monceaux-histoire-litteraire-tome5
  locus: the Passio Donati chapter's own dating/authorship argument, contested against Mabillon's apparatus
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - participant asks how this community commemorates its own dead or marks anniversaries of persecution
  - participant asks whether this community has liturgical practices distinct from the Catholic mainstream
  - participant asks what being formed by martyrdom felt like from the inside, rather than as an outside
    description
  do_not_retrieve_when:
  - participant is asking for a neutral historical narrative of who did what to whom at a specific dated
    event (don.story.acta-purgationis-felicis or don.story.council-of-cirta serve that need more precisely)
  - the conversation needs a story with a securely named, undisputed author
relations:
- type: associated-with
  target: don.figure.caecilian
- type: associated-with
  target: don.figure.donatus
narrative_tier: 3
narrative_tier_justification: 'Tier 3 (Doc_09 SS3): authorship is genuinely contested between two vendored
  authorities -- Mabillon dates the persecution to c. 340 without naming an author; Monceaux dates it
  to 12 March 317 (composed c. 320) and proposes, without asserting as settled, that the preacher was
  Donatus the Great himself -- which rules out Tier 1''s own named-author requirement outright. It is
  a single sermon, not a collected anthology, so Tier 2 does not fit either. Tier 3 is the precise fit:
  material ''attributed to specific figures or moments but resting on collected tradition,'' and the strongest
  evidence for that fit is the annual commemoration itself, independently attested by the sermon''s own
  words (''in solemni et anniversaria commemoratione'') regardless of who first delivered it (Story-Chunks/donstory001,
  Tier Justification).'
tellable_as: The sermon read every year at the martyrs' own grave, remembering what was done at Carthage
  in the name of unity
text: 'Every year, on the twelfth of March -- "the fourth of the Ides of March," in the sermon''s own
  reckoning -- this community gathers to remember what was done at Carthage in the name of unity.


  The account it tells is not soft. Imperial agents -- Leontius, a count, and Ursatius, a duke -- came
  under orders to enforce a single church, with the bishop Caecilian and the tribune Marcellinus standing
  behind them. Soldiers seized a basilica. What had been a house of prayer became, in the sermon''s own
  bitter phrase, a place of feasting and license. A boy, a catechumen not yet baptized, lay dying inside
  it and begged those around him for help. Whether he received what he asked is not the point the sermon
  lingers on; that he asked it, in that place, at that hour, is.


  A bishop named Honoratus of Sicilibba felt a tribune''s sword graze his throat and lived. Others did
  not. The sermon says they were killed inside the basilica itself -- not by the sword, but by clubs,
  while they knelt at prayer with their eyes closed, trusting the ground they stood on. Every age, every
  sex, the account insists. They were buried where they fell, within the building''s own walls, because
  there was nowhere else and no one to stop it. A bishop arriving from Advocata to see what was happening
  was killed before he could so much as drink water offered to him.


  This is what is read aloud, every twelfth of March, to a congregation that was not there and cannot
  verify every particular -- and reads it anyway, because the day itself is how this community has chosen
  to keep faith with what it believes happened to its own.'
absent_detail: This sermon's own precise date and author are not established -- Mabillon and Monceaux
  disagree by two decades and do not agree on an author at all. No established published English translation
  of the sermon exists (it survives only in raw, uncorrected Latin OCR); this record follows Story-Chunks/donstory001's
  own discipline of rendering the narrative in indirect, reported form for this reason, rather than presenting
  an uncertified translation as a verbatim quotation.
modern_contrast: A modern reader tends to think of a religious anniversary as a private, optional observance
  one can skip a year without consequence. This sermon's own community treated the twelfth of March as
  a mandatory, communal act of formation -- a day the whole community was expected to keep, together,
  aloud, not a private choice -- and it is that yearly repetition, not any one person's private memory,
  that kept a persecution decades past from becoming merely historical.
---
Mapped directly from Story-Chunks/donstory001_passio-donati-sermon.md's own Retrieval Front-Matter, Story Text, Tier Justification, and Usage Guidance sections, per this step's own field-mapping instruction. absent_detail and the indirect-speech rendering of the boy's cry and Honoratus's own wounding both preserve the chunk's own explicit certified-translation caveat rather than upgrading it. The contested authorship candidacy of Donatus the Great is carried into relations[] (don.figure.donatus) as an association, not an attribution -- the chunk's own Usage Guidance is explicit that 'the Representative should not attribute this sermon to Donatus the Great as settled fact.'
