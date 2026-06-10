# Guidance Demo Notes

Diffusion-Planner includes a classifier-guidance path. The planner config `diffusion_planner_guidance.yaml` wires:

```yaml
guidance_fn:
  _target_: diffusion_planner.model.guidance.guidance_wrapper.GuidanceWrapper
```

At inference time the decoder passes the guidance function to DPM-Solver as classifier guidance with `guidance_scale=0.5`.

## Official entry points

- `diffusion_planner/config/planner/diffusion_planner_guidance.yaml`
- `diffusion_planner/model/guidance/guidance_wrapper.py`
- `diffusion_planner/model/guidance/collision.py`
- `diffusion_planner/model/guidance/documentation_guidance.md`
- `sim_guidance_demo.sh`

## Windows command

The guidance planner can be selected by replacing the planner config in a nuPlan simulation run:

```powershell
conda run -n diffusion_planner powershell -ExecutionPolicy Bypass `
  -File .\scripts\run_mini_eval.ps1 `
  -NuplanDataRoot "D:\nuplan-data\dataset" `
  -NuplanMapsRoot "D:\nuplan-data\dataset\maps" `
  -NuplanExpRoot "D:\nuplan-data\exp" `
  -ScenarioBuilder "nuplan_mini" `
  -ScenarioFilter "one_of_each_scenario_type" `
  -Worker "sequential" `
  -LimitTotalScenarios 5 `
  -ExperimentUid "dp/guidance_mini5/model" `
  -SummaryPrefix "guidance_mini5_eval" `
  -Planner "diffusion_planner_guidance"
```

## Local result

The guidance run has been executed on the same five mini scenario tokens as the baseline mini5 run.

| Run | Scenarios | Success / Fail | Final score | Mean compute runtime |
| --- | ---: | ---: | ---: | ---: |
| baseline mini5 | 5 | 5 / 0 | 0.9254 | 0.8146 s |
| guidance mini5 | 5 | 5 / 0 | 0.7264 | 0.4459 s |

The guidance run completed successfully, but it reduced the mini5 final score. The main regression was:

| Scenario type | Baseline | Guidance | Main limiting metrics |
| --- | ---: | ---: | --- |
| `stopping_at_stop_sign_with_lead` | 1.0000 | 0.0000 | `ego_is_comfortable=0`, `no_ego_at_fault_collisions=0`, `time_to_collision_within_bound=0` |

This means guidance is not automatically better. On this mini split, the collision/TTC-related hard failure outweighed the small progress improvement in another scenario.

Outputs:

- `results/guidance_mini5_eval_summary.md`
- `results/guidance_mini5_eval_low_score_analysis.md`
- `results/guidance_mini5_eval_latency_summary.md`
- `results/guidance_vs_baseline_mini5.md`
- `results/guidance_vs_baseline_mini5.png`

## Next boundary

The next useful experiment is not simply increasing the number of guidance scenarios. It is to sweep guidance strength, for example `guidance_scale=0.1/0.3/0.5/1.0`, and compare final score, collision, TTC, comfort, and runtime.
