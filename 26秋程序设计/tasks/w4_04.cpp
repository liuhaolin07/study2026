#include <iostream>
using namespace std;
typedef long long ll;
int main()
{
	int n ; cin >> n;
	ll sum=0;
	do{
		sum+=n*n;
	}while(n--);
	
	cout << "sum=" << sum << endl;
	
	return 0;
}
