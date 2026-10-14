#include <iostream>
using namespace std;

int main()
{
	int n; cin >> n;
	int sum=0;
	n+=1;
	while(n--)
	{
		sum+=n;
	}
	
	cout << "sum=" << sum << endl;
	
	return 0;
}
