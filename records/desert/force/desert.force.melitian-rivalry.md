---
id: desert.force.melitian-rivalry
world_id: desert-monasticism
record_type: force
schema_version: 2
status: ready
register: etic
canon_cells: [F3-T]
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: contested
  formation_confidence: Documented
  divergence_note: "Documented as to the Melitian communities' own existence and rough contemporaneity with this world's Nicene-communion material. Inferential-Thin as to whether Melitian and Nicene-communion ascetic practice were organizationally distinguishable in ordinary daily life - unresolved, carried forward here rather than resolved. formation_confidence is set to Documented, the dominant registered rating, rather than Contested, a value no registered record assigns this specific split; the Inferential-Thin half is carried in full above, not suppressed by the single enum value. The other three registered sources bear on this force's Layer 2 reading rather than its confidence rating: brakke-athanasius supports reading this world's literary self-presentation as authored, not neutral; athanasius-vita-antonii supplies the Vita's own two Melitian mentions; apophthegmata-patrum supplies the sayings tradition's own comparable silence. This record's Layer 2 claim is scoped to the Vita and the sayings tradition specifically, not to Athanasius's wider corpus: the same vendored volume names the Melitians well over a hundred times elsewhere (chiefly the Apologia contra Arianos), including, at Apol. Ar. SS67, a letter naming individual Melitian monks (Pinnes, Helias, Paphnutius) the volume's own Introduction cites as proof organized Melitian monasticism existed. That material is polemical and institutional, not about Melitian ascetics as ongoing rival co-participants in this world's own formation logic, and has not been independently incorporated here - a genuine open item (DOC08-INDEX.md's own open items list), not folded in without full verification."
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
description: "The Melitians were a rival ascetic movement, separate from the Nicene church this world's sources come from.
  Throughout their active life they occupied the same land and the same social world as this world's own Nicene
  community. They had their own monastic archive and their own ways of organizing.


  This world's Nicene sources say almost nothing about Melitian ascetics as a live, named rival. This record reads that
  silence as possibly meaningful, not neutral. The reason is Athanasius. His role as the Melitian schism's most powerful
  opponent in the church is documented. But this point comes from general background, not from a specific source
  examined for this world.


  Much of this world's written picture of itself was produced under his influence. The historian David Brakke reads
  Athanasius's Life of Antony as a construction shaped by theological and political motives. This record draws its own
  conclusion from both points: this literature had reason not to dwell on Melitian ascetic communities as legitimate
  partners in the same way of forming a life."
matrix_cell: 2A
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

sources[1] (brakke-athanasius) supports what that source record's own
`work` field actually carries - the Vita Antonii as literary
construction; Doc_02 SS6's own sentence about Athanasius's role toward
the Melitian schism is cited there as background, not attached to this
source's own locus. manifestations[1] names both of the Vita's two
Meletian occurrences (SS68 and SS89, Antony's own deathbed exhortation)
scoped to the Vita specifically - not to Athanasius's wider corpus,
where a mechanical count of `npnf204_athanasius-select-works-letters.xml`
finds 112 Meletian occurrences, 47 of them in the Apologia contra
Arianos - and states the narration/action distinction accurately:
Athanasius narrates that Antony "never held communion." The "sayings
tradition" clause registers desert.source.apophthegmata-patrum with its
own compiler-mediation flagged. The Nepheros locus carries both of that
source's own standing cautions.
