#pragma once

#include <array>
#include <stdexcept>
#include <string>
#include <vector>

/** @brief 仅接受小写英文字母 a-z 的 Trie。 */
class Trie {
private:
    struct Node {
        std::array<int, 26> children{};
        bool is_end = false;

        Node() { children.fill(-1); }
    };

    std::vector<Node> nodes_{1};

    static int index_of(char character) {
        if (character < 'a' || character > 'z') {
            throw std::invalid_argument("Trie: only lowercase a-z is supported");
        }
        return character - 'a';
    }

    int find_node(const std::string& text) const {
        int current = 0;
        for (char character : text) {
            const int index = index_of(character);
            if (nodes_[current].children[index] == -1) {
                return -1;
            }
            current = nodes_[current].children[index];
        }
        return current;
    }

public:
    void insert(const std::string& word) {
        int current = 0;
        for (char character : word) {
            const int index = index_of(character);
            if (nodes_[current].children[index] == -1) {
                nodes_[current].children[index] = static_cast<int>(nodes_.size());
                nodes_.emplace_back();
            }
            current = nodes_[current].children[index];
        }
        nodes_[current].is_end = true;
    }

    bool search(const std::string& word) const {
        const int node = find_node(word);
        return node != -1 && nodes_[node].is_end;
    }

    bool starts_with(const std::string& prefix) const {
        return find_node(prefix) != -1;
    }

    bool startsWith(const std::string& prefix) const { return starts_with(prefix); }

    int node_count() const noexcept { return static_cast<int>(nodes_.size()); }
};
