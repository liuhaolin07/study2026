#include <iostream>
#include <string>
using namespace std;
string s1="0123456789ABCDEF";
void n_to_m(int n,int m)
{
    if(n>=m)
        n_to_m(n/m,m);
    cout << s1[n%m];
}
int main()
{
    int n;
    string s;
    int m;
    cin >> n >> s >> m;
    //先将n进制转为十进制
    int num=stoi(s,NULL,n);
    //再将十进制转为m进制
    n_to_m(num,m);
    return 0;
}
