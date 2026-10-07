---
id: syr.term.ewangeliyon-da-mhallete
world_id: syriac-edessa-nisibis
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F2-I
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: null
sources:
- source_id: syr.source.diatessaron-arabic-harmony
  locus: whole harmony (the tradition's shape)
  license: public-domain
- source_id: syr.source.aphrahat-select-demonstrations
  locus: Gospel citations passim
  license: public-domain
- source_id: syr.source.petersen-diatessaron
  locus: the standard survey
  license: in-copyright-consultation
retrieval:
  tier: 2
  retrieve_when:
  - participant asks what 'the Gospel' meant in this world - four books or one
  - participant asks about the Diatessaron by name
  - Aphrahat's or Ephrem's Gospel text comes up
  prefer_instead:
  - participant asks about the Peshitta - a later standard text, not this world's own vocabulary
relations:
- type: associated-with
  target: syr.gravity.diatessaron-normative
- type: associated-with
  target: syr.term.raza-shrara
- type: associated-with
  target: syr.contested.diatessaron-name
plain_meaning: 'The ''Gospel of the Mixed'': the one continuous Gospel story we read and heard
  in worship. Tatian wove the four accounts into a single narrative around 172. For some two hundred years,
  ''the Gospel'' in our churches meant that one unfolding story, not four separate books.'
world_word: Ewangeliyon da-Mhallete
false_friend:
- the four Gospels (the plural, four-witness canon experience)
- a surviving book (the harmony survives only in fragments and translations)
senses:
  informational: The harmonized single-narrative Gospel (Tatian's Diatessaron, c. 172) that served as
    the standard lectionary text of Syriac-speaking churches through this world's whole window - Aphrahat
    quotes it; Ephrem wrote a commentary on it.
  evidential: The harmony's content and use are well attested; the text itself survives only indirectly
    (commentary, translations, disputed fragments). Whether the Syriac name 'da-Mhallete' was in use within
    the window is genuinely unresolved - Ephrem himself just says 'the Gospel'.
  personal: To hear the Gospel here was to hear one unbroken story of Jesus from beginning to end - a
    different formation than weighing four witnesses against each other.
  translational: '''Was your Bible the same as ours?'' - the Scriptures largely yes, but the Gospel came
    as one woven narrative, not four books; the four ''separated'' Gospels displaced it only after this
    world''s window closed.'
quick_meaning: The one woven Gospel story we read in worship. The four accounts were joined into
  a single telling, and people simply called it 'the Gospel'.
distortion_risk: medium
use_note:
  means: "Ewangeliyon da-Mhallete, the Gospel of the Mixed, is Tatian's harmonized single-narrative Gospel, the standard Gospel text of Syriac-speaking churches throughout this world's window."
  not_for:
    - "a claim that this world read four separate Gospels or used the Peshitta"
    - "a claim that the Syriac name da-Mhallete is securely attested within the window"
    - "a claim that the harmony survives as an intact book"
  years: {from: 200, to: 410}
  status: reviewed
---
A Tier 2, CT-tagged entry. The CT contest (the vernacular name's
earliest secure attestation is unresolved - Theodoret's Greek account
vs the Syriac Eusebius gloss, per Crawford) is carried in the
evidential sense and in syr.contested.diatessaron-name. Peshitta stays
excluded as a term (name first attested with Moses bar Kepha, d. 903);
the Diatessaron-to-Peshitta transition itself is handled in
syr.contested.rabbula-peshitta and the ending forces.
