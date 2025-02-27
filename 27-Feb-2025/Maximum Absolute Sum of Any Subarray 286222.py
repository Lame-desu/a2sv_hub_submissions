# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxSum = maxVal = minVal = sum = 0
        for num in nums:
            sum += num
            if num >= 0:
                maxSum = max(maxSum, abs(sum - minVal))
                maxVal = max(maxVal, sum)
            else:
                maxSum = max(maxSum, abs(sum - maxVal))
                minVal = min(minVal, sum)
        return maxSum