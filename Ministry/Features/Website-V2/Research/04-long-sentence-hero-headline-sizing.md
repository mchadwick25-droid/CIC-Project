# 04 — Sizing a full sentence as the hero headline: what real editorial sites do, and a middle-ground treatment for the CiC hook

**Workstream:** Website V2 · **Kind:** research brief (input to one CSS decision; decides nothing) · **Date:** 2026-09-08 · **Researched by:** Fable · **Companions:** `01-narrative-invitation-design-patterns.md`, `02-craft-and-visual-quality-bar.md`

**Why this brief exists.** The homepage hero was rewritten from a twelve-word tagline ("Twenty centuries of the Church. One table. A chair pulled out for you.") to Mark's own twenty-one-word sentence: *"Encounter representative voices and the two-thousand-year story, coming to life from the actual letters, sermons, and records of distinct Christian traditions."* At the old display size (`clamp(2rem, 4.5vw, 3rem)`, 32–48 px) it ran five to eight lines and outweighed the section beneath it, so it was resized to `clamp(1.375rem, 2.6vw, 1.75rem)` (22–28 px), weight 400, line-height 1.4, in the 38 rem reading measure, still centred (`CiC_FrontEnd_Decision_Log.md` ≈ line 3105). Mark's response: *"while I agree to shrink the hook, it is too small here… this feels small to me."* He asked specifically for what other real websites do when a genuinely long, specific sentence is the primary hero statement — not a short tagline with a smaller deck beneath it. This brief answers that and ends with one concrete CSS treatment.

**The short version.** Mark's instinct is right and it is measurable. Two things happened at once when the hook was shrunk: (1) it dropped out of the *headline* register into the *standfirst* register — 22–28 px on a 17 px body is 1.3–1.65×, which is exactly where the Guardian, BBC, GOV.UK, Tailwind and Tufte all put the *secondary* sentence that sits *under* a headline; and (2) it became smaller and lighter, at every viewport, than the "The Story We Are In" `h2` directly below it (25.6–32 px, weight 500). A sentence-length statement with nothing above it has to carry the headline register itself, and the closest real precedent for a full sentence set as a headline is not a SaaS hero but a newspaper article headline: the Guardian sets every standard article headline — routinely 15–25 words — at **34 px, weight 500, line-height 1.15, in a ~620 px column**, and its long-reads at 50 px. The well-evidenced middle ground for CiC is **24 → 34 px, weight 500, line-height ≈1.25, 38 rem measure, centred at ≥ 641 px and left-aligned on phones** — with the `h2` beneath it stepped down one notch so the ladder reads 34 → 28 → 17.

---

## 0. How this was researched, honestly

Direct fetches of the reference sites (emergencemagazine.org, plough.com, craigmod.com, aeon.co, nytimes.com, theguardian.com, annefrank.org, nfb.ca, practicaltypography.com, nngroup.com) are blocked by the sandbox proxy, as in briefs 01–03. Three kinds of evidence were available and every claim below is tagged with one of them:

- **[verified]** — a stylesheet or design-system source file fetched in full from GitHub and read directly: the Guardian's live rendering code (`dotcom-rendering` `Standfirst.tsx`, `ArticleHeadline.tsx`) and its Source design-system presets (`csnx` `__generated__/typography.ts`), the Guardian's older `guss-typography` scale, BBC GEL's `_settings.scss`, GOV.UK Frontend's `_typography-responsive.scss`, Tufte CSS, gwern.net's `initial.css`, Tailwind's typography plugin `styles.js`, Utopia's defaults — plus the CiC repo itself.
- **[indexed]** — the text of a named page as returned by web search, where the page could not be fetched (Butterick, Poynter, Material 3, FT Origami, NN/g-derived summaries, Fonts In Use, Stuff & Nonsense, Piccalilli, and the trade-press pieces on Snow Fall, Firestorm, Bear 71, Emergence). Numbers from these are quoted as the search index returned them and should be treated as "probably right, not re-checked."
- **[inference]** — my own reasoning or arithmetic, said so each time.

The web-search budget (200 queries) was exhausted. A small part of that was my error — a runaway batch of malformed, duplicate queries at the end of one search wave, which returned nothing and cost roughly forty calls. No finding was lost to it (the useful searches had already run), but any follow-up in this session must use GitHub fetches only.

Line-count figures for the CiC sentence are estimates from a Python model (Alegreya average advance ≈ 0.42–0.46 em, 159 characters); the real check is a browser screenshot at 360, 390, 768 and 1280 px.

---

## 1. What the site actually has right now [verified: `cic-website/index.html`, `assets/style.css`]

