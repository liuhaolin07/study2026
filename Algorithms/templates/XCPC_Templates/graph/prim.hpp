#pragma once

#include "dijkstra.hpp"

#include <functional>
#include <optional>
#include <queue>
#include <stdexcept>
#include <utility>
#include <vector>

/** @brief Prim 最小生成树；图不连通时返回 std::nullopt。 */
inline std::optional<long long> prim_mst(const WeightedGraph& graph) {
    if (graph.empty()) {
        return 0;
    }
    const int size = static_cast<int>(graph.size());
    for (const auto& edges : graph) {
        for (const auto& [to, weight] : edges) {
            (void)weight;
            if (to < 0 || to >= size) {
                throw std::out_of_range("prim_mst: edge endpoint out of range");
            }
        }
    }

    using State = std::pair<int, int>;
    std::priority_queue<State, std::vector<State>, std::greater<State>> queue;
    std::vector<bool> visited(graph.size(), false);
    queue.push({0, 0});
    long long total_weight = 0;
    int visited_count = 0;
    while (!queue.empty()) {
        const auto [weight, vertex] = queue.top();
        queue.pop();
        if (visited[vertex]) {
            continue;
        }
        visited[vertex] = true;
        total_weight += weight;
        ++visited_count;
        for (const auto& [next, edge_weight] : graph[vertex]) {
            if (!visited[next]) {
                queue.push({edge_weight, next});
            }
        }
    }
    if (visited_count != size) {
        return std::nullopt;
    }
    return total_weight;
}

/** @brief 兼容旧接口；图不连通时返回 -1。 */
inline long long prim(const WeightedGraph& graph, int vertex_count) {
    if (vertex_count != static_cast<int>(graph.size())) {
        throw std::invalid_argument("prim: vertex count does not match graph size");
    }
    return prim_mst(graph).value_or(-1);
}
