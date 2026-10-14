#include <iostream>
using namespace std;

int even(int n)
{
	if(n%2) return 0;
	else return 1;
}
int main()
{
	int a;
	int sum=0;
	while(scanf("%d",&a)==1)
	{
		if(even(a)==0) sum+=a;
	}
	printf("%d\n",sum);
	
	return 0;
}
