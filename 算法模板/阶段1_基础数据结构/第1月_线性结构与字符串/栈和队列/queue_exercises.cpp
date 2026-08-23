"// 队列练习题
#include <bits/stdc++.h>
using namespace std;

// 1. 循环队列
class MyCircularQueue {
private:
    vector<int> data;
    int head, tail, size, capacity;
    
public:
    MyCircularQueue(int k) : capacity(k), size(0), head(0), tail(0) {
        data.resize(k);
    }
    
    bool enQueue(int value) {
        if (isFull()) return false;
        data[tail] = value;
        tail = (tail + 1) % capacity;
        size++;
        return true;
    }
    
    bool deQueue() {
        if (isEmpty()) return false;
        head = (head + 1) % capacity;
        size--;
        return true;
    }
    
    int Front() {
        if (isEmpty()) return -1;
        return data[head];
    }
    
    int Rear() {
        if (isEmpty()) return -1;
        return data[(tail - 1 + capacity) % capacity];
    }
    
    bool isEmpty() { return size == 0; }
    bool isFull() { return size == capacity; }
};

// 2. 滑动窗口最大值（单调队列）
vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    int n = nums.size();
    vector<int> result;
    deque<int> dq;  // 存储索引，保持递减
    
    for (int i = 0; i < n; i++) {
        // 移除不在窗口内的元素
        while (!dq.empty() && dq.front() <= i - k) {
            dq.pop_front();
        }
        
        // 保持单调递减
        while (!dq.empty() && nums[dq.back()] < nums[i]) {
            dq.pop_back();
        }
        
        dq.push_back(i);
        
        // 窗口形成后开始记录结果
        if (i >= k - 1) {
            result.push_back(nums[dq.front()]);
        }
    }
    
    return result;
}

// 3. 最近的请求次数
class RecentCounter {
private:
    queue<int> q;
    
public:
    int ping(int t) {
        q.push(t);
        // 移除 t-3000 之前的请求
        while (q.front() < t - 3000) {
            q.pop();
        }
        return q.size();
    }
};

// 4. 用队列实现栈
class MyStack {
private:
    queue<int> q;
    
public:
    void push(int x) {
        int size = q.size();
        q.push(x);
        for (int i = 0; i < size; i++) {
            q.push(q.front());
            q.pop();
        }
    }
    
    int pop() {
        int x = q.front();
        q.pop();
        return x;
    }
    
    int top() { return q.front(); }
    bool empty() { return q.empty(); }
};

int main() {
    cout << \"=== 队列练习 ===\\n\\n\";
    
    // 测试循环队列
    cout << \"1. 循环队列:\\n\";
    MyCircularQueue cq(3);
    cout << \"入队1: \" << cq.enQueue(1) << endl;
    cout << \"入队2: \" << cq.enQueue(2) << endl;
    cout << \"入队3: \" << cq.enQueue(3) << endl;
    cout << \"入队4(满): \" << cq.enQueue(4) << endl;
    cout << \"队首: \" << cq.Front() << endl;
    cout << \"队尾: \" << cq.Rear() << endl;
    
    // 测试滑动窗口最大值
    cout << \"\\n2. 滑动窗口最大值:\\n\";
    vector<int> nums = {1, 3, -1, -3, 5, 3, 6, 7};
    auto res = maxSlidingWindow(nums, 3);
    cout << \"窗口最大值: \";
    for (int x : res) cout << x << \" \";
    cout << endl;
    
    // 测试用队列实现栈
    cout << \"\\n3. 用队列实现栈:\\n\";
    MyStack st;
    st.push(1);
    st.push(2);
    st.push(3);
    cout << \"栈顶: \" << st.top() << endl;
    cout << \"弹出: \" << st.pop() << endl;
    
    return 0;
}
"