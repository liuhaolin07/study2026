 #include <iostream>
 using namespace std;

int main()
{
	int n; cin >> n;
	while(n--)
	{
		int a,b,c; cin >> a >> b >> c;
		cout << a/b << ".";
		a=a-b*(a/b);
		for(int i=1;i<=c-1;i++)
		{
			cout << a*10/b;
			a=a*10-b*(a*10/b);
		}
		int m=a*10/b;
		a=a*10-b*m;
		int n=a*10/b;
		if(n>=5) cout << m+1;
		else cout << m;
		cout << "\n";
	}
	
	return 0;	
 } 
