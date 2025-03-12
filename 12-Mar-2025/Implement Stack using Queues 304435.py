# Problem: Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self.queue = deque()
        self.left = 0
        self.size = 0

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.size += 1

    def pop(self) -> int:
        self.top()
        self.size -= 1
        self.left -= 1
        return self.queue.popleft()

    def top(self) -> int:
        while self.left < len(self.queue):
            self.queue.appendleft(self.queue[self.left])
            self.left += 2
        return self.queue[0]

    def empty(self) -> bool:
        return self.size == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()