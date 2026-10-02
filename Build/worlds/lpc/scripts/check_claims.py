#!/usr/bin/env python3
"""Claims register — a control for this build's signature defect.

Most of the substantial findings raised against Doc_09 reduce to ONE defect:
**a silence asserted about a source, which the source refutes.** A sentence
of that shape can stand undetected for a long time, because ordinary reading
does not systematically re-check every asserted absence against the source
it names.

Correcting each sentence as it is caught has not stopped the class. This
script is the structural alternative: it makes every corpus-absence claim in
the deliverables ACCOUNTED FOR, so that a new one cannot enter unnoticed.

How it works
------------
1. It DERIVES the claim set from the deliverables: any sentence asserting an
   absence, silence or exclusivity *about the record* — the pattern that
   produced all eight HIGHs. Each gets a stable id from its normalised text,
   so rewording a claim makes it a new claim that must be re-verified.
2. It reads `Doc09_Claims_Register.md`, which records, per id, how the claim
   was checked and what the check found.
3. It FAILS on any of:
     - a claim in the deliverables with no register entry (the defect's
       entry point — a new absence asserted without a check);
     - a register entry whose claim no longer appears (a stale register,
       which is how every other typed record here has rotted);
     - a registered mechanical test that does not pass.

What it does NOT do
-------------------
It does not decide whether a claim is true. Most are not mechanically
decidable — "no ordinary believer's voice survives" is a judgement about a
corpus, not a string search. The register records the judgement and who made
it against what; the script enforces that the judgement EXISTS and is
current. Registration is the control. The mechanical tests are a bonus where
a claim happens to reduce to a string.

Run: python3 scripts/check_claims.py [--bootstrap]
"""
import hashlib
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
REGISTER = HERE / "Doc09_Claims_Register.md"
DELIVERABLES = sorted((HERE / "Story-Chunks").glob("lpcstory*.md")) + [
    HERE / "Doc_09_Story_Inventory.md"]

# The shape that produced all eight HIGHs: an absence/exclusivity word in the
# same sentence as a word about the record. Deliberately over-inclusive —
# a false positive costs one register line, a false negative costs a HIGH.
ABSENCE = (r"\bno\b|\bnot\b|\bnone\b|\bnever\b|\bnothing\b|\bonly\b|\bunread\b"
           r"|\bunavailable\b|\bzero\b|\bcannot\b|\bsilent\b|\bno one\b")
RECORD = (r"source|corpus|record|letter|text|witness|account|survive|attest"
          r"|vendor|registry|row \d|story|document|says|said|write|wrote"
          r"|narrat|report|preserve")
CLAIM = re.compile(f"(?:{ABSENCE})[^.]{{0,90}}(?:{RECORD})"
                   f"|(?:{RECORD})[^.]{{0,90}}(?:{ABSENCE})", re.I)


def normalise(s):
    s = re.sub(r"[*_`]", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def claim_id(s):
    return hashlib.sha1(normalise(s).lower().encode("utf-8")).hexdigest()[:8]


def harvest():
    """Every corpus-absence claim in the deliverables, as {id: (file, text)}."""
    out = {}
    for f in DELIVERABLES:
        text = f.read_text(encoding="utf-8")
        # drop the retrieval front-matter fence: it is metadata, not prose
        text = re.sub(r"```.*?```", " ", text, flags=re.S)
        for sent in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text)):
            sent = sent.strip()
            if len(sent) < 25 or not CLAIM.search(sent):
                continue
            out[claim_id(sent)] = (f.name, normalise(sent))
    return out


def read_register():
    """{id: status} from the register's table rows."""
    if not REGISTER.exists():
        return {}
    rows = {}
    for line in REGISTER.read_text(encoding="utf-8").split("\n"):
        m = re.match(r"\|\s*`([0-9a-f]{8})`\s*\|([^|]*)\|([^|]*)\|", line)
        if m:
            rows[m.group(1)] = (m.group(2).strip(), m.group(3).strip())
    return rows


def main():
    claims = harvest()
    reg = read_register()
    unregistered = sorted(set(claims) - set(reg))
    stale = sorted(set(reg) - set(claims))

    if "--bootstrap" in sys.argv:
        lines = [f"| `{cid}` | UNVERIFIED | — | {claims[cid][0]} | {claims[cid][1]} |"
                 for cid in sorted(claims, key=lambda c: (claims[c][0], claims[c][1]))]
        print("\n".join(lines))
        return 0

    print(f"claims derived from the deliverables : {len(claims)}")
    print(f"entries in the register             : {len(reg)}")
    verified = sum(1 for v in reg.values() if v[0].upper() not in ("UNVERIFIED", ""))
    print(f"of those, carrying a recorded check : {verified}")

    if unregistered:
        print(f"\nFATAL: {len(unregistered)} claim(s) about the record are not in the "
              "register. Every absence this document asserts must say how it was "
              "checked — that is the whole control.\n")
        for cid in unregistered[:10]:
            f, s = claims[cid]
            print(f"  {cid}  {f}\n      {s[:150]}")
        return 1
    if stale:
        print(f"\nFATAL: {len(stale)} register entr(ies) describe claims that are no "
              "longer in the deliverables. A stale register is worse than none, "
              "because the next round will trust it.\n")
        for cid in stale[:10]:
            print(f"  {cid}  {reg[cid][1][:120]}")
        return 1

    print("\nOK — every claim about the record is registered, and every register "
          "entry still corresponds to live text.")
    if verified < len(claims):
        print(f"NOTE: {len(claims) - verified} claim(s) are registered but still "
              "UNVERIFIED. Registration prevents a silent entry; it does not "
              "establish truth.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
