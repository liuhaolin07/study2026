#include <iostream>
#include <cstring>
using namespace std;
int main()
{
	int arr[10]={1,2,3,4,5,6,7,8,9,10};
	for(const auto i:arr)
		cout << i << ' ';
	cout << endl;
	int b[10]={0};
	memcpy(b,arr,sizeof(b));
	for(const auto j:b)
		cout << j << ' ';
	
	return 0;
}
