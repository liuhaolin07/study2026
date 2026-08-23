#pragma once

#include <algorithm>
#include <stdexcept>
#include <vector>

/** @brief 二分图最大匹配（增广路算法），复杂度 O(VE)。 */
class BipartiteMatching {
private:
    std::vector<std::vector<int>> graph_;
    std::vector<int> match_right_;
    std::vector<int> match_left_;
    std::vector<bool> visited_;
    int left_size_;
    int right_size_;

    bool augment(int left) {
        for (int right : graph_[left]) {
            if (visited_[right]) {
                continue;
            }
            visited_[right] = true;
            if (match_right_[right] == -1 || augment(match_right_[right])) {
                match_right_[right] = left;
                match_left_[left] = right;
                return true;
            }
        }
        return false;
    }

public:
    BipartiteMatching(int left_size, int right_size)
        : graph_(), match_right_(), match_left_(), visited_(),
          left_size_(left_size), right_size_(right_size) {
        if (left_size < 0 || right_size < 0) {
            throw std::invalid_argument(
                "BipartiteMatching: sizes must be non-negative");
        }
        graph_.resize(left_size);
        match_right_.assign(right_size, -1);
        match_left_.assign(left_size, -1);
    }

    void add_edge(int left, int right) {
        if (left < 0 || left >= left_size_ || right < 0 ||
            right >= right_size_) {
            throw std::out_of_range("BipartiteMatching: vertex out of range");
        }
        graph_[left].push_back(right);
    }

    int max_matching() {
        std::fill(match_right_.begin(), match_right_.end(), -1);
        std::fill(match_left_.begin(), match_left_.end(), -1);
        int result = 0;
        for (int left = 0; left < left_size_; ++left) {
            visited_.assign(right_size_, false);
            result += augment(left) ? 1 : 0;
        }
        return result;
    }

    const std::vector<int>& get_matching() const noexcept { return match_left_; }
};
