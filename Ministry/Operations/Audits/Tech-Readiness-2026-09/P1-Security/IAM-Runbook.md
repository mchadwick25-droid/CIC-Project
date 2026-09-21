# Production Bedrock identity — policy and setup steps

Tech-Readiness P1-Security item 2. `render.yaml`'s own comment has said
since Stage 3 that `cic-bedrock-dev` (the credential both `cic-engine`
and, until this runbook is followed, `cic-engine-staging` currently run
on) is a DEV identity and "production wants its own, scoped to Bedrock
invoke on the models actually used." This is that policy, plus the exact
steps to create and wire it in. **Creating anything in AWS is Mark's own
account action** — nothing here was created from this sandbox, and
nothing here can be (no AWS credentials or console access from this
environment).

## The policy — `iam-policy-cic-bedrock-prod.json`

Scoped to exactly what `engine/provider/bedrock.py` and `engine/api/config.py`
actually call, in the one region this service runs in (`CIC_API_REGION=us-east-1`,
`render.yaml`):

- **`bedrock:InvokeModel` / `bedrock:InvokeModelWithResponseStream`** on the
  two inference profiles this service resolves at startup
  (`resolve_model_id` in `engine/provider/bedrock.py`, called once per role
  in `_build_real_app`):
  - Safety: `us.anthropic.claude-haiku-4-5-20251001-v1:0` — `render.yaml`
    now pins this to the exact profile id the safety battery was last
    tallied against (`CIC_API_SAFETY_MODEL_PATTERN`, both services), so the
    policy can name it exactly rather than wildcarding.
  - Voice: `CIC_API_VOICE_MODEL_PATTERN` is still left at its code default,
    the loose pattern `us.anthropic.claude-sonnet-4-5` — the resolved
    profile id is date-suffixed and not committed anywhere in this repo
    (by design: `resolve_model_id`'s whole point is never typing a
    date-suffixed id from memory). The policy below scopes this with a
    trailing wildcard (`us.anthropic.claude-sonnet-4-5-*`) rather than a
    blanket `anthropic.claude-*` — tighten it to the exact id, the same way
    the safety pattern was pinned, the next time someone runs the
    equivalent of `engine/m5/safety_script_run.py`'s tally for the voice
    model and commits a pin. Until then this is genuinely least-privilege
    for what the *pattern* can ever match, not a blank check.
- **The same two actions on the underlying foundation-model ARNs**, across
  `us-east-1`/`us-east-2`/`us-west-2`. This is not redundant with the
  inference-profile grant above: AWS's cross-region ("`us.`-prefixed")
  inference profiles route a single logical call to whichever of their
  constituent regions has capacity, and Bedrock's own IAM authorization
  checks the underlying foundation-model ARN in the region actually
  invoked, not just the inference-profile ARN the caller named. A policy
  that grants only the inference-profile ARN is a real, easy-to-hit bug —
  it authorizes at the front door and gets `AccessDenied` at the model
  call itself, intermittently, whichever region a given request happened
  to land in. **The three constituent regions above are AWS's documented
  "US" commercial geography for `us.`-prefixed profiles as of this audit,
  not something this sandbox could verify against the live account (no AWS
  access here) — confirm with `aws bedrock get-inference-profile
  --inference-profile-identifier us.anthropic.claude-haiku-4-5-20251001-v1:0`
  (and the sonnet equivalent, once pinned) before applying, and adjust the
  region list if it disagrees.**
- **`bedrock:ListInferenceProfiles`**, `Resource: "*"` — this is what
  `resolve_model_id` calls to turn a pattern into an id at every startup.
  It's a list/read action over the whole account+region's profile catalog,
  not scoped to a specific resource by AWS's own action reference, and it
  reveals model names/ids, not participant data — `Resource: "*"` here is
  the correct minimum, not a hedge.

Nothing else. No `bedrock:*`, no other service, no wildcard action.

## Two identities, one policy — `cic-bedrock-prod` and `cic-bedrock-staging`

`render.yaml`'s own comment on `cic-engine-staging`'s AWS keys already
calls for **separate credentials, not separate scope** — staging and prod
call the exact same two models in the exact same region, so the same
policy document is correct for both; the separation that matters is
blast radius (a compromised staging key should reach nothing prod's key
can), which comes from two distinct IAM users/access keys, not two
different policies.

## Setup steps (Mark, in the AWS console — nothing here is executable from a build thread)

1. **Fill in the account id.** `iam-policy-cic-bedrock-prod.json` has
   `<AWS_ACCOUNT_ID>` in six places — replace with the real 12-digit
   account id (IAM console, top-right account menu, or `aws sts
   get-caller-identity`).
2. **Verify the cross-region geography** (see above) before applying —
   adjust the foundation-model region list if the live account's inference
   profile disagrees with the assumption stated here.
3. **Create the managed policy.** IAM → Policies → Create policy → JSON tab
   → paste the filled-in document → name it `cic-bedrock-invoke` (or
   similar) → create.
4. **Create `cic-bedrock-prod`.** IAM → Users → Create user → no console
   access (programmatic only) → attach the `cic-bedrock-invoke` policy
   directly → create → Security credentials tab → Create access key →
   "Application running outside AWS" → save the access key id and secret
   somewhere Mark controls (a password manager, not this repo).
5. **Create `cic-bedrock-staging`** the same way, attaching the same
   policy, its own separate access key.
6. **Render dashboard — `cic-engine` (prod).** Settings → Environment →
   set `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` to the
   `cic-bedrock-prod` pair (these are already `sync: false` in
   `render.yaml`, so this has always been a dashboard-only step). Save —
   Render redeploys automatically on an env var change for this service.
7. **Render dashboard — `cic-engine-staging`.** Same, with the
   `cic-bedrock-staging` pair.
8. **Smoke-test both.** `curl .../health`, then a real `POST /api/session`
   + one message against each, confirming a normal 200/201 response (not a
   502 `provider call failed` — that would mean the new identity can't
   actually invoke the resolved model, most likely the cross-region
   foundation-model grant in step 2 needs adjusting).
9. **Retire `cic-bedrock-dev` from production use.** Once both services are
   confirmed running on their own identities, deactivate (don't delete yet
   — keep a fast rollback path) the access key `cic-bedrock-dev` was using
   for these two services. After a stable period with no rollback needed,
   delete that access key; whether the `cic-bedrock-dev` IAM user/policy
   itself should be scoped down or retired entirely is Mark's call,
   depending on whether anything else (a script run by hand,
   `engine/provider/preflight.py`, `engine/m5/safety_script_run.py`) still
   legitimately uses it for local/manual runs outside this deployed
   service.

## What this doesn't cover

`engine/m4/object_storage.py`'s R2 credentials
(`CIC_API_PACKAGE_BUCKET*`) are a separate system (Cloudflare R2, not
AWS IAM) with their own runbook
(`Ministry/Operations/Standing/CiC_Object_Storage_Runbook.md`) — out of
scope here, this runbook is Bedrock invoke only.
