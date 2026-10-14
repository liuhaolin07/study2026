#include <stdio.h>
#include <Windows.h>
int main()
{

	for (int pos = 0; pos <= 30; pos++)
	{
		printf("||");
		for (int i = 0; i <= pos; i++)
		{
			printf(" ");
		}
		printf("==>");
		for (int i = pos; i <= 27; i++)
		{
			printf(" ");
		}
		printf("||");
		printf("\r");
		Sleep(100);
	}


	
	return 0;
}

