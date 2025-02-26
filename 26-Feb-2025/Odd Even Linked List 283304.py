# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        odd = head
        even = head.next
        while even and even.next:
            tempo = even.next.next
            even.next.next = odd.next
            odd.next = even.next
            even.next = tempo
            odd = odd.next
            even = even.next
        return head
