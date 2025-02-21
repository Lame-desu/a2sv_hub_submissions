# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        count_element = head
        while count_element:
            count += 1
            count_element = count_element.next
        to_swap = count // k
        swaps = 0
        dummy = ListNode()
        dummy.next = head
        initial = dummy
        traverse = initial.next
        while swaps < to_swap:
            count = 0
            while count < k:
                if count == 0:
                    count += 1
                    continue
                tempo = traverse.next
                traverse.next = traverse.next.next
                tempo.next = initial.next
                initial.next = tempo
                # print(initial, traverse)
                count += 1
            initial = traverse
            traverse = traverse.next
            # print(initial)
            swaps += 1
        return dummy.next
        