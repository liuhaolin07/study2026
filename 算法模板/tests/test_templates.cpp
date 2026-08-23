#include "basic/fast_power.hpp"
#include "basic/gcd.hpp"
#include "basic/prefix_sum.hpp"
#include "basic/prime_sieve.hpp"
#include "data_structure/fenwick_tree.hpp"
#include "data_structure/segment_tree.hpp"
#include "data_structure/segment_tree_lazy.hpp"
#include "data_structure/sparse_table.hpp"
#include "data_structure/union_find.hpp"
#include "dp/edit_distance.hpp"
#include "dp/knapsack.hpp"
#include "dp/lcs.hpp"
#include "dp/lis.hpp"
#include "graph/bellman_ford.hpp"
#include "graph/bipartite_matching.hpp"
#include "graph/dijkstra.hpp"
#include "graph/dijkstra_with_path.hpp"
#include "graph/floyd_warshall.hpp"
#include "graph/kruskal.hpp"
#include "graph/prim.hpp"
#include "graph/topological_sort.hpp"
#include "graph/traversal.hpp"
#include "math/combination.hpp"
#include "math/extended_gcd.hpp"
#include "math/modular_arithmetic.hpp"
#include "sorting/binary_search.hpp"
#include "sorting/sorting.hpp"
#include "string/kmp.hpp"
#include "string/manacher.hpp"
#include "string/trie.hpp"
#include "string/z_function.hpp"

#include <algorithm>
#include <functional>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <vector>

int odr_probe();

