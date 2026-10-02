# Round 2 — Free allowance designs and the end-of-free moment

Research for Church in Conversation (Faithways Studio, Inc.). Web-based, dated 2026-10-02. Builds on `research_track1_access_units.md` (Track 1) and does not repeat its general findings; where Track 1 already gave a figure, this file only adds what is new. No internal CiC numbers were consulted or used.

Method note. The sandbox egress proxy blocks many primary pages (hallow.com, lichess.org, support.anthropic.com, help.poe.com, help.medium.com, nngroup.com, theaudiencers.com, inma.org, slate.com, news.ycombinator.com, quora.com, perplexity.ai help center, ssrn.com, researchgate.net, khanacademy.org, web.archive.org). Points that rest on a search-engine summary of a page rather than the page itself are marked **(via search summary)**. Exact copy is quoted only where a source shows it; where I describe a screen from general knowledge and could not verify the wording today, it is marked **(unverified wording)**. Treat those as prompts to check against a live screenshot before anyone quotes them.

Constraint taken as given: one-time pay-as-you-go top-ups, no subscriptions. The end-of-free moment must be seamless, honest and unmanipulative. This is a catalogue of options and evidence for Mark to react to, not a pre-decided answer.

---

## 0. The shortest possible summary

1. Almost every product surveyed that users praise shows its limit **between units, not inside one**, says **when the free allowance comes back**, and **keeps what the user already made**. The products users resent either charge for a failure, hide the decline path, interrupt mid-task, or use guilt or fake urgency.
2. The two strongest templates for a mission-driven product are the **Guardian "epic"** (an inline end-of-article ask that is calm, specific about cost, and dismissable by simply scrolling on) and **Wikipedia's post-2022 banners** (where the community formally banned "we'll go away without you," non-donor percentages, and guilt lines, and found that softer copy cost little or nothing in donations).
3. Six design directions are given in §5. The ranked recommendation (§6) is a **closing card at the natural end of the final free conversation, followed by a quiet "start another" sheet**, with a separate always-visible support lane. Confidence: moderate-high on the shape, moderate on copy, low on pack sizes (not in scope).

---

## 1. Free allowance designs — the catalogue

Format per product: free amount; reset; anonymous vs signed-in; what happens at the limit; observed reaction. Track 1 already covered units and amounts for most AI products, so the emphasis here is on the limit moment and the reaction.

### 1.1 AI chat and assistants

