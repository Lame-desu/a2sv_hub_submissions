# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        traverse = dummy
        remainder = 0
        while l1 or l2:
            sum  = 0
            sum += remainder
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            if sum > 9:
                value = sum % 10
                remainder = 1
            else:
                value = sum
                remainder = 0
            new_value = ListNode(value)
            traverse.next = new_value
            traverse =  traverse.next
        if remainder == 1:
            traverse.next = ListNode(remainder)
        return dummy.next