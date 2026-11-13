# Metrics and retention definitions

## Event taxonomy (proposed)
| Event | Properties |
|---|---|
| app_open | user_id, ts, platform |
| goal_started | user_id, template |
| goal_created | user_id, goal_id, target_amount, target_date, funding_types[] |
| saving_added | user_id, goal_id, amount, source (round_up / auto / manual) |
| saving_withdrawn | user_id, goal_id, amount |
| goal_completed | user_id, goal_id |
| notification_opened | user_id, type |

## Retention (D1 / D7 / D30)
- **Install/Activation day (day 0):** the date of a user's first `app_open`.
- **D1 retention:** share of day-0 users with an `app_open` on day 1.
- **D7 retention:** same, on day 7. (Strict "on day N" definition; a "within 7 days" window would read higher.)
- **D30 retention:** same, on day 30.
- **Saver retention (the one we care about):** among users who created a goal, share with a `saving_added` event in days 7-13 / 30-36.

Pick one definition per metric and use it for both control and treatment.

## Example query (BigQuery syntax)
See `sql/retention_d1_d7_d30.sql`.
