# CiC System Operations

```
Version: V7 r1
Status: Active
Scope: System-wide — all five formation worlds, all deployment phases
Updated: 2026-06-25
Referenced by: All world deployment packages, Facilitator-Governance,
               Representative Permanent Prompts
Update trigger: Technology stack change / Model change / Scale change /
                Infrastructure change / Phase advancement
```

---

## Section 1 — The Five Formation Worlds

The CiC Phase 1 table consists of five formation worlds. These are the permanent reference identifiers for the project. World names may be refined through each world's build as the formation ecology is discovered; world codes are stable.

| World Code | Working Name | Temporal Horizon | Representative Role | Build Status |
|---|---|---|---|---|
| communal | Early Communal | c. 50–150 CE | Voice of the earliest Eucharistic-communal formation tradition | Not started |
| alex | Alexandrian | c. 150–400 CE | Reader and teacher in the Alexandrian school tradition | V7 complete — deployment outputs in production |
| desert | Desert Christianity | c. 250–450 CE | Voice of the desert formation tradition | Not started — second build planned |
| cappadocian | Nicene-Cappadocian | c. 325–400 CE | Voice of the Cappadocian synthesis | Not started |
| latin | Early Latin | c. 350–430 CE | Voice of the early Latin pastoral-institutional tradition | Not started |

**Name stability note:** Working names above are the current working designations. Each world's build may produce a more precise name as the formation ecology is discovered. The world code is the stable identifier; all cross-references between operational documents use the world code.

---

## Section 2 — Technology Stack

**Current stack:** Option B — Direct Claude API + thin orchestration layer + ElevenLabs (voice, deferred).

**Components:**

- **Language model:** Claude (Anthropic). Specific model version is world-deployment-config level — different worlds may run on different models as the landscape evolves. See each world's deployment config.
- **Orchestration:** Thin custom layer managing context isolation, retrieval routing, and Facilitator/Representative separation. Status: not yet built. Current prototype operates without full orchestration. Change trigger: update when orchestration is implemented.
- **Voice:** ElevenLabs integration. Status: prepared, deferred. Activation trigger: funding decision. Each world's Voice Configuration document is prepared; none is active.
- **Retrieval:** Vector database or equivalent for World Context Layer chunk retrieval. Not yet specified. Change trigger: specify when orchestration is built.

---

## Section 3 — Context Architecture

**Governing principle:** Constitution Article 3 context isolation is the system's primary architectural constraint. Every operational decision about context management is subordinate to it.

**Per-Representative context isolation:** Each Representative's context window contains only that world's documents. Cross-World Contamination prohibition (Article 3 appendix) applies: Theon's context may not absorb vocabulary, formation logic, or theological framing from other worlds through the conversation transcript.

**The Facilitator as separate invocation:** A structurally different model invocation with its own isolated context. Carries what no Representative can: the full table view, the confidence apparatus, population guidance, Living Traditions distinctions for all worlds at the table, and calibration scenarios. The Facilitator's context never contains formation world content beyond what is specified in each world's Facilitator Brief.

**Public transcript:** The only channel between Representatives at a multi-world table. Each Representative encounters other worlds solely through words spoken in conversation — never through formation documents.

---

## Section 4 — Token Economy

**Governing principle:** Token budgets are operational parameters. Formation documents reference this section rather than hardwiring numbers.

| Component | Target | Rationale | Change trigger |
|---|---|---|---|
| World Capsule Core | 3,000–5,000 tokens | Always present; must leave room for retrieved chunks, conversation history, current turn | Model context window expansion / caching economics change |
| World Context Layer — single chunk | 500–1,500 tokens | Self-contained retrievable unit | Retrieval performance testing |
| Facilitator context — core Brief | 2,000–4,000 tokens | Carries confidence apparatus, population guidance, calibration scenarios for active worlds | Facilitator architecture specification |
| Maximum Representative response per turn | 300–600 tokens | Encounter requires exchange, not exposition | Encounter testing data |
| Conversation history window | To be specified | Depends on orchestration implementation | When orchestration layer is built |

**Content-plus-confidence retrieval unit:** Every retrieved chunk carries its confidence level alongside its content. System-wide architectural requirement. Any world with confidence calibration must retrieve calibration with content.

---

## Section 5 — Caching Architecture

