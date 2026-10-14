#include <stdio.h>
int main()
{
	int n; scanf("%d",&n);
	int sum=0;
	for(int i=1;i<=n;i++) {
		sum+=i;
	}
	printf("%d\n",sum);
	sum=0;
	int j=1;
	while(j<=n)
	{
		sum+=j; 
		j++;
	}
	printf("%d\n",sum);
	sum=0;
	int k=1;
	do{
		sum+=k;
		k++;
	}while(k<=n);
	printf("%d",sum);
	
	return 0;
}