| Element | Rule | Rendered size (17 px body) | Weight | Line-height |
|---|---|---|---|---|
| Body | `font-size: 1.0625rem; line-height: 1.65` (Alegreya) | 17 px | 400 | 1.65 |
| All headings (base) | `h1,h2,h3,h4 { font-weight: 500; line-height: 1.15; text-wrap: balance }` | — | **500** | 1.15 |
| **Hook, old** (`style.css` line 152, now overridden) | `clamp(2rem, 4.5vw, 3rem)`; lh 1.15 | 32 → 48 px | 500 (inherited) | 1.15 |
| **Hook, current** (`index.html` line 94) | `clamp(1.375rem, 2.6vw, 1.75rem)`; `font-weight: 400`; `line-height: 1.4`; `max-width: var(--measure)` (38 rem) | **22 → 28 px** | **400** | **1.4** |
| "The Story We Are In" `h2` (line 102) | `clamp(1.6rem, 3.2vw, 2rem)` | **25.6 → 32 px** | 500 (inherited) | 1.15 |
| Who `h2` (line 113) | same as story `h2` | 25.6 → 32 px | 500 | 1.15 |
| Hero container | `.hero { max-width: var(--col) /* 44rem */; text-align: center }` | — | — | — |
| Fonts loaded | Alegreya 400 / **500** / 700 (+ italic 400, 500) | | | |

Three observations fall straight out of that table:

1. **The `h1` is now outranked by the `h2` beneath it at every viewport.** 22 vs 25.6 px on a phone; 28 vs 32 px on desktop; weight 400 vs 500; leading 1.4 (paragraph-like) vs 1.15 (heading-like). Whatever the absolute numbers, a page whose first heading is visibly smaller and lighter than its second heading will "feel small," because the eye reads it as a deck for the section below rather than as the statement the section serves. This is the mechanism behind Mark's reaction, and it is fixable without going back to display size.
2. **Three properties moved down at once.** Size (−33 % at the top end), weight (500 → 400) and leading (1.15 → 1.4) were all changed in the same edit. Each is individually defensible; together they moved the line from "headline" to "lead paragraph." The middle ground is to give one or two of them back, not all three.
3. **Alegreya 500 is already loaded**, so using it costs nothing. (Alegreya is a light-ish oldstyle with a modest x-height; at 22–28 px its regular weight reads more delicate on screen than a Guardian Headline or Georgia would at the same size — a further reason 400 at this size reads "small." [inference])

---

## 2. What the narrative, documentary and essay sites actually do at the top

Mark asked for real sites facing *the same* problem. The honest finding is that most of the reference sites from briefs 01–02 do **not** set a long sentence as their hero; when a long specific sentence appears at the top, it is almost always the *standfirst / abstract* under a short title. That matters, because it tells us where the current CSS drifted to and why it reads small.

| Site / piece | What is at the top | Long-sentence treatment | Evidence |
|---|---|---|---|
| **NYT, *Snow Fall*** (2012) | Short title "Snow Fall" + deck "The Avalanche at Tunnel Creek" + byline, in NYT Cheltenham; the famous long opening sentence is *body copy* over the image | Not a sentence-as-headline case | [indexed: Poynter; Source/OpenNews "How we made Snow Fall"; Fonts In Use]. Sizes unverifiable. |
| **NYT article page** (2013 redesign, still the pattern) | Headline in NYT Cheltenham at **1.9375 rem = 31 px** | Sentence-length headlines are normal here | [indexed: Fonts In Use, "The New York Times article redesign (May 2013)"] |
| **Guardian, *Firestorm*** (2013) | Title, then full-width video chapters; "magazine-style copy" | Not a sentence-as-headline case | [indexed: journalism.co.uk; Poynter; MIT Docubase]. Sizes unverifiable. |
| **Guardian article / long-read** (live code) | Sentence-length headline at 34 px (standard) or 50 px (immersive), weight 500; standfirst at 17–24 px beneath | **The closest real precedent** — see §4 | [verified: `dotcom-rendering`] |
| **NFB, *Bear 71*** | An announcement of the running time, a preloader, an animated wordmark (Patrick Johnson), then video; first line "We're watching her. She's watching us." | Short lines; no long-sentence hero | [indexed: sometimes.ca (Aubyn Freybe-Smith); MIT Open Doc Lab; NFB] |
| **Anne Frank House** (IN10 / DOOR) | "Corporate + storytelling" split; no numeric typography on record | Unverifiable | [indexed: Communication Arts; annefrank.org colophon] |
| **Emergence Magazine** (Studio Airport) | Faces on record (GT America, Rosart, GT Super Italic, Fragen); "slow consumption… balanced typography… minimal navigation" | No sizes on record | [indexed: Fonts In Use Vol. 1; Awwwards; Webby] |
| **Plough** | "Refresh… especially the logo and typography"; compact nameplate to make room for art | No sizes on record | [indexed: "Retooling the Plough"] |
| **craigmod.com** | Essays in one column; his own guidance is 12–15 words per line for reading text, and that "minuscule changes to font sizes" drove the last redesign | No sizes on record | [indexed: "A Simpler Page"; "Hello, Again"] |
| **Aeon** | PT Serif body, grotesque for apparatus, drop caps; standfirst present | Size unverifiable | [indexed: Fonts In Use] |
| **gwern.net** | Page title 2.5 em on a 20 px base (= 50 px desktop; 2 em = 36 px mobile), weight 600, **centred**, lh 1.15, small-caps; the long opening abstract at 19/20 of body size, italic, centred, lh 1.5 | The long sentence is kept at *body* size, italic, under a short title | [verified: `css/initial.css`] |
| **Tufte CSS** | `h1` 3.2 rem = 48 px, weight 400, lh 1; `p.subtitle` 1.8 rem = 27 px, italic, lh 1; body 1.4 rem = 21 px; `h2` 33 px italic 400 — all headings regular weight, all left-aligned, 55 % measure | A sentence-length subtitle at 1.29× body, italic | [verified: `tufte.css`; the demo uses `p.subtitle` for the author line] |
| **Anthropic.com** (for the "regular-weight serif display" register only) | Serif display headline ~96 px weight 400 lh 1.1; page `h1` ~61 px weight 700 | Short lines; not applicable to a 21-word sentence | [indexed: designmd / duply token extractions] |

