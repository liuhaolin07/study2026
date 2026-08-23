#include <iostream>
#include <cmath> 
#include <algorithm>
using namespace std;

struct byte
{
	char c1;
	char c2;
}b[5];

char mo(int m)
{
	if(m<=9) 
	{
		char c=m+'0';
		return c;
	}
	else
	{
		char c3=m-10+'A';
		return c3;
	}
}

int shu(char c)
{
	if(c-'0'<=9) 
	{
		int a=c-'0';
		return a;
	}
	else
	{
		int b=c-'A'+10; //注意要正确转换,A转为10 ,以此类推 
		return b;
	}
}

bool cmp(byte b1,byte b2)
{
	if(b1.c1!=b2.c1)
	{
		return b1.c1>b2.c1;
	}
	else
	{
		return b1.c2>b2.c2;
	}
}
int main()
{
	int n; cin >> n; //询问次数
	while(n--)
	{
		unsigned int m; cin >> m;
		for(int i=0;i<4;i++)
		{
			b[i].c2=mo(m%16);
			m/=16;
			b[i].c1=mo(m%16);
			m/=16;
		}

		//测试
//		for(int i=0;i<4;i++)
//		{
//			cout << b[i].c1 << b[i].c2;
//		}
//		cout << endl; 
		//存储形式由以上结构完成，接下来完成排序		
		sort(b,b+4,cmp);
//		for(int i=0;i<4;i++)
//		{
//			cout << b[i].c1 << b[i].c2;
//		}
		//排序测试无误,接下来转回十进制的无符号整型数
		//注意:要对b数组从前往后遍历,c2到c1,注意权重
		unsigned int sum=0;
		for(int i=0;i<4;i++)
		{
			sum=sum+shu(b[i].c2)*pow(16,2*i)+shu(b[i].c1)*pow(16,2*i+1); 
		} 
		cout << sum << endl;
		//测试样例通过	
	} 
	return 0;
}
