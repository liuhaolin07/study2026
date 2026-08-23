# 图论

- `traversal.hpp`：BFS 距离与迭代 DFS 顺序。
- `dijkstra.hpp` / `dijkstra_with_path.hpp`：非负权最短路与路径重建。
- `bellman_ford.hpp`：负权最短路与可达负环检测。
- `floyd_warshall.hpp`：全源最短路。
- `kruskal.hpp` / `prim.hpp`：最小生成树，非连通图返回 `std::nullopt`。
- `topological_sort.hpp`：拓扑排序，有环返回空数组。
- `bipartite_matching.hpp`：二分图最大匹配。

邻接表顶点均为 0-based。`WeightedGraph` 的边格式为 `{to, weight}`，`WeightedEdge` 的格式为 `{from, to, weight}`。
