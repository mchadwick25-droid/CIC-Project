# lpc Surface Records Review, 2026-10-25

**Scope.** Two new, untracked surface records for Latin Pastoral-Congregational Christianity (c. 246–430; Representative: Datus):

- `Build/worlds/lpc/surface/world_front/lpc.front.latin-pastoral-congregational-christianity.md`
- `Build/worlds/lpc/surface/facilitator_brief/lpc.facilitator_brief.latin-pastoral-congregational-christianity.md`

I also checked the compiled output, `cic-website/data/worlds/latin-pastoral-congregational-christianity.json`. It matches the front record's text.

**Reviewer.** Opus 5.5, independent adversarial review. No model API was called. Diffs under `records/lpc/` and in the lpc generator scripts were ignored, as instructed.

**Method.**

- I checked that every `grounded_in` ID resolves. All of them do.
- For every unit, I opened the records it cites in `records/lpc/` and read each sentence against them. That covered world_core, all 7 figures, all 7 stories, all 4 contested claims, all 3 demonstrations, 7 gravities, 13 forces, the 19 terms, 4 doctrinal witnesses, the ambient records, 5 honest limits, the 7 quotes shown or pulled, and voice_craft.
- I compared the brief's cautions with the don and gallic briefs, the world_core's caution 12, `lpc_Rep_Phase6_Facilitator_Coordination_Round1.md`, and CLAUDE.md's Safety section.
- I scored readability per field with the record gate's own scorer (`engine.m1.gates.grade_text`).
- I ran `tools/check_live_commentary.py --surface worlds`.

## Findings

