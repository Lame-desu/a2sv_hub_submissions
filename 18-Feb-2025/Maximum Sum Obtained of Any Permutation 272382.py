# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix_array = [0] * len(nums)

        for interval in requests:
            prefix_array[interval[0]] += 1
            if interval[1] < len(nums) - 1:
                prefix_array[interval[1] + 1] -= 1
        
        sum = 0
        for i in range(len(prefix_array)):
            sum += prefix_array[i]
            prefix_array[i] = sum

        prefix_array.sort()
        nums.sort()

        max_sum = 0
        for i in range(len(nums)):
            max_sum += prefix_array[i] * nums[i]
        
        return max_sum % (10 ** 9 + 7)