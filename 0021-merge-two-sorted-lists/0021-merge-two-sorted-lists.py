class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(0, None)
        temp = head
        while list1 and list2:
            if list1.val > list2.val:
                head.next = list2
                list2 = list2.next
            else:
                head.next = list1
                list1 = list1.next
            head = head.next
            
        if list2:
            head.next = list2
        else:
            head.next = list1

        return temp.next