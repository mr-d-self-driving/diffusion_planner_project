# Stop-sign Guidance Trajectory Comparison

Scenario: `stopping_at_stop_sign_with_lead` / `6bd0988fce0f548b`

| Run | Scale | Score | Path length | Avg error to expert | Max error | Endpoint error |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| baseline | 0 | 1.0000 | 7.162 m | 1.388 m | 1.965 m | 1.965 m |
| scale_0.5_weight_3.0 | 0.5 | 0.0000 | 17.105 m | 7.971 m | 11.879 m | 11.879 m |
| scale_0.5_weight_1.0 | 0.5 | 1.0000 | 7.302 m | 1.469 m | 2.103 m | 2.103 m |

## Takeaways

- Successful runs in this scenario: `baseline`, `scale_0.5_weight_1.0`. Failed hard-score runs: `scale_0.5_weight_3.0`.
- Closest executed path to the expert by average error: `baseline`.
- Largest average deviation from the expert: `scale_0.5_weight_3.0`.
- Failed runs have executed path lengths in the range `17.105-17.105 m`, compared with baseline `7.162 m`.
- The metric score still matters more than geometric closeness alone: collision/TTC hard failures can occur even when the path shape looks broadly plausible.
- This figure is a static trajectory diagnostic. NuBoard is still needed to inspect actor-level interactions frame by frame.
