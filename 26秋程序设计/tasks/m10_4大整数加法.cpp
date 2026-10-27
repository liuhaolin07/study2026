#include <iostream>
#include <string>
#include <cmath>
#include <cstring>
using namespace std;
const int N=1e5+10;
int a[N],b[N],c[N];
int la,lb,lc;

void add(int a[],int b[],int c[])
{
	for(int i=0;i<lc;i++)
	{
		c[i]+=a[i]+b[i]; //进位加上对应位，用+= 
		c[i+1]+=c[i]/10; //处理进位，+应该可略 
		c[i]%=10;
	}
	if(c[lc]) lc++;
}
int main()
{
	int n; cin >> n;
	while(n--)
	{
		//存在残留数据，每组数据开始前清零
        memset(a, 0, sizeof(a));
        memset(b, 0, sizeof(b));
        memset(c, 0, sizeof(c)); 
		string as,bs; cin >> as >> bs;
		la=as.size(),lb=bs.size(),lc=max(la,lb);
//		for(int i=la-1;i>=0;i--) a[la-i-1]=as[i]-'0';
//		for(int i=lb-1;i>=0;i--) b[lb-i-1]=bs[i]-'0';
		for(int i = 0; i < la; i++) a[la - 1 - i] = as[i] - '0';
		for(int i = 0; i < lb; i++) b[lb - 1 - i] = bs[i] - '0';
		add(a,b,c);
		for(int i=lc-1;i>=0;i--) cout << c[i];
		cout << "\n";
	}
	
	return 0;
}
