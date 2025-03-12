# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if n == 0:
                return 1
            if n <= 1:
                return x
            if n % 2 == 1:
                half = power(x, n//2)
                return half * half * x
            else:
                half = power(x, n//2)
                return half * half
        
        answer = 1 / power(x, abs(n)) if n < 0 else power(x, n)
        return answer