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
        ListNode * res = new ListNode(0);
        ListNode * temp = res;
        int carry=0;
        int val = 0 ;
        while(l1 || l2 || carry)
        {
            val=0;
            if(l1)
            {val+= l1->val;
            l1 = l1->next;}
            if(l2)
            {
                val+=l2->val;
                l2 = l2->next;
            }
            val+=carry;
            carry = val/10;
            val = val%10;
            ListNode * valNode = new ListNode(val);
            temp->next = valNode;
            temp = temp->next;
        }
        return res->next;

        
    }
};