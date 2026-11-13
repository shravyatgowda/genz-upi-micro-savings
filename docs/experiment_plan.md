# Experiment plan: goal-based micro-savings (design only)

> **Status: designed, not run.** This is a pre-registered plan written before any launch. No live traffic was used.

## Hypothesis
If new users are offered goal-based savings with round-ups during onboarding, then more of them will still be active on day 7, because saving gives them a reason to return.

## Variants
| | Control | Treatment |
|---|---|---|
| Experience | Current onboarding, no savings entry point | Same onboarding + "Start a goal" card on Home and after first payment |
| Assignment | 50% | 50%, randomized by user_id hash |

## Eligibility
New users, first payment completed, age verified, in launch cities. Exclude internal/test accounts.

## Metrics
- **Primary:** D7 retention (strict day-7 definition in `docs/metrics_and_retention.md`).
- **Secondary:** goal creation rate, first saving within 24h, saving transactions per user, D30 retention.
- **Guardrails:** UPI payment success rate, withdrawal within 7 days, support tickets per 1,000 users, app crash rate. Stop if payment success drops by more than 0.5 pp.

## Sample size
Computed with `src/sample_size.py`. With **assumed** baseline D7 = 20%, target +3 pp absolute, alpha 0.05 (two-sided), power 80%: about **2,943 users per arm (5,886 total)**. The baseline is an assumption; replace it with real data before running. At an assumed 1,000 eligible new users a day this is about 6 days of enrollment plus 7 days to observe D7.

## Analysis plan
- Two-proportion z-test on D7 with 95% CI for the absolute lift.
- Check sample ratio mismatch (expect 50/50) before reading results.
- Segment cuts only as exploration: device, city, acquisition channel.
- Do not stop early on a good-looking interim result. Read at the planned sample size.

## Decision rule
- **Ship** if D7 lift is positive and statistically significant, and no guardrail is breached.
- **Iterate** if lift is flat but goal creation and saving rates are healthy (the entry point may be wrong).
- **Stop** if any guardrail is breached.

## Risks to validity
Novelty effect (re-check D30), interference from marketing campaigns, small segments, users with multiple devices.
