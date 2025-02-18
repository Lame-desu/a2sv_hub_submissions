# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_prefix = {0:1}
        sum = 0
        count = 0
        for i in range(len(nums)):
            sum+=nums[i]
            remainder =  sum % k
            count += remainder_prefix.get(remainder, 0)
            remainder_prefix[remainder] = remainder_prefix.get(remainder, 0) + 1
        return count