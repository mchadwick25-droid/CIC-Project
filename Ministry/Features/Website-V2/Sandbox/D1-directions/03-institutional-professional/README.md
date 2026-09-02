# D1 Direction 03 — Institutional-Professional / Scholarly Authority

**Sandbox artifact, 2026-09-02.** One of several independent D1 directions. Not a
deliverable; built to be torn down in D2. Files: `homepage.html` (the homepage),
`tradition.html` (the key inner journey: a tradition's record, presented in full
before anyone is asked to begin), this README. Both mockups open directly in a
browser; the only external dependency is Google Fonts, as on the live site.

## 1. The philosophy

The site is a scholarly instrument, and it says so at first glance. A serious
research library's digital exhibit does not open with a mood; it opens with what
the collection is, how it was assembled, and how much of it can be trusted. This
direction takes that posture whole. The first screen of the homepage carries the
state of the record (seven traditions open, 292 movements surveyed, ten eras
frozen, external review not yet begun); the first section under it is the ten-step
build method with its titles verbatim from the Construction Framework; the second is
the Constitution's five-level confidence vocabulary; the third is the register of
traditions as a catalogue table whose "evidentiary base" column reproduces the
census's own assessment of each record, thin spots included. The AI question is
raised by the site itself, in its fourth section, before anyone has to ask it.

Nothing on the page is decorative. Typography carries the hierarchy; a marginal
label column numbers the sections like a monograph; the only motion is the brand's
own "Arriving" mark. Credentialing is load-bearing: the Step 10 firewall quotation,
the 28-of-28 admission battery, the reviewer's brief, the published "where a
reviewer might press first" list are not footnotes here, they are the argument.

The inner journey pushes this to its conclusion. `tradition.html` is an archival
finding aid for the House-Churches: identifier, scope, evidentiary base with
disclosed dependencies, the gravity classification (including the one candidate
that was declined), contested ground, declared limits, the Representative's
derivation, and the four questions the record's own authors want a scholar to
press. The chair is pulled out the whole time — a quiet sticky bar carries "Chloe is
seated. Begin when you're ready — or read on" — but the record comes first on the
page.

## 2. The four charter goals, and the tension

**Accessibility.** A text-led, table-and-list design is the easiest kind to make
accessible and the easiest to keep that way. Real semantic tables (scoped headers,
row groups by era), landmarks, a skip link, visible focus, a 66ch measure, old-style
figures for reading, no information carried by color alone (every confidence level
has a word and a glyph). Floor and contrast math in §5.

**Clear storytelling.** The story this direction tells is the project's fourth
message: *the build is the product*. The homepage's own order is the narrative —
method, then confidence, then the register, then disclosure, then the chair. A
visitor who reads top to bottom has been told, in sequence, how a tradition is
built, how much to trust each claim, who is at the table, and what is unfinished.
The record page tells the same story at the scale of one tradition. The story of
Jesus' faithfulness across centuries is carried, in this direction, by the voices
themselves: Ignatius writing under guard, the unnamed householders history did not
bother to record, Chloe's own line "where we sound most alive, we are also, in one
specific and disclosed way, at our thinnest." The design's job is to give those
lines a page dignified enough to be believed.

**Easy access to features.** Resolved structurally, not by prominence. "Begin a
conversation" sits in the masthead on every page; every register row carries
"Read the record," "Begin with [name]," and the quiet "Bring to the Table" link in
the live site's exact grammar and deep-link form; the record page's seat bar is
sticky. The Table is one click from anywhere; it is simply not the first thing the
page argues for.

**Professional, cutting-edge design that draws visitors in.** Professional, yes —
this is the direction most obviously built by adults for adults, and it will read as
such to a pastor, a professor, or a skeptical reevaluator on first contact.
"Cutting-edge" is claimed on a narrower ground: publishing the method, the
confidence scale, the declined gravity, and the reviewer's own attack questions on
the public face of an AI product is genuinely unusual, and it is the thing here that
no competitor would copy.

**The warmth-versus-authority tension, directly.** This is the direction's real
risk, and it is not resolved by softening the register. It is resolved by where
the warmth is put. Three moves. First, the declared limits get the same typographic
dignity as the strengths — the honesty is the hospitality; a person whose faith is
unraveling has usually been burned by confident, unsourced claims, and a page that
says "here is what we cannot tell you" before "come sit down" is safer for exactly
that person. Second, the human weight is carried by the record's own voices rather
than by ornament, and by the protected lines used verbatim where they land. Third,
the chair is always visible and never pushed: the seat bar and the closing "The
chair has been pulled out the whole time" are the brand's "witness, not
recruiting" pair made physical. If D2 finds those three moves insufficient, the
direction is cold, and should be killed or hybridized rather than warmed with
imagery it has no honest use for.

## 3. What it deliberately sacrifices

- **The first-impression seeker who wants to feel before reading.** Someone
  arriving on a phone with thirty seconds gets a status band and a method grid,
  not a face. The Table CTA is one tap away, but the page is not designed to
  convert on emotion.
- **Portraits as the face of the site.** The seven locked portraits appear only on
  record pages, as plates with captions. The register uses the locked line emblems,
  and one row (Cappadocian) shows an empty dashed ring because no emblem exists yet
  — the record as it stands, not as we would like it.
