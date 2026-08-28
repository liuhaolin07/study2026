#pragma once

#include <functional>
#include <utility>
#include <vector>

namespace xcpc_sort_detail {
template <typename T, typename Compare>
void merge_sort_impl(std::vector<T>& values, std::vector<T>& buffer, int left,
                     int right, Compare compare) {
    if (right - left <= 1) {
        return;
    }
    const int middle = left + (right - left) / 2;
    merge_sort_impl(values, buffer, left, middle, compare);
    merge_sort_impl(values, buffer, middle, right, compare);
    int first = left;
    int second = middle;
    int output = left;
    while (first < middle && second < right) {
        if (compare(values[second], values[first])) {
            buffer[output++] = std::move(values[second++]);
        } else {
            buffer[output++] = std::move(values[first++]);
        }
    }
    while (first < middle) {
        buffer[output++] = std::move(values[first++]);
    }
    while (second < right) {
        buffer[output++] = std::move(values[second++]);
    }
    for (int i = left; i < right; ++i) {
        values[i] = std::move(buffer[i]);
    }
}

template <typename T, typename Compare>
void quick_sort_impl(std::vector<T>& values, int left, int right,
                     Compare compare) {
    while (left < right) {
        int less = left;
        int current = left;
        int greater = right;
        const T pivot = values[left + (right - left) / 2];
        while (current <= greater) {
            if (compare(values[current], pivot)) {
                std::swap(values[less++], values[current++]);
            } else if (compare(pivot, values[current])) {
                std::swap(values[current], values[greater--]);
            } else {
                ++current;
            }
        }
        if (less - left < right - greater) {
            quick_sort_impl(values, left, less - 1, compare);
            left = greater + 1;
        } else {
            quick_sort_impl(values, greater + 1, right, compare);
            right = less - 1;
        }
    }
}
}  // namespace xcpc_sort_detail

/** @brief 稳定归并排序。时间 O(n log n)，空间 O(n)。 */
template <typename T, typename Compare = std::less<T>>
void merge_sort(std::vector<T>& values, Compare compare = Compare{}) {
    std::vector<T> buffer(values.size());
    xcpc_sort_detail::merge_sort_impl(values, buffer, 0,
                                      static_cast<int>(values.size()), compare);
}

/** @brief 三路快速排序；平均 O(n log n)，最坏 O(n^2)。 */
template <typename T, typename Compare = std::less<T>>
void quick_sort(std::vector<T>& values, Compare compare = Compare{}) {
    if (!values.empty()) {
        xcpc_sort_detail::quick_sort_impl(
            values, 0, static_cast<int>(values.size()) - 1, compare);
    }
}
