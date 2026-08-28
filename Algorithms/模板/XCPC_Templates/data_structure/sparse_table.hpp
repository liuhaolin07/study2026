#pragma once

#include <algorithm>
#include <stdexcept>
#include <vector>

/**
 * @brief 静态区间最小值 Sparse Table，查询区间为闭区间 [l, r]。
 * @time_complexity build: O(n log n), query: O(1)
 */
template <typename T>
class SparseTableMin {
private:
    std::vector<std::vector<T>> table_;
    std::vector<int> log2_;
    int size_;

public:
    explicit SparseTableMin(const std::vector<T>& values)
        : table_(), log2_(values.size() + 1, 0),
          size_(static_cast<int>(values.size())) {
        for (int i = 2; i <= size_; ++i) {
            log2_[i] = log2_[i / 2] + 1;
        }
        if (values.empty()) {
            return;
        }
        const int levels = log2_[size_] + 1;
        table_.assign(levels, std::vector<T>(values.size()));
        table_[0] = values;
        for (int level = 1; level < levels; ++level) {
            const int length = 1 << level;
            const int half = length >> 1;
            for (int left = 0; left + length <= size_; ++left) {
                table_[level][left] =
                    std::min(table_[level - 1][left],
                             table_[level - 1][left + half]);
            }
        }
    }

    int size() const noexcept { return size_; }

    T query(int left, int right) const {
        if (left < 0 || right < left || right >= size_) {
            throw std::out_of_range("SparseTableMin: invalid range");
        }
        const int level = log2_[right - left + 1];
        const int length = 1 << level;
        return std::min(table_[level][left],
                        table_[level][right - length + 1]);
    }
};
