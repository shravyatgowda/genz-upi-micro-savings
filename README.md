# Gen-Z UPI & Micro-Savings: Product Teardown, PRD and Prototype

A product case study: a goal-based micro-savings feature (round-ups from everyday UPI payments) for young users. It includes the PRD, research kit, success metrics, an A/B experiment design, and a prototype.

> **What this is and isn't:** a portfolio project. The A/B experiment is **designed on paper only** (no live test was run), and the baseline numbers in the sample-size calculator are assumptions.

## What's inside
| Path | What it is |
|---|---|
| `docs/PRD.md` | Problem, users, goals, user stories, flows, edge cases, metrics, risks |
| `docs/metrics_and_retention.md` | Event taxonomy and D1 / D7 / D30 definitions |
| `docs/experiment_plan.md` | Hypothesis, variants, guardrails, sample size, decision rule |
| `research/` | Interview guide and a synthesis template for your real findings |
| `prototype/` | Clickable prototype (built with v0 and Cursor) |
| `src/sample_size.py` | A/B sample-size calculator (standard library only) |
| `sql/retention_d1_d7_d30.sql` | Retention-by-variant query (BigQuery syntax) |

## Quick start
```bash
python src/sample_size.py                          # defaults from the experiment plan
python src/sample_size.py --baseline 0.25 --mde 0.02
```

## Links
- **Prototype:** _add your live link_
- **Related project:** E-Commerce Funnel & Cohort Retention Analysis _(add repo link)_

## Skills shown
User research, PRD writing, metric definition, experiment design, SQL, rapid AI prototyping.

## License
MIT. See `LICENSE`.
