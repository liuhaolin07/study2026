#include <iostream>
using namespace std;
namespace name {
	int maxn(int a, int b) {
		return a > b ? a : b;
	}
}
namespace game {
	int maxn(int a, int b)
	{
		return a < b ? a : b; //不能写成a?b:a>b,三目运算符，问号前面式子为真则输出：前一个式子
	}
}
int main()
{
	int a, b; cin >> a >> b;
	cout << name::maxn(a, b) << " " << game::maxn(a, b) << endl;

	return 0;
}