namespace {
int checks = 0;
int failures = 0;

void check(bool condition, const char* expression, int line) {
    ++checks;
    if (!condition) {
        ++failures;
        std::cerr << "FAIL line " << line << ": " << expression << '\n';
    }
}

#define CHECK(expression) check(static_cast<bool>(expression), #expression, __LINE__)

template <typename Exception, typename Callable>
void check_throws(Callable&& callable, const char* expression, int line) {
    ++checks;
    try {
        callable();
    } catch (const Exception&) {
        return;
    } catch (...) {
    }
    ++failures;
    std::cerr << "FAIL line " << line << ": expected exception from "
              << expression << '\n';
}

#define CHECK_THROWS(exception, expression) \
    check_throws<exception>([&] { (void)(expression); }, #expression, __LINE__)

void test_basic() {
    CHECK(fast_power(2, 10, 1'000'000'007) == 1024);
    CHECK(fast_power(-2, 3, 5) == 2);
    CHECK_THROWS(std::invalid_argument, fast_power(2, -1, 7));
    CHECK(gcd(-18, 24) == 6);
    CHECK(lcm(-6, 8) == 24);

    const auto small_sieve = eratosthenes_sieve(0);
    CHECK(small_sieve.size() == 1 && !small_sieve[0]);
    const auto sieve = eratosthenes_sieve(10);
    CHECK(sieve[2] && sieve[3] && sieve[5] && sieve[7] && !sieve[9]);
    CHECK(linear_sieve(10) == std::vector<int>({2, 3, 5, 7}));

    PrefixSum<long long> prefix({2, -1, 4, 3});
    CHECK(prefix.sum(1, 3) == 6);
    CHECK(prefix.sum(3, 2) == 0);
}

void test_data_structures() {
    FenwickTree<long long> fenwick({1, 2, 3, 4});
    CHECK(fenwick.query(3) == 10);
    CHECK(fenwick.range_query(1, 2) == 5);
    fenwick.update(1, 5);
    CHECK(fenwick.range_query(0, 1) == 8);
    CHECK_THROWS(std::out_of_range, fenwick.update(4, 1));

    SegmentTree<long long> segment({1, 2, 3, 4});
    CHECK(segment.query(1, 3) == 9);
    segment.update(2, 10);
    CHECK(segment.query(0, 3) == 17);

    LazySegmentTree<long long> lazy({1, 2, 3, 4});
    CHECK(lazy.query(0, 3) == 10);
    lazy.update(1, 3, 2);
    CHECK(lazy.query(0, 3) == 16);
    CHECK(lazy.query(2, 2) == 5);

    UnionFind sets(5);
    CHECK(sets.unite(0, 1));
    CHECK(sets.unite(1, 2));
    CHECK(!sets.unite(0, 2));
    CHECK(sets.component_size(0) == 3 && sets.count_sets() == 3);

    SparseTableMin<int> sparse({5, 2, 7, 1, 4});
    CHECK(sparse.query(1, 4) == 1);
    CHECK(sparse.query(0, 2) == 2);
}

void test_sorting_and_dp() {
    std::vector<int> values{5, 1, 3, 3, -2};
    merge_sort(values);
    CHECK(values == std::vector<int>({-2, 1, 3, 3, 5}));
    quick_sort(values, std::greater<int>{});
    CHECK(values == std::vector<int>({5, 3, 3, 1, -2}));

    const std::vector<int> ordered{1, 2, 2, 4};
    CHECK(lower_bound_index(ordered, 2) == 1);
    CHECK(upper_bound_index(ordered, 2) == 3);
    CHECK(binary_search_index(ordered, 3) == -1);

    const std::vector<int> sequence{10, 9, 2, 5, 3, 7, 101, 18};
    CHECK(lis_length(sequence) == 4);
    const auto lis = lis_sequence(sequence);
    CHECK(lis.size() == 4 && std::is_sorted(lis.begin(), lis.end()) &&
          std::adjacent_find(lis.begin(), lis.end()) == lis.end());

    CHECK(knapsack_01({1, 3, 4}, {15, 20, 30}, 4) == 35);
    CHECK(knapsack_complete({1, 3, 4}, {15, 20, 30}, 4) == 60);
    CHECK(lcs_length("abcde", "ace") == 3);
    CHECK(lcs_sequence("abcde", "ace") == "ace");
    CHECK(edit_distance("kitten", "sitting") == 3);
}

WeightedGraph sample_weighted_graph() {
    WeightedGraph graph(4);
    graph[0] = {{1, 1}, {2, 4}};
    graph[1] = {{2, 2}, {3, 5}};
    graph[2] = {{3, 1}};
    return graph;
}

void test_graph() {
    const auto graph = sample_weighted_graph();
    const auto distance = dijkstra(graph, 0);
    CHECK(distance == std::vector<long long>({0, 1, 3, 4}));
    const auto [path_distance, previous] = dijkstra_with_path(graph, 0);
    CHECK(path_distance == distance);
    CHECK(reconstruct_path(previous, 0, 3) == std::vector<int>({0, 1, 2, 3}));
    CHECK(reconstruct_path(previous, 3, 0).empty());

    WeightedGraph negative_graph(2);
    negative_graph[0].push_back({1, -1});
    CHECK_THROWS(std::invalid_argument, dijkstra(negative_graph, 0));

    const long long inf = std::numeric_limits<long long>::max();
    auto all_pairs = floyd_warshall({{0, 3, inf}, {inf, 0, 2}, {1, inf, 0}});
    CHECK(all_pairs[0][2] == 5 && all_pairs[1][0] == 3);

    std::vector<WeightedEdge> edges{{0, 1, 1}, {1, 2, 2}, {0, 2, 4}};
    CHECK(kruskal_mst(edges, 3) == 3);
    CHECK(!kruskal_mst({{0, 1, 1}}, 3).has_value());

    WeightedGraph undirected(3);
    auto add_undirected = [&](int left, int right, int weight) {
        undirected[left].push_back({right, weight});
        undirected[right].push_back({left, weight});
    };
    add_undirected(0, 1, 1);
    add_undirected(1, 2, 2);
    add_undirected(0, 2, 4);
    CHECK(prim_mst(undirected) == 3);

    const std::vector<std::vector<int>> dag{{1, 2}, {3}, {3}, {}};
    const auto order = topological_sort(dag, 4);
    std::vector<int> position(4);
    for (int i = 0; i < 4; ++i) {
        position[order[i]] = i;
    }
    CHECK(position[0] < position[1] && position[0] < position[2] &&
          position[1] < position[3] && position[2] < position[3]);
    CHECK(topological_sort({{1}, {0}}, 2).empty());

    CHECK(bfs_distance(dag, 0) == std::vector<int>({0, 1, 1, 2}));
    CHECK(dfs_order(dag, 0) == std::vector<int>({0, 1, 3, 2}));

    BipartiteMatching matching(3, 3);
    matching.add_edge(0, 0);
    matching.add_edge(0, 1);
    matching.add_edge(1, 1);
    matching.add_edge(2, 2);
    CHECK(matching.max_matching() == 3);
    CHECK(matching.max_matching() == 3);

    const auto bellman =
        bellman_ford(3, {{0, 1, 4}, {0, 2, 5}, {1, 2, -2}}, 0);
    CHECK(!bellman.has_reachable_negative_cycle);
    CHECK(bellman.distance == std::vector<long long>({0, 4, 2}));
    CHECK(bellman_ford(2, {{0, 1, -1}, {1, 0, -1}}, 0)
              .has_reachable_negative_cycle);
}

void test_string_and_math() {
    CHECK(kmp_search("aaaa", "aa") == std::vector<int>({0, 1, 2}));
    CHECK(kmp_search("abc", "") == std::vector<int>({0}));
    CHECK(z_search("aaaa", "aa") == std::vector<int>({0, 1, 2}));

    Trie trie;
    trie.insert("apple");
    CHECK(trie.search("apple") && !trie.search("app") &&
          trie.starts_with("app"));
    CHECK_THROWS(std::invalid_argument, trie.insert("App"));

    const auto [palindrome_start, palindrome_length] =
        longest_palindrome("babad");
    CHECK(palindrome_length == 3);
    CHECK(std::string("babad").substr(palindrome_start, palindrome_length) ==
              "bab" ||
          std::string("babad").substr(palindrome_start, palindrome_length) ==
              "aba");

    CHECK(combination(5, 2) == 10);
    CHECK(combination(5, 8) == 0);
    CHECK(precompute_combinations(6, 1'000'000'007)[6][3] == 20);
    CHECK(modular::sub(1, 2) == modular::MOD - 1);
    CHECK(modular::mul(-2, 3) == modular::MOD - 6);
    CHECK(modular::mul(3, modular::inv(3)) == 1);

    const auto egcd = extended_gcd(30, 18);
    CHECK(egcd.gcd == 6 && 30 * egcd.x + 18 * egcd.y == 6);
    CHECK(modular_inverse(3, 11) == 4);
    CHECK(!modular_inverse(6, 9).has_value());
    CHECK(odr_probe() == 12);
}
}  // namespace

int main() {
    test_basic();
    test_data_structures();
    test_sorting_and_dp();
    test_graph();
    test_string_and_math();

    if (failures != 0) {
        std::cerr << failures << " of " << checks << " checks failed\n";
        return 1;
    }
    std::cout << "All " << checks << " checks passed\n";
    return 0;
}
