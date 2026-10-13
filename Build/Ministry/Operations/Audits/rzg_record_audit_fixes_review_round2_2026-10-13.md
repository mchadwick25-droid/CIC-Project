# rzg record audit fixes: review round 2, 2026-10-13

Reviewer: Opus, targeted recheck of the 20 fields changed in response to round 1 (see `rzg_record_audit_fixes_review_round1_2026-10-13.md`), against the round 1 findings and the vendored sources. Every field was graded with `grade_text`.

Result: 19 pass, 1 minor, 0 blocking. All 20 meet FK <= 10 and FRE >= 60.

- Passing: the `rzg.demo.consensus-contest` turn (hedge restored, invented doctrine gone); the three demonstration provenance notes; the three witness texts; the three quote renderings; `rzg.limit.no-teaching-on-wealth-or-marriage` ("our teachers did write on both" checks out against Calvin's Institutes II.8.41-44 and Articles XXIII, XXVIII-XXX and XXXIII); the eight term fields.
- Minor, fixed: `rzg.limit.hagiography-refused` `statement` kept a closing line that repeated an earlier sentence. The last sentence now reads "Our record holds no such book."
- Outside the recheck and already registered: the unchanged `use_note.means` of the wealth and marriage limit, and the `senses.informational` date of `rzg.term.confession-of-faith`.

Status: cleared at round 2.
