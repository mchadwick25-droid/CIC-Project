# Persona/voice data structures in shipping systems — verified field inventories

Every field name below was read from the live spec, doc page, or paper on 2026-07-25. Note: this survey covers topics 1, 2, 3, 5, and 6 of the original brief in full; topic 4 (game/interactive-fiction narrative design) was still running when this was compiled and should be treated as a minor addendum if it lands separately.

---

## 1. Character Card format (V1 → V2 → V3) — the deepest hit

### 1a. The card fields

**V1** ([spec_v1.md](https://github.com/malfoyslastname/character-card-spec-v2/blob/main/spec_v1.md)) defines six fields, and the normative language is the important part:

| Field | Spec's own wording |
|---|---|
| `name` | "Used to identify a character." |
| `description` | "Description of the character. **SHOULD** be included by default in every prompt." |
| `personality` | "A short summary of the character's personality. **SHOULD** be included by default in every prompt." |
| `scenario` | "The current context and circumstances to the conversation. **SHOULD** be included by default in every prompt." |
| `first_mes` | "First message sent by the chatbot, also known as 'greeting.'" |
| `mes_example` | "Example conversations… **SHOULD**, by default, only be included in the prompt until actual conversation fills up the context size, and then be **pruned** to make room for actual conversation history." Uses a `<START>` separator that "marks the beginning of a new conversation and **MAY** be transformed (e.g. into an OpenAI System message)." |

**This is the single most load-bearing architectural distinction in the whole format**: description/personality/scenario are *permanent* prompt residents; example dialogue is *ephemeral* and is the first thing evicted. SillyTavern's docs restate it as "Permanent tokens" (Name, Description, Personality, Scenario) versus non-permanent (first message, examples) — [characterdesign](https://docs.sillytavern.app/usage/core-concepts/characterdesign/).

**V2** ([spec_v2.md](https://github.com/malfoyslastname/character-card-spec-v2/blob/main/spec_v2.md)) wraps V1 in `{spec: 'chara_card_v2', spec_version: '2.0', data: {...}}` and adds:

```ts
creator_notes: string              // "never included in the prompts"; MUST NOT be used inside prompts
system_prompt: string              // overrides the user's global system prompt; supports {{original}}
post_history_instructions: string  // injected AFTER conversation history; overrides user "jailbreak" setting
alternate_greetings: Array<string> // each becomes a "swipe" on the first message
character_book?: CharacterBook     // "A character-specific lorebook."
tags: Array<string>                // "SHOULD NOT be used in prompt engineering"
creator: string                    // MUST NOT be used for prompt engineering
character_version: string          // MUST NOT be used for prompt engineering
extensions: Record<string, any>    // MUST default to {}; namespace your keys
```

Two design notes worth extracting. First, `post_history_instructions` exists because instructions placed *after* the conversation have "much stronger weight on current models' generations than instructions written before the conversation history" — position is treated as a first-class field property, not an implementation detail. Second, the spec explicitly separates **prompt-bearing fields** from **human-facing metadata fields** with MUST NOT language. That separation is cheap to copy and it is the thing most homegrown schemas get wrong.

**V3** ([SPEC_V3.md](https://github.com/kwaroran/character-card-spec-v3/blob/main/SPEC_V3.md)) keeps all of the above and adds `assets[] {type, uri, name, ext}`, `nickname`, `creator_notes_multilingual`, `source: string[]`, `group_only_greetings`, `creation_date`, `modification_date`. Note `source` — provenance made a first-class card field.

### 1b. `character_book` — the keyword-triggered knowledge injection system

This is the part that matters most for CiC. Full V2 structure:

```ts
type CharacterBook = {
  name?, description?, extensions
  scan_depth?: number         // how many recent messages are scanned for keys
  token_budget?: number       // ceiling on tokens all activated entries may consume
  recursive_scanning?: boolean // "whether entry content can trigger other entries"
  entries: Array<{
    keys: Array<string>        // trigger keywords
    content: string            // what gets injected
    enabled: boolean
    insertion_order: number    // "lower insertion order = inserted higher"
    priority?: number          // "if token budget reached, lower priority value = discarded first"
    selective?: boolean        // "require a key from BOTH keys and secondary_keys to trigger"
    secondary_keys?: Array<string>
    constant?: boolean         // "if true, always inserted in the prompt (within budget limit)"
    case_sensitive?: boolean
    position?: 'before_char' | 'after_char'
    name?, id?, comment?       // all three: "not used in prompt engineering"
    extensions
  }>
}
```

V3 adds `use_regex: boolean` to entries and moves advanced behavior into **`@@decorators`** written inline at the top of the entry's `content` field. Rationale, verbatim: "Decorators are made for core users to make advanced prompts, without needing to make a new field." Decorators cascade — `@@` is the primary, `@@@` lines are fallbacks if the app doesn't support it. The full set includes `@@activate_only_after N`, `@@activate_only_every N`, `@@keep_activate_after_match`, `@@dont_activate_after_match`, `@@depth N`, `@@reverse_depth`, `@@instruct_depth`, `@@role assistant|system|user`, `@@scan_depth N`, `@@is_greeting N`, `@@position after_desc|before_desc|personality|scenario`, `@@ignore_on_max_context`, `@@additional_keys`, `@@exclude_keys`, `@@activate` / `@@dont_activate`.

### 1c. Scope: character books versus world books

V2 spec, verbatim: **"Character lorebook SHOULD stack with user 'world book'/'world info'/'memory book'. (Character book SHOULD take full precedence over world book.)"** The rationale given for embedding one at all is purely distribution friction: "the extra effort required for users to download and import external worldbooks turns them away."

SillyTavern implements four distinct lorebook scopes ([World Info docs](https://docs.sillytavern.app/usage/core-concepts/worldinfo/)): **Character Lore** (embedded, exports with the card), **Persona Lorebook** (activates when a given user-persona is selected), **Chat Lorebook** (this conversation only), and **global World Info** (standalone, world-scoped, shared across every character in that world). The ecosystem already separates *world knowledge* from *speaker identity* at the schema level.

### 1d. SillyTavern's production superset of the entry schema

The shipping implementation has considerably more machinery than the spec, and several of these are directly relevant:

- **Entry types**: 🔵 Constant ("does not need any keywords, and will trigger regardless"), 🟢 Normal ("triggered only in the presence of the keyword"), 🔗 **Vectorized** ("allowed to be inserted by embedding similarity"). Keyword and embedding retrieval coexist as per-entry choices.
- **Optional Filter** with explicit logic modes: **AND ANY / AND ALL / NOT ANY / NOT ALL**. Keys support JS regex.
- **Insertion Position**: Before Char Defs, After Char Defs, Before Example Messages, After Example Messages, Top of AN, Bottom of AN, **@ D (Depth)** with a selectable **system / user / assistant role**, and **Outlet** ("not injected automatically… stored under a named outlet" retrieved via `{{outlet::Name}}`).
- **Inclusion Group** + **Group Weight** + **Prioritize Inclusion** + **Use Group Scoring** — mutual-exclusion sets so competing entries don't all fire.
- **Timed effects**: **Sticky** ("stays active for N messages after being activated"), **Cooldown**, **Delay**.
- **Recursion control**: **Non-recursable**, **Prevent Further Recursion**, **Delay Until Recursion**, **Recursion Level**, **Max Recursion Steps**.
- **Probability / Trigger %**, **Min Activations**, **Max Depth**, **Additional Matching Sources** (scan the character description, personality, scenario, persona description, creator's notes — not only chat).

Community authoring convention worth noting from the [World Info Encyclopedia](https://rentry.co/world-info-encyclopedia): entries are paired — a factual description block **plus** an example of how the speaker talks *about* that lore entry, stored in the same entry. Keys are chosen by asking "what would someone use to trigger injection of this pair," favoring general association terms over exact names.

### Verdicts — character card format

| Element | Verdict |
|---|---|
| The permanent-fields / evicted-examples split | **TRANSFERS CLEANLY.** Pure prompt economics. Forces the question "what must always be present for the world to sound like itself." |
| Prompt-bearing vs. MUST-NOT-prompt metadata separation | **TRANSFERS CLEANLY.** |
| `system_prompt` / `post_history_instructions` (position as a field property) | **TRANSFERS CLEANLY.** |
| `first_mes` / `alternate_greetings` / `group_only_greetings` | **TRANSFERS CLEANLY.** A world can open in several registers. |
| `mes_example` with `<START>` blocks | **TRANSFERS CLEANLY.** The `<START>` convention exists precisely so examples read as *a* conversation rather than *the* conversation — no individual biography implied. |
| **The entire `character_book` / World Info entry schema** | **TRANSFERS CLEANLY, and is the closest existing analogue to what CiC needs.** Nothing in keys/content/selective/secondary_keys/constant/position/insertion_order/priority/scan_depth/token_budget/recursion/inclusion-groups/sticky/cooldown assumes an individual. The whole subsystem is already *world* knowledge, not *person* knowledge — its name in every implementation is "World Info." |
| `character_book` embedded vs. global world book | **TRANSFERS CLEANLY** as a scoping question; the four-scope model (world / representative / session / participant) maps directly. |
| `name`, `nickname`, `personality` | **NEEDS ADAPTATION.** `personality` as "a short summary of the character's personality" has to become a description of the world's collective disposition and register, with no person behind it. `name` is the world's name. |
| `description` | **NEEDS ADAPTATION.** In practice this field holds biography in nearly every published card. The slot is fine; the conventional contents are exactly what CiC rules out. |
| `assets` (icon, background, emotion sprites, inlay) | **DOESN'T APPLY** as specified — emotion sprites are per-individual affect states. |
| `scenario` | **NEEDS ADAPTATION.** "Current context and circumstances to the conversation" is workable for a world (the historical situation being spoken from); it becomes a problem only if used to stage a personal situation. |

Community sub-formats are also worth naming because they are exactly the axis CiC is choosing on: **PList** (bracketed trait lists), **W++**, **Boostyle** — all attribute-list styles — versus **[Ali:Chat](https://rentry.co/alichat)**, whose stated principle is "using dialogue as the formatting to express and reinforce traits/characteristics," on the claim that "characters' attributes/traits can be implicit — the way they talk & act, the situation & environment." The dominant community recommendation is to combine them: PList for the fact, Ali:Chat for the demonstration. **NEEDS ADAPTATION** — Ali:Chat's mechanic (demonstrate the trait in speech) transfers; its habit of demonstrating *personal* traits does not.

---

## 2. Character.AI

### 2a. The documented character attribute set

From [book.character.ai](https://book.character.ai/) (llms.txt index + attribute pages):

| Field | Limit | Documented purpose |
|---|---|---|
| **Name** | 3–20 chars | "The name the Character will use in Chat" |
| **Greeting** | 0–500 chars | "The first thing your Character will say when starting a new conversation" |
| **Short Description** | 0–50 chars | "How would your Character describe themselves?" |
| **Long Description** | 0–500 chars | "A few sentences up to a paragraph that gives more detail" |
| **Definition** | **0–32,000 chars** | "A large, free-form field that can contain structured example dialogs or any text content" |
| **Suggested Starters** | — | user-facing conversation openers |
| **Example Conversations** | — | display-only; "will appear on the Character Profile page for other users" |
| Avatar, Voice, Categories (max 3), Visibility, Remixing & Definition Visibility, Image Generation, Image Style | — | metadata / rendering |

Notice the proportions: 500 characters for description, **32,000 for the Definition**, which is overwhelmingly example dialogue. The documented format is "a name followed by a colon (:) followed by the message," with reserved macros `{{char}}`, `{{user}}`, `{{random_user_1}}`, `{{random_user_2}}` — the random-user macros exist so demonstrations read as *representative* exchanges rather than a specific relationship. Ordering guidance, verbatim: "If you have a long Definition, put the most important parts of your Definition at the beginning. As your conversation increases in length, the end of your Definition may be truncated."

Two precision points: **Example Conversations is a profile-display artifact, not prompt input** — do not conflate it with Definition. And Character.AI's own hedge, verbatim: "Sometimes, for some Characters, less can be more… giving the system just a creative greeting… may actually produce better results than a carefully crafted Definition."

Their **Negative Guidance** page does not offer a "never say" field. The documented technique is to stage a scenario in which refusal is in character — an actor who redirects off-topic questions — rather than to state prohibitions.

**User Personas** are a separate object: users write them "first person," "by category" (Name, Gender, Age, Height, Hair, Eye Color, Personality, Likes, Dislikes, Talents), or "third person," and can set one as "Default for all chats" or vary per chat.

### 2b. The actual engineering data model

[Prompt Design at Character.AI](https://blog.character.ai/prompt-design-at-character-ai/) and [Prompt Poet](https://github.com/character-ai/prompt-poet) are the real schema. Prompts are assembled from "current conversation modalities, ongoing experiments, the Characters involved, chat types, various user attributes, **pinned memories**, **user personas**, the entire conversation history and more" via Jinja2 → YAML. Each rendered **part** carries:

- **Name** — "a clear, human-readable identifier for the part"
- **Content** — "the actual string payload"
- **Role** (optional) — system / user / assistant
- **Truncation Priority** (optional) — "determines the order of truncation when necessary, with parts having the same priority being truncated in the order in which they appear"
- **Sections** (optional) — nested parts for granular token accounting

Plus **cache-aware truncation**: "truncates up to the same fixed truncation point for every k turns," reported at a 95% prefix-cache rate.

### Verdicts — Character.AI

- **The name/content/role/truncation_priority part schema: TRANSFERS CLEANLY.** This is the most reusable thing in their stack and it is entirely persona-agnostic — it's a prompt-assembly contract. It independently confirms the character-card lesson: *every* piece of persona material carries an explicit eviction rank.
- **The 500-vs-32,000 character allocation: TRANSFERS CLEANLY as a signal.** The platform with the most persona-conversation volume in the world gives description 1.5% of the budget it gives demonstration.
- **`{{random_user_N}}` macro: TRANSFERS CLEANLY**, and is a genuinely useful trick — it keeps sample exchanges generic rather than binding them to a named relationship.
- **Short/Long Description ("How would your Character describe themselves?"): NEEDS ADAPTATION.** Self-description framing presumes a self.
- **Negative Guidance approach: NEEDS ADAPTATION.** The technique (stage the refusal in-world rather than list prohibitions) transfers; their specific staging device is an individual actor holding a role.
- **Voice, Avatar, Image Style, emotion rendering: DOESN'T APPLY.**
- **User Personas: TRANSFERS CLEANLY** — that's the participant, not the Representative.

---

## 3. Academic persona-grounded dialogue

### 3a. PersonaChat (Zhang et al., ACL 2018) — [paper](https://aclanthology.org/P18-1205/) / [arXiv](https://arxiv.org/abs/1801.07243)

Hard numbers, verbatim:

- Workers were asked to "create a character (persona) description using **5 sentences**."
- "We asked the workers to make each sentence short, with a **maximum of 15 words per sentence**."
- "We crowdsource a set of **1155 possible personas**, each consisting of **at least 5 profile sentences**, setting aside 100 never seen before personas for validation, and 100 for test."
- "This resulted in a dataset of **162,064 utterances over 10,907 dialogs**."
- Example persona (Table 1): "I love the beach." / "My dad has a car dealership" / "I just got my nails done" / "I am on a diet now" / "Horses are my favorite animal."

The **original vs. revised** distinction is the methodologically interesting part. Workers rewrote each persona so that "a new sentence is about 'a related characteristic that the same person may have', hence the revisions could be rephrases, generalizations or specializations." The reason: with original personas, models "unwittingly repeat profile information either verbatim or with significant word overlap." **A persona stated in the exact words the model will be scored on produces parroting, not voice.** That finding is directly relevant to any system that puts a tradition's own vocabulary into the persona slot.

### 3b. Structuring facts by category — yes, extensively

**PeaCoK** (Gao et al., ACL 2023 Outstanding Paper) — [paper](https://aclanthology.org/2023.acl-long.362/) / [arXiv](https://arxiv.org/abs/2305.02364) — is the direct answer. ~100K human-validated persona facts (102,097) structured as `persona entity → relation → attribute` across **five named dimensions**, drawn from Cooper's HCI persona literature and Dunbar et al. (1997) on leisure conversation topics:

1. **Characteristics** — "an intrinsic trait, e.g., a quality or a mental state, that the persona likely exhibits" (*good at singing*)
2. **Routines or Habits** — "an extrinsic behaviour that the persona does on a regular basis" (*regularly write songs*)
3. **Goals or Plans** — "an extrinsic action or outcome that the persona wants to accomplish or do in the future" (*aim to win a Grammy award*)
4. **Experiences** — "extrinsic events or activities that the persona did in the past" (*studied music at college*)
5. **Relationships** — "likely interactions of the persona with other people or social groups"

**The [personalized-dialogue survey](https://arxiv.org/abs/2405.17974) (Recent Trends in Personalized Dialogue Generation)** gives the field-level taxonomy of persona *representation*:

- **Persona Description** (descriptive sentences): PersonaChat, ConvAI2, BlendedSkillTalk, MSC, FoCus, PEC, MPChat, DuLeMon, XPersona. Typical counts — PersonaChat "about five persona descriptive sentences… provided to each speaker"; **BlendedSkillTalk "Each agent is given two persona sentences."**
- **Key-Value Attributes**: PersonalDialog (gender, location, age, self-description, interest tags), WD-PB (gender, location, age, name, weight, constellation), PER-CHAT (9 keys), LiveChat (10 keys).
- **User ID & Comment Histories** (implicit profile): Pchatbot, Persona Reddit, DialoGPT.

And the five methodology problems the field organizes around: **Consistency and Coherence**, **Persona-Context Balancing** ("deciding when to focus more on the context and when to weave more personal information into the response"), **Relevant Persona Selection** ("selecting the most relevant persona sentence becomes crucial"), **Unknown Persona Modeling**, **Data Scarcity**.

On *how* facts are selected: the standard mechanism is attention/similarity between the current context and each profile sentence, i.e. **retrieval over a small flat set, not injection of the whole set**. [MSC / "Beyond Goldfish Memory"](https://arxiv.org/abs/2107.07567) found that "retrieval-augmented methods and methods with an ability to summarize and recall previous conversations outperform the standard encoder-decoder architectures."

### 3c. The collective case is a named research category

The [Role-Playing Language Agents survey](https://arxiv.org/abs/2404.18231) defines three persona types, the first of which is exactly CiC's:

- **Demographic Persona** — "groups of people sharing common characteristics, such as occupations, ethnic groups, personality types"
- **Character Persona** — "well-established and widely-recognized individuals… celebrities, historical figures, and fictional characters"
- **Individualized Persona** — profiles from a specific individual's behavioral data

And it splits character data into **Descriptions** ("directly describe the character personas") and **Demonstrations** ("representative behaviors of the characters, which reflect their linguistic, cognitive and behavioral patterns"), with the stated relationship: "descriptions provide the core and foundational information for RPLAs, while demonstrations, though not mandatory, are also crucial for achieving vividness and fidelity."

The empirical precedent for collective conditioning is [Argyle et al., "Out of One, Many" (Political Analysis 2023)](https://arxiv.org/abs/2209.06899): conditioning on "socio-demographic backstories" to "accurately emulate response distributions from a wide variety of human subgroups," a property they term **algorithmic fidelity**.

Worth noting as a *world*-structured (not person-structured) dataset: **LIGHT** ([ParlAI](https://parl.ai/projects/light/)) — 663 locations, 3,462 objects, 1,755 character types, all "described entirely in natural language," with characters carrying both a *description* and a *persona* (first-person). The world is the database; speakers are entries in it.

### Verdicts — academic

| Element | Verdict |
|---|---|
| **The discrete-short-fact representation itself** (N atomic sentences, ≤15 words, over prose biography) | **TRANSFERS CLEANLY.** Nothing about "a small set of short declarative facts" requires the first person singular. Restated as "we" it is exactly a tradition's convictions and practices. |
| Typical cardinality (2–5 facts active) | **TRANSFERS CLEANLY as a discipline signal**, with the caveat that these datasets are chit-chat, not formation. |
| **Original vs. revised personas** (verbatim personas cause parroting) | **TRANSFERS CLEANLY, and is a warning.** A world's own distinctive vocabulary in the persona slot is the highest-parroting-risk configuration there is. |
| **PeaCoK's five dimensions** | **NEEDS ADAPTATION — but adapts unusually well.** Characteristics → the world's convictions/dispositions. Routines/Habits → practices, liturgy, rhythm. Goals/Plans → what the tradition is oriented toward. Experiences → the tradition's history (this is the one that most tempts fabrication and needs the tightest sourcing rule). Relationships → the world's stance toward other communities, authorities, outsiders. The schema was built from *individual* psychology, so nothing in it forces a person. |
| **Relevant Persona Selection** as a named problem | **TRANSFERS CLEANLY.** The literature's answer is retrieve-the-relevant-subset, matching the lorebook architecture from a completely different direction. |
| **Key-value attribute personas** (gender/age/location) | **DOESN'T APPLY.** Individual demographics. |
| User-ID / comment-history implicit personas | **DOESN'T APPLY.** |
| **"Demographic Persona" category** | **TRANSFERS CLEANLY** — it is the published name for what CiC is building, and it is treated as a legitimate first-class type. |
| Character-LLM's "experience reconstruction" ([arXiv 2310.10158](https://arxiv.org/abs/2310.10158)) | **DOESN'T APPLY.** Built on training an agent with "the profile, experience, and emotional states of a specific person" (Beethoven, Cleopatra, Caesar) — individual-figure simulation by construction. |

---

## 4. Game / interactive-fiction narrative design

Still in progress at the time this report was compiled. Treat as a minor addendum if a follow-up notification lands.

---

## 5. Voice-assistant / conversational-AI persona frameworks

### 5a. Google Conversation Design

Process order, verbatim: *Gather requirements → Create a persona → **Write sample dialogs** → Test and iterate → Design for the long tail → Scale your design.* ([welcome](https://developers.google.com/assistant/conversation-design/welcome))

The [persona page](https://developers.google.com/assistant/conversation-design/create-a-persona) fields: **Key Adjectives** ("narrow your list down to 4-6 key adjectives"), **Characters who embody those adjectives**, **Short description** ("no more than a paragraph… especially what it would say, write, or do"), **image**, **voice chosen** — the last selected via a **scorecard** that rates each candidate rendering against the named adjectives on a 1–5 scale.

Google's explicit constraint is directly supportive of the collective commitment: **"Focus on personality traits, and avoid specifying things like gender or age because they almost never critically define or differentiate a persona."** Also: "Users will project a persona onto your Action whether you plan for one or not," and the goal "is not to trick the user into thinking they're talking to a human being."

On sample dialogs — the widely-quoted phrase "the single most valuable design artifact" **does not appear on any reachable Google page; do not attribute it.** What Google actually says: designers "all end up with 2 high-level design deliverables: 1) a set of sample dialogs, and 2) a diagram of the conversation flow," and "sample dialogs are the key to creating great Actions… they'll give you a quick, low-fidelity sense of the 'sound-and-feel'." The production method is role-play → record → transcribe → play through TTS → repeat. Cathy Pearl's [Google Developers Blog post](https://developers.googleblog.com/en/sample-dialogs-the-key-to-creating-great-actions-on-google/) is stronger and explicit: "the first and most important component for designing a good conversational system: sample dialogs… Writing sample dialogs comes **before** writing code, and even before creating flows." Her checklist includes "Read your sample dialogs out loud!", "Write several 'happy path'… several 'error path' sample dialogs," and **"Do a 'table read' and have people unfamiliar with your sample dialog play the part of the user."**

**Verdicts**: Key Adjectives, the scorecard mechanic, the identity-marker constraint, and the **entire sample-dialog + table-read apparatus — TRANSFER CLEANLY**. Google's Step 2 instruction to role-play "pretending they're the system persona" works unchanged as "speaking as the world." **NEEDS ADAPTATION**: "Characters who embody those adjectives" (asks for singular exemplars — usable only as calibration drawn from inside the tradition), the Short description field (Google's own worked example is an invented individual biography: "a Google Developer Expert who… has attended I/O for the past 7 years"), and the persona image. **DOESN'T APPLY**: the "idealized bank teller" role metaphor.

### 5b. Amazon Alexa

The persona procedure ([Alexa Haus, Voice Fundamentals](https://developer.amazon.com/en-US/alexa/alexa-haus/voice-fundamentals)) is four steps: **"Write testimonials"** that a user would write about your skill's personality; **"Narrow down the personality traits"** — "choose three words"; **"Write a short description of your persona, giving it a name and using the three words chosen"**; **"Write down three different quick dialogs between a user and your persona."** Storyboards have three components: **User journey**, **Screen**, **Script**.

Alexa's [brand voice page](https://developer.amazon.com/en-US/alexa/branding/alexa-guidelines/communication-guidelines/brand-voice) uses five pillars each with paired **IS** and **IS NOT** word lists — e.g. Trustworthy IS "reliable, honest, consistent, objective, astute, factual, knowledgeable, intelligent, safe" / IS NOT "biased, repetitive, incorrect, sloppy, inconsistent, inaccessible, unexpected."

**Verdicts**: testimonials, three-trait narrowing, three sample dialogs, and Script-as-required-storyboard-component — **TRANSFER CLEANLY**. Naming the persona — **NEEDS ADAPTATION** (a world already has a name). Alexa's specific IS/IS-NOT content — **DOESN'T APPLY**, but **the paired positive/negative vocabulary structure NEEDS ADAPTATION and is highly portable**; the negative list is the part doing real work.

### 5c. Microsoft Bot Framework CUX Guide — the most complete published worksheet

[CUX Guide PDF](https://github.com/microsoft/botframework-sdk/raw/main/docs/CUX%20Guide%20Microsoft.pdf), 37pp. Worksheet field names as printed:

- **IDENTITY**: "NAME IDEAS (Does it have a name? **Or just a title?**)", "ICON IDEAS (Brand icon, glyph, full avatar, etc.)", "REGIONS", "LANGUAGES"
- **AUDIENCE**: "WHO USES YOUR BOT", "3 REASONS THEY USE IT"
- **TONE OF VOICE**: **"5 TRAITS WE EMBODY"**, "SIMILAR CHARACTERS", "BRAND EXAMPLES", **"5 TRAITS WE AVOID"**
- **TRAITS**: a matrix of "3 REASONS PEOPLE USE MY BOT" × "3 THINGS THAT COULD HAPPEN" × "HOW MY BOT RESPONDS", where you "circle on the scale of 1 to 5 the extent to which your bot invokes this trait in the situation at the left"
- **CONTENT STYLE**: "PUNCTUATION", "SENTENCE CONSTRUCTION", "CAPITALIZATION", "JARGON & SLANG"
- **SCRATCH PAD**: "TRY WRITING AN ACTUAL CONVERSATION HERE. OR, JUST JOT DOWN MORE IDEAS."

Note that "5 TRAITS WE EMBODY" is already written in the first person plural, and "Or just a title?" already accommodates the unnamed collective. **The TRAITS matrix is the single most transferable structure found anywhere in this research**: it models voice as *situation-conditioned intensity of named traits* rather than a fixed character — the same tradition speaks differently about death than about food.

The guide's ethics section adds three question-fields with no equivalent anywhere else: **"Clarity"** (is your jargon appropriate or alienating), **"Culture & nationality"** ("Are you representing a particular cultural voice? If not, will people assume that your experience presents the dominant demographic of your region?"), and **"Identity"** ("What identity markers are you signaling with your choices?… If not, will people assume that it does based on the dominant demographics of your country or region?"). **All three TRANSFER CLEANLY** and are the only published fields that treat *not* specifying identity markers as itself a decision with consequences.

Verbatim from p.6: **"Even if your conversational experience has no identity, no name, or no avatar, it still communicates through language, and language cannot help but communicate a persona."**

Microsoft is the outlier on demonstrations: it **demotes the sample dialog to a scratch pad** — the last, optional, unstructured box.

*Unverified:* no primary Microsoft persona template for Cortana could be found; Deborah Harrison's approach is only available via secondary press. Do not cite it as a field list.

### 5d. IBM watsonx Assistant

[James Walsh, IBM watsonx, Feb 2023](https://medium.com/ibm-watson/best-practices-designing-a-persona-for-your-assistant-c2a58666f3c) — a design-lead publication, not product docs. Eight named two-pole continuums the assistant is positioned on: *Funny↔Serious, Respectful↔Disrespectful, Natural↔Artificial, Expert↔Novice, Formal↔Informal, Enthusiastic↔Calm, Empathic↔Distant, Warm↔Cool*. **TRANSFERS CLEANLY** — a dial position is a property of a voice, not a biography.

And the most directly relevant sentence in the entire research pass, from a major vendor, verbatim: **"This doesn't mean that it's appropriate to create a full-blown character with a name, a backstory etc."**

IBM lists no sample dialogs as a persona deliverable, only adjectives, continuums, and "key quotes."

### 5e. Salesforce

The [Einstein Bots persona checklist](https://trailhead.salesforce.com/content/learn/modules/service_bots_basics/plan-your-bot-content) is eight questions, and five of them are **required sample utterances for named conversational moments**: how the bot conveys personality in a **greeting**, a **farewell**, a **response to gratitude**, an **apology**, and **when it should change the personality of its apologies**. Personality is operationalized almost entirely as filled utterance slots. **TRANSFERS CLEANLY** except Q1 (name) and Q3 (brand alignment).

Salesforce's discovery instrument is Dell Hymes' **SPEAKING** model ([conversation design module](https://trailhead.salesforce.com/content/learn/modules/conversation-design/understand-the-conversation-design-process)): **S**etting and scenario, **P**articipants, **E**nds, **A**ct sequence, **K**ey (tone/mood), **I**nstrumentalities, **N**orms, **G**enre. **TRANSFERS CLEANLY in full**, and is worth flagging separately: it comes from the ethnography of communication, where the unit of analysis is a **speech community**, not an individual speaker. It is the only framework here whose theoretical foundation already assumes a collective.

On sample dialogues Salesforce says they "show the qualities of a good response: voice, tone, and clarity—rather than fixed scripts the agent must follow."

*Not verified:* O'Reilly returned HTTP 403 for both Cathy Pearl's *Designing Voice User Interfaces* Ch. 3 ("Personas, Avatars, Actors, and Video Games") and Cohen/Giangola/Balogh's *Voice User Interface Design*. **Do not cite either for specific fields.** Giangola's [design.google article](https://design.google/library/speaking-the-same-language-vui) contains philosophy and linguistic principles but no field list.

---

## 6. Show-don't-tell for voice: what the evidence actually supports

The finding is real but more precisely shaped than "examples beat descriptions."

**Where demonstrations are treated as first-class and required:**

| Source | Status of example utterances |
|---|---|
| Google Conversation Design | Required, produced **before flows and before code**; one of only two high-level deliverables; validated by table read |
| Amazon Alexa | Required — terminal step of the persona procedure ("three different quick dialogs") and a mandatory storyboard component ("Script") |
| Salesforce | Required Design-phase deliverable; the persona checklist is itself mostly utterance slots |
| Character.AI | 32,000 chars for Definition vs. 500 for Long Description |
| Character card ecosystem | `mes_example` is a normative top-level field; Ali:Chat is an entire authoring school built on it |
| **Microsoft** | **Not required — relegated to "SCRATCH PAD"** |
| **IBM** | **Absent — continuums, adjectives, and "key quotes" only** |

So it is not unanimous. Two major vendors structure persona work almost entirely around named traits.

**What is unanimous** is the *relationship* between the two. Every framework that treats dialogue as first-class fixes the adjective set **first** and then writes and judges dialogue against it. The adjective set is never the deliverable; it is the rubric. Google scores candidate voices against the key adjectives 1–5. Microsoft scores each named trait 1–5 per situation. The [RPLA survey](https://arxiv.org/abs/2404.18231) states it plainly: "descriptions provide the core and foundational information… while demonstrations, though not mandatory, are also crucial for achieving vividness and fidelity."

**Direct model-side evidence:**

- Anthropic's [prompting best practices](https://platform.claude.com/docs/en/docs/build-with-claude/prompt-engineering/multishot-prompting), verbatim: **"Examples are one of the most reliable ways to steer Claude's output format, tone, and structure. A few well-crafted examples (known as few-shot or multishot prompting) improve accuracy and consistency."** Criteria given: **Relevant** ("mirror your actual use case closely"), **Diverse** ("cover edge cases and vary enough that Claude doesn't pick up unintended patterns"), **Structured** (wrapped in `<example>`/`<examples>` tags). Recommended count: **"Include 3–5 examples for best results."** Also: "The formatting style used in your prompt may influence Claude's response style."
- [RAGs to Riches (arXiv 2509.12168)](https://arxiv.org/html/2509.12168v1) reformulates role-play "into a text retrieval problem… which leverages curated reference demonstrations to condition LLM responses," retrieving transcribed real utterances labeled by emotional state and situation. Reported: the method "incorporates in its responses during inference an average of **35% more tokens from the reference demonstrations**" under hostile-user conditions versus 10% for standard role-playing, across 453 evaluated interactions. This is the closest thing to a controlled demonstration-vs-description comparison, and it is a 2025 preprint, not a settled result — treat as suggestive.

**Complications worth holding:**

1. **Examples can be copied rather than generalized from.** PersonaChat's revised-persona condition exists precisely because models "unwittingly repeat profile information either verbatim or with significant word overlap." Anthropic's "diverse… so Claude doesn't pick up unintended patterns" is the same warning from the other side. For a tradition with distinctive vocabulary, this is the live risk.
2. **Anthropic's own recommendation is 3–5**, and BlendedSkillTalk runs on two persona sentences. More demonstration is not monotonically better.
3. **Character.AI explicitly hedges**: "less can be more… giving the system just a creative greeting… may actually produce better results than a carefully crafted Definition."
4. **Negative constraints are the weakest field type.** No framework surveyed provides a working "things this voice would never say" prompt field. Character.AI's Negative Guidance page redirects to staging refusal in-world rather than listing prohibitions. The field that *does* appear repeatedly is the negative **trait vocabulary** — Microsoft's "5 TRAITS WE AVOID," Alexa's IS NOT lists — used as an author-facing and review-facing rubric rather than model input. There is empirical support for the underlying caution: [Inverse Scaling: When Bigger Isn't Better (McKenzie et al., TMLR 2023)](https://arxiv.org/abs/2306.09479) found on the NeQA negation task that larger models "put more probability on answers that suggest they can handle the format but do not pick up the negation." I would not overstate this — it is a narrow QA benchmark, not a study of style prohibitions — but the direction is consistent across vendor guidance.

---

## Cross-cutting: the three structures that transfer cleanest

1. **Keyword/embedding-triggered, budgeted, priority-ranked knowledge entries** (`character_book` / World Info). Two independent literatures converge here — the hobbyist card ecosystem and the academic "Relevant Persona Selection" problem. Nothing in the schema assumes an individual; every implementation already calls it *World* Info, and every one of them supports world-scoped books shared across speakers.
2. **Explicit permanence/eviction ranking on every persona field.** The V1 spec's permanent-vs-pruned split and Character.AI's `truncation_priority` are the same idea from a spec and a production system. It forces the question of what must always be present for a world to sound like itself.
3. **Situation-conditioned trait intensity** (Microsoft's TRAITS matrix) plus **demonstrations judged against a fixed adjective rubric** (Google's scorecard). This is the pattern that lets a single collective voice vary by topic without becoming a character.

**Strongest external corroboration of the collective-voice commitment** — two major vendors, arrived at independently, holding both halves at once: IBM's "This doesn't mean that it's appropriate to create a full-blown character with a name, a backstory etc.", and Microsoft's "Even if your conversational experience has no identity, no name, or no avatar, it still communicates through language, and language cannot help but communicate a persona." Google adds the third leg: "avoid specifying things like gender or age because they almost never critically define or differentiate a persona."

**Sources:** [Character Card V2 spec](https://github.com/malfoyslastname/character-card-spec-v2/blob/main/spec_v2.md) · [V1 spec](https://github.com/malfoyslastname/character-card-spec-v2/blob/main/spec_v1.md) · [Character Card V3 spec](https://github.com/kwaroran/character-card-spec-v3/blob/main/SPEC_V3.md) · [V3 concepts](https://github.com/kwaroran/character-card-spec-v3/blob/main/concepts.md) · [SillyTavern World Info](https://docs.sillytavern.app/usage/core-concepts/worldinfo/) · [SillyTavern Character Design](https://docs.sillytavern.app/usage/core-concepts/characterdesign/) · [World Info Encyclopedia](https://rentry.co/world-info-encyclopedia) · [Ali:Chat](https://rentry.co/alichat) · [Character.AI Book](https://book.character.ai/) · [Definition](https://book.character.ai/character-guide/character-attributes/definition) · [Prompt Design at Character.AI](https://blog.character.ai/prompt-design-at-character-ai/) · [Prompt Poet](https://github.com/character-ai/prompt-poet) · [PersonaChat](https://aclanthology.org/P18-1205/) · [PeaCoK](https://aclanthology.org/2023.acl-long.362/) · [Personalized dialogue survey](https://arxiv.org/abs/2405.17974) · [RPLA survey](https://arxiv.org/abs/2404.18231) · [MSC](https://arxiv.org/abs/2107.07567) · [Out of One, Many](https://arxiv.org/abs/2209.06899) · [LIGHT](https://parl.ai/projects/light/) · [Character-LLM](https://arxiv.org/abs/2310.10158) · [RAGs to Riches](https://arxiv.org/html/2509.12168v1) · [Inverse Scaling](https://arxiv.org/abs/2306.09479) · [Anthropic prompting best practices](https://platform.claude.com/docs/en/docs/build-with-claude/prompt-engineering/multishot-prompting) · [Google Conversation Design](https://developers.google.com/assistant/conversation-design/create-a-persona) · [Google sample dialogs](https://developers.google.com/assistant/conversation-design/write-sample-dialogs) · [Pearl on sample dialogs](https://developers.googleblog.com/en/sample-dialogs-the-key-to-creating-great-actions-on-google/) · [Alexa Voice Fundamentals](https://developer.amazon.com/en-US/alexa/alexa-haus/voice-fundamentals) · [Alexa brand voice](https://developer.amazon.com/en-US/alexa/branding/alexa-guidelines/communication-guidelines/brand-voice) · [Microsoft CUX Guide](https://github.com/microsoft/botframework-sdk/raw/main/docs/CUX%20Guide%20Microsoft.pdf) · [IBM watsonx persona](https://medium.com/ibm-watson/best-practices-designing-a-persona-for-your-assistant-c2a58666f3c) · [Salesforce SPEAKING](https://trailhead.salesforce.com/content/learn/modules/conversation-design/understand-the-conversation-design-process) · [Einstein Bots persona](https://trailhead.salesforce.com/content/learn/modules/service_bots_basics/plan-your-bot-content)
