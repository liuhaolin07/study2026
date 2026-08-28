#pragma once

#include <stdexcept>
#include <vector>

/** @brief 一维前缀和；sum(l,r) 查询闭区间和。 */
template <typename T>
class PrefixSum {
private:
    std::vector<T> prefix_;

public:
    explicit PrefixSum(const std::vector<T>& values)
        : prefix_(values.size() + 1, T{}) {
        for (std::size_t i = 0; i < values.size(); ++i) {
            prefix_[i + 1] = prefix_[i] + values[i];
        }
    }

    int size() const noexcept { return static_cast<int>(prefix_.size()) - 1; }

    T sum(int left, int right) const {
        if (left > right) {
            return T{};
        }
        if (left < 0 || right >= size()) {
            throw std::out_of_range("PrefixSum: range out of bounds");
        }
        return prefix_[right + 1] - prefix_[left];
    }
};
