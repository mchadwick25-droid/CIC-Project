# Round 2 — What should a unit of access be? A catalogue of models, with evidence

Research for Church in Conversation (Faithways Studio, Inc.). Web-based, dated 2026-10-02. Builds on `research_track1_access_units.md` (Track 1) and `research_track3_ledger_stripe.md` (Track 3) in this folder; general findings already made there (taxi-meter effect, dual entitlement, FTC dark-pattern catalogue, Audible/Hollis expiry law, hold→capture→release ledger shape, the big AI chat products' free-tier limits) are referenced, not repeated. No internal CiC numbers were consulted or used.

**Method note.** The sandbox egress proxy blocked direct fetches of arxiv.org, alphaxiv, emergentmind, cdn.openai.com, justanswer.com, studentsupport.cambly.com and web.archive.org. Every figure from those sources rests on search-engine summaries of the page plus secondary coverage, and is marked **(via search summary)**. Figures from aggregator/affiliate review sites are indicative only and marked **(aggregator)**. Exact UI wording is given only where a source quotes it.

**What this document is for.** Mark asked for examples, best practices and other conversation models, not one answer. Sections 1–10 are the catalogue. Sections A–D answer the four questions. The ranked list in D is input to his decision, with the uncertainty stated.

---

## The question underneath Mark's question

"How many rounds is a conversation, and if they accidentally back out do they lose what they paid?" is really three questions, and every model below answers them differently:

1. **What is the thing being bought?** (a reply, an exchange, a stretch of time, a question-with-its-answers, an experience, a share of the mission)
2. **When is it consumed?** (at purchase, at open, at first reply, at the end, never)
3. **What survives an interruption?** (nothing, the thread, the balance, the time, the right to come back)

Products get the fairness-feel wrong when the unit they *sell* and the unit they *meter* differ and the gap is discovered at a bad moment — Cursor's June 2025 "requests" to "credits" switch, JustAnswer's $5 that becomes $46/month, Duolingo energy draining on a correct answer. They get it right when the unit matches what the person came for and the edge cases are decided in the customer's favour before the customer has to ask (Steam's two-hour window, Audible's 365-day exchange, Cambly's "100% of your time back").

---

## 1. Per message / per turn

**Plain description.** Each reply from the system consumes one unit (or a model-dependent number of credits). The meter runs during the conversation.

