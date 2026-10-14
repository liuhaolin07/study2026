#include <iostream>
using namespace std;
int main()
{
	int n; cin >> n;
	while(n--)
	{
		int m; cin >> m;
		if(m>=1&&m<=9) cout << "number" << "\n";
		else if((m>='a'&&m<='z')||(m>='A'&&m<='Z'))
		{
			cout << "letter" << "\n"; 
		}
		else cout << "else\n";
	}
	
	return 0;
}
