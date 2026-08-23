#include <iostream>
#include <cstdio>
using namespace std;
int year, month, day;

int main() {
	int year, month, day;
	int flag = 1;
	int y, m, d; scanf("%4d%2d%2d", &y, &m, &d);
	for (year = y; year <= 8999; year++)
	{
		for (month = m; month <= 12; month++)
		{
			for (day = d+1; day <= 31; day++)
			{
				if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) {}
				else if (month == 4 || month == 6 || month == 9 || month == 11) {
					if (day > 30) continue;
				}
				else if (month == 2)
				{
					if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) //ÅÐ¶ÏÊÇ·ñÎªÈòÄê
					{
						if (day > 29) continue;
					}
					else
					{
						if (day > 28) continue;
					}
				}
				if (year % 100 == month % 10 * 10 + month / 10 && year / 100 == day % 10 * 10 + day / 10)
				{
					if (flag) {
						printf("%d%02d%02d\n", year, month, day);
						flag = 0;
					}
					if (year / 100 == year % 100)
					{
						printf("%d%02d%02d\n", year, month, day);
						return 0;
					}
				}
			}
		}
	}
	return 0;
}
