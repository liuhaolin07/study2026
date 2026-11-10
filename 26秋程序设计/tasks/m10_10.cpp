#include <iostream>
using namespace std;
int main()
{
	int n; cin >> n;
	while(n--)
	{
		int num; cin >> num;
		if(num>=100&&num<=999)
		{
			int bw=num/100;
			int sw=num/10%10;
			int gw=num%10;
			cout << gw <<"," << sw << "," << bw << endl;
		}
		else cout << "illegal" << endl;
	}
	return 0;
}
