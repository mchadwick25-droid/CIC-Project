# D1 Direction 03 — Institutional-Professional / Scholarly Authority

**Sandbox artifact, 2026-09-02.** One of several independent D1 directions; built
to be torn down in D2. Files: `homepage.html`, `tradition.html` (the key inner
journey — a tradition's record, presented in full before anyone is asked to
begin), this README. Both open directly in a browser; the only external
dependency is Google Fonts, as on the live site.

## 1. The philosophy

The site is a scholarly instrument, and it says so at first glance. A serious
research library's digital exhibit does not open with a mood; it opens with what
the collection is, how it was assembled, and how much of it can be trusted. This
direction takes that posture whole. The homepage's first screen carries the state
of the record (seven traditions open, 292 movements surveyed, ten eras frozen,
external review not yet begun). The first section beneath it is the ten-step build
method, titles verbatim from the Construction Framework, with Step 0 shown as the
gate and Step 10 shown as the firewall. The second is the Constitution's five-level
confidence vocabulary. The third is the register of traditions as a catalogue
table whose "evidentiary base" column reproduces the census's own assessment of
each record, thin spots included. The fourth raises the AI question before anyone
has to ask it.

Nothing is decorative. Typography carries the hierarchy; a marginal column numbers
the sections like a monograph; the only motion is the brand's "Arriving" mark.
Credentialing is load-bearing: the Step 10 quotation, the 28-of-28 admission
battery, and the published "where a reviewer might press first" list are the
argument, not the footnotes.

`tradition.html` pushes this to its conclusion: an archival finding aid for the
House-Churches — identifier, scope, evidentiary base with disclosed dependencies,
gravity classification including the one candidate declined, contested ground,
declared limits, the Representative's derivation, and the four questions the
record's own authors want a scholar to press. The chair is pulled out the whole
time — a quiet sticky bar reads "Chloe is seated. Begin when you're ready — or
read on" — but the record comes first.

## 2. The four charter goals, and the tension

**Accessibility.** A text-led, table-and-list design is the easiest kind to make
accessible and to keep that way: real semantic tables with scoped headers and
era row-groups, landmarks, a skip link, visible focus, a 66ch measure, no
information carried by color alone (every confidence level has a word and a
glyph). Floor and contrast math in §5.

**Clear storytelling.** The story is the brand's fourth message, *the build is the
product*, told by the page's own order: method, confidence, register, disclosure,
then the chair. The story of Jesus' faithfulness across centuries is carried by
the record's voices — Ignatius writing under guard, the unnamed householders
history did not bother to write down, Chloe's own "where we sound most alive, we
are also, in one specific and disclosed way, at our thinnest." The design's job is
to give those lines a page dignified enough to be believed.

**Easy access to features.** Solved structurally, not by prominence. "Begin a
conversation" sits in the masthead on every page; every register row carries
"Read the record," "Begin with [name]," and the quiet "Bring to the Table" link in
the live site's exact grammar and deep-link form; the record page's seat bar is
sticky. The Table is one click from anywhere — it is simply not the first thing
the page argues for.

**Professional, cutting-edge design that draws visitors in.** Professional on
sight, to a pastor, a professor, or a skeptical reevaluator. "Cutting-edge" is
claimed on narrower ground: publishing the method, the confidence scale, a
declined gravity, and the reviewer's own attack questions on the public face of an
AI product is genuinely unusual.

**Warmth versus authority, directly.** This is the direction's real risk, and it is
not resolved by softening the register but by where the warmth is put. Three
moves. First, the declared limits get the same typographic dignity as the
strengths: the openness is the hospitality. A person whose faith is unraveling has
usually been burned by confident, unsourced claims; a page that says "here is what
we cannot tell you" before "come sit down" is safer for exactly that person.
Second, the human weight is carried by the record's own voices and the protected
lines used verbatim, never by ornament. Third, the chair is always visible and
never pushed — the seat bar and the closing "The chair has been pulled out the
whole time" are the "witness, not recruiting" pair made physical. If D2 finds
those three moves insufficient, the direction is cold and should be killed or
hybridized, not warmed with imagery it has no honest use for.

## 3. What it deliberately sacrifices

- **The seeker who wants to feel before reading.** Thirty seconds on a phone gets a
  status band and a method grid, not a face. The Table is one tap away, but the
  page is not built to convert on emotion.
- **Portraits as the face of the site.** The locked portraits appear only on record
  pages, as captioned plates. The register uses the locked line emblems, and the
  Cappadocian row shows an empty dashed ring because no emblem exists yet — the
  record as it stands.
- **Any imagery beyond the brand's own.** No photographs (the six site photos are
  not cleared, and would not fit), no illustration, no era-tinted grounds.
- **Density below 900px.** The register scrolls horizontally inside its own
  container; the confidence scale stacks. Acceptable, heavier than cards.
