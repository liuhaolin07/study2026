"// 字符串基础操作
#include <bits/stdc++.h>
using namespace std;

// 反转字符串
string reverseString(string s) {
    int left = 0, right = s.size() - 1;
    while (left < right) {
        swap(s[left], s[right]);
        left++;
        right--;
    }
    return s;
}

// 验证回文串
bool isPalindrome(string s) {
    int left = 0, right = s.size() - 1;
    while (left < right) {
        while (left < right && !isalnum(s[left])) left++;
        while (left < right && !isalnum(s[right])) right--;
        if (tolower(s[left]) != tolower(s[right])) return false;
        left++;
        right--;
    }
    return true;
}

// 最长公共前缀
string longestCommonPrefix(vector<string>& strs) {
    if (strs.empty()) return \"\";
    for (int i = 0; i < strs[0].size(); i++) {
        char c = strs[0][i];
        for (int j = 1; j < strs.size(); j++) {
            if (i >= strs[j].size() || strs[j][i] != c) {
                return strs[0].substr(0, i);
            }
        }
    }
    return strs[0];
}

// 反转字符串中的单词
string reverseWords(string s) {
    vector<string> words;
    string cur;
    for (char c : s) {
        if (c == ' ') {
            if (!cur.empty()) {
                words.push_back(cur);
                cur.clear();
            }
        } else {
            cur += c;
        }
    }
    if (!cur.empty()) words.push_back(cur);
    
    reverse(words.begin(), words.end());
    string res;
    for (int i = 0; i < words.size(); i++) {
        if (i > 0) res += \" \";
        res += words[i];
    }
    return res;
}

int main() {
    // 测试反转字符串
    cout << \"Reverse 'hello': \" << reverseString(\"hello\") << endl;
    
    // 测试回文
    cout << \"'A man, a plan, a canal: Panama' is palindrome: \"
         << isPalindrome(\"A man, a plan, a canal: Panama\") << endl;
    
    // 测试公共前缀
    vector<string> strs = {\"flower\", \"flow\", \"flight\"};
    cout << \"Longest common prefix: \" << longestCommonPrefix(strs) << endl;
    
    // 测试反转单词
    cout << \"Reverse words: '\" << reverseWords(\"the sky is blue\") << \"'\" << endl;
    
    return 0;
}"