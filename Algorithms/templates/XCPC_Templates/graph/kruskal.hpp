#pragma once

#include "data_structure/union_find.hpp"

#include <algorithm>
#include <optional>
#include <stdexcept>
#include <tuple>
#include <vector>

using WeightedEdge = std::tuple<int, int, int>;

/** @brief Kruskal 最小生成树；图不连通时返回 std::nullopt。 */
inline std::optional<long long> kruskal_mst(std::vector<WeightedEdge> edges,
                                            int vertex_count) {
    if (vertex_count < 0) {
        throw std::invalid_argument("kruskal_mst: vertex count must be non-negative");
    }
    for (const auto& [from, to, weight] : edges) {
        (void)weight;
        if (from < 0 || from >= vertex_count || to < 0 || to >= vertex_count) {
            throw std::out_of_range("kruskal_mst: edge endpoint out of range");
        }
    }
    std::sort(edges.begin(), edges.end(), [](const auto& left, const auto& right) {
        return std::get<2>(left) < std::get<2>(right);
    });

    UnionFind sets(vertex_count);
    long long total_weight = 0;
    int used = 0;
    for (const auto& [from, to, weight] : edges) {
        if (sets.unite(from, to)) {
            total_weight += weight;
            ++used;
        }
    }
    if (vertex_count == 0 || used == vertex_count - 1) {
        return total_weight;
    }
    return std::nullopt;
}

/** @brief 兼容旧接口；图不连通时返回 -1。 */
inline long long kruskal(std::vector<WeightedEdge>& edges, int vertex_count) {
    return kruskal_mst(edges, vertex_count).value_or(-1);
}
