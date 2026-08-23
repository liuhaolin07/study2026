//H.选取方法
//有点像差分 
#include <bits/stdc++.h>
using namespace std;
const int Mod=1e9+7;
const int N=5e5+10;
int a[N],dp[N]; 
int n,k;
int dfs(int m) //第m位数 
{
	int ret=1;
	for(int i=1;i<n;i++)
	{
		if(a[i]>=a[m]+k||a[i]<=a[m]-k)
			ret=(ret+dp[i])%Mod;
	}
	return ret;
}
int main()
{
	ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
	cin >> n >> k;
	for(int i=1;i<=n;i++) 
	{
		cin >> a[i];
		dp[i]=dfs(i);
	}
	int ans=0;
	for(int i=1;i<=n;i++) ans=(ans+dp[i])%Mod;
	cout << ans << endl;
	return 0;
}
