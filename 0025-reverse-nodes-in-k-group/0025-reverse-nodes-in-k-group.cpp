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
ListNode *getkth(ListNode *curr, int k)                                                                            
{
    while(curr && k>0)
    {
        curr= curr->next;
        k--;
    }
    return curr;
}
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode * dummy = new ListNode(0,head);
        ListNode * groupprev = dummy;
        while(1)
        {
            ListNode *kth = getkth(groupprev,k);
            if(kth == NULL)
            {
                break;
            }
            ListNode *groupnext = kth->next;
            ListNode * prev = groupnext;
            ListNode *curr = groupprev->next;
            while(curr!=groupnext)
            {
                ListNode * temp = curr->next;
                curr->next = prev;
                prev = curr;
                curr = temp;
            }
            ListNode * temp = groupprev->next;
            groupprev->next = kth;
            groupprev = temp;

        }
        return dummy->next;
    }
};