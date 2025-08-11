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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode * dummy = new ListNode(0);
        ListNode * tail = dummy;
        ListNode *curr1 = l1;
        ListNode *curr2 = l2;
        int carry = 0 ;
        int val1=0;
        int val2=0;
        int val=0;
        while(curr1 || curr2 || carry)
        {
            if(curr1)
            {val1 = curr1->val;
            curr1=curr1->next;
            }
            else
            val1 = 0 ;

            if(curr2)
            {val2 = curr2->val;
            curr2=curr2->next;}
            else
            val2=0;

            

            val = val1+val2+carry;
            carry = val/10;
            val=val%10;
            tail->next = new ListNode(val);
            tail = tail->next;

        }
        
        return dummy->next;
    }
};