# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reverse = None
        fast = slow = head
        count = 0
        while fast and fast.next:
            tempo = slow
            fast = fast.next.next
            slow = slow.next
            tempo.next = reverse
            reverse = tempo
            count += 2
        if fast:
            count += 1

        start = slow if count % 2 == 0 else slow.next

        if count == 1:
            return True
    
        while start:
            if reverse.val != start.val:
                return False
            reverse = reverse.next
            start = start.next
        return True
