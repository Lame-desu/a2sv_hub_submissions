# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        valid_count = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            if minK <= nums[i] <= maxK:
                count += 1
            else:
                count = 0
            valid_count[i] = count
        
        left = 0
        minimums = 0
        maximums = 0
        arrays = 0
        for right in range(len(nums)):
            if nums[right] > maxK or nums[right] < minK:
                minimums = maximums = 0
                left = right + 1

            if nums[right] == minK:
                minimums += 1
            
            if nums[right] == maxK:
                maximums += 1

            while minimums > 0 and maximums > 0:
                arrays += valid_count[right]
                if nums[left] == minK:
                    minimums -= 1
                if nums[left] == maxK:
                    maximums -= 1
                left += 1
        return arrays