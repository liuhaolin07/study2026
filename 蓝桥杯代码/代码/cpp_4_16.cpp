//#include <iostream>
//#include <cstdio> 
//using namespace std;
//int main()
//{
//	int n; cin >> n;
//	while (n--)
//	{
//		//注意输入格式 
//		int a, b, c; scanf("%d,%d,%d",&a,&b,&c);
//		if (a + b > c && a + c > b && b + c > a)
//		{
//			if (a * a + b * b > c * c && a * a + c * c > b * b && b * b + c * c > a * a)
//			{
//				cout << "acute" << endl;
//			}
//			else if (a * a + b * b == c * c || a * a + c * c == b * b || b * b + c * c == a * a)
//			{
//				cout << "right" << endl;
//			}
//			else
//			{
//				cout << "obtuse" << endl;
//			}
//		}
//		else
//		{
//			cout << "illegal" << endl;
//		}
//	}
//	return 0;
//}

//12
#include <stdio.h>
#include <math.h>
int main() {
    int n;
    double A = 0;   

    scanf("%d", &n);  // 有n组数据
    for (int i = 0; i < n; i++) {
        int m100=0, m50=0, m10=0, m5=0, m2=0, m1=0, m_10=0, m_5=0,m_1=0;

        scanf("%lf", &A);  // 读入一个整数
		m100=A/100; A=A-m100*100;
		m50=A/50; A=A-m50*50;
		m10=A/10; A=A-m10*10;
		m5=A/5; A=A-m5*5;		        
		m2=A/2; A=A-m2*2;
		m1=A/1; A=A-m1*1;
		m_10=A/0.1; A=A-m_10*0.1;
		m_5=A/0.05; A=A-m_5*0.05;
		m_1=A*100; //存在精度问题，进行四舍五入 
        printf("%d,%d,%d,%d,%d,%d,%d,%d,%d\n", m100, m50, m10, m5, m2, m1, m_10, m_5, m_1);  // 输出计算结果
    }

    return 0;
}
