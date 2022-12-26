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
        ListNode* temp = head;
        stack<ListNode*> my_stack; 
        int count = 0;
        while(temp) {
            my_stack.push(temp);
            temp = temp->next;
            count++;
         }
        temp = head;
        for(int i = 0; i < count/2; i++) {
            //4
            ListNode* temp2 = my_stack.top();
            my_stack.pop();
            
            //set 4 to point to 2
            temp2->next = temp->next;
            //set 1 to point to 4
            temp->next = temp2;

            //set temp to 4
            temp = temp->next->next;
           
        }
        temp->next = nullptr;
    }
    /*
     cout << "temp: " << temp->val << '\n';
            cout << "temp2: " << temp2->val << '\n';
            cout << "temp3: " << temp3->val << '\n';
     */      
    
};