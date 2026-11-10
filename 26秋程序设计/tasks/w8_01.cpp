//#include <iostream>
//using namespace std;
//const int N=1e5+10;
//int xn[N];
//int main()
//{
//	int x, y;
//    int cnt = 0;  // 记录读到了几个多项式
//    while (cnt < 2) {
//        if (!(cin >> x >> y)) break;
//        xn[x] += y;
//        if (x == 0) cnt++;  // 读到0次幂，说明一个多项式结束
//    }
//	for(int i=100;i>=0;i++)
//	{
//		if(xn[i]!=0&&i!=0) cout << xn[i] << "x" << i << "+";
//		if(i==0) cout << xn[0];
//	}
//	
//	return 0;
//} 
//#include <iostream>
//using namespace std;
//
//const int N = 101; 
//int xn[N];
//
//int main() {
//    int x, y;
//    int cnt = 0;  // 记录读到了几个多项式
//    while (cnt < 2) {
//        if (!(cin >> x >> y)) break;
//        xn[x] += y;
//        if (x == 0) cnt++;  // 读到0次幂，说明一个多项式结束
//    }
//
//    // 找到最高次幂
//    int maxN = -1;
//    for (int i = 100; i >= 0; i--) {
//        if (xn[i] != 0) {
//            maxN = i;
//            break;
//        }
//    }
//
//    // 全部为0的情况
//    if (maxN == -1) {
//        cout << 0 << endl;
//        return 0;
//    }
//
//    // 从高次到低次输出
//    bool first = true;
//    for (int i = maxN; i >= 0; i--) {
//        if (xn[i] == 0) continue;
//
//        // 处理符号
//        if (xn[i] > 0) {
//            if (!first) cout << "+";  // 非首项且为正，输出+
//        } else {
//            cout << "-";  // 负数输出-，后面输出绝对值
//        }
//
//        int absCoeff = xn[i] < 0 ? -xn[i] : xn[i];
//
//        // 输出系数和x部分
//        if (i == 0) {
//            cout << absCoeff;
//        } else if (i == 1) {
//            if (absCoeff == 1) cout << "x";
//            else cout << absCoeff << "x";
//        } else {
//            if (absCoeff == 1) cout << "x" << i;
//            else cout << absCoeff << "x" << i;
//        }
//
//        first = false;
//    }
//    cout << endl;
//
//    return 0;
//}

#include <iostream>
using namespace std;
const int N=101;
int xn[N];
int main()
{
	int cnt=0;
	int x,y;
	while(cnt<2)
	{
		if(!(cin>>x>>y)) break;
		xn[x]+=y;
		if(x==0) cnt++;
	}
	int maxn=-1;
	for(int i=100;i>=0;i--)
	{
		if(xn[i]!=0) {
			maxn=i;
			break; 
		}
		//忘记加break了，找到最高次就退出
		
	}
	if (maxn == -1) {
    cout << 0 << endl;
    return 0;
	}	
	for(int i=maxn;i>=0;i--)
	{
		if(xn[i]==0) continue;
		//这一步后保证maxn[i]不为零 
		//先判断符号
		if(i==maxn)
		{
			if(xn[i]<0) cout << "-";
		 } 
		else if(xn[i]>0) cout << "+";
		else cout << "-";
		//接下来输出系数和x部分 
		int xishu=xn[i]>0?xn[i]:-xn[i]; 
//		if(i!=0) cout << x;
//		cout << 
		//先拿特殊情况出来
		if(i==0) cout << xishu;
		else if(xishu==1) {
		cout << "x";
		if(i!=1) cout << i;
		}
		else {
		cout << xishu << "x";
		//最后输出次方
		if(i!=1) cout << i; 
		}
		
	}
	return 0;
}
