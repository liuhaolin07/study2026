//#include <iostream>
//using namespace std;
//int main()
//{
//	int n, w; cin >> n >> w;
//	while (n--)
//	{
//		double v, s; cin >> v >> s;
//		//if (v / s <= w) cout << "Yes" << "\n";
//		if (v <= w * s) cout << "Yes" << "\n";
//		else cout << "NO" << "\n";
//	}
//
//	return 0;
//}

//#include <iostream>
//using namespace std;
//
//int main() {
//    ios::sync_with_stdio(false);
//    cin.tie(nullptr);
//
//    long long n, w;
//    cin >> n >> w;
//    while (n--) {
//        long long v, s;
//        cin >> v >> s;
//        if (v <= w * s)   // 用乘法代替除法，避免浮点误差
//            cout << "Yes\n";
//        else
//            cout << "NO\n";
//    }
//    return 0;
//}

//#include <iostream>
//#include <string>
//using namespace std;
//int main()
//{
//	int t;
//	cin >> t;
//	while (t--)
//	{
//		string s;
//		cin >> s;
//		if (s[0] == 'a' || s[1] == 'b' || s[2] == 'c') cout << "YES" << "\n";
//		else cout << "NO" << "\n";
//	}
//
//	return 0;
//}

//#include <iostream>
//#include <cstdio>
//using namespace std;
//int main()
//{
//	int a, b; scanf("%d/%d", &a, &b);
//	cout << "0.";
//	int count = 0;
//	while (1)
//	{
//		a = a * 10;
//		cout << a / b;
//		if (a % b == 0) break;
//		a = a % b;
//		count++;
//		if (count == 200) break;
//	}
//
//	return 0;
//}

//#include <iostream>
//using namespace std;
//const int N = 1e3 + 10;
//int a[N][N];
//
//int main()
//{
//	int n; cin >> n;
//	for (int i = 0; i < n; i++)
//	{
//		for (int j = 0; j < n; j++) cin >> a[i][j];
//	}
//	int count = 0;
//	for (int i = 0; i < n; i++)
//	{
//		//找第i行最大值
//		int hangmax = a[i][0];
//		for (int j = 0; j < n; j++)
//		{
//			if (a[i][j] > hangmax) hangmax = a[i][j];
//		}
//		//判断第i行最大值是不是这一列的最小值
//		//先找一下列标
//		
//		for (int j = 0; j < n; j++)
//		{
//			//检查该行所有等于最大值的位置
//			if (a[i][j] != hangmax) continue;
//			//每次检查新列时重新初始化
//			int niemin = a[0][j];
//			for (int k = 0; k < n; k++)
//			{
//				if (a[k][j] < niemin) niemin = a[k][j];
//			}
//			if (niemin == hangmax)
//			{
//				count++;
//				cout << i << " " << j << "\n";
//				return 0;
//			}
//		}
//		
//	}
//	cout << "NO" << "\n";
//
//	return 0;
//}

#include <iostream>
using namespace std;
int main()
{
	int t, s, p; cin >> t >> s >> p;
	if (2 * t == s + p || 2 * s == t + p || 2 * p == s + t) cout << "Yes" << "\n";
	else cout << "No" << "\n";

	return 0;
}