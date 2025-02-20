# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_head = ListNode()
        right_head = ListNode()
        left_traverse = left_head
        right_traverse = right_head

        while head:
            if head.val < x:
                left_traverse.next = head
                left_traverse, head = left_traverse.next, head.next
            else:
                right_traverse.next = head
                right_traverse, head = right_traverse.next, head.next
        right_traverse.next = None
        left_traverse.next = right_head.next
        return left_head.next
        