**ChatGPT (signed out).** About 10 messages per rolling 5 hours on the default model, then automatic switch to a smaller model with no hard stop (sources differ; older coverage says 3–5 messages then a sign-up wall). Session-only: one conversation at a time, no history, lost on close. The modal copy seen by logged-out users is "Log in or sign up to get smarter responses, upload files and images, and more." with a "Stay logged out" option (the button text is from general knowledge; the headline is confirmed by search). Hard-limit copy on the paid-model allowance: "You've reached your usage limit for GPT-4o. Please try again after [time]." and "You have hit the free plan limit for GPT-4o." Reaction: the degrade-not-block design draws little anger; the per-hour wall copy ("You've reached our limit of messages per hour. Please try again later") draws confusion because it gives no number and no exact time. Sources: [meetaitools](https://meetaitools.com/can-you-use-chatgpt-for-free-without-account/), [How-To Geek](https://www.howtogeek.com/chatgpt-no-longer-needs-an-account/), [ghacks](https://www.ghacks.net/2024/04/02/chatgpt-no-longer-requires-an-account-to-use-but-there-are-some-limitations/), [byteplus](https://www.byteplus.com/en/topic/548499), [OpenAI community thread](https://community.openai.com/t/chatgpt-prompts-youve-reached-our-limit-of-messages-per-hour-please-try-again-later/206307), [ai-toolbox](https://www.ai-toolbox.co/chatgpt-management-and-productivity/chatgpt-login-guide).

**Claude Free.** Token-metered, rolling 5-hour window, roughly 15–40 messages per window depending on length; no fixed count published. Signed-in only. At the limit the interface shows the next reset time; starting a new chat does not bypass it. Copy reported: "You've hit your limit for Claude messages. Please wait before trying again." Reaction: the visible reset time is the most-cited positive; the unpredictability of the count is the most-cited negative. Sources: [datastudios](https://www.datastudios.org/post/claude-free-limits-updated-usage-restrictions-message-caps-and-file-upload-rules), [heyuan110](https://www.heyuan110.com/posts/ai/2026-07-08-claude-free-tier-limits/), [claudemarket](https://www.claudemarket.ai/blog/youve-hit-your-limit-for-claude-messages-please-wait-before-trying-again) (support.anthropic.com blocked; **via search summary**).

**Perplexity Free.** 5 Pro searches per rolling 4 hours; unlimited basic searches. Anonymous threads are kept 14 days then deleted; sign-in (magic link or one-time code, no password) saves them. At the limit the Pro toggle is disabled and basic search continues. Notable failure: several guides describe a **silent downgrade** — Pro quietly returns a standard answer with no banner or explanation. Reaction: the two-speed model itself is accepted; the silent downgrade and unannounced cuts to Pro limits (daily to weekly in late 2025, discovered by users hitting walls early) drew Reddit complaints. Sources: [fast.io](https://fast.io/resources/perplexity-message-limit/), [aiqnahub](https://www.aiqnahub.com/perplexity-free-search-limit-standard-mode/), [Android Authority](https://www.androidauthority.com/perplexity-pro-advanced-ai-limits-reduced-3667942/), [Perplexity help: threads](https://www.perplexity.ai/help-center/en/articles/10354769-what-is-a-thread) (**via search summary**), [perplexityaimagazine](https://perplexityaimagazine.com/perplexity-hub/perplexity-threads-not-saving-fix/).

**Character.AI Free.** Throttling plus a "waiting room" queue at peak; c.ai+ ($9.99/mo) skips the queue. At the limit free users are sent to a lobby "with no clear timeline and no way to skip the line"; users report the stated wait ("1 minute") not matching the real wait (7–10 minutes). Reaction: the queue is resented less for existing than for lying about its length. Sources: [roborhythms](https://www.roborhythms.com/character-ai-wait-time-fixes/), [c.ai+ FAQ](https://support.character.ai/hc/en-us/articles/55845963766555-C-ai-FAQ).

**Replika.** Unlimited free text; romance and "intimate" modes behind Pro. The limit moment is the resented part: the bot sends a blurred "romantic" image that opens an upgrade pop-up when tapped, and users describe being "teased" by the character to pay. A January 2025 FTC complaint (Tech Justice Law Project and others) names this as manipulative design. Lesson for CiC: **never let the Representative's voice sell**. Sources: [TIME](https://time.com/7209824/replika-ftc-complaint/), [complaint PDF](https://techjusticelaw.org/wp-content/uploads/2025/01/Complaint-and-Petition-for-Investigation-Re-Replika.pdf), [Suffolk JHBL](https://sites.suffolk.edu/jhbl/2025/11/24/ai-companions-emotional-dependency-and-the-law-ftcs-next-frontier/).

**Pi (Inflection).** Free, no paid tier. In August 2024 Inflection added caps and cooldowns aimed at heavy users ("many messages a minute for hours"). At the limit: a wait, not a charge. Reaction: mild; the product had no purchase to resent. Sources: [TechCrunch](https://techcrunch.com/2024/08/26/five-months-after-microsoft-hired-its-founders-inflection-adds-usage-caps-to-pi/), [Axios](https://www.axios.com/2024/08/26/inflection-pi-ai-chatbot-enterprise).

**Poe.** Daily points for free users; they do not roll over; "wait for them to renew tomorrow, or pay for more now." Add-on points are sold as one-time purchases. Reaction (Track 1): the silent ~90% cut to the daily grant in March 2026 is the complaint, not the daily reset. Source: [Poe FAQ](https://help.poe.com/hc/en-us/articles/19944206309524-Poe-FAQs) (**via search summary**).

**Khanmigo.** No free learner tier; $4/month or $44/year; free for US teachers; a one-month trial by coupon for new learners. The nonprofit chose a cheap flat fee over a metered free tier. Sources: [khanmigo.ai](https://khanmigo.ai/), [Khan support](https://support.khanacademy.org/hc/en-us/articles/13982227159437-How-do-I-sign-up-for-Khanmigo), [myengineeringbuddy](https://www.myengineeringbuddy.com/blog/khanmigo-reviews-alternatives-pricing-offerings/).

**Notion AI.** 20 complimentary responses per workspace, one-time, never refreshed. On response 21 the AI menu items grey out and show an upgrade prompt. Reaction: the one-time trial is widely described as too small to judge the feature. Source: [eesel](https://www.eesel.ai/blog/notion-ai-complimentary-responses), [nexodatech](https://nexodatech.com/notion-ai-free-tier-prompts-limit/).

**Kagi (search).** 100 free searches on sign-up with **no time limit and no card**; then a paid plan is required. Plus a "Fair Pricing" promise that an unused month is credited back. Reaction: consistently praised as honest; "you are the customer, not the product." A direct precedent for a time-unconstrained, count-based free allowance that people trust. Sources: [Tim Hårek review](https://timharek.no/blog/kagi-review/), [Android Police](https://www.androidpolice.com/ethical-search-engine-kagi-return-subscription-money/), [Kagi blog](https://blog.kagi.com/the-many-benefits-of-paying-for-search).

### 1.2 Creative tools with credit packs

**Suno.** Free: 50 credits renewing daily (about 10 songs). Top-ups are sold but at roughly 5x the subscription per-credit price; packs are not published on the pricing page. Reaction: Trustpilot and Reddit complaints cluster on credits consumed by failed or unwanted generations and on top-up pricing that feels punitive. Sources: [eesel Suno review](https://www.eesel.ai/blog/suno-review), [stacksheriff](https://stacksheriff.com/ai-tools/suno-pricing-2/), [Trustpilot](https://ca.trustpilot.com/review/suno.com).

**Midjourney.** No free tier now; paid plans get Fast hours. At the limit the account **automatically drops to Relax mode** (slower, unlimited on Standard and above) rather than stopping; extra Fast hours are $4/hour, bought on the account page, and purchased hours do not expire. Reaction: the automatic degrade is accepted as fair because nothing is lost, only speed. Sources: [aituts](https://aituts.com/midjourney-speed/), [aiarty](https://www.aiarty.com/midjourney-guide/midjourney-relax-mode.htm), [ponr](https://ponr.org/en/articles/midjourney-billing-guide.html).

**ElevenLabs.** Free: 10,000 characters per calendar month, resets on the 1st (UTC). At the limit the API returns a structured `quota_exceeded` error (changed from a misleading 401 to a 429 in 2025 so users would not think their key was broken); the web app offers pay-as-you-go credits. Lesson: a limit error must name itself plainly. Sources: [ElevenLabs changelog](https://elevenlabs.io/docs/changelog/2025/5/5), [GitHub issue](https://github.com/zbynekdrlik/songplayer/issues/125).

### 1.3 Learning and wellbeing apps

**Duolingo (Energy, 2025).** 25 energy to start; every question answered drains one, right or wrong; a free user gets roughly three lessons before the wall. Refill: wait (users report multi-hour timers, up to 18 hours quoted), watch an ad, spend gems, or buy Super. Reaction: the most-cited backlash in this file — a Reddit thread "So now we're punished for using the app?" at ~3,000 upvotes; "worse than the heart system"; "a paywall disguised as a feature." Duolingo's earnings call said energy "rewards correct streaks" and lifted conversion. The lesson is not "don't meter" but "never let the meter punish doing the thing well." Sources: [techissuestoday](https://techissuestoday.com/duolingo-energy-system-user-backlash/) (**via search summary**), [Class Central](https://www.classcentral.com/report/duolingo-breaks-hearts-for-energy/), [toptechguides](https://toptechguides.com/duolingo-energy-update-backlash/), [MarketBeat Q2 2025 transcript](https://www.marketbeat.com/earnings/reports/2025-8-6-duolingo-inc-stock).

**Headspace / Calm.** Both front-load a trial paywall with card required; free content is a rotating sliver. Headspace's trial screen is praised in teardowns for stating terms plainly ("14 days free, then $X" with "nothing vague or hidden") after a breathing exercise the user has already done. Calm's most repeated complaint is being charged a full year after a trial with no reminder email and refunds refused because terms were "technically disclosed." Lesson: honest terms on the screen are necessary but not sufficient; the reminder before the charge is what people judge. Sources: [dev.to paywallpro](https://dev.to/paywallpro/onboarding-first-screen-trends-emotional-hooks-are-back-because-they-never-left-74d), [growth.design Headspace](https://growth.design/case-studies/headspace-user-onboarding), [choosingtherapy](https://www.choosingtherapy.com/headspace-vs-calm/), [unstar](https://unstar.app/blog/calm-headspace-insight-timer-balance-ten-percent-happier-meditation-apps-ranked-2026).

**Hallow.** Daily rosary, daily gospel, hundreds of meditations free forever; Hallow+ $69.99/yr with a 2-week trial. The company publishes a "Why is there a Hallow subscription?" post, gives one free subscription per paid one, gives free subscriptions to all clergy, and has a scholarship request path. Reaction: the free tier is praised as "enough to build a daily prayer habit"; the complaints are the familiar trial-to-charge and cancellation ones, and a sense that "the free-tier paywall pushes constantly." Sources: [Hallow blog](https://hallow.com/blog/why-do-we-charge-for-hallow-plus/) (**via search summary**), [learnofchrist](https://learnofchrist.com/resources/hallow), [psalmo](https://psalmo.app/blog/hallow-alternatives-free).

**Pray.com.** 7-day trial that converts to a $49.99 annual charge; Trustpilot and PissedConsumer reviews describe users who "played it once" and were charged, "no way on the screen to decline," and no obvious cancel path. This is the clearest **faith-context negative example** in the catalogue: the harm is magnified because the product is prayer. Sources: [Trustpilot](https://www.trustpilot.com/review/pray.com), [PissedConsumer](https://pray-com.pissedconsumer.com/review.html), [CancelFreely](https://cancelfreely.com/cancel/pray/).

**YouVersion (Bible App).** Fully free, nothing gated; a static "give" invitation inside the app and youversion.com/giving. Reaction: most reviewers note "no pop-ups, no spam"; a minority object to a $25/month ask ("not welcoming... turns off new born again Christians"). Source: [Trustpilot](https://ca.trustpilot.com/review/bible.com), [YouVersion giving](https://www.youversion.com/giving).

### 1.4 Publishing, reference, culture

**NYT.** Metered: 20/month (2011) → 10 (2012) → 5 (2017) → in recent years a registration wall plus a small, undisclosed meter. Signed-out readers get a hard "Create your free account or log in to continue reading" overlay (wording from general knowledge; **unverified wording**). Reaction: HN threads treat the wall as a reflex to route around, not an invitation. Sources: [TechCrunch 2011](https://techcrunch.com/2011/03/17/all-you-need-to-know-about-the-nytimes-com-paywall/amp/), [HN thread](https://news.ycombinator.com/item?id=29217342) (**via search summary**), [Poool on NYT](https://blog.poool.fr/the-new-york-times-paywall/).

**Medium.** Non-members get a small monthly allowance of member-only stories; wall copy "You've read all your free member-only stories this month." (**via search summary**). Writers can bypass it with Friend Links. Recent changes closed the cookie-clearing and private-window workarounds. Reaction: the wall is tolerated; the removal of workarounds is what prompted the "how to read for free" posts. Sources: [Medium blog](https://blog.medium.com/putting-writers-in-control-of-the-paywall-5247c9340055), [Medium help: Friend Links](https://help.medium.com/hc/en-us/articles/360006543813-Friend-Links), [ekky.dev](https://ekky.dev/blog/2026-06-21-how-to-read-medium-articles-for-free/) (**via search summary**).

**Substack.** The paywall is fixed copy publishers cannot change: a free preview, then "Keep reading with a 7-day free trial" and "Already a paid subscriber? Sign in." Writers choose where in the post the cut lands. Reaction: writers complain the cut is abrupt; readers accept it because the preview is real content and the terms are one line. Sources: [Substack support](https://support.substack.com/hc/en-us/articles/4418620510100-Can-I-add-a-free-trial-offer-to-a-paywall-on-my-post), [Carrie Loranger](https://thrivewithcarrie.substack.com/p/where-to-put-your-substack-paywall).

**The Guardian.** No paywall. An inline "epic" at the bottom of every article plus occasional banners; one-off or monthly contributions. The epic accounts for ~35% of US acquisitions; reader revenue grew from ~zero to over £100m with 1.3m supporters. The 2017 text: "Since you're here … we have a small favour to ask. More people are reading the Guardian than ever but far fewer are paying for it. And advertising revenues across the media are falling fast. So you can see why we need to ask for your help…" Reaction: widely copied; some critics call it "begging" or misleading about the Guardian's finances, but it is the most-praised **inline, non-interrupting** ask in the sector. Sources: [Press Gazette](https://pressgazette.co.uk/paywalls/why-the-guardian-is-no-longer-dependant-on-page-views-to-drive-revenue/), [INMA](https://www.inma.org/blogs/reader-revenue/post.cfm/the-guardian-bypasses-a-paywall-to-find-reader-support) (**via search summary**), [The Audiencers](https://theaudiencers.com/41-how-the-guardian-uses-messaging-to-ask-for-reader-support/) (**via search summary**), [AllSides critique](https://www.allsides.com/blog/guardian-s-misleading-fundraising-plea), [Nieman Lab 2024](https://www.niemanlab.org/2024/05/the-way-we-raise-the-money-at-the-guardian-is-different-than-any-place-ive-ever-been/).

**Wikipedia.** Free, banner-funded; banner frequency is capped (Track 1). The 2022 English Wikipedia RfC found banners "at least partly untruthful" and ruled out copy that implies Wikipedia's existence depends on donations, that readers should feel obliged, or percentages of non-donors ("98% of our readers don't give; they simply look the other way" was removed). Lines like "For the 2nd time recently, we interrupt your reading to humbly ask you to defend Wikipedia's independence" were cut. Testing found removing "humbly" made no significant difference. The 2024 banners still drew criticism for "it will soon be too late to help us." Reaction: a documented case where softer copy cost little. Sources: [2022 banners page](https://en.wikipedia.org/wiki/Wikipedia:Fundraising/2022_banners), [2024 banners page](https://en.wikipedia.org/wiki/Wikipedia:Fundraising/2024_banners), [Signpost 2022-11-28](https://en.wikipedia.org/wiki/Wikipedia:Wikipedia_Signpost/2022-11-28/News_and_notes), [Slate](https://slate.com/technology/2022/12/wikipedia-wikimedia-foundation-donate.html) (**via search summary**).

**Khan Academy.** Free; donation banners: "We're a nonprofit that relies on support from people like you." / "We'll get right to the point: Less than 1% of users give to Khan Academy." / "Khan Academy stays free thanks to donors like you. If you've learned here, your gift helps others do the same—with no ads, no paywalls, and no pressure." Note the "less than 1%" line is the same device Wikipedia's community rejected. Sources: [Khan donate](https://www.khanacademy.org/donate) (**via search summary**), [campaign pages](https://donate.khanacademy.org/campaign/749142/donate).

**Lichess.** Free forever, no ads, no subscriptions; donations from $5 to $250 one-off or monthly; donors get "Patron wings" on their profile and nothing functional. Copy: "Lichess is a free (really), libre, no-ads, open source chess server. The only income is donations, since we refuse subscriptions and advertisement." Reaction: praised as the purest "if you can and want to, give; if not, nothing changes" model. Sources: [Lichess patron](https://lichess.org/patron) (**via search summary**), [Lichess forum](https://lichess.org/forum/lichess-feedback/does-donating-give-you-a-benefit-or-no-just-to-get-those-cool-wings), [Raghav Rao](https://raghavrao.substack.com/p/lichess-forever-free).

**itch.io.** "$0 or donate" downloads show a pay-what-you-want sheet with a small text link "No thanks, just take me to the downloads." Developers report ~10% of players thought they had to pay and left (**via search summary** of the itch.io forum); the GitHub issue asks for the link to be styled as visibly as the pay button. Lesson: a decline path that is technically present but visually buried is read as a trick even when nobody meant it as one. Sources: [GitHub issue 481](https://github.com/itchio/itch.io/issues/481), [itch.io forum](https://itch.io/t/3567113/users-easily-miss-no-thanks-just-take-me-to-the-downloads).

**Gumroad.** PWYW with a suggested price pre-filled; a minimum floor enforced at checkout. Track 1 has the numbers (+8% sales, −65% average price without an anchor). Source: [insightraider](https://insightraider.com/en/answers/does-gumroad-let-you-offer-pay-what-you-want).

**Kindle / Audible samples.** Kindle: first ~10% free; the sample ends on a page offering purchase (a Quora thread complains that on some devices the "buy the whole book" button is missing — the end-of-sample page is the whole conversion mechanism, and its absence is noticed). Audible: ~5-minute samples that play inline. Neither interrupts the reader before the sample's natural end. Sources: [Authors On Mission](https://www.authorsonmission.com/how-do-kindle-samples-work/), [Quora](https://www.quora.com/How-come-when-I-finish-a-Kindle-free-sample-there-is-no-buy-the-whole-book-button) (**via search summary**).

**Wordle (NYT).** One puzzle per day, no replay, a countdown to the next one. Praised as the healthiest scarcity in consumer software: "daily puzzle games work because they end." The limit is the product. Sources: [UX Magazine](https://uxmag.com/articles/the-fascinating-psychology-tricks-that-make-wordle-so-addictive), [playdaily](https://playdaily.org/resources/stories/what-makes-great-daily-puzzle-game).

### 1.5 How generous, and how to tighten later

- Publishers started wide and tightened with data (NYT 20→10→5; Track 1). Perplexity and Poe tightened **silently** and paid for it in trust. Rule: tighten openly, with a date, and grandfather anyone mid-allowance.
- Kagi's 100 searches with no expiry shows a count-based allowance with no clock is accepted as generous even when the count is modest.
- Wikipedia's data: most donors give on impression 1–2; by impression 10 conversion is negligible (Track 1). The ask should be rare and well made, not repeated.
- Khan Academy and Hallow both keep a large permanently-free core and explain the charge in one public page. Both are cited as reasons people trust the paid part.

### 1.6 Abuse by clearing cookies

- Overby, Pattabhiramaiah and Kanuri (2025), clickstream from a major newspaper: a paywall encounter converts to a subscription about **0.21%** of the time; readers circumvent about **10%** of the time, typically with a fresh cookie from private browsing. Sources: [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5146366) (**via search summary**), [Notre Dame news](https://news.nd.edu/news/subscription-required-newspaper-paywalls-scatter-most-readers-but-provide-surprising-value/) (**via search summary**), [INMA](https://www.inma.org/blogs/reader-revenue/post.cfm/every-10th-paywall-stop-is-evaded-by-readers).
- Publishers' answer was to fuse the meter with registration (meter on the account, not the browser) and to add IP-level and fingerprint checks; the incognito trick "has lost much of its value" against server-side entitlement. Sources: [Fingerprint](https://fingerprint.com/blog/how-paywalls-work-paywall-protection-tutorial/), [pcrisk](https://www.pcrisk.com/blog/tips/14045-how-to-get-around-paywalls).
- Medium's recent closure of the cookie and private-window workarounds generated bypass guides but no measurable revolt, which suggests the fix is tolerated when the wall itself is modest.
- Practical reading for CiC: a 10% leak on a small anonymous allowance is a rounding error on cost; a motivated abuser will not be stopped by anything short of an account. Spend the engineering on account-bound metering and magic-link sign-in, not on fingerprinting.

---

## 2. The end-of-free moment — twelve-plus real examples

Each entry: timing, dismissibility, choices shown, price display, reassurance, decline wording, what is preserved, tone, and whether users praised or resented it.

### 2.1 Praised, or at least accepted

**E1. Guardian epic (inline, end of article).** Timing: after the reader has finished, never before or during. Dismissible by scrolling; no overlay. Choices: one-off or monthly, several amounts, "support from as little as £1" (**unverified wording**). Price in real money. Reassurance: the article stays open; nothing is withheld. Decline: none needed, it is just the page. Preserved: everything. Tone: "we have a small favour to ask," cost-reason framing (advertising revenue falling, journalism "takes a lot of time, money and hard work"). Evidence of success: 35% of US acquisitions, 1.3m supporters. Criticism: AllSides calls one version "misleading" about the Guardian's finances — the cost-reason must be true.

**E2. Wikipedia banner, post-RfC version.** Timing: on page load, top of page, capped number of impressions. Dismissible with an X. Choices: a grid of amounts with $2.75 suggested, one-time or monthly. Reassurance in the 2022 "day one" banner: "Most people don't give, and that's totally ok." Decline: X, and after a few impressions it stops. Preserved: the article. Tone that the community now permits: "like a library or a public park where we can all go to learn"; "donate $2, or whatever seems right." Praised line from a donor: "I'm not being beaten down to donate, I was just asked politely." Lines removed after criticism: "98% of our readers don't give," "we interrupt your reading to humbly ask," and "it will soon be too late to help us."

**E3. Kagi "trial ended."** Timing: at the 101st search, never earlier. Hard wall for search itself. Choices: three plans with prices and search counts. Reassurance: no card was ever taken; the 100 searches had no expiry; Fair Pricing promises unused months are credited. Tone: factual. Praised as honest in nearly every review found.

**E4. Midjourney "Fast hours used."** Timing: at the next job, after the last paid-speed job finished. Not a wall: the job runs anyway in Relax mode. Choice: "buy more Fast hours, $4/hour" on the account page; purchased hours never expire. Preserved: all images. Tone: neutral. Accepted because the only loss is speed.

**E5. ChatGPT model downgrade.** Timing: after the 10th message, mid-conversation, but the conversation continues on a smaller model. Nothing dismissed; a small note under the reply. Choice: "upgrade" link. Preserved: the conversation. Users rarely complain about this version; they complain about the opaque per-hour hard stop.

**E6. Claude reset-time notice.** Timing: at send, when the window is exhausted. Choices: wait or upgrade. The reset time is shown. Preserved: all chats. Tone: terse. The visible reset time is the praised element.

**E7. Wordle "Next Wordle in 13:42:07."** Timing: after the puzzle is solved or lost, on the result sheet. Choices: share, see stats. No purchase at all. Preserved: the result and the streak. Tone: celebratory and final. The countdown is the model for "come back on <date>" that people love rather than resent — because it is a promise, not a threat.

**E8. Headspace trial sheet after the first breath.** Timing: after the user has already done a breathing exercise. Modal with a close X. Choice: one plan, "14 days free, then $X/year," terms in full on the screen. Decline: X; the free basics course remains. Praised in teardowns for plain terms; resented in reviews when the trial converts without a reminder. The screen is good; the follow-through is the problem.

**E9. Substack paywall cut.** Timing: mid-post, at a point the writer chose. Inline, no overlay. Choice: "Keep reading with a 7-day free trial"; "Already a paid subscriber? Sign in." Preserved: the preview. Tone: one sentence, no pitch. Readers accept it because the preview was real.

**E10. Lichess Patron page (reached by choice, never pushed).** Timing: only when the user clicks "Patron" or "Donate." Choice: $5–$250 one-off, or monthly. Reassurance: "free (really)… no ads… we refuse subscriptions and advertisement." What the donor gets: wings on the profile, nothing functional. Praised precisely because it never interrupts.

**E11. Hallow "Why is there a subscription?"** Not a modal but a standing page linked from the paywall. States that most content is free forever, that one subscription is given away for every one sold, that clergy are free, and that anyone can request a scholarship. The existence of this page is what reviewers cite when they say the paid tier feels fair.

**E12. Zendesk / live-chat "Email transcript."** Timing: any time during or at the end of the chat, from a small menu. The conversation can be sent to the visitor's email by request or automatically when the chat ends. Not a paywall, but the standard pattern for "the visitor can keep what was said." Source: [Zendesk](https://support.zendesk.com/hc/en-us/articles/4408833687450).

### 2.2 Resented, with the evidence

**E13. Duolingo out-of-energy sheet.** Timing: mid-lesson, at the exact moment the bar hits zero, blocking the next question. Choices: a wait timer (hours), "watch an ad," spend gems, or "Try Super." Preserved: nothing of the interrupted lesson. Tone: cheerful mascot over a blocked task. Evidence: ~3,000-upvote Reddit thread; "punished for using the app"; coverage calling it "a paywall disguised as a feature." The specific resentments: the meter drains on **correct** answers, and the wall lands **mid-task**.

**E14. Candy Crush "You're out of lives."** Timing: on the fifth failure, blocking play. Choices: wait 30 minutes per life (2.5 hours for a full set), "Ask friends," or buy lives. Catalogued by DarkPattern.games and deceptive.design as "pay to skip" and as pop-ups that "display how much the player will lose if they stop." Tone: upbeat over a timer. Lesson: even a cheerful wall is a wall if it blocks the thing you were doing.

**E15. Character.AI waiting room.** Timing: on app open at peak. Not dismissible; "no clear timeline and no way to skip the line" except c.ai+. Resented chiefly because the stated wait is false.

**E16. Replika blurred-image upsell.** Timing: inside the conversation, in the character's voice. Tap opens a purchase sheet. Named in an FTC complaint as manipulative; users describe it as being "teased" to pay. The one example here that is directly about a conversational character, and the clearest "never do this" for CiC.

**E17. Pray.com trial screen.** Timing: at onboarding, before any value. Users report "no way on the screen to decline" and a $49.99 charge after 7 days. The faith-context magnifier: reviewers write that it "turns off new born again Christians and sinners alike."

**E18. itch.io donation sheet.** Timing: on "Download." Dismissible via a small grey link, "No thanks, just take me to the downloads." Resented not by players who saw the link but by the ~10% who did not, and by developers who lost those players. Lesson: the decline path must be as visible as the pay path.

**E19. Perplexity silent downgrade.** Timing: after the 5th Pro search, with **no message at all**; a worse answer simply arrives. Guides describe it as the most confusing part of the free tier. Lesson: the opposite failure from an aggressive wall — the honest thing is to say what changed.

**E20. Wikipedia pre-2022 banners.** "For the 2nd time recently, we interrupt your reading to humbly ask you to defend Wikipedia's independence"; "98% of our readers don't give; they simply look the other way." Found by the editing community to be "calculatedly manipulative" and partly untrue; now banned by RfC.

**E21. Calm trial-to-charge.** The trial sheet is fine; the charge a year later with no reminder is what reviewers call a trap. Not strictly an end-of-free modal, but the most common faith-adjacent and wellbeing-app complaint, and the reason one-time packs are an easier promise to keep.

### 2.3 Patterns across the catalogue

| Property | Praised examples | Resented examples |
|---|---|---|
| Timing | After a natural end (Guardian, Wordle, Kindle, Headspace-after-breath, Kagi at 101) | Mid-task (Duolingo, Candy Crush), on open (Pray.com, C.AI queue), in-character (Replika) |
| What is said | Reset time or "no expiry"; cost reason that is true | Nothing (Perplexity), a false wait (C.AI), a guilt line (old Wikipedia) |
| Decline | Scroll on; a plain X; a real button | A buried link (itch.io), none (Pray.com), confirmshaming |
| Preserved | Everything made so far | The interrupted lesson or game |
| Voice | The institution's, outside the content | The character's (Replika) |
| Price | Dollars, whole terms on screen | Points, unpublished packs (Suno), hidden renewal |

---

## 3. Evidence-based practice

### 3.1 Soft vs hard walls, interruption timing, warnings

- **Paywall encounters rarely convert and often scatter.** Overby et al. 2025: 0.21% subscribe at an encounter; ~10% circumvent; most leave. Pattabhiramaiah, Sriram and Manchanda (J. Marketing 2019): metered paywalls "might suppress usage among loyal consumers" — the meter bites the people you most want to keep. Chiou and Tucker 2013: Newsday lost ~34% of traffic the month after a hard wall. Sources: [SSRN 5146366](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5146366) (**via search summary**), [AMA summary](https://www.ama.org/2019/03/07/before-you-put-up-a-paywall-read-this-study/) (**via search summary**), [Pattabhiramaiah draft](https://www.scheller.gatech.edu/directory/research/marketing/pattabhiramaiah/pdf/draft_nytpaywall_r4_final.pdf), [Chiou & Tucker](https://www.sciencedirect.com/science/article/abs/pii/S0167624513000097).
- **Choice restriction beats quantity restriction** for conversion interest in an online experiment (ICIS 2020, LMU Munich): restricting *which* content is free (some always-free, some always-paid) outperformed a count meter, via reactance and reduced "fit uncertainty." For CiC this is an argument that "Family Tree always free, conversations paid" is the right kind of split, and that the free conversations should be complete rather than truncated so the visitor is not left uncertain what they would be buying. Source: [AISeL ICIS 2020](https://aisel.aisnet.org/icis2020/user_behaviors/user_behaviors/6/).
- **Interrupt at boundaries.** Bailey and Konstan: interruptions mid-task make primary tasks take 3–27% longer and produce about twice the errors compared with interruptions at task boundaries; Iqbal and Bailey's "Oasis" holds notifications until a natural breakpoint. The end of a conversation is a boundary; the middle of a reply is not. Sources: [Bailey & Konstan](https://interruptions.net/literature/Bailey-CHB06_1.pdf), [Iqbal & Bailey TOCHI 2008](https://www.interruptions.net/literature/Bailey-TOCHI08.pdf), [If not now, when?](https://www.researchgate.net/publication/221518227_If_not_now_when_The_effects_of_interruption_at_different_moments_within_task_execution).
- **Modals.** NN/g: users "dismiss modal overlays hastily as they assume nothing good will come of them"; a modal that appears when content loads "makes it look like the site is conditioning access to that content," which "diminishes credibility and trust." Their list of problematic trends includes stacked overlays, bad timing, and manipulative decline wording. Sources: [NN/g Popups](https://www.nngroup.com/articles/popups/) (**via search summary**), [NN/g Overlay Overload](https://www.nngroup.com/articles/overlay-overload/) (**via search summary**).
- **Warnings before the limit.** No controlled study found. Practice evidence: ChatGPT voice warns at 3 minutes left (Track 1); Claude shows reset time only at the wall; Perplexity's silent downgrade is the documented negative. Reasonable inference: one calm notice at the start of the last free unit ("this is your last free conversation for now") is better than a running counter (taxi-meter effect, Track 1) and better than no notice (Perplexity).

### 3.2 Anchoring, "best value," cost-reason framing

- **Middle-tier highlight.** Practitioner A/B aggregations: a "Most popular" badge lifted conversion in 64% of tests by ~27%; mid-tier adoption rose from 40–50% to 55–65%; strong visual differentiation beats subtle. Not peer-reviewed; direction is consistent with the decoy literature. Sources: [winsavvy](https://www.winsavvy.com/pricing-strategy-a-b-test-results-across-500-companies/), [mida.so](https://www.mida.so/blog/ab-testing-pricing-pages). Ethical line: a badge that reports a true fact ("most people choose this") is persuasion; a decoy priced to be a bad deal, or a badge on a tier no one actually picks, is a dark pattern under both the FTC's and CMA's taxonomies.
- **Cost-reason framing is the ethical lever with the most evidence.** Buell and colleagues: operational transparency (showing the work) raises perceived effort, gratitude and willingness to pay; "Lifting the Veil" (Mohan, Buell, John): cost transparency raised purchase interest. Stangl, Kastner and Natter 2026 (Track 1): cost-structure appeals raise fairness and payments. Caveat from Buell: it backfires if the process shown looks sloppy. Sources: [Buell, Management Science 2017](https://ideas.repec.org/a/inm/ormsc/v63y2017i6p1673-1695.html), [Lifting the Veil](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2498174) (**via search summary**), [thinkinsights](https://thinkinsights.net/insights/what-operational-transparency).
- **Dark patterns work, and mild ones are the dangerous ones.** Luguri and Strahilevitz (J. Legal Analysis 2021): mild dark patterns more than doubled acceptance of a product; aggressive ones nearly quadrupled it but "generated a powerful backlash," while mild ones did not; less-educated subjects were more susceptible. Confirmshaming ("No thanks, I don't want to save money") is the Mathur et al. 2019 category most relevant to a decline button. Sources: [Luguri & Strahilevitz](https://academic.oup.com/jla/article/13/1/43/6180579), [Mathur et al.](https://arxiv.org/pdf/1907.07032).

### 3.3 Mission-driven and faith contexts

- **Wikipedia's RfC** is the only case found where a community wrote down what counts as manipulative in a mission ask and tested the cost of removing it: no "existence depends on you," no non-donor percentages, no obligation framing; removing "humbly" made no significant difference to donations. This is the closest thing to an evidence-based style guide for CiC's register.
- **Public radio**: 52% of listeners reduce or stop listening during pledge drives; stations found they could shorten drives without losing revenue by moving asks to mail and short reminder spots, and some offer a "pledge-free stream" to members. The lesson: the ask does not need to interrupt the content to work. Sources: [Current.org](https://current.org/wp-content/uploads/archive-site/funding/funding0506pledge.shtml), [Current.org 2018](https://current.org/2018/09/ohio-station-gives-listeners-a-way-to-escape-pledge-drive/).
- **Church giving platforms**: Tithe.ly and Pushpay use pre-filled amounts, a "cover the fees" checkbox (50–60% opt in; often checked by default), and Pushpay's "Recurring Suggestion" nudges one-time givers whose pattern "looks like" recurring toward a schedule, with a dashboard of "who still needs a nudge." Faith+Lead's "stewardship trap" piece and others warn that scripture-as-guilt is manipulation even with good intent. Sources: [churchstack](https://www.churchstack.io/blog/online-giving-platforms-churches-comparison), [Stablish](https://www.stablish.io/resources/best-church-giving-software-2026), [Faith+Lead](https://faithlead.org/blog/the-stewardship-trap/).
- **What feels manipulative in a faith context specifically** (from the Pray.com, Hallow, YouVersion and Replika evidence): a charge that arrives without warning after prayer content; an ask that implies the free participant is less serious; a character or sacred text used as the voice of the ask; a default-checked extra; any suggestion that paying changes one's standing. The YouVersion comment ("not welcoming... to new born again Christians") shows that even a plain $25/month ask can read as a barrier to the people a faith product most wants.
- **Hallow's positive pattern** (give-one-get-one, clergy free, scholarship request, public "why we charge") is the faith-sector precedent for making a paid tier feel like a gift economy rather than a toll.

### 3.4 Regulation relevant to checkout design

- **FTC.** "Bringing Dark Patterns to Light" (2022) names confirmshaming, false urgency, drip pricing, pre-checked boxes and obstructed cancellation (Track 1). The Junk Fees Rule (effective May 12, 2025) requires the "total price" up front, but its scope is live-event tickets and short-term lodging only; the principle is still the FTC's stated expectation. Amazon settled the Prime "Iliad" case for $2.5bn in September 2025 ($1bn penalty, $1.5bn refunds) over deceptive enrollment and cancellation. A one-time pack has no enrollment or cancellation, which removes the whole ROSCA/negative-option exposure. Sources: [FTC press release](https://www.ftc.gov/news-events/news/press-releases/2024/12/federal-trade-commission-announces-bipartisan-rule-banning-junk-ticket-hotel-fees), [NatLawReview](https://natlawreview.com/article/ftc-finalizes-junk-fees-rule-new-pricing-disclosure-requirements-take-effect-may-12), [MediaPost on Amazon](https://www.mediapost.com/publications/article/409399/amazon-settles-dark-patterns-charges-for-25-bi.html).
- **UK.** The CMA's Online Choice Architecture paper (2022) treats drip pricing, sludge, dark nudges, decoys and choice overload as "almost always harmful"; the DMCC Act 2024 gives the CMA direct fining powers; drip pricing and fake urgency are its stated first targets (April 2025), with investigations opened in November 2025. Sources: [Sidley April 2025](https://www.sidley.com/en/insights/newsupdates/2025/04/new-uk-consumer-rules-herald-stricter-enforcement-and-significant-fines), [Sidley Nov 2025](https://www.sidley.com/en/insights/newsupdates/2025/11/uk--competition-and-markets-authority-opens-investigations-into-online-pricing-practices), [CMS](https://cms-lawnow.com/en/ealerts/2025/03/tangled-web-uk-regulators-crack-down-on-harmful-online-choice-architecture).
- **EU.** DSA Article 25 bans interfaces that "deceive or manipulate" or "materially distort" free decisions (platforms); the Commission has not yet issued Article 25 guidelines. The Digital Fairness Act proposal is now expected in Q4 2026 (not yet tabled as of September 2026), targeting dark patterns, addictive design, personalisation and subscription traps; enforcement unlikely before 2028. Virtual-currency principles from the CPC network (Track 1) already apply. Sources: [EP legislative train](https://www.europarl.europa.eu/legislative-train/theme-protecting-our-democracy-upholding-our-values/file-digital-fairness-act), [Privacy Laws](https://www.privacylaws.com/news/eu-proposal-on-digital-fairness-act-expected-by-the-end-of-2026/), [Osborne Clarke](https://www.osborneclarke.com/insights/digital-fairness-act-unpacked-dark-patterns).

---

## 4. Alternatives to a pop-up for the same moment

**A1. Inline end-of-conversation card (Guardian pattern).** When the final free conversation reaches its natural close, the Representative's last reply is followed by a Facilitator card in the thread itself — no overlay, nothing blocked. It states the situation, offers packs and support, and can be scrolled past. Examples: Guardian epic; Substack's inline cut; the Kindle end-of-sample page. Strength: cannot interrupt, cannot be "accidentally dismissed" (an NN/g complaint), reads as part of the experience. Weakness: lower conversion per view than a modal in publisher data; easy to miss if the participant leaves before scrolling.

**A2. A "closing page" summary with the offer.** Ending a conversation already needs a close (Wordle's result sheet, Duolingo's lesson-complete screen, Headspace's session-complete). The closing page can show what the participant just did (the tradition, the questions asked, a line or two they marked), offer "save or email this conversation," and below that the purchase and support options. Examples: Wordle result sheet (no purchase); Duolingo places its only ads and upsells on the lesson-complete screen; Kindle end-of-sample page. Strength: the ask sits at a task boundary (Bailey and Konstan), and the summary gives the participant something before asking for anything. Weakness: needs a real closing-page design regardless of billing; must not become a "congratulations, now pay" screen.

**A3. "Email me a link" / keep what you made.** Offer to send the finished conversation, or a resume link, to an email address — for anonymous visitors this doubles as the lightest possible registration (Perplexity's magic link; Zendesk's "email transcript"). Perplexity also sets a precedent for honesty about retention: anonymous threads are kept 14 days then deleted, and the help page says so. Strength: solves "can I keep this?" and account creation in one step; no password. Weakness: must be real email, promptly delivered, with no marketing attached, or it becomes a lead-capture trick.

**A4. A gentle "come back on <date>" path.** Show the refresh date plainly, with no countdown clock ticking on screen: "Your next free conversation is ready on Tuesday 7 October." Examples: Claude's reset time (praised), Wordle's next-puzzle promise (loved), Poe's "renew tomorrow." Strength: converts the limit from a wall into a promise; costs nothing. Weakness: trains some users to wait rather than pay (Track 1); but for a reflective product, waiting is not a failure state.

**A5. A donor-supported "sponsored conversation" lane.** Let supporters pre-pay conversations for strangers, and let a visitor at the limit take one "given by someone who has been here before" — the suspended-coffee tradition (caffè sospeso; A Cup of Common Wealth's website-to-chalkboard model; 15m+ coffees via one Facebook movement). Faith-sector precedent: Hallow's give-one-get-one and scholarship request; Khan Academy's Learners Fund; Lichess Patron. Strength: fits a church-shaped product better than any discount; gives supporters a concrete thing their money did; gives the limit screen a third option that is neither pay nor leave. Weakness: needs a simple fairness rule (one sponsored conversation per person per period), honest accounting, and copy that never implies the taker is a charity case. Sources: [caffè sospeso](https://en.wikipedia.org/wiki/Caff%C3%A8_sospeso), [Schedulefly on A Cup of Common Wealth](https://schedulefly.substack.com/p/from-a-coffee-shop-chalkboard-to), [KCUR](https://www.kcur.org/2015-12-17/movement-to-pay-it-forward-with-a-cup-of-coffee-spills-into-u-s).

**A6. Degrade instead of stop (for reference, probably not for CiC).** ChatGPT's smaller model, Midjourney's Relax mode, Perplexity's basic search. It is the least-resented limit in AI products, but for CiC a "cheaper Representative" would be a fidelity defect, so the only honest degrade is a shorter conversation cap, not a worse voice.

---

## 5. Design directions for CiC's end-of-free moment

All copy below is **DRAFT** and illustrative. It is written in the Facilitator's register (plain, adult, outside every world), aims at B2 / grade 8–10, and uses no countdowns, no guilt, no urgency, and no assistant cadence. Names in brackets are placeholders; pack sizes and prices are deliberately not proposed. "[Tradition]" stands for whichever world was in conversation. Nothing here asserts a fact about CiC beyond the brief.

### D1. The Closing Card (inline, in the thread)

Layout: after the Representative's final reply of the last free conversation, a card in the Facilitator's visual style (clearly not a Representative bubble). No overlay. Three elements stacked: a status line, a short reason, two buttons and one text link. Below the card, the conversation remains fully readable and can be saved.

DRAFT copy:
> **This conversation is complete, and it was your last free one for now.**
> Your next free conversation is ready on [date]. Everything you talked about here is saved.
> Each conversation runs on real computing and on years of work with the sources. If you would like to keep going before [date], you can pay for more conversations, one time, nothing recurring.
> [See conversations and prices]  [Save this conversation]
> Or come back on [date]. There is no hurry.

Trade-offs: least interruptive; lowest risk of feeling like a trap; cannot be mis-dismissed; probably the lowest conversion per view; depends on the participant scrolling to the end.

### D2. The Closing Page (a full "end of conversation" screen)

Layout: a page that every conversation ends on, free or paid. Top: the tradition's name and the handful of questions the participant asked (from the transcript, not generated). Middle: "Save" and "Email me this conversation." Bottom: the allowance status and, only when relevant, the purchase and support options as two quiet rows. The page is the same for paid users; the bottom block changes.

DRAFT copy:
> **You spoke with [Tradition] about [first question, shortened].**
> [Save]  [Email me this conversation]
> ---
> That was your last free conversation for now. The next one is free on [date].
> **If you want to continue sooner:** conversations can be bought one at a time or in small sets. They never expire. If a reply ever fails, you are not charged for it.
> [See prices]
> **If you want to support the work instead, or as well:** [Support the project]

Trade-offs: gives before asking; sits at a true task boundary; works for anonymous and signed-in alike; needs real design effort on the summary; risk that the summary looks like a report card.

### D3. The Threshold Sheet (a dismissible sheet at the start of the next conversation)

Layout: nothing happens at the end of the last free conversation except the normal close. When the participant taps "Start a conversation" after the allowance is used, a bottom sheet (mobile) or centred panel (desktop) appears with a plain X and an equally weighted "Not now" button. Packs shown as three rows, dollars and per-conversation price, no badge unless it reports a true "most chosen."

DRAFT copy:
> **Your free conversations are used for now.**
> They come back on [date]. Your past conversations are saved and you can read them any time.
> **Conversations to buy** — one-time, never expire, no subscription.
> [N conversations — $X ($Y each)]
> [N conversations — $X ($Y each)]
> [N conversations — $X ($Y each)]
> A failed or interrupted reply never uses one up.
> [Not now]   [Support the project without buying]

Trade-offs: the cleanest separation between the conversation (never touched) and the commerce (only when the person reaches for more); the familiar "wall" shape, so it must be clearly dismissible; a modal still carries NN/g's "conditioning access" smell even when honest.

### D4. The Quiet Ledger (always-visible status, no event at all)

Layout: a small, permanent line in the header or the conversation list: "Free conversations: 1 left — next one free on [date]" that becomes "0 left — next one free on [date] · Buy more · Support." The end of the last free conversation triggers nothing; the start of the next just shows the same line, and the "Start" button becomes "Buy a conversation" or "Come back on [date]." No modal, no card.

DRAFT copy (header line):
> Free conversations: 0 until [date] · [Buy more] · [Support]

Trade-offs: zero interruption; most honest about the meter; but a visible counter runs into the taxi-meter effect during the conversation; the ask is so quiet that many will never notice it; strongest fit for signed-in participants who return often.

### D5. The Sponsored Seat (a third door on the limit screen)

Layout: D1, D2 or D3, plus one extra option — "Take a conversation someone has paid forward" — available once per period per person, with a line explaining where it came from. The support lane on every variant then has a matching "Pay a conversation forward" option, with a running public count ("[n] conversations waiting to be taken") that is real.

DRAFT copy (extra block):
> **Someone has paid a conversation forward.** Supporters sometimes buy conversations for people they will never meet. There are [n] waiting. You can take one now; it asks nothing of you.
> [Take a sponsored conversation]
> Later, if you want, you can pay one forward too.

Trade-offs: the most distinctive and the most church-shaped; turns the support lane into something concrete; risks feeling like charity if the copy slips; needs a fairness rule and honest counts; the hardest to build well.

### D6. The Degrade-to-Shorter (reference option)

Layout: instead of stopping, a used-up free allowance allows one more conversation with a lower internal turn cap, announced plainly at the start ("This conversation has room for about [n] exchanges"). The purchase sheet appears only at that conversation's end.

Trade-offs: least likely to send anyone away; the voice is never degraded, only the length; but it blurs the meaning of "free conversations," complicates the ledger, and may be read as a half-measure.

---

## 6. Ranked recommendation (input to Mark's decision, not the decision)

1. **D2 + D3 together** (closing page as the ordinary end of every conversation; threshold sheet only when someone reaches for more after the allowance is used). Confidence: moderate-high on the shape. It puts the ask at a task boundary, never inside the conversation, gives something (the summary, save, email) before asking, keeps the commerce out of the thread, and makes the decline path a first-class button. It is the intersection of the praised examples (Guardian, Wordle, Headspace-after-breath, Kagi) and avoids every named failure (mid-task, silent, in-character, buried decline).
2. **D1** if the closing page proves too heavy to build first. Confidence: moderate. Lowest risk, lowest conversion.
3. **D5** as a second-phase addition to whichever shape is chosen. Confidence: moderate on fit, low on build cost. It is the option most likely to be remembered and talked about, and the one most consistent with a mission-driven, church-shaped project.
4. **D4** as a complement for signed-in users, not as the main mechanism.
5. **D6** only if pilot data shows people leave rather than wait or pay.

Rules that should hold under any direction (all drawn from the evidence above): the Representative never speaks the ask; one calm notice at the start of the last free conversation, no running counter; the refresh date stated as a plain date, no clock; dollars and per-conversation price; "never expire" and "a failed reply never counts" stated on the screen; "Not now" as a real button, never a grey link; no pre-checked anything; no badge that is not a true fact; the support lane always separate from the packs and never the only path; no copy that touches the participant's seriousness or standing.

Uncertainties: (a) no study found on warnings-before-limit specifically, so "one calm notice" is inference; (b) the sponsored-seat model has no digital precedent at scale beyond coffee and Hallow's opaque give-one-get-one, so its fairness rules are untested; (c) conversion data for inline cards versus sheets comes from news publishers, not reflective products; (d) several primary pages (Hallow, Lichess, Claude support, NN/g) were read via search summaries and should be re-checked before anyone quotes them.

---

## Appendix: additional sources used in this round (accessed 2026-10-02)

AI products: byteplus; OpenAI community; meetaitools; How-To Geek; ghacks; ai-toolbox; datastudios; heyuan110; claudemarket; fast.io (Perplexity); aiqnahub; Android Authority; perplexityaimagazine; roborhythms; Character.AI c.ai+ FAQ; TechCrunch and Axios (Pi); Poe FAQ (summary); eesel and nexodatech (Notion AI); Kagi blog, Tim Hårek, Android Police; eesel and stacksheriff and Trustpilot (Suno); aituts, aiarty, ponr (Midjourney); ElevenLabs changelog.

Learning and wellbeing: techissuestoday, Class Central, toptechguides, MarketBeat (Duolingo); dev.to paywallpro, growth.design, choosingtherapy, unstar (Headspace/Calm); Hallow blog (summary), learnofchrist, psalmo; Trustpilot, PissedConsumer, CancelFreely (Pray.com); Trustpilot bible.com, YouVersion giving; khanmigo.ai, Khan support.

Publishing and mission: TechCrunch 2011, HN, Poool (NYT); Medium blog and help, ekky.dev; Substack support, Carrie Loranger; Press Gazette, INMA, The Audiencers, AllSides, Nieman Lab (Guardian); Wikipedia Fundraising 2022 and 2024 banner pages, Signpost, Slate; Khan Academy donate pages; Lichess patron and forums, Raghav Rao; itch.io GitHub issue 481 and forum; insightraider (Gumroad); Authors On Mission, Quora (Kindle); UX Magazine, playdaily (Wordle); Zendesk transcripts.

Evidence: SSRN 5146366, Notre Dame, INMA (Overby et al.); AMA, Scheller draft (Pattabhiramaiah); ScienceDirect (Chiou & Tucker); AISeL ICIS 2020 (paywall configurations); interruptions.net (Bailey, Konstan, Iqbal); NN/g Popups and Overlay Overload (summaries); winsavvy, mida.so (badges); Buell (Management Science 2017), Mohan/Buell/John (SSRN), thinkinsights; Luguri & Strahilevitz (JLA 2021); Mathur et al. (arXiv 1907.07032); Current.org (pledge drives); churchstack, Stablish, Faith+Lead (church giving); TIME, Tech Justice Law Project, Suffolk JHBL (Replika); DarkPattern.games, deceptive.design, diva-portal (Candy Crush); Forbes/Tassi, Deconstructor of Fun (Marvel Snap).

Regulation: FTC press release and Federal Register (Junk Fees Rule); NatLawReview; MediaPost, Truth on the Market (Amazon settlement); Sidley (April and Nov 2025), CMS, Lexology (CMA/DMCCA); EP legislative train, Privacy Laws, Osborne Clarke, ACM DL (DSA Art. 25, DFA).
