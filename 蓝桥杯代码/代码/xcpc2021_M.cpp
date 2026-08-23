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
