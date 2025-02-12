# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        count = 0
        num_count = {sorted_nums[0]: count}
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] != sorted_nums[i-1]:
                num_count[sorted_nums[i]] = i
        for i in range(len(nums)):
            nums[i] = num_count[nums[i]]
        return nums