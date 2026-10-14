#include <iostream>
#include <string>
using namespace std;

int path[6];
bool vis[6];
void dfs(int pos,int begin)
{
	if(pos>5)
	{
		for(int i=1;i<=5;i++)
		{
			cout << path[i];
		}
		cout << "\n";
		return;
	}
	for(int i=begin;i<=begin+4;i++)
	{
		if(vis[i]) continue;
		
		path[pos]=i;
		vis[i]=true;
		dfs(pos+1,begin);
		vis[i]=false;
	}
	
	return;
}
int main()
{
	int n; cin >> n;
	while(n--)
	{
		int a; cin >> a;
		dfs(1,a);
	}
	
	return 0;
}
