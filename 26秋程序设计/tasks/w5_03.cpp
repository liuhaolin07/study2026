#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	float t;int n; cin >> t >> n;
	float sum=0.0;
	for(int i=0;i<n;i++)
	{
		double temp;
		cin >> temp;
		sum+=temp;
		if(sum>=t)
		{
			printf("num=%d\naver=%10.2f",i+1,sum/(i+1));
			return 0;
		}
	}
	printf("num=%d\naver=%10.2f",n,sum/n);
	return 0;
}
