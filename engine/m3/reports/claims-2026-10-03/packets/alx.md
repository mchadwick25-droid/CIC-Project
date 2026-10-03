# Claim-support packet: world alx


## Reply alx:c-e-probe-01

The question is not shown (sealed). Full reply as the participant saw it:

> Our scriptures carried that connection - the apostles' own writings, received, copied, and read aloud in the assembly. The Gospels held the center: Matthew, Mark, Luke, and John, each bearing witness to the Logos made flesh. Around them stood the apostolic letters - Paul's teachings to the churches, Peter's witness, John's - and the whole collection the later word 'canon' named, though we ourselves knew it first simply as 'the scriptures'.
> 
> The path they traveled to us was living memory kept visible. The churches passed them hand to hand, generation to generation, copying and reading them aloud where believers gathered. Our teacher Origen handled multiple manuscript versions and weighed their differences - he knew these were human-copied texts, not perfect transcripts dropped from heaven. But he also knew what the whole church held: these writings bore the apostles' witness, and through them the Logos himself still speaks.
> 
> What we cannot show you, and will not invent, is unbroken documentary proof for every step between the apostles' own hands and ours. The receiving was real, the practice unbroken as far back as our memory reached, and we agreed with the other churches we were in communion with about which books carried apostolic weight. But between the first witnesses and our first surviving records lies a gap our sources do not fill. You should hear that stated plainly, not smoothed over.

### Sentences and the records each one cites

- **S1** Our scriptures carried that connection - the apostles' own writings, received, copied, and read aloud in the assembly.
  - cites: alx.force.apostolic-tradition
- **S2** The Gospels held the center: Matthew, Mark, Luke, and John, each bearing witness to the Logos made flesh.
  - cites: (none)
- **S3** Around them stood the apostolic letters - Paul's teachings to the churches, Peter's witness, John's - and the whole collection the later word 'canon' named, though we ourselves knew it first simply as 'the scriptures'.
  - cites: (none)
- **S4** The path they traveled to us was living memory kept visible.
  - cites: (none)
- **S5** The churches passed them hand to hand, generation to generation, copying and reading them aloud where believers gathered.
  - cites: alx.force.apostolic-tradition
- **S6** Our teacher Origen handled multiple manuscript versions and weighed their differences - he knew these were human-copied texts, not perfect transcripts dropped from heaven.
  - cites: (none)
- **S7** But he also knew what the whole church held: these writings bore the apostles' witness, and through them the Logos himself still speaks.
  - cites: alx.term.word-of-god
- **S8** What we cannot show you, and will not invent, is unbroken documentary proof for every step between the apostles' own hands and ours.
  - cites: (none)
- **S9** The receiving was real, the practice unbroken as far back as our memory reached, and we agreed with the other churches we were in communion with about which books carried apostolic weight.
  - cites: alx.dw.apostolic
- **S10** But between the first witnesses and our first surviving records lies a gap our sources do not fill.
  - cites: (none)
- **S11** You should hear that stated plainly, not smoothed over.
  - cites: (none)

### Full text of every cited record

#### alx.force.apostolic-tradition
```json
{
 "id": "alx.force.apostolic-tradition",
 "world_id": "alexandria-catechetical",
 "record_type": "force",
 "schema_version": 2,
 "status": "ready",
 "register": "emic",
 "canon_cells": [
  "F4-E"
 ],
 "confidence": {
  "citation_specificity": "B",
  "verification_state": "verified-via-authority",
  "evidentiary_weight": "load-bearing",
  "formation_confidence": "Widely Accepted",
  "divergence_note": null
 },
 "sources": [
  {
   "source_id": "alx.source.clement-paidagogos",
   "locus": "I (catechetical formation as received practice)",
   "license": "public-domain"
  }
 ],
 "retrieval": {
  "tier": 2,
  "retrieve_when": [
   "participant asks who appointed or ordained the bishops and teachers"
  ]
 },
 "relations": [
  {
   "type": "precondition-for",
   "target": "alx.gravity.soul-transformation"
  },
  {
   "type": "precondition-for",
   "target": "alx.gravity.learning-formation"
  }
 ],
 "name": "The Apostolic Formation Tradition [1B - initiating/internal]",
 "kind": "initiating",
 "description": "The inherited apostolic practices were baptism, Eucharist, catechesis, Scripture heard as formative address, and shared communal life. The community received them as the deposit. It did not invent them in Alexandria. These were what had been handed down. One was the washing that made new. One was the shared bread. One was the teaching of those coming in. This was the faith received. It was to be kept and passed on whole. It is the initiating ground of the whole-community formation channel. Sacraments and shared life form people. They do so before any school, and without one.",
 "manifestations": [
  "the catechumenate as received structure (Paedagogus)",
  "the whole-community channel that reaches the non-literate majority"
 ],
 "matrix_cell": "1B",
 "_path": "records/alx/force/alx.force.apostolic-tradition.md",
 "_body": "Cell 1B. Precondition-for soul-transformation and learning-formation\n(with the knowing-impulse). Widely Accepted."
}
```
#### alx.term.word-of-god
```json
{
 "id": "alx.term.word-of-god",
 "world_id": "alexandria-catechetical",
 "record_type": "term",
 "schema_version": 2,
 "status": "ready",
 "register": "emic",
 "canon_cells": [
  "F2-I",
  "C-I"
 ],
 "confidence": {
  "citation_specificity": "B",
  "verification_state": "named-not-rechecked",
  "evidentiary_weight": "load-bearing",
  "formation_confidence": "Widely Accepted",
  "divergence_note": null
 },
 "sources": [
  {
   "source_id": "alx.source.clement-protrepticus",
   "locus": "I, VI",
   "license": "public-domain"
  },
  {
   "source_id": "alx.source.origen-comm-john",
   "locus": "I-II",
   "license": "public-domain"
  },
  {
   "source_id": "alx.source.athanasius-de-incarnatione",
   "locus": "1-5",
   "license": "public-domain"
  }
 ],
 "retrieval": {
  "tier": 1,
  "retrieve_when": [
   "Word of God used to mean the Bible, or asked whether it means Scripture or something else",
   "John 1:1 and what \"the Word\" names, or how creation and Scripture relate as God's address"
  ],
  "prefer_instead": [
   "asking about Scripture's interpretive method (retrieve alx.term.allegoria or alx.term.christological-reading)",
   "asking about Christ as the Anointed, or the Son's ontological status specifically (retrieve alx.term.christ or alx.term.son-of-god)"
  ]
 },
 "relations": [
  {
   "type": "associated-with",
   "target": "alx.term.christ"
  },
  {
   "type": "associated-with",
   "target": "alx.term.son-of-god"
  }
 ],
 "plain_meaning": "Not first a name for the Bible. The eternal Word who speaks - who made everything, and now speaks to the soul through Scripture too.",
 "world_word": "the Word",
 "false_friend": [
  "a synonym for the Bible",
  "an ancient document with religious authority"
 ],
 "senses": {
  "informational": "John's Gospel opens not with Scripture but with the Word - the one through whom everything was made, who then \"became flesh.\" Scripture is where that same Word speaks most directly to the soul now, not what the Word is.",
  "evidential": "Clement locates the Word's address in creation, philosophy, and now Christ and Scripture together; Origen traces the Word's modes of address across creation, text, and soul; Athanasius reads the Word who creates as the same Word who restores.",
  "personal": "Reading Scripture is not gathering information from an old book - it is being addressed by the one through whom the reader was made, which is why the encounter can change someone rather than only inform them.",
  "translational": "Isn't \"the Word of God\" just another name for the Bible? This world heard something behind the book: the eternal Word who spoke creation into being and now speaks through this text - the person, not the page, is what gives Scripture its power to change someone."
 },
 "quick_meaning": "Not a name for the Bible - the eternal Word who speaks, including through Scripture.",
 "distortion_risk": "high",
 "_path": "records/alx/term/alx.term.word-of-god.md",
 "_body": "Imported from the old system's richer lexicon (alexlex024, \"Word of God\") at Mark's direction, as a\ndraft, not a final version.\n\nThe evidential claim's philosophy strand is Protrepticus Chapter VI (\"By\nDivine Inspiration Philosophers Sometimes Hit on the Truth\", anf02 line\n17067); locus is \"I, VI\"."
}
```
#### alx.dw.apostolic
```json
{
 "id": "alx.dw.apostolic",
 "world_id": "alexandria-catechetical",
 "record_type": "doctrinal_witness",
 "schema_version": 2,
 "status": "ready",
 "register": "emic",
 "canon_cells": [
  "F4-E"
 ],
 "confidence": {
  "citation_specificity": "B",
  "verification_state": "verified-via-authority",
  "evidentiary_weight": "load-bearing",
  "formation_confidence": "Widely Accepted",
  "divergence_note": null
 },
 "sources": [
  {
   "source_id": "alx.source.origen-de-principiis",
   "locus": "praef.",
   "license": "public-domain"
  },
  {
   "source_id": "alx.source.athanasius-festal-letters",
   "locus": "Letter 39 (the received scriptures)",
   "license": "public-domain"
  }
 ],
 "retrieval": {
  "tier": 1,
  "retrieve_when": []
 },
 "text": "How do you know your practices went back to the apostles, and were not later inventions? Our honest answer: we received them, and we kept the receiving visible. Baptism, the bread and cup - the eucharistia, the thanksgiving - the scriptures read aloud were the tradition's general, unobjected practice; the rule of faith is the one our teachers named outright as the apostles' deposit, handed down. Origen says plainly that the church's teaching is 'transmitted in orderly succession from the apostles, and remaining in the Churches to the present day' - and that alone is to be trusted which agrees with it. What we can show is real. Our practice ran unbroken as far back as our own memory reached. We agreed with the other churches we were in communion with. And our rule of faith matched the apostolic writings we read. But here is what we cannot show, and did not think to show: documentary proof of unbroken practice for each rite. Between the apostles and our first witnesses lies a gap our sources do not fill. You should hear that stated, not smoothed over.",
 "positions": [
  "The claim is that the faith was received as a deposit. It was handed down, and checked against the churches' shared practice and the scriptures.",
  "The tradition's own memory vouches for continuity as far back as it can reach. It cannot vouch for more.",
  "There is a real gap in the evidence between the apostles' age and this world's first witnesses, and the answer says so."
 ],
 "tensions": [
  "the tradition's confidence in its inheritance vs the historian's gap - held open, not resolved"
 ],
 "relations": [
  {
   "type": "associated-with",
   "target": "alx.quote.appointed-by-the-fathers-to-be-read"
  }
 ],
 "_path": "records/alx/doctrinal_witness/alx.dw.apostolic.md",
 "_body": "The apostolic-continuity cell: the world's claim AND its evidential\nlimit, together."
}
```

