#pragma once

#include <stdexcept>
#include <vector>

/**
 * @brief 区间和线段树，支持单点赋值和闭区间查询。
 * @time_complexity build: O(n), update/query: O(log n)
 */
template <typename T>
class SegmentTree {
private:
    std::vector<T> tree_;
    int size_;

    void build(int node, int left, int right, const std::vector<T>& values) {
        if (left == right) {
            tree_[node] = values[left];
            return;
        }
        const int mid = left + (right - left) / 2;
        build(node * 2, left, mid, values);
        build(node * 2 + 1, mid + 1, right, values);
        tree_[node] = tree_[node * 2] + tree_[node * 2 + 1];
    }

    T query_impl(int node, int left, int right, int query_left,
                 int query_right) const {
        if (query_right < left || right < query_left) {
            return T{};
        }
        if (query_left <= left && right <= query_right) {
            return tree_[node];
        }
        const int mid = left + (right - left) / 2;
        return query_impl(node * 2, left, mid, query_left, query_right) +
               query_impl(node * 2 + 1, mid + 1, right, query_left,
                          query_right);
    }

    void update_impl(int node, int left, int right, int index, T value) {
        if (left == right) {
            tree_[node] = value;
            return;
        }
        const int mid = left + (right - left) / 2;
        if (index <= mid) {
            update_impl(node * 2, left, mid, index, value);
        } else {
            update_impl(node * 2 + 1, mid + 1, right, index, value);
        }
        tree_[node] = tree_[node * 2] + tree_[node * 2 + 1];
    }

    void check_index(int index) const {
        if (index < 0 || index >= size_) {
            throw std::out_of_range("SegmentTree: index out of range");
        }
    }

public:
    explicit SegmentTree(const std::vector<T>& values)
        : tree_(values.empty() ? 1 : values.size() * 4, T{}),
          size_(static_cast<int>(values.size())) {
        if (size_ > 0) {
            build(1, 0, size_ - 1, values);
        }
    }

    int size() const noexcept { return size_; }

    T query(int left, int right) const {
        if (left > right) {
            return T{};
        }
        check_index(left);
        check_index(right);
        return query_impl(1, 0, size_ - 1, left, right);
    }

    void update(int index, T value) {
        check_index(index);
        update_impl(1, 0, size_ - 1, index, value);
    }
};
