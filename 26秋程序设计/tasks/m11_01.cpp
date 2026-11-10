#include <iostream>
using namespace std;
int main()
{
	int n,w; cin >> n >> w;
	while(n--)
	{
		int v,s; cin>> v >> s;
		double m=(double)v/s;
		if(m<=w) cout << "Yes" << '\n';
		else cout << "NO" << '\n';
	}
	
	return 0;
}
