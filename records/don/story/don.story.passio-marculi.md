---
id: don.story.passio-marculi
world_id: don
record_type: story
schema_version: 2
status: draft
register: emic
canon_cells:
- F5-P
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Contested
  divergence_note: General portrait Contested (corroborated even by hostile Optatus/Augustine material
    that the death occurred); specific visionary and miraculous detail Inferential-Thin, per Tier 3's
    own confidence rule (Story-Chunks/donstory002, Tier Justification).
sources:
- source_id: don.source.passio-marculi
  locus: the whole Passio; cic/texts/monumenta-vetera-donatistarum_migne-pl8.txt, lines 664-1359
  license: public-domain
- source_id: don.source.optatus-against-donatists
  locus: '''Against the alleged Donatist martyrs,'' arguing the deaths deserved punishment for schism'
  license: public-domain
- source_id: don.source.augustine-answer-to-letters-of-petilian
  locus: II.45-46, disputing whether the deaths qualify as martyrdom
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - participant asks what a martyr's death was believed to look like, or what dying well meant within
    this tradition
  - participant asks about the Macarian persecution (347-348) specifically
  - conversation needs this tradition's own fullest hagiographic-register account, distinct from the more
    documentary don.story.macrobius-letter-isaac-maximianus
  do_not_retrieve_when:
  - participant wants a historically cautious, minimally-embellished account of the same persecution (don.story.macrobius-letter-isaac-maximianus
    serves that need)
  - participant is asking whether the Catholic side accepted this as genuine martyrdom (it did not, on
    two separate grounds)
relations:
- type: associated-with
  target: don.figure.marculus
- type: associated-with
  target: don.story.macrobius-letter-isaac-maximianus
narrative_tier: 3
narrative_tier_justification: 'Tier 3 (Doc_09 SS3): anonymous, near-contemporary composition carrying,
  in textbook form, the three markers Tier 3''s own definition names for hagiographic narrative -- the
  miracle sequence (the cup/crown/palm vision, the unbroken fall, the guiding light), the idealized portrait
  (a man who had already renounced worldly advancement before persecution arrived), and the death as completion
  of a formed life (the vision shown before the death, then delivered exactly as shown). The general portrait
  (that Marculus died at Macarius''s hands, resisting a persecution operation) is Contested-confidence,
  corroborated even by the hostile Optatus/Augustine material; the specific visionary and miraculous details
  are Inferential/Thin, per Tier 3''s own confidence rule for genre-shaped detail (Story-Chunks/donstory002,
  Tier Justification).'
tellable_as: Marculus's own death at the cliff of Novapetra, shown in advance what completing a formed
  life would look like
text: 'The tradition remembers Marculus as a man who had already given up what the world offers before
  persecution ever reached him -- a life of unusual virtue, a refusal of worldly advancement, given instead
  to the church.


  When Macarius''s persecution came into Numidia, ten bishops were sent either to persuade Marculus''s
  own community to submit or to join the resistance themselves instead. Marculus was seized at a place
  called Vegesela. He was bound to columns and flogged, and the tradition insists he bore it without visible
  pain, praising God the whole time. He was paraded through several Numidian towns as a spectacle, then
  held for four days at a cliff called Novapetra.


  In that waiting, the tradition says, he fasted, and he was given a vision: a cup, a crown, and a palm,
  shown to him together, the way the community remembers such things being shown to those about to complete
  a formed life. Before dawn, he was thrown from the cliff. The tradition holds that his body did not
  break on the fall, and that a light settled over the place afterward, bright enough that the brethren
  could find him and take him for burial before anyone could stop them.


  This is how the tradition remembers Marculus: not as a man who died, but as a man shown, in advance,
  what completing his own formation would look like -- and then given exactly that.'
absent_detail: 'The cliff-top vision, the unbroken fall, and the guiding light are the tradition''s own
  testimony to what it believed formation produced, not a claim about what a modern observer would have
  seen. The hostile Catholic side does not accept this death as martyrdom at all, on two separate grounds:
  Optatus argues the deaths were deserved punishment for schism; Augustine, separately, disputes whether
  Marculus was thrown or threw himself.'
modern_contrast: A modern reader tends to assume a 'miracle account' and a 'documentary account' of the
  same event are mutually exclusive registers -- one credulous, one reliable. This world's own corpus
  places both side by side, deliberately, about the same 347-348 persecution (this story and don.story.macrobius-letter-isaac-maximianus),
  treating them as different kinds of evidence for different kinds of claims rather than competing versions
  of one truth.
---
Mapped directly from Story-Chunks/donstory002_passio-marculi.md. The corroborating-but-disputing hostile sources (Optatus, Augustine) are carried in sources[] exactly as the chunk's own Source field lists them, not smoothed into a single citation.
