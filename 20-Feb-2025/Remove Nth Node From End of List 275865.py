# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        left_traverse = dummy
        right_traverse = head
        i, j = 0, 1
        
        while j - i < n:
            right_traverse = right_traverse.next
            j += 1
        
        while right_traverse.next:
            left_traverse = left_traverse.next
            right_traverse = right_traverse.next

        left_traverse.next = left_traverse.next.next
        return dummy.next
        
