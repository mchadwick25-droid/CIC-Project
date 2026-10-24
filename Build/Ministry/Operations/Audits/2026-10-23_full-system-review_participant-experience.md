# Full-system review, 2026-10-23: participant experience and accessibility

One of four parallel reviews Mark asked for on 2026-10-23. This one covers the lens of the person using the product. The other three lenses are engineering, safety and operations; scholarly rigor and content; and market and sale-readiness. They appear here only as one-line cross-lens notes.

## 1. Scope and method

**Commits reviewed.** `origin/main` e64646393 (merge of PR #1083) and `origin/live` 469d072cf (merge of PR #1081). Between them, five files differ under `cic-website/` and `cic-poc/frontend/`: `privacy.html`, `pilot.html`, `go-deeper-return.html`, `assets/go-deeper-config.js` (a comment only) and `data/corpus-coverage.json`. Every finding below holds on both branches unless it says otherwise.

**What I rendered.** I used headless Chromium (`/opt/pw-browsers/chromium`) through `playwright-core`, at three viewports: phone 390×844, iPad 820×1180 and desktop 1440×900. `cic-website/` was served locally with `python3 -m http.server`. The conversation app was built with `npm run build` and served with `vite preview`. A second build with `VITE_DEEPER_ENABLED=on` matches production, per `render.yaml:217`. All of this lived in the scratchpad; nothing in the repository changed.

The app talks to the engine through `/api`. I answered those calls with a mock inside the browser, so no model was called and no money was spent. The mock gave the real world list from `records/worlds/*.yaml`. The crisis text came verbatim from `engine/m4/crisis_resources.py`, and the limit lines came from `engine/deeper/ops/go-deeper.yaml`. The ordinary reply was placeholder text of my own, marked "MOCK REPLY".

**Pages, at all three widths:**
- `index.html`
- `traditions/alexandria-catechetical.html`
- `atlas-v3.html`
- `go-deeper.html` and `go-deeper-return.html`
- `privacy.html`
- `pilot.html` and `pilot-feedback.html`
- `table.html`, `about.html`, `support.html`, `story.html`, `whats-next.html`
- `tree/alexandria-catechetical.html`
- `talk.html` with the app inside its frame

**App states:**
- the app's own chooser screen
- a conversation with one reply
- a crisis (Track A) turn
- a 503 when a session starts
- a network failure
- a three-seat Table
- the low-token and out-of-tokens moments, with the token panel on

**Checks I ran:**
- axe-core 4.14.0, with the tags wcag2a, wcag2aa, wcag21a, wcag21aa, wcag22aa and best-practice.
- My own measures:
  - visible text below 14 px;
  - sideways page overflow;
  - targets under 24 px and under 44 px (inline links in sentences excluded);
  - landmarks, `h1` and live regions;
  - bytes transferred.
- A keyboard-only Tab walk on five pages, checking for a visible focus ring.
- Emulated reduced motion, at 320, 390 and 1280 px.
- Root font size at 200%, as a rough stand-in for text zoom.
- Readability by sample, with the repo's own scorer (`engine.m1.gates.fk_grade` and `fre_score`):
  - paragraph and list text inside `<main>` on 14 pages;
  - the 22 card texts;
  - the three crisis scripts;
  - the welcome and limit lines;
  - six app strings.
- Front-end tests: `npx vitest run` passed 326 of 326, and `npm run build` succeeded. `npm run lint` exits 2 because the folder has no ESLint config.

**Not checked, and why:**
- **Real devices.** No real iPhone, iPad or Android phone, and no Safari. I have only headless Chromium. Pilot item 3 ("Zoom did not work") is a Safari-on-device report I could not reproduce.
- **Real screen readers.** No VoiceOver, TalkBack or NVDA. axe and the DOM checks show semantics, not what a listener hears.
- **The browser's own text-size setting.** I approximated it with a 200% root font size.
- **Slow networks.** I measured bytes, not timed loads under throttling. Load times below are labelled as estimates.
- **The engine's own welcome turn.** It never appeared, because the mock did not return a door turn. Its text was read from `engine/m4/facilitator_turns.py:85-91`.
- **Any real conversation.** Ruled out by CLAUDE.md's metered-spend rule.
- **axe "needs review" contrast items.** These are text over images and gradients: 111 nodes on the landing page at phone width. I did not check them by hand. axe reported no contrast failures anywhere.

## 2. Done, with evidence

- **The landing page and chooser work by keyboard.**
  - A Tab walk at 1280×800 on `index.html` reaches, in order: skip link, header, search, the card's Talk and Table, the card itself, "Previous card", "Next card", era chips, "See all 11", "View as list" and "How this works".
  - Every stop shows a visible focus ring.
  - The tradition page and the buy page behave the same way.
  - Arrow buttons are 56 px and labelled (Decision-Log 2026-10-20, line 365).
  - Arrow keys, Page Up/Down, Home and End drive the page rail (Decision-Log, line 599).
- **Reduced motion works.**
  - With `prefers-reduced-motion: reduce`, the hand becomes the plain list (`chooser is-list`) and no animations run (`document.getAnimations()` shows 0 running).
  - The app honours the same setting (`app.css:201`, `:225`, `:1434`, `:2050`, `:2281`).
- **No page scrolls sideways** at 390, 820, 1440 or 320 px, across all 14 site pages. The one exception is the app's fallback chooser (§6, M3).
- **Most of the site passes axe cleanly.** Eight pages show 0 violations at all three widths: `go-deeper.html`, `go-deeper-return.html`, `privacy.html`, `pilot.html`, `pilot-feedback.html`, `table.html`, `support.html` and `whats-next.html`.
- **The card text floor was met where Mark asked.** He asked for the tagline and "Shaped by" lines on the card front, now 16 px at the largest card and never under 14 px (Decision-Log 2026-10-20, lines 324 and 500). The rendered tagline contrast is 14.2:1.
- **The crisis redirect is fixed text, appended by code** (`engine/m4/crisis_resources.py`).
  - It reads at FK 7.3 / reading ease 74 across the three scripts.
  - It opens by telling the person who is speaking: "this is the Facilitator speaking, not Theon".
  - It never makes the redirect depend on the person saying they are fine.
  - The colour is #A39B92 on #17130F, 6.74:1 by my own calculation.
- **Error messages are written for people.**
  - Example: "This conversation has slipped away from us — the server was restarted, and nothing you said caused it." (`lib/api.ts`)
  - They render in `role="alert"`. The waiting note ("Theon is considering") is `role="status"`. The transcript is `role="log"` (`TranscriptScroll.tsx:132`).
- **The plain-language pages hit the target.** Privacy scores FK 5.3 / reading ease 78. Pilot scores 3.5 / 85. The return page scores 2.4 / 91.
- **The pilot's top complaints were acted on.** Item 2 (waiting sign), item 3 (reading space), item 5 (page order), item 30 (intro 17 px, ribbon 16 px) and item 29 (simpler pages) are all closed in `Pilot_Feedback_Log.md`, lines 24–27, 89 and 119.

## 3. In process

- **Theme B ("answer briefly", an honest-limit line)** is decided but not built. Its wording and thresholds are still open (`Pilot_Feedback_Decisions.md`, lines 82–107). This is the pilot's "400 words where 4 suffice" (item 8).
- **The tree's "Add to the table" button** has its wording decided but is not built (Decision-Log, line 510).
- **Two differences from the list drawing Mark approved** are waiting for his ruling: compact rows, and a way back to cards on a phone (Decision-Log, line 508).
- **The site-wide header sweep** is not done. About 300 pages still use a fixed `1000px` breakpoint, and header buttons on other pages are 38–40 px tall (Decision-Log, lines 338–354; handoff `2026-10-20_conversation-chooser-step4-and-rulings.md`, lines 11–18).
- **Recorded stories still say "world".** By Mark's ruling they wait for a rewrite and re-recording (Decision-Log, 2026-10-20, "The stories keep 'world'"). The 76 "this world" uses on the eleven tradition pages sit in that recorded text. This is not a defect.
- **The Table's Facilitator texts are marked DRAFT, not yet approved,** in the engine (`engine/m4/facilitator_turns.py:240-251` comment). They are what a Table participant reads today.
- **The chooser's own `README.md:5`** still says "Nothing built", and `Build-Plan.md:56` still describes the hand of five with Shuffle. Both are stale.

## 4. Still needed for the full system to be live

1. **One real-device pass** on iPhone Safari, iPad Safari and an Android phone, with VoiceOver turned on for part of it. These checks are listed in `Build-Plan.md:79-85` and are still unmet; every handoff since 2026-10-20 records them as "not checked".
2. **Production privacy text must match what production sells** (R1 below).
3. **Accessible structure in the conversation app:** a main landmark, a heading, a label on the message box, and focus kept in the message box (R3).
4. **A clearer crisis moment on screen** (R2), without changing the approved words.
5. **Token amounts translated into questions** a person can picture, on the buy page and in the panel (R6).
6. **The 14 px floor applied beyond the two card lines** (R7).
7. **A decision on whether any law or platform rule needs an AI notice inside the conversation.** This is open and marked "Not checked" in `Pilot_Feedback_Decisions.md`, lines 269 and 287.

## 5. Quality: strengths with examples

- **The chooser is distinctive and clear.** The desktop hand of collector's cards reads at a glance. Each card names the person, the place and the dates, and gives a two-sentence tagline that keeps the tradition's own flavour. For example: "Mar Yausep is a representative voice for the Christian tradition of Edessa and Nisibis (200–410 CE). Doctrine was sung in hymns."
- **Mark's own no-mouse use is designed in, not added later.** The page rail, the list view, the 56 px arrows and the keyboard flip all come from his words (Decision-Log, lines 583–605).
- **The Facilitator and the Representative are kept apart in the participant's eyes.** The crisis script names who is speaking. The Representative stays silent on that turn. The Facilitator's welcome is two short sentences (FK 4.5).
- **Errors never blame the participant** ("nothing you said caused it"), and the feedback forms carry a real-help line: "No one reads them live. If you need help now…" (`components/feedbackText.ts:3`).
- **The test suite carries real accessibility checks:** 326 front-end tests, including focus return on menus, Escape on dialogs, and resending after a dropped stream.

## 6. Risks, ranked by consequence

### Blocking

**R1. The live privacy page says no payment is taken, while the live buy page takes payment.**
- **Evidence.**
  - `git show origin/live:cic-website/privacy.html` says: "During the pilot, Go Deeper sells nothing. We do not take your name, your email or any payment."
  - `origin/live:cic-website/go-deeper.html:154-159` carries three live Stripe Payment Links. The "Choose" buttons render with prices: $7.00 for 1,100 tokens, $15.00 for 2,750.
  - `origin/live:cic-website/assets/go-deeper-config.js` has `enabled: true`.
  - `main` already carries the corrected paragraph ("You can buy more tokens… Stripe asks for your name, email and card").
  - `Pilot_Feedback_Decisions.md:387` records this conflict as put to Mark and unanswered at the time.
- **Failure scenario.** A pilot participant on a phone buys the $7 pack and gives Stripe a name, an email and a card. Later they read the privacy page, which says none of that is taken. The project's first paying user meets a false statement about their own data.
- **Smallest fix.** Promote `main`'s privacy text through `CiC_Promotion_Runbook.md` (Mark's call). Until then, the buy buttons could be switched off on `live`.

