#!/usr/bin/env python3
"""Run this FIRST once the AWS account exists - before touching config.py.

Nothing in app/bedrock_llm.py will construct a Bedrock LLM with a guessed
model id - it refuses and tells you to run this instead. This script exists
because guessing wrong is a silent 400 on every real turn, not a warning,
and because "does prompt caching actually work here" is exactly the
question the whole migration turns on (see the cost review: 61% of input
tokens are cache reads at 16x pooling on the first-party API - if that
collapses on Bedrock, the $/hour figure roughly triples).

    export AWS_REGION=us-east-1          # or wherever the account lives
    pip install langchain-aws boto3
    python3 tools/cost/bedrock_preflight.py

Three things, in order, each gating the next:
  1. list what Claude models/inference-profiles are actually callable in
     this region on this account - the exact ids to put in
     bedrock_generation_model_id / bedrock_monitoring_model_id
  2. one real call, checking the response actually comes back in the
     Messages-API shape usage_logging.py parses (usage_metadata,
     input_token_details) - not just that boto3 didn't raise
  3. two calls sharing a prompt, checking whether cache_read_input_tokens
     is nonzero on the second - the one number the whole cost case rests on

Spends at most a few cents. Nothing here writes to settings or .env -
copy the ids it finds into environment variables by hand, deliberately,
so the choice is visible in the diff that turns Bedrock on.
"""
from __future__ import annotations

import argparse
import os
import sys


def check_deps() -> None:
    missing = []
    for mod in ("boto3", "langchain_aws"):
        try:
            __import__(mod)
        except ImportError:
            missing.append(mod)
    if missing:
        sys.exit(f"preflight FAILED - missing: {', '.join(missing)}\n"
                 "pip install -r cic/runtime/requirements.txt\n"
                 "Nothing was spent.")


def check_credentials(region: str) -> None:
    import boto3
    from botocore.exceptions import NoCredentialsError, ClientError

    try:
        sts = boto3.client("sts", region_name=region)
        ident = sts.get_caller_identity()
        print(f"AWS identity: {ident['Arn']}")
    except NoCredentialsError:
        sys.exit("preflight FAILED - no AWS credentials found (env vars, "
                 "~/.aws/config, or instance role). Nothing was spent.")
    except ClientError as exc:
        sys.exit(f"preflight FAILED - STS call rejected: {exc}\nNothing was spent.")


def list_claude_models(region: str) -> list[dict]:
    """Every Anthropic model/profile this account can actually call here.

    Lists BOTH on-demand foundation models and cross-region inference
    profiles - Claude on Bedrock is normally called through a profile
    (id shape "us.anthropic.claude-..."), not the bare foundation-model id,
    and the two lists don't always agree on what's usable.
    """
    import boto3

    client = boto3.client("bedrock", region_name=region)
    found = []

    try:
        for m in client.list_foundation_models(byProvider="anthropic").get("modelSummaries", []):
            found.append({"kind": "foundation-model", "id": m["modelId"],
                         "name": m.get("modelName", "")})
    except Exception as exc:
        print(f"  (list_foundation_models failed: {exc})")

    try:
        for p in client.list_inference_profiles().get("inferenceProfileSummaries", []):
            if "anthropic" in p.get("inferenceProfileId", "").lower():
                found.append({"kind": "inference-profile", "id": p["inferenceProfileId"],
                             "name": p.get("inferenceProfileName", "")})
    except Exception as exc:
        print(f"  (list_inference_profiles failed: {exc})")

    return found


def try_call(model_id: str, region: str) -> tuple[bool, dict]:
    """One real call. Returns (ok, usage_shape_report)."""
    from langchain_aws import ChatAnthropicBedrock
    from langchain_core.messages import HumanMessage

    llm = ChatAnthropicBedrock(model=model_id, region_name=region, max_tokens=16)
    response = llm.invoke([HumanMessage(content="Say OK.")])

    usage_metadata = getattr(response, "usage_metadata", None) or {}
    response_metadata = getattr(response, "response_metadata", None) or {}
    raw_usage = response_metadata.get("usage") or {}

    report = {
        "text": response.content[:60] if isinstance(response.content, str) else str(response.content)[:60],
        "has_usage_metadata": bool(usage_metadata),
        "usage_metadata_keys": sorted(usage_metadata.keys()),
        "has_raw_usage_block": bool(raw_usage),
        "raw_usage_keys": sorted(raw_usage.keys()),
    }
    # This is the exact shape usage_logging.py reads - see that module's
    # docstring. If either of the cache fields is missing under BOTH
    # locations, that logger will silently log 0 for real Bedrock traffic
    # the same way it once did for streamed first-party calls.
    input_token_details = usage_metadata.get("input_token_details") or {}
    report["cache_fields_present"] = (
        "cache_creation_input_tokens" in raw_usage
        or "cache_creation" in input_token_details
    )
    return True, report


