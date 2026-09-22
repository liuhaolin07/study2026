#include <stdio.h>
#include <math.h>
int main()
{
	int num;
	int n; scanf("%d",&n); //²»ÒªÍü¼Ó& 
	int ret=1;
	while(n)
	{
		int temp=n%10;
		if(temp%2==ret%2)
		{
			num+=pow(2,ret-1);
		}
		n/=10;
		ret++;
//			printf("%d\n",num);
	}
	printf("%d",num);
	
	return 0;
}
