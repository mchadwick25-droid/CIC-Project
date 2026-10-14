---
id: desert.story.antony-secret-burial
world_id: desert-monasticism
record_type: story
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: "Widely Accepted for the narrative's existence and general content within the Vita, composed within a few years of Antony's death by an author who appears in the account himself: SS91 has Antony order one sheepskin and the garment he lay on given to \"Athanasius the bishop.\" SS91-92 do not say that the author received them or that he heard the account from the two attendants; SS92 says only that no one but those two knows the burial place - matching desert.story.antony-call's own basis for material from the same Vita. Contested as to incident-level historical reliability specifically. This record does not treat the later, out-of-horizon relic traditions (a 561 'discovery' and translation, later moves to Constantinople and France) as continuous with what Antony himself asked for - the Vita itself already states no one but the two attendants ever knew the site."
sources:
- source_id: desert.source.athanasius-vita-antonii
  locus: "SS89-90 - Antony's last visit to the outer-mountain monks and his stated reason for refusing burial among the living (the Egyptian custom of keeping a holy man's wrapped body in the house); SS91 - his final instructions to the two attendants who had lived with him fifteen years, and the division of his belongings; SS92 - his death and secret burial"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how this world thought about death, burial, or being remembered afterward"
  - "participant asks whether this world's founder wanted to be honored or memorialized in a particular way"
  - "participant asks about relics or the physical remains of holy people"
relations:
- type: illustrates
  target: desert.gravity.withdrawal
- type: associated-with
  target: desert.figure.antony
narrative_tier: 1
narrative_tier_justification: "Tier 1 (Documented Historical Narrative): named author (Athanasius), composed within a few years of Antony's death by an author who says in his preface that he saw Antony many times and attended him for a long time. The Vita names no source for the death and burial; SS91 has Antony order one sheepskin given to Athanasius the bishop. Matches desert.story.antony-call's own basis for material from the same Vita."
tellable_as: 'Antony''s last order: bury me in secret, and let no one but you two know the place'
text: >-
  Near the end of his life, Antony made one last visit to the monks who lived on the outer
  mountain. He told them: this is my last visit to you, and I would be surprised if we saw each
  other again in this life. I am near a hundred and five years old. He urged them to keep up
  their discipline, to live as though dying daily, and to have nothing to do with the Meletian
  schismatics or the Arian heretics. Then he went back to the inner mountain, where he was used
  to living, and within a few months he grew sick.

  Antony had one more instruction to give. In Egypt at that time, people often kept the bodies
  of holy men in their own houses, wrapped in linen and laid out on couches, instead of burying
  them in the ground. Antony had often urged bishops and ordinary people to give this custom up,
  saying it was neither lawful nor holy. He was afraid the same thing would be done to his own
  body. So he called the two monks who had lived with him and cared for him for fifteen years,
  and gave them exact orders. Bury me yourselves, he told them, and hide my body in the ground.
  Let no one know the place but the two of you alone. He divided his few belongings between
  them: one sheepskin and the cloak he was lying on for the bishop Athanasius, the other
  sheepskin for the bishop Serapion, and his rough hair garment for the two attendants
  themselves.

  When he died, the two men did exactly as he had asked. They wrapped his body and buried it in
  the ground, and to this day, Athanasius writes, no one knows where - except those two men
  alone.
telling: "Athanasius writes that Antony visited the monks of the outer mountain and told them it was his last visit. He said he would be surprised if they met again in this life, and that he was near a hundred and five years old.\n\nThe monks begged him to stay and die among them. He would not, and above all for one reason. The Egyptians wrapped the bodies of good men in linen and kept them on couches in their houses. Antony had often urged the bishops to command the people against this, and he had taught that it was neither lawful nor holy.\n\nHe went back to the inner mountain, where he was used to living, and a few months later he fell sick. Two men had stayed with him there for fifteen years, serving him because of his age. He called them and told them to let no one take his body into Egypt. \"Bury my body and hide it underground yourselves,\" he said. \"Keep my words, so that no one may know the place but you alone.\"\n\nHe told them to divide his garments. One sheepskin and the garment he lay on were for the bishop Athanasius. The other sheepskin was for the bishop Serapion, and the two men were to keep the hair garment. Then he said farewell, and died.\n\nThey buried him as he had commanded. Athanasius writes that to this day no one knows where he lies, except those two."
absent_detail: "The two attendants are never named, and no account survives in their own words of how they experienced carrying out this instruction, or of the years afterward when they alone knew where the desert's most famous monk was buried. Later traditions claim the site was 'discovered' in 561 and the body eventually moved to Alexandria and then France - traditions that fall outside this world's own c. 320-430 window and that the Vita's own instructions would seem to rule out."
modern_contrast: "A modern reader is used to founders and famous figures being remembered through monuments, gravesites, or preserved remains open to visitors. In the Vita, Antony does the opposite with his body. He orders the two attendants to bury it underground and hide it, so that no one else knows the place. He also refuses the Egyptian custom of keeping the bodies of holy men in houses, which he had often urged people to give up. The Vita gives that custom as his stated reason. It also shows his sheepskins and garment being given away, and those who received them guarding them as a treasure (SS92), so it does not say that no memory of him was kept."
use_note:
  means: "Athanasius reports that, near death, Antony ordered two attendants to bury him secretly, refusing the custom of keeping a holy man's body in the house."
  not_for:
    - "Presenting incident-level details as verified history, since their reliability is contested"
    - "Linking it to the later 561 discovery or to relic traditions in Alexandria and France"
    - "Naming the attendants or narrating their experience, which no source gives"
  years: {from: 355, to: 356}
  status: reviewed
---
This record reconciles `cic-website/atlas-v3.html`'s desert-monasticism
`documentedStories` entry "Antony Has Himself Buried Where No One Will
Find Him" against this world's own registered records: no other
`records/desert/story/*.md` record covers this episode.

Verified directly against the vendored file
cic/texts/npnf204_athanasius-select-works-letters.xml, lines
33437-33549 (Vita SS89-92), rather than carried forward from the live
site's own prose unchecked. This record's own `text` field is a fresh
B2-register retelling grounded in that passage, not a copy of the
site's own prose.

Relation to desert.gravity.withdrawal: that gravity's own description
names withdrawal as "a lifelong deepening, not a single decisive act."
This episode is this world's own final instance of the same pattern -
Antony retreats yet further (leaving even the outer-mountain monks
permanently for the inner mountain) shortly before death, and his
burial instructions extend the logic of withdrawal from ordinary life
into a withdrawal from being memorialized at all. Declared `illustrates`
rather than `associated-with` on that basis; reciprocal `illustrated-by`
relation added on desert.gravity.withdrawal in the same pass. Reciprocal
`associated-with` relation also added on desert.figure.antony, matching
that record's own existing convention of listing every story it is
associated with.
