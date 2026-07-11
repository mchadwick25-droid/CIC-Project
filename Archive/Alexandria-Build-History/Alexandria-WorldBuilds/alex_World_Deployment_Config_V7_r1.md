# Alexandria World Deployment Configuration

```
World: Alexandrian Christianity
World code: alex
Version: V7 r1
Status: Active
References: CiC_System_Operations_V7_r1.md (system-wide parameters)
            CiC_Phase_Status_V7_r1.md (gate and phase status)
Update trigger: World revision / Adjacent world build affects cross-build constraints /
                Retrieval performance data changes cluster groupings /
                Model selection update
```

---

## Section 1 — Model Configuration

**Current model:** To be specified at deployment initiation. Record here when set.

| Field | Value |
|---|---|
| Deployment date | [DATE] |
| Model | [MODEL NAME AND VERSION] |
| Context window available | [TOKENS] |
| Notes | [Any model-specific configuration notes] |

**Model selection guidance:** Alexandria is the most analytically complex Phase 1 world — 111 lexicon entries, eight construction documents, the most demanding confidence calibration discipline. Select for strong long-context performance and nuanced instruction-following.

---

## Section 2 — Retrieval Configuration

**Always-present in World Capsule Core — never retrieved:**
- Logos (alexlex001) — Theon's integrating reflex, always present
- Divine Pedagogy (alexlex002) — always-present Supporting Gravity compressed form
- Hope (alexlex045) — compressed form in Core; full entry retrieved on discouragement/incompleteness topics

**Retrieval clusters — retrieve as groups:**

| Cluster | Entries | Retrieve when |
|---|---|---|
| Formation sequence | alexlex001–008 | Formation, stages, theosis, knowledge questions |
| Anthropological stack | alexlex009–013 | Soul, human nature, image of God, freedom |
| Scripture interpretation | alexlex014–016 | How to read Scripture, allegory, Christological reading |
| Salvation arc | alexlex017–021 | Sin, death, salvation, transformation — retrieve together |
| Christological titles | alexlex022–024 | Christ, Son, Logos as person, Nicene confession |
| Sacramental practices | alexlex025–028 | Baptism, Eucharist, prayer, fasting, bodily formation |
| Authority trio | alexlex029–031 | Authority, tradition, Rule of Faith, Teacher-Bishop tension — retrieve together |
| Formation response | alexlex032–035 | Repentance, martyrdom, household, interpretation |
| Part One conversions | alexlex036–044 | Salvation, faith, love, Incarnation, mystery, oikonomia, virtue, church, Spirit |

**Single-entry retrieval:**
- Martyrdom (alexlex033) — triggered specifically by martyrdom/witness questions
- Hope (alexlex045) — full entry when discouragement or incompleteness is the encounter topic

**Cross-build constrained entries — retrieve with constraint active:**
- Group 2 Tier 2 desert-adjacent entries (Apatheia, Theoria, Watchfulness, Askesis, Monasticism, Solitude, Prayer Rule, Demons, Spiritual Father) plus Passion/Pathos
- Status: ACTIVE
- See Phase Status document for resolution trigger

**Term disambiguation:**

| Term | Scoping rule |
|---|---|
| Logos | Scope to Christology/Scripture/formation; do not surface entire lexicon |
| Scripture | Scope to interpretive cluster (method) or formation sequence (process) |
| Participation | Scope to sacramental cluster (practices) or formation sequence (soul's journey) |
| Transformation | Scope to salvation arc (problem/solution) or formation sequence (process) |

---

## Section 3 — Caching Configuration

Supplements CiC System Operations caching tiers with Alexandria-specific selections. See CiC_System_Operations_V7_r1.md Section 5 for tier definitions.

**Tier 1 — Always cache:**
- alex_World_Capsule_Core_V7_r1
- alex_Representative_Permanent_Prompt_V7_r1

**Tier 2 — Warm cache:**
- Authority trio (alexlex029, 030, 031)
- Salvation arc (alexlex017–021)
- Hope (alexlex045)
- Salvation and Incarnation (alexlex036, 039) — most frequently retrieved Part One entries

**Review trigger:** Reassess after three months of encounter data.

---

## Section 4 — Facilitator Configuration

**Facilitator context contents — Alexandria-specific:**
- alex_World_Facilitation_Brief_V7_r1
- Confidence apparatus: AQ1 stratum boundary, Eusebius HIGH Author Gravity flag, desert-attribution flags, CT tag distinctions
- Population routing: five types with specific guidance
- Living Traditions: Coptic Orthodox distinction protocol
- Calibration scenarios: five Alexandria-specific scenarios
- Alexandria-Desert disambiguation: shared vocabulary flags when both worlds at table

**Must not be in Facilitator context:**
- Alexandria formation documents (belong to Theon's context only)
- Any other world's formation documents
- Any biographical fiction about Theon

---

## Section 5 — Cross-Build Constraints

| Constraint | Status | Affected entries | Resolution |
|---|---|---|---|
| Desert-attributed evidence | Active | 9 Group 2 Tier 2 entries + Passion/Pathos | Desert Phase 3 gravity discovery |
| Antony data point | Active | Life of Antony Tier 3 hagiographic ceiling | External scholarly review |

---

## Section 6 — Article 31 Scholarly Review Items

Items for the external reviewer.

| Item | Priority |
|---|---|
| Doc_04 AQ1 school-stratum dependency | Highest |
| Eusebius HIGH Author Gravity (Origen-Demetrius; school succession) | High |
| Speculative-Doctrinal gravity mid-horizon confidence | High |
| Antony data point insufficient for ecology-wide claim | Medium |
| Pre-Nicene Athanasius dating (On the Incarnation) | Medium |
| Apokatastasis [CT] meaning contest | Medium |

---

## Section 7 — Version History

**V7 r1** — Initial production. World Deployment Configuration established extracting all Alexandria-specific operational parameters from formation documents. Retrieval clusters are predicted — review against actual encounter data after deployment.
