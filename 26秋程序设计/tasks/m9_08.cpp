#include <stdio.h>

int shui(int a)
{
	int w1=a/100,w2=a/10%10,w3=a%10;
	if(a==(w1*w1*w1+w2*w2*w2+w3*w3*w3)) return 1;
	else return 0;
}
int main()
{
	int t; scanf("%d",&t);
	while(t--)
	{
		int m,n; scanf("%d %d",&m,&n);
		int count=0;
		for(int i=m;i<=n;i++)
		{
			if(shui(i))
			{
				count++;
				printf("%d ",i);
			}
		}
		if(count==0) printf("%d",-1);
		printf("\n");
	}
	
	return 0;
}
