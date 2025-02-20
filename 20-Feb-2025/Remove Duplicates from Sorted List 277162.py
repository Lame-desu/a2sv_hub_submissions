# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        traverse = head
        while traverse and traverse.next:
            if traverse.val == traverse.next.val:
                traverse.next = traverse.next.next
                continue
            traverse = traverse.next
        return head