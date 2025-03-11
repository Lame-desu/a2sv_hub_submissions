# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def isDivisible(num):
            if num == 1:
                return True

            if 0 <= num < 1:
                return False

            if num % 4 != 0:
                return False

            return isDivisible(num / 4)
        return isDivisible(n)