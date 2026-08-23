#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring> 
using namespace std;
int main()
{
    bool flag = 1;
    int i = 0;
    int n; cin >> n;
    int num = 2;
    int hit = 0;
    while (1)
    {
        flag = 1;   
        for (i = 2; i <= sqrt(num); i++)
        {
            if (num % i == 0)
            {
                flag = 0;
                break;
            }
        }
        if (flag)
            hit++;
        if (hit == n)
        {
            cout << num << endl;
            break;
        }
        num++;
    }
    return 0;
}
