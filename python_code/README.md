# Python 30 天学习计划 · 支撑材料

> 依据《30天计划》（Obsidian: 计算机语言/Python/30天计划.md）配套编写。
> 每天一个文件夹：`test.py`（可运行示例+练习）+ `*.md`（学习笔记），部分含数据文件。

## 进度对照

| 阶段 | 天数 | 文件夹 | 状态 |
|------|------|--------|------|
| 一、Python基础 | Day 1 | Day1（环境+语法） | ✅ |
| | Day 2 | Day2（条件与循环） | ✅ |
| | Day 3 | Day3（数据结构） | ✅ |
| | Day 4 | Day4（函数） | ✅ |
| | Day 5 | Day5（文件和模块 + scores.txt/csv） | ✅ |
| 二、NumPy | Day 6 | Day6（ndarray入门） | ✅ |
| | Day 7 | Day7（矩阵运算/线代） | ✅ |
| | Day 8 | Day8（随机数模拟） | ✅ |
| | Day 9 | Day9（统计计算） | ✅ |
| | Day 10-12 | Day10-12（项目：蒙特卡洛求π） | ✅ |
| 三、Matplotlib | Day 13 | Day13（plot/scatter） | ✅ |
| | Day 14 | Day14（subplot多图） | ✅ |
| | Day 15 | Day15（bar/histogram） | ✅ |
| | Day 16-17 | Day16-17（项目：天气可视化） | ✅ |
| 四、Pandas | Day 18 | Day18（DataFrame入门） | ✅ |
| | Day 19 | Day19（csv/excel读取+students.csv） | ✅ |
| | Day 20 | Day20（清洗+messy_students.csv） | ✅ |
| | Day 21 | Day21（筛选排序） | ✅ |
| | Day 22 | Day22（groupby聚合） | ✅ |
| | Day 23-24 | Day23-24（项目：校园消费分析） | ✅ |
| 五、数模实战 | Day 25 | Day25（建模流程+人口模型） | ✅ |
| | Day 26 | Day26（线性回归） | ✅ |
| | Day 27 | Day27（KNN/决策树） | ✅ |
| | Day 28 | Day28（scipy优化） | ✅ |
| | Day 29 | Day29（项目：预测房价） | ✅ |
| | Day 30 | Day30（GitHub整理README模板） | ✅ |

## 环境准备

```bash
pip install numpy pandas matplotlib scipy scikit-learn openpyxl
```

Day 1–5 只需标准库；Day 6 起按上表安装。所有绘图脚本已配置 Windows 中文字体。

## 使用方式

1. 进入当天文件夹，先读 `*.md` 笔记；
2. 运行 `python test.py`（或各项目同名主脚本），对照输出理解代码；
3. 完成笔记末尾的「今日任务验收」和练习；
4. 项目文件夹会生成图片/csv，可对照检查自己的运行结果。
