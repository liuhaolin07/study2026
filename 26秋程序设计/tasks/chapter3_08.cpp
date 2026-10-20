#include <stdio.h>

typedef unsigned long long ull;

ull mod_pow(ull x, ull n, ull m)
{
    ull ans = 1 % m;
    x %= m;

    while (n > 0) {
        if (n & 1ULL)
            ans = (ull)((unsigned __int128)ans * x % m);

        x = (ull)((unsigned __int128)x * x % m);
        n >>= 1;
    }

    return ans;
}

int main(void)
{
    ull x, n, m;

    if (scanf("%llu %llu %llu", &x, &n, &m) != 3 || m == 0)
        return 1;

    printf("%llu\n", mod_pow(x, n, m));

    return 0;
}
