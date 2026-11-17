// #include <iostream>
// using namespace std;

// // 输出全排列
// void perm(int a[], int start, int end)
// {
//     if (start == end)
//     {
//         for (int i = 0; i < end; i++)
//         {
//             cout << a[i] << " ";
//         }
//         cout << endl;
//     }
//     else
//     {
//         for (int i = start; i < end; i++)
//         {
//             swap(a[start], a[i]);
//             perm(a, start + 1, end);
//             swap(a[start], a[i]);
//         }
//     }
// }

// int main()
// {
//     int n;
//     cout << "Enter the number of elements: ";
//     cin >> n;

//     int *a = new int[n];
//     cout << "Enter the elements: ";
//     for (int i = 0; i < n; i++)
//     {
//         cin >> a[i];
//     }

//     cout << "All permutations are:" << endl;
//     perm(a, 0, n);

//     delete[] a;
//     return 0;
// }
