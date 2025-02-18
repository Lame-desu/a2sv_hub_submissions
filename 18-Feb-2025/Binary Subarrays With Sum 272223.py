# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = {0 : 1}
        right = 0
        count = 0
        for i in range(len(nums)):
            right += nums[i]
            count += prefix_sum.get(right - goal, 0)
            prefix_sum[right] = prefix_sum.get(right, 0) + 1
        return count
