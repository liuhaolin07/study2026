# 快速开始

## 1. 准备环境

需要支持 C++17 的 `g++`。确认编译器可用：

```powershell
g++ --version
```

## 2. 运行完整测试

从项目根目录执行：

```powershell
.\tests\run_tests.ps1
```

预期输出：

```text
Checking standalone headers...
Checked 31 standalone headers.
Compiling template tests...
Running template tests...
All 72 checks passed
```

如果 MinGW 不能在中文路径下创建可执行文件，脚本会自动把测试程序输出到系统临时目录。

## 3. 使用模板

创建 `main.cpp`：

```cpp
#include "sorting/binary_search.hpp"

#include <iostream>
#include <vector>

int main() {
    const std::vector<int> values{1, 2, 2, 4};
    std::cout << lower_bound_index(values, 2) << '\n';
}
```

编译：

```powershell
g++ -std=c++17 -I".\XCPC_Templates" main.cpp -o main.exe
```

## 4. 学习一个算法

1. 从 [模板索引](./XCPC_Templates/README.md) 选择主题。
2. 阅读头文件中的复杂度与输入约束。
3. 不看模板手写一次，并补充一个边界测试。
4. 完成相关题目后更新 [PROGRESS.md](../course/PROGRESS.md)。

新增模板的质量要求见 [docs/MAINTENANCE.md](./docs/MAINTENANCE.md)。
