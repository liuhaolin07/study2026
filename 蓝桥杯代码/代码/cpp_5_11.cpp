#include <iostream>
using namespace std;
const int N = 1e5 + 10;
const int Mod=998244353;
int fib[N];
int dp(int n)
{
	if (n == 0 || n == 1) return n;
	if (fib[n] != -1) return fib[n];
	return fib[n] = (dp(n - 1) + dp(n - 2))%Mod;
}
int main()
{
	for (int i = 0; i < N; i++) fib[i] = -1;
	int t; cin >> t;
        while(t--)
        {
            int n; cin >> n;
	    cout << dp(n) << endl;
        }

	return 0;
}