**What this survey establishes.** Nobody in the story-led genre sets a 21-word sentence at display size; nobody sets it at 22 px either. When the sentence sits under a short title it lives at 1.2–1.5× body (gwern, Tufte, Aeon, the Guardian standfirst). When the sentence *is* the title — which is the choice CiC has made, deliberately, with no short line above it — the only mature, high-volume precedent is the newspaper article headline, and that is where the numbers in §4 come from.

---

## 3. The standfirst / deck convention, with numbers

The standfirst (UK) or deck/dek (US) is the named editorial convention for "a longer descriptive sentence beneath the headline." It is what the current CiC CSS has, in effect, become. Concrete values, body size in brackets:

| Source | Standfirst / lead | Ratio to body | Weight / style | Line-height | Tag |
|---|---|---|---|---|---|
| **Guardian** live site (`Standfirst.tsx`), body `article17` = 17 px | Standard: `headlineMedium17` mobile → `headlineMedium20` tablet+; Immersive: `headlineMedium20` → `headlineMedium24`; Comment/Obituary use `headlineLight` | 1.0 → 1.18 (standard); 1.18 → 1.41 (immersive) | 500 (medium) or 300 (light); Guardian Headline face | Presets ship at 1.15 | [verified] |
| **BBC GEL** (`_settings.scss`), body-copy 16 px desktop | Double Pica 24/28 (intro tier); Paragon 28/32 | 1.5; 1.75 | — | 1.17; 1.14 | [verified] |
| **GOV.UK Frontend** (`_typography-responsive.scss`), body 19 px | Lead paragraph = scale 24: 21/25 mobile, 24/30 tablet+ | 1.26 | 400 | 1.19 → 1.25 | [verified] |
| **Tailwind `prose`** (`styles.js`) | base: p 16/28, `.lead` 20 px lh 1.6; lg: p 18, lead 22 lh 1.45; xl: p 20, lead 24 lh 1.5 | 1.20–1.25 | 400 | 1.45–1.6 | [verified] |
| **Tufte CSS** | `p.subtitle` 27 px on a 21 px body | 1.29 | 400 italic | 1.0 | [verified] |
| **gwern.net** | abstract at 19/20 × body (≈19 px on 20) | 0.95 | italic | 1.5 | [verified] |
| **Piccalilli**, "Some simple ways to make content look good" | `.lede` = `clamp(1.25rem, 1.16rem + 0.43vw, 1.5rem)` (20–24 px), italic, `max-width: 50ch` | ≈1.25–1.5 | 400 italic | — | [indexed] |
| **Carmen Ansio**, "Editorial Typography in CSS" | `--step-lead: clamp(1.1rem, 0.9rem + 0.6vw, 1.35rem)`; `--step-display: clamp(2rem, 1rem + 4vw, 3.5rem)` | ≈1.1–1.35 | — | — | [indexed] |
| **Poynter**, "Hierarchy Within Headlines" (2002, print) | Main head 36 pt → first deck 18 pt → second deck 14 pt; "if the main headline is bold, the decks should be lighter; a Roman main head may take italic decks" | deck ≈ ½ headline | lighter / italic | — | [indexed] |
| **Stuff & Nonsense** (Andy Clarke), "Designing standfirst paragraphs" | "Two, three or four lines… 20–50 words"; distinct from headline and body "by increasing its size or contrast using a heavier or lighter weight"; "no rule book" | — | — | — | [indexed] |

