//#include <iostream>
//using namespace std;
//const int N=1e4+10;
//int arr[N];
//int main()
//{
//    int n;cin >> n;
//    int i=0;
//    for(i=0;i<n;i++)
//    {
//        cin >> arr[i];
//    }
//    int num;cin >> num;
//    int flag=0;
//    for(i=0;i<n;i++)
//    {
//        if(arr[i]==num)
//        {    cout << i;
//         flag++;
//        }
//    }
//    if(flag==0)
//    {
//        cout << "-1" << endl;
//    }
//    return 0;
//}
//#include <iostream>
//#include <string>
//using namespace std;
//int main()
//{
//    string s;
//    int ans=0;
//    getline(cin,s);
//    for(int i=0;i<s.size();i++)
//    {
//        if(s[i]!=' '&&s[i]!='\n')
//            ans++;
//    }
//    cout << ans << endl;
//    return 0;
//}
#include <iostream>
#include <string>
using namespace std;
int main()
{
    string s,s1;
    cin >> s;
    for(int i=0;i<s.size();i++)
        s1[i]=s[s.size()-1-i];
    if(s==s1)
        cout << "yes" <<endl;
    else 
        cout << "no" << endl;
    return 0;
}
