# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_count = 0
        sum = left = 0 
        for i in range(len(nums)):
            sum+=nums[i]

            while ((i-left+1) - sum) > k:
                sum-=nums[left]
                left += 1

            max_count = max(max_count, i-left+1)
        return max_count