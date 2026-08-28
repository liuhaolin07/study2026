# 模板库

分两层：**比赛骨架**（自己手写）+ **算法头文件库**（可直接复用、带自动化测试）。

## 目录

```
模板/
├── contest.cpp          # 比赛开场直接复制的骨架
├── XCPC_Templates/      # 31 个算法头文件（basic/sorting/data_structure/dp/graph/string/math）
├── tests/               # 72 项自动化测试（run_tests.ps1）
├── docs/MAINTENANCE.md  # 模板维护指南
├── STANDARDS.md         # 代码规范
├── TEMPLATE_GUIDE.md    # 模板编写指南
└── QUICKSTART.md        # 快速上手
```

## 收录规则（重要）

> **每个算法模板必须自己独立写一遍、通过对应模板题，才能收录。**
> 抄来的模板赛场上不敢用，也调不动。

- `contest.cpp` 骨架 + 手写模板 → 参考 [hh2048/XCPC](https://github.com/hh2048/XCPC) 学习风格，不整库照搬
- 建议每个模板单独一个 `.cpp` 文件，文件头注明：适用场景、复杂度、已通过的模板题题号、坑点
- XCPC_Templates 内的头文件改动必须跑通 `tests/run_tests.ps1` 才能提交

## 快速验证

在 PowerShell 中运行：

```powershell
.\tests\run_tests.ps1
```

脚本自动查找 `g++`（fallback: `D:\app_edge\w64devkit\bin\g++.exe`），使用 `-std=c++17 -Wall -Wextra -Werror` 编译两个翻译单元并运行测试。非 ASCII 路径下会把测试可执行文件写到系统临时目录。

## 核心头文件库（XCPC_Templates）

| 分类 | 数量 | 主要内容 |
|---|---:|---|
| `basic` | 4 | 快速幂、GCD/LCM、素数筛、前缀和 |
| `sorting` | 2 | 归并/快速排序、二分查找边界 |
| `data_structure` | 5 | 并查集、树状数组、线段树、懒线段树、Sparse Table |
| `dp` | 4 | LIS、背包、LCS、编辑距离 |
| `graph` | 9 | BFS/DFS、最短路、MST、拓扑排序、二分图匹配 |
| `string` | 4 | KMP、Z 函数、Trie、Manacher |
| `math` | 3 | 组合数、模运算、扩展欧几里得 |

完整文件索引和接口说明见 [XCPC_Templates/README.md](./XCPC_Templates/README.md)。

### 使用方式

将模板根目录加入编译器 include path：

```powershell
g++ -std=c++17 -I".\XCPC_Templates" main.cpp -o main.exe
```

然后按分类包含头文件：

```cpp
#include "data_structure/fenwick_tree.hpp"
#include "graph/dijkstra.hpp"

int main() {
    FenwickTree<long long> sums({1, 2, 3, 4});
    return sums.range_query(1, 3) == 9 ? 0 : 1;
}
```

### 行为约定

- 数组和图顶点统一使用 **0-based** 下标。
- 区间接口使用闭区间 `[left, right]`。
- 非法参数或越界使用标准异常，不静默返回错误结果。
- Dijkstra 拒绝负权边；需要负权边时使用 Bellman-Ford。
- `prim_mst` 和 `kruskal_mst` 在图不连通时返回 `std::nullopt`。
- 所有自由函数均可安全地被多个 `.cpp` 同时包含。

## 学习进度

课程（8 阶段 / 24 月）进度保存在 [`../课程/PROGRESS.md`](../课程/PROGRESS.md)。阶段目录允许逐步填写，不把空目录计为已完成内容。新增或修改模板时遵循 [维护指南](./docs/MAINTENANCE.md)，并先运行完整测试。
