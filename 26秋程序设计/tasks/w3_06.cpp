#include <stdio.h>
#include <math.h>
int main()
{
	double a,b,c; scanf("%lf %lf %lf",&a,&b,&c);
	double m=b*b-4*a*c;
	if(m<0)
	{
		printf("This equation hasn't real roots");
		return 0;
	}
	double p=-b/2/a,q=sqrt(b*b-4*a*c)/2/a;
	printf("real roots:\nx1=%7.2f\nx2=%7.2f",p+q,p-q);
	
	return 0;
}
