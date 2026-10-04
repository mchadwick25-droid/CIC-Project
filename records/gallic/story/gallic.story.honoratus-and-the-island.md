---
id: gallic.story.honoratus-and-the-island
world_id: gallic-monastic-ascetic-christianity
record_type: story
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: B
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Contested
  divergence_note: >-
    Contested for the formation portrait (the founder who flees rank, tames a waste, and is overtaken
    by the priesthood while keeping a monk's humility inside it); Inferential-Thin for the specific
    events - and, unlike every other story in this repository, Inferential-Thin for the wording itself:
    the English rests on the Doc_09 builder's own rendering of rough OCR of the Latin (Migne PL 50,
    vendored file lines c. 660-722), with the presence of every rendered phrase checkable by grep at
    the lines given and its sense not verified against a critical edition. One OCR word ("aridilabus")
    is left unrendered and said so. The Latin is normalized from OCR whose own spellings differ
    ("iunectit," "dia evitati," "llonoratus"). The sermon's existence and attribution are independently
    attested by Gennadius ch. LXX (ancient text: "his Life of Saint Honoratus, his predecessor"). The
    Representative must not quote the English here as Hilary's words - only as a rendering. Verification
    is direct as to presence (the lines were read directly at Doc_09), not as to sense.
sources:
- source_id: gallic.source.hilary-arles-vita-honorati
  locus: 'Sermo de Vita Sancti Honorati, the paragraphs Migne numbers 16-17 with the unnumbered paragraph preceding them (vendored file lines c. 660-722): "Vacantem itaque insulam" through "Fugit horror solitudinis, cedit turba serpentium"; "Quid longius morer"; "Hic primum illigatur ... ad ipsum dignitas venit" (c. 714-716); "tam integram in sacerdotio monachi humilitatem conservabat, quam plene monachus sacerdotii merita possederat" (c. 668/722) - rough OCR, wording Inferential-Thin'
  license: public-domain
- source_id: gallic.source.gennadius-de-viris-illustribus
  locus: 'De Viris Illustribus ch. LXX (npnf203, ancient text): "his Life of Saint Honoratus, his predecessor" - attests the sermon''s existence and attribution'
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - participant asks how Lerins was founded, who Honoratus was, or whether the south told stories of its own founders
  - participant uses "island," "Lerins," "founder," "reluctant bishop"
  - conversation reaches the monk-bishop at the Lerins node in the node's own Latin, the harbour image of Egypt as the measure, or the cross-node capture-shape
  - Representative needs the one story Lerins's own insiders tell of Lerins
  prefer_instead:
  - participant is asking about daily life at Lerins - this story does not describe it, and nothing in our evidence does
  - participant wants Honoratus's later episcopate at Arles as history - the sermon is a disciple's funeral eulogy, and this story stops at the island
claim_guards:
- participant wants exact wording - the Representative must not quote this record's English as Hilary's, only as a rendering
relations:
- type: associated-with
  target: gallic.figure.honoratus
- type: associated-with
  target: gallic.story.election-at-tours
- type: associated-with
  target: gallic.story.bishop-archebius
- type: illustrates
  target: gallic.gravity.monk-bishop
- type: associated-with
  target: gallic.gravity.egypt-as-measure
- type: associated-with
  target: gallic.gravity.virtus
narrative_tier: 3
narrative_tier_justification: >-
  Tier 3 - Attributed Tradition - by the governing framework's own description: hagiographic narrative
  is a specific type within this tier, and the account of what a formed life looks like is itself
  genuine formation evidence while the specific events claimed are not. This is a disciple's funeral
  sermon on his master, a genre that idealizes by design; its markers are all present - the founder who
  flees rank, the waste tamed by a psalm, the serpents that yield, a "camp of God" lit by "angelic
  offices," the office that overtakes the fugitive. Gennadius (ch. LXX) independently attests that
  Hilary wrote "his Life of Saint Honoratus, his predecessor" - so the tradition's existence and
  attribution are secure - but the sermon's claims about events are exactly what the tier says they
  are: the tradition's witness to what it believed a formed life could become. Why not Tier 1, though
  the author is named, socially located, and close: because the genre is the decisive fact, as for the
  two Tier 3 Tours stories, and because - a limit peculiar to this story - the build cannot yet read the
  whole sermon and cannot vouch for the sense of its own renderings; Contested for the portrait,
  Inferential-Thin not only for events but for wording. Recorded rather than resolved: whether a story
  whose wording is Inferential-Thin should be built at all. It is built - bounded to the lines actually
  read, nothing supplied from outside them - because the alternative would leave the bishop-forming
  house with no story at all, and because the presence of every element is checkable by grep. A full
  read of the sermon with a stated translation method would let a future pass confirm, correct, or
  extend it.
tellable_as: >-
  Honoratus goes unafraid onto an island shunned for its squalor and serpents, carrying a psalm; the
  serpents give way, a camp of God rises where no one would live - and there "the priestly fillet
  fastens on its fugitive."
