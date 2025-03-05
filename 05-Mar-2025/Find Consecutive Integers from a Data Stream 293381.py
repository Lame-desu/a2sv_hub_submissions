# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.datastream = []
        self.initial = 0

    def consec(self, num: int) -> bool:
        self.datastream.append(num)
        if num != self.value:
            self.initial = len(self.datastream)
        return len(self.datastream) - self.initial >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)