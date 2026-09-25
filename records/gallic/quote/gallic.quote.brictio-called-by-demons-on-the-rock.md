---
id: gallic.quote.brictio-called-by-demons-on-the-rock
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F6-P
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted at the narrative level and Documented at its locus (Dialogues III.15). Contested for
    the two demons on the rock and their call to Brictio - Gallus's own perception, as he transmits it,
    not an independently attested event; carried here as the tradition's own account of what Gallus says
    he saw and heard, not a claim that demons literally sat on the rock.
sources:
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: "Dialogues III.15 (npnf211 div ii.iv.iii.xv, file lines 5289-5299): Martin seated in the small
    court; two demons on the rock overhanging the monastery calling Brictio's name; Brictio's furious
    arrival"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks how the Brictio story opens, or wants Gallus's own scene-setting"
  - "participant asks what the two demons on the rock are said to have done"
  prefer_instead:
  - "participant wants the whole story in the world's own accessible voice - retrieve gallic.story.brictio-in-the-courtyard"
text: >-
  Again, on a certain day, after he had sat down on that wooden seat of his (which you all know), placed
  in the small open court which surrounded his abode, he perceived two demons sitting on the lofty rock
  which overhangs the monastery. He then heard them, in eager and gladsome tones, utter the following
  invitation, ‘Come hither, Brictio, come hither, Brictio.’ I believe they perceived the miserable man
  approaching from a distance, being conscious how great frenzy of spirit they had excited within him.
  Nor is there any delay: Brictio rushes in in absolute fury; and there, full of madness, he vomits forth
  a thousand reproaches against Martin.
speaker_or_author: "Gallus, as Sulpitius Severus records his account in the Dialogues"
license: verbatim
modern_lens_note: >-
  Gallus tells the story from Martin's own vantage point on an ordinary seat "which you all know" - a
  detail for listeners who had stood in that courtyard themselves. The demons are named before Brictio
  even appears; the audience is told how to read the coming outburst before it happens, as possession
  rather than as an honest complaint.
relations:
- type: associated-with
  target: gallic.story.brictio-in-the-courtyard
modern_rendering: PENDING_OPUS_RENDERING
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"certain day, after he had sat down"` (via "certain day," anchor) returns line 5290, the opening of
`<div4 title="Chapter XV." ... id="ii.iv.iii.xv">` (line 5285); `grep -n "thousand reproaches against
Martin"` returns line 5299. Read with `sed -n '5289,5299p'`.

Normalization: line breaks joined with single spaces. The chapter's own opening curly double quotation
mark (marking the whole chapter as Gallus's reported speech within the Dialogues) is dropped, as is the
outer punctuation throughout - the same convention the fleet's worked example
(gallic.quote.martin-on-the-christ-with-wounds) uses. The single curly quotes around the demons' own
words, ‘Come hither, Brictio, come hither, Brictio,’ are kept, since that is direct speech quoted inside
Gallus's narration, not the edition's outer speech-marking. No word was added, dropped, substituted, or
reordered.
