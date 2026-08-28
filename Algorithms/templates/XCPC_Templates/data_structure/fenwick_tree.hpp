#pragma once

#include <stdexcept>
#include <vector>

/**
 * @brief 树状数组，使用 0-based 对外下标。
 * @time_complexity update/query: O(log n), build: O(n log n)
 */
template <typename T>
class FenwickTree {
private:
    std::vector<T> bit_;
    int size_;

    void check_index(int index) const {
        if (index < 0 || index >= size_) {
            throw std::out_of_range("FenwickTree: index out of range");
        }
    }

public:
    explicit FenwickTree(int size) : bit_(), size_(size) {
        if (size < 0) {
            throw std::invalid_argument("FenwickTree: size must be non-negative");
        }
        bit_.assign(static_cast<std::size_t>(size) + 1, T{});
    }

    explicit FenwickTree(const std::vector<T>& values)
        : FenwickTree(static_cast<int>(values.size())) {
        for (int i = 0; i < size_; ++i) {
            update(i, values[i]);
        }
    }

    int size() const noexcept { return size_; }

    void update(int index, T delta) {
        check_index(index);
        for (++index; index <= size_; index += index & -index) {
            bit_[index] += delta;
        }
    }

    /** @brief 返回 [0, index] 的和；index == -1 时返回 0。 */
    T query(int index) const {
        if (index == -1) {
            return T{};
        }
        check_index(index);
        T sum{};
        for (++index; index > 0; index -= index & -index) {
            sum += bit_[index];
        }
        return sum;
    }

    T range_query(int left, int right) const {
        if (left > right) {
            return T{};
        }
        check_index(left);
        check_index(right);
        return query(right) - query(left - 1);
    }
};
