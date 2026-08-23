def sort_numbers(numbers, reverse=False):
    return sorted(numbers, reverse=reverse)


def data_statistics(numbers):
    if not numbers:
        return None

    total = sum(numbers)
    count = len(numbers)

    return {
        "count": count,
        "sum": total,
        "average": total / count,
        "max": max(numbers),
        "min": min(numbers),
    }


nums = [12, 18, 9, 25, 30]

print("原列表：", nums)
print("升序：", sort_numbers(nums))
print("降序：", sort_numbers(nums, reverse=True))

result = data_statistics(nums)
if result:
    print("数据个数：", result["count"])
    print("总和：", result["sum"])
    print("平均值：", result["average"])
    print("最大值：", result["max"])
    print("最小值：", result["min"])
else:
    print("列表为空")
