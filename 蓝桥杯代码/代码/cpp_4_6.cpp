#include <bits/stdc++.h>
using namespace std;
int num,sum[20];
string s;
int main()
{
	
    for(int i=1;i<=20262026;i++)
    {
		memset(sum,0,sizeof(sum));
        s=to_string(i);
        for(int i=0;i<s.size();i++)
        {
            sum[s[i]]++;
        }
        if(sum['2']==2&&sum['0']==1&&sum['6']==1)
            num++;
    }
    cout << num << endl;
    return 0;
}
