#include <bits/stdc++.h>
using namespace std;
int main()
{
  int n;
  string d;
  cin >> n >> d;
  string s;
  int flag;
  for(int i=0;i<d.size();i++)
  {
    if(d[i]!='.') s+=d[i];
    else
    {
      flag=d.size()-i-1;
    }
  }
  while(n--)
  {
    string s1;
    int j=0;
    for(int i=s.size()-1;i>=0;i--)
    {
      s1[j++]=((s[i]-'0')*2)%10;
      s1[j]+=((s[i]-'0')*2)/10;
    }
    s=s1;
  }
  if(s[s.size()-flag]>='5') s[s.size()-flag-1]=(s[s.size()-flag-1]-'0')+1;
  else {};
  for(int i=0;i<s.size()-flag;i++) cout << s[i];
  return 0;
}