- **Any imagery beyond the brand's own.** No photographs (the six site photos are
  not cleared and would not fit anyway), no illustration, no era-tinted grounds on
  the marketing surface.
- **Density on small screens.** The register scrolls horizontally inside its own
  container below 900px; the five-level scale stacks. Acceptable, but heavier than
  a card layout.
- **The site's current lightness.** The live homepage is one hero and one carousel.
  This is a long document. Returning visitors will use the masthead button and never
  scroll; first-time visitors are asked to read.

## 4. Typography, color, motion — inside the locked system

**Type.** Alegreya for reading and display; Alegreya Sans for labels, tables, chrome;
Alegreya SC (the same superfamily's true small caps) for section numerals, catalogue
identifiers, and the confidence labels. Alegreya SC is within the locked pairing's
family; if Mark reads it as a third face, it drops to `font-variant` small caps
with no other change. Old-style figures throughout except in identifiers. One
measure (66ch), one line-height (1.6), nothing under 13px carrying meaning.

**Color.** Every token is the brand's, used for the job the constitution assigns
it: madder for action only; **Tyrian for the confidence and transparency apparatus
alone** — the scale, the labels, the lexicon underline, the ✲ mark, the section
eyebrows that name the apparatus — so a visitor learns on the homepage the same
color they will meet inside the conversation; gold-leaf for the Representative as
rule and large text only (it clears AA on parchment by 0.04, so it never sets small
text); graphite never as text. Each register row carries its tradition's census
color as a 4px inset rule, non-text. The dark register uses the logo sheet's
`#EDE5D6` / `#CB6E52`, with buttons flipped to dark text on madder because light
text on that madder fails (2.85:1).

**Motion.** The "Arriving" mark plays once per page arrival, exactly as the live
stylesheet has it, and reduced-motion receives the still mark. Nothing else moves.
Hover states change underline weight and color only. The sticky seat bar and the
sticky marginal column are position, not motion.

## 5. Accessibility floor

**WCAG 2.2 AA is the floor, with three AAA practices adopted** because a text-led
design gets them nearly free and this site's readers skew toward long reading:
1.4.6 (7:1 for primary text — iron-gall on parchment is 13.7:1), 1.4.8 (measure ≤80ch,
line-height ≥1.5, no justified text), and 2.4.9 (link purpose from link text alone —
every register action names the Representative). Full AAA is not proposed: 1.4.6
for *all* text would forbid `--ink-faded` (5.4:1) as secondary text, and the
secondary register is where a catalogue lives.

Measured pairs (WCAG 2.x relative luminance), light register on parchment
`#F7F3EB`: iron-gall 13.70 · ink-faded 5.39 · madder 5.86 · madder-deep 8.20 ·
Tyrian 6.67 · gold-leaf 4.54 (large text and rules only) · graphite 3.38 (never
text) · vellum text on madder button 6.33. Dark register on `#17130F`: `#EDE5D6`
14.76 · `#B8AEA1` 8.45 · `#CB6E52` 5.18 (as text, and as button fill under
`#17130F` text) · Tyrian-light `#C4B0EA` 9.45 · gold `#E0A458` 8.47. Focus ring: 2px
madder, 3px offset (2.4.11/2.4.13). Targets: register links ≥28px rows, buttons
≥44px (2.5.8 passes at 24px). Reflow tested to 320px by construction: the register
is the only element that scrolls, inside its own container.

## 6. Proposed stretches — for Mark to rule on, not quietly done

1. **"Rigorous but not distracting — scholarship underneath, one click away"**
   (brand voice pair, FINAL) and **"Technology but not seen — experience first,
   governance second, mechanism third."** This direction inverts the order on the
   marketing site only: governance and method first, the experience one click away.
   The defense: what is shown first is the *shape* of the rigor (step titles, five
   labels, one-line sourcing), while the depth (registries, indices, footnotes)
   stays one click down, so "not distracting" holds even though "underneath" does
   not. This is the direction's single most attackable point and D2 should attack
   it there.
2. **The constitution's S0 threshold** makes the three doors the primary surface.
   The site is not S0 and the Website README says the constitution governs the app.
   Still, this homepage makes the record the primary surface and the door
   persistent chrome — the inverse of S0's door-primacy — and that should be an
   explicit ruling for the site, not an assumption.
3. **The mark's public sentence** appears in the hero frontispiece beside a 56px
   still mark, so the page's first contact with the mark carries its one sentence
   as the usage sheet requires. The mark therefore appears twice on the page
   (masthead, animated; frontispiece, still). Confirm this reads as one mark, not two.

## 7. Seams found while building

- `world-census.json` still carries "Richest written record of the **four** built
  worlds" for the Bethlehem Circle; reproduced verbatim in the register and flagged.
- The Cappadocian tradition has a locked portrait but no line emblem; the emblem set
  predates its admission. Rendered as an empty dashed ring, labeled.
- `tradition.html` references the House-Churches portrait from `cic-website/assets/
  portraits/` by relative path (six levels up). It resolves when opened from the
  repository; if the file is moved, the alt text stands in. Everything else in both
  files is inline.
- Nothing here promises Representative Modes, multi-voice seating, or external
  review as present. All three are listed under "What is unfinished."
