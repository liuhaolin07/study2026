# devcpp_2026 — Dev-C++ 练习

> 用 Dev-C++ 写的 C/C++ 代码。分两大块：**语言练习**和**刷题**。
> 这里不追求刷题量，重点是语言基本功 + 用 Dev-C++ 这个工具链顺手写题。

## 目录结构

```
devcpp_2026/
├── README.md
├── Week1/ … WeekN/        # 语言练习（语法、调试、内存）
│   └── hello_c.c
└── 刷题/                  # 用 Dev-C++ 写的算法题
    ├── 洛谷/               # Pxxxx 题号命名
    ├── Codeforces/         # 比赛名 + 题号命名
    ├── 牛客/               # 牛客网题目
    └── 其他/               # 杂项来源
```

## 语言练习（`WeekN/`）

按周组织，每周一个子目录。文件名用英文或拼音，不要留「未命名1.cpp」。

每个文件顶部加一行注释说明用途，例如：
```c
// hello_c.c — Dev-C++ 入门练习，输出 Hello World
#include <stdio.h>
int main() { printf("hello C\n"); return 0; }
```

## 刷题（`刷题/<平台>/`）

按平台分目录，文件名用**题号 + 题名**：

```
devcpp_2026/刷题/洛谷/P1001_A+B_Problem.cpp
devcpp_2026/刷题/Codeforces/CF1980-Div2_A_供电系统.cpp
```

每道题的 `.cpp` 文件顶部注释写清：
```cpp
// P1001 A+B Problem — 洛谷
// 考点: 输入输出
// 状态: AC ✅
```

## 提交约定

1. **只提交 `.c` / `.cpp` 源文件**，不提交 `.exe`、`.dev` 工程文件、编译产物（已在根 `.gitignore` 忽略）
2. 用 Dev-C++ 编译通过再提交
3. Commit message 格式：
   - 语言练习：`devcpp: Week2 指针练习`
   - 刷题：`devcpp: P1001 A+B Problem (洛谷)`

## 提交流程

```bash
# 写完 → Dev-C++ 编译通过 → git 提交
git add devcpp_2026/
git commit -m "devcpp: P1001 A+B Problem (洛谷)"
git push
```

> 💡 如果某天用 Dev-C++ 写的题属于**竞赛算法体系**，它该进 `Algorithms/topics/<专题>/`（那是主训练仓库的约定），这里只放 Dev-C++ 特有的语言练习和零散刷题。