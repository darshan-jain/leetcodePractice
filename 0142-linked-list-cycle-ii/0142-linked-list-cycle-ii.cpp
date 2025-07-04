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
        int hasCycle = 0 ;
        ListNode * slow = head;
        ListNode * temp = head;
        ListNode * fast = head;
        while(fast && fast->next)
        {
            slow = slow->next;
            fast = fast->next->next;
            if(slow == fast)
            {
                hasCycle = 1;
                break;
            }
        }

        
        // O(n^2) Approach
        // if(hasCycle)
        // {
        //     while(temp)
        //     {
        //         do
        //         {
        //             if(temp==slow)
        //             {
        //                 return temp;
        //             }
        //             slow = slow->next;
        //         }while(slow!=fast);
        //         //fast = slow;
        //         temp = temp->next;
        //     }
        // }
        // else{
        //     return NULL;
        // }

        //O(n) Approach 
        if(hasCycle)
        {
            ListNode * ptr = head;
            while(ptr!=fast)
            {
                ptr= ptr->next;
                fast =fast->next;
            }
            return ptr;
        }
        return NULL;
        
    }
};