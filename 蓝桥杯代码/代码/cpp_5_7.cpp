#include <bits/stdc++.h>
using namespace std;
const int N=1e5+10;
vector<int> dp(N+1,-1);
int dfs(int x)
{
	if(x<=2) return dp[x]=x;
	if(dp[x]!=-1) return dp[x];
	return dfs(x-1)+dfs(x-2);
 } 
int main()
{
	int n; cin >> n;
	cout << dfs(n) << endl;
	return 0;
}
