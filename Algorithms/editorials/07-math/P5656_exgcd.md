# P5656 【模板】二元一次不定方程 (exgcd)

- 专题:`07-math` § 扩展欧几里得
- 难度:提高-

## 题意

T 组询问,每组给定 a, b, c,求关于 x, y 的方程 `ax + by = c` 的整数解:无整数解输出 `-1`;否则输出 **x 最小的正整数解**及对应的 y。

## 思路怎么来的

从裴蜀定理出发:`ax + by = c` 有整数解 ⟺ `gcd(a, b) | c`。所以第一步求 g = gcd(a, b),判 c % g。

有解时,先解出"缩小版"方程 `ax' + by' = g` 的特解——这正是**扩展欧几里得**干的事:在辗转相除 `gcd(a, b) = gcd(b, a mod b)` 的递归里,顺手把系数倒推回来。递归结构:

- 递归出口:b = 0 时 `a·1 + 0·0 = a = gcd`,即 x = 1, y = 0;
- 回溯时设下层解出了 `b·x₂ + (a mod b)·y₂ = g`,代入 `a mod b = a - ⌊a/b⌋·b` 展开整理,得本层解:
  `x₁ = y₂`,`y₁ = x₂ - ⌊a/b⌋·y₂`。

特解 `(x₀, y₀) = (x'·(c/g), y'·(c/g))` 满足原方程。但题目要 **x 为最小正整数**——通解来了:所有解为

> `x = x₀ + t·(b/g)`,`y = y₀ - t·(a/g)`,t ∈ Z

即 x 的解集在模 `m = |b/g|` 的意义下均匀分布,**最小正整数解 = x₀ 对 m 取模落到 [1, m]**(取模为 0 时补一个周期 m)。y 由 `y = (c - a·x) / b` 反解,天然整数。

a = 0 或 b = 0 时周期公式失效(除零),必须分支特判——这也是本题数据专门设的陷阱。

## 复杂度

exgcd 递归深度 O(log min(a, b)),T 组询问总计 O(T log V)。

## 参考代码

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll exgcd(ll a, ll b, ll &x, ll &y) {
    if (b == 0) { x = 1; y = 0; return a; }
    ll x2, y2;
    ll g = exgcd(b, a % b, x2, y2);
    x = y2;
    y = x2 - (a / b) * y2;
    return g;
}

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        ll a, b, c;
        scanf("%lld %lld %lld", &a, &b, &c);
        if (a == 0 && b == 0) {
            puts(c == 0 ? "1 0" : "-1");          // 0=c:任意解,取 x 最小正 = 1, y = 0
        } else if (a == 0) {
            // by = c:x 任意,最小正整数 x = 1
            if (c % b) puts("-1");
            else printf("1 %lld\n", c / b);
        } else if (b == 0) {
            // ax = c:x = c/a 必须是正整数,y 任意取 0
            if (c % a || c / a <= 0) puts("-1");
            else printf("%lld 0\n", c / a);
        } else {
            ll x, y;
            ll g = exgcd(a, b, x, y);
            if (c % g) { puts("-1"); continue; }
            ll m = llabs(b / g);                  // x 解的周期
            x = x * (c / g);                      // 任意特解
            x = ((x % m) + m) % m;                // 落到 [0, m-1]
            if (x == 0) x = m;                    // 题目要正整数
            printf("%lld %lld\n", x, (c - a * x) / b);
        }
    }
    return 0;
}
```

## 易错点

1. **a = 0 / b = 0 的分支**:周期 m = b/g 会除零,官方数据专门卡这个;三分支逐一按定义给最小正 x。
2. **"最小正整数"不是"最小非负"**:取模后 x = 0 要加回一个周期 m。
3. **溢出**:`x * (c/g)` 与 `a * x` 都可达 10^18 量级(1e9 × 1e9),全程 long long。
4. 回溯写法中 `x = y2; y = x2 - (a/b)*y2` 的顺序:先用旧值算新值,两行换序就错;用临时变量最稳。
5. m 要取绝对值(`llabs`),b 为负时周期仍应是正数。

## 延伸

exgcd 是同余理论的引擎:题单路线 P1082 同余方程(`ax ≡ 1 (mod b)` 就是 `ax + by = 1`)→ P1516 青蛙的约会(把相遇条件化成不定方程,再解最小正周期)→ P4777 EXCRT(两两合并同余方程,每次合并都调一次 exgcd)。数论题的通用策略:**把"同余"翻译成"不定方程",再交给 exgcd**。
