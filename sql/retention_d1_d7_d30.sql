-- D1 / D7 / D30 retention by experiment variant (strict "active on day N" definition).
-- Assumes a table of app_open events: `your-project.upi_savings.events`
-- (user_id, event_name, event_ts, variant). Replace names to match your data.
WITH first_open AS (
  SELECT user_id, ANY_VALUE(variant) AS variant, MIN(DATE(event_ts)) AS day0
  FROM `your-project.upi_savings.events`
  WHERE event_name = 'app_open'
  GROUP BY user_id
),
opens AS (
  SELECT DISTINCT user_id, DATE(event_ts) AS open_day
  FROM `your-project.upi_savings.events`
  WHERE event_name = 'app_open'
),
joined AS (
  SELECT f.variant, f.user_id, DATE_DIFF(o.open_day, f.day0, DAY) AS day_n
  FROM first_open f
  JOIN opens o USING (user_id)
)
SELECT
  variant,
  COUNT(DISTINCT user_id)                                          AS users,
  SAFE_DIVIDE(COUNT(DISTINCT IF(day_n = 1,  user_id, NULL)), COUNT(DISTINCT user_id)) AS d1,
  SAFE_DIVIDE(COUNT(DISTINCT IF(day_n = 7,  user_id, NULL)), COUNT(DISTINCT user_id)) AS d7,
  SAFE_DIVIDE(COUNT(DISTINCT IF(day_n = 30, user_id, NULL)), COUNT(DISTINCT user_id)) AS d30
FROM joined
GROUP BY variant;