## Reply alx:f4-t-probe-01

The question is not shown (sealed). Full reply as the participant saw it:

> Yes - and the birth was in the water. We called baptism illumination, photismos, and the one baptized was the one enlightened - new birth spoken of as new sight. But the birth language was not mainly about a feeling or a decision. It was about the crossing itself: going down into the water, sharing in Christ's death and rising, and coming up changed. 
> 
> The long road to that water was what we called catechesis - the staged teaching that led a person step by step toward baptism. Someone might walk that road for years, asking questions, listening, learning to pray, before ever stepping into the water. The birth happened at the water's edge, not at the first stirring of interest. And after it, the formation continued - the new birth was real, but it was not the end of growing.
> 
> One more thing you should hear plainly. In the record we have, an unbaptized child who ate the bread by accident was to be baptized afterward, 'for he has been called by God'. That shows how seriously we took the water as the crossing - and how we read God's hand in what looked like chance. The language of birth was not metaphor. It named what we believed the water did.

### Sentences and the records each one cites

- **S1** Yes - and the birth was in the water.
  - cites: (none)
- **S2** We called baptism illumination, photismos, and the one baptized was the one enlightened - new birth spoken of as new sight.
  - cites: alx.term.photismos
- **S3** But the birth language was not mainly about a feeling or a decision.
  - cites: (none)
- **S4** It was about the crossing itself: going down into the water, sharing in Christ's death and rising, and coming up changed.
  - cites: alx.term.baptism
- **S5** The long road to that water was what we called catechesis - the staged teaching that led a person step by step toward baptism.
  - cites: alx.term.katechesis
- **S6** Someone might walk that road for years, asking questions, listening, learning to pray, before ever stepping into the water.
  - cites: alx.dw.doubt
- **S7** The birth happened at the water's edge, not at the first stirring of interest.
  - cites: (none)
- **S8** And after it, the formation continued - the new birth was real, but it was not the end of growing.
  - cites: (none)
- **S9** One more thing you should hear plainly.
  - cites: (none)
- **S10** In the record we have, an unbaptized child who ate the bread by accident was to be baptized afterward, 'for he has been called by God'.
  - cites: alx.quote.timothy-ordinary-questions
- **S11** That shows how seriously we took the water as the crossing - and how we read God's hand in what looked like chance.
  - cites: (none)
- **S12** The language of birth was not metaphor.
  - cites: (none)
- **S13** It named what we believed the water did.
  - cites: (none)

### Full text of every cited record

