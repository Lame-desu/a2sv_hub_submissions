# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        nums_set = set()
        count = 0
        for num in nums:
            if num in nums_set:
                count += 1
                nums_set.remove(num)
            else:
                nums_set.add(num)
        return [count, len(nums) - 2 * count]