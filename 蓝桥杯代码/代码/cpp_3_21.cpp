//#include <iostream>
//#include <cmath>  //floor包含在头文件cmath中
//const int N=1e6+10;
//int arr[N];
//int n;  //挑选结点数
//int num;  //编号
//using namespace std;
////int color(int x)
////{
////  if(x==1) return 1;
////  if(color(floor(num/2.0))&&(num%2==0)) return 1;
////  else if((color(floor(num/2.0))==0)&&num%2) return 1;
////  else return 0;
////}

//int color(int x)
//{
//  if(x==1) return 1;
//  if(x==3) return 0;
//  if(num%2==0) return color(x/2);
//  else
//  {
//    if(color(x/2))  return 0;
//    else return 1;
//  }
//}

//int main()
//{
//  cin >> n;
//  while(n--)
//  {
//    int a,b;
//    cin >> a >> b;
//    num=pow(2,a-1)+b-1;
//    int flag=color(num);
//    if(flag)  cout << "RED" << endl;
//    else cout << "BLACK" << endl;
//  }
//
//  return 0;
//}
//#include <iostream>
//using namespace std;
//
//const int N=1010;
//int a[N],b[N],c[N];
//
//int m;
//int x,y,z=0;
//int dx,dy,dz;
//void max(int& x,int &y)
//{
//	int c=y;
//	if(x>y)	
//	{
//		y=x;
//		x=c;
//	}
//}
//void sort(int& x,int& y,int& z)
//{
//	max(x,y);
//	max(x,z);
//	max(y,z);
//}
//int JIFEN(int x,int y,int z)
//{
//  if(a[x]==b[y]&&a[x]==c[z])
//    return 200;
//  if((a[x]+1==b[y])&&(b[y]+1==c[z]))
//    return 200;
////排序
//  sort(a[x],b[y],c[z]);
//  if((a[x]+1==b[y])&&(b[y]+1==c[z]))
//    return 100;
//  if(a[x]==b[y]||a[x]==c[z]||b[y]==c[z])
//    return 100;
//  else 
//  return 0;
//}
//int main()
//{
//  int n;cin >> n;
//  for(int i=0;i<=n;i++) cin >> a[i];
//  for(int i=0;i<=n;i++) cin >> b[i];
//  for(int i=0;i<=n;i++) cin >> c[i];
//  cin >> m;
//  int sum=0;
//  while(m--)
//  {
//    cin >> dx >> dy >>dz;
//    x = (x+dx)%n;
//    y = (y+dy)%n;
//    z = (z+dz)%n;
//    sum +=JIFEN(x,y,z);
//    cout << sum;
//  }
//  return 0;
//}
//#include <iostream>
//#include <string>
//using namespace std;
//
//int main() {
//    int num;
//    while (cin >> num) {
//        while (num != 1) {
            //for中continue后会执行i++语句
            // for (int i=2 ; i <= num; i++) {
            //     if (num % i == 0) {
            //         cout << i;
            //         num /= i;
            //         if (num != 1)  cout << "*";
            //         if(num%i==0)    continue;
            //     }
            // }
//            int i = 2;
//            while (i <= num) {
//                if (num % i == 0) {
//                            cout << i;
//                            num /= i;
//                            if (num != 1)  cout << "*";
//                            
//                }
//                if(num%i==0)    continue;
//                i++;
//            }
//            cout << endl;
//        }
//        return 0;
//    }
//}
//#include <iostream>
//using namespace std;
//int main()
//{
//    int num;
//    while(cin>>num)
//    {
//        int i=2;//放在内循环里面循环一次初始化一次，时间复杂度高
//        while(num!=1)
//        {
//            if(num%i==0)
//            {
//				cout << i;
//				num/=i;
//				if(num!=1)  cout << "*";
//			}    
//            if(num%i==0)  {continue;} 
//            i++;
//        }
//        cout << endl;
//    }
//    return 0;
//}
//#include <iostream>
//using namespace std;
//int main()
//{
//    int num;
//    while(cin>>num)
//    {
//        int i=2;//放在内循环里面循环一次初始化一次，时间复杂度高
//        while(num!=1)
//        {
//            if(num%i==0)
//            {    
//                cout << i;
//                num/=i;
//                if(num!=1)  cout << "*";    //这两行要放在if里面
//            }
//            else    
//            i++; 
//        }
//        cout << endl;
//    }
//    return 0;
//}
#include <iostream>
#include <cmath>
using namespace std;
bool IFSU(int n)
    {
        bool flag=true;
        for(int i=2;i<=sqrt(n);i++)
        {
            if(n%i==0)  flag=false;
        }
        return flag;
    }
int main()
{
    int num;
    
    while(cin>>num)
    {
        int i=2;//放在内循环里面循环一次初始化一次，时间复杂度高
        while(num!=1)
        {
            if(IFSU(num)) 
            {
                cout << num;
                break;
            }
            if(num%i==0)
            {    
                cout << i;
                num/=i;
                if(num!=1)  cout << "*";    //这两行要放在if里面
            }
            else    
            i++; 
        }
        cout << endl;
    }
    return 0;
}



