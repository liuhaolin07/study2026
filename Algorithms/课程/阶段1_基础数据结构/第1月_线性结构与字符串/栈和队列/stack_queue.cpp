"// 栈和队列常见操作与实现
#include <bits/stdc++.h>
using namespace std;

// 用栈实现队列
class MyQueue {
private:
    stack<int> inStack, outStack;
    
    void transfer() {
        while (!inStack.empty()) {
            outStack.push(inStack.top());
            inStack.pop();
        }
    }
    
public:
    void push(int x) { inStack.push(x); }
    
    int pop() {
        if (outStack.empty()) transfer();
        int x = outStack.top();
        outStack.pop();
        return x;
    }
    
    int peek() {
        if (outStack.empty()) transfer();
        return outStack.top();
    }
    
    bool empty() { return inStack.empty() && outStack.empty(); }
};

// 有效括号判断
bool isValid(string s) {
    stack<char> st;
    for (char c : s) {
        if (c == '(' || c == '[' || c == '{') {
            st.push(c);
        } else {
            if (st.empty()) return false;
            if (c == ')' && st.top() != '(') return false;
            if (c == ']' && st.top() != '[') return false;
            if (c == '}' && st.top() != '{') return false;
            st.pop();
        }
    }
    return st.empty();
}

// 最小栈
class MinStack {
private:
    stack<int> dataStack;
    stack<int> minStack;
    
public:
    void push(int x) {
        dataStack.push(x);
        if (minStack.empty() || x <= minStack.top()) {
            minStack.push(x);
        }
    }
    
    void pop() {
        if (dataStack.top() == minStack.top()) {
            minStack.pop();
        }
        dataStack.pop();
    }
    
    int top() { return dataStack.top(); }
    int getMin() { return minStack.top(); }
};

int main() {
    // 测试括号匹配
    cout << "\"()[]{}\" isValid: " << isValid("()[]{}") << endl;
    cout << "\"(]\" isValid: " << isValid("(]") << endl;
    
    // 测试最小栈
    MinStack ms;
    ms.push(3);
    ms.push(5);
    cout << "Min after [3,5]: " << ms.getMin() << endl;
    ms.push(2);
    ms.push(1);
    cout << "Min after [3,5,2,1]: " << ms.getMin() << endl;
    ms.pop();
    cout << "Min after pop: " << ms.getMin() << endl;
    
    // 测试队列
    MyQueue q;
    q.push(1);
    q.push(2);
    cout << "Queue front: " << q.peek() << endl;
    cout << "Queue pop: " << q.pop() << endl;
    cout << "Queue empty: " << q.empty() << endl;
    
    return 0;
}"