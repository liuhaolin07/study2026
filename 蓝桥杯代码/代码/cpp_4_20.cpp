#include <iostream>
using namespace std;
int main()
{
	int n; cin >> n;
	int a[5];
	while(n--)
	{
		for(int i=1;i<=4;i++) cin >> a[i];
		//冒泡 ，相邻元素比较 
//		for(int i=1;i<4;i++)
//		{
//			int flag=1;
//			for(int j=1;j<4;j++)
//			{
//				if(a[j+1]<a[j])
//				{
//					swap(a[j],a[j+1]);
//					flag=0;
//				}
//			}
//			if(flag==1) break;
//		}
		//下面这个就够用了
		for(int i=1;i<4;i++)
		{
			for(int j=i+1;j<=4;j++)
			{
				if(a[i]>a[j]) swap(a[i],a[j+1]); //保证最小的那个在最前面 
			}
		 } 
		for(int i=1;i<=4;i++) cout << a[i] << " ";
		cout << endl;
	}
	return 0;
}
