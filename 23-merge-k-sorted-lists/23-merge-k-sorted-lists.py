# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 0:
            return None
        
        while len(lists) != 1:
            node = self.mergeTwoLists(lists[0], lists[1])
            lists.pop(0)
            lists.pop(0)
            lists.append(node)
        return lists[0]
        
        
    def mergeTwoLists(self, list1, list2):
        # return pointer to head of merged list
        head = ListNode()
        head_copy = head
        
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2=list2.next
            head = head.next
        
        if list1:
            head.next = list1
        else:
            head.next = list2
        return head_copy.next
        