| Tier | What | Applies to |
|---|---|---|
| Tier 1 — Always cache | World Capsule Core + Representative Permanent Prompt for each active world | All active worlds |
| Tier 2 — Warm cache | High-frequency World Context Layer clusters | World-specific; see each world's Deployment Config |
| Tier 3 — Cold retrieve | Long-tail Tier 2/3 lexicon entries | All worlds |

**Cross-world cache management:** At a multi-world table, each world's Core and Permanent Prompt are cached separately. Facilitator context cached separately from all Representatives. No cross-contamination.

---

## Section 6 — Table Configuration

**Phase 1 worlds:** Five — communal, alex, desert, cappadocian, latin.

**Table size by phase:**

| Phase | Maximum worlds at table | Minimum | Notes |
|---|---|---|---|
| Prototype Alpha | 2 | 1 | Single-encounter scope; user may select 1 or 2 |
| Prototype Beta | 3 | 1 | User may select 1, 2, or 3 |
| Phase 1 Full | 5 | 1 | User may select any combination 1–5 |

**Maximum is a governance limit, not a default.** Users select how many worlds they want at the table. The maximum prevents coherence and attention collapse; the minimum is always 1.

**Current scope:** Prototype Alpha — single-encounter (one world, one Representative, one participant). Multi-world table architecture is the next system-build dependency and is not yet implemented.

**Multi-world orchestration:** When built, the multi-world table layer assembles worlds, maintains the public transcript across Representatives, and manages turn orchestration. Governed by Facilitator-Governance v3.2. Each world's Facilitator Brief Section B carries curation input for that world's table behavior.

**Cross-world drift monitoring:** Six named drift signals per Facilitator-Governance v3.2, including mode-dominance drift as the fifth multi-world signal. Facilitator responsibility across all table configurations.

**Known high-blur pairings:** The following pairings require active Facilitator disambiguation:

| Pairing | Blur risk | Yield | Notes |
|---|---|---|---|
| alex + desert | High | High | Shared figures (Origen), shared vocabulary (theosis, apatheia, contemplation), transmits-to relationship |
| alex + cappadocian | Medium | High | Shared Nicene confession, shared allegorical heritage; diverge on Teacher-Bishop resolution |
| desert + cappadocian | Medium | Medium | Shared ascetic vocabulary; Basil's Rule is desert-adjacent |

Other pairings to be assessed as worlds are built.

---

## Section 7 — Voice Deployment

**Current status:** Text-first across all worlds through Prototype Alpha and Phase 1 launch.

**Activation trigger:** Funding decision for ElevenLabs integration.

**When voice is activated:** Each world's Voice Configuration document specifies model, parameters, and pronunciation guidance. The fabrication discipline carries into voice for all worlds: Representatives never narrate biographical detail; they speak for worlds, not from documented lives.

---

## Section 8 — Participant Safety

**Governing article:** Constitution Article 33.

| Parameter | Current setting | Change trigger |
|---|---|---|
| Minimum age | Adult only (18+) through Prototype Alpha | Minor-safety protocol development |
| Session supervision | Project lead present for every Prototype Alpha session | When supervision scales beyond manual oversight |
| Crisis recognition | Facilitator trained per Essential Experience v6.2 Section 9 | Protocol revision |
| Session exit | Participant may stop at any time — permanent | Not subject to change |
| Data handling | Conversation text collected for testing with participant consent | Formal privacy policy development |

---

## Section 9 — Fabrication Prohibition

Applies to all five worlds, all Representatives, all deployment components including runtime.

No content in any world's runtime system may introduce biographical fiction about any Representative. TC-001 is the governing ruling for Alexandria; the same principle applies to all worlds. Each Representative is a voice representing a formation world, not a fictional person with biography.

This prohibition applies to: World Capsule Cores, Representative Permanent Prompts, Facilitator Briefs, retrieved lexicon chunks, dynamically generated content, and voice output.

**Change trigger:** This is an architectural commitment. Not subject to routine change.

---

## Section 10 — Version History

**V7 r1** — Initial production. System Operations document established as part of the CiC Operational Document Set. All five Phase 1 worlds registered from the start. Table configuration establishes maximum-per-phase with user selection of 1 to maximum. Parameters set against current technology (Option B stack, Claude API, ElevenLabs deferred) and current phase (Prototype Alpha, single-encounter scope, manual feedback collection).
