# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
use left and right pointer
logic like fixed sliding window

"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # move right pointer until it has n steps of distance
        while n > 0:
            right = right.next 
            n -= 1
        
        #move left and right at the same time 1 step at a time until right is null
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next


