# XCPC C++17 核心模板库

所有头文件都应能独立包含，并通过根目录 `tests/run_tests.ps1` 的多编译单元测试。

## 文件索引

### 基础与排序

| 文件 | 功能 | 复杂度 |
|---|---|---|
| `basic/fast_power.hpp` | 防乘法溢出的模快速幂 | O(log exp) |
| `basic/gcd.hpp` | GCD / LCM | O(log min(a,b)) |
| `basic/prime_sieve.hpp` | 埃氏筛、线性筛 | O(n log log n) / O(n) |
| `basic/prefix_sum.hpp` | 一维前缀和 | 构建 O(n)，查询 O(1) |
| `sorting/sorting.hpp` | 归并排序、三路快速排序 | O(n log n) 平均 |
| `sorting/binary_search.hpp` | lower/upper bound、精确二分 | O(log n) |

### 数据结构

| 文件 | 功能 | 复杂度 |
|---|---|---|
| `data_structure/union_find.hpp` | 路径压缩并查集 | 均摊 O(alpha(n)) |
| `data_structure/fenwick_tree.hpp` | 单点加、区间和 | O(log n) |
| `data_structure/segment_tree.hpp` | 单点赋值、区间和 | O(log n) |
| `data_structure/segment_tree_lazy.hpp` | 区间加、区间和 | O(log n) |
| `data_structure/sparse_table.hpp` | 静态区间最小值 | 构建 O(n log n)，查询 O(1) |

### 动态规划

| 文件 | 功能 | 复杂度 |
|---|---|---|
| `dp/lis.hpp` | LIS 长度与序列 | O(n log n) |
| `dp/knapsack.hpp` | 0-1 / 完全背包 | O(nC) |
| `dp/lcs.hpp` | LCS 长度与序列 | O(nm) |
| `dp/edit_distance.hpp` | Levenshtein 编辑距离 | O(nm) |

### 图论

| 文件 | 功能 | 复杂度 |
|---|---|---|
| `graph/traversal.hpp` | BFS 距离、DFS 顺序 | O(V+E) |
| `graph/dijkstra.hpp` | 非负权单源最短路 | O((V+E) log V) |
| `graph/dijkstra_with_path.hpp` | 最短路与路径重建 | O((V+E) log V) |
| `graph/bellman_ford.hpp` | 负权最短路、负环检测 | O(VE) |
| `graph/floyd_warshall.hpp` | 全源最短路 | O(V^3) |
| `graph/kruskal.hpp` | Kruskal MST | O(E log E) |
| `graph/prim.hpp` | Prim MST | O(E log V) |
| `graph/topological_sort.hpp` | Kahn 拓扑排序 | O(V+E) |
| `graph/bipartite_matching.hpp` | 二分图最大匹配 | O(VE) |

### 字符串与数学

| 文件 | 功能 | 复杂度 |
|---|---|---|
| `string/kmp.hpp` | KMP 全部匹配位置 | O(n+m) |
| `string/z_function.hpp` | Z 函数与模式匹配 | O(n+m) |
| `string/trie.hpp` | 小写字母 Trie | O(L) |
| `string/manacher.hpp` | 最长回文子串 | O(n) |
| `math/combination.hpp` | 组合数与 Pascal 表 | O(k) / O(n^2) |
| `math/modular_arithmetic.hpp` | 模加减乘除、幂与逆元 | O(log MOD) |
| `math/extended_gcd.hpp` | 扩展 GCD、任意模逆元 | O(log min(a,b)) |

## 示例

```cpp
#include "graph/dijkstra.hpp"

int main() {
    WeightedGraph graph(3);
    graph[0] = {{1, 2}, {2, 5}};
    graph[1] = {{2, 1}};
    const auto distance = dijkstra(graph, 0);
    return distance[2] == 3 ? 0 : 1;
}
```

接口的统一约定和新增模板流程见项目根目录的 `docs/MAINTENANCE.md`。