**Reading the table.** The standfirst tier clusters tightly at **1.2–1.5× body**, regular or light weight, often italic, with a paragraph-ish line-height of 1.3–1.6. The current CiC hook — 1.29× body at the phone end, weight 400, line-height 1.4 — is a textbook standfirst. The Guardian standfirst is *literally* `headlineMedium20`/`24`, i.e. 20–24 px medium; CiC's 22–28 px regular sits right beside it. The only thing missing is the headline it is supposed to sit under. That is the whole diagnosis.

---

## 4. The "sentence as headline" precedent, with numbers

Where a full sentence *is* the headline, the mature pattern is the newspaper article page. Values, body in brackets:

| Source | Headline | Ratio to body | Weight | Line-height | Column / alignment | Tag |
|---|---|---|---|---|---|---|
| **Guardian** (`ArticleHeadline.tsx` + Source presets) | `decideHeadlineFont`: **34 px** standard (`headlineMedium34` = 2.125 rem), **50 px** immersive (`headlineBold50`); available headline sizes 14/15/17/20/24/28/34/42/50/64 | 2.0 (standard); 2.94 (immersive) | 500 default; 300 "light" for Comment/Obituary; 700 for Feature/Review/Interview | **1.15** on every preset; Interview overrides to 35 px / 42 px (≈1.03 / 1.24) | ~620 px article column, **left-aligned**, headlines routinely 2–4 lines | [verified] |
| Guardian `guss-typography` (older scale) | headline levels 20/24, 24/28, 28/32, 32/36, 36/40, 40/44, 44/48 | — | — | ≈1.10–1.14 (+4 px) | — | [verified] |
| **NYT article** (2013 redesign) | 1.9375 rem = **31 px** Cheltenham | ≈1.9 (on ~16–17 px) | — | — | — | [indexed: Fonts In Use] |
| **BBC GEL** | Trafalgar 32/36 desktop (standard headline); Canon 44/48 (feature) | 2.0; 2.75 | — | 1.125; 1.09 | — | [verified] |
| **GOV.UK** | scale 36: 27/30 mobile → 36/40 tablet; scale 48: 32/35 → 48/50 | 1.89; 2.53 | 700 | 1.11; 1.04 | left | [verified] |
| **Material 3** | Headline Large 32/40, Medium 28/36, Small 24/32; Display Small 36/44; Title Large 22/28 | 2.0 / 1.75 / 1.5 / 2.25 / 1.375 (on 16) | **400 throughout** | **1.25–1.33** (designed to wrap) | — | [indexed: m3.material.io + two cheat-sheets agree] |
| **FT Origami** `o-typography` scale | 3: 24/28 · 4: 28/32 · 5: 32/32 · 6: 40/40 · 7: 48/48 | — | — | 1.17 → 1.0 as size rises | — | [indexed: npm README] |
| **Tufte CSS** | `h1` 48 px, weight **400**, lh 1; `h2` 33 px italic 400 | 2.29; 1.57 | 400 | 1.0 | left, 55 % width | [verified] |
| **gwern.net** | title 50 px desktop / 36 px mobile, weight 600, centred, lh 1.15 | 2.5 | 600 | 1.15 | centred (short titles) | [verified] |
| **Tailwind `prose`** | `h1` 36 px (base) / 48 (lg) / 56 (xl), weight 800, lh 1.11 → 1.0; `h2` 24 / 30 / 36, weight 700, lh 1.33 | 2.25 / 1.5 | 800 / 700 | — | — | [verified] |

**Reading the table.** Across all of these the *standard headline* tier — the tier that carries sentence-length heads on a reading column — sits at **1.9–2.0× body (31–34 px on a 16–17 px body)**, with line-heights of 1.1–1.25 and weights ranging from 400 (Tufte, Material) through 500 (Guardian default) to 700 (GOV.UK, Tailwind). The next tier up (36–50 px, 2.25–2.9×) is reserved for short display heads or immersive features. The old CiC hook (32–48 px) spanned both tiers; the current one (22–28 px, 1.3–1.65×) is below both.

