---
id: alx.quote.dionysius-nepos
world_id: alexandria-catechetical
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F6-I
- F1-E
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Documented
  divergence_note: null
sources:
- source_id: alx.source.eusebius-historia-ecclesiastica
  locus: 'VII.24 (npnf201 lines 41310-41318; Dionysius''s own book On the Promises, quoted
    verbatim, matching the text field below)'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how a disagreement inside the community was handled"
  - "participant asks whether a bishop could disagree with a respected teacher and stay friends"
  - "participant asks who settled a dispute about how to read a book"
relations:
- type: associated-with
  target: alx.story.arsinoite-conference
text: in many other respects I approve and love Nepos, for his faith and industry and diligence in the Scriptures, and for his
  extensive psalmody, with which many of the brethren are still delighted; and I hold him in the more
  reverence because he has gone to rest before us. But the truth should be loved and honored most of all.
modern_rendering: >-
  In many other respects I approve of Nepos and love him. I do so for his
  faith, his hard work and his diligence in the Scriptures, and for his
  many psalms. Many of our people still delight in them. And I hold him in
  all the more reverence because he has gone to his rest before us. But
  the truth must be loved and honored most of all.
speaker_or_author: alx.figure.dionysius
license: verbatim
modern_lens_note: >
  Mild risk: 'brethren' is this translation's period-standard rendering for
  the whole community (not literally 'brothers' to the exclusion of women) - a
  modern reader may misread it as gendered. 'Psalmody' (the singing/composing
  of psalms) is a slightly unusual word but self-explanatory in context.
use_note:
  means: "Dionysius of Alexandria, quoted by Eusebius at VII.24, says he loves the late bishop Nepos for his faith and psalmody but loves truth more."
  not_for:
    - "a neutral account of Nepos's teaching, when the speaker is the bishop refuting it"
    - "a claim that Dionysius conceded Nepos's reading, when he is refuting it"
    - "the conference in the Arsinoite villages itself, which sits in alx.story.arsinoite-conference"
  years: {from: 248, to: 264}
  status: reviewed
reading_card:
  setting: Dionysius, bishop of Alexandria, in his book On the Promises, quoted by Eusebius.
  source_says: Nepos taught an earthly reign of Christ. Dionysius praises the dead bishop, then says unsound
    writing must be examined and corrected.
  historians_conclude:
    text: The construction record holds that allegory ruled the literate Alexandrian tradition but was
      disputed inside Egypt.
    confidence: Contested
  contributes: 'It shows disagreement handled inside the household: love the man, argue the teaching.'
  whose_view: The refuting bishop speaks; Nepos's book is lost and known only through him.
  open: His words are filtered twice, by himself and by Eusebius. 'I confess that' is the translator's.
  reads_differently_today: '''Brethren'' is this translation''s word for the whole community, women included.
    ''Psalmody'' means singing or writing psalms.'
  complicated_by:
  - alx.contested.allegory-from-within
  sources:
    setting: alx.source.eusebius-historia-ecclesiastica, HE VII.24.1-3, npnf201 lines 41285-41300
    source_says: alx.source.eusebius-historia-ecclesiastica, HE VII.24.1-5, npnf201 lines 41285-41330
    historians_conclude: alx.contested.allegory-from-within, concedes; Build/worlds/alx/Doc_05_Ecological_Reconstruction.md
      §6.4 construction note
    contributes: alx.term.allegoria; alx.gravity.scripture-formative
    whose_view: npnf201 editor's note at line ~41297 ('This work of Nepos has entirely perished'); alx.story.arsinoite-conference,
      absent_detail
    open: 'Build/worlds/alx/Doc_02_Source_Ecology.md §3.6 (Dionysius: doubly mediated); npnf201 endnote
      at line 41310'
    reads_differently_today: alx.quote.dionysius-nepos, modern_lens_note
---
How this world disagreed inside the household: love the man, honor the
truth more. Spoken about Nepos, the Egyptian bishop whose Refutation of
Allegorists Dionysius answered (see alx.contested.allegory-from-within
and alx.story.arsinoite-conference). Serves F6-I (what troubled/
never settled) and F1-E (who had the right to decide - and how it was
actually done). Verified verbatim.

The vendored edition's own endnote at this point (npnf201, line 41310)
reads "The words 'I confess that' are not in the original, but the
insertion of some clause of the kind is necessary to complete the
sentence" - i.e. the edition itself disclaims those three words as
translator supply, not Dionysius's own wording, even though they are
printed inline. On a license: verbatim record attributed to Dionysius by
name, that disclaimed clause is excluded, matching how this registry
already excludes bracketed/footnoted editorial supply elsewhere. The
text field opens at "in many other respects," which IS genuine vendored
translation (line 41312) and carries the qualifier by which Dionysius
limits his approval - the substantive point this record exists to
preserve. Locus range 41310-41318 is kept (41310 is where the
disclaiming endnote sits, useful context for anyone checking the locus).
