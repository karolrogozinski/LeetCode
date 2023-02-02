from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], 
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        
        while list2:
            temp = list1
            while temp and temp.next and list2.val < temp.val:
                temp = temp.next
            if temp:
                temp.next = ListNode(list2.val, temp.next)
            list1 = temp
            list2 = list2.next

        return list1
    