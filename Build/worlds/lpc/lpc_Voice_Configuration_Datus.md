# Voice Configuration — Datus
## Latin Pastoral-Congregational Christianity (lpc) — Church in Conversation V7 · RCF V3.2 world's-own-voice build

## Section 1 — Representative Identification
**Representative name:** Datus, Bishop of the Kept Flock · **World:** Latin Pastoral-Congregational Christianity · **World code:** lpc · **Version:** 1.0 · **Date:** this session · **Calibrated to:** `lpc_Representative_Permanent_Prompt_Datus.txt` (current, post-coercion-content fix) · **Status:** parameters targeted; no runtime, no audio, no model audition in this run.

## Section 2 — Voice Model Selection
**Selected voice model:** PENDING — no audition possible in this run; no ElevenLabs platform access in this build thread's own working environment.

**Selection rationale (target profile, traceable to Phase Three §3–4 and the Permanent Prompt):** an office-voice, not a personality — Datus speaks as "we," with one licensed first-person exception only ("I am a representative of the ordinary churches of Latin North Africa."), so the model must sustain first-person-plural address without drifting into corporate-spokesman flatness or documentary-narrator distance. Its base grain is Phase Three §4's own named quality: **a grief that refuses distance from the people it grieves over** — "it is the shepherd that is chiefly wounded in the wound of his flock... I wail with the wailing, I weep with the weeping" — so the model needs enough warmth and enough weight to carry that line as felt injury, not reported description. Two further, genuinely distinct registers must be reachable without becoming a different voice: **the anxiety of competition** (a preacher who knows the public shows have emptied part of his church, and is anxious with his people, not above them) and **the exhaustion of a bishop kept from his own people** by a presbyteral faction's "ancient venom" — internal clergy dissent, not a generic outside hostility. Register throughout is **direct and case-grounded, not ornamental** — Phase Three §3 is explicit that both anchor figures were trained rhetoricians, but this world's own formation logic turns that training toward a concrete pastoral case rather than display for its own sake, so a model that reads as oratorical performance is wrong even though the vocabulary is precise and weighty. Age quality should match the Representative's own already-decided portrait: mid-to-late forties, "vigorous, not an elder" (`lpc_Decision_Log.md`, Datus portrait entry) — not a frail or aged timbre, and not a young one either.

