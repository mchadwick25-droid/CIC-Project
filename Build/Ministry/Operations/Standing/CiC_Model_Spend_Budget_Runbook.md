# Model spend: AWS Budget deny action, and the monthly reconciliation

Decision 55. Mark creates the AWS items below; the build thread does not hold the keys. Bedrock stays the primary route. This page is the stop that Bedrock did not have.

## 1. The deny policy (Mark creates, once)

In IAM, create a customer-managed policy named `CicBedrockInvokeDeny` with this JSON. It blocks every model call and nothing else, so the engine keeps running and the Facilitator can still speak its fixed text.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyModelInvocation",
      "Effect": "Deny",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream",
        "bedrock:Converse",
        "bedrock:ConverseStream"
      ],
      "Resource": "*"
    }
  ]
}
```

Do not attach it to anything. The Budget action attaches it when the limit is hit.

## 2. The Budget (Mark creates, once)

AWS Billing, Budgets, Create budget, Customized, Cost budget.

| Setting | Value |
|---|---|
| Period | Monthly, recurring |
| Amount | Mark's monthly model ceiling, in dollars |
| Scope | Filter on Service: Claude models sold through AWS Marketplace, plus Amazon Bedrock (Bedrock usage of these models bills as Marketplace) |
| Alert 1 | 50% of actual, email to Mark |
| Alert 2 | 80% of actual, email to Mark |
| Alert 3 | 100% of actual, email to Mark, plus the action below |

Action on Alert 3: Add action, role = the IAM user or role whose keys the engine uses on Render, policy = `CicBedrockInvokeDeny`, Run automatically.

Billing data lags by hours, so this is a stop within a day, not a per-call cap. The door's weekly ceiling remains the fast control.

## 3. Lifting the stop

Detach `CicBedrockInvokeDeny` from the role (IAM, Roles, the role, Permissions). Do it only after deciding to raise the ceiling or wait for the month to roll over.

## 4. Monthly reconciliation (spec principle 13)

After each month's invoice, from a shell holding a copy of the usage database:

    python -m engine.m8.reconcile --db <usage.db> --month YYYY-MM --route bedrock --invoice-dollars <invoice line>

It prices the month's log by route and prints the invoice-to-list ratio. The door's invoice factor (1.35) is checked against that line. Out of tolerance (5% on the route price) exits non-zero and means the price table or the factor needs a decision; it is logged in the Decision-Log, not adjusted quietly.

## 5. Global profiles

`python -m engine.provider.list_profiles --region us-east-1` from the live-tests environment makes one control-plane call and reports which global profiles exist for the voice and safety patterns. A listed profile may still be denied, so moving a pattern to a global id is a settings change followed by the capped live test Mark approves by name.
