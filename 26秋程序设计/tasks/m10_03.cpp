#include <iostream>
#include <cmath>
#include <string>
using namespace std;

int main()
{
	string s,t; cin >> s >> t;
	int lens=s.size(),lent=t.size();
//	for(int i=0;i<max(lens,lent);i++)
//	{
//		for(int j=0;j<lent;j++)
//		{
//			if(t[j]==t[i]) break;
//		}
//	}
	int i=0,j=0;
	while(i<lens&&j<lent)
	{
		if(s[i]==t[j]) 
		{
			i++;j++;
		}
		else i++;
	}
	if(j==lent) cout << "YES" << endl;
	else cout << "NO" << endl; 
	
	return 0;
}
