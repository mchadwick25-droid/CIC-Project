# CiC Hosted Tour — Decision Log

Dated entries: what was decided, the reasoning including the heart of it, the next
action. This thread builds the "Take a tour" experience — first as a demonstration
tour of The House-Churches (Chloe) — filling the map thread's "Take a tour with
{Representative}" button. It does not modify `cic-poc`, the map demo, the
census/atlas files, or any governing document.

---

## 2026-07-16 — Founding pass: the Chloe demonstration tour designed, built, and recorded

Deliverables, all in `Ministry/Technology/Hosted-Tour/`:
`CiC_Hosted_Tour_Design_Note_V0_1.md` · `CiC_Chloe_Tour_Interactive_Demo.html`
(~90KB self-contained) · `CiC_Chloe_Tour_Demo_Flow.gif` (1.63 MB, 12 frames, ~78s
loop) · `CiC_Chloe_Tour_Flow_Slideshow.html` (twelve captioned frames, auto-play +
arrows) · `CiC_Hosted_Tour_Integration_Note_V0_1.md`.

### Decided: the demonstration tour is "A Sunday Gathering in Rome, As Justin Describes It" — nine stops, one documented morning

Verified against the world's own Doc_09 before building (not trusted from the launch
prompt): `pahcstory006` (Justin Martyr, *First Apology* 65–67) is Tier 1 — the only
Tier 1 narrated liturgical description in any live world — Widely Accepted for Roman
practice, Contested as a network template. The launch prompt's other candidate (the
Didache's baptism/meal instructions) is licensed but Tier 4; it is named at the
tour's ending as a *future* tour in reconstruction register, never blended into this
one (the world's own diversity-first rule). **The heart of it:** the first tour
anyone sees should carry the strongest claim the portfolio can honestly make — a
witness's own words, relayed by name — so the register of the whole feature is set
by testimony, not production.

### Decided: Stop 8, "What We Cannot Show You," is the tour's centerpiece decline — three documented absences

Per the Tours rule (front-end log, 2026-07-07) an honest "we can't show you this"
stop is a feature; this tour carries three, each cited to the world's own record:
the room (window archaeologically invisible, Doc_02 §5 / Doc_09 §4 item 10;
Dura-Europos and Abercius are Excluded rows P11/P12), the words of the prayers
(Justin's own "according to his ability" — extempore, nothing to preserve), and the
people (exactly two ordinary members named in the entire evidence base — "Tavia, and
the wife of Epitropus. A name and a greeting. Nothing more." Doc_09 §4 item 9).
**The heart of it:** the tour's most memorable stop is the one where it refuses —
Conviction 4 staged as experience rather than stated as policy.

### Decided: no scene or person imagery in this tour at all — and the credits line says why

The map thread's PD-art discipline was adopted and then honestly applied to this
world's evidence: it licenses none. The visual layer is the shared engraved/
parchment chrome, engraved text-plates of Justin's quoted words (an image of a
source's words is the one picture this world can show), and the order-tracker band
(reading → word → prayers → bread & cup → collection) — a structural visual drawn
from Justin's own reported sequence. The tray credits line extends the map's own
principle: "no scene imagery is shown because none survives from this world's own
window: the tour's honesty extends to its own artwork." The era-medallion Fayum
portrait was deliberately NOT imported from the map — era iconography there, an
evidence claim here.

### Decided: two voices, strictly separated

Chloe speaks on the stage, only in her Permanent-Prompt register (short plain
sentences, a household's measure, warmth at the door), only what her sources carry —
including the Q&A demonstration at Stop 6, where the who-presides question gets the
world's own unsettled answer ("I will not close for you what our own life has not
closed"). The product speaks only in the caption strip docked BELOW the stage
(Mark's house rule, adopted from the map thread's twenty-third pass), at 10th-grade
readability, about what the *feature* is doing — never as Chloe, never adding
historical claims.

### Adopted unchanged from the map thread (per its twenty-fourth pass)

Visual tokens copied from the reference demo's own CSS (including `--live-chloe`
and the identical inlined Cinzel data-URI, spliced programmatically so the faces
cannot drift); self-contained single-file pattern; tour engine (skippable, `?tour=1`
auto-start, `?pose=N` instant-state, reduced-motion respected, honest stub ending);
the pose-mode + headless-Chrome + Pillow recording pipeline (the extension GIF
recorder limitation is confirmed noted); hover-for-short/click-for-full as the one
sourcing grammar (the per-stop source cartouche).

### Verification record

All 12 pose frames captured via headless Chrome and visually inspected; two fixes
found and applied during verification: (1) the Q&A answer was clipped at the stage
edge in pose 8 — auto-scroll added so Chloe's answer is fully visible (it is the
payload of that step); (2) the slideshow's frame image could push captions below
the fold — height-constrained so caption and controls always fit. Chrome headless
requires absolute `--screenshot=` paths (relative paths silently write nothing) —
recorded for the next builder. Build scripts (`build_tour_recordings.py`, splice
step) live in this session's scratchpad; the HTML files are the durable source.

### Flagged, not resolved (for Mark / the assembly session)

1. **Chloe's scripted lines need Mark's read** before public showing — especially
   the Stop 6 Q&A answer, written for her register from the deployed Capsule and
   Permanent Prompt. She is his Representative.
2. **The return path** from tour ending back to the World Map is a one-line
   addition touching both demos — belongs to the assembly session (see Integration
   Note).
3. **"Sermon" scoping:** the tour never claims "no early sermon survives anywhere,"
   only that this world's own evidence base includes none — the wider claim would
   exceed the record (design note §7).

**Next action:** Mark plays the demo (`?tour=1` for the guided walk), marks up
Chloe's wording, then the assembly session combines this with the map thread's
package — shared tokens first, then the two-file handoff per the Integration Note.

---

## 2026-07-16 — Immersive build-out (demo V0.2): real images, real audio, and the two honest refusals inside Mark's ask

**Mark's direction:** build the Chloe tour out with time/world-specific art,
pictures of ruined buildings from the time, and audio (music or teaching, quality
voice generation, regional accent in English or original language with subtitles) —
immersive, loyal to the source texts and time/location.

**Built (demo now ~1MB self-contained, 13 tour steps; GIF 2.5MB/87s and
thirteen-frame slideshow rebuilt via the same pipeline):**

- **Four photographs, all real, all verified visually before inclusion, each with
  hover-credit and an honest "what this is / is not" caption:** the House of the
  Menander atrium at Pompeii (buried 79 CE — the world's opening decade) at The
  Door; a second-century Ostia street at The Day; Rylands Papyrus P52 (a Christian
  book page copied within the world's own lifetime) at The Reading; a real
  carbonized Pompeii loaf at The Bread and the Cup. **The line held:**
  setting-culture archaeology and era artifacts presented as exactly that — never
  claimed as this community's own places, no depicted people, and still no
  Dura-Europos (Excluded row). Licenses: CC BY-SA 2.0 (Raddato), CC BY 3.0
  (Mister No), CC BY-SA 2.0 IT (Beatrice), PD (Rylands); credits carried on hover
  and in the tray line.
- **Two audio clips, both source-performative per the standing audio policy:** the
  Two Ways (Didache 1:1–2) at The Word — introduced by Chloe naming the sermon
  absence first, which is Mark's own worked example answered in-world — and
  Justin's account whole (1 Apol. 67, PD translation) at The Way Out. Neural TTS
  (edge-tts), transcripts attached, each player labeled: modern reading, English
  translation of a Greek original, **no accent claimed.**

**Two refusals inside the ask, named to Mark plainly rather than quietly skipped:**

1. **No regional accent.** No accent for 2nd-century Rome/Antioch exists to
   reproduce in English; performing one would be invented texture — the audio says
   so on its own label. **The heart of it:** an accent is a claim the evidence
   cannot carry, made in the most memorable medium there is.
2. **No music.** Instead of silently omitting it, the honest-decline stop gained a
   fourth decline, THE SINGING: Pliny's report of pre-dawn song (P07/pahcstory004)
   quoted with the cost its own usage guidance requires named — the testimony came
   from torturing two enslaved ministrae — and the plain statement that what was
   sung was never recorded by anyone. The music request is thus answered *inside
   the world's own voice*, as testimony, not as a feature gap.

**Verification:** all 13 pose frames recaptured and inspected; one timing bug found
and fixed (figure scroll racing image layout — reveal now waits on image load).

**Next action:** Mark reviews the enhanced demo (especially Chloe's new lines at
The Word and THE SINGING decline) before any public recording; assembly session
unchanged.

---
