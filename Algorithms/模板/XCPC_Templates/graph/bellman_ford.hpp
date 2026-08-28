#pragma once

#include "kruskal.hpp"

#include <limits>
#include <stdexcept>
#include <vector>

struct BellmanFordResult {
    std::vector<long long> distance;
    std::vector<int> previous;
    bool has_reachable_negative_cycle = false;
};

/**
 * @brief Bellman-Ford 单源最短路，可处理负边并检测源点可达的负环。
 * @time_complexity O(VE)
 */
inline BellmanFordResult bellman_ford(int vertex_count,
                                      const std::vector<WeightedEdge>& edges,
                                      int start) {
    if (vertex_count < 0 || start < 0 || start >= vertex_count) {
        throw std::invalid_argument("bellman_ford: invalid vertex count or start");
    }
    for (const auto& [from, to, weight] : edges) {
        (void)weight;
        if (from < 0 || from >= vertex_count || to < 0 || to >= vertex_count) {
            throw std::out_of_range("bellman_ford: edge endpoint out of range");
        }
    }

    const auto infinity = std::numeric_limits<long long>::max();
    BellmanFordResult result{std::vector<long long>(vertex_count, infinity),
                             std::vector<int>(vertex_count, -1), false};
    result.distance[start] = 0;
    for (int iteration = 1; iteration < vertex_count; ++iteration) {
        bool changed = false;
        for (const auto& [from, to, weight] : edges) {
            if (result.distance[from] == infinity) {
                continue;
            }
            const long long candidate = result.distance[from] + weight;
            if (candidate < result.distance[to]) {
                result.distance[to] = candidate;
                result.previous[to] = from;
                changed = true;
            }
        }
        if (!changed) {
            break;
        }
    }
    for (const auto& [from, to, weight] : edges) {
        if (result.distance[from] != infinity &&
            result.distance[from] + weight < result.distance[to]) {
            result.has_reachable_negative_cycle = true;
            break;
        }
    }
    return result;
}