The Guardian case deserves one more sentence because it is the exact shape of CiC's problem: a serif headline of 15–25 words, medium weight, on a ~38 rem reading column, immediately followed by a standfirst and then 17 px body. It runs three or four lines on desktop and five or six on a phone, and the Guardian has shipped it that way to tens of millions of readers a day since the 2018 redesign whose stated goals were "reduce headline size" and "legibility across all weights" [indexed: D&AD; Dezeen].

---

## 5. Numeric guidance that applies to a multi-line, sentence-length statement

### 5.1 Size

- Butterick (*Practical Typography*, "Headings"): "there is no typographic universe in which you need to double the point size to achieve emphasis"; increase "just a little… it'll be less than you think"; emphasise with space above and below. [indexed] — This is the strongest argument *against* going back to 48 px. Note that Butterick is writing about headings inside a document, where a body paragraph follows on the same page; the CiC hook is the only text on its screen, which is why the newspaper 2.0× tier, not Butterick's 1.1×, is the right comparison. Even so, his ceiling — do not double — lands at 34 px on a 17 px body, which is precisely the Guardian value.
- WCAG's "large text" threshold is 18 pt = **24 px** (or 14 pt bold = 18.67 px) [indexed: W3C Understanding 1.4.3]. A hero statement whose *minimum* is 24 px is unambiguously "large text" on every device; the current 22 px minimum is not.
- Butterick's body range is 15–25 px; 17 px CiC body is mid-range, so ratios above transfer directly. [indexed]

### 5.2 Line-height for a heading that wraps to 3–6 lines

- The general rule: unitless line-height must *fall* as size rises — 1.6 body → 1.3–1.4 at large sizes (Hovhannisyan, "Don't use a fixed line height"); headings 1.1–1.25 (Pimp my Type; Studio Tonic); "headings and other elements no longer than a line or two: 1–1.35" (USWDS); ≥24 px headings 1.25 (University of Michigan design system); the 2013 Smashing survey found an average of 1.2 for primary headings. [all indexed]
- The multi-line exception, stated explicitly: "if you've got a headline that wraps to two or three lines, bump it up slightly to 1.2 or 1.3" (madegooddesigns); "always look at your headings with line breaks in between" (Pimp my Type). [indexed]
- Real systems whose headline tiers are *designed to wrap*: Material 3 at 1.25–1.33 with weight 400; GOV.UK 24/30 = 1.25; Guardian's Interview format loosens its headline from 1.15 to ≈1.24 on tablet. [verified for GOV.UK and Guardian; indexed for Material]
- Josh Comeau's technique `line-height: calc(1em + 0.5rem)` yields a ratio that tightens automatically as the font grows — 1.33 at 24 px, 1.24 at 34 px — which is exactly the multi-line behaviour above. [indexed: CSS-Tricks notes on his reset]
- Bringhurst, as summarised by several secondary sources: heading leading 1.1–1.3, tighter than body; more leading for sans and for small x-heights. [indexed; not verified against the book]

The current 1.4 is above every heading figure here and inside the *paragraph* band (Tailwind lead 1.45–1.6; gwern abstract 1.5). It is a second, quieter reason the line reads as a paragraph.

### 5.3 Weight

- Guardian default headline weight is 500 ("medium"); 300 for Comment/Obituary, 700 for Feature/Review/Interview. [verified]
- Material headlines are 400 across the board; Tufte's are 400. [indexed; verified]
- Poynter: decks should be *lighter* than the head. [indexed] — By the same logic, a head with nothing above it should not be the lightest thing on the page.
- Butterick: bold is easier to read than italic for headings, but "non-bold headings work too." [indexed]
- Robin Rendle (CSS-Tricks): experienced typographers build hierarchy with weight before size. [indexed] — A single step 400 → 500 buys hierarchy without a single extra pixel of height.

### 5.4 Measure

- Body measure: 45–90 characters (Butterick); 45–75 (Bringhurst, via secondary sources); Craig Mod's 12–15 words per line for reading text. [indexed]
- Large type wants a *narrower* character count — 30–40 characters is repeatedly cited for headings [indexed: loremforge; numberanalytics] — because each line is taller and the return sweep is longer.
- At 34 px in a 38 rem (608 px) column Alegreya gives roughly 40–45 characters per line, i.e. the heading band; the Guardian column is ~620 px. Keeping `--measure` is correct. [inference + verified column widths]

### 5.5 Centred or left-aligned