| ID | Sev | File:field | Finding | Evidence | Fix |
|---|---|---|---|---|---|
| F1 | P1 | front: `orientation.story[8].text` | Wrong as written. "A few old sermons may date from that time, and they have not yet been studied." Morin edited these sermons in 1917, so scholars have studied them. What is true is narrower: *this build* has not assessed them. A participant will read this as a claim about scholarship in general. | `lpc.limit.the-silent-century`, divergence_note: "Nine tractatus in Morin 1917 … are not yet assessed (OG-54)". The brief has it right: "have not yet been assessed". | "A few old sermons may date from those years. We have not yet read them for this world, so the silence is held as an open question." |
| F2 | P1 | brief: `world_identity.text` | Stated as settled, but the record rates it Inferential-Thin. "Its core conviction is that the church is answerable, not that it is pure" is given as fact. The cited witness is rated **Inferential-Thin** and frames it as the world's own self-reading ("As we understand ourselves", "As we see it"). The world_core's divergence_note says this convergence is "this build's own synthetic judgment". | `lpc.witness.answerability-as-ground` (formation_confidence: Inferential-Thin). `lpc.core…` divergence_note. | Mark it as a reading: "This build reads its core conviction as answerability, not purity. The world's own voice puts it that way, but the claim is a synthesis and rated Inferential-Thin." |
| F3 | P1 | brief: `formation_strengths[3].text` | Unsupported. "Persecution, plague, a rival church and a city under siege all reached ordinary believers as teaching." None of the cited records says the siege of Hippo reached believers as teaching. The world_core's list of pressures turned into teaching is persecution, plague, the rival communion and Pelagian teaching. The siege is an *ending* force. Its own record says it closed the world and ended the pastoral bond. | world_core formation_logic: "Persecution produces De Lapsis … Plague produces De Mortalitate. The rival communion produces … Pelagian teaching … produces thirteen works." `lpc.force.vandal-invasion-siege-of-hippo`: "the bond between this bishop and this flock ends when he does". Cited: plague force, plague story, preaching gravity. None of them mentions the siege. | Drop "and a city under siege". Optionally replace it with the grace controversy and add `lpc.force.manichaeism-and-pelagian-anthropology` to grounded_in. |
| F4 | P1 | brief: `cautions[5]` | Safety. The caution says the Numidicus story's "retrieval note steers away from it when a participant is in acute grief or trauma, toward a gentler deathbed story." In a Facilitator brief, this reads as Datus handling a participant in acute trauma by choosing a different story. That contradicts caution 2 and CLAUDE.md: on an acute-distress turn the voice is not called at all. The retrieval note can only apply to grief below the Facilitator's distress threshold. | `lpc.story.numidicus` retrieval.prefer_instead. Brief `cautions[1]`: "When it finds them, Datus is not called at all." CLAUDE.md Safety: "A Representative never handles real crisis or distress itself." | Scope it: "For grief that has not reached the Facilitator's distress threshold, the story's own retrieval note steers away from it, toward a gentler deathbed story. Acute distress or trauma is the Facilitator's turn, and Datus is not called." |
| F5 | P2 | brief: `cautions[2]` | The brief tells the Facilitator how to word the crisis redirect itself: "Say instead that the person is held, and that this needs more than this conversation can give." The fleet design keeps the actual redirect template-anchored and fleet-wide; the don brief says this explicitly. The substance is grounded in world_core caution 12, so this is not invented. But as written it reads as per-world redirect wording, which would be new policy. The closing "This has not yet been tested with a live Facilitator" is a status line that will go stale. | world_core caution 12. CLAUDE.md: "the actual redirect is Facilitator-governed and template-anchored, not freely generated". don brief cautions/body on B7. Phase Six §3 calls this "distinct from the generic crisis-redirect language Facilitator-Governance §12 already specifies". | Frame it as a register risk for the Facilitator's own warm words around the template: "The redirect and its resources follow the fleet template. In the Facilitator's own words around it, avoid anything that sounds like 'prove yourself first'; the sense to carry is that the person is held." Move the untested-status line to `Open_Gaps_Tracking.md`. |
| F6 | P2 | brief: `cautions[3]`; `redirect_notes.text` | Grounding gaps. Two claims rest on the approved Phase Six document, not on any lpc record: the "bishop leaving them" risk, and "do not point the participant to that world's Representative". Neither is invented. But neither is traceable through the records, and the second is a cross-world Facilitator rule. | `lpc_Rep_Phase6_Facilitator_Coordination_Round1.md` §2 (the 133-year bullet) and §2 "The second" caution. No match in `records/lpc/`. world_core caution 2 bars *filling* the silence from Donatism; it says nothing about referral. | Ask the records thread to carry both into world_core cautions, or into a limit's guard, so the brief can cite them. Until then, add the source to grounded_in where the schema allows. |
| F7 | P2 | front: `documented_stories[1].teaser` | Conflates two requests. "Celerinus grieves that his sister has sacrificed. He asks Lucian … to grant peace. Lucian sends it back, on condition…" This implies Lucian granted peace to the sister. Lucian's reply grants peace to **Numeria and Candida**. The story's absent_detail also says Candida's lapse was contested, not conceded. | `lpc.story.celerinus-writes-to-lucian` text: "He asked Lucian to intervene, for her and for two other women, Numeria and Candida … He asked that the two women have peace". The story's claim_guards. | "…He asks Lucian to grant peace to her and to two other women. Lucian grants it to the two women by name, on condition that each case goes before the bishop." |
| F8 | P2 | brief: `formation_limitations[3].text` | "One letter describing a church at Hippo" is unsupported. Neither cited record places the letter at Hippo; world_core says only "a pastoral letter describes an apse…". "No order of service survives" is also not in the cited records. It appears only in Phase Six §2. | world_core thinness; `lpc.limit.rural-punic-berber-life`. | "The buildings are known mostly from one pastoral letter, not from excavation." Ground "no order of service" in a record, or say "the works that argue about the rites take them for granted and do not describe them" (world_core). |
| F9 | P2 | brief: `living_tradition_handling.text` | Overgeneralized. "Later churches rejected Cyprian's rebaptism." The cited record says the church that became the canonical one, in the West, judged him wrong. Eastern practice on receiving converts varied. | `lpc.force.transmission-institutionally-dominant-side`: "That church kept Cyprian even where it judged him wrong, on rebaptism." | "The Western church rejected Cyprian's rebaptism, though it honours him." |
| F10 | P2 | brief: `participant_type_fit[2].text` | "Four points are held as Contested" lists the four contested_claim records. But this same brief, in `formation_limitations[4]` and `redirect_notes`, holds the silent century as Contested too. An academic reader counts five. | `lpc.limit.the-silent-century` (Contested); `lpc.force.transmission-asymmetric-span-133-year-silence` (Contested). | "Four disputes are held as Contested, beside the Contested silence noted above:" |
| F11 | P2 | front: `orientation.story[9].text`, `voices[3].text` | "Baptized at Milan" is right, but neither unit's grounded_in carries Milan. The figure record gives only "baptised 387". | `lpc.limit.ordinary-interior-life` (Confessions IX.vi.14) carries Milan. | Add `lpc.limit.ordinary-interior-life` to both grounded_in lists. |
| F12 | P2 | front: `relations_summary.text`; `legacy[1].text`; `sourcing.text`; `highlights[2].note`. Brief: `pairing_guidance.text` | Unclear phrasing. Each of these blurs a precise idea; none of it is AI-sounding. (a) "When bishops disagree past any agreement" and the brief's "disagreement past agreement" do not parse cleanly; the idea is disagreement that will not be settled. (b) "stands behind much of the Western church from before that church divided" is tangled. (c) "The churches are known mostly from one letter, not from digging." A reader will take "churches" as congregations; the record means buildings. (d) "Who decides was the quarrel." is a clipped fragment. | world_core: "ancestral to the Western church before that church divided"; "unexcavated, not empty". | (a) "When bishops cannot settle a disagreement…". (b) "It is an ancestor of the Western church as it was before that church divided." (c) "The church buildings are known mostly from one letter, not from excavation." (d) "The quarrel was over who decides." |
| F13 | P2 | front: `sourcing.text`. Brief: `pairing_guidance.text`, `cautions[2]` | Process and status phrasing on a live surface. "any other built here so far" puts the build's own progress on a participant-facing page. "this record does not invent one" narrates the record's own method. "has not yet been tested" is a dated status line. `check_live_commentary.py` flags nothing beyond the `verified_on` dates, which it keeps. These are register slips, not changelog cruft. | Checker output: three `KEEP iso-date` lines only. | Front: "This world keeps more of its own words than most." Brief: "No pairing has been tested for this world." For the status line, see F5. |

