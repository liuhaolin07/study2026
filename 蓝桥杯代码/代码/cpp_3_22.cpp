//#include <iostream>
//#include <string>
//#include <cctype>
//using namespace std;
//int main()
//{
//    string s;
//    getline(cin,s);
//    int num=0;
//    for(int e:s)
//    {
//        num+=isalpha(e);
//    }
//    cout << num << endl;
//    
//    return 0;
//}
//#include <iostream>
//using namespace std;
//int IFF(int d,int x,int y,int n)
//{
//    if(x>n||y>n)    return 1;
//    if(d==2&&x==y)    return 1;
//    if(d==1){
//    if(IFF(d+1,x,y,n)==0||IFF(d+1,y,x,n)==0)  return 1;}
//    if(d==2)
//    {
//        if(IFF(d-1,x,y,n)==0||IFF(d-1,y,x,n)==0)  return 1;
//    }
//}
//
//int main()
//{
//    int n,k;    cin >> n >> k;
//    int d,x,y;
//    int num=0;
//    for(int i=0;i<k&&(cin >> d >> x >> y);i++)
//    {
//        if(IFF(d,x,y,n))    num++;
//    }
//    cout << num << endl;
//    return 0;
//}
//#include <iostream>
//#include <cmath>
//#include <algorithm>
//using namespace std;
//const int N=3010;
//int arr[N];
//int brr[N];
//int main()
//{
//    int n;cin >> n;
//    for(int i=0;i<n;i++)
//        cin >> arr[i];
//    for(int i=0;i<n-1;i++)
//        brr[i]=abs(arr[i+1]-arr[i]);
//    sort(brr,brr+n-1);
//    int flag=1;
//    for(int i=0;i<n-1;i++)
//    {
//        if(i+1!=brr[i])   flag=0;
//    }
//    if(flag)    cout << "Jolly" << endl;
//    else cout << "Not jolly" << endl;
//    return 0;
//}
//#include <iostream>
//using namespace std;
//int IFF(int d,int x,int y,int n)
//{
//    if(d==1)
//    {
//        if(x>n||y>n)    return 1;
//        else if(IFF(d+1,x,y,n)==0||IFF(d+1,y,x,n)==0)  return 1;
//        else    return 0;
//    }
//    else
//    {
//        if(x>n||y>n)    return 1;
//        else if(x==y)    return 1;
//        else
//        {
//            if(IFF(d-1,x,y,n)==0||IFF(d-1,y,x,n)==0||IFF(d,y,x,n)==0) 
//                return 1;
//        }
//    }
//}
//
//int main()
//{
//    int n,k;    cin >> n >> k;
//    int d,x,y;
//    int num=0;
//    for(int i=0;i<k&&(cin >> d >> x >> y);i++)
//    {
//        if(IFF(d,x,y,n))    num++;
//    }
//    cout << num << endl;
//    return 0;
//}
#include <iostream>
#include <algorithm>
using namespace std;
const int N=1010;
int a[N];
int b[N];
int c[N];
int main()
{
    int n;cin >> n;
    for(int i=0;i<n;i++)
        cin >> a[i];
    int bn=0,cn=0;
    for(int i=0;i<n;i++)
    {
        if(a[i]%2)  b[bn++]=a[i];
        if(a[i]%2==0) c[cn++]=a[i];
    }
    sort(b,b+bn);
    sort(c,c+cn);
    for(int e:b)
        cout << e << " ";
    for(int d:c)
        cout << d << " ";

    return 0;
}