- Butterick ("Centered text"): "overused… the typographic equivalent of vanilla ice cream"; acceptable for "short phrases or titles"; "whole text blocks should not be centered." [indexed]
- Pimp my Type ("Avoid centered text"): "when text is longer than two or three lines, it is always recommended to ignore center alignment." Prototypr: "only use centered text for short, 1-to-3 line elements (like a Hero Headline or a Quote)." [indexed]
- Nielsen's F-pattern work, as summarised by Brickfield (2026) and others: keep headers flush left; "when you centre a heading but left-align the text below, you force readers to reset their reading pattern." An adjacent accessibility summary limits centred blocks to 1–2 lines. [indexed; the nngroup.com pages themselves could not be fetched]
- Rafal Tomal: a centred headline over left-aligned body looks slightly off-centre; if you must, make the headline area wider than the body column. [indexed]
- Counter-evidence for centring: gwern centres its title *and* its abstract; 37signals liked centred headlines "from classical typography and antique book layouts"; Tufte and the Guardian left-align everything. [verified: gwern; indexed: SvN]

The evidence draws a fairly clear line at about four lines: centred is fine up to three or four, and costs something beyond that. With the recommended sizes the hook is ~4 lines centred on desktop (defensible, and it matches the centred arriving-mark above it) and 5–6 lines on a phone (past the line). See §7.

---

## 6. What to ignore, and why

The bulk of "hero section" advice returned by search — learnui.design, thrivethemes, uxmovement, spell.sh, landingrabbit, marketermilk and similar — assumes the SaaS template: a 6–10-word headline at 48–72 px (one guide: `clamp(48px, 8vw, 96px)`), a 12–20-word subline at 18–20 px, and a button. Several say outright: "avoid using paragraph body text and regular weight fonts for your hero." None of it applies here, for the reason Mark stated: the sentence *is* the statement, and there is no shorter line above it to take the display size. Splitting it into a short head plus a deck would satisfy those guides and betray the copy decision. The same goes for Poynter's 36/18/14 multi-deck ladder — it is the right convention for the *story* `h2` and its intro, not for the hook. Those sources were read and set aside on purpose.

---

## 7. Recommendation

### 7.1 The treatment

Replace `index.html` line 94 with:

```css
.hero h1{
  font-size:clamp(1.5rem, 1.1rem + 1.75vw, 2.125rem); /* 24px → 34px; hits 34 at ~940px */
  font-weight:500;                                     /* Alegreya Medium is already loaded */
  line-height:calc(1em + .5rem);                       /* ≈1.33 at 24px, ≈1.24 at 34px */
  max-width:var(--measure);                            /* keep 38rem */
  margin:0 auto 1rem;
  /* text-wrap:balance is inherited from the base h1 rule — keep it */
}
@media (max-width:640px){
  .hero h1{ text-align:left; text-wrap:pretty; }       /* 5–6 lines on a phone: past the centring line */
}
```

And step the section head beneath it down one notch so the ladder reads **34 → 28 → 17** (Guardian: 34 → 20–24 → 17; BBC: 32 → 28 → 16; Material: 32 → 28 → 16):

```css
.story h2, .who h2{ font-size:clamp(1.5rem, 1.2rem + 1.1vw, 1.75rem); } /* 24px → 28px */
```

If Mark would rather not touch the `h2`s, the alternative is to take the hook one step higher instead — `clamp(1.5rem, 1.05rem + 2vw, 2.25rem)` (24 → 36 px), which keeps a visible step over a 32 px `h2`. I prefer the first option: 34 px is the value with the most direct real-site precedent, and the `h2` at 32 px was itself sized against the old 48 px hook.

Expected rendering, from the line-count model [inference — confirm with screenshots]: 4 lines at 1280 px, 4–5 lines at 768 px, 5–6 lines at 390 px, 6 lines at 360 px. Compared with today: one more line on desktop, the same on phones. Compared with the old 48 px: two to three fewer lines.

### 7.2 Why each value, tied to the evidence

