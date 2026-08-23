#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

// 快速幂求逆元
long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

void solve_B() {
    int n;
    if (!(cin >> n)) return;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    // BFS 预处理每个点的深度
    vector<int> depth(n + 1, 0);
    vector<int> q;
    q.push_back(1);
    depth[1] = 1;
    int head = 0;
    while (head < q.size()) {
        int u = q[head++];
        for (int v : adj[u]) {
            if (depth[v] == 0) {
                depth[v] = depth[u] + 1;
                q.push_back(v);
            }
        }
    }

    // 预处理调和级数 H[i] 取模
    vector<long long> H(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        H[i] = (H[i - 1] + modInverse(i)) % MOD;
    }

    // 累加每个节点的期望
    long long ans = 0;
    for (int i = 1; i <= n; ++i) {
        ans = (ans + H[depth[i]]) % MOD;
    }

    cout << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    solve_B();
    return 0;
}
 
