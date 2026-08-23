#include <iostream>
#include <string>
using namespace std;
int main()
{
	string s; cin >> s;
	int len=s.size();
	int ret=0;
	for(int i=0;i<len-5;++i)
	{
		if(s.substr(i,5)=="fjcpc") ++ret;
	}
	cout << ret << endl;
	return 0;
}
