#pragma once

#include <algorithm>
#include <limits>
#include <stdexcept>
#include <vector>

/**
 * @brief Floyd-Warshall 全源最短路。
 * @note 不可达边使用 long long 最大值；调用方可检查 dist[i][i] < 0 判断负环。
 */
inline std::vector<std::vector<long long>> floyd_warshall(
    std::vector<std::vector<long long>> graph) {
    const int size = static_cast<int>(graph.size());
    for (const auto& row : graph) {
        if (static_cast<int>(row.size()) != size) {
            throw std::invalid_argument("floyd_warshall: matrix must be square");
        }
    }
    const auto infinity = std::numeric_limits<long long>::max();
    const auto lowest = std::numeric_limits<long long>::lowest();
    for (int middle = 0; middle < size; ++middle) {
        for (int from = 0; from < size; ++from) {
            if (graph[from][middle] == infinity) {
                continue;
            }
            for (int to = 0; to < size; ++to) {
                if (graph[middle][to] == infinity) {
                    continue;
                }
                const long long left = graph[from][middle];
                const long long right = graph[middle][to];
                long long candidate;
                if (right > 0 && left > infinity - right) {
                    candidate = infinity;
                } else if (right < 0 && left < lowest - right) {
                    candidate = lowest;
                } else {
                    candidate = left + right;
                }
                graph[from][to] = std::min(graph[from][to], candidate);
            }
        }
    }
    return graph;
}
