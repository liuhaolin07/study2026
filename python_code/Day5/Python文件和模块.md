# Day 5 学习笔记：文件和模块

> 目标：程序能把结果存进文件、能读外部数据、会拆分代码成模块。
> 配套练习：`test.py`（可直接 `python test.py` 运行）、`scores.txt`、`scores.csv`

---

## 一、文件读写三步走

```python
with open("文件名", "模式", encoding="utf-8") as f:
    ...
```

### 常用模式

| 模式 | 含义 | 文件不存在时 |
|------|------|--------------|
| `"r"` | 只读（默认） | 报错 FileNotFoundError |
| `"w"` | 覆盖写入 | 自动新建 |
| `"a"` | 追加写入 | 自动新建 |

### 为什么用 `with`？

`with` 语句结束时**自动关闭文件**，不用手写 `f.close()`，即使中间报错也能正确关闭。

### ⚠️ Windows 最大的坑：编码

- 不写 `encoding="utf-8"` 时，Windows 默认用 GBK 打开文件；
- 读 UTF-8 文件会报 `UnicodeDecodeError` 或读到乱码；
- **读写一律显式加 `encoding="utf-8"`**。

---

## 二、读取文本的三种方式

```python
f.read()        # 一次性读整个文件 → 一个大字符串
f.readlines()   # 按行读 → 字符串列表，每行末尾带 "\n"
for line in f:  # 逐行迭代，内存友好（推荐）
    print(line.strip())   # strip() 去掉换行符和首尾空格
```

处理一行数据的经典套路：

```python
parts = line.strip().split()   # "张三 90" → ["张三", "90"]
name, score = parts[0], int(parts[1])
```

---

## 三、CSV 文件

CSV = 用逗号分隔的表格文本，Excel 可以直接打开。

```python
import csv

# 方式1：reader，每行是列表，按下标取
with open("scores.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)          # 单独取出表头
    for row in reader:
        print(row[0], row[2])      # 第0列姓名、第2列数学

# 方式2：DictReader，每行是字典，按列名取（推荐）
with open("scores.csv", "r", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["姓名"], row["数学"])
```

> 学到 Day 18 之后会用 pandas 的 `read_csv` 一行搞定，但 csv 模块是底层原理。

---

## 四、模块与 import

### 三种导入写法

```python
import math                 # 用 math.sqrt(2)
from math import sqrt       # 直接用 sqrt(2)
import numpy as np          # 起别名（约定俗成的缩写）
```

### 标准库常用模块速查

| 模块 | 用途 | 示例 |
|------|------|------|
| `math` | 数学函数 | `sqrt`, `floor`, `pi` |
| `random` | 随机数 | `randint(1,6)`, `random()`, `choice(...)` |
| `os` | 操作系统交互 | `os.listdir(".")`, `os.path.exists(p)` |
| `csv` | CSV 读写 | 见上节 |

### 导入自己写的文件

同文件夹下的 `my_utils.py` 就是一个模块：

```python
from my_utils import average, max_min
```

### `if __name__ == "__main__":`

写在 `.py` 底部的这段代码：
- **直接运行**该文件时会执行；
- 被**别人 import** 时不会执行。

用来放自测代码，两不耽误。见 `my_utils.py`。

---

## 五、常见报错对照

| 报错 | 原因 | 解决 |
|------|------|------|
| `FileNotFoundError` | 路径写错 / 不在对应文件夹下运行 | 先 `os.listdir(".")` 看当前目录；终端要 cd 到数据所在文件夹再运行 |
| `UnicodeDecodeError` | 编码不匹配 | 加 `encoding="utf-8"` |
| 中文乱码 | 写入时没指定编码 | 同上 |

---

## 六、今日任务验收

1. ✅ 会用 `open` + `with` 写/读 txt（test.py 第 1–4 节）
2. ✅ 会用 csv 模块读成绩单（第 3 节）
3. ✅ 会 import 标准库和自己写的模块（第 5 节）
4. ✅ 练习：读取成绩文件 → 平均分、最高分、排名榜（第 6 节）

**明日预告（Day 6）**：进入 NumPy 科学计算——ndarray 是后面所有数模工具的地基。
