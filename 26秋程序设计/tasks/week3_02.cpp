#include <stdio.h>
int main()
{
	int b; scanf("%d",&b);
	int w12=b/100,w34=b%100;
//	int w1=b/1000,w2=b/100%10,w3=b/10%10;w4=b%10;
	if(w12<8)
	{
		printf("%d",w12+16); //Сʱ 
		if(w34<10) printf("0");
		printf("%d",w34); 
	}
	else  //w12>=8
	{
		if(w12==8)
		{
			printf("%d",w34); 
		}
		else
		{
			printf("%d",w12-8); //Сʱ
			if(w34<10) printf("0");
			printf("%d",w34); 		
		}
	}
	
	return 0;
}
