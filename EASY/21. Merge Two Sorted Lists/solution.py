from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], 
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode()
        tail = result

        while True:
            if not list1:
                tail.next = list2
                break
            if not list2:
                tail.next = list1
                break

            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
    
            tail = tail.next
    
        return result.next
    