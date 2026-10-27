//01
//#include <iostream>
//using namespace std;

//int main()
//{
//	int n; cin >> n;
//	if(n<=6&&n>=0) cout << "Free" << endl;
//	else if(n>=7&&n<=17) cout << "Half" << endl;
//	else if(n>=18&&n<=59) cout << "Full" << endl;
//	else cout << "Free" << endl;
//	
//	return 0; 
//}

//02
//#include <iostream>
//using namespace std;
//
//int main()
//{
//	int n; cin >> n;
//	if(n==1) 
//	{
//		cout << "Not Prime" << endl;
//		return 0;
//	}
//	for(int i=2;i*i<=n;i++)
//	{
//		if(n%i==0) 
//		{
//			cout << "Not Prime" << endl;
//			return 0;
//		}
//	}
//	cout << "Prime" << endl;
//	
//	return 0; 
//}

//03
#include <iostream>
using namespace std;
int main()
{
	int n; cin >> n;
	for(int i=1;i<=(n+1)/2;i++)
	{
		for(int j=1;j<=(n+1)/2-i;j++) cout << " ";
		for(int k=1;k<=2*i-1;k++) cout << "*";
		cout << "\n";
	}
	for(int i=1;i<=(n-1)/2;i++)
	{
		int l=(n-1)/2;
		for(int j=1;j<=i;j++) cout << " ";
		for(int k=1;k<=2*(l+1-i)-1;k++) cout << "*";
		cout << "\n";
	}
	return 0;
}
