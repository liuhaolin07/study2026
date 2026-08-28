#pragma once

#include <algorithm>
#include <limits>
#include <stdexcept>
#include <vector>

/**
 * @brief 精确计算 C(n, k)，非法 k 返回 0。
 * @throws std::overflow_error 当结果超出 long long。
 */
inline long long combination(int n, int k) {
    if (n < 0) {
        throw std::invalid_argument("combination: n must be non-negative");
    }
    if (k < 0 || k > n) {
        return 0;
    }
    k = std::min(k, n - k);
    __int128 result = 1;
    for (int i = 1; i <= k; ++i) {
        result = result * (n - k + i) / i;
        if (result > std::numeric_limits<long long>::max()) {
            throw std::overflow_error("combination: result does not fit in long long");
        }
    }
    return static_cast<long long>(result);
}

/** @brief Pascal 递推预处理 C(i,j) mod mod。时间/空间 O(n^2)。 */
inline std::vector<std::vector<long long>> precompute_combinations(
    int n, long long mod) {
    if (n < 0 || mod <= 0) {
        throw std::invalid_argument("precompute_combinations: invalid n or modulus");
    }
    std::vector<std::vector<long long>> table(
        static_cast<std::size_t>(n) + 1,
        std::vector<long long>(static_cast<std::size_t>(n) + 1, 0));
    for (int i = 0; i <= n; ++i) {
        table[i][0] = table[i][i] = 1 % mod;
        for (int j = 1; j < i; ++j) {
            table[i][j] = (table[i - 1][j - 1] + table[i - 1][j]) % mod;
        }
    }
    return table;
}
