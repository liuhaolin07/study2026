#pragma once

#include <functional>
#include <limits>
#include <queue>
#include <stdexcept>
#include <utility>
#include <vector>

using WeightedGraph = std::vector<std::vector<std::pair<int, int>>>;

namespace xcpc_detail {
inline void validate_dijkstra_graph(const WeightedGraph& graph, int start) {
    const int size = static_cast<int>(graph.size());
    if (start < 0 || start >= size) {
        throw std::out_of_range("dijkstra: start vertex out of range");
    }
    for (const auto& edges : graph) {
        for (const auto& [to, weight] : edges) {
            if (to < 0 || to >= size) {
                throw std::out_of_range("dijkstra: edge endpoint out of range");
            }
            if (weight < 0) {
                throw std::invalid_argument(
                    "dijkstra: negative edge; use Bellman-Ford instead");
            }
        }
    }
}
}  // namespace xcpc_detail

/**
 * @brief Dijkstra 单源最短路；不可达距离为 long long 最大值。
 * @time_complexity O((V + E) log V)
 */
inline std::vector<long long> dijkstra(const WeightedGraph& graph, int start) {
    xcpc_detail::validate_dijkstra_graph(graph, start);
    const auto infinity = std::numeric_limits<long long>::max();
    std::vector<long long> distance(graph.size(), infinity);
    using State = std::pair<long long, int>;
    std::priority_queue<State, std::vector<State>, std::greater<State>> queue;

    distance[start] = 0;
    queue.push({0, start});
    while (!queue.empty()) {
        const auto [current_distance, vertex] = queue.top();
        queue.pop();
        if (current_distance != distance[vertex]) {
            continue;
        }
        for (const auto& [next, weight] : graph[vertex]) {
            if (current_distance > infinity - weight) {
                continue;
            }
            const long long candidate = current_distance + weight;
            if (candidate < distance[next]) {
                distance[next] = candidate;
                queue.push({candidate, next});
            }
        }
    }
    return distance;
}
