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
    void reorderList(ListNode* head) {
        
        ListNode * slow = head;
        ListNode * fast = head;
        while(fast!=NULL && fast->next!=NULL)
        {
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode * mid = slow->next;
        slow->next = NULL;
        ListNode * prev = NULL;
        while(mid!=NULL)
        {
            ListNode *temp = mid->next;
            mid->next = prev;
            prev = mid;
            mid = temp;
        }

        ListNode *l1 = head;
        ListNode *l2 = prev;
        while(l1 && l2)
        {
            ListNode *l1next = l1->next;
            ListNode *l2next = l2->next;
            l1->next = l2;
            l2->next = l1next;
            l1 = l1next;
            l2 = l2next;
        }
        


        
    }
};