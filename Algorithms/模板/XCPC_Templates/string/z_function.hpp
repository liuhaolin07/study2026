#pragma once

#include <algorithm>
#include <string>
#include <vector>

/** @brief Z 函数，z[i] 是 text 与 text[i..] 的最长公共前缀长度。 */
inline std::vector<int> z_function(const std::string& text) {
    const int size = static_cast<int>(text.size());
    std::vector<int> z(size, 0);
    for (int i = 1, left = 0, right = 0; i < size; ++i) {
        if (i <= right) {
            z[i] = std::min(right - i + 1, z[i - left]);
        }
        while (i + z[i] < size && text[z[i]] == text[i + z[i]]) {
            ++z[i];
        }
        if (i + z[i] - 1 > right) {
            left = i;
            right = i + z[i] - 1;
        }
    }
    if (!z.empty()) {
        z[0] = size;
    }
    return z;
}

/** @brief 用 Z 函数查找所有匹配起点。 */
inline std::vector<int> z_search(const std::string& text,
                                 const std::string& pattern) {
    if (pattern.empty()) {
        return {0};
    }
    std::vector<int> result;
    std::string combined = pattern;
    combined.push_back('\0');
    combined += text;
    const auto z = z_function(combined);
    const int offset = static_cast<int>(pattern.size()) + 1;
    for (int i = offset; i < static_cast<int>(combined.size()); ++i) {
        if (z[i] >= static_cast<int>(pattern.size())) {
            result.push_back(i - offset);
        }
    }
    return result;
}
