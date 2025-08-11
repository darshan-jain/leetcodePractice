/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        int hasCycle = 0;
        ListNode * slow = head;
        ListNode *fast = head;
        while(fast && fast->next)
        {
            slow = slow->next;
            fast = fast->next->next;
            if(slow == fast)
            {
                hasCycle=1;
                break;
            }

        }

        if(hasCycle==0)
        {
            return NULL;
        }
        ListNode *ptr = head;
        while(ptr!=slow)
        {
            ptr = ptr->next;
            slow = slow->next;
        }
        return ptr;
        
    }
};