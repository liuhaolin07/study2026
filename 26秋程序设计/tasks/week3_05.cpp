#include <stdio.h>
#include <math.h>
int main()
{
	double a,b,c; scanf("%lf %lf %lf",&a,&b,&c);
	double p=-b/2/a,q=sqrt(b*b-4*a*c)/2/a; //注意运算先后顺序 
	printf("x1=%7.2f\nx2=%7.2f",p+q,p-q);
	
	return 0;
}
