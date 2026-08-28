---
id: desert.figure.antony
world_id: desert-monasticism
record_type: figure
schema_version: 2
status: draft
register: emic
canon_cells: [F4-I, F4-P]
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: "Documented for the outline of Antony's career as Athanasius narrates it (withdrawal, the tombs, the fort, the inner mountain, death at a great age) - not for its incident-level historicity, which David Brakke's reading treats as a shaped, polemically-motivated literary construction rather than neutral biography (Doc_01 SS10), and not for the 'unlettered' characterization specifically, which desert.contested.antony-literacy holds open against Rubenson's counter-reading of the Letters."
sources:
- source_id: desert.source.athanasius-vita-antonii
  locus: "SS1-2 (birth, the Matthew 19:21 moment), SS8-9 (the tombs), SS12-13 (the fort, a twenty years' sojourn), SS49-50 (the inner mountain), SS72-73 (the Greek philosophers scene), SS89 (his age near death), SS92-93 (his death)"
  license: public-domain
- source_id: desert.source.antony-letters
  locus: "seven letters attributed to him - the one possible surviving material in his own voice, cited only through Rubenson at Contested confidence, never quoted directly (no vendored edition)"
- source_id: desert.source.apophthegmata-patrum
  locus: "sayings attributed to Antony by name recur across the collection - the standing compiler-mediation caveat every Apophthegmata citation carries applies here without exception"
- source_id: desert.source.brakke-athanasius
  locus: "the Vita read as a shaped, politically and theologically motivated literary construction rather than neutral biography"
names:
- name: Antony
  tag: in-world
- name: "Antony of Egypt (c. 251-356)"
  tag: scholarly
dates:
  born: "c. 251 (derived: Vita SS89 has him say, shortly before his death, that he is 'near a hundred and five years old'; external chronology fixes his death in 356)"
  died: "356, at the inner mountain - narrated at Vita SS92-93, written by Athanasius shortly after"
  floruit: "withdrawal begun in his late teens or early twenties, within six months of his parents' deaths, after hearing Matthew 19:21 read aloud in church and taking it as address to himself directly (Vita SS2); the tombs, then the fort at Pispir for some twenty years (SS8-13), then the inner mountain from c. 313 until his death (SS49-50)"
narratable: true
bridge_line: "the man who, by his own hagiographer's account, gave away nearly everything at about eighteen or twenty on the strength of one verse heard in church, never learned to read, and still told visiting philosophers that a sound mind has no need of letters"
relations:
- type: associated-with
  target: desert.quote.the-word-took-a-human-body
- type: associated-with
  target: desert.gravity.withdrawal
- type: associated-with
  target: desert.gravity.spiritual-combat
- type: associated-with
  target: desert.contested.antony-literacy
- type: associated-with
  target: desert.story.antony-call
- type: associated-with
  target: desert.story.antony-withdrawal
- type: associated-with
  target: desert.story.antony-tomb-combat
- type: associated-with
  target: desert.quote.antony-dying-daily
- type: associated-with
  target: desert.quote.antony-arians-serpents
- type: associated-with
  target: desert.quote.antony-not-worsted
- type: associated-with
  target: desert.quote.antony-nicene-formula
---
SYSTEMIC AUTHOR-GRAVITY FLAG (this world's own version of the risk
Doc_03's Author Gravity discipline names generally): Antony's own
portrait in this corpus rests overwhelmingly on one source, Athanasius's
Vita, written by a bishop with his own anti-Arian and pro-episcopal-
authority purposes (Brakke's reading, Doc_01 SS10) - this world's
paradigmatic figure is known to us chiefly through someone else's
literary construction of him, not through his own extended voice. The
one possible exception, the seven Letters, is itself the pivot of a
live, unresolved contest over how literate and how philosophically
formed the man behind the Vita's "unlettered rustic" portrait actually
was (desert.contested.antony-literacy) - this record states the Vita's
own claim (SS1, SS72-73: he "could not endure to learn letters," and
told visiting philosophers "whoever hath a sound mind hath not need of
letters") without asserting it as settled biographical fact.

Formation significance: withdrawal (desert.gravity.withdrawal) is not
illustrated by Antony's career so much as it is patterned on it - his
own staged progression (village edge, then the tombs, then the fort,
then the inner mountain) is this world's own paradigm case for
withdrawal as a lifelong deepening rather than a single decisive act,
per Doc_01 SS2.1 and desert.gravity.withdrawal's own re-derivation.
His demonic combat at the tombs and in the fort (SS8-9, SS12-13) is
likewise the paradigm case for desert.gravity.spiritual-combat, tested
in this build separately from Evagrius's later systematized form of the
same struggle. This record does not extend Antony's own individual
career into a claim about how representative his experience was of
ordinary participants generally. Two distinct, overlapping pairs are at
work here, kept separate: this record's own relations[] name the two
gravities Antony's own career is associated with (withdrawal and
spiritual-combat); Doc_04 SS3 separately routes the literacy contest's
own Cross-Check treatment to withdrawal and elder-authority
specifically, and it is withdrawal's and elder-authority's own gravity
records - not spiritual-combat's - that each state the contest does not
threaten their classification, since each is independently attested
across the wider Apophthegmata tradition and the Pachomian corpus, not
solely through Antony's own characterization.

Step3c, Round 1 review Finding M8: the paragraph above previously
merged those two distinct pairs into one ("both gravity records he is
associated with... withdrawal, elder-authority"), asserting a relation
this record does not declare (elder-authority) while dropping one it
does (spiritual-combat). Corrected to name both pairs separately.
Finding M1: David Brakke's reading, load-bearing in this record's own
divergence_note, was unregistered - desert.source.brakke-athanasius
added to sources[]. Finding M4: the bridge_line attributed the
illiteracy claim to "those who knew him" (plural) where this record's
own single-voice-concentration caution requires naming the one
hagiographer; "never taught to read" shifted agency away from what the
Vita's SS1 actually narrates (a refusal, not an absence of teaching);
and the philosophers clause carried no hedge once the attribution
phrase had closed. Reworded to keep the whole sentence under one
attribution and to match SS72's own "had not learned letters." Finding
M5: "at nineteen or twenty" was an unmarked derivation from Vita SS2's
own "about eighteen or twenty" - corrected to the source's own words.
Finding M15: the Vita locus named SS89-90 for "his death"; SS89-90 is
his final visit and age near death, and the death itself is at SS92-93,
which this record's own dates.died already cited correctly - the locus
corrected to match.

Step3c, Round 2 review Finding C3: "gave away everything" overstated
SS2, reopened for the M5 fix above, which has him reserve "a little...
for his sister's sake" - full renunciation comes later, at SS3.
Corrected to "gave away nearly everything." Finding M3: the Round 1 fix
for M8 re-merged the two pairs it was written to keep apart, attributing
to "his associated gravity records" (withdrawal, spiritual-combat) a
does-not-threaten-classification statement that elder-authority - not
spiritual-combat - actually carries. Reworded to state each fact
separately without merging which records say what.
