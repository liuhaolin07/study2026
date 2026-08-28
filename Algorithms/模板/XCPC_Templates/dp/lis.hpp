#pragma once

#include <vector>
#include <algorithm>

/**
 * @brief 最长递增子序列 (LIS)
 * @param nums 输入数组
 * @return LIS 的长度
 * @time_complexity O(n log n)
 */
inline int lis_length(const std::vector<int>& nums) {
    if (nums.empty()) return 0;
    
    std::vector<int> tails;
    for (int num : nums) {
        auto it = std::lower_bound(tails.begin(), tails.end(), num);
        if (it == tails.end()) {
            tails.push_back(num);
        } else {
            *it = num;
        }
    }
    
    return tails.size();
}

/**
 * @brief 最长递增子序列 (LIS) - 获取具体序列
 * @param nums 输入数组
 * @return vector<int> LIS 序列
 * @time_complexity O(n log n)
 */
inline std::vector<int> lis_sequence(const std::vector<int>& nums) {
    if (nums.empty()) return {};
    
    int n = nums.size();
    std::vector<int> tails;
    std::vector<int> indices;
    std::vector<int> prev(n, -1);
    
    for (int i = 0; i < n; i++) {
        auto it = std::lower_bound(tails.begin(), tails.end(), nums[i]);
        int idx = it - tails.begin();
        
        if (it == tails.end()) {
            tails.push_back(nums[i]);
            indices.push_back(i);
        } else {
            *it = nums[i];
            indices[idx] = i;
        }
        
        if (idx > 0) {
            prev[i] = indices[idx - 1];
        }
    }
    
    // 重建序列
    std::vector<int> result;
    int curr = indices.back();
    while (curr != -1) {
        result.push_back(nums[curr]);
        curr = prev[curr];
    }
    std::reverse(result.begin(), result.end());
    
    return result;
}
