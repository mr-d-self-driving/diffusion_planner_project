# Mini Evaluation Low-score Analysis

Source scenarios: 1

The simulations all succeeded. This report only highlights lower-scoring scenarios and the metrics that reduced their weighted score.

| Rank | Scenario Type | Scenario Token | Score | Main limiting metrics |
| ---: | --- | --- | ---: | --- |
| 1 | stopping_at_stop_sign_with_lead | 6bd0988fce0f548b | 1.0000 | none below 0.999 |

Interpretation:

- `ego_is_comfortable=0` usually points to acceleration, jerk, yaw rate, or lateral acceleration exceeding the nuPlan comfort thresholds.
- `speed_limit_compliance<1` means the executed ego trajectory exceeded the mapped speed limit for part of the scenario.
- `ego_progress_along_expert_route<1` means the planner progressed slightly less than the expert route baseline.
- These are mini-split diagnostic results, not paper-level Val14/Test14 conclusions.
