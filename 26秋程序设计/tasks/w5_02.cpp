#include <iostream>
#include <string>
using namespace std;

string zhuan(char c)
{
	if(c=='0') return "ling";
	if(c=='1') return "yi";
	if(c=='2') return "er";
	if(c=='3') return "san";
	if(c=='4') return "si";
	if(c=='5') return "wu";
	if(c=='6') return "liu";
	if(c=='7') return "qi";
	if(c=='8') return "ba";
	if(c=='9') return "jiu";
}
int main()
{
	int n; cin >> n;
	if(n<0)
	{
		cout << "fu ";
		n=-n;
	}
	string s=to_string(n);
	int num=s.length();
	for(int i=0;i<num-1;i++)
	{
		cout << zhuan(s[i]) << " ";
	}
	cout << zhuan(s[num-1]);
	
	return 0;
}
