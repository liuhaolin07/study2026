#pragma once

#include <algorithm>
#include <string>
#include <vector>

/** @brief Levenshtein 编辑距离。时间 O(nm)，空间 O(m)。 */
inline int edit_distance(const std::string& source, const std::string& target) {
    std::vector<int> previous(target.size() + 1);
    std::vector<int> current(target.size() + 1);
    for (std::size_t j = 0; j <= target.size(); ++j) {
        previous[j] = static_cast<int>(j);
    }
    for (std::size_t i = 1; i <= source.size(); ++i) {
        current[0] = static_cast<int>(i);
        for (std::size_t j = 1; j <= target.size(); ++j) {
            const int replace_cost = source[i - 1] == target[j - 1] ? 0 : 1;
            current[j] = std::min({previous[j] + 1, current[j - 1] + 1,
                                   previous[j - 1] + replace_cost});
        }
        std::swap(previous, current);
    }
    return previous.back();
}
