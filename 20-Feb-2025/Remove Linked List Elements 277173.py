# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        traverse = dummy

        while traverse and traverse.next:
            if traverse.next.val == val:
                traverse.next = traverse.next.next
                continue
            traverse = traverse.next
        return dummy.next
            