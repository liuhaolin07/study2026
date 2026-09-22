#include <stdio.h>
int main()
{
	int x=0,y=0,c;  //记得初始化，不然x,y随机 
	while(scanf("%d",&c)&&c!=-1)
	{
//		printf("%d\n",c);
		if(c%2==1) x++;
		else y++;
//			printf("--%d %d--",x,y);
	}
	printf("%d %d",x,y);
	
	return 0;
}
