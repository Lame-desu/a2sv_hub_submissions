# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sum = 0
        prefix_array = {0 : 1}
        single_length = 0
        count = 0
        for num in nums:
            if num % k == 0:
                single_length += 1
            sum += num
            remainder = sum % k
            if remainder in prefix_array:
                count += prefix_array[remainder]
            if count - single_length > 0:
                return True
            prefix_array[remainder] = 1 if remainder not in prefix_array else prefix_array[remainder] + 1
        return False
            