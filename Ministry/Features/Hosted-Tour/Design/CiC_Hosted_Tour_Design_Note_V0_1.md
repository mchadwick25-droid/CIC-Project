# Hosted Tour — Design Note V0.1
## The Chloe demonstration tour: "A Sunday Gathering in Rome, As Justin Describes It"

**Date:** 2026-07-16
**Thread:** Hosted Tour Experience (Chloe demonstration tour)
**Status:** Design note for the demonstration deliverable. Nothing here modifies `cic-poc`, the map demo, or any governing document.
**Governed by:** Vision V1.1 (Conviction 4, Historical Responsibility); the Tours decision of 2026-07-07 (`CiC_FrontEnd_Decision_Log.md` — "only what the evidence actually supports is shown, played, or offered; where evidence runs out, the system says so plainly"); the No-Tier-5 rule (Construction Framework V7.3); Chloe's world's own construction record (`World-Builds/01-Post-Apostolic-House-Church/`, esp. Doc_09 Story Inventory) and deployment data (`cic-poc/backend/data/pahc_world/`, read-only).
**Conventions adopted from the map thread** (per `CiC_World_Orientation_Map_Decision_Log.md`, twenty-fourth pass): parchment/ink/gold tokens with Cinzel + Georgia, self-contained single-file HTML, caption strip docked BELOW the screen, tour engine (skippable, `?tour=1`, `?pose=N`, reduced-motion), PD-art-with-credits discipline, hover-for-short/click-for-full sourcing grammar, 10th-grade participant-facing copy.

---

## 1. What a Chloe tour IS

A tour is Chloe hosting, not the app presenting. The participant arrives from the World Orientation Map's "Take a tour with Chloe" button and is walked, stop by stop, through **one documented scene**: the Sunday gathering in Rome exactly as Justin Martyr describes it to the emperor (*First Apology* 65–67, c. 153–157 CE). Chloe narrates every stop in her own established register (per her Permanent Prompt: plain, short sentences, a household's measure, warmth at the door, honest silence held rather than filled). She relays Justin by name throughout — this is a witness's account carried by a host, never omniscient narration.

The tour is **skippable at any moment**, and skipping is never framed as failure — the open door is the point (Participant Agency). At one stop the participant sees the tour *pause* for a question and resume — demonstrating that a tour is conversation with structure, not a video with a chat box.

