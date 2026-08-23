#pragma once

#include <numeric>
#include <stdexcept>
#include <utility>
#include <vector>

/** @brief 路径压缩 + 按大小合并的并查集。 */
class UnionFind {
private:
    std::vector<int> parent_;
    std::vector<int> size_;
    int components_;

    void check_index(int index) const {
        if (index < 0 || index >= static_cast<int>(parent_.size())) {
            throw std::out_of_range("UnionFind: index out of range");
        }
    }

public:
    explicit UnionFind(int n) : parent_(), size_(), components_(n) {
        if (n < 0) {
            throw std::invalid_argument("UnionFind: size must be non-negative");
        }
        parent_.resize(n);
        size_.assign(n, 1);
        std::iota(parent_.begin(), parent_.end(), 0);
    }

    int find(int x) {
        check_index(x);
        if (parent_[x] != x) {
            parent_[x] = find(parent_[x]);
        }
        return parent_[x];
    }

    bool unite(int x, int y) {
        int root_x = find(x);
        int root_y = find(y);
        if (root_x == root_y) {
            return false;
        }
        if (size_[root_x] < size_[root_y]) {
            std::swap(root_x, root_y);
        }
        parent_[root_y] = root_x;
        size_[root_x] += size_[root_y];
        --components_;
        return true;
    }

    bool connected(int x, int y) { return find(x) == find(y); }

    int component_size(int x) { return size_[find(x)]; }

    int count_sets() const noexcept { return components_; }
};
