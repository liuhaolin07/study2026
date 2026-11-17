#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main()
{
    int n;
    cin >> n;
    while (n--)
    {
        double a, b, c;
        cin >> a >> b >> c;
        double s = sqrt(4 * a * a * b * b - (a * a + b * b - c * c) * (a * a + b * b - c * c)) / 4;
        cout << fixed << setprecision(2) << 2 * s / (a + b + c) << endl;
    }

    return 0;
}