### High

**R2. On screen, the crisis turn looks like every other Facilitator turn, and on a phone its first line is scrolled out of view.**
- **Evidence.**
  - The turn uses `.turn--facilitator` (`app.css:437-440`): grey italic serif, no box, no heading, no `role="alert"`. It is the same style as the welcome and the limit line.
  - At 390×844, after the turn arrives, the transcript is pinned to its end. The opening sentence ("this is the Facilitator speaking, not Theon. What you just told me matters…") sits under the floating portrait card. What is visible starts mid-paragraph.
  - Focus stays on the page body.
  - The text names no organization, number or link. This follows decision CO-022, Option A (`crisis_resources.py` docstring).
- **Failure scenario.** A distressed person on a phone sends one message. They see a block of grey italic text that looks like the narration around it. The line saying the Facilitator stepped in is off-screen above. "A crisis line" points to nothing they can tap.
- **Smallest fix, without changing the approved words.**
  - Give `kind: 'safety'` turns their own treatment: upright text, a bordered panel and a visible "From the Facilitator" label.
  - Scroll the start of the turn into view, not the end.
  - Announce it with `role="alert"`, or move focus to it.
  - Whether a neutral way to find local help may be added is a governance question for Mark (Q2).

**R3. The conversation app has almost no accessible structure, and keyboard focus is lost after every message.**
- **Evidence.**
  - axe on the conversation, Table and crisis states reports `landmark-one-main`, `page-has-heading-one` and `region` at all three widths. There is no `<main>` and no heading on the conversation or Table screens.
  - The message `<textarea>` has no label and no `aria-label`, only a placeholder ("Ask Theon…") that disappears as soon as the person types (`ChatInput.tsx:82-92`).
  - In a scripted run at 1280×800: on load, focus sits on the page body. After Enter sends a message, focus falls back to the body, because the textarea is disabled while sending. It falls back again when the limit is reached. Tab from the body goes "More", then the transcript, then the message box: three presses after every message.
