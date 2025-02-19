# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = reverse = ListNode() 
        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1
                dummy, list1 = dummy.next, list1.next
            else:
                dummy.next = list2
                dummy, list2 = dummy.next, list2.next
        if list1 or list2:
            dummy.next = list1 if list1 else list2
        return reverse.next