## Writing judgment (item 3)

On FK, the author's numbers hold up. I measured a mean FK of 5.9 on the front (56 of 57 fields below 8) and 6.8 on the brief (25 of 27 below 8). No field is above grade 10, and no field is below Reading Ease 60. The don and gallic fronts score 6.8 and 6.5, so this is the fleet's pattern, not something lpc does alone.

I do not find the prose flattened or generic:

- The low grade comes from short, plain words, not from cut-down ideas.
- The mean sentence is 12.5 words, at the floor of the 12–20 target. No sentence runs past 25 words.
- Only 25 of 225 sentences have six words or fewer. Most of those are deliberate beats ("He is not." "The Donatists built their own.").
- The reasoning survives in plain words. For example: "To shut them out for good would say that one hour under pressure decides a life. To let them straight back would say the hour meant nothing."

All four signature images survive:

- **The wounded shepherd:** orientation[1], voices[0], who_speaks.
- **The certificate:** orientation[3]; the "certificates of peace" highlight.
- **The road walked in the open:** the tile and orientation[4].
- **The font answered twice:** orientation[10]. The brief's world_identity also has it.

I found no AI tells: no hedging filler, no assistant cadence, and no disclaimer used as a crutch. Specific phrasing faults are listed under F12. None of them is a finding of flattening.

Raising FK toward 8 for its own sake is not warranted. The fixes above are for clarity, not for grade.

## Safety summary (item 2)

The brief's safety architecture matches governance:

- Caution 2: the Facilitator checks every turn; Datus is not called on distress turns; code appends the resources.
- Caution 1: lean toward caution, and do not assume the person is fine.
- Caution 3: never make the redirect depend on the participant saying they are fine.

Nothing makes a redirect conditional. Two things need fixing:

- **F4 (P1):** the Numidicus caution can be read as Datus managing acute trauma.
- **F5 (P2):** the redirect-wording caution can be read as per-world redirect policy.

## Clean surface (item 4)

Neither file has a body after the front matter. That is cleaner than the don and gallic models, which carry long process bodies. `check_live_commentary.py` reports only `verified_on` dates, which it keeps. The register slips are listed under F13.

## Verdict

**Revise.** F1–F4 are P1. Each is a small, local text fix, and none of them needs a new record. Only the P1 fixes need a recheck, done as a targeted recheck, not a full re-review. The P2s should be fixed in the same pass. F6 also needs the records thread to carry two Phase Six cautions into a record.
