# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        min_point = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            max_sum = max(max_sum, sum - min_point)
            min_point = min(min_point, sum)
        return max_sum
            



        
        