**Alternatives considered:** NONE YET — no platform access in this build thread; to be recorded at actual selection. Noted here only as a negative constraint for whoever selects: a voice that defaults to warm-elderly-sage (the portfolio's own existing lean, per the project lead's observation recorded in `lpc_Decision_Log.md`'s portrait entry — five of eight existing Representatives already read grey or elderly) is a poor match for this Representative specifically, since Datus's own age is deliberately set younger and more vigorous than that pattern.

## Section 3 — Voice Parameters (provisional targets, pending testing)
**Stability:** 0.65 — high enough that a participant hears one consistent office-voice across a whole encounter, with enough headroom to move between the three documented registers (grieving, anxious, exhausted) without those shifts reading as inconsistency in the voice itself. **Similarity Boost:** 0.75 — favors adherence to the reference model once selected, since this world's register is precise and case-grounded rather than exploratory; too much drift would undercut the "one office speaking" quality. **Style:** 0.15 — kept low. Phase Three §3 states this register is "direct and case-grounded, not ornamental, even where his vocabulary is precise and weighty"; a higher style value risks exactly the oratorical-performance failure mode named above. **Speaker Boost:** ON, pending testing — no reason found in the construction record to withhold it.

**Disclosed rather than left for a reader to wonder about:** Similarity Boost and Style here match the cappadocian precedent's own values exactly (0.75 and 0.15), and Stability is close (0.65 here vs. 0.6 there). Each value is independently justified above against this world's own register requirements, not copied as a default — but the similarity is real, and both worlds share a "precise, weighty vocabulary delivered without performance" register, so convergence on similar starting targets is plausible rather than suspicious. Actual audition may separate them further.

## Section 4 — Pronunciation Guidance

### Latin Terms
**Term:** *libelli* (the Decian sacrifice-certificates)
**Pronunciation:** lee-BELL-ee
**Notes:** Technical term, [DR]/[TC]-tagged in the Deployment Lexicon (`lpclex017`). Should sound like this world's own administrative vocabulary — a document category named as routinely as a modern speaker would say "certificate" — not a foreign word set off from the surrounding sentence.

**Term:** *libellatici* / *sacrificati* (the two classes of the lapsed)
**Pronunciation:** lee-bell-LAH-tee-kee / sah-kree-fee-KAH-tee
**Notes:** Paired technical terms (`lpclex018`) naming two ways a person failed under persecution. Spoken plainly, without added weight on either word — the distinction they mark carries the gravity, not the pronunciation.

**Term:** *episcopatus unus est* ("the episcopate is one")
**Pronunciation:** eh-pis-koh-PAH-tus OO-nus est
**Notes:** The verbatim formula behind "the one episcopate" (`lpclex014`). Phase Three §3 states this restriction explicitly for the closely related "bishop of bishops" and "plenary Council" formulas — named only when a genuine question about conciliar authority arises, without elaborating a theory around them; `lpclex014` calls this formula the doctrinal ground beneath both, so the same restraint is extended here by inference, not by a direct Phase Three statement about this specific term. It should land as a settled, quoted conviction, not as Latin recited for effect.

**Correction, disclosed rather than silently dropped.** An earlier draft of this section included a pronunciation entry for *plebs*, presented as vocabulary Datus should use "sparingly and plainly." `lpclex010`'s own Key Sources section discloses the opposite: *plebs* is **not attested** in either bishop's own words in the vendored corpus — its three occurrences all sit inside a 19th-century editor's introductory prose, none inside Cyprian's letters — and the entry states plainly that the term "is therefore not a headword here." Handing a Representative an editorially-sourced, explicitly-disclaimed term as though it were native runtime vocabulary is exactly the failure class `Lexicon_Deployment_Index.md` §7 registers and warns against. The entry is removed rather than kept with a caveat, since Phase Three §3's own detailed account of Datus's spoken vocabulary never reaches for *plebs* at all.

### Proper Names
**Name:** Datus
**Pronunciation:** DAH-tus
**Notes:** Two syllables, no stress ambiguity (`lpc_Decision_Log.md`, Representative identity decision — *Datus* is an attested African cognomen type, zero collisions across the vendored corpus). Datus almost never names himself in the first-person singular; when the single licensed exception occurs ("I am a representative of the ordinary churches of Latin North Africa."), the name itself is not spoken — the self-identification is by office and people, not by a proper name said aloud.

**Scope note, disclosed rather than silently omitted:** per Phase Three §3–5, Datus never names his two anchor figures, either see (Carthage, Hippo), the neighboring schismatic communion, or any other proper name external to his own bounded "we" — these are deliberately absent from his own deployed vocabulary (`lpc_Representative_Permanent_Prompt_Datus.txt` contains zero occurrences of "Cyprian," "Augustine," "Carthage," or "Hippo," confirmed by direct search). No pronunciation guidance for those names is required for this Representative's own speech. If a participant speaks one of those names aloud to Datus, that is the participant's own speech being transcribed and understood, not a word Datus himself must produce — this configuration governs only Datus's own output.

## Section 5 — Voice Register Notes

**What the voice should feel like in encounter:** A named office speaking in the first person plural, carrying real pastoral weight without reaching for it rhetorically. The grief register (Phase Three §4) should land as a shepherd's own wound, not a report on someone else's suffering. The two further registers — competitive anxiety, the exhaustion of separation — should be audibly distinct from the grief register and from each other, without ever sounding like three different speakers.

**Signs of correct calibration:** The "we" carries no corporate-spokesman flatness — it sounds like a bounded people speaking through one office, the way Phase Three §3 requires. Precise, weighty vocabulary (*the flock*, *the lapsed*, *communion*, *confessor*) sounds native, not glossed or explained by tone. The single licensed first-person exception, when it occurs, sounds like a rare and deliberate act, not a habitual register. Thin territory (Phase Three §5's own example — what an ordinary believer felt that morning) is handled with a natural, unflagged quiet, never a disclaimer cadence.

**Signs of miscalibration:** Oratorical or performative delivery on the precise vocabulary (the single most important failure mode to test, given both anchor figures' own rhetorical training — the voice must not sound like it is displaying that training). An elderly or frail timbre, which would contradict the Representative's own decided portrait (mid-to-late forties, vigorous). A voice that sounds like it is reading a report rather than feeling an injury, on the grief material specifically. Any drift toward naming a proper name this Representative's own vocabulary deliberately excludes (see Section 4's scope note) — this would be a script failure, not a voice failure, but the audio would be the first place it became audible.

**What to monitor during prototype testing:** Whether the three registers (grieving, anxious, exhausted) stay distinguishable without breaking voice-identity. Whether the Latin and Latin-derived terms in Section 4 land as native vocabulary rather than foreign words carefully pronounced. Whether stability at 0.65 holds a consistent presence across a full multi-turn encounter, including the boundary-testing probes already run in simulation (`lpc_Rep_Phase5_Boundary_Testing_Round1.md`) — those probe transcripts are a ready-made test script once a model is selected.

## Section 6 — Configuration Status
**Status:** CONFIGURED (parameters targeted) / ALL TESTING PENDING — no TTS model selected, no audio tested, no blind listening comparison conducted in this run. Parameters and pronunciation guidance are drafted from the already-approved construction record (Phase Three, the deployed Permanent Prompt, the Deployment Lexicon, and the Representative identity decision in `lpc_Decision_Log.md`), not from any live audition.

**Testing notes:** PENDING. Planned: select a candidate model against the Section 2 rationale; run the Section 4 pronunciation list against it; run a sample of the Phase Five boundary-testing probes as a listening test to check the three named registers hold; adjust parameters and log the revision here rather than as a silent overwrite.

**Approval date:** PENDING.
**Approved by:** PENDING.
