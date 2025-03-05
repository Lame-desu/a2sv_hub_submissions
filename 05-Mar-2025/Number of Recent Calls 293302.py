# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.count = 0
        self.left = 0
        self.times = []

    def ping(self, t: int) -> int:
        self.times.append(t)
        self.count += 1
        while t - 3000 > self.times[self.left]:
            self.left += 1
            self.count -= 1
        return self.count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)