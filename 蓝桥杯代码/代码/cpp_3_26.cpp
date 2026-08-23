////对象指针，专门用来存储“类对象”在内存中的地址
//#include <iostream>
//#include <string>
//using namespace std;
//
//class Hero {
//public:
//	string name;
//	int hp;
//
//	void attack() {
//		cout << name << "发起了进攻！当前血量：" << hp << endl;
//	}
//};
//int main() {
//	//1.创建一个普通对象
//	Hero myHero;
//	myHero.name = "亚瑟";
//	myHero.hp = 1000;
//	//2.定义对象指针，并将其指向myHero对象的地址
//	Hero* ptr = &myHero;
//	//3.通过指针访问成员
//	//方式一：使用箭头运算符 ->
//	ptr->hp -= 100; //通过指针修改对象的hp属性
//	ptr->attack(); //通过指针调用对象的成员函数
//	//方式二：使用解引用运算符 *(先解引用，再用点号访问成员)
//	(*ptr).hp -= 100; //通过解引用修改对象的hp属性
//	(*ptr).attack(); //通过解引用调用对象的成员函数
//
//	return 0;
//}

//测验：无人机管理系统
#include <iostream>
using namespace std;

class Drone{
public:
	int id;
	static int totalCount;
	Drone(){
		id=0;
		totalCount++;
	}
	void showTotal(){
		cout << "该无人机编号为：" << id << endl; 
	}
	static void Drone::showTotal(){
		cout << "当前无人机的总数量为：" << totalCount << endl;
	}
}; 
//必不可少的一步：静态成员变量必须在类外进行初始化！
int Drone::totalCount=0;

int main()
{
	Drone fleet[3];
	Drone* ptr=fleet;
	for(int i=0;i<3;i++)
	{
		ptr->id=101+i;
		ptr->showTotal();
		
		ptr++;
	}
	
	cout << endl;
	
	Drone::showTotal();
	
	return 0;
}

