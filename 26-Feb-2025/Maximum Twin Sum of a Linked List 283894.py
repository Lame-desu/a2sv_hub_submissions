# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        last = None
        tempo = ""
        while fast and fast.next:
            tempo = slow
            slow, fast = slow.next, fast.next.next
            tempo.next = last
            last = tempo
        sum = 0
        while tempo and slow:
            sum = max(sum, tempo.val + slow.val)
            tempo, slow = tempo.next, slow.next
        return sum