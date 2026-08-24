#include <iostream>
using namespace std;
int main()
{
	int n; cin >> n;
		//未考虑n为0的情况 
		if(n==0) {
			cout << "0";
			return 0; 
		}
	while(n)
	{
		int a=n%3;
		n=n/3;
		if(a==2) cout << "O";
		else if(a==1) cout << "o";
		else cout << "0";
		if(n) cout << ".";
	}
	
	return 0;
}
