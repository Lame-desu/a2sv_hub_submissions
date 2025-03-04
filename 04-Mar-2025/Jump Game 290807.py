# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        for index, step in enumerate(nums):
            max_jump = max(max_jump, index + step)
            if index + step == len(nums) - 1 or index == len(nums) - 1:
                return True
            if step == 0:
                if max_jump > index:
                    continue
                else:
                    return False
        return False