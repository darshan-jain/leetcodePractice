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
    ListNode* rotateOnce(ListNode* head)
    {
        ListNode* last = head->next;
        ListNode* prev = head;
        int len = 1;
        while(last->next)
        {
            last = last->next;
            prev = prev->next;
        }
        last->next = head;
        head = last;
        prev->next = NULL;
        return head;
    }
    ListNode* rotateRight(ListNode* head, int k) {
        if(!head)
        return NULL;
        if(head->next==NULL)
        {
            return head;
        }
        ListNode * curr = head;
        int len = 0;
        while(curr)
        {
            curr = curr->next;
            len++;
        }
        cout<<len;

        k = k%len;

        while(k>0)
        {
            head = rotateOnce(head);
            k--;
        }
        return head;
        
    }
};