"""Day 5 自定义模块示例
被 test.py 通过  from my_utils import average, max_min  使用。
同文件夹下的 .py 文件都可以当作模块被导入。
"""


def average(numbers):
    """返回平均值"""
    return sum(numbers) / len(numbers)


def max_min(numbers):
    """返回 (最大值, 最小值)"""
    return max(numbers), min(numbers)


if __name__ == "__main__":
    # 只有直接运行本文件时才执行；被别人 import 时不会执行
    data = [1, 2, 3, 4, 5]
    print("自测 average =", average(data))
    print("自测 max_min =", max_min(data))
