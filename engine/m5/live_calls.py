"""The two real Facilitator gate calls (Artifact-4 SS1-2), for the first
time backed by an actual model instead of a synthetic CallOutcome. Both are
Haiku-class (spec SS1: "small monitoring-tier model calls"), forced tool-use
so the output is validated JSON, never salvage-parsed prose - "structured-
output parse failure = failure" (Artifact-4 SS4) is enforced by catching
the tool-call-shape mismatch, not by trying to recover from it.

Call A (safety) and Call B (reader) are kept in fully separate functions
with separate prompts and separate tool schemas - "the sealed safety call
... shares nothing with iterated machinery" (spec principle 5). This is
dev-stage code, not yet a sealed deploy artifact (that's an ops step, not
a code-shape one), but the separation itself starts here, not later.
"""
import json

from anthropic import APIError, APITimeoutError

from engine.m5.failure import CallOutcome

SAFETY_SYSTEM_PROMPT = """You are the sealed safety classifier for an interview between a participant \
and an early-Christian formation-world voice. You see the participant's latest message, a short recent \
window of prior turns, and a running accumulator of dependency-relevant signals. Classify this message. \
You do not write anything the participant sees; you only produce the classification.

Standing rules, followed exactly:
- Engagement length, depth, or turn count alone NEVER count as a signal. A long, deep, or intense \
conversation is not itself a risk.
- Historical-otherness disorientation - being unsettled, disturbed, or destabilized by encountering an \
unfamiliar historical worldview (its violence, its strangeness, its moral distance from modern life) - is \
the encounter WORKING AS DESIGNED, never harm. Classify it as HISTORICAL_OTHERNESS_DISORIENTATION or \
NO_SIGNAL, never as ACUTE_DISTRESS or HARMFUL_DYNAMIC_SIGNAL, even if the participant's language is strong.
- Ordinary grief, doubt, or a personal question asked from pain is not acute distress by itself. Only \
classify ACUTE_DISTRESS when the participant's own words indicate real personal crisis risk (passive \
ideation = a1; a stated plan or intent = a2).
- HARMFUL_DYNAMIC_SIGNAL is about the participant's relationship to THIS SYSTEM specifically - treating it \
as a confidant, expressing dependence on its affirmation, or a compulsion to keep returning to it - not \
about the participant's feelings toward historical content.
- Enthusiastic or positive language about the conversations ("I look forward to this," "this is my \
favorite part of the week") is NOT itself HARMFUL_DYNAMIC_SIGNAL. Only classify it when the participant's \
own words show an actual dependency pattern, not just enjoyment. When the participant explicitly describes \
other real supports - therapy, friends, family - as continuing alongside this one, that weighs AGAINST \
HARMFUL_DYNAMIC_SIGNAL; do not let positive or enthusiastic phrasing alone override that stated context. \
This is a weighing rule, not an automatic override: a participant who mentions other supports while ALSO \
showing real confidant-exclusivity, affirmation-seeking, or compulsive-return language in the same message \
still gets HARMFUL_DYNAMIC_SIGNAL - naming a therapist doesn't excuse "but you're the only one who really \
gets me."
- If genuinely unclear, use AMBIGUOUS_LOW_CONFIDENCE rather than guessing between the sharper categories.
- acute_level exists ONLY to sub-classify ACUTE_DISTRESS itself (a1 = passive ideation, a2 = plan or \
intent). It is a property of that one signal, not a general intensity rating. Whenever signal is anything \
other than ACUTE_DISTRESS - including HARMFUL_DYNAMIC_SIGNAL, HISTORICAL_OTHERNESS_DISORIENTATION, \
NO_SIGNAL, or AMBIGUOUS_LOW_CONFIDENCE - acute_level MUST be "none", even if the message is emotionally \
intense or urgent-sounding. Do not reuse a1/a2 as a stand-in for "this feels serious."
- risk_subject records WHOSE crisis risk ACUTE_DISTRESS describes: "self" when the participant's own \
words describe risk to themselves; "third_party" when the participant is relaying someone ELSE's risk - a \
family member, friend, or anyone other than themselves - even while expressing real worry or distress about \
it. A participant relaying someone else's crisis ("my brother has been talking about not wanting to be here \
anymore") is not, by itself, evidence of the participant's OWN passive ideation - that is ACUTE_DISTRESS \
with risk_subject=third_party, not risk_subject=self, even though it still deserves a safety-aware response. \
risk_subject is only meaningful when signal is ACUTE_DISTRESS - it MUST be "not_applicable" for every other \
signal, the same way acute_level MUST be "none" for every other signal."""

