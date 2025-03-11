# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(num):
            if num < 5:
                return 0
            return num // 5 + factorial(num // 5)
        return factorial(n)