text: >-
  This is how the tradition of Lerins remembers its founder - as far as these lines can be read, as
  the disciple who succeeded him at Arles and preached his life at his death told it.

  Honoratus, Hilary says, had been drawn from his homeland by desire for the desert, and Christ
  invited him into a desert near this city - in eremum huic urbi propinquam - an island that stood
  empty because of the excess of its squalor and was unapproachable for fear of venomous creatures,
  lying not far under the Alpine ridge. Besides the opportunity of seclusion, he was drawn there by
  the nearness and love of the bishop Leontius, a holy and most blessed man in Christ - though many,
  in a new boldness, tried to hold him back, the neighbours telling him of that terrible desolation,
  competing in the ambition of faith to keep him within their own borders. But he, impatient of
  human society and longing to be cut off from the world even by the barrier of the sea, carried in
  heart and mouth, now to himself, now to his own, the psalm Thou shalt walk upon the asp and the
  basilisk, and trample the lion and the dragon, and the Lord's promise, Behold, I have given you
  power to tread upon serpents and scorpions. So he goes in unafraid, Hilary says, and scatters the
  fear of his own by his own security. The horror of the solitude flees; the crowd of serpents gives
  way. Hilary counts it among his master's miracles and merits - inter miracula ac merita - that the
  serpents, so often met in those parts, as we have seen, stirred up especially by the sea's heat,
  were never a danger to anyone, nor even a fear.

  The sermon goes on to ask why it should delay longer. With Christ, so to speak, co-operating,
  every adversity that had deterred men before was overcome, and your Honoratus pitched a certain
  camp of God there; the place that had long driven men from dwelling in it is lit up by angelic
  offices. The hiding-place is illuminated while the light is hidden.

  And then the sentence the tradition of Lerins is remembered by: here he was first bound to the
  long-avoided office of the clergy; here the priestly fillet fastens on its fugitive; and he who
  had refused to go to the dignity - the dignity came to him. Hic primum illigatur diu evitati
  clericatus officio; hic refugam suum sacerdotalis infula innectit; et qui ire ad dignitatem
  detrectaverat, ad ipsum dignitas venit. He appeared there a presbyter worthy of honour not twofold
  only but manifold - and he kept a monk's humility as entire in the priesthood as, when a monk, he
  had fully possessed the merits of the priesthood.
absent_detail: >-
  What a participant might reasonably expect here, and cannot have, is a story from inside Lerins - a
  day, a rule kept, a novice received, an elder's saying, a monk's prayer on the island. This is the
  closest our Native corpus comes, and it is a story about the founder's arrival and his elevation,
  told at his funeral by the man who succeeded him as a bishop: it narrates the island's edges (the
  serpents at the shore; the fillet that took him off it), not its interior. The silence is partly a
  transmission gap - Hilary's sermon exists in full, unread here beyond these lines; Eucherius's In
  Praise of the Desert is in the same condition - and partly our own: Vincent, the one Lerins voice
  read in full, tells nothing of the island but that he dwells "in the seclusion of a Monastery." The
  honest position is that we can tell how the founder came to Lerins and how he left it, and not what
  he or anyone did there in between. One OCR word for the place where serpents were met is left
  unrendered.
modern_contrast: >-
  A modern reader expects a monastery's founding story to describe the monastery - its rule, its day,
  its first novices. Lerins's own founding story, as far as it can be read, describes a shore: squalor,
  serpents, a psalm carried in heart and mouth, and then the office that came for the man who had fled
  it. And it admits inside the south what Cassian refused in his own books - a wonder counted inter
  miracula ac merita - so that the refusal of wonder-stories was Cassian's, not the whole south's.
use_note:
  means: "Hilary of Arles preached that Honoratus went unafraid onto a serpent-shunned island carrying a psalm, the serpents gave way, and the priestly fillet fastened on its fugitive."
  not_for:
    - "daily life at Lerins, which nothing in the record describes"
    - "Honoratus's later episcopate at Arles as history, when the sermon is a disciple's eulogy that stops at the island"
    - "an exact reading of Hilary's Latin, when the wording is rough OCR rendered only as far as it can be read"
    - "Martin's election, which sits in gallic.story.election-at-tours"
  years: {from: 429, to: 430}
  status: reviewed
---
Grounded in Hilary of Arles's Sermo de Vita Sancti Honorati (Migne PL 50, vendored file lines c.
660-722, rough OCR); the disclosure of the wording's own Inferential-Thin status, the unrendered OCR
word, and Gennadius's independent attestation of the sermon are all carried above in the
divergence_note. Nothing is supplied from outside those lines: nothing about Honoratus at Arles,
nothing about the island's daily life. Cross-node pairing with gallic.story.election-at-tours and
gallic.story.bishop-archebius is declared as story-to-story associated-with relations; the
resemblance is this record's own finding, not the sermon's own claim - it does not mention Martin,
and Sulpitius never mentions Lerins.

This story's own relations to this world's gravities are declared in full in its `relations[]`
field above, reciprocal edges declared on each target.
