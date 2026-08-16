---
id: ijcq009
world_id: imperial-juridical-christianity
record_type: quote
schema_version: 1
jobs:
- 1
- 2
- 3
register: emic
review_state: draft
speaker_or_author: ijcfig010
text_translation: Then didst Thou by a vision make known to Thy renowned bishop the spot where lay the
  bodies of Gervasius and Protasius, the martyrs. Thou hadst in Thy secret storehouse preserved [them]
  uncorrupted for so many years. Whence Thou mightest at the fitting time produce them to repress the
  feminine but royal fury.
locus: Augustine, Confessions 9.7 (the discovery of Gervasius and Protasius)
translation_used: srcIJC48
license: verbatim
confidence:
  citation_specificity: A
  verification_state: verified-direct
  verification_date: '2026-08-16'
  evidentiary_weight: load-bearing
  formation_confidence: Documented
---
Added 2026-08-15 at Mark's explicit request ("add a quote from Confessions 9.7's martyrs discovery").
A second quote from the same chapter as ijcq008 (which drew on paragraph id="vi.IX.VII-p2", the vigil
kept during the basilica standoff) - this one is paragraph id="vi.IX.VII-p4", the very next paragraph:
Augustine's account of the vision that led Ambrose to the bodies of the martyrs Gervasius and
Protasius, and their translation to the Ambrosian Basilica.

A SCOPING QUESTION WAS CONSIDERED before using this passage: srcIJC08's own license reads narrowly -
"eyewitness testimony to Ambrose's own conduct only" during "Ambrose's antiphonal psalm-singing, 386
standoff." The martyrs' discovery is a distinct episode from the psalm-singing vigil, though Augustine
narrates it in the same chapter as a continuation of the same conflict (explicitly stated purpose: "to
repress the feminine but royal fury," i.e. Justina's Arian party - the same antagonist as the standoff).
Judged in scope because it is still Ambrose's own conduct (he receives the vision, acts on it, and
presides over the relics' translation) within the same 386 conflict srcIJC08 already licenses, not a
different event requiring a new source row. srcIJC48's own licensed_for note is widened alongside this
record to name both paragraphs explicitly, rather than leaving the wider reading merely implicit in an
unchanged work_locus.

Wording transcribed directly (tail-aware ElementTree walker) from
cic/texts/npnf101_augustine-confessions-letters.xml, div3 id="vi.IX.VII", paragraph
id="vi.IX.VII-p4". Selected over the paragraph's other vivid material (the blind man healed by touching
the martyrs' bier) because this sentence keeps the political frame explicit - the miracle's stated
purpose is to check the "royal fury," directly continuing imperial_juridical's own theme of the church's
authority set against imperial pressure, the same frame ijcq002 (Ambrose's own sermon) and ijcq008
(Augustine's account of the vigil) both carry.

UPDATE 2026-08-16 (T3 readability follow-on): gate_voice_readability flagged the original text_translation
above at FK grade 22.2 / FRE 30.1 - one 60-word sentence with a nested parenthetical relative clause
("(whom Thou hadst...)") plus a trailing "whence" clause. Per Mark's "re-select simpler verbatim excerpts
first" decision, this is split into three sentences: two clean period-for-comma-and-parenthesis splits, plus
one bracketed [them] where the relative pronoun "whom" (the object of "preserved," referring back to "the
martyrs") had to become an explicit object pronoun to let its clause stand alone - the same
editorially-supplied-word convention used for pahcq004's [He], marked in brackets rather than silently
absorbed. Every other word is the 1886 Pilkington translation's own, in its own order. Re-scored: FK 8.4 /
FRE 66.0, clearing both thresholds. license stays verbatim.
