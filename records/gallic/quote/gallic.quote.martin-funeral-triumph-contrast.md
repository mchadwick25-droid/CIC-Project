---
id: gallic.quote.martin-funeral-triumph-contrast
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as Sulpitius's own closing rhetoric for the letter: a deliberate contrast he draws
    himself between a Roman military triumph and Martin's funeral, not a claim about any witnessed
    event beyond the procession already described. The claim "Martin is praised with the divine
    psalms" is present-tense in the letter itself - the cult beginning in the same breath as the death
    it mourns.
sources:
- source_id: gallic.source.sulpitius-letters
  locus: 'Letter III, To Bassula, His Mother-in-Law (npnf211 div ii.iii.iii, file lines 2506-2518): Sulpitius''s closing contrast between a worldly triumph and Martin''s funeral, ending "Martin is praised with the divine psalms"'
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - participant asks how this community understood grief and joy together at a death
  - participant asks how or when Martin's cult began, or what "Martin is praised with the divine
    psalms" meant
  - conversation reaches what counted as a triumph in this world, against what the wider Roman world
    counted as one
  prefer_instead:
  - participant is asking about the later cult of Martin at Tours, the basilica, or Gregory of Tours -
    outside our window and evidence
text: >-
  each single person preferred that he himself should grieve, but that another should rejoice. Thus
  then this multitude, singing hymns of heaven, attended the body of the sainted man onwards to the
  place of sepulture. Let there be compared with this spectacle, I will not say the worldly pomp of a
  funeral, but even of a triumph; and what can be reckoned similar to the obsequies of Martin? Let your
  worldly great men lead before their chariots captives with their hands bound behind their backs.
  Those accompanied the body of Martin who, under his guidance, had overcome the world. Let madness
  honor these earthly warriors with the united praises of nations. Martin is praised with the divine
  psalms, Martin is honored in heavenly hymns.
speaker_or_author: Sulpitius Severus, narrating
license: verbatim
modern_lens_note: >-
  Sulpitius reaches for the highest secular honor he knows - a Roman triumph, with chained captives led
  before the general's chariot - and sets it against Martin's funeral on purpose, to say the comparison
  fails: Martin's own companions are people he freed, "who, under his guidance, had overcome the
  world," not people he conquered. The line "Martin is praised with the divine psalms" is not a future
  hope; Sulpitius writes it as already true, within months of the death.
relations:
- type: associated-with
  target: gallic.story.death-of-martin-at-condate
modern_rendering: >-
  Each person preferred to do the grieving himself and let the other rejoice. So this crowd, singing
  the hymns of heaven, went with the holy man's body on to the place of burial. Set beside this
  sight not just the worldly pomp of a funeral, but even that of a triumphal parade. What can be
  counted equal to Martin's funeral? Let your great men of this world lead captives before their
  chariots, hands tied behind their backs. Those who went with Martin's body had, under his
  guidance, overcome the world. Let madness honor these earthly warriors with the joined praises of
  nations. Martin is praised with the sacred psalms; Martin is honored in the hymns of heaven.
---
Verified verbatim against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"each single person preferred that he himself should grieve"` returns line 2506; `grep -n "Martin is
honored in heavenly hymns"` returns line 2518. Read in full at lines 2506-2518: one continuous,
unbroken run of prose in the source, from the shared grief-and-joy sentence through the triumph
contrast to its close.

The host record's own current wording of the closing sentences uses an ellipsis ("Those accompanied
the body of Martin who, under his guidance, had overcome the world. ... Martin is praised with the
divine psalms, Martin is honored in heavenly hymns."), eliding "Let madness honor these earthly
warriors with the united praises of nations."; this record carries the complete passage verbatim,
including that sentence, per the source. No word was added, dropped, substituted, or reordered; hard
line wraps were joined with single spaces.