- **Failure scenario.** Mark, on his laptop without a mouse, sends a question. To ask a follow-up he has to Tab three times, every time. A VoiceOver user hears "edit text" with no name once they start typing, and has no heading to jump to.
- **Smallest fix.**
  - Add `aria-label` to the textarea (for example "Your question for Theon").
  - Keep the textarea enabled with `aria-disabled` while sending, or refocus it when the reply lands.
  - Wrap the screen in `<main>` with a visually hidden `<h1>` ("Conversation with Theon").

**R4. Nothing has been tried on a real phone, a real tablet or with a real screen reader.**
- **Evidence.**
  - `Build-Plan.md:79-85` (VoiceOver on iPhone, keyboard pass, Mark's device preview) is unmet.
  - The Decision-Log records "Not checked: real iPad or iPhone Safari, a screen reader" at lines 512, 526, 589, 605, 615 and 625.
  - `Pilot_Feedback_Log.md` item 1 is fixed but not confirmed on an iPad.
- **Failure scenario.** The pilot's own first tester reported "Zoom did not work" and a screen that did not fit. Both are Safari-on-device problems that headless Chromium cannot see. The next tester may hit them too.
- **Smallest fix.** One 30-minute session on Mark's iPad and a phone, using a short script (choose, talk, hit the limit, buy, come back), plus five minutes with VoiceOver on.

**R5. The landing page is heavy for a phone.**
- **Evidence.**
  - At 390 px, `index.html` transferred 5,919 KB in my run.
  - 3,319 KB of that is `data/world-census.json`. That is 1,010 KB even gzipped, and `chooser.js:528` waits for it before any card renders.
  - Each portrait is a 390–890 KB PNG (`assets/portraits/*.png`). Yet 3 KB webp thumbnails already exist in `assets/portraits/thumb/`.
  - `table.html` is 4,946 KB, and `atlas-v3.html` is 3,783 KB of HTML (1.2 MB gzipped).
  - My local server does not compress, so real transfer of the JSON is nearer 1 MB.
- **Failure scenario.** Estimate, not measured: on a slow mobile link of about 1.6 Mbit/s, the gzipped census alone takes about 5 seconds. The four portraits in view add about 11 seconds. A first-time visitor on a phone sees an empty space where the cards should be.
- **Smallest fix.** Give the chooser its own small file with only the eleven built traditions, loading the full census later for search. Serve card-sized webp or AVIF portraits.

### Medium

**R6. The limit and buying moments speak in tokens, not in questions.**
- **Evidence.**
  - The panel says "550 free tokens every 30 days: 50 to launch a new conversation, 20 to 25 for each question" (`deeperCopy.ts:4`). The ribbon then says only "25 tokens left".
  - The buy page offers "$7.00 — More conversations: 1,100 tokens". `main` removed the earlier "about ten conversations" (diff of `pilot.html`).
  - At 390×844, when the limit is reached, the panel covers the message box and half of the limit note. The two actions ("Get more conversations", "I have a code") are small underlined links. "Get more conversations" appears three times on one screen.
- **Failure scenario.** A non-native English reader sees "25 tokens left" and cannot tell whether that is one more question or none. At checkout they cannot tell what $7 buys.
- **Smallest fix.** Show "about N questions left" beside the token count, and "about N questions" on each pack. Make the two actions full buttons. Move focus to the panel heading when the limit opens it.

**R7. Much participant text sits under the 14 px floor.**
- **Evidence (rendered sizes).**
  - The site's top navigation ("Church Family Tree", "Conversation with One", "Build a Table") is 13.6 px on every page (`style.css`, `0.85rem`).
  - On a phone, the card band and dates are 11.8–13 px, and the Talk/Table labels are 12–13 px.
  - "Synthesized voice — not a recording." is 12.5 px.
  - In the app:
    - the speaker labels ("You", "Theon · Alexandrian Christianity") are 11.5 px;
    - the AI line is 13 px;
    - the portrait card's era band is 6.5 px;
    - the fallback chooser runs from 10.9 to 12.8 px;
    - the limit note is 0.85 rem.
  - In `app.css`, 55 of 93 `font-size` rules (rem or px) are under 0.875 rem / 14 px, by my count.
  - Pilot items 3 and 30 were both about small text.
- **Failure scenario.** An older participant on an iPad reads the speaker label and the AI notice at 11–13 px and gives up on the labels.
- **Smallest fix.** Raise the shared `0.85rem` and smaller tokens to `0.875rem`, site-wide and in `app.css`. Purely decorative text (the 6.5 px band) can be hidden from view or enlarged.

**R8. When the engine fails, the participant drops into an older, different chooser that scrolls sideways.**
- **Evidence.**
  - With a 503 or a network failure at session start, the app shows its own Launch screen inside the `talk.html` frame. That screen has round portraits, "Begin the Interview", "Add to the Table" and "What this voice knows well".
  - The whole page scrolls sideways: `scrollTo(800,0)` works at 390 px, and the extra width measured 1,715–2,365 px.
  - It shows registry text such as "Egyptian and Palestinian desert monasticism - Nitria, Kellia, Scetis (Strand C, semi-anchoritic)…" (the `place` field).
- **Failure scenario.** The engine has a cold start. The person taps "Talk" on Chloe and gets a red error above a second, unfamiliar card row that slides sideways under their thumb.
- **Smallest fix.** When embedded, show the error with "Try again" and "Back to the cards", never Launch.

**R9. The landing page's feedback button has no name at phone and iPad width.**
- **Evidence.** axe flags `button-name` (critical) on `#feedback-toggle` at 390 and 820 px. At those widths the visible label is `<span class="fb-short" aria-hidden="true">Feedback</span>`, and the full label is hidden (`index.html:278`).
- **Failure scenario.** A VoiceOver user on an iPhone hears "button", with no name, at the top of the first page.
- **Smallest fix.** Remove `aria-hidden` from the short label, or add `aria-label="Tell us what you think"`.

**R10. Several participant pages read above the target.**
- **Evidence (scored with `engine.m1.gates`).**
  - `about.html` scores FK 10.2 / reading ease 46, with 24 of 29 passages under 60.
  - `whats-next.html` scores 11.8 / 43. It also carries build jargon: "Right now, every conversation runs on the plain, single-mode Representative — Representative Modes, including General, haven't shipped yet."
  - `support.html` scores 8.8 / 52.
  - Six of the eleven card fronts miss reading ease 60. The lowest is Albina's tagline, at 11.7 / 32.5. The long fixed opening "X is a representative voice for the Christian tradition of…" drives this.
  - Scoring short fragments such as headings and prices is noisy. The page figures are for whole bodies of text.
- **Failure scenario.** A non-native reader opens About to understand who is behind the site and meets "Formation Grows More Deeply Through Encounter".
- **Smallest fix.** Rewrite About, What's Next and Support to the target, and remove "Representative Modes" and similar internal names from What's Next.

**R11. The AI notice is far from the point of choosing.**
- **Evidence.**
  - The landing page's statement ("These are AI voices built only from the surviving writings of each tradition. They are not real people…") is the last element of `<main>` (`index.html:367`). That is below the cards, the giving section and the story; on a phone the list view puts it thousands of pixels down.
  - Inside the conversation, the only notice is "This is an AI-generated voice." at 13 px under the message box.
  - The Facilitator's welcome does not mention AI (`facilitator_turns.py:85-91`).
  - Mark chose this on purpose (change order 1, `Pilot_Feedback_Decisions.md:269`). The pilot's only tester said they "Love the disclaimer before conversation" (item 10).
- **Failure scenario.** A first-time visitor on a phone taps "Talk" on the first card and never scrolls to the statement. The 13 px line is the only notice they meet.
- **Smallest fix.** A decision, not a defect (Q3). If wanted: one short line under "Free to start. Add more any time.", such as "The voices are AI, built from each tradition's writings."

### Low

- **R12. "World" still shows in the app's own strings.**
  - "Meet another world" (`Conversation.tsx:183`), "Return to the worlds" (`TableRoom.tsx:229`) and "gives back more than one world at a time" (`Launch.tsx:108`).
  - The same action reads "Meet another tradition" on the line above (`:179`).
  - Raw strings can leak: "No active session" and "No table convened" (`useConversation.ts:135`, `useTable.ts:181`).
  - Two error strings use a hyphen where the rest use an em dash.
- **R13. The narration "Play" buttons' visible text is not part of their accessible name.** axe flags `label-content-name-mismatch` on 27 nodes across `index.html`, `about.html`, `story.html` and the tradition page: the `aria-label` is "Play narration". Voice-control users who say the visible word miss.
- **R14. Smaller structure issues.** A heading-level skip (`h4` with no `h3`) on the tradition page's story entries. `tree/*.html` pages have no `main` landmark. The page rail sits outside landmarks.
- **R15. Inside `talk.html` on a phone, two header bars stack.** Together they take about 150 px. The site's strip cuts "Build a Table" at the right edge.
- **R16. The atlas is hard to use on a phone.** The map's labels are 11 px. The intro says "Click any name… hover a name for a glimpse", which is mouse wording, on touch screens. The page is 3.8 MB.
- **R17. The monthly-bound line is hard to parse.** "Messages here that get no reply from a Representative have reached the limit for this month" (`facilitator_turns.py:231`) is hard for a non-native reader, though it scores 7.5 / 62.

## 7. Best parts

1. The card chooser: beautiful, keyboard-complete, motion-safe, and shaped line by line by Mark's own words.
2. A crisis protocol a participant can trust. The text is fixed, appended by code, plainly written, and clear about who is speaking.
3. Error and waiting messages that are kind and human, and announced to screen readers.
4. Plain-language privacy, pilot and buying pages, at grade 2–5 with reading ease 78–91.
5. A design record that ties each choice to Mark's words, and a pilot log that tracks every comment to a status.

## 8. Gaps

1. No real-device or screen-reader test of anything.
2. The conversation app's accessible structure: no landmarks, no heading, an unlabelled message box, and focus lost after each send.
3. The crisis moment's on-screen treatment.
4. The live privacy page versus live payments.
5. Tokens never translated into questions.
6. The landing page's weight on mobile.
7. The 14 px floor applied to two lines rather than to the whole interface.

## 9. Cross-lens notes

- **Engineering.**
  - `npm run lint` cannot run (no ESLint config in `cic-poc/frontend/`).
  - `README.md` says `engine/deeper/` is "switched off", but `render.yaml:209-218` sets `CIC_DEEPER_ENABLED=1` and `VITE_DEEPER_ENABLED=on`.
  - `engine/m4/crisis_resources.py` and `cic-poc/frontend/src/app.css` carry long design commentary inside live files, which CLAUDE.md's live-surface rule forbids.
- **Safety.** `engine/deeper/ops/go-deeper.yaml` still has a `daily_ceiling` note ("It works again tomorrow"), while `Pilot_Feedback_Decisions.md:305-317` records no daily reset. Is that note still reachable? The Table's Facilitator texts are marked DRAFT (`facilitator_turns.py`), and the welcome-turn change was not reviewed against Governance V3.6 (Decision-Log, line 396).
- **Scholarly.**
  - The landing page claims the voices are "built only from the surviving writings of each tradition".
  - The engine's "are you an AI?" answer says "each claim in it is checked to make sure its words come from the record it names".
  - Both claims need checking against what the engine does.
  - Gaul's tagline claim-check finding is still open by Mark's ruling (Decision-Log, line 111).
- **Market.** The giving section ("Give once / Give monthly") sits above the AI statement on the landing page. A due-diligence reader will notice that the first paid flow has never been tried on a real device.

## 10. Five questions for Mark

1. **Production privacy versus payments (R1).** Promote `main`'s privacy text now, or switch the live buy buttons off until the next promotion?
2. **The crisis moment on screen (R2).** May the crisis turn get its own visual treatment (upright text, a bordered panel, "From the Facilitator") and be scrolled to its start? And, as a governance question, may it link to a neutral "find help where you are" page, or does CO-022 Option A rule out any link?
3. **The AI notice (R11).** Keep it at the bottom of the landing page and in the 13 px line, as you ruled, or add one short line near "Free to start"? Should someone check whether any law or platform rule needs a notice inside the conversation?
4. **Tokens in plain words (R6).** May the panel and the buy page say "about N questions" beside the tokens? If so, what number should one question count as: 20, 25, or an average?
5. **A device session (R4).** Can you give 30 minutes on your iPad and a phone, with VoiceOver on for part of it, using a short script I write? It would close the largest untested gap before more pilot users arrive.
