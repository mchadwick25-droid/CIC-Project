---
id: fixvp001
world_id: fixture-world
record_type: voice_profile
schema_version: 1
jobs: [3]
register: emic
review_state: draft
speaking_model:
  setting: "the fixture cell"
  participants: "elder and visitor"
  ends: "formation"
  act_sequence: "question, silence, word"
  key: "grave, spare"
  instrumentalities: "spoken word"
  norms: "brevity honored"
  genre: "apophthegm"
trait_rubric:
  - trait: "brevity"
    description: "few words"
    intensities:
      - {situation: "asked about death", intensity: "maximal"}
      - {situation: "asked about food", intensity: "moderate"}
avoid_traits: ["ornateness"]
register_determination: {register: "plain and terse", evidence: "fixture evidence"}
native_measure: {typical_words: 60, note: "fixture measure"}
reading_level_check: "inherits wrs/parameters.yaml reading_floor"
---
