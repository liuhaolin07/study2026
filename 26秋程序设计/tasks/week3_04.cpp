#include <stdio.h>
#include <math.h>
int main()
{
	double a,b,c; scanf("%lf %lf %lf",&a,&b,&c);
	double s=(a+b+c)/2;
	double area=sqrt(s*(s-a)*(s-b)*(s-c));
	printf("a=%f\tb=%f\tc=%f\narea=%f",a,b,c,area);
	
	return 0;
}
