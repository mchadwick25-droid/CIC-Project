---
id: desert.dw.melitian-power
world_id: desert-monasticism
record_type: doctrinal_witness
schema_version: 2
status: draft
register: emic
canon_cells: [F3-P]
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: contested
  formation_confidence: Contested
  divergence_note: "Contested throughout, matching desert.force.melitian-rivalry's own basis - this witness does not resolve whether the Nicene-communion majority's own treatment of Melitian ascetics was justified or merely successful; it names the asymmetry honestly rather than defending it. The claim that Melitian daily practice resembled our own rests on desert.source.nepheros-archive's own UNVERIFIED working assumption, not on independent confirmation, and this record states that plainly rather than treating it as established."
sources:
- source_id: desert.source.athanasius-vita-antonii
  locus: "SS68 - never held communion with the Meletian schismatics; SS89 - the deathbed exhortation to have nought to do with them"
  license: public-domain
- source_id: desert.source.nepheros-archive
  locus: "the Melitian community's own documentary archive - caveated per that source's own two standing cautions: representativeness for the mainstream strands is an unverified working assumption, and the editors' own 'intermediary' organizational reading does not map cleanly onto this world's three strands"
text: "There was another community near us, holding to a different bishop after an old dispute, and we did not treat them as fellow ascetics. The one we remember as our own founder never held communion with them, from the beginning to his own dying instruction. What that meant in practice was closer to silence than to open conflict in the writing we left behind - they are named only to be refused, never engaged as ongoing co-participants, which is itself a kind of judgment. Their own letters, when they survive, show ordinary monks doing ordinary monastic business - though whether that business really looked like ours day to day, or only looks that way from the little we can compare, is not something we can honestly settle from what survives. We did not, so far as we can tell, offer them the same recognition we gave each other."
positions:
- "we refused Melitian ascetics recognition as fellow participants in the same formation logic"
- "the refusal shows chiefly as near-silence and named non-recognition in what we wrote down, not as documented active persecution"
- "the surviving Melitian letters show ordinary monastic business, but whether that practice was truly comparable to our own day to day remains an open, unverified question, not something we can honestly claim to have settled"
tensions:
- "a claimed unity of the faith against a documented, unacknowledged parallel community practicing what looks like the same discipline - 'looks like' carrying real uncertainty, not confirmed resemblance"
---
Drawn directly from desert.force.melitian-rivalry, whose own body
states the corpus's honest position: silence read as informative rather
than neutral, and the Nepheros archive as a documentary check on that
silence, held at that source's own stated confidence rather than
upgraded.

Step4, Round 1 review Finding S7: this witness previously stated flatly
that Melitian documentary evidence showed practice "no different in
daily texture from our own," turning desert.source.nepheros-archive's
own capitalised "UNVERIFIED working assumption" into a settled finding,
and carried neither of that source's own two standing cautions in any
field. Both cautions now carried in the Nepheros locus and
divergence_note, and the claim itself walked back to state the genuine
uncertainty rather than resolve it. The text also previously attributed
"named them a schism" to Antony's own words when "schismatics" is
Athanasius's own narration, not Antony's reported speech (the exact
narrator/actor confusion desert.force.melitian-rivalry itself corrected
at Doc08 Round 2 review Finding C3) - reworded above to avoid the same
confusion. The locus is corrected from SS68-69 (SS69 is the separate
Arian confrontation - see desert.dw.councils) to SS68 and SS89,
the Vita's actual two Melitian passages, both of which
desert.force.melitian-rivalry already registers and this witness now
uses.

Step4, Round 2 review Finding M5: the compiled text's closing sentence
still read "so far as this record can show" after the fix above -
build meta-language surviving in the one field of this record type that
actually compiles (`build_prompt()`/`build_chunks()` emit
`doctrinal_witness.text` directly). Corrected to first-person phrasing.
Finding C4: positions[2]'s closing "not a settled finding" used review
vocabulary rather than this world's own register - reworded.
