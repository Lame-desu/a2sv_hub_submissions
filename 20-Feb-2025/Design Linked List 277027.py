# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        traverse = self.head
        i = 0
        while traverse and i < index:
            traverse = traverse.next
            i += 1
        if traverse:
            return traverse.val
        else:
            return -1    
            
    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val)
        new_head.next = self.head
        self.head = new_head

    def addAtTail(self, val: int) -> None:
        dummy = ListNode()
        dummy.next = self.head
        traverse = dummy
        while traverse.next:
            traverse = traverse.next
        new_tail = ListNode(val)
        traverse.next = new_tail
        self.head = dummy.next

    def addAtIndex(self, index: int, val: int) -> None:
        dummy = ListNode()
        dummy.next = self.head
        traverse = dummy

        for i in range(index):
            if not traverse.next:
                return
            traverse = traverse.next
        new_node = ListNode(val)
        new_node.next = traverse.next
        traverse.next = new_node
        self.head = dummy.next

    def deleteAtIndex(self, index: int) -> None:
        dummy = ListNode()
        dummy.next = self.head
        traverse = dummy
        i = 0
        while i < index and traverse:
            traverse = traverse.next
            i += 1
        if traverse and traverse.next:
            traverse.next = traverse.next.next

        self.head = dummy.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)