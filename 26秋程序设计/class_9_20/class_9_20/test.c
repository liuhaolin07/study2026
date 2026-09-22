//#include <stdio.h>
//
//int main()
//{
//	int num = 1;
//	printf("My favourite num is %d.", num);
//
//
//	return 0;
//}


//#include <stdio.h>
//#include <limits.h>
//
//int main(void) {
//    printf("int: %zu 字节\n", sizeof(int));
//    printf("long: %zu 字节\n", sizeof(long));
//
//    printf("int 范围: %d ~ %d\n", INT_MIN, INT_MAX);
//    printf("long 范围: %ld ~ %ld\n", LONG_MIN, LONG_MAX);
//    //printf("%f", 10 / 3.0 * 3);
//    //printf("%f",10/3*3.0);
//    return 0;
//}

//#include <stdio.h>
//
//int main()
//{
//	int a; float b; char c;
//	scanf_s("%d %f %c", &a, &b, &c,1);
//	printf("%d,%f,%c", a, b, c);
//
//	return 0;
//}

//输入输出字符串

/*
#include <stdio.h>

int main(void)
{
    char str[100];

    scanf_s("%99s", str); //str表示字符数组的首地址
    //注意，scanf("%s", str) 遇到空格就会停止读取。
    //如果要读取包含空格的一整行，可以使用 fgets()。
    printf("%s\n", str);
    
}
*/

//C 语言字符串的本质是以 '\0' 结尾的字符序列。
// 字符串 "abc" 包含 3 个可见字符，但使用 sizeof("abc") 计算得到的大小是 4 字节。

//#include <stdio.h>
//
//int main()
//{
//    int c;
//    int b;
//    int a = 5;
//    c = (b = a + 2) - (a = 2);
//    printf("%d", c);
//    return 0;
//}
//输出5

#include <stdio.h>
int main()
{
    int a = 84891;
    float b = 85.64760974;
    printf("%-4d\t%5.2f\n", a, b);

    return 0;
}


