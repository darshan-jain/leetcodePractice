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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {

        // int sizeA =0 ;
        // int sizeB = 0 ;
        // ListNode *currA;
        // currA = headA;
        // while (currA){
        //     sizeA++;
        //     currA=currA->next;
        // }

        // ListNode *currB;
        // currB = headB;
        // while (currB){
        //     sizeB++;
        //     currB=currB->next;
        // }

        // //make sure A is big - so exchange A & B if sizeA < sizeB
        // if(sizeA<sizeB)
        // {
        //     ListNode *temp = headA;
        //     headA = headB;
        //     headB = temp;
        // }

        // //A is always big 

        // ListNode *startptrA;
        // startptrA = headA;
        
        // while(startptrA){
        //     ListNode *valA = startptrA;
        //     ListNode *valB = headB;
        //     while(valA && valB)
        //     {
        //         if(valA == valB)
        //         {
        //             return valA;
        //         }
        //         else{
        //             valA = valA->next;
        //             valB = valB->next;
        //         }
        //     }
        //     startptrA = startptrA->next;
        // }

        // return NULL;

        ListNode *l1,*l2;
        l1 = headA;
        l2 = headB;
        while(l1!=l2)
        {
            if(l1)
            {
                l1 = l1->next;
            }
            else{
                l1 = headB;
            }

            if(l2)
            {
                l2 = l2->next;
            }
            else{
                l2 = headA;
            }
        }

        return l1;

        
    }
};