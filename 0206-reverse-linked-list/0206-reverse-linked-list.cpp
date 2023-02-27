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
    ListNode* reverseList(ListNode* head) {
        
        ListNode* curr = head;
        ListNode* n_next = head;
        ListNode* prev = nullptr;
        
        while(curr != nullptr) {
            n_next = curr->next; // store next
            curr->next = prev; // reverse direction
            prev = curr;
            if(n_next == nullptr) {
                break;
            }
            curr = n_next;
        }
        return curr;
        
        
    }
};