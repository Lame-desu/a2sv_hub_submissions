# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0 : 1}
        total_sum = count = 0
        for i in range(len(nums)):
            total_sum+=nums[i]
            count += prefix_sum.get(total_sum - k, 0)
            prefix_sum[total_sum] =  prefix_sum.get(total_sum, 0) + 1
        return count
