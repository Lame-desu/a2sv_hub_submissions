# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binarysearch(left, right):
            if left > right:
                return -1

            mid = (right + left) // 2

            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                return binarysearch(mid+1, right)

            if target < nums[mid]:
                return binarysearch(left, mid-1)
    
        return binarysearch(0, len(nums)-1)
            