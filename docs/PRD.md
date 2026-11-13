# PRD: Goal-Based Micro-Savings for a Gen-Z UPI App

| | |
|---|---|
| Author | Shravya T |
| Status | Draft v1 (portfolio project, not a shipped product) |
| Type | Product teardown + feature PRD |

## 1. Problem
Young UPI users make many small payments (snacks, rides, subscriptions) and rarely have anything left to show for it at month end. Existing options (savings accounts, mutual-fund apps) feel like adult, high-effort products: they need setup, a minimum amount, and a reason to come back.

**Hypothesis to validate through research:** Gen-Z users will save more, and come back to the app more, if saving is attached to payments they already make and framed around a specific goal.

> Evidence for this section comes from my user interviews (see `research/synthesis_template.md`). Replace the placeholders there with your real findings before sharing this PRD.

## 2. Target users
- **Primary:** college students and early earners, 18-24, UPI-active, irregular or allowance-based income.
- **Secondary:** teens using a guardian-linked account where the rules allow it (see Open Questions).

## 3. Goals and non-goals
**Goals**
1. Let a user create a savings goal in under 60 seconds.
2. Move money into the goal automatically from everyday payments (round-ups) or manually.
3. Make progress visible and rewarding without nudging users to overspend.

**Non-goals (v1)**
- Investing, interest-bearing products, or lending.
- Social/public leaderboards (privacy risk for teens).
- Savings for third parties or group pooling.

## 4. User stories
| # | As a... | I want to... | So that... |
|---|---|---|---|
| 1 | student | create a goal (e.g. "Goa trip, Rs 8,000 by March") | I know what I'm saving for |
| 2 | student | round up each UPI payment to the next Rs 10 into my goal | I save without thinking |
| 3 | student | add a one-time amount or set a weekly auto-save | I control the pace |
| 4 | student | see progress and a projected finish date | I stay motivated |
| 5 | student | pause or withdraw anytime with no penalty | I trust the product |
| 6 | guardian (if applicable) | see a teen's goal progress, not their payments | I support without surveillance |

## 5. Core flow
1. Home -> "Start a goal" card -> pick template (Trip, Gadget, Emergency, Custom).
2. Enter target amount and date -> app suggests a weekly amount.
3. Choose funding: round-ups, weekly auto-save, manual (any combination).
4. Confirm with UPI PIN for the first mandate/transfer.
5. Goal screen: progress ring, streak, projected date, "Add money" button.
6. Completion: celebration, option to withdraw, or start the next goal.

## 6. Requirements
### Must have (v1)
- Create/edit/delete goal; target amount, date, template.
- Round-up rule (nearest Rs 10, cap Rs 50 per payment, monthly cap set by user).
- Manual add and withdraw to the linked bank account at any time.
- Progress screen with projected completion date.
- Push notifications: progress milestones (25/50/75/100%), with a per-goal mute.

### Should have
- Weekly auto-save with amount suggestion.
- Streaks that **never** punish a missed week (streak freeze).

### Later
- Shared goals, gamified challenges, merchant rewards.

## 7. Edge cases and error states
| Case | Expected behavior |
|---|---|
| Round-up would take balance below Rs 0 | Skip that round-up, no overdraft, show "Skipped: low balance" in activity |
| UPI payment fails or is reversed after round-up | Reverse the round-up; show both entries in activity |
| Round-up transfer fails (bank/network) | Retry up to 3 times, then queue and notify the user |
| Goal date passes before target reached | Offer: extend date, increase weekly amount, or close and withdraw |
| User deletes goal with balance | Block delete until balance is withdrawn or moved to another goal |
| Duplicate mandate / double tap | Idempotency key per transfer so a user is never charged twice |
| Withdrawal to a closed/changed bank account | Hold funds, prompt to re-verify account |
| Minor with guardian link removed | Pause auto-save, keep balance accessible per policy |

## 8. Success metrics
| Type | Metric | Definition |
|---|---|---|
| North star | Weekly saving users | Users with at least one saving transaction in the week |
| Activation | Goal created within 7 days of install | created_goal / new users |
| Activation | First saving within 24h of goal creation | |
| Retention | D1 / D7 / D30 | see `docs/metrics_and_retention.md` |
| Engagement | Saving transactions per active saver per month | |
| Guardrail | UPI payment success rate | must not drop vs control |
| Guardrail | Withdrawal rate within 7 days of saving | watch for regret/mistrust |
| Guardrail | Support tickets per 1,000 savers | |

## 9. Rollout and experiment
Staged rollout (internal -> 5% -> 25% -> 100%) with an A/B experiment at the 25% stage. Full design in `docs/experiment_plan.md`. The experiment is designed on paper: no live test was run.

## 10. Risks
- **Regulatory:** holding user funds may need a partner bank or specific licenses. Needs legal review.
- **Trust:** unexpected deductions erode trust, so every round-up must be visible and reversible.
- **Overspending:** rewards must not encourage extra payments just to earn round-ups.
- **Teen safety and consent:** age verification and guardian visibility rules.

## 11. Open questions
1. Which partner bank or product holds the savings balance?
2. What are the age and guardian-link rules for users under 18 in this app?
3. Round-up default: opt-in at goal creation or a later prompt?
4. What minimum goal amount avoids transaction-fee drag?
