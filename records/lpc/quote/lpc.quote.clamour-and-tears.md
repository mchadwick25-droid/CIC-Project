---
id: lpc.quote.clamour-and-tears
world_id: latin-pastoral-congregational-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F3-I
use_note:
  means: "Possidius says a crowd at Hippo seized Augustine and loudly told their bishop to make him a priest, while he wept."
  not_for:
    - "a claim that it was an orderly election"
    - "a claim that it describes Augustine's later consecration as bishop"
    - "a claim that Possidius, Augustine's friend, writes as an uninvolved witness"
    - "a claim that it describes a sermon at Hippo or the years 258 to 391"
  years: {from: 391, to: 391}
  status: reviewed
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: The vendored Weiskotten scan carries a single OCR artifact inside this quotation --
    'ancf' for 'and' -- reproduced here exactly as the scan gives it (matching this record's own text
    against the raw file precisely, per this step's own discipline), not silently corrected; modern_rendering
    gives the plain sense ('they demanded it...') rather than reproducing the artifact.
sources:
- source_id: lpc.source.possidius-vita-augustini-weiskotten1919
  locus: Vita Augustini IV; cic/texts/possidius_vita-augustini_weiskotten1919.txt, lines 1808-1817
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - participant asks how Augustine came to be ordained
  - participant asks how a crowd at Hippo drew Augustine into the priesthood against his will
  - participant asks whether a congregation at Hippo claimed a man for office the way Carthage claimed Cyprian
  - participant asks whether a man could be made a priest against his will
  prefer_instead:
  - participant wants Augustine's own later account of the same event in his own words -- this quote is
    Possidius's own narration; Augustine's own first-person account survives separately (Sermo CCCLV)
    and is named in this record's own body, not quoted here as the record's own text
claim_guards: []
relations:
- type: associated-with
  target: lpc.story.the-psalms-on-the-wall
- type: associated-with
  target: lpc.figure.possidius
- type: associated-with
  target: lpc.figure.augustine
text: The Catholics, already acquainted with the life and teaching of the holy Augustine, laid hands on
  him — for he was standing there among the people secure and unaware of what was about to happen... So
  they laid hands on him and, as is the custom in such cases, brought him to the bishop to be ordained,
  for all with common consent desired that this should be done and accomplished ; ancf they demanded it
  with great zeal and clamor, while he wept freely.
speaker_or_author: lpc.figure.possidius
license: verbatim
modern_lens_note: 'A modern listener may hear ''they demanded it with clamor'' and picture an orderly
  election. Possidius describes something closer to a seizure: a congregation physically laying hands
  on a man standing unaware among them and refusing to let him leave until the ordination was done, while
  he wept -- the same congregational-acclamation pattern lpc.story.election-of-cyprian shows for Cyprian,
  a century and a half earlier, recurring at Hippo for Augustine.'
modern_rendering: The Catholics already knew the life and teaching of the holy Augustine, and they seized
  him. He was standing there among the people, feeling safe and unaware of what was about to happen...
  So they seized him and, as is the custom in such cases, brought him to the bishop to be ordained. They
  did this because all of them, with one accord, wanted it done and carried through. They demanded it
  with great eagerness and loud shouting, while he wept freely.
---
The passage is Vita Augustini IV, Augustine's ordination as presbyter in 391, at cic/texts/possidius_vita-augustini_weiskotten1919.txt, lines 1808-1817. The ellipsis marks the omitted sentence about Augustine avoiding churches that had no bishop. This chapter lies outside the passages lpc.story.the-psalms-on-the-wall cites (SSSS28-29 and SS31). The edition's endnote also quotes Augustine's own first-person account, Sermo CCCLV i 2: 'Apprehensus presbyter factus sum, et per hunc gradum perueni ad episcopatum' ('I was seized and made a presbyter, and through this step I arrived at the episcopate'), at lines 5203-5204. It corroborates Possidius but is not this record's text, which stays Possidius's own narration.
