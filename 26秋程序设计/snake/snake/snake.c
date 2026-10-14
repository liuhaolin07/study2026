
//#include <stdio.h>
//#include <stdlib.h>
//#include <windows.h>
//
//#define WIDTH 30
//#define LENGTH 4
//
//int main(void)
//{
//    int x = 0;  // 蛇身最左端在内部区域的坐标
//
//    while (1)
//    {
//        system("cls");
//
//        for (int i = 0; i < WIDTH; i++)
//        {
//            if (i == 0 || i == WIDTH - 1)
//            {
//                printf("#");
//            }
//            else
//            {
//                int isSnake = 0;
//
//                for (int k = 0; k < LENGTH; k++)
//                {
//                    int pos = 1 + (x + k) % (WIDTH - 2);
//
//                    if (i == pos)
//                    {
//                        isSnake = 1;
//                        break;
//                    }
//                }
//
//                if (isSnake)
//                    printf("O");
//                else
//                    printf(" ");
//            }
//        }
//
//        printf("\n");
//        Sleep(200);
//
//        // 向右移动，并在右侧穿墙
//        x = (x + 1) % (WIDTH - 2);
//    }
//
//    return 0;
//}
#include <stdio.h>

int even(int n)
{
	return n % 2 == 0;
}
int main()
{
	int a;
	int sum = 0;
	while (1)
	{
		scanf_s("%d", &a);
		if (a == 0) break;
		if (even(a) == 0) sum += a;
	}
	printf("%d\n", sum);

	return 0;
}