//16.分数化小数
#include <iostream>
using namespace std;

//模拟除法 
int main()
{
	int n; cin >> n;
	while(n--)
	{
		int s[1010]; 
		int a,b,c; cin >> a >> b >> c;
		s[0]=a/b; //整数部分 
		a=a-s[0]*b; //这里错了啊,找了好久,你必须要保证这里的a<b 
//		cout << s[0] << endl; 
		int cnt=1;
		//模拟除法要写对,不然等会一位上冒出来两位数 
		while(cnt<=c+1)
		{
			int x=a*10;
			s[cnt++] = x/b;
			a=x-(x/b)*b;
		}
		//出循环cnt==c +2,不妨多算一位方便进位 
		cnt--;
		//处理最后一位 
		if(s[cnt]>5)
		{
			s[cnt-1]+=1;
			cnt--;
		}
//				for(int i=1;i<=c;i++)
//		{
//			cout << s[i] << " ";
//		}
		//从后往前依次进位 
		while(cnt>0)
		{
			if(s[cnt]>=10)
			{
				s[cnt-1]+=s[cnt]/10; //注意:要以cnt>0为判断条件,cnt不能取0,否则会造成越界 
				s[cnt]-=(s[cnt]/10)*10; 
			}
			cnt--;
		} 
		//接下来输出
		cout << s[0] << ".";
		for(int i=1;i<=c;i++)
		{
			cout << s[i];
		}
		cout << endl; 
	}
	return 0;
} 
