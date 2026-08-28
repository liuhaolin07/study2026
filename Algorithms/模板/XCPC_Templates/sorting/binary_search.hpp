#pragma once

#include <functional>
#include <vector>

/** @brief 第一个不小于 target 的位置；不存在时返回 values.size()。 */
template <typename T, typename Compare = std::less<T>>
int lower_bound_index(const std::vector<T>& values, const T& target,
                      Compare compare = Compare{}) {
    int left = 0;
    int right = static_cast<int>(values.size());
    while (left < right) {
        const int middle = left + (right - left) / 2;
        if (compare(values[middle], target)) {
            left = middle + 1;
        } else {
            right = middle;
        }
    }
    return left;
}

/** @brief 第一个大于 target 的位置；不存在时返回 values.size()。 */
template <typename T, typename Compare = std::less<T>>
int upper_bound_index(const std::vector<T>& values, const T& target,
                      Compare compare = Compare{}) {
    int left = 0;
    int right = static_cast<int>(values.size());
    while (left < right) {
        const int middle = left + (right - left) / 2;
        if (!compare(target, values[middle])) {
            left = middle + 1;
        } else {
            right = middle;
        }
    }
    return left;
}

/** @brief 精确查找，未找到返回 -1。 */
template <typename T, typename Compare = std::less<T>>
int binary_search_index(const std::vector<T>& values, const T& target,
                        Compare compare = Compare{}) {
    const int index = lower_bound_index(values, target, compare);
    if (index == static_cast<int>(values.size()) || compare(target, values[index]) ||
        compare(values[index], target)) {
        return -1;
    }
    return index;
}
