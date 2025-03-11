# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        prev_mins = [0] * len(nums)
        suffix_maxs = [len(nums)-1] * len(nums)
        _min = nums[0]
        for k, num in enumerate(nums):
            _min = min(_min, num)
            prev_mins[k] = _min
        stack = []
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[i] > stack[-1]:
                if stack[-1] > prev_mins[i]:
                    return True
                stack.pop()
            stack.append(nums[i])
        return False
            