#include <stdio.h>
#include <string.h>

int mystrstr(char a[],char b[])
{
	int lena=strlen(a);
	int lenb=strlen(b);
	if(lenb==0) return 0;
	int i=0;
	for(i=0;i<=lena-lenb;i++)
	{
		int j;
		for(j=0;j<lenb;j++)
		{
			if(a[i+j]!=b[j]) break; //不匹配推出内层循环 
		}
		if(j==lenb) return i; 
	}
	return -1;
}

int main()
{
	char a[505],b[505];
	scanf("%s",a); scanf("%s",b);
	printf("%d\n",mystrstr(a,b));
	return 0;
}

