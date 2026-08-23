"// 链表常见操作
#include <bits/stdc++.h>
    using namespace std;

// 单链表节点
struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// 双链表节点
struct DoublyListNode
{
    int val;
    DoublyListNode *prev;
    DoublyListNode *next;
    DoublyListNode(int x) : val(x), prev(nullptr), next(nullptr) {}
};

// 反转链表（迭代）
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

// 判断是否有环
bool hasCycle(ListNode *head)
{
    if (!head || !head->next)
        return false;
    ListNode *slow = head;
    ListNode *fast = head->next;
    while (slow != fast)
    {
        if (!fast || !fast->next)
            return false;
        slow = slow->next;
        fast = fast->next->next;
    }
    return true;
}

// 合并两个有序链表
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

int main()
{
    // 测试反转链表
    ListNode *head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);

    cout << \"Original: \";
        for (ListNode *p = head; p; p = p->next) cout
         << p->val << \" \";
        cout
         << endl;

    head = reverseList(head);
    cout << \"Reversed: \";
        for (ListNode *p = head; p; p = p->next) cout
         << p->val << \" \";
        cout
         << endl;

    return 0;
}
"