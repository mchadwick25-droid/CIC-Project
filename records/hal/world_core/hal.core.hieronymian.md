---
id: hal.core.hieronymian
world_id: hieronymian-ascetic-literary
record_type: world_core
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: null
sources:
- source_id: hal.source.jerome-ep108
  locus: whole letter (the world's richest single witness)
  license: public-domain
- source_id: hal.source.jerome-ep127
  locus: whole letter (the Rome pole after 385)
  license: public-domain
- source_id: hal.source.jerome-ep22
  locus: whole letter (the formation ideal, Rome period)
  license: public-domain
- source_id: hal.source.vulgate-prefaces
  locus: passim (the scholarly project defended in its own voice)
  license: public-domain
time_window:
  start: 382
  end: 420
horizon: 'Bethlehem and Rome, c. 382-420 CE: the ascetic-literary formation ecology around
  Jerome''s scriptural scholarship and the network of aristocratic Roman women who sustained
  and were formed by it - Marcella''s Aventine household, Paula and Eustochium''s Bethlehem
  monasteries, Fabiola''s Roman charitable foundations. The world begins when Jerome arrives
  in Rome and converges with Marcella''s already-established ascetic circle; it closes when
  both resident-leadership threads at Bethlehem - Eustochium''s and Jerome''s - end within
  the same narrow window. Its geography is bipolar throughout most of its span: Bethlehem
  (the double monastic community and pilgrim hospice) and Rome (the Aventine circle, an
  independent center of scriptural counsel) held together by letters, dedications, and
  patronage across the sea. The final decade narrows to Bethlehem alone.'
formation_logic: 'Formation as textual asceticism: ascetic renunciation (fasting, continence,
  the deliberate unmaking of aristocratic wealth and standing) and scholarly-literary labor
  (Hebrew study, translation, commentary, sustained correspondence) practiced as one
  discipline, not two. A person entering this life was formed as much by the correction of
  a word against the Hebrew as by fasting; wealth was converted into text, hospitality, and
  care for the sick; the letter itself was a formation event, carrying direction, argument,
  and belonging across the distance between the two poles. Authority ran through recognized
  scriptural learning and voluntary patronage - never through episcopal office or territorial
  jurisdiction.'
thinness: 'Richest in Jerome''s own letters, translation prefaces, and polemic, and in the
  remembered lives of the women - Paula, Marcella, Eustochium, Fabiola - as he chose to
  commemorate them. Thin-to-silent, structurally: no text composed by any of the women
  survives (one letter of Eustochium and the younger Paula to Rome is attested but lost);
  ordinary, unnamed residents of the Bethlehem communities are never individuated; enslaved
  persons and household dependents affected by their patrons'' renunciation are wholly
  absent; daily-life detail rests almost entirely on one letter; no material or documentary
  evidence independent of the texts has been identified.'
cautions: '1) Author gravity is the central limit. Nearly the whole record is in Jerome''s hand. He curated it himself in later life. Every account of the women''s agency comes through his framing. That framing is real and load-bearing, and it has one source. Never treat his rich narrative as independent proof.
  2) Epitaph genre. The obituary letters for Paula, Marcella, and Fabiola praise by design. Their picture of the formation ideal is evidence. Their scene-level detail is not.
  3) The letter in Paula and Eustochium''s joint name is widely accepted as Jerome''s own composition. Never cite it as the women''s own voice.
  4) How well Jerome knew Hebrew is an open question (hal.contested.hebrew-fluency). The Representative gives only his own words: he began as a young man and partly acquired it. Never state his fluency as settled. The modern dispute is for the Facilitator.
  5) "The Vulgate" as a name and as a standard church-wide text belongs to later centuries. In this window the translation project was ongoing, partial, and contested.
  6) Pre-horizon trap. Jerome also wrote before 382: Letters 1-21, the desert and Antioch years, the Life of Paulus. That is background, not this world''s span.
  7) Bethlehem daily life is modern reconstruction from one source plus analogy. That covers the schedule, the scriptorium, and the school. Never call it Documented.
  8) Independent witnesses are few, and each leans one way. Palladius and Rufinus are hostile. Sulpitius Severus admires him. Use them to triangulate, not to settle.'
thin_topics:
- keywords: [women's own words, Paula's writings, Eustochium's writings, Marcella's letters, her own voice]
  note: No text composed by any of the women survives; everything reaches us in Jerome's hand.
- keywords: [ordinary monks, unnamed residents, lay believers, congregation, catechumenate]
  note: The unnamed members of both Bethlehem communities are never individuated; no catechumenate or ordinary-lay formation is attested.
- keywords: [slaves, enslaved persons, servants, household dependents]
  note: Wholly absent from the record as subjects; affected by their patrons' renunciation but never heard.
- keywords: [daily schedule, horarium, liturgy hours, scriptorium, school]
  note: Rests on one letter plus analogy to other monastic patterns - reconstruction, not documentation.
- keywords: [archaeology, excavation, buildings, material remains, papyri]
  note: No documentary or archaeological evidence specific to these communities has been identified.
- keywords: [rural, villages, Palestinian locals, Jewish teachers' perspective]
  note: Local Bethlehem residents and Jerome's Jewish teachers appear only in passing, never in their own voice.
---
Draft world_core re-derived from the prior build's cleared Doc_01 (Approved
to proceed, Rounds 1-3 complete) under the new-spec record architecture.
Step 0 scope and the Doc_01 findings (382 start on the Marcella-convergence
ground; 420 close on institutional-continuity grounds; bipolar geography as
a structural finding; strand-singular after the authority-mode steelman) are
treated as settled and carried, not re-argued. World/Representative identity
naming remains Mark's per-world touchpoint; the registry entry holds
representative: null accordingly.

Time-window notes carried from Doc_01: the close is nominally Jerome's
death-year, held explicitly on institutional-continuity grounds - Eustochium's
death (418/419/420, contested across a three-year window) and Jerome's
(420, year Widely Accepted, the traditional day resting on liturgical feast
tradition and Prosper's chronicle) cluster too tightly and too uncertainly
to privilege either. See hal.contested.chronology.

The ABSENT STORIES question (Doc_09a section 4) is answered in full in the
prior build and carried into this corpus's honest_limit records and the
story records' absent_detail fields: (1) no story from the unnamed monastic
multitude's own perspective; (2) no family-resistance story in the resisting
member's own words; (3) no story of Jerome's Jewish teachers' own experience;
(4) no story authored by Paula, Eustochium, or Marcella; (5) no story of
household dependents or enslaved persons; (6) no ordinary-lay-believer
formation story. These are structural features of who could write, recorded
as data, never to be filled by invention (no Tier 5, ever).

Direct verification against the vendored npnf206 edition confirms: the letter of
Eustochium and the younger Paula reporting the 416 attack to Rome is
attested (Innocent's reply, Ep. 137, describes their report) but does not
itself survive - the one attested act of the women's own authorship, lost.
Recorded in hal.search.womens-own-texts and the honest_limit records.
