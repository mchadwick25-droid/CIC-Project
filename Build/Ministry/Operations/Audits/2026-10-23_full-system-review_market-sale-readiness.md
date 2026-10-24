# Full-system review, 2026-10-23: market view and sale-readiness

One of four parallel, independent reviews that Mark asked for on 2026-10-23. This one reads the project the way a buyer's or a funder's due-diligence team would. Mark is not selling. The sale view is a lens, used to make the best parts and the gaps visible. The other three lenses (engineering, safety and operations; scholarly rigor and content; participant experience and accessibility) run in other threads.

Reviewer: Opus 5.5. Read-only on the product. No model calls outside this conversation, no live tests, no paid services. This is not legal advice. Where a legal question matters, the report names the question and says what the repo shows. A lawyer must answer it.

---

## 1. Scope and method

**Commits reviewed**
- `origin/main`: `e64646393` (merge of PR #1083)
- `origin/live`: `469d072cf`
- The clone is shallow. The earliest visible commit is 2026-10-07, with 633 commits visible. History checks (authors, secrets) cover only that window.

**What I read myself**
- `CLAUDE.md` and `README.md`.
- `cic-website/`: `index.html`, `go-deeper.html`, `privacy.html`, `support.html`, `about.html`.
- `records/worlds/*.yaml` (the `state:` fields) and `cic-website/data/world-census.json`.
- `Build/Ministry/Operations/Pilot-Feedback/Pilot_Feedback_Log.md` and `Pilot_Feedback_Decisions.md`.
- `Build/Ministry/Features/Go-Deeper/Decision-Log.md` (stored value, expiry, refunds, minors, choice 17).
- `render.yaml` on `live` and `main`.
- `Build/Ministry/Operations/Standing/CiC_Promotion_Runbook.md` (the Cloudflare section).
- `CiC_System_Hub_Decision_Log.md` (the entity-date entry, lines 428–440).
- `CiC_FrontEnd_Decision_Log.md` (the Stripe flag, lines 314–324).
- `cic/texts/README.md` and `cic/texts/REGISTRY.yaml` (counts).

**What I sent to subagents and then checked**
- Three subagents ran: product and economics, rights and vendors, and web comparables.
- I re-checked every claim that carries weight in this report at its source: file and line, or the web page itself.
- Where a subagent's claim did not hold, I corrected it here. One example: it said "most" corpus files were supplied by AI threads. The registry shows 75 files supplied by Mark and the rest by Claude research threads.

**Live checks**
- I fetched `https://churchinconversation.com/go-deeper` on 2026-10-23. It returned 200, carried three live `buy.stripe.com` links and the line "By paying you confirm you are 18 or over."
- `https://churchinconversation.com/terms.html` returned 404.

**What I could not check**
- The organisation and funding material. It is held privately outside the repo (README, 2026-10-07). That covers the signed IP assignment, the bylaws and whether the incorporation-date problem was fixed.
- The Stripe dashboard, the AWS invoice, the Render and Cloudflare accounts, and the domain registrar.
- Whether Stripe ever answered the stored-value question.
- The live usage log. I used only the figures transcribed from it in the Pilot Feedback Log.
- The terms of the Gemini image tool.
- Git history before 2026-10-07.

---

## 2. What the product is, in plain words

Church in Conversation is a website and web app. People talk, in text and in audio, with AI voices called Representatives. Each voice speaks for one historical Christian tradition, which the project calls a "world": for example Alexandria, the Desert Fathers, the Syriac church or the Cappadocians.

Each voice is built only from that tradition's own surviving writings. These are vendored, public-domain editions, and each quote is checked word for word against the source file. Claims carry a five-level confidence tag. A person can talk with one voice ("Conversation with One") or with several at once ("Build a Table"). A public map, the Church Family Tree, shows 296 traditions across 2,000 years.

The home page says plainly: "These are AI voices built only from the surviving writings of each tradition. They are not real people, and they do not speak for any church today." (`cic-website/index.html:367`)

**Who runs it.** Faithways Studio, Inc., a Colorado public benefit corporation. It is for-profit, not a nonprofit, and gifts are not tax-deductible (`cic-website/support.html`; `CiC_Full_UX_Feature_Checklist_2026-07-20.md:211`). The footer on some pages still says "A ministry in formation."

**How it earns.**
- Free: 550 tokens every 30 days.
- Token packs: $7 for 1,100 tokens, $15 for 2,750, $30 for 6,600, paid through Stripe Payment Links (`engine/deeper/ops/go-deeper.yaml`; `go-deeper.html`).
- Gifts: "Give once" and "Give monthly", to an "Accessibility Fund".

**Who it is for.** The repo shows curious adults and church people. The pilot audiences named are "general", "pastors" and "historians". Recent rulings also design for schools, homeschool families and youth groups (Go Deeper Decision-Log, 2026-10-22 entries).

---

## 3. Done, with evidence

| What | Evidence |
|---|---|
| 11 worlds live and admitted | `records/worlds/*.yaml`: 11 `state: admitted` (alx, cappadocian, desert, don, gallic, hal, ijc, pahc, rzg, syr, witt); census `Built & Live` = 11 |
| A 296-tradition map, public | `world-census.json`: 296 movements, each with a status (215 pre-survey candidates, 28 floor questions, and so on) |
| A source library with a recorded rights status on every file | `cic/texts/README.md`: 929 text rows. CI checks rights (`cic/engine/texts_registry.py`, `rights_clears()` accepts only "public domain" or "cc by"). 35 rows are CC BY-SA 4.0; the rest are public domain |
| Production engine on Render, deploying the protected `live` branch | `render.yaml` on `live`: `cic-engine`, plan `standard`, `app.churchinconversation.com` |
| Model spend through one channel | AWS Bedrock, Anthropic models; the direct Anthropic keys were disabled 2026-08-28 (`render.yaml` header) |
| Paid tokens switched on in production | `CIC_DEEPER_ENABLED: "1"` on `live`; three live Stripe links on the public site (fetched 2026-10-23) |
| A privacy page | `cic-website/privacy.html`: storage, 90-day deletion, 14-day backups, cookie, vendors named, deletion route |
| AI disclosure in the interface | `index.html:367`; in-room labels "This is an AI-generated voice." (`cic-poc/frontend/src/screens/Conversation.tsx:196`) |
| A crisis path owned by the Facilitator, with template-anchored resources added by code | CLAUDE.md Safety section. Tested by the safety lens, not by me |
| A first measured cost per round | Pilot_Feedback_Log.md, 2026-10-23: round 1 $0.0874 with checks; later rounds about $0.018–0.026; safety call $0.0024 (list price, last 30 days) |
| Runbooks | `Build/Ministry/Operations/Standing/`: promotion, incident and rollback, backup and restore, alerting, model spend, object storage, Go Deeper turn-on |
| CI with many gates and a 15-minute production watch | `.github/workflows/ci.yml` (census, paths, live commentary, world gates, library validators, engine and frontend tests, Docker build); `live-watch.yml` |
| A competitor scan already written | `Build/Ministry/Marketplace/CiC_Marketplace_Landscape_Scan_V0_1.md` and `..._Differentiation_and_Lessons_V0_1.md` (2026-07, V0.1) |

---

## 4. In process

- **Accounts.** Built through A4 but switched off. `CIC_ACCOUNTS_ENABLED` is not set in `render.yaml`, and no mail provider has been chosen (Go Deeper Decision-Log:743).
- **Worlds being built.** Two are in `state: building` (lpc, rcg). Six are candidates. The Library threads are vendoring sources for Eras III, VI, VII and VIII (Pilot_Feedback_Log.md:203).
- **Responses to pilot feedback.** Four themes have converged with Mark, but nothing is built yet: the landing page and its simplicity, answer length, and who a Representative stands for (Pilot_Feedback_Decisions.md). Mark has not yet approved the participant-experience design.
- **The cost report.** Live since PR 1055. Read once, on 72 messages. The AWS invoice has not been reconciled against it (`engine/m8/reconcile.py`).
- **Audio to Cloudflare R2.** Designed, not done. 644 MB of audio sits in `cic-website/audio`, and `wrangler.jsonc` has no R2 binding (`CiC_Audio_R2_Cutover_Runbook.md`, step 1 still Mark's).
- **Open conflict on the privacy first line.** The approved line says nothing is for sale, but the buy page sells (Pilot_Feedback_Decisions.md:388). Mark has not ruled.

---

## 5. Still needed for the full system to be live

"Live" here means open to the public, taking money, and defensible to a careful outsider.

1. A Terms of Use page. None exists.
2. Purchase terms shown at the point of sale: expiry, refunds and lost codes. The policy is drafted but "No page carries this yet" (Decision-Log:596).
3. Answers to the open legal and tax questions: stored value (Stripe), gift-card law and validity period, unclaimed property, sales tax, and minors (Decision-Log:39–40, 567, 602).
4. Clean organisation records: the signed IP assignment and the bylaws on a correct incorporation date (see 8.B2).
5. A production AWS identity in place of `cic-bedrock-dev` (`render.yaml:35–37`).
6. Accounts switched on, or a recorded change order allowing sales without them (see 8.B1).
7. A tested real purchase and refund. Mark chose to leave it untested: "i dont want to spend money" (Pilot_Feedback_Decisions.md:386).
8. External scholarly review. It has been moved to "Year 2 of a 5-year timeline" (`CiC_System_Hub_Decision_Log.md:5119`). The reviewer brief is a draft.
9. More than one tester's written evidence (see 8.H1).

---

## 6. Comparison with real alternatives

Every product below was checked on a page opened during this review. I re-opened the pages behind the starred (★) figures myself. Anything not opened is marked UNVERIFIED.

| Product | What it is | What it does better than CiC | What it does worse |
|---|---|---|---|
| **YouVersion** ★ | Bible app. More than 1 billion downloads. Has chosen not to launch a public AI chatbot. Its CEO says top models misquote Scripture "at least 15%" of the time, some up to 60% ([Christian Post, 2026-03-17](https://www.christianpost.com/news/ais-bible-misquotes-range-from-15-to-60-youversion-ceo.html)) | Reach and trust | No conversation at all. Its refusal is the strongest public case for CiC's word-for-word quote check |
| **Magisterium AI** (Longbeard) | Catholic AI that answers only from about 27,000 Church documents ([Northeastern CSSH](https://cssh.northeastern.edu/a-catholic-ai-app-promises-answers-for-the-faithful-can-it-succeed/)). Up to 100,000 monthly users claimed (via the Washington Post). magisterium.com returned HTTP 429: UNVERIFIED | Institutional credibility; a closed corpus like CiC's | Speaks for one church's teaching office. No historical voices, no confidence tags |
| **Bible Chat / CrossTalk** | AI that answers Bible questions ([crosstalk.ai](https://crosstalk.ai/)). The site claims more than 100,000 users. Appfigures estimates about $6.3M net revenue since 2023 ([Appfigures](https://appfigures.com/resources/insights/20250418/5-this-is-how-to-drive-demand-for-the-oldest-book-in-the-world)); the app named there is inferred to be the same: UNVERIFIED | Mobile habit, scale, App Store revenue | One neutral voice. No claim-level sources |
| **Text With Jesus** | Chat with Jesus, Mary, the Apostles and others; voice messages; freemium plus credit packs ([textwith.me](https://textwith.me/en/jesus/)) | A polished voice product. Credit packs are the nearest precedent for CiC's packs | Gives sacred figures invented personal voices with no grounding: the very failure CiC is built against |
| **Logos AI** (Faithlife) | AI answers from the user's licensed Logos library ([logos.com/ai](https://www.logos.com/ai)) | A large licensed scholarly library; a professional user base | A research tool, not a conversation. How it verifies is not shown |
| **Gloo** ★ | "Values-aligned AI" and tools for churches. IPO priced at $8 on 2025-11-19, below its $10–12 range. Raised about $73M at about $582M. About 57,000 paying customers ([Renaissance Capital](https://www.renaissancecapital.com/IPO-Center/News/115024/Christian-tech-platform-Gloo-Holdings-prices-IPO-at-$8-below-the-range)) | Sells to institutions at scale | Church operations, not historical understanding |
| **Hallow** ★ | Prayer and audio app. $50M Series C (Goodwater, 2023), $105M total raised, 10 million downloads ([Pulse 2.0](https://pulse2.com/hallow-10-million-app-downloads-and-50-million-in-funding)) | Audio craft; proof that Christians pay for subscriptions | Devotional, not dialogue or history |
| **Hello History** | Chat with historical figures ([hellohistory.ai](https://www.hellohistory.ai/)) | Broad catalogue; an education programme | Generic personas. No sources, no uncertainty |
| **Character.AI** | Persona chat at scale. The site returned 403. It banned open-ended chat for under-18s ([AP via 6abc](https://6abc.com/amp/post/characterai-is-banning-minors-interacting-chatbots/18090030/)). Agreed with Google to settle teen-harm suits ([Bloomberg Law, 2026-01-08](https://news.bloomberglaw.com/litigation/character-ai-google-agree-to-settle-teen-chatbot-harm-lawsuits)). User and price figures: UNVERIFIED | Engagement | The cautionary case on minors and safety |
| **Khanmigo** | AI tutor. In 2023 it offered chats with historical figures who would not comment on events after their lifetimes ([CNN via KRDO](https://krdo.com/news/2023/08/21/meet-your-new-ai-tutor/)). Whether the feature still exists in 2026: UNVERIFIED | School channel; teacher dashboards | Light personas, no primary-source citation |
| **BibleProject** | Free videos, podcast and classes, funded by supporters ([bibleproject.com](https://bibleproject.com/)) | Clarity and design; donor-funded at scale. Mark has already named its simple selection as a model (Pilot_Feedback_Log.md, 2026-10-19) | One-way content |
| **RightNow Media** | Video Bible-study library that churches pay for. "Over 30,000 churches and organizations" ([rightnowmedia.org](https://www.rightnowmedia.org/)) | A proven model where the church pays | Not interactive |
| **The Great Courses** | Lecture courses, including early Christianity ([plus.thegreatcourses.com](https://plus.thegreatcourses.com/search)) | Named professors | Passive |

**What the comparison shows**
- I found no product that combines all three: a voice for a whole tradition (not an invented individual), quotes checked word for word against primary sources, and visible confidence tags. CiC's own 2026-07 scan reached the same conclusion (`CiC_Marketplace_Landscape_Scan_V0_1.md`, lines 233–245).
- That is a real gap in the market. It is also a sign that rigor-first products are hard to fund. The scan notes that "rigor is currently funded as infrastructure or philanthropy, not as venture-scale consumer product" (lines 220–231).
- Most rivals sell subscriptions, or the church pays. CiC's pay-as-you-go packs are unusual.

**Regulation that bears on this**
- **California SB 243** ★, signed 2025-10-13, in force 2026-01-01 ([TechCrunch](https://techcrunch.com/2025/10/13/california-becomes-first-state-to-regulate-ai-companion-chatbots)). It requires AI disclosure, suicide and self-harm protocols reported to the state, and protections for minors. Whether CiC is a "companion chatbot" under the statute is a lawyer's question; I did not read the statute's definition.
- **FTC 6(b) inquiry into AI companions and minors**, 2025-09-11 ([FTC](https://www.ftc.gov/news-events/news/press-releases/2025/09/ftc-launches-inquiry-ai-chatbots-acting-companions)).
- **Amended COPPA rule**, with compliance due 2026-04-22: UNVERIFIED (from search results only).

---

## 7. Best parts

1. **The method itself is the moat.** It is the hardest thing to copy. Each world passes review-gated construction documents (Doc_01 to Doc_10) with capped review rounds. Every quote is checked word for word against a vendored file, and claims are tagged with a five-level confidence vocabulary. The machinery runs in CI, not only on paper (world gates, library validators, `roundcount`). A competitor can copy the interface in weeks. It cannot copy eleven worlds built this way without doing the same work.
2. **The corpus.** 929 source texts, each with a rights line that CI checks, each tied to a tradition through `cic/corpus-map/`. It is shared across worlds, so each new world costs less than the last.
3. **Honest positioning that the market is asking for.** YouVersion has publicly refused AI chat over misquotation. CiC's answer to that exact problem is built in. The disclaimer is clear, and the one written pilot tester praised it (Log item 10). The no-invention rule held when tested (item 8).
4. **Unit costs look sound at small scale.** A three-round conversation costs about $0.15 against $0.48–0.65 net revenue (Log, 2026-10-23). The margin has not been checked against an invoice (see 8.H4).
5. **The Atlas of 296 traditions.** A public asset that costs nothing to run per visitor. It gives the brand weight and makes a clear path to future worlds.
6. **Unusually thorough decision records.** Nearly every ruling is logged with a date and a reason. A diligence team can trace why things are the way they are. Few early projects can show this.
7. **A privacy design that keeps payment apart from conversation.** "What you say in a conversation is never stored with your payment" (`go-deeper.html`). This matters for prayer-adjacent data, which the project's own scan calls "the sector's most radioactive category" (Differentiation doc, L4).

---

## 8. Gaps and risks, ranked

### Blocking (fix before a diligence team or a growing public sees it)

**B1. Real money is being taken ahead of the project's own gates.**
- Evidence:
  - The public buy page carries three live Stripe links (fetched 2026-10-23), and `CIC_DEEPER_ENABLED` is `"1"` on `live`.
  - The Decision-Log says "No Payment Link is created before the answer" to the Stripe stored-value question (line 600). I found no record of that answer.
  - Choice 17 says "no tokens are sold until the account feature is set up" (line 705), and the expiry line is to be shown at every purchase. Accounts are off. The buy page states no expiry and no refund terms; the Decision-Log says "No page carries this yet" (line 596).
  - The four legal and tax questions are recorded as open (line 602).
  - Real payment is untested (Pilot_Feedback_Decisions.md:386). The privacy first line approved for PR 1083 says nothing is for sale (line 388).
  - I found no change order in `Decision-Log.md` reversing choice 17 or the "no link before the answer" rule. One may exist elsewhere: not checked.
- Smallest fix: one of two. Hide the buy buttons (empty the three `PAYMENT_LINKS` on `main`, since Cloudflare deploys `main`) until the gates are met. Or record a named change order that accepts selling now, put the expiry and refund lines on the buy page, and add Terms.
- For a lawyer: Are prepaid conversation tokens stored value or a gift card under the law that applies? What validity period follows? Does unclaimed-property law apply? Is sales tax due? Does Stripe's restricted-business list cover this?

**B2. The chain of title for the IP may be defective.**
- Evidence: the IP Assignment Agreement (Mark and Susan to Faithways Studio, Inc.) defines "the Incorporation Date" as 2026-07-21 and makes the assignment effective on that date. The real incorporation date is 2026-07-27. The documents were signed before the company existed. The bylaws' signed copy may be missing (`CiC_System_Hub_Decision_Log.md:428–437`). The log records this as "flagged to Mark and Susan directly, not resolved." The organisation files are now held outside the repo, so I could not see whether the documents were re-executed.
- Why it matters: a buyer or funder buys the company's IP. If the assignment is defective, the code, records, corpus work and brand may still belong to Mark and Susan personally.
- For a lawyer: Is an assignment signed before incorporation effective? Should it be re-executed or ratified on or after 2026-07-27?
- Smallest fix: have a lawyer review it, re-execute it if needed, and keep a signed copy.

**B3. No Terms of Use.**
- Evidence: there is no terms page in `cic-website/`; `/terms.html` returns 404; no "terms of use" text appears anywhere on the site or in the app. Anthropic's Usage Policy also requires AI disclosure at the start of each session or in the interface, and extra guidelines for minors ([anthropic.com/legal/aup](https://www.anthropic.com/legal/aup)). The disclosure part looks met (section 3); the minors part depends on the school and youth routes now being designed.
- For a lawyer: what the terms must cover. At least: AI-generated content, not pastoral or professional advice, age, the token licence and its expiry, refunds, the governing law of a Colorado PBC, and limits of liability.

### High

**H1. Very thin evidence from real users.**
- Evidence: one written pilot tester (Log line 6). Items 12–26 are "Mark, synthesis of user discussions", with the raw words not captured (Log, 2026-10-19 attribution entry). Mark said on 2026-08-09: "i am not keeping pilot feedback in written form, i am interviewing people" (`CiC_LLM_Provider_Cost_Options_2026-08-09.md`, §7). Traffic over 30 days: 72 messages, 50 first rounds (Log:187).
- Why it matters: a buyer or funder pays for proof that people come back. There is none in the repo yet.
- Smallest fix: the pilot form already exists (Tally, cap 100, closes 2026-12-31). Write down each interview's own words in a short form and count returning visitors from the usage log.

**H2. The bus factor is one, and the work is AI-carried.**
- Evidence: in the visible history, 481 commits are by "Claude" and 152 by Mark's account. No other human contributor appears. The adversarial reviews are AI reviews. External scholarly review is pushed to Year 2. Much state lives in chat threads, handed over through dated handoff files (16 files, 2026-10-19 to 10-23).
- Why it matters: a buyer asks who can run this on Monday if Mark cannot. The runbooks help. But the daily system of dozens of parallel threads has no second operator.
- Smallest fix: name one second person with read access, and walk them through the promotion and incident runbooks once.

**H3. The rights to the portraits, voices and some texts have not been checked against vendor terms.**
- Portraits: made with Google Gemini, partly on a 14-day trial (`In-App-Icons-Graphics/Decision-Log.md:312–315`). I found no record that its terms on commercial use and ownership were checked.
- Voices: made with ElevenLabs. Its terms allow commercial use on paid plans, and the user keeps the output rights; ElevenLabs takes a perpetual licence to use content to improve its service ([elevenlabs.io/terms-of-use](https://elevenlabs.io/terms-of-use), as read by the subagent and not re-opened by me). Whether every file was made on a paid plan is not recorded.
- Texts: 35 corpus texts are CC BY-SA 4.0 (`cic/texts/README.md`). Share-alike may reach packages and quotes. The public-domain rule is US-only (`texts_registry.py`), so some texts may still be in copyright elsewhere. Rights checks were mostly done by AI research threads (75 of 930 registry entries were supplied by Mark).
- Site photos: 5 of 6 are CC BY-SA, "not independently re-fetched" (`Brand-Assets/World-Media/README.md`).
- For a lawyer: commercial use and ownership of AI output under each tool's terms at the time it was made; what share-alike requires for the derived packages and for quotes; and which markets beyond the US need a separate rights check.
- Smallest fix: a one-page rights register for every vendor tool and plan, with dates.

**H4. The margin has not been checked against a bill.**
- Evidence: the cost report shows list-price estimates, "not the AWS bill" (Log:187). If AWS bills about 1.35 times list, a cold round costs about $0.106, above the $0.087 net a 20-token round earns at the $30 pack (Log:193). The weekly spend cap was removed on 2026-10-23 (ruling 69). Whether the AWS account has a budget alarm is unverified (Decision-Log:47).
- Smallest fix: compare one AWS invoice month with `engine/m8/reconcile.py`, and set an AWS budget alarm (a dashboard step for Mark).

**H5. The legal design for minors was ruled without a lawyer.**
- Evidence: "The under-13 route is designed here, not sent to a lawyer" (Decision-Log:1013–1017). The privacy page says nothing about children or age. The only age line on the public site is "By paying you confirm you are 18 or over."
- Why it matters: SB 243, the FTC inquiry and the Character.AI cases show this is where regulators are looking.
- For a lawyer: whether COPPA applies to a school or parent route for under-13s, which consent method is needed, and whether SB 243 applies.
- Smallest fix: keep every under-13 route unbuilt until counsel signs off, and add an age statement to the privacy page.

### Medium

**M1. Mixed messages about what the organisation is.**
- Most footers say "part of Faithways Studio, Inc." Four pages say "A ministry in formation" (`go-deeper.html`, `go-deeper-return.html`, `pilot.html`, `support.html`).
- A for-profit company asks for gifts to an "Accessibility Fund."
- The Stripe account was once flagged under "fundraising by nonprofits/charities", and "its resolution was never confirmed" (`CiC_FrontEnd_Decision_Log.md:318–321`).
- For a lawyer: what a PBC may promise about a named fund, and how gifts to a for-profit must be described and accounted for.

**M2. No trademark search.**
- "no legal trademark search ... remains open" (`CiC_Branding_Messaging_Analysis_Decision_Log.md:110–111`). Who owns the domains and who the registrar is are not recorded in the repo.

**M3. Production runs on a development identity.**
- `render.yaml:35–37`: "cic-bedrock-dev is a DEV identity - production wants its own."

**M4. Ten times the use would hit one machine.**
- The engine is a single Render service with SQLite databases on a 1 GB disk (`render.yaml:121–127`). Render's docs say: "You can't scale a service to multiple instances if it has a disk attached." ([render.com/docs/disks](https://render.com/docs/disks))
- At ten times today's traffic this is likely fine. At a hundred times it needs a database change.
- 644 MB of audio is served from the repo and site assets, not from R2.

**M5. Vendor dependence.**
- Voice quality rests on one model family through AWS Bedrock (pinned to `claude-sonnet-4-5` and `claude-haiku-4-5` profile ids).
- A price change, a model retirement or a change in Bedrock's terms would hit cost and the readability and voice baselines at once. Those baselines were measured on the pinned ids.
- Other dependencies: Render, Cloudflare, Stripe, ElevenLabs (audio is pre-generated, so the risk is low), Tally, and Supabase (old pilot transcripts).

### Low

**L1. Repo hygiene.**
- 729 remote branches.
- Three unreferenced screenshots at the root (`shot-*.png`). The README says nothing else sits at the root.
- No LICENSE, SECURITY.md or ownership notice. `package.json` says `"private": true` with no licence.
- `render.yaml`, a live file, carries long history commentary in its header, against CLAUDE.md's clean-surfaces rule.
- No secrets were found in the visible tree or history (scan by the subagent; the clone is shallow).

**L2. Six tests are reported failing on a clean `main`.**
- `engine/m1/tests/test_rendering_fidelity.py` (four) and `engine/m10/tests/test_validation.py` (two), with a waiver decision pending (Log:207). Reported second-hand; I did not run them.

**L3. The staging service is suspended.**
- Promotions go to `live` without the staging step the runbook names (Log:149). Ruled by Mark on 2026-10-12. A diligence reader will ask why.

---

## 9. Due-diligence checklist

| A buyer or funder would ask for | In the repo? |
|---|---|
| Articles, bylaws, cap table, shareholder agreement | Held privately. The repo records a date defect (B2) |
| IP assignment from the founders to the company | Held privately; possibly defective (B2) |
| Code licence and ownership notice | No |
| Terms of Use | No (B3) |
| Privacy policy | Yes. Contains a contradictory hidden cookie line and no age statement |
| A rights register for texts, images, voices and photos | Texts yes (strong). Images, voices and photos partial (H3) |
| Trademark and domain records | No (M2) |
| Revenue, users, retention | 30-day message counts only. No revenue recorded in the repo (H1) |
| Unit economics against invoices | List-price estimates only (H4) |
| Vendor contracts and terms reviewed | Not recorded |
| Security policy, incident history | Runbooks yes; SECURITY.md no; incident log not checked |
| Architecture and runbooks | Yes, thorough |
| Tests and CI | Yes, extensive. Six known failures pending a waiver (L2) |
| Team and key-person plan | No (H2) |
| Independent scholarly endorsement | No. Planned for Year 2 |
| Safety protocol documented | Yes (Facilitator Governance V3.6). Its testing belongs to the safety lens |

---

## 10. The next 30 days

In order of consequence. Each is small.

1. **Decide B1 this week.** Either switch the buy buttons off or record a change order, then add the expiry and refund lines and Terms. The buttons are one edit on `main`.
2. **Book one hour with a lawyer.** Bring the B1, B2, B3 and H5 questions as one list. The questions are already written: Decision-Log lines 39–40, 567 and 602, plus this report's 8.B2.
3. **Re-execute or ratify the IP assignment** if the lawyer says so. File the signed copy where it can be found.
4. **Reconcile one AWS invoice month** against the cost report, and set an AWS budget alarm.
5. **Capture ten real users in their own words.** Use the pilot form and short written interview notes. Count who comes back.
6. **Write a one-page rights register** for Gemini, ElevenLabs and the CC BY-SA texts and photos, with plan and date.
7. **Name a second person** with read access, and give them the runbooks.
8. **Tidy the shop window:** one footer line about the company, the hidden contradictory cookie sentence, the three root screenshots, and a LICENSE or "all rights reserved" notice. Branch cleanup can wait.

---

## 11. Five questions for Mark

1. Did you mean the buy buttons to be live now, before accounts, the Stripe answer and the expiry line? If yes, shall a change order record that?
2. Were the IP assignment and the bylaws re-executed after the 2026-07-27 incorporation? Where is the signed copy?
3. Did Stripe answer the stored-value question, and was the old restricted-category flag cleared?
4. How many people have you interviewed since August, and would you be willing to write down their own words from now on?
5. Who is the one person who could keep this running for a month if you had to step away?

---

## Cross-lens notes

- Engineering: six tests reported failing on a clean `main`; the production Bedrock identity is a dev identity; SQLite on one disk; staging suspended.
- Safety: SB 243 may apply. Check that the crisis protocol is documented in the form the statute asks for, if counsel says it applies.
- Scholarly: 35 CC BY-SA texts and the US-only public-domain rule; external review pushed to Year 2.
- Participant experience: the pilot themes (simplicity, answer length, who the Representative is) are converged but not built.
