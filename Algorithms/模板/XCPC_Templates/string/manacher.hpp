#pragma once

#include <algorithm>
#include <string>
#include <utility>
#include <vector>

/** @brief 返回最长回文子串的 {起点, 长度}。时间 O(n)。 */
inline std::pair<int, int> longest_palindrome(const std::string& text) {
    const int size = static_cast<int>(text.size());
    if (size == 0) {
        return {0, 0};
    }
    std::vector<int> odd(size);
    for (int i = 0, left = 0, right = -1; i < size; ++i) {
        int radius = i > right ? 1 : std::min(odd[left + right - i], right - i + 1);
        while (i - radius >= 0 && i + radius < size &&
               text[i - radius] == text[i + radius]) {
            ++radius;
        }
        odd[i] = radius;
        if (i + radius - 1 > right) {
            left = i - radius + 1;
            right = i + radius - 1;
        }
    }
    std::vector<int> even(size);
    for (int i = 0, left = 0, right = -1; i < size; ++i) {
        int radius = i > right ? 0 : std::min(even[left + right - i + 1], right - i + 1);
        while (i - radius - 1 >= 0 && i + radius < size &&
               text[i - radius - 1] == text[i + radius]) {
            ++radius;
        }
        even[i] = radius;
        if (i + radius - 1 > right) {
            left = i - radius;
            right = i + radius - 1;
        }
    }

    std::pair<int, int> best{0, 1};
    for (int i = 0; i < size; ++i) {
        const int odd_length = odd[i] * 2 - 1;
        if (odd_length > best.second) {
            best = {i - odd[i] + 1, odd_length};
        }
        const int even_length = even[i] * 2;
        if (even_length > best.second) {
            best = {i - even[i], even_length};
        }
    }
    return best;
}
