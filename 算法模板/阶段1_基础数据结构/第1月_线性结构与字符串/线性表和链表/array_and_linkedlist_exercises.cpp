// 数组和链表练习题

#include <iostream>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// 1. 反转链表
ListNode *reverseList(ListNode *head)
{
    ListNode *prev = nullptr;
    ListNode *curr = head;
    while (curr)
    {
        ListNode *next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}

// 2. 判断是否有环（快慢指针）
bool hasCycle(ListNode *head)
{
    ListNode *slow = head;
    ListNode *fast = head;
    while (fast && fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast)
            return true;
    }
    return false;
}

// 3. 合并两个有序链表
ListNode *mergeTwoLists(ListNode *l1, ListNode *l2)
{
    ListNode dummy(0);
    ListNode *cur = &dummy;
    while (l1 && l2)
    {
        if (l1->val < l2->val)
        {
            cur->next = l1;
            l1 = l1->next;
        }
        else
        {
            cur->next = l2;
            l2 = l2->next;
        }
        cur = cur->next;
    }
    cur->next = l1 ? l1 : l2;
    return dummy.next;
}

// 4. 删除链表的倒数第 N 个结点（快慢指针）
ListNode *removeNthFromEnd(ListNode *head, int n)
{
    ListNode dummy(0);
    dummy.next = head;
    ListNode *fast = &dummy;
    ListNode *slow = &dummy;

    // fast 先走 n+1 步
    for (int i = 0; i <= n; i++)
    {
        fast = fast->next;
    }
    // slow 和 fast 一起走
    while (fast)
    {
        slow = slow->next;
        fast = fast->next;
    }

    // 删除目标节点
    slow->next = slow->next->next;
    return dummy.next;
}

// 打印链表
void printList(ListNode *head)
{
    while (head)
    {
        cout << head->val << " -> ";
        head = head->next;
    }
    cout << "null\n";
}

int main()
{
    cout << "=== 链表练习题测试 ===\n\n";

    // 测试反转链表
    cout << "1. 反转链表:\n";
    ListNode *head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    cout << "原链表: ";
    printList(head);
    head = reverseList(head);
    cout << "反转后: ";
    printList(head);

    // 测试合并有序链表
    cout << "\n2. 合并有序链表:\n";
    ListNode *l1 = new ListNode(1);
    l1->next = new ListNode(3);
    l1->next->next = new ListNode(5);
    ListNode *l2 = new ListNode(2);
    l2->next = new ListNode(4);
    l2->next->next = new ListNode(6);
    cout << "L1: ";
    printList(l1);
    cout << "L2: ";
    printList(l2);
    ListNode *merged = mergeTwoLists(l1, l2);
    cout << "合并: ";
    printList(merged);

    // 测试环形链表
    cout << "\n3. 环形链表检测:\n";
    ListNode *cycleHead = new ListNode(1);
    cycleHead->next = new ListNode(2);
    cycleHead->next->next = new ListNode(3);
    cycleHead->next->next->next = cycleHead->next; // 3->2 形成环
    cout << "有环? " << (hasCycle(cycleHead) ? "是" : "否") << endl;

    // 测试删除倒数节点
    cout << "\n4. 删除倒数节点:\n";
    ListNode *delHead = new ListNode(1);
    delHead->next = new ListNode(2);
    delHead->next->next = new ListNode(3);
    delHead->next->next->next = new ListNode(4);
    cout << "原链表: ";
    printList(delHead);
    delHead = removeNthFromEnd(delHead, 2);
    cout << "删除倒数第2个: ";
    printList(delHead);

    return 0;
}
