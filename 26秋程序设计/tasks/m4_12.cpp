#include <stdio.h>
int main()
{
	int n; scanf("%d",&n);
	while(n--)
	{
		int m; scanf("%d",&m);
		int count=0;
		while(m)
		{
			count+=m%2;
			m/=2;
		}
		printf("%d\n",count);
	}
	
	return 0;
}