- **The live site's lightness.** One hero and a carousel become a long document.
  Returning visitors use the masthead button and never scroll; first-timers are
  asked to read.

## 4. Typography, color, motion — inside the locked system

**Type.** Alegreya for reading and display; Alegreya Sans for labels, tables,
chrome; Alegreya SC — the same superfamily's true small caps — for section
numerals, catalogue identifiers, and confidence labels. If Mark reads SC as a third
face, it drops to `font-variant` small caps with no other change. Old-style
figures throughout except in identifiers; one measure, one line-height; nothing
under 13px carries meaning.

**Color.** Every token is the brand's, used for the job the constitution assigns
it. Madder for action only. **Tyrian for the confidence and transparency apparatus
alone** — the scale, its labels, the lexicon underline, the ✲ mark, the eyebrows
that name the apparatus — so a visitor learns on the homepage the color they will
meet inside the conversation. Gold-leaf for the Representative as rule and large
text only (it clears AA on parchment by 0.04, so it never sets small text).
Graphite never as text. Each register row carries its tradition's census color as a
4px inset rule. The dark register uses the logo sheet's `#EDE5D6` / `#CB6E52`, with
buttons flipped to dark text on madder because light text on that madder fails
(2.85:1).

**Motion.** The "Arriving" mark plays once per arrival, exactly as the live
stylesheet has it; reduced-motion receives the still mark. Nothing else moves.
Sticky bars and the sticky marginal column are position, not motion.

## 5. Accessibility floor

**WCAG 2.2 AA is the floor, with three AAA practices adopted** because a text-led
design gets them nearly free and this site's readers skew toward long reading:
1.4.6 for primary text (iron-gall on parchment is 13.7:1), 1.4.8 (measure ≤80ch,
line-height ≥1.5, no justification), and 2.4.9 (link purpose from link text alone —
every register action names the Representative). Full AAA is not proposed: 1.4.6 for
*all* text would forbid `--ink-faded` (5.4:1) as secondary text, and the secondary
register is where a catalogue lives.

Measured (WCAG relative luminance), light register on parchment `#F7F3EB`:
iron-gall 13.70 · ink-faded 5.39 · madder 5.86 · madder-deep 8.20 · Tyrian 6.67 ·
gold-leaf 4.54 (large text and rules only) · graphite 3.38 (never text) · vellum
on madder button 6.33. Dark register on `#17130F`: `#EDE5D6` 14.76 · `#B8AEA1` 8.45 ·
`#CB6E52` 5.18 as text and as button fill under `#17130F` text · Tyrian-light
`#C4B0EA` 9.45 · gold `#E0A458` 8.47. Focus: 2px madder, 3px offset (2.4.11/2.4.13).
Targets: buttons ≥44px, register links ≥28px rows (2.5.8 passes at 24px). Reflow to
320px by construction — the register is the only element that scrolls, inside its
own container.

## 6. Proposed stretches — for Mark to rule on, not quietly done

1. **Two FINAL voice pairs are inverted on the marketing site only:** "Rigorous but
   not distracting — scholarship underneath, one click away," and "Technology but
   not seen — experience first, governance second, mechanism third." This homepage
   puts governance and method first and the experience one click away. The
   defense: what is shown first is the *shape* of the rigor (step titles, five
   labels, one-line sourcing) while the depth (registries, indices, footnotes)
   stays one click down — so "not distracting" holds even though "underneath" does
   not. This is the direction's most attackable point; D2 should attack it there.
2. **S0's door-primacy.** The constitution governs the app, not this site, but this
   homepage makes the record the primary surface and the door persistent chrome —
   the inverse of S0. That should be an explicit ruling for the site.
3. **The mark appears twice on the homepage** — animated in the masthead, still at
   56px in the hero frontispiece beside its one public sentence, so first contact
   carries the sentence as the usage sheet requires. Confirm it reads as one mark.

## 7. Seams found while building

- `world-census.json` still says "Richest written record of the **four** built
  worlds" for the Bethlehem Circle; reproduced verbatim in the register and flagged.
- Cappadocian has a locked portrait but no line emblem; rendered as an empty
  dashed ring, labeled.
- `tradition.html` loads the House-Churches portrait from `cic-website/assets/
  portraits/` by relative path (six levels up); it resolves from the repository,
  and the alt text stands in otherwise. Everything else in both files is inline.
- Nothing here promises Representative Modes, multi-voice seating, or external
  review as present; all three are listed under "What is unfinished."
- The corpus-wide "tradition," not "world" rule is applied to every visitor-facing
  line, including the reviewer's brief material on `tradition.html` (one
  substitution in its four questions). Left as "world" only in verbatim titles
  (World Profile, World Identification), the Step 10 quotation, and file names.
