# Day 19 学习笔记：数据读取与导出

> 目标：csv / excel 双向读写，掌握乱码与索引两个高频坑。
> 前置安装：`pip install pandas openpyxl`
> 配套练习：`test.py` + `students.csv`

---

## 一、读 CSV

```python
df = pd.read_csv("data.csv", encoding="utf-8")
```

常用参数：

| 参数 | 作用 |
|------|------|
| `encoding` | 中文文件常见 utf-8 / gbk；Excel 友好导出用 utf-8-sig |
| `index_col="学号"` | 指定某列做行索引 |
| `usecols=[...]` | 只读部分列（大文件提速） |
| `nrows=N` | 先读 N 行预览 |
| `parse_dates=["日期"]` | 直接把列解析成日期类型 |

## 二、读 / 写 Excel

```python
df = pd.read_excel("data.xlsx")            # 需要 openpyxl
df.to_excel("out.xlsx", sheet_name="表1", index=False)
```

报 `ImportError: Missing optional dependency 'openpyxl'` → `pip install openpyxl`。

## 三、导出

```python
df.to_csv("out.csv", index=False, encoding="utf-8-sig")
```

- **`index=False`**：不把 0,1,2,… 行号写进文件（十有八九你不想写）；
- **`encoding="utf-8-sig"`**：Windows 下用 Excel 双击打开不乱码。

## 四、读写闭环检查清单

读入后立刻执行：

```python
df.head()     # 长得对不对？
df.info()     # 行数、缺失、类型
df.describe() # 数值是否合理（有没有 -999 当缺失值之类的脏东西）
```

## 五、今日任务验收

- ✅ 读 students.csv 并完成按班汇总
- ✅ csv ↔ xlsx 互转闭环
- ✅ usecols 局部读取；追加总分列后导出 total.xlsx

**明日预告（Day 20）**：数据清洗——真实数据永远是脏的。
