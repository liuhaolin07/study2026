# 算法模板与竞赛学习库

这是一个以 C++17 为主的竞赛算法学习仓库。仓库分为两部分：

- `资源库/模板收集/XCPC_Templates/`：可直接复用并有自动化测试的核心模板库。
- `阶段1_基础数据结构/` 至 `阶段8_综合训练和优化/`：按主题组织的个人学习与练习目录。

当前核心库包含 **31 个头文件**，自动化测试包含 **72 项检查**。

## 快速验证

在 PowerShell 中运行：

```powershell
.\tests\run_tests.ps1
```

脚本会自动查找 `g++`，使用 `-std=c++17 -Wall -Wextra -Werror` 编译两个翻译单元并运行测试。如果 `g++` 不在 `PATH` 中：

```powershell
.\tests\run_tests.ps1 -Compiler "D:\path\to\g++.exe"
```

## 核心模板

| 分类 | 数量 | 主要内容 |
|---|---:|---|
| `basic` | 4 | 快速幂、GCD/LCM、素数筛、前缀和 |
| `sorting` | 2 | 归并/快速排序、二分查找边界 |
| `data_structure` | 5 | 并查集、树状数组、线段树、懒线段树、Sparse Table |
| `dp` | 4 | LIS、背包、LCS、编辑距离 |
| `graph` | 9 | BFS/DFS、最短路、MST、拓扑排序、二分图匹配 |
| `string` | 4 | KMP、Z 函数、Trie、Manacher |
| `math` | 3 | 组合数、模运算、扩展欧几里得 |

完整文件索引和接口说明见 [XCPC_Templates/README.md](./资源库/模板收集/XCPC_Templates/README.md)。

## 使用方式

将模板根目录加入编译器 include path：

```powershell
g++ -std=c++17 -I".\资源库\模板收集\XCPC_Templates" main.cpp -o main.exe
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

## 行为约定

- 数组和图顶点统一使用 **0-based** 下标。
- 区间接口使用闭区间 `[left, right]`。
- 非法参数或越界使用标准异常，不静默返回错误结果。
- Dijkstra 拒绝负权边；需要负权边时使用 Bellman-Ford。
- `prim_mst` 和 `kruskal_mst` 在图不连通时返回 `std::nullopt`。
- 所有自由函数均可安全地被多个 `.cpp` 同时包含。

## 学习进度

个人进度保存在 [PROGRESS.md](./PROGRESS.md)。阶段目录允许逐步填写，不把空目录计为已完成内容。新增或修改模板时遵循 [维护指南](./docs/MAINTENANCE.md)，并先运行完整测试。