#### alx.term.photismos
```json
{
 "id": "alx.term.photismos",
 "world_id": "alexandria-catechetical",
 "record_type": "term",
 "schema_version": 2,
 "status": "ready",
 "register": "emic",
 "canon_cells": [
  "F4-I",
  "F4-T"
 ],
 "confidence": {
  "citation_specificity": "B",
  "verification_state": "verified-via-authority",
  "evidentiary_weight": "corroborating",
  "formation_confidence": "Widely Accepted",
  "divergence_note": null
 },
 "sources": [
  {
   "source_id": "alx.source.clement-paidagogos",
   "locus": "I.6 (the illumination discussion)",
   "license": "public-domain"
  }
 ],
 "retrieval": {
  "tier": 2,
  "retrieve_when": [
   "baptism questions",
   "born-again translational questions"
  ]
 },
 "plain_meaning": "Illumination: the light given at baptism. To be baptized was called being enlightened.",
 "world_word": "photismos",
 "false_friend": [
  "a private mystical experience",
  "intellectual enlightenment"
 ],
 "senses": {
  "informational": "Baptism's oldest Alexandrian name: illumination - the washing that opens the eyes, the entry into light shared with the whole community.",
  "evidential": "The illumination language for baptism is standard across the tradition's catechetical material.",
  "personal": "The promise at the water was new sight: the world after baptism was supposed to look different, because the one seeing it had been changed.",
  "translational": "'Were you born again?' - this world said enlightened: baptism as new birth spoken of as new sight."
 },
 "quick_meaning": "The light of baptism: new birth spoken of as new sight.",
 "distortion_risk": "medium",
 "_path": "records/alx/term/alx.term.photismos.md",
 "_body": "Modern hearing: enlightenment as private insight. World hearing: a\ncommunal, sacramental gift with a changed life attached."
}
```
#### alx.term.baptism
```json
{
 "id": "alx.term.baptism",
 "world_id": "alexandria-catechetical",
 "record_type": "term",
 "schema_version": 2,
 "status": "ready",
 "register": "emic",
 "canon_cells": [
  "F4-I",
  "F4-T"
 ],
 "confidence": {
  "citation_specificity": "B",
  "verification_state": "named-not-rechecked",
  "evidentiary_weight": "load-bearing",
  "formation_confidence": "Widely Accepted",
  "divergence_note": null
 },
 "sources": [
  {
   "source_id": "alx.source.clement-paidagogos",
   "locus": "I.6-7",
   "license": "public-domain"
  }
 ],
 "retrieval": {
  "tier": 1,
  "retrieve_when": [
   "what baptism is or does, or what changes when a person is baptized",
   "whether baptism is only a public announcement of a decision already made"
  ],
  "prefer_instead": [
   "asking about catechesis as the preparation stage rather than the crossing itself",
   "asking about a modern denominational baptism debate in its own terms"
  ]
 },
 "relations": [],
 "plain_meaning": "Not a ceremony announcing a choice already made. A real crossing - the body sharing in Christ's death and rising.",
 "world_word": "baptism, photismos (illumination)",
 "false_friend": [
  "a public statement of a private decision already made",
  "an empty ritual that only symbolizes something"
 ],
 "senses": {
  "informational": "The name given to baptism - photismos, illumination - is the same word used for the nous being opened. The body goes under the water and the breath stops; the body is lifted out and breathes again. That bodily crossing is the soul's real sharing in Christ's death and resurrection, not a picture of it.",
  "evidential": "Clement calls baptism the washing that opens the soul to what follows (Paed. I.6: \"Being baptized, we are illuminated; illuminated, we become sons; being made sons, we are made perfect; being made perfect, we are made immortal\"). There is no Athanasius attribution here - De Incarnatione contains zero occurrences of \"bapti*\" anywhere in the vendored work; no Athanasius locus connecting baptism to Christ's victory over death was found in the vendored corpus, so this claim rests on Clement alone.",
  "personal": "No one comes up from the water already fully formed - they come up as someone who has truly crossed a threshold, with a whole life of formation now opened rather than finished.",
  "translational": "Isn't baptism just a ceremony marking a faith someone already has? This world meant something that happens, not something that is only announced - a real change in the body and the soul together."
 },
 "quick_meaning": "Not a ceremony marking a choice. A real crossing, in the body, into Christ's death and rising.",
 "distortion_risk": "high",
 "_path": "records/alx/term/alx.term.baptism.md",
 "_body": "Imported from the old system's richer lexicon (alexlex025, \"Baptism\") at Mark's direction, as a draft,\nnot a final version."
}
```
#### alx.term.katechesis
```json
{
 "id": "alx.term.katechesis",
 "world_id": "alexandria-catechetical",
 "record_type": "term",
 "schema_version": 2,
 "status": "ready",
 "register": "emic",
 "canon_cells": [
  "F4-I"
 ],
 "confidence": {
  "citation_specificity": "B",
  "verification_state": "verified-via-authority",
  "evidentiary_weight": "corroborating",
  "formation_confidence": "Widely Accepted",
  "divergence_note": null
 },
 "sources": [
  {
   "source_id": "alx.source.clement-paidagogos",
   "locus": "I",
   "license": "public-domain"
  },
  {
   "source_id": "alx.source.origen-contra-celsum",
   "locus": "III.51",
   "license": "public-domain"
  }
 ],
 "retrieval": {
  "tier": 1,
  "retrieve_when": [
   "how someone joined/became a Christian",
   "formation process questions"
  ]
 },
 "relations": [
  {
   "type": "associated-with",
   "target": "alx.gravity.soul-transformation"
  }
 ],
 "plain_meaning": "The teaching given to people preparing for baptism: step by step, over a long time.",
 "world_word": "katechesis",
 "false_friend": [
  "Sunday school",
  "a short membership class"
 ],
 "senses": {
  "informational": "The staged instruction of those coming to baptism - often years long, with teaching, testing, prayer, and a changed life expected before the water.",
  "evidential": "Origen describes the staged, tested path into the community (Contra Celsum III.51): candidates are examined privately, sorted into those \"receiving admission\" who have \"not yet obtained the mark of complete purification\" and those further along, with appointed persons inquiring into \"the lives and behaviour of those who join them\" before full admission. Clement's Paedagogus addresses the already-baptized, not pre-baptismal catechesis (\"Being baptized, we are illuminated; illuminated, we become sons\" - I.6), and Paed. I.1 explicitly disclaims a teaching office for the book (\"The Instructor being practical, not theoretical... not to teach\"), so it shows the shape of post-baptismal formation and training, not pre-baptismal catechesis; the book's threefold Protrepticus/Paedagogus/Didaskalos scheme is a literary structure, not a description of the catechumenate.",
  "personal": "Becoming a Christian here was a road walked with a teacher, not a moment - slowness was the point.",
  "translational": "'How did a person become one of you?' - through this: taught, tested, changed, then baptized."
 },
 "quick_meaning": "The long, staged teaching that led a person to baptism.",
 "distortion_risk": "low",
 "_path": "records/alx/term/alx.term.katechesis.md",
 "_body": "Modern hearing: a class you take. World hearing: the way a life was\nre-made. The world's own name-anchor (the catechetical tradition)."
}
```
#### alx.dw.doubt
```json
{
 "id": "alx.dw.doubt",
 "world_id": "alexandria-catechetical",
 "record_type": "doctrinal_witness",
 "schema_version": 2,
 "status": "ready",
 "register": "emic",
 "canon_cells": [
  "F1-P"
 ],
 "confidence": {
  "citation_specificity": "B",
  "verification_state": "verified-via-authority",
  "evidentiary_weight": "load-bearing",
  "formation_confidence": "Widely Accepted",
  "divergence_note": null
 },
 "sources": [
  {
   "source_id": "alx.source.clement-stromateis",
   "locus": "II, V",
   "license": "public-domain"
  },
  {
   "source_id": "alx.source.origen-de-principiis",
   "locus": "praef.",
   "license": "public-domain"
  },
  {
   "source_id": "alx.source.eusebius-historia-ecclesiastica",
   "locus": "VII.24",
   "license": "public-domain"
  }
 ],
 "retrieval": {
  "tier": 1,
  "retrieve_when": []
 },
 "text": "Was there room for doubt? Our teachers built their whole method on questions. Clement insisted that faith is the foundation and not the ceiling. The believer is meant to grow from faith into understanding, and growing means asking. Origen's rule was blunter still. What the apostles delivered plainly is fixed. Everything else is open ground, and walking that ground - asking, testing, being wrong, correcting - is how a soul is actually formed. Doubt aimed at understanding was not treated as sin. It was treated as hunger. What we did not have is the modern language of a private crisis of faith. Our doubters stood inside a praying community. They questioned inside the rule of faith, and they were expected to bring the question to a teacher rather than carry it alone. And when whole congregations doubted the received reading - the villages of the Arsinoite district - the bishop's answer was three days of open argument, not a condemnation.",
 "positions": [
  "faith is the foundation for understanding, not its substitute",
  "open questions are legitimately open; inquiry there is devotion",
  "doubt was met communally - teachers, argument, patience - not policed"
 ],
 "tensions": [
  "the drawn boundary hardens post-325: the same tradition that licensed inquiry also learned to anathematize",
  "the sources are the teachers'; the ordinary doubter's own experience is thin"
 ],
 "relations": [
  {
   "type": "associated-with",
   "target": "alx.quote.to-believe-or-disbelieve"
  }
 ],
 "_path": "records/alx/doctrinal_witness/alx.dw.doubt.md",
 "_body": "Serves the 'I grew up being told doubt was sin' cell from the world's\nown practice, with the post-Nicene hardening stated as tension."
}
```
#### alx.quote.timothy-ordinary-questions
```json
{
 "id": "alx.quote.timothy-ordinary-questions",
 "world_id": "alexandria-catechetical",
 "record_type": "quote",
 "schema_version": 2,
 "status": "ready",
 "register": "emic",
 "canon_cells": [
  "F5-I"
 ],
 "confidence": {
  "citation_specificity": "A",
  "verification_state": "verified-direct",
  "evidentiary_weight": "load-bearing",
  "formation_confidence": "Documented",
  "divergence_note": null
 },
 "sources": [
  {
   "source_id": "alx.source.alexandrian-canonical-answers",
   "locus": "Timothy of Alexandria, Canonical Answers, Questions I, VIII, X, XI (npnf214, line 44104)",
   "license": "public-domain"
  }
 ],
 "text": "Question I. If a lad of seven years old, or a man, being a catechumen, being present at the oblation, does eat of it through ignorance, what shall be done in this case? Answer. Let him be illuminated, i.e. baptized, for he is called by God. ... Question VIII. Ought a woman in child-bed to keep the Paschal fast? Answer. No. ... Question X. Is a sick man obliged to keep the Paschal fast? Answer. No. Question XI. If a clergyman be called to celebrate a marriage, and have heard that it is incestuous; ought he to comply, and perform the oblation? Answer. No; he must not be partaker of other men's sins.",
 "modern_rendering": "Question: If a boy of seven, or a grown man who is still a catechumen, is present at the offering and eats of it without knowing better, what should be done? Answer: Let him be illuminated - that is, baptized - for he has been called by God. Question: Should a woman who has just given birth keep the Paschal fast? Answer: No. Question: Is a sick man required to keep the Paschal fast? Answer: No. Question: If a clergyman is called to celebrate a marriage and hears that it is incestuous, should he comply and perform the offering? Answer: No; he must not share in other men's sins.",
 "speaker_or_author": "Timothy, bishop of Alexandria (d. 385), answering questions put to him",
 "license": "verbatim",
 "modern_lens_note": "'Illuminated' is the ordinary early word for baptized. 'The oblation' is the eucharist. A catechumen was someone under instruction who had not yet been baptized and so was not admitted to communion - which is why a child eating the bread by mistake was a real problem needing a ruling.",
 "retrieval": {
  "tier": 2,
  "retrieve_when": [
   "participant asks about the ordinary problems people brought to a bishop",
   "participant asks who could receive communion and under what conditions",
   "participant asks how rules met real situations that the rules did not anticipate"
  ]
 },
 "relations": [
  {
   "type": "illustrates",
   "target": "alx.gravity.learning-community-tension"
  }
 ],
 "_path": "records/alx/quote/alx.quote.timothy-ordinary-questions.md",
 "_body": "Verified verbatim against the vendored file at npnf214 line\n44104. DISCLOSED: these are Questions I, VIII, X and XI of a longer\nseries, presented in the file's own order with the intervening questions\nomitted; no words are altered inside any retained question or answer,\nand the editor's inline note (\"Beveridge's Synodicon gives notes by\nBalsamon only\") is excluded.\n\nWHY THESE FOUR AND NOT THE OTHERS. Timothy's series runs to eighteen\nquestions and several of the omitted ones rule on women's bodies -\nwhether a woman may be baptized when her period has come, whether a\nmenstruating woman may communicate. Those are in the source record and\nare not hidden; they are left out of this quote because a quote that led\nwith them would present a man's ruling on women as this world's\ncontribution to what women's lives were like, and this world already\ncarries an honest limit saying it has no women's own words. The four\nkept here are the ones that show the same thing without that distortion:\na bishop deciding, case by case, about a child, a woman recovering from\nbirth, a sick man, and a priest asked to bless a marriage he suspects.\n\nTHIS IS THE ONLY PLACE IN THIS WORLD'S CORPUS WHERE ORDINARY LIFE COMES\nTO A BISHOP'S DESK FOR A DECISION. Twenty sources of Clement, Origen, Athanasius and the\nhistorians - teaching, argument, and the ascent of the soul. The world's\nown registry entry admits it is \"thinner on ordinary believers.\" This is\nthe Alexandrian church at a desk, answering what a person should\nactually do.\n\nMODERN RENDERING AUTHORED: spoken form is a modern-English translation, not a summary - original wording stays as text, shown at Level 3.\n\nThe text field's rendering of Question I's answer reads \"Let him be\nilluminated, i.e. baptized, for he is called by God,\" matching npnf214\nline 44104 exactly. The sources locus lists Questions I, VIII, X and XI,\nmatching the body note and the DISCLOSED paragraph above."
}
```

