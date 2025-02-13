# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[0:k])
        max_average = max_sum / k
        initial = 0
        last = k
        while last < len(nums):
            max_sum = max_sum - nums[initial] + nums[last]
            initial, last = initial+1, last+1
            current_average = max_sum / k
            max_average = max_average if max_average >= current_average else current_average
        return max_average
            