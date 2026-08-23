#include <iostream>
#include <vector>
using namespace std;
int main()
{
	vector<int> v;
	int n; cin >> n;
	v.push_back(6);
	v.push_back(10);
	v.push_back(15);
	for(int i=1;i<=10000;i++)
	{
		if(v.size()==n) break;
		if(i==6||i==10||i==15) continue;
		if(i%6==0||i%10==0||i%15==0)
		{
			v.push_back(i);
		}
	}
	for(int i=0;i<n;i++)
	{
		cout << v[i] << " "; 
	}
	return 0;
}
