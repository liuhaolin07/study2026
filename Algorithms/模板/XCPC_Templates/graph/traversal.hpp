#pragma once

#include <algorithm>
#include <queue>
#include <stdexcept>
#include <vector>

inline void validate_unweighted_graph(const std::vector<std::vector<int>>& graph) {
    const int size = static_cast<int>(graph.size());
    for (const auto& edges : graph) {
        for (int to : edges) {
            if (to < 0 || to >= size) {
                throw std::out_of_range("graph traversal: edge endpoint out of range");
            }
        }
    }
}

/** @brief BFS 最短边数；不可达顶点距离为 -1。 */
inline std::vector<int> bfs_distance(
    const std::vector<std::vector<int>>& graph, int start) {
    validate_unweighted_graph(graph);
    if (start < 0 || start >= static_cast<int>(graph.size())) {
        throw std::out_of_range("bfs_distance: start vertex out of range");
    }
    std::vector<int> distance(graph.size(), -1);
    std::queue<int> queue;
    distance[start] = 0;
    queue.push(start);
    while (!queue.empty()) {
        const int vertex = queue.front();
        queue.pop();
        for (int next : graph[vertex]) {
            if (distance[next] == -1) {
                distance[next] = distance[vertex] + 1;
                queue.push(next);
            }
        }
    }
    return distance;
}

/** @brief 迭代 DFS 的首次访问顺序。 */
inline std::vector<int> dfs_order(const std::vector<std::vector<int>>& graph,
                                  int start) {
    validate_unweighted_graph(graph);
    if (start < 0 || start >= static_cast<int>(graph.size())) {
        throw std::out_of_range("dfs_order: start vertex out of range");
    }
    std::vector<int> stack{start};
    std::vector<bool> visited(graph.size(), false);
    std::vector<int> order;
    while (!stack.empty()) {
        const int vertex = stack.back();
        stack.pop_back();
        if (visited[vertex]) {
            continue;
        }
        visited[vertex] = true;
        order.push_back(vertex);
        for (auto it = graph[vertex].rbegin(); it != graph[vertex].rend(); ++it) {
            if (!visited[*it]) {
                stack.push_back(*it);
            }
        }
    }
    return order;
}
