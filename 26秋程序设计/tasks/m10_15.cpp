#include <bits/stdc++.h>
using namespace std;

int gcd(int a,int b)
{
	if(b==0) return a;
	return gcd(b,a%b);
}
int main()
{
	int n; cin >> n;
	int a,b; scanf("%d/%d",&a,&b);
	n--;
	int x=a,y=b;
	while(n--)
	{
		int m,k;
		scanf("%d/%d",&m,&k);
		x=x*k+m*y;
		y=y*k;
	}
	//注意读题：分母为 1 时只输出整数：比如 3/1 要输出 3 而不是 3/1。 
	int z=gcd(x,y);
	if(y/z==1) 
	{
		cout << x/z << "\n";
		return 0;
	} 
	cout << x/z << "/" << y/z << "\n";
	
	return 0;
}
