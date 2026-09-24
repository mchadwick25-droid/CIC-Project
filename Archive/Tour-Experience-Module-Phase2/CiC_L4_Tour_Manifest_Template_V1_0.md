# TOUR MANIFEST TEMPLATE

## Church in Conversation — Tour / Hosted Experience Module (Phase Two)

### Version 1.0

**Status of this template itself:** DRAFT — a planning-tier deliverable (Task Board
TR-4), not yet run through independent adversarial review. It has not been used to
build a real manifest yet. Flagged as an open item in the Decision Log rather than
silently treated as final.

**File naming convention (proposed, mirrors the Story Repository Chunk convention):**
`[world-code]tour[number]_[slug]_Manifest.md`
**Example:** `pahctour001_a-sunday-gathering-in-rome_Manifest.md`

**What this is:** the durable artifact type every future tour is authored against —
"one manifest per tourable scene, authored on the construction side (not at runtime),
derived only from an approved Doc_09 chunk, and subject to the same independent
review cycle every construction document gets" (`CiC_Tour_Experience_Module_Strategy_
V0_3.md` §4.1, the module's own founding definition of this artifact). This document
turns that definition into an actual fillable template, and adds Part 2, the
review-cycle definition TR-4 also asks for.

**Governed by:** `CiC_Tour_Experience_Module_Strategy_V0_3.md` §2 (Product Strategy),
§4.1 (Architecture — the Tour Manifest), §4.3 (Guardrails); the anchor world's own
approved Doc_09 Story Inventory (including Source Identification for Tier 4 stories);
Construction Framework's four-tier story classification and No Tier 5 rule;
Constitution Article 17 (visible-confidence rule, extended here from a sentence to a
whole mode) and Article 19 (no free invention at any stage). Worked example throughout:
`Ministry/Features/Hosted-Tour/Design/CiC_Hosted_Tour_Design_Note_V0_1.md` — the one
tour actually built (Chloe/House-Churches, `pahcstory006`), which every field below is
either extracted from or generalized from.

**A naming note, checked rather than assumed:** the task that produced this document
guessed "L4" might mean an operational/deployed-experience tier. That guess does not
match this project's actual precedent. The real "L4" is `reference/L4-Templates/` at the repo
root — a folder of reusable, fill-in-the-blank templates for the world-build
construction pipeline (`Story_Repository_Chunk_Template.md`, `World_Capsule_Core_
Template.md`, `Voice_Configuration_Template.md`, and others), each governing one
document type in the Doc_01–Doc_10 sequence, each carrying the same builder-note/
bracket/Final-Assembly-Instruction structure this document also uses. **This document
is filed under `Ministry/Features/Tour-Experience-Module-Phase2/`, not inside
`reference/L4-Templates/` itself** — the task's own filing instruction, and the honest reason
for it: tours are not yet an approved part of the core world-build pipeline (per
TR-14's own BLOCKED status), and `reference/L4-Templates/` is live, governed territory
(`CiC-L1L3-Foundation` branch work reconciled into it as recently as this same day,
commit `2b86b8b`) — not a place to add an unreviewed file uninvited, whether or not
any other thread happens to be actively editing it at this exact moment. "L4" in this
document's title names the *tier of artifact* this
is — a reusable construction template, same species as the real reference/L4-Templates — not a
claim that it has been promoted into that folder. If and when tours become a real part
of the pipeline (TR-14+), moving this file into `reference/L4-Templates/` proper is the natural
next step, not done here.

---

## Version History

v1.0 — Initial production. Front-matter, repeating Beat block, required Decline Stop
section, Refusal List, Entry/Exit, Asset Register, Guardrail Overlay Checklist, and a
Review-Cycle Definition (Part 2). Built by extracting the actual field structure of
the one built tour (Chloe/House-Churches) and generalizing only where the three
planned future tours (Syriac/Yausep, Desert/Papnoute, Bethlehem Circle/Albina — TR-11,
TR-12, TR-13) demonstrably need something Chloe's tour didn't.

---

## Part 0 — Before You Start: Run the Eligibility Gate First

A manifest may only be authored for a world/scene that
`CiC_Tour_Eligibility_Gate_V1_0.md` (this same folder) has already cleared, at the
class (A/B) and tour-tier that gate found. Do not open this template for a world that
gate hasn't run for, and do not let this template's own front-matter fields
(Tour-Class, Anchor-Tier) be decided here for the first time — they are the Gate's
output, carried in.

---

## Front-Matter

```
World-Code:            [the world's own two-to-six-letter lowercase identifier]

Tour-Title:            [participant-facing title, in the world's own register —
                        e.g. "A Sunday Gathering in Rome, As Justin Describes It"]

Tour-ID:               [world-code]tour[number]

Anchor-Chunk:           [the single approved Doc_09 story chunk ID this tour is a
                        projection of — e.g. pahcstory006. Exactly one anchor.]

Anchor-Tier:            [1 or 4 ONLY — see the note below]

Tour-Class:            [A — attested-scene / B — reconstruction]

{Builder note: Tier 1 → Class A; Tier 4 → Class B. Tier 2 and Tier 3 stories are NOT
valid tour anchors under the current architecture — not because they are weakly
sourced, but because a tour is a communal/shared-scene claim, and Tier 2/3 material in
this project's portfolio has so far only ever supported individual, specific-event or
attributed-tradition narratives (the Desert world's three Tier-1 *founding* scenes —
Antony's call, the staged withdrawal, Pachomius's founding — are vivid and
well-sourced but are precisely this: "individual, specific-event narratives, not
communal experiences a participant can be hosted through... narrating Antony's call is
already licensed conversational material; it is not a tour in this module's sense,"
Strategy §3.3). If a future world's own evidence genuinely produces a communal,
narrated Tier 2 or Tier 3 scene, that is a real open architecture question this
template does not resolve — flag it to the review cycle rather than force-fitting it
into Class A or B.}

Satellite-Chunks:      [any additional approved chunks this tour names but does not
                        narrate as its own scene — e.g. Chloe's tour names pahcstory009/
                        010 (the Didache's meal) at its ending, in reconstruction
                        register, as a *future* tour, never blended into this one.
                        Leave blank if none.]

Register-Banner-Text:  [the persistent, participant-facing marking, displayed for the
                        WHOLE duration of the tour, not disclosed once and allowed to
                        fade — Article 17's visible-confidence rule applied to a mode.
                        Class A wording pattern: "A witness's own account —
                        [author], writing [date/occasion]."
                        Class B wording pattern: "A reconstruction of typical
                        practice — no single recorded event; every element sourced."]

Hosting-Representative: [the world's own Representative who hosts — e.g. Chloe]

Hardest-Constraint:    [one line, carried from the world's own Eligibility Gate
                        Gate 4 finding — e.g. "Rome-only; never generalized
                        network-wide; never blended with the Didache or Ignatian
                        eucharistic practices."]
```

---

## Beats

{Builder note: the NUMBER of beats is never fixed by this template — Chloe's tour has
nine narrative beats (0–8), later carrying four inline photographs and two audio clips
across thirteen tracked recording frames. What IS fixed: the SEQUENCE must be the
source's own reported order, never an invented dramatic arc. For a Class A tour, that
is the witness's own sequence (Justin's own reported order: arrival → reading →
exhortation → prayers → bread and cup → collection). For a Class B tour, that is the
attested typical sequence (e.g. the Desert world's cell-to-synaxis-threshold-and-back
day). Repeat this block once per beat.}

```
Beat #:                 [0, 1, 2, ...]

Beat Name:              [participant-facing, short — e.g. "The Day", "The Reading"]

Narration bounds        [what the Representative says at this beat, in their own
(Representative's         established register per their Permanent Prompt/World
voice, register-           Capsule Core — NOT a replacement voice. For Class A:
locked to Tour-Class):     relayed-witness register, the author named throughout
                           ("Justin tells the emperor that..."). For Class B:
                           explicit-reconstruction register throughout ("In a
                           gathering such as ours might keep..." — syrstory009's own
                           approved opening is the model phrasing). The two
                           registers never blend within one manifest, and never
                           drift mid-tour toward neutral, omniscient narration (the
                           "museum docent" drift risk, Strategy §4.3).]

Sourced Elements         [Class B only. One-to-one against the anchor chunk's own
(Class B only):            Source Identification section. Every claim-bearing
                           detail in this beat's narration must appear here with its
                           citation, or it does not belong in the narration. Leave
                           this field explicitly "N/A — Class A" for Class A tours;
                           Class A narration is bound by the story text itself, not
                           a separate element list.]

Honest-Silence Beat?     [Yes/No. If Yes: state exactly what the source is silent
                           about at this specific beat, and cite the world's OWN
                           record establishing that the silence is real — e.g.
                           "Justin gives no words for the prayers; none are shown —
                           the absence is in the source itself ('according to his
                           ability'), not around it." An honest-silence beat is
                           testimony, not an apology; write it in the
                           Representative's own voice, not as a system disclaimer.]

Q&A Demonstration?       [Yes/No. At most one or two beats per tour should model the
                           tour pausing for a real question and resuming — this
                           demonstrates that a tour is conversation with structure,
                           not a video with a chat box (Design Note §1). If Yes,
                           name the modeled question and note that its answer draws
                           on the world's OWN unsettled or settled position (the
                           deployed Capsule/Permanent Prompt), not invented content
                           written fresh for the tour.]

Assets bound here:       [none / asset ID(s) — cross-reference the Asset Register
                           below]

Source cartouche         [one line: citation + tier + confidence label, in this
— short (hover):           world's own five-level vocabulary]

Source cartouche         [the full source note — what a participant sees on click]
— full (click):
```

---

## The Decline Stop (Required)

Every tour manifest carries at least one honest decline beat, named as a first-class
stop rather than an error state — per the Tours rule (front-end decision log,
2026-07-07: "only what the evidence actually supports is shown, played, or offered;
where evidence runs out, the system says so plainly") and modeled directly on Chloe's
Stop 7, "What We Cannot Show You."

```
Decline #1:  [what is declined — the room, the exact words, the people, the sound,
             or whatever this world's own record actually withholds]
Evidentiary  [cite the world's own record establishing this is a REAL, disclosed
basis:        absence — a Doc_09 item number, an Excluded Source Registry row, the
              source's own admission of a gap ("according to his ability"), a
              countable fact (e.g. "exactly two ordinary members are named in the
              entire evidence base"). "No asset exists for this yet" is NOT a valid
              basis here — that is a production gap, not an evidentiary one.]

Decline #2:  [...]
Decline #3:  [...]
[as many as the world's own evidence requires — Chloe's tour carries four (the room,
the words, the people, the singing); a thinner world may need only one; do not
manufacture additional declines to hit a target count, and do not omit a real one
because three feels sufficient.]
```

{Builder note: if this section comes up empty on a first pass, treat that as a signal
to look harder before treating the source as unusually complete — real ancient
evidence bases essentially never run out nowhere. Chloe's tour is built on the
strongest single narrated source in the whole portfolio and still needed four.}

---

## Refusal List (Do-Not Conditions)

```
Inherited from the anchor      [copy forward, verbatim or near-verbatim, from the
chunk's Do-Not-Retrieve-When:   chunk's own front-matter]

Tour-specific additions:       [conditions that exist BECAUSE this is a tour, not
                                 because the underlying chunk already said so —
                                 typically drawn straight from the world's own
                                 Eligibility Gate Gate 4 finding:
                                 - no generalization beyond the anchor's own
                                   geographic/temporal bound
                                 - no blending of two or more differently-sourced
                                   practices into one composite (diversity-first)
                                 - no compositing of an unattested sensory element
                                   even with a disclaimer — a disclaimer cannot
                                   restrain a sensory claim; text can hedge
                                   mid-sentence, sound and image cannot (Strategy
                                   §2.6)
                                 - no borrowing evidence, imagery, or sound from a
                                   neighboring world's or era's record
                                   (cross-contamination discipline)]
```

---

## Entry / Exit

```
Invitation line          [in the Representative's own voice, offered — never
(in-voice):                imposed — when the anchor chunk's own Retrieve-When
                           conditions fire. The retrieval front-matter the chunk
                           already carries is, unmodified, the tour's invitation
                           heuristic (Strategy §2.1).]

Threshold framing:        [what this tour is / what it's built from / what it will
                           not claim — stated before the first beat, in-voice.
                           Chloe's Door beat is the model: "one Roman writer's
                           account — not a network template; other households kept
                           the meal in other shapes."]

Return-to-conversation    [how the Representative hands the participant back —
handoff:                   no summary imposed, no interpretation offered unasked.]

Exit affordance:          Available at every beat, by design. Interrupting with a
                           question is never treated as exiting.
```

---

## Asset Register (only if this world's own evidence licenses any)

{Builder note: description-first is the module's launch default (Strategy §2.4), and
for the strongest tour in the portfolio (PAHC) it is a necessity, not a budget
choice — that world's window is archaeologically invisible and its two famous
"early-church" visuals (Dura-Europos, the Abercius inscription) are Excluded Source
Registry rows. If this world's own Source Registry licenses nothing Native, this
section should read "None — description-first by evidentiary necessity" rather than
being left blank or silently skipped.}

Repeat per asset:

```
Asset ID:            [...]
Type:                 [photograph / audio]
What it is:           [plain statement — e.g. "a real carbonized loaf from Pompeii,
                        scored in eight"]
What it is NOT        [the honest caption limit — e.g. "whether this very shape sat
(the caption's          on our tables, no source says" — never omit this line]
honest limit):
Registry status:      [Native row citation, OR "audio: source-performative — the
                        SOURCE ITSELF was spoken/sung/read aloud, cite the
                        performance" — assets are never generated, and never
                        licensed on the strength of "it looks right for the period"]
License/credit:       [...]
Bound beat:           [...]
```

**Audio-specific note (from the one world where this has actually been decided,
generalized as a principle, not copied verbatim):** audio is licensed only where the
source itself was an oral performance — a teaching being given, a hymn sung, a text
read aloud — never as ambient/atmospheric sound design. Where a performer's identity
is itself attested (e.g. a choir), voices should be cast to match the attested
performer; a voice that misrepresents who actually performed the material is a
fidelity error even when the words themselves are sourced. Where the *melody* or
*sound itself* is unattested, the honest move is to voice the attested text and
withhold the unattested sound — not to composite a plausible substitute from an
adjacent culture or era, even labeled "it may have sounded like…" (refused on the
merits in Strategy §2.6 — a Tier-4-style composite fails element-by-element when the
missing element is precisely the one being reconstructed).

---

## Guardrail Overlay Checklist

Confirm each before this manifest may enter review:

- [ ] **Tier-register lock** — Class A narrates in relayed-witness register, author
      named throughout; Class B narrates in explicit-reconstruction register
      throughout; the two never blend within this manifest.
- [ ] **No-new-texture** — every sensory/procedural detail in every beat traces to a
      Source Identification entry (Class B) or the anchor chunk's own story text
      (Class A). Nothing is present "atmospherically" without a citation.
- [ ] **Diversity-first** — if this world's approved chunks document more than one
      distinct practice, this manifest represents exactly one and does not blend.
- [ ] **Q&A drops to ordinary mode** — the manifest does not script participant
      questions or answers beyond the one or two demonstrated pause-and-resume
      beats (if any); real questions in a live tour get full retrieval and all
      standing guardrails, not manifest text.
- [ ] **Tours end** — exit is defined at every beat; no beat leaves a session
      ambiguously "in a scene."
- [ ] **Register-banner persistence** — the banner text is specified once here, and
      is intended to display for the tour's WHOLE duration, not only at the
      threshold.
- [ ] **Decline Stop is sourced, not generic** — every declined item cites a real
      absence in the world's own record.

---

## Final Assembly Instruction

1. Replace all [BRACKETS] with world- and tour-specific content.
2. Remove all builder notes in {curly braces}.
3. Confirm every Class B beat's Sourced Elements line maps one-to-one to the anchor
   chunk's own Source Identification section. If an element in this manifest has no
   match there, remove it from the manifest — a Tour Manifest may not introduce
   evidence the chunk's own review never saw.
4. Confirm the Decline Stop section names at least one honest, sourced absence.
5. Confirm Register-Banner-Text is set and matches Tour-Class exactly (A/B wording
   pattern above).
6. Confirm the Refusal List actually carries forward the anchor chunk's own
   Do-Not-Retrieve-When conditions, not just the tour-specific additions.
7. Save as `[world-code]tour[number]_[slug]_Manifest.md`. Until TR-14 (`cic-poc`
   integration) exists, file it under this feature folder (`Ministry/Features/
   Tour-Experience-Module-Phase2/`) rather than inventing a data-directory location
   that doesn't exist yet — per the standing rule that builder-machine tasks
   (manifest/template work) are startable with zero live-system risk
   (`Hosted-Tour/Integration-Notes.md`).

---

## Part 2 — Review-Cycle Definition

### The question this section answers

TR-4 asks not just for a template but for who reviews a new Tour Manifest, against
what standard, and how many rounds — and specifically whether this project's own
established pattern (independent adversarial review, 2–3 rounds, most recently run in
full on the Imperial-Juridical-Christianity build, 2026-07-20) is the right model here,
or whether tours warrant something lighter.

### Decided: the same rigor, narrower scope — not lighter

The Strategy document already answers the rigor question at its founding decision
(§1.2): a Tour Manifest is "subject to the same independent review cycle every
construction document gets," because a tour is a structurally higher-stakes claim than
a conversational answer — "this is what a morning gathering looked like," not "here is
what I can tell you about it" — and under Historical Responsibility that claim
requires *more* evidentiary weight, not less. This document does not relitigate that
decision; it carries it forward and answers the mechanics.

**But the SCOPE of the review is genuinely narrower than a Doc_09 review, and that
narrowness is itself load-bearing, not a shortcut.** A Tour Manifest may not cite
material outside its anchor chunk (§4.1) — it is a *projection* of an already-approved
document, never an extension of it. The manifest review is therefore not a fresh
evidentiary or theological argument (the anchor chunk already carried that argument
through its own review); it is a **citation-fidelity and register-discipline check**:
does every claim in this manifest actually trace back to something the anchor chunk's
own already-cleared review already saw?

**Why this doesn't argue for a LIGHTER review, even though its scope is narrower:**
images and audio are new failure surfaces this project's existing review checklists
were never built to catch, and they fail in a way text does not — "an image is a claim
that cannot hedge... a picture has no register for Inferential/Thin" (Strategy §2.4),
and "a disclaimer does not neutralize a sensory claim: text can hedge mid-sentence,
sound cannot" (§2.6). A citation error in a Tour Manifest's asset caption or narration
beat is, if anything, *harder to walk back* once shown or played than a hedged sentence
in an ordinary answer would be. The narrower input (one anchor chunk, not a whole
world's ecology) does not translate into a smaller consequence if the review misses
something.

### Who reviews

An independent reviewer with no drafting involvement in the manifest — the same
standing discipline as every other construction-document review in this project
(the "independent isolated agent, no drafting involvement, first-principles skeptical
read" pattern, most recently documented in `worlds/ijc/Review-Artifacts/Doc09_Round1_Review.md`). The reviewer must have direct
read access to:

- the anchor world's own approved Doc_09 chunk(s), including Source Identification
  for any Tier 4 material;
- the world's Source Registry, including Excluded rows;
- the world's deployed World Capsule Core and Permanent Prompt;
- this template's own Guardrail Overlay Checklist and Final Assembly Instruction.

A reviewer without access to the anchor chunk cannot do this job at all — the entire
review is a fidelity check against material that has already been cleared once, not a
fresh argument from primary sources.

### Against what standard — the review checklist

1. **Anchor/class match** — Tier 1 → Class A only, Tier 4 → Class B only; flag (don't
   silently force-fit) any Tier 2/3 anchor.
2. **Citation fidelity** — every Sourced Element traces to the anchor chunk's own
   Source Identification (Class B) or its own story text (Class A); nothing has been
   added that the chunk's own review never saw.
3. **Register-tier lock held throughout** — no drift into neutral, omniscient
   narration mid-tour (the "museum docent" drift risk, Strategy §4.3).
4. **No-new-texture** — flag any sensory/procedural claim that reads as invented
   atmosphere rather than a cited detail.
5. **Decline-stop honesty** — every named absence is sourced as a real absence in the
   world's own record, not merely unproduced content.
6. **Refusal-list completeness** — the manifest's Do-Not list actually carries forward
   everything the anchor chunk's own Do-Not-Retrieve-When already flags, plus the
   tour-specific additions the world's own Eligibility Gate already named.
7. **Asset caption fidelity** (if any assets exist) — Native registry status is real,
   and the "what this does not show" line states an honest limit, not a generic
   credit line.
8. **Register-banner persistence and entry/exit mechanics** — present, correctly
   worded for the class, and exit is genuinely available at every beat.

Disposition vocabulary matches the project's existing standard exactly: a manifest
under construction carries **"DRAFT — pending independent adversarial review"**; a
clean pass is **"Cleared review and Approved to proceed"**; a failing pass is
**"Substantial Revision Required,"** with findings tiered HIGH/MEDIUM/LOW the same way
Doc-level reviews are tiered today.

### How many rounds

**Minimum two rounds. A third round is mandatory if Round 1 returns any HIGH-severity
finding.** This is not a fixed guess — it mirrors this project's own actually-observed
pattern rather than inventing a new number: the most recent full independent
adversarial review cycle (Imperial-Juridical-Christianity, Doc_01 through Doc_09) ran
"2–3 rounds per document, several requiring 3," and the one real, worked example of a
Round 1 review turning up a HIGH finding (`Doc09_Round1_Review.md` — a document falsely
certifying a sibling document as already cleared) required a further round before the
set could be marked Cleared. A Tour Manifest with a HIGH finding — a citation that
doesn't actually trace to the anchor chunk, or a decline-stop that isn't really sourced
as an absence — is exactly this project's own recurring failure shape (a
confident-sounding claim that doesn't survive a direct check), and deserves the same
treatment, not a lighter one.

### Genuine boundary calls are not review findings

If a review round surfaces a real judgment question rather than a citation defect —
the shape of the Syriac Yausep capsule-versus-chunk tension (Strategy §3.2, item 3) —
it is not logged as something to "fix." It is routed to Mark directly, per the
standing ruling already on record ("let the source make the call": the reviewed,
approved chunk's own license governs; a Representative's capsule self-limit governs
only unscripted expansion, §2.6). **The reviewer's actual job includes telling these
two things apart** — collapsing a live boundary call into an ordinary defect would
either force premature revision of something that is genuinely Mark's decision, or let
a real defect hide behind the appearance of being "just a judgment call." Getting this
distinction right is itself part of what Round 1 checks.

### What this section does not resolve (flagged, not invented around)

Who *specifically* staffs this review — a dedicated reviewer role, or the same
rotating independent-agent pattern used for World-Build documents — is not decided
here; it is Mark's own staffing call, the same way it has been for every other
construction-document review cycle in this project. This document defines the
standard and the mechanics; it does not assign a name to the seat.
