#include <iostream>
#include <string>
using namespace std;
int main()
{
	int n; cin >> n;
	while(n--)
	{
		int a,b; cin >> a >> b;
		string s;
		while(a>0)
		{
			s+= a%b+'0';
			a/=b;
		}
		for(int i=s.size()-1;i>=0;i--) cout << s[i];
		cout << '\n';
	}
	
	return 0;
}
