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
	int t; cin >> t;
	while(t--)
	{
		int n; cin >> n;
		for(int i=2;i<=n;i++)
		{
			if(ifprime(i)) cout << i <<" ";
		 } 
		 cout << '\n';
	}
	
	return 0;
}
