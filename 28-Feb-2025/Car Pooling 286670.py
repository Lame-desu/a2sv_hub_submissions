# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix_sum = [0] * 1001
        for passangers, initial, final in trips:
            if passangers > capacity:
                return False
            prefix_sum[initial] += passangers
            prefix_sum[final] -= passangers
        
        for i in range(1, 1001):
            prefix_sum[i] += prefix_sum[i - 1]
            if prefix_sum[i] > capacity:
                return False
        return True
