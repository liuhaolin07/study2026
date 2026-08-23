// cpp
#include <iostream>
#include <vector>
using namespace std;

// 二分查找模板 - 常用变体
// 1) 查找是否存在 (标准版)

bool binary_search_exists(const vector<long long>& a, long long target) {
	int l = 0, r = (int)a.size() - 1;
	while (l <= r) {
		int m = l + (r - l) / 2;
		if (a[m] == target) return true;
		else if (a[m] < target) l = m + 1;
		else r = m - 1;
	}
	return false;
}

// 2) lower_bound: 返回第一个 >= target 的索引（若都小于返回 n）
int lower_bound_idx(const vector<long long>& a, long long target) {
	int l = 0, r = (int)a.size(); // 维护区间 [l, r)
	while (l < r) {
		int m = l + (r - l) / 2;
		if (a[m] < target) l = m + 1;
		else r = m;
	}
	return l;
}

// 3) upper_bound: 返回第一个 > target 的索引（若都 <= 返回 n）
int upper_bound_idx(const vector<long long>& a, long long target) {
	int l = 0, r = (int)a.size(); // [l, r)
	while (l < r) {
		int m = l + (r - l) / 2;
		if (a[m] <= target) l = m + 1;
		else r = m;
	}
	return l;
}

// 4) 查找最后一个 <= target 的索引（若都 > 返回 -1）
int last_le_idx(const vector<long long>& a, long long target) {
	int idx = upper_bound_idx(a, target) - 1;
	if (idx >= 0 && idx < (int)a.size() && a[idx] <= target) return idx;
	return -1;
}

// 5) 查找第一个 >= target 的元素值例子
// usage: int i = lower_bound_idx(a, t); if (i < a.size()) use a[i]

// 说明：输入数组 a 必须是已排序（非降序）的。

int main() {
    // 示例用法
    vector<long long> a = {1, 3, 5, 7, 9};
    long long target = 5;

    // 1) 查找是否存在
    bool exists = binary_search_exists(a, target);
    cout << "Exists: " << exists << endl;

    // 2) lower_bound
    int lb_idx = lower_bound_idx(a, target);
    cout << "Lower bound index: " << lb_idx << endl;

    // 3) upper_bound
    int ub_idx = upper_bound_idx(a, target);
    cout << "Upper bound index: " << ub_idx << endl;

    // 4) last_le_idx
    int last_le = last_le_idx(a, target);
    cout << "Last index <= target: " << last_le << endl;

    return 0;
}