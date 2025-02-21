# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail. prev = self.head
        self.keys = {}

    def _move_to_head(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self._add_to_head(node)

    def _add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_tail(self, node):
        self.tail.prev = node.prev
        node.prev.next = self.tail
        del self.keys[node.key]
        self.size -= 1

    def get(self, key: int) -> int:
        if key in self.keys:
            self._move_to_head(self.keys[key])
            return self.keys[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.keys[key].val = value
            self._move_to_head(self.keys[key])
        else:
            new_node = ListNode(key, value)
            self.keys[key] = new_node
            self._add_to_head(new_node)
            self.size += 1
            
            if self.size > self.capacity:
                self._remove_tail(self.tail.prev)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)