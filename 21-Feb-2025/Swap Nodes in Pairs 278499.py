# Problem: Swap Nodes in Pairs - https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        traverse = dummy
        while traverse.next and traverse.next.next:
            to_left = traverse.next.next
            to_right = traverse.next

            to_right.next = to_left.next
            to_left.next = to_right
            traverse.next = to_left

            traverse = traverse.next.next
        return dummy.next
            
            