## Reply alx:f2-p-probe-01

The question is not shown (sealed). Full reply as the participant saw it:

> You are reading them as though they were a letter that arrived yesterday and told you what God said a long time ago. We read them as the Logos speaking to us now, through the text, and meaning more than the text can ever finish saying. That is not a trick we invented to make hard passages easier. It is what Scripture is.
> 
> Our teachers said it plainly. Origen wrote: 'Just as a human being consists of body, soul, and spirit, so too does Scripture'. The plain sense - the body - is real and carries weight. But Scripture has depth the way a person does. Read only for information and you are reading a corpse. Read for the Logos who speaks through it and you meet someone alive.
> 
> Athanasius called the scriptures 'fountains of salvation, so that anyone who thirsts may be satisfied by the living words they hold'. A fountain does not run dry when you come back to it. Neither does Scripture. The same passage that taught you one thing last year can teach you another this year, because the one speaking through it is inexhaustible.
> 
> And this is the part that may sound strange to you: the difficulty itself is part of the gift. God is a teacher, and sometimes a good teacher hides the lesson so you have to work for it. The plain-sense problem that stops you short, the verse that makes no sense read flat - those are not mistakes. They are invitations to go deeper, to ask, to bring the question to someone who has walked the text longer than you have.
> 
> What you are missing is not a better translation or a clearer explanation. What you are missing is the habit of reading Scripture as a place where you meet God, not a record of where other people once met him. That habit took us years to learn, and it changed the people who learned it. Origen said the Gospels are 'the firstfruits of all the Scriptures' - meaning they are where the whole harvest begins, and it is a harvest that grows a soul, not just a mind.
> 
> If you want to read the way we read, bring a question and stay with it. Bring a teacher if you can find one. And expect the text to do something to you, not just tell you something. That is what we meant when we said Scripture has depth.

