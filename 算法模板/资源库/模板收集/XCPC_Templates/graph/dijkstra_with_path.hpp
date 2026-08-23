#pragma once

#include "dijkstra.hpp"

#include <algorithm>
#include <limits>
#include <vector>

/** @brief Dijkstra，额外返回每个顶点在最短路树中的前驱。 */
inline std::pair<std::vector<long long>, std::vector<int>> dijkstra_with_path(
    const WeightedGraph& graph, int start) {
    xcpc_detail::validate_dijkstra_graph(graph, start);
    const auto infinity = std::numeric_limits<long long>::max();
    std::vector<long long> distance(graph.size(), infinity);
    std::vector<int> previous(graph.size(), -1);
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
                previous[next] = vertex;
                queue.push({candidate, next});
            }
        }
    }
    return {distance, previous};
}

inline std::vector<int> reconstruct_path(const std::vector<int>& previous,
                                         int start, int end) {
    const int size = static_cast<int>(previous.size());
    if (start < 0 || start >= size || end < 0 || end >= size) {
        throw std::out_of_range("reconstruct_path: vertex out of range");
    }
    std::vector<int> path;
    int vertex = end;
    for (int steps = 0; vertex != -1 && steps <= size; ++steps) {
        path.push_back(vertex);
        if (vertex == start) {
            std::reverse(path.begin(), path.end());
            return path;
        }
        vertex = previous[vertex];
        if (vertex < -1 || vertex >= size) {
            throw std::invalid_argument("reconstruct_path: invalid predecessor");
        }
    }
    return {};
}
