# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        diff = [0] * (len(nums)+1)
        curr_sum = k = 0

        for i in range(len(nums)):
            curr_sum += diff[i]
            while curr_sum +  nums[i] > 0:
                if k >= len(queries):
                    return -1
                
                l, r, val = queries[k]
                diff[l] -= val
                diff[r+1] += val
                if l <= i and r >= i:
                    curr_sum -= val
                k += 1
        return k



