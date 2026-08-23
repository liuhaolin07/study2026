//#include <bits/stdc++.h>
//using namespace std;
//const int N=1e5+10;
//int a[N],n;
//int main()
//{
//	cin >> n;
//	for(int i=1;i<=n;i++) cin >> a[i];
//	sort(a+1,a+n+1);
//	
//}

//23-M.й╞вссно╥
#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t;cin >> t;
	while(t--)
	{
		int n; cin >> n;
		int flag=1;
		while(n)
		{
			if(n%2==0)
			{
				n-=1;
				flag=-flag;
			}
			else
			{
				n-=1;
				flag=-flag;
			}
			if(n==0&&flag==-1)
			{
				cout << "Alice" << endl;
			 } 
			if(n==0&&flag==1)
			{
				 cout << "Bob" << endl;
			}
		}
	}
	return 0;
}
