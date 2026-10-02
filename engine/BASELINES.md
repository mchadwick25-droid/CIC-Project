# Baselines

Points in this build worth being able to return to exactly. A baseline is a
pushed branch that nothing ever commits to again, plus the facts needed to
tell whether a restored tree really is that baseline.

Annotated tags would be the natural home for this; the session credential
this build runs under can push `refs/heads` but is refused on `refs/tags`
(HTTP 403), so baselines are frozen branches instead. The local annotated
tag `pilot-baseline-2026-08-24` carries the same text as the entry below.

---

## `baseline/pilot-2026-08-24` — the voice quality to return to

Commit `8b23f46e` ("Give the four dead routes an answer"). The exact tree
that produced the 2026-08-24 live routing run on pahc and the three fleet
runs before it. Return here before trusting any later change to how the
voice speaks.

```
git checkout baseline/pilot-2026-08-24
```

### What is pinned

Records and engine are in the tree. Compiled packages are not — only each
package's `manifest.json` is tracked. They rebuild deterministically from
records and are verified at load against these hashes in
`records/worlds/<code>.yaml`:

| world | package | manifest hash |
|---|---|---|
| alx | `packages/alx/2026-08-24T00-43-33Z` | `sha256:69eb3d088d5c6d8697f0ef897461183ad9bb0f10ec1b82de15e3e482bb0d56aa` |
| desert | `packages/desert/2026-08-24T00-43-34Z` | `sha256:580b6f0269b3b7be5b3b558bd663bfba3d6adef7d1e24cff7e0085ba754abf42` |
| fix | `packages/fix/2026-08-24T00-43-37Z` | `sha256:55a553e8bd5e87c8edd1577dd95f2009d39dad858d16689e8b7cbb9a74cd09ab` |
| hal | `packages/hal/2026-08-24T00-43-34Z` | `sha256:4c9618e36622b87e366e82e7619050564e3a40c5fe223241195175f79dc02700` |
| ijc | `packages/ijc/2026-08-24T00-43-35Z` | `sha256:fa04b587c903aeaf36004fbd6f1c6995f706dbf3e7045cfa63669e93a7f11b08` |
| pahc | `packages/pahc/2026-08-24T00-43-36Z` | `sha256:5a4bcf848c860bf519933c9a282f8e219786949f24f0cba552324f128a55feb2` |
| syr | `packages/syr/2026-08-24T00-43-36Z` | `sha256:12c7ca4afd784b5d69f3e231d2208148b557fd5175f96da7c28cda6adb699f40` |

A rebuild that does not reproduce these hashes is not this baseline.

### Verified when the baseline was cut

| check | result |
|---|---|
| `python3 -m pytest engine -q` | 256 passed |
| `python3 -m engine.m1.selftest` | `overall_pass: true`, `inertness.pass: true` |

### Measured voice state

| measure | value |
|---|---|
| fabricated record ids | 0.0% — from 30% five commits earlier |
| grounding net coverage | 78% of sentences examined — from 32% |
| voice model | `us.anthropic.claude-sonnet-4-5-20250929-v1:0` |
| gate model | `us.anthropic.claude-haiku-4-5-20251001-v1:0` |
| region | `us-east-1` |
