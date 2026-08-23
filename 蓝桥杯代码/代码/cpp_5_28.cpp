#include <iostream>
#include <algorithm>
const int N=1010;
using namespace std;
int main()
{
	int t; cin >> t;
	while(t--)
	{
		int n; cin >> n;
		int a[N];
		for(int i=0;i<n;i++)
		{
			cin >> a[i]; 
		}
		sort(a,a+n);
		cout << (a[n-1]-a[0]+1)/2 << endl;
	}
	return 0;
}
