"// 数组（顺序表）基本操作
#include <bits/stdc++.h>
using namespace std;

// 动态数组实现
class ArrayList {
private:
    int* data;
    int capacity;
    int size_;
    
    void resize() {
        capacity *= 2;
        int* newData = new int[capacity];
        for (int i = 0; i < size_; i++) {
            newData[i] = data[i];
        }
        delete[] data;
        data = newData;
    }
    
public:
    ArrayList() : capacity(4), size_(0) {
        data = new int[capacity];
    }
    
    ~ArrayList() {
        delete[] data;
    }
    
    // 末尾添加
    void push_back(int val) {
        if (size_ >= capacity) resize();
        data[size_++] = val;
    }
    
    // 中间插入
    void insert(int index, int val) {
        if (index < 0 || index > size_) return;
        if (size_ >= capacity) resize();
        for (int i = size_; i > index; i--) {
            data[i] = data[i - 1];
        }
        data[index] = val;
        size_++;
    }
    
    // 删除
    void erase(int index) {
        if (index < 0 || index >= size_) return;
        for (int i = index; i < size_ - 1; i++) {
            data[i] = data[i + 1];
        }
        size_--;
    }
    
    // 访问
    int get(int index) {
        if (index < 0 || index >= size_) return -1;
        return data[index];
    }
    
    // 大小
    int size() { return size_; }
    
    // 判空
    bool empty() { return size_ == 0; }
    
    // 打印
    void print() {
        cout << \"[ \";
        for (int i = 0; i < size_; i++) {
            cout << data[i] << \" \";
        }
        cout << \"]\\n\";
    }
};

// 示例：反转数组
void reverseArray(int arr[], int n) {
    int left = 0, right = n - 1;
    while (left < right) {
        swap(arr[left], arr[right]);
        left++;
        right--;
    }
}

// 示例：移除元素
int removeElement(vector<int>& nums, int val) {
    int slow = 0;
    for (int fast = 0; fast < nums.size(); fast++) {
        if (nums[fast] != val) {
            nums[slow++] = nums[fast];
        }
    }
    return slow;
}

// 示例：两数之和
vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> map;
    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        if (map.count(complement)) {
            return {map[complement], i};
        }
        map[nums[i]] = i;
    }
    return {};
}

int main() {
    // 测试动态数组
    cout << \"=== 动态数组测试 ===\\n\";
    ArrayList list;
    list.push_back(1);
    list.push_back(2);
    list.push_back(3);
    list.push_back(4);
    list.print();  // [1 2 3 4]
    
    list.insert(1, 10);
    list.print();  // [1 10 2 3 4]
    
    list.erase(2);
    list.print();  // [1 10 3 4]
    
    // 测试移除元素
    cout << \"\\n=== 移除元素测试 ===\\n\";
    vector<int> nums = {3, 2, 2, 3, 4, 3};
    int newLen = removeElement(nums, 3);
    cout << \"新长度: \" << newLen << \" \";
    for (int i = 0; i < newLen; i++) cout << nums[i] << \" \";
    cout << endl;
    
    // 测试两数之和
    cout << \"\\n=== 两数之和测试 ===\\n\";
    nums = {2, 7, 11, 15};
    auto res = twoSum(nums, 9);
    cout << \"索引: \" << res[0] << \", \" << res[1] << endl;
    
    return 0;
}
"