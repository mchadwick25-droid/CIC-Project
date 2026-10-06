---
id: desert.search.unopened-volume-sweep
world_id: desert-monasticism
record_type: search_record
schema_version: 2
status: draft
register: etic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Documented
  divergence_note: >-
    Every finding here was read from the vendored files directly, not from catalogue metadata. The
    three declinations below are rulings on evidence, and each names what would reverse it.
sources: []
query: "Every vendored volume on cross_world's second-hand-source list for this world - volumes whose principal author this world NAMES in its records while never opening that author's own works. Six at the start of the sweep: anf02, anf04, anf09, npnf208, npnf214, origen_philocalia_lewis1911.txt"
result: found
channel: "direct reading of the vendored files in cic/texts, 2026-08-27, plus a trace of which name in which record triggered each match"
found_sources: [desert.source.origen-de-principiis, desert.source.origen-philocalia, desert.source.origen-commentary-matthew]
note: "THREE OPENED, THREE DECLINED. Opened: anf04 (De Principiis - the doctrine the Origenist controversy was actually about, which this world could name and not state), origen_philocalia_lewis1911.txt (the curated Origen, and the Greek check on Rufinus' Latin), anf09 (Origen on Matthew 18 and the sinning brother, set against desert.story.moses-leaking-jug). Declined with reasons: anf02 (the matched author is Theophilus OF ANTIOCH, c. 180; this world names Theophilus OF ALEXANDRIA, d. 412 - a homonym, two men two centuries apart), npnf208 (the sole Basil match is a cross-world caution stating that Rousseau's Basil monograph belongs to World #5 and NOT here - the check matched a sentence whose whole purpose is to say this world does not do Basil), npnf214 (the sole Chalcedon match names the council of 451 as lying past this world's c. 430 boundary and says in the same clause 'Not directly attested within this world'). ALL THREE DECLINED VOLUMES REMAIN ON THE OBSERVER'S LIST and should. The observer is an observation, not a gate, and the right response to two of these is a note here rather than a change to the check. END STATE: six volumes down to three, and the three left are exactly the three ruled declined above. TWO SELF-INFLICTED ERRORS ON THE WAY THERE, both recorded in the body because both are traps for the next sweep."
---
WHAT THE SWEEP WAS FOR. cross_world's second-hand-source observer asks a
real question - is this world naming an author it has never actually
read? - and it had six answers for desert. The answers turned out to be
three different things, and the difference is worth recording because the
same three shapes will recur for every other world swept.

SHAPE ONE: A REAL GAP. This world names Origen constantly. Its closing
force is the Origenist controversy. Its most systematized strand is
Evagrian, which is to say Origenist. It had never opened a line of
Origen, and so it could report that a fight happened over him without
being able to say what the fight was about. Three volumes, three
different reasons to want them, all opened - see found_sources above and
desert.quote.god-is-not-a-body, which is the sentence the whole affair
turns on.

SHAPE TWO: A HOMONYM. anf02 matched on "Theophilus" and the Theophilus in
that volume is the bishop of Antioch who wrote To Autolycus around 180.
The Theophilus this world names is the patriarch of Alexandria who
reversed himself in 399 and drove the Tall Brothers out of Egypt. Two
men, two centuries, one name. The observer's own code comment already
worries about exactly this class of error - it records catching
"Basilidean" matching Basil and "Leonides" matching Leo - and word
boundaries do not help when the collision is a real full name. WHAT WOULD
REVERSE THIS: nothing about Theophilus of Antioch. If this world ever
wants the second-century apologists it should open anf02 for Tatian or
Athenagoras on their own merits, and this declination would not be the
reason it had not.

SHAPE THREE: A NEGATIVE MENTION. npnf208 and npnf214 both matched on a
sentence written to EXCLUDE the thing matched. The Basil mention is
desert.source.rousseau-pachomius' cross-world caution that Rousseau's
Basil book belongs to the Cappadocian world and must not be conflated
with his Pachomius book. The Chalcedon mention is
desert.force.centralization-trend saying the trend runs on past this
world's boundary toward 451, "of which the Origenist controversy is one
early instance. Not directly attested within this world". In both cases
the check is measuring the presence of a word in a disclaimer. That is
not a defect in the check worth coding around - a world that mentions a
council is a world that might want it, and the observer is right to ask -
but it is a defect in reading the check's output as a worklist. WHAT
WOULD REVERSE THESE: for npnf208, evidence that Basilian monastic
legislation bore on Egyptian practice inside this world's window, which
this world has not seen; for npnf214, any use of a conciliar canon as
evidence about this world rather than about what came after it.

THE RULE THIS SWEEP PROPOSES for the other five worlds, offered rather
than imposed: trace the match to the record and the field before deciding
anything. Three of six matches here were answered by reading one sentence
of this world's own records. Only after that is it worth opening the
volume, and then the question is not whether the author is named but
whether the volume answers something this world already asks and cannot
answer. anf09 was nearly declined on that test and reversed on it, which
is the test working rather than failing.

TWO ERRORS I MADE DURING THE SWEEP, kept because each is a trap the next
world's sweep will meet.

FIRST: A TRAILING PERIOD SILENTLY UNDOES AN OPENING. The observer decides
what a world has "opened" by matching `cic/texts/([\w.-]+)` against each
source record's `edition` field. A dot is inside that character class. So
an edition reading "vendored as cic/texts/anf04_....xml. De Principiis
runs from..." captures the filename WITH THE TRAILING PERIOD ATTACHED,
which matches no file, and the volume goes on registering as unopened
however carefully the record was written. Two of the three volumes opened
by this sweep did exactly that and looked like failures until the paths
were reworded to end at a space or a hyphen. The rest of the fleet was
then checked for the same defect - every `cic/texts/` path in every
`edition` field across all seven record sets, resolved against the actual
directory listing - and none was found, so this is a live trap rather
than existing damage. A record writer should end the path with a space.

SECOND: OPENING A VOLUME CAN PUT A NEW ONE ON THE LIST. The first draft
of desert.source.origen-de-principiis mentioned, in passing, that the
same ANF volume carries Origen's correspondence with Julius Africanus.
That put anf06 on this world's second-hand list, on the strength of an
aside about the canonicity of Susanna, which is not this world's
business in any way. The mention was removed rather than a seventh
declination written for it. The general point: this observer measures
NAMES IN FIELDS, so naming an author incidentally is not free, and a
source record's `work` field should name what the world holds the volume
for, not everything the volume contains.