**Named examples.**
- **ChatBuddy** (iOS, multi-model wrapper): "pay per reply," replies priced "from 0.02 credits," no subscription, "credits never expire," and the stated rule "if a provider fails, you are not charged" ([App Store listing via boei.help comparison](https://boei.help/blog/ai-chatbot-message-credits-pricing-comparison/)) **(via search summary)**.
- **Chatbase** (B2B chatbot builder): a "message credit" is spent per *request to the model*, not per conversation, so bills run higher than the plan price; when credits run out the bot shows "This AI Agent is currently unavailable. If you are the owner, please check your account" ([getmacha](https://www.getmacha.com/blog/chatbase-complete-guide); [myaskai](https://myaskai.com/blog/chatbase-pricing-explained)). The industry range is $0.01–$0.10 per response on entry plans, up to ~$0.50 on premium models **(aggregator)**.
- **Character.AI (2026 free tier)**: messages stay unlimited but the *acts around messaging* are now metered — ~400 swipes/day, 15–25 "go-ons," memos — and full-screen mid-chat ads run since April 2026. The Reddit reaction is the useful datum: "people could tolerate ads, but metering the act of chatting felt like a different category of change" ([piunikaweb, 11 Mar 2026](https://piunikaweb.com/2026/03/11/character-ai-limits-swipes-go-ons-memos-free-users/); [roborhythms](https://www.roborhythms.com/character-ai-swipe-limit/); [Medium](https://medium.com/@chuckmellisa/character-ai-just-capped-swipes-go-ons-and-memos-free-users-are-done-67e18227a80f)).
- **Hello History** (talk to 400+ historical figures, GPT-4): 20-message free trial, then subscription at $3.99/week, $5.99/month or $34.99/year for "up to 10,000 messages" per month. Review quoted: "They make it seem like some sort of free app, but after talking to a couple of historical figures and getting hooked, then they cut off access without warning, saying that we have to pay" ([alternatives.co](https://alternatives.co/software/hello-history/pricing/); [opentools](https://opentools.ai/tools/hello-history)) **(aggregator)**. This is the closest existing product to CiC's surface and it chose a message meter inside a subscription — the combination Mark has ruled out.
- **Nomi** (50 messages/day free), **Chai** (~70/day free), **Kindroid** (unlimited on a smaller model) show the companion category's convergence: message caps on free, unlimited on paid ([talkalma](https://talkalma.com/articles/free-ai-companion-apps.html); [lumichat](https://www.lumichat.ink/blog/best-nomi-ai-alternatives)) **(aggregator)**.

**Unit definition and edges.** A unit = one successful assistant reply. Accidental exit: units already spent stay spent; the thread usually persists. Refresh mid-reply: depends entirely on whether the product resumes streams (Track 1 §1.3). Error: the good practice is "not charged on provider failure" (ChatBuddy); the bad practice is Suno/Firefly-style deduction on failure (Track 1). Idle: no concept of idle; nothing is lost by waiting. Very short use: perfectly proportional — one question, one unit. Very long use: cost scales linearly and visibly, which is the problem.

**Fairness/value evidence.** Lambrecht & Skiera's taxi-meter effect (Track 1) applies at full strength: a visible per-reply meter makes each follow-up question feel like a charge. Prelec & Loewenstein's "pain of paying" and the coupling literature say the tighter the coupling of payment to each unit of consumption, the more the consumption itself is dampened ([Soman & Gourville 2001](https://www.researchgate.net/publication/247837070_Transaction_Decoupling_How_Price_Bundling_Affects_the_Decision_to_Consume); [Rotman, payment transparency](https://www-2.rotman.utoronto.ca/facbios/file/transparency.pdf)). For a product whose whole value is in the follow-up, that is the wrong direction.

**Revenue behaviour.** Maps exactly to cost; heavy users pay more; revenue per conversation is bounded only by the user. But it is the model in which the user is most likely to stop early (every reply is a decision to spend).

**Abuse risk.** Lowest of all models — the thing being metered is the thing that costs money.

**Fit for CiC.** Poor as the *visible* unit. Acceptable only as the *hidden* internal meter under a conversation-shaped unit (model 2).

---

## 2. Per whole conversation, with a hidden cap

**Plain description.** The participant buys "a conversation." Internally it has a ceiling (turns, tokens, or context-window size) set high enough that almost nobody meets it. The ceiling is not displayed.

**Named examples.**
- **ChatGPT**: the hidden cap is the context window. The wall message reads "You've reached the maximum length for this conversation, but you can keep talking by starting a new chat" (earlier: "The conversation is too long, please start a new one"). Complaints cluster on *loss of accumulated context* ("I really don't want to start a new conversation losing the data"), and on the cap arriving without warning after weeks of use ([OpenAI community](https://community.openai.com/t/the-conversation-is-too-long-please-start-a-new-one/128517); [growtraffic](https://growtraffic.co.uk/why-is-chatgpt-saying-the-conversation-is-too-long-please-start-a-new-one/); [folk](https://www.folk.com/blog/chatgpt-maximum-length-conversation-fix)).
- **Claude.ai**: three distinct messages — "This conversation is too long to continue" (thread filled the window) vs "Your message will exceed the length limit for this chat" (this one message does not fit). Anthropic's help page frames length limits as separate from usage limits and recommends one conversation per phase of a project ([support.anthropic.com](https://support.anthropic.com/en/articles/11647753-understanding-usage-and-length-limits); [five.reviews](https://www.five.reviews/fixes/claude-ai-conversation-too-long-error-fix/)).
- **Bing Chat (2023)**: the one case where the hidden cap became visible, and the one with a published rationale. Feb 2023: 5 turns/session, 50/day, because "most people already find the answer they are looking for within five turns"; the end-of-session message was "Sorry, this conversation has reached its limit. Use the 'broom' button to sweep this away and chat more." Raised to 10, 15, 20, then **30 turns/session and 300/day in June 2023**, and crucially the raise applied retroactively so users could "return to conversations where they may have previously reached their turn limit and pick up where they left off." Microsoft's Mikhail Parakhin: "most people do way less than 30 turns per chat conversation" ([Bing release notes](https://blogs.bing.com/search/2023/6/Bing-Preview-Release-Notes-Increasing-Chat-Turns-to-30-300/); [Windows Central](https://www.windowscentral.com/software-apps/windows-11/bing-chat-increases-turn-limit-to-30); [SERoundtable](https://www.seroundtable.com/microsoft-30-bing-chat-turns-noone-36138.html); [Engadget](https://www.engadget.com/microsoft-limits-bing-conversations-to-prevent-disturbing-chatbot-responses-154142211.html)).
- **Duolingo Max Video Call (Lily)**: a hidden *closer* rather than a hard cap — "after a set number of back-and-forths, a hidden 'Closer' prompts Lily to wrap up," sessions run 2–6 minutes, beginners ~1 minute of talk, advanced up to ~3; unlimited calls per day. Reviewers note it "keeps calls short and low-pressure but also caps how far a talk can go" ([duoplanet](https://duoplanet.com/duolingo-video-call/); [theowlandme](https://theowlandme.blog/2026/01/10/review-duolingo-max-video-calls/)) **(aggregator)**. This is the gentlest implementation of a hidden cap in the survey: the Representative *ends* the conversation in its own voice instead of a system wall.
- **Replika**: a hidden *memory* cap rather than a length cap — a ~25-message active window; the single most common complaint is forgetting ("Replika companions continue to forget even things that users just talked about") ([thredly](https://thredly.io/replika-memory); [App Store reviews](https://apps.apple.com/us/app/replika-ai-companion-chat/id1158555867?see-all=reviews)) **(aggregator)**. Relevant because CiC's cap will in practice be the context window, and the failure mode a participant notices first is the Representative losing the thread, not a wall.

**Unit definition and edges.** A unit = one thread with one Representative (or one Table), spent on first successful reply (Track 1/3 recommendation). Accidental exit: nothing lost if the thread persists and is resumable. Refresh: same. Error: hold is released, not captured (Track 3). Idle: the thread sleeps; a long grace window (days) costs ~nothing. Very short use: the hard case — one question "wastes" a conversation unless reopen-within-window or short-conversation-is-free rules exist (Track 1 §1.3 item 5). Very long use: the cap is hit; the honest design has to decide what happens: (a) a soft close in the Representative's voice (Lily pattern), (b) a system wall with the thread preserved (Claude/ChatGPT pattern), (c) a "continue in a new conversation that remembers this one" (summary carry-over — the fix every ChatGPT how-to article recommends by hand).

**Fairness/value evidence.** Bing's retroactive raise and Audible's "one credit = one book" are the precedents that a whole-thing unit is read as fair *provided the thing is whole*. The complaints are entirely about the cap being met without warning and the context being lost — neither is about the unit itself.

**Revenue behaviour.** Price per conversation is fixed; cost per conversation varies with length, so margin is a distribution, not a number. The cap bounds worst-case cost. Repeat purchase depends on the product giving reasons to return (Track 1 §2.2).

**Abuse risk.** Moderate: one paid conversation can be stretched to the cap. Mitigated by the cap and by per-turn rate limits (Track 3).

**Fit for CiC.** Strong — this is Track 1's recommendation. The open design question Round 2 adds: *what happens at the cap*, and whether a conversation can be "continued" into a second one that carries memory, which turns the cap from a wall into a page-turn.

---

## 3. Per conversation with a visible depth meter ("N left")

**Plain description.** Same unit as model 2, but the remaining room is shown: "30 of 30," "12 exchanges left," a bar.

**Named examples.**
- **Bing Chat "x of 30"** counter (2023): the turn counter sat under the input box. Microsoft's own data was that the counter was rarely reached ([SERoundtable](https://www.seroundtable.com/microsoft-30-bing-chat-turns-noone-36138.html)). The counter was removed when limits were raised; no product surveyed shows a per-conversation countdown today.
- **Perplexity free tier**: "a live counter shows how many you have left" (Pro searches, 5 per 4-hour rolling window) plus "a countdown indicator ... shows the remaining time before the next Pro search slot opens" ([fast.io](https://fast.io/resources/perplexity-message-limit/); [datastudios](https://www.datastudios.org/post/perplexity-free-plan-restrictions-features-speed-and-usage-limits)) **(aggregator)**. Note this counts *conversations started*, not depth within one.
- **ChatGPT Advanced Voice (free)**: ~15 min/day; no visible timer during the call; "a warning when 3 minutes of audio usage remains, and the conversation will automatically end once the limit is reached" ([Neowin](https://www.neowin.net/news/chatgpts-advanced-voice-mode-comes-to-free-users-with-usage-limits/); [precallai](https://precallai.com/chatgpt-voice-mode-daily-limit-for-free-users-complete-guide)). A forum thread complains that the clock runs "all time when the mode is open," i.e. idle time counts ([OpenAI community](https://community.openai.com/t/advanced-voice-mode-counts-all-time-when-the-mode-is-open-against-limits/972560)).
- **Hello History**: "20 messages" trial counter, then a hard wall — the review quoted under model 1 is a reaction to a visible-then-sudden counter.
- **Course Hero**: 30 document "unlocks" per month, visible, non-rolling; complaints: "only had 30 unlocks, and occasionally even fewer," and no refund of an unlock on a document "with wrong answers" ([Course Hero support](https://support.coursehero.com/hc/en-us/articles/203512610-How-many-documents-can-I-unlock-per-month-on-Course-Hero); [Trustpilot](https://uk.trustpilot.com/review/coursehero.com?page=8)).

**Unit definition and edges.** As model 2, but the participant can see the ceiling approaching. Edges are identical; the difference is purely psychological.

**Fairness/value evidence.** Two-sided. Transparency (EU CPC principles, FTC drip-pricing findings — Track 1) argues for showing the meter. The taxi-meter and coupling literature argues against showing it *during* consumption. The reconciliation the voice-mode pattern found: no meter while talking, one calm warning near the end. The only product-level test of a full-time counter (Bing) ended with the counter removed. Course Hero shows that a visible counter plus a non-refundable unit on a bad outcome is the combination that generates "robbed."

**Revenue behaviour.** Same as model 2. A visible meter increases early endings (people conserve), which lowers cost per conversation but also lowers depth, which is the value.

**Abuse risk.** Same as model 2.

**Fit for CiC.** The *full-time* meter is a poor fit: a participant watching "7 left" while a Representative is mid-thought is being pulled out of the world. The *late warning* variant (voice-mode pattern) is a good fit and is what Track 1 proposed. There is a real design choice between a Facilitator-voiced warning ("This conversation has room for a few more exchanges") and the Lily pattern (the Representative itself draws the exchange to a natural close). The governance rule that the Facilitator, not the Representative, speaks from outside the world suggests the warning is Facilitator text; the *close* could be in-world.

---

## 4. Time-boxed sessions and passes

**Plain description.** The unit is a stretch of clock time: a 15/30/45-minute session, a per-minute meter, or a day/week pass.

**Named examples.**
- **Cambly**: minutes per week, expire each Monday (Track 1). Edge policy, in its own words **(via search summary)**: "When a Cambly technical issue occurs during your lesson, you can get 100% of your time back through self-service"; if the tutor doesn't answer, "click 'Cancel lesson' to get your lesson back right away"; if minutes aren't returned, "go to your Lesson History, click on the lesson, click Help ... and follow the steps to request them back" ([Cambly student support](https://studentsupport.cambly.com/hc/en-us/articles/44738624394381-Getting-your-lesson-time-back)). The user agreement is the opposite register: "non-refundable and non-creditable, except where required by law" ([Cambly user agreement](https://www.cambly.com/legal/user_agreement/previous)).
- **Preply**: lessons "expire at the end of each billing cycle" and do not roll over; on cancellation, unused balance becomes credits that expire. Trustpilot/BBB: "ridiculous that credits expire in only a month," "no reminder when lessons are about to expire" ([Preply terms](https://termsofuse.preply.com/terms_of_use/en_SubscriptionServicesTerms.pdf); [BBB](https://www.bbb.org/us/ma/brookline/profile/tutoring/preply-inc-0021-495047/complaints); [pissedconsumer](https://preply.pissedconsumer.com/review.html)).
- **italki**: the dispute shape worth copying. Either party can file a "lesson incomplete request" within 3 days; the teacher has 7 days to respond; credits "could be returned in full to the student, released in full to the teacher, or split," and resolved credits go back to the Student Wallet ([italki support](https://support.italki.com/hc/en-us/articles/900002897883-How-do-I-report-a-lesson-problem-); [teacher no-show](https://support.italki.com/hc/en-us/articles/900006731846-What-should-I-do-if-my-teacher-did-not-show-up-for-the-lesson-)).
- **BetterHelp**: live sessions "usually run 30 to 45 minutes"; "does not charge for missed sessions"; the length "can depend on your therapist" ([therapyhelpers](https://therapyhelpers.com/blog/faqs-about-betterhelp-online-counseling/); [weareneveralone](https://weareneveralone.co/how-long-are-betterhelp-sessions/)) **(aggregator)**. **Talkspace** sells single live-session credits at $65 and out-of-pocket sessions at $175 (initial $299) ([Talkspace help](https://help.talkspace.com/hc/en-us/articles/360041531131-Talkspace-Services-Out-of-Pocket-Pricing)).
- **Clarity.fm**: per-minute, expert-set rates ($2–$30+, commonly $5–8/min), 15% commission; the fairness argument made *for* it is that "advice seekers come prepared ... not wasting the expert's time"; the argument against is "cost scales with how much you talk" and "no flat-rate option" ([MentorCruise](https://mentorcruise.com/blog/clarityfm-review-and-alternative/); [GrowthMentor](https://www.growthmentor.com/blog/clarity-vs-growthmentor)).
- **Keen (psychic advice, 25 years old, the most refined per-minute consumer model found)**: prepaid balance drawn down per minute; new users get the first 3 minutes free then $1.99/min for the first session; the published **Satisfaction Guarantee**: "credit one unsatisfactory conversation every 30 days for up to $25.00," requests "within 72 hours of the conversation," credits "issued in Keen dollars only" and "remain on your Keen account until used"; unspent balance is refundable on request ([Keen help: Satisfaction Guarantee](https://help.keen.com/hc/en-us/articles/1500000300362-Keen-s-Satisfaction-Guarantee); [refund of unspent balance](https://help.keen.com/hc/en-us/articles/4413380305299-How-can-I-request-a-refund-of-my-unspent-balance)).
- **Intro.co**: 15-minute video blocks at $35–$500 (experts $100–$2,000/hour), 30% commission ([growthmentor](https://www.growthmentor.com/blog/intro-co-alternatives); [SF Standard](https://sfstandard.com/2024/07/12/intro-cameo-techie-meeting-call/)).
- **ChatGPT voice** (15 min/day) and **Character.AI** daily throttles are time-boxed *free* allowances, not purchases.

**Unit definition and edges.** A unit = N minutes or one scheduled slot. Accidental exit: the clock usually keeps running (Cambly minutes, Keen balance) unless the product detects a drop and refunds (Cambly technical-issue rule). Refresh: as exit. Error: the better products refund 100% of the slot (Cambly, italki via dispute). Idle: the worst edge — idle time is billed (ChatGPT voice complaint), which is exactly wrong for reflection. Very short use: proportional (per-minute) or wasteful (fixed slot). Very long use: capped by the slot or by the balance.

**Fairness/value evidence.** Time units are legible and feel like a human-service norm (therapy, tutoring), but every complaint cluster in this category is about expiry (Cambly Mondays, Preply month-end) and about the clock running when value isn't flowing. Per-minute is the purest taxi meter; Keen survives it with a satisfaction guarantee and free first minutes, i.e. by spending money on edge-case trust.

**Revenue behaviour.** Durable where sessions are scheduled with a human (the slot has real scarcity). For an AI, a time box is an arbitrary proxy for compute, and a *pass* (day/week unlimited) reintroduces unbounded cost exposure.

**Abuse risk.** Per-minute: low. Passes: high (unlimited inside the window).

**Fit for CiC.** Weak as the primary unit. A reflective conversation does not want a clock, and a Representative does not have a calendar. The one transferable piece is the edge policy language (Cambly's "100% of your time back," Keen's guarantee), and possibly a *one-time, non-renewing week pass* as a third pack type for heavy users (Track 1 §1.2 D).

---

## 5. Abstract credits / tokens

**Plain description.** The participant buys a currency (credits, points, gems, "Keen dollars") and each action costs a variable number of them.

**Named examples.**
- **Cursor, June 16 – July 4, 2025**: the clearest recent case of a unit change destroying trust. Pro went from "500 fast requests/month, unlimited slow" to a $20 credit pool at API rates; "unlimited" applied only to Auto mode; users "burned through their $20 pool in days and then got billed at API rates for the overage"; the CEO's July 4 post: "Our recent pricing changes for individual plans were not communicated clearly, and we take full responsibility," with refunds for the window ([wearefounders timeline](https://www.wearefounders.uk/cursors-pricing-disaster-the-full-timeline-of-how-an-ai-coding-darling-burned-its-most-loyal-users/); [vantage](https://www.vantage.sh/blog/cursor-pricing-explained)). Lesson: a *request* was a unit people could count; a *credit* was not.
- **Poe** (silent ~90% cut to free points; purchased points non-refundable, one-year life — Track 1).
- **Suno**: free 50 credits refresh daily; subscription credits don't roll over; purchased top-ups "do not expire as long as your subscription stays active" — i.e. a non-expiring credit that is nonetheless lost if the subscription lapses ([Suno help](https://help.suno.com/en/categories/550209); [usagepricing](https://www.usagepricing.com/blueprint/suno)) **(aggregator)**. Plus the failed-generation deduction complaints from Track 1.
- **Duolingo gems → energy**: a full 25-energy refill costs 750 gems on iOS, 350 on Android, "450 gems if you reload in the middle of an exercise" — a worked example of a double currency whose exchange rate changes by platform and timing ([duoplanet](https://duoplanet.com/duolingo-energy-system/); [duolingoguides](https://duolingoguides.com/what-are-duolingo-gems-for/)) **(aggregator)**.
- **AI Dungeon**: monthly credits whose burn rate "depends on which model you pick and how long each response is," plus an ad-funded energy lane ("one ad gives you 10 turns") ([dungeonsdeep](https://dungeonsdeep.ai/blog/ai-dungeon-review-2026); [opentools](https://opentools.ai/tools/ai-dungeon)) **(aggregator)**.

**Unit definition and edges.** A unit = whatever the exchange table says today. Accidental exit: credits already burned are gone; variable-cost actions make the loss unpredictable. Error: the single biggest complaint cluster in this category (Suno, Firefly, Runway's half-way rule — Track 1). Idle: n/a. Very short / very long: proportional, but in a currency the participant cannot price without a table.

**Fairness/value evidence.** Raghubir & Srivastava's "monopoly money": scrip of equal face value is spent more freely than cash because it "does not feel like real money" ([APA PDF](https://www.apa.org/pubs/journals/releases/xap143213.pdf); [NYU Stern](https://w4.stern.nyu.edu/sternbusiness/spring_2009/monopolyMoney.html)). That is why game companies use it, and why the EU CPC principles now require real-money pricing and exact-amount purchase (Track 1). Abstract credits are the model regulators are moving against and the model behind the two biggest trust failures found (Cursor, Poe).

**Revenue behaviour.** Highest short-term yield (decoupling, breakage, forced bundle sizes). Least durable (every pricing change is a re-litigation; see Cursor).

**Abuse risk.** Low on cost (credits track cost), high on reputational/regulatory exposure.

**Fit for CiC.** Poor. A credit layer between a participant and a conversation with Benedict's monks is an "AI tell" in pricing form. Track 1 reached the same conclusion; Round 2 adds the Cursor and Suno-lapse cases as the specific failure shapes.

---

## 6. Daily/weekly refreshing allowance plus one-time boosts

**Plain description.** A free quota refills on a clock; the paid product is a *boost* (extra units, a skip-the-line, a refill) bought one-off.

**Named examples.**
- **Duolingo Energy** (25 units, refill by time, ads, gems, or a correct-answer streak; Super/Max = unlimited) and the backlash that *correct* answers drain it (Track 1; [duoplanet](https://duoplanet.com/duolingo-energy-system/)).
- **Suno** 50/day; **Perplexity** 5 Pro searches per rolling 4 hours with a visible countdown; **ChatGPT voice** 15 min/day; **Character.AI** daily swipe/go-on caps resetting 00:00 UTC; **Nomi/Chai** 50–70 messages/day. Every one is a free-tier shape whose paid answer is a *subscription*, not a one-time boost.
- **"Say less"** (anonymous AI chat): "optional boosts through watching videos or subscriptions if users want more daily messages or quicker response times, with no pressure or interruption" ([App Store via aicompanionguides](https://aicompanionguides.com/blog/best-free-ai-chat-apps/)) **(aggregator)** — the rare case of boosts without a wall.
- **Mobile games** (Candy Crush lives, gacha stamina): the origin of the pattern; refills sold one-off; the industry's own data on the 1.8% who ever pay and the 70% of payers who never pay twice is in Track 1 §2.1.

**Unit definition and edges.** The free unit = whatever refills (messages, sessions, minutes). Boost = a one-time add. Accidental exit: free units spent are spent, but the clock refills them, so loss is bounded by the refill period. Error: usually not refunded (the game model treats failure as the player's). Idle: idle *earns* the refill — the opposite of model 4. Short use: fine. Long use: hits the wall daily, which trains waiting.

**Fairness/value evidence.** Refill models feel fair for free (you lose nothing permanent) and feel manipulative the moment the refill is tuned to produce a wall mid-task (Duolingo "mid-exercise" gem surcharge; Character.AI swipe caps). Track 1's point stands: the refresh is a retention hook, not a revenue unit.

**Revenue behaviour.** Boost revenue is lumpy and small unless the wall is aggressive; the aggressive version is the one that gets the Character.AI reaction.

**Abuse risk.** Low (bounded by the clock), but cookie-clearing resets anonymous refills (Track 3 §f).

**Fit for CiC.** Good as the *free* shape (Track 1 §3.4 already proposes a weekly/monthly free conversation). Poor as the *paid* shape: a "boost" vocabulary is game vocabulary.

---

## 7. Question / topic / thread units with follow-ups included

**Plain description.** The unit is a *question* (or topic), and the answer plus its clarifications and follow-ups are part of the same unit — either unlimited, N follow-ups, or a time window of follow-ups.

**Named examples.**
- **JustAnswer**: "You can ask as many follow-up questions as needed by using the Reply area at the bottom of your Question page. You can still continue the conversation even after rating your answer" ([JustAnswer help](https://www.justanswer.com/help/using-justanswer)) **(via search summary)**. The unit is generous; the *billing* is the problem: the FTC sued on 13 January 2026 alleging the $1–$5 "join" fee enrolled people in a $46–$79/month subscription, "26 times the advertised price," with disclosures made "less prominent" between 2022 and 2025; JustAnswer has moved to dismiss ([ppc.land](https://ppc.land/ftc-justanswer-trapped-consumers-in-hidden-subscriptions-that-cost-26-times-the-advertised-price/); [Hinshaw](https://www.hinshawlaw.com/en/insights/blogs/consumer-crossroads-where-financial-services-and-litigation-intersect/ask-and-you-shall-receive-a-recurring-subscription-ftc-sues-a-web-qanda-service-for-deceptive-negative-option); [MLex](https://www.mlex.com/mlex/articles/2468164/justanswer-moves-to-dismiss-us-ftc-s-rosca-complaint-over-misleading-subscription-signups); BBB/ConsumerAffairs complaints at [BBB](https://www.bbb.org/us/ca/san-francisco/profile/ecommerce/justanswer-1116-82403/complaints?page=1)). The lesson is not "question units fail"; it is "a one-time-looking price that is secretly recurring is the worst thing a question unit can be attached to." CiC's no-subscription rule is precisely the protection.
- **HealthTap**: a personalized question to a specific doctor "usually $9.99"; "free clarifying questions and two follow-up questions are allowed at $5.99 each"; answer guaranteed within 72 hours; anonymous questions free within 24 hours ([onlinedoctor.com](https://www.onlinedoctor.com/health-tap-review/); [HealthTap](https://www.healthtap.com/send_question)) **(aggregator)**. A concrete "question + N follow-ups" price card.
- **Avvo**: free Q&A with follow-ups allowed on the thread; a separate fixed-fee "AvvoAdvisor" call at $39.95 ([Avvo](https://www.avvo.com/ask-a-lawyer); [smartlegalforms](https://www.smartlegalforms.com/pages/legal-advice)).
- **Chegg**: "up to 20 questions to Chegg Experts every month" — a question unit inside a subscription ([brighterly](https://brighterly.com/blog/course-hero-vs-chegg/)) **(aggregator)**.
- **Keen** (model 4) is effectively a question unit with a 72-hour satisfaction window.

**Unit definition and edges.** A unit = one thread opened by one question; follow-ups ride free (JustAnswer, Avvo) or are counted (HealthTap: 2) or time-boxed. Accidental exit: nothing lost — the thread is asynchronous by nature. Refresh: nothing lost. Error: n/a to the unit; a non-answer is handled by rating/refund. Idle: the thread waits; follow-up windows (72 hours Keen; "7 days" is common in expert marketplaces) decide when it closes. Short use: proportional. Long use: unlimited follow-ups are abused by a few (JustAnswer's membership is the answer to that), so most products put *some* bound on follow-ups.

**Fairness/value evidence.** Strong. "I asked a thing and got it answered, with the clarifications I needed" is the most natural "got what I paid for" frame in the survey. Every complaint found in this category is about billing mechanics, never about the unit.

**Revenue behaviour.** Durable where questions recur. One known weakness: people under-ask (one topic per purchase) unless follow-ups are visibly free.

**Abuse risk.** Moderate if follow-ups are unlimited and unbounded in time; low with a follow-up window.

**Fit for CiC.** Strong, and under-explored by Track 1. A CiC "conversation" *is* a topic thread with follow-ups: "Ask the monks of Cluny about the Rule of Benedict, and keep asking." Framing the unit as a *question you can keep pursuing* rather than a *session you are inside* changes the accidental-exit answer from "the conversation is saved" to "your question is still open" — a stronger, more natural promise. It also gives the cap a natural shape: a topic has an end; a follow-up window (say, 7 days) ends it without anyone counting turns.

---

## 8. Content-unlock / experience passes (own it for good)

**Plain description.** The participant buys permanent access to a *thing* — a world, a Representative, a Table — and uses it as much as they like.

**Named examples.**
- **Udemy**: "buy once and own forever," courses often $10–20 on sale, "lifetime access ... including future updates the instructor pushes." Reviews: "The biggest advantage is simple: lifetime access ... without worrying about subscriptions or renewals" ([Udemy support](https://support.udemy.com/hc/en-us/articles/229603708-Lifetime-access); [coddy](https://coddy.tech/vs/udemy); [uxcel](https://uxcel.com/blog/complete-udemy-review)).
- **The Great Courses vs Wondrium**: single courses $30–90 with lifetime access vs $20/month streaming; a forum user: "I just buy the individual courses I want ... I'm not sure I'd use it enough for a subscription" ([Well-Trained Mind forum](https://forums.welltrainedmind.com/topic/727862-best-way-to-access-the-great-courses-audible-vs-wondrium-vs/); [learnopoly](https://learnopoly.com/the-great-courses-review/)).
- **Audible**: one credit = one whole book, kept forever, exchangeable within 365 days ("that is an absolutely fair use of the Audible returns policy"), with Audible reserving the right to limit over-use; users report 2–4 returns a year pass without friction ([audiobookaddicts](https://audiobookaddicts.com/return-audible-book/); [techpenny](https://techpenny.com/returning-books-audible/)).
- **Museum audio guides**: British Museum app, full bundle £6 per language, themed tours £1.99–2.99; Louvre apps $1.99 "Unlock Full Version"; against that, **Bloomberg Connects** (1,250+ institutions) and **Smartify** are free, philanthropy-funded ([British Museum](https://www.britishmuseum.org/visit/audio-app); [Louvre App Store](https://apps.apple.com/us/app/louvre-museum-audio-guide/id1025300047); [Bloomberg Connects FAQ](https://www.bloombergconnects.org/faq/)).
- **Steam** (the refund norm that makes one-time unlocks feel safe): "any reason, within 14 days, under two hours played," no justification required; "I did not like it" accepted; now "a de facto industry standard" that Epic, GOG and consoles copied; Nintendo's "cannot be refunded or exchanged for any reason" is the cited counter-example ([PC Gamer](https://www.pcgamer.com/steam-refunds/); [indieforgames](https://indieforgames.com/steam-refund-policy/); [pocket-lint on Nintendo](https://www.pocket-lint.com/can-switch-purchases-be-refunded/)).
- **Replika lifetime** ($299.99, discontinued July 2025 — Track 1) and **Text With Jesus "Forever Premium" $199.99** ([App Store](https://apps.apple.com/us/app/text-with-jesus/id6446922759)): the AI-companion versions of "own it," both exposed to the fact that an AI product's marginal cost never reaches zero.

**Unit definition and edges.** A unit = permanent access to a world/Representative. Accidental exit: nothing is ever lost. Refresh/error/idle: irrelevant to the unit. Short use: the buyer "overpaid" relative to use but owns the thing (the Udemy frame). Long use: unbounded — the whole problem for an AI product.

**Fairness/value evidence.** The strongest "I got what I paid for" of any model (Udemy, Great Courses, Audible, Steam). Gourville & Soman's payment depreciation works *for* the seller here: the pain of the one payment fades, consumption continues ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0969698919304473)).

**Revenue behaviour.** Excellent per-sale clarity; one sale per world per person; growth comes from new worlds, which CiC is already building. Fatal flaw for pure AI: unlimited conversations under a one-time price (Replika's lifetime retreat). Workable hybrid: *the world is unlocked for good, with a fair-use allowance of conversations per period* — but that is a subscription in disguise unless the allowance is generous and the wording is honest.

**Abuse risk.** High if unlimited; moderate with fair use.

**Fit for CiC.** Mixed. "Unlock the Desert Fathers" is emotionally right (it is how people buy courses and books) and wrong on cost. It fits best as a *bundle* purchase (model 10) or as the *Family Tree is free, each world's conversations are bought* framing already in place, with the conversation (model 2/7) as the consumable inside it.

---

## 9. Pay-what-you-want / support tiers with free access

**Plain description.** Access is free; money is asked for as support, with or without a suggested amount.

**Named examples.**
- **Radiohead *In Rainbows* (2007)**: comScore: 38% paid, 62% took it free, average $2.26 across all downloaders (~$6 among payers); other surveys found 39% paid nothing and a $4.38 average; Kim, Natter & Spann (2009) found PWYW buyers pay ~86% of their internal reference price ([comScore](https://www.comscore.com/Insights/Press-Releases/2007/11/UK-Radiohead-Downloaders); [Progressive Boink survey](https://www.progressiveboink.com/2012/7/9/3147109/radiohead-in-rainbows-price-survey); [UBC blog on KNS 2009](https://blogs.ubc.ca/thedutchman/2011/02/27/paid-what-you-want/)).
- **Gumroad data**: PWYW yields 8% more sales and a 65% lower average price *without a suggested price*; the suggested price "is the single biggest lever"; one creator with a $24 suggestion and $1 minimum averaged ~$10 ([insightraider](https://insightraider.com/en/answers/does-gumroad-let-you-offer-pay-what-you-want); [justagirlandherblog](https://justagirlandherblog.com/pwyw-pricing/)).
- **Gneezy et al.** (Track 1): PWYW + half-to-charity was the only profitable condition.
- **Bible Project** (100% free, crowdfunded), **YouVersion** (free, ~40k donors — Track 1), **Bloomberg Connects** (free, philanthropy), **7 Cups** (free trained listeners; licensed therapy paid), **Wikipedia** banner data (Track 1).
- **Hallow parish model**: not PWYW but *subsidised access* — Premium for $1/year through parish partnerships, free for all religious, free for catechists and religious-ed families, one free lay account per parish ([Assumption BVM](https://assumptionbvm.org/Resources/News/articleType/ArticleView/articleId/1156417/Hallow-Prayer-App-1-Offer-to-Parishioners); [San Rafael](https://sanrafaelparish.org/hallow-parish-partnership)).

**Unit definition and edges.** No unit — which is why there are no edge cases, and why there is also no revenue floor.

**Fairness/value evidence.** Highest fairness-feel; weakest value signal (a $0 price tells the participant nothing about what the conversation cost to make). Mission framing and a suggested amount are what make it pay.

**Revenue behaviour.** Unreliable as the engine; reliable as a *second lane* (Track 1 §2.3). For a PBC that is not a 501(c)(3) (Track 3 §g), "donation" language also has legal edges.

**Abuse risk.** Total — the product is free.

**Fit for CiC.** As the only model: no. As a standing lane beside paid conversations, and as the mechanism for *scholarship/clergy/student* access (Hallow pattern): yes, and it answers the faith-adjacent worry that paying could ever feel like a condition of participation.

---

## 10. Bundles, gifts and group seats (churches, classes)

**Plain description.** Someone other than the participant buys access for many: a congregation licence, a class set, a gift.

**Named examples.**
- **RightNow Media**: one subscription per church, "unlimited invitations," priced by weekly attendance — from $25/month ($275/yr) for a microchurch of up to 25, $154.99/month for small churches, up to $1,159.99/month; "once a church subscribes, there is one subscription with unlimited access for everyone in your ministry" ([RightNow Media pricing](https://www.rightnowmedia.org/us/pricing); [microchurch](https://microchurch.rightnowmedia.org/); [learnofchrist](https://learnofchrist.com/resources/rightnow-media)).
- **FORMED.org (Catholic)**: parish subscription historically $1,999/year, one parish reports $2,451.31; individuals $9.95/month; parishioners register free under the parish licence ([St Joseph Bogota](https://stjosephbogota.org/formed-subscription/); [Ascension Parish](https://www.ascension-parish.com/what-is-formed-org/); [FORMED FAQ](https://leaders.formed.org/faq)).
- **Khanmigo for districts**: $5–$10 per student per year at the entry tiers; individuals $4/month ([myengineeringbuddy](https://www.myengineeringbuddy.com/blog/khanmigo-reviews-alternatives-pricing-offerings/); [kidsaitools](https://www.kidsaitools.com/en/articles/khanmigo-review-2026)) **(aggregator)**.
- **Hallow parish partnerships** (above). **Audible gift memberships**, **Steam gifting**, **Udemy gift a course** are the consumer-gift norms.

**Unit definition and edges.** A unit = a seat-year or an attendance band, with per-seat use governed by one of models 2–7 underneath. Accidental exit etc. inherit from the underlying unit. The distinctive edge is *who holds the balance* (the church? the member?) and what happens when a member leaves.

**Fairness/value evidence.** High for the end user (free to them); the buyer judges value on uptake, so usage reporting matters.

**Revenue behaviour.** The smoothest revenue in the survey — annual, predictable, and sold to an institution with a budget line. It is, however, a *subscription* at the institution level; Mark's one-time rule would make it a one-time class/term pack instead (e.g. "30 conversations for a confirmation class," non-expiring).

**Abuse risk.** Low (bounded seats or bounded conversation pool).

**Fit for CiC.** Strong as a complement — churches, seminaries, classes are the obvious buyers of a tradition's voice — and consistent with one-time purchase if sold as a pool of conversations rather than a seat-year. Not a substitute for the individual unit.

---

## A. Natural length of reflective AI conversations, and what the datasets say

Headline: **general-purpose chat is short (median 1–2 user turns), companionship chat is long-tailed, and the long tail is where a reflective product lives.** No published dataset isolates "slow, scholarly, faith-adjacent" conversations; the honest answer is a range with the sources.

| Source | Population | Length finding |
|---|---|---|
| **WildChat** (1M ChatGPT logs, ICLR 2024) | anonymous GPT-3.5/4 web users | mean **2.52** user turns; ~41% multi-turn; **3.7% exceed 10 turns** ([arXiv 2405.01470](https://arxiv.org/pdf/2405.01470); [ICLR PDF](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)) **(via search summary)** |
| **LMSYS-Chat-1M** | Chatbot Arena users | mean **2.0** turns ([alphaxiv](https://www.alphaxiv.org/abs/2309.11998)) **(via search summary)** |
| **ShareChat** (142,808 shared conversations, 660,293 turns, ChatGPT/Perplexity/Grok/Gemini/Claude, Apr 2023–Oct 2025) | self-selected shared links | mean **4.62** turns, "heterogeneous distribution" ([arXiv 2512.17843](https://arxiv.org/pdf/2512.17843)) **(via search summary)** — longer because people share the good ones |
| **Chai** (531,044 companion conversations, 2023) | companion/roleplay app | power law (Zeta, slope −1.8): **50% ≤ 10 messages; 1.2% > 500 messages; 0.1% > 5,000** ([arXiv 2303.06135](https://arxiv.org/pdf/2303.06135); [ar5iv](https://ar5iv.labs.arxiv.org/html/2303.06135)) |
| **Anthropic affective-use study** (4.5M Claude conversations, June 2025) | Claude.ai free+paid | 2.9% affective; "extensive conversations (with over 50+ human messages) were not the norm"; longer coaching chats "occasionally morph into companionship"; sentiment rises over the conversation ([Anthropic](https://anthropic.com/news/how-people-use-claude-for-support-advice-and-companionship); [TechCrunch](https://techcrunch.com/2025/06/26/people-use-ai-for-companionship-much-less-than-were-led-to-believe)) |
| **Anthropic Economic Index** | Claude.ai | higher-wage-occupation conversations run 1.53× the turns of others; task-iteration dominates learning ([Anthropic](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)) |
| **OpenAI "How People Use ChatGPT"** (1.5M messages, Sept 2025) | consumer ChatGPT | 49% Asking / 40% Doing / 11% Expressing; per-conversation turn counts not reported in coverage ([OpenAI PDF](https://cdn.openai.com/pdf/a253471f-8260-40c6-a2cc-aa93fe9f142e/economic-research-chatgpt-usage-paper.pdf); [CNBC](https://www.cnbc.com/2025/09/17/openai-releases-first-of-kind-study-revealing-how-people-use-chatgpt.html)) **(via search summary)** |
| **OpenAI/MIT affective study** (Mar 2025, ~40M interactions + 6,000 heavy voice users) | heavy Advanced Voice users | heavy users ~30 min/day; "total usage duration, more than any other factor, predicts affective engagement" ([OpenAI](https://openai.com/index/affective-use-study/); [MIT Media Lab](https://www.media.mit.edu/posts/openai-mit-research-collaboration-affective-use-and-emotional-wellbeing-in-ChatGPT/)) |
| **Bing Chat** (2023) | search chat | capped at 30 turns; "most people do way less than 30" (Parakhin) |
| **Character.AI** | companion | 17–29 min per session, 75–120 min/day depending on source **(aggregator)**; ChatGPT ~7–12 min/session ([the-decoder](https://the-decoder.com/character-ai-keeps-young-people-glued-to-their-smartphones-for-an-average-of-80-minutes-a-day/); [blankspaces](https://www.blankspaces.app/blog/chatgpt-screen-time-statistics)) |
| **Woebot / Wysa** (clinical studies) | mental-health chat | Woebot: 260 messages and 6+ hours over a study period, ~12 sessions/2 weeks; Wysa: mean 7.06 bot conversations per 14 days ([Frontiers](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2022.847991/full); [buildmvpfast](https://www.buildmvpfast.com/blog/mental-health-ai-chatbots-woebot-wysa-therapeutic-effectiveness-2026)) **(aggregator)** — i.e. ~10–20 messages per conversation, many conversations |
| **Length-vs-satisfaction experiment** (CHI 2024, GPT-4 Slack bots at 0/3/5/7 turns) | lab | longer conversations did *not* raise perceived quality even for "highly conversable" questions; brevity should be adaptive to the goal, not minimised ([ACM](https://dl.acm.org/doi/10.1145/3613905.3650823); [arXiv 2404.17025](https://arxiv.org/pdf/2404.17025)) |

**What this means for a hidden cap.** (1) If CiC's conversations behave like general chat, a cap at 20–30 user turns sits above p95 (WildChat: 3.7% exceed 10). (2) If they behave like companionship, the distribution is a power law and *no* turn cap sits above p95 comfortably — 1.2% of Chai chats pass 500 messages — so the cap must be *designed as an ending* (Lily closer, topic window) rather than hoped not to be reached. (3) The most defensible first estimate for a reflective, scholarly product is between the two: Woebot/Wysa-style 10–20 messages per sitting with return visits; Bing's 30 is the only published AI cap with an explicit "nobody reaches it" claim. (4) The context window, not the turn count, is the real ceiling: ChatGPT's wall is ~32k tokens (~10,000 words — [growtraffic](https://growtraffic.co.uk/why-is-chatgpt-saying-the-conversation-is-too-long-please-start-a-new-one/) **(aggregator)**); Replika's effective memory is ~25 messages. A long Representative reply (hundreds of words) burns context far faster than a short companion reply, so a *words-exchanged* budget is a better internal unit than turns. (5) The CHI 2024 result is the comfort: capping length does not by itself reduce satisfaction; being cut off *without a close* does. Only CiC's own pilot logs can replace this range with a number (Track 1 already says so).

---

## B. Accidental-exit, refresh, disconnect and error protection — patterns, wording, and where they fail

**Pattern 1 — Refund the slot on technical failure, in plain words, self-service.** Cambly: "When a Cambly technical issue occurs during your lesson, you can get 100% of your time back through self-service, then contact support if needed" **(via search summary)**. Where it falls short: the user agreement says the opposite ("non-refundable and non-creditable, except where required by law"), and the help page is the only place the real policy lives — which is why Trustpilot carries complaints from people who read the agreement first ([Cambly](https://studentsupport.cambly.com/hc/en-us/articles/44738624394381-Getting-your-lesson-time-back); [user agreement](https://www.cambly.com/legal/user_agreement/previous)). Lesson: put the generous rule in the terms, not just the help centre.

**Pattern 2 — No-questions refund window (Steam).** "Within 14 days ... under two hours ... no reason needed." Edge complaints are about the two-hour clock counting load/wait time ([Steam forum](https://steamcommunity.com/discussions/forum/1/4030224579612819809/)). Lesson: the clock should count *value delivered* (replies received), not wall time.

**Pattern 3 — Satisfaction credit with a bounded window (Keen).** One unsatisfactory conversation per 30 days, up to $25, within 72 hours, credited in site currency, never expiring. Falls short in that the credit is scrip, not cash (Monopoly-money problem), and the $25 cap can be below the cost of a long session. Lesson: a bounded, pre-published guarantee removes the "will they?" anxiety even when it is small.

**Pattern 4 — Exchange, don't refund (Audible).** 365-day exchange; "Audible finds the benefit is being overused it may ... limit the number of exchanges" — i.e. a soft cap enforced by judgement, and users have reverse-engineered "2–4 a year." Lesson: an unstated abuse threshold becomes folklore; stating it ("one in any 30 days," Keen) is cleaner.

**Pattern 5 — Dispute with a deadline and a split outcome (italki).** Report within 3 days; counterparty has 7 days; credits "returned in full, released in full, or split." Lesson: the time limits are what make it feel orderly; the split option is what makes it feel fair to both sides. CiC has no human counterparty, so the equivalent is a *self-service* release plus an audit entry (Track 3's `release` / `adjust` entries).

**Pattern 6 — Resumable threads and retroactive relief (Bing, Claude, ChatGPT).** Bing's June 2023 raise let users "return to conversations where they may have previously reached their turn limit." Claude and ChatGPT preserve the thread at the wall and tell the user to start a new chat; neither carries memory forward automatically, which is the whole complaint ("losing the data"). Lesson: the thread must survive; the *better* implementation lets the next conversation inherit a summary.

**Pattern 7 — "Not charged on failure" as a one-line promise (ChatBuddy, ElevenLabs, OpenAI prepaid — Track 1).** The products that lose trust are the ones where the rule is conditional ("first half of processing" — Runway) or absent (Suno, Firefly).

**Pattern 8 — Idle handling.** Customer-support chat defaults: Zendesk 20 minutes of no input on desktop, LiveChat 10 minutes default, LiveHelpNow recommends 10, Amazon Connect 2–480 minutes configurable ([Zendesk](https://support.zendesk.com/hc/en-us/articles/11005634190874-When-do-chats-time-out); [LiveChat](https://www.livechat.com/help/inactivity-how-it-works/); [AWS](https://docs.aws.amazon.com/connect/latest/adminguide/setup-chat-timeouts.html)). Those timeouts exist to free a *human agent*; an AI thread has no agent to free, so the idle timeout should be measured in days (the Track 1 ≥7-day grace), and the ChatGPT-voice complaint (idle time billed) is the anti-pattern.

**Pattern 9 — Mid-reply cut-offs.** No surveyed product cuts a reply to upsell; voice mode gives a 3-minute warning then ends the session. Duolingo's Lily closes in-character. These are the two acceptable shapes.

**Where products pay for getting it wrong.** JustAnswer (FTC suit, Jan 2026), Cursor (public apology + refunds, July 2025), Preply (BBB/Trustpilot expiry complaints), Suno/Firefly (failed-generation deductions), Character.AI (metering the act of chatting), Nintendo (no refunds, used as the industry's bad example). In every case the money at stake per incident was small; the trust cost was not.

---

## C. Fairness perception — which unit definitions produce "I got what I paid for" vs "I got robbed"

Evidence-backed principles, each tied to a model above:

1. **The unit must be the thing the person wanted.** Udemy ("own forever"), Audible (one book), Steam (a game, returnable), JustAnswer's *unit* (a question with unlimited follow-ups — the unit is loved even while the billing is sued). Models 2, 7, 8 pass; models 1, 5 fail (a reply or a credit is not what anyone came for).
2. **Coupling and the taxi meter.** Tight payment-to-consumption coupling dampens consumption and enjoyment (Prelec & Loewenstein; Soman & Gourville; Lambrecht & Skiera — Track 1). Models 1, 4 (per-minute), 5 are tightly coupled; 2, 7, 8 are loosely coupled. For a product whose value is in depth, loose coupling is the point.
3. **Decoupled currency is spent more freely — and resented later.** Raghubir & Srivastava's monopoly money explains why credits (model 5) raise short-term revenue and why regulators and users push back; Cursor is the 2025 case.
4. **Expiry is read as theft.** Preply, Cambly, Course Hero, Audible (Hollis), Suno top-ups that die with the subscription. Any model whose purchased units expire starts with a fairness deficit. Non-expiry is the single cheapest fairness feature (Track 1 §2.3).
5. **Charging for failure is read as predatory regardless of amount.** Suno, Firefly, Runway's half-way rule; Course Hero's "no refund on wrong answers." The hold→release ledger (Track 3) is the mechanical answer.
6. **A published, bounded guarantee beats an unstated generous one.** Keen's "one per 30 days up to $25 within 72 hours" produces fewer "will they?" questions than Audible's "we may limit overuse."
7. **Dual entitlement / cost-structure appeals** (Track 1): telling people what the conversation costs raises fairness and willingness to pay. This argues for pricing in dollars per conversation and saying what a conversation runs on.
8. **Length does not buy satisfaction; closure does** (CHI 2024). A capped conversation that *ends well* is not experienced as short-changed; a conversation cut at a wall is.
9. **Faith-adjacent specifics.** Hallow's $1/year parish access, free for clergy/religious/catechists, and "why we charge" post (Track 1) show that a faith product can charge without the charge being read as a toll on participation — by making subsidised access visible and by explaining the cost. 7 Cups' free-listener / paid-therapist split shows the opposite risk: when the free tier is a lesser *kind* of help, users notice.

**Net:** "I got what I paid for" = a whole thing, in dollars, that doesn't expire, isn't charged when it fails, and ends on purpose. "I got robbed" = a counted thing, in a currency, that expires, is charged on failure, and ends at a wall.

---

## D. Comparison table and ranked input

Scores 1 (poor) to 5 (strong). "Fit" is for a slow, reflective, faith-adjacent conversation under a one-time, no-subscription constraint. Scores are judgements from the evidence above, not measurements.

| Model | Fairness-feel | Value-clarity | Revenue durability | Abuse resistance | Build complexity (5 = simplest) | Fit for CiC | Main uncertainty |
|---|---|---|---|---|---|---|---|
| 1. Per message/turn | 2 | 3 | 3 | 5 | 4 | 1 | — |
| 2. Per conversation, hidden cap | 4 | 4 | 3 | 3 | 3 | 5 | What happens at the cap; short-conversation rule |
| 3. Per conversation, visible meter | 3 | 4 | 3 | 3 | 3 | 2 (full-time) / 4 (late warning) | Whether any warning pulls people out of the world |
| 4. Time-boxed / per-minute / pass | 3 | 4 | 3 | 2 (pass) / 4 (minute) | 3 | 2 | Idle-time billing; clock vs reflection |
| 5. Abstract credits | 2 | 1 | 2 | 4 | 3 | 1 | Regulatory direction |
| 6. Refreshing allowance + boosts | 4 (free) / 2 (paid) | 2 | 2 | 3 | 4 | 4 (free shape) / 1 (paid shape) | Refill period |
| 7. Question/topic + follow-ups | 5 | 5 | 3 | 3 | 3 | 5 | Follow-up window length; one-topic-per-purchase under-asking |
| 8. Content-unlock / own a world | 5 | 5 | 2 | 1 (unlimited) / 3 (fair use) | 4 | 3 | Unbounded compute; "fair use" honesty |
| 9. PWYW / support with free access | 5 | 1 | 1 | 1 | 5 | 2 (alone) / 5 (as a lane) | Suggested amount; PBC donation language |
| 10. Bundles / gifts / group seats | 4 | 4 | 5 | 4 | 2 | 4 (complement) | One-time pool vs institutional subscription |

**Ranked input to Mark's decision (not a decision):**

1. **A conversation framed as a question you can keep pursuing — model 7 wearing model 2's mechanics.** Sell "a conversation with [Representative]" in dollars; define it to the participant as *your question and everything you ask after it*; close it by a follow-up window (days) and a hidden words-exchanged ceiling, with the Representative drawing it to a close in its own voice when the ceiling nears (Lily pattern) and a Facilitator-register line for the system facts. Accidental exit becomes "your question is still open." This is Track 1's recommendation with a better name and a better ending. Uncertainty: whether participants read "question" as narrower than "conversation" and under-ask.
2. **Model 2 as Track 1 stated it** (conversation + hidden cap + long grace), if the "question" framing tests badly.
3. **Model 10 as a one-time class/congregation pool** (N non-expiring conversations bought by a church or teacher), built on whichever of 1–2 is chosen — the most durable revenue in the survey and the most natural buyer for a tradition's voice.
4. **Model 9 as a standing lane** (suggested amount, mission framing, clergy/student scholarship access), never as the price of the product.
5. **Model 6 as the free shape only** (a refreshing free conversation; no "boosts" vocabulary).
6. **Model 8** only as a *bundle name* ("the Desert Fathers, five conversations") never as unlimited access.
7. **Model 4** only as an optional one-time, non-renewing week pass held in reserve.
8. Models **1, 3 (full-time meter), 5**: not recommended; the evidence against them is the strongest in the survey.

**Honest note on uncertainty.** The fairness literature is robust and old; the AI-product evidence is 2023–2026 and mostly from products that *also* sell subscriptions, so nobody has published what a consumables-only AI conversation product's repeat-purchase or length distribution looks like. The two numbers that matter most — CiC's own p95 conversation length in words, and whether a one-question visit is common — do not exist yet and cannot be borrowed from any source here.

---

## Appendix — sources used in Round 2 (accessed 2026-10-02)

Datasets and studies: WildChat (arXiv 2405.01470; ICLR 2024); LMSYS-Chat-1M (alphaxiv 2309.11998); ShareChat (arXiv 2512.17843); Chai "Rewarding Chatbots" (arXiv 2303.06135; ar5iv); Anthropic affective-use (anthropic.com/news; TechCrunch 26 Jun 2025); Anthropic Economic Index (Jan 2026 report); OpenAI "How People Use ChatGPT" (cdn.openai.com; CNBC 17 Sep 2025); OpenAI/MIT affective-use study (openai.com/index; MIT Media Lab); CHI 2024 length-satisfaction (ACM 10.1145/3613905.3650823; arXiv 2404.17025); Woebot/Wysa (Frontiers Digital Health 2022; buildmvpfast).

Products: ChatBuddy, Chatbase (boei.help; getmacha; myaskai); Character.AI 2026 (piunikaweb; roborhythms; Medium); Hello History (alternatives.co; opentools); Nomi/Chai/Kindroid (talkalma; lumichat); ChatGPT length wall (community.openai.com; growtraffic; folk); Claude length limits (support.anthropic.com; five.reviews); Bing Chat (blogs.bing.com; Windows Central; SERoundtable; Engadget); Duolingo Video Call (duoplanet; theowlandme); Replika memory (thredly; App Store); Perplexity counter (fast.io; datastudios); ChatGPT voice (Neowin; precallai; community.openai.com); Course Hero/Chegg (support.coursehero.com; Trustpilot; brighterly); Cambly (studentsupport.cambly.com; user agreement); Preply (terms PDF; BBB; pissedconsumer); italki (support.italki.com); BetterHelp (therapyhelpers; weareneveralone); Talkspace (help.talkspace.com); Clarity.fm (MentorCruise; GrowthMentor); Keen (help.keen.com x2); Intro.co (growthmentor; SF Standard); Cursor (wearefounders; vantage); Suno (help.suno.com; usagepricing); AI Dungeon (dungeonsdeep; opentools); JustAnswer (justanswer.com/help; ppc.land; Hinshaw; MLex; BBB); HealthTap (onlinedoctor.com; healthtap.com); Avvo; Udemy (support.udemy.com; coddy; uxcel); Great Courses/Wondrium (Well-Trained Mind forum; learnopoly); Audible (audiobookaddicts; techpenny); museum apps (British Museum; Louvre App Store; Bloomberg Connects FAQ); Steam/Nintendo (PC Gamer; indieforgames; pocket-lint; Steam forum); Text With Jesus (App Store); Radiohead (comScore; Progressive Boink; UBC blog); Gumroad (insightraider; justagirlandherblog); Hallow parishes (assumptionbvm.org; sanrafaelparish.org); RightNow Media (pricing; microchurch; learnofchrist); FORMED (stjosephbogota; ascension-parish; leaders.formed.org); Khanmigo districts (myengineeringbuddy; kidsaitools); 7 Cups (selfpause; simplypsychology).

Fairness research: Prelec & Loewenstein 1998; Soman & Gourville 2001 (ResearchGate); Gourville & Soman payment depreciation (ScienceDirect); Rotman payment-transparency PDF; Raghubir & Srivastava "Monopoly Money" (APA PDF; NYU Stern); Kim, Natter & Spann 2009 (via UBC blog). Chat idle timeouts: Zendesk; LiveChat; LiveHelpNow; Amazon Connect.
