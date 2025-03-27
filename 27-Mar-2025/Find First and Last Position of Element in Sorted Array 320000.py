# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        #find left value
        # leftInd, rightInd = 0, 0
        # left, right = 0, len(nums)-1
        # while left <= right:
        #     if nums[left] == target:
        #         break

        #     mid = (right + left) // 2
        #     if nums[mid] < target:
        #         left = mid + 1
        #     elif nums[mid] >= target:
        #         right = mid - 1
        # leftInd = left
        # left, right = 0, len(nums) - 1
        # while left <= right:
        #     if nums[right] == target:
        #         break
        #     mid = (right + left + 1) // 2
        #     if nums[mid] > target:
        #         right = mid - 1

        #     elif nums[mid] <= target:
        #         left = mid + 1
        # rightInd = right
        # if  leftInd <= rightInd < len(nums):
        #     return [leftInd, rightInd]
        # else:
        #     return [-1, -1] 
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)-1    
        if left < len(nums) and nums[left] == target:
            return [left, right]
        else:
            return [-1, -1]    