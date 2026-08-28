# 算法模板示例说明

这个目录包含所有算法的实现模板。每个算法都应该按照以下标准结构组织：

## 📁 单个算法的目录结构

```
算法名称/
├── README.md          # 详细说明文档
├── solution.py        # Python 实现
├── solution.cpp       # C++ 实现
├── test.py            # 测试用例
└── notes.md           # 学习笔记（可选）
```

## 📝 README.md 模板

```markdown
# [算法名称]

## 📖 算法描述

简述算法的基本概念和应用场景

## 🎯 问题定义

清晰描述该算法要解决的问题

## 💡 算法思想

- 核心思路
- 关键步骤
- 算法的优势和劣势

## 📊 复杂度分析

| 指标 | 复杂度 | 说明 |
|------|--------|------|
| 时间复杂度 | O(...) | 详细说明 |
| 空间复杂度 | O(...) | 详细说明 |
| 最好情况 | O(...) | 详细说明 |
| 最坏情况 | O(...) | 详细说明 |
| 平均情况 | O(...) | 详细说明 |

## 🔍 代码实现

查看 solution.py 和 solution.cpp

## 📋 测试用例

查看 test.py

## 🎓 相关题目

- LeetCode题号: 描述
- 其他平台题目

## 📚 参考资源

- 相关教科书或教程链接
```

## 🐍 Python 实现模板

```python
"""
[算法名称] - [描述]

时间复杂度: O(...)
空间复杂度: O(...)

作者: 
日期: 
"""

class [AlgorithmName]:
    \"\"\"[算法名称]的实现类\"\"\"
    
    def __init__(self):
        \"\"\"初始化\"\"\"
        pass
    
    def solve(self, *args):
        \"\"\"
        算法主方法
        
        参数:
            args: 输入参数
            
        返回:
            结果
        \"\"\"
        pass


# 使用示例
if __name__ == "__main__":
    algo = [AlgorithmName]()
    result = algo.solve(...)
    print(result)
```

## 🔨 C++ 实现模板

```cpp
#include <iostream>
#include <vector>
using namespace std;

/*
* [算法名称] - [描述]
* 
* 时间复杂度: O(...)
* 空间复杂度: O(...)
* 
* 作者: 
* 日期: 
*/

class AlgorithmName {
private:
    // 私有成员和辅助函数
    
public:
    // 构造函数
    AlgorithmName() {}
    
    // 主算法函数
    void solve() {
        // 实现
    }
};

int main() {
    AlgorithmName algo;
    algo.solve();
    return 0;
}
```

## ✅ 测试用例模板 (test.py)

```python
import unittest
from solution import [AlgorithmName]

class Test[AlgorithmName](unittest.TestCase):
    
    def setUp(self):
        \"\"\"测试前设置\"\"\"
        self.algo = [AlgorithmName]()
    
    def test_case_1(self):
        \"\"\"测试用例1\"\"\"
        input_data = ...
        expected = ...
        self.assertEqual(self.algo.solve(input_data), expected)
    
    def test_case_2(self):
        \"\"\"测试用例2\"\"\"
        pass
    
    def test_edge_case(self):
        \"\"\"边界情况\"\"\"
        pass

if __name__ == '__main__':
    unittest.main()
```

## 📋 检查清单

在完成每个算法时，请确保：

- [ ] README.md 包含完整说明
- [ ] Python 实现代码可运行
- [ ] C++ 实现代码可编译
- [ ] 至少 3-5 个测试用例
- [ ] 所有测试都通过（✅）
- [ ] 复杂度分析准确
- [ ] 代码注释清晰
- [ ] 包含使用示例

## 🎯 完成标准

### 基础要求
- ✅ 核心代码实现完整
- ✅ 逻辑正确，测试通过
- ✅ 代码有适当注释

### 进阶要求
- ✅ 有多种实现方式对比
- ✅ 优化版本说明
- ✅ 相关题目应用

### 优秀要求
- ✅ 有详细的图解说明
- ✅ 包含时间/空间优化方案
- ✅ 与其他算法的关联说明
- ✅ 面试常见问题总结

---

**继续加油！每个算法都是向算法大师的一步！** 🚀
