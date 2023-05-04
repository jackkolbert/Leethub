# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        head = ListNode(val=0,next=None)
        head_copy = head
        while l1 and l2:
            true_val_carry = int(carry)
            val = l1.val + l2.val + true_val_carry
            carry = int(val / 10)
            
            head.val = val % 10
            if l1.next and l2.next:
                head.next = ListNode()
                head = head.next
            
            l1 = l1.next
            l2 = l2.next
            
        if l1:
            head.next = l1
            while carry != 0:
                l1.val += carry
                if l1.val >= 10:
                    carry = int(l1.val/10)
                    l1.val = l1.val % 10
                    if l1.next:
                        l1 = l1.next
                    else:
                        l1.next = ListNode(val=carry, next=None)
                        carry = 0
                else:
                    carry = 0
            
        elif l2:
            head.next = l2
            while carry != 0:
                l2.val += carry
                if l2.val >= 10:
                    carry = int(l2.val/10)
                    l2.val = l2.val % 10
                    if l2.next:
                        l2 = l2.next
                    else:
                        l2.next = ListNode(val=carry, next=None)
                        carry = 0
                else:
                    carry = 0
                    
        elif carry != 0:
            head.next = ListNode(val=carry, next=None)
        return head_copy
        
        
            