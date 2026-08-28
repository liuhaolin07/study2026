#pragma once

#include <vector>
#include <string>

/**
 * @brief KMP 算法 (字符串匹配)
 * @param text 文本串
 * @param pattern 模式串
 * @return vector<int> 匹配位置的起始索引
 * @time_complexity O(n + m)
 */
inline std::vector<int> kmp_search(const std::string& text, const std::string& pattern) {
    int n = text.size();
    int m = pattern.size();
    std::vector<int> result;
    if (pattern.empty()) {
        return {0};
    }
    
    // 构建 next 数组 (LPS: Longest Prefix Suffix)
    std::vector<int> next(m, 0);
    for (int i = 1, j = 0; i < m; i++) {
        while (j > 0 && pattern[i] != pattern[j]) {
            j = next[j - 1];
        }
        if (pattern[i] == pattern[j]) {
            j++;
        }
        next[i] = j;
    }
    
    // 匹配
    for (int i = 0, j = 0; i < n; i++) {
        while (j > 0 && text[i] != pattern[j]) {
            j = next[j - 1];
        }
        if (text[i] == pattern[j]) {
            j++;
        }
        if (j == m) {
            result.push_back(i - m + 1);
            j = next[j - 1];
        }
    }
    
    return result;
}
