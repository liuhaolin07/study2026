#pragma once

#include <queue>
#include <stdexcept>
#include <vector>

/** @brief Kahn 拓扑排序；有环时返回空数组。 */
inline std::vector<int> topological_sort(
    const std::vector<std::vector<int>>& graph, int vertex_count) {
    if (vertex_count != static_cast<int>(graph.size())) {
        throw std::invalid_argument(
            "topological_sort: vertex count does not match graph size");
    }
    std::vector<int> indegree(vertex_count, 0);
    for (const auto& edges : graph) {
        for (int to : edges) {
            if (to < 0 || to >= vertex_count) {
                throw std::out_of_range(
                    "topological_sort: edge endpoint out of range");
            }
            ++indegree[to];
        }
    }
    std::queue<int> queue;
    for (int vertex = 0; vertex < vertex_count; ++vertex) {
        if (indegree[vertex] == 0) {
            queue.push(vertex);
        }
    }
    std::vector<int> order;
    while (!queue.empty()) {
        const int vertex = queue.front();
        queue.pop();
        order.push_back(vertex);
        for (int next : graph[vertex]) {
            if (--indegree[next] == 0) {
                queue.push(next);
            }
        }
    }
    if (static_cast<int>(order.size()) != vertex_count) {
        return {};
    }
    return order;
}