| Property | Old | Current | Proposed | Reasoning |
|---|---|---|---|---|
| Max size | 48 px (2.8×) | 28 px (1.65×) | **34 px (2.0×)** | The standard newspaper headline tier for sentence-length heads on a reading column: Guardian `headlineMedium34` [verified], BBC Trafalgar 32 [verified], NYT 31 [indexed], Material Headline Large 32 [indexed]. Butterick's "don't double" ceiling on a 17 px body is 34 px [indexed]. Puts the `h1` back above the `h2`. |
| Min size | 32 px | 22 px | **24 px (1.4×)** | WCAG "large text" threshold [indexed]; Guardian immersive standfirst top (24) and headline sizes 24/28 [verified]; Material Headline Small 24 [indexed]; GOV.UK scale-36 mobile is 27 [verified], so 24 is conservative. Holds phones to ≈5–6 lines. |
| Fluid form | bare `vw` preferred value | bare `vw` | `rem + vw` | A `rem` term keeps the size responding to browser zoom and user font settings; bare `vw` does not (Smashing "Modern fluid typography"; LogRocket) [indexed]. Rem share ≥ 50 % of the value at the top of the range. (The existing `.story h2` rule has the same bare-`vw` weakness; the `h2` snippet above fixes it in passing.) |
| Weight | 500 | 400 | **500** | Guardian default headline weight [verified]; the site's own `h1–h4` base; Poynter's principle that the head is never lighter than its deck [indexed]; Rendle: hierarchy by weight before size [indexed]. Not 700 — Tufte, Material and the Guardian all carry serious headlines below bold, and Alegreya 700 would fight the story's quiet register. |
| Line-height | 1.15 | 1.4 | **≈1.24–1.33** (`calc(1em + .5rem)`) | The multi-line heading band: "bump to 1.2–1.3 when it wraps to 2–3 lines" [indexed]; Material 1.25–1.33 and GOV.UK 24/30 for tiers designed to wrap [indexed; verified]; Comeau's calc gives exactly that curve [indexed]. 1.4 is paragraph leading (Tailwind lead 1.45–1.6) and was reading as such. |
| Measure | none (60 rem hero) | 38 rem | **38 rem** | ≈ Guardian's 620 px column [verified]; 40–45 characters per line at 34 px, the heading band [inference]. |
| Alignment | centred | centred | **centred ≥ 641 px; left on phones** | Centring is defensible to 3–4 lines (Butterick; Pimp my Type; Prototypr) and matches the centred arriving-mark; at 5–6 lines on a phone it is past every threshold cited, and Nielsen's flush-left guidance applies [indexed]. `text-wrap: pretty` on the phone avoids a one-word last line once balance's line cap is exceeded. |

### 7.3 What to check in a browser before shipping

1. Screenshot at 360, 390, 768 and 1280 px, light and dark. Count the lines; if desktop exceeds 4, drop the max to 2rem (32 px) rather than widening the measure.
2. Confirm the hook now visibly leads "The Story We Are In" at every width (it did not before).
3. On the phone, judge the centred mark over the left-aligned sentence. If it looks disjointed, the two honest options are to left-align `.mark-line` as well, or to keep the sentence centred and accept 5–6 centred lines for a statement read once. Do not fix it by shrinking the type again.
4. Look at Alegreya 500 at 34 px specifically for the italic-leaning "y" and "g" — the face's medium is slightly darker than its regular but still open; if it reads heavy, 400 at 36 px is the fallback, not 400 at 28.
5. Zoom to 200 % and confirm the sentence still scales (the `rem` term).

---

## 8. Sources

**Fetched and read directly (GitHub-hosted)**
- Guardian `dotcom-rendering` — `Standfirst.tsx`, `ArticleHeadline.tsx`: https://github.com/guardian/dotcom-rendering
- Guardian Source presets — `libs/@guardian/source/src/foundations/__generated__/typography.ts`: https://github.com/guardian/csnx
- Guardian Source RFC #631 (headline API, 28/34/42 px): https://github.com/guardian/source/discussions/631
- Guardian `guss-typography` `_typography.config.scss`: https://github.com/guardian/guss-typography
- BBC GEL `gel-typography/lib/_settings.scss`: https://github.com/bbc/gel-typography
- GOV.UK Frontend `_typography-responsive.scss`: https://github.com/alphagov/govuk-frontend
- Tufte CSS `tufte.css` and demo page: https://github.com/edwardtufte/tufte-css
- gwern.net `css/initial.css`: https://github.com/gwern/gwern.net
- Tailwind typography plugin `src/styles.js`: https://github.com/tailwindlabs/tailwindcss-typography
- Utopia core README (defaults 320→1240, 18→20, 1.2→1.25): https://github.com/trys/utopia-core
- CiC repo: `cic-website/index.html`, `cic-website/assets/style.css`, `Ministry/Technology/CiC_FrontEnd_Decision_Log.md`

