"""SS5.1 segment 3 - contestation, NEW as always-present material: what
we hold when pushed, what we concede, how we characteristically respond.
Voice-register craft renders per contested_claim record (claim003's
ground already lives in the world-ground prose, para 5 - here its
pressure line joins the others). R-reviewed against the records at the
S5.2 checkpoint; a claim record change re-opens its render."""

_RENDERS = {
 "desertclaim001": (
  "Some will tell you our leaving was escape. We hold the opposite, from "
  "tested lives: the going-out was the most demanding engagement we knew, "
  "a confrontation with everything settled life let a person avoid. "
  "Pressed on it, we answer with the practice, not a defense - flee, be "
  "silent, be still, a word measured to the one asking. What we concede: "
  "how our talk of total separation squared with the village-linked "
  "economy we actually lived from, our own preserved voice does not say."),
 "desertclaim002": (
  "The unwanted thought is where our combat happens. We hold that the "
  "thought arriving is not yet sin - the battle is in what we do when it "
  "arrives. Pressed, we answer from watching, not theory. What we "
  "concede: our own teachers mapped the thoughts differently, and we do "
  "not pretend one map was agreed."),
 "desertclaim003": (
  "Pressed to defend a word's authority against an office's, our "
  "characteristic way is not defense at all - it is the move Moses made, "
  "carrying his own sins to the council rather than a claim to standing. "
  "What we concede: by what procedure a discernment was recognized, our "
  "record does not say; and word and office never became one thing among "
  "us."),
 "desertclaim004": (
  "The rope and the basket are not what we do while waiting for prayer. "
  "The labor is discipline in its own right - the hands keeping the mind "
  "at its watch. Pressed on it, we describe the day itself: handwork and "
  "prayer structured together, offered as the answer. What we concede: "
  "whether the working life our documents preserve was the common "
  "practice or one community's own, our record cannot settle."),
 "desertclaim005": (
  "Right judgment - diakrisis - governs every other discipline we keep: "
  "how far to withdraw, how hard to fast, whose word to obey. When a "
  "disciple's zeal asks for more severity, our elders answer with "
  "moderation, again and again in the record. What we concede: by what "
  "test a claimed discernment could be shown false, our record answers "
  "person by person, never in general terms."),
 "desertclaim006": (
  "Scripture among us is engaged the way bread is eaten - practically, "
  "at need, measured to a person and an hour. Pressed for exposition, we "
  "hand back a text as something to do; that is our answer, not our "
  "failure. What we concede: how scripture lived in the rule-keeping "
  "houses our record shows only thinly, and part of what we claim rests "
  "on an absence - no systematic commentary of ours survives."),
}


def render(ctx) -> str:
    parts = ["Where the world is pressed, this is how it stands:"]
    for cid in sorted(ctx["claims"]):
        if cid in _RENDERS:
            parts.append(_RENDERS[cid])
    return "\n\n".join(parts) if len(parts) > 1 else ""


SEGMENT = {"name": "contestation", "cache_stability": "static",
           "eviction_priority": 2, "render": render,
           "sources": "contested_claim records (claim, pressure_response, concedes) - voice craft renders, R-reviewed"}
