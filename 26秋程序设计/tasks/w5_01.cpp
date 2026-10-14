#include <iostream>

using namespace std;
int ifprime(int n)
{
	for(int i=2;i*i<=n;i++)
	{
		if(n%i==0) return 0;
	}
	return 1;
}

int main()
{
	int n,m; cin >> n >> m;
	int sum=0,count=0;
	for(int i=2;i;i++)
	{
		if(ifprime(i))
		{
			count++;
			if(count>=n)
			{
				sum+=i;
			}
			if(count==m) break;
		}
	}
	cout << sum << endl;
	
	return 0;
}
