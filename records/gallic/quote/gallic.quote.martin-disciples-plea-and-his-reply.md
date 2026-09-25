---
id: gallic.quote.martin-disciples-plea-and-his-reply
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
  formation_confidence: Widely Accepted
  divergence_note: >-
    The wording is Documented as Sulpitius's own text. Sulpitius was not present at Martin's death and
    says so himself in this same letter's opening; the disciples' collective lament and Martin's one
    recorded prayer both rest on the testimony of others, carried by Sulpitius at ordinary narrative
    strength rather than as a witnessed wonder. Widely Accepted rather than Documented because this is
    one author's letter, on others' report, not multiple independent sources.
sources:
- source_id: gallic.source.sulpitius-letters
  locus: 'Letter III, To Bassula, His Mother-in-Law (npnf211 div ii.iii.iii, file lines 2412-2430): the brethren''s lament as Martin''s strength fails, and Martin''s reply, "O Lord, if I am still necessary to thy people..."'
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - participant asks how the community responded when Martin's death became visibly near
  - participant asks what Martin himself said about wanting to live or wanting to die
  - conversation reaches grief spoken honestly, or a leader answering it without dismissing it
  prefer_instead:
  - participant wants Sulpitius's own later, more elaborate rendering of Martin's inner struggle -
    retrieve gallic.quote.martin-imagined-soldiers-speech, which follows this moment in the letter
  - participant wants the deathbed's final words, not this earlier failing of strength - retrieve
    gallic.quote.martin-allow-me-dear-brother or gallic.quote.martin-rebukes-the-devil-and-dies
text: >-
  he began suddenly to fail in bodily strength, and, assembling the brethren, he told them that he was
  on the point of dissolution. Then indeed, sorrow and grief took possession of all, and there was but
  one voice of them lamenting, and saying: "Why, dear father, will you leave us? Or to whom can you
  commit us in our desolation? Fierce wolves will speedily attack thy flock, and who, when the shepherd
  has been smitten, will save us from their bites? We know, indeed, that you desire to be with Christ;
  but thy reward above is safe, and will not be diminished by being delayed; rather have pity upon us,
  whom you are leaving desolate." Then Martin, affected by these lamentations, as he was always, in
  truth, full of compassion, is said to have burst into tears; and, turning to the Lord, he replied to
  those weeping round him only in the following words, "O Lord, if I am still necessary to thy people,
  I do not shrink from toil: thy will be done."
speaker_or_author: the brethren at Condate, and Martin, as Sulpitius reports them
license: verbatim
modern_lens_note: >-
  The disciples do not ask Martin to be comforted about death; they ask him not to leave them
  unprotected, naming the danger plainly - "fierce wolves." Martin's answer is just as plain: not a
  reassurance, but a single sentence putting his own preference under someone else's will. Grief and
  duty sit in the same scene without either one canceling the other out.
relations:
- type: associated-with
  target: gallic.story.death-of-martin-at-condate
- type: associated-with
  target: gallic.figure.martin
modern_rendering: >-
  He suddenly began to lose his bodily strength. He gathered the brothers and told them he was about
  to die. Then sorrow and grief took hold of everyone. They all cried out with one voice, lamenting:
  "Dear father, why will you leave us? To whom can you entrust us, left alone and without comfort? Fierce
  wolves will soon attack your flock. When the shepherd has been struck down, who will save us from
  their bites? We know, of course, that you long to be with Christ. But your reward in heaven is
  safe. Waiting will not make it any smaller. Have pity on us instead, for you are leaving us
  alone and without comfort." Martin was moved by their laments, for he was truly always full of compassion. He is said
  to have burst into tears. He turned to the Lord. To those weeping around him he gave only this
  answer: "O Lord, if your people still need me, I do not shrink from the work. Your will be done."
---
Verified verbatim against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"on the point of dissolution"` returns line 2414; `grep -n "thy will be done"` returns line 2430. Read
in full at lines 2412-2430: this is one continuous, unbroken run of prose in the source - the failing
of strength, the brethren's lament, and Martin's reply all follow without a gap - so it is carried as
a single quotation rather than three separate fragments.

The host record's own current wording of the disciples' lament elides the middle of their speech with
an ellipsis ("Fierce wolves will speedily attack thy flock ... rather have pity upon us"); this record
carries the complete sentence verbatim, including the elided clause ("and who, when the shepherd has
been smitten, will save us from their bites? We know, indeed, that you desire to be with Christ; but
thy reward above is safe, and will not be diminished by being delayed;"), per the source. No word was
added, dropped, substituted, or reordered from the source's own wording; only the source's hard line
wraps were joined with single spaces, and the edition's own curly quotation marks around speech are
dropped as its own punctuation.

speaker_or_author names both parties since the excerpt carries two distinct attributed speeches - the
brethren's collective lament and Martin's own reply - each introduced by Sulpitius's narration as
belonging to a named party in the scene.
