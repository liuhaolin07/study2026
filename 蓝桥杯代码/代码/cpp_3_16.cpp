#include <iostream>
#include <vector>
using namespace std;
//const int N=2e6+10;
//vector<int> a(N);
//void print(int p)
//{
//    cout << a[p] <<endl;
//}
//int main()
//{
//    a.push_back(0);
//    int n,m;cin >> n >> m;
//    int i=n;
//    while(i>=1)
//    {
//        int xn;
//        cin >> xn;
//        a.push_back(xn);
//        i--;
//    }
//    while(i<=m)
//    {
//        int xm;
//        cin >> xm;
//        print(xm);
//    }
//    return 0;    
//}
//int main()
//{
//    a.push_back(0);
//    int n,m;cin >> n >> m;
//    for(int i=1;i<=n;i++)
//        cin >> a[i]; 
//    while(m--)
//    {
//        int xm;
//        cin >> xm;
//        print(xm);
//    }
//    return 0;    
//}
const int N = 1e5+10;
int main()
{
    int a[N][N]={0};
    int flag,i,j,k;
    int n,q;cin >> n >> q;
    while(q--)
    {
        cin >> flag >> i >> j;
        if(flag==1)
        {
            int xn;
            cin >> xn;
            if(xn!=0)
                a[i][j]=xn;
        }
        else
            cout << a[i][j] << endl;
    }
    return 0;
}
