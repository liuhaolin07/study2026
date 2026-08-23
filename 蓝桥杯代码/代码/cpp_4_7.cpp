#include <bits/stdc++.h>
using namespace std;
queue<int> q;
int h,w; 
void print(queue<int> p) //这里不要传引用，不然元素会丢失 
{
	while(!p.empty())
	{
		cout << p.front();
		p.pop();
	}
	cout << endl;
}
void push_back(int i)
{
	if(i%4==1||i%4==3) q.push(2);
    if(i%4==2) q.push(0);
    if(i%4==0) q.push(5);
}
int main()
{
    //察觉到有先进先出的特点，与queue类似
    cin >> h >> w;
	int i=w;
    for(int j=1;j<=w;j++)
    {
        if(j%4==1||j%4==3) q.push(2);
        if(j%4==2) q.push(0);
        if(j%4==0) q.push(5);
    }
    while(h--)
    {
    	print(q);
		q.pop();
		i++;
		push_back(i);		
	}
    return 0;
}
