# P4777 【模板】扩展中国剩余定理(EXCRT)

- 专题:`07-math` § 同余方程组
- 难度:提高+/省选-
- 对应速查:`笔记/速查/05-数论与组合速查.md` § 四

## 题意

解同余方程组 `x ≡ bᵢ (mod aᵢ)`(1 ≤ n ≤ 10^5,1 ≤ aᵢ, bᵢ ≤ 10^5),模数**不保证互质**。有解输出最小非负整数解,无解输出 -1。

## 思路怎么来的

CRT 的两两合并思想在这里同样成立,只是"互质"的福利没了——合并要用 exgcd 硬解:

设已合并出 `x ≡ r (mod M)`,要再满足 `x ≡ b (mod a)`。代入 `x = r + M·k`:

> `M·k ≡ b - r (mod a)` —— 关于未知数 k 的线性同余方程。

由速查表 § 二的结论,`M·k ≡ c (mod a)` 有解 ⟺ `g = gcd(M, a)` 整除 c;exgcd 求出 `M·p + a·q = g`,则 `(M/g)·p ≡ 1 (mod a/g)`,于是

> `k ≡ (c/g)·p (mod a/g)`,取 `k₀` 为最小非负解,新方程 `x ≡ r + M·k₀ (mod lcm(M, a))`。

n 个方程就合并 n-1 次;`c % g != 0` 当场判无解。整个推导就是"**把新条件翻译成对自由变量 k 的同余方程**",每一步都在速查表里有原型。

## 复杂度

每次合并一次 exgcd,O(n log M)。

## 参考代码

```cpp
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef __int128 lll;

ll exgcd(ll a, ll b, ll &x, ll &y) {      // a*x + b*y = gcd(a,b)
    if (!b) { x = 1; y = 0; return a; }
    ll x1, y1, g = exgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

int main() {
    int n;
    scanf("%d", &n);
    ll r = 0, M = 1;                       // 已合并:x ≡ r (mod M)
    while (n--) {
        ll a, b;                           // 新条件:x ≡ b (mod a)
        scanf("%lld %lld", &a, &b);
        ll p, q, g = exgcd(M, a, p, q);    // M*p + a*q = g
        ll c = ((b - r) % a + a) % a;      // 归正:M*k ≡ c (mod a)
        if (c % g) { puts("-1"); return 0; }
        ll ma = a / g;                     // k ≡ (c/g)*p (mod ma)
        lll k = (lll)(c / g % ma) * ((p % ma + ma) % ma) % ma;
        r = (ll)(r + (lll)M * k);          // __int128 承接 M*k,防溢出
        M = M / g * a;                     // lcm:先除后乘
        r %= M;
    }
    printf("%lld\n", (r % M + M) % M);
    return 0;
}
```

## 易错点

1. **溢出是本题的第一杀手**:`M·k` 可达 10^18 量级再往上,乘法一律走 `__int128`;`M/g*a` 先除后乘。
2. 负数归正三处:`b - r` 可能为负(`(c % a + a) % a`);exgcd 的 p 可能为负(`(p % ma + ma) % ma`);输出前 `r % M + M` 兜底。
3. 无解条件是 `c % g != 0`(即 g ∤ (b - r)),不是 `b % g`。
4. p 是"模 a/g 意义下 M/g 的逆元"——用它之前先对 ma 取模,别拿原始 p 直接乘。
5. 方程顺序:**先拿前两个合并出基础解**,循环里始终维护"已合并"不变式;别想着一次性解 n 元。
6. 与 CRT 区分:模数互质时两者都行,但 EXCRT 是超集,统一用 EXCRT 写法少背一个公式。

## 延伸

- CRT(P1495)可以当本题的特例检验:互质数据用两种写法互拍。
- 大步跳跃的应用:P1516 青蛙的约会(单条同余方程)→ 本题(方程组)→ P5602? 之后是"同余最短路"(最小非表示数,银牌边缘)。
- 合并思想还能做"区间内满足条件的数计数":对每个条件求最小解,Chinese-remainder 逐层合并上下界。
