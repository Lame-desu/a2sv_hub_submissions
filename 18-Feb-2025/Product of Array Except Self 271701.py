# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        result = 1
        for i in range(len(nums)):
            result*=nums[i]
            answer[i] = result
        result = 1
        for i in range(len(nums) -1, 0, -1):
            value = result * answer[i-1]
            answer[i] = value
            result *= nums[i]
        answer[0] = result
        return answer
