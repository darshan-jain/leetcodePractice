/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if(head==NULL || (head->next==NULL && n>=1))
        return NULL;
        ListNode *slow = new ListNode(0);
        slow->next = head;
        ListNode * fast = head;
        while(n>0)
        {
            fast = fast->next;
            n--;
        }
        while(fast!=NULL)
        {
            slow = slow->next;
            fast = fast->next;
        }
        ListNode *todelete = slow->next;
        if(todelete == head)
        {
            head = head->next;
        }
        ListNode *item = slow->next->next;
        slow->next = item;
        return head;


    }
};