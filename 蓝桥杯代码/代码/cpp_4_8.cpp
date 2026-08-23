//#include <bits/stdc++.h>
//using namespace std;
//queue<int> q;
//int i;
//void print(queue<int> p)
//{
//    for(int k=1;k<=i;k++)
//    {
//      cout << p.front();
//      p.pop();
//    }
//    cout << endl;
//}
//int main()
//{
//  int n; cin >> n;
//
//  for(i=1;i<=n;i++)
//  {
//    if(i%4==1||i%4==3) q.push(2);
//    if(i%4==2) q.push(0);
//    if(i%4==0) q.push(6);
//    print(q);
//  }
//  
//  return 0;
//}

//#include <iostream>
//using namespace std;
//const int N=2e6+10;
//int m,a;
//int f[N];
//int fib(int i)
//{
//  if(i==0||i==1) return f[i]=i;
//  f[i]=f[i-1]+f[i-2];
//  return f[i];
//}
//int main()
//{
//  cin >> m >> a;
//  int cnt=0;
//  for(int i=1;i<=N;i++)
//  {
//    if(fib(i)%m==a) 
//    {
//      cnt++;
//      cout << i << endl;
//      return 0;
//    }
//  }
//  cout << -1 << endl;
//  return 0;
//}

//#include <bits/stdc++.h>
//using namespace std;
//const int N=3e5+10;
//int n,k,cnt;
//string s;
//void de()
//{
//  if(cnt==k) 
//  {
//    for(int z=0;z<n-k;z++)
//  {
//    if(s[z]!='*')
//      cout << s[z];
//  }
//  }
//}
//int main()
//{
//  cin >> n >> k;
//  //删去按顺序(从左往右)最小的k个数字
//  cin >> s;
//    for(int i=0;i<n;i++)
//  {
//    if(s[i]=='0')
//    {
//      s[i]='*'; cnt++;
//      de();
//    }
//  } 
//      for(int i=0;i<n;i++)
//  {
//    if(s[i]=='1')
//    {
//      s[i]='*'; cnt++;
//      de();
//    }
//  } 
//      for(int i=0;i<n;i++)
//  {
//    if(s[i]=='2')
//    {
//      s[i]='*'; cnt++;
//      de();
//    }
//  } 
//      for(int i=0;i<n;i++)
//  {
//    if(s[i]=='3')
//    {
//      s[i]='*'; cnt++;
//      de();
//    }
//  } 
//      for(int i=0;i<n;i++)
//  {
//    if(s[i]=='4')
//    {
//      s[i]='*'; cnt++;
//      de();
//    }
//  } 
//      for(int i=0;i<n;i++)
//  {
//    if(s[i]=='5')
//    {
//      s[i]='*'; cnt++;
//      de();
//    }
//  } 
//      for(int i=0;i<n;i++)
//  {
//    if(s[i]=='6')
//    {
//      s[i]='*'; cnt++;
//      de();
//    }
//  } 
//      for(int i=0;i<n;i++)
//  {
//    if(s[i]=='7')
//    {
//      s[i]='*'; cnt++;
//      de();
//    }
//  } 
//      for(int i=0;i<n;i++)
//  {
//    if(s[i]=='8')
//    {
//      s[i]='*'; cnt++;
//      de();
//    }
//  } 
//      for(int i=0;i<n;i++)
//  {
//    if(s[i]=='9')
//    {
//      s[i]='*'; cnt++;
//      de();
//    }
//  } 
//
//  return 0;
//}

//#include<bits/stdc++.h>
//using namespace std;
////map中对于value排序
////之前说的map是个键值对，所以需要vector
////来接收的话，那么就需要一对一，就需要用到pair了
// 
//bool cmp(const pair<string,int> a,pair<string,int>b){
//	return a.second>b.second;
//}
// 
//int main()
//{
//	map<string,int>m;
//	m["asas"]=18;
//	m["ioio"]=90;
//	m["cj"]=89;
//	vector<pair<string,int>>v(m.begin(),m.end());
//	sort(v.begin(),v.end(),cmp);
//	map<string,int>::iterator it;
//	for(int i=0;i<v.size();i++){
//		cout<<v[i].first<<" "<<v[i].second<<endl;
//	}
//	return 0;
//}

//#include <bits/stdc++.h>
//using namespace std;
//const int N=3e5+10;
//int n,k;
//string s;
//int main()
//{
//  cin >> n >> k;
//  cin >> s;
//  string s0=s;
//  sort(s.begin(),s.end());
//  int r1=0,r2=0; //r1--s0  r2--s
//  while(r1<n&&r2<k)
//  {
//    if(s0[r1]==s[r2])
//    {
//      s0[r1]='*';
//      r1++,r2++;
//    }
//    else r1++;
//  }
//  for(int i=0;i<n-k;i++)
//  {
//    if(s0[i]!='*') cout << s0[i];
//  }
//  return 0;
//}

#include <bits/stdc++.h>
using namespace std;
const int N=3e5+10;
int n,k;
string s;
int main()
{
  cin >> n >> k;
  cin >> s;
  string s0=s;
  sort(s.begin(),s.end());
  int r2=0; //r1--s0  r2--s
  while(r2!=k)
  {
  for(int r1=0;r1<n;r1++)
  {
    if(s0[r1]!='*'&&s0[r1]==s[r2])
    {
      s0[r1]='*';
      r2++;
      if(r2==k) break;
    }
  }
}
  for(int i=0;i<n-k;i++)
  {
    if(s0[i]!='*') cout << s0[i];
  }
  return 0;
}