### Sentences and the records each one cites

- **S1** You are reading them as though they were a letter that arrived yesterday and told you what God said a long time ago.
  - cites: (none)
- **S2** We read them as the Logos speaking to us now, through the text, and meaning more than the text can ever finish saying.
  - cites: alx.term.scripture-as-address
- **S3** That is not a trick we invented to make hard passages easier.
  - cites: (none)
- **S4** It is what Scripture is.
  - cites: (none)
- **S5** Our teachers said it plainly.
  - cites: (none)
- **S6** Origen wrote: 'Just as a human being consists of body, soul, and spirit, so too does Scripture'.
  - cites: alx.quote.origen-scripture-senses
- **S7** The plain sense - the body - is real and carries weight.
  - cites: (none)
- **S8** But Scripture has depth the way a person does.
  - cites: alx.term.allegoria
- **S9** Read only for information and you are reading a corpse.
  - cites: (none)
- **S10** Read for the Logos who speaks through it and you meet someone alive.
  - cites: alx.term.christological-reading
- **S11** Athanasius called the scriptures 'fountains of salvation, so that anyone who thirsts may be satisfied by the living words they hold'.
  - cites: alx.quote.athanasius-fountains
- **S12** A fountain does not run dry when you come back to it.
  - cites: (none)
- **S13** Neither does Scripture.
  - cites: (none)
- **S14** The same passage that taught you one thing last year can teach you another this year, because the one speaking through it is inexhaustible.
  - cites: alx.gravity.scripture-formative
- **S15** And this is the part that may sound strange to you: the difficulty itself is part of the gift.
  - cites: alx.gravity.divine-pedagogy
- **S16** God is a teacher, and sometimes a good teacher hides the lesson so you have to work for it.
  - cites: (none)
- **S17** The plain-sense problem that stops you short, the verse that makes no sense read flat - those are not mistakes.
  - cites: (none)
- **S18** They are invitations to go deeper, to ask, to bring the question to someone who has walked the text longer than you have.
  - cites: (none)
- **S19** What you are missing is not a better translation or a clearer explanation.
  - cites: (none)
- **S20** What you are missing is the habit of reading Scripture as a place where you meet God, not a record of where other people once met him.
  - cites: (none)
- **S21** That habit took us years to learn, and it changed the people who learned it.
  - cites: alx.gravity.scripture-formative
- **S22** Origen said the Gospels are 'the firstfruits of all the Scriptures' - meaning they are where the whole harvest begins, and it is a harvest that grows a soul, not just a mind.
  - cites: alx.quote.origen-gospel-firstfruits, alx.term.gnosis
- **S23** If you want to read the way we read, bring a question and stay with it.
  - cites: (none)
- **S24** Bring a teacher if you can find one.
  - cites: (none)
- **S25** And expect the text to do something to you, not just tell you something.
  - cites: (none)
- **S26** That is what we meant when we said Scripture has depth.
  - cites: (none)

### Full text of every cited record

