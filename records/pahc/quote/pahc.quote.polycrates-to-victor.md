---
id: pahc.quote.polycrates-to-victor
world_id: post-apostolic-house-church
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F3-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources:
- source_id: pahc.source.second-third-century-remains
  locus: 'Polycrates of Ephesus, from his Epistle to Victor and the Roman Church (anf08 line 72521; the
    passage at 72582), preserved in Eusebius HE V.24'
  license: public-domain
text: As for us, then, we scrupulously observe the exact day, neither adding nor taking away. For in
  Asia great luminaries have gone to their rest, who shall rise again in the day of the coming of the
  Lord... Moreover I also, Polycrates, who am the least of you all, in accordance with the tradition of
  my relatives, some of whom I have succeeded—seven of my relatives were bishops, and I am the eighth,
  and my relatives always observed the day when the people put away the leaven—I myself, brethren, I
  say, who am sixty-five years old in the Lord, and have fallen in with the brethren in all parts of
  the world, and have read through all Holy Scripture, am not frightened at the things which are said
  to terrify us. For those who are greater than I have said, "We ought to obey God rather than men."
modern_rendering: >-
  As for us, we scrupulously keep the exact day, adding nothing and
  taking nothing away. For in Asia great luminaries have gone to their
  rest, who shall rise again on the day the Lord comes. Moreover I also,
  Polycrates, the least of you all, follow the tradition of my
  relatives, some of whom I have succeeded. Seven of my relatives were
  bishops, and I am the eighth, and my relatives always observed the day
  when the people put away the leaven. I myself, brothers, am
  sixty-five years old in the Lord. I have fallen in with the brethren
  in all parts of the world, and have read through all Holy Scripture. I
  am not frightened by the things which are said to terrify us. For
  those who are greater than I have said: 'We ought to obey God rather
  than men.'
speaker_or_author: Polycrates, bishop of Ephesus, writing to Victor of Rome
license: verbatim
modern_lens_note: >-
  The dispute is over the date of the Passover: Asia kept it on the fourteenth day of the month
  whenever it fell, Rome always on a Sunday. "The things which are said to terrify us" is Victor's
  threat to cut Asia out of communion, which he then did. The quoted line is Acts 5:29, spoken by
  Peter to the Sanhedrin - Polycrates is answering Rome with the words the apostles used to the
  authorities that tried them.
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether churches in different places did things differently"
  - "participant asks what happened when Rome told another church it was wrong"
  - "participant asks how they worked out when to keep a feast"
relations:
- {type: illustrates, target: pahc.gravity.translocal-network}
- {type: illustrates, target: pahc.gravity.authority-consolidation}
---
Verified verbatim against the vendored file 2026-08-27 at anf08 line
72582. DISCLOSED, two elisions, both at clause or sentence boundaries:
after "coming of the Lord" the file continues "when He cometh with glory
from heaven and shall raise again all the saints," followed by the roll
of Asian dead - Philip and his daughters, John, Polycarp, Thraseas,
Sagaris, Papirius, Melito - and the sentence "These all kept the
passover on the fourteenth day of the month, in accordance with the
Gospel"; and the ANF's interleaved Greek glosses and bracketed editorial
notes are excluded throughout.

Quote-verbatim gate fix (2026-09-22): the `text` field itself carried neither disclosed elision as an
actual ellipsis mark, so the gate (and any reader checking the quote against its own citation) had no
way to see the gap the paragraph above already discloses. Two separate fixes: the roll-of-the-dead
elision is now marked with a real "..." rather than silently absent - it's long, heavily interrupted
by the edition's own endnotes, and already deliberately elided by this record's own reasoning, so
ellipsis is the honest marker, not restoration. The second, shorter elision ("and my relatives always
observed the day when the people put away the leaven") is fully restored instead - it's short, clean
once the edition's own endnote is stripped, and the record's previous "I am the eighth - I myself"
also had the wrong punctuation (the source has no dash there at all; the real dash sits at "leaven-I
myself"). No claim in this record changes either way.

THIS IS A PRIMARY GRAVITY'S HARDEST CASE AND IT WAS MISSING.
pahc.gravity.translocal-network is about the letters that held scattered
congregations together. Every other witness to it in this world's
registry shows the network working. This shows it failing: Rome
threatening excommunication over a calendar, Asia refusing, and both
sides claiming apostolic descent for their practice. Polycrates' answer
is not an argument from scripture or from reason - it is a list of the
dead, and a count of his own family's bishops, and a refusal.

MODERN RENDERING AUTHORED (2026-08-29, pahc register pass; Mark's standing quote ruling: spoken form is a modern-English translation, not a summary - original wording stays as text, shown at Level 3).

BAR SWEEP (2026-08-29, Mark: "much better thats the bar" - see Ministry/Technology/CiC_Register_Bar_2026-08-29.md): rendering rewritten to the approved sample's level - short sentences, everyday words, translation fidelity kept; original stays as text for Level 3.
