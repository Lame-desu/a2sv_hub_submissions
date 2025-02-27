# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxVal = minVal = sum = 0
        for num in nums:
            sum += num
            maxVal = max(maxVal, sum)
            minVal = min(minVal, sum)
        return maxVal - minVal