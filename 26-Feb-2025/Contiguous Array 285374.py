# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxLength = 0
        prefix_sum = {0: -1}
        sum = 0
        for i, num in enumerate(nums):
            sum += 1 if num == 1 else -1
            if sum in prefix_sum:
                maxLength = max(maxLength, i-prefix_sum[sum])
            else:
                prefix_sum[sum] = i
        return maxLength