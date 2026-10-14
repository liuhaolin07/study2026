#include <iostream>
#include <string>
using namespace std;
int main()
{
    int n; cin >> n;
    while (n--)
    {
        string s; cin >> s;
        int m = s.length();
        if (m > 10)
        {
            cout << s[0] << m-2 << s[m-1] << endl;
        }
        else cout << s << endl;
    }

    return 0;
}
