---
id: alx.term.allegoria
world_id: alexandria-catechetical
record_type: term
schema_version: 2
status: draft
register: emic
canon_cells:
- F2-I
- F2-T
- F2-P
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: corroborating
  formation_confidence: Widely Accepted
  divergence_note: null
sources:
- source_id: alx.source.origen-philocalia
  locus: I
  license: public-domain
- source_id: alx.source.clement-stromateis
  locus: passim
  license: public-domain
- source_id: alx.source.eusebius-historia-ecclesiastica
  locus: "VII.24 (Nepos's Refutation of Allegorists and Dionysius's three-day disputation at Arsinoe)"
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - how they read Scripture
  - Genesis/science and difficult-passage questions
  do_not_retrieve_when: []
relations:
- type: associated-with
  target: alx.quote.no-sun-no-moon-no-sky
- type: associated-with
  target: alx.gravity.scripture-formative
- type: associated-with
  target: alx.contested.allegory-from-within
plain_meaning: 'Reading Scripture at more than one level: the plain sense, and deeper senses about Christ
  and the soul.'
world_word: allegoria (the spiritual sense)
false_friend:
- making the text mean anything you like
- denying that events happened
senses:
  informational: 'The conviction that Scripture, like a person, has body, soul, and spirit: a plain sense
    and deeper senses, given by God so every reader is met at their depth.'
  evidential: Origen's own statement of the method survives in Greek in the Philocalia; the practice is
    visible across the commentaries. It was contested even inside Egypt - Nepos wrote against it, and
    Dionysius answered with three days of open argument, not decree.
  personal: 'A hard or strange passage was not a wall but an invitation: the difficulty itself was read
    as God''s teaching.'
  translational: '''Did you read Genesis as science?'' - no; this world read it for what it says of God,
    Christ, and the soul, and thought the plain-only reading the shallow one.'
quick_meaning: Reading Scripture for its deeper senses as well as the plain one.
distortion_risk: high
---
CONTEST (stated, per the lexicon discipline): contested from WITHIN
Egyptian Christianity (alx.contested.allegory-from-within - Nepos).
Modern hearing: 'reading into the text.'
World hearing: reading all the way down. Author-gravity: the
systematized method is Origen-concentrated (the standing flag).

corrected 2026-09-08, records/alx audit: the evidential claim ("Nepos
wrote against it, and Dionysius answered with three days of open
argument, not decree") was cited only to Philocalia I and Stromateis
passim, neither of which carries this episode; it is Eusebius, HE
VII.24, now added to sources at that locus - "sitting with them from
morning till evening for three successive days, I endeavored to
correct what was written in it." The closing note's "and from outside
(Porphyry)" had no vendored source in this corpus discussing Porphyry's
critique of allegorical reading (checked across cic/texts/*.xml and
*.txt) and has been removed rather than left uncited. The Philocalia I
claim itself was found clean and is unchanged.
