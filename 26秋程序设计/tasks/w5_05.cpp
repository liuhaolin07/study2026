#include <iostream>
using namespace std;
int main()
{
	int r,c; cin >> r >> c;
	cout << endl;
	for(int i=1;i<=r;i++)
	{
		for(int j=1;j<=c;j++)
		{
			cout << i*j << "\t";
		}
		cout << endl;
	}
	
	return 0;
}
