#include <iostream>
#include <cstdio>
using namespace std;

const int N=15;

int arr[N][N];

int dx[4]={0,1,0,-1};
int dy[4]={1,0,-1,0};
//       右 下 左 上 

int x=1,y=1; //初始坐标
int pos; 
int main()
{
	int n;cin >> n;
	int cnt=1;
	while(cnt<=n*n)
	{
		arr[x][y]=cnt;
		int a,b;
		a=x+dx[pos];
		b=y+dy[pos];
		
		//判断越界
		if(b>n||a>n||b<1||arr[a][b])
		{
			pos=(pos+1)%4;
			a=x+dx[pos];
			b=y+dy[pos];
		 } 
		x=a;
		y=b;
		cnt++;//存储下一个数字 
	}
	for(int i=1;i<=n;i++)
	{
		for(int j=1;j<=n;j++)
			printf("%3d",arr[i][j]);
		cout << endl;
	}
	return 0;
 } 