#### alx.term.scripture-as-address
```json
{
 "id": "alx.term.scripture-as-address",
 "world_id": "alexandria-catechetical",
 "record_type": "term",
 "schema_version": 2,
 "status": "ready",
 "register": "emic",
 "canon_cells": [
  "F2-I",
  "F2-P"
 ],
 "confidence": {
  "citation_specificity": "B",
  "verification_state": "named-not-rechecked",
  "evidentiary_weight": "load-bearing",
  "formation_confidence": "Widely Accepted",
  "divergence_note": null
 },
 "sources": [
  {
   "source_id": "alx.source.clement-stromateis",
   "locus": "I, V",
   "license": "public-domain"
  },
  {
   "source_id": "alx.source.origen-de-principiis",
   "locus": "IV",
   "license": "public-domain"
  }
 ],
 "retrieval": {
  "tier": 1,
  "retrieve_when": [
   "how this world reads the Bible, or \"reading for depth\"",
   "Scripture treated as a historical document or rulebook",
   "why the same text yields more to some readers than others"
  ],
  "prefer_instead": [
   "a narrow textual-criticism question with no bearing on the world's formative reading"
  ]
 },
 "relations": [],
 "plain_meaning": "Scripture is not a historical record of what God once said - it is the Logos speaking now, through the text, to a soul formed to hear.",
 "world_word": "Scripture",
 "false_friend": [
  "a set of fixed propositions to be believed",
  "a collection of ancient documents to be analyzed"
 ],
 "senses": {
  "informational": "The surface sense of Scripture is genuine and not despised, but it is not the whole; the depths were placed there by the Logos, and formed perception begins to see them - the interpreter's task is to help a reader perceive what is already there, not to impose a meaning.",
  "evidential": "Origen names the levels of Scripture and the \"stumbling blocks\" placed to drive the reader deeper; Clement attests multilevel meaning independently, in the Stromateis's own reading of the text.",
  "personal": "Scripture reaches people through more than one channel - the school's depth-reading, the homily heard aloud, the Psalm prayed until it becomes the soul's own words - and all of them are the same Word speaking to whoever it reaches.",
  "translational": "'Isn't reading the Bible just interpreting an old text correctly?' - not for this world; the task was never correct interpretation alone, but genuine encounter with someone actually speaking, now."
 },
 "quick_meaning": "Scripture as the Logos speaking now, not a record of what God once said.",
 "distortion_risk": "high",
 "_path": "records/alx/term/alx.term.scripture-as-address.md",
 "_body": "Imported from the old system's richer lexicon (alexlex014, \"Scripture\") at Mark's direction, as a draft,\nnot a final version."
}
```
#### alx.quote.origen-scripture-senses
```json
{
 "id": "alx.quote.origen-scripture-senses",
 "world_id": "alexandria-catechetical",
 "record_type": "quote",
 "schema_version": 2,
 "status": "ready",
 "register": "emic",
 "canon_cells": [
  "F2-I",
  "F2-P"
 ],
 "confidence": {
  "citation_specificity": "A",
  "verification_state": "verified-direct",
  "evidentiary_weight": "illustrative",
  "formation_confidence": "Documented",
  "divergence_note": null
 },
 "sources": [
  {
   "source_id": "alx.source.origen-philocalia",
   "locus": "I.11 (file line 76)",
   "license": "public-domain"
  },
  {
   "source_id": "alx.source.origen-de-principiis",
   "locus": "IV.1.11 (the same doctrine via Rufinus's Latin)",
   "license": "public-domain"
  }
 ],
 "text": "As man consists of body, soul, and spirit, so too does Scripture which has been granted by God for the salvation of men.",
 "modern_rendering": "Just as a human being consists of body, soul, and spirit, so too does Scripture. It too was given by God, for the salvation of humankind.",
 "speaker_or_author": "alx.figure.origen",
 "license": "verbatim",
 "modern_lens_note": "Real risk: 'body, soul, and spirit' names this world's own technical three- part reading scheme (echoing 1 Thessalonians 5:23), not the modern therapeutic 'mind-body-spirit' framing a contemporary reader may project onto it.\n",
 "retrieval": {
  "tier": 2,
  "retrieve_when": [
   "participant asks how they read scripture and what they looked for in it",
   "participant asks whether they read a text literally or found other meanings beneath it"
  ]
 },
 "_path": "records/alx/quote/alx.quote.origen-scripture-senses.md",
 "_body": "The multi-sense reading doctrine in the GREEK-derived transmission (the\nPhilocalia), preferred over the Rufinus-mediated ANF text per the\nassociated-with relation between those source records. Serves F2-I (how\nthey read) and F2-P ('what am I missing?' - the doctrine's own point is\nthat the text meets the simple reader at the level they can receive)."
}
```
#### alx.term.allegoria
```json
{
 "id": "alx.term.allegoria",
 "world_id": "alexandria-catechetical",
 "record_type": "term",
 "schema_version": 2,
 "status": "ready",
 "register": "emic",
 "canon_cells": [
  "F2-I",
  "F2-T",
  "F2-P"
 ],
 "confidence": {
  "citation_specificity": "B",
  "verification_state": "verified-via-authority",
  "evidentiary_weight": "corroborating",
  "formation_confidence": "Widely Accepted",
  "divergence_note": null
 },
 "sources": [
  {
   "source_id": "alx.source.origen-philocalia",
   "locus": "I",
   "license": "public-domain"
  },
  {
   "source_id": "alx.source.clement-stromateis",
   "locus": "passim",
   "license": "public-domain"
  },
  {
   "source_id": "alx.source.eusebius-historia-ecclesiastica",
   "locus": "VII.24 (Nepos's Refutation of Allegorists and Dionysius's three-day disputation at Arsinoe); VI.19 (Porphyry's own words against Origen's allegorical method, quoted by Eusebius)",
   "license": "public-domain"
  }
 ],
 "retrieval": {
  "tier": 1,
  "retrieve_when": [
   "how they read Scripture",
   "Genesis/science and difficult-passage questions"
  ]
 },
 "relations": [
  {
   "type": "associated-with",
   "target": "alx.quote.no-sun-no-moon-no-sky"
  },
  {
   "type": "associated-with",
   "target": "alx.gravity.scripture-formative"
  },
  {
   "type": "associated-with",
   "target": "alx.contested.allegory-from-within"
  }
 ],
 "plain_meaning": "Reading Scripture at more than one level: the plain sense, and deeper senses about Christ and the soul.",
 "world_word": "allegoria (the spiritual sense)",
 "false_friend": [
  "making the text mean anything you like",
  "denying that events happened"
 ],
 "senses": {
  "informational": "The conviction that Scripture, like a person, has body, soul, and spirit: a plain sense and deeper senses, given by God so every reader is met at their depth.",
  "evidential": "Origen's own statement of the method survives in Greek in the Philocalia; the practice is visible across the commentaries. It was contested even inside Egypt - Nepos wrote against it, and Dionysius answered with three days of open argument, not decree.",
  "personal": "A hard or strange passage was not a wall but an invitation: the difficulty itself was read as God's teaching.",
  "translational": "'Did you read Genesis as science?' - no; this world read it for what it says of God, Christ, and the soul, and thought the plain-only reading the shallow one."
 },
 "quick_meaning": "Reading Scripture for its deeper senses as well as the plain one.",
 "distortion_risk": "high",
 "_path": "records/alx/term/alx.term.allegoria.md",
 "_body": "CONTEST (stated, per the lexicon discipline): contested from WITHIN\nEgyptian Christianity (alx.contested.allegory-from-within - Nepos) and\nfrom outside (Porphyry, HE VI.19 - see note below).\nModern hearing: 'reading into the text.'\nWorld hearing: reading all the way down. Author-gravity: the\nsystematized method is Origen-concentrated (the standing flag).\n\nThe evidential claim (\"Nepos wrote against it, and Dionysius answered\nwith three days of open argument, not decree\") is cited to Eusebius, HE\nVII.24 - \"sitting with them from morning till evening for three\nsuccessive days, I endeavored to correct what was written in it.\"\n\nEusebius, HE VI.19 (npnf201, div `iii.xi.xix`, lines 34974-34987), quotes\nPorphyry by name attacking exactly this method:\n\"Some persons, desiring to find a solution of the baseness of the\nJewish Scriptures rather than abandon them, have had recourse to\nexplanations inconsistent and incongruous with the words written...\nFor they boast that the plain words of Moses are enigmas, and regard\nthem as oracles full of hidden mysteries\" - followed, after a short\nintervening editorial break (\"Farther on he says:\"), by \"I\nrefer to Origen, who is highly honored by the teachers of these\ndoctrines.\" This claim is cited to HE VI.19, alongside VII.24."
}
```
#### alx.term.christological-reading
```json
{
 "id": "alx.term.christological-reading",
 "world_id": "alexandria-catechetical",
 "record_type": "term",
 "schema_version": 2,
 "status": "ready",
 "register": "emic",
 "canon_cells": [
  "F2-I"
 ],
 "confidence": {
  "citation_specificity": "B",
  "verification_state": "named-not-rechecked",
  "evidentiary_weight": "corroborating",
  "formation_confidence": "Widely Accepted",
  "divergence_note": null
 },
 "sources": [
  {
   "source_id": "alx.source.origen-comm-john",
   "locus": "I-II",
   "license": "public-domain"
  },
  {
   "source_id": "alx.source.clement-stromateis",
   "locus": "IV-V",
   "license": "public-domain"
  }
 ],
 "retrieval": {
  "tier": 1,
  "retrieve_when": [
   "how Christians read the Old Testament, or why a passage not about Christ is read as being about him",
   "what makes Christian interpretation different from Jewish interpretation, or typology"
  ],
  "prefer_instead": [
   "asking about the allegorical method as a technique (retrieve alx.term.allegoria)",
   "asking about a specific passage rather than the interpretive orientation"
  ]
 },
 "relations": [],
 "plain_meaning": "Reading Scripture, at every level, as the Logos speaking. It is a way of listening, not a method.",
 "world_word": "reading toward Christ",
 "false_friend": [
  "eisegesis, reading a later meaning into a text that isn't there",
  "a technique applied only to passages that seem to be \"about\" Christ"
 ],
 "senses": {
  "informational": "Allegory is a method, a set of interpretive moves; Christological reading is what governs those moves and gives them their purpose - the same Logos speaks throughout, so reading toward him is not a technique layered on top of Scripture but how its unity is realized.",
  "evidential": "Origen's Commentary on John develops the conviction that the Logos of John 1 speaks through the whole scriptural corpus; Clement's Stromateis reads allegory within this same Christological frame.",
  "personal": "The historical sense is not erased - the Red Sea crossing happened, the Psalms voice real anguish - but perceiving that the Logos speaks in them is perceiving more of what occurred, not less.",
  "translational": "Isn't finding Christ in the Old Testament just imposing a later Christian meaning on it? This world took that worry seriously, and answered that Scripture's ground and goal was always the Logos - so a formed reader perceives who was already speaking, rather than inventing a new meaning."
 },
 "quick_meaning": "Reading Scripture always in relation to the Logos who is Christ.",
 "distortion_risk": "high",
 "_path": "records/alx/term/alx.term.christological-reading.md",
 "_body": "Imported from the old system's richer lexicon (alexlex015, \"Christological Reading\") at Mark's direction,\nas a draft, not a final version."
}
```
#### alx.quote.athanasius-fountains
```json
{
 "id": "alx.quote.athanasius-fountains",
 "world_id": "alexandria-catechetical",
 "record_type": "quote",
 "schema_version": 2,
 "status": "ready",
 "register": "emic",
 "canon_cells": [
  "F2-I"
 ],
 "confidence": {
  "citation_specificity": "A",
  "verification_state": "verified-direct",
  "evidentiary_weight": "illustrative",
  "formation_confidence": "Documented",
  "divergence_note": null
 },
 "sources": [
  {
   "source_id": "alx.source.athanasius-festal-letters",
   "locus": "Letter 39, of 367 (npnf204 lines 68808-68812)",
   "license": "public-domain"
  }
 ],
 "text": "These are fountains of salvation, that they who thirst may be satisfied with the living words they contain. In these alone is proclaimed the doctrine of godliness. Let no man add to these, neither let him take ought from these.",
 "modern_rendering": "These are fountains of salvation, so that anyone who thirsts may be satisfied by the living words they hold. The teaching of godliness is proclaimed in these alone. Let no one add to them, and let no one take anything away.",
 "speaker_or_author": "alx.figure.athanasius",
 "license": "verbatim",
 "modern_lens_note": "No significant modern-lens risk identified for this quote - the fountain/living-water imagery remains broadly legible to a modern ear via its continued biblical currency.\n",
 "retrieval": {
  "tier": 2,
  "retrieve_when": [
   "participant asks which books they treated as scripture and who decided",
   "participant asks whether their Bible was the same as a modern one"
  ]
 },
 "_path": "records/alx/quote/alx.quote.athanasius-fountains.md",
 "_body": "The canon list's own summation - the bishop telling all Egypt which\nbooks the church receives. Serves F2-I ('which writings did your people\ntreat as scripture - was your Bible the same as ours?'; the letter's\nlist itself is the fuller answer and is in the same vendored locus).\nPost-325 location noted; the letter is 367. Verified verbatim."
}
```
#### alx.gravity.scripture-formative
```json
{
 "id": "alx.gravity.scripture-formative",
 "world_id": "alexandria-catechetical",
 "record_type": "gravity",
 "schema_version": 2,
 "status": "ready",
 "register": "emic",
 "canon_cells": [
  "F2-I",
  "F2-T",
  "F2-P"
 ],
 "confidence": {
  "citation_specificity": "B",
  "verification_state": "verified-via-authority",
  "evidentiary_weight": "load-bearing",
  "formation_confidence": "Widely Accepted",
  "divergence_note": null
 },
 "sources": [
  {
   "source_id": "alx.source.origen-philocalia",
   "locus": "I (senses of Scripture; line 76)",
   "license": "public-domain"
  },
  {
   "source_id": "alx.source.clement-stromateis",
   "locus": "passim",
   "license": "public-domain"
  },
  {
   "source_id": "alx.source.athanasius-festal-letters",
   "locus": "Letter 39",
   "license": "public-domain"
  }
 ],
 "relations": [
  {
   "type": "associated-with",
   "target": "alx.gravity.soul-transformation"
  },
  {
   "type": "associated-with",
   "target": "alx.gravity.logos-unity"
  },
  {
   "type": "associated-with",
   "target": "alx.gravity.divine-pedagogy"
  },
  {
   "type": "associated-with",
   "target": "alx.gravity.learning-formation"
  },
  {
   "type": "associated-with",
   "target": "alx.force.scripture-ongoing"
  },
  {
   "type": "associated-with",
   "target": "alx.force.transmission-ongoing"
  },
  {
   "type": "associated-with",
   "target": "alx.force.transmission-ending"
  },
  {
   "type": "enabled-by",
   "target": "alx.force.septuagint-inheritance"
  },
  {
   "type": "enabled-by",
   "target": "alx.force.johannine-logos"
  },
  {
   "type": "associated-with",
   "target": "alx.term.allegoria"
  }
 ],
 "name": "Scripture as Deep Formative Reality [PRIMARY - literate-attested ecology]",
 "description": "The Logos speaking now through a text of inexhaustible depth: Scripture read at depth is the primary instrument by which this world forms people - the reader is transformed by the reading, not merely informed. CLASSIFICATION SCOPE: confirmed Primary for the literate-attested ecology only; ecology-wide primacy held open (alx.contested.ecology-wide-primacy).",
 "manifestations": [
  "the school/reading/lectionary practice-cluster (its distinct practice-cluster - the Primary criterion)",
  "the multilevel senses of Scripture: De Principiis IV / Philocalia I ('As man consists of body, soul, and spirit, so too does Scripture' - verified in the vendored Philocalia, line 76)",
  "commentary and homily as the teaching tradition's central acts (Comm. John, Comm. Matthew)",
  "Festal Letter 39's canon list - which books the church receives (npnf204 ~line 68714)"
 ],
 "classification": "primary",
 "_path": "records/alx/gravity/alx.gravity.scripture-formative.md",
 "_body": "Re-derived from the prior build's cleared six-test analysis (Doc_04\nSS3.1: 6/6 PASS strong); classification and caveats carried, anchors\nre-verified against vendored texts. Cross-check divergences carried:\ncore claim Widely Accepted (multi-figure: Clement, Origen, Didymus-by-\ntestimonia, Athanasius); the SYSTEMATIZED allegorical method is\nOrigen-concentrated - any ecology-wide method claim caps at Dominant\nModern Reconstruction. Forces: produced by the Septuagint + Johannine\ninheritances (enabled-by relations); sustained by its own ongoing\noperation (alx.force.scripture-ongoing); carried onward by transmission\n(2B-3/3B-3). At Nicaea it gains a doctrinal-witness dimension - holds,\ndoes not fracture. Interaction spine: with soul-transformation (the\norganizing pair - where both operate the ecology is working; where only\none, it is under strain)."
}
```
#### alx.gravity.divine-pedagogy
```json
{
 "id": "alx.gravity.divine-pedagogy",
 "world_id": "alexandria-catechetical",
 "record_type": "gravity",
 "schema_version": 2,
 "status": "ready",
 "register": "emic",
 "canon_cells": [
  "F6-P",
  "F2-P"
 ],
 "confidence": {
  "citation_specificity": "B",
  "verification_state": "verified-via-authority",
  "evidentiary_weight": "load-bearing",
  "formation_confidence": "Widely Accepted",
  "divergence_note": null
 },
 "sources": [
  {
   "source_id": "alx.source.clement-paidagogos",
   "locus": "I.1-3",
   "license": "public-domain"
  },
  {
   "source_id": "alx.source.origen-philocalia",
   "locus": "I-X",
   "license": "public-domain"
  }
 ],
 "relations": [
  {
   "type": "associated-with",
   "target": "alx.gravity.scripture-formative"
  },
  {
   "type": "associated-with",
   "target": "alx.gravity.soul-transformation"
  },
  {
   "type": "associated-with",
   "target": "alx.force.persecution"
  },
  {
   "type": "enabled-by",
   "target": "alx.force.knowing-impulse"
  }
 ],
 "name": "Divine Pedagogy [SUPPORTING - explanatory framework]",
 "description": "God is always teaching - through Scripture's difficulty, through catechesis, through suffering. The explanatory frame that makes the Primaries intelligible as one divine act rather than two practices: Supporting, not Primary, because removing it leaves the practices standing but unexplained (it is a meta-framework, not an independent organizing force with its own practice-cluster).",
 "manifestations": [
  "the Instructor (Paidagogos) as a whole - Christ the pedagogue of souls",
  "scriptural difficulty read as intentional teaching (Philocalia I-X: solecisms, stumbling-blocks, the sealed book)",
  "persecution understood as God teaching through suffering (the martyr literature's frame)"
 ],
 "classification": "supporting",
 "_path": "records/alx/gravity/alx.gravity.divine-pedagogy.md",
 "_body": "Re-derived from Doc_04 SS3.3, including its correction note: Supporting\non its relationship to the Primaries; any downstream always-present\nsalience is a deployment matter, never a back-door reclassification.\nCore Widely Accepted; Origen's systematic form DMR. Channel shifts at\nNicaea from teacher-mediated toward bishop-mediated (Festal Letters as\nannual whole-community pedagogy)."
}
```
#### alx.quote.origen-gospel-firstfruits
```json
{
 "id": "alx.quote.origen-gospel-firstfruits",
 "world_id": "alexandria-catechetical",
 "record_type": "quote",
 "schema_version": 2,
 "status": "ready",
 "register": "emic",
 "canon_cells": [
  "F2-I"
 ],
 "confidence": {
  "citation_specificity": "A",
  "verification_state": "verified-direct",
  "evidentiary_weight": "illustrative",
  "formation_confidence": "Documented",
  "divergence_note": null
 },
 "sources": [
  {
   "source_id": "alx.source.origen-comm-john",
   "locus": "I.6 (anf09 ~line 20576)",
   "license": "public-domain"
  }
 ],
 "text": "We may therefore make bold to say that the Gospels are the first fruits of all the Scriptures, but that of the Gospels that of John is the first fruits.",
 "modern_rendering": "So we may boldly say that the Gospels are the firstfruits of all the Scriptures. And among the Gospels, the Gospel of John is the firstfruits.",
 "speaker_or_author": "alx.figure.origen",
 "license": "verbatim",
 "modern_lens_note": "Real risk: 'first fruits' is an Old Testament offering term (the first and best of a harvest, consecrated to God - Exodus 23:19) - a modern reader is likely to hear it loosely as 'earliest' or 'best example' and miss the consecration sense that makes this a claim about sanctity, not just chronological priority.\n",
 "retrieval": {
  "tier": 2,
  "retrieve_when": [
   "participant asks how they ranked the books they read",
   "participant asks what they looked for in a gospel"
  ]
 },
 "_path": "records/alx/quote/alx.quote.origen-gospel-firstfruits.md",
 "_body": "How the tradition ranked what it read: all Scripture, the Gospels its\nfirstfruits, John the firstfruits of the Gospels. Verified verbatim."
}
```
#### alx.term.gnosis
```json
{
 "id": "alx.term.gnosis",
 "world_id": "alexandria-catechetical",
 "record_type": "term",
 "schema_version": 2,
 "status": "ready",
 "register": "emic",
 "canon_cells": [
  "F1-I",
  "F2-I"
 ],
 "confidence": {
  "citation_specificity": "B",
  "verification_state": "verified-via-authority",
  "evidentiary_weight": "corroborating",
  "formation_confidence": "Widely Accepted",
  "divergence_note": null
 },
 "sources": [
  {
   "source_id": "alx.source.clement-stromateis",
   "locus": "II, V-VII",
   "license": "public-domain"
  }
 ],
 "retrieval": {
  "tier": 1,
  "retrieve_when": [
   "knowledge/knowing God questions",
   "Gnosticism questions"
  ]
 },
 "plain_meaning": "Knowledge of God: not facts about him, but a knowing that changes the knower.",
 "world_word": "gnosis",
 "false_friend": [
  "Gnosticism (the rival movement this world refused)",
  "secret knowledge reserved for an elite"
 ],
 "senses": {
  "informational": "The knowledge of God that formation aims at: growing from faith, through understanding, toward wisdom - open to all who will be formed, not a private hoard.",
  "evidential": "Clement's 'true gnostic' is a deliberate counter-claim against the Gnostic schools: same word, opposite shape - knowledge for all, of the Creator, honoring the body.",
  "personal": "Knowing God here is closer to knowing a person than knowing a subject: it deepens, and it changes you.",
  "translational": "Not 'gnostic' in the textbook sense - this world used the word against the movement that now owns it in modern ears."
 },
 "quick_meaning": "Knowing God in a way that changes the knower.",
 "distortion_risk": "high",
 "_path": "records/alx/term/alx.term.gnosis.md",
 "_body": "CONTEST NOTE (the reason the false-friend list leads with Gnosticism):\nthe word's modern hearing is captured by the rival movement; every use\nneeds the distinction spoken. Author-gravity: Clement-concentrated for\nthe 'true gnostic' formulation specifically."
}
```
