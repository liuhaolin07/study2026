"""Day 5 自定义模块示例
被 test.py 通过  from my_utils import average, max_min  使用。
同文件夹下的 .py 文件都可以当作模块被导入。
关键概念：每个 .py 文件都有自己的 __name__ 属性——
直接运行本文件时它的值是 "__main__"，被 import 时则是文件名（不带 .py），
所以文末的 if 判断能区分"我是主角还是配角"。
"""


def average(numbers):
    """返回平均值（写 docstring 是好习惯：调用方悬停就能看到说明）"""
    return sum(numbers) / len(numbers)


def max_min(numbers):
    """返回 (最大值, 最小值)"""
    return max(numbers), min(numbers)


if __name__ == "__main__":
    # 只有直接运行本文件时才执行；被 test.py import 时不会执行。
    # 这样模块既能被复用，又能单独点开自测，两不耽误
    data = [1, 2, 3, 4, 5]
    print("自测 average =", average(data))
    print("自测 max_min =", max_min(data))
