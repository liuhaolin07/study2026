#include <stdio.h>
int ifrun(int m)
{
	if(m%400==0||(m%4==0&&m%100!=0)) return 1;
	else return 0;
}
int main()
{
	int n; scanf("%d",&n);
	while(n--)
	{
		int y; scanf("%d",&y);
		if(y<=0||ifrun(y)==0) printf("no\n");
		else printf("yes\n");
	}
	
	return 0;
}
