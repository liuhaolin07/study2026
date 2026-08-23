//A.
#include <iostream>
using namespace std;
const int N=1e6+10;
int step[5],n;
bool vis[2*N];

bool ifprime(int m)
{
	for(int i=2;i*i<=m;i++)
	{
		if(m%i==0) return 0;
	}
	return 1;
}
//int num;
//void dfs(int pos)
//{
//	if(pos>=3&&ifprime(step[1]+step[2]))
//	{
//		num++;
//		if(num>n) return;
//		cout << step[1] << "+" << step[2] << "=" << step[1]+step[2] << endl;
//		return;
//	}
//	for(int i=1;i<=2*n;i++)
//	{
//		if(!vis[i])
//		{
//			vis[i]=true;
//			step[pos]=i;
//			dfs(pos+1);
//			vis[i]=false;
//		}
//	}
//}
//int main()
//{
//	int t; cin >> t;
//	while(t--)
//	{
//		cin >> n;
//		int num=0;
//		for(int i=1;i<=2*n;i++)
//		{
//			for(int j=i+1;j<=2*n;j++)
//			{
//				if(ifprime(i+j))
//				{
//					cout << i << "+" << j << "=" << i+j << endl;
//					num++;
//				} 
//				if(num==n) break;
//			}
//			if(num==n) break;
//		}
//		if(num!=n) cout << -1 << endl;
//	}
//	return 0;
//}

#include <iostream>
using namespace std;

void solve() {
    int t;
    cin >> t;
    while (t--) {
        long long n;
        cin >> n;
        if (n % 2 != 0) {
            cout << -1 << endl;
            continue;
        }
        if (n == 1) {
            cout << "1 2" << endl;
        } else if (n == 4) {
            cout << "1 6" << endl;
            cout << "2 3" << endl;
            cout << "4 7" << endl;
            cout << "5 8" << endl;
        } else {
            cout << "1 2" << endl; 
            for (long long i = 1; i <= n / 2; ++i) {
            }
        }
    }
}

int main() {
    solve();
    return 0;
}













//B.

//#include <iostream>
//#include <iomanip>
//#include <cmath>
//#define PI 3.1415926
//using namespace std;
//int main()
//{
//	double r, x; cin >> r >> x;
//	double m=x/r;
//	double d=x * (1 / cos(m) - 1);
//	
//	cout << fixed << setprecision(15) << min(d,2*PI*r-d) << endl;
//	return 0;
//}



