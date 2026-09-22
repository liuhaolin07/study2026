/*
 * 文件名称：contest.cpp
 * 作    用：CSP 认证考场起手模板，每道题开场复制这一份再开始写
 * 设计原理：把"每题都要写一遍"的样板（快速 IO、类型别名、本地文件重定向、
 *           多组数据处理）固化下来，考场上省下 3~5 分钟且不会写错
 * 易    错：本地 g++ 版本比考场新，必须用 -std=c++17 编译以保持与考场一致
 *
 * 编译命令（与考场 Ubuntu 24.04 + g++ 13.2.0 对齐）：
 *   g++ -O2 -std=c++17 -DONLINE_JUDGE -Wall contest.cpp -o contest
 *
 * 本地调试（不带 -DONLINE_JUDGE，会启用文件重定向）：
 *   g++ -O2 -std=c++17 -Wall contest.cpp -o contest
 *   然后把测试数据放到同目录的 in.txt，输出会写到 out.txt
 */

// ========== 0. 头文件与命名空间 ==========
#include <bits/stdc++.h>  // g++ 专属万能头，考场支持；换编译器需拆开写
using namespace std;

// ========== 1. 类型别名 ==========
// 作用：短名字减少敲错；CSP 大量题目会溢出 int，默认用 ll
// ⚠️ 易错：涉及求和/乘积/计数一律 long long，int 上限只有 2.1e9
using ll = long long;
using ull = unsigned long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;

// 常用常量
const int INF = 0x3f3f3f3f;              // 约 1.06e9，两个相加不会溢出 int
const ll LINF = 0x3f3f3f3f3f3f3f3fLL;    // ll 版 INF
const int MOD = 1e9 + 7;                 // ⚠️ 题目给什么模数就改成什么，别默认
const double EPS = 1e-9;                 // 浮点比较用，不要用 == 判浮点相等

// ⚠️ N 一定要按题目数据范围改，并且留余量（n<=1e5 就开 100005）
//    线段树的数组要开 4*N，不是 N
const int N = 100005;

// ========== 2. 宏 ==========
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define eb emplace_back
#define fi first
#define se second
#define rep(i, a, b) for (int i = (a); i < (b); ++i)
#define per(i, a, b) for (int i = (b) - 1; i >= (a); --i)

// ========== 3. 全局数据区 ==========
// 作用：全局数组自动清零，局部数组不会。多组数据的题尤其要注意重置
// ⚠️ 易错：局部变量 int a[N] 是未初始化的随机值，这是经典 bug
int n, m;
// ll a[N];

// ========== 4. 常用工具函数 ==========

// 快速读入：数据量 >= 1e6 时比 cin 更快
// 原理：用 getchar 逐字符解析，跳过空白，处理负号
// ⚠️ 易错：和 ios::sync_with_stdio(false) 不要混用，二选一
//          本模板默认用 cin 加速，read() 只在极端数据量时启用
inline ll read() {
    ll x = 0, f = 1;
    char c = getchar();
    while (c < '0' || c > '9') {
        if (c == '-') f = -1;
        c = getchar();
    }
    while (c >= '0' && c <= '9') {
        x = x * 10 + (c - '0');
        c = getchar();
    }
    return x * f;
}

// 快速幂：O(log b)，求 a^b % p
// 原理：二进制拆分指数，边乘边取模
// ⚠️ 易错：res 和 a 必须用 ll，否则 a*a 在乘法那一步就溢出了
ll qpow(ll a, ll b, ll p = MOD) {
    ll res = 1 % p;          // ⚠️ p 可能等于 1，此时答案应为 0
    a %= p;
    while (b > 0) {
        if (b & 1) res = res * a % p;
        a = a * a % p;
        b >>= 1;
    }
    return res;
}

// 判断闰年：CSP 日期题高频
// 原理：四年一闰，百年不闰，四百年再闰
// ⚠️ 易错：&& 和 || 的优先级，必须加括号
inline bool is_leap(int y) {
    return (y % 4 == 0 && y % 100 != 0) || y % 400 == 0;
}

// 每月天数表，索引 1~12，二月按平年算
// ⚠️ 易错：用之前先把 days[2] 按 is_leap(y) 改成 28 或 29
int month_days[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

// 按分隔符切分字符串：CSP 字符串题几乎必用
// 原理：find 定位分隔符，substr 取段
// ⚠️ 易错：连续两个分隔符之间会产生空字符串段，题意需要时要手动跳过
vector<string> split_str(const string& s, char delim) {
    vector<string> res;
    size_t start = 0, pos;
    while ((pos = s.find(delim, start)) != string::npos) {
        res.pb(s.substr(start, pos - start));
        start = pos + 1;
    }
    res.pb(s.substr(start));  // 最后一段没有分隔符结尾，必须单独补上
    return res;
}

// 离散化：把大值域压到 1~n，配合树状数组/线段树用
// 原理：排序去重后，用 lower_bound 查每个值的排名
// ⚠️ 易错：lower_bound 返回的是迭代器，要减 begin() 再 +1 才是 1-based 下标
void discrete(vector<int>& v, vector<int>& src) {
    v = src;
    sort(all(v));
    v.erase(unique(all(v)), v.end());
    for (int& x : src) x = int(lower_bound(all(v), x) - v.begin()) + 1;
}

// ========== 5. 主函数 ==========
int main() {
    // --- IO 加速：大数据量必须，否则 cin/cout 会 TLE ---
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // ⚠️ 加了上面两行之后，绝对不能再混用 scanf/printf
    // ⚠️ 输出换行用 '\n' 不要用 endl（endl 每次都会 flush，很慢）

#ifndef ONLINE_JUDGE
    // 本地调试：从文件读入、写文件输出，方便反复跑同一组数据
    // 考场上定义了 ONLINE_JUDGE 宏，这段代码自动失效
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif

    // --- 多组数据处理（题目是单组就删掉 while）---
    // ⚠️ 易错：用 while (cin >> n) 读到 EOF，不要用 while (!cin.eof())
    //          后者会多读一次，把上一组的数据又算一遍
    // while (cin >> n) {
    //     solve();
    // }

    // 题意：
    // 思路：
    // 复杂度：

    return 0;
}
