---
id: don.story.passio-marculi
world_id: donatism
record_type: story
schema_version: 2
status: draft
register: emic
canon_cells:
- F6-E
- F1-P
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Contested
  divergence_note: 'Contested for the formation portrait; Inferential-Thin for the visionary and miraculous
    details specifically, which are offered as the tradition''s own testimony and never as verified events.
    The bare fact of Marculus''s death under Macarius is corroborated from two separate hostile directions
    - Optatus argues the deaths were deserved punishment for schism, and Augustine, separately and on a
    different question, disputes whether they qualify as martyrdom at all - but neither hostile writer
    accepts our own account of what happened, so the corroboration covers the killing and nothing beyond
    it. The Passio''s own heading gives a day and no year: the 347-348 Macarian dating rests on the standard
    field literature, not on the text.'
sources:
- source_id: don.source.passio-marculi
  locus: cic/texts/monumenta-vetera-donatistarum_migne-pl8.txt, lines 664-1359 (the Passio entire)
  license: public-domain
- source_id: don.source.optatus-against-the-donatists
  locus: cic/texts/optatus_against-the-donatists.txt, lines 2064-2096 - the argument against the alleged
    Donatist martyrs
  license: public-domain
- source_id: don.source.augustine-answer-to-petilian
  locus: Answer to the Letters of Petilian II.45-46 - the separate dispute over whether the deaths were
    self-sought
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - participant asks what dying well means among us, or what a martyr's death was believed to look like
  - participant asks about the Macarian persecution of 347-348
  - participant wants our fullest account in the hagiographic register, as against the more documentary
    don.story.macrobius-letter
  prefer_instead:
  - participant wants a minimally embellished account of the same persecution - don.story.macrobius-letter
    has a named author writing close to the events
  - participant is testing whether the rival communion accepted these deaths as martyrdom; it did not,
    and that contest needs naming before this story is told
relations:
- type: associated-with
  target: don.figure.marculus
- type: associated-with
  target: don.figure.optatus-of-milevis
- type: associated-with
  target: don.figure.augustine
narrative_tier: 3
narrative_tier_justification: 'Tier 3, and the closest thing in our corpus to that tier''s textbook case.
  Tier 3 names hagiographic narrative as a specific type within it - the idealized portrait, the miracle
  sequence, the death as completion of a formed life - and all three markers are present in full: a man
  who had already renounced worldly advancement before the persecution arrived; the visionary cup, crown
  and palm, the unbroken fall, the guiding light; and the vision shown before the death and then delivered
  exactly as shown. Tier 1 is ruled out because the account is anonymous, without the named author and
  identifiable social location Tier 1 requires. The tier''s own confidence rule is applied rather than
  waived: the general portrait carries Contested confidence, corroborated even by hostile witnesses for
  the bare fact of the killing; the visionary and miraculous details carry Inferential-Thin confidence.
  The formation ideal is the evidence here. The cliff-top vision is not.'
tellable_as: Marculus is shown a cup, a crown and a palm four days before he is thrown from a cliff - and
  the tradition says his body came down gently and a light settled over the place until the brethren found
  him.
text: >-
  We remember Marculus as a man who had already given up what the world
  offers before persecution ever reached him - a life of unusual virtue, a
  refusal of worldly advancement, given instead to the church.

  When Macarius's persecution came into Numidia, ten bishops were sent
  either to persuade Marculus's own community to submit or, as the
  tradition tells us happened, to join the resistance themselves instead.
  Marculus was seized at a place called Vegesela. He was bound to columns
  and flogged, and - so the account insists - bore it without visible
  pain, praising God the whole time, as though the whips could not reach
  the part of him that mattered. He was paraded through several Numidian
  towns as a spectacle, then held for four days at a cliff called
  Novapetra.

  In that waiting, the account says, he fasted, and was given a vision: a
  cup, a crown and a palm, shown to him together, the way we remember
  such things being shown to those about to complete a formed life.
  Before dawn he was thrown from the cliff. The tradition holds that his
  body did not break on the fall - that it descended gently, as though
  something were carrying it down rather than dropping it - and that a
  light settled over the place afterward, bright enough that the brethren
  could find him and take him for burial before anyone could stop them
  and deny it.

  This is how we remember Marculus: not as a man who died, but as a man
  shown, in advance, what completing his own formation would look like,
  and then given exactly that.
absent_detail: The Passio names no author and gives no year - only a day. Nothing survives of what Marculus
  himself said under interrogation in his own words, and no independent witness confirms the vision, the
  fall, or the light. What the hostile record supplies is only that he was killed, and an argument about
  whether that killing counts.
modern_contrast: >-
  A modern reader is likely to hear the vision, the unbroken body and the
  light as claims about what a camera would have recorded, and to weigh
  the story by whether they are believable. That is not the weight the
  account was built to carry. It was written to show a community what a
  finished life looks like - the death as the completion of something
  already underway, not as an interruption of it. The events are disputed
  even in our own century's record; the ideal is not, and the ideal is
  what the text was for.
---
Compiled from World-Builds/Donatism/Story-Chunks/donstory002_passio-
marculi.md (Doc_09 story index row donstory002, Tier 3), whose narrative
text is carried forward rather than re-derived.

THE TWO HOSTILE WITNESSES DISPUTE DIFFERENT THINGS AND MUST NOT BE
MERGED. It is not a citation chain: Optatus
argues, on the model of Phineas, Moses and Elijah, that the deaths were
deserved punishment for schism - conceding the killing; Augustine
separately argues, on the different question of whether the men threw
themselves down or were thrown, that the label martyrdom does not apply.
Two authors, two arguments, two works, as carried in sources[] above.

ANOTHER DONATUS, NOT DONATUS THE GREAT. Optatus's passage argues about
"the deaths of Marculus and Donatus" together. Which Donatus that is, is
not resolved here and is not asserted; the story text above deliberately
does not name him, and don.figure.donatus does not claim him.

THE DATING IS THE FIELD'S, NOT THE TEXT'S - don.core.donatism cautions
item 6. The Passio's own heading reads "INCIPIT PASSIO BENEDICTI
MARTYRIS MARCULI. 8 (al. die 5) kal. decembris" - a day only. The
"ANNO DOMINI 348" printed above the catalogue entry is the volume's own
dated section marker, and the descriptive rubric calling Marculus a
Donatist priest is Mabillon's and Migne's, not the Passio's self-
description.
