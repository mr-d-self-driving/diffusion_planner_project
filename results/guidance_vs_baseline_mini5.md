# Evaluation Run Comparison

Baseline: `baseline_mini5`

Candidate: `guidance_mini5`

## Final Score

| Metric | Baseline | Candidate | Delta |
| --- | ---: | ---: | ---: |
| score | 0.9254 | 0.7264 | -0.1990 |
| ego_is_comfortable | 0.6000 | 0.4000 | -0.2000 |
| ego_progress_along_expert_route | 0.9856 | 0.9924 | 0.0068 |
| no_ego_at_fault_collisions | 1.0000 | 0.8000 | -0.2000 |
| speed_limit_compliance | 0.9197 | 0.9151 | -0.0046 |
| time_to_collision_within_bound | 1.0000 | 0.8000 | -0.2000 |

## Scenario Score Delta

| Scenario Type | Scenario Token | Baseline | Candidate | Delta | Main candidate limits |
| --- | --- | ---: | ---: | ---: | --- |
| stopping_at_stop_sign_with_lead | 6bd0988fce0f548b | 1.0000 | 0.0000 | -1.0000 | ego_is_comfortable=0.0000; no_ego_at_fault_collisions=0.0000; time_to_collision_within_bound=0.0000 |
| on_pickup_dropoff | d0b68e15688c58ad | 0.8880 | 0.8855 | -0.0025 | ego_progress_along_expert_route=0.9733; speed_limit_compliance=0.5756 |
| near_multiple_vehicles | 1f151e15c9cf5c81 | 0.8750 | 0.8750 | 0.0000 | ego_is_comfortable=0.0000 |
| starting_protected_noncross_turn | aa8237ebd54f5a0b | 1.0000 | 1.0000 | 0.0000 | none below 0.999 |
| accelerating_at_traffic_light_without_lead | 99ca544752f255ad | 0.8641 | 0.8714 | 0.0073 | ego_is_comfortable=0.0000; ego_progress_along_expert_route=0.9885 |

## Interpretation

- A positive delta means the candidate run scored higher than the baseline on the same scenario token.
- A zero candidate score usually indicates a hard metric failure such as at-fault collision or time-to-collision violation.
- This comparison uses the same five mini scenario tokens, so it is useful for debugging guidance behavior, but it is still not a paper-level benchmark.
