# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        traverse = head
        index_value = {}
        index = 0 
        while traverse:
            index_value[index] = traverse.val
            traverse, index = traverse.next, index + 1
        i, n,  max_index = 0, index-1, index // 2
        traverse = head
        sum = 0
        while i < max_index:
            sum = max(sum, traverse.val + index_value[n - i])
            traverse, i = traverse.next, i + 1
        return sum