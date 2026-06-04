# 当前局限和风险

## 没有完整官方 benchmark 指标

当前已完成 nuPlan mini 上的 1 场景 smoke test 和 5 场景 closed-loop nonreactive evaluation，但还没有跑完整官方 challenge split，因此不能声称复现了论文表格中的 Val14/Test14 分数。

当前已配置 mini 数据和地图:

- `NUPLAN_DATA_ROOT=D:\nuplan-data\dataset`
- `NUPLAN_MAPS_ROOT=D:\nuplan-data\dataset\maps`
- `NUPLAN_EXP_ROOT=D:\nuplan-data\exp`

但论文级别评测仍需要更完整的数据 split、场景过滤配置和更大规模评估。

## Synthetic forward 不是性能验证

当前模型前向传播使用 synthetic batch，只能说明:

- 模型结构能运行
- CUDA 能运行
- tensor shape 正确
- 输出没有 NaN/Inf
- checkpoint 能加载

它不能单独说明模型在真实驾驶场景中的规划质量，因此项目进一步接入了 mini closed-loop evaluation。但 mini 结果仍不能替代完整官方 benchmark。

## Windows 不是官方主路径

项目脚本和 nuPlan 生态明显更偏 Linux/bash。Windows 下需要额外兼容处理，尤其是 `fcntl` 和路径格式问题。严格实验建议使用 Linux 或 WSL2。

## 没有重新训练

当前使用官方 checkpoint，没有复现训练过程。重新训练需要大规模 nuPlan 预处理数据和较长 GPU 训练时间。

## 真实场景可视化仍待完善

当前提供的 `visualize_synthetic_trajectory.py` 只用于展示模型输出链路和 plotting 工具；`mini_eval_score_runtime.png` 展示的是评估指标图，不是地图轨迹图。真实场景轨迹展示应使用 nuBoard 或从真实 scenario 中导出地图和轨迹。

## 简历表述边界

可以说:

- 复现并验证了 Diffusion-Planner 核心模型链路
- 完成官方 checkpoint 加载和 CUDA 前向推理
- 打通 nuPlan planner 入口导入
- 完成 nuPlan mini 小规模 closed-loop evaluation
- 解决多类依赖兼容问题

不建议说:

- 完整复现论文指标
- 在 nuPlan benchmark 上达到论文性能
- 完成模型训练
- 完成官方 full split 大规模评测
