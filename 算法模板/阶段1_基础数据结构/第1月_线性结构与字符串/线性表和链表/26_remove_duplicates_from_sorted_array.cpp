/*
 * LeetCode 26. 删除有序数组中的重复项
 * 给你一个有序数组 nums，原地删除重复元素，返回新长度
 *
 * 核心思想：双指针（快慢指针）
 * 因为数组有序，重复元素相邻。
 * slow 指向已处理好的不重复序列末尾
 * fast 向前扫描，发现新元素就复制到 slow+1
 *
 * 时间复杂度 O(n)，空间复杂度 O(1)
 */

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return n;

        int slow = 0;  // 不重复序列的末尾下标
        for (int fast = 1; fast < n; fast++) {
            if (nums[fast] != nums[slow]) {
                slow++;                    // 腾出位置
                nums[slow] = nums[fast];   // 保留新元素
            }
        }
        return slow + 1;  // 长度 = 下标 + 1
    }
};

int main() {
    Solution sol;
    
    // 测试用例 1
    vector<int> nums1 = {1, 1, 2};
    int k1 = sol.removeDuplicates(nums1);
    cout << "输入: [1,1,2]" << endl;
    cout << "输出: " << k1 << ", nums = [";
    for (int i = 0; i < k1; i++) {
        cout << nums1[i];
        if (i < k1 - 1) cout << ",";
    }
    cout << "]\n" << endl;
    
    // 测试用例 2
    vector<int> nums2 = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    int k2 = sol.removeDuplicates(nums2);
    cout << "输入: [0,0,1,1,1,2,2,3,3,4]" << endl;
    cout << "输出: " << k2 << ", nums = [";
    for (int i = 0; i < k2; i++) {
        cout << nums2[i];
        if (i < k2 - 1) cout << ",";
    }
    cout << "]" << endl;
    
    return 0;
}
