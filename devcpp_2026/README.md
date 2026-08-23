# devcpp_2026 — Dev-C++ 练习

> 用 Dev-C++ 写的 C/C++ 习题和练手代码，与 `Algorithms/`（竞赛体系）分开管理。
> 这里不追求刷题量，重点是**语言基本功**：语法、编译、调试、内存。

## 目录约定

按**周**组织，每周一个子目录：

```
devcpp_2026/
├── Week1/
│   └── hello_c.c          # 入门练习
├── Week2/
│   └── ...
└── ...
```

## 提交约定

1. **只提交 `.c` / `.cpp` 源文件**，不提交 `.exe`、`.dev` 工程文件、编译产物（已在根 `.gitignore` 忽略）
2. 文件名用英文或拼音，不要留「未命名1.cpp」
3. 每个文件顶部加一行注释说明用途，例如：
   ```c
   // hello_c.c — Dev-C++ 入门练习，输出 Hello World
   #include <stdio.h>
   int main() { printf("hello C\n"); return 0; }
   ```

## 提交流程

```bash
# 写完 → 编译通过 → git 提交
git add devcpp_2026/
git commit -m "devcpp: Week1 C语言入门练习"
git push
```

> 💡 如果某天用 Dev-C++ 写了一道**竞赛算法题**（不是语言练习），那题该进 `Algorithms/topics/<专题>/`，不进这里。