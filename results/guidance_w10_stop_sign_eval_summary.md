# nuPlan mini evaluation summary

- generated_at: `2026-06-11 23:49:55`
- run_root: `D:\nuplan-data\exp\exp\simulation\closed_loop_nonreactive_agents\dp\guidance_w10_stop_sign\model`
- aggregator_file: `closed_loop_nonreactive_agents_weighted_average_metrics_2026.06.11.23.48.19.parquet`

## Run status

| total | succeeded | failed | mean_duration_s | mean_compute_runtime_s | median_compute_runtime_s |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | 0 | 73.3427 | 0.4532 | 0.3879 |

## Final score

| score |
| --- |
| 1 |

## Aggregated metric components

| metric | value |
| --- | --- |
| drivable_area_compliance | 1 |
| driving_direction_compliance | 1 |
| ego_is_comfortable | 1 |
| ego_is_making_progress | 1 |
| ego_progress_along_expert_route | 1 |
| no_ego_at_fault_collisions | 1 |
| speed_limit_compliance | 1 |
| time_to_collision_within_bound | 1 |

## Scenario runner report

| succeeded | scenario_name | scenario_type | score | log_name | planner | duration_s | mean_runtime_s | error |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| True | 6bd0988fce0f548b | stopping_at_stop_sign_with_lead | 1 | 2021.07.16.18.06.21_veh-38_04933_05307 | diffusion_planner | 73.3427 | 0.4532 |  |

## Metric files

| metric_rows |
| --- |
| 16 |

## Boundary

This is a mini-split engineering evaluation. It verifies the local closed-loop pipeline, but it is not a paper-score reproduction on the official full benchmark split.
