#pragma once

#include <stdexcept>
#include <vector>

/**
 * @brief 区间加、区间和懒标记线段树。
 * @time_complexity build: O(n), update/query: O(log n)
 */
template <typename T>
class LazySegmentTree {
private:
    std::vector<T> tree_;
    std::vector<T> lazy_;
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

    void apply(int node, int left, int right, T delta) {
        tree_[node] += static_cast<T>(right - left + 1) * delta;
        lazy_[node] += delta;
    }

    void push(int node, int left, int right) {
        if (lazy_[node] == T{} || left == right) {
            return;
        }
        const int mid = left + (right - left) / 2;
        apply(node * 2, left, mid, lazy_[node]);
        apply(node * 2 + 1, mid + 1, right, lazy_[node]);
        lazy_[node] = T{};
    }

    void update_impl(int node, int left, int right, int query_left,
                     int query_right, T delta) {
        if (query_right < left || right < query_left) {
            return;
        }
        if (query_left <= left && right <= query_right) {
            apply(node, left, right, delta);
            return;
        }
        push(node, left, right);
        const int mid = left + (right - left) / 2;
        update_impl(node * 2, left, mid, query_left, query_right, delta);
        update_impl(node * 2 + 1, mid + 1, right, query_left, query_right,
                    delta);
        tree_[node] = tree_[node * 2] + tree_[node * 2 + 1];
    }

    T query_impl(int node, int left, int right, int query_left,
                 int query_right) {
        if (query_right < left || right < query_left) {
            return T{};
        }
        if (query_left <= left && right <= query_right) {
            return tree_[node];
        }
        push(node, left, right);
        const int mid = left + (right - left) / 2;
        return query_impl(node * 2, left, mid, query_left, query_right) +
               query_impl(node * 2 + 1, mid + 1, right, query_left,
                          query_right);
    }

    void check_range(int left, int right) const {
        if (left < 0 || right < 0 || left >= size_ || right >= size_) {
            throw std::out_of_range("LazySegmentTree: range out of bounds");
        }
    }

public:
    explicit LazySegmentTree(const std::vector<T>& values)
        : tree_(values.empty() ? 1 : values.size() * 4, T{}),
          lazy_(values.empty() ? 1 : values.size() * 4, T{}),
          size_(static_cast<int>(values.size())) {
        if (size_ > 0) {
            build(1, 0, size_ - 1, values);
        }
    }

    int size() const noexcept { return size_; }

    void update(int left, int right, T delta) {
        if (left > right) {
            return;
        }
        check_range(left, right);
        update_impl(1, 0, size_ - 1, left, right, delta);
    }

    T query(int left, int right) {
        if (left > right) {
            return T{};
        }
        check_range(left, right);
        return query_impl(1, 0, size_ - 1, left, right);
    }
};
