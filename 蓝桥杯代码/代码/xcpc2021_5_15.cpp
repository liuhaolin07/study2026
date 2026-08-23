//C.二维数组变换
//#include <bits/stdc++.h>
//using namespace std;
//
//int main() {
//    ios::sync_with_stdio(false);
//    cin.tie(nullptr);
//
//    int n, q;
//    cin >> n >> q;
//    vector<vector<int>> A(n, vector<int>(n));
//    for (int i = 0; i < n; i++) {
//        for (int j = 0; j < n; j++) cin >> A[i][j];
//    }
//
//    vector<vector<int>> tmp(n, vector<int>(n)); // 临时缓冲，开到 n*n 方便复用
//
//    while (q--) {
//        int op;
//        int x0, y0, x1, y1;
//        cin >> op >> x0 >> y0 >> x1 >> y1;
//
//        // 若题目是 1-based 坐标，转 0-based
//        x0--; y0--; x1--; y1--;
//
//        int L = x1 - x0 + 1;
//
//        // 拷贝子块到 tmp 的左上角 L*L
//        for (int i = 0; i < L; i++)
//            for (int j = 0; j < L; j++)
//                tmp[i][j] = A[x0 + i][y0 + j];
//
//        auto place = [&](int i, int j, int ni, int nj) {
//            A[x0 + ni][y0 + nj] = tmp[i][j];
//        };
//
//        for (int i = 0; i < L; i++) {
//            for (int j = 0; j < L; j++) {
//                int ni, nj;
//                if (op == 1) {           // rotate 90 clockwise
//                    ni = j;
//                    nj = L - 1 - i;
//                } else if (op == 2) {    // flip left-right
//                    ni = i;
//                    nj = L - 1 - j;
//                } else if (op == 3) {    // flip up-down
//                    ni = L - 1 - i;
//                    nj = j;
//                } else if (op == 4) {    // main diagonal
//                    ni = j;
//                    nj = i;
//                } else {                 // op == 5, anti-diagonal
//                    ni = L - 1 - j;
//                    nj = L - 1 - i;
//                }
//                place(i, j, ni, nj);
//            }
//        }
//    }
//
//    for (int i = 0; i < n; i++) {
//        for (int j = 0; j < n; j++) {
//            if (j) cout << ' ';
//            cout << A[i][j];
//        }
//        cout << '\n';
//    }
//    return 0;
//}

//M.数字模拟
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<string> g(5);
    for (int i = 0; i < 5; i++) {
        string a, b, c;
        cin >> a >> b >> c;
        g[i] = a + "." + b + "." + c; // 17 列
    }

    vector<vector<string>> pat(10);
    pat[0] = {"*****","*...*","*...*","*...*","*****"};
    pat[1] = {"....*","....*","....*","....*","....*"};
    pat[2] = {"*****","....*","*****","*....","*****"};
    pat[3] = {"*****","....*","*****","....*","*****"};
    pat[4] = {"*...*","*...*","*****","....*","....*"};
    pat[5] = {"*****","*....","*****","....*","*****"};
    pat[6] = {"*****","*....","*****","*...*","*****"};
    pat[7] = {"*****","....*","....*","....*","....*"};
    pat[8] = {"*****","*...*","*****","*...*","*****"};
    pat[9] = {"*****","*...*","*****","....*","*****"};

    string ans;
    for (int t = 0; t < 3; t++) {
        int start = t * 6; // 5 列数字 + 1 列分隔
        vector<string> blk(5);
        for (int r = 0; r < 5; r++) blk[r] = g[r].substr(start, 5);

        int digit = -1;
        for (int d = 0; d <= 9; d++) {
            if (blk == pat[d]) { digit = d; break; }
        }
        ans.push_back(char('0' + digit));
    }

    cout << ans << "\n";
    return 0;
}
