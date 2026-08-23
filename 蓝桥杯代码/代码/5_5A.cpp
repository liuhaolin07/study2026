#include <iostream>
using namespace std;
void solve()
{
	long long n, m; cin >> n >> m;
	if (n > m)
	{
		cout << "No" << endl;
		return;
	}
	long long min_n=0;
	while(m>0)
	{
		min_n+=m%3;
		m/=3;
	}
	if(n>=min_n&&(n-min_n)%2==0)
	{
		cout << "Yes" << endl;
	} 
	else 
	{
		cout << "No" << endl;
	}
	return;
}
int main()
{
	int t; cin >> t;
	while (t--)
	{
		solve();
	}
	return 0;
}
