#include <stdio.h>
int main()
{
	int n; scanf("%d",&n);
	for(int i=0;i<n;i++){
		int a[5];scanf("%d %d %d %d",&a[0],&a[1],&a[2],&a[3]);
		//冒泡排序
		for(int i=0;i<3;i++)
		{
			for(int j=0;j<3-i;j++)
			{
				if(a[j]>a[j+1])
				{
					int temp=a[j];
					a[j]=a[j+1];
					a[j+1]=temp;
				}
			}
			//i=0，最大的移到末尾；i=1，第二大的移到倒数第二位 
		} 
		printf("%d %d %d %d\n",a[0],a[1],a[2],a[3]);
		
	}	
	
	return 0; 
}