**Why this scene:** `pahcstory006` is the only Tier 1 narrated description of a worship gathering in any live world's Story Inventory — verified against the world's own Doc_09 (thirteen stories; 006's tier justification and usage guidance read in full). The launch prompt's suggestion checked out; its other candidate (the Didache's baptism and meal instructions) exists as `pahcstory009`/`pahcstory010` — both Tier 4 reconstructions, licensed but a categorically different claim, so they are named in the demo's ending as *future* tours rather than blended into this one (the world's own diversity-first rule: Justin's meal, the Didache's meal, and Ignatius's meal are three practices, never one composite).

## 2. The two voices

- **Chloe's voice (on the stage):** the content of the tour. Her words only ever carry what her sources carry. Register rules from the Permanent Prompt: short plain sentences; no answer over two short paragraphs; "we/our/among us"; disagreement kept visible; silence held honestly.
- **The product's voice (docked caption strip, below the screen, per Mark's house rule):** describes what the *feature* is doing at each step ("Every stop names its source", "The tour pauses for questions — it doesn't ignore them"). 10th-grade readability. Never speaks as Chloe, never adds historical claims.

## 3. The stops, with source basis

Every stop carries a source cartouche: citation + tier + confidence in the established five-level vocabulary, hover for the short form, click for the full source note.

| # | Stop | What happens | Source basis | Confidence label |
|---|------|--------------|--------------|------------------|
| 0 | **The Door** | Chloe welcomes; the threshold names what this tour is, what it's built from, and what it will not claim (one Roman writer's account — not a network template; other households kept the meal in other shapes) | `pahcstory006` front-matter + usage guidance; Permanent Prompt (hospitality register) | Tier 1 · Widely Accepted (Roman practice) / Contested (as network-wide template) |
| 1 | **The Day** | "On the day named for the sun," from city and countryside, to one place | Justin, *1 Apol.* 67 via `pahcstory006` | Widely Accepted |
| 2 | **The Reading** | Records of the apostles or writings of the prophets, "as long as time allows" | same | Widely Accepted |
| 3 | **The Word** | The one presiding exhorts to imitate these good examples | same | Widely Accepted |
| 4 | **The Prayers** | All stand together and pray. Honest inline note: Justin gives no words — none are shown | same; the *absence* per the story text itself | Widely Accepted (that they prayed standing) — the words themselves: not in evidence |
| 5 | **The Bread and the Cup** | Bread, wine mixed with water; thanksgiving "according to his ability"; the Amen. **Q&A demonstration:** participant asks "Who is the one presiding — a bishop?"; Chloe answers with the world's own unsettledness (bishop / council of presbyters, both real, unresolved — Doc_01/Capsule), and the tour resumes | `pahcstory006`; the presiding question: World Capsule Core + Permanent Prompt (the unsettled authority question is this world's own live tension) | Widely Accepted (the meal's shape) · the authority question: held open, as the world held it |
| 6 | **The Collection** | Voluntary giving, laid with the presider, for orphans, widows, the sick, prisoners, strangers — "all who are in need" | Justin, *1 Apol.* 67 via `pahcstory006` | Widely Accepted |
| 7 | **What We Cannot Show You** | The honest-decline stop (required by the launch prompt; three real declines, each sourced as an absence): (a) **the room** — no image of any gathering place survives from this world's window; its period is archaeologically invisible, and the famous later images (Dura-Europos) are Excluded registry rows this world refuses to borrow; (b) **the exact words** of the prayers and thanksgiving — Justin says "according to his ability"; no fixed text existed to preserve; (c) **the people** — of the ordinary members of such a room, two names survive in this world's entire evidence base: "Tavia, and the wife of Epitropus. A name and a greeting. Nothing more." No story is constructed for them. | (a) Doc_09 §4 item 10 (Doc_02 §5: archaeologically invisible; P11/P12 Excluded); (b) `pahcstory006` story text; (c) Doc_09 §4 item 9 (Ignatius, *Smyrn.* 13:1–2 / *Pol.* 8) | Stated as Documented absences — the label the world's own record gives them |
| 8 | **The Way Out** | Chloe hands back; the honest stub ending: "This is a design demonstration — it ends here, honestly." Plus the truthful forward view: where sources allow, more tours (the catechumen's path to the water — Tier 4, explicitly-marked reconstruction register); where a world has no documented scene, the button will say so plainly instead of opening | Ending convention from the map thread; forward view per `pahcstory009`/`010` and the Tours decision | — |

## 4. What this tour honestly declines to show (the rule, applied)

Mark's worked example from the Tours decision — "sit through a sermon" in a world with no documented sermons → "this world doesn't have the documented sources to describe this" — is generalized here as a **first-class stop**, not an error state. Stop 7 exists *because* the House-Churches' record runs out in exactly the places a visitor most wants to go (the room's look, the prayers' words, the people's faces). The demo treats each decline as testimony: the absence is stated in Chloe's own voice, with the same source cartouche as any positive claim, citing where the world's own record establishes the absence. Also declined, silently (they simply never appear): any depiction of Chloe or her people, any music, any sensory texture beyond the sourced elements — per the No-Tier-5 rule extended to every medium.

## 5. Imagery decision for this world

The map thread's PD-art discipline is adopted — and for *this world* the honest application is: **no period scene or person imagery inside the tour at all**, because this world's own record licenses none (archaeologically invisible; Dura-Europos/Abercius Excluded; the era-medallion Fayum portrait is era iconography on the map, not evidence about this world, and is not imported into the tour). The tour's visual layer is instead: the shared engraved/parchment aesthetic (UI chrome, claiming nothing), **engraved text-plates** of Justin's own quoted words (an image of a source's words is the one picture this world can honestly show), and a small **engraved sequence diagram** of the gathering's order (reading → word → prayers → meal → collection) — a structural visual derived from Justin's own reported order, not invented scenery. The demo's credits line carries the map thread's principle forward: the tour's honesty extends to its own artwork.

## 6. Engine and recording (conventions, adopted unchanged)

Scripted steps with captions docked below; moving gold pointer; skippable at any moment; `?tour=1` auto-start; `?pose=N` instant-state mode for headless-Chrome frame capture; `prefers-reduced-motion` respected; recording assembled with Pillow into a GIF plus a captioned slideshow HTML. Both themes (parchment / old leather) via the map demo's own token pattern.

## 6a. The immersive build-out (V0.2 of the demo, same day, at Mark's direction)

Mark asked for time/world-specific art, ruins photography, and audio. Applied within the discipline — every added medium follows the same rule as a sentence:

**Photographs — four, all real, all verified before use, each carrying its credit on hover and an honest "what this is / is not" caption:**
1. *The Door:* atrium of the House of the Menander, Pompeii (buried 79 CE — the decade the world opens). Caption states plainly: the setting culture's house, not a gathering place of this community; none of theirs has ever been found. (Photo: Carole Raddato, CC BY-SA 2.0.)
2. *The Day:* the Decumanus Maximus at Ostia, Rome's harbor town — 2nd-century streets and brick housing. "The stones are real; the walkers are not shown, for no image of us survives." (Photo: Mister No, CC BY 3.0.)
3. *The Reading:* Rylands Papyrus P52 — the oldest surviving scrap of a Christian book, copied c. 125–175 CE, within the world's own lifetime; labeled as the era's artifact (Egyptian preservation), not this community's own. (John Rylands Library, public domain.)
4. *The Bread and the Cup:* a real carbonized loaf from Pompeii, scored in eight. "Whether this very shape sat on our tables, no source says." (Photo: User:Beatrice, CC BY-SA 2.0 IT.)

The line held: setting-culture archaeology and era artifacts, presented as exactly that — never staged scenes, never depicted people, and still nothing from the Excluded rows (no Dura-Europos). Duotone-adjacent sepia unification is applied in CSS, keeping the source photos unaltered inside the file.

**Audio — two clips, both source-performative per the Tour module's standing audio policy (audio only where the source itself was spoken):**
1. *The Word:* the Two Ways teaching, Didache 1:1–2 (Registry P01) — introduced by Chloe with the sermon-absence named first ("No sermon of ours survives in our own records — none was written down. But the plain teaching I give those preparing for the water *was* written"), which is Mark's own worked example from the Tours decision, answered in-world.
2. *The Way Out:* Justin's account whole, *First Apology* 67 (after the public-domain ANF translation).
Both are neural-TTS modern readings (Microsoft neural voices via edge-tts), each labeled on the player: a modern reading, English translation of a Greek original, **no accent claimed** — a regional "accent" for 2nd-century Rome/Antioch does not exist to reproduce, and faking one is invented texture. Transcripts attached to each player. The Representative herself remains unvoiced, per the standing ruling.

**Music — declined, in-world.** The honest-decline stop gained a fourth decline, THE SINGING: Pliny's report of pre-dawn singing (Registry P07, `pahcstory004`) is cited with the care its own usage guidance requires — the testimony was extracted by torturing two enslaved ministrae, and Chloe names their cost before quoting the page. What was sung was never recorded; no music is played and none invented.

## 7. Flags (not resolved here, not invented around)

1. **Stop 5's Q&A answer** paraphrases the world's unsettled authority question from the deployed Capsule/Permanent Prompt. The wording was written for Chloe's register and should get Mark's read before any public showing — she is his Representative.
2. **"Sermon" phrasing:** Justin describes an exhortation happening; no sermon text survives *within this world's own evidence base* (its six primary voices include no sermon transcript). The demo says only that — it does not claim "no early Christian sermon survives anywhere," which would be a wider claim than this world's record can carry.
3. The demo ends at a stub by design; actual handoff into a live encounter is the assembly session's question (see the Integration Note).
