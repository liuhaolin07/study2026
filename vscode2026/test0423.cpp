#include <iostream>
using namespace std;
const int N=1e5+10;
int a[N],n;
bool vis[N];
void dfs(int u)
{
    if(u>n)
    {
        for(int i=1;i<=n;i++) cout << a[i] << ' ';
        cout << endl;
    }
    for(int i=1;i<=n;i++)
    {
        if(!vis[i])
        {
            a[u]=i;
            vis[i]=true;
            dfs(u+1);
            vis[i]=false;
        }
    }
}
int main()
{
    cin >> n;
    dfs(1);
    return 0;
}