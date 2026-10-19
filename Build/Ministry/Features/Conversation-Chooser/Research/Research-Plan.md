# Research plan — the conversation chooser — 2026-10-19

Deliverable 1 of 4. Shown to Mark as a private page (`https://claude.ai/artifact/HzrgjJunooHwsMXaqWwVX2`) and accepted. Questions were written before any system was opened.

## 1. The idea under test, as six claims

1. **The wheel.** A hand of world cards that rolls like a wheel is a better chooser for eleven worlds than a grid or a list.
2. **The card front.** A picture and the one-sentence intro are enough to choose from. A flip gives the next level of detail.
3. **Two actions.** One card can offer both "interview this Representative" and "add to a table" without confusing the visitor.
4. **Raise to build a table.** Raising two or three cards, then going straight to the table, is clearer than today's table builder.
5. **Era colour.** Colour by era helps the visitor choose.
6. **The fallback.** The wheel can work for keyboard, screen readers, reduced motion and phones, or a plain fallback can stand in without loss.

## 2. The questions

1. What does Google Arts and Culture's "Who's your favorite?" hand do on desktop, on a phone, from the keyboard and with reduced motion on? What sits on each card, what happens on click, and does the pattern appear elsewhere on the site?
2. Which live products choose from a rotating or fanned hand of cards? Which tried it and removed it, and why? What do usability studies say about reading angled or moving cards, reaching the tenth item, and motion sickness?
3. Do visitors find a flip? What happens on touch, where there is no hover? Can a screen reader reach the back? What should the second level hold, and how much text fits at the B2 reading level?
4. How do choosers give a card one main action and one quieter action without the "two competing links" problem that brief 05 found on today's chair cards?
5. How do products gather a small set before one "go" action, and keep the chosen state visible? Does a raised card read as "chosen"?
6. Eleven worlds sit in three eras, and the census gives eras I and VII the same ground tone. Does colour help at this scale, and is it safe for colour-blind readers? What else must carry the era besides colour?
7. What do the standards require (WCAG 2.2 reflow, dragging, motion, use of colour; the ARIA carousel pattern)? Which pattern degrades cleanly to a list on a 320 to 400 px phone, with the keyboard, with a screen reader and with reduced motion?
8. Does a wheel of all eleven fit Theme D's clean page and "a rotating few, not everything on the first page"? Where does the disclosure and safety step sit if choosing moves to the landing page? Does the card text keep the honest-limit lines?

## 3. Criteria for choosing systems

- C1. A chooser, not a gallery: picking an item leads to an action.
- C2. Same scale: five to twenty items, each with a picture and a name.
- C3. Serious content, or a game where the hand is native.
- C4. Live now, or a documented case of the pattern being dropped.
- C5. Checkable: the surface can be opened and recorded, or the standard or study is published.
- C6. Coverage: at least two counter-examples, two phone-first choosers, one keyboard and screen-reader authority, one game.

## 4. The systems

| # | System | Why it is in | Criteria |
|---|---|---|---|
| 1 | Google Arts and Culture, home | Mark's model: the "Who's your favorite?" hand | C1 C2 C4 |
| 2 | BibleProject | Mark likes its simple selection | C1 C3 C4 |
| 3 | Apple TV and tvOS shelves | The chosen card rises; a formal focus model | C1 C2 C4 |
| 4 | Apple Cover Flow | The best-known wheel of cards, dropped everywhere | C2 C4 C6 |
| 5 | iOS picker wheel | Apple's rule for when a wheel is right | C1 C4 C6 |
| 6 | Material 3 carousel | Google's centred and hero carousels, with research | C1 C4 C6 |
| 7 | Spotify, choose artists | Collecting a small set before "go", phone-first | C1 C2 C4 C6 |
| 8 | Netflix, "Who's watching?" | Big picture, a name, one tap | C1 C2 C4 |
| 9 | Balatro, Slay the Spire, Hearthstone | Card hands that fan and raise | C2 C3 C6 |
| 10 | Duolingo course picker; Khan Academy courses | Learning products that chose lists | C1 C3 C6 |
| 11 | Rijksmuseum and Europeana collection pages | Museum choosers with reading on the card | C1 C3 C4 |
| 12 | WCAG 2.2 and the ARIA carousel pattern | The rules the fallback must meet | C5 C6 |
| 13 | Nielsen Norman Group and academic carousel studies | The evidence against carousels and flips | C5 C6 |
| 14 | CiC briefs 05 and 06 (September 2026) | Already on record; to be re-read, not assumed | C5 |

## 5. How systems were opened

The cloud session's network policy blocked most product sites. Mark chose to add the hosts to the environment's Allowed domains; the change had not reached the session when the grid was written. Three routes were defined and labelled in the grid: opened (rendered in the session's browser harness, or in a screenshot from Mark), partly opened (the published source text fetched and read in full), indexed only (web-search text about it).

Hosts that opened from the session on 2026-10-19: Wikipedia, Apple's developer documentation data endpoint, GitHub's API and raw files, Google Fonts, archive.org (rate-limited), the live CiC site, the Rijksmuseum. Blocked: Google Arts and Culture, BibleProject, Material, Nielsen Norman, W3C, MDN, Chrome developer pages, the Wayback Machine, Spotify, Netflix, Duolingo, Khan Academy, Europeana, the academic publishers.

## 6. What the chooser is today (read from the code)

- Landing page: eleven chairs under "Who would you like to talk with?", in three era blocks, each a sideways scroll strip of 296 px cards with snap points. Each card: 96 px portrait, name, role, tradition, dates, a seven-line brief, two links.
- Build a Table: a separate page with three seats on a ring; a side panel (bottom sheet on phones) lists the eleven; two or three seats, then "Launch the Table"; with none filled, a random three.
- Hand-off: both routes open the app in a frame via `talk.html?worlds=<ids>&mode=interview|table`. The app has its own fallback picker.
- Disclosure and safety: no separate consent screen; the disclosure is the Arrival block at the top of the room; crisis handling is server-side and untouched by a new chooser.
- Colour: two accent colours per world (site and app registry) that disagree for nine of eleven; era headings carry no colour; the world list exists in three copies.
- Second level: each world's JSON holds a tile brief, four to eight voices with hedge lines, a legacy, sources and documented stories. Enough for a card back, to be cut hard.
