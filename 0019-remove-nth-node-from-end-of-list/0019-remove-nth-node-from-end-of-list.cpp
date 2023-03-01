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
        ListNode* temp_1 = head;
        ListNode* temp_2 = head;
        ListNode* prev = nullptr;
        
        if(head == nullptr || head->next == nullptr) {
            return nullptr;
        }
        for(int i = 0; i < n; i++) {
            temp_1 = temp_1->next;
        }
        
        while(temp_1 != nullptr) {
            temp_1 = temp_1->next;
            prev = temp_2;
            temp_2 = temp_2->next; // temp_2 is the node to be removed
        }
        if(prev == nullptr) {
            cout << "wtf";
            head = head->next;
        }
        else if(prev->next == nullptr || prev->next->next == nullptr) {
            prev->next = nullptr;
        }
        else {
            prev->next = prev->next->next;
        }
        return head;
    }
};