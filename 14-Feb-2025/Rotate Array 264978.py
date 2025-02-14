# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        to_be_replaced = nums[-k:]
        print(to_be_replaced)

        for j in range(len(nums)-k-1, -1, -1):
            nums[j+k] = nums[j]
        
        for i in range(len(to_be_replaced)):
            nums[i] = to_be_replaced[i]