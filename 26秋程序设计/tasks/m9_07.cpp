#include <stdio.h>
int main()
{
	int n; scanf("%d",&n);
	int num=0;
	while(n--)
	{
		int a,b,c; scanf("%d %d %d",&a,&b,&c);
		
		for(int i=10;i<=100;i++)
		{
			if(i%3==a&&i%5==b&&i%7==c)
			{
				num=i;
				break;
			}
		}
		if(num==0) printf("Impossible\n");
		else 
		{
			printf("%d\n",num);
			num=0;
		}
	}
	
	return 0;
}
