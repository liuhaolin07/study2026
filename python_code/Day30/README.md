# 🐍 Python-MathModeling

> 30 天 Python 学习计划的最终成果仓库（数学建模方向）
> 计划周期：2026-08 ~ 2026-09

## 目录结构

```
Python-MathModeling
│
├── basics/            # 第1阶段：Python 基础（Day 1-5）
│   ├── day01_基础语法
│   ├── day02_条件与循环
│   ├── day03_数据结构
│   ├── day04_函数
│   └── day05_文件和模块
├── numpy_demo/        # 第2阶段：NumPy 科学计算（Day 6-12）
├── visualization/     # 第3阶段：Matplotlib 可视化（Day 13-17）
├── data_analysis/     # 第4阶段：Pandas 数据分析（Day 18-24）
├── regression/        # 第5阶段：回归与分类（Day 26-27）
├── optimization/      # 第5阶段：优化（Day 28）
└── final_project/     # 综合项目：房价预测（Day 29）
```

## 环境

```bash
pip install numpy pandas matplotlib scipy scikit-learn openpyxl
```

- Python ≥ 3.10
- 所有绘图代码已配置中文字体（Microsoft YaHei）

## 快速导览

| 阶段 | 关键成果 |
|------|----------|
| Python 基础 | 温度转换、成绩文件分析程序 |
| NumPy | **蒙特卡洛求 π**（含收敛性分析图）|
| Matplotlib | **天气数据可视化**（4 图分析报告）|
| Pandas | **校园消费数据分析**（清洗→统计→可视化）|
| 建模实战 | 线性回归 / KNN / 决策树 / 线性规划 / **房价预测综合项目** |

## 学到的核心技能

- 向量化编程与随机模拟（蒙特卡洛方法）
- 数据清洗流水线：缺失值 / 重复值 / 异常值
- 分组聚合分析（groupby / agg / pivot）
- sklearn 建模四步法：fit → predict → evaluate → visualize
- 五步建模流程：问题分析 → 建模 → 处理数据 → 求解 → 可视化

## TODO

- [ ] 补充层次分析法 AHP / TOPSIS 评价模型
- [ ] 时间序列预测专题
- [ ] 把 final_project 换成真实房价数据集重跑
