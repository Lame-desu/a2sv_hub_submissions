# Problem: Design Browser History - https://leetcode.com/problems/design-browser-history/description/

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)

    def visit(self, url: str) -> None:
        new_visit = ListNode(url)
        new_visit.prev = self.head
        self.head.next = new_visit
        self.head = self.head.next
        

    def back(self, steps: int) -> str:
        step = 0
        while self.head.prev and step < steps:
            step += 1
            self.head = self.head.prev
        return self.head.val

    def forward(self, steps: int) -> str:
        step = 0
        while self.head.next and step < steps:
            step += 1
            self.head = self.head.next
        return self.head.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)