/*
 * LeetCode 26. 删除有序数组中的重复项
 *
 * 题目描述：
 *   给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，
 *   使每个元素 只出现一次 ，返回删除后数组的新长度。
 *
 *   元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。
 *
 *   要求：O(1) 额外空间
 *
 * 示例：
 *   输入：nums = [1,1,2]
 *   输出：2, nums = [1,2,_]
 *   解释：函数返回 2，且 nums 的前两个元素为 1 和 2。
 *
 *   输入：nums = [0,0,1,1,1,2,2,3,3,4]
 *   输出：5, nums = [0,1,2,3,4,_,_,_,_,_]
 *
 * 思路讲解：
 *
 * 核心方法：双指针（快慢指针）
 *
 * 由于数组是有序的，重复元素一定是相邻的。
 * 我们可以用两个指针来遍历数组：
 *   - slow（慢指针）：指向当前"已经处理好的不重复序列"的最后一个位置
 *   - fast（快指针）：向前遍历数组，寻找新的不重复元素
 *
 * 算法步骤：
 *   1. 如果数组长度 <= 1，直接返回原长度
 *   2. slow 从 0 开始，fast 从 1 开始
 *   3. 当 nums[fast] != nums[slow] 时，说明找到了新元素：
 *        - slow 向前移动一位
 *        - 将 nums[fast] 复制到 nums[slow]
 *   4. fast 继续向前移动
 *   5. 返回 slow + 1（因为 slow 是下标，长度需要 +1）
 *
 * 图解（nums = [0,0,1,1,1,2,2,3,3,4]）：
 *
 * 初始状态：
 *   slow=0, fast=1
 *   [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
 *    ↑
 *  slow/fast?
 *
 * 第1步：nums[1]==nums[0]，重复，fast++，slow不动
 *   slow=0, fast=2
 *   [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
 *    ↑     ↑
 *  slow   fast  (发现新元素 1)
 *
 * 第2步：nums[2]!=nums[0]，slow++，复制
 *   slow=1, fast=3
 *   [0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
 *       ↑     ↑
 *     slow   fast  (继续)
 *
 * 第3步：nums[3]==nums[1]，重复，fast++
 *   slow=1, fast=4 (还是1，重复)
 *   ...
 *
 * 第4步：nums[5]!=nums[1]，slow++，复制
 *   slow=2, fast=6
 *   [0, 1, 2, 1, 1, 2, 2, 3, 3, 4]
 *          ↑           ↑
 *        slow         fast
 *
 * 最终结果：
 *   slow=4
 *   [0, 1, 2, 3, 4, _, _, _, _, _]
 *             ↑
 *           slow
 *   返回 5
 *
 * 复杂度分析：
 *   时间复杂度：O(n)，只需遍历一次数组
 *   空间复杂度：O(1)，只使用了两个指针
 *
 * 思考延伸：
 *   如果要"最多保留2个重复项"（LeetCode 80），
 *   只需将比较条件改为 nums[fast] != nums[slow-1] 即可。
 */

#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    // 标准双指针解法
    int removeDuplicates(vector<int> &nums)
    {
        int n = nums.size();
        if (n <= 1)
            return n;

        int slow = 0; // 慢指针，指向不重复序列的末尾
        for (int fast = 1; fast < n; fast++)
        {
            // 找到新元素：当前元素与慢指针指向的元素不同
            if (nums[fast] != nums[slow])
            {
                slow++;                  // 慢指针前进
                nums[slow] = nums[fast]; // 将新元素保留到前面
            }
            // 如果相等，fast 继续向前，slow 不动
        }
        return slow + 1; // 长度 = 最后一个下标 + 1
    }

    // 另一种写法：更直观的计数法
    int removeDuplicates_v2(vector<int> &nums)
    {
        int n = nums.size();
        if (n <= 1)
            return n;

        int count = 1; // 至少有一个不重复元素
        for (int i = 1; i < n; i++)
        {
            if (nums[i] != nums[i - 1])
            {
                nums[count] = nums[i];
                count++;
            }
        }
        return count;
    }
};

// 测试
int main()
{
    cout << "=== LeetCode 26. 删除有序数组中的重复项 ===" << endl;

    Solution sol;

    // 测试用例1
    vector<int> nums1 = {1, 1, 2};
    cout << "\n测试1: [1,1,2]" << endl;
    int k1 = sol.removeDuplicates(nums1);
    cout << "结果长度: " << k1 << endl;
    cout << "数组前" << k1 << "个元素: ";
    for (int i = 0; i < k1; i++)
        cout << nums1[i] << " ";
    cout << endl;

    // 测试用例2
    vector<int> nums2 = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    cout << "\n测试2: [0,0,1,1,1,2,2,3,3,4]" << endl;
    int k2 = sol.removeDuplicates(nums2);
    cout << "结果长度: " << k2 << endl;
    cout << "数组前" << k2 << "个元素: ";
    for (int i = 0; i < k2; i++)
        cout << nums2[i] << " ";
    cout << endl;

    // 测试用例3：边界情况
    vector<int> nums3 = {1};
    cout << "\n测试3: [1]" << endl;
    int k3 = sol.removeDuplicates(nums3);
    cout << "结果长度: " << k3 << endl;

    // 测试用例4：所有元素相同
    vector<int> nums4 = {5, 5, 5, 5};
    cout << "\n测试4: [5,5,5,5]" << endl;
    int k4 = sol.removeDuplicates(nums4);
    cout << "结果长度: " << k4 << endl;
    cout << "数组前" << k4 << "个元素: ";
    for (int i = 0; i < k4; i++)
        cout << nums4[i] << " ";
    cout << endl;

    return 0;
}