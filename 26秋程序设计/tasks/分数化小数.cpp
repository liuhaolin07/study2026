#include<iostream>
#include <vector>
#include <string>
using namespace std;

#define ll long long
//模拟竖式除法

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	
	int n; cin >> n;
	while(n--)
	{
		ll a,b;
		int c;
		cin >> a >> b >> c;
		ll interger=a/b;
		ll re=a%b;
		string de;
		for(int i=0;i<=c;i++)
		{
			re*=10;
			int digit=re/b;
			de+=(char)('0'+digit);//数字加'0'转为字符，本质是ASCII码
			re%=b; 
		}
		//处理四舍五入
		//de目前有c+1位
		int carry=0;
		if(de[c]>='5')
		{
		carry=1;
		}
		de=de.substr(0,c);//截取前c个字符
		int i=c-1;
		while(carry&&i>=0)
		{
			int sum=(de[i]-'0')+carry;
			de[i]=(char)('0'+(sum%10));//sum%10是数字，+'0'转为字符 
			carry=sum/10;
			i--;
		 } 
		 //还有进位调整整数
		// 处理整数部分的进位
        interger += carry;

        cout << interger << "." << de << "\n";
	} 
	
	return 0;
}
