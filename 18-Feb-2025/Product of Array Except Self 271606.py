# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward_product = [1] * (len(nums) + 1)
        backward_product = [1] * (len(nums) + 1)
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            forward_product[i + 1] = product
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            product *= nums[i]
            backward_product[i] = product

        answer = []
        for i in range(len(nums)):
            value = forward_product[i] * backward_product[i+1]
            answer.append(value)
        return answer