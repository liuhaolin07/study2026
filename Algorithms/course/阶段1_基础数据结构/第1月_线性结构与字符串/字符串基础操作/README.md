"# 字符串基础操作

## 学习目标

- [ ] 理解字符串的存储和基本操作
- [ ] 掌握 C++ 字符串函数
- [ ] 掌握常见字符串处理技巧
- [ ] 了解字符串哈希思想

## 核心概念

### C++ string 类
- 动态数组存储
- 支持随机访问
- 丰富的成员函数

### 常用操作
```cpp
string s = "hello";
s.size();              // 长度
s.empty();             // 判空
s[i];                  // 访问
s += " world";         // 拼接
s.substr(pos, len);    // 子串
s.find(sub);           // 查找
s.compare(t);          // 比较
```

### 常见算法模板

#### 反转字符串
```cpp
reverse(s.begin(), s.end());
```

#### 判断回文
```cpp
bool isPalindrome(string s) {
    int i = 0, j = s.size() - 1;
    while (i < j) {
        if (s[i] != s[j]) return false;
        i++; j--;
    }
    return true;
}
```

#### 字符串分割
```cpp
vector<string> split(string s, char delim) {
    vector<string> res;
    string cur;
    for (char c : s) {
        if (c == delim) {
            res.push_back(cur);
            cur.clear();
        } else {
            cur += c;
        }
    }
    if (!cur.empty()) res.push_back(cur);
    return res;
}
```

## 练习题

| 题目 | 难度 | 状态 |
|------|------|------|
| LeetCode 344: 反转字符串 | 简单 | ⬜ |
| LeetCode 125: 验证回文串 | 简单 | ⬜ |
| LeetCode 14: 最长公共前缀 | 简单 | ⬜ |
| LeetCode 151: 反转字符串中的单词 | 中等 | ⬜ |
| 洛谷 P1308: 统计单词数 | 简单 | ⬜ |"