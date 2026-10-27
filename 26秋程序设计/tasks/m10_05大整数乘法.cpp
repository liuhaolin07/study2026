#include <bits/stdc++.h>
using namespace std;
const int N=1e5+10;
int a[N],b[N],c[2*N];
int la,lb,lc;

void mul(int a[],int b[],int c[])
{
	//先相乘，后相加
	for(int i=0;i<lb;i++)
	{
		for(int j=0;j<la;j++)
		{
			c[i+j]+=a[j]*b[i];
		}
	 } 
	 //处理进位
	 for(int i=0;i<lc;i++)
	 {
	 	c[i+1]+=c[i]/10;
	 	c[i]%=10;
	  } 
	  // 处理前导零
	while(lc > 1 && c[lc - 1] == 0) lc--; //至少有一位 
}
int main()
{
	int n; cin >> n;
	while(n--)
	{
		// 每组数据开始前清零
        memset(a, 0, sizeof(a));
        memset(b, 0, sizeof(b));
        memset(c, 0, sizeof(c));
        string x,y; cin >> x >> y;
        la=x.size(),lb=y.size();
        lc=la+lb; //不要int了，不然成局域变量很麻烦 
        for(int i=0;i<la;i++) a[la-1-i]=x[i]-'0';
        for(int i=0;i<lb;i++) b[lb-1-i]=y[i]-'0';
        mul(a,b,c);
        for(int i=lc-1;i>=0;i--) cout << c[i];
        cout << "\n";
	}	
	return 0;
} 
