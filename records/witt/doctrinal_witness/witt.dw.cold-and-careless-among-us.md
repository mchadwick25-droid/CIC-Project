---
id: witt.dw.cold-and-careless-among-us
world_id: lutheran-wittenberg-and-its-congregations
record_type: doctrinal_witness
schema_version: 2
status: draft
register: emic
canon_cells:
- F6-P
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: contested
  formation_confidence: Contested
  divergence_note: >-
    Documented as our founder's own testimony, given more than once across a decade; Contested at the
    scholarly level whether that testimony describes real congregations or is rhetoric, and this record
    carries witt.force.parishes-state-as-reported's own explicit bar forward: nothing here may be read as
    evidence that any actual Saxon congregation was in fact cold, ignorant, or negligent.
sources:
- source_id: witt.force.parishes-state-as-reported
  locus: "'an ass can almost intone the lessons... God does not want hearers and repeaters of words, but doers and followers' (v2 14676-14688); 'we see to our sorrow that many pastors and preachers are very negligent' (LC 51-52); Katharina von Bora's own question about coldness in prayer (TT 3147-3150)"
  license: public-domain
- source_id: witt.story.household-and-kate-on-prayer
  locus: "Luther's own answer to the coldness question, verified verbatim there against cic/texts/luther_table-talk_bell1886.txt lines 3143-3152 -- 'the devil drives on his own servants continually, diligent in their false worship... but we, indeed, are ice cold therein, and negligent'"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether the people who taught us the faith turned out to be hypocrites"
  prefer_instead:
  - "participant asks what our people would have made of someone like the participant specifically -- retrieve witt.demo.someone-like-me instead, the identity-collision content this record does not repeat"
  - "participant means whether a woman could carry real authority among us -- our record does not answer that honestly beyond a single question, per witt.voice.craft's own declined-cells reasoning"
text: >-
  The people who taught you the faith turned out to be hypocrites. Did
  that happen among us? We will not pretend it did not. Our own founder
  said, more than once, across a whole decade, that it did -- not about
  strangers, but about pastors and preachers of our own. In one parish
  he said flatly that a donkey could intone the lessons about as well as
  the people repeating them, because God wants doers, not repeaters of
  words. Years later, writing for the whole territory, he said plainly
  that many pastors were negligent, and that ordinary people held the
  Gospel far too lightly. That is not a stranger's accusation; that is
  our own founder's own complaint, said in his own voice, more than
  once.

  We must be careful here, and honest about the shape of what we
  actually hold. That testimony is his own -- real, and said more than
  once -- but it is testimony, not a report from any actual parish
  standing beside it to check it against. We do not have the records
  that would tell us whether he was right about how bad it really was,
  only that he believed it and said so. And on this same question of
  coldness, we hold one more voice, briefer, closer to home: a question
  asked once at our founder's own table, why some prayed with such
  fervor under the old system while we, under the new one, prayed so
  coldly and carelessly. Our founder answered her plainly: the devil
  drives his own servants hard, and they take great pains at their
  false worship, while we, at the true one, grow ice-cold and
  negligent. That answer is real, given at his own table to someone who
  lived closest to him, and it was thought worth remembering.
positions:
- "our own founder testified, more than once and across a decade, that pastors were negligent and that ordinary people held the Gospel too lightly -- not a stranger's charge, but his own"
- "that testimony is real, but it is testimony, not a verified report from any actual parish -- we do not let it stand as proof of what any specific congregation was actually like"
- "the same coldness was named from inside our own household: a question, asked once at our founder's own table, about why prayer under the new teaching felt colder than it had under the old"
tensions:
- "we cannot tell you whether our founder's own complaint was accurate -- the records that could confirm or correct it, the parish visitations themselves, are not held in our library"
- "this record does not answer every part of this cell -- whether we ever wanted to leave, what we would tell someone who did leave, or where God was in real suffering are questions this authoring pass leaves for a future pass; and the identity-collision and women's-authority questions this same cell can ask remain declined, per witt.voice.craft's own stated reasoning, not attempted here either"
relations:
- type: associated-with
  target: witt.story.household-and-kate-on-prayer
- type: associated-with
  target: witt.figure.katharina-von-bora
---
Closes F6-P at the Answer-the-Canon step (inserted between B-7a and B-8) by answering the cell's
hypocrisy sub-question at real strength, the one this world's own already-built force record
(witt.force.parishes-state-as-reported) grounds most directly and honestly -- rather than force an answer
to the cell's other five sub-questions (someone-like-me; suffering; wanting to leave; what to tell someone
who left; women's authority), several of which witt.voice.craft's own B-7 body note already named as
declined for good, stated reasons (identity-collision material confined to witt.demo.someone-like-me;
women's-authority material would require inventing content this world's own Absent Stories finding
refuses). Closing the CELL honestly, at its strongest real sub-question, is the discipline this record
follows rather than attempting all six at partial strength; the tensions field names the scope directly
rather than leaving a reader to assume this record answers more than it does.

Built entirely from witt.force.parishes-state-as-reported, already verified-via-authority at its own B-5
authoring pass and carrying its own explicit bar ("no downstream record may cite this force... as
evidence that Saxon congregations were ignorant, cold, or negligent") forward into this record's own
confidence.divergence_note and text, exactly as that bar requires. Not re-opened against the vendored
files by this record.

CORRECTION (go-live adversarial review, Round 1, 2026-09-19; H-2, HIGH): this record's own `text` field
originally claimed "we do not have his full answer" to Katharina von Bora's coldness-in-prayer question --
false. The vendored library carries Luther's own answer verbatim, `cic/texts/luther_table-talk_bell1886.txt`
lines 3147-3151 ("the devil driveth on his servants continually... but we, indeed, are ice cold therein,
and negligent"), already verified there by `witt.story.household-and-kate-on-prayer` (`verification_state:
verified-direct`) and already correctly summarized in `witt.figure.katharina-von-bora`'s own body note
("answered by her husband with a saying about the devil driving his own servants harder than they drive
themselves"). Two defects in one field: a false honest-limit (claiming the record is emptier than it is)
and dropped content (a vivid, fully-sourced piece of this world's own voice, withheld from the
participant). Fixed by adding the answer in indirect speech, reconciled with the two records that already
held it correctly rather than editing either of them to match the error; `sources[]` and `relations[]`
updated to cite `witt.story.household-and-kate-on-prayer` directly, closing the sourcing gap that let the
false claim stand unchecked (nothing in the build gates checks a negative "we do not have" claim against
the library; this was found by opening the vendored source, not by reading the record).

The declined-cells reasoning for identity-collision and women's-authority material (why neither is
re-attempted here) belongs to witt.voice.craft's own B-7 body note, cited by reference above rather than
restated in a frontmatter field -- no frontmatter field is invented to hold that pointer, per this
project's own file-discipline rule; it is carried in this body note only.
