#pragma once

#include <algorithm>
#include <string>
#include <vector>

/** @brief 最长公共子序列长度。时间 O(nm)，空间 O(m)。 */
inline int lcs_length(const std::string& first, const std::string& second) {
    std::vector<int> previous(second.size() + 1, 0);
    std::vector<int> current(second.size() + 1, 0);
    for (char left : first) {
        for (std::size_t j = 1; j <= second.size(); ++j) {
            if (left == second[j - 1]) {
                current[j] = previous[j - 1] + 1;
            } else {
                current[j] = std::max(previous[j], current[j - 1]);
            }
        }
        std::swap(previous, current);
        std::fill(current.begin(), current.end(), 0);
    }
    return previous.back();
}

/** @brief 返回一个最长公共子序列。时间/空间 O(nm)。 */
inline std::string lcs_sequence(const std::string& first,
                                const std::string& second) {
    std::vector<std::vector<int>> dp(
        first.size() + 1, std::vector<int>(second.size() + 1, 0));
    for (std::size_t i = 1; i <= first.size(); ++i) {
        for (std::size_t j = 1; j <= second.size(); ++j) {
            if (first[i - 1] == second[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = std::max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    std::string result;
    std::size_t i = first.size();
    std::size_t j = second.size();
    while (i > 0 && j > 0) {
        if (first[i - 1] == second[j - 1]) {
            result.push_back(first[i - 1]);
            --i;
            --j;
        } else if (dp[i - 1][j] >= dp[i][j - 1]) {
            --i;
        } else {
            --j;
        }
    }
    std::reverse(result.begin(), result.end());
    return result;
}