def check_caching(model_id: str, region: str) -> None:
    """Two calls sharing a large-enough prefix; is the second a cache read?"""
    from langchain_aws import ChatAnthropicBedrock
    from langchain_core.messages import HumanMessage, SystemMessage

    # Needs to clear the model's minimum cacheable prefix (model-dependent,
    # commonly 1024-4096 tokens on Claude - see shared/prompt-caching.md in
    # the claude-api skill). Padded well past the largest known minimum so
    # a failure here means caching didn't work, not that the prefix was
    # merely too short.
    filler = ("This is filler text to clear the minimum cacheable prefix "
             "on Bedrock. " * 400)
    llm = ChatAnthropicBedrock(model=model_id, region_name=region, max_tokens=8)
    system = [{"type": "text", "text": filler,
              "cache_control": {"type": "ephemeral"}}]

    r1 = llm.invoke([SystemMessage(content=system), HumanMessage(content="Say A.")])
    r2 = llm.invoke([SystemMessage(content=system), HumanMessage(content="Say B.")])

    def cache_read(r):
        raw = (getattr(r, "response_metadata", None) or {}).get("usage") or {}
        if "cache_read_input_tokens" in raw:
            return raw["cache_read_input_tokens"]
        details = (getattr(r, "usage_metadata", None) or {}).get("input_token_details") or {}
        return details.get("cache_read", 0)

    read1, read2 = cache_read(r1), cache_read(r2)
    print(f"  call 1 cache_read_input_tokens: {read1}")
    print(f"  call 2 cache_read_input_tokens: {read2}")
    if read2 > 0:
        print("  CACHING WORKS on this model/region - the 16x pooling factor "
              "the cost review measured is worth re-testing at real traffic.")
    else:
        print("  *** NO CACHE HIT on the second call. Before assuming caching")
        print("  is broken: re-run with --reps 3 (Bedrock write-then-read has")
        print("  the same latency window as first-party - two calls fired back")
        print("  to back can race the write). If it's still zero on a third try,")
        print("  the $/hour projection in the cost review does not carry over -")
        print("  re-measure with tools/cost/analyze_usage_log.py on real traffic")
        print("  before deciding anything about cost.")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--region", default=os.environ.get("AWS_REGION", "us-east-1"))
    ap.add_argument("--model-id", default="",
                    help="skip discovery and test this exact model/profile id")
    ap.add_argument("--skip-cache-check", action="store_true",
                    help="skip step 3 (saves a few cents, ~2000 filler tokens)")
    a = ap.parse_args()

    print("preflight: checking dependencies ...")
    check_deps()

    print(f"preflight: checking AWS credentials (region={a.region}) ...")
    check_credentials(a.region)

    if a.model_id:
        candidates = [{"kind": "manual", "id": a.model_id, "name": ""}]
    else:
        print(f"\npreflight: listing Anthropic models/profiles in {a.region} ...")
        candidates = list_claude_models(a.region)
        if not candidates:
            sys.exit(
                "preflight FAILED - no Anthropic models or inference profiles "
                "visible in this region on this account. Either model access "
                "hasn't been granted yet (Bedrock console -> Model access), or "
                "this is the wrong region. Nothing was spent."
            )
        print(f"  found {len(candidates)}:")
        for c in candidates:
            print(f"    [{c['kind']:17}] {c['id']}  {c['name']}")

    haiku = [c for c in candidates if "haiku" in c["id"].lower()]
    sonnet = [c for c in candidates if "sonnet" in c["id"].lower()]
    pick = (sonnet or haiku or candidates)[0]
    print(f"\npreflight: test-calling {pick['id']!r} ...")
    ok, report = try_call(pick["id"], a.region)
    print(f"  response text: {report['text']!r}")
    print(f"  usage_metadata present: {report['has_usage_metadata']} "
          f"(keys: {report['usage_metadata_keys']})")
    print(f"  raw usage block present: {report['has_raw_usage_block']} "
          f"(keys: {report['raw_usage_keys']})")
    if not report["cache_fields_present"]:
        print("  *** WARNING: cache_creation field not found in EITHER usage")
        print("  shape usage_logging.py reads. If this holds on the real")
        print("  traffic path too, every cache figure this project logs will")
        print("  silently read as 0 for Bedrock calls - audit")
        print("  app/usage_logging.py's field names against this response")
        print("  before trusting any Bedrock cost number.")
    else:
        print("  cache_creation field found - usage_logging.py's existing")
        print("  parse path should work unmodified.")

    if not a.skip_cache_check:
        print(f"\npreflight: checking prompt caching on {pick['id']!r} "
              "(2 calls, ~2000 filler tokens) ...")
        check_caching(pick["id"], a.region)

    print(f"\nNext step: set these in the environment (not committed) once "
          f"you've picked the right ids from the list above -")
    print(f"  BEDROCK_GENERATION_MODEL_ID=<sonnet-class id>")
    print(f"  BEDROCK_MONITORING_MODEL_ID=<haiku-class id>")
    print(f"  LLM_PROVIDER=bedrock")
    print(f"  AWS_REGION={a.region}")


if __name__ == "__main__":
    main()
