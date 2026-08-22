---
id: desert.force.melitian-rivalry
world_id: desert-monasticism
record_type: force
schema_version: 2
status: draft
register: etic
canon_cells: [F3-T]
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: contested
  formation_confidence: Documented
  divergence_note: "Documented as to the Melitian communities' own existence and rough contemporaneity with this world's Nicene-communion material. Inferential/Thin as to whether Melitian and Nicene-communion ascetic practice were organizationally distinguishable in ordinary daily life - Doc_01 SS11 item 1, still unresolved, carried forward again here rather than resolved. formation_confidence set to Documented, the dominant registered rating, rather than Contested, a value no registered record assigns this specific split; the Inferential/Thin half is carried in full above, not suppressed by the single enum value. The other three registered sources bear on this force's Layer 2 reading rather than its confidence rating: brakke-athanasius supports reading this world's literary self-presentation as authored, not neutral; athanasius-vita-antonii supplies the Vita's own two Melitian mentions; apophthegmata-patrum supplies the sayings tradition's own comparable silence. This record's Layer 2 claim is scoped to the Vita and the sayings tradition specifically, not to Athanasius's wider corpus: the same vendored volume names the Melitians well over a hundred times elsewhere (chiefly the Apologia contra Arianos), including, at Apol. Ar. SS67, a letter naming individual Melitian monks (Pinnes, Helias, Paphnutius) the volume's own Introduction cites as proof organized Melitian monasticism existed. That material is polemical and institutional, not about Melitian ascetics as ongoing rival co-participants in this world's own formation logic, and has not been independently incorporated here - flagged as a genuine open item (DOC08-INDEX.md's own open items list) rather than folded in without full verification, per Doc08 Round 3 review Finding S1."
sources:
- source_id: desert.source.nepheros-archive
  locus: "the Melitian community's own documentary archive, the material basis for this force's own Layer 1 - caveated per that source's own two standing cautions: Melitian-for-Nicene-communion representativeness is an unverified working assumption, and the editors' own 'intermediary' organizational reading does not map cleanly onto this world's three strands"
- source_id: desert.source.brakke-athanasius
  locus: "the Vita's own status as a theologically and politically motivated literary construction serving Athanasius's anti-Arian, pro-episcopal program - the basis for reading this world's own literary self-presentation as authored, not neutral"
- source_id: desert.source.athanasius-vita-antonii
  locus: "SS68 - Athanasius narrating that Antony 'never held communion with the Meletian schismatics, knowing their wickedness and apostacy from the beginning'; SS89 - Athanasius narrating Antony's own deathbed exhortation to 'have nought to do with the Meletian schismatics, for you know their wicked and profane character'"
  license: public-domain
- source_id: desert.source.apophthegmata-patrum
  locus: "the sayings tradition's own comparable silence about Melitian ascetics as a named, ongoing presence (compiler-mediated, per this source's own compiler screen)"
name: "The Melitian schism as a persistent, doctrinally distinct rival ascetic movement [2A - ongoing/external]"
kind: ongoing
description: "A rival, ecclesiastically distinct ascetic movement occupying the same geographic and social space as this world's own Nicene-communion material throughout its active life, with its own monastic archive and organizational forms. This world's own Nicene-communion sources are essentially silent about Melitian ascetics as a live, named rival presence - a silence this record reads as potentially informative rather than neutral, given Athanasius's own documented role - per Doc_02 SS6, cited as background rather than to a registered source record - as the Melitian schism's most powerful ecclesiastical adversary: this world's own literary self-presentation, produced substantially under his influence (desert.source.brakke-athanasius's own reading of the Vita as a theologically and politically motivated construction), had reason not to dwell on Melitian ascetic communities as legitimate co-participants in the same formation logic."
manifestations:
- "the Nepheros archive's own Melitian community, documented in the same period and region as the Nicene-communion material this world otherwise centers"
- "the Vita itself naming the Melitians only twice, both times to have Antony reject them - once narrating that he never held communion with them (Vita SS68), once in Antony's own reported deathbed exhortation to 'have nought to do' with them (SS89, the founder's dying instruction) - rather than engaging them as ongoing ascetic co-participants: deliberate polemical non-recognition within this world's own founding narrative specifically, not a claim that Athanasius's writing generally is silent about the Melitians (it is not - see divergence_note); and the sayings tradition's own comparable silence about Melitian ascetics as a named, ongoing presence (compiler-mediated)"
relations:
- type: associated-with
  target: desert.gravity.economic-embeddedness
- type: associated-with
  target: desert.contested.strand-porousness
- type: associated-with
  target: desert.quote.antony-arians-serpents
---
Re-derived from the prior build's cleared Doc_08 Cell 2A-ii. This
record cannot yet trace a formation impact with confidence beyond what
gravity 8 (economic embeddedness) already carries as an evidential
complication - whether Melitian material should be read as directly
informative about this world's own mainstream practice is the same
open question desert.contested.strand-porousness already holds open
(the Nepheros "fourth pattern" question), and this force is that
question's own generating pressure, not a new resolution of it.

kind: ongoing maps Doc_08's own Cell 2A (ongoing/external); the cell
code is carried in this record's own name, per the convention
established at desert.force.martyrdom-unavailable's own body note.

Doc08, Round 1 review Finding S2: sources[1] (brakke-athanasius) had
been given a locus quoting Doc_02 SS6's own sentence about Athanasius's
role toward the Melitian schism - a claim that source record's own
`work` field, entirely about the Vita Antonii as literary construction,
does not carry. The description's citation of that specific claim is
now routed to Doc_02 SS6 as background, matching the discipline already
used at desert.force.martyrdom-unavailable; brakke-athanasius's locus
is corrected to what that source record actually supports. Finding M3:
formation_confidence corrected from Contested to Documented (above).
Finding M12: manifestations[1] now names Vita SS68 rather than
asserting silence unqualified - the corpus's own most-cited vendored
text does mention the Melitians, to reject communion with them, which
strengthens rather than weakens this force's own reading. Finding M8:
the "sayings tradition" clause now registers desert.source.apophthegmata-patrum
with its own compiler-mediation flagged, rather than citing an
unregistered source. Finding M14: the Nepheros locus now carries both
of that source's own standing cautions, not caution (1) alone.

Doc08, Round 2 review Finding M6: the M12 sweep stopped at Vita SS68,
the first of two Meletian occurrences in the Vita; SS89 - Antony's own
deathbed exhortation - is the second and, if anything, the stronger
instance for this record's own point (polemical non-recognition carried
into the founder's dying instruction) - added above. Finding C3:
manifestations[1] had attributed the SS68 act to Athanasius
("Athanasius's own writing naming the Melitians only to reject
communion with them") when the vendored text's subject is Antony ("he
never held communion"); Athanasius is the narrator, not the actor -
corrected above to state the narration/action distinction accurately
for both passages.

Doc08, Round 3 review Finding S1: the Round 2 fix's own body note and
manifestations[1] both claimed "in the vendored file" / "only twice"
for Athanasius's own writing generally, when a mechanical count of
`npnf204_athanasius-select-works-letters.xml` finds 112 Meletian
occurrences, 47 of them in Athanasius's own Apologia contra Arianos -
false by a wide margin, and the review this fix pass was working from
had already scoped the claim correctly ("Inside the Vita the word
appears twice"). Both places above are now scoped to the Vita
specifically, matching that correct scope; divergence_note now also
discloses, rather than suppresses, the Apol. Ar. SS67 material the
sweep missed (named Melitian monks in Athanasius's own defence
document) as a flagged open item rather than an independently verified
addition to this record's own Layer 2 claim.
