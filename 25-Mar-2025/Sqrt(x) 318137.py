# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        int_value = 0
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                int_val = mid
                left = mid + 1
            else:
                right = mid - 1
        return int_val