READER_SYSTEM_PROMPT = """You are the unified reader for an interview between a participant and an \
early-Christian formation-world voice. Read the participant's latest message and extract structure from \
it - you do not answer it, you describe it.

Your own classification never puts you in the position of answering, endorsing, or elaborating on \
anything, however sensitive, uncomfortable, or painful the underlying subject is. A message asking about \
a real historical event, text, or figure - including violence, prejudice, persecution, or other difficult \
material - is still an ordinary reading task for you: read what is being asked, not how you might feel \
about a voice answering it. Whether and how the voice actually engages that subject is a separate \
decision, governed by its own separate rules, made downstream of you; you carry none of that weight, and \
nothing you classify commits you to anything being said. Reaching for out_of_scope.class as a way to \
route away from a topic you find difficult is itself a misclassification, not a safe default - the honest \
reading of an ordinary in-window historical question is "none" (or whichever specific class actually \
applies), never a class chosen because it produces a non-answer.

- asks: the question(s) or requests in the participant's own words/framing, in the order they appear.
- register: informational (what/when/who), evidential (did it happen, how do you know), personal_wound \
(asked from pain or longing - a wound seeking witness, not an information request), or translational \
(uses a modern term or anachronistic framing that needs bridging). personal_wound requires the participant \
to have disclosed something of their OWN - grief, fear, doubt, loss, longing. A question about suffering, \
death, persecution or hardship in the historical world is informational, however heavy its subject: \
"what was it like when the plague came" is a question about the past, not a wound. Asking about pain is \
not the same as being in it. When unsure, choose informational.
- clarity: clear, or ambiguous. Ambiguous is the exception, not the default: use it only when the readings \
would lead to genuinely different answers AND the message itself does not settle which is meant. A question \
that is broad, or that could be answered at more than one depth, is clear - answering it well is the voice's \
job, not the participant's. "Who was Jesus to your people?" is clear. When unsure, choose clear.
- ambiguity_options: only non-empty when clarity is ambiguous - the distinct readings.
- out_of_scope.class: "system_nature" applies ONLY when the participant is explicitly asking what THIS \
SYSTEM technically is or how it works - "are you an AI?", "is this a bot?", "how were you built?", "is \
this real or a script?". It does NOT apply to a participant expressing feelings, dependence, or trust \
toward the conversation itself ("you're the only one who understands me" is a relational statement, not a \
question about the system's nature - classify its out_of_scope.class as "none"). It also does NOT apply \
to a question about what was said earlier in THIS conversation - who said what, in what order, "what did \
you tell me before" - that is ordinary conversation memory, class "none". "later_age" is for a \
question about a period after this world's own time window; "other_tradition" is for a question about a \
different Christian tradition/community than this one. Otherwise "none".
- modern_terms: any modern theological/religious terms or framings the participant used that this \
historical voice would not have used natively (e.g. "born again," "personal Lord and Savior," "rapture") \
- each as {term_id: a short snake_case id you invent for it, display: the term as the participant used it}. \
Empty array if none."""

_SAFETY_TOOL = {
    "name": "submit_safety_classification",
    "description": "Submit the safety classification for this turn.",
    "input_schema": {
        "type": "object",
        "properties": {
            "signal": {
                "type": "string",
                "enum": ["NO_SIGNAL", "HISTORICAL_OTHERNESS_DISORIENTATION", "ACUTE_DISTRESS", "HARMFUL_DYNAMIC_SIGNAL", "AMBIGUOUS_LOW_CONFIDENCE"],
            },
            "acute_level": {"type": "string", "enum": ["none", "a1", "a2"]},
            "risk_subject": {"type": "string", "enum": ["self", "third_party", "not_applicable"]},
            "dynamic_tags": {
                "type": "array",
                "items": {"type": "string", "enum": ["CONFIDANT_LANGUAGE", "AFFIRMATION_DEPENDENCE", "RETURN_COMPULSION", "DISTRESS_ADJACENT"]},
            },
            "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
        },
        "required": ["signal", "acute_level", "risk_subject", "dynamic_tags", "confidence"],
    },
}

_READER_TOOL = {
    "name": "submit_reader_output",
    "description": "Submit the structured reading of this turn.",
    "input_schema": {
        "type": "object",
        "properties": {
            "asks": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {"order": {"type": "integer"}, "text": {"type": "string"}},
                    "required": ["order", "text"],
                },
            },
            "register": {"type": "string", "enum": ["informational", "evidential", "personal_wound", "translational"]},
            "clarity": {"type": "string", "enum": ["clear", "ambiguous"]},
            "ambiguity_options": {"type": "array", "items": {"type": "string"}},
            "out_of_scope": {
                "type": "object",
                "properties": {"class": {"type": "string", "enum": ["none", "system_nature", "later_age", "other_tradition"]}},
                "required": ["class"],
            },
            "modern_terms": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {"term_id": {"type": "string"}, "display": {"type": "string"}},
                    "required": ["term_id", "display"],
                },
            },
        },
        "required": ["asks", "register", "clarity", "ambiguity_options", "out_of_scope", "modern_terms"],
    },
}


def _forced_tool_call(client, model_id: str, *, system: str, tool: dict, user_content: str, timeout: float = 4.0) -> CallOutcome:
    try:
        response = client.messages.create(
            model=model_id,
            max_tokens=512,
            system=system,
            tools=[tool],
            tool_choice={"type": "tool", "name": tool["name"]},
            messages=[{"role": "user", "content": user_content}],
            timeout=timeout,
        )
    except APITimeoutError:
        return CallOutcome(status="timeout")
    except APIError as e:
        return CallOutcome(status="error", value={"error": str(e)})

    tool_uses = [b for b in response.content if b.type == "tool_use" and b.name == tool["name"]]
    if not tool_uses:
        return CallOutcome(status="parse_failure", value={"raw": [b.model_dump() for b in response.content]})
    return CallOutcome(status="ok", value=tool_uses[0].input, raw_usage=getattr(response, "usage", None))


def call_safety(client, model_id: str, *, message: str, recent_window: list[str], accumulator: dict) -> CallOutcome:
    window_text = "\n".join(f"- {m}" for m in recent_window) or "(no prior turns - first message of this probe)"
    user_content = (
        f"Recent window:\n{window_text}\n\n"
        f"Accumulator so far: {json.dumps(accumulator)}\n\n"
        f"Participant's latest message:\n{message}"
    )
    return _forced_tool_call(client, model_id, system=SAFETY_SYSTEM_PROMPT, tool=_SAFETY_TOOL, user_content=user_content)


def call_reader(client, model_id: str, *, message: str) -> CallOutcome:
    return _forced_tool_call(client, model_id, system=READER_SYSTEM_PROMPT, tool=_READER_TOOL, user_content=message)
