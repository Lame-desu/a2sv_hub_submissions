# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def validate_sum(value):
            curr_sum = 0
            count = 1
            i = 0
            while i < len(nums):
                if curr_sum + nums[i] > value:
                    count += 1
                    curr_sum = 0
                else:
                    curr_sum += nums[i]
                    i += 1

                if count > k:
                    return False
            return True

        
        min_val, max_val = 0, sum(nums)
        while min_val <= max_val:
            mid = (min_val + max_val) // 2

            if validate_sum(mid):
                max_val = mid - 1
            else:
                min_val = mid + 1

        return min_val    
            

                    