//B.
#include <iostream>
#include <algorithm>
//好久没写算法题了，还是这种学一周就会的，不能只会初级的呀 
typedef long long ll;
using namespace std;
//AI的存在只会加速算法竞赛学习，对吗
//多个要素按优先级比大小，用结构体，是否还有其他解决办法
//struct Ban{
//	ll x,y,z;
//}B[3];
//int main()
//{
//	int t; cin >> t;
//	while(t--)
//	{
//		cin >> B[1].x >> B[1].y >> B[1].z;
//		cin >> B[2].x >> B[2].y >> B[2].z;
//				
//	}
//}
int main()
{
	int t; cin >> t;
	while(t--)
	{
		ll x1,y1,z1,x2,y2,z2;
		cin >> x1 >> y1 >> z1 >> x2 >> y2 >> z2;
		if(x1>x2) cout << ">" << endl;
		else if(x1<x2) cout << "<" << endl;
		else 
		{
			if(y1>y2) cout << ">" << endl;
			else if(y1<y2) cout << "<" << endl;
			else
			{
				if(z1>z2) cout << ">" << endl;
				else if(z1<z2) cout << "<" << endl;
				else cout << "=" << endl;
			 } 
		}
	}
	
	return 0;
}
