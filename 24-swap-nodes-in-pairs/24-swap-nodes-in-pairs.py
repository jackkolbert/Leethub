# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        if head.next is None:
            return head
        
        first = True
        ret = None
        node1 = head
        node2 = head.next
        prev = None
        while True:
            print(node1.val)
            print(node2.val)
            next_head = node2.next
            if first:
                first = False
                ret = node1.next
    
            node2.next = node1
            node1.next = next_head
            
            if prev:
                prev.next = node2
            prev = node1
            
            if next_head is None or next_head.next is None:
                break
            node1 = next_head
            node2 = next_head.next
        return ret