#include <iostream>
using namespace std;

int main()
{
	int n; cin >> n;
	while(n--)
	{
		char c; cin >> c;
		if(c>='0'&&c<='9')
		{
			cout << "number" << endl;
		}
		else if((c>='a'&&c<='z')||(c>='A'&&c<='Z'))
		{
			cout << "letter" << endl;
		}
		else cout << "else" << endl;
	}
	
	return 0;
}