**Indexed page text (could not be fetched)**
- Butterick, *Practical Typography* — Headings; Centered text; Point size; Body text: https://practicaltypography.com/headings.html · https://practicaltypography.com/centered-text.html · https://practicaltypography.com/point-size.html
- Poynter, "Hierarchy Within Headlines: Layers of Storytelling" (2002): https://www.poynter.org/reporting-editing/2002/hierarchy-within-headlines-layers-of-storytelling/
- Andy Clarke, "Art Direction for the Web: Designing standfirst paragraphs": https://stuffandnonsense.co.uk/blog/art-direction-for-the-web-designing-standfirst-paragraphs/
- Piccalilli, "Some simple ways to make content look good": https://piccalil.li/blog/some-simple-ways-to-make-content-look-good/
- Carmen Ansio, "Editorial Typography in CSS": https://www.carmenansio.com/articles/editorial-typography-css/
- GOV.UK Design System, Paragraphs (lead paragraph 24 px): https://design-system.service.gov.uk/styles/paragraphs
- Material 3 typography: https://m3.material.io/styles/typography/applying-type (plus Egor Tarasov's cheat-sheet)
- FT Origami `o-typography` README: https://www.npmjs.com/package/@financial-times/o-typography
- Fonts In Use, "The New York Times article redesign (May 2013)": https://fontsinuse.com/uses/3907/the-new-york-times-article-redesign-may-2013
- D&AD / Dezeen on the 2018 Guardian redesign: https://www.dandad.org/work/d-ad-awards-archive/the-guardian-headline-and-titlepiece-fonts · https://www.dezeen.com/2018/01/15/guardian-newspaper-unveils-new-compact-format-redesign-font-logo/
- Pimp my Type, "Avoid centered text": https://pimpmytype.com/avoid-centered-text/ · "The ideal line length & line height": https://pimpmytype.com/line-length-line-height/
- Prototypr, "Text Alignment Best Practises": https://blog.prototypr.io/text-alignment-best-practises-c4114daf1a9b
- Brickfield, "Why Centered Text Slows Reading" (summarising Nielsen's F-pattern): https://brickfield.ie/2026/01/26/why-centered-text-slows-reading/
- Rafal Tomal, "Center-aligned headline and left-aligned body text": https://rafaltomal.com/tips/center-headline-left-body/
- Aleksandr Hovhannisyan, "Don't Use a Fixed Line Height": https://www.aleksandrhovhannisyan.com/blog/dont-use-a-fixed-line-height/
- madegooddesigns, "Line Height & Letter Spacing" (multi-line heading exception): https://madegooddesigns.com/line-height-letter-spacing/
- USWDS Typography: https://designsystem.digital.gov/components/typography/ · University of Michigan Library design system: https://design-system.lib.umich.edu/visual-elements/typography
- Smashing, "Typographic Design Patterns and Current Practices (2013)": https://www.smashingmagazine.com/2013/05/typographic-design-patterns-practices-case-study-2013/ · "Modern Fluid Typography Using CSS Clamp": https://www.smashingmagazine.com/2022/01/modern-fluid-typography-css-clamp/
- CSS-Tricks, "Notes on Josh Comeau's Custom CSS Reset": https://css-tricks.com/notes-on-josh-comeaus-custom-css-reset/ · Robin Rendle, "Six tips for better web typography": https://css-tricks.com/six-tips-for-better-web-typography/
- W3C, Understanding SC 1.4.3 (large text = 18 pt / 14 pt bold): https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum
- Snow Fall: https://www.poynter.org/reporting-editing/2012/how-the-new-york-times-snow-fall-project-unifies-text-multimedia/ · https://source.opennews.org/articles/how-we-made-snow-fall/
- Firestorm: https://www.journalism.co.uk/news/how-the-guardian-built-multimedia-interactive-firestorm/s2/a553101/ · https://docubase.mit.edu/project/firestorm/
- Bear 71: https://sometimes.ca/Bear-71 · https://opendoclab.mit.edu/bear-71/ · https://bear71vr.nfb.ca/
- Anne Frank House: https://www.commarts.com/webpicks/anne-frank-house · https://www.annefrank.org/en/about-us/colophon/
- Emergence Magazine: https://fontsinuse.com/uses/28555/emergence-magazine-vol-1-2019 · https://www.webbyawards.com/crafted-with-code/emergence-magazine/
- Plough, "Retooling the Plough": https://www.plough.com/articles/retooling-the-plough
- Craig Mod, "A Simpler Page": https://craigmod.com/essays/a_simpler_page/ · "Hello, Again": https://craigmod.com/essays/hello_again/
- Aeon: https://fontsinuse.com/uses/3730/aeon-magazine
- Anthropic tokens (register only): https://designmd.cc/benchmarks/anthropic
- 37signals on centred headlines: https://signalvnoise.com/posts/2705-behind-the-scenes-37signalscom-redesign
- Generic SaaS-hero guidance, read and set aside: https://www.learnui.design/blog/mobile-desktop-website-font-size-guidelines.html · https://thrivethemes.com/hero-section-examples/ · https://uxmovement.com/content/the-optimal-design-for-a-landing-page-hero/
