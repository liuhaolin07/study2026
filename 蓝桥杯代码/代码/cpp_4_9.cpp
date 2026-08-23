//#include <bits/stdc++.h>
//using namespace std;
//struct pl{
//    int t,d,l;
//}p[15];
//bool st[15];
//int n;
//bool dfs(int u,int last)
//{
//    if(u==n) return 1;
//    for(int i=0;i<n;i++)
//    {
//        int t=p[i].t,d=p[i].d,l=p[i].l;
//        if(!st[i]&&(t+d)>=last)
//        {
//            st[i]=true;
//            if(dfs(u+1,max(last,t)+l)) return 1;
//            st[i]=false;
//        }
//    }
//    return 0;
//}
//int main()
//{
//    int t; cin >> t;
//    while(t--)
//    {
//        memset(st,0,sizeof(st));
//        cin >> n;
//        for(int i=0;i<n;i++)
//            cin >> p[i].t >> p[i].d >> p[i].l;
//        if(dfs(0,0)) cout << "YES" << endl;
//        else cout << "NO" << endl;
//    }
//    return 0;
//}

//#include <bits/stdc++.h>
//using namespace std;
//map<int,int> mp;
//int main()
//{
//    int n; cin >> n;
//    for(int i=1;i<=n;i++)
//    {
//        int a; cin >> a;
//        mp[a]=i;
//    }
//    int q; cin >> q;
//    while(q--)
//    {
//        int b; cin >> b;
//        if(mp[b]==0) cout << 0 << endl;
//        else
//        {
//            cout << mp[b] << endl;
//            mp[b]=0;
//        }
//    }
//    return 0;
//}

#include <bits/stdc++.h>
using namespace std;
int main()
{
	int sum=0;
	for(int i=1;i<=38;i++)
	{
		sum+=i;
	}
	cout << sum+20;
	return 0;
}
