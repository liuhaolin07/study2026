//汉诺塔问题，函数递归 
#include <iostream>
#include <cmath>
using namespace std;

void hannuo(int n,char from,char to,char by)
{
	//只有一个盘子时 
	if(n==1)
	{
		cout << from << "->" << to << "\n";
		return;
	}
	//先把n-1个盘子由A经C移到B
	hannuo(n-1,from,by,to); 
	//接下来把第n个由A移到C，经由B 
	cout << from << "->" << to << "\n";
	//最后把n-1个由B经由A移到C
	hannuo(n-1,by,to,from); 	 
}
int main()
{
	int n; cin >> n;
	int k=pow(2,n)-1;
	hannuo(n,'A','C','B');
	cout << k << "\n";
	
	return 0;
}
