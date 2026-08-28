#pragma once

#include <algorithm>
#include <stdexcept>
#include <vector>

inline void validate_knapsack_input(const std::vector<int>& weights,
                                    const std::vector<long long>& values,
                                    int capacity) {
    if (weights.size() != values.size()) {
        throw std::invalid_argument("knapsack: weights and values size mismatch");
    }
    if (capacity < 0) {
        throw std::invalid_argument("knapsack: capacity must be non-negative");
    }
    for (int weight : weights) {
        if (weight <= 0) {
            throw std::invalid_argument("knapsack: weights must be positive");
        }
    }
}

/** @brief 0-1 背包最大价值。时间 O(nC)，空间 O(C)。 */
inline long long knapsack_01(const std::vector<int>& weights,
                             const std::vector<long long>& values,
                             int capacity) {
    validate_knapsack_input(weights, values, capacity);
    std::vector<long long> dp(static_cast<std::size_t>(capacity) + 1, 0);
    for (std::size_t i = 0; i < weights.size(); ++i) {
        for (int current = capacity; current >= weights[i]; --current) {
            dp[current] =
                std::max(dp[current], dp[current - weights[i]] + values[i]);
        }
    }
    return dp[capacity];
}

/** @brief 完全背包最大价值。时间 O(nC)，空间 O(C)。 */
inline long long knapsack_complete(const std::vector<int>& weights,
                                   const std::vector<long long>& values,
                                   int capacity) {
    validate_knapsack_input(weights, values, capacity);
    std::vector<long long> dp(static_cast<std::size_t>(capacity) + 1, 0);
    for (std::size_t i = 0; i < weights.size(); ++i) {
        for (int current = weights[i]; current <= capacity; ++current) {
            dp[current] =
                std::max(dp[current], dp[current - weights[i]] + values[i]);
        }
    }
    return dp[capacity];
}
