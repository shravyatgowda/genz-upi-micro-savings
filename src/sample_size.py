"""Sample-size calculator for the two-proportion A/B test in docs/experiment_plan.md.

Standard library only. Usage:
    python src/sample_size.py                       # defaults from the experiment plan
    python src/sample_size.py --baseline 0.20 --mde 0.03 --power 0.8 --alpha 0.05
"""
import argparse
import math
from statistics import NormalDist


def per_arm(baseline: float, mde_abs: float, alpha: float = 0.05, power: float = 0.80) -> int:
    """Users needed per arm to detect an absolute lift of `mde_abs` (two-sided)."""
    p1, p2 = baseline, baseline + mde_abs
    pbar = (p1 + p2) / 2
    z_a = NormalDist().inv_cdf(1 - alpha / 2)
    z_b = NormalDist().inv_cdf(power)
    num = (z_a * math.sqrt(2 * pbar * (1 - pbar)) + z_b * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(num / (mde_abs ** 2))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", type=float, default=0.20, help="baseline D7 retention (ASSUMPTION)")
    ap.add_argument("--mde", type=float, default=0.03, help="absolute minimum detectable effect")
    ap.add_argument("--alpha", type=float, default=0.05)
    ap.add_argument("--power", type=float, default=0.80)
    ap.add_argument("--daily-new-users", type=int, default=1000, help="eligible new users per day (ASSUMPTION)")
    a = ap.parse_args()

    n = per_arm(a.baseline, a.mde, a.alpha, a.power)
    total = 2 * n
    days = math.ceil(total / a.daily_new_users)
    print(f"Baseline {a.baseline:.1%} -> target {a.baseline + a.mde:.1%} (absolute +{a.mde:.1%})")
    print(f"alpha={a.alpha}, power={a.power}")
    print(f"Users per arm: {n:,} | total: {total:,}")
    print(f"At {a.daily_new_users:,} eligible new users/day: ~{days} days of enrollment (+7 days to observe D7)")


if __name__ == "__main__":
    main()
